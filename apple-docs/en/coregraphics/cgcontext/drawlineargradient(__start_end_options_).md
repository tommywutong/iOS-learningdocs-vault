---
title: 'drawLinearGradient(_:start:end:options:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/drawlineargradient(_:start:end:options:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/drawlineargradient(_:start:end:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/drawlineargradient%28_%3Astart%3Aend%3Aoptions%3A%29.json'
content_hash: 'sha256:44a36e52810b7763'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# drawLinearGradient(_:start:end:options:)

<sub>Instance Method</sub>

Paints a gradient fill that varies along the line defined by the provided starting and ending points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drawLinearGradient(_ gradient: CGGradient, start startPoint: CGPoint, end endPoint: CGPoint, options: CGGradientDrawingOptions)
```

## Parameters

- `gradient` — A gradient object.

- `startPoint` — The coordinate that defines the starting point of the gradient.

- `endPoint` — The coordinate that defines the ending point of the gradient.

- `options` — Option flags ([kCGGradientDrawsBeforeStartLocation](../cggradientdrawingoptions/drawsbeforestartlocation.md) or [kCGGradientDrawsAfterEndLocation](../cggradientdrawingoptions/drawsafterendlocation.md)) that control whether the fill is extended beyond the starting or ending point.

## Discussion

The color at location 0 in the CGGradient object is mapped to the starting point. The color at location 1 in the CGGradient object is mapped to the ending point. Colors are linearly interpolated between these two points based on the location values of the gradient. The option flags control whether the gradient is drawn before the start point or after the end point.

## See Also

### Drawing Gradients and Shadings

- [CGContextDrawRadialGradient](<drawradialgradient(__startcenter_startradius_endcenter_endradius_options_).md>) — Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [CGGradientDrawingOptions](../cggradientdrawingoptions.md) — Drawing locations for gradients.
- [CGContextDrawShading](<drawshading(__).md>) — Fills the clipping path of a context with the specified shading.
