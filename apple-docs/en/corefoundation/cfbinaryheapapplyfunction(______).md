---
title: 'CFBinaryHeapApplyFunction(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbinaryheapapplyfunction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapapplyfunction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapapplyfunction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:92d0001955f26aab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapApplyFunction(_:_:_:)

<sub>Function</sub>

Iteratively applies a function to all the values in a binary heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBinaryHeapApplyFunction(_ heap: CFBinaryHeap!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `heap` — The binary heap to use.

- `applier` — The callback function to call once for each value in `heap`.

- `context` — A program-defined value that is passed to the `applier` callback function, but is otherwise unused by this function.

## See Also

### CFBinaryHeap Miscellaneous Functions

- [CFBinaryHeapAddValue](<cfbinaryheapaddvalue(____).md>) — Adds a value to a binary heap.
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
