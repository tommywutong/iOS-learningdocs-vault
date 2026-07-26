---
title: NSMigrationManagerKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanagerkey
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanagerkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanagerkey.json'
content_hash: 'sha256:110e3d246a944db2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMigrationManagerKey

<sub>Global Variable</sub>

Key for the migration manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMigrationManagerKey: String
```

## Discussion

To access this key in a custom value expression string in the Xcode mapping model editor use `$manager`.

## See Also

### Constants

- [NSMigrationSourceObjectKey](nsmigrationsourceobjectkey.md) — Key for the source object.
- [NSMigrationDestinationObjectKey](nsmigrationdestinationobjectkey.md) — Key for the destination object.
- [NSMigrationEntityMappingKey](nsmigrationentitymappingkey.md) — Key for the entity mapping object.
- [NSMigrationPropertyMappingKey](nsmigrationpropertymappingkey.md) — Key for the property mapping object.
- [NSMigrationEntityPolicyKey](nsmigrationentitypolicykey.md) — Key for the entity migration policy object.
