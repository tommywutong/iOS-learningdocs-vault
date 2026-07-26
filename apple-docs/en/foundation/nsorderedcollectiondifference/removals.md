---
title: removals
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectiondifference/removals
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/removals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference/removals.json'
content_hash: 'sha256:88bde6e12260005f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)

# removals

<sub>Instance Property</sub>

A collection of removal change objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var removals: [NSOrderedCollectionChange] { get }
```

## See Also

### Accessing Changes

- [hasChanges](haschanges.md) — A Boolean value that indicates if the difference has changes.
- [insertions](insertions.md) — A collection of insertion change objects.
- [NSOrderedCollectionChange](../nsorderedcollectionchange.md) — An object that represents an indexed change within an ordered collection.
- [NSCollectionChangeType](../nscollectionchangetype.md) — The type of change represented in computing the difference of an ordered collection.
