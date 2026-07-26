---
title: 'replaceAssets(at:withAssets:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/replaceassets(at:withassets:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/replaceassets(at:withassets:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/replaceassets%28at%3Awithassets%3A%29.json'
content_hash: 'sha256:caa96dbbd2026cd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# replaceAssets(at:withAssets:)

<sub>Instance Method</sub>

Replaces the assets at the specified indexes in the asset collection with the specified assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func replaceAssets(at indexes: IndexSet, withAssets assets: any NSFastEnumeration)
```

## Parameters

- `indexes` — The indexes of the assets to be replaced in the asset collection.

- `assets` — An array of [PHAsset](../phasset.md) objects to be inserted into (or moved within) the asset collection.

## Discussion

To ensure that the index set you specify is valid even if the asset collection has changed since you fetched it, create a change request with a snapshot of the asset collection’s contents using the [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) method before rearranging assets.

> [!note] Note
> Assets from My Photo Stream or iCloud Shared Albums and assets synced to the device through iTunes cannot be added to collections. Transient asset collections (such as those created with the [+ transientAssetCollectionWithAssets:title:](<../phassetcollection/transientassetcollection(with_title_).md>) method) do not support adding or removing content.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](title.md) — The displayed name of the asset collection.
- [- addAssets:](<addassets(__).md>) — Adds the specified assets to the asset collection.
- [- insertAssets:atIndexes:](<insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssets:](<removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- removeAssetsAtIndexes:](<removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- moveAssetsAtIndexes:toIndex:](<moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.
