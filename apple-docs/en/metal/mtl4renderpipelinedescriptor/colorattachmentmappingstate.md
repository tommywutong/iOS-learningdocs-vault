---
title: colorAttachmentMappingState
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedescriptor/colorattachmentmappingstate
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/colorattachmentmappingstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedescriptor/colorattachmentmappingstate.json'
content_hash: 'sha256:50bdbdf210dca565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineDescriptor](../mtl4renderpipelinedescriptor.md)

# colorAttachmentMappingState

<sub>Instance Property</sub>

Configures a logical-to-physical rendering remap state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorAttachmentMappingState: MTL4LogicalToPhysicalColorAttachmentMappingState { get set }
```

## Discussion

Use this property to assign how a [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md) instance maps the output of your fragment shader to physical color attachments.
