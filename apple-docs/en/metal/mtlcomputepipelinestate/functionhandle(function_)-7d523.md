---
title: 'functionHandle(function:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/functionhandle(function:)-7d523'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/functionhandle(function:)-7d523'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/functionhandle%28function%3A%29-7d523.json'
content_hash: 'sha256:0ca9ec0507a06e2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# functionHandle(function:)

<sub>Instance Method</sub>

Creates a function handle for a visible function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(function: any MTLFunction) -> (any MTLFunctionHandle)?
```

## Parameters

- `function` — An [MTLFunction](../mtlfunction.md) instance that represents the visible function to create a handle for.

## Return Value

A handle to the visible function. When this value is `nil`, an error occurred during handle creation.
