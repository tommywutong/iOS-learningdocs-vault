---
title: 'searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex%28_%3Areindexsearchableitemswithidentifiers%3Aacknowledgementhandler%3A%29.json'
content_hash: 'sha256:06e01f8aa7c4997b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)

<sub>Instance Method</sub>

Reindexes the searchable items for the specified identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler: @escaping () -> Void)
```

## Parameters

- `searchableIndex` — The index that contains the items that require reindexing.

- `identifiers` — An array of strings that identify the searchable items.

- `acknowledgementHandler` — The handler to call when you finish saving client state information.

## Discussion

For more information, see [- searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:](<searchableindex(__reindexsearchableitemswithidentifiers_acknowledgementhandler_).md>).

## See Also

### Updating the Index

- [indexDidUpdateNotification](indexdidupdatenotification.md) — The notification the delegate posts after Spotlight updates the index.
- [- searchableIndex:reindexAllSearchableItemsWithAcknowledgementHandler:](<searchableindex(__reindexallsearchableitemswithacknowledgementhandler_).md>) — Reindexes all searchable items and clears any local state.
