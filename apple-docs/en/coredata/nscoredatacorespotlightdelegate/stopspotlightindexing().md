---
title: stopSpotlightIndexing()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscoredatacorespotlightdelegate/stopspotlightindexing()
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/stopspotlightindexing()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/stopspotlightindexing%28%29.json'
content_hash: 'sha256:76f6665ad9c3698b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# stopSpotlightIndexing()

<sub>Instance Method</sub>

Stops the indexing of the store’s entities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func stopSpotlightIndexing()
```

## Discussion

After you call this method, the delegate no longer posts notifications about index changes.

## See Also

### Managing the Index

- [- attributeSetForObject:](<attributeset(for_).md>) — Returns the searchable attributes for the specified managed object.
- [- deleteSpotlightIndexWithCompletionHandler:](<deletespotlightindex(completionhandler_).md>) — Deletes all searchable items from the configured index.
- [- startSpotlightIndexing](<startspotlightindexing().md>) — Starts the indexing of the store’s entities.
