---
title: usesStoreSpecificMigrationManager
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/usesstorespecificmigrationmanager
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/usesstorespecificmigrationmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/usesstorespecificmigrationmanager.json'
content_hash: 'sha256:a54447f78b116d40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# usesStoreSpecificMigrationManager

<sub>Instance Property</sub>

A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var usesStoreSpecificMigrationManager: Bool { get set }
```

## Return Value

[true](../../swift/true.md) if the receiver uses a store-specific migration manager, otherwise [false](../../swift/false.md).

## Discussion

[true](../../swift/true.md) if the receiver uses a store-specific migration manager, otherwise [false](../../swift/false.md). The default value is [true](../../swift/true.md).

A store-specific migration manager class is not guaranteed to perform any of the migration manager delegate callbacks or update values for the observable properties.

## See Also

### Customizing the Manager

- [userInfo](userinfo.md) — The user info for the migration manager.
