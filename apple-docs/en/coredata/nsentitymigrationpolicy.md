---
title: NSEntityMigrationPolicy
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymigrationpolicy
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymigrationpolicy.json'
content_hash: 'sha256:4d57a3f13a0112ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSEntityMigrationPolicy

<sub>Class</sub>

A policy instance that customizes the migration process for an entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSEntityMigrationPolicy
```

## Overview

You set the policy for an entity mapping by passing the name of the migration policy class as the argument to [entityMigrationPolicyClassName](nsentitymapping/entitymigrationpolicyclassname.md). Typically, you specify the name in the Xcode mapping model editor.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Customizing Stages of the Mapping Life Cycle

- [- beginEntityMapping:manager:error:](<nsentitymigrationpolicy/begin(__with_).md>) — Sets up state information before the start of a given entity mapping.
- [- createDestinationInstancesForSourceInstance:entityMapping:manager:error:](<nsentitymigrationpolicy/createdestinationinstances(forsource_in_manager_).md>) — Creates the destination instance(s) for a given source instance.
- [- endInstanceCreationForEntityMapping:manager:error:](<nsentitymigrationpolicy/endinstancecreation(formapping_manager_).md>) — Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [- createRelationshipsForDestinationInstance:entityMapping:manager:error:](<nsentitymigrationpolicy/createrelationships(fordestination_in_manager_).md>) — Constructs the relationships between the newly-created destination instances.
- [- endRelationshipCreationForEntityMapping:manager:error:](<nsentitymigrationpolicy/endrelationshipcreation(formapping_manager_).md>) — Indicates the end of the relationship creation stage for the specified entity mapping.
- [- performCustomValidationForEntityMapping:manager:error:](<nsentitymigrationpolicy/performcustomvalidation(formapping_manager_).md>) — Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [- endEntityMapping:manager:error:](<nsentitymigrationpolicy/end(__manager_).md>) — Performs cleanup at the end of the migration, from any phase of the mapping.

### Constants

- [NSMigrationManagerKey](nsmigrationmanagerkey.md) — Key for the migration manager.
- [NSMigrationSourceObjectKey](nsmigrationsourceobjectkey.md) — Key for the source object.
- [NSMigrationDestinationObjectKey](nsmigrationdestinationobjectkey.md) — Key for the destination object.
- [NSMigrationEntityMappingKey](nsmigrationentitymappingkey.md) — Key for the entity mapping object.
- [NSMigrationPropertyMappingKey](nsmigrationpropertymappingkey.md) — Key for the property mapping object.
- [NSMigrationEntityPolicyKey](nsmigrationentitypolicykey.md) — Key for the entity migration policy object.

## See Also

### Entity Mapping

- [NSMigrationManager](nsmigrationmanager.md) — A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [NSMappingModel](nsmappingmodel.md) — A model instance that specifies how to map a model from a source to a destination managed object model.
- [NSEntityMapping](nsentitymapping.md) — A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [NSEntityMappingType](nsentitymappingtype.md) — The types for mapping an entity between a source model and a destination model.
- [NSPropertyMapping](nspropertymapping.md) — A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.
