---
title: predicate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/predicate
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/predicate.json'
content_hash: 'sha256:b12fb552d510d185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# predicate

<sub>Instance Property</sub>

The predicate used to filter query results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var predicate: NSPredicate? { get set }
```

## Discussion

Setting this property while a query is running stops the query and discards the current results. The receiver immediately starts a new query.

## See Also

### Configuring queries

- [searchScopes](searchscopes.md) — An array containing the search scopes.
- [sortDescriptors](sortdescriptors.md) — An array of sort descriptor objects.
- [valueListAttributes](valuelistattributes.md) — An array of attributes whose values are gathered by the query.
- [groupingAttributes](groupingattributes.md) — An array of grouping attributes. (read-only)
- [notificationBatchingInterval](notificationbatchinginterval.md) — The interval at which notification of updated results occurs.
- [delegate](delegate.md) — The query’s delegate.
- [searchItems](searchitems.md) — An array of objects that define the query’s scope.
