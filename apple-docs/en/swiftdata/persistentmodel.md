---
title: PersistentModel
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/persistentmodel
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentmodel.json'
content_hash: 'sha256:b7c51d1cea9b6b1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# PersistentModel

<sub>Protocol</sub>

An interface that enables SwiftData to manage a Swift class as a stored model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PersistentModel : AnyObject, Observable, Hashable, Identifiable, SendableMetatype
```

## Relationships

- **Inherits From**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Observable](../observation/observable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a persistent model

- [init(backingData:)](<persistentmodel/init(backingdata_).md>)

### Identifying the model instance

- [persistentModelID](persistentmodel/persistentmodelid.md)
- [PersistentIdentifier](persistentidentifier.md) — A type that describes the aggregate identity of a SwiftData model.
- [modelContext](persistentmodel/modelcontext.md)

### Accessing a value by key path

- [getValue(forKey:)](<persistentmodel/getvalue(forkey_)-299oe.md>)
- [getValue(forKey:)](<persistentmodel/getvalue(forkey_)-3o59k.md>)
- [getValue(forKey:)](<persistentmodel/getvalue(forkey_)-4cs0c.md>)
- [getValue(forKey:)](<persistentmodel/getvalue(forkey_)-5m792.md>)
- [getValue(forKey:)](<persistentmodel/getvalue(forkey_)-998oq.md>)
- [getTransformableValue(forKey:)](<persistentmodel/gettransformablevalue(forkey_).md>)

### Modifying a value by key path

- [setValue(forKey:to:)](<persistentmodel/setvalue(forkey_to_)-18176.md>)
- [setValue(forKey:to:)](<persistentmodel/setvalue(forkey_to_)-3mmp2.md>)
- [setValue(forKey:to:)](<persistentmodel/setvalue(forkey_to_)-3uqwc.md>)
- [setValue(forKey:to:)](<persistentmodel/setvalue(forkey_to_)-8wepb.md>)
- [setValue(forKey:to:)](<persistentmodel/setvalue(forkey_to_)-xt24.md>)
- [setTransformableValue(forKey:to:)](<persistentmodel/settransformablevalue(forkey_to_).md>)

### Accessing supplementary information

- [schemaMetadata](persistentmodel/schemametadata.md)
- [persistentBackingData](persistentmodel/persistentbackingdata.md)
- [hasChanges](persistentmodel/haschanges.md)
- [isDeleted](persistentmodel/isdeleted.md)

### Internal

- [Internal symbols](persistentmodelinternal.md) — Restricted-use symbols that the framework requires for macro expansion and other internal tasks.

### Associated Types

- [Root](persistentmodel/root.md)

### Type Methods

- [createBackingData()](<persistentmodel/createbackingdata().md>)

### Default Implementations

- [Equatable Implementations](persistentmodel/equatable-implementations.md)
- [Hashable Implementations](persistentmodel/hashable-implementations.md)

## See Also

### Creating a model container

- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-1czix.md>) — Creates a model container using the specified schema, migration plan, and configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-8s4ts.md>) — Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [init(for:migrationPlan:configurations:)](<modelcontainer/init(for_migrationplan_configurations_)-qof9.md>) — Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [ModelConfiguration](modelconfiguration.md) — A type that describes the configuration of an app’s schema or specific group of models.
- [Schema](schema.md) — An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [SchemaMigrationPlan](schemamigrationplan.md) — An interface for describing the evolution of a schema and how to migrate between specific versions.
