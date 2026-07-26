---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/delegate
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/delegate.json'
content_hash: 'sha256:3a346794a3d04077'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# delegate

<sub>Instance Property</sub>

The query’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var delegate: (any NSMetadataQueryDelegate)? { get set }
```

## Discussion

This property contains an object that acts as the query’s delegate, or `nil`. The delegate must implement the [NSMetadataQueryDelegate](../nsmetadataquerydelegate.md). Pass `nil` to remove the current delegate.

## See Also

### Configuring queries

- [searchScopes](searchscopes.md) — An array containing the search scopes.
- [predicate](predicate.md) — The predicate used to filter query results.
- [sortDescriptors](sortdescriptors.md) — An array of sort descriptor objects.
- [valueListAttributes](valuelistattributes.md) — An array of attributes whose values are gathered by the query.
- [groupingAttributes](groupingattributes.md) — An array of grouping attributes. (read-only)
- [notificationBatchingInterval](notificationbatchinginterval.md) — The interval at which notification of updated results occurs.
- [searchItems](searchitems.md) — An array of objects that define the query’s scope.
