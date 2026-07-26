---
title: blendingState
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/blendingstate
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/blendingstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/blendingstate.json'
content_hash: 'sha256:4b56c10815df9b8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineColorAttachmentDescriptor](../mtl4renderpipelinecolorattachmentdescriptor.md)

# blendingState

<sub>Instance Property</sub>

Configure the blend state for color attachments the pipeline state uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var blendingState: MTL4BlendState { get set }
```

## Discussion

This property’s default value is `MTL4BlendStateDisabled`.
