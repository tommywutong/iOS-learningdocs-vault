---
title: previewPhotoFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/previewphotoformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/previewphotoformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/previewphotoformat.json'
content_hash: 'sha256:4858b69ccc54ced4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# previewPhotoFormat

<sub>Instance Property</sub>

A dictionary describing the format for delivery of preview-sized images alongside the main photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var previewPhotoFormat: [String : Any]? { get set }
```

## Discussion

By default, this property is `nil`, specifying that the photo output should return only the main image requested. To also receive a preview-sized image, set this property to a dictionary describing the format for that image, containing the following keys and values:

The dictionary must contain the [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md) key, whose corresponding value must be one of the pixel format types listed in the [availablePreviewPhotoPixelFormatTypes](availablepreviewphotopixelformattypes-2vfwu.md) array.

Optionally, you can also include the [kCVPixelBufferWidthKey](../../corevideo/kcvpixelbufferwidthkey.md) and [kCVPixelBufferHeightKey](../../corevideo/kcvpixelbufferheightkey.md) keys to specify the size of the preview image. (If you specify either width or height, you must specify both.) If the size you specify does not match the aspect ratio of the primary photo, the photo output provides a preview image whose size matches the longer of the two specified dimensions, preserving the original aspect ratio.

> [!note] Note
> The photo capture system supports both _preview_ and _thumbnail_ images as companions to the full-size primary image in a photo capture. A preview image is intended for immediate display (as seen when taking photos in the iOS Camera app), and as such is sized for full-screen presentation on the current device. A thumbnail image is intended for embedding in the output image file and can be used by other software (such as Quick Look in a file browser) to allow users to quickly review the image without loading the entire image file; the size of thumbnail images may be limited depending on the output file format.

## See Also

### Enabling preview and thumbnail delivery

- [availablePreviewPhotoPixelFormatTypes](availablepreviewphotopixelformattypes-30d9.md) — An array of available of pixel format types available to specify a preview photo format.
- [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [availableRawEmbeddedThumbnailPhotoCodecTypes](availablerawembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [rawEmbeddedThumbnailPhotoFormat](rawembeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [availableEmbeddedThumbnailPhotoCodecTypes](availableembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
