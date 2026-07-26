---
title: 'setTextures(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/settextures(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/settextures(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/settextures%28_%3Arange%3A%29.json'
content_hash: 'sha256:be6cfff0dfd4b1e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setTextures(_:range:)

<sub>Instance Method</sub>

Binds multiple textures to the texture argument table, allowing compute functions to access their data on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

## Parameters

- `textures` — A list of [MTLTexture](../mtltexture.md) instances to bind to the texture argument table.

- `range` — The texture table indices to bind each of the `textures` to, in the order they appear.

## Discussion

> [!important] Important
> This method requires that the number of instances in `textures` be the same as the length of `range`.

## See Also

### Binding textures

- [- setTexture:atIndex:](<settexture(__index_).md>) — Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.
