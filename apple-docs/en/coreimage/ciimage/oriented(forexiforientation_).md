---
title: 'oriented(forExifOrientation:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/oriented(forexiforientation:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/oriented(forexiforientation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/oriented%28forexiforientation%3A%29.json'
content_hash: 'sha256:cc366ffab32b695e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# oriented(forExifOrientation:)

<sub>Instance Method</sub>

Returns a new image created by transforming the original image to the specified EXIF orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func oriented(forExifOrientation orientation: Int32) -> CIImage
```

## Parameters

- `orientation` — An integer specifying an image orientation according to the EXIF specification. For details, see [kCGImagePropertyOrientation](../../imageio/kcgimagepropertyorientation.md).

## Return Value

An image object representing the result of rotating or mirroring the image to the target orientation.

## Discussion

This method determines and then applies the transformation needed to reorient the image to the specified orientation. If you plan to also apply other transformations, you can retrieve the transformation this method would use by calling the [- imageTransformForOrientation:](<orientationtransform(forexiforientation_).md>) method.

## See Also

### Creating an Image by Modifying an Existing Image

- [- imageByApplyingFilter:withInputParameters:](<applyingfilter(__parameters_).md>) — Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [- imageByApplyingFilter:](<applyingfilter(__).md>) — Applies the filter to an image and returns the output.
- [- imageByApplyingTransform:](<transformed(by_).md>) — Returns a new image that represents the original image after applying an affine transform.
- [- imageByApplyingTransform:highQualityDownsample:](<transformed(by_highqualitydownsample_).md>)
- [- imageByCroppingToRect:](<cropped(to_).md>) — Returns a new image with a cropped portion of the original image.
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
