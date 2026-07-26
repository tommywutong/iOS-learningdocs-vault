---
title: CGGradientDrawingOptions
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggradientdrawingoptions
source_url: 'https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggradientdrawingoptions.json'
content_hash: 'sha256:10a0af58d4294b1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGradientDrawingOptions

<sub>Structure</sub>

Drawing locations for gradients.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGGradientDrawingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCGGradientDrawsBeforeStartLocation](cggradientdrawingoptions/drawsbeforestartlocation.md) — The fill should extend beyond the starting location. The color that extends beyond the starting point is the solid color defined by the [CGGradient](cggradient.md) object to be at location 0.
- [kCGGradientDrawsAfterEndLocation](cggradientdrawingoptions/drawsafterendlocation.md) — The fill should extend beyond the ending location. The color that extends beyond the ending point is the solid color defined by the [CGGradient](cggradient.md) object to be at location 1.

### Initializers

- [init(rawValue:)](<cggradientdrawingoptions/init(rawvalue_).md>)

## See Also

### Drawing Gradients and Shadings

- [CGContextDrawLinearGradient](<cgcontext/drawlineargradient(__start_end_options_).md>) — Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [CGContextDrawRadialGradient](<cgcontext/drawradialgradient(__startcenter_startradius_endcenter_endradius_options_).md>) — Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [CGContextDrawShading](<cgcontext/drawshading(__).md>) — Fills the clipping path of a context with the specified shading.
