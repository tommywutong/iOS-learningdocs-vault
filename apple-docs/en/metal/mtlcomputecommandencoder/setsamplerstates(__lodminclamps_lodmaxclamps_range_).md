---
title: 'setSamplerStates(_:lodMinClamps:lodMaxClamps:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setsamplerstates(_:lodminclamps:lodmaxclamps:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstates(_:lodminclamps:lodmaxclamps:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setsamplerstates%28_%3Alodminclamps%3Alodmaxclamps%3Arange%3A%29.json'
content_hash: 'sha256:4fb3d7b19f7088d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setSamplerStates(_:lodMinClamps:lodMaxClamps:range:)

<sub>Instance Method</sub>

Encodes multiple texture samplers for the compute function, specifying clamp values for the level of detail of each sampler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSamplerStates(_ samplers: [(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)
```

## Parameters

- `samplers` — A list of [MTLSamplerState](../mtlsamplerstate.md) instances to bind to the sampler argument table.

- `lodMinClamps` — An array of minimum levels of detail to use for the corresponding sampler in `samplers`.

- `lodMaxClamps` — An array of maximum levels of detail to use for the corresponding sample in `samplers`.

- `range` — A range of indices in the sampler state argument table.

## Discussion

> [!important] Important
> This method requires that the lengths of `samplers`, `lodMinClamps`, and `lodMaxClamps` be the same as the length of `range`.

Calling this method ignores the [lodMinClamp](../mtlsamplerdescriptor/lodminclamp.md) and [lodMaxClamp](../mtlsamplerdescriptor/lodmaxclamp.md) properties of the samplers, using the provided levels of detail instead.

## See Also

### Binding texture samplers

- [- setSamplerState:atIndex:](<setsamplerstate(__index_).md>) — Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [- setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [setSamplerStates(_:range:)](<setsamplerstates(__range_).md>) — Encodes multiple texture samplers to the sampler argument table, allowing compute kernels to use them for sampling textures on the GPU.
