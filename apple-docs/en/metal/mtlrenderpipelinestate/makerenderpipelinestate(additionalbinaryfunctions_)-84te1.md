---
title: 'makeRenderPipelineState(additionalBinaryFunctions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-84te1'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-84te1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate%28additionalbinaryfunctions%3A%29-84te1.json'
content_hash: 'sha256:59a7731668e031a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# makeRenderPipelineState(additionalBinaryFunctions:)

<sub>Instance Method</sub>

Creates a new pipeline state that’s a copy of the current pipeline state with additional shaders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(additionalBinaryFunctions: MTLRenderPipelineFunctionsDescriptor) throws -> any MTLRenderPipelineState
```

## Parameters

- `additionalBinaryFunctions` — An [MTLRenderPipelineFunctionsDescriptor](../mtlrenderpipelinefunctionsdescriptor.md) instance, which contains [MTLFunction](../mtlfunction.md) arrays for vertex, fragment, and tile shaders.
