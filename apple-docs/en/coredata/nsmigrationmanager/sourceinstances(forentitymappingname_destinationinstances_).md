---
title: 'sourceInstances(forEntityMappingName:destinationInstances:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/sourceinstances(forentitymappingname:destinationinstances:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/sourceinstances(forentitymappingname:destinationinstances:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/sourceinstances%28forentitymappingname%3Adestinationinstances%3A%29.json'
content_hash: 'sha256:7312cc5016ad91cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# sourceInstances(forEntityMappingName:destinationInstances:)

<sub>Instance Method</sub>

Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sourceInstances(forEntityMappingName mappingName: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]
```

## Parameters

- `mappingName` — The name of an entity mapping in use.

- `destinationInstances` — A array of managed objects in the destination store.

## Return Value

An array containing the managed object instances in the source store used to create `destinationInstances` using the entity mapping named `mappingName`. If `destinationInstances` is `nil`, all of the source instances used to create the destination instance for this property mapping are returned.

## Discussion

This method throws an `NSInvalidArgumentException` exception if `mappingName` is not a valid mapping name.

## See Also

### Managing Sources and Destinations

- [- associateSourceInstance:withDestinationInstance:forEntityMapping:](<associate(sourceinstance_withdestinationinstance_for_).md>) — Associates a given source managed object instance with an array of destination instances for a given property mapping.
- [- destinationInstancesForEntityMappingNamed:sourceInstances:](<destinationinstances(forentitymappingname_sourceinstances_).md>) — Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.
