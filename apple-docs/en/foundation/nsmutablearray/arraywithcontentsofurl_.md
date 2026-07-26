---
title: 'arrayWithContentsOfURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/arraywithcontentsofurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/arraywithcontentsofurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/arraywithcontentsofurl%3A.json'
content_hash: 'sha256:63dee01d93b50897'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# arrayWithContentsOfURL:

<sub>Type Method</sub>

Creates and returns a mutable array containing the contents specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSMutableArray<id> *) arrayWithContentsOfURL:(NSURL *) url;
```

## Parameters

- `url` — The location of the file containing a string representation of a mutable array produced by the `writeToURL:atomically:` method.

## Return Value

A mutable array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into a mutable array.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable even if the array is mutable.
