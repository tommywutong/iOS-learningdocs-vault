---
title: 'setTileSamplerState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilesamplerstate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilesamplerstate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:78c7c64cb57dd8c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileSamplerState(_:index:)

<sub>Instance Method</sub>

Assigns a sampler state to an entry in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler` — An [MTLSamplerState](../mtlsamplerstate.md) instance the command assigns to an entry in the tile shader argument table for sampler states.

- `index` — An integer that represents the entry in the tile shader argument table for sampler states that stores a record of `sampler`.

## Discussion

By default, the sampler state at each index is `nil`.

## See Also

### Assigning sampler states

- [- setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<settilesamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [setTileSamplerStates(_:range:)](<settilesamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the tile shader argument table.
- [setTileSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<settilesamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.
