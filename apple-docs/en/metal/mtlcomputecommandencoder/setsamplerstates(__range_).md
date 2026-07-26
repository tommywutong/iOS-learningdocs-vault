---
title: 'setSamplerStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setsamplerstates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setsamplerstates%28_%3Arange%3A%29.json'
content_hash: 'sha256:7dfeeb4ae6f23689'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setSamplerStates(_:range:)

<sub>Instance Method</sub>

Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instance to bind to the sampler argument table.

- `range` — The sampler table indicies to bind each of the `samplers` to, in the order they appear.

## Discussion

> [!warning] Warning
> This method requires that the number of instances in `samplers` be the same as the length of `range`.

## See Also

### Binding texture samplers

- [- setSamplerState:atIndex:](<setsamplerstate(__index_).md>) — Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [- setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [setSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.
