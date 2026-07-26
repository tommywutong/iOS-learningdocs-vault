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
doc_path: /documentation/coredata/nsmigrationmanager/userinfo
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/userinfo.json'
content_hash: 'sha256:ce50698b748fc9e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# userInfo

<sub>Instance Property</sub>

The user info for the migration manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

You can use the user info dictionary to aid the customization of your migration process.

## See Also

### Customizing the Manager

- [usesStoreSpecificMigrationManager](usesstorespecificmigrationmanager.md) — A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.
