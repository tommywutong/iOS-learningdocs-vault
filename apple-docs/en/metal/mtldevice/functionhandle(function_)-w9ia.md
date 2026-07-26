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
doc_path: '/documentation/metal/mtldevice/functionhandle(function:)-w9ia'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/functionhandle(function:)-w9ia'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/functionhandle%28function%3A%29-w9ia.json'
content_hash: 'sha256:646a840e1d7d2995'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# functionHandle(function:)

<sub>Instance Method</sub>

Get the function handle for the specified binary-linked function from the pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(function: any MTL4BinaryFunction) -> (any MTLFunctionHandle)?
```

## Parameters

- `function` — A [MTL4BinaryFunction](../mtl4binaryfunction.md) instance representing the function binary.

## Return Value

A [MTLFunctionHandle](../mtlfunctionhandle.md) instance  for a binary function that was compiled with `MTLFunctionOptionPipelineIndependent`, otherwise `nil`.
