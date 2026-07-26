---
title: destinationEntityVersionHash
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/destinationentityversionhash
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/destinationentityversionhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/destinationentityversionhash.json'
content_hash: 'sha256:87818d6ef94d5ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# destinationEntityVersionHash

<sub>Instance Property</sub>

The version hash for the destination entity for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var destinationEntityVersionHash: Data? { get set }
```

## Discussion

The version hash is calculated by Core Data based on the property values of the entity (see `NSEntityDescription`’s [versionHash](../nsentitydescription/versionhash.md) method). The `destinationEntityVersionHash` must equal the version hash of the destination entity represented by the mapping.

## See Also

### Related Documentation

- [sourceEntityVersionHash](sourceentityversionhash.md) — The version hash of the source entity for the entity mapping.

### Managing Destination Information

- [destinationEntityName](destinationentityname.md) — The destination entity name for the entity mapping.
