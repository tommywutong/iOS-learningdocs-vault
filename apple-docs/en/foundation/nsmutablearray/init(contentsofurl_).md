---
title: 'init(contentsOfURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/init(contentsofurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/init(contentsofurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/init%28contentsofurl%3A%29.json'
content_hash: 'sha256:a115bc3d15659f61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# init(contentsOfURL:)

<sub>Initializer</sub>

Creates and returns a mutable array containing the contents specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOfURL url: URL)
```

## Parameters

- `url` — The location of the file containing a string representation of a mutable array produced by the [- writeToURL:atomically:](<../nsarray/write(to_atomically_).md>) method.

## Return Value

A mutable array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into a mutable array.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable even if the array is mutable.

## See Also

### Related Documentation

- [- writeToURL:atomically:](<../nsarray/write(to_atomically_).md>) — Writes the contents of the array to the location specified by a given URL. _(deprecated)_

### Creating and Initializing a Mutable Array

- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.
