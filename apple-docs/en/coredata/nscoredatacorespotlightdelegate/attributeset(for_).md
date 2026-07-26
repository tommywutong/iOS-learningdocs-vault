---
title: 'attributeSet(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nscoredatacorespotlightdelegate/attributeset(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/attributeset(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/attributeset%28for%3A%29.json'
content_hash: 'sha256:0de32b3062d13bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# attributeSet(for:)

<sub>Instance Method</sub>

Returns the searchable attributes for the specified managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func attributeSet(for object: NSManagedObject) -> CSSearchableItemAttributeSet?
```

## Parameters

- `object` — The managed object to index.

## Return Value

An instance of [CSSearchableItemAttributeSet](../../corespotlight/cssearchableitemattributeset.md) that provides the searchable item’s attributes.

## Discussion

> [!important] Important
> If you enable [indexedBySpotlight](../nspropertydescription/isindexedbyspotlight.md) on a property description that describes a relationship, override this method and return the necessary set of attributes. Core Data doesn’t automatically infer indexable information for relationships.

To prevent Core Spotlight from indexing a specific managed object, override this method and return `nil` for that object.

## See Also

### Managing the Index

- [- deleteSpotlightIndexWithCompletionHandler:](<deletespotlightindex(completionhandler_).md>) — Deletes all searchable items from the configured index.
- [- startSpotlightIndexing](<startspotlightindexing().md>) — Starts the indexing of the store’s entities.
- [- stopSpotlightIndexing](<stopspotlightindexing().md>) — Stops the indexing of the store’s entities.
