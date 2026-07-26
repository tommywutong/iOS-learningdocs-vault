---
title: 'makeComputePipelineStateWithAdditionalBinaryFunctions(functions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestatewithadditionalbinaryfunctions(functions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestatewithadditionalbinaryfunctions(functions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestatewithadditionalbinaryfunctions%28functions%3A%29.json'
content_hash: 'sha256:cfd1528a4b16b193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# makeComputePipelineStateWithAdditionalBinaryFunctions(functions:)

<sub>Instance Method</sub>

Creates a new pipeline state object with additional callable functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineStateWithAdditionalBinaryFunctions(functions: [any MTLFunction]) throws -> any MTLComputePipelineState
```

## Parameters

- `functions` — The list of additional functions that you want to be able to call.

## Return Value

A new compute pipeline state with access to the provided functions. When this value is `nil`, an error occurred during handle creation.
