---
title: 'makeComputePipelineState(descriptor:dynamicLinkingDescriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4archive/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive/makecomputepipelinestate%28descriptor%3Adynamiclinkingdescriptor%3A%29.json'
content_hash: 'sha256:201dfc621adf7e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Archive](../mtl4archive.md)

# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:)

<sub>Instance Method</sub>

Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil) throws -> any MTLComputePipelineState
```

## Parameters

- `descriptor` — A compute pipeline descriptor.

- `dynamicLinkingDescriptor` — A descriptor that provides additional properties to link other functions with the pipeline.

## Return Value

A compute pipeline state object upon success, otherwise this function throws.
