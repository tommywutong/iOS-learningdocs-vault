---
title: texture
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/texture
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/texture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/texture.json'
content_hash: 'sha256:057cc88941cf90c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# texture

<sub>Instance Property</sub>

The texture object associated with this attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var texture: (any MTLTexture)? { get set }
```

## Discussion

You need to set the attachment’s `texture` property, choosing an appropriate pixel format for the texture.

- To store color values in an attachment, use a texture with a color-renderable pixel format.
- To store depth values, use a texture with a depth-renderable pixel format, such as [MTLPixelFormatDepth32Float](../mtlpixelformat/depth32float.md).
- To store stencil values, use a texture with a stencil-renderable pixel format, such as [MTLPixelFormatStencil8](../mtlpixelformat/stencil8.md).

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Specifying the texture for the attachment

- [level](level.md) — The mipmap level of the texture used for rendering to the attachment.
- [slice](slice.md) — The slice of the texture used for rendering to the attachment.
- [depthPlane](depthplane.md) — The depth plane of the texture used for rendering to the attachment.
