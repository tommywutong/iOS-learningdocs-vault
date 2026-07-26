---
title: 'newMachineLearningPipelineStateWithDescriptor:completionHandler:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor:completionhandler:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor%3Acompletionhandler%3A.json'
content_hash: 'sha256:709ced5164d4fc7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newMachineLearningPipelineStateWithDescriptor:completionHandler:

<sub>Instance Method</sub>

Creates a new machine learning pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4CompilerTask>) newMachineLearningPipelineStateWithDescriptor:(MTL4MachineLearningPipelineDescriptor *) descriptor completionHandler:(MTL4NewMachineLearningPipelineStateCompletionHandler) completionHandler;
```

## Parameters

- `descriptor` — A machine learning pipeline state descriptor to use for creating the new pipeline state.

- `completionHandler` — A block Metal calls when it finishes the build task.

## Return Value

A compiler task representing the asynchronous compilation task.
