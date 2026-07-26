---
title: 'createDestinationInstances(forSource:in:manager:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitymigrationpolicy/createdestinationinstances(forsource:in:manager:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/createdestinationinstances(forsource:in:manager:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymigrationpolicy/createdestinationinstances%28forsource%3Ain%3Amanager%3A%29.json'
content_hash: 'sha256:12cbefdcd2a77e19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMigrationPolicy](../nsentitymigrationpolicy.md)

# createDestinationInstances(forSource:in:manager:)

<sub>Instance Method</sub>

Creates the destination instance(s) for a given source instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createDestinationInstances(forSource sInstance: NSManagedObject, in mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

## Parameters

- `sInstance` — The source instance for which to create destination instances.

- `mapping` — The mapping object in use.

- `manager` — The migration manager performing the migration.

## Discussion

This method is invoked by the migration manager on each source instance (as specified by the [sourceExpression](../nsentitymapping/sourceexpression.md) in the mapping) to create the corresponding destination instance(s). It also associates the source and destination instances by calling `NSMigrationManager`’s [- associateSourceInstance:withDestinationInstance:forEntityMapping:](<../nsmigrationmanager/associate(sourceinstance_withdestinationinstance_for_).md>) method.

### Special Considerations

If you override this method and do not invoke `super`, you must invoke `NSMigrationManager`’s [- associateSourceInstance:withDestinationInstance:forEntityMapping:](<../nsmigrationmanager/associate(sourceinstance_withdestinationinstance_for_).md>) to associate the source and destination instances as required. .

## See Also

### Customizing Stages of the Mapping Life Cycle

- [- beginEntityMapping:manager:error:](<begin(__with_).md>) — Sets up state information before the start of a given entity mapping.
- [- endInstanceCreationForEntityMapping:manager:error:](<endinstancecreation(formapping_manager_).md>) — Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [- createRelationshipsForDestinationInstance:entityMapping:manager:error:](<createrelationships(fordestination_in_manager_).md>) — Constructs the relationships between the newly-created destination instances.
- [- endRelationshipCreationForEntityMapping:manager:error:](<endrelationshipcreation(formapping_manager_).md>) — Indicates the end of the relationship creation stage for the specified entity mapping.
- [- performCustomValidationForEntityMapping:manager:error:](<performcustomvalidation(formapping_manager_).md>) — Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [- endEntityMapping:manager:error:](<end(__manager_).md>) — Performs cleanup at the end of the migration, from any phase of the mapping.
