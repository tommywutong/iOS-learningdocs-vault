---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/WhatsNewiniOS10tvOS10andOSX1012/WhatsNewiniOS10tvOS10andOSX1012.html
archived_at: '2026-07-15T08:16:57.023400Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Tessellation.md)[Previous](What%27s%20New%20in%20iOS%209%20and%20OS%20X%2010.11.md)

# What’s New in iOS 10, tvOS 10, and macOS 10.12

This chapter summarizes the new features introduced in iOS 10, tvOS 10, and macOS 10.12.

The new Metal feature sets are listed as follows:

- [MTLFeatureSet_iOS_GPUFamily1_v3](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily1_v3)
- [MTLFeatureSet_iOS_GPUFamily2_v3](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily2_v3)
- [MTLFeatureSet_iOS_GPUFamily3_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily3_v2)
- [MTLFeatureSet_tvOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v2)
- `MTLFeatureSet_OSX_GPUFamily1_v2`
- `MTLFeatureSet_OSX_ReadWriteTextureTier2`

To determine whether a feature set is supported by a device, query the existing [supportsFeatureSet:](https://developer.apple.com/documentation/metal/mtldevice/1433418-supportsfeatureset) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object.

Each new feature described in this chapter is annotated with its feature set availability. For further information about feature availability, implementation limits, and pixel format capabilities for all feature sets, see the [Metal Feature Set Tables](https://developer.apple.com/metal/feature-sets/) page.

All new Metal shading language features are available in version 1.2 ([MTLLanguageVersion1_2](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_2)). For further information, see the _Metal Shading Language Guide_.

For a complete overview of tessellation in Metal, see the [Tessellation](Tessellation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjvfvjvomi) chapter.

For a complete overview of resource heaps in Metal, see the [Resource Heaps](Resource%20Heaps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjwfvjvomi) chapter.

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`

Memoryless render targets are render targets that exist only transiently in on-GPU tile memory, without any other CPU or GPU memory backing. Memoryless render targets satisfy the increased memory demands of high-resolution displays and MSAA data, allowing you to:

- Prevent wasting memory that is only needed for temporary render targets (color, depth, and stencil).
- Increase image quality by using higher MSAA levels in the same memory budget.

To create a memoryless render target, set the [storageMode](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516262-storagemode) property of a [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor) object to [MTLStorageModeMemoryless](https://developer.apple.com/documentation/metal/mtlstoragemode/memoryless). Then, use this descriptor to create a [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) object.

Only [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) objects can be created with a [MTLStorageModeMemoryless](https://developer.apple.com/documentation/metal/mtlstoragemode/memoryless) storage mode. A memoryless render target can only be used by a temporary render target; to do so, set it as the [texture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437958-texture) property of a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object.

The following use cases are just a few examples of temporary render targets that can be used as memoryless render targets. For each of these, the contents of the render targets are never used after the rendering operations are completed:

- Traditional depth testing, using a depth render target with a [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) store action.
- Traditional stencil buffer operations, using a stencil render target with a [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) store action.
- MSAA rendering, using a MSAA color render target with a [MTLStoreActionMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve) store action.
- Deferred rendering, using two logical rendering passes within a single render command encoder:

  1. The first pass populates the temporary G-buffer render targets with albedo, normal, and other data.
  2. The second pass reads the temporary G-buffer render targets, then computes and accumulates lighting data to output the final color to a persistent render target.

  Each temporary render target is a memoryless render target and has a [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) store action.
- Deferred lighting, using three logical rendering passes within a single render command encoder:

  1. The first pass populates the temporary depth and normal render targets with geometry data.
  2. The second pass reads the previous temporary render targets, then computes and accumulates lighting data to populate the temporary diffuse and specular render targets.
  3. The third pass reads all previous temporary render targets, then computes the lighting equation to output the final color to a persistent render target.

  Each temporary render target is a memoryless render target and has a [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) store action.

Memoryless render targets must adhere to the following rules and restrictions. Memoryless render targets...

- Can be part of a heap, but they cannot be aliased. For further information, see the [Resource Heaps](Resource%20Heaps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjwfvjvomi) chapter.
- Must have a renderable color, depth, or stencil pixel format.
- Can only be populated by a rendering pass.
- Must have a [MTLTextureType2D](https://developer.apple.com/documentation/metal/mtltexturetype/type2d) or [MTLTextureType2DMultisample](https://developer.apple.com/documentation/metal/mtltexturetype/mtltexturetype2dmultisample) texture type.
- Can only be used for the [texture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437958-texture) property of a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object.
- Cannot be used for the [resolveTexture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437926-resolvetexture) property of a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object.
- Must be used by a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object with a [MTLLoadActionDontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare) or [MTLLoadActionClear](https://developer.apple.com/documentation/metal/mtlloadaction/clear) load action.
- Must be used by a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object with a [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) or [MTLStoreActionMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve) store action. The [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object can also have an initial [MTLStoreActionUnknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown) store action, but this must be changed before its associated render command encoder ends encoding. For further information, see the [Deferred Store Action](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjufvjvomjq) section.
- Cannot be read from or written to by any methods in the [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) protocol.
- Cannot be used as a parent texture to create a texture view.
- Cannot be used by a [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) object. All blit operations are disallowed.
- Cannot be used by a [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) object. All compute operations are disallowed.
- Can be read by a fragment function using a framebuffer fetch. For further information, see the Programmable Blending section of the _Metal Shading Language Guide_.

Apps using memoryless render targets should carefully control the total amount of data passed for processing in a single rendering pass. Memoryless render targets use on-GPU tile memory for their temporary storage; as long as all data associated with the draw calls issued for a rendering pass can be cached, memoryless render targets will be processed one tile at a time. To ensure successful usage of memoryless render targets, make sure you follow these additional rules:

- All resources referenced in the rendering pass shouldn’t consume more physical memory than available.
- You should not submit more than 64K unique viewports, scissors, and depth-bias values.

The command buffer will report any memory errors via the [MTLCommandBufferErrorMemoryless](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrormemoryless) error code.

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`, `OSX_GPUFamily1_v2`

Function specialization uses function constants to create specialized versions of your graphics and compute functions. Function constants are compile-time constants declared in your Metal shading language source; function constant values are assigned in your Metal app before the specialized function is compiled.

The Metal shading language provides the `[[ function_constant(index) ]]` attribute to declare function constants, as shown in Listing 11-1.

__Listing 11-1__  Declaring a function constant

```
constant bool a [[ function_constant(0) ]];
```

Function constants can be used to:

- Control which function code paths get compiled
- Specify optional arguments of a function
- Specify optional elements of a struct declared with the `[[ stage_in ]]` qualifier

The Metal framework provides the [MTLFunctionConstantValues](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues) class to set the constant values for a specialized function. Constant values can be set by index, index range, or name. Listing 11-2 shows how to set a constant value by index.

__Listing 11-2__  Setting a constant value by index

```
const bool a = true;
MTLFunctionConstantValues* constantValues = [MTLFunctionConstantValues new];
[constantValues setConstantValue:&a type:MTLDataTypeBool atIndex:0];
```

A single [MTLFunctionConstantValues](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues) object can be applied to multiple [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) objects (for example, a vertex function and a fragment function). After a specialized function has been created, any changes to its constant values have no further effect on it. However, you can reset, add, or modify any constant values in the [MTLFunctionConstantValues](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues) object and reuse it to create another [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object.

Specialized functions are [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) objects created from a [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) object by calling one of these methods:

- [newFunctionWithName:constantValues:completionHandler:](https://developer.apple.com/documentation/metal/mtllibrary/1640053-makefunction)
- [newFunctionWithName:constantValues:error:](https://developer.apple.com/documentation/metal/mtllibrary/1640020-newfunctionwithname)

These methods invoke the Metal compiler to evaluate your function constants and their constant values. The compiler specializes the named function by omitting function constant code paths, arguments, and elements that are not enabled by the constant values provided. Function constant values are first looked up by their index, then by their name. Any values that do not correspond to a function constant in the named function are ignored (without generating errors or warnings).

A [MTLFunctionConstant](https://developer.apple.com/documentation/metal/mtlfunctionconstant) object provides reflection data for function constants. This object should only be obtained if you need the reflection data to set constant values for a specialized function (for example, determining if a function constant is optional or required before setting its constant value). To obtain reflection data, fetch a [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object by calling the [newFunctionWithName:](https://developer.apple.com/documentation/metal/mtllibrary/1515524-newfunctionwithname) method and querying the `functionConstants` property. Use this reflection data to set your constant values and compile your specialized function.

__Available in:__ `iOS_GPUFamily3_v2`, `OSX_GPUFamily1_v2`

Fragment functions can now write to buffers. Writable buffers must be declared in the `device` address space and must not be `const`. Use dynamic indexing to write to a buffer.

Vertex and fragment functions now support atomic functions for buffers (in the `device` address space). For further information, see the Atomic Functions section of the _Metal Shading Language Guide_.

__Available in:__ `OSX_GPUFamily1_v2`

Both vertex and fragment functions can now write to textures. Writable textures must be declared with the `access::write` or `access::read_write` qualifier. Use an appropriate variant of the `write()` function to write to a texture (where `lod` is always constant and equal to zero).

A read-write texture is a texture that can be both read from and written to by the same vertex, fragment, or kernel function.

A read-write texture is declared in the Metal shading language as a texture with the `access::read_write` qualifier. Listing 11-3 shows a simple read and write operation on a read-write texture, within the same function.

__Listing 11-3__  Using a read-write texture

```
kernel void my_kernel(texture2d<float, access::read_write> texA [[ texture(0) ]],
                      ushort2 gid [[ thread_position_in_grid ]])
{
    float4 color = texA.read(gid);
    color = processColor(color);
    texA.write(color, gid);
}
```

To set a read-write texture in the graphics or compute function argument table, use one of the existing methods in the Metal framework API:

- [setVertexTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515842-setvertextexture)
- [setFragmentTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515390-setfragmenttexture)
- [setTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443130-settexture)

__Listing 11-4__  Setting a read-write texture (Metal Shading Language)

```
// kernel function signature
kernel void my_kernel(texture2d<float, access::read_write> texA [[ texture(0) ]], ...)
```


__Listing 11-5__  Setting a read-write texture (Metal Framework)

```
// kernel function argument table
[computeCommandEncoder setTexture:texA atIndex:0];
```


The `fence()` function allows you to control the order of a texture’s write and read operations within a thread, as shown in Listing 11-8. The `fence()` function ensures that writes to the texture by a thread become visible to subsequent reads from that texture by the same thread.

__Listing 11-8__  Using a read-write texture with a fence

```
kernel void my_kernel(texture2d<float, access::read_write> texA [[texture(0)]],
                      ushort2 gid [[ thread_position_in_grid ]])
{
    float4 color = generateColor();
    texA.write(color, gid);

    // add a fence to ensure the correct ordering of write and read operations within the thread
    texA.fence();

    float4 readColor = texA.read(gid);
}
```


The set of pixel formats supported by read-write textures is separated into two tiers, each defined by a specific feature set.

__Available in:__ `OSX_GPUFamily1_v2`

- `R32Float`
- `R32Uint`
- `R32Sint`

__Available in:__ `OSX_ReadWriteTextureTier2`

- `RGBA32Float`
- `RGBA32Uint`
- `RGBA32Sint`
- `RGBA16Float`
- `RGBA16Uint`
- `RGBA16Sint`
- `RGBA8Unorm`
- `RGBA8Uint`
- `RGBA8Sint`
- `R16Float`
- `R16Uint`
- `R16Sint`
- `R8Unorm`
- `R8Uint`
- `R8Sint`

__Between Command Encoders__

All resource writes performed in a given command encoder are visible in the next command encoder. This is true for both render and compute command encoders.

__Within a Render Command Encoder__

For buffers, atomic writes are visible to subsequent atomic reads across multiple threads.

For textures, the [textureBarrier](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515866-texturebarrier) method ensures that writes performed in a given draw call are visible to subsequent reads in the next draw call.

__Within a Compute Command Encoder__

All resource writes performed in a given kernel function are visible in the next kernel function.

__Discard__

If the `discard_fragment()` function is called, all resource writes that occurred before the call are actually committed to memory. After the call, the execution of the fragment function either stops entirely or continues, but future resource writes are completely ignored.

__Scissor Test__

The scissor test is always performed before executing the fragment function. If the scissor test fails, the fragment function is not executed and no resource writes take place.

__Early and Late Fragment Tests__

The `[[early_fragment_tests]]` qualifier can be added to a fragment function to request that depth, stencil, and occlusion query tests be performed before executing the fragment function. If any of the tests fail, the fragment function is not executed and no resource writes take place.

If the `[[early_fragment_tests]]` qualifier is not added, all fragment function resource writes are committed to memory whether the tests pass or not.

__MSAA__

The number of times a resource write operation is executed depends on how many times the fragment function is executed. By default, the fragment function is executed between 1 and `N` times, where `N` is the number of samples covered by the fragment. However, if the fragment function uses inputs with the `color`, `sample_id`, `sample_perspective`, or `sample_no_perspective` qualifiers, it is always executed at the sample rate.

If the fragment function result is discarded due to either setting a coverage mask of `0` or returning a low alpha value when the [alphaToCoverageEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514624-alphatocoverageenabled) property is set to `YES`, then all fragment function resource writes are still committed to memory.

__Helper Threads__

Helper threads are fragment function invocations for pixels near primitive edges that produce no output, typically used to calculate derivatives. Resource writes performed by helper threads are ignored; atomics will not update memory and the values returned by atomics will be undefined.

For further information, see the Fragment Functions section of the _Metal Shading Language Guide_.

__Available in:__ `iOS_GPUFamily3_v2`

An array of textures is a data structure for storing homogeneous textures, allowing you to dynamically index into a texture with ease. An array of textures is declared in the Metal shading language as either:

- `array<typename T, size_t N>`, or
- `const array<typename T, size_t N>`

`T` is a texture type declared with the `access::read` or `access::sample` qualifier and `N` is the number of textures in the array.

An array of textures can be passed as an argument to graphics, compute, or user functions, or it can be declared as a local variable inside functions. Listing 11-9 shows how to pass an array of 10 textures as an argument to a kernel function.

__Listing 11-9__  Passing an array of textures as an argument to a function

```
kernel void my_kernel(
    const array<texture2d<float>, 10> src [[ texture(0) ]],
    texture2d<float, access::write> dst [[ texture(10) ]])
```

There is no new Metal framework API to set an array of textures; use the existing methods in the [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) protocol or [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder) protocol.

The Metal shading language also adds support for a reference to an immutable array of textures, declared as `array_ref<T>` where `T` is a texture type and `size()` provides the number of textures in the array.

The storage for an array of textures is not owned by an `array_ref<T>` object. Implicit conversion operations are provided from types with contiguous iterators like `metal::array`. The `array_ref<T>` type can be passed as an argument to user functions only. A common use for the `array_ref<T>` type is when passing an array of textures as an argument to functions where you want to be able to accept a variety of array types, as shown in Listing 11-10.

__Listing 11-10__  Passing an `array_ref<T>` type as an argument to a function

```
float4 foo(array_ref<texture2d<float>> src)
{
    float4 clr(0.0f);
    for(int i=0; i<src.size(); i++)
    {
        clr += process_texture(src[i]);
    }
    return clr;
}

kernel void my_kernel_A(
    const array<texture2d<float>, 10> srcA [[ texture(0) ]],
    texture2d<float, access::write> dstB [[ texture(10) ]])
{
    float4 clrA = foo(srcA);
    /* ... */
}

kernel void my_kernel_B(
    const array<texture2d<float>, 20> srcB [[ texture(0) ]],
    texture2d<float, access::write> dstB [[ texture(20) ]])
{
    float4 clrB = foo(srcB);
    /* ... */
}
```


__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`, `OSX_GPUFamily1_v2`

[MTLPixelFormatX32_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/x32_stencil8) and [MTLPixelFormatX24_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatx24_stencil8) are new stencil pixel formats that allow you to easily access stencil texture data in a graphics or compute function by using a stencil texture view.

A stencil texture view allows you to create a stencil-only texture from a combined depth and stencil texture. Both textures can then be set as texture arguments and sampled separately in a graphics or compute function. The stencil-only texture returns 8-bit unsigned integer values for each pixel. The format of the depth and stencil parent texture dictates the format of the stencil texture view, as listed in Table 11-1.

__Table 11-1__  Pixel format compatibility for stencil texture views

| Depth and stencil parent texture format | Stencil texture view format |
| [MTLPixelFormatDepth32Float_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatdepth32float_stencil8) | [MTLPixelFormatX32_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/x32_stencil8) |
| [MTLPixelFormatDepth24Unorm_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/depth24unorm_stencil8)\* | [MTLPixelFormatX24_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatx24_stencil8)\* |

\*These pixel formats are only supported in certain devices; query the [depth24Stencil8PixelFormatSupported](https://developer.apple.com/documentation/metal/mtldevice/1433371-depth24stencil8pixelformatsuppor) property of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object to check for support.

A stencil texture view can be created by using the existing Metal framework API in the [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) protocol, as shown in Listing 11-11.

__Listing 11-11__  Creating a stencil texture view

```
// Create a combined depth and stencil texture
MTLTextureDescriptor *depthStencilDescriptor = [MTLTextureDescriptor new];
depthStencilDescriptor.textureType = MTLTextureType2D;
depthStencilDescriptor.pixelFormat = MTLPixelFormatDepth32Float_Stencil8;
depthStencilDescriptor.width = 32;
depthStencilDescriptor.height = 32;
depthStencilDescriptor.usage = (MTLTextureUsageShaderRead | MTLTextureUsagePixelFormatView);

id<MTLTexture> depthStencilTexture = [device newTextureWithDescriptor:depthStencilDescriptor];
/* Initialize the combined depth and stencil texture data */

// Create a stencil texture view
id<MTLTexture> stencilTextureView = [depthStencilTexture newTextureViewWithPixelFormat:MTLPixelFormatX32_Stencil8];
```


__Available in:__ `OSX_GPUFamily1_v2`

[MTLPixelFormatDepth16Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/depth16unorm) is a new 16-bit depth pixel format with one normalized unsigned integer component.

__Available in:__ `iOS_GPUFamily3_v2`

Table 11-2 lists the new extended range pixel formats. These pixel formats are intended to be used as displayable render targets for devices with a wide gamut display.

__Table 11-2__  Extended range pixel formats

| Pixel format | Bits per pixel (bpp) | Bits per component (bpc) | Encoding | Range |
| [MTLPixelFormatBGRA10_XR](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr) | 64 | 10 | Linear | [-0.752941, 1.25098]\* |
| [MTLPixelFormatBGRA10_XR_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr_srgb) | 64 | 10 | Gamma | [-0.527100, 1.66894]\*  (before gamma expansion) |
| [MTLPixelFormatBGR10_XR](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgr10_xr) | 32 | 10 | Linear | [-0.752941, 1.25098] |
| [MTLPixelFormatBGR10_XR_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr_srgb) | 32 | 10 | Gamma | [-0.527100, 1.66894]  (before gamma expansion) |

\*The alpha component of the [MTLPixelFormatBGRA10_XR](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr) and [MTLPixelFormatBGRA10_XR_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr_srgb) pixel formats is always clamped to the `[0.0, 1.0]` range on sampling, rendering, and writing (despite supporting values outside this range).

All extended range formats are color-renderable and can be set in the [pixelFormat](https://developer.apple.com/documentation/quartzcore/cametallayer/1478155-pixelformat) property of a [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer) object or the [colorPixelFormat](https://developer.apple.com/documentation/metalkit/mtkview/1535940-colorpixelformat) property of a [MTKView](https://developer.apple.com/documentation/metalkit/mtkview) object. Only devices with a wide gamut display will display values outside the `[0.0, 1.0]` range; all other devices will clamp values to the `[0.0, 1.0]` range.

__Available in:__ `iOS_GPUFamily3_v2`, `OSX_GPUFamily1_v2`

The [MTLStoreActionStoreAndMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve) store action allows you to store and resolve MSAA data using a single render command encoder. The unresolved MSAA data is stored in the texture specified by the [texture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437958-texture) property and the resolved MSAA data is stored in the texture specified by the [resolveTexture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437926-resolvetexture) property, as shown in Listing 11-12

__Listing 11-12__  Performing a combined MSAA store and resolve operation using a single render command encoder

```
// Create MSAA texture
// This texture is used to store the unresolved MSAA data
MTLTextureDescriptor *msaaTextureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm width:_width height:_height mipmapped:NO];
msaaTextureDescriptor.textureType = MTLTextureType2DMultisample;
msaaTextureDescriptor.sampleCount = _sampleCount; // must be > 1

id <MTLTexture> msaaTexture = [_device newTextureWithDescriptor:msaaTextureDescriptor];

// Create resolve texture
// This texture is used to store the resolved MSAA data
MTLTextureDescriptor *colorTextureDescriptor = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm width:_width height:_height mipmapped:NO];

id <MTLTexture> colorTexture = [_device newTextureWithDescriptor:colorTextureDescriptor];

// Create descriptor for store and resolve rendering pass
MTLRenderPassDescriptor *renderPassDescriptor = [MTLRenderPassDescriptor renderPassDescriptor];
renderPassDescriptor.colorAttachments[0].texture = msaaTexture;
renderPassDescriptor.colorAttachments[0].resolveTexture = colorTexture;
renderPassDescriptor.colorAttachments[0].loadAction = MTLLoadActionDontCare;
renderPassDescriptor.colorAttachments[0].storeAction = MTLStoreActionStoreAndMultisampleResolve;

// Create command buffer and render command encoder
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];
id <MTLRenderCommandEncoder> renderCommandEncoder = [commandBuffer renderCommandEncoderWithDescriptor:renderPassDescriptor];
/* Encode rendering pass commands */

// End encoding and commit command buffer
[renderCommandEncoder endEncoding];
[commandBuffer commit];
```


__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`, `OSX_GPUFamily1_v2`

The [MTLStoreActionUnknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown) store action allows you to defer specifying a store action when configuring a [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor) object. The store action must be specified after the render command encoder is created but before you call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method, as shown in Listing 11-13. Call one of the following methods on a [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) object to specify a store action other than [MTLStoreActionUnknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown):

- [setColorStoreAction:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640054-setcolorstoreaction)
- [setDepthStoreAction:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640036-setdepthstoreaction)
- [setStencilStoreAction:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639936-setstencilstoreaction)

Equivalent methods are provided for a [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder) object, which you may only call on the parent encoder and must not call on any child encoders.

__Listing 11-13__  Deferring the decision of specifying a store action

```
// Create descriptor with an unknown store action
MTLRenderPassDescriptor *renderPassDescriptor = [MTLRenderPassDescriptor renderPassDescriptor];
renderPassDescriptor.colorAttachments[0].texture = colorTexture;
renderPassDescriptor.colorAttachments[0].loadAction = MTLLoadActionDontCare;
renderPassDescriptor.colorAttachments[0].storeAction = MTLStoreActionUnknown;

// Create command buffer and render command encoder
id <MTLCommandBuffer> commandBuffer = [_commandQueue commandBuffer];
id <MTLRenderCommandEncoder> renderCommandEncoder = [commandBuffer renderCommandEncoderWithDescriptor:renderPassDescriptor];
/* Encode rendering pass commands */

// Specify a known store action
[renderCommandEncoder setColorStoreAction:MTLStoreActionStore atIndex:0];

// End encoding and commit command buffer
[renderCommandEncoder endEncoding];
[commandBuffer commit];
```

A render command encoder created with a [MTLStoreActionUnknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown) store action can have its store action changed as many times as desired before a call to the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method. A render command encoder created with a non-[MTLStoreActionUnknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown) store action cannot have its store action changed after creation.

__Available in:__ `OSX_GPUFamily1_v2`

Dual-source blending allows a fragment function to output two source colors, `Source0` and `Source1`, into the GPU’s blend unit for a single render target.

To produce two output colors, `Source0` and `Source1`, the Metal Shading Language extends the `color(m)` attribute qualifier with an `index(i)` attribute qualifier, where:

- `m` is the color attachment index.
- `i` is the color output index.

__Listing 11-14__  Enabling dual-source blending in a fragment function

```
struct DualSourceOutput
{
    half4 Source0 [[ color(0), index(0) ]];
    half4 Source1 [[ color(0), index(1) ]];
};

fragment DualSourceOutput dual_source_fragment(constant float4* color0 [[ buffer(0) ]],
                                               constant float4* color1 [[ buffer(1) ]])
{
    DualSourceOutput dso;
    dso.Source0 = half4(color0[0]);
    dso.Source1 = half4(color1[0]);
    return dso;
}
```


The second output color, `Source1`, is referenced as a source or destination blend factor in the following fixed-function blending equations:

`Output.rgb = (Source0.rgb * SBF) {BO} (Destination.rgb * DBF)`

`Output.a = (Source0.a * SBF) {BO} (Destination.a * DBF)`

Where `BO` is a [MTLBlendOperation](https://developer.apple.com/documentation/metal/mtlblendoperation) operator, `SBF` is the source blend factor, `DBF` is the destination blend factor, and `Source1` can be referenced as one of the following [MTLBlendFactor](https://developer.apple.com/documentation/metal/mtlblendfactor) enums:

__Table 11-3__  `Source1` blend factors

| MTLBlendFactor | RGB blend factor values | Alpha blend factor value |
| `Source1Color` | R,G,B from `Source1` | A from `Source1` |
| `OneMinusSource1Color` | 1-R,1-G,1-B from `Source1` | 1-A from `Source1` |
| `Source1Alpha` | A,A,A from `Source1` | A from `Source1` |
| `OneMinusSource1Alpha` | 1-A,1-A,1-A from `Source1` | 1-A from `Source1` |

For example, Listing 11-15 shows the render pipeline configuration that yields the following dual-source blend equation:

`Output.rgb = (Source0.rgb * 1) + (Destination.rgb * Source1.rgb)`

__Listing 11-15__  Configuring dual-source blending in a render pipeline descriptor

```
MTLRenderPipelineDescriptor *rpd = [[MTLRenderPipelineDescriptor alloc] init];
rpd.label = @"DualSourcePipeline";
rpd.fragmentFunction = [_defaultLibrary newFunctionWithName:@"dual_source_fragment"];
rpd.colorAttachments[0].blendingEnabled = YES;
rpd.colorAttachments[0].rgbBlendOperation = MTLBlendOperationAdd;
rpd.colorAttachments[0].sourceRGBBlendFactor = MTLBlendFactorOne;
rpd.colorAttachments[0].destinationRGBBlendFactor = MTLBlendFactorSource1Color;
```


Dual-source blending configurations must adhere to the following rules and restrictions:

- Dual-source blending is not compatible with multiple render targets.
- Fragment functions can only output to `color(0)`.
- `index(0)` always refers to `Source0` and `index(1)` always refers to `Source1`.
- `Source1` blend factors can only be set on `colorAttachments[0]`.

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`, `OSX_GPUFamily1_v1`, `OSX_GPUFamily1_v2`

MSAA blits from textures to buffers or from buffers to textures are now supported in the new iOS and tvOS feature sets. Blit destinations must be of an adequate size to store the MSAA data.

(MSAA blits were already supported in the `OSX_GPUFamily1_v1` feature set and continue to be supported in the `OSX_GPUFamily1_v2` feature set.)

__Available in:__ `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v1`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`

Writes to sRGB textures are now supported in additional iOS and tvOS feature sets.

(Writes to sRGB textures were already supported in the `iOS_GPUFamily3_v1` feature set.)

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`, `OSX_GPUFamily1_v2` (unless otherwise stated)

This section summarizes additional features introduced in version 1.2 of the Metal shading language. For further information, see the _Metal Shading Language Guide_.

New integer functions to extract, insert, and reverse bits, as described in Integer Functions.

Texture read and write functions can now be used with 16-bit unsigned integer coordinates (`ushort` type), as described in Texture Functions.

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`

A new synchronization function for SIMD-group threads, as described in threadgroup Synchronization Functions.

__Available in:__ `iOS_GPUFamily1_v3`, `iOS_GPUFamily2_v3`, `iOS_GPUFamily3_v2`, `tvOS_GPUFamily1_v2`

New sampler qualifiers to specify maximum anisotropy and LOD clamp range, as described in Samplers.

A struct of resources can now be passed by value as an argument to a graphics or compute function, as described in Function Arguments and Variables.

New convenience constants of type `float` and `half`, as described in Math Functions.

- For all [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) objects, a [MTLStoreActionStore](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionstore) store action is required to store the contents of a render target for subsequent render command encoders or for the display. Prior to iOS 10 and tvOS 10, if all color render targets had a [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) store action, the driver would choose to store the rendered contents to the first enabled render target. In iOS 10 and tvOS 10, the driver no longer performs this unnecessary action.
- In iOS 10 and tvOS 10, buffer alignments have been relaxed for all methods in the [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder) protocol.

[Next](Tessellation.md)[Previous](What%27s%20New%20in%20iOS%209%20and%20OS%20X%2010.11.md)

