---
title: startSpotlightIndexing()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscoredatacorespotlightdelegate/startspotlightindexing()
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/startspotlightindexing()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/startspotlightindexing%28%29.json'
content_hash: 'sha256:eb1154fc06130286'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# startSpotlightIndexing()

<sub>Instance Method</sub>

Starts the indexing of the store’s entities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func startSpotlightIndexing()
```

## Discussion

After you call this method, the delegate posts a notification whenever the index changes. The type of notification is [indexDidUpdateNotification](indexdidupdatenotification.md), and its `userInfo` dictionary contains the keys [NSStoreUUIDKey](../nsstoreuuidkey.md) and [NSPersistentHistoryTokenKey](../nspersistenthistorytokenkey.md).

## See Also

### Managing the Index

- [- attributeSetForObject:](<attributeset(for_).md>) — Returns the searchable attributes for the specified managed object.
- [- deleteSpotlightIndexWithCompletionHandler:](<deletespotlightindex(completionhandler_).md>) — Deletes all searchable items from the configured index.
- [- stopSpotlightIndexing](<stopspotlightindexing().md>) — Stops the indexing of the store’s entities.
