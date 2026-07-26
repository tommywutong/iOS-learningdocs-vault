---
title: 'MigrationStage.custom(fromVersion:toVersion:willMigrate:didMigrate:)'
framework: SwiftData
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/migrationstage/custom(fromversion:toversion:willmigrate:didmigrate:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/migrationstage/custom(fromversion:toversion:willmigrate:didmigrate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/migrationstage/custom%28fromversion%3Atoversion%3Awillmigrate%3Adidmigrate%3A%29.json'
content_hash: 'sha256:974f80753e13746a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [MigrationStage](../migrationstage.md)

# MigrationStage.custom(fromVersion:toVersion:willMigrate:didMigrate:)

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case custom(fromVersion: any VersionedSchema.Type, toVersion: any VersionedSchema.Type, willMigrate: (@Sendable (ModelContext) throws -> Void)?, didMigrate: (@Sendable (ModelContext) throws -> Void)?)
```

## See Also

### Migration stages

- [MigrationStage.lightweight(fromVersion:toVersion:)](<lightweight(fromversion_toversion_).md>)
