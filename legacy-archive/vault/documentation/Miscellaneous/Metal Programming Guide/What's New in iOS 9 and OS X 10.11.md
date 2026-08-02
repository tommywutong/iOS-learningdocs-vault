---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/WhatsNewiniOS9andOSX1011/WhatsNewiniOS9andOSX1011.html
archived_at: '2026-07-15T08:16:57.081670Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](What%E2%80%99s%20New%20in%20iOS%2010%2C%20tvOS%2010%2C%20and%20macOS%2010.12.md)[Previous](Metal%20Feature%20Set%20Tables.md)

# What's New in iOS 9 and OS X 10.11

This chapter summarizes the new features introduced in iOS 9 and OS X 10.11.

All devices that support Metal conform to a feature set value described in Listing 10-1.

__Listing 10-1__  Metal Feature Sets

```
typedef NS_ENUM(NSUInteger, MTLFeatureSet)
{
    MTLFeatureSet_iOS_GPUFamily1_v1 = 0,
    MTLFeatureSet_iOS_GPUFamily2_v1 = 1,
    MTLFeatureSet_iOS_GPUFamily1_v2 = 2,
    MTLFeatureSet_iOS_GPUFamily2_v2 = 3,
    MTLFeatureSet_iOS_GPUFamily3_v1 = 4,
    MTLFeatureSet_OSX_GPUFamily1_v1 = 10000
};
```

All OS X devices that support Metal support the `OSX_GPUFamily1_v1` feature set.

