---
title: definition
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/definition
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/definition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/definition.json'
content_hash: 'sha256:596cd99b8304231d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# definition

<sub>Instance Property</sub>

Returns a filter shape object that represents the domain of definition of the image.

<sub>macOS</sub>

```swift
var definition: CIFilterShape { get }
```

## Return Value

A filter shape object.

## See Also

### Getting Image Information

- [extent](extent.md) — A rectangle that specifies the extent of the image.
- [properties](properties.md) — Returns the metadata properties dictionary of the image.
- [url](url.md) — The URL from which the image was loaded.
- [colorSpace](colorspace.md) — The color space of the image.
- [- imageTransformForOrientation:](<orientationtransform(forexiforientation_).md>) — Returns the transformation needed to reorient the image to the specified orientation.
