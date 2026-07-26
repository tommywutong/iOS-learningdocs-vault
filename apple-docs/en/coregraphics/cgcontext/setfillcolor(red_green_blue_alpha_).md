---
title: 'setFillColor(red:green:blue:alpha:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setfillcolor(red:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setfillcolor(red:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setfillcolor%28red%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:c93e5c6a0673769c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setFillColor(red:green:blue:alpha:)

<sub>Instance Method</sub>

Sets the current fill color to a value in the DeviceRGB color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setFillColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)
```

## Parameters

- `red` — The red intensity value for the color to set. The DeviceRGB color space permits the specification of a value ranging from `0.0` (zero intensity) to `1.0` (full intensity).

- `green` — The green intensity value for the color to set. The DeviceRGB color space permits the specification of a value ranging from `0.0` (zero intensity) to `1.0` (full intensity).

- `blue` — The blue intensity value for the color to set. The DeviceRGB color space permits the specification of a value ranging from `0.0` (zero intensity) to `1.0` (full intensity).

- `alpha` — A value that specifies the opacity level. Values can range from `0.0` (transparent) to `1.0` (opaque). Values outside this range are clipped to `0.0` or `1.0`.

## Discussion

When you call this function, two things happen:

- Core Graphics sets the current fill color space to DeviceRGB.
- Core Graphics sets the current fill color to the value specified by the `red`, `green`, `blue`, and `alpha` parameters.

## See Also

### Setting Fill, Stroke, and Shadow Colors

- [CGContextSetFillColorWithColor](<setfillcolor(__)-8lhn8.md>) — Sets the current fill color in a graphics context, using a CGColor.
- [CGContextSetFillColor](<setfillcolor(__)-756dy.md>) — Sets the current fill color.
- [CGContextSetCMYKFillColor](<setfillcolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current fill color to a value in the DeviceCMYK color space.
- [CGContextSetGrayFillColor](<setfillcolor(gray_alpha_).md>) — Sets the current fill color to a value in the DeviceGray color space.
- [CGContextSetFillColorSpace](<setfillcolorspace(__).md>) — Sets the fill color space in a graphics context.
- [CGContextSetShadow](<setshadow(offset_blur_).md>) — Enables shadowing in a graphics context.
- [CGContextSetShadowWithColor](<setshadow(offset_blur_color_).md>) — Enables shadowing with color a graphics context.
- [CGContextSetStrokeColorWithColor](<setstrokecolor(__)-1sskg.md>) — Sets the current stroke color in a context, using a CGColor.
- [CGContextSetStrokeColor](<setstrokecolor(__)-4pd8p.md>) — Sets the current stroke color.
- [CGContextSetCMYKStrokeColor](<setstrokecolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current stroke color to a value in the DeviceCMYK color space.
- [CGContextSetGrayStrokeColor](<setstrokecolor(gray_alpha_).md>) — Sets the current stroke color to a value in the DeviceGray color space.
- [CGContextSetRGBStrokeColor](<setstrokecolor(red_green_blue_alpha_).md>) — Sets the current stroke color to a value in the DeviceRGB color space.
- [CGContextSetStrokeColorSpace](<setstrokecolorspace(__).md>) — Sets the stroke color space in a graphics context.
- [CGContextSetStrokePattern](<setstrokepattern(__colorcomponents_).md>) — Sets the stroke pattern in the specified graphics context.
- [CGContextSetAlpha](<setalpha(__).md>) — Sets the opacity level for objects drawn in a graphics context.
