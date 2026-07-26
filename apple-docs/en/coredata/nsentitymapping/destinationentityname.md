---
title: destinationEntityName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/destinationentityname
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/destinationentityname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/destinationentityname.json'
content_hash: 'sha256:be48a5a547934a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# destinationEntityName

<sub>Instance Property</sub>

The destination entity name for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var destinationEntityName: String? { get set }
```

## Discussion

Mappings are not directly bound to entity descriptions. You can use the migration manager’s [- destinationEntityForEntityMapping:](<../nsmigrationmanager/destinationentity(for_).md>) method to retrieve the entity description for this entity name.

## See Also

### Related Documentation

- [sourceEntityName](sourceentityname.md) — The source entity name for the entity mapping.

### Managing Destination Information

- [destinationEntityVersionHash](destinationentityversionhash.md) — The version hash for the destination entity for the entity mapping.
