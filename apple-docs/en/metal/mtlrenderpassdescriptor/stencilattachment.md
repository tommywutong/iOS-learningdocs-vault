---
title: stencilAttachment
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/stencilattachment
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/stencilattachment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/stencilattachment.json'
content_hash: 'sha256:a3e1d5e1d91f3645'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# stencilAttachment

<sub>Instance Property</sub>

State information for an attachment that stores stencil data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor! { get set }
```

## See Also

### Specifying the attachments for a rendering pass

- [colorAttachments](colorattachments.md) — An array of state information for attachments that store color data.
- [depthAttachment](depthattachment.md) — State information for an attachment that stores depth data.
