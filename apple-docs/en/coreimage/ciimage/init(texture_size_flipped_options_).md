---
title: 'init(texture:size:flipped:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.9+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/ciimage/init(texture:size:flipped:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/init(texture:size:flipped:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/init%28texture%3Asize%3Aflipped%3Aoptions%3A%29.json'
content_hash: 'sha256:3824f72bccc51312'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# init(texture:size:flipped:options:)

<sub>Initializer</sub>

Initializes an image object with data supplied by an OpenGL texture.

> [!warning] Deprecated
> Core Image OpenGL API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
init(texture name: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]? = nil)
```

## Parameters

- `name` — An OpenGL texture. Because [CIImage](../ciimage.md) objects are immutable, the texture  must remain unchanged for the life of the image object. See the discussion for more information.

- `size` — The dimensions of the texture.

- `flipped` — `true` to have Core Image flip the coordinates of the texture vertically to convert between OpenGL and Core Image coordinate systems.

- `options` — A dictionary specifying image options. (See `Image Dictionary Keys`.)

## Return Value

The initialized image object.

## Discussion

When using a texture to create a [CIImage](../ciimage.md) object, the texture must be valid in the Core Image context ([CIContext](../cicontext.md)) that you draw the [CIImage](../ciimage.md) object into. This means that one of the following must be true:

- The texture must be created using the `CGLContext` object that the [CIContext](../cicontext.md) is based on.
- The context that the texture was created in must be shared with the `CGLContext` that the [CIContext](../cicontext.md)is based on.

Note that textures do not have a retain and release mechanism. This means that your application must make sure that the texture exists for the life cycle of the image. When you no longer need the image, you can delete the texture.

Core Image ignores the texture filtering and wrap modes (`GL_TEXTURE_FILTER` and `GL_TEXTURE_WRAP`) that you set through OpenGL. The filter and wrap modes are overridden by what the CISampler object specifies when you apply a filter to the [CIImage](../ciimage.md) object.

## See Also

### Deprecated

- [- initWithCGLayer:](<init(cglayer_)-2lgo6.md>) — Initializes an image object  from the contents supplied by a CGLayer object. _(deprecated)_
- [- initWithCGLayer:options:](<init(cglayer_options_)-3p3l3.md>) — Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options. _(deprecated)_
- [- initWithTexture:size:flipped:colorSpace:](<init(texture_size_flipped_colorspace_).md>) — Initializes an image object with data supplied by an OpenGL texture. _(deprecated)_
- [- initWithIOSurface:plane:format:options:](<init(iosurface_plane_format_options_)-93isn.md>) — Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface. _(deprecated)_
- [kCIImageTextureTarget](../ciimageoption/texturetarget.md) — The key for an OpenGL texture target. _(deprecated)_
- [kCIImageTextureFormat](../ciimageoption/textureformat.md) — The key for an OpenGL texture format. _(deprecated)_
