---
title: 'setFragmentSamplerStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates%28_%3Arange%3A%29.json'
content_hash: 'sha256:eb592b007d88054f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentSamplerStates(_:range:)

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the fragment shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the fragment shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setFragmentSamplerStates:withRange:](setfragmentsamplerstates_withrange_.md).

## See Also

### Assigning sampler states

- [- setFragmentSamplerState:atIndex:](<setfragmentsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the fragment shader argument table.
- [- setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setfragmentsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [setFragmentSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setfragmentsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
