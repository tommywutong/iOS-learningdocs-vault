---
title: 'CFBinaryHeapAddValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbinaryheapaddvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapaddvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapaddvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:41710ce52c71a24e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapAddValue(_:_:)

<sub>Function</sub>

Adds a value to a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBinaryHeapAddValue(_ heap: CFBinaryHeap!, _ value: UnsafeRawPointer!)
```

## Parameters

- `heap` — The binary heap to use.

- `value` — The value to add to the binary heap. The value is retained by the binary heap using the retain callback provided in the [CFBinaryHeapCallBacks](cfbinaryheapcallbacks.md) structure when the binary heap was created.

## See Also

### CFBinaryHeap Miscellaneous Functions

- [CFBinaryHeapApplyFunction](<cfbinaryheapapplyfunction(______).md>) — Iteratively applies a function to all the values in a binary heap.
- [CFBinaryHeapContainsValue](<cfbinaryheapcontainsvalue(____).md>) — Returns whether a given value is in a binary heap.
- [CFBinaryHeapCreate](<cfbinaryheapcreate(________).md>) — Creates a new mutable or fixed-mutable binary heap.
- [CFBinaryHeapCreateCopy](<cfbinaryheapcreatecopy(______).md>) — Creates a new mutable or fixed-mutable binary heap with the values from a pre-existing binary heap.
- [CFBinaryHeapGetCount](<cfbinaryheapgetcount(__).md>) — Returns the number of values currently in a binary heap.
- [CFBinaryHeapGetCountOfValue](<cfbinaryheapgetcountofvalue(____).md>) — Counts the number of times a given value occurs in a binary heap.
- [CFBinaryHeapGetMinimum](<cfbinaryheapgetminimum(__).md>) — Returns the minimum value in a binary heap.
- [CFBinaryHeapGetMinimumIfPresent](<cfbinaryheapgetminimumifpresent(____).md>) — Returns the minimum value in a binary heap, if present.
- [CFBinaryHeapGetTypeID](<cfbinaryheapgettypeid().md>) — Returns the type identifier of the `CFBinaryHeap` opaque type.
- [CFBinaryHeapGetValues](<cfbinaryheapgetvalues(____).md>) — Copies all the values from a binary heap into a sorted C array.
- [CFBinaryHeapRemoveAllValues](<cfbinaryheapremoveallvalues(__).md>) — Removes all values from a binary heap, making it empty.
- [CFBinaryHeapRemoveMinimumValue](<cfbinaryheapremoveminimumvalue(__).md>) — Removes the minimum value from a binary heap.
