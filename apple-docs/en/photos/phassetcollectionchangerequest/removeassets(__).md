---
title: 'removeAssets(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/removeassets(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/removeassets(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/removeassets%28_%3A%29.json'
content_hash: 'sha256:9e9b3c038a7a051b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# removeAssets(_:)

<sub>Instance Method</sub>

Removes the specified assets from the asset collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAssets(_ assets: any NSFastEnumeration)
```

## Parameters

- `assets` — An array of [PHAsset](../phasset.md) objects to be removed from the asset collection.

## Discussion

This method removes assets from the collection based on their identity (determined by the [localIdentifier](../phobject/localidentifier.md) property of each asset). To remove objects at specified indexes, use the [- removeAssetsAtIndexes:](<removeassets(at_).md>) method.

> [!note] Note
> Transient asset collections (such as those created with the [+ transientAssetCollectionWithAssets:title:](<../phassetcollection/transientassetcollection(with_title_).md>) method) do not support adding or removing content.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](title.md) — The displayed name of the asset collection.
- [- addAssets:](<addassets(__).md>) — Adds the specified assets to the asset collection.
- [- insertAssets:atIndexes:](<insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssetsAtIndexes:](<removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [- moveAssetsAtIndexes:toIndex:](<moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.
