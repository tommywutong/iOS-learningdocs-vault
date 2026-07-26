---
title: fileDataRepresentation()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/filedatarepresentation()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/filedatarepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/filedatarepresentation%28%29.json'
content_hash: 'sha256:b1a1f9e0cc157aa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# fileDataRepresentation()

<sub>Instance Method</sub>

Generates and returns a flat data representation of the photo and its attachments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func fileDataRepresentation() -> Data?
```

## Return Value

Data appropriate for writing to a file of the type specified when requesting photo capture, or `nil` if the photo and attachment data cannot be flattened.

## Discussion

When you request a photo capture with the [AVCapturePhotoOutput](../avcapturephotooutput.md) [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method, the [AVCapturePhotoSettings](../avcapturephotosettings.md) object you provide specifies image data formats (such as JPEG and HEVC) and container file formats (such as JFIF and HEIF) for the resulting image file. Calling this method formats and packages the image pixel buffer, along with metadata and other attachments created during capture (such as preview photos and depth maps), into data appropriate for writing to a file of that type.

## See Also

### Packaging data for file output

- [- fileDataRepresentationWithCustomizer:](<filedatarepresentation(with_).md>) — Gets a customized representation of the photo data.
- [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md) — A protocol that defines the methods to implement to customize the packaging of photo data.
- [- CGImageRepresentation](<cgimagerepresentation().md>) — Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [- previewCGImageRepresentation](<previewcgimagerepresentation().md>) — Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [- fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:](<filedatarepresentation(withreplacementmetadata_replacementembeddedthumbnailphotoformat_replacementembeddedthumbnailpixelbuffer_replacementdepthdata_).md>) — Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments. _(deprecated)_
