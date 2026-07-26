---
title: isStopped
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/isstopped
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/isstopped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/isstopped.json'
content_hash: 'sha256:e7fdfdf85ad9d340'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# isStopped

<sub>Instance Property</sub>

A Boolean value that indicates whether the query has stopped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isStopped: Bool { get }
```

## Discussion

This property contains [true](../../swift/true.md) when the receiver has stopped the query; otherwise, [false](../../swift/false.md).

## See Also

### Running queries

- [started](isstarted.md) — A Boolean value that indicates whether the query has started. (read-only)
- [- startQuery](<start().md>) — Attempts to start the query.
- [gathering](isgathering.md) — A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [- stopQuery](<stop().md>) — Stops the receiver’s current query from gathering any further results.
