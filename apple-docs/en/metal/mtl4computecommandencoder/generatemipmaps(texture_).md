---
title: 'generateMipmaps(texture:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/generatemipmaps(texture:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/generatemipmaps(texture:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/generatemipmaps%28texture%3A%29.json'
content_hash: 'sha256:9b803ec4f24430bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# generateMipmaps(texture:)

<sub>Instance Method</sub>

Encodes a command that generates mipmaps for a texture instance from the base mipmap level up to the highest mipmap level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func generateMipmaps(texture: any MTLTexture)
```

## Parameters

- `texture` — A mipmapped, color-renderable or color-filterable [MTLTexture](../mtltexture.md) instance the command generates mipmaps for.

## Discussion

This method generates mipmaps for a mipmapped texture. The texture you provide needs to have a [mipmapLevelCount](../mtltexture/mipmaplevelcount.md) greater than `1`, and a color-renderable or color-filterable [pixelFormat](../mtltexture/pixelformat.md).
