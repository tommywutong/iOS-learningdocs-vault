---
title: 'CFArrayGetValues(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraygetvalues(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraygetvalues(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraygetvalues%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a436a1e12ea0a4f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayGetValues(_:_:_:)

<sub>Function</sub>

Fills a buffer with values from an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayGetValues(_ theArray: CFArray!, _ range: CFRange, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theArray` — The array to examine.

- `range` — The range of values within `theArray` to retrieve. The range must lie within the bounds of `theArray`. The range may be empty (length `0`), in which case no values are put into the buffer `values`.

- `values` — A C array of pointer-sized values to be filled with values from `theArray`. The values in the C array are in the same order as they appear in `theArray`. If this value is not a valid pointer to a C array of at least `range.length` pointers, the behavior is undefined. If the values are Core Foundation objects, ownership follows [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining an Array

- [CFArrayBSearchValues](<cfarraybsearchvalues(__________).md>) — Searches an array for a value using a binary search algorithm.
- [CFArrayContainsValue](<cfarraycontainsvalue(______).md>) — Reports whether or not a value is in an array.
- [CFArrayGetCount](<cfarraygetcount(__).md>) — Returns the number of values currently in an array.
- [CFArrayGetCountOfValue](<cfarraygetcountofvalue(______).md>) — Counts the number of times a given value occurs in an array.
- [CFArrayGetFirstIndexOfValue](<cfarraygetfirstindexofvalue(______).md>) — Searches an array forward for a value.
- [CFArrayGetLastIndexOfValue](<cfarraygetlastindexofvalue(______).md>) — Searches an array backward for a value.
- [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) — Retrieves a value at a given index.
