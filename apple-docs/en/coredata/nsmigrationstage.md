---
title: NSMigrationStage
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationstage
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationstage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationstage.json'
content_hash: 'sha256:1011e153356ddad9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMigrationStage

<sub>Class</sub>

An abstract base class for describing an individual stage of a migration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMigrationStage
```

## Overview

> [!important] Important
> Don’t create instances of [NSMigrationStage](nsmigrationstage.md). Instead, use a concrete subclass, such as [NSLightweightMigrationStage](nslightweightmigrationstage.md) or [NSCustomMigrationStage](nscustommigrationstage.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSCustomMigrationStage](nscustommigrationstage.md), [NSLightweightMigrationStage](nslightweightmigrationstage.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing the purpose

- [label](nsmigrationstage/label.md) — The textual description of the migration stage’s purpose.

## See Also

### Migration stages

- [NSLightweightMigrationStage](nslightweightmigrationstage.md) — An object that describes a series of models suitable for lightweight migration.
- [NSCustomMigrationStage](nscustommigrationstage.md) — An object that enables you to participate in the migration between two versions of the same model.
