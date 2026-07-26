---
title: MigrationStage
framework: SwiftData
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/migrationstage
source_url: 'https://developer.apple.com/documentation/swiftdata/migrationstage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/migrationstage.json'
content_hash: 'sha256:6eae529d07f405cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# MigrationStage

<sub>Enumeration</sub>

Describes a migration between two versions of the same schema.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MigrationStage
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Migration stages

- [MigrationStage.lightweight(fromVersion:toVersion:)](<migrationstage/lightweight(fromversion_toversion_).md>)
- [MigrationStage.custom(fromVersion:toVersion:willMigrate:didMigrate:)](<migrationstage/custom(fromversion_toversion_willmigrate_didmigrate_).md>)

## See Also

### Managing migration stages

- [stages](schemamigrationplan/stages.md)
