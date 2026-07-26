---
title: elements
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchindexdescription/elements
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchindexdescription/elements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchindexdescription/elements.json'
content_hash: 'sha256:fe201b69747431f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchIndexDescription](../nsfetchindexdescription.md)

# elements

<sub>Instance Property</sub>

An array of fetch index element descriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var elements: [NSFetchIndexElementDescription] { get set }
```

## Discussion

Setting this property to an invalid value throws an exception, such as when the new value includes both R-tree and non-R-tree elements.

## See Also

### Inspecting an Index Description

- [entity](entity.md) — The entity description for the fetch index description.
- [name](name.md) — The name of the fetch index description.
- [partialIndexPredicate](partialindexpredicate.md) — A predicate that selects rows for indexing, if the index is a partial index.
