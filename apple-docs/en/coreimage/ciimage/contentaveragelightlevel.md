---
title: contentAverageLightLevel
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/contentaveragelightlevel
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/contentaveragelightlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/contentaveragelightlevel.json'
content_hash: 'sha256:1a3df1dc7f9139d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# contentAverageLightLevel

<sub>Instance Property</sub>

Returns the content average light level of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentAverageLightLevel: Float { get }
```

## Discussion

If the image average light level is unknown, then the value 0.0 will be returned.

If the image headroom is known, then a value greater than or equal to 0.0 will be returned.

The image average light level may known when a CIImage is first initialized. If the a CIImage is initialized with a:

- `CGImage` : then the headroom will be determined by `CGImageGetContentAverageLightLevel()`.
- `CVPixelBuffer` : then the headroom will be determined by `kCVImageBufferContentLightLevelInfoKey`.

If the image is the result of applying a [CIFilter](../cifilter-swift.class.md) or [CIKernel](../cikernel.md), this property will return `0.0`.

There are exceptions to this.  Applying a [CIWarpKernel](../ciwarpkernel.md) or certain [CIFilter](../cifilter-swift.class.md) (e.g. `CIGaussianBlur`, `CILanczosScaleTransform`, `CIAreaAverage` and some others) to an image will result in a [CIImage](../ciimage.md) instance with the same `contentAverageLightLevel` property value.
