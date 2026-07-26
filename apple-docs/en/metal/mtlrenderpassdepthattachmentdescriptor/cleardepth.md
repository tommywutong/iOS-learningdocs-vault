---
title: clearDepth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdepthattachmentdescriptor/cleardepth
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/cleardepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdepthattachmentdescriptor/cleardepth.json'
content_hash: 'sha256:c0b880e24760da6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDepthAttachmentDescriptor](../mtlrenderpassdepthattachmentdescriptor.md)

# clearDepth

<sub>Instance Property</sub>

The depth to use when clearing the depth attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var clearDepth: Double { get set }
```

## Discussion

If the [loadAction](../mtlrenderpassattachmentdescriptor/loadaction.md) property of the attachment is set to [MTLLoadActionClear](../mtlloadaction/clear.md), then at the start of a render pass, the GPU fills the contents of the attachment with the value stored in the [clearDepth](cleardepth.md) property. Otherwise, the GPU ignores [clearDepth](cleardepth.md).

The default value is `1.0`.
