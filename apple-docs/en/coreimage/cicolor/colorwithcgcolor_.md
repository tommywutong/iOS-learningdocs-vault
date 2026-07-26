---
title: 'colorWithCGColor:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicolor/colorwithcgcolor:'
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor/colorwithcgcolor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor/colorwithcgcolor%3A.json'
content_hash: 'sha256:a2235fc4b3c121f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColor](../cicolor.md)

# colorWithCGColor:

<sub>Type Method</sub>

Create a Core Image color object with a Core Graphics color object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) colorWithCGColor:(CGColorRef) color;
```

## Return Value

An autoreleased [CIColor](../cicolor.md) instance.

## See Also

### Creating Color Objects

- [+ colorWithRed:green:blue:](<init(red_green_blue_).md>) — Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [colorWithRed:green:blue:alpha:](colorwithred_green_blue_alpha_.md) — Create a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.
- [+ colorWithString:](<init(string_).md>) — Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [+ colorWithRed:green:blue:colorSpace:](<init(red_green_blue_colorspace_)-2og6y.md>) — Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [+ colorWithRed:green:blue:alpha:colorSpace:](<init(red_green_blue_alpha_colorspace_)-5mvff.md>) — Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
