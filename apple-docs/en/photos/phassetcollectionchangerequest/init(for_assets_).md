---
title: 'init(for:assets:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/init(for:assets:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/init(for:assets:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/init%28for%3Aassets%3A%29.json'
content_hash: 'sha256:d4545c5fe8a8ef2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# init(for:assets:)

<sub>Initializer</sub>

Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(for assetCollection: PHAssetCollection, assets: PHFetchResult<PHAsset>?)
```

## Parameters

- `assetCollection` — The asset collection to be modified.

- `assets` — A fetch result listing the assets in the collection.

## Return Value

An asset collection change request.

## Discussion

After you create a change request within a photo library change block, you propose changes to the collection’s title or list of member assets with the properties and instance methods of the change request. After Photos runs your change block, the asset collection reflects your changes. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

Use this method when you need to insert, remove, or rearrange assets at specified indexes in the asset collection’s list of member assets. By passing in a fetch result reflecting what your app sees as the current state of the collection’s membership, the Photos framework can ensure that the indexes you specify are valid even if the collection has changed since you last fetched it. If you don’t need to work with indexes in the list of member assets, you can use the [+ changeRequestForAssetCollection:](<init(for_).md>) method instead.

## See Also

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<init(for_).md>) — Creates a request for modifying the specified asset collection.
- [title](title.md) — The displayed name of the asset collection.
- [- addAssets:](<addassets(__).md>) — Adds the specified assets to the asset collection.
- [- insertAssets:atIndexes:](<insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssets:](<removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- removeAssetsAtIndexes:](<removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [- moveAssetsAtIndexes:toIndex:](<moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.
