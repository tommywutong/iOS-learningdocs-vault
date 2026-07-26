---
title: objectStaticLinkingDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/objectstaticlinkingdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/objectstaticlinkingdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/objectstaticlinkingdescriptor.json'
content_hash: 'sha256:c0d87c3fed59687d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# objectStaticLinkingDescriptor

<sub>Instance Property</sub>

Provides static linking information for the object stage of the render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var objectStaticLinkingDescriptor: MTL4StaticLinkingDescriptor! { get set }
```

## Discussion

Use this property to link extra shader functions to the object stage of the render pipeline.
