---
title: 'distortionEffect(_:maxSampleOffset:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/distortioneffect(_:maxsampleoffset:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/distortioneffect(_:maxsampleoffset:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/distortioneffect%28_%3Amaxsampleoffset%3Aisenabled%3A%29.json'
content_hash: 'sha256:233df0b7dfd36a63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# distortionEffect(_:maxSampleOffset:isEnabled:)

<sub>Instance Method</sub>

Returns a new visual effect that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func distortionEffect(_ shader: Shader, maxSampleOffset: CGSize, isEnabled: Bool = true) -> some VisualEffect

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

### Applying other effects

- [blur(radius:opaque:)](<blur(radius_opaque_).md>) — Applies a Gaussian blur to the view.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter on the raster layer created from `self`.
