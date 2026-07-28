---
title: 'Objective-C 内部实现：isa 指针的多种用途'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/01/19/objc-class-isa'
original_language: en
published: 2023-01-19
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d9c27a69ebece0ab'
translated: true
---

> 原文：[Objective-C Internals: The Many Uses of isa The Objective-C runtime optimizes performance by packing additional information into an object’s isa pointer. This post compares the different packing mecha](https://alwaysprocessing.blog/2023/01/19/objc-class-isa)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：isa 指针的多种用途

![两只狗坐在一条长长的走廊里，两旁有很多扇不同的门。它们会选择哪一扇？](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c42b427a-167d-4a99-224d-48f7af07c100/public)

Objective-C 运行时通过将附加信息打包进对象的 `isa` 指针来优化性能。本文比较了不同的打包机制，并讨论了存储在指针值中的各种字段值。

本系列的第一篇文章[介绍了](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#method-dispatch)`isa` 指针：每个 Objective-C 对象中的一个实例变量（instance variable），它指向该对象的类对象（class object），而类对象则标识了该对象实例的类型。前一篇文章引用了此字段的[内部定义](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl#preamble)（`char isa_storage[sizeof(isa_t)]`），并提到 `isa` 字段已废弃。现在，我们将更详细地探讨运行时如何使用此字段及其废弃的原因。

## 背景

在 iOS、macOS 和 tvOS 上的 Apple 32 位 Objective-C 运行时中，`isa` 字段仅仅是一个指向对象类对象的指针。以下来自 [`objc-private.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-private.h#L80-L110)、[`objc-object.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L976-L993) 和 [`objc-class.mm`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-class.mm#L181-L185) 的代码展示了（针对这些平台的）`object_getClass()` 运行时函数的有效实现，该函数从一个对象实例中获取 `isa` 类指针值。

```
// objc-private.h
union isa_t {
private:
    Class cls;

public:
    Class getClass(bool authenticated);
};

// objc-object.h
Class objc_object::getIsa() {
    return ISA(); // bool argument defaulted to false
}

Class isa_t::getClass(bool) {
    return cls;
}

Class objc_object::ISA(bool) {
    return isa().getClass(false);
}

// objc-class.mm
Class object_getClass(id obj) {
    if (obj) return obj->getIsa();
    else return Nil;
}
```

## 非指针 isa（Non-Pointer isa）

Apple 的 64 位 Objective-C 运行时（除 64 位 Intel 处理器上的模拟器外）和 Apple Watch 的 Objective-C 运行时使用“非指针 `isa`（non-pointer `isa`）”，它将附加信息打包进未使用的指针位中。

在指针值中设置额外的位会改变它所引用的地址并使其值无效——新值可能不是进程地址空间中的地址，如果解引用（dereference）可能导致非对齐内存访问（unaligned memory access）等。因此得名“非指针 `isa`”。

由于 `isa` 字段不再只存储类指针值，它在公有头文件 [`objc.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc.h#L41-L43) 中被标记为已废弃，以阻止可能导致未定义行为的直接使用。（可用性宏定义位于 [`objc-api.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-api.h#L170-L172) 中。）`object_getClass()` 和 `object_setClass()` 函数是直接使用 `isa` 字段的官方替代方案。

```
// objc-api.h
#if !defined(OBJC_ISA_AVAILABILITY)
#   define OBJC_ISA_AVAILABILITY  __attribute__((deprecated))
#endif

// objc.h
struct objc_object {
    Class _Nonnull isa  OBJC_ISA_AVAILABILITY;
};
```

### 非指针 isa 的变体

在撰写本文时，非指针 `isa` 有以下[三种实现](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/isa.h#L44-L171)：

1. 打包式 `isa`（Packed `isa`）（Apple Silicon `arm64`-非-`e` 变体，64 位 Intel）
2. 带指针认证的打包式 `isa`（Packed `isa` with Pointer Authentication）（Apple Silicon `arm64e` 变体）
3. 索引式 `isa`（Indexed `isa`）（Apple Watch）

下表显示了每种非指针 `isa` 变体打包到未使用的类指针位中的额外字段：

打包式 `isa`

打包式 `isa` + 指针认证

索引式 `isa`

`nonpointer`

✓

✓

✓

`has_assoc`

✓

✓

✓

`has_cxx_dtor`

✓

x

✓

`shiftcls`

✓

−

−

`shiftcls_and_sig`

−

✓

−

`indexcls`

−

−

✓

`magic`

✓

✓

✓

`weakly_referenced`

✓

✓

✓

`has_sidetable_rc`

✓

✓

✓

`extra_rc`

✓

✓

✓

**图例：**

- ✓ 变体拥有此字段
- − 字段不适用于此变体
- x 变体**没有**此字段

现在，我们来探讨运行时时如何使用每个字段，以及它们如何提升 Objective-C 运行时性能。

### nonpointer

这是指针载荷中最低有效位（因此对于指针值来说始终为零），如果设置，表示 `isa` 值是非指针变体。此字段使运行时能够为了兼容性目的，在运行时按类（per-class）选择使用传统的 `isa` 值即类指针的行为，或者选择非指针 `isa` 优化。

在 macOS 上，对于[链接到 OS X 10.10 或更早版本](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L3610-L3616)的任何 App，非指针 `isa` 会被禁用，因为直到 OS X 10.11 才废弃了直接使用 `isa`。

```
if (dyld_get_active_platform() == PLATFORM_MACOS && !dyld_program_sdk_at_least(dyld_platform_version_macOS_10_11)) {
    DisableNonpointerIsa = true;
}
```

如果主 App 可执行文件包含 [`__DATA,__objc_rawisa`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L3620-L3631) 段，运行时会禁用非指针 `isa` 功能。那些可能会加载在直接使用 `isa` 被废弃之前链接的插件（plug-in）的 App，会使用此段来实现二进制兼容性。（这也是仅限 macOS。）

```
for (EACH_HEADER) {
    if (hi->mhdr()->filetype != MH_EXECUTE) continue;
    unsigned long size;
    if (getsectiondata(hi->mhdr(), "__DATA", "__objc_rawisa", &size)) {
        DisableNonpointerIsa = true;
    }
    break;  // assume only one MH_EXECUTE image
}
```

对于所有平台，Objective-C 运行时会为 `OS_object` 类及其派生类[禁用非指针 `isa` 功能](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2679-L2684)，因为 `libdispatch` 也将 `isa` 指针用作 vtable（虚函数表）。

```
else if (!hackedDispatch  &&  0 == strcmp(ro->getName(), "OS_object")) {
    // hack for libdispatch et al - isa also acts as vtable pointer
    hackedDispatch = true;
    instancesRequireRawIsa = true;
}
```

### has_assoc、has_cxx_dtor、weakly_referenced 和 has_sidetable_rc

这四个字段的主要目的是确定一个对象是否可以使用快速释放路径（fast deallocation path），即简单地使用 `free()` 释放对象内存。否则，运行时在释放内存之前必须先执行额外的簿记（bookkeeping）工作。来自 [`objc-object.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L562-L583)：

```
void objc_object::rootDealloc() {
    if (isTaggedPointer()) return;

    if (isa().nonpointer                     &&
        !isa().weakly_referenced             &&
        !isa().has_assoc                     &&
#if ISA_HAS_CXX_DTOR_BIT
        !isa().has_cxx_dtor                  &&
#else
        !isa().getClass(false)->hasCxxDtor() &&
#endif
        !isa().has_sidetable_rc)
    {
        free(this);
    } else {
        object_dispose((id)this);
    }
}
```

- `has_assoc`：如果对象有一个通过使用 `objc_setAssociatedObject()` 运行时 API 创建的[关联对象（associated object）](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj)，则设置此位。如果一个对象有一个或多个关联对象，运行时必须在释放对象内存之前从其侧表中移除这些条目。
- `has_cxx_dtor`：如果该类或其超类有一个 `.cxx_destruct` 方法，则设置此位。如果一个 Objective-C 对象有一个或多个 C++ 类型的实例变量^[[1](#_footnotedef_1)]，运行时会在对象分配期间（在任何 `init` 方法之前）调用该类的 `.cxx_construct` 实例方法来运行任何非平凡的构造函数（non-trivial constructor）。在 `dealloc` 方法链完成后，运行时在释放对象内存之前，会调用该类的 `.cxx_destruct` 实例方法来运行任何非平凡的析构函数（non-trivial destructor）。

    - 当自动引用计数（Automatic Reference Counting，ARC）启用时，编译器会在类的 `.cxx_destruct` 方法中实现释放其实例变量的操作，从而抑制直接调用 `free()` 的优化。[`object_dispose()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L8582-L8591:) 代码路径会调用 [`objc_destructInstance()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L8560-L8574:)，后者在可用时使用非指针 `isa` 位来省略不必要的清理操作。
    - 注意，当启用指针认证时此位不可用，但该信息可从类对象获得，代价是需要一次额外的内存加载（memory load）。
- `weakly_referenced`：只要创建了对该对象的弱引用（weak reference）^[[2](#_footnotedef_2)]，就设置此位。与关联对象类似，运行时必须在释放对象内存之前从其侧表中移除条目。
- `has_sidetable_rc`：如果[保留计数（retain count）](https://alwaysprocessing.blog/2023/07/22/objc-retain#the-full-variant)已溢出 [extra_rc](#extra_rc)，则侧表会存储额外的保留计数，同样，运行时必须在释放对象内存之前移除这些条目。

### shiftcls 和 shiftcls_and_sig

这些字段为打包式 `isa` 变体存储类指针。类对象总是 8 字节对齐的（无论是通过二进制镜像中的布局还是运行时的标准分配器），因此最低的 3 位总是 0。所以，“shift class”字段存储的是[移除了底部 3 位](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L201)后的类指针。此字段还依赖于对虚拟内存系统允许的[最大指针值](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/isa.h#L116)的了解，因为在位域（bit field）中存储该值时，值的高位会被截断。

运行时会使用指针认证（Pointer Authentication）对 Apple Silicon 上的类指针进行签名，并将其存储在 `shiftcls_and_sig` 字段中。除了有效指针值的下限和上限外，此字段还依赖于对指针认证所用位的了解。

### indexcls

Apple Watch 上的 Objective-C 运行时将类指针存储在一个数组中，并将类的数组索引（array index）存储在 `isa` 的 `indexcls` 字段中。索引是[在运行时惰性分配的](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L7171-L7189)，如果数组容量（32,767 个条目）耗尽，运行时会回退到使用指针 `isa`。

Apple Watch ABI 使用 32 位指针^[[3](#_footnotedef_3)]，没有足够的未使用位来同时存储指针值和打包位。使用数组存储类指针减少了表示类身份所需的位数，从而以一些间接性为代价实现了非指针 `isa` 的性能优势。

### magic

此字段未被运行时使用。运行时导出了用于 magic 掩码（magic mask）和 magic 值的常量，调试器使用它们来识别具有非指针 `isa` 的对象实例，以便启用 Objective-C 调试功能。

### extra_rc

当非指针 `isa` 功能对于该平台或类层次结构不可用时，对象实例的保留计数（retain count）存储在侧表中。然而，对于许多并发的 retain 或 release 操作，使用侧表可能会成为性能瓶颈，因为每次操作都必须获取锁。非指针 `isa` 功能通过将实例的保留计数存储在此字段中，减少了这种争用。

如果保留计数溢出了该字段，则[一半的保留计数会被移动到侧表](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L673-L695)中，而另一半保留在此字段中。只移动一半计数使得后续的 release 操作可以在获取锁访问侧表中的计数之前，先递减此字段的值。

此字段的大小因平台而异。下表列出了每个平台下该字段的大小和最大内联保留计数值。

`extra_rc` 位数

最大值

64 位 Intel 上的打包式 `isa`

8

255

Apple Silicon `arm64`-非-`e` 变体上的打包式 `isa`

19

524,287

带指针认证的 Apple Silicon（`arm64e` 变体）上的打包式 `isa`

8

255

索引式 `isa`（Apple Watch）

7

127

---

[1](#_footnoteref_1). 未来一篇文章会详细探讨 Objective-C++。

[2](#_footnoteref_2). 未来一篇文章会详细探讨弱引用。

[3](#_footnoteref_3). 未来一篇文章会详细分析 Apple 的 `arm64_32` ABI。
