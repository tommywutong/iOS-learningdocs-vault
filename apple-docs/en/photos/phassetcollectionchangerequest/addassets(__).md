---
title: 'addAssets(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/addassets(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/addassets(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/addassets%28_%3A%29.json'
content_hash: 'sha256:3d5f7cf06c440414'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# addAssets(_:)

<sub>Instance Method</sub>

Adds the specified assets to the asset collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addAssets(_ assets: any NSFastEnumeration)
```

## Parameters

- `assets` — An array of [PHAsset](../phasset.md) objects to be added to the asset collection.

## Discussion

If you created the change request with a snapshot of the asset collection’s contents using the [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) method, Photos inserts the new assets after the existing assets in the collection. Otherwise, the arrangement of the new assets relative to others in the collection is undefined.

> [!note] Note
> Assets from My Photo Stream or iCloud Shared Albums and assets synced to the device through iTunes cannot be added to collections. Transient asset collections (such as those created with the [+ transientAssetCollectionWithAssets:title:](<../phassetcollection/transientassetcollection(with_title_).md>) method) do not support adding or removing content.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](title.md) — The displayed name of the asset collection.
- [- insertAssets:atIndexes:](<insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssets:](<removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- removeAssetsAtIndexes:](<removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [- moveAssetsAtIndexes:toIndex:](<moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.
