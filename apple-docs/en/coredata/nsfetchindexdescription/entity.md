---
title: entity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchindexdescription/entity
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchindexdescription/entity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchindexdescription/entity.json'
content_hash: 'sha256:84a7213d2cd3faab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchIndexDescription](../nsfetchindexdescription.md)

# entity

<sub>Instance Property</sub>

The entity description for the fetch index description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var entity: NSEntityDescription? { get }
```

## See Also

### Inspecting an Index Description

- [elements](elements.md) — An array of fetch index element descriptions.
- [name](name.md) — The name of the fetch index description.
- [partialIndexPredicate](partialindexpredicate.md) — A predicate that selects rows for indexing, if the index is a partial index.
