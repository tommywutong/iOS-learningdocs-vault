---
title: 'init(byMerging:forStoreMetadata:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/init(bymerging:forstoremetadata:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init(bymerging:forstoremetadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/init%28bymerging%3Aforstoremetadata%3A%29.json'
content_hash: 'sha256:d030d2f251c6976f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# init(byMerging:forStoreMetadata:)

<sub>Initializer</sub>

Returns, for the version information in given metadata, a model merged from a given array of models.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(byMerging models: [NSManagedObjectModel], forStoreMetadata metadata: [String : Any])
```

## Parameters

- `models` — An array of instances of `NSManagedObjectModel`.

- `metadata` — A dictionary containing version information from the metadata for a persistent store.

## Return Value

A  merged model from `models` for the version information in `metadata`. If a model cannot be created to match the version information in `metadata`, returns `nil`.

## Discussion

This is the companion method to [+ mergedModelFromBundles:forStoreMetadata:](<mergedmodel(from_forstoremetadata_).md>).

## See Also

### Creating a managed object model

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes the managed object model using the model file at the specified URL.
- [- init](<init().md>) — Initializes an empty managed object model.
- [+ mergedModelFromBundles:](<mergedmodel(from_).md>) — Returns a model created by merging all the models found in given bundles.
- [+ mergedModelFromBundles:forStoreMetadata:](<mergedmodel(from_forstoremetadata_).md>) — Returns a merged model from a specified array for the version information in provided metadata.
- [+ modelByMergingModels:](<init(bymerging_).md>) — Creates a single model from an array of existing models.
