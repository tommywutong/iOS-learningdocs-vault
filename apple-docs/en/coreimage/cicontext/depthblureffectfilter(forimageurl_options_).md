---
title: 'depthBlurEffectFilter(forImageURL:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/depthblureffectfilter(forimageurl:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/depthblureffectfilter(forimageurl:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/depthblureffectfilter%28forimageurl%3Aoptions%3A%29.json'
content_hash: 'sha256:9716f6394afde036'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# depthBlurEffectFilter(forImageURL:options:)

<sub>Instance Method</sub>

Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image URL that can be used to apply a depth blur effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func depthBlurEffectFilter(forImageURL url: URL, options: [AnyHashable : Any]? = nil) -> CIFilter?
```

## Parameters

- `url` — The URL location of the image to apply the depth blur effect to.

- `options` — Reserved for future use.

## Discussion

The receiver context is used to render the image in order to get the facial landmarks used to create the effect.

## See Also

### Creating Depth Blur Filters

- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:hairSemanticSegmentation:glassesMatte:gainMap:orientation:options:](<depthblureffectfilter(for_disparityimage_portraiteffectsmatte_hairsemanticsegmentation_glassesmatte_gainmap_orientation_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:hairSemanticSegmentation:orientation:options:](<depthblureffectfilter(for_disparityimage_portraiteffectsmatte_hairsemanticsegmentation_orientation_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImage:disparityImage:portraitEffectsMatte:orientation:options:](<depthblureffectfilter(for_disparityimage_portraiteffectsmatte_orientation_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect created with the supplied auxiliary images.
- [- depthBlurEffectFilterForImageData:options:](<depthblureffectfilter(forimagedata_options_).md>) — Create a [CIFilter](../cifilter-swift.class.md) instance for the supplied image data that can be used to apply a depth blur effect.
