---
title: depthAttachment
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/depthattachment
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/depthattachment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/depthattachment.json'
content_hash: 'sha256:815e285b106dfa16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# depthAttachment

<sub>Instance Property</sub>

State information for an attachment that stores depth data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var depthAttachment: MTLRenderPassDepthAttachmentDescriptor! { get set }
```

## See Also

### Specifying the attachments for a rendering pass

- [colorAttachments](colorattachments.md) — An array of state information for attachments that store color data.
- [stencilAttachment](stencilattachment.md) — State information for an attachment that stores stencil data.
