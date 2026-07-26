---
title: isStarted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/isstarted
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/isstarted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/isstarted.json'
content_hash: 'sha256:5fac1dc6dcc68e5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# isStarted

<sub>Instance Property</sub>

A Boolean value that indicates whether the query has started. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isStarted: Bool { get }
```

## Discussion

This property contains [true](../../swift/true.md) when the receiver has executed the `startQuery` method; otherwise, [false](../../swift/false.md).

## See Also

### Running queries

- [- startQuery](<start().md>) — Attempts to start the query.
- [gathering](isgathering.md) — A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [stopped](isstopped.md) — A Boolean value that indicates whether the query has stopped.
- [- stopQuery](<stop().md>) — Stops the receiver’s current query from gathering any further results.
