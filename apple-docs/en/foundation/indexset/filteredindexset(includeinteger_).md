---
title: 'filteredIndexSet(includeInteger:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/filteredindexset(includeinteger:)'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/filteredindexset(includeinteger:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/filteredindexset%28includeinteger%3A%29.json'
content_hash: 'sha256:0ff14c291d9f646d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# filteredIndexSet(includeInteger:)

<sub>Instance Method</sub>

Returns an IndexSet filtered according to the result of `includeInteger`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filteredIndexSet(includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet
```

## Parameters

- `includeInteger` — The predicate which decides if an integer will be included in the result or not.

## See Also

### Selecting Elements

- [filteredIndexSet(in:includeInteger:)](<filteredindexset(in_includeinteger_)-6cdvc.md>) — Returns an IndexSet filtered according to the result of `includeInteger`.
- [filteredIndexSet(in:includeInteger:)](<filteredindexset(in_includeinteger_)-9dn86.md>) — Returns an IndexSet filtered according to the result of `includeInteger`.
