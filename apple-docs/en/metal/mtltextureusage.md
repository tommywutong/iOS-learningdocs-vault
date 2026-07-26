---
title: MTLTextureUsage
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage.json'
content_hash: 'sha256:cc28a13f3bf6fec3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureUsage

<sub>Structure</sub>

An enumeration for the various options that determine how you can use a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLTextureUsage
```

## Overview

If a texture has multiple uses in your app, you can combine multiple usage options for that texture. After you set the texture’s usage options, you can use it only in the ways that you specified.

Metal can optimize operations for a given texture, based on its intended use. Set explicit usage options for a texture, if you know them in advance, before you use the texture. Only set usage options that correspond to a texture’s intended use.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to a given texture if you set any of these options:

- [MTLTextureUsageUnknown](mtltextureusage/unknown.md)
- [MTLTextureUsageShaderWrite](mtltextureusage/shaderwrite.md)
- [MTLTextureUsagePixelFormatView](mtltextureusage/pixelformatview.md)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Specifying texture usage options

- [MTLTextureUsageUnknown](mtltextureusage/unknown.md) — An option for a texture whose usage is unknown.
- [MTLTextureUsageShaderRead](mtltextureusage/shaderread.md) — An option for reading or sampling from the texture in a shader.
- [MTLTextureUsageShaderWrite](mtltextureusage/shaderwrite.md) — An option for writing to the texture in a shader.
- [MTLTextureUsageShaderAtomic](mtltextureusage/shaderatomic.md) — An option that enables atomic memory operations on texture elements in shader code.
- [MTLTextureUsageRenderTarget](mtltextureusage/rendertarget.md) — An option for rendering to the texture in a render pass.
- [MTLTextureUsagePixelFormatView](mtltextureusage/pixelformatview.md) — An option to create texture views with a different component layout.

### Creating texture usage options

- [init(rawValue:)](<mtltextureusage/init(rawvalue_).md>) — Creates new, empty usage options.

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
- [MTLTextureType](mtltexturetype.md) — The dimension of each image, including whether multiple images are arranged into an array or a cube.
