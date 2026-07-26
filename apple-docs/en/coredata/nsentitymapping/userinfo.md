---
title: userInfo
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/userinfo
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/userinfo.json'
content_hash: 'sha256:9af3799893807e1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# userInfo

<sub>Instance Property</sub>

The user info dictionary for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

You can use the info dictionary in any way that might be useful in your migration. You can set the contents of the dictionary directory or using the appropriate inspector in the Xcode mapping model editor.

## See Also

### Managing Mapping Information

- [name](name.md) — The name of the entity mapping.
- [mappingType](mappingtype.md) — The mapping type for the entity mapping.
- [entityMigrationPolicyClassName](entitymigrationpolicyclassname.md) — The class name of the migration policy for the entity mapping.
- [attributeMappings](attributemappings.md) — The array of attribute mappings for the entity mapping.
- [relationshipMappings](relationshipmappings.md) — The array of relationship mappings for the entity mapping.
