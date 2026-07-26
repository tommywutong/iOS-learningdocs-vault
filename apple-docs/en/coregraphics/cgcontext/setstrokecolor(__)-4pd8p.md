---
title: 'setStrokeColor(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setstrokecolor(_:)-4pd8p'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setstrokecolor(_:)-4pd8p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setstrokecolor%28_%3A%29-4pd8p.json'
content_hash: 'sha256:2de3e7f6ed189b5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setStrokeColor(_:)

<sub>Instance Method</sub>

Sets the current stroke color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setStrokeColor(_ components: UnsafePointer<CGFloat>)
```

## Parameters

- `components` — An array of intensity values describing the color to set. The number of array elements must equal the number of components in the current stroke color space, plus an additional component for the alpha value.

## Discussion

The current stroke color space must not be a pattern color space. For information on setting the stroke color when using a pattern color space, see [CGContextSetStrokePattern](<setstrokepattern(__colorcomponents_).md>). Note that the preferred API is now [CGContextSetStrokeColorWithColor](<setstrokecolor(__)-1sskg.md>).

## See Also

### Setting Fill, Stroke, and Shadow Colors

- [CGContextSetFillColorWithColor](<setfillcolor(__)-8lhn8.md>) — Sets the current fill color in a graphics context, using a CGColor.
- [CGContextSetFillColor](<setfillcolor(__)-756dy.md>) — Sets the current fill color.
- [CGContextSetCMYKFillColor](<setfillcolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current fill color to a value in the DeviceCMYK color space.
- [CGContextSetGrayFillColor](<setfillcolor(gray_alpha_).md>) — Sets the current fill color to a value in the DeviceGray color space.
- [CGContextSetRGBFillColor](<setfillcolor(red_green_blue_alpha_).md>) — Sets the current fill color to a value in the DeviceRGB color space.
- [CGContextSetFillColorSpace](<setfillcolorspace(__).md>) — Sets the fill color space in a graphics context.
- [CGContextSetShadow](<setshadow(offset_blur_).md>) — Enables shadowing in a graphics context.
- [CGContextSetShadowWithColor](<setshadow(offset_blur_color_).md>) — Enables shadowing with color a graphics context.
- [CGContextSetStrokeColorWithColor](<setstrokecolor(__)-1sskg.md>) — Sets the current stroke color in a context, using a CGColor.
- [CGContextSetCMYKStrokeColor](<setstrokecolor(cyan_magenta_yellow_black_alpha_).md>) — Sets the current stroke color to a value in the DeviceCMYK color space.
- [CGContextSetGrayStrokeColor](<setstrokecolor(gray_alpha_).md>) — Sets the current stroke color to a value in the DeviceGray color space.
- [CGContextSetRGBStrokeColor](<setstrokecolor(red_green_blue_alpha_).md>) — Sets the current stroke color to a value in the DeviceRGB color space.
- [CGContextSetStrokeColorSpace](<setstrokecolorspace(__).md>) — Sets the stroke color space in a graphics context.
- [CGContextSetStrokePattern](<setstrokepattern(__colorcomponents_).md>) — Sets the stroke pattern in the specified graphics context.
- [CGContextSetAlpha](<setalpha(__).md>) — Sets the opacity level for objects drawn in a graphics context.
