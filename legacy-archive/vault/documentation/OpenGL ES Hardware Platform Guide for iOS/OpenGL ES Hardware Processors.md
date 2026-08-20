---
title: OpenGL ES Hardware Platform Guide for iOS
apple_id: TP40012935
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/OpenGLES/Conceptual/OpenGLESHardwarePlatformGuide_iOS/OpenGLESPlatforms/OpenGLESPlatforms.html
archived_at: '2026-07-18T01:39:28.003670Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [OpenGL ES Hardware Platform Guide for iOS](Introduction%20to%20Hardware%20for%20OpenGL%20ES.md)


[Next](OpenGL%20ES%20on%20iOS%20Simulator.md)[Previous](Introduction%20to%20Hardware%20for%20OpenGL%20ES.md)

# OpenGL ES Hardware Processors

All currently shipping iPhone, iPad, and iPod Touch devices use the PowerVR SGX graphics processors (535, 543, and 554). These processors support [OpenGL ES 2.0](http://www.khronos.org/registry/gles/specs/2.0/es_full_spec_2.0.25.pdf) and also support [OpenGL ES 1.1](http://www.khronos.org/registry/gles/specs/1.1/es_full_spec_1.1.12.pdf) by efficiently implementing the fixed-function pipeline using shaders.

Table 1-1 describes each processor-device combination.

__Table 1-1__  iOS graphics hardware compatibility

| Device compatibility | PowerVR hardware platform | OpenGL ES versions supported |
| iPod Touch (3rd and 4th generations) | SGX 535 | 1.1, 2.0 |
| iPod Touch (5th generation) | SGX 543 | 1.1, 2.0 |
| iPhone 3GS, iPhone 3GS (China), and iPhone 4 | SGX 535 | 1.1, 2.0 |
| iPhone 4S and iPhone 5 | SGX 543 | 1.1, 2.0 |
| iPad Wi-Fi and iPad Wi-Fi + 3G | SGX 535 | 1.1, 2.0 |
| iPad 2 Wi-Fi, iPad 2 Wi-Fi + 3G, iPad 3 Wi-Fi, and iPad 3 Wi-Fi + 3G | SGX 543 | 1.1, 2.0 |
| iPad 4 Wi-Fi and iPad 4 Wi-Fi + 3G | SGX 554 | 1.1, 2.0 |
| iPad Mini Wi-Fi and iPad Mini Wi-Fi + 3G | SGX 543 | 1.1, 2.0 |

Imagination Technologies has several useful references about PowerVR technologies:

- [PowerVR Series 5 Architecture Guide for Developers](http://www.imgtec.com/powervr/insider/docs/PowerVR%20Series%205.Architecture%20Guide%20for%20Developers.pdf). Provides an overview of the SGX Series 5 architecture with some performance recommendations.
- [PowerVR Performance Recommendations](http://www.imgtec.com/powervr/insider/docs/PowerVR.Performance%20Recommendations.pdf). Provides recommendations for optimizing graphics performance on devices that use SGX Series 5 processors.
- [PowerVR SGX OpenGL ES2.0 Application Development Recommendations](http://www.imgtec.com/factsheets/SDK/POWERVR%20SGX.OpenGL%20ES%202.0%20Application%20Development%20Recommendations.1.1f.External.pdf). Introduces the SGX Series of processors and describes how to optimize for them.
- [PowerVR 3D Application Development Recommendations](http://www.imgtec.com/factsheets/SDK/PowerVR%20MBX.3D%20Application%20Development%20Recommendations.1.0.67a.External.pdf). Introduces 3D graphics apps and provides some “golden rules” for developing such apps.

PowerVR SGX series hardware uses a technique known as _tile-based deferred rendering (TBDR)_. When you call OpenGL ES functions to submit rendering commands to the hardware, those commands are buffered until a large list of commands is accumulated. The hardware renders these commands as a single operation by dividing the framebuffer into tiles and then drawing the commands once for each tile, with each tile rendering only the primitives that are visible within it. The key advantage to a deferred renderer is that it accesses memory very efficiently. Partitioning rendering into tiles allows the GPU to more effectively cache the pixel values from the framebuffer, making depth testing and blending more efficient.

Deferred rendering also allows the GPU to perform hidden surface removal before fragments are processed. Pixels that are not visible are discarded without sampling textures or performing fragment processing, significantly reducing the calculations that the GPU must perform to render the tile. To gain the most benefit from this feature, draw as much of the frame with opaque content as possible and minimize use of blending, alpha testing, and the `discard` instruction in GLSL shaders. Because the hardware performs hidden surface removal, it is not necessary for your app to sort primitives from front to back.

Some operations under a deferred renderer are more expensive than they would be under a traditional stream renderer. The memory bandwidth and computational savings described above perform best when processing large scenes. When the hardware receives OpenGL ES commands that require it to render smaller scenes, the renderer loses much of its efficiency. For example, if your app renders batches of triangles using a texture and then modifies the texture, the OpenGL ES implementation must either flush out those commands immediately or duplicate the texture; neither option uses the hardware efficiently. Similarly, any attempt to read pixel data from the framebuffer requires that preceding commands be processed if they would alter that framebuffer.

These practices apply to OpenGL ES apps on SGX Series 5 hardware:

- Avoid operations that modify OpenGL ES objects already in use by the renderer because of previously submitted drawing commands. When you need to modify OpenGL ES resources, schedule those modifications at the beginning or end of a frame. These commands include `glBufferSubData`, `glBufferData`, `glMapBuffer`, `glTexSubImage`, `glCopyTexImage`, `glCopyTexSubImage`, `glReadPixels`, `glBindFramebuffer`, `glFlush`, and `glFinish`.
- To take advantage of the processor’s hidden surface removal, follow the drawing guidelines found in [Do Not Sort Rendered Objects Except Where Necessary For Correct Rendering](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/Tuning%20Your%20OpenGL%20ES%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqmjqguwvgvzx) in _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.
- Vertex buffer objects (VBOs) provide a significant performance improvement on the PowerVR SGX. See [Use Vertex Buffer Objects to Manage Copying Vertex Data](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/Best%20Practices%20for%20Working%20with%20Vertex%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqmjqg4wvgvzw) in _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.
- Do not use separate stencil buffers. Instead use a combined depth/stencil buffer.
- Use Core Animation rotations of renderbuffers to rotate content between landscape and portrait mode. For best performance, ensure that the renderbuffer’s height and width are each a multiple of 32 pixels.

Table 1-2 provides a high-level summary for OpenGL ES 2.0 platforms.

__Table 1-2__  Summary of key OpenGL ES 2.0 attribute values implemented for SGX 535, 543, and 554

| OpenGL ES 2.0 attributes | Values for SGX 535 | Values for SGX 543 and 554 |
| MAX_TEXTURE_SIZE, MAX_RENDERBUFFER_SIZE, MAX_CUBE_MAP_TEXTURE_SIZE | 2048 x 2048 | 4096 x 4096 |
| MAX_TEXTURE_IMAGE_UNITS | 8 | 8 |
| MAX_COMBINED_TEXTURE_IMAGE_UNITS | 8 | 8 |
| MAX_VERTEX_TEXTURE_IMAGE_UNITS | 0 | 0 |
| MAX_VERTEX_ATTRIBS | 16 | 16 |
| MAX_VERTEX_UNIFORM_VECTORS | 128 | 128 |
| MAX_FRAGMENT_UNIFORM_VECTORS | 64 | 64 |
| MAX_VARYING_VECTORS | 8 | 8 |

The PowerVR SGX processes high-precision floating-point calculations using a scalar processor, even when those values are declared in a vector. Proper use of write masks and careful definitions of your calculations can improve the performance of your shaders. For more information, see [Perform Vector Calculations Lazily](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/Best%20Practices%20for%20Shaders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqnznknlte) in _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.

Medium- and low-precision floating-point values are processed in parallel. However, low-precision variables have a few specific performance limitations:

- Swizzling components of vectors declared with low precision is expensive and should be avoided.
- Many built-in functions use medium-precision inputs and outputs. If your app provides low-precision floating-point values as parameters or assigns the results to a low-precision floating-point variable, the shader may have to include additional instructions to convert the values. These additional instructions are also added when swizzling the vector results of a computation.

The vertex shader and fragment processing combined cannot use more than 8 texture image units. See Section 2.10.5 in the [Khronos OpenGL ES Version 2.0.25 specification](http://www.khronos.org/registry/gles/specs/2.0/es_full_spec_2.0.25.pdf) for details. Additionally, texture fetches in vertex shaders are not supported.

For best results, limit your use of low-precision variables to color values.

The following extensions are supported for all SGX Series 5 processors: 535, 543, and 554:

- [APPLE_copy_texture_levels](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_copy_texture_levels.txt)
- [APPLE_framebuffer_multisample](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_framebuffer_multisample.txt)
- [APPLE_rgb_422](http://www.opengl.org/registry/specs/APPLE/rgb_422.txt)
- [APPLE_texture_format_BGRA8888](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_format_BGRA8888.txt)
- [APPLE_texture_max_level](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_max_level.txt)
- [APPLE_sync](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_sync.txt)
- [EXT_blend_minmax](http://www.opengl.org/registry/specs/EXT/blend_minmax.txt)
- [EXT_debug_label](http://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_label.txt)
- [EXT_debug_marker](http://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_marker.txt)
- [EXT_discard_framebuffer](http://www.khronos.org/registry/gles/extensions/EXT/EXT_discard_framebuffer.txt)
- [EXT_map_buffer_range](http://www.khronos.org/registry/gles/extensions/EXT/EXT_map_buffer_range.txt)
- [EXT_separate_shader_objects](http://www.khronos.org/registry/gles/extensions/EXT/EXT_separate_shader_objects.txt)
- [EXT_shader_framebuffer_fetch](http://www.khronos.org/registry/gles/extensions/EXT/EXT_shader_framebuffer_fetch.txt)
- [EXT_read_format_bgra](http://www.khronos.org/registry/gles/extensions/EXT/EXT_read_format_bgra.txt)
- [EXT_shader_texture_lod](http://www.khronos.org/registry/gles/extensions/EXT/EXT_shader_texture_lod.txt)
- [EXT_texture_filter_anisotropic](http://www.khronos.org/registry/gles/extensions/EXT/texture_filter_anisotropic.txt)
- [EXT_texture_storage](http://www.khronos.org/registry/gles/extensions/EXT/EXT_texture_storage.txt)
- [IMG_read_format](http://www.khronos.org/registry/gles/extensions/IMG/IMG_read_format.txt)
- [IMG_texture_compression_pvrtc](http://www.khronos.org/registry/gles/extensions/IMG/IMG_texture_compression_pvrtc.txt)
- [OES_depth24](http://www.khronos.org/registry/gles/extensions/OES/OES_depth24.txt)
- [OES_depth_texture](http://www.khronos.org/registry/gles/extensions/OES/OES_depth_texture.txt)
- [OES_element_index_uint](http://www.khronos.org/registry/gles/extensions/OES/OES_element_index_uint.txt)
- [OES_fbo_render_mipmap](http://www.khronos.org/registry/gles/extensions/OES/OES_fbo_render_mipmap.txt)
- [OES_mapbuffer](http://www.khronos.org/registry/gles/extensions/OES/OES_mapbuffer.txt)
- [OES_packed_depth_stencil](http://www.khronos.org/registry/gles/extensions/OES/OES_packed_depth_stencil.txt)
- [OES_rgb8_rgba8](http://www.khronos.org/registry/gles/extensions/OES/OES_rgb8_rgba8.txt)
- [OES_standard_derivatives](http://www.khronos.org/registry/gles/extensions/OES/OES_standard_derivatives.txt)
- [OES_texture_half_float](http://www.khronos.org/registry/gles/extensions/OES/OES_texture_float.txt)
- [OES_texture_float](http://www.khronos.org/registry/gles/extensions/OES/OES_texture_float.txt)
- [OES_texture_half_float](http://www.khronos.org/registry/gles/extensions/OES/OES_texture_float.txt)
- [OES_vertex_array_object](http://www.khronos.org/registry/gles/extensions/OES/OES_vertex_array_object.txt)

The following extensions are supported for the SGX 543 and 554 processors only:

- [EXT_color_buffer_half_float](http://www.khronos.org/registry/gles/extensions/EXT/EXT_color_buffer_half_float.txt)
- [EXT_occlusion_query_boolean](http://www.khronos.org/registry/gles/extensions/EXT/EXT_occlusion_query_boolean.txt)
- [EXT_shadow_samplers](http://www.khronos.org/registry/gles/extensions/EXT/EXT_shadow_samplers.txt)
- [EXT_texture_rg](http://www.khronos.org/registry/gles/extensions/EXT/EXT_texture_rg.txt)
- [OES_texture_half_float_linear](http://www.khronos.org/registry/gles/extensions/OES/OES_texture_float_linear.txt)

OpenGL ES 1.1 is implemented on PowerVR SGX Series 5 hardware using customized shaders. Whenever your app changes OpenGL ES state variables, a new shader is implicitly generated as needed. Because of this, changing OpenGL ES state may be more expensive than it would be on a pure hardware implementation. You can improve the performance of your app by reducing the number of state changes it performs. For more information, see [Be Mindful of OpenGL ES State Variables](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/OpenGL%20ES%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojtfvbuqnrnknltm) in _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.

Table 1-3 provides a high-level summary for OpenGL ES 1.1 platforms.

__Table 1-3__  Summary of key OpenGL ES 1.1 attribute values implemented for SGX 535, 543, and 554

| OpenGL ES 1.1 Attributes | Values for SGX 535 | Values for SGX 543 and 554 |
| MAX_TEXTURE_SIZE, MAX_RENDERBUFFER_SIZE, MAX_CUBE_MAP_TEXTURE_SIZE | 2048 x 2048 | 4096 x 4096 |
| MAX_TEXTURE_UNITS | 8 | 8 |
| LINE_WIDTH_RANGE | 1.0 - 16.0 pixels | 1.0 - 16.0 pixels |
| POINT_SIZE_RANGES | 1.0 - 511.0 pixels | 1.0 - 511.0 pixels |
| MAX_PALETTE_MATRICES_OES | 11 | 11 |
| MAX_VERTEX_UNITS_OES | 4 | 4 |
| MAX_CLIP_PLANES | 6 | 6 |
| MAX_TEXTURE_LOD_BIAS_EXT | 4 | 4 |

The following extensions are supported for all SGX Series 5 processors: 535, 543, and 554:

- [APPLE_copy_texture_levels](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_copy_texture_levels.txt)
- [APPLE_framebuffer_multisample](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_framebuffer_multisample.txt)
- [APPLE_texture_2D_limited_npot](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_2D_limited_npot.txt)
- [APPLE_texture_format_BGRA8888](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_format_BGRA8888.txt)
- [APPLE_texture_max_level](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_max_level.txt)
- [EXT_blend_minmax](http://www.opengl.org/registry/specs/EXT/blend_minmax.txt)
- [EXT_debug_label](http://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_label.txt)
- [EXT_debug_marker](http://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_marker.txt)
- [EXT_discard_framebuffer](http://www.khronos.org/registry/gles/extensions/EXT/EXT_discard_framebuffer.txt)
- [EXT_map_buffer_range](http://www.khronos.org/registry/gles/extensions/EXT/EXT_map_buffer_range.txt)
- [EXT_read_format_bgra](http://www.khronos.org/registry/gles/extensions/EXT/EXT_read_format_bgra.txt)
- [EXT_texture_filter_anisotropic](http://www.khronos.org/registry/gles/extensions/EXT/texture_filter_anisotropic.txt)
- [EXT_texture_lod_bias](http://www.khronos.org/registry/gles/extensions/EXT/texture_lod_bias.txt)
- [EXT_texture_storage](http://www.khronos.org/registry/gles/extensions/EXT/EXT_texture_storage.txt)
- [IMG_read_format](http://www.khronos.org/registry/gles/extensions/IMG/IMG_read_format.txt)
- [IMG_texture_compression_pvrtc](http://www.khronos.org/registry/gles/extensions/IMG/IMG_texture_compression_pvrtc.txt)
- [OES_blend_equation_separate](http://www.khronos.org/registry/gles/extensions/OES/OES_blend_equation_separate.txt)
- [OES_blend_func_separate](http://www.khronos.org/registry/gles/extensions/OES/OES_blend_func_separate.txt)
- [OES_blend_subtract](http://www.khronos.org/registry/gles/extensions/OES/OES_blend_subtract.txt)
- [OES_compressed_paletted_texture](http://www.khronos.org/registry/gles/extensions/OES/OES_compressed_paletted_texture.txt)
- [OES_depth24](http://www.khronos.org/registry/gles/extensions/OES/OES_depth24.txt)
- [OES_draw_texture](http://www.khronos.org/registry/gles/extensions/OES/OES_draw_texture.txt)
- [OES_element_index_uint](http://www.khronos.org/registry/gles/extensions/OES/OES_element_index_uint.txt)
- [OES_fbo_render_mipmap](http://www.khronos.org/registry/gles/extensions/OES/OES_fbo_render_mipmap.txt)
- [OES_framebuffer_object](http://www.khronos.org/registry/gles/extensions/OES/OES_framebuffer_object.txt)
- [OES_mapbuffer](http://www.khronos.org/registry/gles/extensions/OES/OES_mapbuffer.txt)
- [OES_matrix_palette](http://www.khronos.org/registry/gles/extensions/OES/OES_matrix_palette.txt)
- [OES_packed_depth_stencil](http://www.khronos.org/registry/gles/extensions/OES/OES_packed_depth_stencil.txt)
- [OES_point_size_array](http://www.khronos.org/registry/gles/extensions/OES/OES_point_size_array.txt)
- [OES_point_sprite](http://www.khronos.org/registry/gles/extensions/OES/OES_point_sprite.txt)
- [OES_read_format](http://www.khronos.org/registry/gles/extensions/OES/OES_read_format.txt)
- [OES_rgb8_rgba8](http://www.khronos.org/registry/gles/extensions/OES/OES_rgb8_rgba8.txt)
- [OES_stencil8](http://www.khronos.org/registry/gles/extensions/OES/OES_stencil8.txt)
- [OES_stencil_wrap](http://www.khronos.org/registry/gles/extensions/OES/OES_stencil_wrap.txt)
- [OES_texture_mirrored_repeat](http://www.khronos.org/registry/gles/extensions/OES/OES_texture_mirrored_repeat.txt)
- [OES_vertex_array_object](http://www.khronos.org/registry/gles/extensions/OES/OES_vertex_array_object.txt)

[Next](OpenGL%20ES%20on%20iOS%20Simulator.md)[Previous](Introduction%20to%20Hardware%20for%20OpenGL%20ES.md)

