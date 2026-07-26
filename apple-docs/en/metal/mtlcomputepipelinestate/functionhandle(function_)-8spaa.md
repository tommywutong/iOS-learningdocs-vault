---
title: 'functionHandle(function:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/functionhandle(function:)-8spaa'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/functionhandle(function:)-8spaa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/functionhandle%28function%3A%29-8spaa.json'
content_hash: 'sha256:a0c6603334a437a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# functionHandle(function:)

<sub>Instance Method</sub>

Gets the function handle for a function this pipeline links at the binary level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(function: any MTL4BinaryFunction) -> (any MTLFunctionHandle)?
```

## Parameters

- `function` — A binary function object representing the function binary to find.

## Return Value

A function handle corresponding to the function if the binary function matches a function in this pipeline state, otherwise `nil`.
