---
title: 'setTileSamplerStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settilesamplerstates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilesamplerstates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settilesamplerstates%3Awithrange%3A.json'
content_hash: 'sha256:5ec8af7d6f5d6b19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileSamplerStates:withRange:

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setTileSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Parameters

- `samplers` — A pointer to a C array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the tile shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the tile shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setTileSamplerStates(_:range:)](<settilesamplerstates(__range_).md>).

## See Also

### Assigning sampler states

- [- setTileSamplerState:atIndex:](<settilesamplerstate(__index_).md>) — Assigns a sampler state to an entry in the tile shader argument table.
- [- setTileSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<settilesamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [setTileSamplerStates:lodMinClamps:lodMaxClamps:withRange:](settilesamplerstates_lodminclamps_lodmaxclamps_withrange_.md) — Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.
