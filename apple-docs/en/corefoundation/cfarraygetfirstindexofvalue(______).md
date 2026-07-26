---
title: 'CFArrayGetFirstIndexOfValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraygetfirstindexofvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraygetfirstindexofvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraygetfirstindexofvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:00e1552ebd6a9d04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayGetFirstIndexOfValue(_:_:_:)

<sub>Function</sub>

Searches an array forward for a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayGetFirstIndexOfValue(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!) -> CFIndex
```

## Parameters

- `theArray` — The array to examine.

- `range` — The range within `theArray` to search. The range must lie within the bounds of  `theArray`. The range may be empty (length `0`). The search progresses from the lowest index defined by the range to the highest.

- `value` — The value for which to find a match in `theArray`. The equal callback provided when `theArray` was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in `theArray`, is not understood by the equal callback, the behavior is undefined.

## Return Value

The lowest index of the matching values in the range, or `-1` if no value in the range matched.

## See Also

### Examining an Array

- [CFArrayBSearchValues](<cfarraybsearchvalues(__________).md>) — Searches an array for a value using a binary search algorithm.
- [CFArrayContainsValue](<cfarraycontainsvalue(______).md>) — Reports whether or not a value is in an array.
- [CFArrayGetCount](<cfarraygetcount(__).md>) — Returns the number of values currently in an array.
- [CFArrayGetCountOfValue](<cfarraygetcountofvalue(______).md>) — Counts the number of times a given value occurs in an array.
- [CFArrayGetLastIndexOfValue](<cfarraygetlastindexofvalue(______).md>) — Searches an array backward for a value.
- [CFArrayGetValues](<cfarraygetvalues(______).md>) — Fills a buffer with values from an array.
- [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) — Retrieves a value at a given index.
