---
title: indexes
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/indexes
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/indexes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/indexes.json'
content_hash: 'sha256:7c7453d4cd664d1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# indexes

<sub>Instance Property</sub>

An array of fetch index descriptions for the entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var indexes: [NSFetchIndexDescription] { get set }
```

## Discussion

This value doesn’t form part of the entity’s version hash, and stores that don’t natively support indexing may ignore it.

> [!important] Important
> Set indexes last in a model. Changing an entity hierarchy in any way that affects the validity of indexes drops all existing indexes for entities in that hierarchy, such as adding or removing superentities or subentities, or adding and removing properties anywhere in the hierarchy.

## See Also

### Configuring indexes and constraints

- [uniquenessConstraints](uniquenessconstraints.md) — An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.
- [compoundIndexes](compoundindexes.md) — The compound indexes for the entity as an array of arrays. _(deprecated)_
