---
title: NSMigrationManager
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager.json'
content_hash: 'sha256:8e8b5c93af610659'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMigrationManager

<sub>Class</sub>

A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMigrationManager
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Migration Manager

- [- initWithSourceModel:destinationModel:](<nsmigrationmanager/init(sourcemodel_destinationmodel_).md>) — Initializes a migration manager instance with given source and destination models.

### Getting the Manager’s Configuration

- [destinationContext](nsmigrationmanager/destinationcontext.md) — The managed object context the migration manager uses for writing the destination persistent store.
- [destinationModel](nsmigrationmanager/destinationmodel.md) — The destination model for the migration manager.
- [mappingModel](nsmigrationmanager/mappingmodel.md) — The mapping model for the migration manager.
- [sourceContext](nsmigrationmanager/sourcecontext.md) — The managed object context the migration manager uses for reading the source persistent store.
- [sourceModel](nsmigrationmanager/sourcemodel.md) — The source model for the migration manager.
- [- destinationEntityForEntityMapping:](<nsmigrationmanager/destinationentity(for_).md>) — Returns the entity description for the destination entity of a given entity mapping.
- [- sourceEntityForEntityMapping:](<nsmigrationmanager/sourceentity(for_).md>) — Returns the entity description for the source entity of a given entity mapping.

### Customizing the Manager

- [userInfo](nsmigrationmanager/userinfo.md) — The user info for the migration manager.
- [usesStoreSpecificMigrationManager](nsmigrationmanager/usesstorespecificmigrationmanager.md) — A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.

### Managing Sources and Destinations

- [- associateSourceInstance:withDestinationInstance:forEntityMapping:](<nsmigrationmanager/associate(sourceinstance_withdestinationinstance_for_).md>) — Associates a given source managed object instance with an array of destination instances for a given property mapping.
- [- destinationInstancesForEntityMappingNamed:sourceInstances:](<nsmigrationmanager/destinationinstances(forentitymappingname_sourceinstances_).md>) — Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.
- [- sourceInstancesForEntityMappingNamed:destinationInstances:](<nsmigrationmanager/sourceinstances(forentitymappingname_destinationinstances_).md>) — Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.

### Performing a Migration

- [migrateStore(from:type:options:mapping:to:type:options:)](<nsmigrationmanager/migratestore(from_type_options_mapping_to_type_options_).md>) — Migrates the source store to the destination using the specified mapping model.
- [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<nsmigrationmanager/migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>) — Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model. _(deprecated)_

### Monitoring a Migration’s Progress

- [migrationProgress](nsmigrationmanager/migrationprogress.md) — A number between `0` and `1` that indicates the proportion of completeness of the migration.
- [currentEntityMapping](nsmigrationmanager/currententitymapping.md) — The entity mapping currently being processed.

### Aborting a Migration

- [- cancelMigrationWithError:](<nsmigrationmanager/cancelmigrationwitherror(__).md>) — Cancels the migration with a given error.
- [- reset](<nsmigrationmanager/reset().md>) — Resets the association tables for the migration.

### Deprecated

- [Deprecated Symbols](nsmigrationmanager-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Entity Mapping

- [NSMappingModel](nsmappingmodel.md) — A model instance that specifies how to map a model from a source to a destination managed object model.
- [NSEntityMapping](nsentitymapping.md) — A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [NSEntityMigrationPolicy](nsentitymigrationpolicy.md) — A policy instance that customizes the migration process for an entity mapping.
- [NSEntityMappingType](nsentitymappingtype.md) — The types for mapping an entity between a source model and a destination model.
- [NSPropertyMapping](nspropertymapping.md) — A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.
