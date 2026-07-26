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
doc_path: /documentation/metal/mtlrenderpassdescriptor/colorattachments
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/colorattachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/colorattachments.json'
content_hash: 'sha256:371bd336e384cb57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# colorAttachments

<sub>Instance Property</sub>

An array of state information for attachments that store color data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray { get }
```

## See Also

### Specifying the attachments for a rendering pass

- [depthAttachment](depthattachment.md) — State information for an attachment that stores depth data.
- [stencilAttachment](stencilattachment.md) — State information for an attachment that stores stencil data.
