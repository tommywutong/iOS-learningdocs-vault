---
title: sourceEntityName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/sourceentityname
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/sourceentityname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/sourceentityname.json'
content_hash: 'sha256:aad6eaa966681d36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# sourceEntityName

<sub>Instance Property</sub>

The source entity name for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceEntityName: String? { get set }
```

## Discussion

Mappings are not directly bound to entity descriptions; you can use the [- sourceEntityForEntityMapping:](<../nsmigrationmanager/sourceentity(for_).md>) method on the migration manager to retrieve the entity description for this entity name.

## See Also

### Related Documentation

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
- [destinationEntityName](destinationentityname.md) — The destination entity name for the entity mapping.

### Managing Source Information

- [sourceEntityVersionHash](sourceentityversionhash.md) — The version hash of the source entity for the entity mapping.
- [sourceExpression](sourceexpression.md) — The source expression for the entity mapping.
