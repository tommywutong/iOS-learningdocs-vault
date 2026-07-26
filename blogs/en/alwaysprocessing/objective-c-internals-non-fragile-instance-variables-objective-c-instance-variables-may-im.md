---
title: 'Objective-C Internals: Non-Fragile Instance Variables Objective-C instance variables may impact ABI stability. In Objective-C 2, Apple introduced a "non-fragile" layout to preserve ABI stability acros'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/03/12/objc-ivar-abi'
original_language: en
published: 2023-03-12
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1d8f40491166d9c8'
translated: false
---

> 原文：[Objective-C Internals: Non-Fragile Instance Variables Objective-C instance variables may impact ABI stability. In Objective-C 2, Apple introduced a "non-fragile" layout to preserve ABI stability acros](https://alwaysprocessing.blog/2023/03/12/objc-ivar-abi)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Non-Fragile Instance Variables

![Two yellow English Labradors sitting in room with many boxes. Can they rearrange the boxes without breaking anything?](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c2988a3b-e50e-4f00-1116-eb898b8df300/public)

Objective-C instance variables may impact ABI stability. In Objective-C 2, Apple introduced a "non-fragile" layout to preserve ABI stability across some types of changes to a class’s instance variables.

Parts of the Objective-C runtime have implications for the ABI, illustrated by the evolution of instance variables in Objective-C classes.

## Fragile Instance Variables

Objective-C class instance variables in 32-bit versions of macOS have a "fragile" layout, meaning instance variables for this deployment target are accessed by their offset from the start of the class as if the instance variables throughout the class hierarchy were concatenated into a C struct. And, like fields in a C struct, the offset of each instance variable is hardcoded into each read or write in machine code and cannot change once deployed.

So, each instance variable’s size, alignment, and offset are part of its class’s ABI. Adding or removing instance variables in a public-facing Objective-C class risks breaking subclasses at runtime, hence the term "fragile." (Changing the type of an instance variable can be considered a remove-add operation.)

When linking to a binary library (e.g., an app linking to the AppKit framework), the entity linking to the binary library relies on its ABI remaining "stable." To maintain a stable ABI, all changes made to a binary library must not invalidate the contract used by the compiler and linker to interoperate with the binary library. If a new version of the binary library changes the contract, anything previously linked to it will likely break.

To explore how Apple handled the constraints of ABI stability before Objective-C 2, let’s examine the following abridged and annotated class definitions from the macOS 10.13 SDK.

```
// #import <objc/NSObject.h>
@interface NSObject <NSObject> {
  Class             isa;                // 0x00
}
@end

// #import <AppKit/NSResponder.h>
@interface NSResponder: NSObject {
  id                _nextResponder;     // 0x04
}
@end

// #import <AppKit/NSView.h>
typedef struct __VFlags {
  unsigned int flags;
} _VFlags;

@class _NSViewAuxiliary;

@interface NSView: NSResponder {
  /* All instance variables are private */
  NSRect            _frame;             // 0x08
  NSRect            _bounds;            // 0x18
  NSView           *_superview;         // 0x28
  NSArray          *_subviews;          // 0x2c
  NSWindow         *_window;            // 0x30
  id                _unused_was_gState; // 0x34
  id                _frameMatrix;       // 0x38
  CALayer          *_layer;             // 0x3c
  id                _dragTypes;         // 0x40
  _NSViewAuxiliary *_viewAuxiliary;     // 0x44
  _VFlags           _vFlags;            // 0x48
  struct __VFlags2 {
    unsigned int flags;
  }                 _vFlags2;           // 0x4c
}
@end
```

The comment to the right of each instance variable above indicates the hard-coded offset relative to the `self` pointer the compiler would emit to read or write to it.

The following represents `NSView`'s instance variable ABI, reflecting its in-memory layout and how the compiler viewed instance variables as if they were fields in a C struct.

```
struct NSViewHeapLayout {
  Class             isa;                // 0x00
  id                _nextResponder;     // 0x04
  NSRect            _frame;             // 0x08
  NSRect            _bounds;            // 0x18
  NSView           *_superview;         // 0x28
  NSArray          *_subviews;          // 0x2c
  NSWindow         *_window;            // 0x30
  id                _unused_was_gState; // 0x34
  id                _frameMatrix;       // 0x38
  CALayer          *_layer;             // 0x3c
  id                _dragTypes;         // 0x40
  _NSViewAuxiliary *_viewAuxiliary;     // 0x44
  _VFlags           _vFlags;            // 0x48
  struct __VFlags2  _vFlags2;           // 0x4c
};
```

If we comb through all public SDKs since the release of Mac OS X 10.0, we can observe the instance variables of `NSObject` and `NSResponder` have not changed (thus preserving ABI stability). However, `NSView` has two curious instance variables as artifacts of maintaining ABI stability:

1. `_unused_was_gState`

    - In early versions of Mac OS X, `NSView` had a `_gState` instance variable to support its integration into the graphics stack. This state became obsolete in later releases, so the AppKit maintainers renamed the instance variable to reflect that it’s intentionally unused.
    - The AppKit maintainers could not remove the instance variable as removal would shift the offset of the instance variables following it, including those in subclasses.
    - I suspect the maintainers did not repurpose the instance variable, as some apps likely read from (and even wrote to) the variable. It’s generally not possible for such apps to correctly handle a pointer to an entirely different opaque type, so repurposing it may have broken those apps. However, any affected apps would likely function well enough with the variable’s default/placeholder value.

          - The `@private` access modifier was added to the Objective-C language simultaneously with the launch of Objective-C 2. Before introducing access control, convention was the only tool to prevent subclasses from directly accessing a superclass state (hence the comment at the start of the `NSView` instance variable block).
2. `_viewAuxiliary`: When a class required ABI stability, using a private helper class was a typical pattern to reserve the ability to add or remove instance variables in each release. So, each instance of `NSView` allocates an instance of `_NSViewAuxiliary` to store instance variables and state without affecting `NSView`'s ABI.

When a class required ABI stability but did not have the option to use a private helper class (e.g., `NSObject` or `NSResponder`), another typical pattern to add or remove instance variables was to use a side table. (The Objective-C runtime in Mac OS X 10.6 and iPhoneOS 3.1 added generalized support for side table storage with its [associated references](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj) feature.)

## Non-Fragile Instance Variables

In Objective-C 2, Apple changed the Objective-C runtime and ABI to support a "non-fragile" layout, which is available on all versions of iOS, tvOS, watchOS, and 64-bit versions of macOS. This feature preserves ABI stability when adding instance variables to a class and removing non-public instance variables. As a result, using the above patterns (dead instance variables, private helper classes, and side table storage) is no longer necessary to preserve ABI stability.

Non-fragile instance variable layout has two primary requirements to preserve ABI stability:

- Adding instance variables to a class requires updating the offset used to access all of the instance variables that follow it, including the instance variables in all subclasses.
- Removing instance variables from a class requires that the instance variables could not have been accessed outside of the class’s binary image.

When compiling Objective-C 2 code, the compiler emits an offset symbol for each instance variable, the use of which fulfills the ABI stability requirements:

- When the Objective-C runtime detects a class’s superclass has grown, it updates the class’s instance variable offset symbols to accommodate the larger superclass size.
- The symbols emitted for instance variables with `@package` or `@private` access have _private extern_ visibility in the object file and thus are not exported from the binary image. Removing these non-public instance variables is an ABI stable change because any code previously attempting to access them would have failed to link.

The Objective-C runtime does not (currently) decrease the offsets of a class’s instance variables if its superclass shrinks. This approach favors minimizing Objective-C runtime heap use and app startup time at the expense of increased heap use by instances of affected classes.

As an optimization, the initial value for each offset symbol is the instance variable’s offset at build time, enabling the Objective-C runtime to skip computing offsets at each app launch if the base class doesn’t grow.

## Fragile vs. Non-Fragile Example

To illustrate the differences in the code generated by the compiler between Objective-C 1 and Objective-C 2, let’s look at some trivial code to load the `_superview` instance variable.

```
NSView *superview = aView->_superview;
```

The code emitted by the compiler will be the same whether we’re compiling `NSView` itself or building a third-party app (assuming the instance variable is still implicitly `@public`).

In Objective-C 1, with fragile layout, the compiler simply adds the offset of the instance variable, as observed at compile time, to the object instance pointer to compute the address from which to load the instance variable.

```
NSView *superview = *(NSView **)((intptr_t)aView + 0x28);
```

If the layout of `NSView` changes after this compilation, the result of the load at the hardcoded offset may become undefined.

In Objective-C 2, with non-fragile layout, the compiler adds the value of the instance variable offset symbol to the object instance pointer to compute the address from which to load the instance variable.

```
extern uint32_t OBJC_IVAR_$_NSView._superview;
NSView *superview = *(NSView **)((intptr_t)aView + OBJC_IVAR_$_NSView._superview);
```

The layout of `NSView` is opaque to this compilation, so the result of the load will remain well-defined as long as the instance variable exists. However, if the instance variable is removed, `dyld` will not be able to load the binary image because the instance variable offset symbol will not be resolvable. (I suppose this is better than undefined runtime behavior!)

## The Objective-C Runtime Implementation

Updating a class’s instance variable offsets occurs as part of the class’s first-time initialization in [`realizeClassWithoutSwift()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2594-L2741).

```
static Class realizeClassWithoutSwift(Class cls, Class previously) {
  // ...
  // Reconcile instance variable offsets / layout.
  // This may reallocate class_ro_t, updating our ro variable.
  if (supercls && !isMeta) reconcileInstanceVariables(cls, supercls, ro);
  // ...
}
```

An update is only necessary if the superclass has "grown into" the subclass (relative to the layout computed during the compilation of the subclass). The superclass may have increased in size because it added instance variables, changed instance variables to types of larger sizes, added fields to a struct stored as an instance variable, or its superclass grew. (Recall the runtime no-ops if the superclass shrank.)

The [`reconcileInstanceVariables()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2484-L2581) function first ensures the class’s `class_ro_t`[[1](#_footnotedef_1)] data structure has been copied to the heap if it is necessary to update the class’s instance variable offsets as the initial data structure value is mapped from a read-only section of the executable. A writable copy is required so that the runtime can store the updated class layout metadata.

```
static void reconcileInstanceVariables(Class cls, Class supercls, const class_ro_t*& ro) {
  // ...
  if (ro->instanceStart >= super_ro->instanceSize) {
    // Superclass has not overgrown its space. We're done here.
    return;
  }

  if (ro->instanceStart < super_ro->instanceSize) {
    // Superclass has changed size. This class's ivars must move.
    // Also slide layout bits in parallel.
    // This code is incapable of compacting the subclass to
    //   compensate for a superclass that shrunk, so don't do that.
    class_ro_t *ro_w = make_ro_writeable(rw);
    ro = rw->ro();
    moveIvars(ro_w, super_ro->instanceSize);
  }
}
```

The [`moveIvars()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2433-L2481) function applies the necessary shift to the class’s instance variable offset symbols to accommodate the growth of the superclass.

````
static void moveIvars(class_ro_t *ro, uint32_t superSize) {
  uint32_t diff = superSize - ro->instanceStart;

  if (ro->ivars) {
    // Find maximum alignment in this class's ivars
    uint32_t maxAlignment = 1;
    for (const auto& ivar : *ro->ivars) {
      if (!ivar.offset) continue;  // anonymous bitfield

      uint32_t alignment = ivar.alignment();
      if (alignment > maxAlignment) maxAlignment = alignment;
    }

    // Compute a slide value that preserves that alignment
    uint32_t alignMask = maxAlignment - 1;
    diff = (diff + alignMask) & ~alignMask;

    // Slide all of this class's ivars en masse
    for (const auto& ivar : *ro->ivars) {
      if (!ivar.offset) continue;  // anonymous bitfield

      uint32_t oldOffset = (uint32_t)*ivar.offset;
      uint32_t newOffset = oldOffset + diff;
      *ivar.offset = newOffset;
    }
  }

  *(uint32_t *)&ro->instanceStart += diff;
  *(uint32_t *)&ro->instanceSize += diff;
}
```
````

The `for` loop above "slides" the offset of the instance variables out from the start of the class to accommodate the larger base class while preserving alignment. The `ivar` variables it’s writing to are the instance variable offset symbols, like `OBJC_IVAR_$_NSView._superview`, discussed in the previous section.

So, by adding one step of indirection to read or write an instance variable value, and with a small potential startup penalty, the Objective-C runtime is elegantly able to eliminate a significant ABI compatibility problem with minimal overhead and complexity.

---

[1](#_footnoteref_1). A future post will cover the division of the read-only and read-write class metadata structures.
