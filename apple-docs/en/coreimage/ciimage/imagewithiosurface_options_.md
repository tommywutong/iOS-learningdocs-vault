---
title: 'imageWithIOSurface:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithiosurface:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithiosurface:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithiosurface%3Aoptions%3A.json'
content_hash: 'sha256:4504435b9ab8c439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithIOSurface:options:

<sub>Type Method</sub>

Creates, using the specified options, and returns an image from the contents of an IOSurface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithIOSurface:(IOSurfaceRef) surface options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `surface` — An IOSurface object.

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

An image object initialized with the data from the IOSurface.

## See Also

### Related Documentation

- [imageWithIOSurface:](imagewithiosurface_.md) — Creates and returns an image from the contents of an IOSurface.

### Deprecated

- [imageWithCGLayer:](imagewithcglayer_.md) — Creates and returns an image object from the contents supplied by a `CGLayer` object. _(deprecated)_
- [imageWithCGLayer:options:](imagewithcglayer_options_.md) — Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options. _(deprecated)_
- [- initWithCGLayer:](<init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [imageWithTexture:size:flipped:colorSpace:](imagewithtexture_size_flipped_colorspace_.md) — Creates and returns an image object initialized with data supplied by an OpenGL texture. _(deprecated)_
- [imageWithTexture:size:flipped:options:](imagewithtexture_size_flipped_options_.md) — Creates and returns an image object initialized with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithIOSurface:plane:format:options:](<init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](../ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](../ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
