---
title: writeMask
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/writemask
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/writemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/writemask.json'
content_hash: 'sha256:f301e74041e5dde1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineColorAttachmentDescriptor](../mtl4renderpipelinecolorattachmentdescriptor.md)

# writeMask

<sub>Instance Property</sub>

Configures the color write mask.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var writeMask: MTLColorWriteMask { get set }
```

## Discussion

This property defaults to `MTLColorWriteMaskAll`.
