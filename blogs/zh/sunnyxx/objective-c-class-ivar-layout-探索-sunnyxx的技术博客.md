---
title: Objective-C Class Ivar Layout 探索 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/09/13/class-ivar-layout/'
original_language: zh
published: 2015-09-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9b890f8342cc114d'
translated: n/a
---

> 原文：[Objective-C Class Ivar Layout 探索 · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/09/13/class-ivar-layout/)　·　sunnyxx (孙源)

# Objective-C Class Ivar Layout 探索

2015年9月13日

这次探索源于一个朋友问的问题，当我们定义一个类的实例变量的时候，可以指定其修饰符：

```objc
@interface Sark : NSObject {
    __strong id _gayFriend; // 无修饰符的对象默认会加 __strong
    __weak id _girlFriend;
    __unsafe_unretained id _company;
}
@end
```

这使得 ivar (instance variable) 可以像属性一样在 ARC 下进行正确的引用计数管理。

那么问题来了，假如这个类是动态生成的：

```objc
Class class = objc_allocateClassPair(NSObject.class, "Sark", 0);
class_addIvar(class, "_gayFriend", sizeof(id), log2(sizeof(id)), @encode(id));
class_addIvar(class, "_girlFriend", sizeof(id), log2(sizeof(id)), @encode(id));
class_addIvar(class, "_company", sizeof(id), log2(sizeof(id)), @encode(id));
objc_registerClassPair(class);
```

该如何像上面一样来添加 ivar 的属性修饰符呢？

刨根问底了一下，发现 ivar 的修饰信息存放在了 Class 的 Ivar Layout 中：

```objc
struct class_ro_t {
    uint32_t flags;
    uint32_t instanceStart;
    uint32_t instanceSize;
#ifdef __LP64__
    uint32_t reserved;
#endif
    const uint8_t * ivarLayout; // <- 记录了哪些是 strong 的 ivar

    const char * name;
    const method_list_t * baseMethods;
    const protocol_list_t * baseProtocols;
    const ivar_list_t * ivars;

    const uint8_t * weakIvarLayout; // <- 记录了哪些是 weak 的 ivar
    const property_list_t *baseProperties;
};
```

ivarLayout 和 weakIvarLayout 分别记录了哪些 ivar 是 strong 或是 weak，都未记录的就是基本类型和 __unsafe_unretained 的对象类型。

这两个值可以通过 runtime 提供的几个 API 来访问：

```objc
const uint8_t *class_getIvarLayout(Class cls)
const uint8_t *class_getWeakIvarLayout(Class cls)
void class_setIvarLayout(Class cls, const uint8_t *layout)
void class_setWeakIvarLayout(Class cls, const uint8_t *layout)
```

但我们几乎没可能用到这几个 API，IvarLayout 的值由 runtime 确定，没必要关心它的存在，但为了解决上述问题，我们试着破解了 IvarLayout 的编码方式。

举个例子说明，若类定义为：

```objc
@interface Foo : NSObject {
    __strong id ivar0;
    __weak id ivar1;
    __weak id ivar2;
}
@end
```

则储存 strong ivar 的 ivarLayout 的值为 **0x012000**

储存 weak ivar 的 weakIvarLayout 的值为 **0x1200**

一个 uint8_t 在 16 进制下是两位，所以编码的值每两位一对儿，以上面的 ivarLayout 为例：

1. 前两位 **01** 表示有 0 个非 strong 对象和 1 个 strong 对象
2. 之后两位 **20** 表示有 2 个非 strong 对象和 0 个 strong 对象
3. 最后两位 **00** 为结束符，就像 cstring 的 **\\0** 一样

同理，上面的 weakIvarLayout：

1. 前两位 **12** 表示有 1 个非 weak 对象和接下来连续 2 个 weak 对象
2. **00** 结束符

这样，用两个 layout 编码值就可以排查出一个 ivar 是属于 strong 还是 weak 的，若都没有找到，就说明这个对象是 unsafe_unretained.

做个练习，若类定义为：

```objc
@interface Bar : NSObject {
    __weak id ivar0;
    __strong id ivar1;
    __unsafe_unretained id ivar2;
    __weak id ivar3;
    __strong id ivar4;
}
@end
```

则储存 strong ivar 的 ivarLayout 的值为 **0x012100**

储存 weak ivar 的 weakIvarLayout 的值为 **0x01211000**

于是乎将 class 的创建代码增加了两个 ivarLayout 值的设置：

```objc
Class class = objc_allocateClassPair(NSObject.class, "Sark", 0);
class_addIvar(class, "_gayFriend", sizeof(id), log2(sizeof(id)), @encode(id));
class_addIvar(class, "_girlFriend", sizeof(id), log2(sizeof(id)), @encode(id));
class_addIvar(class, "_company", sizeof(id), log2(sizeof(id)), @encode(id));
class_setIvarLayout(class, (const uint8_t *)"\x01\x12"); // <--- new
class_setWeakIvarLayout(class, (const uint8_t *)"\x11\x10"); // <--- new
objc_registerClassPair(class);
```

本以为解决了这个问题，但是 runtime 继续打脸，strong 和 weak 的内存管理并没有生效，继续研究发现， class 的 flags 中有一个标记位记录这个类是否 ARC，正常编译的类，且标识了 **-fobjc-arc** flag 时，这个标记位为 1，而动态创建的类并没有设置它。所以只能继续黑魔法，运行时把这个标记位设置上，探索过程不赘述了，实现如下：

```objc
static void fixup_class_arc(Class class) {
    struct {
        Class isa;
        Class superclass;
        struct {
            void *_buckets;
#if __LP64__
            uint32_t _mask;
            uint32_t _occupied;
#else
            uint16_t _mask;
            uint16_t _occupied;
#endif
        } cache;
        uintptr_t bits;
    } *objcClass = (__bridge typeof(objcClass))class;
#if !__LP64__
#define FAST_DATA_MASK 0xfffffffcUL
#else
#define FAST_DATA_MASK 0x00007ffffffffff8UL
#endif
    struct {
        uint32_t flags;
        uint32_t version;
        struct {
            uint32_t flags;
        } *ro;
    } *objcRWClass = (typeof(objcRWClass))(objcClass->bits & FAST_DATA_MASK);
#define RO_IS_ARR 1<<7        objcRWClass->ro->flags |= RO_IS_ARR;
    objcRWClass->
}
```

把这个 fixup 放在 `objc_registerClassPair(class);` 之后，这个动态的类终于可以像静态编译的类一样操作 ivar 了，可以测试一下：

```objc
id sark = [class new];
Ivar weakIvar = class_getInstanceVariable(class, "_girlFriend");
Ivar strongIvar = class_getInstanceVariable(class, "_gayFriend");
{
    id girl = [NSObject new];
    id boy = [NSObject new];
    object_setIvar(sark, weakIvar, girl);
    object_setIvar(sark, strongIvar, boy);
} // ARC 在这里会释放大括号内的 girl，boy
// 输出：weakIvar 为 nil，strongIvar 有值
NSLog(@"%@, %@", object_getIvar(sark, weakIvar), object_getIvar(sark, strongIvar));
```

Done.
