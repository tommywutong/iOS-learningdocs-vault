---
title: 'radialGradient(_:center:startRadius:endRadius:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/radialgradient%28_%3Acenter%3Astartradius%3Aendradius%3Aoptions%3A%29.json'
content_hash: 'sha256:486d60deafea7aeb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# radialGradient(_:center:startRadius:endRadius:options:)

<sub>Type Method</sub>

Returns a shading instance that fills a radial gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func radialGradient(_ gradient: AnyGradient, center: CGPoint, startRadius: CGFloat, endRadius: CGFloat, options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

## Parameters

- `gradient` — An [AnyGradient](../../anygradient.md) instance that defines the colors of the gradient.

- `center` — The point in the current user space on which SwiftUI centers the gradient.

- `startRadius` — The distance from the center where the gradient starts.

- `endRadius` — The distance from the center where the gradient ends.

- `options` — Options that you use to configure the gradient.

## Return Value

A shading instance filled with a radial gradient.

## See Also

### Gradients

- [linearGradient(_:startPoint:endPoint:options:)](<lineargradient(__startpoint_endpoint_options_).md>) — Returns a shading instance that fills a linear (axial) gradient.
- [conicGradient(_:center:angle:options:)](<conicgradient(__center_angle_options_).md>) — Returns a shading instance that fills a conic (angular) gradient.
