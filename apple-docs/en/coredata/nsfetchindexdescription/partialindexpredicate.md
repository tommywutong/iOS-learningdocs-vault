---
title: partialIndexPredicate
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchindexdescription/partialindexpredicate
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchindexdescription/partialindexpredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchindexdescription/partialindexpredicate.json'
content_hash: 'sha256:e009514be7ae2da3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchIndexDescription](../nsfetchindexdescription.md)

# partialIndexPredicate

<sub>Instance Property</sub>

A predicate that selects rows for indexing, if the index is a partial index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var partialIndexPredicate: NSPredicate? { get set }
```

## See Also

### Inspecting an Index Description

- [elements](elements.md) — An array of fetch index element descriptions.
- [entity](entity.md) — The entity description for the fetch index description.
- [name](name.md) — The name of the fetch index description.
