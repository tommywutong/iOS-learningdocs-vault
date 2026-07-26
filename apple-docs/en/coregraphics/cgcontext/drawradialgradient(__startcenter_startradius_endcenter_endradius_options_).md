---
title: 'drawRadialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/drawradialgradient%28_%3Astartcenter%3Astartradius%3Aendcenter%3Aendradius%3Aoptions%3A%29.json'
content_hash: 'sha256:77633fad1738e383'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# drawRadialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)

<sub>Instance Method</sub>

Paints a gradient fill that varies along the area defined by the provided starting and ending circles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drawRadialGradient(_ gradient: CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)
```

## Parameters

- `gradient` — A CGGradient object.

- `startCenter` — The coordinate that defines the center of the starting circle.

- `startRadius` — The radius of the starting circle.

- `endCenter` — The coordinate that defines the center of the ending circle.

- `endRadius` — The radius of the ending circle.

- `options` — Option flags ([kCGGradientDrawsBeforeStartLocation](../cggradientdrawingoptions/drawsbeforestartlocation.md) or [kCGGradientDrawsAfterEndLocation](../cggradientdrawingoptions/drawsafterendlocation.md)) that control whether the gradient is drawn before the starting circle or after the ending circle.

## Discussion

The color at location 0 in the CGGradient object is mapped to the circle defined by `startCenter` and `startRadius`. The color at location 1 in the CGGradient object is mapped to the circle defined by `endCenter` and `endRadius`. Colors are linearly interpolated between the starting and ending circles based on the location values of the gradient. The option flags control whether the gradient is drawn before the start point or after the end point.

## See Also

### Drawing Gradients and Shadings

- [CGContextDrawLinearGradient](<drawlineargradient(__start_end_options_).md>) — Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [CGGradientDrawingOptions](../cggradientdrawingoptions.md) — Drawing locations for gradients.
- [CGContextDrawShading](<drawshading(__).md>) — Fills the clipping path of a context with the specified shading.
