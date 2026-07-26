---
title: colorAttachments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/colorattachments
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/colorattachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/colorattachments.json'
content_hash: 'sha256:449b44ee144bca61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# colorAttachments

<sub>Instance Property</sub>

An array of attachments that store color data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorAttachments: MTLRenderPipelineColorAttachmentDescriptorArray { get }
```

## See Also

### Specifying rendering pipeline state

- [- reset](<reset().md>) — Specifies the default rendering pipeline state values for the descriptor.
- [depthAttachmentPixelFormat](depthattachmentpixelformat.md) — The pixel format of the attachment that stores depth data.
- [stencilAttachmentPixelFormat](stencilattachmentpixelformat.md) — The pixel format of the attachment that stores stencil data.
