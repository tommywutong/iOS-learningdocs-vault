---
title: stencilAttachmentPixelFormat
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/stencilattachmentpixelformat
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/stencilattachmentpixelformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/stencilattachmentpixelformat.json'
content_hash: 'sha256:9163839607ed2fc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# stencilAttachmentPixelFormat

<sub>Instance Property</sub>

The pixel format of the attachment that stores stencil data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stencilAttachmentPixelFormat: MTLPixelFormat { get set }
```

## Discussion

By default, the pixel format of the rendering pipeline state for each attachment is `MTLPixelFormatInvalid`.

## See Also

### Specifying rendering pipeline state

- [- reset](<reset().md>) — Specifies the default rendering pipeline state values for the descriptor.
- [colorAttachments](colorattachments.md) — An array of attachments that store color data.
- [depthAttachmentPixelFormat](depthattachmentpixelformat.md) — The pixel format of the attachment that stores depth data.
