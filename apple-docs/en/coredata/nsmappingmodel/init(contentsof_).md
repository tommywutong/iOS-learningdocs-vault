---
title: 'init(contentsOf:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmappingmodel/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmappingmodel/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmappingmodel/init%28contentsof%3A%29.json'
content_hash: 'sha256:c27cbe4839170016'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMappingModel](../nsmappingmodel.md)

# init(contentsOf:)

<sub>Initializer</sub>

Returns a mapping model initialized from a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(contentsOf url: URL?)
```

## Parameters

- `url` — The location of an archived mapping model.

## Return Value

A mapping model initialized from `url`.

## See Also

### Creating a Mapping

- [+ mappingModelFromBundles:forSourceModel:destinationModel:](<init(from_forsourcemodel_destinationmodel_).md>) — Returns the mapping model that will translate data from the source to the destination model.
- [+ inferredMappingModelForSourceModel:destinationModel:error:](<inferredmappingmodel(forsourcemodel_destinationmodel_).md>) — Returns a newly created mapping model that will migrate data from the source to the destination model.
