---
title: 'setObjectSamplerState(_:lodMinClamp:lodMaxClamp:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setobjectsamplerstate(_:lodminclamp:lodmaxclamp:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectsamplerstate(_:lodminclamp:lodmaxclamp:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setobjectsamplerstate%28_%3Alodminclamp%3Alodmaxclamp%3Aindex%3A%29.json'
content_hash: 'sha256:8ab56f47df3bf4e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setObjectSamplerState(_:lodMinClamp:lodMaxClamp:index:)

<sub>Instance Method</sub>

Assigns a sampler state and clamp values to an entry in the object shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setObjectSamplerState(_ sampler: (any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)
```

## Parameters

- `sampler` — An [MTLSamplerState](../mtlsamplerstate.md) instance the command assigns to an entry in the object shader argument table for sampler states.

- `lodMinClamp` — The smallest level of detail value an object shader can use when it samples a texture.

- `lodMaxClamp` — The largest level of detail value an object shader can use when it samples a texture.

- `index` — An integer that represents the entry in the object argument table for sampler states that stores a record of `sampler`.

## Discussion

The method’s `lodMinClamp` and `lodMaxClamp` parameters override the default values for `sampler`. You can set the sampler’s default values by configuring the [lodMinClamp](../mtlsamplerdescriptor/lodminclamp.md) and [lodMaxClamp](../mtlsamplerdescriptor/lodmaxclamp.md) properties of [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

## See Also

### Assigning sampler states for object shaders

- [- setObjectSamplerState:atIndex:](<setobjectsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the object shader argument table.
- [setObjectSamplerStates(_:range:)](<setobjectsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the object shader argument table.
- [setObjectSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setobjectsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.
