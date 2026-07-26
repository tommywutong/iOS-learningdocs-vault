---
title: 'mergedModel(from:forStoreMetadata:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/mergedmodel%28from%3Aforstoremetadata%3A%29.json'
content_hash: 'sha256:74ebfa5b1e5cf443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# mergedModel(from:forStoreMetadata:)

<sub>Type Method</sub>

Returns a merged model from a specified array for the version information in provided metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func mergedModel(from bundles: [Bundle]?, forStoreMetadata metadata: [String : Any]) -> NSManagedObjectModel?
```

## Parameters

- `bundles` — An array of bundles.

- `metadata` — A dictionary containing version information from the metadata for a persistent store.

## Return Value

The managed object model used to create the store for the metadata. If a model cannot be created to match the version information specified by `metadata`, returns `nil`.

## Discussion

This method is a companion to [+ mergedModelFromBundles:](<mergedmodel(from_).md>).

## See Also

### Creating a managed object model

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes the managed object model using the model file at the specified URL.
- [- init](<init().md>) — Initializes an empty managed object model.
- [+ mergedModelFromBundles:](<mergedmodel(from_).md>) — Returns a model created by merging all the models found in given bundles.
- [+ modelByMergingModels:](<init(bymerging_).md>) — Creates a single model from an array of existing models.
- [+ modelByMergingModels:forStoreMetadata:](<init(bymerging_forstoremetadata_).md>) — Returns, for the version information in given metadata, a model merged from a given array of models.
