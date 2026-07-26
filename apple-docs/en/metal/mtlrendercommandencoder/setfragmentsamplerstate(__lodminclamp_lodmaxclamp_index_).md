---
title: 'setFragmentSamplerState(_:lodMinClamp:lodMaxClamp:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate(_:lodminclamp:lodmaxclamp:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate(_:lodminclamp:lodmaxclamp:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentsamplerstate%28_%3Alodminclamp%3Alodmaxclamp%3Aindex%3A%29.json'
content_hash: 'sha256:fe7538473b84b935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentSamplerState(_:lodMinClamp:lodMaxClamp:index:)

<sub>Instance Method</sub>

Assigns a sampler state and clamp values to an entry in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentSamplerState(_ sampler: (any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)
```

## Parameters

- `sampler` — An [MTLSamplerState](../mtlsamplerstate.md) instance the command assigns to an entry in the fragment shader argument table for sampler states.

- `lodMinClamp` — The smallest level of detail value a fragment shader can use when it samples a texture.

- `lodMaxClamp` — The largest level of detail value a fragment shader can use when it samples a texture.

- `index` — An integer that represents the entry in the fragment shader argument table for sampler states that stores a record of `sampler`.

## Discussion

The method’s `lodMinClamp` and `lodMaxClamp` parameters override the default values for `sampler`. You can set the sampler’s default values by configuring the [lodMinClamp](../mtlsamplerdescriptor/lodminclamp.md) and [lodMaxClamp](../mtlsamplerdescriptor/lodmaxclamp.md) properties of [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

## See Also

### Assigning sampler states

- [- setFragmentSamplerState:atIndex:](<setfragmentsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the fragment shader argument table.
- [setFragmentSamplerStates(_:range:)](<setfragmentsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [setFragmentSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setfragmentsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
