---
title: 'mergedModel(from:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectmodel/mergedmodel%28from%3A%29.json'
content_hash: 'sha256:60a1d15776a37f99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectModel](../nsmanagedobjectmodel.md)

# mergedModel(from:)

<sub>Type Method</sub>

Returns a model created by merging all the models found in given bundles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func mergedModel(from bundles: [Bundle]?) -> NSManagedObjectModel?
```

## Parameters

- `bundles` — An array of instances of `NSBundle` to search. If you specify `nil`, then the main bundle is searched.

## Return Value

A model created by merging all the models found in `bundles`.

## See Also

### Creating a managed object model

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes the managed object model using the model file at the specified URL.
- [- init](<init().md>) — Initializes an empty managed object model.
- [+ mergedModelFromBundles:forStoreMetadata:](<mergedmodel(from_forstoremetadata_).md>) — Returns a merged model from a specified array for the version information in provided metadata.
- [+ modelByMergingModels:](<init(bymerging_).md>) — Creates a single model from an array of existing models.
- [+ modelByMergingModels:forStoreMetadata:](<init(bymerging_forstoremetadata_).md>) — Returns, for the version information in given metadata, a model merged from a given array of models.
