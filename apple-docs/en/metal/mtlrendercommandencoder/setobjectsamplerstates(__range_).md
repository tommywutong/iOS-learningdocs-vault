---
title: 'setObjectSamplerStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setobjectsamplerstates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectsamplerstates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setobjectsamplerstates%28_%3Arange%3A%29.json'
content_hash: 'sha256:2bfa01309d341c02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setObjectSamplerStates(_:range:)

<sub>Instance Method</sub>

Assigns multiple sampler states to a range of entries in the object shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setObjectSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers` — An array of [MTLSamplerState](../mtlsamplerstate.md) instances the command assigns to entries in the object shader argument table for sampler states.

- `range` — A span of integers that represent the entries in the object shader argument table for sampler states. Each entry stores a record of the corresponding element in `samplers`.

## Discussion

By default, the sampler state at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setObjectSamplerStates:withRange:](setobjectsamplerstates_withrange_.md).

## See Also

### Assigning sampler states for object shaders

- [- setObjectSamplerState:atIndex:](<setobjectsamplerstate(__index_).md>) — Assigns a sampler state to an entry in the object shader argument table.
- [- setObjectSamplerState:lodMinClamp:lodMaxClamp:atIndex:](<setobjectsamplerstate(__lodminclamp_lodmaxclamp_index_).md>) — Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [setObjectSamplerStates(_:lodMinClamps:lodMaxClamps:range:)](<setobjectsamplerstates(__lodminclamps_lodmaxclamps_range_).md>) — Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.
