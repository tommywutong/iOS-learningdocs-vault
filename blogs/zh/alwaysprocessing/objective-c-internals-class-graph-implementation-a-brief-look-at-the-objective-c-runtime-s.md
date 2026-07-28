---
title: 'Objective-C 内部实现：类图实现'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl'
original_language: en
published: 2023-01-10
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eda6c7fbf8e91717'
translated: true
---

> 原文：[Objective-C 内部实现：类图实现——浅析 Objective-C 运行时源代码，聚焦对象和类类型的定义，展示继承如何实现](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：类图实现

![两只黄色拉布拉多犬在电脑前工作，桌面上散落着设计图纸。](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c8a0ec22-9d84-4e34-3f9d-bba189527d00/public)

浅析 Objective-C 运行时源代码，聚焦对象和类类型的定义，展示继承如何实现、根类的特殊情况，以及元类查找相关的特性。

上一篇文章探讨了 [Objective-C 类架构](https://alwaysprocessing.blog/2023/01/02/objc-class-arch)，并以[示意图](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#architecture-diagram)展示了类层次结构的对象图。在此，我们将通过检视类对象图的实现（类、超类与元类）来进一步深化这些概念。

让我们从一些关键类型的公开定义开始。在 Objective-C 中，`Class` 类型代表任意类类型，`id` 类型代表任意类的实例。Objective-C 运行时头文件 [`objc.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc.h#L37-L46) 定义了这些类型：

```
/// 一个不透明类型，代表 Objective-C 类。
typedef struct objc_class *Class;

/// 代表一个类的实例。
struct objc_object {
    Class _Nonnull isa  OBJC_ISA_AVAILABILITY;
};

/// 指向类实例的指针。
typedef struct objc_object *id;
```

如上一篇文章所述，Objective-C [类也是对象](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#method-dispatch)，但这种关系并未在公开类型定义中体现。不过，如果我们查看内部类型定义，就能发现这种关系。

首先，[objc-private.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-private.h#L113-L246) 包含了实际的 `objc_object` 定义。虽然内部定义包含许多非虚的 C++ 成员函数，但其唯一的成员变量 `isa_storage` 对应了（已废弃的）`isa` 实例变量（我不知道为什么内部类型是 `char` 数组，但如果要猜测，可能是为了防止因该字段的各种重载而被意外直接使用。我在[这篇文章](https://alwaysprocessing.blog/2023/01/19/objc-class-isa)中讨论了更多关于 `isa` 字段的细节）。

```
struct objc_object {
    char isa_storage[sizeof(isa_t)];
};
```

接下来，[objc-runtime-new.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.h#L2142-L2663) 包含了 `objc_class` 数据结构定义。它有几个自己的成员变量，并且和 `objc_object` 一样，包含许多非虚的 C++ 成员函数。

```
struct objc_class : objc_object {
    // Class ISA;
    Class superclass;
    cache_t cache;             // 原 cache 指针和 vtable
    class_data_bits_t bits;    // class_rw_t * 加上自定义 rr/alloc 标志
};
```

这里我们看到 `objc_class` 派生自 `objc_object`，因此继承了 `isa` 字段。所以，类对象与其他任何对象类型的实现方式完全相同。接下来是 `superclass` 字段，它指向父类对象（如果存在的话）。（`cache` 和 `bits` 不属于类图的构建部分，我们将在未来探讨它们。）

而这就是构建 Objective-C 类图所需的一切：两个数据结构（`objc_object` 和 `objc_class`）和两个字段（`isa` 和 `superclass`）！

## objc_class 成员函数

接下来，让我们检查一些 [`objc_class` 成员函数](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.h#L2540-L2570)，以了解架构图中边的实现。

### 根类 (Root Classes)

```
bool isRootClass() {
    return getSuperclass() == nil;
}
```

如果某个类没有超类，那么它就是根类。然而，这在实际中并不常见，因为几乎所有 Objective-C 对象都派生自 [`NSObject`](https://developer.apple.com/documentation/objectivec/nsobject?language=objc)（或者在极少数情况下派生自 [`NSProxy`](https://developer.apple.com/documentation/foundation/nsproxy?language=objc)）。因此请注意，根元类_不是_根类。

### 根元类 (Root Metaclasses)

```
bool isRootMetaclass() {
    return ISA() == (Class)this;
}
```

根元类的 `isa` 指针指向自身，运行时通过此方式识别根元类。据我所知，这是类图中唯一的循环。

### 元类标识

```
bool isMetaClass() const {
    return cache.getBit(FAST_CACHE_META);
}

// 类似于 isMetaClass，但在未实现类上同样有效
bool isMetaClassMaybeUnrealized() {
    if (isStubClass())
        return false;
    return bits.flags() & RW_META;
}
```

编译器设置的一个位标志用于标识元类实例，这是区分元类实例与类实例的主要特征。

未实现类（包括存根类 (stub classes)）在 [Objective-C 内部实现：未实现类（以及 Toll-Free Bridging）](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes)文章中有更详细的描述。

### 元类获取

```
// 当 this 是元类时，不等于 this->ISA()
Class getMeta() {
    if (isMetaClassMaybeUnrealized()) return (Class)this;
    else return this->ISA();
}
```

当从某个类实例获取元类时，需要检查该实例是否已经是元类。如果它是元类，则返回自身。否则，类实例通过其 `isa` 指针返回元类。

## 编译器输出

`objc_class` 数据结构是 Objective-C ABI 的一部分，这意味着其大小和字段布局的细节对第三方程序是已知的，这些程序会将此信息编码到它们的可执行二进制文件中。我们可以通过检查以下简单类定义的编译器输出来观察这一点。

```
#import <Foundation/Foundation.h>

@interface MyObject: NSObject
@end

@implementation MyObject
@end
```

通过运行 `clang -S MyObject.m` 为上述 `MyObject.m` 文件生成汇编代码，将会产生一个包含以下代码片段（以及更多内容）的汇编文件。

```
.section    __DATA,__objc_data
_OBJC_CLASS_$_MyObject:
    .quad   _OBJC_METACLASS_$_MyObject
    .quad   _OBJC_CLASS_$_NSObject
    .quad   __objc_empty_cache
    .quad   0
    .quad   __OBJC_CLASS_RO_$_MyObject
_OBJC_METACLASS_$_MyObject:
    .quad   _OBJC_METACLASS_$_NSObject
    .quad   _OBJC_METACLASS_$_NSObject
    .quad   __objc_empty_cache
    .quad   0
    .quad   __OBJC_METACLASS_RO_$_MyObject
```

在这里，我们看到编译器生成的代码与我们上一篇文章中从架构图得出的观察结果一致：

- `MyClass` 类对象具有：
    - 一个指向 `MyClass` 元类的 `isa` 变量。
    - 一个指向 `NSObject` 类对象的 `super` 变量。
- `MyClass` 元类具有：
    - 一个指向 `NSObject`（根对象）元类的 `isa` 变量。
    - 一个指向 `NSObject` 元类的 `super` 变量。

（如上所述，`cache` 和 `bits` 字段将是未来文章的主题。）
