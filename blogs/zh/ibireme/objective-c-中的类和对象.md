---
title: Objective-C 中的类和对象
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2013/11/25/objc-object/'
original_language: zh
published: 2013-11-25
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2068371a16e2d0b3'
translated: n/a
---

> 原文：[Objective-C 中的类和对象](https://blog.ibireme.com/2013/11/25/objc-object/)　·　ibireme (郭曜源)

Objective-C的runtime是开源的，源码可以在苹果官网下载到：[objc4](http://www.opensource.apple.com/tarballs/objc4/)。

在objc4-532.2以后，苹果把NSObject的实现也挪进来了。想要了解NSObject底层实现终于不用去抠[GNUstep](http://www.gnustep.org/)了～

好了，下面正文：

---

### 1.id和Class的定义

runtime里面，声明了id和Class的类型，简化一下如下：

```
struct objc_class {
    struct objc_class *isa;
};
struct objc_object {
    struct objc_class *isa;
};

typedef struct objc_class *Class; //类  (class object)
typedef struct objc_object *id;   //对象 (instance of class)
```

在objc中，id代表了一个对象。根据上面的声明，凡是首地址是*isa的struct指针，都可以被认为是objc中的对象。运行时可以通过isa指针，查找到该对象是属于什么类(Class)。

### 2.运行时的实现方式

根据上面的说法，类对象(Class)同样也算是对象，那它的isa又是指向了什么呢？为了了解这些东西是怎么回事，这里写一个简单的类NyanCat，并且用C重写一遍，看看编译器在底层到底是如何实现的。

```
@interface NyanCat : NSObject {
    int age;
    NSString *name;
}
- (void)nyan;
+ (void)nyan;
@end

@implementation NyanCat
- (void)nyan1 {
    printf("instance nyan~");
}
+ (void)nyan2 {
    printf("class nyan~");
}
@end
```

上面是一个简单的类，有两个instance variable，有一个类方法、一个实例方法。

```
clang -rewrite-objc NyanCat.m
```

在终端执行上面这一条语句，让clang将该类重写为cpp代码，我们就能查看到大概底层的实现机制了(实际编译的文件和这个会有些出入，不同目标架构和不同版本clang也会有不同..权且当参考了)。

rewrite后的代码基本是纯C的，稍微整理一下，可以提取出下面这些信息：

```
//Class的实际结构
struct _class_t {
	struct _class_t *isa;        //isa指针
	struct _class_t *superclass; //父类
	void *cache;
	void *vtable;
	struct _class_ro_t *ro;     //Class包含的信息
};

//Class包含的信息
struct _class_ro_t {
	unsigned int flags;
	unsigned int instanceStart;
	unsigned int instanceSize;
	unsigned int reserved;
	const unsigned char *ivarLayout;
	const char *name;                                 //类名
	const struct _method_list_t *baseMethods;         //方法列表
	const struct _objc_protocol_list *baseProtocols;  //协议列表
	const struct _ivar_list_t *ivars;                 //ivar列表
	const unsigned char *weakIvarLayout;
	const struct _prop_list_t *properties;            //属性列表
};

 //NyanCat(meta-class)
struct _class_t OBJC_METACLASS_$_NyanCat  = {
	.isa        = &OBJC_METACLASS_$_NSObject,
	.superclass = &OBJC_METACLASS_$_NSObject,
	.cache      = (void *)&_objc_empty_cache,
	.vtable     = (void *)&_objc_empty_vtable,
	.ro         = &_OBJC_METACLASS_RO_$_NyanCat, //包含了类方法等
};

//NyanCat(Class)
struct _class_t OBJC_CLASS_$_NyanCat = {
	.isa        = &OBJC_METACLASS_$_NyanCat,   //此处isa指向meta-class
	.superclass = &OBJC_CLASS_$_NSObject,
	.superclass = (void *)&_objc_empty_cache,
	.vtable     = (void *)&_objc_empty_vtable,
	.ro         = &_OBJC_CLASS_RO_$_NyanCat,   //包含了实例方法 ivar信息等
};

typedef struct objc_object NyanCat;   //定义NyanCat类型
//更详细的不贴代码了..
```

所有NyanCat的实例的isa都指向了NyanCat(Class)。

NyanCat(Class)是一个全局变量，其中记录了类名、成员变量信息、property信息、protocol信息和实例方法列表等。

NyanCat(Class)的isa指向了全局变量NyanCat(meta-class)，meta-class里只记录了类名、类方法列表等。

画出图来就是这样：

[![objc-meta](https://blog.ibireme.com/wp-content/uploads/2013/11/objc-meta.png)](https://blog.ibireme.com/wp-content/uploads/2013/11/objc-meta.png)  
 举例来说一下：

```
NyanCat *cat = [[NyanCat alloc] init];
[cat nyan1];
```

向cat (instance) 发送消息nyan1时，运行时会通过isa指针查找到NyanCat(Class)，这里保存着本类中定义的实例方法的指针。

```
[NyanCat nyan2];
```

向NyanCat(Class)发送消息nyan2时，运行时会通过isa查找到NyanCat(meta-class)，这里保存着本类中定义的类方法的指针。

运行时如何利用Chass和meta-class来实现动态消息的，以后在记吧～

### 3.类的继承

在_class_t里面，第二个成员是superclass，很明显这个指针指向了它的父类。运行时可以通过isa和superclass获取一个类在继承树上的完整信息。

为了说明方便，这里把上面的例子稍微改一下：NyanCat : Cat : NSObject 这样一个继承树，画出图来就是这样子的：

[![objctree](https://blog.ibireme.com/wp-content/uploads/2013/11/objctree.png)](https://blog.ibireme.com/wp-content/uploads/2013/11/objctree.png)

如上面图中，跟随黑线，可以看到isa的指向。运行时，每个对象的isa都不为空，这样只要是一个id类型的对象，runtime都可以通过访问首地址偏移(isa)来获取该对象的信息了。

上图中跟随绿线，可以看到superclass的指向。当运行时在搜寻方法、ivar信息时，如果没有找到信息，则会沿superclass的线查找上去，最终NSObject(根类)的superclass是nil。

如果自己定义了一个根类(比如NSProxy)，则这个根类会替换图中NSObject的位置。

为了验证上面的说法，可以敲一下代码看看：

```
#import "NyanCat.h"
#import <objc/runtime.h>
#import <objc/objc.h>

void test() {
    NyanCat *cat = [[NyanCat alloc] init];

    Class cls = object_getClass(cat); //NyanCat(Class)
    class_getName(cls);               //"NyanCat"
    class_isMetaClass(cls);           //NO

    Class meta = object_getClass(cls); //NyanCat(meta-class)
    class_getName(meta);               //"NyanCat"
    class_isMetaClass(cls);            //YES

    Class meta_meta = object_getClass(meta); //NSObject(meta-class)
    class_getName(meta_meta);                //"NSObject"
    class_isMetaClass(meta_meta);            //YES
}
```

最后吐嘈一下：平时开发时，meta-class基本是用不着接触的，superclass指针无法访问，isa指针可能稍后也会隐藏起来(苹果的动作真多)。。所以上面说得这些，了解一下就好～～
