---
title: entityMigrationPolicyClassName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/entitymigrationpolicyclassname
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/entitymigrationpolicyclassname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/entitymigrationpolicyclassname.json'
content_hash: 'sha256:50c4f11f79837117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# entityMigrationPolicyClassName

<sub>Instance Property</sub>

The class name of the migration policy for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entityMigrationPolicyClassName: String? { get set }
```

## Discussion

If not specified, the default migration class name is [NSEntityMigrationPolicy](../nsentitymigrationpolicy.md). You can specify a subclass to provide custom behavior.

## See Also

### Managing Mapping Information

- [name](name.md) — The name of the entity mapping.
- [mappingType](mappingtype.md) — The mapping type for the entity mapping.
- [attributeMappings](attributemappings.md) — The array of attribute mappings for the entity mapping.
- [relationshipMappings](relationshipmappings.md) — The array of relationship mappings for the entity mapping.
- [userInfo](userinfo.md) — The user info dictionary for the entity mapping.
