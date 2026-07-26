---
title: PHAssetEditOperation.delete
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasseteditoperation/delete
source_url: 'https://developer.apple.com/documentation/photos/phasseteditoperation/delete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasseteditoperation/delete.json'
content_hash: 'sha256:7f21b4aed8163ac0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetEditOperation](../phasseteditoperation.md)

# PHAssetEditOperation.delete

<sub>Case</sub>

The asset can be deleted from the photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case delete
```

## Discussion

To delete one or more assets, create a change request with the [+ deleteAssets:](<../phassetchangerequest/deleteassets(__).md>) method inside a [PHPhotoLibrary](../phphotolibrary.md) change block.

## See Also

### Constants

- [PHAssetEditOperationContent](content.md) — The asset’s photo or video content can be edited.
- [PHAssetEditOperationProperties](properties.md) — The asset’s metadata properties can be edited.
