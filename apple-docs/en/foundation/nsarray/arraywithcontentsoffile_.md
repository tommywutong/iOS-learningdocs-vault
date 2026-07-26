---
title: 'arrayWithContentsOfFile:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/arraywithcontentsoffile:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/arraywithcontentsoffile:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/arraywithcontentsoffile%3A.json'
content_hash: 'sha256:d7e2a32ce4e22fef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# arrayWithContentsOfFile:

<sub>Type Method</sub>

Creates and returns an array containing the contents of the file specified by a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSArray<id> *) arrayWithContentsOfFile:(NSString *) path;
```

## Parameters

- `path` — The path to a file containing a string representation of an array produced by the [- writeToFile:atomically:](<write(tofile_atomically_).md>) method.

## Return Value

An array containing the contents of the file specified by `aPath`. Returns `nil` if the file can’t be opened or if the contents of the file can’t be parsed into an array.

## Discussion

The array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this array are immutable, even if the array is mutable.

## See Also

### Related Documentation

- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the contents of the array to a file at a given path. _(deprecated)_

### Creating an Array

- [array](array.md) — Creates and returns an empty array.
- [arrayWithArray:](arraywitharray_.md) — Creates and returns an array containing the objects in another given array.
- [+ arrayWithObject:](<init(object_).md>) — Creates and returns an array containing a given object.
- [arrayWithObjects:](arraywithobjects_.md) — Creates and returns an array containing the objects in the argument list.
- [+ arrayWithObjects:count:](<init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.
