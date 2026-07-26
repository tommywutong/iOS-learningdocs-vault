---
title: previewCGImageRepresentation()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/previewcgimagerepresentation()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/previewcgimagerepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/previewcgimagerepresentation%28%29.json'
content_hash: 'sha256:00bf0dd1eb471a89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# previewCGImageRepresentation()

<sub>Instance Method</sub>

Extracts and returns the captured photo’s preview image as a Core Graphics image object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func previewCGImageRepresentation() -> CGImage?
```

## Return Value

A Core Graphics image representation of the captured photo, or `nil` if either the image cannot be converted or a preview image was not requested as part of the photo capture.

## See Also

### Packaging data for file output

- [- fileDataRepresentationWithCustomizer:](<filedatarepresentation(with_).md>) — Gets a customized representation of the photo data.
- [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md) — A protocol that defines the methods to implement to customize the packaging of photo data.
- [- fileDataRepresentation](<filedatarepresentation().md>) — Generates and returns a flat data representation of the photo and its attachments.
- [- CGImageRepresentation](<cgimagerepresentation().md>) — Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [- fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:](<filedatarepresentation(withreplacementmetadata_replacementembeddedthumbnailphotoformat_replacementembeddedthumbnailpixelbuffer_replacementdepthdata_).md>) — Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments. _(deprecated)_
