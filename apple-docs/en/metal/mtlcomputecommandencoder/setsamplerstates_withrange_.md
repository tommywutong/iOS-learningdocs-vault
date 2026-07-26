---
title: 'setSamplerStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setsamplerstates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setsamplerstates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setsamplerstates%3Awithrange%3A.json'
content_hash: 'sha256:7ed9098aa2d5bd5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setSamplerStates:withRange:

<sub>Instance Method</sub>

Encodes multiple texture samplers, allowing compute kernels to use them for sampling textures on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances to bind to the sampler argument table.

- `range` — The sampler table indexes to bind each of the `samplers` to, in the order they appear.

## Discussion

> [!warning] Warning
> This method requires that the number of instances in `samplers` be the same as the length of `range`.

## See Also

### Binding texture samplers

- [- setSamplerState:atIndex:](<setsamplerstate(__index_).md>) — Encodes a texture sampler, allowing compute kernels to use it for sampling textures on the GPU.
- [- setSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Encodes a texture sampler with a custom level of detail clamping, allowing compute kernels to use it for sampling textures on the GPU.
- [setSamplerStates:lodMinClamps:lodMaxClamps:withRange:](setsamplerstates_lodminclamps_lodmaxclamps_withrange_.md) — Encodes multiple texture samplers with custom levels of detail clamping, allowing compute kernels to use them for sampling textures on the GPU.
