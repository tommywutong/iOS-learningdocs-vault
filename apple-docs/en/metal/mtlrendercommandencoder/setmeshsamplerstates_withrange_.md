---
title: 'setMeshSamplerStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshsamplerstates%3Awithrange%3A.json'
content_hash: 'sha256:9b1b65e3e0a42b8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshSamplerStates:withRange:

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setMeshSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Parameters

- `samplers` — A pointer to a C array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the mesh shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the mesh shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Swift version of this method is [setMeshSamplerStates(_:range:)](<setmeshsamplerstates(__range_).md>).

## See Also

### Assigning sampler states for mesh shaders

- [- setMeshSamplerState:atIndex:](<setmeshsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the mesh shader argument table.
- [- setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setmeshsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:](setmeshsamplerstates_lodminclamps_lodmaxclamps_withrange_.md) — Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.
