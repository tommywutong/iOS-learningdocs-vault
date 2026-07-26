---
title: 'setSamplerStates:lodMinClamps:lodMaxClamps:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setsamplerstates:lodminclamps:lodmaxclamps:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstates:lodminclamps:lodmaxclamps:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setsamplerstates%3Alodminclamps%3Alodmaxclamps%3Awithrange%3A.json'
content_hash: 'sha256:18a6a580c869148b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setSamplerStates:lodMinClamps:lodMaxClamps:withRange:

<sub>Instance Method</sub>

Encodes multiple texture samplers with custom levels of detail clamping, allowing compute kernels to use them for sampling textures on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setSamplerStates:(id<MTLSamplerState> const[]) samplers lodMinClamps:(const float[]) lodMinClamps lodMaxClamps:(const float[]) lodMaxClamps withRange:(NSRange) range;
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances to bind to the sampler argument table.

- `lodMinClamps` — An array of minimum levels of detail to use for the corresponding sampler in the `samplers` array.

- `lodMaxClamps` — An array of maximum levels of detail to use for the corresponding sampler in the `samplers` array.

- `range` — The sampler table indicies to bind each of the `samplers` to, in the order they appear.

## Discussion

> [!important] Important
> This method requires that the lengths of `samplers`, `lodMinClamps`, and `lodMaxClamps` be the same as the length of `range`.

Calling this method ignores the [lodMinClamp](../mtlsamplerdescriptor/lodminclamp.md) and [lodMaxClamp](../mtlsamplerdescriptor/lodmaxclamp.md) properties of the samplers, using the provided levels of detail instead.

## See Also

### Binding texture samplers

- [- setSamplerState:atIndex:](<setsamplerstate(__index_).md>) — Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [- setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [setSamplerStates:withRange:](setsamplerstates_withrange_.md) — Encodes multiple texture samplers, allowing compute kernels to use them for sampling textures on the GPU.
