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
doc_path: '/documentation/foundation/nsdictionary/write(tofile:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/write(tofile:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/write%28tofile%3Aatomically%3A%29.json'
content_hash: 'sha256:8cd876771364e0ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# write(toFile:atomically:)

<sub>Instance Method</sub>

Writes a property list representation of the contents of the dictionary to a given path.

> [!warning] Deprecated
> Use [- writeToURL:error:](<write(to_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

## Parameters

- `path` — The path at which to write the file. If `path` contains a tilde (~) character, you must expand it with [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md) before invoking this method.

- `useAuxiliaryFile` — A flag that specifies whether the file should be written atomically. If `useAuxiliaryFile` is [true](../../swift/true.md), the dictionary is written to an auxiliary file, and then the auxiliary file is renamed to `path`. If `useAuxiliaryFile` is [false](../../swift/false.md), the dictionary is written directly to `path`. The [true](../../swift/true.md) option guarantees that `path`, if it exists at all, won’t be corrupted even if the system should crash during writing.

## Return Value

[true](../../swift/true.md) if the file is written successfully, otherwise [false](../../swift/false.md).

## Discussion

This method recursively validates that all the contained objects are property list objects (instances of `NSData`, `NSDate`, `NSNumber`, `NSString`, `NSArray`, or `NSDictionary`) before writing out the file, and returns [false](../../swift/false.md) if all the objects are not property list objects, since the resultant file would not be a valid property list.

If the dictionary’s contents are all property list objects, the file written by this method can be used to initialize a new dictionary with the class method [dictionaryWithContentsOfFile:](dictionarywithcontentsoffile_.md) or the instance method [- initWithContentsOfFile:](<init(contentsoffile_).md>).

If you need greater control over the property list representation, use [PropertyListSerialization](../propertylistserialization.md) instead.

For more information about property lists, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

### Storing Dictionaries

- [- writeToURL:error:](<write(to_).md>) — Writes a property list representation of the contents of the dictionary to a given URL.
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes a property list representation of the contents of the dictionary to a given URL. _(deprecated)_
