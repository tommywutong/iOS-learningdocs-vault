---
title: 'makeMachineLearningPipelineState(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makemachinelearningpipelinestate(descriptor:)-36hxx'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makemachinelearningpipelinestate(descriptor:)-36hxx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makemachinelearningpipelinestate%28descriptor%3A%29-36hxx.json'
content_hash: 'sha256:1929a5f690599977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeMachineLearningPipelineState(descriptor:)

<sub>Instance Method</sub>

Creates a new machine learning pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeMachineLearningPipelineState(descriptor: MTL4MachineLearningPipelineDescriptor) async throws -> any MTL4MachineLearningPipelineState
```

## Parameters

- `descriptor` — A machine learning pipeline state descriptor to use for creating the new pipeline state.

## Return Value

A machine learning pipeline state upon success, otherwise this function throws.
