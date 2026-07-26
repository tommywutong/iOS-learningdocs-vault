---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/init%28capacity%3A%29.json'
content_hash: 'sha256:4d0dd301b0dff4ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# init(capacity:)

<sub>Initializer</sub>

Returns an initialized mutable ordered set with a given initial capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity numItems: Int)
```

## Parameters

- `numItems` — The initial capacity of the new ordered set.

## Return Value

An initialized mutable ordered set with initial capacity to hold `numItems` members.

## Discussion

Mutable ordered sets allocate additional memory as needed, so `numItems` simply establishes the set’s initial capacity.

This method is a designated initializer of `NSMutableOrderedSet`.

## See Also

### Creating a Mutable Ordered Set

- [- init](<init().md>) — Initializes a newly allocated mutable ordered set.
