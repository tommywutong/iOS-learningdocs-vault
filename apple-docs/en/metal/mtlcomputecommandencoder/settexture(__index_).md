---
title: 'setTexture(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/settexture(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/settexture(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/settexture%28_%3Aindex%3A%29.json'
content_hash: 'sha256:d22c75a0b11cf5d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setTexture(_:index:)

<sub>Instance Method</sub>

Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance to bind to the texture argument table.

- `index` — The index the texture binds to in the texture argument table.

## See Also

### Binding textures

- [setTextures(_:range:)](<settextures(__range_).md>) — Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.
