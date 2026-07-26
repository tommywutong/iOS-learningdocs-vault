---
title: 'setMeshSamplerState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setmeshsamplerstate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshsamplerstate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setmeshsamplerstate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:11f0742b0dca3e75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setMeshSamplerState(_:index:)

<sub>Instance Method</sub>

Assigns a sampler state to an entry in the mesh shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setMeshSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler` — An [MTLSamplerState](../mtlsamplerstate.md) instance the command assigns to an entry in the mesh shader argument table for sampler states.

- `index` — An integer that represents the entry in the mesh shader argument table for sampler states that stores a record of `sampler`.

## Discussion

By default, the sampler state at each index is `nil`.

## See Also

### Assigning sampler states for mesh shaders

- [- setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setmeshsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [setMeshSamplerStates(_:range:)](<setmeshsamplerstates(__range_).md>) — Assigns multiple sampler states to a range of entries in the mesh shader argument table.
- [setMeshSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setmeshsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.
