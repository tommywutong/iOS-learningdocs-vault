---
title: copy()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolor/copy()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/copy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/copy%28%29.json'
content_hash: 'sha256:15b62310906e0eb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# copy()

<sub>Instance Method</sub>

Creates a copy of an existing color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy() -> CGColor?
```

## Return Value

A copy of the specified color. In Objective-C, you’re responsible for releasing this object using [CGColorRelease](../cgcolorrelease.md).

## See Also

### Creating Colors

- [CGColorCreateCopyWithAlpha](<copy(alpha_).md>) — Creates a copy of an existing color, substituting a new alpha value.
- [CGColorCreateGenericCMYK](<init(genericcmykcyan_magenta_yellow_black_alpha_).md>) — Creates a color in the Generic CMYK color space.
- [CGColorCreateGenericGray](<init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreateSRGB](<init(srgbred_green_blue_alpha_).md>) — Creates a color in the sRGB color space.
- [CGColorCreate](<init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
- [CGColorCreateWithPattern](<init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
