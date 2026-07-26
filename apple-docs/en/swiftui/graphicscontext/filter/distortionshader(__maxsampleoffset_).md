---
title: 'distortionShader(_:maxSampleOffset:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/distortionshader(_:maxsampleoffset:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/distortionshader(_:maxsampleoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/distortionshader%28_%3Amaxsampleoffset%3A%29.json'
content_hash: 'sha256:89c94e701f506ec2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# distortionShader(_:maxSampleOffset:)

<sub>Type Method</sub>

Returns a filter that applies `shader` as a geometric distortion effect on the location of each pixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static func distortionShader(_ shader: Shader, maxSampleOffset: CGSize) -> GraphicsContext.Filter
```

## Parameters

- `shader` — The shader to apply as a distortion effect.

- `maxSampleOffset` — The maximum distance in each axis between the returned source pixel position and the destination pixel position, for all source pixels.

## Return Value

A new filter that applies the shader as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function signature matching:

```swift
[[ stitchable ]] float2 name(float2 position, args...)
```

where `position` is the user-space coordinates of the destination pixel applied to the shader. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the user-space coordinates of the corresponding source pixel.

## See Also

### Using a custom Metal shader

- [colorShader(_:)](<colorshader(__).md>) — Returns a filter that applies `shader` to the color of each source pixel.
- [layerShader(_:maxSampleOffset:)](<layershader(__maxsampleoffset_).md>) — Returns a filter that applies `shader` to the contents of the source layer.
