---
title: 'newTextureView(with:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexture/newtextureview(with:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/newtextureview(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/newtextureview%28with%3A%29.json'
content_hash: 'sha256:439ff09e86759e72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# newTextureView(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func newTextureView(with descriptor: MTLTextureViewDescriptor) -> (any MTLTexture)?
```

## Discussion

Create a new texture which shares the same storage as the source texture, but with different (but compatible) properties specified by the descriptor
