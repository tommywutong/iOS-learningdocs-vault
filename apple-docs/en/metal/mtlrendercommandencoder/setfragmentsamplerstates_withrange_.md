---
title: 'setFragmentSamplerStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstates%3Awithrange%3A.json'
content_hash: 'sha256:e04c0b8d103777ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentSamplerStates:withRange:

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setFragmentSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Parameters

- `samplers` — A pointer to a C array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the fragment shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the fragment shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setFragmentSamplerStates(_:range:)](<setfragmentsamplerstates(__range_).md>).

## See Also

### Assigning sampler states

- [- setFragmentSamplerState:atIndex:](<setfragmentsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the fragment shader argument table.
- [- setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setfragmentsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:](setfragmentsamplerstates_lodminclamps_lodmaxclamps_withrange_.md) — Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
