---
title: 'CFArrayGetValueAtIndex(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraygetvalueatindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraygetvalueatindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraygetvalueatindex%28_%3A_%3A%29.json'
content_hash: 'sha256:ae7444f3569a4e9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayGetValueAtIndex(_:_:)

<sub>Function</sub>

Retrieves a value at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayGetValueAtIndex(_ theArray: CFArray!, _ idx: CFIndex) -> UnsafeRawPointer!
```

## Parameters

- `theArray` — The array to examine.

- `idx` — The index of the value to retrieve. If the index is outside the index space of `theArray` (`0` to `N-1` inclusive (where `N` is the count of `theArray`), the behavior is undefined.

## Return Value

The value at the `idx` index in `theArray`. If the return value is a Core Foundation Object, ownership follows [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining an Array

- [CFArrayBSearchValues](<cfarraybsearchvalues(__________).md>) — Searches an array for a value using a binary search algorithm.
- [CFArrayContainsValue](<cfarraycontainsvalue(______).md>) — Reports whether or not a value is in an array.
- [CFArrayGetCount](<cfarraygetcount(__).md>) — Returns the number of values currently in an array.
- [CFArrayGetCountOfValue](<cfarraygetcountofvalue(______).md>) — Counts the number of times a given value occurs in an array.
- [CFArrayGetFirstIndexOfValue](<cfarraygetfirstindexofvalue(______).md>) — Searches an array forward for a value.
- [CFArrayGetLastIndexOfValue](<cfarraygetlastindexofvalue(______).md>) — Searches an array backward for a value.
- [CFArrayGetValues](<cfarraygetvalues(______).md>) — Fills a buffer with values from an array.
