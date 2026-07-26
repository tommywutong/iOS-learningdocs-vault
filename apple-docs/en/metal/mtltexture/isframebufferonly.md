---
title: isFramebufferOnly
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/isframebufferonly
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/isframebufferonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/isframebufferonly.json'
content_hash: 'sha256:1395839b87dc4a9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# isFramebufferOnly

<sub>Instance Property</sub>

A Boolean value that indicates whether the texture can only be used as a render target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isFramebufferOnly: Bool { get }
```

## Discussion

The default is [false](../../swift/false.md), which indicates the use of the texture is not restricted.

If [true](../../swift/true.md), neither [- replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](<replace(region_mipmaplevel_slice_withbytes_bytesperrow_bytesperimage_).md>) nor [- getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:](<getbytes(__bytesperrow_bytesperimage_from_mipmaplevel_slice_).md>) can be used with this texture. Also, this texture can only be used as an attachment for [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) and cannot be a texture argument for [MTLRenderCommandEncoder](../mtlrendercommandencoder.md), [MTLBlitCommandEncoder](../mtlblitcommandencoder.md), or [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md).

Textures you obtain from a [CAMetalDrawable](../../quartzcore/cametaldrawable.md) instance are only usable as attachments, depending on the value of [framebufferOnly](../../quartzcore/cametallayer/framebufferonly.md) passed to their parent [CAMetalLayer](../../quartzcore/cametallayer.md) instance. These restrictions don’t apply to textures that your app creates directly.

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
- [usage](usage.md) — Options that determine how you can use the texture.
- [allowGPUOptimizedContents](allowgpuoptimizedcontents.md) — A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [shareable](isshareable.md) — A Boolean indicating whether this texture can be shared with other processes.
- [swizzle](swizzle.md) — The pattern that the GPU applies to pixels when you read or sample pixels from the texture.
- [MTLTextureType](../mtltexturetype.md) — The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [MTLTextureUsage](../mtltextureusage.md) — An enumeration for the various options that determine how you can use a texture.
