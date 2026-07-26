---
title: 'setSamplerState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setsamplerstate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setsamplerstate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:bbd994da8367b374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setSamplerState(_:index:)

<sub>Instance Method</sub>

Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler` — An [MTLSamplerState](../mtlsamplerstate.md) instance to bind to the sampler argument table.

- `index` — The index in the sampler argument table to bind the sampler to.

## See Also

### Binding texture samplers

- [- setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [setSamplerStates(_:range:)](<setsamplerstates(__range_).md>) — Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.
- [setSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.
