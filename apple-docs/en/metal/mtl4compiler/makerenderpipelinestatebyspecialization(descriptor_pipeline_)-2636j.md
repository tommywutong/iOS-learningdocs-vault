---
title: 'makeRenderPipelineStateBySpecialization(descriptor:pipeline:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makerenderpipelinestatebyspecialization(descriptor:pipeline:)-2636j'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makerenderpipelinestatebyspecialization(descriptor:pipeline:)-2636j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makerenderpipelinestatebyspecialization%28descriptor%3Apipeline%3A%29-2636j.json'
content_hash: 'sha256:64b4037bf17739e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeRenderPipelineStateBySpecialization(descriptor:pipeline:)

<sub>Instance Method</sub>

Creates a new render pipeline state from another, previously unspecialized, pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRenderPipelineStateBySpecialization(descriptor: MTL4PipelineDescriptor, pipeline: any MTLRenderPipelineState) throws -> any MTLRenderPipelineState
```

## Parameters

- `descriptor` — A render pipeline state descriptor or any type: default, tile, or mesh render pipeline descriptor.

- `pipeline` — A render pipeline state containing unspecialized substate.

## Return Value

A fully-specialized pipeline state object upon success, otherwise this function throws.

## Discussion

Metal specializes the pipeline state with new state values the descriptor provides, observing the following rules:

- The compiler only updates properties that were originally specified as _unspecialized_. It doesn’t modify other already-specialized properties
- The compiler sets to their default behavior any unspecialized properties that your passed-in descriptor doesn’t specialize

Additionally, there are some cases where the Metal can’t specialize a pipeline:

- If the original pipeline state object doesn’t have any unspecialized properties
- You can’t re-specialize a previously specialized pipeline state object
