---
title: 'arrayWithArray:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/arraywitharray:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/arraywitharray:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/arraywitharray%3A.json'
content_hash: 'sha256:c9f3faa2ccd510e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# arrayWithArray:

<sub>Type Method</sub>

Creates and returns an array containing the objects in another given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) arrayWithArray:(NSArray<id> *) array;
```

## Parameters

- `array` — An array.

## Return Value

An array containing the objects in `anArray`.

## See Also

### Related Documentation

- [initWithObjects:](initwithobjects_.md) — Initializes a newly allocated array by placing in it the objects in the argument list.

### Creating an Array

- [array](array.md) — Creates and returns an empty array.
- [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) — Creates and returns an array containing the contents of the file specified by a given path. _(deprecated)_
- [+ arrayWithObject:](<init(object_).md>) — Creates and returns an array containing a given object.
- [arrayWithObjects:](arraywithobjects_.md) — Creates and returns an array containing the objects in the argument list.
- [+ arrayWithObjects:count:](<init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.
