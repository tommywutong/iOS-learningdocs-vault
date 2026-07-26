---
title: clampedToExtent()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/clampedtoextent()
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/clampedtoextent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/clampedtoextent%28%29.json'
content_hash: 'sha256:34878291f6fb82d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# clampedToExtent()

<sub>Instance Method</sub>

Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func clampedToExtent() -> CIImage
```

## Return Value

An image object representing the result of the clamp operation.

## Discussion

Calling this method is equivalent to using the [CIAffineClamp](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CIAffineClamp) filter, which creates an image of infinite extent by repeating pixel colors from the edges of the original image.

This operation can be useful when using the image as input to other filters. When an image has finite extent, Core Image treats the area outside the extent as if it were filled with empty (black, zero alpha) pixels. If you apply a filter that samples from outside the image’s extent, those empty pixels affect the result of the filter.

For example, applying the `CIGaussianBlur` filter to an image softens the edges of the blurred image, because the opaque pixels at the edges of the image blur into the transparent pixels outside the image’s extent. Applying a clamp effect before the blur filter avoids edge softening by making the original image opaque in all directions. (However, the blurred image will also have infinite extent. Use the [- imageByCroppingToRect:](<cropped(to_).md>) method to return to the original image’s dimensions while retaining hard edges.)

## See Also

### Creating an Image by Modifying an Existing Image

- [- imageByApplyingFilter:withInputParameters:](<applyingfilter(__parameters_).md>) — Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [- imageByApplyingFilter:](<applyingfilter(__).md>) — Applies the filter to an image and returns the output.
- [- imageByApplyingTransform:](<transformed(by_).md>) — Returns a new image that represents the original image after applying an affine transform.
- [- imageByApplyingTransform:highQualityDownsample:](<transformed(by_highqualitydownsample_).md>)
- [- imageByCroppingToRect:](<cropped(to_).md>) — Returns a new image with a cropped portion of the original image.
- [- imageByApplyingOrientation:](<oriented(forexiforientation_).md>) — Returns a new image created by transforming the original image to the specified EXIF orientation.
- [- imageByClampingToRect:](<clamped(to_).md>) — Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [- imageByCompositingOverImage:](<composited(over_).md>) — Returns a new image created by compositing the original image over the specified destination image.
- [- imageByConvertingWorkingSpaceToLab](<convertingworkingspacetolab().md>)
- [- imageByConvertingLabToWorkingSpace](<convertinglabtoworkingspace().md>)
- [- imageByColorMatchingColorSpaceToWorkingSpace:](<matchedtoworkingspace(from_).md>) — Returns a new image created by color matching from the specified color space to the context’s working color space.
- [- imageByColorMatchingWorkingSpaceToColorSpace:](<matchedfromworkingspace(to_).md>) — Returns a new image created by color matching from the context’s working color space to the specified color space.
- [- imageByPremultiplyingAlpha](<premultiplyingalpha().md>) — Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [- imageByUnpremultiplyingAlpha](<unpremultiplyingalpha().md>) — Returns a new image created by dividing the image’s RGB values by its alpha values.
- [- imageBySettingAlphaOneInExtent:](<settingalphaone(in_).md>) — Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
