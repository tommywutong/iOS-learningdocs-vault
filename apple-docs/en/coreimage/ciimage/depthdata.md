---
title: depthData
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/depthdata
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/depthdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/depthdata.json'
content_hash: 'sha256:713d1c02b02dbf18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# depthData

<sub>Instance Property</sub>

Depth data associated with the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthData: AVDepthData? { get }
```

## Discussion

Returns an [AVDepthData](../../avfoundation/avdepthdata.md) if the [CIImage](../ciimage.md) was created with [imageWithData:](imagewithdata_.md) or [imageWithContentsOfURL:](imagewithcontentsofurl_.md) and one of the options [kCIImageAuxiliaryDepth](../ciimageoption/auxiliarydepth.md) or [kCIImageAuxiliaryDisparity](../ciimageoption/auxiliarydisparity.md), otherwise [nil](../../objectivec/nil-227m0.md).

## See Also

### Accessing Original Image Content

- [CGImage](cgimage.md) — The CoreGraphics image object this image was created from, if applicable.
- [pixelBuffer](pixelbuffer.md) — The CoreVideo pixel buffer this image was created from, if applicable.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte associated with the image.
- [semanticSegmentationMatte](semanticsegmentationmatte.md)
