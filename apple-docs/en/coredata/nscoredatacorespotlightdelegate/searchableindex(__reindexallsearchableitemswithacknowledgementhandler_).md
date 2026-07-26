---
title: 'searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex%28_%3Areindexallsearchableitemswithacknowledgementhandler%3A%29.json'
content_hash: 'sha256:16c70c4375b718b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)

<sub>Instance Method</sub>

Reindexes all searchable items and clears any local state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Void)
```

## Parameters

- `searchableIndex` — The index that requires reindexing.

- `acknowledgementHandler` — The handler to call when you finish saving client state information.

## Discussion

For more information, see [searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)](<../../corespotlight/cssearchableindexdelegate/searchableindex(__reindexallsearchableitemswithacknowledgementhandler_).md>).

## See Also

### Updating the Index

- [indexDidUpdateNotification](indexdidupdatenotification.md) — The notification the delegate posts after Spotlight updates the index.
- [- searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:](<searchableindex(__reindexsearchableitemswithidentifiers_acknowledgementhandler_).md>) — Reindexes the searchable items for the specified identifiers.
