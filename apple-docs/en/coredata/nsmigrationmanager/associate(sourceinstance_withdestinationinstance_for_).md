---
title: 'associate(sourceInstance:withDestinationInstance:for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/associate%28sourceinstance%3Awithdestinationinstance%3Afor%3A%29.json'
content_hash: 'sha256:0cf719b5c7b1cec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# associate(sourceInstance:withDestinationInstance:for:)

<sub>Instance Method</sub>

Associates a given source managed object instance with an array of destination instances for a given property mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func associate(sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, for entityMapping: NSEntityMapping)
```

## Parameters

- `sourceInstance` — A source managed object.

- `destinationInstance` — The destination manage object for `sourceInstance`.

- `entityMapping` — The entity mapping to use to associate `sourceInstance` with the object in `destinationInstances`.

## Discussion

Data migration is performed as a three-stage process (first create the data, then relate the data, then validate the data). You use this method to associate data between the source and destination stores, in order to allow for relationship creation or fix-up after the creation stage.

This method is called in the default implementation of `NSEntityMigrationPolicy`’s [- createDestinationInstancesForSourceInstance:entityMapping:manager:error:](<../nsentitymigrationpolicy/createdestinationinstances(forsource_in_manager_).md>) method.

## See Also

### Managing Sources and Destinations

- [- destinationInstancesForEntityMappingNamed:sourceInstances:](<destinationinstances(forentitymappingname_sourceinstances_).md>) — Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.
- [- sourceInstancesForEntityMappingNamed:destinationInstances:](<sourceinstances(forentitymappingname_destinationinstances_).md>) — Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.
