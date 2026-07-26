---
title: 'makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4archive/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive/makerenderpipelinestate%28descriptor%3Adynamiclinkingdescriptor%3A%29.json'
content_hash: 'sha256:9e14217230f1348a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Archive](../mtl4archive.md)

# makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:)

<sub>Instance Method</sub>

Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor? = nil) throws -> any MTLRenderPipelineState
```

## Parameters

- `descriptor` — A render pipeline descriptor.

- `dynamicLinkingDescriptor` — A descriptor that provides additional properties to link other functions with the pipeline.

## Return Value

A compute pipeline state object upon success, otherwise this function throws.

## Discussion

You create any kind of render pipeline states with this method, including:

- Traditional render pipelines
- Mesh render pipelines
- Tile render pipelines
