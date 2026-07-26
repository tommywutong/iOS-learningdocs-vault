---
title: 'destinationInstances(forEntityMappingName:sourceInstances:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/destinationinstances(forentitymappingname:sourceinstances:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationinstances(forentitymappingname:sourceinstances:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/destinationinstances%28forentitymappingname%3Asourceinstances%3A%29.json'
content_hash: 'sha256:f6c76c1c10f8204b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# destinationInstances(forEntityMappingName:sourceInstances:)

<sub>Instance Method</sub>

Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func destinationInstances(forEntityMappingName mappingName: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]
```

## Parameters

- `mappingName` — The name of an entity mapping in use.

- `sourceInstances` — A array of managed objects in the source store.

## Return Value

An array containing the managed object instances created in the destination store for the entity mapping named `mappingName` for `sourceInstances`. If `sourceInstances` is `nil`, all of the destination instances created by the specified property mapping are returned.

## Discussion

This method throws an `NSInvalidArgumentException` exception if `mappingName` is not a valid mapping name.

## See Also

### Managing Sources and Destinations

- [- associateSourceInstance:withDestinationInstance:forEntityMapping:](<associate(sourceinstance_withdestinationinstance_for_).md>) — Associates a given source managed object instance with an array of destination instances for a given property mapping.
- [- sourceInstancesForEntityMappingNamed:destinationInstances:](<sourceinstances(forentitymappingname_destinationinstances_).md>) — Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.
