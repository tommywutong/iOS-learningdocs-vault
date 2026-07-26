---
title: MTLTextureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor.json'
content_hash: 'sha256:71ad984f7671c48f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureDescriptor

<sub>Class</sub>

An instance that you use to configure new Metal texture instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTextureDescriptor
```

## Overview

To create a new texture, first create an [MTLTextureDescriptor](mtltexturedescriptor.md) instance and set its property values. Then, call either the [- newTextureWithDescriptor:](<mtldevice/maketexture(descriptor_).md>) or [- newTextureWithDescriptor:iosurface:plane:](<mtldevice/maketexture(descriptor_iosurface_plane_).md>) method of an [MTLDevice](mtldevice.md) instance, or the [- newTextureWithDescriptor:offset:bytesPerRow:](<mtlbuffer/maketexture(descriptor_offset_bytesperrow_).md>) method of an [MTLBuffer](mtlbuffer.md) instance.

When you create a texture, Metal copies property values from the descriptor into the new texture. You can reuse an [MTLTextureDescriptor](mtltexturedescriptor.md) instance, modifying its property values as needed, to create more [MTLTexture](mtltexture.md) instances, without affecting any textures you already created.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating texture descriptors

- [+ texture2DDescriptorWithPixelFormat:width:height:mipmapped:](<mtltexturedescriptor/texture2ddescriptor(pixelformat_width_height_mipmapped_).md>) — Creates a texture descriptor object for a 2D texture.
- [+ textureCubeDescriptorWithPixelFormat:size:mipmapped:](<mtltexturedescriptor/texturecubedescriptor(pixelformat_size_mipmapped_).md>) — Creates a texture descriptor object for a cube texture.
- [+ textureBufferDescriptorWithPixelFormat:width:resourceOptions:usage:](<mtltexturedescriptor/texturebufferdescriptor(with_width_resourceoptions_usage_).md>) — Creates a texture descriptor object for a texture buffer.

### Specifying texture attributes

- [textureType](mtltexturedescriptor/texturetype.md) — The dimension and arrangement of texture image data.
- [pixelFormat](mtltexturedescriptor/pixelformat.md) — The size and bit layout of all pixels in the texture.
- [width](mtltexturedescriptor/width.md) — The width of the texture image for the base level mipmap, in pixels.
- [height](mtltexturedescriptor/height.md) — The height of the texture image for the base level mipmap, in pixels.
- [depth](mtltexturedescriptor/depth.md) — The depth of the texture image for the base level mipmap, in pixels.
- [mipmapLevelCount](mtltexturedescriptor/mipmaplevelcount.md) — The number of mipmap levels for this texture.
- [sampleCount](mtltexturedescriptor/samplecount.md) — The number of samples in each fragment.
- [arrayLength](mtltexturedescriptor/arraylength.md) — The number of array elements for this texture.
- [resourceOptions](mtltexturedescriptor/resourceoptions.md) — The behavior of a new memory allocation.
- [cpuCacheMode](mtltexturedescriptor/cpucachemode.md) — The CPU cache mode used for the CPU mapping of the texture.
- [storageMode](mtltexturedescriptor/storagemode.md) — The location and access permissions of the texture.
- [hazardTrackingMode](mtltexturedescriptor/hazardtrackingmode.md) — The texture’s hazard tracking mode.
- [allowGPUOptimizedContents](mtltexturedescriptor/allowgpuoptimizedcontents.md) — A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.
- [usage](mtltexturedescriptor/usage.md) — Options that determine how you can use the texture.
- [swizzle](mtltexturedescriptor/swizzle.md) — The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
- [MTLTextureSwizzleChannels](mtltextureswizzlechannels.md) — A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.
- [MTLTextureSwizzle](mtltextureswizzle.md) — A set of options to choose from when creating a texture swizzle pattern.
- [MTLTextureType](mtltexturetype.md) — The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [MTLTextureUsage](mtltextureusage.md) — An enumeration for the various options that determine how you can use a texture.

### Instance Properties

- [compressionType](mtltexturedescriptor/compressiontype.md)
- [placementSparsePageSize](mtltexturedescriptor/placementsparsepagesize.md) — Determines the page size for a placement sparse texture.

## See Also

### Texture basics

- [Understanding color-renderable pixel format sizes](understanding-color-renderable-pixel-format-sizes.md) — Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing texture data](optimizing-texture-data.md) — Optimize a texture’s data to improve GPU or CPU access.
- [MTLTexture](mtltexture.md) — A resource that holds formatted image data.
- [MTLTextureCompressionType](mtltexturecompressiontype.md)
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — An object that creates textures from existing data in common image formats.
- [MTLSharedTextureHandle](mtlsharedtexturehandle.md) — A texture handle that can be shared across process address space boundaries.
- [MTLPixelFormat](mtlpixelformat.md) — The data formats that describe the organization and characteristics of individual pixels in a texture.
