---
title: 'performCustomValidation(forMapping:manager:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitymigrationpolicy/performcustomvalidation(formapping:manager:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/performcustomvalidation(formapping:manager:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymigrationpolicy/performcustomvalidation%28formapping%3Amanager%3A%29.json'
content_hash: 'sha256:75ccf6fa051f047d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMigrationPolicy](../nsentitymigrationpolicy.md)

# performCustomValidation(forMapping:manager:)

<sub>Instance Method</sub>

Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performCustomValidation(forMapping mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

## Parameters

- `mapping` — The mapping object in use.

- `manager` — The migration manager performing the migration.

## Discussion

This method is called before the default save validation is performed by the framework.

If you implement this method, you must manually obtain the collection of objects you are interested in validating.

## See Also

### Customizing Stages of the Mapping Life Cycle

- [- beginEntityMapping:manager:error:](<begin(__with_).md>) — Sets up state information before the start of a given entity mapping.
- [- createDestinationInstancesForSourceInstance:entityMapping:manager:error:](<createdestinationinstances(forsource_in_manager_).md>) — Creates the destination instance(s) for a given source instance.
- [- endInstanceCreationForEntityMapping:manager:error:](<endinstancecreation(formapping_manager_).md>) — Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [- createRelationshipsForDestinationInstance:entityMapping:manager:error:](<createrelationships(fordestination_in_manager_).md>) — Constructs the relationships between the newly-created destination instances.
- [- endRelationshipCreationForEntityMapping:manager:error:](<endrelationshipcreation(formapping_manager_).md>) — Indicates the end of the relationship creation stage for the specified entity mapping.
- [- endEntityMapping:manager:error:](<end(__manager_).md>) — Performs cleanup at the end of the migration, from any phase of the mapping.
