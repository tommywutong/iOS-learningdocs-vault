---
title: colorSpace
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/colorspace
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/colorspace.json'
content_hash: 'sha256:0db21438df3191e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# colorSpace

<sub>Instance Property</sub>

The color space of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorSpace: CGColorSpace? { get }
```

## Discussion

This property’s value is `nil` if the image’s color space cannot be determined.

## See Also

### Getting Image Information

- [definition](definition.md) — Returns a filter shape object that represents the domain of definition of the image.
- [extent](extent.md) — A rectangle that specifies the extent of the image.
- [properties](properties.md) — Returns the metadata properties dictionary of the image.
- [url](url.md) — The URL from which the image was loaded.
- [- imageTransformForOrientation:](<orientationtransform(forexiforientation_).md>) — Returns the transformation needed to reorient the image to the specified orientation.
