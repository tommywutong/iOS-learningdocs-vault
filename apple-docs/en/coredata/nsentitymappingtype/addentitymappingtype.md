---
title: NSEntityMappingType.addEntityMappingType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymappingtype/addentitymappingtype
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymappingtype/addentitymappingtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymappingtype/addentitymappingtype.json'
content_hash: 'sha256:8fff89a378d6a37a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMappingType](../nsentitymappingtype.md)

# NSEntityMappingType.addEntityMappingType

<sub>Case</sub>

Specifies that this is a new entity in the destination model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case addEntityMappingType
```

## Discussion

Instances of the entity only exist in the destination.

## See Also

### Constants

- [NSUndefinedEntityMappingType](undefinedentitymappingtype.md) — Specifies that the developer handles destination instance creation.
- [NSCustomEntityMappingType](customentitymappingtype.md) — Specifies a custom mapping.
- [NSRemoveEntityMappingType](removeentitymappingtype.md) — Specifies that this entity is not present in the destination model.
- [NSCopyEntityMappingType](copyentitymappingtype.md) — Specifies that source instances are migrated as-is.
- [NSTransformEntityMappingType](transformentitymappingtype.md) — Specifies that entity exists in source and destination and is mapped.
