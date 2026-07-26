---
title: 'setStencilReferenceValues(front:back:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setstencilreferencevalues(front:back:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setstencilreferencevalues(front:back:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setstencilreferencevalues%28front%3Aback%3A%29.json'
content_hash: 'sha256:dc75a937b7b4ccc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setStencilReferenceValues(front:back:)

<sub>Instance Method</sub>

Configures different comparison values for front- and back-facing primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setStencilReferenceValues(front frontReferenceValue: UInt32, back backReferenceValue: UInt32)
```

## Parameters

- `frontReferenceValue` — A stencil test comparison value the render pipeline applies to only front-facing primitives.

- `backReferenceValue` — A stencil test comparison value the render pipeline applies to only back-facing primitives.

## Discussion

The command sets separate reference values for front- and back-facing primitives (see [stencilCompareFunction](../mtlstencildescriptor/stencilcomparefunction.md), [frontFaceStencil](../mtldepthstencildescriptor/frontfacestencil.md), and [backFaceStencil](../mtldepthstencildescriptor/backfacestencil.md)). These reference values apply to the stencil state you set with the [- setDepthStencilState:](<setdepthstencilstate(__).md>) method.

The render pass’s default reference value for the front and back stencil compare function is `0`.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
