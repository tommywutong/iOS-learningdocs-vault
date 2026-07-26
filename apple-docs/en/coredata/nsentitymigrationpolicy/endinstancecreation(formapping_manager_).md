---
title: 'endInstanceCreation(forMapping:manager:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitymigrationpolicy/endinstancecreation(formapping:manager:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/endinstancecreation(formapping:manager:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymigrationpolicy/endinstancecreation%28formapping%3Amanager%3A%29.json'
content_hash: 'sha256:41d48629f3a39afd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMigrationPolicy](../nsentitymigrationpolicy.md)

# endInstanceCreation(forMapping:manager:)

<sub>Instance Method</sub>

Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func endInstanceCreation(forMapping mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

## Parameters

- `mapping` — The mapping object in use.

- `manager` — The migration manager performing the migration.

## Discussion

You can override this method to clean up state from the creation of destination or to prepare state for the creation of relationships.

## See Also

### Customizing Stages of the Mapping Life Cycle

- [- beginEntityMapping:manager:error:](<begin(__with_).md>) — Sets up state information before the start of a given entity mapping.
- [- createDestinationInstancesForSourceInstance:entityMapping:manager:error:](<createdestinationinstances(forsource_in_manager_).md>) — Creates the destination instance(s) for a given source instance.
- [- createRelationshipsForDestinationInstance:entityMapping:manager:error:](<createrelationships(fordestination_in_manager_).md>) — Constructs the relationships between the newly-created destination instances.
- [- endRelationshipCreationForEntityMapping:manager:error:](<endrelationshipcreation(formapping_manager_).md>) — Indicates the end of the relationship creation stage for the specified entity mapping.
- [- performCustomValidationForEntityMapping:manager:error:](<performcustomvalidation(formapping_manager_).md>) — Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [- endEntityMapping:manager:error:](<end(__manager_).md>) — Performs cleanup at the end of the migration, from any phase of the mapping.
