---
title: 'moveAssets(at:to:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/moveassets(at:to:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/moveassets(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/moveassets%28at%3Ato%3A%29.json'
content_hash: 'sha256:a8bc5e10d4641fa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# moveAssets(at:to:)

<sub>Instance Method</sub>

Moves the assets at the specified indexes in the asset collection to a new index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func moveAssets(at fromIndexes: IndexSet, to toIndex: Int)
```

## Parameters

- `fromIndexes` — The indexes of the assets to be moved in the asset collection.

- `toIndex` — The index at which to place the moved assets, relative to the collection’s ordering after removing the items at `indexes`.

## Discussion

When you call this method, Photos first removes the items in the `indexes` parameter from the collection, and then inserts them at the location specified by the `toIndex` parameter.

To ensure that the index set you specify is valid even if the asset collection has changed since you fetched it, create a change request with a snapshot of the asset collection’s contents using the [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) method before rearranging assets.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](title.md) — The displayed name of the asset collection.
- [- addAssets:](<addassets(__).md>) — Adds the specified assets to the asset collection.
- [- insertAssets:atIndexes:](<insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssets:](<removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- removeAssetsAtIndexes:](<removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
