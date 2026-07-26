---
title: 'makeRenderPipelineState(additionalBinaryFunctions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-49r1w'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-49r1w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate%28additionalbinaryfunctions%3A%29-49r1w.json'
content_hash: 'sha256:83fd5583c81ede67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# makeRenderPipelineState(additionalBinaryFunctions:)

<sub>Instance Method</sub>

Creates a new render pipeline state by adding binary functions to each stage of this pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(additionalBinaryFunctions binaryFunctionsDescriptor: MTL4RenderPipelineBinaryFunctionsDescriptor) throws -> any MTLRenderPipelineState
```

## Parameters

- `binaryFunctionsDescriptor` — A non-`nil` dynamic linking descriptor.

## Return Value

A new render pipeline state upon success, otherwise `nil`.
