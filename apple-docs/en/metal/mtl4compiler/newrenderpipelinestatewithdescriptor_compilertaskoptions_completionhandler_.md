---
title: 'newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor:compilertaskoptions:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor:compilertaskoptions:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor%3Acompilertaskoptions%3Acompletionhandler%3A.json'
content_hash: 'sha256:cdd5a7b91d35970f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newRenderPipelineStateWithDescriptor:compilerTaskOptions:completionHandler:

<sub>Instance Method</sub>

Creates a new render pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newRenderPipelineStateWithDescriptor:(MTL4PipelineDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTLNewRenderPipelineStateCompletionHandler) completionHandler;
```

## Parameters

- `descriptor` — A render, tile, or mesh pipeline state descriptor that describes the pipeline to create.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

- `completionHandler` — A block Metal calls when it finishes the build task.

## Return Value

A compiler task representing the asynchronous compilation task.

## Discussion

Use this method to build any render pipeline type, including render, tile, and mesh render pipeline states. The type of the descriptor you pass indicates the pipeline type this method builds.

Passing in a compute pipeline descriptor to the `descriptor` parameter produces an error.
