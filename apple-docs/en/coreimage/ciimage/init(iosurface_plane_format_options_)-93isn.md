---
title: 'init(ioSurface:plane:format:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.9+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciimage/init(iosurface:plane:format:options:)-93isn'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(iosurface:plane:format:options:)-93isn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28iosurface%3Aplane%3Aformat%3Aoptions%3A%29-93isn.json'
content_hash: 'sha256:f65efaff3c4b8a23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(ioSurface:plane:format:options:)

<sub>Initializer</sub>

Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.

<sub>macOS</sub>

```swift
init(ioSurface surface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]? = nil)
```

## Parameters

- `surface` — An IOSurface object.

- `plane` — The index of the data plane in the IOSurface object containing bitmap data for initializing the image.

- `format` — A pixel format constant. See `Pixel Formats`.

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

An image object initialized with the data from the IOSurface.

## See Also

### Deprecated

- [- initWithCGLayer:](<init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [kCIImageTextureTarget](../ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](../ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
