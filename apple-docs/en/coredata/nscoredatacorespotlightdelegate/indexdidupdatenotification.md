---
title: indexDidUpdateNotification
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatenotification
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatenotification.json'
content_hash: 'sha256:ce4450e5b9fcfc86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# indexDidUpdateNotification

<sub>Type Property</sub>

The notification the delegate posts after Spotlight updates the index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let indexDidUpdateNotification: Notification.Name
```

## Discussion

The notification’s `userInfo` dictionary contains the keys [NSStoreUUIDKey](../nsstoreuuidkey.md) and [NSPersistentHistoryTokenKey](../nspersistenthistorytokenkey.md).

## See Also

### Updating the Index

- [- searchableIndex:reindexAllSearchableItemsWithAcknowledgementHandler:](<searchableindex(__reindexallsearchableitemswithacknowledgementhandler_).md>) — Reindexes all searchable items and clears any local state.
- [- searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:](<searchableindex(__reindexsearchableitemswithidentifiers_acknowledgementhandler_).md>) — Reindexes the searchable items for the specified identifiers.
