---
title: sortDescriptors
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/sortdescriptors
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/sortdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/sortdescriptors.json'
content_hash: 'sha256:e5a305a170aaf3ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# sortDescriptors

<sub>Instance Property</sub>

An array of sort descriptor objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sortDescriptors: [NSSortDescriptor] { get set }
```

## Discussion

Setting this property while a query is running stops the query and discards the current results. The receiver immediately starts a new query.

## See Also

### Configuring queries

- [searchScopes](searchscopes.md) — An array containing the search scopes.
- [predicate](predicate.md) — The predicate used to filter query results.
- [valueListAttributes](valuelistattributes.md) — An array of attributes whose values are gathered by the query.
- [groupingAttributes](groupingattributes.md) — An array of grouping attributes. (read-only)
- [notificationBatchingInterval](notificationbatchinginterval.md) — The interval at which notification of updated results occurs.
- [delegate](delegate.md) — The query’s delegate.
- [searchItems](searchitems.md) — An array of objects that define the query’s scope.
