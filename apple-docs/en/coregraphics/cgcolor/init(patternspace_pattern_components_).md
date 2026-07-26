---
title: 'init(patternSpace:pattern:components:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolor/init(patternspace:pattern:components:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/init(patternspace:pattern:components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/init%28patternspace%3Apattern%3Acomponents%3A%29.json'
content_hash: 'sha256:2c0793af92435c80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# init(patternSpace:pattern:components:)

<sub>Initializer</sub>

Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(patternSpace space: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)
```

## Parameters

- `space` — A pattern color space for the new color. Core Graphics retains the color space you pass in. On return, you may safely release it.

- `pattern` — A pattern for the new color object. Core Graphics retains the pattern you pass in. On return, you may safely release it.

- `components` — An array of intensity values describing the color. The array should contain `n + 1` values that correspond to the `n` color components in the specified color space, followed by the alpha component. Each component value should be in the range appropriate for the color space. Values outside this range will be clamped to the nearest correct value.

## Return Value

A new color. In Objective-C, you’re responsible for releasing this object using [CGColorRelease](../cgcolorrelease.md).

## See Also

### Creating Colors

- [CGColorCreateCopy](<copy().md>) — Creates a copy of an existing color.
- [CGColorCreateCopyWithAlpha](<copy(alpha_).md>) — Creates a copy of an existing color, substituting a new alpha value.
- [CGColorCreateGenericCMYK](<init(genericcmykcyan_magenta_yellow_black_alpha_).md>) — Creates a color in the Generic CMYK color space.
- [CGColorCreateGenericGray](<init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreateSRGB](<init(srgbred_green_blue_alpha_).md>) — Creates a color in the sRGB color space.
- [CGColorCreate](<init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
