---
title: NSEntityMappingType.removeEntityMappingType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymappingtype/removeentitymappingtype
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymappingtype/removeentitymappingtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymappingtype/removeentitymappingtype.json'
content_hash: 'sha256:919cbb2758ad0269'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMappingType](../nsentitymappingtype.md)

# NSEntityMappingType.removeEntityMappingType

<sub>Case</sub>

Specifies that this entity is not present in the destination model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case removeEntityMappingType
```

## Discussion

Instances of the entity only exist in the source—source instances are not mapped to destination.

## See Also

### Constants

- [NSUndefinedEntityMappingType](undefinedentitymappingtype.md) — Specifies that the developer handles destination instance creation.
- [NSCustomEntityMappingType](customentitymappingtype.md) — Specifies a custom mapping.
- [NSAddEntityMappingType](addentitymappingtype.md) — Specifies that this is a new entity in the destination model.
- [NSCopyEntityMappingType](copyentitymappingtype.md) — Specifies that source instances are migrated as-is.
- [NSTransformEntityMappingType](transformentitymappingtype.md) — Specifies that entity exists in source and destination and is mapped.
