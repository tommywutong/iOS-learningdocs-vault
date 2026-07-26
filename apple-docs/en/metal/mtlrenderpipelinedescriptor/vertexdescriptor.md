---
title: vertexDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/vertexdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/vertexdescriptor.json'
content_hash: 'sha256:e48c352229b93e2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# vertexDescriptor

<sub>Instance Property</sub>

The organization of vertex data in an attribute’s argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var vertexDescriptor: MTLVertexDescriptor? { get set }
```

## Discussion

An [MTLVertexDescriptor](../mtlvertexdescriptor.md) instance is used to describe the organization of per-vertex input structs passed in an argument of a vertex shader function.
