---
title: 'deleteSpotlightIndex(completionHandler:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/deletespotlightindex%28completionhandler%3A%29.json'
content_hash: 'sha256:f3cfbfd7febbdc5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# deleteSpotlightIndex(completionHandler:)

<sub>Instance Method</sub>

Deletes all searchable items from the configured index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func deleteSpotlightIndex(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func deleteSpotlightIndex() async throws
```

## Discussion

The closure returns no value and takes only a single parameter, which is an error object that contains information about issues preventing the deletion of searchable items, or `nil` if Core Spotlight successfully deletes all searchable items.

Depending on the cause of the issue, an error can originate from Core Data or from Core Spotlight. Make sure your app can handle both scenarios.

> [!note] Note
> You must call [- stopSpotlightIndexing](<stopspotlightindexing().md>) before you call this method; otherwise, Core Data immediately recreates the index.

## See Also

### Managing the Index

- [- attributeSetForObject:](<attributeset(for_).md>) — Returns the searchable attributes for the specified managed object.
- [- startSpotlightIndexing](<startspotlightindexing().md>) — Starts the indexing of the store’s entities.
- [- stopSpotlightIndexing](<stopspotlightindexing().md>) — Stops the indexing of the store’s entities.
