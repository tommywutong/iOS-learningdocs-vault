---
title: 'depthBlurEffectFilter(for:disparityImage:portraitEffectsMatte:orientation:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:orientation:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:orientation:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/depthblureffectfilter%28for%3Adisparityimage%3Aportraiteffectsmatte%3Aorientation%3Aoptions%3A%29.json'
content_hash: 'sha256:6c2c008341117db5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# depthBlurEffectFilter(for:disparityImage:portraitEffectsMatte:orientation:options:)

<sub>Instance Method</sub>

Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func depthBlurEffectFilter(for image: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]? = nil) -> CIFilter?
```

## Parameters

- `image` — The image object to apply the depth blur effect to.

- `disparityImage` — The auxiliary disparity image. For more information, see [kCIImageAuxiliaryDisparity](../ciimageoption/auxiliarydisparity.md).

- `portraitEffectsMatte` — The portrait effects matte image. For more information, see [kCIImageAuxiliaryPortraitEffectsMatte](../ciimageoption/auxiliaryportraiteffectsmatte.md).

- `orientation` — The intended display orientation for the image.

- `options` — Reserved for future use.

## Discussion

The receiver context is used to render the image in order to get the facial landmarks used to create the effect. The auxiliary images used to create the filter can be obtained from a JPEG or HEIC file containing embedded portrait effects matte data.

## See Also

### Related Documentation

- [CIImageOption](../ciimageoption.md)
- [Configuring camera capture to collect a Portrait Effects matte](../../avfoundation/configuring-camera-capture-to-collect-a-portrait-effects-matte.md) — Prepare your app to capture a portrait effects matte when taking photos.

### Creating Depth Blur Filters

- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:hairSemanticSegmentation:glassesMatte:gainMap:orientation:options:](<depthblureffectfilter(for_disparityimage_portraiteffectsmatte_hairsemanticsegmentation_glassesmatte_gainmap_orientation_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:hairSemanticSegmentation:orientation:options:](<depthblureffectfilter(for_disparityimage_portraiteffectsmatte_hairsemanticsegmentation_orientation_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImageData:options:](<depthblureffectfilter(forimagedata_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.
- [- depthBlurEffectFilterForImageURL:options:](<depthblureffectfilter(forimageurl_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.
