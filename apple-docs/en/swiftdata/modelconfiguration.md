---
title: ModelConfiguration
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelconfiguration
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration.json'
content_hash: 'sha256:47832b7f0f038dfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ModelConfiguration

<sub>Structure</sub>

A type that describes the configuration of an app’s schema or specific group of models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ModelConfiguration
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [DataStoreConfiguration](datastoreconfiguration.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a model configuration

- [init(isStoredInMemoryOnly:)](<modelconfiguration/init(isstoredinmemoryonly_).md>) — Creates a basic model configuration.
- [init(for:isStoredInMemoryOnly:)](<modelconfiguration/init(for_isstoredinmemoryonly_).md>) — Creates a model configuration for the specified model types.
- [init(_:schema:isStoredInMemoryOnly:allowsSave:groupContainer:cloudKitDatabase:)](<modelconfiguration/init(__schema_isstoredinmemoryonly_allowssave_groupcontainer_cloudkitdatabase_).md>) — Creates a named model configuration for the specified schema.
- [init(_:schema:url:allowsSave:cloudKitDatabase:)](<modelconfiguration/init(__schema_url_allowssave_cloudkitdatabase_).md>) — Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.

### Accessing configuration details

- [url](modelconfiguration/url.md) — The on-disk location of the schema’s persistent storage.
- [allowsSave](modelconfiguration/allowssave.md) — A Boolean value that determines whether the associated persistent storage is writable.
- [isStoredInMemoryOnly](modelconfiguration/isstoredinmemoryonly.md) — A Boolean value that determines whether the associated persistent storage is ephemeral and exists only in memory.

### Sharing and syncing the model store

- [cloudKitContainerIdentifier](modelconfiguration/cloudkitcontaineridentifier.md) — The identifier of the configuration’s CloudKit database container.
- [cloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.property.md) — The option to use when detecting the container of the preferred CloudKit database.
- [CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct.md) — A type that describes the options for detecting a CloudKit database.
- [groupAppContainerIdentifier](modelconfiguration/groupappcontaineridentifier.md) — The identifier of the configuration’s app group container.
- [groupContainer](modelconfiguration/groupcontainer-swift.property.md) — The option to use when detecting the preferred app group container.
- [GroupContainer](modelconfiguration/groupcontainer-swift.struct.md) — A type that describes the options for detecting an app group container.

## See Also

### Creating a model container

- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-1czix.md>) — Creates a model container using the specified schema, migration plan, and configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-8s4ts.md>) — Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-qof9.md>) — Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [PersistentModel](persistentmodel.md) — An interface that enables SwiftData to manage a Swift class as a stored model.
- [Schema](schema.md) — An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [SchemaMigrationPlan](schemamigrationplan.md) — An interface for describing the evolution of a schema and how to migrate between specific versions.
