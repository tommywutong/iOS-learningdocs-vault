---
title: photoDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/photodimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/photodimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/photodimensions.json'
content_hash: 'sha256:24dd376039a11be0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# photoDimensions

<sub>Instance Property</sub>

The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var photoDimensions: CMVideoDimensions { get }
```

## Discussion

The output dimensions of a captured image are set at the moment of capture, depending on device orientation and capture session configuration. (For example, when the capture session includes a video output and video stabilization is in use, captured photos are smaller.)

This property provides the dimensions of the image to be delivered in the  [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method. Use this property in earlier delegate methods to find the size of the image before delivery.

If you do not request capture in a processed format (that is, if you request capture in RAW format only), this property’s value has zero width and zero height.

## See Also

### Examining output dimensions

- [deferredPhotoProxyDimensions](deferredphotoproxydimensions.md) — The resolved dimensions of the photo proxy when using deferred photo delivery.
- [rawPhotoDimensions](rawphotodimensions.md) — The size, in pixels, of the RAW-format photo image that the capture delivers.
- [previewDimensions](previewdimensions.md) — The size, in pixels, of the preview image that the system delivers with the capture.
- [embeddedThumbnailDimensions](embeddedthumbnaildimensions.md) — The size, in pixels, of the thumbnail image that the capture delivers.
- [rawEmbeddedThumbnailDimensions](rawembeddedthumbnaildimensions.md) — The size, in pixels, of the RAW-format embedded thumbnail image that the capture delivers.
- [livePhotoMovieDimensions](livephotomoviedimensions.md) — The size, in pixels, of the Live Photo movie content that the capture delivers.
- [portraitEffectsMatteDimensions](portraiteffectsmattedimensions.md) — The size, in pixels, of the portrait effects matte that the capture delivers.
- [- dimensionsForSemanticSegmentationMatteOfType:](<dimensionsforsemanticsegmentationmatte(oftype_).md>) — Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.
- [photoProcessingTimeRange](photoprocessingtimerange.md) — The time range in which to expect the system to deliver the photo to the delegate.
