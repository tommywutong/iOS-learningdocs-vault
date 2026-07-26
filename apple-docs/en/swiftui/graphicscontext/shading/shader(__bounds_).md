---
title: 'shader(_:bounds:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/shader(_:bounds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/shader(_:bounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/shader%28_%3Abounds%3A%29.json'
content_hash: 'sha256:08b0e90f890388b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# shader(_:bounds:)

<sub>Type Method</sub>

Returns a shading instance that fills with the results of querying a shader for each pixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static func shader(_ shader: Shader, bounds: CGRect = .zero) -> GraphicsContext.Shading
```

## Parameters

- `shader` — The shader defining the filled colors.

- `bounds` — The rect used to define any `bounds` arguments of the shader.

## Return Value

A shading instance that fills using the shader.

## Discussion

For a shader function to act as a shape fill it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader, and `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the premultiplied color value in the color space of the destination (typically sRGB).
