---
title: name
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/name
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/name.json'
content_hash: 'sha256:ed7becec933af539'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# name

<sub>Instance Property</sub>

The name of the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String! { get set }
```

## Discussion

The name is used only as a means of distinguishing mappings in a model. If not specified, the value defaults to SOURCE-\>DESTINATION.

## See Also

### Managing Mapping Information

- [mappingType](mappingtype.md) — The mapping type for the entity mapping.
- [entityMigrationPolicyClassName](entitymigrationpolicyclassname.md) — The class name of the migration policy for the entity mapping.
- [attributeMappings](attributemappings.md) — The array of attribute mappings for the entity mapping.
- [relationshipMappings](relationshipmappings.md) — The array of relationship mappings for the entity mapping.
- [userInfo](userinfo.md) — The user info dictionary for the entity mapping.
