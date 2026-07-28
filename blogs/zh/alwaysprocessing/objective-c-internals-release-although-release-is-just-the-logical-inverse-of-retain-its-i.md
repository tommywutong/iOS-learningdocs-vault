---
title: 'Objective-C 内部实现：release'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/10/01/objc-release'
original_language: en
published: 2023-10-01
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9f86ed9ae4033707'
translated: true
---

> 原文：[Objective-C Internals: Release Although release is "just" the logical inverse of retain, its implementation is much more complex, primarily due to the ARM synchronization model. This post explores the](https://alwaysprocessing.blog/2023/10/01/objc-release)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：release

![两人正在拉扯一根绳子。谁会先放手？](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/739048ac-8a94-451e-418a-6042a3a1ed00/public)

虽然 release “只是” retain 的逻辑逆操作，但其实现要复杂得多，这主要是由于 ARM 同步模型所致。本文将探讨 release 实现（相对于 retain）的独特之处，重点介绍 ARM 上的内存排序要求。

Objective-C 使用[引用计数（reference counting）](https://en.wikipedia.org/wiki/Reference_counting)方法来管理内存。本文将研究 release 操作，它会减少一个对象实例（object instance）的引用计数。[上一篇文章](https://alwaysprocessing.blog/2023/07/22/objc-retain)介绍了 retain 实现，它会增加一个对象实例的引用计数。retain 和 release 的实现相似，因为它们是互逆操作。在讨论相似之处时，我会引用[那篇关于 retain 的文章](https://alwaysprocessing.blog/2023/07/22/objc-retain)，以便本文专注于 release 的独特方面。

## 入口点

引用计数操作有两个接口：长期存在的 `NSObject` API 和 ARC 使用的编译器私有 API，两者都会调用到核心实现。以下两小节将分别检查每个接口的 release 实现，下一节将讨论核心实现。

### NSObject

与 `-[NSObject retain]` 类似，`-[NSObject release]` 也很简单——它只是调用 `_objc_rootRelease()` 来释放 `self`。

`runtime/NSObject.mm` 第 [2544-2546](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L2544-L2546) 行

```
- (void)release {
  _objc_rootRelease(self);
}
```

术语 _root_，正如在[上一篇关于 retain 的文章](https://alwaysprocessing.blog/2023/07/22/objc-retain#nsobject)中所讨论的，表示该操作是通过对象[类层级（class hierarchy）](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#architecture-diagram)中根类（root class）接收到的 `-release` 消息来执行的。

接下来，`_objc_rootRelease` 函数也很简单，它调用 `objc_object::rootRelease()`。

`runtime/NSObject.mm` 第 [1883-1889](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1883-L1889) 行

```
void _objc_rootRelease(id obj) {
  ASSERT(obj);
  obj->rootRelease();
}
```

最后，`objc_object::rootRelease()` 调用 `rootRelease` 的一个重载。

`runtime/objc-object.h` 第 [729-733](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L729-L733) 行

```
bool objc_object::rootRelease() {
  return rootRelease(true, RRVariant::Fast);
}
```

这里调用的重载是核心实现，它有两个参数：

1. `performDealloc` 指定当引用计数达到零时，release 操作是否应该释放（deallocate）该对象实例。除非是 [`_objc_rootReleaseWasZero()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1850-L1856) SPI^[[1](#_footnotedef_1)]（供第一方使用的系统编程接口，区别于供第三方使用的应用程序编程接口）在执行 release，否则运行时总是为这个参数传递 `true`。
2. `variant` 提供了关于调用路径的上下文信息，使核心实现能够省去不必要的工作。通过 `NSObject` 执行的 release 使用 `RRVariant::Fast` 来跳过检查类是否具有自定义引用计数实现，因为通过根类执行的操作，根据定义，不可能是自定义的。

### 自动引用计数（Automatic Reference Counting）

当启用 ARC 时，编译器通过一个为 ARC 添加的编译器私有 API 来执行引用计数操作，这是一种性能优化（在[上一篇关于 retain 的文章](https://alwaysprocessing.blog/2023/07/22/objc-retain#automatic-reference-counting)中也讨论过）。

`runtime/NSObject.mm` 第 [1780-1786](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1780-L1786) 行

```
void objc_release(id obj) {
  if (_objc_isTaggedPointerOrNil(obj)) return;
  return obj->release();
}
```

如果对象指针值引用的是堆上的一个对象，且经过与 [retain](https://alwaysprocessing.blog/2023/07/22/objc-retain#automatic-reference-counting) 相同的仪式派生出来，则该函数调用 `objc_object::release()` 来执行 release 操作。

`runtime/objc-object.h` 第 [709-716](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L709-L716) 行

```
inline void objc_object::release() {
  ASSERT(!isTaggedPointer());
  rootRelease(true, RRVariant::FastOrMsgSend);
}
```

该函数调用核心实现（尽管 `rootRelease` 中的 _root_ 在此处是用词不当），参数为：

- `true` 给 `performDealloc`，原因与上面 [NSObject](#nsobject) 入口点中讨论的相同。
- `RRVariant::FastOrMsgSend` 给 `variant`。尚未进行任何内省，无论是直接的（见下面的 [rootRelease](#rootrelease)）还是间接的（通过消息发送，见上面的 [NSObject](#nsobject)），因此还不知道该对象的类是否覆盖了任何引用计数方法（这就是该函数名称中**不**包含 _root_ 的原因）。

  `variant` 中的 `MsgSend` 部分指示核心执行必要的内省，以确定该对象的类是否覆盖了引用计数方法。如果覆盖了，核心实现通过向对象发送一个 `-release` 消息（该消息可能会通过 `-[NSObject release]` 重新进入运行时）来执行 release 操作。

## rootRelease

[`objc_object::rootRelease(bool, RRVariant)`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L741-L902) 函数比较大，因此我们将逐段分析。

`runtime/objc-object.h` 第 [744](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L744) 行

```
if (slowpath(isTaggedPointer())) return (id)this;
```

尽管 ARC 入口点检查了 tagged pointer，但 `NSObject` 入口点没有。我目前不清楚为什么 `NSObject` 实现不执行此检查，但它必须发生在某个地方，在这个版本的运行时中，它就在这里。

接下来，运行时加载对象的 `isa` 值^[[2](#_footnotedef_2)]。

`runtime/objc-object.h` 第 [746-750](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L746-L750) 行

```
bool sideTableLocked = false;
isa_t newisa, oldisa;
oldisa = LoadExclusive(&isa().bits);
```

如果 release 操作的入口点是编译器私有 API，那么运行时必须检查该类是否覆盖了任何引用计数方法^[[3](#_footnotedef_3)]。

`runtime/objc-object.h` 第 [752-764](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L752-L764) 行

```
if (variant == RRVariant::FastOrMsgSend) {
  // These checks are only meaningful for objc_release()
  // They are here so that we avoid a re-load of the isa.
  if (slowpath(oldisa.getDecodedClass(false)->hasCustomRR())) {
    ClearExclusive(&isa().bits);
    if (oldisa.getDecodedClass(false)->canCallSwiftRR()) {
      swiftRelease.load(memory_order_relaxed)((id)this);
      return true;
    }
    ((void(*)(objc_object *, SEL))objc_msgSend)(this, @selector(release));
    return true;
  }
}
```

如果类具有自定义引用计数实现，则运行时向对象发送一个 `-release` 消息以完成 ARC 发起的 release 操作。注意，该对象随后可能会调用 `-[NSObject release]`，但此代码块不会再次执行，因为 `variant` 将是 `RRVariant::Fast`。

继续看下一个代码块。

`runtime/objc-object.h` 第 [766-773](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L766-L773) 行

```
if (slowpath(!oldisa.nonpointer)) {
  // a Class is a Class forever, so we can perform this check once
  // outside of the CAS loop
  if (oldisa.getDecodedClass(false)->isMetaClass()) {
    ClearExclusive(&isa().bits);
    return false;
  }
}
```

`Class` 对象永远不会被释放，也不需要引用计数。因此，如果对象是一个类对象，则该函数返回它而不执行任何进一步的工作。

### 比较并交换循环（Compare and Swap Loop）

[比较并交换（compare-and-swap）](https://en.wikipedia.org/wiki/Compare-and-swap)循环是 release 实现的核心。它以一个可能出乎意料的 `goto` 标签开始。下面的[完全变体](#the-full-variant)小节将讨论此函数对 `goto` 的使用。

`runtime/objc-object.h` 第 [775-777](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L775-L777) 行

```
retry:
do {
  newisa = oldisa;
```

循环首先将 `newisa` 设置为当前的 `isa` 值（即 `oldisa`），后续步骤将更新它以反映递减后的引用计数。

然后，循环检查该对象实例是否具有[非指针 `isa`（non-pointer `isa`）](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa)。如果没有，则引用计数记录在 side table^[[4](#_footnotedef_4)] 中。此检查在循环内执行，因为如果此线程在比较并交换中失败，可能是由于另一个线程以某种方式改变了该对象，使其不再使用非指针 `isa`。

`runtime/objc-object.h` 第 [778-781](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L778-L781) 行

```
  if (slowpath(!newisa.nonpointer)) {
    ClearExclusive(&isa().bits);
    if (tryRetain) return sidetable_tryRetain() ? (id)this : nil;
    else return sidetable_retain(sideTableLocked);
  }
```

接下来，循环检查是否在另一场竞态中落败。

`runtime/objc-object.h` 第 [782-788](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L782-L788) 行

```
  if (slowpath(newisa.isDeallocating())) {
    ClearExclusive(&isa().bits);
    if (sideTableLocked) {
      ASSERT(variant == RRVariant::Full);
      sidetable_unlock();
    }
    return false;
  }
```

一个对象可能正在被释放，而此时另一个线程正试图释放它，这至少发生在两种场景下：

1. 另一个线程释放了该对象，导致它被释放，这通常是由于进程并发地读取和写入一个 `strong`、`nonatomic` 的属性（property）时出现的竞态条件（race condition）所致。此场景的所有情况都属于未定义行为（undefined behavior）。
2. `-dealloc` 中的逻辑导致了 release 的执行（例如，`-dealloc` 的实现将 `self` 传递给一个清理例程，而 ARC 编译器在那里发出了一对 retain/release）。此场景**不是**像上面的竞态条件，因为 release 发生在执行释放的同一线程上。

如果 release 是由 `_objc_rootReleaseWasZero()` SPI 执行的，则返回 `false` 表示调用者不应启动释放，因为该对象已在释放中。`NSObject` 和 ARC 入口点在其他情况下不使用此返回值。

最后，我们来看实际的递减操作。

`runtime/objc-object.h` 第 [791-797](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L791-L797) 行

```
  // don't check newisa.fast_rr; we already called any RR overrides
  uintptr_t carry;
  newisa.bits = subc(newisa.bits, RC_ONE, 0, &carry);  // extra_rc--
  if (slowpath(carry)) {
    // don't ClearExclusive()
    goto underflow;
  }
```

回想一下，非指针 `isa` 是一个位域（bit field），具有[三种变体](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa-variants)。`RC_ONE` 的值是当将位域视为整数时，表示引用计数为一的那个位。引用计数存储在 `isa` 的最高有效位中，因此如果所有引用计数的位都为零，就会发生下溢（underflow）或进位（carry）（将在下一小节讨论）。否则，如果没有发生下溢，`newisa` 包含递减后的引用计数，并准备写回给对象实例。

`runtime/objc-object.h` 第 [798](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L798) 行

```
} while (slowpath(!StoreReleaseExclusive(&isa().bits, &oldisa.bits, newisa.bits)));
```

如果 `&isa()` 处的值与 `&oldisa` 处的值匹配，则比较并交换操作成功，并将 `newisa` 的值写入 `&isa()`，循环结束。

否则，自该线程将值加载到 `oldisa` 后，`&isa()` 处的值已发生变化。比较并交换操作失败，并将 `&isa()` 处的新值写入 `&oldisa`。循环继续，直到该线程赢得一次比较并交换操作，或者另一个线程将对象状态更改为激活了上述某个返回路径。

循环结束后，运行时检查引用计数是否为零。如果为零，则[释放](#deallocate)该对象实例。

`runtime/objc-object.h` 第 [800-801](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L800-L801) 行

```
  if (slowpath(newisa.isDeallocating()))
    goto deallocate;
```

否则，对象具有正引用计数。如有必要，运行时将释放 side table 锁。函数以返回 `false` 结束，向 `_objc_rootReleaseWasZero()` SPI 指示该对象不应被释放。

`runtime/objc-object.h` 第 [803-808](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L803-L808) 行

```
  if (variant == RRVariant::Full) {
    if (slowpath(sideTableLocked)) sidetable_unlock();
  } else {
    ASSERT(!sideTableLocked);
  }
  return false;
```

### 完全变体（The Full Variant）

如果引用计数在非指针 `isa` 的位中下溢，则运行时撤销对 `newisa` 的更改。然后，它检查是否有任何先前溢出的引用计数存入了 side table。

`runtime/objc-object.h` 第 [810-816](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L810-L816) 行

```
underflow:
// newisa.extra_rc-- underflowed: borrow from side table or deallocate
newisa = oldisa; // abandon newisa to undo the decrement

if (slowpath(newisa.has_sidetable_rc)) {
```

如果没有引用计数溢出到 side table，则说明没有剩余的引用计数，因此 release 会[释放](#deallocate)该对象实例，尽管我认为这在实践中不会发生，因为它意味着过度释放（over-release）。要么 side table 中有引用计数，要么引用计数已达到零并由上述代码路径释放了该对象实例。在我看来，如果运行时在这种情况下触发陷阱（trap）会更干净，因为当 `-dealloc` 被第二次调用时，进程很可能会崩溃。

如果确实有引用计数先前溢出到了 side table，则运行时检查此函数调用是否具有 `Fast` 或 `FastOrMsgSend` 变体。如果是，则它停止尝试 release 操作，并将工作转交给 `rootRelease_underflow()`。

`runtime/objc-object.h` 第 [817-820](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L817-L820) 行

```
  if (variant != RRVariant::Full) {
    ClearExclusive(&isa().bits);
    return rootRelease_underflow(performDealloc);
  }
```

该函数立即以 `Full` 变体回调到 `objc_object::rootRelease(bool, RRVariant)` 中。

`runtime/NSObject.mm` 第 [1379-1383](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1379-L1383) 行

```
NEVER_INLINE uintptr_t objc_object::rootRelease_underflow(bool performDealloc) {
  return rootRelease(performDealloc, RRVariant::Full);
}
```

我在[上一篇关于 retain 的文章](https://alwaysprocessing.blog/2023/07/22/objc-retain#the-full-variant)中推测，此函数的目的是在堆栈回溯（stack trace）中提供一个帧，以帮助 Apple 工程师排查运行时中的 release 崩溃，因为 side table 锁定（使用不可重入的自旋锁（spin lock））的相互作用可能难以分析。

如果使用 `Full` 变体进行引用计数递减时发生下溢，则运行时获取一个 side table 锁。

`runtime/objc-object.h` 第 [822-832](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L822-L832) 行

```
  // Transfer retain count from side table to inline storage.
  if (!sideTableLocked) {
    ClearExclusive(&isa().bits);
    sidetable_lock();
    sideTableLocked = true;
    // Need to start over to avoid a race against the nonpointer -> raw pointer transition.
    oldisa = LoadExclusive(&isa().bits);
    goto retry;
  }
```

获取 side table 锁可能会导致线程挂起，因此运行时首先移除其对 `isa` 地址的独占监视（exclusive monitor），这是正确使用独占监视所必需的。来自 [ARM 架构参考手册](https://developer.arm.com/documentation/ddi0406/c/Application-Level-Architecture/Application-Level-Memory-Model/Synchronization-and-semaphores/Load-Exclusive-and-Store-Exclusive-usage-restrictions)（强调为原文所加）：

> 独占操作支持每个处理器线程执行一个未完成的独占访问。……如果 `STREX`（store exclusive）的目标地址与同一线程中前一个 `LDREX`（load exclusive）的地址不同，则行为可能不可预测。因此，仅当 `LDREX`/`STREX` 对使用相同地址执行时，才能依赖其最终成功。**如果上下文切换可能改变执行线程，则必须执行 `CLREX` 指令以避免不良影响……**

获取 side table 锁后，运行时重新加载 `isa` 值并再次启动[比较并交换循环](#compare-and-swap-loop)以执行递减。必须重新加载 `isa`，因为在此线程等待获取 side table 锁时，另一个线程可能已经更改了 `isa`。

最后，如果递减再次导致下溢，则运行时可安全地从 side table 加载任何额外的引用计数。

`runtime/objc-object.h` 第 [834-835](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L834-L835) 行

```
  // Try to remove some retain counts from the side table.
  auto borrow = sidetable_subExtraRC_nolock(RC_HALF);
```

[`sidetable_subExtraRC_nolock()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1500-L1528) 返回一个 [`SidetableBorrow`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-private.h#L213-L214) 结构体（这里 borrow 指的是在减法运算中取高位数字的值，而不是从 side table 租借值），它有两个字段：

- `borrowed`：从 side table 中取出的引用计数数量。
- `remaining`：side table 中剩余的引用计数数量。

运行时首先检查是否所有引用计数都已从 side table 中移除，以便稍后执行额外的簿记（bookkeeping）。然后，它检查 side table 是否返回了任何引用计数。如果 side table 为空，则没有剩余引用计数，因此 release 将[释放](#deallocate)该对象实例。

`runtime/objc-object.h` 第 [837-839](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L837-L839) 行

```
  bool emptySideTable = borrow.remaining == 0; // we'll clear the side table if no refcounts remain there

  if (borrow.borrowed > 0) {
```

如果 side table 为该对象实例返回了引用计数，则运行时尝试用从 side table 取出的引用计数更新非指针 `isa`。

`runtime/objc-object.h` 第 [840-846](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L840-L846) 行

```
    // Side table retain count decreased.
    // Try to add them to the inline count.
    bool didTransitionToDeallocating = false;
    newisa.extra_rc = borrow.borrowed - 1;  // redo the original decrement too
    newisa.has_sidetable_rc = !emptySideTable;

    bool stored = StoreReleaseExclusive(&isa().bits, &oldisa.bits, newisa.bits);
```

`borrow.borrowed` 字段包含从 side table 取出的引用计数。运行时从中减一（回想一下，这是下溢的代码路径，因此 release 的记账尚未发生），并将该值存储在非指针 `isa` 的 `extra_rc` 字段中。然后，它更新 `has_sidetable_rc` 位，以反映该对象实例在 side table 中是否仍有溢出的引用计数。

接着，它尝试存储新的 `isa` 值。存储可能会失败，这由下一个代码块处理。

`runtime/objc-object.h` 第 [848-863](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L848-L863) 行

```
    if (!stored && oldisa.nonpointer) {
      // Inline update failed.
      // Try it again right now. This prevents livelock on LL/SC architectures
      // where the side table access itself may have dropped the reservation.
      uintptr_t overflow;
      newisa.bits = addc(oldisa.bits, RC_ONE * (borrow.borrowed-1), 0, &overflow);
      newisa.has_sidetable_rc = !emptySideTable;
      if (!overflow) {
        stored = StoreReleaseExclusive(&isa().bits, &oldisa.bits, newisa.bits);
        if (stored) {
          didTransitionToDeallocating = newisa.isDeallocating();
        }
      }
    }
  }
```

如果将从 side table 取出的引用计数放入非指针 `isa` 失败，运行时立即再次尝试。运行时的 [`StoreReleaseExclusive()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L199-L208) 函数在 store exclusive 失败时执行 load exclusive 操作，因此 `oldisa` 是最新值。在为此 release 操作减去一之后，它加上从 side table 取出的引用计数，更新跟踪该对象实例在 side table 中是否具有引用计数的位，然后再次尝试存储更新后的 `isa`。这次重试很可能少于 32 条指令（符合 ARM 的建议；见下面的附注），并且比一般路径更有可能成功。

如果存储成功，运行时在引用计数达到零时将 `didTransitionToDeallocating` 设置为 `true`。但这在实践中永远不会发生，因为向非指针 `isa` 添加 `RC_HALF - 1` 个引用计数刚刚成功了。

如果重试未成功（例如，添加 `RC_HALF - 1` 个引用计数溢出），运行时通过清除独占监视器来中止此事务，将引用计数放回 side table，并在跳回比较并交换循环开始之前重新加载非指针 `isa`。不过，它仍然持有 side table 锁。

`runtime/objc-object.h` 第 [865-872](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L865-L872) 行

```
  if (!stored) {
      // Inline update failed. Put the retains back in the side table.
      ClearExclusive(&isa().bits);
      sidetable_addExtraRC_nolock(borrow.borrowed);
      oldisa = LoadExclusive(&isa().bits);
      goto retry;
  }
```

如果两个存储尝试中有一个成功，并且 side table 没有该对象实例的任何其他引用计数，则运行时从 side table 中移除该对象实例的条目。

`runtime/objc-object.h` 第 [874-876](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L874-L876) 行

```
  // Decrement successful after borrowing from side table.
  if (emptySideTable)
      sidetable_clearExtraRC_nolock();
```

最后，如有必要，运行时释放其 side table 锁并返回 false，以指示引用计数未达到零（此值仅由 `_objc_rootReleaseWasZero()` SPI 使用）。引用计数在此路径上不可能达到零（见上文），因此 release 操作在成功更新 side table 后在此结束。

`runtime/objc-object.h` 第 [878-882](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L878-L882) 行

```
  if (!didTransitionToDeallocating) {
    if (slowpath(sideTableLocked)) sidetable_unlock();
    return false;
  }
}
```

否则，执行继续到释放逻辑。

### 释放（Deallocate）

如果引用计数达到零（或发生下溢且该对象实例未在 side table 中存储引用计数），则运行时释放^[[5](#_footnotedef_5)]该对象。

`runtime/objc-object.h` 第 [888-901](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L888-L901) 行

```
deallocate:
// Really deallocate.
ASSERT(newisa.isDeallocating());
ASSERT(isa().isDeallocating());

if (slowpath(sideTableLocked)) sidetable_unlock();

__c11_atomic_thread_fence(__ATOMIC_ACQUIRE);

if (performDealloc) {
  ((void(*)(objc_object *, SEL))objc_msgSend)(this, @selector(dealloc));
}
return true;
```

首先，如果有必要，运行时释放 side table 锁。

接下来，它有一个 `acquire` 内存屏障（fence）。我假设这是[原子屏障同步（atomic-fence synchronization）](https://en.cppreference.com/w/cpp/atomic/atomic_thread_fence#Atomic-fence_synchronization)，但我不清楚此屏障与哪个 `release` 操作同步。屏障之后唯一可能有争议的读取是下面几行消息发送中对 `isa` 的读取，但此线程刚刚设置了 `isa`。

我期望来自另一个线程对 `isa` 的写入是未定义行为，因为引用计数为零。然而，这样的写入可能会改变类，由于屏障的存在，此线程可以看到这一点。因此，据我所知，屏障的唯一潜在影响是在非常罕见和奇怪的情况下对消息发送的影响。

此屏障可能是来自先前实现的一个遗留物，已不再相关；也可能是在发布前夕为“修复”内存排序问题而做的最后一刻更改；又或者是一个不必要的添加；或者是我误解了其行为。

然后，最后，如果 release 不是通过 `_objc_rootReleaseWasZero()` SPI 发生的，则会向该对象发送一个 `-dealloc` 消息。

release 操作以返回 `true` 结束，表示引用计数已达到零，除了 `_objc_rootReleaseWasZero()` SPI 外，所有调用者都会忽略此返回值。

# 结语

当我决定将 retain 和 release 分开介绍时，我以为关于 release 的文章会比 retain 短得多，但它反而长了 20%！

当引用计数溢出时，运行时将一半计数保留在非指针 `isa` 中，然后将一半添加到 side table。它可以快速执行对非指针 `isa` 的关键写入，然后跟进对 side table 的昂贵写入。相比之下，当引用计数下溢时，运行时必须从 side table 中取出引用计数，以获取执行对非指针 `isa` 的关键写入所需的信息。在独占加载和存储之间的昂贵读取增加了存储可能失败的概率，这创建了一个 release 操作必须处理的独特极端情况。写作是学习的好方法。

吸取了这个教训，我祈祷下一篇关于 autorelease（自动释放）的文章会更简单直接！

---

[1](#_footnoteref_1). 如果 release 导致引用计数为零，则该 SPI 返回 `true`，使实现根类的系统框架能够在释放根类实例之前执行清理工作。Safari 10.1（约 2017 年 3 月）[增加了对此 SPI 的使用](https://github.com/WebKit/WebKit/blob/Safari-603.1.30/Source/WebKit2/Shared/Cocoa/WKObject.mm#L206-L213)，不过该更改后来在 [Safari 11.1 中被还原](https://github.com/WebKit/WebKit/commit/4b5bca14adf3033809dd7a0a8a7ba634646cf7ea)。

[2](#_footnoteref_2). 关于 retain 的文章中的 [rootRetain 部分](https://alwaysprocessing.blog/2023/07/22/objc-retain#rootretain)简要讨论了运行时的 `LoadExclusive` 函数。

[3](#_footnoteref_3). 关于 retain 的文章中的 [rootRetain 部分](https://alwaysprocessing.blog/2023/07/22/objc-retain#rootretain)详细讨论了消息发送逻辑及其对 Objective-C 运行时函数的使用。

[4](#_footnoteref_4). 未来的文章将讨论引用计数 side table 的实现。

[5](#_footnoteref_5). 未来的文章将更详细地讨论对象释放。
