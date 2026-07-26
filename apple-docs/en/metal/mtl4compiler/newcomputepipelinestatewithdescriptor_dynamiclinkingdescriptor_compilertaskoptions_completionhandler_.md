---
title: 'newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor%3Adynamiclinkingdescriptor%3Acompilertaskoptions%3Acompletionhandler%3A.json'
content_hash: 'sha256:cc9a0da2d97dde68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:

<sub>Instance Method</sub>

Creates a new compute pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4PipelineStageDynamicLinkingDescriptor *) dynamicLinkingDescriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTLNewComputePipelineStateCompletionHandler) completionHandler;
```

## Parameters

- `descriptor` — A compute pipeline state descriptor, describing the compute pipeline to create.

- `dynamicLinkingDescriptor` — An optional parameter that provides additional configuration for linking the pipeline state object.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

- `completionHandler` — A block Metal calls when it finishes the build task.

## Return Value

A compiler task representing the asynchronous compilation task.
