---
title: MTLTextureType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturetype
source_url: 'https://developer.apple.com/documentation/metal/mtltexturetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturetype.json'
content_hash: 'sha256:c8fea2b9c5e2426c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureType

<sub>Enumeration</sub>

The dimension of each image, including whether multiple images are arranged into an array or a cube.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTextureType
```

## Overview

For a `MTLTextureTypeCube` texture, the property values describe one slice, which is any one of its six sides. For example, [mipmapLevelCount](mtltexture/mipmaplevelcount.md) is the number of mipmap levels for one slice, not the total sum of mipmap levels in six slices. By definition, the [width](mtltexture/width.md) and [height](mtltexture/height.md) of a cube texture are the same value.

Each slice of a cube texture maps to a side with a specific orientation.

| Slice index | Slice orientation |
|---|---|
| 0 | +X |
| 1 | -X |
| 2 | +Y |
| 3 | -Y |
| 4 | +Z |
| 5 | -Z |

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying the texture type

- [MTLTextureType1D](mtltexturetype/type1d.md) — A one-dimensional texture image.
- [MTLTextureType1DArray](mtltexturetype/type1darray.md) — An array of one-dimensional texture images.
- [MTLTextureType2D](mtltexturetype/type2d.md) — A two-dimensional texture image.
- [MTLTextureType2DArray](mtltexturetype/type2darray.md) — An array of two-dimensional texture images.
- [MTLTextureType2DMultisample](mtltexturetype/type2dmultisample.md) — A two-dimensional texture image that uses more than one sample for each pixel.
- [MTLTextureTypeCube](mtltexturetype/typecube.md) — A cube texture with six two-dimensional images.
- [MTLTextureTypeCubeArray](mtltexturetype/typecubearray.md) — An array of cube textures, each with six two-dimensional images.
- [MTLTextureType3D](mtltexturetype/type3d.md) — A three-dimensional texture image.
- [MTLTextureType2DMultisampleArray](mtltexturetype/type2dmultisamplearray.md) — An array of two-dimensional texture images that use more than one sample for each pixel.
- [MTLTextureTypeTextureBuffer](mtltexturetype/typetexturebuffer.md) — A texture buffer.

### Initializers

- [init(rawValue:)](<mtltexturetype/init(rawvalue_).md>)

## See Also

### Querying texture attributes

- [textureType](mtltexture/texturetype.md) — The dimension and arrangement of the texture image data.
- [pixelFormat](mtltexture/pixelformat.md) — The format of pixels in the texture.
- [width](mtltexture/width.md) — The width of the texture image for the base level mipmap, in pixels.
- [height](mtltexture/height.md) — The height of the texture image for the base level mipmap, in pixels.
- [depth](mtltexture/depth.md) — The depth of the texture image for the base level mipmap, in pixels.
- [mipmapLevelCount](mtltexture/mipmaplevelcount.md) — The number of mipmap levels in the texture.
- [arrayLength](mtltexture/arraylength.md) — The number of slices in the texture array.
- [sampleCount](mtltexture/samplecount.md) — The number of samples in each pixel.
- [framebufferOnly](mtltexture/isframebufferonly.md) — A Boolean value that indicates whether the texture can only be used as a render target.
- [usage](mtltexture/usage.md) — Options that determine how you can use the texture.
- [allowGPUOptimizedContents](mtltexture/allowgpuoptimizedcontents.md) — A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [shareable](mtltexture/isshareable.md) — A Boolean indicating whether this texture can be shared with other processes.
- [swizzle](mtltexture/swizzle.md) — The pattern that the GPU applies to pixels when you read or sample pixels from the texture.
- [MTLTextureUsage](mtltextureusage.md) — An enumeration for the various options that determine how you can use a texture.
