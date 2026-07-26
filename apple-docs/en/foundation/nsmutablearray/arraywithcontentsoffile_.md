---
title: 'arrayWithContentsOfFile:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/arraywithcontentsoffile:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/arraywithcontentsoffile:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/arraywithcontentsoffile%3A.json'
content_hash: 'sha256:f0db035255ebd907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# arrayWithContentsOfFile:

<sub>Type Method</sub>

Creates and returns a mutable array containing the contents of the file specified by the given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSMutableArray<id> *) arrayWithContentsOfFile:(NSString *) path;
```

## Parameters

- `path` — The path to a file containing a string representation of a mutable array produced by the [- writeToFile:atomically:](<../nsarray/write(tofile_atomically_).md>) method.

## Return Value

A mutable array containing the contents of the file specified `aPath`. Returns `nil` if the file can’t be opened or if the contents of the file can’t be parsed into a mutable array.

## Discussion

The mutable array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this array are immutable even if the array is mutable.

## See Also

### Related Documentation

- [- writeToFile:atomically:](<../nsarray/write(tofile_atomically_).md>) — Writes the contents of the array to a file at a given path. _(deprecated)_

### Creating and Initializing a Mutable Array

- [arrayWithCapacity:](arraywithcapacity_.md) — Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.
- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.
- [initWithContentsOfFile:](initwithcontentsoffile_.md) — Initializes a newly allocated mutable array with the contents of the file specified by a given path
- [initWithContentsOfURL:](initwithcontentsofurl_.md) — Initialized a newly allocated mutable array with the contents of the location specified by a given URL.
