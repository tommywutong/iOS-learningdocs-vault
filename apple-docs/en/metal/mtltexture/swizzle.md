---
title: swizzle
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/swizzle
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/swizzle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/swizzle.json'
content_hash: 'sha256:d2493488871bef5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# swizzle

<sub>Instance Property</sub>

The pattern that the GPU applies to pixels when you read or sample pixels from the texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var swizzle: MTLTextureSwizzleChannels { get }
```

## See Also

### Querying texture attributes

- [textureType](texturetype.md) — The dimension and arrangement of the texture image data.
- [pixelFormat](pixelformat.md) — The format of pixels in the texture.
- [width](width.md) — The width of the texture image for the base level mipmap, in pixels.
- [height](height.md) — The height of the texture image for the base level mipmap, in pixels.
- [depth](depth.md) — The depth of the texture image for the base level mipmap, in pixels.
- [mipmapLevelCount](mipmaplevelcount.md) — The number of mipmap levels in the texture.
- [arrayLength](arraylength.md) — The number of slices in the texture array.
- [sampleCount](samplecount.md) — The number of samples in each pixel.
- [framebufferOnly](isframebufferonly.md) — A Boolean value that indicates whether the texture can only be used as a render target.
- [usage](usage.md) — Options that determine how you can use the texture.
- [allowGPUOptimizedContents](allowgpuoptimizedcontents.md) — A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [shareable](isshareable.md) — A Boolean indicating whether this texture can be shared with other processes.
- [MTLTextureType](../mtltexturetype.md) — The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [MTLTextureUsage](../mtltextureusage.md) — An enumeration for the various options that determine how you can use a texture.
