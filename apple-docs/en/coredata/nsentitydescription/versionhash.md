---
title: versionHash
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/versionhash
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/versionhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/versionhash.json'
content_hash: 'sha256:0a7452df95c89600'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# versionHash

<sub>Instance Property</sub>

The version hash for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionHash: Data { get }
```

## Discussion

The version hash is used to uniquely identify an entity based on the collection and configuration of properties for the entity. The version hash uses only values which affect the persistence of data and the user-defined [versionHashModifier](versionhashmodifier.md) value. (The values which affect persistence are: the name of the entity, the version hash of the superentity (if present), if the entity is abstract, and all of the version hashes for the properties.) This value is stored as part of the version information in the metadata for stores which use this entity, as well as a definition of an entity involved in an [NSEntityMapping](../nsentitymapping.md) object.

## See Also

### Managing versioning

- [versionHashModifier](versionhashmodifier.md) — The version hash modifier for the receiver.
