---
title: 'arrayWithContentsOfURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/arraywithcontentsofurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/arraywithcontentsofurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/arraywithcontentsofurl%3A.json'
content_hash: 'sha256:d4ec42f4504fceb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# arrayWithContentsOfURL:

<sub>Type Method</sub>

Creates and returns an array containing the contents specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSArray<id> *) arrayWithContentsOfURL:(NSURL *) url;
```

## Parameters

- `url` — The location of a file containing a string representation of an array produced by the `writeToURL:atomically:` method.

## Return Value

An array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into an array.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.
