---
title: 'insertAssets(_:at:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/insertassets(_:at:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/insertassets(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/insertassets%28_%3Aat%3A%29.json'
content_hash: 'sha256:0db2957b25354222'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# insertAssets(_:at:)

<sub>Instance Method</sub>

Inserts the specified assets into the collection at the specified indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertAssets(_ assets: any NSFastEnumeration, at indexes: IndexSet)
```

## Parameters

- `assets` — An array of [PHAsset](../phasset.md) objects to be inserted into the asset collection.

- `indexes` — The indexes at which the assets should be inserted. The count of locations in this index set must equal the count of assets.

## Discussion

To ensure that the index set you specify is valid even if the asset collection has changed since you fetched it, create a change request with a snapshot of the asset collection’s contents using the [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) method before inserting assets.

For a detailed discussion of how the index set you specify maps to insertions in the list of assets, see the similar [NSMutableArray](../../foundation/nsmutablearray.md) method [insert(_:at:)](<../../foundation/nsmutablearray/insert(__at_)-73pln.md>).

> [!note] Note
> Assets from My Photo Stream or iCloud Shared Albums and assets synced to the device through iTunes cannot be added to collections. Transient asset collections (such as those created with the [+ transientAssetCollectionWithAssets:title:](<../phassetcollection/transientassetcollection(with_title_).md>) method) do not support adding or removing content.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](title.md) — The displayed name of the asset collection.
- [- addAssets:](<addassets(__).md>) — Adds the specified assets to the asset collection.
- [- removeAssets:](<removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- removeAssetsAtIndexes:](<removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [- moveAssetsAtIndexes:toIndex:](<moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.
