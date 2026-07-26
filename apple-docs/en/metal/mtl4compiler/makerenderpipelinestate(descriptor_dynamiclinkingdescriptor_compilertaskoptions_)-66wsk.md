---
title: 'makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-66wsk'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-66wsk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makerenderpipelinestate%28descriptor%3Adynamiclinkingdescriptor%3Acompilertaskoptions%3A%29-66wsk.json'
content_hash: 'sha256:e985a598e7e6f717'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

<sub>Instance Method</sub>

Creates a new render pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) async throws -> any MTLRenderPipelineState
```

## Parameters

- `descriptor` — A render, tile, or mesh pipeline state descriptor that describes the pipeline to create.

- `dynamicLinkingDescriptor` — An optional parameter that provides additional configuration for linking the pipeline state object.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

## Return Value

A render pipeline state if operation upon success, otherwise this function throws.

## Discussion

Use this method to build any render pipeline type, including render, tile, and mesh render pipeline states. The type of the descriptor you pass indicates the pipeline type this method builds.

Passing in a compute pipeline descriptor to the `descriptor` parameter produces an error.
