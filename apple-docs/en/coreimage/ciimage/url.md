---
title: url
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/url
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/url.json'
content_hash: 'sha256:48fdd58daf463c73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# url

<sub>Instance Property</sub>

The URL from which the image was loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var url: URL? { get }
```

## Discussion

A URL is available only if the image object was created with a URL (such as with the [- initWithContentsOfURL:](<init(contentsof_).md>) method or related methods). Otherwise, this property’s value is `nil`.

## See Also

### Getting Image Information

- [definition](definition.md) — Returns a filter shape object that represents the domain of definition of the image.
- [extent](extent.md) — A rectangle that specifies the extent of the image.
- [properties](properties.md) — Returns the metadata properties dictionary of the image.
- [colorSpace](colorspace.md) — The color space of the image.
- [- imageTransformForOrientation:](<orientationtransform(forexiforientation_).md>) — Returns the transformation needed to reorient the image to the specified orientation.
