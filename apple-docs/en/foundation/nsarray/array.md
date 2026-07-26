---
title: array
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsarray/array
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/array'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/array.json'
content_hash: 'sha256:165fe7b9564edd6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# array

<sub>Type Method</sub>

Creates and returns an empty array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) array;
```

## Return Value

An empty array.

## Discussion

This method is used by mutable subclasses of `NSArray`.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Creating an Array

- [arrayWithArray:](arraywitharray_.md) — Creates and returns an array containing the objects in another given array.
- [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) — Creates and returns an array containing the contents of the file specified by a given path. _(deprecated)_
- [+ arrayWithObject:](<init(object_).md>) — Creates and returns an array containing a given object.
- [arrayWithObjects:](arraywithobjects_.md) — Creates and returns an array containing the objects in the argument list.
- [+ arrayWithObjects:count:](<init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.
