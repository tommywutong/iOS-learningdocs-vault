---
title: 'init(forStoreWith:model:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+（15.0 起废弃）, iPadOS 11.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.13+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:model:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:model:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/init%28forstorewith%3Amodel%3A%29.json'
content_hash: 'sha256:37658260e67225f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# init(forStoreWith:model:)

<sub>Initializer</sub>

Creates a Core Spotlight delegate with the specified store description and managed object model.

> [!warning] Deprecated
> Use [- initForStoreWithDescription:coordinator:](<init(forstorewith_coordinator_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
convenience init(forStoreWith description: NSPersistentStoreDescription, model: NSManagedObjectModel)
```

## Parameters

- `description` — An object that describes the persistent store that contains the entities to index.

- `model` — The managed object model that contains the definitions of the entities to index.

## See Also

### Creating a Core Spotlight Delegate

- [- initForStoreWithDescription:coordinator:](<init(forstorewith_coordinator_).md>) — Creates a Core Spotlight delegate with the specified store description and coordinator.
