---
title: 'begin(_:with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitymigrationpolicy/begin(_:with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/begin(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymigrationpolicy/begin%28_%3Awith%3A%29.json'
content_hash: 'sha256:28fc9ad815854fdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMigrationPolicy](../nsentitymigrationpolicy.md)

# begin(_:with:)

<sub>Instance Method</sub>

Sets up state information before the start of a given entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func begin(_ mapping: NSEntityMapping, with manager: NSMigrationManager) throws
```

## Parameters

- `mapping` — The mapping object in use.

- `manager` — The migration manager performing the migration.

## Discussion

This method is the precursor to the creation stage. In a custom class, you can implement this method to set up any state information that will be useful for the duration of the migration.

## See Also

### Related Documentation

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)

### Customizing Stages of the Mapping Life Cycle

- [- createDestinationInstancesForSourceInstance:entityMapping:manager:error:](<createdestinationinstances(forsource_in_manager_).md>) — Creates the destination instance(s) for a given source instance.
- [- endInstanceCreationForEntityMapping:manager:error:](<endinstancecreation(formapping_manager_).md>) — Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [- createRelationshipsForDestinationInstance:entityMapping:manager:error:](<createrelationships(fordestination_in_manager_).md>) — Constructs the relationships between the newly-created destination instances.
- [- endRelationshipCreationForEntityMapping:manager:error:](<endrelationshipcreation(formapping_manager_).md>) — Indicates the end of the relationship creation stage for the specified entity mapping.
- [- performCustomValidationForEntityMapping:manager:error:](<performcustomvalidation(formapping_manager_).md>) — Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [- endEntityMapping:manager:error:](<end(__manager_).md>) — Performs cleanup at the end of the migration, from any phase of the mapping.
