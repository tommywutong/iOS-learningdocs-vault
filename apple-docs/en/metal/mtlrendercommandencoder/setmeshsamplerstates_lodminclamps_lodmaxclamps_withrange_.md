---
title: 'setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates:lodminclamps:lodmaxclamps:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates:lodminclamps:lodmaxclamps:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates%3Alodminclamps%3Alodmaxclamps%3Awithrange%3A.json'
content_hash: 'sha256:292032503c23b638'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:

<sub>Instance Method</sub>

Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setMeshSamplerStates:(id<MTLSamplerState> const[]) samplers lodMinClamps:(const float[]) lodMinClamps lodMaxClamps:(const float[]) lodMaxClamps withRange:(NSRange) range;
```

## Parameters

- `samplers` — A pointer to a C array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the mesh shader argument table for sampler states.

- `lodMinClamps` — A pointer to a C array of floating-point values. Each element is the smallest level of detail value a mesh shader can use when it samples a texture with the corresponding element in `samplers`.

- `lodMaxClamps` — A pointer to a C array of floating-point values. Each element is the largest level of detail value a mesh shader can use when it samples a texture with the corresponding element in `samplers`.

- `range` — A span of integers that represent the entries in the mesh shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

Each element of the method’s `lodMinClamps` and `lodMaxClamps` parameters overrides the default values for the corresponding sampler in `samplers`. You can set a sampler’s default values by configuring the [lodMinClamp](../mtlsamplerdescriptor/lodminclamp.md) and [lodMaxClamp](../mtlsamplerdescriptor/lodmaxclamp.md) properties of [MTLSamplerDescriptor](../mtlsamplerdescriptor.md) before you create the sampler.

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setMeshSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setmeshsamplerstates(__lodminclamps_lodmaxclamps_range_).md>).

## See Also

### Assigning sampler states for mesh shaders

- [- setMeshSamplerState:atIndex:](<setmeshsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the mesh shader argument table.
- [- setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setmeshsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [setMeshSamplerStates:withRange:](setmeshsamplerstates_withrange_.md) — Assigns multiple sampler states to a range of entries in the mesh shader argument table.
