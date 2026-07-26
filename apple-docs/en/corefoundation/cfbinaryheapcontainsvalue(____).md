---
title: 'CFBinaryHeapContainsValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbinaryheapcontainsvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcontainsvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcontainsvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:c5bb2eed20166caa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapContainsValue(_:_:)

<sub>Function</sub>

Returns whether a given value is in a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBinaryHeapContainsValue(_ heap: CFBinaryHeap!, _ value: UnsafeRawPointer!) -> Bool
```

## Parameters

- `heap` — The binary heap to search.

- `value` — The value for which to find matches in the binary heap. The compare callback provided in the [CFBinaryHeapCallBacks](cfbinaryheapcallbacks.md) structure when the binary heap was created is used to compare values. If `value`, or any of the values in the binary heap, are not understood by the compare callback, the behavior is undefined.

## Return Value

`true` if `value` is a member of `heap`, `false` otherwise.

## See Also

### CFBinaryHeap Miscellaneous Functions

- [CFBinaryHeapAddValue](<cfbinaryheapaddvalue(____).md>) — Adds a value to a binary heap.
- [CFBinaryHeapApplyFunction](<cfbinaryheapapplyfunction(______).md>) — Iteratively applies a function to all the values in a binary heap.
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
