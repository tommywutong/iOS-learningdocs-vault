---
title: 'setStencilReferenceValue(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setstencilreferencevalue(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setstencilreferencevalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setstencilreferencevalue%28_%3A%29.json'
content_hash: 'sha256:1ed8c3c7c3197dc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setStencilReferenceValue(_:)

<sub>Instance Method</sub>

Configures the same comparison value for front- and back-facing primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setStencilReferenceValue(_ referenceValue: UInt32)
```

## Parameters

- `referenceValue` — A stencil test comparison value the render pipeline applies to both front- and back-facing primitives.

## Discussion

The command sets the same reference value for front- and back-facing primitives (see [stencilCompareFunction](../mtlstencildescriptor/stencilcomparefunction.md), [frontFaceStencil](../mtldepthstencildescriptor/frontfacestencil.md), and [backFaceStencil](../mtldepthstencildescriptor/backfacestencil.md)). This reference value applies to the stencil state you set with the [- setDepthStencilState:](<setdepthstencilstate(__).md>) method.

The render pass’s default reference value for the front and back stencil compare function is `0`.

## See Also

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.
