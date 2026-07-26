---
title: fragmentFunctionDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpipelinedescriptor/fragmentfunctiondescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/fragmentfunctiondescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinedescriptor/fragmentfunctiondescriptor.json'
content_hash: 'sha256:ff5528dbec6f13c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineDescriptor](../mtl4renderpipelinedescriptor.md)

# fragmentFunctionDescriptor

<sub>Instance Property</sub>

Assigns the shader function that this pipeline executes for each fragment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var fragmentFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

## Discussion

When you don’t specify a fragment function, you need to disable rasterization by setting property [rasterizationEnabled](israsterizationenabled.md) to false.
