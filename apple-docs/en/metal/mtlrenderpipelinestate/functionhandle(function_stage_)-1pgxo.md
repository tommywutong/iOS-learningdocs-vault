---
title: 'functionHandle(function:stage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:)-1pgxo'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:)-1pgxo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/functionhandle%28function%3Astage%3A%29-1pgxo.json'
content_hash: 'sha256:782a4da9dbad631f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# functionHandle(function:stage:)

<sub>Instance Method</sub>

Obtains the function handle for a specific function this pipeline state links at the binary level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(function: any MTL4BinaryFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?
```

## Parameters

- `function` — A binary function to retrieve the handle.

- `stage` — The shader stage that uses the function.

## Return Value

A function handle representing the function if present, otherwise `nil`.
