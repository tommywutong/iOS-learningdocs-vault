---
title: 'initWithContentsOfURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/initwithcontentsofurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/initwithcontentsofurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/initwithcontentsofurl%3A.json'
content_hash: 'sha256:36399a22648a133c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# initWithContentsOfURL:

<sub>Instance Method</sub>

Initialized a newly allocated mutable array with the contents of the location specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSMutableArray<id> *) initWithContentsOfURL:(NSURL *) url;
```

## Parameters

- `url` — The location of a file containing a string representation of a mutable array produced by [- writeToURL:atomically:](<../nsarray/write(to_atomically_).md>) method.

## Return Value

A mutable array initialized to contain the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into a mutable array. The returned objects must be different than the original receiver.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`,`NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## See Also

### Related Documentation

- [- writeToURL:atomically:](<../nsarray/write(to_atomically_).md>) — Writes the contents of the array to the location specified by a given URL. _(deprecated)_

### Creating and Initializing a Mutable Array

- [arrayWithCapacity:](arraywithcapacity_.md) — Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.
- [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) — Creates and returns a mutable array containing the contents of the file specified by the given path.
- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.
- [initWithContentsOfFile:](initwithcontentsoffile_.md) — Initializes a newly allocated mutable array with the contents of the file specified by a given path
