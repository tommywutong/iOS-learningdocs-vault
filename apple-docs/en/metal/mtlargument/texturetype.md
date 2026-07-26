---
title: textureType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlargument/texturetype
source_url: 'https://developer.apple.com/documentation/metal/mtlargument/texturetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargument/texturetype.json'
content_hash: 'sha256:6c631d942cd07a9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgument](../mtlargument.md)

# textureType

<sub>Instance Property</sub>

The texture type of a texture argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var textureType: MTLTextureType { get }
```

## Discussion

For information on possible values, see [MTLTextureType](../mtltexturetype.md). If the argument is not a texture, querying this property is a fatal error.

## See Also

### Describing a texture argument

- [textureDataType](texturedatatype.md) — The data type of a texture argument. _(deprecated)_
- [isDepthTexture](isdepthtexture.md) — A Boolean value that indicates whether the texture is a depth texture. _(deprecated)_
