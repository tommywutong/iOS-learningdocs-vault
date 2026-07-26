---
title: 'orientationTransform(forExifOrientation:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/orientationtransform(forexiforientation:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/orientationtransform(forexiforientation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/orientationtransform%28forexiforientation%3A%29.json'
content_hash: 'sha256:45bfab281a9901f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# orientationTransform(forExifOrientation:)

<sub>Instance Method</sub>

Returns the transformation needed to reorient the image to the specified orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func orientationTransform(forExifOrientation orientation: Int32) -> CGAffineTransform
```

## Parameters

- `orientation` — An integer specifying an image orientation according to the EXIF specification. For details, see [kCGImagePropertyOrientation](../../imageio/kcgimagepropertyorientation.md).

## Return Value

An affine transform that will rotate or mirror the image to match the specified orientation when applied.

## Discussion

This method determines the transformation needed to match the specified orientation, but does not apply that transformation to the image. To apply the transformation (possibly after concatenating it with other transformations), use the [- imageByApplyingTransform:](<transformed(by_).md>) method or the `CIAffineTransform` filter. To determine and apply the transformation in a single step, use the [- imageByApplyingOrientation:](<oriented(forexiforientation_).md>) method.

## See Also

### Getting Image Information

- [definition](definition.md) — Returns a filter shape object that represents the domain of definition of the image.
- [extent](extent.md) — A rectangle that specifies the extent of the image.
- [properties](properties.md) — Returns the metadata properties dictionary of the image.
- [url](url.md) — The URL from which the image was loaded.
- [colorSpace](colorspace.md) — The color space of the image.
