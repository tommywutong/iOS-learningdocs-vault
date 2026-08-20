---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Blit-Ctx/Blit-Ctx.html
archived_at: '2026-07-15T08:16:48.602070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Metal%20Tools.md)[Previous](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md)

# Buffer and Texture Operations: Blit Command Encoder

[MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) provides methods for copying data between resources (buffers and textures). Data copying operations may be necessary for image processing and texture effects, such as blurring or reflections. They may be used to access image data that is rendered off-screen.

To perform data copying operations, first create a [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) object by calling the [blitCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443001-blitcommandencoder) method of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer). Then call the [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) methods described below to encode commands onto the command buffer.

The following [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) methods copy image data between resource objects: between two buffer objects, between two texture objects, and between a buffer and a texture.

The method [copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400767-copy) copies data between two buffers: from the source buffer into the destination buffer `toBuffer`. If the source and destination are the same buffer, and the range being copied overlaps, the results are undefined.

The method [copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400752-copy) copies image data from a source buffer into the destination texture `toTexture`.

The method [copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400754-copyfromtexture) copies a region of image data between two textures: from a single cube slice and mipmap level of the source texture to the destination texture `toTexture`.

The method [copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400773-copy) copies a region of image data from a single cube slice and mipmap level of a source texture into the destination buffer `toBuffer`.

The [generateMipmapsForTexture:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400748-generatemipmapsfortexture) method of [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) automatically generate mipmaps for the given texture, starting from the base level texture image. `generateMipmapsForTexture:` creates scaled images for all mipmap levels up to the maximum level.

For details on how the number of mipmaps and the size of each mipmap are determined, see [Slices](Resource%20Objects-%20Buffers%20and%20Textures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltm).

The [fillBuffer:range:value:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400761-fillbuffer) method of [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) stores the 8-bit constant `value` in every byte over the specified `range` of the given buffer.

To end encoding commands for a blit command encoder, call [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding). After ending the previous command encoder, you can create a new command encoder of any type to encode additional commands into the command buffer.

[Next](Metal%20Tools.md)[Previous](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md)

