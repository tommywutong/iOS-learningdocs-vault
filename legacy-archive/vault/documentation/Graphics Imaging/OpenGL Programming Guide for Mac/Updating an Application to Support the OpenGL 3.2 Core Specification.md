---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/UpdatinganApplicationtoSupportOpenGL3/UpdatinganApplicationtoSupportOpenGL3.html
archived_at: '2026-07-15T07:36:30.164110Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Setting%20Up%20Function%20Pointers%20to%20OpenGL%20Routines.md)[Previous](Legacy%20OpenGL%20Functionality%20by%20Version.md)

# Updating an Application to Support the OpenGL 3.2 Core Specification

The OpenGL 3.0 specification deprecated many areas of functionality defined in earlier versions of the OpenGL specification. The OpenGL 3.2 Core profile explicitly removes these deprecated features and adjusts other parts of the specification to provide a streamlined, clean programming interface to OpenGL. Use this chapter to assist you in migrating your application away from this deprecated functionality.

The features that were removed from OpenGL are described in in Appendix E of the OpenGL 3.2 Core specification, and you should use that as the definitive guide for the changes you need to make in your application. Here is a summary of most significant areas that changed:

- If your application uses the fixed-function pipeline, it must be rewritten to use shaders instead.
- If your application uses shaders, you must rewrite your shaders to use OpenGL Shading Language 1.5; many built-in shader variables provided in earlier versions of the OpenGL Shading Language were explicitly removed from the OpenGL Shading Language 1.5 specification. Similarly, your application may no longer provide vertex data using the fixed-function routines; all vertex attributes are now specified as generic vertex attributes.
- Your application must explicitly generate object names using the OpenGL API.
- Vertex data must be provided to OpenGL using buffer objects.
- The built-in matrix stack functionality from earlier versions of OpenGL has been removed; you must recreate this functionality using shader inputs.
- Support for auxiliary and accumulation buffers has been removed; use framebuffer objects instead.
- Your application no longer fetches the list of extensions as a single string. Instead, you first fetch the number of extensions and then separately fetch each extension string.

OpenGL 3.2 provides functionality that earlier versions of OpenGL provided through extensions. Other extensions that were previously supported on OS X are no longer supported when your application uses the OpenGL 3.2 Core profile. Table B-1 lists extensions described elsewhere in this guide; use this table to determine whether the extension is supported, and if not, what equivalent functionality is supported.

__Table B-1__  Extensions described in this guide

| Extension | Status |
| APPLE_fence | Obsolete. Use the `ARB_Sync` functionality provided by OpenGL 3.2 (Core). |
| ARB_vertex_buffer_object | Functionality provided by OpenGL 3.2 (Core). |
| APPLE_vertex_array_object | Obsolete. Use the `ARB_vertex_array_object` functionality provided by OpenGL 3.2 (Core). |
| APPLE_vertex_array_range | Obsolete. Use the `ARB_map_buffer_range` functionality provided by OpenGL 3.2 (Core). |
| APPLE_flush_buffer_range | Obsolete. Use the `ARB_map_buffer_range` functionality provided by OpenGL 3.2 (Core). |
| APPLE_client_storage | Supported. |
| APPLE_texture_range | Supported. |
| ARB_texture_rectangle | Functionality provided by OpenGL 3.2 (Core). |
| ARB_shader_objects | Functionality provided by OpenGL 3.2 (Core). |
| ARB_vertex_shader | Functionality provided by OpenGL 3.2 (Core). |
| ARB_fragment_shader | Functionality provided by OpenGL 3.2 (Core). |
| EXT_transform_feedback | Functionality provided by OpenGL 3.2 (Core). |
| EXT_gpu_shader4 | Obsolete. Functionality included in GLSL 1.5 |
| EXT_geometry_shader4 | Functionality provided by OpenGL 3.2 (Core). |
| EXT_bindable_uniform | Obsolete. Use the `ARB_uniform_buffer_object` functionality provided by OpenGL 3.2 (Core). |
| ARB_pixel_buffer_object | Functionality provided by OpenGL 3.2 (Core). |
| EXT_framebuffer_object | Obsolete. Use the `ARB_framebuffer_object` functionality provided by OpenGL 3.2 (Core). |
| APPLE_pixel_buffer | Obsolete. Use framebuffer objects instead. |
| NV_multisample_filter_hint | Obsolete. Use multisampled renderbuffers to precisely control multisampling. |

[Next](Setting%20Up%20Function%20Pointers%20to%20OpenGL%20Routines.md)[Previous](Legacy%20OpenGL%20Functionality%20by%20Version.md)

