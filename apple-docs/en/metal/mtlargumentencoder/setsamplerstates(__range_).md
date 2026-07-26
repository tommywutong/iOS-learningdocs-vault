---
title: 'setSamplerStates(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setsamplerstates(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setsamplerstates%28_%3Arange%3A%29.json'
content_hash: 'sha256:74b1c44301cce60f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setSamplerStates(_:range:)

<sub>Instance Method</sub>

Encodes an array of samplers into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSamplerStates(_ samplers: [(any MTLSamplerState)?], range: Range<Int>)
```

## Parameters

- `samplers` — An array of samplers the method encodes.

- `range` — A range of indices within the argument buffer for each element in `samplers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding samplers

- [- setSamplerState:atIndex:](<setsamplerstate(__index_).md>) — Encodes a sampler into the argument buffer.
