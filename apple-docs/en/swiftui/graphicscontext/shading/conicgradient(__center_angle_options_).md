---
title: 'conicGradient(_:center:angle:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/conicgradient(_:center:angle:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/conicgradient(_:center:angle:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/conicgradient%28_%3Acenter%3Aangle%3Aoptions%3A%29.json'
content_hash: 'sha256:a7dc18f13872f015'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# conicGradient(_:center:angle:options:)

<sub>Type Method</sub>

Returns a shading instance that fills a conic (angular) gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func conicGradient(_ gradient: AnyGradient, center: CGPoint, angle: Angle = Angle(), options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

## Parameters

- `gradient` — An [AnyGradient](../../anygradient.md) instance that defines the colors of the gradient.

- `center` — The point in the current user space on which SwiftUI centers the gradient.

- `angle` — The angle about the center that SwiftUI uses to start and finish the gradient. The gradient sweeps all the way around the center.

- `options` — Options that you use to configure the gradient.

## Return Value

A shading instance filled with a conic gradient.

## See Also

### Gradients

- [linearGradient(_:startPoint:endPoint:options:)](<lineargradient(__startpoint_endpoint_options_).md>) — Returns a shading instance that fills a linear (axial) gradient.
- [radialGradient(_:center:startRadius:endRadius:options:)](<radialgradient(__center_startradius_endradius_options_).md>) — Returns a shading instance that fills a radial gradient.
