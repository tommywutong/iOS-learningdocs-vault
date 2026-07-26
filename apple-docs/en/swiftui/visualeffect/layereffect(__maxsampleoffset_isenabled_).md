---
title: 'layerEffect(_:maxSampleOffset:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/layereffect(_:maxsampleoffset:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/layereffect(_:maxsampleoffset:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/layereffect%28_%3Amaxsampleoffset%3Aisenabled%3A%29.json'
content_hash: 'sha256:804ca5161f02e363'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# layerEffect(_:maxSampleOffset:isEnabled:)

<sub>Instance Method</sub>

Returns a new visual effect that applies `shader` to `self` as a filter on the raster layer created from `self`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func layerEffect(_ shader: Shader, maxSampleOffset: CGSize, isEnabled: Bool = true) -> some VisualEffect

```

## Parameters

- `shader` — The shader to apply as a layer effect.

- `maxSampleOffset` — If the shader function samples from the layer at locations not equal to the destination position, this value must specify the maximum sampling distance in each axis, for all source pixels.

- `isEnabled` — Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a distortion effect.

## Discussion

For a shader function to act as a layer effect it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position,
  SwiftUI::Layer layer, args...)
```

where `position` is the user-space coordinates of the destination pixel applied to the shader, and `layer` is a subregion of the rasterized contents of `self`. `args...` should be compatible with the uniform arguments bound to `shader`.

The `SwiftUI::Layer` type is defined in the `<SwiftUI/SwiftUI.h>` header file. It exports a single `sample()` function that returns a linearly-filtered pixel value from a position in the source content, as a premultiplied RGBA pixel value:

```swift
namespace SwiftUI {
  struct Layer {
    half4 sample(float2 position) const;
  };
};
```

The function should return the color mapping to the destination pixel, typically by sampling one or more pixels from `layer` at location(s) derived from `position` and them applying some kind of transformation to produce a new color.

> [!important] Important
> Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## See Also

### Applying other effects

- [blur(radius:opaque:)](<blur(radius_opaque_).md>) — Applies a Gaussian blur to the view.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
