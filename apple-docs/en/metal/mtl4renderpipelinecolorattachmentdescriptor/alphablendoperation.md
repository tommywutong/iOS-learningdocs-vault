---
title: alphaBlendOperation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/alphablendoperation
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/alphablendoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/alphablendoperation.json'
content_hash: 'sha256:c364c15750d91fb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineColorAttachmentDescriptor](../mtl4renderpipelinecolorattachmentdescriptor.md)

# alphaBlendOperation

<sub>Instance Property</sub>

Configures the alpha blending operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var alphaBlendOperation: MTLBlendOperation { get set }
```

## Discussion

This property defaults to `MTLBlendOperationAdd`.
