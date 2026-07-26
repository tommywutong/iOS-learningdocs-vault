---
title: 'init(byMerging:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/init(bymerging:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init(bymerging:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/init%28bymerging%3A%29.json'
content_hash: 'sha256:a765ac421e3637c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# init(byMerging:)

<sub>Initializer</sub>

Creates a single model from an array of existing models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(byMerging models: [NSManagedObjectModel]?)
```

## Parameters

- `models` — An array of instances of `NSManagedObjectModel`.

## Return Value

A single model made by combining the models in `models`.

## Discussion

You use this method to combine multiple models (typically from different frameworks) into one.

## See Also

### Creating a managed object model

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes the managed object model using the model file at the specified URL.
- [- init](<init().md>) — Initializes an empty managed object model.
- [+ mergedModelFromBundles:](<mergedmodel(from_).md>) — Returns a model created by merging all the models found in given bundles.
- [+ mergedModelFromBundles:forStoreMetadata:](<mergedmodel(from_forstoremetadata_).md>) — Returns a merged model from a specified array for the version information in provided metadata.
- [+ modelByMergingModels:forStoreMetadata:](<init(bymerging_forstoremetadata_).md>) — Returns, for the version information in given metadata, a model merged from a given array of models.
