---
title: 'setVertexSamplerStates(_:lodMinClamps:lodMaxClamps:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates(_:lodminclamps:lodmaxclamps:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates(_:lodminclamps:lodmaxclamps:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setvertexsamplerstates%28_%3Alodminclamps%3Alodmaxclamps%3Arange%3A%29.json'
content_hash: 'sha256:9af87a79f52cf98c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setVertexSamplerStates(_:lodMinClamps:lodMaxClamps:range:)

<sub>Instance Method</sub>

Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVertexSamplerStates(_ samplers: [(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the vertex shader argument table for sampler states.

- `lodMinClamps` — An array of floating-point values. Each element is the smallest level of detail value a vertex shader can use when it samples a texture with the corresponding element in `samplers`.

- `lodMaxClamps` — An array of floating-point values. Each element is the largest level of detail value a vertex shader can use when it samples a texture with the corresponding element in `samplers`.

- `range` — A span of integers that represent the entries in the vertex shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

Each element of the method’s `lodMinClamps` and `lodMaxClamps` parameters overrides the default values for the corresponding sampler in `samplers`. You can set a sampler’s default values by configuring the [lodMinClamp](../mtlsamplerdescriptor/lodminclamp.md) and [lodMaxClamp](../mtlsamplerdescriptor/lodmaxclamp.md) properties of [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:](setvertexsamplerstates_lodminclamps_lodmaxclamps_withrange_.md).

## See Also

### Assigning sampler states

- [- setVertexSamplerState:atIndex:](<setvertexsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the vertex shader argument table.
- [- setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setvertexsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [setVertexSamplerStates(_:range:)](<setvertexsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the vertex shader argument table.
