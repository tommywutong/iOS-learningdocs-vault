---
title: 'makeComputePipelineState(additionalBinaryFunctions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestate(additionalbinaryfunctions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestate(additionalbinaryfunctions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestate%28additionalbinaryfunctions%3A%29.json'
content_hash: 'sha256:3ba0f282fa13b3cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# makeComputePipelineState(additionalBinaryFunctions:)

<sub>Instance Method</sub>

Allocates a new compute pipeline state by adding binary functions to this pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(additionalBinaryFunctions: [any MTL4BinaryFunction]) throws -> any MTLComputePipelineState
```

## Parameters

- `additionalBinaryFunctions` — A non-`nil` array containing binary functions to add to this pipeline.

## Return Value

A new compute pipeline state upon success, otherwise `nil`.
