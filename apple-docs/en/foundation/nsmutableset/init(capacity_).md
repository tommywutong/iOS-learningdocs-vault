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
doc_path: '/documentation/foundation/nsmutableset/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/init%28capacity%3A%29.json'
content_hash: 'sha256:2a15065b757f2f0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# init(capacity:)

<sub>Initializer</sub>

Returns an initialized mutable set with a given initial capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity numItems: Int)
```

## Parameters

- `numItems` — The initial capacity of the set.

## Return Value

An initialized mutable set with initial capacity to hold `numItems` members. The returned set might be different than the original receiver.

## Discussion

Mutable sets allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer for `NSMutableSet`.

## See Also

### Creating a mutable set

- [- init](<init().md>) — Initializes a newly allocated set.
