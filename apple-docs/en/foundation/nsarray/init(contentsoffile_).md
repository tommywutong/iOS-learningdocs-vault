---
title: 'init(contentsOfFile:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/init(contentsoffile:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(contentsoffile:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28contentsoffile%3A%29.json'
content_hash: 'sha256:b2ecd1f59d5b2db7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(contentsOfFile:)

<sub>Initializer</sub>

Initializes a newly allocated array with the contents of the file specified by a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOfFile path: String)
```

## Parameters

- `path` — The path to a file containing a representation of an array produced by the [- writeToFile:atomically:](<write(tofile_atomically_).md>) method.

## Return Value

An array initialized to contain the contents of the file specified by `aPath` or `nil` if the file can’t be opened or the contents of the file can’t be parsed into an array. The returned object might be different than the original receiver.

## Discussion

The array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## See Also

### Related Documentation

- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the contents of the array to a file at a given path. _(deprecated)_

### Initializing an Array

- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithArray:](<init(array_)-o72h.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [- initWithObjects:count:](<init(objects_count_)-5odxv.md>) — Initializes a newly allocated array to include a given number of objects from a given C array.
