---
title: textureFormat
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.9+（10.14 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coreimage/ciimageoption/textureformat
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageoption/textureformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageoption/textureformat.json'
content_hash: 'sha256:d517b924bca10321'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageOption](../ciimageoption.md)

# textureFormat

<sub>Type Property</sub>

The key for an OpenGL texture format.

> [!warning] Deprecated
> Core Image OpenGL API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
static let textureFormat: CIImageOption
```

## Discussion

The value for this key must be an [NSNumber](../../foundation/nsnumber.md) object containing a Core Image pixel format constant. (See `Pixel Formats`.) You may only use this key when initializing an image using the [- initWithTexture:size:flipped:options:](<../ciimage/init(texture_size_flipped_options_).md>) method.

## See Also

### Deprecated

- [- initWithCGLayer:](<../ciimage/init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<../ciimage/init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<../ciimage/init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<../ciimage/init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithIOSurface:plane:format:options:](<../ciimage/init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
