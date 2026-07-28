---
title: 'Objective-C 内部实现：Retain'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/07/22/objc-retain'
original_language: en
published: 2023-07-22
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f04a4c2a6197e049'
translated: true
---

> 原文：[Objective-C Internals: Retain Objective-C memory is managed through a reference counting scheme, which has evolved from a relatively simple API into a sophisticated, highly-optimized implementation wh](https://alwaysprocessing.blog/2023/07/22/objc-retain)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：Retain

![两个人用线缆连接计算设备。这能建立起一个对象所有权关系图吗？](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c7eb8f6e-a4d2-4d14-9dec-278d8e82e500/public)

Objective-C 内存通过引用计数（reference counting）方案进行管理，该方案已从相对简单的 API 演进为精细、高度优化的实现，同时保持了源代码和 ABI 兼容性。

## 背景

OS X 10.7 和 iOS 5 引入了[自动引用计数（Automatic Reference Counting）](https://clang.llvm.org/docs/AutomaticReferenceCounting.html)（ARC），通过消除样板代码并减少引用计数 bug（如内存泄漏和过度释放）的发生面，提高了 Objective-C 程序员的开发效率。

在 ARC 之前，`-[NSObject retain]`、`-[NSObject release]`^[[1](#_footnotedef_1)] 和 `-[NSObject autorelease]`^[[2](#_footnotedef_2)] 方法是管理对象引用计数的唯一接口。而且，在 OS X 10.8 和 iOS 6 之前，`NSObject` 的实现是 Foundation 的一部分，而不是 Objective-C runtime。

ARC 的设计者们从 Apple 向 Objective-C 添加垃圾收集（garbage collection）的失败尝试中吸取教训，识别出了提高该功能成功可能性的一个关键需求：自动引用计数必须在同一进程中与手动引用计数透明地互操作（interoperate），而无需重新编译现有代码（例如，一个第三方仅二进制库）。

在 macOS 早期，有些对象重写引用计数方法^[[3](#_footnotedef_3)] 来使用自己的实现的情况并不罕见，这通常是出于性能原因。ARC 必须支持与这些自定义引用计数实现透明地互操作，以满足上述需求。

## 入口点

引用计数操作有两个接口：长期存在的 `NSObject` API 和 ARC 使用的编译器私有 API，两者都调用同一个核心实现。以下两个小节将分别研究每个接口的 retain 实现，下一节将讨论核心实现。

### NSObject

`-[NSObject retain]` 的实现^[[4](#_footnotedef_4)] 很简单——它只是调用 `_objc_rootRetain` 来 retain `self`。

`runtime/NSObject.mm` 第 [2502-2504 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L2502-L2504)

```
- (id)retain {
  return _objc_rootRetain(self);
}
```

术语 _root_ 表示对象[类层次结构](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#architecture-diagram)中的根类接收到了 `-retain` 消息。因此，该类没有重写 `-retain`，或者重写调用了超类（superclass）方法，所以 retain 操作保证使用 runtime 的实现。（正如我们将在下一节中看到的，并非所有入口点都有此保证。）

接下来，`_objc_rootRetain` 函数也很简单，它调用了 `objc_object::rootRetain()`。

`runtime/NSObject.mm` 第 [1875-1881 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1875-L1881)

```
id _objc_rootRetain(id obj) {
  ASSERT(obj);
  return obj->rootRetain();
}
```

最后，`objc_object::rootRetain()` 调用了 `rootRetain` 的一个重载版本。

`runtime/objc-object.h` 第 [607-611 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L607-L611)

```
id objc_object::rootRetain() {
  return rootRetain(false, RRVariant::Fast);
}
```

此处调用的重载版本是核心实现，它有两个参数：

1. `tryRetain` 启用对加载弱引用（weak reference）的支持^[[5](#_footnotedef_5)]。参数值为 `false`，因为弱引用不能走这个代码路径。（runtime 必须先从一个弱引用加载对象，然后该对象才能接收消息，并且，根据定义，通过加载操作获得的对象引用是强引用。）
2. `variant` 提供关于调用路径的上下文，使核心实现能够省略不必要的工作。通过 `NSObject` 执行的 retain 使用 `RRVariant::Fast` 来跳过检查该类是否有自定义引用计数实现，因为通过 _root_ 类执行操作，根据定义就不是自定义的。

### 自动引用计数（Automatic Reference Counting）

当 ARC 启用时，编译器通过一个为 ARC 添加的编译器私有 API 执行引用计数操作，以此作为性能优化。该 API 允许引用计数操作直接调用 Objective-C runtime，并跳过发送消息的开销。

`runtime/NSObject.mm` 第 [1772-1777 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1772-L1777)

```
id objc_retain(id obj) {
  if (_objc_isTaggedPointerOrNil(obj)) return obj;
  return obj->retain();
}
```

该函数首先检查对象指针值，如果它不引用堆上的对象，则立即返回，这可能发生在两种情况下：

1. 指针为 `nil`。向 `nil` 发送消息是合法的，因此 `-[NSObject retain]` 的这种优化也必须支持 `nil` 指针。
2. 指针是[标签指针（tagged pointer）](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr)。标签指针是 Objective-C runtime 的一个实现细节，对编译器不可见，因此编译器无法消除 retain 操作。标签指针不参与引用计数（没有堆分配需要跟踪），因此无需继续处理。

如果对象指针值引用了堆上的对象，则该函数调用 `objc_object::retain()` 来执行 retain 操作。

`runtime/objc-object.h` 第 [589-596 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L589-L596)

```
inline id objc_object::retain() {
  ASSERT(!isTaggedPointer());
  return rootRetain(false, RRVariant::FastOrMsgSend);
}
```

此函数使用以下参数调用核心实现（尽管此时 `rootRetain` 中的 _root_ 是用词不当）：

- `tryRetain` 为 `false`，原因同[NSObject](#nsobject) 入口点中讨论的。
- `variant` 为 `RRVariant::FastOrMsgSend`。没有进行任何内省，无论是直接的（见下面的 [rootRetain](#rootretain)）还是间接的（通过消息发送，见上面的 [NSObject](#nsobject)），因此还不知道该对象的类是否重写了任何引用计数方法（因此该函数名中**不**包含术语 _root_）。

  `variant` 中的 `MsgSend` 部分指示核心执行必要的内省，以确定该对象的类是否重写了引用计数方法。如果是，核心实现通过向对象发送 `-retain` 消息来执行 retain 操作（该消息可能通过 [`-[NSObject retain]`](#nsobject) 重新进入 runtime）。

## rootRetain

[`objc_object::rootRetain(bool, RRVariant)`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L619-L706) 函数体量较大，因此我们将逐段分析。

`runtime/objc-object.h` 第 [622 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L622)

```
if (slowpath(isTaggedPointer())) return (id)this;
```

尽管 ARC 入口点检查了标签指针，但 `NSObject` 入口点没有。我目前不清楚为什么 `NSObject` 实现不执行此检查，但它必须在某处发生，在这个版本的 runtime 中，它发生在这里。

接下来，runtime 加载对象的 `isa` 值。

`runtime/objc-object.h` 第 [624-630 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L624-L630)

```
bool sideTableLocked = false;
bool transcribeToSideTable = false;
isa_t oldisa = LoadExclusive(&isa().bits);
isa_t newisa;
```

在所有的现代 Apple 平台上，`isa` 存储了对象的 retain 计数（引用计数）[。](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#extra_rc) Objective-C runtime 在 [`arm64` 架构](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L180-L215)上使用 ARM 的[独占监视器](https://developer.arm.com/documentation/dht0008/a/arm-synchronization-primitives/exclusive-accesses/exclusive-monitors)同步原语来管理并发（concurrency），`LoadExclusive` 函数由此得名。在[所有其他架构](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L219-L245)上，包括 `arm64e`，Objective-C runtime 使用 [C11 原子操作](https://en.cppreference.com/w/c/atomic)。（我不确定这里 `arm64` 和 `arm64e` 哪个是异常情况，也不确定原因。）

如果编译器私有 API 是 retain 操作的入口点，runtime 必须检查该类是否重写了任何引用计数方法。

`runtime/objc-object.h` 第 [632-642 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L632-L642)

```
if (variant == RRVariant::FastOrMsgSend) {
  // These checks are only meaningful for objc_retain()
  // They are here so that we avoid a re-load of the isa.
  if (slowpath(oldisa.getDecodedClass(false)->hasCustomRR())) {
    ClearExclusive(&isa().bits);
    if (oldisa.getDecodedClass(false)->canCallSwiftRR()) {
      return swiftRetain.load(memory_order_relaxed)((id)this);
    }
    return ((id(*)(objc_object *, SEL))objc_msgSend)(this, @selector(retain));
  }
}
```

自定义引用计数实现很少见，因此 runtime 使用其 [`slowpath()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L163) 宏向 CPU 的分支预测单元提示此路径不太可能运行。`getDecodedClass()` 返回对象的 [`Class` 对象](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl)，其中有一个[标志位](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-runtime-new.h#L1937-L1939)指示该类是否重写了任何引用计数方法。这个快速检查为 ARC 入口点提供了必要的类内省，以最小的开销支持自定义引用计数实现。

如果某个类具有自定义引用计数实现，runtime 会向对象发送 `-retain` 消息以完成 ARC 发起的 retain 操作。请注意，该对象随后可能会调用 `-[NSObject retain]`，但此代码块不会再次执行，因为 `variant` 将是 `RRVariant::Fast`。

纯 Swift 类（即不从 `NSObject` 派生的类）为了与 Objective-C 兼容，派生自 [`SwiftObject` 类](https://github.com/apple/swift/blob/swift-5.8.1-RELEASE/stdlib/public/runtime/SwiftObject.h#L41-L78)（仅限 Apple 平台）。Swift 使用自己的引用计数系统，因此 `SwiftObject` [实现了](https://github.com/apple/swift/blob/swift-5.8.1-RELEASE/stdlib/public/runtime/SwiftObject.mm#L270) [引用计数方法](https://github.com/apple/swift/blob/e495eed8914a87aa3403411fbc2cf3f9e6119846/include/swift/Runtime/HeapObject.h#L1108-L1146)以支持将纯 Swift 对象桥接到 Objective-C。作为针对这种情况的优化，Objective-C runtime 直接调用 Swift runtime 的 `swift_retain()` 函数^[[6](#_footnotedef_6)]（而不是通过消息发送来 retain 对象）。

继续到下一个块。

`runtime/objc-object.h` 第 [644-651 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L644-L651)

```
if (slowpath(!oldisa.nonpointer)) {
  // a Class is a Class forever, so we can perform this check once
  // outside of the CAS loop
  if (oldisa.getDecodedClass(false)->isMetaClass()) {
    ClearExclusive(&isa().bits);
    return (id)this;
  }
}
```

`Class` 对象永远不会被释放，也不需要引用计数。因此，如果对象是类对象，该函数会直接返回它，不执行任何进一步的工作。

### 比较并交换 （Compare and Swap） 循环

[比较并交换](https://en.wikipedia.org/wiki/Compare-and-swap)循环是 retain 实现的核心。它从（重新）初始化循环的起始状态开始。

`runtime/objc-object.h` 第 [654-655 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L654-L655)

```
do {
  transcribeToSideTable = false;
  newisa = oldisa;
```

它将 `newisa` 设置为当前的 `isa` 值（即 `oldisa`），循环将更新 `newisa` 以反映递增后的 retain 计数。下一小节将探讨 `transcribeToSideTable` 的用途。

`runtime/objc-object.h` 第 [656-660 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L656-L660)

```
  if (slowpath(!newisa.nonpointer)) {
    ClearExclusive(&isa().bits);
    if (tryRetain) return sidetable_tryRetain() ? (id)this : nil;
    else return sidetable_retain(sideTableLocked);
  }
```

首先，循环检查对象实例是否具有[非指针 `isa`](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa)。如果没有，则 retain 计数记录在侧表中^[[7](#_footnotedef_7)]。这个检查在循环内执行，因为如果此线程在比较并交换中失败，可能是由于另一个线程以某种方式改变了对象状态，导致其不再使用非指针 `isa`。

接下来，循环检查是否在另一个竞态中失败。

`runtime/objc-object.h` 第 [661-673 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L661-L673)

```
  // don't check newisa.fast_rr; we already called any RR overrides
  if (slowpath(newisa.isDeallocating())) {
    ClearExclusive(&isa().bits);
    if (sideTableLocked) {
      ASSERT(variant == RRVariant::Full);
      sidetable_unlock();
    }
    if (slowpath(tryRetain)) {
      return nil;
    } else {
      return (id)this;
    }
  }
```

在（至少）三种场景下，一个线程尝试 retain 对象时，该对象可能正在被释放：

1. `tryRetain` 为 `true`，并且此线程在加载弱对象时失败，对象已开始释放。函数返回 `nil`，表示无法获取强引用。在此场景中，调用方 `objc_loadWeakRetained()` 持有一个指向弱引用侧表的锁，防止对象被释放，因此通过对象指针读取 `isa` 是定义良好的行为。
2. 另一个线程释放了该对象，导致它被释放，这通常发生在进程同时从 `strong`、`nonatomic` 属性进行读写操作的竞态条件下。此场景中的一切行为都是未定义的。函数返回 `self` 以履行 `-retain` 的约定，但它将成为一个[悬垂指针](https://en.wikipedia.org/wiki/Dangling_pointer)，几乎肯定会导致调用线程在不久后崩溃。在竞态条件下命中此代码路径算是“幸运”的。实际上，通过悬垂指针读取到的 `isa` 位可能使该函数走向无数种方向，导致不可预测的结果。
3. `-dealloc` 中的逻辑导致执行了一个 retain（例如，`-dealloc` 的实现将 `self` 传递给一个清理例程，ARC 编译器在此例程中发出 retain/release 配对）。此场景**不是**像上述两种情况那样的竞态条件，因为 retain 发生在执行释放的同一线程上。然而，如果执行 retain 的函数要求对象实例在其调用作用域结束后仍然存活（例如，将 `self` 存储在另一个对象的 `strong` 属性中），此场景可能导致未定义行为，因为当释放完成后，该指针将变成悬垂指针。

最后，我们来到实际的递增操作。

`runtime/objc-object.h` 第 [674-675 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L674-L675)

```
  uintptr_t carry;
  newisa.bits = addc(newisa.bits, RC_ONE, 0, &carry);  // extra_rc++
```

回忆一下，非指针 `isa` 是一个具有[三种变体](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa-variants)的位字段。`RC_ONE` 的值是将该位字段视为整数时代表一个 retain 计数的位。retain 计数存储在 `isa` 的最高有效位中，因此如果所有 retain 计数位都已被使用，将会发生溢出或进位（carry）（将在下一小节讨论）。如果没有发生溢出，`newisa` 包含了递增后的 retain 计数，并准备好写回对象实例。

`runtime/objc-object.h` 第 [691 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L691)

```
} while (slowpath(!StoreExclusive(&isa().bits, &oldisa.bits, newisa.bits)));
```

如果 `&isa()` 处的值与 `&oldisa` 的值匹配，则比较并交换操作成功，并将 `newisa` 的值写入 `&isa()`，循环结束。

否则，自该线程将值加载到 `oldisa` 后，`&isa()` 的值已发生改变。比较并交换操作失败，并将 `&isa()` 的新值写入 `oldisa`。循环继续，直到该线程赢得一次比较并交换操作，或者另一个线程更改对象状态以激活上述返回路径之一。

### 完整变体（Full Variant）

如果 retain 计数溢出了非指针 `isa` 中的位，runtime 将使用侧表来存储部分 retain 计数。

`runtime/objc-object.h` 第 [677-690 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L677-L690)

```
  if (slowpath(carry)) {
    // newisa.extra_rc++ overflowed
    if (variant != RRVariant::Full) {
      ClearExclusive(&isa().bits);
      return rootRetain_overflow(tryRetain);
    }
    // Leave half of the retain counts inline and
    // prepare to copy the other half to the side table.
    if (!tryRetain && !sideTableLocked) sidetable_lock();
    sideTableLocked = true;
    transcribeToSideTable = true;
    newisa.extra_rc = RC_HALF;
    newisa.has_sidetable_rc = true;
  }
```

如果此次函数调用使用的是 `Fast` 或 `FastOrMsgSend` 变体，它会停止尝试 retain 操作，并将任务转交给 `rootRetain_overflow()`。

`runtime/objc-object.h` 第 [1372-1376 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1372-L1376)

```
NEVER_INLINE id objc_object::rootRetain_overflow(bool tryRetain) {
  return rootRetain(tryRetain, RRVariant::Full);
}
```

我推测这个函数的目的是在堆栈跟踪（stack trace）中提供一个帧，以帮助 Apple 工程师排查 runtime 中的 retain 崩溃问题，因为侧表锁（使用不可重入的自旋锁）的相互作用可能难以分析。

如果 retain 计数在 `rootRetain` 中使用 `Full` 变体时溢出，实现会将 retain 计数值的一半发送到侧表，并将另一半留在非指针 `isa` 中。将 retain 计数一分为二，是为了最小化侧表访问次数（需要更少的 CPU 指令和更少的锁获取）。如果实现只将溢出的位发送到侧表，那么在溢出边界值处的引用计数操作可能会成为系统的性能负担。

`runtime/objc-object.h` 第 [693-700 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L693-L700)

```
  if (variant == RRVariant::Full) {
    if (slowpath(transcribeToSideTable)) {
      // Copy the other half of the retain counts to the side table.
      sidetable_addExtraRC_nolock(RC_HALF);
    }
    if (slowpath(!tryRetain && sideTableLocked)) sidetable_unlock();
  }
```

侧表在比较并交换成功后才更新，因为另一个线程可能赢得将溢出 retain 计数移动到侧表的竞态。比较并交换循环获取侧表的锁，这防止了在另一个线程也尝试读取或写入侧表时发生竞态条件。

### 返回 self

在比较并交换成功，并且如果需要，侧表也已更新后，retain 操作就完成了。

`runtime/objc-object.h` 第 [693-700 行](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L693-L700)

```
return (id)this;
```

最后一步是返回 `self`^[[8](#_footnotedef_8)] 以履行 [`-[NSObject retain`](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1571946-retain) 的约定]：

> 为方便起见，`retain` 返回 `self`，因为它可能用于嵌套表达式中。

自从 20 多年前 Mac OS X 首次发布以来，Retain 已经演变成一个高度优化的操作。Release、autorelease 和 dealloc 也是如此，我们很快会看到它们。

---

[1](#_footnoteref_1). 本文篇幅较长，因此我决定在[下一篇文章](https://alwaysprocessing.blog/2023/10/01/objc-release)中讨论 release。

[2](#_footnoteref_2). Autorelease 是一个纯粹基于 release 构建的附加功能。我将在未来的文章中讨论其实现，因为它不是核心 retain/release 操作的一部分。

[3](#_footnoteref_3). Objective-C runtime 将 `retain`、`release`、`autorelease`、`_tryRetain`、`_isDeallocating`、`retainCount`、`allowsWeakReference` 和 `retainWeakReference` 选择器（selector）视为[引用计数方法族](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-runtime-new.mm#L1073-L1080)的一部分。如果某个类重写了这些方法中的任何一个，Objective-C runtime 会将该类归类为具有自定义引用计数实现。

[4](#_footnoteref_4). `NSObject` 的实现已在 OS X 10.8 和 iOS 6 中移入 Objective-C runtime，以支持 `os_object` 的引入，这使得 GCD 和 XPC 类型能够参与 ARC 并与 Foundation 集合（collection）配合使用。在此次迁移之前，它在 Foundation 中的实现可能是一样的。

[5](#_footnoteref_5). 对弱引用实现的探究已列入后续文章的待办事项。

[6](#_footnoteref_6). Swift runtime 依赖于 Objective-C runtime，从而产生了反向依赖关系。Objective-C runtime 通过[动态加载](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L95-L119)来自 `libswiftCore.dylib` 的 `swift_retain` 符号来解决此问题。

[7](#_footnoteref_7). 未来的文章将讨论 retain 计数侧表的实现。

[8](#_footnoteref_8). Apple 从 OS X 10.7 和 iOS 5 开始使用 Objective-C++ 来实现 Objective-C runtime，但直到 OS X 10.9 和 iOS 7 才开始使用 Objective-C++ 来实现对象类型本身。未来的文章将探讨这种方法，并展示 `this` 和 `self` 是如何相同的。
