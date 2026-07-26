---
title: 'linearGradient(_:startPoint:endPoint:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/lineargradient%28_%3Astartpoint%3Aendpoint%3Aoptions%3A%29.json'
content_hash: 'sha256:179050f0d4805330'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# linearGradient(_:startPoint:endPoint:options:)

<sub>Type Method</sub>

Returns a shading instance that fills a linear (axial) gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func linearGradient(_ gradient: AnyGradient, startPoint: CGPoint, endPoint: CGPoint, options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

## Parameters

- `gradient` — An [AnyGradient](../../anygradient.md) instance that defines the colors of the gradient.

- `startPoint` — The start point of the gradient axis.

- `endPoint` — The end point of the gradient axis.

- `options` — Options that you use to configure the gradient.

## Return Value

A shading instance filled with a linear gradient.

## Discussion

The shading instance defines an axis from `startPoint` to `endPoint` in the current user space and maps colors from `gradient` to lines perpendicular to the axis.

## See Also

### Gradients

- [radialGradient(_:center:startRadius:endRadius:options:)](<radialgradient(__center_startradius_endradius_options_).md>) — Returns a shading instance that fills a radial gradient.
- [conicGradient(_:center:angle:options:)](<conicgradient(__center_angle_options_).md>) — Returns a shading instance that fills a conic (angular) gradient.
