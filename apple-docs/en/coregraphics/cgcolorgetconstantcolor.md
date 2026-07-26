---
title: CGColorGetConstantColor
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.5+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorgetconstantcolor
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorgetconstantcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorgetconstantcolor.json'
content_hash: 'sha256:cc17ec50a4cc8656'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorGetConstantColor

<sub>Function</sub>

Returns a color object that represents a constant color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGColorRefCGColorGetConstantColor(CFStringRef colorName);
```

## Parameters

- `colorName` — A color name. You can pass any of constants in [Getting System Colors](cgcolor.md#Getting-System-Colors).

## Return Value

A color object.

## Discussion

As this function is not a “Copy” or “Create” function, it does not necessarily return a new reference each time it’s called. As a consequence, you should not release the returned value. However, colors returned from this function can be retained and released in a properly nested fashion, just as any other Core Foundation type can.

## See Also

### Creating Colors

- [CGColorCreateCopy](<cgcolor/copy().md>) — Creates a copy of an existing color.
- [CGColorCreateCopyWithAlpha](<cgcolor/copy(alpha_).md>) — Creates a copy of an existing color, substituting a new alpha value.
- [CGColorCreateGenericCMYK](<cgcolor/init(genericcmykcyan_magenta_yellow_black_alpha_).md>) — Creates a color in the Generic CMYK color space.
- [CGColorCreateGenericGray](<cgcolor/init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<cgcolor/init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<cgcolor/init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreateSRGB](<cgcolor/init(srgbred_green_blue_alpha_).md>) — Creates a color in the sRGB color space.
- [CGColorCreate](<cgcolor/init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
- [CGColorCreateWithPattern](<cgcolor/init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
