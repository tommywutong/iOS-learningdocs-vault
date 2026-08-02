---
title: OpenGL ES Hardware Platform Guide for iOS
apple_id: TP40012935
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/OpenGLES/Conceptual/OpenGLESHardwarePlatformGuide_iOS/OpenGLESiniOSSimulator/OpenGLESiniOSSimulator.html
archived_at: '2026-07-18T01:39:28.110864Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [OpenGL ES Hardware Platform Guide for iOS](Introduction%20to%20Hardware%20for%20OpenGL%20ES.md)


[Next](Document%20Revision%20History.md)[Previous](OpenGL%20ES%20Hardware%20Processors.md)

# OpenGL ES on iOS Simulator

iOS Simulator includes complete and conformant implementations of both OpenGL ES 1.1 and OpenGL ES 2.0 that you can use for your app development. Simulator differs from the PowerVR SGX processors in a number of ways:

- Simulator does not use a tile-based deferred renderer.
- Simulator does not support the same set of extensions as the PowerVR SGX processors support.
- Simulator does not provide a pixel-accurate match to the PowerVR SGX processors.

Table 2-1 provides a high-level summary of key OpenGL ES 2.0 attribute values implemented for iOS Simulator.

__Table 2-1__  Key OpenGL ES 2.0 attribute values implemented for iOS Simulator

| OpenGL ES 2.0 attributes | Values for iOS Simulator |
| MAX_TEXTURE_SIZE, MAX_RENDERBUFFER_SIZE, MAX_CUBE_MAP_TEXTURE_SIZE | 4096 x 4096 |
| MAX_TEXTURE_IMAGE_UNITS | 8 |
| MAX_VERTEX_TEXTURE_IMAGE_UNITS | 0 |
| MAX_VERTEX_ATTRIBS | 16 |
| MAX_VERTEX_UNIFORM_VECTORS | 128 |
| MAX_FRAGMENT_UNIFORM_VECTORS | 64 |
| MAX_VARYING_VECTORS | 8 |

iOS Simulator supports the following extensions to OpenGL ES 2.0:

- [APPLE_copy_texture_levels](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_copy_texture_levels.txt)
- [APPLE_framebuffer_multisample](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_framebuffer_multisample.txt)
- [APPLE_rgb_422](http://www.opengl.org/registry/specs/APPLE/rgb_422.txt)
- [APPLE_sync](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_sync.txt)
- [APPLE_texture_format_BGRA8888](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_format_BGRA8888.txt)
- [APPLE_texture_max_level](http://www.khronos.org/registry/gles/extensions/APPLE/APPLE_texture_max_level.txt)
- [EXT_blend_minmax](http://www.opengl.org/registry/specs/EXT/blend_minmax.txt)
- [EXT_color_buffer_half_float](http://www.khronos.org/registry/gles/extensions/EXT/EXT_color_buffer_half_float.txt)
- [EXT_debug_label](http://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_label.txt)
- [EXT_debug_marker](http://www.khronos.org/registry/gles/extensions/EXT/EXT_debug_marker.txt)
- [EXT_discard_framebuffer](http://www.khronos.org/registry/gles/extensions/EXT/EXT_discard_framebuffer.txt)
- [EXT_map_buffer_range](http://www.khronos.org/registry/gles/extensions/EXT/EXT_map_buffer_range.txt)
- [EXT_occlusion_query_boolean](http://www.khronos.org/registry/gles/extensions/EXT/EXT_occlusion_query_boolean.txt)
- [EXT_separate_shader_objects](http://www.khronos.org/registry/gles/extensions/EXT/EXT_separate_shader_objects.txt)
- [EXT_shader_framebuffer_fetch](http://www.khronos.org/registry/gles/extensions/EXT/EXT_shader_framebuffer_fetch.txt)
- [EXT_read_format_bgra](http://www.khronos.org/registry/gles/extensions/EXT/EXT_read_format_bgra.txt)
- [EXT_shader_texture_lod](http://www.khronos.org/registry/gles/extensions/EXT/EXT_shader_texture_lod.txt)
- [EXT_shadow_samplers](http://www.khronos.org/registry/gles/extensions/EXT/EXT_shadow_samplers.txt)
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
- [OES_vertex_array_object](http://www.khronos.org/registry/gles/extensions/OES/OES_vertex_array_object.txt)

Table 2-2 provides a high-level summary of key OpenGL ES 1.1 attribute values implemented for iOS Simulator.

__Table 2-2__  Key OpenGL ES 1.1 attribute values implemented for iOS Simulator

| OpenGL ES 1.1 attributes | Values for iOS Simulator |
| MAX_TEXTURE_SIZE, MAX_RENDERBUFFER_SIZE, MAX_CUBE_MAP_TEXTURE_SIZE | 4096 x 4096 |
| MAX_TEXTURE_UNITS | 8 |
| MAX_PALETTE_MATRICES_OES | 11 |
| MAX_VERTEX_UNITS_OES | 4 |
| MAX_CLIP_PLANES | 6 |

iOS Simulator supports the following extensions to OpenGL ES 1.1:

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

[Next](Document%20Revision%20History.md)[Previous](OpenGL%20ES%20Hardware%20Processors.md)

