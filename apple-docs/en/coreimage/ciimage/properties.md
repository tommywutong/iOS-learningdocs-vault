---
title: properties
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/properties
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/properties.json'
content_hash: 'sha256:6b2d96268d29fa02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# properties

<sub>Instance Property</sub>

Returns the metadata properties dictionary of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var properties: [String : Any] { get }
```

## Discussion

If the [CIImage](../ciimage.md) was created from `NSURL` or `NSData` then this dictionary is determined by calling `CGImageSourceCopyPropertiesAtIndex()`.

If the [CIImage](../ciimage.md) was created with the [kCIImageProperties](../ciimageoption/properties.md) option, then that dictionary is returned.

If the [CIImage](../ciimage.md) was created by applying [CIFilter](../cifilter-swift.class.md) or [CIKernel](../cikernel.md) then the properties of the root inputImage will be returned.

## See Also

### Getting Image Information

- [definition](definition.md) — Returns a filter shape object that represents the domain of definition of the image.
- [extent](extent.md) — A rectangle that specifies the extent of the image.
- [url](url.md) — The URL from which the image was loaded.
- [colorSpace](colorspace.md) — The color space of the image.
- [- imageTransformForOrientation:](<orientationtransform(forexiforientation_).md>) — Returns the transformation needed to reorient the image to the specified orientation.
