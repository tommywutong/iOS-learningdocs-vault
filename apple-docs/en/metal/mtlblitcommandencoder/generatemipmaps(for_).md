---
title: 'generateMipmaps(for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/generatemipmaps(for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/generatemipmaps(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/generatemipmaps%28for%3A%29.json'
content_hash: 'sha256:097e8956ef90b3e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# generateMipmaps(for:)

<sub>Instance Method</sub>

Encodes a command that generates mipmaps for a texture from the base mipmap level up to the highest mipmap level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func generateMipmaps(for texture: any MTLTexture)
```

## Parameters

- `texture` — A texture instance the command generates mipmaps for that has: - A [mipmapLevelCount](../mtltexture/mipmaplevelcount.md) property that’s greater than `1` - A [pixelFormat](../mtltexture/pixelformat.md) that’s color-renderable and color-filterable

## Discussion

The command generates with scaled images for all levels up to the highest mipmap level.

> [!note] Note
> The image filtering that GPU drivers use to generate the mipmaps may vary by the feature families ([MTLGPUFamily](../mtlgpufamily.md)) it supports.
