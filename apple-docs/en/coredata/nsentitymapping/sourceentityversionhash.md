---
title: sourceEntityVersionHash
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/sourceentityversionhash
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/sourceentityversionhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/sourceentityversionhash.json'
content_hash: 'sha256:05fe5062b2d1cbae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# sourceEntityVersionHash

<sub>Instance Property</sub>

The version hash of the source entity for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceEntityVersionHash: Data? { get set }
```

## Discussion

The version hash is calculated by Core Data based on the property values of the entity (see `NSEntityDescription`’s [versionHash](../nsentitydescription/versionhash.md) method). The `sourceEntityVersionHash` must equal the version hash of the source entity represented by the mapping.

## See Also

### Related Documentation

- [destinationEntityVersionHash](destinationentityversionhash.md) — The version hash for the destination entity for the entity mapping.

### Managing Source Information

- [sourceEntityName](sourceentityname.md) — The source entity name for the entity mapping.
- [sourceExpression](sourceexpression.md) — The source expression for the entity mapping.
