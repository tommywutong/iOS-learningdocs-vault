---
title: 'functionHandle(withName:stage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/functionhandle(withname:stage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(withname:stage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/functionhandle%28withname%3Astage%3A%29.json'
content_hash: 'sha256:c4a09cb1041d4218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# functionHandle(withName:stage:)

<sub>Instance Method</sub>

Obtains a function handle for the a specific function this pipeline links at the Metal IR level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(withName name: String, stage: MTLRenderStages) -> (any MTLFunctionHandle)?
```

## Parameters

- `name` — A string containing the name of the function.

- `stage` — The shader stage that uses the function.

## Return Value

A function handle representing the function if present, otherwise `nil`.
