---
title: portraitEffectsMatteDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/portraiteffectsmattedimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/portraiteffectsmattedimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/portraiteffectsmattedimensions.json'
content_hash: 'sha256:cd21e0010f4ce5b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# portraitEffectsMatteDimensions

<sub>Instance Property</sub>

The size, in pixels, of the portrait effects matte that the capture delivers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var portraitEffectsMatteDimensions: CMVideoDimensions { get }
```

## See Also

### Examining output dimensions

- [photoDimensions](photodimensions.md) — The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [deferredPhotoProxyDimensions](deferredphotoproxydimensions.md) — The resolved dimensions of the photo proxy when using deferred photo delivery.
- [rawPhotoDimensions](rawphotodimensions.md) — The size, in pixels, of the RAW-format photo image that the capture delivers.
- [previewDimensions](previewdimensions.md) — The size, in pixels, of the preview image that the system delivers with the capture.
- [embeddedThumbnailDimensions](embeddedthumbnaildimensions.md) — The size, in pixels, of the thumbnail image that the capture delivers.
- [rawEmbeddedThumbnailDimensions](rawembeddedthumbnaildimensions.md) — The size, in pixels, of the RAW-format embedded thumbnail image that the capture delivers.
- [livePhotoMovieDimensions](livephotomoviedimensions.md) — The size, in pixels, of the Live Photo movie content that the capture delivers.
- [- dimensionsForSemanticSegmentationMatteOfType:](<dimensionsforsemanticsegmentationmatte(oftype_).md>) — Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.
- [photoProcessingTimeRange](photoprocessingtimerange.md) — The time range in which to expect the system to deliver the photo to the delegate.
