---
title: 'init(from:forSourceModel:destinationModel:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmappingmodel/init(from:forsourcemodel:destinationmodel:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmappingmodel/init(from:forsourcemodel:destinationmodel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmappingmodel/init%28from%3Aforsourcemodel%3Adestinationmodel%3A%29.json'
content_hash: 'sha256:58c9a1c2c8dcdae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMappingModel](../nsmappingmodel.md)

# init(from:forSourceModel:destinationModel:)

<sub>Initializer</sub>

Returns the mapping model that will translate data from the source to the destination model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(from bundles: [Bundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)
```

## Parameters

- `bundles` — An array of bundles in which to search for mapping models.

- `sourceModel` — The managed object model for the source store.

- `destinationModel` — The managed object model for the destination store.

## Return Value

Returns the mapping model to translate data from `sourceModel` to `destinationModel`. If a suitable mapping model cannot be found, returns `nil`.

## Discussion

This method is a companion to the [+ mergedModelFromBundles:](<../nsmanagedobjectmodel/mergedmodel(from_).md>) and [+ mergedModelFromBundles:forStoreMetadata:](<../nsmanagedobjectmodel/mergedmodel(from_forstoremetadata_).md>) methods. In this case, the framework uses the version information from the models to locate the appropriate mapping model in the available bundles.

## See Also

### Related Documentation

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)

### Creating a Mapping

- [+ inferredMappingModelForSourceModel:destinationModel:error:](<inferredmappingmodel(forsourcemodel_destinationmodel_).md>) — Returns a newly created mapping model that will migrate data from the source to the destination model.
- [- initWithContentsOfURL:](<init(contentsof_).md>) — Returns a mapping model initialized from a given URL.
