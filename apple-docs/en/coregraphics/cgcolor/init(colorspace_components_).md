---
title: 'init(colorSpace:components:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolor/init(colorspace:components:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/init(colorspace:components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/init%28colorspace%3Acomponents%3A%29.json'
content_hash: 'sha256:f159ce2b8b8e8921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# init(colorSpace:components:)

<sub>Initializer</sub>

Creates a color using a list of intensity values (including alpha) and an associated color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(colorSpace space: CGColorSpace, components: UnsafePointer<CGFloat>)
```

## Parameters

- `space` — A color space for the new color. Core Graphics retains this object; upon return, you may safely release it.

- `components` — An array of intensity values describing the color. The array should contain _n_+1 values that correspond to the _n_ color components in the specified color space, followed by the alpha component. Each component value should be in the range appropriate for the color space. Values outside this range will be clamped to the nearest correct value.

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
- [CGColorCreateWithPattern](<init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
