---
title: 'init(array:copyItems:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/init(array:copyitems:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(array:copyitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28array%3Acopyitems%3A%29.json'
content_hash: 'sha256:a89d5ded46466df4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(array:copyItems:)

<sub>Initializer</sub>

Initializes a newly allocated array using `anArray` as the source of data objects for the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(array: [Any], copyItems flag: Bool)
```

## Parameters

- `array` — An array containing the objects with which to initialize the new array.

- `flag` — If [true](../../swift/true.md), each object in `array` receives a [copyWithZone:](../../objectivec/nsobject-swift.class/copywithzone_.md) message to create a copy of the object—objects must conform to the `NSCopying` protocol. In a managed memory environment, this is instead of the `retain` message the object would otherwise receive. The object copy is then added to the returned array. If [false](../../swift/false.md), then in a managed memory environment each object in `array` simply receives a `retain` message when it is added to the returned array.

## Return Value

An array initialized to contain the objects—or if `flag` is [true](../../swift/true.md), copies of the objects—in `array`. The returned object might be different than the original receiver.

## Discussion

After an immutable array has been initialized in this way, it cannot be modified.

The [- copyWithZone:](<../nscopying/copy(with_).md>) method performs a shallow copy. If you have a collection of arbitrary depth, passing [true](../../swift/true.md) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [false](../../swift/false.md) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## See Also

### Related Documentation

- [+ arrayWithObject:](<init(object_).md>) — Creates and returns an array containing a given object.

### Initializing an Array

- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithArray:](<init(array_)-o72h.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated array with the contents of the file specified by a given path. _(deprecated)_
- [- initWithObjects:count:](<init(objects_count_)-5odxv.md>) — Initializes a newly allocated array to include a given number of objects from a given C array.
