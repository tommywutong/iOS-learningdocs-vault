---
title: 'Objective-C 内部实现：未实现类与免费桥接'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes'
original_language: en
published: 2023-02-16
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a35b9c1ea90ab378'
translated: true
---

> 原文：[Objective-C Internals: Unrealized Classes (and Toll-Free Bridging) Objective-C unrealized classes may refer to future classes or class stubs. Future classes (a private runtime feature) facilitate toll](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：未实现类与免费桥接

![两只拉布拉多犬坐在桥下一台电脑前。大概是在躲避收费。](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c34a57c8-254d-4af6-e20a-c518c2f76f00/public)

Objective-C 未实现类可能指未来类（future class）或存根类（stub class）。未来类（一种私有运行时特性）促进了与 CoreFoundation 的免费桥接（Toll-Free Bridging）。同时，Swift 编译器会发出存根类，以支持稳定的 Swift ABI 与 Objective-C 之间的互操作性。

此前一篇探讨 Objective-C 类实现的文章忽略了[^1](#_footnotedef_1)用于[识别元类](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl#metaclass-identity)的函数中的一个有趣细节：_未实现类_的概念。

```
// 类似 isMetaClass，但也适用于未实现的类
bool isMetaClassMaybeUnrealized() { /* ... */ }
```

_未实现类_是一种部分初始化的元类，仅知道类名。未实现元类有两种类型：未来类和存根类。

## 未来类

Mac OS X 10.5 中的 Objective-C 运行时引入了未来类，作为私有运行时特性，用于清理[免费桥接](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html)的实现。令人惊讶的是，这实际上在 [`objc_getFutureClass`](https://developer.apple.com/documentation/objectivec/1441638-objc_getfutureclass) 中有文档说明：

> 由 CoreFoundation 的免费桥接使用。不要自行调用此函数。

### 免费桥接

首先，我们简要看一下免费桥接的实现。Mac OS X Developer Preview 1 [引入了 CoreFoundation 框架和“免费桥接”](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html)。简而言之，免费桥接允许开发者自由地在桥接的 CoreFoundation 和 Foundation 类型之间进行转换（例如，将 `CFArrayRef` 转换为 `NSArray *` 或反向转换），以将一种类型当作另一种类型传递，而不会产生任何运行时开销。此外，完全支持用户定义的免费桥接 Foundation 类的子类。

对免费桥接的全面探讨超出了本文的范围，但你可以[在此处阅读更多内容](https://ridiculousfish.com/blog/posts/bridge.html)。我们只需要强调两个关键的实现细节，以便理解其对 Objective-C 运行时的使用。

首先，所有 CoreFoundation 对象都有一个与 Objective-C 兼容的 `isa` 字段作为其第一个成员。来自 [CFRuntime.h](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFRuntime.h#L207)：

```
typedef struct __CFRuntimeBase {
    void *_isa;
    // ...
} CFRuntimeBase;
```

其次，每个具有 Foundation 等价物的 CoreFoundation 函数（例如，[`CFArrayGetCount()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Collections.subproj/CFArray.c#L603-L607) 和 `-[NSArray count]`）会在 `isa` 与桥接的 CoreFoundation 类型的 `isa` 不匹配时调用 Objective-C 实现，这就为用户定义的 Foundation 子类提供了桥接支持。（[CFInternal.h](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFInternal.h#L470-L472) 定义了 Objective-C 分派宏。）

```
CFIndex CFArrayGetCount(CFArrayRef array) {
    CF_OBJC_FUNCDISPATCH0(__kCFArrayTypeID, CFIndex, array, "count");
    __CFGenericValidateType(array, __kCFArrayTypeID);
    return __CFArrayGetCount(array);
}

#define CF_OBJC_FUNCDISPATCH0(typeID, rettype, obj, sel) \
    if (__builtin_expect(CF_IS_OBJC(typeID, obj), 0)) \
    {rettype (*func)(const void *, SEL) = (void *)__CFSendObjCMsg; \
    static SEL s = NULL; if (!s) s = sel_registerName(sel); \
    return func((const void *)obj, s);}

CF_INLINE int CF_IS_OBJC(CFTypeID typeID, const void *obj) {
    return (((CFRuntimeBase *)obj)->_isa != __CFISAForTypeID(typeID) && ((CFRuntimeBase *)obj)->_isa > (void *)0xFFF);
}
```

CoreFoundation 如何获取与 Foundation 共享的 `isa` 指针，是本小节剩余部分的主题。

### Mac OS X 10.0 - Mac OS X 10.4 "Tiger"

免费桥接的原始实现相当复杂。Foundation 定义了公开的 Objective-C 类（例如 `NSObject`、`NSArray`、`NSMutableArray`）、[类簇（class cluster）](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/ClassClusters/ClassClusters.html)的私有实现（例如 `NSCFArray`）以及一个桥接占位符（例如 `NSCFArray__`），它是桥接实现的一个简单子类。

当加载 Foundation 时，它会调用 CoreFoundation 的 [`__CFSetupFoundationBridging()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/ForFoundationOnly.h#L52-L53) 函数，该函数执行两项操作：

1. 调用 [`__CFInitialize()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFRuntime.c#L738-L739)。初始化的第一步之一是为 `__CFRuntimeObjCClassTable` 中的每个条目分配内存，该表将 `CFTypeID` 映射到其桥接的 Objective-C `Class`。在此分配的 `objc_class` （[回顾](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl#preamble)一下，`Class` 是 `objc_class *` 的 `typedef`）将在下一步中成为在 CoreFoundation 和 Foundation 之间共享的免费桥接类实例。指针值在初始化过程的早期就被预留，以便在后续初始化步骤中分配的 CoreFoundation 对象能够使用，从而保证这些对象能够正确桥接。
2. 对于每种桥接类型，查找占位符子类，如果存在，则调用 [`_CFRuntimeSetupBridging()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFRuntime.c#L204-L209)。

    1. `_CFRuntimeSetupBridging()` 将占位符的 `objc_class` 结构体按位复制到上一步分配的内存中。
    2. CoreFoundation 然后将占位符类的按位副本当作桥接实现。

```
void __CFSetupFoundationBridging(void *, void *, void *, void *) {
    // ...
    __CFInitialize();
    // ...
    Class aClass = objc_lookUpClass("NSCFArray__");
    if (arrayClass != Nil) {
        _CFRuntimeSetupBridging(CFArrayGetTypeID(), aClass->super_class, aClass);
    }
    aClass = objc_lookUpClass("NSCFDictionary__");
    if (aClass != Nil) {
        _CFRuntimeSetupBridging(CFDictionaryGetTypeID(), aClass->super_class, aClass);
    }
    // ...
}

void __CFInitialize(void) {
    // ...
    __CFRuntimeObjCClassTable[CFDictionaryGetTypeID()] = calloc(sizeof(struct objc_class), 1);
    __CFRuntimeObjCClassTable[CFArrayGetTypeID()] = calloc(sizeof(struct objc_class), 1);
    // ...
}

Boolean _CFRuntimeSetupBridging(CFTypeID typeID, struct objc_class *mainClass, struct objc_class *subClass) {
    void *isa = __CFISAForTypeID(typeID);
    memmove(isa, subClass, sizeof(struct objc_class));
    class_poseAs(isa, mainClass);
    return true;
}
```

假扮（posing）是 Objective-C 运行时的一个已废弃特性（并在 Objective-C 2 中被移除），它实际上允许一个子类接管其超类的身份。假扮的类会获得原始类的名称，并且为了保持名称唯一性，运行时会在原始类名前加上 `%`，在原始元类名前加上 `_%`。因此，继续以数组为例，`NSCFArray__` 变成了 `NSCFArray`，而原来的 `NSCFArray` 变成了 `%NSCFArray`。

假扮的类实例会接收发送给原始类实例的所有消息。在上述桥接完成后，任何发送给 `NSCFArray` 类（例如 `alloc`）的消息，都会由假扮成 `NSCFArray` 的类（即 `NSCFArray__`）接收。因此，这种重定向会导致 Foundation 使用假扮的类类型创建新对象。然后，当将 Foundation 对象作为 `CFTypeRef` 传递给 CoreFoundation 时，`CF_IS_OBJC` 会返回 `false`，因为该对象具有将其标识为私有桥接类型的 `isa`（因此不需要 Objective-C 分派到用户定义的子类）。由于它是一个私有类，CoreFoundation 可以直接访问其内部。

### Mac OS X 10.5 "Leopard" 及更高版本，以及 iOS

未来类极大地简化了免费桥接的实现。在 Mac OS X 10.5 及更高版本中，桥接配置仍在 `__CFInitialize()` 中进行，但有一些关键区别：

1. 当动态链接器加载框架时就会调用 `__CFInitialize()`，消除了对下游代码的任何初始化依赖。
2. 对于每种桥接类型，CoreFoundation 都会使用类名调用 `objc_getFutureClass()`，并使用运行时返回的 `Class` 指针填充 `__CFRuntimeObjCClassTable`。

    - 如果类已加载，运行时返回其实例指针。
    - 否则，运行时[分配一个 `objc_class` 实例](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2996-L3019)，并返回指向这个“未来”类的指针。然后，当进程稍后加载具有该名称的类时，运行时会将类定义[复制](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L3406-L3436)到之前分配的内存中（类似于先前版本中的 `_CFRuntimeSetupBridging()`），并将从二进制映像加载的类定义[重新映射](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L1976-L1997)到之前分配的类定义（类似于假扮）。尽管有相似之处，但这种策略简化了 Objective-C 运行时和 CoreFoundation 的实现。

以下是 Leopard 中新的 [Core Foundation 实现的近似代码](https://github.com/apple-oss-distributions/CF/blob/CF-476.10/CFRuntime.c#L723)。

```
static void __CFInitialize(void) __attribute__ ((constructor));
static void __CFInitialize(void) {
    // ...
    _CFRuntimeBridgeClasses(0x10/*CFDictionaryGetTypeID()*/, "NSCFDictionary");
    _CFRuntimeBridgeClasses(0x11/*CFArrayGetTypeID()*/, "NSCFArray");
    // ...
}

void _CFRuntimeBridgeClasses(CFTypeID cf_typeID, const char *objc_classname) {
    __CFRuntimeObjCClassTable[cf_typeID] = objc_getFutureClass(objc_classname);
}
```

并没有要求未来类必须在进程的生命周期内被实现。但是，如果未来类收到任何消息，进程将会崩溃。我抽查了未来类与 Objective-C 运行时函数的使用情况，所测试的函数能够正常工作，即使这可能只是巧合。

## 存根类

macOS 10.15 和 iOS 13 中的 Objective-C 运行时引入了存根类（stub class），以支持稳定的 Swift ABI。在以下情形中，Swift 编译器会发出存根类：

1. 一个 Swift 类类型被声明为可以通过 `@objc` 特性在 Objective-C 中表示，这包括任何直接或间接继承自 `NSObject` 的类。
2. 步骤 1 中的 Swift 类被编译到启用了[库演变（library evolution）](https://www.swift.org/blog/library-evolution/)（使用 `-enable-library-evolution` 构建标志）的动态库（包括框架）中。库演变也称为弹性（resilience）或 ABI 稳定性。
3. 另一个模块中的 Swift 类导入了步骤 2 中的模块，并对步骤 1 中定义的类进行派生子类。当编译这个派生 Swift 类时，编译器会发出作为存根类的 Objective-C 类元数据。

我对为什么在此场景下需要存根进行了初步调查，但未能得出结论。我想答案可能要等到 Swift 内部系列文章才能揭晓🙃。但是，我们可以检查 Objective-C 运行时如何处理存根类。

`isa` 值为 1 到 15（含）[标识](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.h#L2426-L2429)一个 `objc_class` 实例为存根类。目前，[1 以外的 `isa` 值被保留](https://github.com/apple/swift/blob/swift-5.7.3-RELEASE/docs/ObjCInterop.md#stub-classes)。

```
bool isStubClass() const {
    uintptr_t isa = (uintptr_t)isaBits();
    return 1 <= isa && isa < 16;
}
```

如果调用了 `objc_getClassList()` 或 `objc_copyClassList()`，运行时将根据需要初始化加载到进程中的所有存根类。否则，存根类会在需要类对象时按需初始化。

由 Swift 编译器生成的 Objective-C 头文件会向类接口添加一个 `__attribute__((objc_class_stub))`，这指示 Clang 通过调用 [`objc_loadClassref()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2049-L2062) 来获取类对象，而不是直接引用类符号。运行时函数在首次访问时调用 Swift 初始化器来生成 `Class` 对象，并将结果存储在存根中以供将来访问。

我期待有一天能写一篇文章，介绍究竟是哪种 Swift 特性使得这种额外的间接步骤成为必要！

---

[^1](#_footnoteref_1). 那篇类实现文章已更新，补充了未实现类的细节，并链接到本文。
