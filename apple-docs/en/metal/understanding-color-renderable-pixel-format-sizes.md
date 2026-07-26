---
title: Understanding color-renderable pixel format sizes
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/understanding-color-renderable-pixel-format-sizes
source_url: 'https://developer.apple.com/documentation/metal/understanding-color-renderable-pixel-format-sizes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/understanding-color-renderable-pixel-format-sizes.json'
content_hash: 'sha256:2ec0ce5ea8de94ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Textures](textures.md)

# Understanding color-renderable pixel format sizes

<sub>Article</sub>

Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.

## Overview

A _color render target_ is a texture that’s an output destination for the color data that a render pass generates. Pixel formats that you can assign to these color render targets are _color-renderable pixel formats_.

The storage size of each pixel format depends on the sum of its components. For example, the storage size of [MTLPixelFormatBGRA8Unorm](mtlpixelformat/bgra8unorm.md) is 32 bits per pixel (composed of four 8-bit components). The storage size of [MTLPixelFormatBGR5A1Unorm](mtlpixelformat/bgr5a1unorm.md) is 16 bits per pixel (composed of three 5-bit components and one 1-bit component). When you use multiple render targets in a single render pass, the combined storage size for that render pass is equal to the combined size of the pixel formats those render targets use in that pass.

Apple GPUs interpret the storage size of color render targets differently in tile memory than they do in system memory, according to the color-renderable pixel format that you assign to the target. Because tile memory has a limited size, the combined size of all color render targets in an individual render pass needs to fit within the tile memory size limit.

> [!important] Important
> To check the tile memory size for each Apple GPU, see the [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

On non-Apple GPUs, you can use up to eight color render targets per render pass with any color-renderable pixel format. Because non-Apple GPUs don’t have tile memory, they don’t have a combined size limit for their color render targets.

## See Also

### Texture basics

- [Optimizing texture data](optimizing-texture-data.md) — Optimize a texture’s data to improve GPU or CPU access.
- [MTLTexture](mtltexture.md) — A resource that holds formatted image data.
- [MTLTextureCompressionType](mtltexturecompressiontype.md)
- [MTLTextureDescriptor](mtltexturedescriptor.md) — An instance that you use to configure new Metal texture instances.
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — An object that creates textures from existing data in common image formats.
- [MTLSharedTextureHandle](mtlsharedtexturehandle.md) — A texture handle that can be shared across process address space boundaries.
- [MTLPixelFormat](mtlpixelformat.md) — The data formats that describe the organization and characteristics of individual pixels in a texture.
