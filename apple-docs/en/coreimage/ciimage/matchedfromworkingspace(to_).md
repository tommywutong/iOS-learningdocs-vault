---
title: 'matchedFromWorkingSpace(to:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/matchedfromworkingspace(to:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/matchedfromworkingspace(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/matchedfromworkingspace%28to%3A%29.json'
content_hash: 'sha256:a859637b5376559a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# matchedFromWorkingSpace(to:)

<sub>Instance Method</sub>

Returns a new image created by color matching from the context’s working color space to the specified color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func matchedFromWorkingSpace(to colorSpace: CGColorSpace) -> CIImage?
```

## Parameters

- `colorSpace` — The color space to be converted to. This color space must conform to the [CGColorSpaceModel.rgb](../../coregraphics/cgcolorspacemodel/rgb.md) color space model.

## Return Value

An image object representing the result of the color matching operation, or `nil` if the color spaces to be converted are not compatible.

## See Also

### Creating an Image by Modifying an Existing Image

- [- imageByApplyingFilter:withInputParameters:](<applyingfilter(__parameters_).md>) — Returns a new image created by applying a filter to the original image with the specified name and parameters.
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
- [- imageByPremultiplyingAlpha](<premultiplyingalpha().md>) — Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [- imageByUnpremultiplyingAlpha](<unpremultiplyingalpha().md>) — Returns a new image created by dividing the image’s RGB values by its alpha values.
- [- imageBySettingAlphaOneInExtent:](<settingalphaone(in_).md>) — Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
