---
title: 'CFArrayGetLastIndexOfValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraygetlastindexofvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraygetlastindexofvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraygetlastindexofvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cfedc5f518f7c024'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayGetLastIndexOfValue(_:_:_:)

<sub>Function</sub>

Searches an array backward for a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayGetLastIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex
```

## Parameters

- `theArray` — The array to examine.

- `range` — The range within `theArray` to search. The range must not exceed the bounds of `theArray`. The range may be empty (length `0`). The search progresses from the highest index defined by the range to the lowest.

- `value` — The value for which to find a match in `theArray`. The equal callback provided when `theArray` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If value, or any other value in `theArray`, is not understood by the equal callback, the behavior is undefined.

## Return Value

The highest index of the matching values in the range, or `-1` if no value in the range matched.

## See Also

### Examining an Array

- [CFArrayBSearchValues](<cfarraybsearchvalues(__________).md>) — Searches an array for a value using a binary search algorithm.
- [CFArrayContainsValue](<cfarraycontainsvalue(______).md>) — Reports whether or not a value is in an array.
- [CFArrayGetCount](<cfarraygetcount(__).md>) — Returns the number of values currently in an array.
- [CFArrayGetCountOfValue](<cfarraygetcountofvalue(______).md>) — Counts the number of times a given value occurs in an array.
- [CFArrayGetFirstIndexOfValue](<cfarraygetfirstindexofvalue(______).md>) — Searches an array forward for a value.
- [CFArrayGetValues](<cfarraygetvalues(______).md>) — Fills a buffer with values from an array.
- [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) — Retrieves a value at a given index.
