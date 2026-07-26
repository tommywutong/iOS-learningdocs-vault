---
title: Query()
framework: SwiftData
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/query()
source_url: 'https://developer.apple.com/documentation/swiftdata/query()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query%28%29.json'
content_hash: 'sha256:43032f8726ddef4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Query()

<sub>Macro</sub>

Fetches all instances of the attached model type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(accessor) @attached(peer, names: prefixed(`_`)) macro Query()
```

## See Also

### Model fetch

- [Filtering and sorting persistent data](filtering-and-sorting-persistent-data.md) — Manage data store presentation using predicates and dynamic queries.
- [Additional query macros](additionalquerymacros.md) — Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.
- [Query](query.md) — A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
- [FetchDescriptor](fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