iOS devices that support Metal support a feature set determined by their GPU and OS versions. See the [MTLFeatureSet](https://developer.apple.com/documentation/metal/mtlfeatureset) reference and _[iOS Device Compatibility Reference](../../iOS%20Device%20Compatibility%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojz)_ for more information.

To find out which feature set is supported by a device, query the [supportsFeatureSet:](https://developer.apple.com/documentation/metal/mtldevice/1433418-supportsfeatureset) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object.

Use the [MTLCreateSystemDefaultDevice](https://developer.apple.com/documentation/metal/1433401-mtlcreatesystemdefaultdevice) function to obtain the preferred GPU for your app. `OSX_GPUFamily1_v1` feature set devices may have multiple GPUs, which you can obtain by calling the [MTLCopyAllDevices](https://developer.apple.com/documentation/metal/1433367-mtlcopyalldevices) function. To further obtain the characteristics of a single GPU in a multi-GPU system, query the [headless](https://developer.apple.com/documentation/metal/mtldevice/1433377-headless) property to find out if the GPU is attached to a display and query the [lowPower](https://developer.apple.com/documentation/metal/mtldevice/1433409-lowpower) property to find the lower-power GPU in an automatic graphics switching system.

You can query specific render and compute characteristics with the new [supportsTextureSampleCount:](https://developer.apple.com/documentation/metal/mtldevice/1433355-supportstexturesamplecount) method and [maxThreadsPerThreadgroup](https://developer.apple.com/documentation/metal/mtldevice/1433393-maxthreadsperthreadgroup) property added to the [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) protocol.

The `OSX_GPUFamily1_v1` feature set includes support for managing resources on GPUs that contain discrete memory. Resource memory allocation is explicitly handled by selecting an appropriate storage mode value from the Listing 10-2 enum for textures and Listing 10-3 enum for buffers.

__Listing 10-2__  Texture Storage Modes

```
typedef NS_ENUM(NSUInteger, MTLStorageMode)
{
    MTLStorageModeShared  = 0,
    MTLStorageModeManaged = 1,
    MTLStorageModePrivate = 2,
};
```


__Listing 10-3__  Buffer Storage Modes

```
#define MTLResourceStorageModeShift  4

typedef NS_ENUM(NSUInteger, MTLResourceOptions)
{
    MTLResourceStorageModeShared  = MTLStorageModeShared  << MTLResourceStorageModeShift,
    MTLResourceStorageModeManaged = MTLStorageModeManaged << MTLResourceStorageModeShift,
    MTLResourceStorageModePrivate = MTLStorageModePrivate << MTLResourceStorageModeShift,
};
```

iOS feature sets only support shared and private storage modes. A description of the three new resource storage modes is summarized in the following sub-sections.

Resources allocated with the shared storage mode are stored in memory that is accessible to both the CPU and the GPU. On devices with discrete memory, these resources are accessed directly from CPU local memory rather than being copied to GPU memory.

In iOS feature sets, this is the default storage mode for textures. In the `OSX_GPUFamily1_v1` feature set, textures cannot be allocated with the shared storage mode.

Resources allocated with the private storage mode are stored in memory that is only accessible to the GPU.

Buffers and textures allocated with private storage mode can only be accessed by the GPU. The [contents](https://developer.apple.com/documentation/metal/mtlbuffer/1515716-contents) property of a buffer returns `NULL` and the [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) methods listed below are illegal to call:

- [replaceRegion:mipmapLevel:withBytes:bytesPerRow:](https://developer.apple.com/documentation/metal/mtltexture/1515464-replaceregion)
- [replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](https://developer.apple.com/documentation/metal/mtltexture/1515679-replaceregion)
- [getBytes:bytesPerRow:fromRegion:mipmapLevel:](https://developer.apple.com/documentation/metal/mtltexture/1515751-getbytes)
- [getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:](https://developer.apple.com/documentation/metal/mtltexture/1516318-getbytes)

To access a private resource, your app may perform one or more of the following actions:

- Blit to or from the private resource.
- Read from the private resource from any shader function.
- Render to the private resource from a fragment shader.
- Write to the private resource from a compute function.

On GPUs without discrete memory, managed resources have only a single memory allocation accessible to both the CPU and GPU. On GPUs with discrete memory, managed resources internally allocate both CPU-accessible and GPU-accessible memory.

Managed textures are not available in iOS feature sets; use [MTLStorageModeShared](https://developer.apple.com/documentation/metal/mtlstoragemode/shared) instead.

Any time your app uses the CPU to directly modify the contents of a buffer, you must make a call to the [didModifyRange:](https://developer.apple.com/documentation/metal/mtlbuffer/1516121-didmodifyrange) method to notify Metal that you have changed the contents of the resource indicated by the specific range.

If you use the GPU to modify the contents of a managed resource and you wish to access the results with the CPU, then you must first synchronize the resource using the [synchronizeResource:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400775-synchronize) method or [synchronizeTexture:slice:level:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400757-synchronizetexture) method.

Generally, there are four main scenarios to consider when choosing a storage mode:

- Choose [MTLResourceStorageModePrivate](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodeprivate) for resources that are only ever read from and/or written to by the GPU. For example—render target textures (a particularly common and important case).
- Choose [MTLResourceStorageModeManaged](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515616-storagemodemanaged) or [MTLResourceStorageModePrivate](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodeprivate) for resources that are initialized once and used many times in the future.
- Choose [MTLResourceStorageModeManaged](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515616-storagemodemanaged) for resources that are populated per-frame by the CPU and then read by the GPU. For example—shader constant buffers or dynamic vertex data.
- Choose [MTLResourceStorageModeShared](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515613-storagemodeshared) for resources written to by the CPU and then blitted into GPU memory (or, for CPU reads from GPU memory). For example—staging buffers.

For textures, set the desired storage mode with the [storageMode](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516262-storagemode) property of a [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor) object. The default storage mode for textures is [MTLStorageModeShared](https://developer.apple.com/documentation/metal/mtlstoragemode/shared) in iOS feature sets and [MTLStorageModeManaged](https://developer.apple.com/documentation/metal/mtlstoragemode/mtlstoragemodemanaged) in the `OSX_GPUFamily1_v1` feature set.

For buffers, set the desired storage mode by passing in the respective [MTLResourceOptions](https://developer.apple.com/documentation/metal/mtlresourceoptions) value in any of the [newBufferWithLength:options:](https://developer.apple.com/documentation/metal/mtldevice/1433375-newbufferwithlength), [newBufferWithBytes:length:options:](https://developer.apple.com/documentation/metal/mtldevice/1433429-newbufferwithbytes), or [newBufferWithBytesNoCopy:length:options:deallocator:](https://developer.apple.com/documentation/metal/mtldevice/1433382-makebuffer) methods of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice). The default storage mode for buffers is [MTLStorageModeShared](https://developer.apple.com/documentation/metal/mtlstoragemode/shared), but `OSX_GPUFamily1_v1` feature set apps may benefit from increased performance by explicitly managing their buffers with the managed or private storage modes.

The storage mode of a resource, for either a texture or a buffer, can be queried with the [storageMode](https://developer.apple.com/documentation/metal/mtlresource/1515477-storagemode) property of a [MTLResource](https://developer.apple.com/documentation/metal/mtlresource) object.

Hardware support for different texture types and pixel formats is a key capability difference between feature sets. This section lists the major texture additions to the framework; for a more detailed discussion, see the code listings and comparison tables in the [MTLPixelFormat](https://developer.apple.com/documentation/metal/mtlpixelformat) reference and [Metal Feature Set Tables](Metal%20Feature%20Set%20Tables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjtfvjvomi) chapter.

The `iOS_GPUFamily2_v1`, `iOS_GPUFamily2_v2`, and `iOS_GPUFamily3_v1` feature sets add support for ASTC textures. These pixel formats are listed in Listing 10-4.

__Listing 10-4__  ASTC Pixel Formats

```
typedef NS_ENUM(NSUInteger, MTLPixelFormat)
{
    // ASTC
    MTLPixelFormatASTC_4x4_sRGB      = 186,
    MTLPixelFormatASTC_5x4_sRGB      = 187,
    MTLPixelFormatASTC_5x5_sRGB      = 188,
    MTLPixelFormatASTC_6x5_sRGB      = 189,
    MTLPixelFormatASTC_6x6_sRGB      = 190,
    MTLPixelFormatASTC_8x5_sRGB      = 192,
    MTLPixelFormatASTC_8x6_sRGB      = 193,
    MTLPixelFormatASTC_8x8_sRGB      = 194,
    MTLPixelFormatASTC_10x5_sRGB     = 195,
    MTLPixelFormatASTC_10x6_sRGB     = 196,
    MTLPixelFormatASTC_10x8_sRGB     = 197,
    MTLPixelFormatASTC_10x10_sRGB    = 198,
    MTLPixelFormatASTC_12x10_sRGB    = 199,
    MTLPixelFormatASTC_12x12_sRGB    = 200,
    MTLPixelFormatASTC_4x4_LDR       = 204,
    MTLPixelFormatASTC_5x4_LDR       = 205,
    MTLPixelFormatASTC_5x5_LDR       = 206,
    MTLPixelFormatASTC_6x5_LDR       = 207,
    MTLPixelFormatASTC_6x6_LDR       = 208,
    MTLPixelFormatASTC_8x5_LDR       = 210,
    MTLPixelFormatASTC_8x6_LDR       = 211,
    MTLPixelFormatASTC_8x8_LDR       = 212,
    MTLPixelFormatASTC_10x5_LDR      = 213,
    MTLPixelFormatASTC_10x6_LDR      = 214,
    MTLPixelFormatASTC_10x8_LDR      = 215,
    MTLPixelFormatASTC_10x10_LDR     = 216,
    MTLPixelFormatASTC_12x10_LDR     = 217,
    MTLPixelFormatASTC_12x12_LDR     = 218,
};
```

The `OSX_GPUFamily1_v1` feature set supports BC textures instead. The new pixel formats are listed in Listing 10-5.

__Listing 10-5__  BC Pixel Formats

```
typedef NS_ENUM(NSUInteger, MTLPixelFormat)
{
    // BC1, BC2, BC3 (aka S3TC/DXT)
    MTLPixelFormatBC1_RGBA           = 130,
    MTLPixelFormatBC1_RGBA_sRGB      = 131,
    MTLPixelFormatBC2_RGBA           = 132,
    MTLPixelFormatBC2_RGBA_sRGB      = 133,
    MTLPixelFormatBC3_RGBA           = 134,
    MTLPixelFormatBC3_RGBA_sRGB      = 135,

    // BC4, BC5 (aka RGTC)
    MTLPixelFormatBC4_RUnorm         = 140,
    MTLPixelFormatBC4_RSnorm         = 141,
    MTLPixelFormatBC5_RGUnorm        = 142,
    MTLPixelFormatBC5_RGSnorm        = 143,

    // BC6H, BC7 (aka BPTC)
    MTLPixelFormatBC6H_RGBFloat      = 150,
    MTLPixelFormatBC6H_RGBUfloat     = 151,
    MTLPixelFormatBC7_RGBAUnorm      = 152,
    MTLPixelFormatBC7_RGBAUnorm_sRGB = 153,
};
```


The [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) protocol contains a new [MTLBlitOption](https://developer.apple.com/documentation/metal/mtlblitoption) value that enables copying to or from a texture with a PVRTC pixel format. Two new methods support these operations by passing the [MTLBlitOptionRowLinearPVRTC](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionrowlinearpvrtc) value into their `options` parameter:

- To copy PVRTC data from a buffer to a texture, use [copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400771-copyfrombuffer)
- To copy PVRTC data from a texture to a buffer, use [copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400756-copy)

PVRTC blocks are arranged linearly in memory in row-major order, similar to all other compressed texture formats. PVRTC pixel formats are only available in iOS feature sets.

The `OSX_GPUFamily1_v1` feature set does not support separate depth and stencil render targets. If these render targets are needed, use one of the newly introduced depth/stencil pixel formats to set the same texture as both the depth and stencil render target. The combined depth/stencil pixel formats are listed in Listing 10-6.

__Listing 10-6__  Depth/Stencil Pixel Formats

```
typedef NS_ENUM(NSUInteger, MTLPixelFormat)
{
    // Depth/Stencil
    MTLPixelFormatDepth24Unorm_Stencil8 = 255,
    MTLPixelFormatDepth32Float_Stencil8 = 260,
};
```

All feature sets support the `MTLPixelFormatDepth32Float_Stencil8` pixel format. Only some devices that support the `OSX_GPUFamily1_v1` feature set also support the `MTLPixelFormatDepth24Unorm_Stencil8` pixel format. Query the [depth24Stencil8PixelFormatSupported](https://developer.apple.com/documentation/metal/mtldevice/1433371-depth24stencil8pixelformatsuppor) property of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object to determine whether the pixel format is supported or not.

Textures with a depth, stencil, or depth/stencil pixel format can only be allocated with the private storage mode. To load or save the contents of these textures, you must perform a blit operation. The [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) protocol contains the new [MTLBlitOption](https://developer.apple.com/documentation/metal/mtlblitoption) values that define the behavior of a blit operation for textures with a depth, stencil, or depth/stencil pixel format:

- Use the [MTLBlitOptionNone](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionnone) value to blit the contents of a texture with a depth-only or stencil-only pixel format.
- Use the [MTLBlitOptionDepthFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptiondepthfromdepthstencil) value to blit the depth portion of a texture with a combined depth/stencil pixel format.
- Use the [MTLBlitOptionStencilFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionstencilfromdepthstencil) value to blit the stencil portion of a texture with a combined depth/stencil pixel format.

Two new methods support these operations with their `options` parameter:

- To copy depth or stencil data from a buffer to a texture, use [copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400771-copyfrombuffer)
- To copy depth or stencil data from a texture to a buffer, use [copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400756-copy)

The `OSX_GPUFamily1_v1` feature set adds support for cube array textures with the [MTLTextureTypeCubeArray](https://developer.apple.com/documentation/metal/mtltexturetype/typecubearray) texture type value. Similarly, support for this texture type has been added to the Metal shading language with the `texturecube_array` type. The maximum length of a cube array texture is `341` (2048 divided by 6 cube faces).

The [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor) class contains the new [usage](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515783-usage) property that allows you to declare how a texture will be used in your app. Multiple [MTLTextureUsage](https://developer.apple.com/documentation/metal/mtltextureusage) values may be combined with a bitwise OR (`|`) if the texture will serve multiple uses over its lifetime. A [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) object can only be used in the ways specified by its [usage](https://developer.apple.com/documentation/metal/mtltexture/1515763-usage) value(s) (an error will occur otherwise). The [MTLTextureUsage](https://developer.apple.com/documentation/metal/mtltextureusage) options and their intended use are described as follows:

- [MTLTextureUsageShaderRead](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusageshaderread) enables loading or sampling from the texture in any shader stage.
- [MTLTextureUsageShaderWrite](https://developer.apple.com/documentation/metal/mtltextureusage/1515854-shaderwrite) enables writing to the texture from compute shaders.
- [MTLTextureUsageRenderTarget](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusagerendertarget) enables using this texture as a color, depth, or stencil render target in a render pass descriptor.
- [MTLTextureUsagePixelFormatView](https://developer.apple.com/documentation/metal/mtltextureusage/1516223-pixelformatview) indicates that the texture will be used to create a new texture with the [newTextureViewWithPixelFormat:](https://developer.apple.com/documentation/metal/mtltexture/1515598-newtextureviewwithpixelformat) or [newTextureViewWithPixelFormat:textureType:levels:slices:](https://developer.apple.com/documentation/metal/mtltexture/1515409-newtextureviewwithpixelformat) methods.

Specifying and adhering to an appropriate texture usage allows Metal to optimize GPU operations for a given texture. For example—set the descriptor’s [usage](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515783-usage) value to [MTLTextureUsageRenderTarget](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusagerendertarget) if you intend to use the resulting texture as a render target. This may significantly improve your app’s performance (with certain hardware).

If you don’t know what a texture will be used for, set the descriptor’s [usage](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515783-usage) value to [MTLTextureUsageUnknown](https://developer.apple.com/documentation/metal/mtltextureusage/1515856-unknown). This value allows your newly created texture to be used everywhere, but Metal will not be able to optimize its use in your app.

Listing 10-7 shows you how to create a texture with multiple uses.

__Listing 10-7__  Specifying a Texture’s Usage

```
MTLTextureDescriptor* textureDescriptor = [[MTLTextureDescriptor alloc] init];
textureDescriptor.usage = MTLTextureUsageRenderTarget | MTLTextureUsageShaderRead;
// set additional properties

id <MTLTexture> texture = [self.device newTextureWithDescriptor:textureDescriptor];
// use the texture in a color render target
// sample from the texture in a fragment shader
```


The [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) protocol adds the extended [newTextureViewWithPixelFormat:textureType:levels:slices:](https://developer.apple.com/documentation/metal/mtltexture/1515409-newtextureviewwithpixelformat) method that allows you to specify a new texture type, base level range, and base slice range for a new texture view (in addition to the pixel format parameter that was already supported by the [newTextureViewWithPixelFormat:](https://developer.apple.com/documentation/metal/mtltexture/1515598-newtextureviewwithpixelformat) method). Textures created with these texture view methods can now query their parent texture’s attributes with the [parentTexture](https://developer.apple.com/documentation/metal/mtltexture/1515372-parenttexture), [parentRelativeLevel](https://developer.apple.com/documentation/metal/mtltexture/1516265-parentrelativelevel), and [parentRelativeSlice](https://developer.apple.com/documentation/metal/mtltexture/1516221-parentrelativeslice) properties (in addition to querying other attributes already supported by the [pixelFormat](https://developer.apple.com/documentation/metal/mtltexture/1515344-pixelformat) and [textureType](https://developer.apple.com/documentation/metal/mtltexture/1515517-texturetype) properties). For details on texture view creation restrictions, such as valid casting targets, see _[MTLTexture Protocol Reference](https://developer.apple.com/documentation/metal/mtltexture)_.

The `OSX_GPUFamily1_v1` feature set adds support for IOSurfaces. Use the [newTextureWithDescriptor:iosurface:plane:](https://developer.apple.com/documentation/metal/mtldevice/1433378-newtexturewithdescriptor) method to create a new texture from an existing IOSurface.

There are several graphics API additions to the [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) class. The main new features are summarized below:

- The method [setStencilFrontReferenceValue:backReferenceValue:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515522-setstencilreferencevalues) allows front-facing and back-facing primitives to use different stencil test reference values.
- Depth clipping is supported with the [MTLDepthClipMode](https://developer.apple.com/documentation/metal/mtldepthclipmode) enum and [setDepthClipMode:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516267-setdepthclipmode) method.
- Counting occlusion query is supported in the `OSX_GPUFamily1_v1` and `iOS_GPUFamily3_v1` feature sets with the new [MTLVisibilityResultModeCounting](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/mtlvisibilityresultmodecounting) value that can be passed into the [setVisibilityResultMode:offset:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515556-setvisibilityresultmode) method.
- Texture barriers are supported in the `OSX_GPUFamily1_v1` feature set by calling the [textureBarrier](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515866-texturebarrier) method between same-texture write and read operations.
- Base vertex and base instance values are supported in the `OSX_GPUFamily1_v1` and `iOS_GPUFamily3_v1` feature sets with the [drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515561-drawprimitives) and [drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515520-drawindexedprimitives) methods. Similarly, support for these drawing inputs has been added to the Metal shading language by providing the new `[[ base_vertex ]]` and `[[ base_instance ]]` vertex shader inputs.
- Indirect drawing is supported in the `OSX_GPUFamily1_v1` and `iOS_GPUFamily3_v1` feature sets with the argument structures listed in Listing 10-8. Use these structs alongside the [drawPrimitives:indirectBuffer:indirectBufferOffset:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515467-drawprimitives) and [drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515392-drawindexedprimitives) methods, respectively.

  __Listing 10-8__  Indirect Drawing Argument Structures

```
// Without an index list
typedef struct {
    uint32_t vertexCount;
    uint32_t instanceCount;
    uint32_t vertexStart;
    uint32_t baseInstance;
} MTLDrawPrimitivesIndirectArguments;

// With an index list
typedef struct {
    uint32_t indexCount;
    uint32_t instanceCount;
    uint32_t indexStart;
    int32_t  baseVertex;
    uint32_t baseInstance;
} MTLDrawIndexedPrimitivesIndirectArguments;
```
- Shader constant updates can now be performed more efficiently by setting a vertex buffer once and then simply updating its offset inside your draw loop, as shown in Listing 10-9. If your app has a very small amount of constant data (tens of bytes) you can instead use the [setVertexBytes:length:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515846-setvertexbytes) method so the Metal framework can manage the constant buffer for you.

  __Listing 10-9__  Shader Constant Updates

```
id <MTLBuffer> constant_buffer = // initialize buffer
MyConstants* constant_ptr = constant_buffer.contents;
[renderpass setVertexBuffer:constant_buffer offset:0 atIndex:0];

for (i=0; i<draw_count; i++)
{
    constant_ptr[i] = // write constants directly into the buffer
    [renderpass setVertexBufferOffset:i*sizeof(MyConstants) atIndex:0];
    // draw
}
```


The `OSX_GPUFamily1_v1` feature set adds support for layered rendering with new APIs in the [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) and [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) classes. Layered rendering enables a vertex shader to render each primitive to a layer of a texture array, cube texture, or 3D texture, specified by the vertex shader of its first vertex. For a 2D texture array or a cube texture, each slice is layer; for a 3D texture, each depth plane of pixels is a layer. Load and store actions apply to every layer of the render target.

To enable layered rendering, you must configure your render pass and render pipeline descriptors appropriately:

1. Set the value of the [renderTargetArrayLength](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437975-rendertargetarraylength) property to specify the minimum number of layers available across all render targets. For example—set this value to `6` if you have a 2D texture array and a cube texture, each with a minimum of 6 layers.
2. Set the value of the [inputPrimitiveTopology](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514684-inputprimitivetopology) property to specify the primitive type being rendered. For example—set this value to [MTLPrimitiveTopologyClassTriangle](https://developer.apple.com/documentation/metal/mtlprimitivetopologyclass/mtlprimitivetopologyclasstriangle) for cube-based shadow mapping. The full enum declaration containing all primitive type values is listed in Listing 10-10
3. Additionally, the value of [sampleCount](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514699-samplecount) must be 1 (this is the default value).

__Listing 10-10__  Primitive Topology Values

```
typedef NS_ENUM(NSUInteger, MTLPrimitiveTopologyClass)
{
    MTLPrimitiveTopologyClassUnspecified = 0,
    MTLPrimitiveTopologyClassPoint = 1,
    MTLPrimitiveTopologyClassLine = 2,
    MTLPrimitiveTopologyClassTriangle = 3
};
```


There are also a few compute API additions to both existing and new classes, as summarized below:

- Indirect processing is supported in the `OSX_GPUFamily1_v1` and `iOS_GPUFamily3_v1` feature sets with the argument structure listed in Listing 10-11. Use this struct alongside the [dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443157-dispatchthreadgroups) method.

  __Listing 10-11__  Indirect Processing Argument Structures

```
typedef struct {
    uint32_t threadgroupsPerGrid[3];
} MTLDispatchThreadgroupsIndirectArguments;
```
- The new [MTLComputePipelineDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor) class specifies the compute configuration state used during a compute operation pass. This descriptor object is used to create a [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object. This new class is the compute counterpart to the previously-introduced [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) class.

Metal provides two new frameworks that help you build Metal apps in a much easier and more powerful way.

The MetalKit framework provides a set of utility functions and classes that reduce the effort required to create a Metal app. MetalKit provides development support for three key areas:

- Texture loading helps your app easily and asynchronously load textures from a variety of sources. Common file formats such as PNG and JPEG are supported, as well as texture-specific formats such as KTX and PVR.
- Model handling provides Metal-specific functionality that makes it easy to interface with Model I/O assets. Use these highly-optimized functions and objects to transfer data efficiently between Model I/O meshes and Metal buffers.
- View management provides a standard implementation of a Metal view that drastically reduces the amount of code needed to create a graphics-rendering app.

The MetalKit framework is available in all Metal feature sets. To learn more about the MetalKit APIs, see _[MetalKit Framework Reference](https://developer.apple.com/documentation/metalkit)_.

The Metal Performance Shaders framework provides highly-optimized compute and graphics shaders that are designed to integrate easily and efficiently into your Metal app.

Use the Metal Performance Shader classes to achieve optimal performance for all supported devices, without having to target or update your shader code for specific GPU families. Metal Performance Shader objects fit seamlessly into your Metal app and can be used with resource objects such as buffers and textures.

Common shaders provided by the Metal Performance Shader framework include:

- Gaussian blur.
- Image histogram.
- Sobel edge detection.

The Metal Performance Shaders framework is available in the `iOS_GPUFamily2_v1`, `iOS_GPUFamily2_v2`, and `iOS_GPUFamily3_v1` feature sets. To learn more about the Metal Performance Shaders APIs, see _[Metal Performance Shaders Framework Reference](https://developer.apple.com/documentation/metalperformanceshaders)_.

[Next](What%E2%80%99s%20New%20in%20iOS%2010%2C%20tvOS%2010%2C%20and%20macOS%2010.12.md)[Previous](Metal%20Feature%20Set%20Tables.md)

