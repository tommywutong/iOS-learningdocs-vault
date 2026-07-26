---
title: 'inferredMappingModel(forSourceModel:destinationModel:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmappingmodel/inferredmappingmodel(forsourcemodel:destinationmodel:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmappingmodel/inferredmappingmodel(forsourcemodel:destinationmodel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmappingmodel/inferredmappingmodel%28forsourcemodel%3Adestinationmodel%3A%29.json'
content_hash: 'sha256:b0fe2b0534ae7eb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMappingModel](../nsmappingmodel.md)

# inferredMappingModel(forSourceModel:destinationModel:)

<sub>Type Method</sub>

Returns a newly created mapping model that will migrate data from the source to the destination model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func inferredMappingModel(forSourceModel sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel
```

## Parameters

- `sourceModel` — The source managed object model.

- `destinationModel` — The destination managed object model.

## Return Value

A newly-created mapping model to migrate data from the source to the destination model. If the mapping model can not be created, returns `nil`.

## Discussion

A model will be created only if all changes are simple enough to be able to reasonably infer a mapping (for example, removing or renaming an attribute, adding an optional attribute or relationship, or adding renaming or deleting an entity). Element IDs are used to track renamed properties and entities.

## See Also

### Creating a Mapping

- [+ mappingModelFromBundles:forSourceModel:destinationModel:](<init(from_forsourcemodel_destinationmodel_).md>) — Returns the mapping model that will translate data from the source to the destination model.
- [- initWithContentsOfURL:](<init(contentsof_).md>) — Returns a mapping model initialized from a given URL.
