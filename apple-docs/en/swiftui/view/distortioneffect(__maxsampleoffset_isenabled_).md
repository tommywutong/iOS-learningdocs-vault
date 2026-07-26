---
title: 'distortionEffect(_:maxSampleOffset:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/distortioneffect(_:maxsampleoffset:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/distortioneffect(_:maxsampleoffset:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/distortioneffect%28_%3Amaxsampleoffset%3Aisenabled%3A%29.json'
content_hash: 'sha256:c86ed6e73b91dbd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# distortionEffect(_:maxSampleOffset:isEnabled:)

<sub>Instance Method</sub>

Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func distortionEffect(_ shader: Shader, maxSampleOffset: CGSize, isEnabled: Bool = true) -> some View

```

## Parameters

- `shader` — The shader to apply as a distortion effect.

- `maxSampleOffset` — The maximum distance in each axis between the returned source pixel position and the destination pixel position, for all source pixels.

- `isEnabled` — Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a distortion effect it must have a function signature matching:

```swift
[[ stitchable ]] float2 name(float2 position, args...)
```

where `position` is the user-space coordinates of the destination pixel applied to the shader. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the user-space coordinates of the corresponding source pixel.

> [!important] Important
> Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [Shader](../shader.md) — A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [ShaderFunction](../shaderfunction.md) — A reference to a function in a Metal shader library.
- [ShaderLibrary](../shaderlibrary.md) — A Metal shader library.
