---
title: 'Objective-C Internals: Retain Objective-C memory is managed through a reference counting scheme, which has evolved from a relatively simple API into a sophisticated, highly-optimized implementation wh'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/07/22/objc-retain'
original_language: en
published: 2023-07-22
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f04a4c2a6197e049'
translated: false
---

> 原文：[Objective-C Internals: Retain Objective-C memory is managed through a reference counting scheme, which has evolved from a relatively simple API into a sophisticated, highly-optimized implementation wh](https://alwaysprocessing.blog/2023/07/22/objc-retain)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Retain

![Two people connecting computing devices with wires. Does this establish an object ownership graph?](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c7eb8f6e-a4d2-4d14-9dec-278d8e82e500/public)

Objective-C memory is managed through a reference counting scheme, which has evolved from a relatively simple API into a sophisticated, highly-optimized implementation while maintaining source and ABI compatibility.

## Background

OS X 10.7 and iOS 5 introduced [Automatic Reference Counting](https://clang.llvm.org/docs/AutomaticReferenceCounting.html), or ARC, to improve Objective-C programmer productivity by eliminating boilerplate code and reducing the surface area for reference counting bugs (leaks and over-releases).

Before ARC, the `-[NSObject retain]`, `-[NSObject release]`^[[1](#_footnotedef_1)], and `-[NSObject autorelease]`^[[2](#_footnotedef_2)] methods were the exclusive interface to manage object reference counts. And, until OS X 10.8 and iOS 6, the `NSObject` implementation was part of Foundation, not the Objective-C runtime.

The designers of ARC identified a key requirement to improve the likelihood of the feature’s success, learning from Apple’s ill-fated attempt to add garbage collection to Objective-C: Automatic Reference Counting must transparently interoperate with manual reference counting in the same process without requiring recompilation of existing code (e.g., a third-party binary-only library).

In the early days of macOS, it wasn’t unheard of for some objects to override the reference counting methods^[[3](#_footnotedef_3)] to use their own implementation, often for performance reasons. ARC had to support transparent interoperability with these custom reference counting implementations to deliver on the aforementioned requirement.

## Entry Points

There are two interfaces for reference counting operations: the long-standing `NSObject` API and a compiler-private API used by ARC, both of which call into a core implementation. The following two subsections will examine each interface’s retain implementation, and the next section will discuss the core implementation.

### NSObject

The `-[NSObject retain]` implementation^[[4](#_footnotedef_4)] is trivial—it simply calls `_objc_rootRetain` to retain `self`.

`runtime/NSObject.mm` lines [2502-2504](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L2502-L2504)

```
- (id)retain {
  return _objc_rootRetain(self);
}
```

The term _root_ indicates the root class in the object’s [class hierarchy](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#architecture-diagram) received the `-retain` message. Therefore, the class does not override `-retain` or the override calls the superclass method, so the retain operation is guaranteed to use the runtime’s implementation. (As we’ll see in the following section, not all entry points have this guarantee.)

Next, the `_objc_rootRetain` function, which is also trivial, calls `objc_object::rootRetain()`.

`runtime/NSObject.mm` lines [1875-1881](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1875-L1881)

```
id _objc_rootRetain(id obj) {
  ASSERT(obj);
  return obj->rootRetain();
}
```

Finally, `objc_object::rootRetain()` calls an overload of `rootRetain`.

`runtime/objc-object.h` lines [607-611](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L607-L611)

```
id objc_object::rootRetain() {
  return rootRetain(false, RRVariant::Fast);
}
```

The overload called here is the core implementation, which has two parameters:

1. `tryRetain` enables support to load weak references^[[5](#_footnotedef_5)]. The argument is `false` because a weak reference cannot exercise this code path. (The runtime must first load an object from a weak reference before the object can receive a message, and, by definition, the object reference obtained through the load operation is strong.)
2. `variant` provides context about the call path, enabling the core implementation to elide unnecessary work. Retains performed through `NSObject` use `RRVariant::Fast` to skip the check for whether the class has a custom reference counting implementation because performing the operation through the _root_ class is, by definition, not custom.

### Automatic Reference Counting

When ARC is enabled, the compiler performs reference counting operations through a compiler-private API added for ARC as a performance optimization. The API allows reference counting operations to call directly into the Objective-C runtime and skip the overhead of sending a message.

`runtime/NSObject.mm` lines [1772-1777](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1772-L1777)

```
id objc_retain(id obj) {
  if (_objc_isTaggedPointerOrNil(obj)) return obj;
  return obj->retain();
}
```

The function first checks the object pointer value and returns immediately if it does not reference an object on the heap, which may occur in two cases:

1. The pointer `nil`. Sending a message to `nil` is legal, so this optimization of `-[NSObject retain]` must also support `nil` pointers.
2. The pointer is a [tagged pointer](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr). A tagged pointer is an implementation detail of the Objective-C runtime not visible to the compiler, so the compiler can not eliminate the retain operation. Tagged pointers do not participate in reference counting (there is no heap allocation to track), so there’s no need to proceed.

If the object pointer value references an object on the heap, the function calls `objc_object::retain()` to perform the retain operation.

`runtime/objc-object.h` lines [589-596](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L589-L596)

```
inline id objc_object::retain() {
  ASSERT(!isTaggedPointer());
  return rootRetain(false, RRVariant::FastOrMsgSend);
}
```

This function calls the core implementation (though _root_ in `rootRetain` is a misnomer at this point) with:

- `false` for `tryRetain`, for the same reason discussed above in the [NSObject](#nsobject) entry point.
- `RRVariant::FastOrMsgSend` for `variant`. No introspection, whether direct (see [rootRetain](#rootretain) below) or indirect (via a message send, see [NSObject](#nsobject) above), has occurred, so it’s not yet known whether the object’s class overrides any of the reference counting methods (hence the function’s name does **not** contain the term _root_).

  The `MsgSend` part of the `variant` instructs the core implementation to do the introspection necessary to determine whether the object’s class overrides the reference counting methods. If it does, the core implementation performs the retain operation by sending the object a `-retain` message (which may re-enter the runtime via [`-[NSObject retain]`](#nsobject)).

## rootRetain

The [`objc_object::rootRetain(bool, RRVariant)`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L619-L706) function is on the larger side, so we’ll analyze it piece by piece.

`runtime/objc-object.h` line [622](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L622)

```
if (slowpath(isTaggedPointer())) return (id)this;
```

Although the ARC entry point checks for a tagged pointer, the `NSObject` entry point does not. It’s not immediately apparent to me why the `NSObject` implementation doesn’t perform this check, but it has to happen somewhere, and in this version of the runtime, it’s here.

Next, the runtime loads the object’s `isa` value.

`runtime/objc-object.h` lines [624-630](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L624-L630)

```
bool sideTableLocked = false;
bool transcribeToSideTable = false;
isa_t oldisa = LoadExclusive(&isa().bits);
isa_t newisa;
```

The `isa` stores the object’s [retain count](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#extra_rc) on all modern Apple platforms. The Objective-C runtime uses ARM’s [exclusive monitor](https://developer.arm.com/documentation/dht0008/a/arm-synchronization-primitives/exclusive-accesses/exclusive-monitors) synchronization primitive to manage concurrency on the [`arm64` architecture](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L180-L215), which is where the `LoadExclusive` function gets its name. On [all other architectures](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L219-L245), including `arm64e`, the Objective-C runtime uses [C11 atomics](https://en.cppreference.com/w/c/atomic). (I’m unsure whether `arm64` or `arm64e` is the outlier case here or why.)

If the compiler-private API was the entry point for the retain operation, the runtime must check whether the class overrides any of the reference counting methods.

`runtime/objc-object.h` lines [632-642](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L632-L642)

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

Custom referencing counting implementations are rare, so the runtime uses its [`slowpath()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L163) macro to hint to the CPU’s branch prediction unit this path is unlikely to run. `getDecodedClass()` returns the object’s [`Class` object](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl), which has a [flag](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-runtime-new.h#L1937-L1939) indicating whether the class overrides any reference counting methods. This quick check provides the necessary class introspection for the ARC entry point to support custom reference counting implementations with minimal overhead.

If a class has a custom reference counting implementation, the runtime sends the object a `-retain` message to fulfill the ARC-initiated retain operation. Note the object may then call `-[NSObject retain]`, but this code block will not execute again as the `variant` will be `RRVariant::Fast`.

Pure Swift classes (i.e., classes not derived from `NSObject`) derive from the [`SwiftObject` class](https://github.com/apple/swift/blob/swift-5.8.1-RELEASE/stdlib/public/runtime/SwiftObject.h#L41-L78) (only on Apple platforms) for Objective-C compatibility. Swift uses its own reference counting system, so `SwiftObject` [implements](https://github.com/apple/swift/blob/swift-5.8.1-RELEASE/stdlib/public/runtime/SwiftObject.mm#L270) the [reference counting methods](https://github.com/apple/swift/blob/e495eed8914a87aa3403411fbc2cf3f9e6119846/include/swift/Runtime/HeapObject.h#L1108-L1146) to support bridging pure Swift objects to Objective-C. As an optimization for this case, the Objective-C runtime calls the Swift runtime’s `swift_retain()` function directly^[[6](#_footnotedef_6)] (vs. retaining the object via a message send).

Continuing to the next block.

`runtime/objc-object.h` lines [644-651](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L644-L651)

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

`Class` objects are never deallocated and do not require reference counting. So, if the object is a class object, the function returns it without performing any further work.

### Compare and Swap Loop

The [compare-and-swap](https://en.wikipedia.org/wiki/Compare-and-swap) loop is the heart of the retain implementation. It starts by (re-)initializing the loop’s start state.

`runtime/objc-object.h` lines [654-655](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L654-L655)

```
do {
  transcribeToSideTable = false;
  newisa = oldisa;
```

It sets `newisa` to the current `isa` value (i.e., `oldisa`), which the loop will update to reflect the incremented retain count. The following subsection will look at the use of `transcribeToSideTable`.

`runtime/objc-object.h` lines [656-660](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L656-L660)

```
  if (slowpath(!newisa.nonpointer)) {
    ClearExclusive(&isa().bits);
    if (tryRetain) return sidetable_tryRetain() ? (id)this : nil;
    else return sidetable_retain(sideTableLocked);
  }
```

First, the loop checks if the object instance has a [non-pointer `isa`](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa). If it does not, the retain count is recorded in a side table^[[7](#_footnotedef_7)]. This check is performed in the loop because if this thread loses a compare-and-swap, it could be due to another thread mutating the object in a way that removed its use of a non-pointer `isa`.

Next, the loop checks to see if it lost another race.

`runtime/objc-object.h` lines [661-673](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L661-L673)

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

An object may be deallocating while a thread is attempting to retain it in (at least) three scenarios:

1. `tryRetain` is `true`, and this thread lost the race to load the weak object before it started deallocation. The function returns `nil`, indicating it could not obtain a strong reference. In this scenario, the caller, `objc_loadWeakRetained()`, holds a lock to the weak reference side table, preventing the object from being freed, so the read of the `isa` from the object pointer is defined behavior.
2. Another thread released the object, causing it to deallocate, usually due to a race condition that occurs when a process concurrently reads from and writes to a `strong`, `nonatomic` property. Everything about this scenario is undefined behavior. The function returns `self` to fulfill the `-retain` contract, but it will become a [dangling pointer](https://en.wikipedia.org/wiki/Dangling_pointer), almost certainly resulting in a crash in the thread’s near future. Hitting this code path in a race condition is "lucky." In practice, the `isa` bits read through the dangling pointer could have sent this function in any number of directions resulting in unpredictable effects.
3. Logic in `-dealloc` causes a retain to be performed (e.g., the `-dealloc` implementation passes `self` to a clean-up routine where the ARC compiler emits a retain/release pair). This scenario is **not** a race condition like the two cases above because the retain occurred on the same thread executing the deallocation. However, this scenario can lead to undefined behavior if the function performing the retain requires the object instance to survive its call scope (e.g., storing `self` in a `strong` property of another object) because the pointer will become danging when deallocation completes.

Finally, we get to the actual increment.

`runtime/objc-object.h` lines [674-675](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L674-L675)

```
  uintptr_t carry;
  newisa.bits = addc(newisa.bits, RC_ONE, 0, &carry);  // extra_rc++
```

Recall the non-pointer `isa` is a bit field with [three variants](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa-variants). The value of `RC_ONE` is the bit that represents a retain count of one when viewing the bit field as an integer. The retain count is stored in the most significant bits of the `isa`, so an overflow, or carry, will occur if all of the retain count bits are in use (discussed in the following subsection). `newisa` contains the incremented retain count if no overflow occurs and is ready to be written back to the object instance.

`runtime/objc-object.h` line [691](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L691)

```
} while (slowpath(!StoreExclusive(&isa().bits, &oldisa.bits, newisa.bits)));
```

If the value at `&isa()` matches the value at `&oldisa`, the compare-and-swap operation succeeds and writes the value of `newisa` to `&isa()`, and the loop ends.

Otherwise, the value of `&isa()` has changed since this thread loaded it into `oldisa`. The compare-and-swap operation fails and writes the new value at `&isa()` to `&oldisa`. The loop continues until the thread wins a compare-and-swap operation or another thread changes the object state to activate one of the above return paths.

### The Full Variant

If the retain count overflows the bits in the non-pointer `isa`, the runtime will use a side table to store part of the retain count.

`runtime/objc-object.h` lines [677-690](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L677-L690)

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

If this function invocation uses the `Fast` or `FastOrMsgSend` variant, it stops its attempt of the retain operation and passes the buck to `rootRetain_overflow()`.

`runtime/objc-object.h` lines [1372-1376](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1372-L1376)

```
NEVER_INLINE id objc_object::rootRetain_overflow(bool tryRetain) {
  return rootRetain(tryRetain, RRVariant::Full);
}
```

I assume the purpose of this function is to provide a frame in stack traces to help Apple engineers troubleshoot retain crashes in the runtime, as the interplay of side table locking (which uses a non-reentrant spin lock) can be challenging to reason about.

If the retain count overflows in `rootRetain` with the `Full` variant, the implementation sends half of the retain count value to a side table and keeps the other half in the non-pointer `isa`. The retain count is divided in half to minimize the number of side table accesses (requiring fewer CPU instructions and fewer lock acquisitions). If the implementation sent only the overflow bits to the side table, reference counting operations at the overflow boundary value could become a performance drag on the system.

`runtime/objc-object.h` lines [693-700](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L693-L700)

```
  if (variant == RRVariant::Full) {
    if (slowpath(transcribeToSideTable)) {
      // Copy the other half of the retain counts to the side table.
      sidetable_addExtraRC_nolock(RC_HALF);
    }
    if (slowpath(!tryRetain && sideTableLocked)) sidetable_unlock();
  }
```

The side table is updated after the compare-and-swap succeeds because another thread may win the race in moving the overflow retain count to the side table. The compare-and-swap loop acquires a lock to the side table, which prevents a race condition if another thread also attempts to read from or write to the side table.

### Return self

After the compare-and-swap succeeds and, if necessary, the side table is updated, the retain operation is complete.

`runtime/objc-object.h` line [693-700](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L693-L700)

```
return (id)this;
```

The last step is to return `self`^[[8](#_footnotedef_8)] to fulfill the [`-[NSObject retain`](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1571946-retain) contract]:

> As a convenience, `retain` returns `self` because it may be used in nested expressions.

Retain has evolved into a highly optimized operation since the first release of Mac OS X over 20 years ago. The same is true for release, autorelease, and dealloc, which we’ll see soon.

---

[1](#_footnoteref_1). This post is long, so I decided to discuss release in the [next post](https://alwaysprocessing.blog/2023/10/01/objc-release).

[2](#_footnoteref_2). Autorelease is a purely additive feature built on release. I’ll discuss its implementation in a future post, given it’s not part of the core retain/release operations.

[3](#_footnoteref_3). The Objective-C runtime considers the `retain`, `release`, `autorelease`, `_tryRetain`, `_isDeallocating`, `retainCount`, `allowsWeakReference`, and `retainWeakReference` selectors to be part of the [reference counting method family](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-runtime-new.mm#L1073-L1080). If a class overrides any of these methods, the Objective-C runtime classifies the class as having a custom reference counting implementation.

[4](#_footnoteref_4). The implementation of `NSObject` moved into the Objective-C runtime in OS X 10.8 and iOS 6 to support the introduction of `os_object`, which enabled GCD and XPC types to participate in ARC and to work with Foundation collections. Before this move, its implementation in Foundation was likely the same.

[5](#_footnoteref_5). Exploring the implementation of weak references is on the backlog of upcoming posts.

[6](#_footnoteref_6). The Swift runtime depends on the Objective-C runtime, creating a reverse dependency. The Objective-C runtime resolves this by [dynamically loading](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L95-L119) the `swift_retain` symbol from `libswiftCore.dylib`.

[7](#_footnoteref_7). A future post will discuss the implementation of the retain count side table.

[8](#_footnoteref_8). Apple started using Objective-C++ to implement the Objective-C runtime in OS X 10.7 and iOS 5, but it wasn’t until OS X 10.9 and iOS 7 that Apple used Objective-C++ to implement the object type itself. A future post will explore this approach and show how `this` and `self` are the same.
