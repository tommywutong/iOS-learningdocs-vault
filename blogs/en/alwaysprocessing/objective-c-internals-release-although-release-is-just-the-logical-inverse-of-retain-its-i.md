---
title: 'Objective-C Internals: Release Although release is "just" the logical inverse of retain, its implementation is much more complex, primarily due to the ARM synchronization model. This post explores the'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/10/01/objc-release'
original_language: en
published: 2023-10-01
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9f86ed9ae4033707'
translated: false
---

> 原文：[Objective-C Internals: Release Although release is "just" the logical inverse of retain, its implementation is much more complex, primarily due to the ARM synchronization model. This post explores the](https://alwaysprocessing.blog/2023/10/01/objc-release)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Release

![Two people tugging on a line. Who will release it first?](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/739048ac-8a94-451e-418a-6042a3a1ed00/public)

Although release is "just" the logical inverse of retain, its implementation is much more complex, primarily due to the ARM synchronization model. This post explores the unique aspects of the release implementation (relative to retain), focusing on the memory ordering requirements on ARM.

Objective-C manages memory using a [reference counting](https://en.wikipedia.org/wiki/Reference_counting) approach. This post will look at the release operation, which removes a reference count from an object instance. The [previous post](https://alwaysprocessing.blog/2023/07/22/objc-retain) covered the retain implementation, which adds a reference count to an object instance. The retain and release implementations are similar because they are inverse operations. I’ll refer back to the [retain post](https://alwaysprocessing.blog/2023/07/22/objc-retain), where the discussion is similar, so this post can focus on the unique aspects of retain.

## Entry Points

There are two interfaces for reference counting operations: the long-standing `NSObject` API and a compiler-private API used by ARC, both of which call into a core implementation. The following two subsections will examine each interface’s release implementation, and the next section will discuss the core implementation.

### NSObject

Like [`-[NSObject retain]`](https://alwaysprocessing.blog/2023/07/22/objc-retain#nsobject), `-[NSObject release]` is trivial—it simply calls `_objc_rootRelease()` to release `self`.

`runtime/NSObject.mm` lines [2544-2546](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L2544-L2546)

```
- (void)release {
  _objc_rootRelease(self);
}
```

The term _root_, as discussed in the [retain post](https://alwaysprocessing.blog/2023/07/22/objc-retain#nsobject), indicates the operation is occurring via a `-release` message received by the root class in the object’s [class hierarchy](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#architecture-diagram).

Next, the `_objc_rootRelease` function, which is also trivial, calls `objc_object::rootRelease()`.

`runtime/NSObject.mm` lines [1883-1889](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1883-L1889)

```
void _objc_rootRelease(id obj) {
  ASSERT(obj);
  obj->rootRelease();
}
```

Finally, `objc_object::rootRelease()` calls an overload of `rootRelease`.

`runtime/objc-object.h` lines [729-733](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L729-L733)

```
bool objc_object::rootRelease() {
  return rootRelease(true, RRVariant::Fast);
}
```

The overload called here is the core implementation, which has two parameters:

1. `performDealloc` specifies whether the release operation should deallocate the object instance if the retain count reaches zero. The runtime always passes `true` for this parameter unless the [`_objc_rootReleaseWasZero()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1850-L1856) SPI[[1](#_footnotedef_1)] (_system programming interface_ for first-party use, as opposed to _application programming interface_ for third-party use) is performing the release.
2. `variant` provides context about the call path, enabling the core implementation to elide unnecessary work. Releases performed through `NSObject` use `RRVariant::Fast` to skip the check for whether the class has a custom reference counting implementation because the operation occurring through the root class is, by definition, not custom.

### Automatic Reference Counting

When ARC is enabled, the compiler performs reference counting operations through a compiler-private API added for ARC as a performance optimization (also discussed in the [retain post](https://alwaysprocessing.blog/2023/07/22/objc-retain#automatic-reference-counting)).

`runtime/NSObject.mm` lines [1780-1786](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1780-L1786)

```
void objc_release(id obj) {
  if (_objc_isTaggedPointerOrNil(obj)) return;
  return obj->release();
}
```

If the object pointer value references an object on the heap, derived through the same ceremony as [retain](https://alwaysprocessing.blog/2023/07/22/objc-retain#automatic-reference-counting), the function calls `objc_object::release()` to perform the release operation.

`runtime/objc-object.h` lines [709-716](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L709-L716)

```
inline void objc_object::release() {
  ASSERT(!isTaggedPointer());
  rootRelease(true, RRVariant::FastOrMsgSend);
}
```

This function calls the core implementation (though _root_ in `rootRelease` is a misnomer at this point) with:

- `true` for `performDealloc`, for the same reason discussed above in the [NSObject](#nsobject) entry point.
- `RRVariant::FastOrMsgSend` for `variant`. No introspection, whether direct (see [rootRelease](#rootrelease) below) or indirect (via a message send, see [NSObject](#nsobject) above), has occurred, so it’s not yet known whether the object’s class overrides any of the reference counting methods (hence the function’s name does **not** contain the term _root_).

  The `MsgSend` part of the `variant` instructs the core implementation to do the introspection necessary to determine whether the object’s class overrides the reference counting methods. If it does, the core implementation performs the release operation by sending the object a `-release` message (which may re-enter the runtime via [`-[NSObject release]`](#nsobject)).

## rootRelease

The [`objc_object::rootRelease(bool, RRVariant)`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L741-L902) function is on the larger side, so we’ll analyze it piece by piece.

`runtime/objc-object.h` line [744](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L744)

```
if (slowpath(isTaggedPointer())) return (id)this;
```

Although the ARC entry point checks for a tagged pointer, the `NSObject` entry point does not. It’s not immediately apparent to me why the `NSObject` implementation doesn’t perform this check, but it has to happen somewhere, and in this version of the runtime, it’s here.

Next, the runtime loads the object’s `isa` value[[2](#_footnotedef_2)].

`runtime/objc-object.h` lines [746-750](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L746-L750)

```
bool sideTableLocked = false;
isa_t newisa, oldisa;
oldisa = LoadExclusive(&isa().bits);
```

If the compiler-private API was the entry point for the release operation, the runtime must check whether the class overrides any reference counting methods[[3](#_footnotedef_3)].

`runtime/objc-object.h` lines [752-764](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L752-L764)

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

If a class has a custom reference counting implementation, the runtime sends the object a `-release` message to fulfill the ARC-initiated release operation. Note the object may then call `-[NSObject release]`, but this code block will not execute again as the `variant` will be `RRVariant::Fast`.

Continuing to the next block.

`runtime/objc-object.h` lines [766-773](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L766-L773)

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

`Class` objects are never deallocated and do not require reference counting. So, if the object is a class object, the function returns it without performing any further work.

### Compare and Swap Loop

The [compare-and-swap](https://en.wikipedia.org/wiki/Compare-and-swap) loop is the heart of the release implementation. It starts, perhaps unexpectedly, with a `goto` label. [The Full Variant](#the-full-variant) subsection below discusses this function’s use of `goto`.

`runtime/objc-object.h` lines [775-777](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L775-L777)

```
retry:
do {
  newisa = oldisa;
```

The loop first sets `newisa` to the current `isa` value (i.e., `oldisa`), which the following steps will update to reflect the decremented retain count.

Then, the loop checks if the object instance has a [non-pointer `isa`](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa). If it does not, the retain count is recorded in a side table[[4](#_footnotedef_4)]. This check is performed in the loop because if this thread loses a compare-and-swap, it could be due to another thread mutating the object in a way that removed its use of a non-pointer `isa`.

`runtime/objc-object.h` lines [778-781](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L778-L781)

```
  if (slowpath(!newisa.nonpointer)) {
    ClearExclusive(&isa().bits);
    if (tryRetain) return sidetable_tryRetain() ? (id)this : nil;
    else return sidetable_retain(sideTableLocked);
  }
```

Next, the loop checks to see if it lost another race.

`runtime/objc-object.h` lines [782-788](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L782-L788)

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

An object may be deallocating while a thread is attempting to release it in (at least) two scenarios:

1. Another thread released the object, causing it to deallocate, usually due to a race condition that occurs when a process concurrently reads from and writes to a `strong`, `nonatomic` property. Everything about this scenario is undefined behavior.
2. Logic in `-dealloc` causes a release to be performed (e.g., the `-dealloc` implementation passes `self` to a clean-up routine where the ARC compiler emits a retain/release pair). This scenario is **not** a race condition like the case above because the release occurred on the same thread executing the deallocation.

If the `_objc_rootReleaseWasZero()` SPI performed the release, the return value of `false` indicates the caller should not initiate deallocation, as the object is already deallocating. The return value is otherwise unused by the `NSObject` and ARC entry points.

Finally, we get to the actual decrement.

`runtime/objc-object.h` lines [791-797](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L791-L797)

```
  // don't check newisa.fast_rr; we already called any RR overrides
  uintptr_t carry;
  newisa.bits = subc(newisa.bits, RC_ONE, 0, &carry);  // extra_rc--
  if (slowpath(carry)) {
    // don't ClearExclusive()
    goto underflow;
  }
```

Recall the non-pointer `isa` is a bit field with [three variants](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa-variants). The value of `RC_ONE` is the bit that represents a retain count of one when viewing the bit field as an integer. The retain count is stored in the most significant bits of the `isa`, so an underflow, or carry, will occur if all of the retain count bits are zero (discussed in the following subsection). Otherwise, `newisa` contains the decremented retain count if no underflow occurs and is ready to be written back to the object instance.

`runtime/objc-object.h` line [798](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L798)

```
} while (slowpath(!StoreReleaseExclusive(&isa().bits, &oldisa.bits, newisa.bits)));
```

If the value at `&isa()` matches the value at `&oldisa`, the compare-and-swap operation succeeds and writes the value of `newisa` to `&isa()`, and the loop ends.

Otherwise, the value of `&isa()` has changed since this thread loaded it into `oldisa`. The compare-and-swap operation fails and writes the new value at `&isa()` to `&oldisa`. The loop continues until the thread wins a compare-and-swap operation or another thread changes the object state to activate one of the above return paths.

After the loop ends, the runtime checks if the retain count is zero. If it is, it [deallocates](#deallocate) the object instance.

`runtime/objc-object.h` lines [800-801](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L800-L801)

```
  if (slowpath(newisa.isDeallocating()))
    goto deallocate;
```

Otherwise, the object has a positive retain count. If necessary, the runtime will release the side table lock. The function ends by returning `false`, indicating to the `_objc_rootReleaseWasZero()` SPI that the object should not deallocate.

`runtime/objc-object.h` lines [803-808](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L803-L808)

```
  if (variant == RRVariant::Full) {
    if (slowpath(sideTableLocked)) sidetable_unlock();
  } else {
    ASSERT(!sideTableLocked);
  }
  return false;
```

### The Full Variant

If the retain count underflows the bits in the non-pointer `isa`, the runtime reverts the changes to `newisa`. Then, it checks whether any retain counts previously overflowed to the side table.

`runtime/objc-object.h` lines [810-816](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L810-L816)

```
underflow:
// newisa.extra_rc-- underflowed: borrow from side table or deallocate
newisa = oldisa; // abandon newisa to undo the decrement

if (slowpath(newisa.has_sidetable_rc)) {
```

If no retain counts overflowed to the side table, no retain counts remain, so the release [deallocates](#deallocate) the object instance, though I don’t think this can happen in practice as it would imply an over-release. Either there are retain counts in the side table, or the retain count reached zero and the above code path deallocated the object instance. In my opinion, it would be cleaner if the runtime trapped in this case, as the process will likely crash when `-dealloc` gets called for a second time.

If retain counts did previously overflow to the side table, the runtime checks whether this function invocation has the `Fast` or `FastOrMsgSend` variant. If so, it stops its attempt at the release operation and passes the buck to `rootRelease_underflow()`.

`runtime/objc-object.h` lines [817-820](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L817-L820)

```
  if (variant != RRVariant::Full) {
    ClearExclusive(&isa().bits);
    return rootRelease_underflow(performDealloc);
  }
```

The function immediately calls back into `objc_object::rootRelease(bool, RRVariant)` with the `Full` variant.

`runtime/NSObject.mm` lines [1379-1383](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1379-L1383)

```
NEVER_INLINE uintptr_t objc_object::rootRelease_underflow(bool performDealloc) {
  return rootRelease(performDealloc, RRVariant::Full);
}
```

I speculated in the [retain post](https://alwaysprocessing.blog/2023/07/22/objc-retain#the-full-variant) the purpose of this function is to provide a frame in stack traces to help Apple engineers troubleshoot release crashes in the runtime, as the interplay of side table locking (which uses a non-reentrant spin lock) can be challenging to reason about.

If the release count decrement underflows with the `Full` variant, the runtime obtains a side table lock.

`runtime/objc-object.h` lines [822-832](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L822-L832)

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

Acquiring the side table lock may cause the thread to suspend, so the runtime first removes its exclusive monitor on the `isa` address, which is required to use the exclusive monitor correctly. From the [ARM Architecture Reference Manual](https://developer.arm.com/documentation/ddi0406/c/Application-Level-Architecture/Application-Level-Memory-Model/Synchronization-and-semaphores/Load-Exclusive-and-Store-Exclusive-usage-restrictions) (emphasis mine):

> The exclusives support a single outstanding exclusive access for each processor thread that is executed. … If the target address of an `STREX` _(store exclusive)_ is different from the preceding `LDREX` _(load exclusive)_ in the same thread of execution, behavior can be unpredictable. As a result, an `LDREX`/`STREX` pair can only be relied upon to eventually succeed if they are executed with the same address. **Where a context switch… might change the thread of execution, a `CLREX` instruction… must be executed to avoid unwanted effects…**

After obtaining the side table lock, the runtime reloads the `isa` value and starts the [compare-and-swap loop](#compare-and-swap-loop) again to perform the decrement. A reload of the `isa` is necessary because another thread may have changed the `isa` while this thread was waiting to acquire the side table lock.

Finally, if the decrement again results in an underflow, it’s safe for the runtime to load any additional retain counts from the side table.

`runtime/objc-object.h` lines [834-835](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L834-L835)

```
  // Try to remove some retain counts from the side table.
  auto borrow = sidetable_subExtraRC_nolock(RC_HALF);
```

[`sidetable_subExtraRC_nolock()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/NSObject.mm#L1500-L1528) returns a [`SidetableBorrow`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-private.h#L213-L214) struct (borrow in the sense of taking the value of higher digits in a subtraction operation, not as in leasing the values from the side table), which has two fields:

- `borrowed`: The number of retain counts taken from the side table.
- `remaining`: The number of retain counts remaining in the side table.

The runtime first checks whether all the retain counts have been removed from the side table to perform additional bookkeeping later. Then, it checks whether the side table returned any retain counts. If the side table is empty, no retain counts remain, so the release will [deallocate](#deallocate) the object instance.

`runtime/objc-object.h` lines [837-839](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L837-L839)

```
  bool emptySideTable = borrow.remaining == 0; // we'll clear the side table if no refcounts remain there

  if (borrow.borrowed > 0) {
```

If the side table returned retain counts for the object instance, the runtime attempts to update the non-pointer `isa` with the retain counts taken from the side table.

`runtime/objc-object.h` lines [840-846](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L840-L846)

```
    // Side table retain count decreased.
    // Try to add them to the inline count.
    bool didTransitionToDeallocating = false;
    newisa.extra_rc = borrow.borrowed - 1;  // redo the original decrement too
    newisa.has_sidetable_rc = !emptySideTable;

    bool stored = StoreReleaseExclusive(&isa().bits, &oldisa.bits, newisa.bits);
```

The `borrow.borrowed` field contains the retain counts taken from the side table. The runtime subtracts one from the count (recall this is the code path for an underflow, so the release accounting has not yet occurred) and stores the value in the non-pointer `isa`'s `extra_rc` field. It then updates the `has_sidetable_rc` bit to reflect whether the side table still has overflowed retain counts for the object instance.

It then attempts to store the new `isa` value. The store may fail, which is handled by the next code block.

`runtime/objc-object.h` lines [848-863](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L848-L863)

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

If placing the retain counts taken from the side table into the non-pointer `isa` fails, the runtime immediately tries again. The runtime’s [`StoreReleaseExclusive()`](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-os.h#L199-L208) function performs the load exclusive operation if the store exclusive fails, so `oldisa` is the most recent value. After subtracting one for this release operation, it adds the retain counts taken from the side table, updates the bit tracking if the object instance has retain counts in the side table, and then attempts to store the updated `isa` again. This retry is likely less than 32 instructions (meeting ARM’s recommendation; see aside below) and is more likely to succeed than the general path.

If the store is successful, the runtime sets `didTransitionToDeallocating` to `true` if the retain count has reached zero. But this can never happen in practice, as adding `RC_HALF - 1` retain counts to the non-pointer `isa` just succeeded.

If the retry did not succeed (e.g., adding `RC_HALF - 1` retain counts overflowed), the runtime aborts this transaction by clearing the exclusive monitor, putting the retain counts back into the side table, and reloading the non-pointer `isa` before jumping back to the start of the compare-and-swap loop. It does, however, still hold the side table lock.

`runtime/objc-object.h` lines [865-872](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L865-L872)

```
  if (!stored) {
      // Inline update failed. Put the retains back in the side table.
      ClearExclusive(&isa().bits);
      sidetable_addExtraRC_nolock(borrow.borrowed);
      oldisa = LoadExclusive(&isa().bits);
      goto retry;
  }
```

If either of the store attempts succeeds, and the side table does not have any additional retain counts for the object instance, the runtime removes the entry for the object instance from the side table.

`runtime/objc-object.h` lines [874-876](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L874-L876)

```
  // Decrement successful after borrowing from side table.
  if (emptySideTable)
      sidetable_clearExtraRC_nolock();
```

Finally, if necessary, the runtime releases its side table lock and returns false to indicate the retain count did not reach zero (which is only used by the `_objc_rootReleaseWasZero()` SPI). The retain count cannot reach zero on this path (see above), so the release operation ends here after a successful side table update.

`runtime/objc-object.h` lines [878-882](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L878-L882)

```
  if (!didTransitionToDeallocating) {
    if (slowpath(sideTableLocked)) sidetable_unlock();
    return false;
  }
}
```

Otherwise, execution continues to the deallocation logic.

### Deallocate

If the retain count reaches zero (or underflows and the object instance is not storing retain counts in a side table), the runtime deallocates[[5](#_footnotedef_5)] the object.

`runtime/objc-object.h` lines [888-901](https://github.com/apple-oss-distributions/objc4/blob/objc4-841.13/runtime/objc-object.h#L888-L901)

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

First, the runtime releases the side table lock, if necessary.

Next, it has an `acquire` fence. I presume this is a [atomic-fence synchronization](https://en.cppreference.com/w/cpp/atomic/atomic_thread_fence#Atomic-fence_synchronization), but it’s not clear to me what `release` operation this fence synchronizes with. The only potentially contentious read after the fence is of the `isa` in the message send a few lines down, but this thread just set the `isa`.

I would expect writes to the `isa` from another thread to be undefined behavior because the retain count is zero. Such a write, though, could change the class, which would be visible to this thread because of the fence. So, as far as I can tell, the fence’s only potential effect is on the message send in quite rare and bizarre circumstances.

The fence is probably an artifact from a previous implementation that is no longer relevant, a last minute change to "fix" a memory ordering problem just before a release, an unnecessary addition, or am I misunderstanding the behavior.

Then, finally, if the release didn’t occur through the `_objc_rootReleaseWasZero()` SPI, a `-dealloc` message is sent to the object.

The release operation ends by returning `true`, indicating the retain count has reached zero, which is ignored by every caller except the `_objc_rootReleaseWasZero()` SPI.

# Epilogue

When I decided to cover retain and release separately, I thought the release post would be significantly shorter than retain, but it’s 20% longer!

When the retain count overflows, the runtime keeps half of the count in the non-pointer `isa` and then adds half to the side table. It can quickly perform the critical write to the non-pointer `isa` and follow up with the expensive write to the side table. In contrast, when the retain count underflows, the runtime must take retain counts from the side table to gain the information necessary to perform the critical write to the non-pointer `isa`. The expensive read between the exclusive load and store increases the probability that the store may fail, which creates a unique corner case the release operation must handle. Writing is a great way to learn.

With that lesson learned, I have my fingers crossed that the next post on autorelease will be more straightforward!

---

[1](#_footnoteref_1). The SPI returns `true` if the release results in a retain count of zero, enabling system frameworks implementing root classes to perform clean up work before deallocating the root class instance. Safari 10.1 (circa March 2017) [added a use of the SPI](https://github.com/WebKit/WebKit/blob/Safari-603.1.30/Source/WebKit2/Shared/Cocoa/WKObject.mm#L206-L213), though the change was later [reverted in Safari 11.1](https://github.com/WebKit/WebKit/commit/4b5bca14adf3033809dd7a0a8a7ba634646cf7ea).

[2](#_footnoteref_2). The [rootRetain section](https://alwaysprocessing.blog/2023/07/22/objc-retain#rootretain) in the retain post briefly discusses the runtime’s `LoadExclusive` function.

[3](#_footnoteref_3). The [rootRetain section](https://alwaysprocessing.blog/2023/07/22/objc-retain#rootretain) in the retain post has a detailed discussion on the message send logic and its use of Objective-C runtime functions.

[4](#_footnoteref_4). A future post will discuss the implementation of the retain count side table.

[5](#_footnoteref_5). A future post will discuss object deallocation in more detail.
