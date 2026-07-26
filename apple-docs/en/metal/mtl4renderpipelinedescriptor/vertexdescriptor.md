---
title: vertexDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedescriptor/vertexdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/vertexdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedescriptor/vertexdescriptor.json'
content_hash: 'sha256:99cbb002e41b2d58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineDescriptor](../mtl4renderpipelinedescriptor.md)

# vertexDescriptor

<sub>Instance Property</sub>

Configures an optional vertex descriptor for the vertex input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var vertexDescriptor: MTLVertexDescriptor? { get set }
```

## Discussion

A vertex descriptor specifies the layout of your vertex data, allowing your vertex shaders to access the content in your vertex arrays via the `[[stage_in]]` attribute in Metal Shading Language.
