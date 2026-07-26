---
title: 'filteredIndexSet(in:includeInteger:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/filteredindexset(in:includeinteger:)-9dn86'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/filteredindexset(in:includeinteger:)-9dn86'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/filteredindexset%28in%3Aincludeinteger%3A%29-9dn86.json'
content_hash: 'sha256:2ff0aead9d65a9bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# filteredIndexSet(in:includeInteger:)

<sub>Instance Method</sub>

Returns an IndexSet filtered according to the result of `includeInteger`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filteredIndexSet(in range: ClosedRange<IndexSet.Element>, includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet
```

## Parameters

- `range` — A range of integers. For each integer in the range that intersects the integers in the IndexSet, then the `includeInteger` predicate will be invoked.

- `includeInteger` — The predicate which decides if an integer will be included in the result or not.

## See Also

### Selecting Elements

- [filteredIndexSet(in:includeInteger:)](<filteredindexset(in_includeinteger_)-6cdvc.md>) — Returns an IndexSet filtered according to the result of `includeInteger`.
- [filteredIndexSet(includeInteger:)](<filteredindexset(includeinteger_).md>) — Returns an IndexSet filtered according to the result of `includeInteger`.
