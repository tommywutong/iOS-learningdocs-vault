---
title: uniquenessConstraints
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/uniquenessconstraints
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/uniquenessconstraints'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/uniquenessconstraints.json'
content_hash: 'sha256:eaabcf3d364df21c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# uniquenessConstraints

<sub>Instance Property</sub>

An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uniquenessConstraints: [[Any]] { get set }
```

## Discussion

Each inner array contains one or more [NSAttributeDescription](../nsattributedescription.md) objects or strings that contain the names of attributes on the entity.

This value forms part of the entity’s version hash. Stores that don’t support uniqueness constraints must refuse to initialize when receiving a model that contains such constraints.

> [!note] Note
> Uniqueness constraint violations can be computationally expensive to handle. The recommendation is to use only one uniqueness constraint per entity hierarchy, although subentites may extend a superentity’s constraint.

## See Also

### Configuring indexes and constraints

- [indexes](indexes.md) — An array of fetch index descriptions for the entity.
- [compoundIndexes](compoundindexes.md) — The compound indexes for the entity as an array of arrays. _(deprecated)_
