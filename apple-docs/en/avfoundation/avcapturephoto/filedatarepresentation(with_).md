---
title: 'fileDataRepresentation(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephoto/filedatarepresentation(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/filedatarepresentation(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/filedatarepresentation%28with%3A%29.json'
content_hash: 'sha256:15064a2751c3ee4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# fileDataRepresentation(with:)

<sub>Instance Method</sub>

Gets a customized representation of the photo data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func fileDataRepresentation(with customizer: any AVCapturePhotoFileDataRepresentationCustomizer) -> Data?
```

## Parameters

- `customizer` — An object that customizes the returned metadata, image thumbnail, or depth data.

## Return Value

A data representation of the photo.

## See Also

### Packaging data for file output

- [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md) — A protocol that defines the methods to implement to customize the packaging of photo data.
- [- fileDataRepresentation](<filedatarepresentation().md>) — Generates and returns a flat data representation of the photo and its attachments.
- [- CGImageRepresentation](<cgimagerepresentation().md>) — Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [- previewCGImageRepresentation](<previewcgimagerepresentation().md>) — Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [- fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:](<filedatarepresentation(withreplacementmetadata_replacementembeddedthumbnailphotoformat_replacementembeddedthumbnailpixelbuffer_replacementdepthdata_).md>) — Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments. _(deprecated)_
