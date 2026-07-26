---
title: access
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturereferencetype/access
source_url: 'https://developer.apple.com/documentation/metal/mtltexturereferencetype/access'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturereferencetype/access.json'
content_hash: 'sha256:666fd40a76c3fd3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureReferenceType](../mtltexturereferencetype.md)

# access

<sub>Instance Property</sub>

The texture’s read/write access to the argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var access: MTLBindingAccess { get }
```

## Discussion

This property indicates the type of access qualifiers (read-only, write-only, or read-write) used in the Metal shading language code. For information on possible values, see [MTLArgumentAccess](../mtlargumentaccess.md).

## See Also

### Describing the texture

- [textureType](texturetype.md) — The texture type of the texture.
- [textureDataType](texturedatatype.md) — The data type of the texture.
- [isDepthTexture](isdepthtexture.md) — A Boolean value that indicates whether the texture is a depth texture.
