---
title: entityMappings
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmappingmodel/entitymappings
source_url: 'https://developer.apple.com/documentation/coredata/nsmappingmodel/entitymappings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmappingmodel/entitymappings.json'
content_hash: 'sha256:36cad0553ff79197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMappingModel](../nsmappingmodel.md)

# entityMappings

<sub>Instance Property</sub>

The entity mappings for the mapping model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entityMappings: [NSEntityMapping]! { get set }
```

## Discussion

The order of the mappings in the array determines the order in which they will be processed during migration.

## See Also

### Managing Entity Mappings

- [entityMappingsByName](entitymappingsbyname.md) — The entity mappings for the mapping model, keyed by name.
