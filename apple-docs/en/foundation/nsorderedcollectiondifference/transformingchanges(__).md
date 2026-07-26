---
title: 'transformingChanges(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedcollectiondifference/transformingchanges(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/transformingchanges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference/transformingchanges%28_%3A%29.json'
content_hash: 'sha256:9a7fa09c6beaba43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)

# transformingChanges(_:)

<sub>Instance Method</sub>

Create a new ordered collection difference by mapping over this difference’s members, processing the change objects with the block provided.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func transformingChanges(_ block: (NSOrderedCollectionChange) -> NSOrderedCollectionChange) -> CollectionDifference<Any>
```

## Parameters

- `block` — A block receives an ordered collection change and returns an updated change.

## Return Value

A new ordered collection difference.
