---
title: 'setDepthTestBounds(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthtestbounds(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthtestbounds(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthtestbounds%28_%3A%29.json'
content_hash: 'sha256:719c16e56cc47448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setDepthTestBounds(_:)

<sub>Instance Method</sub>

Configures the range for depth bounds testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthTestBounds(_ bounds: ClosedRange<Float>)
```

## Parameters

- `bounds` — A closed range the renderer applies to depth bounds testing. The renderer discards fragments with a stored depth that is outside `bounds`.

## Discussion

The render command encoder disables depth bounds testing by default. The render command encoder also disables depth bounds testing when the `bounds` property equals `0.0...1.0`. `bounds.lowerBound` needs to be greater than or equal to `0.0`. `bounds.upperBound` needs to be less than or equal to `1.0`.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.
