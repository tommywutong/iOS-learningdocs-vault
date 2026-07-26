---
title: 'newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor%3Adynamiclinkingdescriptor%3Acompilertaskoptions%3Aerror%3A.json'
content_hash: 'sha256:1aa68ce02db682f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:

<sub>Instance Method</sub>

Creates a new render pipeline state synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithDescriptor:(MTL4PipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4RenderPipelineDynamicLinkingDescriptor *) dynamicLinkingDescriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions error:(NSError **) error;
```

## Parameters

- `descriptor` — A render, tile, or mesh pipeline state descriptor that describes the pipeline to create.

- `dynamicLinkingDescriptor` — An optional parameter that provides additional configuration for linking the pipeline state object.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

- `error` — An optional parameter into which Metal stores information in case of an error.

## Return Value

A new render pipeline state object upon success, `nil` otherwise.

## Discussion

Use this method to build any render pipeline type, including render, tile, and mesh render pipeline states. The type of the descriptor you pass indicates the pipeline type this method builds.

Passing in a compute pipeline descriptor to the `descriptor` parameter produces an error.
