---
title: 'setFragmentSamplerState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:889911b510bb95a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentSamplerState(_:index:)

<sub>Instance Method</sub>

Assigns a sampler state to an entry in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler` — An [MTLSamplerState](../mtlsamplerstate.md) instance the command assigns to an entry in the fragment shader argument table for sampler states.

- `index` — An integer that represents the entry in the fragment shader argument table for sampler states that stores a record of `sampler`.

## Discussion

By default, the sampler state at each index is `nil`.

## See Also

### Assigning sampler states

- [- setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setfragmentsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [setFragmentSamplerStates(_:range:)](<setfragmentsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [setFragmentSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setfragmentsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
