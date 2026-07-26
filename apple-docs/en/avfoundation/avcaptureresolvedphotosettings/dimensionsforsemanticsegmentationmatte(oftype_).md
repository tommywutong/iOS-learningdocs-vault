---
title: 'dimensionsForSemanticSegmentationMatte(ofType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureresolvedphotosettings/dimensionsforsemanticsegmentationmatte(oftype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/dimensionsforsemanticsegmentationmatte(oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/dimensionsforsemanticsegmentationmatte%28oftype%3A%29.json'
content_hash: 'sha256:a0baed5133d90698'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# dimensionsForSemanticSegmentationMatte(ofType:)

<sub>Instance Method</sub>

Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func dimensionsForSemanticSegmentationMatte(ofType semanticSegmentationMatteType: AVSemanticSegmentationMatte.MatteType) -> CMVideoDimensions
```

## Parameters

- `semanticSegmentationMatteType` — The segmentation matte type for which to retrieve dimensions.

## Return Value

A [CMVideoDimensions](../../coremedia/cmvideodimensions.md) structure that provides the height and width of the image mattes.

## See Also

### Examining output dimensions

- [photoDimensions](photodimensions.md) — The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [deferredPhotoProxyDimensions](deferredphotoproxydimensions.md) — The resolved dimensions of the photo proxy when using deferred photo delivery.
- [rawPhotoDimensions](rawphotodimensions.md) — The size, in pixels, of the RAW-format photo image that the capture delivers.
- [previewDimensions](previewdimensions.md) — The size, in pixels, of the preview image that the system delivers with the capture.
- [embeddedThumbnailDimensions](embeddedthumbnaildimensions.md) — The size, in pixels, of the thumbnail image that the capture delivers.
- [rawEmbeddedThumbnailDimensions](rawembeddedthumbnaildimensions.md) — The size, in pixels, of the RAW-format embedded thumbnail image that the capture delivers.
- [livePhotoMovieDimensions](livephotomoviedimensions.md) — The size, in pixels, of the Live Photo movie content that the capture delivers.
- [portraitEffectsMatteDimensions](portraiteffectsmattedimensions.md) — The size, in pixels, of the portrait effects matte that the capture delivers.
- [photoProcessingTimeRange](photoprocessingtimerange.md) — The time range in which to expect the system to deliver the photo to the delegate.
