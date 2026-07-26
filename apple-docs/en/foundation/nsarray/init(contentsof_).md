---
title: 'init(contentsOf:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28contentsof%3A%29.json'
content_hash: 'sha256:0ce32629c104f927'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(contentsOf:)

<sub>Initializer</sub>

Initializes a newly allocated array with the contents of the location specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOf url: URL)
```

## Parameters

- `url` — The location of a file containing a string representation of an array produced by the `writeToURL:atomically:` method.

## Return Value

An array initialized to contain the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into an array. The returned object might be different than the original receiver.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.
