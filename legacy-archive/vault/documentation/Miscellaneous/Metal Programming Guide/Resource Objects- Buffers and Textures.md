---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Mem-Obj/Mem-Obj.html
archived_at: '2026-07-15T08:16:51.240393Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Functions%20and%20Libraries.md)[Previous](Command%20Organization%20and%20Execution%20Model.md)

# Resource Objects: Buffers and Textures

This chapter describes Metal resource objects ([MTLResource](https://developer.apple.com/documentation/metal/mtlresource)) for storing unformatted memory and formatted image data. There are two types of [MTLResource](https://developer.apple.com/documentation/metal/mtlresource) objects:

- [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) represents an allocation of unformatted memory that can contain any type of data. Buffers are often used for vertex, shader, and compute state data.
- [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) represents an allocation of formatted image data with a specified texture type and pixel format. Texture objects are used as source textures for vertex, fragment, or compute functions, as well as to store graphics rendering output (that is, as an attachment).

[MTLSamplerState](https://developer.apple.com/documentation/metal/mtlsamplerstate) objects are also discussed in this chapter. Although samplers are not resources themselves, they are used when performing lookup calculations with a texture object.

A [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) object represents an allocation of memory that can contain any type of data.

The following [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) methods create and return a [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) object:

- The [newBufferWithLength:options:](https://developer.apple.com/documentation/metal/mtldevice/1433375-newbufferwithlength) method creates a `MTLBuffer` object with a new storage allocation.
- The [newBufferWithBytes:length:options:](https://developer.apple.com/documentation/metal/mtldevice/1433429-newbufferwithbytes) method creates a `MTLBuffer` object by copying data from existing storage (located at the CPU address `pointer`) into a new storage allocation.
- The [newBufferWithBytesNoCopy:length:options:deallocator:](https://developer.apple.com/documentation/metal/mtldevice/1433382-makebuffer) method creates a `MTLBuffer` object with an existing storage allocation and does not allocate any new storage for this object.

All buffer creation methods have the input value `length` to indicate the size of the storage allocation, in bytes. All the methods also accept a `MTLResourceOptions` object for `options` that can modify the behavior of the created buffer. If the value for `options` is 0, the default values are used for resource options.

The [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) protocol has the following methods:

- The [contents](https://developer.apple.com/documentation/metal/mtlbuffer/1515716-contents) method returns the CPU address of the buffer’s storage allocation.
- The [newTextureWithDescriptor:offset:bytesPerRow:](https://developer.apple.com/documentation/metal/mtlbuffer/1613852-newtexturewithdescriptor) method creates a special kind of texture object that references the buffer's data. This method is detailed in [Creating a Texture Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltcma).

A [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) object represents an allocation of formatted image data that can be used as a resource for a vertex shader, fragment shader, or compute function, or as an attachment to be used as a rendering destination. A `MTLTexture` object can have _one_ of the following structures:

- A 1D, 2D, or 3D image
- An array of 1D or 2D images
- A _cube_ of six 2D images

`MTLPixelFormat` specifies the organization of individual pixels in a `MTLTexture` object. Pixel formats are discussed further in [Pixel Formats for Textures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltcmq).

The following methods create and return a [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) object:

- The [newTextureWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1433425-maketexture) method of `MTLDevice` creates a `MTLTexture` object with a new storage allocation for the texture image data, using a [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor) object to describe the texture’s properties.
- The [newTextureViewWithPixelFormat:](https://developer.apple.com/documentation/metal/mtltexture/1515598-newtextureviewwithpixelformat) method of `MTLTexture` creates a `MTLTexture` object that shares the same storage allocation as the calling `MTLTexture` object. Since they share the same storage, any changes to the pixels of the new texture object are reflected in the calling texture object, and vice versa. For the newly created texture, the [newTextureViewWithPixelFormat:](https://developer.apple.com/documentation/metal/mtltexture/1515598-newtextureviewwithpixelformat) method reinterprets the existing texture image data of the storage allocation of the calling `MTLTexture` object as if the data was stored in the specified pixel format. The `MTLPixelFormat` of the new texture object must be _compatible_ with the `MTLPixelFormat` of the original texture object. (See [Pixel Formats for Textures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltcmq) for details about the ordinary, packed, and compressed pixel formats.)
- The [newTextureWithDescriptor:offset:bytesPerRow:](https://developer.apple.com/documentation/metal/mtlbuffer/1613852-newtexturewithdescriptor) method of `MTLBuffer` creates a `MTLTexture` object that shares the storage allocation of the calling `MTLBuffer` object as its texture image data. As they share the same storage, any changes to the pixels of the new texture object are reflected in the calling texture object, and vice versa. Sharing storage between a texture and a buffer can prevent the use of certain texturing optimizations, such as pixel swizzling or tiling.

[MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor) defines the properties that are used to create a [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) object, including its image size (width, height, and depth), pixel format, arrangement (array or cube type) and number of mipmaps. The `MTLTextureDescriptor` properties are only used during the creation of a `MTLTexture` object. After you create a `MTLTexture` object, property changes in its `MTLTextureDescriptor` object no longer have any effect on that texture.

To create one or more textures from a descriptor:

1. Create a custom [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor) object that contains texture properties that describe the texture data:

   - The [textureType](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516228-texturetype) property specifies a texture’s dimensionality and arrangement (for example, array or cube).
   - The [width](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515649-width), [height](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516000-height), and [depth](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516298-depth) properties specify the pixel size in each dimension of the base level texture mipmap.
   - The [pixelFormat](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515450-pixelformat) property specifies how a pixel is stored in a texture.
   - The [arrayLength](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515331-arraylength) property specifies the number of array elements for a [MTLTextureType1DArray](https://developer.apple.com/documentation/metal/mtltexturetype/type1darray) or [MTLTextureType2DArray](https://developer.apple.com/documentation/metal/mtltexturetype/type2darray) type texture object.
   - The [mipmapLevelCount](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516300-mipmaplevelcount) property specifies the number of mipmap levels.
   - The [sampleCount](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516260-samplecount) property specifies the number of samples in each pixel.
   - The [resourceOptions](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515776-resourceoptions) property specifies the behavior of its memory allocation.
2. Create a texture from the `MTLTextureDescriptor` object by calling the [newTextureWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1433425-maketexture) method of a `MTLDevice` object. After texture creation, call the [replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](https://developer.apple.com/documentation/metal/mtltexture/1515679-replaceregion) method to load the texture image data, as detailed in [Copying Image Data to and from a Texture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltcny).
3. To create more `MTLTexture` objects, you can reuse the same `MTLTextureDescriptor` object, modifying the descriptor’s property values as needed.

Listing 3-1 shows code for creating a texture descriptor `txDesc` and setting its properties for a 3D, 64x64x64 texture.

__Listing 3-1__  Creating a Texture Object with a Custom Texture Descriptor

```
MTLTextureDescriptor* txDesc = [[MTLTextureDescriptor alloc] init];
txDesc.textureType = MTLTextureType3D;
txDesc.height = 64;
txDesc.width = 64;
txDesc.depth = 64;
txDesc.pixelFormat = MTLPixelFormatBGRA8Unorm;
txDesc.arrayLength = 1;
txDesc.mipmapLevelCount = 1;
id <MTLTexture> aTexture = [device newTextureWithDescriptor:txDesc];
```


A _slice_ is a single 1D, 2D, or 3D texture image and all its associated mipmaps. For each slice:

- The size of the base level mipmap is specified by the [width](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515649-width), [height](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516000-height), and [depth](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516298-depth) properties of the `MTLTextureDescriptor` object.
- The scaled size of mipmap level _i_ is specified by max(1, floor(`width` / 2i)) x max(1, floor(`height` / 2i)) x max(1, floor(`depth` / 2i)). The maximum mipmap level is the first mipmap level where the size 1 x 1 x 1 is achieved.
- The number of mipmap levels in one slice can be determined by floor(log2(max(`width`, `height`, `depth`)))+1.

All texture objects have at least one slice; cube and array texture types may have several slices. In the methods that write and read texture image data that are discussed in [Copying Image Data to and from a Texture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltcny), `slice` is a zero-based input value. For a 1D, 2D, or 3D texture, there is only one slice, so the value of `slice` must be 0. A cube texture has six total 2D slices, addressed from 0 to 5. For the 1DArray and 2DArray texture types, each array element represents one slice. For example, for a 2DArray texture type with `arrayLength` = 10, there are 10 total slices, addressed from 0 to 9. To choose a single 1D, 2D, or 3D image out of an overall texture structure, first select a slice, and then select a mipmap level within that slice.

For common 2D and cube textures, use the following convenience methods to create a `MTLTextureDescriptor` object with several of its property values automatically set:

- The [texture2DDescriptorWithPixelFormat:width:height:mipmapped:](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515511-texture2ddescriptor) method creates a `MTLTextureDescriptor` object for a 2D texture. The `width` and `height` values define the dimensions of the 2D texture. The `type` property is automatically set to `MTLTextureType2D`, and `depth` and `arrayLength` are set to 1.
- The [textureCubeDescriptorWithPixelFormat:size:mipmapped:](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516090-texturecubedescriptor) method creates a `MTLTextureDescriptor` object for a cube texture, where the `type` property is set to `MTLTextureTypeCube`, `width` and `height` are set to size, and `depth` and `arrayLength` are set to 1.

Both `MTLTextureDescriptor` convenience methods accept an input value, `pixelFormat`, which defines the pixel format of the texture. Both methods also accept the input value `mipmapped`, which determines whether or not the texture image is mipmapped. (If `mipmapped` is `YES`, the texture is mipmapped.)

Listing 3-2 uses the `texture2DDescriptorWithPixelFormat:width:height:mipmapped:` method to create a descriptor object for a `64x64` 2D texture that is not mipmapped.

__Listing 3-2__  Creating a Texture Object with a Convenience Texture Descriptor

```
MTLTextureDescriptor *texDesc = [MTLTextureDescriptor           texture2DDescriptorWithPixelFormat:MTLPixelFormatBGRA8Unorm           width:64 height:64 mipmapped:NO]; id <MTLTexture> myTexture = [device newTextureWithDescriptor:texDesc];
```


To synchronously copy image data into or copy data from the storage allocation of a `MTLTexture` object, use the following methods:

- [replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](https://developer.apple.com/documentation/metal/mtltexture/1515679-replaceregion) copies a region of pixel data from the caller's pointer into a portion of the storage allocation of a specified texture slice. [replaceRegion:mipmapLevel:withBytes:bytesPerRow:](https://developer.apple.com/documentation/metal/mtltexture/1515464-replaceregion) is a similar convenience method that copies a region of pixel data into the default slice, assuming default values for slice-related arguments (i.e., `slice` = 0 and `bytesPerImage` = 0).
- [getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:](https://developer.apple.com/documentation/metal/mtltexture/1516318-getbytes) retrieves a region of pixel data from a specified texture slice. [getBytes:bytesPerRow:fromRegion:mipmapLevel:](https://developer.apple.com/documentation/metal/mtltexture/1515751-getbytes) is a similar convenience method that retrieves a region of pixel data from the default slice, assuming default values for slice-related arguments (`slice` = 0 and `bytesPerImage` = 0).

Listing 3-3 shows how to call [replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:](https://developer.apple.com/documentation/metal/mtltexture/1515679-replaceregion) to specify a texture image from source data in system memory, `textureData`, at slice `0` and mipmap level `0`.

__Listing 3-3__  Copying Image Data into the Texture

```
//  pixelSize is the size of one pixel, in bytes
//  width, height - number of pixels in each dimension
NSUInteger myRowBytes = width * pixelSize;
NSUInteger myImageBytes = rowBytes * height;
[tex replaceRegion:MTLRegionMake2D(0,0,width,height)
    mipmapLevel:0 slice:0 withBytes:textureData
    bytesPerRow:myRowBytes bytesPerImage:myImageBytes];
```


`MTLPixelFormat` specifies the organization of color, depth, and stencil data storage in individual pixels of a `MTLTexture` object. There are three varieties of pixel formats: ordinary, packed, and compressed.

- Ordinary formats have only regular 8-, 16-, or 32-bit color components. Each component is arranged in increasing memory addresses with the first listed component at the lowest address. For example, [MTLPixelFormatRGBA8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba8unorm) is a 32-bit format with eight bits for each color component; the lowest addresses contains red, the next addresses contain green, and so on. In contrast, for [MTLPixelFormatBGRA8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra8unorm), the lowest addresses contains blue, the next addresses contain green, and so on.
- Packed formats combine multiple components into one 16-bit or 32-bit value, where the components are stored from the least to most significant bit (LSB to MSB). For example, [MTLPixelFormatRGB10A2Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb10a2uint) is a 32-bit packed format that consists of three 10-bit channels (for R, G, and B) and two bits for alpha.
- Compressed formats are arranged in blocks of pixels, and the layout of each block is specific to that pixel format. Compressed pixel formats can only be used for 2D, 2D Array, or cube texture types. Compressed formats cannot be used to create 1D, 2DMultisample or 3D textures.

The [MTLPixelFormatGBGR422](https://developer.apple.com/documentation/metal/mtlpixelformat/gbgr422) and [MTLPixelFormatBGRG422](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgrg422) are special pixel formats that are intended to store pixels in the YUV color space. These formats are only supported for 2D textures (but neither 2D Array, nor cube type), without mipmaps, and an even `width`.

Several pixel formats store color components with sRGB color space values (for example, [MTLPixelFormatRGBA8Unorm_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba8unorm_srgb) or [MTLPixelFormatETC2_RGB8_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatetc2_rgb8_srgb)). When a sampling operation references a texture with an sRGB pixel format, the Metal implementation converts the sRGB color space components to a linear color space before the sampling operation takes place. The conversion from an sRGB component, S, to a linear component, L, is as follows:

- If S <= 0.04045, L = S/12.92
- If S > 0.04045, L = ((S+0.055)/1.055)2.4

Conversely, when rendering to a color-renderable attachment that uses a texture with an sRGB pixel format, the implementation converts the linear color values to sRGB, as follows:

- If L <= 0.0031308, S = L \* 12.92
- If L > 0.0031308, S = (1.055 \* L0.41667) - 0.055

For more information about pixel format for rendering, see [Creating a Render Pass Descriptor](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltk).

A [MTLSamplerState](https://developer.apple.com/documentation/metal/mtlsamplerstate) object defines the addressing, filtering, and other properties that are used when a graphics or compute function performs texture sampling operations on a `MTLTexture` object. A sampler descriptor defines the properties of a sampler state object. To create a sampler state object:

1. Call the [newSamplerStateWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1433408-makesamplerstate) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object to create a [MTLSamplerDescriptor](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor) object.
2. Set the desired values in the `MTLSamplerDescriptor` object, including filtering options, addressing modes, maximum anisotropy, and level-of-detail parameters.
3. Create a [MTLSamplerState](https://developer.apple.com/documentation/metal/mtlsamplerstate) object from the sampler descriptor by calling the [newSamplerStateWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1433408-makesamplerstate) method of the `MTLDevice` object that created the descriptor.

You can reuse the sampler descriptor object to create more `MTLSamplerState` objects, modifying the descriptor’s property values as needed. The descriptor's properties are only used during object creation. After a sampler state has been created, changing the properties in its descriptor no longer has an effect on that sampler state.

Listing 3-4 is a code example that creates a `MTLSamplerDescriptor` and configures it in order to create a [MTLSamplerState](https://developer.apple.com/documentation/metal/mtlsamplerstate). Non-default values are set for filter and address mode properties of the descriptor object. Then the [newSamplerStateWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1433408-makesamplerstate) method uses the sampler descriptor to create a sampler state object.

__Listing 3-4__  Creating a Sampler State Object

```
// create MTLSamplerDescriptor
MTLSamplerDescriptor *desc = [[MTLSamplerDescriptor alloc] init];
desc.minFilter = MTLSamplerMinMagFilterLinear;
desc.magFilter = MTLSamplerMinMagFilterLinear;
desc.sAddressMode = MTLSamplerAddressModeRepeat;
desc.tAddressMode = MTLSamplerAddressModeRepeat;
//  all properties below have default values
desc.mipFilter        = MTLSamplerMipFilterNotMipmapped;
desc.maxAnisotropy    = 1U;
desc.normalizedCoords = YES;
desc.lodMinClamp      = 0.0f;
desc.lodMaxClamp      = FLT_MAX;
// create MTLSamplerState
id <MTLSamplerState> sampler = [device newSamplerStateWithDescriptor:desc];
```


Both the CPU and GPU can access the underlying storage for a [MTLResource](https://developer.apple.com/documentation/metal/mtlresource) object. However, the GPU operates asynchronously from the host CPU, so keep the following in mind when using the host CPU to access the storage for these resources.

When executing a [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object, the [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object is only guaranteed to observe any changes made by the host CPU to the storage allocation of any `MTLResource` object referenced by that `MTLCommandBuffer` object if (and only if) those changes were made by the host CPU before the `MTLCommandBuffer` object was committed. That is, the `MTLDevice` object might not observe changes to the resource that the host CPU makes after the corresponding `MTLCommandBuffer` object was committed (i.e., the [status](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443048-status) property of the `MTLCommandBuffer` object is [MTLCommandBufferStatusCommitted](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/mtlcommandbufferstatuscommitted)).

Similarly, after the `MTLDevice` object executes a `MTLCommandBuffer` object, the host CPU is only guaranteed to observe any changes the `MTLDevice` object makes to the storage allocation of any resource referenced by that command buffer if the command buffer has completed execution (that is, the `status` property of the `MTLCommandBuffer` object is [MTLCommandBufferStatusCompleted](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/completed)).

[Next](Functions%20and%20Libraries.md)[Previous](Command%20Organization%20and%20Execution%20Model.md)

