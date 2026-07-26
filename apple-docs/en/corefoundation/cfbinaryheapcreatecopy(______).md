---
title: 'CFBinaryHeapCreateCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbinaryheapcreatecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcreatecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcreatecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:30a0835cca0db82e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapCreateCopy(_:_:_:)

<sub>Function</sub>

Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBinaryHeapCreateCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ heap: CFBinaryHeap!) -> CFBinaryHeap!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the binary heap. The binary heap starts with the same number of values as `heap` and can grow to this number of values. If this parameter is `0`, the binary heap’s maximum capacity is limited only by memory. If nonzero, `capacity` must be large enough to hold all the values in `heap`.

- `heap` — The binary heap which is to be copied. The values from the binary heap are copied as pointers into the new binary heap (that is, the values themselves are copied, not that to which the values point, if anything). However, the values are also retained by the new binary heap.

## Return Value

A new `CFBinaryHeap` object holding the same values as `heap`. The new binary heap uses the same callbacks as `heap`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFBinaryHeap Miscellaneous Functions

- [CFBinaryHeapAddValue](<cfbinaryheapaddvalue(____).md>) — Adds a value to a binary heap.
- [CFBinaryHeapApplyFunction](<cfbinaryheapapplyfunction(______).md>) — Iteratively applies a function to all the values in a binary heap.
- [CFBinaryHeapContainsValue](<cfbinaryheapcontainsvalue(____).md>) — Returns whether a given value is in a binary heap.
- [CFBinaryHeapCreate](<cfbinaryheapcreate(________).md>) — Creates a new mutable or fixed-mutable binary heap.
- [CFBinaryHeapGetCount](<cfbinaryheapgetcount(__).md>) — Returns the number of values currently in a binary heap.
- [CFBinaryHeapGetCountOfValue](<cfbinaryheapgetcountofvalue(____).md>) — Counts the number of times a given value occurs in a binary heap.
- [CFBinaryHeapGetMinimum](<cfbinaryheapgetminimum(__).md>) — Returns the minimum value in a binary heap.
- [CFBinaryHeapGetMinimumIfPresent](<cfbinaryheapgetminimumifpresent(____).md>) — Returns the minimum value in a binary heap, if present.
- [CFBinaryHeapGetTypeID](<cfbinaryheapgettypeid().md>) — Returns the type identifier of the `CFBinaryHeap` opaque type.
- [CFBinaryHeapGetValues](<cfbinaryheapgetvalues(____).md>) — Copies all the values from a binary heap into a sorted C array.
- [CFBinaryHeapRemoveAllValues](<cfbinaryheapremoveallvalues(__).md>) — Removes all values from a binary heap, making it empty.
- [CFBinaryHeapRemoveMinimumValue](<cfbinaryheapremoveminimumvalue(__).md>) — Removes the minimum value from a binary heap.
