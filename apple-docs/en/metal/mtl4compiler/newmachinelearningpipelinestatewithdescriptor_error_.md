---
title: 'newMachineLearningPipelineStateWithDescriptor:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor%3Aerror%3A.json'
content_hash: 'sha256:6c2aa0763afae448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newMachineLearningPipelineStateWithDescriptor:error:

<sub>Instance Method</sub>

Creates a new ML pipeline state with descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTL4MachineLearningPipelineState>) newMachineLearningPipelineStateWithDescriptor:(MTL4MachineLearningPipelineDescriptor *) descriptor error:(NSError **) error;
```

## Parameters

- `descriptor` — A machine learning pipeline state descriptor to use for creating the new pipeline state.

- `error` — An optional parameter into which Metal stores information in case of an error.

## Return Value

A machine learning pipeline state if operation is successful, otherwise `nil`.
