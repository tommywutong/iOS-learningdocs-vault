---
title: 'copy(alpha:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcolor/copy(alpha:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor/copy(alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor/copy%28alpha%3A%29.json'
content_hash: 'sha256:ffd2fb08f6e1d11f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGColor](../cgcolor.md)

# copy(alpha:)

<sub>Instance Method</sub>

Creates a copy of an existing color, substituting a new alpha value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy(alpha: CGFloat) -> CGColor?
```

## Parameters

- `alpha` — A value that specifies the desired opacity of the copy. Values outside the range `[0,1]` are clamped to `0` or `1`.

## Return Value

A copy of the specified color, using the specified alpha value. In Objective-C, you’re responsible for releasing this object using [CGColorRelease](../cgcolorrelease.md).

## See Also

### Creating Colors

- [CGColorCreateCopy](<copy().md>) — Creates a copy of an existing color.
- [CGColorCreateGenericCMYK](<init(genericcmykcyan_magenta_yellow_black_alpha_).md>) — Creates a color in the Generic CMYK color space.
- [CGColorCreateGenericGray](<init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreateSRGB](<init(srgbred_green_blue_alpha_).md>) — Creates a color in the sRGB color space.
- [CGColorCreate](<init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
- [CGColorCreateWithPattern](<init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
