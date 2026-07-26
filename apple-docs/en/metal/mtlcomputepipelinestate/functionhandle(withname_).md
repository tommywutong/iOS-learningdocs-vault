---
title: 'functionHandle(withName:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/functionhandle(withname:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/functionhandle(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/functionhandle%28withname%3A%29.json'
content_hash: 'sha256:72c1faa34ab84408'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# functionHandle(withName:)

<sub>Instance Method</sub>

Gets the function handle for a function this pipeline links at the Metal IR level by name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(withName name: String) -> (any MTLFunctionHandle)?
```

## Parameters

- `name` — A string representing the name of the function.

## Return Value

A function handle corresponding to the function if the name matches a function in this pipeline state, otherwise `nil`.
