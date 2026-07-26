---
title: SchemaMigrationPlan
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schemamigrationplan
source_url: 'https://developer.apple.com/documentation/swiftdata/schemamigrationplan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schemamigrationplan.json'
content_hash: 'sha256:5395a0fff949c709'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# SchemaMigrationPlan

<sub>Protocol</sub>

An interface for describing the evolution of a schema and how to migrate between specific versions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SchemaMigrationPlan : SendableMetatype
```

## Relationships

- **Inherits From**: [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Managing versioned schemas

- [schemas](schemamigrationplan/schemas.md)
- [VersionedSchema](versionedschema.md) — An interface for describing a specific version of a schema, including the models it contains.

### Managing migration stages

- [stages](schemamigrationplan/stages.md)
- [MigrationStage](migrationstage.md) — Describes a migration between two versions of the same schema.

## See Also

### Creating a model container

- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-1czix.md>) — Creates a model container using the specified schema, migration plan, and configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-8s4ts.md>) — Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-qof9.md>) — Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [PersistentModel](persistentmodel.md) — An interface that enables SwiftData to manage a Swift class as a stored model.
- [ModelConfiguration](modelconfiguration.md) — A type that describes the configuration of an app’s schema or specific group of models.
- [Schema](schema.md) — An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
