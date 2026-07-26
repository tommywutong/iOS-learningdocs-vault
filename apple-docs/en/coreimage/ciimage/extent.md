---
title: extent
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/extent
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/extent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/extent.json'
content_hash: 'sha256:78dd6242c873e994'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# extent

<sub>Instance Property</sub>

A rectangle that specifies the extent of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extent: CGRect { get }
```

## Discussion

This rectangle specifies the extent of the image in working space coordinates.

## See Also

### Getting Image Information

- [definition](definition.md) — Returns a filter shape object that represents the domain of definition of the image.
- [properties](properties.md) — Returns the metadata properties dictionary of the image.
- [url](url.md) — The URL from which the image was loaded.
- [colorSpace](colorspace.md) — The color space of the image.
- [- imageTransformForOrientation:](<orientationtransform(forexiforientation_).md>) — Returns the transformation needed to reorient the image to the specified orientation.
