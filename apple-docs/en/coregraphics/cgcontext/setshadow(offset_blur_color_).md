---
title: 'setShadow(offset:blur:color:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setshadow(offset:blur:color:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setshadow(offset:blur:color:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setshadow%28offset%3Ablur%3Acolor%3A%29.json'
content_hash: 'sha256:663fd82a86cfa8a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setShadow(offset:blur:color:)

<sub>Instance Method</sub>

Enables shadowing with color a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setShadow(offset: CGSize, blur: CGFloat, color: CGColor?)
```

## Parameters

- `offset` — Specifies a translation in base-space.

- `blur` — A non-negative number specifying the amount of blur.

- `color` — Specifies the color of the shadow, which may contain a non-opaque alpha value. If `NULL`, then shadowing is disabled.

## See Also

### Setting Fill, Stroke, and Shadow Colors

- [CGContextSetFillColorWithColor](<setfillcolor(__)-8lhn8.md>) — Sets the current fill color in a graphics context, using a CGColor.
- [CGContextSetFillColor](<setfillcolor(__)-756dy.md>) — Sets the current fill color.
- [CGContextSetCMYKFillColor](<setfillcolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current fill color to a value in the DeviceCMYK color space.
- [CGContextSetGrayFillColor](<setfillcolor(gray_alpha_).md>) — Sets the current fill color to a value in the DeviceGray color space.
- [CGContextSetRGBFillColor](<setfillcolor(red_green_blue_alpha_).md>) — Sets the current fill color to a value in the DeviceRGB color space.
- [CGContextSetFillColorSpace](<setfillcolorspace(__).md>) — Sets the fill color space in a graphics context.
- [CGContextSetShadow](<setshadow(offset_blur_).md>) — Enables shadowing in a graphics context.
- [CGContextSetStrokeColorWithColor](<setstrokecolor(__)-1sskg.md>) — Sets the current stroke color in a context, using a CGColor.
- [CGContextSetStrokeColor](<setstrokecolor(__)-4pd8p.md>) — Sets the current stroke color.
- [CGContextSetCMYKStrokeColor](<setstrokecolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current stroke color to a value in the DeviceCMYK color space.
- [CGContextSetGrayStrokeColor](<setstrokecolor(gray_alpha_).md>) — Sets the current stroke color to a value in the DeviceGray color space.
- [CGContextSetRGBStrokeColor](<setstrokecolor(red_green_blue_alpha_).md>) — Sets the current stroke color to a value in the DeviceRGB color space.
- [CGContextSetStrokeColorSpace](<setstrokecolorspace(__).md>) — Sets the stroke color space in a graphics context.
- [CGContextSetStrokePattern](<setstrokepattern(__colorcomponents_).md>) — Sets the stroke pattern in the specified graphics context.
- [CGContextSetAlpha](<setalpha(__).md>) — Sets the opacity level for objects drawn in a graphics context.
