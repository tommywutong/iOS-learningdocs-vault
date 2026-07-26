---
title: 'init(for:migrationPlan:configurations:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontainer/init(for:migrationplan:configurations:)-qof9'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontainer/init(for:migrationplan:configurations:)-qof9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontainer/init%28for%3Amigrationplan%3Aconfigurations%3A%29-qof9.json'
content_hash: 'sha256:fd816cfd3b742d81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContainer](../modelcontainer.md)

# init(for:migrationPlan:configurations:)

<sub>Initializer</sub>

Creates a model container using the specified schema, migration plan, and zero or more configurations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(for givenSchema: Schema, migrationPlan: (any SchemaMigrationPlan.Type)? = nil, configurations: ModelConfiguration...) throws
```

## Parameters

- `givenSchema` — A schema that maps your app’s model classes to the associated data in the app’s persistent storage. For more information, see [Schema](../schema.md).

- `migrationPlan` — A plan that describes the evolution of your app’s schema and how the container migrates between specific versions. For more information, see [SchemaMigrationPlan](../schemamigrationplan.md).

- `configurations` — A list of configurations that describe how the container manages the persisted data for specific groups of models. For more information, see [ModelConfiguration](../modelconfiguration.md).

## Discussion

> [!important] Important
> A container must have at least one configuration. If you don’t specify any, the framework creates an instance of [ModelConfiguration](../modelconfiguration.md) for you by combining your app’s entitlements with the type’s default values.

## See Also

### Creating a model container

- [init(for:migrationPlan:configurations:)](<init(for_migrationplan_configurations_)-1czix.md>) — Creates a model container using the specified schema, migration plan, and configurations.
- [init(for:migrationPlan:configurations:)](<init(for_migrationplan_configurations_)-8s4ts.md>) — Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [PersistentModel](../persistentmodel.md) — An interface that enables SwiftData to manage a Swift class as a stored model.
- [ModelConfiguration](../modelconfiguration.md) — A type that describes the configuration of an app’s schema or specific group of models.
- [Schema](../schema.md) — An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [SchemaMigrationPlan](../schemamigrationplan.md) — An interface for describing the evolution of a schema and how to migrate between specific versions.
