---
title: 'setSamplerState(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setsamplerstate(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstate(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setsamplerstate%28_%3Aindex%3A%29.json'
content_hash: 'sha256:a348305cf7eb52ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setSamplerState(_:index:)

<sub>Instance Method</sub>

Encodes a sampler into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

## Parameters

- `sampler` — A sampler the method encodes.

- `index` — The index of a sampler within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding samplers

- [setSamplerStates(_:range:)](<setsamplerstates(__range_).md>) — Encodes an array of samplers into the argument buffer.
