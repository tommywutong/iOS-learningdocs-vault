---
title: 'init(cgLayer:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.4+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciimage/init(cglayer:)-2lgo6'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(cglayer:)-2lgo6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28cglayer%3A%29-2lgo6.json'
content_hash: 'sha256:a368ea9534532059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(cgLayer:)

<sub>Initializer</sub>

Initializes an image object  from the contents supplied by a CGLayer object.

> [!warning] Deprecated
> Use initWithCGImage: instead.

<sub>macOS</sub>

```swift
init(cgLayer layer: CGLayer)
```

## Parameters

- `layer` — A CGLayer object. For more information see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [CGLayer](../../coregraphics/cglayer.md).

## Return Value

The initialized image object.

## See Also

### Deprecated

- [- initWithCGLayer:options:](<init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithIOSurface:plane:format:options:](<init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](../ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](../ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
