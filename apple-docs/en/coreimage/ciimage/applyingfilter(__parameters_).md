---
title: 'applyingFilter(_:parameters:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/applyingfilter(_:parameters:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/applyingfilter(_:parameters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/applyingfilter%28_%3Aparameters%3A%29.json'
content_hash: 'sha256:40f8f4bfc903a9fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# applyingFilter(_:parameters:)

<sub>Instance Method</sub>

Returns a new image created by applying a filter to the original image with the specified name and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func applyingFilter(_ filterName: String, parameters params: [String : Any]) -> CIImage
```

## Parameters

- `filterName` — The name of the filter to apply, as used when creating a [CIFilter](../cifilter-swift.class.md) instance with the [+ filterWithName:](<../cifilter-swift.class/init(name_).md>) method.

- `params` — A dictionary whose key-value pairs are set as input values to the filter. Each key is a constant that specifies the name of an input parameter for the filter, and the corresponding value is the value for that parameter. See [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346) for built-in filters and their allowed parameters.

## Return Value

An image object representing the result of applying the filter.

## Discussion

Calling this method is equivalent to the following sequence of steps:

1. Creating a [CIFilter](../cifilter-swift.class.md) instance
2. Setting the original image as the filter’s `inputImage` parameter
3. Setting the remaining filter parameters from the `params` dictionary
4. Retrieving the [outputImage](../cifilter-swift.class/outputimage.md) object from the filter

> [!important] Important
> This method, though convenient, is inefficient if used multiple times in succession. Achieve better performance by chaining filters without asking for the outputs of individual filters. For more information, see [Processing an Image Using Built-in Filters](../processing-an-image-using-built-in-filters.md).

## See Also

### Creating an Image by Modifying an Existing Image

- [- imageByApplyingFilter:](<applyingfilter(__).md>) — Applies the filter to an image and returns the output.
- [- imageByApplyingTransform:](<transformed(by_).md>) — Returns a new image that represents the original image after applying an affine transform.
- [- imageByApplyingTransform:highQualityDownsample:](<transformed(by_highqualitydownsample_).md>)
- [- imageByCroppingToRect:](<cropped(to_).md>) — Returns a new image with a cropped portion of the original image.
- [- imageByApplyingOrientation:](<oriented(forexiforientation_).md>) — Returns a new image created by transforming the original image to the specified EXIF orientation.
- [- imageByClampingToExtent](<clampedtoextent().md>) — Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [- imageByClampingToRect:](<clamped(to_).md>) — Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [- imageByCompositingOverImage:](<composited(over_).md>) — Returns a new image created by compositing the original image over the specified destination image.
- [- imageByConvertingWorkingSpaceToLab](<convertingworkingspacetolab().md>)
- [- imageByConvertingLabToWorkingSpace](<convertinglabtoworkingspace().md>)
- [- imageByColorMatchingColorSpaceToWorkingSpace:](<matchedtoworkingspace(from_).md>) — Returns a new image created by color matching from the specified color space to the context’s working color space.
- [- imageByColorMatchingWorkingSpaceToColorSpace:](<matchedfromworkingspace(to_).md>) — Returns a new image created by color matching from the context’s working color space to the specified color space.
- [- imageByPremultiplyingAlpha](<premultiplyingalpha().md>) — Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [- imageByUnpremultiplyingAlpha](<unpremultiplyingalpha().md>) — Returns a new image created by dividing the image’s RGB values by its alpha values.
- [- imageBySettingAlphaOneInExtent:](<settingalphaone(in_).md>) — Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
