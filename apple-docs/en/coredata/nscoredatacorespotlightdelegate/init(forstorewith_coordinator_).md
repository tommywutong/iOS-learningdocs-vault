---
title: 'init(forStoreWith:coordinator:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:coordinator:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:coordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/init%28forstorewith%3Acoordinator%3A%29.json'
content_hash: 'sha256:4fec7d09c187fd06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# init(forStoreWith:coordinator:)

<sub>Initializer</sub>

Creates a Core Spotlight delegate with the specified store description and coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(forStoreWith description: NSPersistentStoreDescription, coordinator psc: NSPersistentStoreCoordinator)
```

## Parameters

- `description` — An object that describes the persistent store that contains the entities to index.

- `psc` — The persistent store coordinator, which you initialize with the managed object model that contains the definitions of the entities to index.

## Discussion

After you initialize a Core Spotlight delegate, call the [- startSpotlightIndexing](<startspotlightindexing().md>) to begin indexing your store’s contents.

> [!note] Note
> If you initialize your Core Spotlight delegate using this method, you don’t need to set the [NSCoreDataCoreSpotlightExporter](../nscoredatacorespotlightexporter.md) option on the specified store description.

## See Also

### Creating a Core Spotlight Delegate

- [- initForStoreWithDescription:model:](<init(forstorewith_model_).md>) — Creates a Core Spotlight delegate with the specified store description and managed object model. _(deprecated)_
