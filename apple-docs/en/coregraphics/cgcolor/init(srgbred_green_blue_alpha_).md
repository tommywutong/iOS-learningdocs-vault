---
title: 'init(srgbRed:green:blue:alpha:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolor/init(srgbred:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/init(srgbred:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/init%28srgbred%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:219d915e9a31753a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# init(srgbRed:green:blue:alpha:)

<sub>Initializer</sub>

Creates a color in the sRGB color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(srgbRed red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

## Parameters

- `red` — A red component value `(0.0 - 1.0)`.

- `green` — A green component value `(0.0 - 1.0)`.

- `blue` — A blue component value `(0.0 - 1.0)`.

- `alpha` — An alpha value `(0.0 - 1.0)`.

## Return Value

A color object.

## See Also

### Creating Colors

- [CGColorCreateCopy](<copy().md>) — Creates a copy of an existing color.
- [CGColorCreateCopyWithAlpha](<copy(alpha_).md>) — Creates a copy of an existing color, substituting a new alpha value.
- [CGColorCreateGenericCMYK](<init(genericcmykcyan_magenta_yellow_black_alpha_).md>) — Creates a color in the Generic CMYK color space.
- [CGColorCreateGenericGray](<init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreate](<init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
- [CGColorCreateWithPattern](<init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
