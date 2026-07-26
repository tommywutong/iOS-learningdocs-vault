---
title: 'canPerform(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollection/canperform(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollection/canperform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollection/canperform%28_%3A%29.json'
content_hash: 'sha256:29854fdffcd9185f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollection](../phcollection.md)

# canPerform(_:)

<sub>Instance Method</sub>

Returns whether the collection supports the specified editing operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canPerform(_ anOperation: PHCollectionEditOperation) -> Bool
```

## Parameters

- `anOperation` — A bit mask of editing operations to be tested.

## Return Value

`true` if the asset supports the specified editing operation; otherwise, `false`.

## Discussion

If an asset collection or collection list supports editing, you can create a [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md) or [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md) object inside a [PHPhotoLibrary](../phphotolibrary.md) change block to submit a change.

## See Also

### Determining Collection Capabilities

- [canContainAssets](cancontainassets.md) — A Boolean value indicating whether the collection can contain assets.
- [canContainCollections](cancontaincollections.md) — A Boolean value indicating whether the collection can contain other collections.
- [PHCollectionEditOperation](../phcollectioneditoperation.md) — Values identifying possible actions that a collection can support, used by the [- canPerformEditOperation:](<canperform(__).md>) method.
