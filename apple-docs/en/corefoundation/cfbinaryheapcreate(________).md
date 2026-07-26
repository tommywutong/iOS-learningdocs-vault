---
title: 'CFBinaryHeapCreate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbinaryheapcreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c85bac0c8b4be392'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapCreate(_:_:_:_:)

<sub>Function</sub>

Creates a new mutable or fixed-mutable binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBinaryHeapCreate(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFBinaryHeapCallBacks>!, _ compareContext: UnsafePointer<CFBinaryHeapCompareContext>!) -> CFBinaryHeap!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the binary heap. The binary heap starts empty and can grow to this number of values. If this parameter is `0`, the binary heap’s maximum capacity is limited only by memory.

- `callBacks` — A pointer to a [CFBinaryHeapCallBacks](cfbinaryheapcallbacks.md) structure initialized with the callbacks that operate on the values placed into the binary heap. If the binary heap will be holding `CFString` objects, pass the [kCFStringBinaryHeapCallBacks](kcfstringbinaryheapcallbacks.md) constant. This functions makes a copy of the contents of the callbacks structure, so that a pointer to a structure on the stack can be passed in, or can be reused for multiple binary heap creations. This callbacks parameter may not be `NULL`.

- `compareContext` — Not used. Pass `NULL`.

## Return Value

A new `CFBinaryHeap` object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFBinaryHeap Miscellaneous Functions

- [CFBinaryHeapAddValue](<cfbinaryheapaddvalue(____).md>) — Adds a value to a binary heap.
- [CFBinaryHeapApplyFunction](<cfbinaryheapapplyfunction(______).md>) — Iteratively applies a function to all the values in a binary heap.
- [CFBinaryHeapContainsValue](<cfbinaryheapcontainsvalue(____).md>) — Returns whether a given value is in a binary heap.
- [CFBinaryHeapCreateCopy](<cfbinaryheapcreatecopy(______).md>) — Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.
- [CFBinaryHeapGetCount](<cfbinaryheapgetcount(__).md>) — Returns the number of values currently in a binary heap.
- [CFBinaryHeapGetCountOfValue](<cfbinaryheapgetcountofvalue(____).md>) — Counts the number of times a given value occurs in a binary heap.
- [CFBinaryHeapGetMinimum](<cfbinaryheapgetminimum(__).md>) — Returns the minimum value in a binary heap.
- [CFBinaryHeapGetMinimumIfPresent](<cfbinaryheapgetminimumifpresent(____).md>) — Returns the minimum value in a binary heap, if present.
- [CFBinaryHeapGetTypeID](<cfbinaryheapgettypeid().md>) — Returns the type identifier of the `CFBinaryHeap` opaque type.
- [CFBinaryHeapGetValues](<cfbinaryheapgetvalues(____).md>) — Copies all the values from a binary heap into a sorted C array.
- [CFBinaryHeapRemoveAllValues](<cfbinaryheapremoveallvalues(__).md>) — Removes all values from a binary heap, making it empty.
- [CFBinaryHeapRemoveMinimumValue](<cfbinaryheapremoveminimumvalue(__).md>) — Removes the minimum value from a binary heap.
