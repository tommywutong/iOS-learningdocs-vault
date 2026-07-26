---
title: 'setTileSamplerStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilesamplerstates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilesamplerstates%28_%3Arange%3A%29.json'
content_hash: 'sha256:9f8c5c07d0071ed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileSamplerStates(_:range:)

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the tile shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the tile shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setTileSamplerStates:withRange:](settilesamplerstates_withrange_.md).

## See Also

### Assigning sampler states

- [- setTileSamplerState:atIndex:](<settilesamplerstate(__index_).md>) — Assigns a sampler state to an entry in the tile shader argument table.
- [- setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<settilesamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [setTileSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<settilesamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.
