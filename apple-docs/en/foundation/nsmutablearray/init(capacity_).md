---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/init%28capacity%3A%29.json'
content_hash: 'sha256:88b42eb1ea81e05b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# init(capacity:)

<sub>Initializer</sub>

Returns an array, initialized with enough memory to initially hold a given number of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity numItems: Int)
```

## Parameters

- `numItems` — The initial capacity of the new array.

## Return Value

An array initialized with enough memory to hold `numItems` objects. The returned object might be different than the original receiver.

## Discussion

Mutable arrays expand as needed; `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer.

## See Also

### Creating and Initializing a Mutable Array

- [init(contentsOfURL:)](<init(contentsofurl_).md>) — Creates and returns a mutable array containing the contents specified by a given URL.
- [- init](<init().md>) — Initializes a newly allocated array.
