---
title: 'imageWithTexture:size:flipped:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.9+（10.14 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciimage/imagewithtexture:size:flipped:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithtexture:size:flipped:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithtexture%3Asize%3Aflipped%3Aoptions%3A.json'
content_hash: 'sha256:a8ce9d607469e952'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithTexture:size:flipped:options:

<sub>Type Method</sub>

Creates and returns an image object initialized with data supplied by an OpenGL texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithTexture:(unsigned int) name size:(CGSize) size flipped:(BOOL) flipped options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `name` — An OpenGL texture. Because [CIImage](../ciimage.md) objects are immutable, the texture  must remain unchanged for the life of the image object. See the discussion for more information.

- `size` — The dimensions of the texture.

- `flipped` — `true` to have Core Image flip the coordinates of the texture vertically to convert between OpenGL and Core Image coordinate systems.

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

An image object initialized with the texture data.

## Discussion

When using a texture to create a [CIImage](../ciimage.md) object, the texture must be valid in the Core Image context ([CIContext](../cicontext.md)) that you draw the [CIImage](../ciimage.md) object into. This means that one of the following must be true:

- The texture must be created using the `CGLContext` object that the Core Image context is based on.
- The context that the texture was created in must be shared with the `CGLContext` that the Core Image context is based on.

Note that textures do not have a retain and release mechanism. This means that your application must make sure that the texture exists for the life cycle of the image. When you no longer need the image, you can delete the texture.

Core Image ignores the texture filtering and wrap modes (`GL_TEXTURE_FILTER` and `GL_TEXTURE_WRAP`) that you set through OpenGL. The filter and wrap modes are overridden by what the [CISampler](../cisampler.md) object specifies when you apply a filter to the [CIImage](../ciimage.md) object.

## See Also

### Deprecated

- [imageWithCGLayer:](imagewithcglayer_.md) — Creates and returns an image object from the contents supplied by a `CGLayer` object. _(deprecated)_
- [imageWithCGLayer:options:](imagewithcglayer_options_.md) — Creates and returns an image object  from the contents supplied by a `CGLayer` object, using the  specified options. _(deprecated)_
- [- initWithCGLayer:](<init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [imageWithTexture:size:flipped:colorSpace:](imagewithtexture_size_flipped_colorspace_.md) — Creates and returns an image object initialized with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithTexture:size:flipped:options:](<init(texture_size_flipped_options_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [imageWithIOSurface:options:](imagewithiosurface_options_.md) — Creates, using the specified options, and returns an image from the contents of an IOSurface.
- [- initWithIOSurface:plane:format:options:](<init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](../ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](../ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
