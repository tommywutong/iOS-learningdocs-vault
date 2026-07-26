---
title: 'initWithContentsOfFile:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/initwithcontentsoffile:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/initwithcontentsoffile:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/initwithcontentsoffile%3A.json'
content_hash: 'sha256:a351d01eb14fae45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# initWithContentsOfFile:

<sub>Instance Method</sub>

Initializes a newly allocated mutable array with the contents of the file specified by a given path

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSMutableArray<id> *) initWithContentsOfFile:(NSString *) path;
```

## Parameters

- `path` — The path to a file containing a representation of a mutable array produced by [- writeToFile:atomically:](<../nsarray/write(tofile_atomically_).md>) method.

## Return Value

A mutable array initialized to contain the contents of the file specified by `aPath` or `nil` if the file can’t be opened or the contents of the file can’t be parsed into a mutable array. The returned object must be different than the original receiver.

## Discussion

The mutable array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable even if the array is mutable.

## See Also

### Related Documentation

- [- writeToFile:atomically:](<../nsarray/write(tofile_atomically_).md>) — Writes the contents of the array to a file at a given path. _(deprecated)_

### Creating and Initializing a Mutable Array

- [arrayWithCapacity:](arraywithcapacity_.md) — Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.
- [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) — Creates and returns a mutable array containing the contents of the file specified by the given path.
- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.
- [initWithContentsOfURL:](initwithcontentsofurl_.md) — Initialized a newly allocated mutable array with the contents of the location specified by a given URL.
