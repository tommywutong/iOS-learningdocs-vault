---
title: 'init(genericCMYKCyan:magenta:yellow:black:alpha:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolor/init(genericcmykcyan:magenta:yellow:black:alpha:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/init(genericcmykcyan:magenta:yellow:black:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/init%28genericcmykcyan%3Amagenta%3Ayellow%3Ablack%3Aalpha%3A%29.json'
content_hash: 'sha256:d53c6a1c0fed1171'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# init(genericCMYKCyan:magenta:yellow:black:alpha:)

<sub>Initializer</sub>

Creates a color in the Generic CMYK color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(genericCMYKCyan cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)
```

## Parameters

- `cyan` — A cyan value (`0.0` - `1.0`).

- `magenta` — A magenta value (`0.0` - `1.0`).

- `yellow` — A yellow value (`0.0` - `1.0`).

- `black` — A black value (`0.0` - `1.0`).

- `alpha` — An alpha value `(0.0 - 1.0)`.

## Return Value

A color object.

## See Also

### Creating Colors

- [CGColorCreateCopy](<copy().md>) — Creates a copy of an existing color.
- [CGColorCreateCopyWithAlpha](<copy(alpha_).md>) — Creates a copy of an existing color, substituting a new alpha value.
- [CGColorCreateGenericGray](<init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreateSRGB](<init(srgbred_green_blue_alpha_).md>) — Creates a color in the sRGB color space.
- [CGColorCreate](<init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
- [CGColorCreateWithPattern](<init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
