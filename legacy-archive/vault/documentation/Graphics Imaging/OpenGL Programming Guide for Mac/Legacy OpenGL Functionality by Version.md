---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_api_versions/opengl_api_versions.html
archived_at: '2026-07-15T07:36:30.173608Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Updating%20an%20Application%20to%20Support%20the%20OpenGL%203.2%20Core%20Specification.md)[Previous](Tuning%20Your%20OpenGL%20Application.md)

# Legacy OpenGL Functionality by Version

OpenGL functionality changes with each version of the OpenGL API. This appendix describes the functionality that was added with each version. See the official OpenGL specification for detailed information.

The functionality for each version is guaranteed to be available through the OpenGL API even if a particular renderer does not support all of the extensions in a version. For example, a renderer that claims to support OpenGL 1.3 might not export the `GL_ARB_texture_env_combine` or `GL_EXT_texture_env_combine` extensions. It's important that you query both the renderer version and extension string to make sure that the renderer supports any functionality that you want to use.

In the following tables, the extensions describe the feature that the core functionality is based on. The core functionality might not be the same as the extension. For example, compare the core texture crossbar functionality with the extension that it's based on.

__Table A-1__  Functionality added in OpenGL 1.1

| Functionality | Extension |
| Copy texture and subtexture | [GL_EXT_copy_texture](http://www.opengl.org/registry/specs/EXT/copy_texture.txt) and [GL_EXT_subtexture](http://www.opengl.org/registry/specs/EXT/subtexture.txt) |
| Logical operation | [GL_EXT_blend_logic_op](http://www.opengl.org/registry/specs/EXT/blend_logic_op.txt) |
| Polygon offset | [GL_EXT_polygon_offset](http://www.opengl.org/registry/specs/EXT/polygon_offset.txt) |
| Texture image formats | [GL_EXT_texture](http://www.opengl.org/registry/specs/EXT/texture.txt) |
| Texture objects | [GL_EXT_texture_object](http://www.opengl.org/registry/specs/EXT/texture_object.txt) |
| Texture proxies | [GL_EXT_texture](http://www.opengl.org/registry/specs/EXT/texture.txt) |
| Texture replace environment | [GL_EXT_texture](http://www.opengl.org/registry/specs/EXT/texture.txt) |
| Vertex array | [GL_EXT_vertex_array](http://www.opengl.org/registry/specs/EXT/vertex_array.txt) |

There were a number of other minor changes outlined in Appendix C section 9 of the OpenGL specification. See [http://www.opengl.org](http://www.opengl.org/).

__Table A-2__  Functionality added in OpenGL 1.2

| Functionality | Extension |
| BGRA pixel formats | [GL_EXT_bgra](http://www.opengl.org/registry/specs/EXT/bgra.txt) |
| Imaging subset (optional) | [GL_SGI_color_table](http://www.opengl.org/registry/specs/SGI/color_table.txt) , [GL_EXT_color_subtable](http://www.opengl.org/registry/specs/EXT/color_subtable.txt), [GL_EXT_convolution](http://www.opengl.org/registry/specs/EXT/convolution.txt), [GL_HP_convolution_border_modes](http://www.opengl.org/registry/specs/HP/convolution_border_modes.txt), [GL_SGI_color_matrix](http://www.opengl.org/registry/specs/SGI/color_matrix.txt), [GL_EXT_histogram](http://www.opengl.org/registry/specs/EXT/histogram.txt), [GL_EXT_blend_minmax](http://www.opengl.org/registry/specs/EXT/blend_minmax.txt), and [GL_EXT_blend_subtract](http://www.opengl.org/registry/specs/EXT/blend_subtract.txt) |
| Normal rescaling | [GL_EXT_rescale_normal](http://www.opengl.org/registry/specs/EXT/rescale_normal.txt) |
| Packed pixel formats | [GL_EXT_packed_pixels](http://www.opengl.org/registry/specs/EXT/packed_pixels.txt) |
| Separate specular color | [GL_EXT_separate_specular_color](http://www.opengl.org/registry/specs/EXT/separate_specular_color.txt) |
| Texture coordinate edge clamping | [GL_SGIS_texture_edge_clamp](http://www.opengl.org/registry/specs/SGIS/texture_edge_clamp.txt) |
| Texture level of detail control | [GL_SGIS_texture_lod](http://www.opengl.org/registry/specs/SGIS/texture_lod.txt) |
| Three-dimensional texturing | [GL_EXT_texture3D](http://www.opengl.org/registry/specs/EXT/texture3D.txt) |
| Vertex array draw element range | [GL_EXT_draw_range_elements](http://www.opengl.org/registry/specs/EXT/draw_range_elements.txt) |

OpenGL 1.2.1 introduced ARB extensions with no specific core API changes.

__Table A-3__  Functionality added in OpenGL 1.3

| Functionality | Extension |
| Compressed textures | [GL_ARB_texture_compression](http://www.opengl.org/registry/specs/ARB/texture_compression.txt) |
| Cube map textures | [GL_ARB_texture_cube_map](http://www.opengl.org/registry/specs/ARB/texture_cube_map.txt) |
| Multisample | [GL_ARB_multisample](http://www.opengl.org/registry/specs/ARB/multisample.txt) |
| Multitexture | [GL_ARB_multitexture](http://www.opengl.org/registry/specs/ARB/multitexture.txt) |
| Texture add environment mode | [GL_ARB_texture_env_add](http://www.opengl.org/registry/specs/ARB/texture_env_add.txt) |
| Texture border clamp | [GL_ARB_texture_border_clamp](http://www.opengl.org/registry/specs/ARB/texture_border_clamp.txt) |
| Texture combine environment mode | [GL_ARB_texture_env_combine](http://www.opengl.org/registry/specs/ARB/texture_env_combine.txt) |
| Texture dot3 environment mode | [GL_ARB_texture_env_dot3](http://www.opengl.org/registry/specs/ARB/texture_env_dot3.txt) |
| Transpose matrix | [GL_ARB_transpose_matrix](http://www.opengl.org/registry/specs/ARB/transpose_matrix.txt) |

__Table A-4__  Functionality added in OpenGL 1.4

| Functionality | Extension |
| Automatic mipmap generation | [GL_SGIS_generate_mipmap](http://www.opengl.org/registry/specs/SGIS/generate_mipmap.txt) |
| Blend function separate | [GL_ARB_blend_func_separate](http://www.opengl.org/registry/specs/EXT/blend_func_separate.txt) |
| Blend squaring | [GL_NV_blend_square](http://www.opengl.org/registry/specs/NV/blend_square.txt) |
| Depth textures | [GL_ARB_depth_texture](http://www.opengl.org/registry/specs/ARB/depth_texture.txt) |
| Fog coordinate | [GL_EXT_fog_coord](http://www.opengl.org/registry/specs/EXT/fog_coord.txt) |
| Multiple draw arrays | [GL_EXT_multi_draw_arrays](http://www.opengl.org/registry/specs/EXT/multi_draw_arrays.txt) |
| Point parameters | [GL_ARB_point_parameters](http://www.opengl.org/registry/specs/ARB/point_parameters.txt) |
| Secondary color | [GL_EXT_secondary_color](http://www.opengl.org/registry/specs/EXT/secondary_color.txt) |
| Separate blend functions | [GL_EXT_blend_func_separate](http://www.opengl.org/registry/specs/EXT/blend_func_separate.txt), [GL_EXT_blend_color](http://www.opengl.org/registry/specs/EXT/blend_color.txt) |
| Shadows | [GL_ARB_shadow](http://www.opengl.org/registry/specs/ARB/shadow.txt) |
| Stencil wrap | [GL_EXT_stencil_wrap](http://www.opengl.org/registry/specs/EXT/stencil_wrap.txt) |
| Texture crossbar environment mode | [GL_ARB_texture_env_crossbar](http://www.opengl.org/registry/specs/ARB/texture_env_crossbar.txt) |
| Texture level of detail bias | [GL_EXT_texture_lod_bias](http://www.opengl.org/registry/specs/EXT/texture_lod_bias.txt) |
| Texture mirrored repeat | [GL_ARB_texture_mirrored_repeat](http://www.opengl.org/registry/specs/ARB/texture_mirrored_repeat.txt) |
| Window raster position | [GL_ARB_window_pos](http://www.opengl.org/registry/specs/ARB/window_pos.txt) |

__Table A-5__  Functionality added in OpenGL 1.5

| Functionality | Extension |
| Buffer objects | [GL_ARB_vertex_buffer_object](http://www.opengl.org/registry/specs/ARB/vertex_buffer_object.txt) |
| Occlusion queries | [GL_ARB_occlusion_query](http://www.opengl.org/registry/specs/ARB/occlusion_query.txt) |
| Shadow functions | [GL_EXT_shadow_funcs](http://www.opengl.org/registry/specs/EXT/shadow_funcs.txt) |

__Table A-6__  Functionality added in OpenGL 2.0

| Functionality | Extension |
| Multiple render targets | [GL_ARB_draw_buffers](http://www.opengl.org/registry/specs/ARB/draw_buffers.txt) |
| Non–power-of-two textures | [GL_ARB_texture_non_power_of_two](http://www.opengl.org/registry/specs/ARB/texture_non_power_of_two.txt) |
| Point sprites | [GL_ARB_point_sprite](http://www.opengl.org/registry/specs/ARB/point_sprite.txt) |
| Separate blend equation | [GL_EXT_blend_equation_separate](http://www.opengl.org/registry/specs/EXT/blend_equation_separate.txt) |
| Separate stencil | [GL_ATI_separate_stencil](http://www.opengl.org/registry/specs/ATI/separate_stencil.txt)  [GL_EXT_stencil_two_side](http://www.opengl.org/registry/specs/EXT/stencil_two_side.txt) |
| Shading language | [GL_ARB_shading_language_100](http://www.opengl.org/registry/specs/ARB/shading_language_100.txt) |
| Shader objects | [GL_ARB_shader_objects](http://www.opengl.org/registry/specs/ARB/shader_objects.txt) |
| Shader programs | [GL_ARB_fragment_shader](http://www.opengl.org/registry/specs/ARB/fragment_shader.txt)  [GL_ARB_vertex_shader](http://www.opengl.org/registry/specs/ARB/vertex_shader.txt) |

__Table A-7__  Functionality added in OpenGL 2.1

| Functionality | Extension |
| Pixel buffer objects | [GL_ARB_pixel_buffer_object](http://www.opengl.org/registry/specs/ARB/pixel_buffer_object.txt) |
| sRGB textures | [GL_EXT_texture_sRGB](http://www.opengl.org/registry/specs/EXT/texture_sRGB.txt) |

[Next](Updating%20an%20Application%20to%20Support%20the%20OpenGL%203.2%20Core%20Specification.md)[Previous](Tuning%20Your%20OpenGL%20Application.md)

