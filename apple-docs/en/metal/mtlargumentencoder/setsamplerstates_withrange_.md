---
title: 'setSamplerStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setsamplerstates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setsamplerstates%3Awithrange%3A.json'
content_hash: 'sha256:760c09a757ad4896'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setSamplerStates:withRange:

<sub>Instance Method</sub>

Encodes an array of samplers into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Parameters

- `samplers` — An array of samplers the method encodes.

- `range` — A range of indices within the argument buffer for each element in `samplers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding samplers

- [- setSamplerState:atIndex:](<setsamplerstate(__index_).md>) — Encodes a sampler into the argument buffer.
