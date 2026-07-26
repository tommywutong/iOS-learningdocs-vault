---
title: PHAssetEditOperation.content
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasseteditoperation/content
source_url: 'https://developer.apple.com/documentation/photos/phasseteditoperation/content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasseteditoperation/content.json'
content_hash: 'sha256:f7f5ee0d499bc675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetEditOperation](../phasseteditoperation.md)

# PHAssetEditOperation.content

<sub>Case</sub>

The asset’s photo or video content can be edited.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case content
```

## Discussion

To begin the process of editing an asset, use the [- requestContentEditingInputWithOptions:completionHandler:](<../phasset/requestcontenteditinginput(with_completionhandler_).md>) method.

## See Also

### Constants

- [PHAssetEditOperationDelete](delete.md) — The asset can be deleted from the photo library.
- [PHAssetEditOperationProperties](properties.md) — The asset’s metadata properties can be edited.
