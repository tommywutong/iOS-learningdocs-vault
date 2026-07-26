---
title: 'write(to:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdictionary/write(to:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/write(to:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/write%28to%3Aatomically%3A%29.json'
content_hash: 'sha256:446cc055653d746b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# write(to:atomically:)

<sub>Instance Method</sub>

Writes a property list representation of the contents of the dictionary to a given URL.

> [!warning] Deprecated
> Use [- writeToURL:error:](<write(to_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, atomically: Bool) -> Bool
```

## Parameters

- `url` — The URL to which to write the dictionary.

- `atomically` — A flag that specifies whether the output should be written atomically. If `atomically` is [true](../../swift/true.md), the dictionary is written to an auxiliary location, and then the auxiliary location is renamed to `url`. If `atomically` is [false](../../swift/false.md), the dictionary is written directly to `url`. The [true](../../swift/true.md) option guarantees that `url`, if it exists at all, won’t be corrupted even if the system should crash during writing. `atomically` is ignored if `url` is of a type that cannot be written atomically.

## Return Value

[true](../../swift/true.md) if the location is written successfully, otherwise [false](../../swift/false.md).

## Discussion

This method recursively validates that all the contained objects are property list objects (instances of `NSData`, `NSDate`, `NSNumber`, `NSString`, `NSArray`, or `NSDictionary`) before writing out the file, and returns [false](../../swift/false.md) if all the objects are not property list objects, since the resultant output would not be a valid property list.

If the dictionary’s contents are all property list objects, the location written by this method can be used to initialize a new dictionary with the class method `NSDictionary/init(contentsOfURL:)-98pl3` or the instance method `NSDictionary/init(contentsOfURL:)-4pv16`.

If you need greater control over the property list representation, use [PropertyListSerialization](../propertylistserialization.md) instead.

For more information about property lists, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

### Storing Dictionaries

- [- writeToURL:error:](<write(to_).md>) — Writes a property list representation of the contents of the dictionary to a given URL.
- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes a property list representation of the contents of the dictionary to a given path. _(deprecated)_
