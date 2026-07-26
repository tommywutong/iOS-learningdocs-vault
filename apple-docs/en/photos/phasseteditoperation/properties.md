---
title: PHAssetEditOperation.properties
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasseteditoperation/properties
source_url: 'https://developer.apple.com/documentation/photos/phasseteditoperation/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasseteditoperation/properties.json'
content_hash: 'sha256:8e23a3b06c9f5534'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetEditOperation](../phasseteditoperation.md)

# PHAssetEditOperation.properties

<sub>Case</sub>

The asset’s metadata properties can be edited.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case properties
```

## Discussion

To change an asset’s properties, create a change request with the [+ changeRequestForAsset:](<../phassetchangerequest/init(for_).md>) method inside a [PHPhotoLibrary](../phphotolibrary.md) change block.

## See Also

### Constants

- [PHAssetEditOperationDelete](delete.md) — The asset can be deleted from the photo library.
- [PHAssetEditOperationContent](content.md) — The asset’s photo or video content can be edited.
