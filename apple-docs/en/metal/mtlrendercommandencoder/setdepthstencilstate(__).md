---
title: 'setDepthStencilState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthstencilstate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstencilstate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthstencilstate%28_%3A%29.json'
content_hash: 'sha256:8276dd3601f93729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setDepthStencilState(_:)

<sub>Instance Method</sub>

Configures the combined depth and stencil state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthStencilState(_ depthStencilState: (any MTLDepthStencilState)?)
```

## Parameters

- `depthStencilState` — An instance that conforms to the [MTLDepthStencilState](../mtldepthstencilstate.md) protocol.

## Discussion

This method changes the combined depth and stencil state for the render command encoder that’s compatible with its depth and stencil attachment configuration. For example, if the new state enables depth testing or depth writing, the render pass needs to have a depth attachment. Similarly, if the new state enables stencil testing or stencil writing, the render pass’s stencil needs to have a stencil attachment. You create depth and stencil attachments for a render pass by assigning the [depthAttachment](../mtlrenderpassdescriptor/depthattachment.md) and [stencilAttachment](../mtlrenderpassdescriptor/stencilattachment.md) properties of the [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) instance that creates it.

Pass `nil` to clear the state from the previous call, which restores a state that’s equivalent to the default values of an [MTLDepthStencilDescriptor](../mtldepthstencildescriptor.md) instance’s properties.

## See Also

### Configuring depth and stencil behavior

- [- setDepthBias:slopeScale:clamp:](<setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [- setDepthClipMode:](<setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [setDepthTestBounds(_:)](<setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
- [- setStencilFrontReferenceValue:backReferenceValue:](<setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.
