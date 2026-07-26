---
title: Schema
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema
source_url: 'https://developer.apple.com/documentation/swiftdata/schema'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema.json'
content_hash: 'sha256:619ffe908a0b1d85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# Schema

<sub>Class</sub>

An object that maps model classes to data in the model store, and helps with the migration of that data between releases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Schema
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a schema

- [init(_:version:)](<schema/init(__version_)-8el78.md>)
- [init(_:version:)](<schema/init(__version_)-8jo9o.md>)
- [init(versionedSchema:)](<schema/init(versionedschema_).md>)
- [VersionedSchema](versionedschema.md) — An interface for describing a specific version of a schema, including the models it contains.
- [init()](<schema/init().md>)
- [Schema components](schemacomponents.md) — Specify the constituent parts of your schema, including entities, attributes, and relationships.

### Accessing entities

- [entities](schema/entities.md)
- [entitiesByName](schema/entitiesbyname.md)
- [Entity](schema/entity.md) — An object that provides a blueprint for the associated model class.

### Accessing version details

- [schemaEncodingVersion](schema/schemaencodingversion.md)
- [encodingVersion](schema/encodingversion.md)

### Saving and loading

- [save(to:)](<schema/save(to_).md>)
- [load(from:)](<schema/load(from_).md>)

### Classes

- [Index](schema/index.md)
- [Unique](schema/unique.md)

### Structures

- [PropertyMetadata](schema/propertymetadata.md)
- [Version](schema/version-swift.struct.md)

### Initializers

- [init(_:version:)](<schema/init(__version_)-1aea5.md>)

### Instance Properties

- [version](schema/version-swift.property.md)

### Instance Methods

- [entity(for:)](<schema/entity(for_).md>)

### Type Methods

- [entityName(for:)](<schema/entityname(for_).md>)

## See Also

### Creating a model container

- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-1czix.md>) — Creates a model container using the specified schema, migration plan, and configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-8s4ts.md>) — Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-qof9.md>) — Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [PersistentModel](persistentmodel.md) — An interface that enables SwiftData to manage a Swift class as a stored model.
- [ModelConfiguration](modelconfiguration.md) — A type that describes the configuration of an app’s schema or specific group of models.
- [SchemaMigrationPlan](schemamigrationplan.md) — An interface for describing the evolution of a schema and how to migrate between specific versions.
