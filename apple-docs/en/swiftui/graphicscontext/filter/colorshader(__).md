---
title: 'colorShader(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/colorshader(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colorshader(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/colorshader%28_%3A%29.json'
content_hash: 'sha256:62334ba115e5e9b2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# colorShader(_:)

<sub>Type Method</sub>

Returns a filter that applies `shader` to the color of each source pixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static func colorShader(_ shader: Shader) -> GraphicsContext.Filter
```

## Parameters

- `shader` — The shader to apply to `self` as a color filter.

## Return Value

A filter that applies the shader  as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, half4 color, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader and `color` its source color, as a pre-multiplied color in the destination color space. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the modified color value.

## See Also

### Using a custom Metal shader

- [distortionShader(_:maxSampleOffset:)](<distortionshader(__maxsampleoffset_).md>) — Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.
- [layerShader(_:maxSampleOffset:)](<layershader(__maxsampleoffset_).md>) — Returns a filter that applies `shader` to the contents of the source layer.
