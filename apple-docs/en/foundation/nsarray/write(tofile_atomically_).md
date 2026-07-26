---
title: 'write(toFile:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/write(tofile:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/write(tofile:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/write%28tofile%3Aatomically%3A%29.json'
content_hash: 'sha256:ac89eb8e2d986ef6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# write(toFile:atomically:)

<sub>Instance Method</sub>

Writes the contents of the array to a file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

## Parameters

- `path` — The path at which to write the contents of the array. If `path` contains a tilde (~) character, you must expand it with [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md) before invoking this method.

- `useAuxiliaryFile` — If [true](../../swift/true.md), the array is written to an auxiliary file, and then the auxiliary file is renamed to `path`. If [false](../../swift/false.md), the array is written directly to `path`. The [true](../../swift/true.md) option guarantees that `path`, if it exists at all, won’t be corrupted even if the system should crash during writing.

## Return Value

[true](../../swift/true.md) if the file is written successfully, otherwise [false](../../swift/false.md).

## Discussion

If the array’s contents are all property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects), the file written by this method can be used to initialize a new array with the class method [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) or the instance method [- initWithContentsOfFile:](<init(contentsoffile_).md>). This method recursively validates that all the contained objects are property list objects before writing out the file, and returns [false](../../swift/false.md) if all the objects are not property list objects, since the resultant file would not be a valid property list.

## See Also

### Related Documentation

- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated array with the contents of the file specified by a given path. _(deprecated)_

### Storing Arrays

- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the contents of the array to the location specified by a given URL. _(deprecated)_
