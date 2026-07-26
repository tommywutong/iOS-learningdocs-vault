---
title: mappingType
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/mappingtype
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/mappingtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/mappingtype.json'
content_hash: 'sha256:a60859838f8ae6bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# mappingType

<sub>Instance Property</sub>

The mapping type for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mappingType: NSEntityMappingType { get set }
```

## Discussion

If you specify a custom entity mapping type, you must specify a value for the migration policy class name as well (see [entityMigrationPolicyClassName](entitymigrationpolicyclassname.md)).

## See Also

### Managing Mapping Information

- [name](name.md) — The name of the entity mapping.
- [entityMigrationPolicyClassName](entitymigrationpolicyclassname.md) — The class name of the migration policy for the entity mapping.
- [attributeMappings](attributemappings.md) — The array of attribute mappings for the entity mapping.
- [relationshipMappings](relationshipmappings.md) — The array of relationship mappings for the entity mapping.
- [userInfo](userinfo.md) — The user info dictionary for the entity mapping.
