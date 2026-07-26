---
title: 'imageWithCGLayer:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+（10.11 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciimage/imagewithcglayer:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithcglayer:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithcglayer%3Aoptions%3A.json'
content_hash: 'sha256:7cd16fdbe5eb3666'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithCGLayer:options:

<sub>Type Method</sub>

Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithCGLayer:(CGLayerRef) layer options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `layer` — A `CGLayer` object. For more information see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [CGLayer](../../coregraphics/cglayer.md).

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

An image object initialized with the contents of the layer object  and set up with the specified options.

## See Also

### Deprecated

- [imageWithCGLayer:](imagewithcglayer_.md) — Creates and returns an image object from the contents supplied by a `CGLayer` object. _(deprecated)_
- [- initWithCGLayer:](<init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [imageWithTexture:size:flipped:colorSpace:](imagewithtexture_size_flipped_colorspace_.md) — Creates and returns an image object initialized with data supplied by an OpenGL texture. _(deprecated)_
- [imageWithTexture:size:flipped:options:](imagewithtexture_size_flipped_options_.md) — Creates and returns an image object initialized with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [imageWithIOSurface:options:](imagewithiosurface_options_.md) — Creates, using the specified options, and returns an image from the contents of an IOSurface.
- [- initWithIOSurface:plane:format:options:](<init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](../ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](../ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
