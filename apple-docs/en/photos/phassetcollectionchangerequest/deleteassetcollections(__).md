---
title: 'deleteAssetCollections(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/deleteassetcollections(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/deleteassetcollections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/deleteassetcollections%28_%3A%29.json'
content_hash: 'sha256:400ef9a1eee80c5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# deleteAssetCollections(_:)

<sub>Type Method</sub>

Requests that the specified asset collections be deleted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func deleteAssetCollections(_ assetCollections: any NSFastEnumeration)
```

## Parameters

- `assetCollections` — An array of [PHAssetCollection](../phassetcollection.md) objects to be deleted.

## Discussion

Call this method within a photo library change block to delete asset collections. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).
