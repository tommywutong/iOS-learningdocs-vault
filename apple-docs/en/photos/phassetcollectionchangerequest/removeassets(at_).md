---
title: 'removeAssets(at:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/removeassets(at:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/removeassets(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/removeassets%28at%3A%29.json'
content_hash: 'sha256:27eddb16799caec7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# removeAssets(at:)

<sub>Instance Method</sub>

Removes the assets at the specified indexes from the asset collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAssets(at indexes: IndexSet)
```

## Parameters

- `indexes` — The indexes of the assets to be removed from the asset collection.

## Discussion

To ensure that the index set you specify is valid even if the asset collection has changed since you fetched it, create a change request with a snapshot of the asset collection’s contents using the [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) method before removing assets. To remove objects based on their identities (without regard to their indexes in the collection), use the [- removeAssets:](<removeassets(__).md>) method.

> [!note] Note
> Transient asset collections (such as those created with the [+ transientAssetCollectionWithAssets:title:](<../phassetcollection/transientassetcollection(with_title_).md>) method) do not support adding or removing content.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](title.md) — The displayed name of the asset collection.
- [- addAssets:](<addassets(__).md>) — Adds the specified assets to the asset collection.
- [- insertAssets:atIndexes:](<insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssets:](<removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [- moveAssetsAtIndexes:toIndex:](<moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.
