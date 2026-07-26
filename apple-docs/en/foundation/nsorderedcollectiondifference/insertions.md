---
title: insertions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectiondifference/insertions
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/insertions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference/insertions.json'
content_hash: 'sha256:8e1bf5bb3c11284d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)

# insertions

<sub>Instance Property</sub>

A collection of insertion change objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var insertions: [NSOrderedCollectionChange] { get }
```

## See Also

### Accessing Changes

- [hasChanges](haschanges.md) — A Boolean value that indicates if the difference has changes.
- [removals](removals.md) — A collection of removal change objects.
- [NSOrderedCollectionChange](../nsorderedcollectionchange.md) — An object that represents an indexed change within an ordered collection.
- [NSCollectionChangeType](../nscollectionchangetype.md) — The type of change represented in computing the difference of an ordered collection.
