---
title: makeSharedTextureHandle()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/makesharedtexturehandle()
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/makesharedtexturehandle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/makesharedtexturehandle%28%29.json'
content_hash: 'sha256:a1e4118a3731f66a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# makeSharedTextureHandle()

<sub>Instance Method</sub>

Creates a new texture handle from a shareable texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeSharedTextureHandle() -> MTLSharedTextureHandle?
```

## Discussion

If the texture is not shareable, this method returns `nil`.
