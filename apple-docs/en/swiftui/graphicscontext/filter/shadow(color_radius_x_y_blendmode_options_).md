---
title: 'shadow(color:radius:x:y:blendMode:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/shadow(color:radius:x:y:blendmode:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/shadow(color:radius:x:y:blendmode:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/shadow%28color%3Aradius%3Ax%3Ay%3Ablendmode%3Aoptions%3A%29.json'
content_hash: 'sha256:327be01eeccb4633'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# shadow(color:radius:x:y:blendMode:options:)

<sub>Type Method</sub>

Returns a filter that adds a shadow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0, blendMode: GraphicsContext.BlendMode = .normal, options: GraphicsContext.ShadowOptions = ShadowOptions()) -> GraphicsContext.Filter
```

## Parameters

- `color` — A [Color](../../color.md) that tints the shadow.

- `radius` — A measure of how far the shadow extends from the edges of the content receiving the shadow.

- `x` — An amount to translate the shadow horizontally.

- `y` — An amount to translate the shadow vertically.

- `blendMode` — The [BlendMode](../blendmode-swift.struct.md) to use when blending the shadow into the background layer.

- `options` — A set of options that you can use to customize the process of adding the shadow. Use one or more of the options in [ShadowOptions](../shadowoptions.md).

## Return Value

A filter that adds a shadow style.

## Discussion

SwiftUI produces the shadow by blurring the alpha channel of the object receiving the shadow, multiplying the result by a color, optionally translating the shadow by an amount, and then blending the resulting shadow into a new layer below the source primitive. You can customize some of these steps by adding one or more shadow options.
