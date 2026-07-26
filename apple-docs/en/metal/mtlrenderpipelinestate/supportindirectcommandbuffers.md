---
title: supportIndirectCommandBuffers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/supportindirectcommandbuffers
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/supportindirectcommandbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/supportindirectcommandbuffers.json'
content_hash: 'sha256:59b0971ea4047120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# supportIndirectCommandBuffers

<sub>Instance Property</sub>

A Boolean value that indicates whether the render pipeline supports encoding commands into an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportIndirectCommandBuffers: Bool { get }
```

## Discussion

This property gets its value by copying from the [supportIndirectCommandBuffers](../mtlrenderpipelinedescriptor/supportindirectcommandbuffers.md) property of the [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md) instance as the GPU device creates the pipeline state.
