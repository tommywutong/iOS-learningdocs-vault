---
title: 'setVertexSamplerStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates%28_%3Arange%3A%29.json'
content_hash: 'sha256:e584a4b2f29b6dee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexSamplerStates(_:range:)

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the vertex shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the vertex shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setVertexSamplerStates:withRange:](setvertexsamplerstates_withrange_.md).

## See Also

### Assigning sampler states

- [- setVertexSamplerState:atIndex:](<setvertexsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the vertex shader argument table.
- [- setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setvertexsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [setVertexSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setvertexsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.
