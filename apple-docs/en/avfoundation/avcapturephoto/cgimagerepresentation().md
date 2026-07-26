---
title: cgImageRepresentation()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/cgimagerepresentation()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/cgimagerepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/cgimagerepresentation%28%29.json'
content_hash: 'sha256:afd0bfa57d77e771'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# cgImageRepresentation()

<sub>Instance Method</sub>

Extracts and returns the captured photo’s primary image as a Core Graphics image object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func cgImageRepresentation() -> CGImage?
```

## Return Value

A Core Graphics image representation of the captured photo, or `nil` if the image cannot be converted.

## See Also

### Packaging data for file output

- [- fileDataRepresentationWithCustomizer:](<filedatarepresentation(with_).md>) — Gets a customized representation of the photo data.
- [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md) — A protocol that defines the methods to implement to customize the packaging of photo data.
- [- fileDataRepresentation](<filedatarepresentation().md>) — Generates and returns a flat data representation of the photo and its attachments.
- [- previewCGImageRepresentation](<previewcgimagerepresentation().md>) — Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [- fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:](<filedatarepresentation(withreplacementmetadata_replacementembeddedthumbnailphotoformat_replacementembeddedthumbnailpixelbuffer_replacementdepthdata_).md>) — Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments. _(deprecated)_
