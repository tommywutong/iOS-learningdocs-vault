---
title: 'deleteAssets(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetchangerequest/deleteassets(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/deleteassets(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/deleteassets%28_%3A%29.json'
content_hash: 'sha256:93217b6ce2d91abb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# deleteAssets(_:)

<sub>Type Method</sub>

Requests that the specified assets be deleted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func deleteAssets(_ assets: any NSFastEnumeration)
```

## Parameters

- `assets` — An array of [PHAsset](../phasset.md) objects to be deleted.

## Discussion

Call this method within a photo library change block to delete assets. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).
