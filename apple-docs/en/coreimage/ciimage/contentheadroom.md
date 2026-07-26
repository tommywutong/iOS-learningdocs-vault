---
title: contentHeadroom
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/contentheadroom
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/contentheadroom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/contentheadroom.json'
content_hash: 'sha256:194ae16feac9e664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# contentHeadroom

<sub>Instance Property</sub>

Returns the content headroom of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentHeadroom: Float { get }
```

## Discussion

If the image headroom is unknown, then the value 0.0 will be returned.

If the image headroom is known, then a value greater than or equal to 1.0 will be returned. A value of 1.0 will be returned if the image is SDR. A value greater than 1.0 will be returned if the image is HDR.

The image headroom may known when a CIImage is first initialized. If the a CIImage is initialized using:

- `NSURL` or `NSData` : the headroom may be determined by associated metadata or deduced from pixel format or colorSpace information.
- `CGImage` : headroom may be determined by `CGImageGetHeadroomInfo()` or deduced from pixel format or colorSpace information.
- `IOSurface` : then the headroom will be determined by `kIOSurfaceContentHeadroom`. or deduced from pixel format or colorSpace information.
- `CVPixelBuffer` : then the headroom will be determined by `kCVImageBufferContentLightLevelInfoKey`. or deduced from pixel format or colorSpace information.
- `BitmapData` : headroom may be deduced from pixel format or colorSpace information.

If the image is the result of applying a [CIFilter](../cifilter-swift.class.md) or [CIKernel](../cikernel.md), this method will return `0.0`.

There are exceptions to this.  Applying a `CIWarpKernel`` or certain ``CIFilter-class``  (e.g. `CIGaussianBlur`, `CILanczosScaleTransform`, `CIAreaAverage`and some others)  to an image will result in a ``CIImage`` instance with the same`contentHeadroom` property value.

## See Also

### Instance Properties

- [opaque](isopaque.md) — Returns YES if the image is known to have and alpha value of `1.0` over the entire image extent.
- [metalTexture](metaltexture.md)
