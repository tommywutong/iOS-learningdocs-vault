---
title: 'init(contentsOf:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/init%28contentsof%3A%29.json'
content_hash: 'sha256:51ff3a35a5a30df7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# init(contentsOf:)

<sub>Initializer</sub>

Initializes the managed object model using the model file at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOf url: URL)
```

## Parameters

- `url` — An URL object specifying the location of a model file.

## Return Value

A managed object model initialized using the file at `url`.

## See Also

### Related Documentation

- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)

### Creating a managed object model

- [- init](<init().md>) — Initializes an empty managed object model.
- [+ mergedModelFromBundles:](<mergedmodel(from_).md>) — Returns a model created by merging all the models found in given bundles.
- [+ mergedModelFromBundles:forStoreMetadata:](<mergedmodel(from_forstoremetadata_).md>) — Returns a merged model from a specified array for the version information in provided metadata.
- [+ modelByMergingModels:](<init(bymerging_).md>) — Creates a single model from an array of existing models.
- [+ modelByMergingModels:forStoreMetadata:](<init(bymerging_forstoremetadata_).md>) — Returns, for the version information in given metadata, a model merged from a given array of models.
