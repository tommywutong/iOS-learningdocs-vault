---
title: embeddedThumbnailPhotoFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/embeddedthumbnailphotoformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embeddedthumbnailphotoformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/embeddedthumbnailphotoformat.json'
content_hash: 'sha256:a2528c4fe90689bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# embeddedThumbnailPhotoFormat

<sub>Instance Property</sub>

A dictionary describing the format for delivery of thumbnail images embedded in photo file output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var embeddedThumbnailPhotoFormat: [String : Any]? { get set }
```

## Discussion

By default, this property is `nil`, specifying that the photo output should not embed thumbnail images in photo file output. To enable embedding, set this property to a dictionary describing the format for thumbnail images, containing the following keys and values:

- The dictionary must contain the key [AVVideoCodecKey](../avvideocodeckey.md), whose corresponding value must be one of the pixel format types listed in the [availableEmbeddedThumbnailPhotoCodecTypes](availableembeddedthumbnailphotocodectypes.md) array.
- Optionally, you can also include the [AVVideoWidthKey](../avvideowidthkey.md) and [AVVideoHeightKey](../avvideoheightkey.md) keys to specify the size of the thumbnail image. (If you specify either width or height, you must specify both.) If the size you specify does not match the aspect ratio of the primary photo, the photo output provides a thumbnail image whose size matches the longer of the two specified dimensions, preserving the original aspect ratio.

> [!note] Note
> The photo capture system supports both _preview_ and _thumbnail_ images as companions to the full-size primary image in a photo capture. A preview image is intended for immediate display (as seen when taking photos in the iOS Camera app), and as such is sized for full-screen presentation on the current device. A thumbnail image is intended for embedding in the output image file and can be used by other software (such as Quick Look in a file browser) to allow users to quickly review the image without loading the entire image file; the size of thumbnail images may be limited depending on the output file format.

## See Also

### Enabling preview and thumbnail delivery

- [previewPhotoFormat](previewphotoformat.md) — A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [availablePreviewPhotoPixelFormatTypes](availablepreviewphotopixelformattypes-30d9.md) — An array of available of pixel format types available to specify a preview photo format.
- [availableRawEmbeddedThumbnailPhotoCodecTypes](availablerawembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [rawEmbeddedThumbnailPhotoFormat](rawembeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [availableEmbeddedThumbnailPhotoCodecTypes](availableembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
