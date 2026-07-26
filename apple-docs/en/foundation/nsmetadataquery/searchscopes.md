---
title: searchScopes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/searchscopes
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/searchscopes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/searchscopes.json'
content_hash: 'sha256:bd281245a860e100'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# searchScopes

<sub>Instance Property</sub>

An array containing the search scopes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var searchScopes: [Any] { get set }
```

## Discussion

This array can contain `NSURL` or `NSString` objects that represent file-system directories or the search scopes for the query. For a list of valid search scopes, see [Metadata Query Search Scopes](../metadata-query-search-scopes.md). An empty array indicates that there is no limitation on where the query searches.

## See Also

### Related Documentation

- [File Metadata Search Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)

### Configuring queries

- [predicate](predicate.md) — The predicate used to filter query results.
- [sortDescriptors](sortdescriptors.md) — An array of sort descriptor objects.
- [valueListAttributes](valuelistattributes.md) — An array of attributes whose values are gathered by the query.
- [groupingAttributes](groupingattributes.md) — An array of grouping attributes. (read-only)
- [notificationBatchingInterval](notificationbatchinginterval.md) — The interval at which notification of updated results occurs.
- [delegate](delegate.md) — The query’s delegate.
- [searchItems](searchitems.md) — An array of objects that define the query’s scope.
