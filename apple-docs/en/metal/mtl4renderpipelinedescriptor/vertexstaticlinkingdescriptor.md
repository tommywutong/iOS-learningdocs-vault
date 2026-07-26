---
title: vertexStaticLinkingDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedescriptor/vertexstaticlinkingdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/vertexstaticlinkingdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedescriptor/vertexstaticlinkingdescriptor.json'
content_hash: 'sha256:5889c8380f7d6df3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineDescriptor](../mtl4renderpipelinedescriptor.md)

# vertexStaticLinkingDescriptor

<sub>Instance Property</sub>

Provides static linking information for the vertex stage of the render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var vertexStaticLinkingDescriptor: MTL4StaticLinkingDescriptor! { get set }
```

## Discussion

Use this property to link extra shader functions to the vertex stage of the render pipeline.
