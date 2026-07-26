---
title: 'CFArrayBSearchValues(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraybsearchvalues(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraybsearchvalues(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraybsearchvalues%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b3da41f0a5162b0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayBSearchValues(_:_:_:_:_:)

<sub>Function</sub>

Searches an array for a value using a binary search algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayBSearchValues(_ theArray: CFArray!, _ range: CFRange, _ value: UnsafeRawPointer!, _ comparator: CFComparatorFunction!, _ context: UnsafeMutableRawPointer!) -> CFIndex
```

## Parameters

- `theArray` — An array, sorted from least to greatest according to the `comparator` function.

- `range` — The range within `theArray` to search. The range must not exceed the bounds of `theArray`. The range may be empty (length `0`).

- `value` — The value for which to find a match in `theArray`. If `value`, or any other value in `theArray`, is not understood by the `comparator` callback, the behavior is undefined.

- `comparator` — The function with the comparator function type signature that is used in the binary search operation to compare values in `theArray` with the given value. If there are values in the range that the `comparator` function does not expect or cannot properly compare, the behavior is undefined.

- `context` — A pointer-sized program-defined value, which is passed as the third argument to the `comparator` function, but is otherwise unused by this function. If the context is not what is expected by the `comparator` function, the behavior is undefined.

## Return Value

The return value is one of the following:

## Discussion

- The index of a value that matched, if the target value matches one or more in the range.
- Greater than or equal to the end point of the range, if the value is greater than all the values in the range.
- The index of the value greater than the target value, if the value lies between two of (or less than all of) the values in the range.

## See Also

### Examining an Array

- [CFArrayContainsValue](<cfarraycontainsvalue(______).md>) — Reports whether or not a value is in an array.
- [CFArrayGetCount](<cfarraygetcount(__).md>) — Returns the number of values currently in an array.
- [CFArrayGetCountOfValue](<cfarraygetcountofvalue(______).md>) — Counts the number of times a given value occurs in an array.
- [CFArrayGetFirstIndexOfValue](<cfarraygetfirstindexofvalue(______).md>) — Searches an array forward for a value.
- [CFArrayGetLastIndexOfValue](<cfarraygetlastindexofvalue(______).md>) — Searches an array backward for a value.
- [CFArrayGetValues](<cfarraygetvalues(______).md>) — Fills a buffer with values from an array.
- [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) — Retrieves a value at a given index.
