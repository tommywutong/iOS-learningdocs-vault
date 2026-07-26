---
title: fragmentStaticLinkingDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4meshrenderpipelinedescriptor/fragmentstaticlinkingdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/fragmentstaticlinkingdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4meshrenderpipelinedescriptor/fragmentstaticlinkingdescriptor.json'
content_hash: 'sha256:bc836a0486b4efd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MeshRenderPipelineDescriptor](../mtl4meshrenderpipelinedescriptor.md)

# fragmentStaticLinkingDescriptor

<sub>Instance Property</sub>

Provides static linking information for the fragment stage of the render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var fragmentStaticLinkingDescriptor: MTL4StaticLinkingDescriptor! { get set }
```

## Discussion

Use this property to link extra shader functions to the fragment stage of the render pipeline.
