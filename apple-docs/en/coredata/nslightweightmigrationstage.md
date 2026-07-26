---
title: NSLightweightMigrationStage
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nslightweightmigrationstage
source_url: 'https://developer.apple.com/documentation/coredata/nslightweightmigrationstage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nslightweightmigrationstage.json'
content_hash: 'sha256:f741ba917ee995d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSLightweightMigrationStage

<sub>Class</sub>

An object that describes a series of models suitable for lightweight migration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSLightweightMigrationStage
```

## Overview

Use [NSLightweightMigrationStage](nslightweightmigrationstage.md) when you have a series of models to migrate and those models are compatible with lightweight migrations. Instances of this class supplement your custom migration stages and help maintain a consistent stage order for the entire migration.

## Relationships

- **Inherits From**: [NSMigrationStage](nsmigrationstage.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a migration stage

- [init(_:)](<nslightweightmigrationstage/init(__).md>) — Creates a lightweight migration stage with the specified version checksums.

### Accessing the checksums

- [versionChecksums](nslightweightmigrationstage/versionchecksums.md) — The array of version checksums.

## See Also

### Migration stages

- [NSCustomMigrationStage](nscustommigrationstage.md) — An object that enables you to participate in the migration between two versions of the same model.
- [NSMigrationStage](nsmigrationstage.md) — An abstract base class for describing an individual stage of a migration.
