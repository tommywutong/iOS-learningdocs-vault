---
title: 'setTextures:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/settextures:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/settextures:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/settextures%3Awithrange%3A.json'
content_hash: 'sha256:a8e04705b9c3a15f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setTextures:withRange:

<sub>Instance Method</sub>

Binds multiple textures to the texture argument table, allowing compute kernels to access their data on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setTextures:(id<MTLTexture> const[]) textures withRange:(NSRange) range;
```

## Parameters

- `textures` — An array of [MTLTexture](../mtltexture.md) instances to bind to the texture argument table.

- `range` — The texture table indices to bind each of the `textures` to, in the order they appear.

## Discussion

> [!important] Important
> This method requires that the number of instances in `textures` be the same as the length of `range`.

## See Also

### Binding textures

- [- setTexture:atIndex:](<settexture(__index_).md>) — Binds a texture to the texture argument table, allowing compute kernels to access its data on the GPU.
