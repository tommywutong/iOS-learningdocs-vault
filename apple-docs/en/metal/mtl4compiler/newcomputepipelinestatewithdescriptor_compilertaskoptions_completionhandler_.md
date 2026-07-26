---
title: 'newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:compilertaskoptions:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:compilertaskoptions:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor%3Acompilertaskoptions%3Acompletionhandler%3A.json'
content_hash: 'sha256:090342406867fae9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:

<sub>Instance Method</sub>

Creates a new compute pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTLNewComputePipelineStateCompletionHandler) completionHandler;
```

## Parameters

- `descriptor` — A compute pipeline state descriptor, describing the compute pipeline to create.

- `compilerTaskOptions` — A descriptor of the compilation itself, providing parameters that influence execution of the compilation process.

- `completionHandler` — A block Metal calls when it finishes the build task.

## Return Value

A compiler task representing the asynchronous compilation task.
