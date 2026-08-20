---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/OpenCL.html
archived_at: '2026-07-18T02:53:11.125446Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OpenCL Changes for Objective-C

### OpenCL

#### cl_gl_ext.h

Modified clCreateEventFromGLsyncKHR()

|  | Declaration |
| --- | --- |
| From | ``` cl_event clCreateEventFromGLsyncKHR (     cl_context,     cl_GLsync,     cl_int * ); ``` |
| To | ``` cl_event _Nullable clCreateEventFromGLsyncKHR (     cl_context _Nonnull,     cl_GLsync _Nonnull,     cl_int * _Nullable ); ``` |

Modified clCreateImageFromIOSurface2DAPPLE()

|  | Declaration |
| --- | --- |
| From | ``` cl_mem clCreateImageFromIOSurface2DAPPLE (     cl_context,     cl_mem_flags,     const cl_image_format *,     size_t,     size_t,     IOSurfaceRef,     cl_int * ); ``` |
| To | ``` cl_mem _Nullable clCreateImageFromIOSurface2DAPPLE (     cl_context _Nonnull,     cl_mem_flags,     const cl_image_format * _Nonnull,     size_t,     size_t,     IOSurfaceRef _Nonnull,     cl_int * _Nullable ); ``` |

Modified clCreateImageFromIOSurfaceWithPropertiesAPPLE()

|  | Declaration |
| --- | --- |
| From | ``` cl_mem clCreateImageFromIOSurfaceWithPropertiesAPPLE (     cl_context,     cl_mem_flags,     const cl_image_format *,     const cl_image_desc *,     cl_iosurface_properties_APPLE *,     cl_int * ); ``` |
| To | ``` cl_mem _Nullable clCreateImageFromIOSurfaceWithPropertiesAPPLE (     cl_context _Nonnull,     cl_mem_flags,     const cl_image_format * _Nonnull,     const cl_image_desc * _Nonnull,     cl_iosurface_properties_APPLE * _Nonnull,     cl_int * _Nullable ); ``` |

Modified clGetGLContextInfoAPPLE()

|  | Declaration |
| --- | --- |
| From | ``` cl_int clGetGLContextInfoAPPLE (     cl_context,     void *,     cl_gl_platform_info,     size_t,     void *,     size_t * ); ``` |
| To | ``` cl_int clGetGLContextInfoAPPLE (     cl_context _Nonnull,     void * _Nonnull,     cl_gl_platform_info,     size_t,     void * _Nullable,     size_t * _Nullable ); ``` |

#### gcl.h

Added #def CL_DISPATCH_QUEUE_PRIORITY_BACKGROUNDModified gcl_copy_image()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_copy_image (     cl_image dst_image,     cl_image src_image,     const size_t dst_origin[3],     const size_t src_origin[3],     const size_t region[3] ); ``` |
| To | ``` void gcl_copy_image (     cl_image _Nonnull dst_image,     cl_image _Nonnull src_image,     const size_t dst_origin[3],     const size_t src_origin[3],     const size_t region[3] ); ``` |

Modified gcl_copy_image_to_ptr()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_copy_image_to_ptr (     void *dst_ptr,     cl_image src_image,     const size_t src_origin[3],     const size_t region[3] ); ``` |
| To | ``` void gcl_copy_image_to_ptr (     void * _Nonnull dst_ptr,     cl_image _Nonnull src_image,     const size_t src_origin[3],     const size_t region[3] ); ``` |

Modified gcl_copy_ptr_to_image()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_copy_ptr_to_image (     cl_mem dst_image,     void *src_ptr,     const size_t dst_origin[3],     const size_t region[3] ); ``` |
| To | ``` void gcl_copy_ptr_to_image (     cl_mem _Nonnull dst_image,     void * _Nonnull src_ptr,     const size_t dst_origin[3],     const size_t region[3] ); ``` |

Modified gcl_create_buffer_from_ptr()

|  | Declaration |
| --- | --- |
| From | ``` cl_mem gcl_create_buffer_from_ptr (     void *ptr ); ``` |
| To | ``` cl_mem _Nullable gcl_create_buffer_from_ptr (     void * _Nonnull ptr ); ``` |

Modified gcl_create_dispatch_queue()

|  | Declaration |
| --- | --- |
| From | ``` dispatch_queue_t gcl_create_dispatch_queue (     cl_queue_flags flags,     cl_device_id device_id ); ``` |
| To | ``` dispatch_queue_t _Nullable gcl_create_dispatch_queue (     cl_queue_flags flags,     cl_device_id _Nullable device_id ); ``` |

Modified gcl_create_image()

|  | Declaration |
| --- | --- |
| From | ``` cl_image gcl_create_image (     const cl_image_format *image_format,     size_t image_width,     size_t image_height,     size_t image_depth,     IOSurfaceRef io_surface ); ``` |
| To | ``` cl_image _Nullable gcl_create_image (     const cl_image_format * _Nonnull image_format,     size_t image_width,     size_t image_height,     size_t image_depth,     IOSurfaceRef _Nullable io_surface ); ``` |

Modified gcl_create_kernel_from_block()

|  | Declaration |
| --- | --- |
| From | ``` cl_kernel gcl_create_kernel_from_block (     void *kernel_block_ptr ); ``` |
| To | ``` cl_kernel _Nullable gcl_create_kernel_from_block (     void * _Nonnull kernel_block_ptr ); ``` |

Modified gcl_free()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_free (     void *ptr ); ``` |
| To | ``` void gcl_free (     void * _Nonnull ptr ); ``` |

Modified gcl_get_context()

|  | Declaration |
| --- | --- |
| From | ``` cl_context gcl_get_context (     void ); ``` |
| To | ``` cl_context _Nullable gcl_get_context (     void ); ``` |

Modified gcl_get_device_id_with_dispatch_queue()

|  | Declaration |
| --- | --- |
| From | ``` cl_device_id gcl_get_device_id_with_dispatch_queue (     dispatch_queue_t queue ); ``` |
| To | ``` cl_device_id _Nullable gcl_get_device_id_with_dispatch_queue (     dispatch_queue_t _Nonnull queue ); ``` |

Modified gcl_get_kernel_block_workgroup_info()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_get_kernel_block_workgroup_info (     void *kernel_block_ptr,     cl_kernel_work_group_info param_name,     size_t param_value_size,     void *param_value,     size_t *param_value_size_ret ); ``` |
| To | ``` void gcl_get_kernel_block_workgroup_info (     void * _Nonnull kernel_block_ptr,     cl_kernel_work_group_info param_name,     size_t param_value_size,     void * _Nonnull param_value,     size_t * _Nullable param_value_size_ret ); ``` |

Modified gcl_get_supported_image_formats()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_get_supported_image_formats (     cl_device_id device_id,     cl_image_type image_type,     unsigned int num_entries,     cl_image_format *image_formats,     unsigned int *num_image_formats ); ``` |
| To | ``` void gcl_get_supported_image_formats (     cl_device_id _Nonnull device_id,     cl_image_type image_type,     unsigned int num_entries,     cl_image_format * _Nonnull image_formats,     unsigned int * _Nullable num_image_formats ); ``` |

Modified gcl_gl_create_image_from_renderbuffer()

|  | Declaration |
| --- | --- |
| From | ``` cl_image gcl_gl_create_image_from_renderbuffer (     GLuint render_buffer ); ``` |
| To | ``` cl_image _Nullable gcl_gl_create_image_from_renderbuffer (     GLuint render_buffer ); ``` |

Modified gcl_gl_create_image_from_texture()

|  | Declaration |
| --- | --- |
| From | ``` cl_image gcl_gl_create_image_from_texture (     GLenum texture_target,     GLint mip_level,     GLuint texture ); ``` |
| To | ``` cl_image _Nullable gcl_gl_create_image_from_texture (     GLenum texture_target,     GLint mip_level,     GLuint texture ); ``` |

Modified gcl_gl_create_ptr_from_buffer()

|  | Declaration |
| --- | --- |
| From | ``` void * gcl_gl_create_ptr_from_buffer (     GLuint bufobj ); ``` |
| To | ``` void * _Nullable gcl_gl_create_ptr_from_buffer (     GLuint bufobj ); ``` |

Modified gcl_gl_set_sharegroup()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_gl_set_sharegroup (     void *share ); ``` |
| To | ``` void gcl_gl_set_sharegroup (     void * _Nonnull share ); ``` |

Modified gcl_malloc()

|  | Declaration |
| --- | --- |
| From | ``` void * gcl_malloc (     size_t bytes,     void *host_ptr,     cl_malloc_flags flags ); ``` |
| To | ``` void * _Nullable gcl_malloc (     size_t bytes,     void * _Nullable host_ptr,     cl_malloc_flags flags ); ``` |

Modified gcl_map_image()

|  | Declaration |
| --- | --- |
| From | ``` void * gcl_map_image (     cl_image image,     cl_map_flags map_flags,     const size_t origin[3],     const size_t region[3] ); ``` |
| To | ``` void * _Nullable gcl_map_image (     cl_image _Nonnull image,     cl_map_flags map_flags,     const size_t origin[3],     const size_t region[3] ); ``` |

Modified gcl_map_ptr()

|  | Declaration |
| --- | --- |
| From | ``` void * gcl_map_ptr (     void *ptr,     cl_map_flags map_flags,     size_t cb ); ``` |
| To | ``` void * _Nullable gcl_map_ptr (     void * _Nonnull ptr,     cl_map_flags map_flags,     size_t cb ); ``` |

Modified gcl_memcpy()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_memcpy (     void *dst,     const void *src,     size_t size ); ``` |
| To | ``` void gcl_memcpy (     void * _Nonnull dst,     const void * _Nonnull src,     size_t size ); ``` |

Modified gcl_memcpy_rect()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_memcpy_rect (     void *dst,     const void *src,     const size_t dst_origin[3],     const size_t src_origin[3],     const size_t region[3],     size_t dst_row_pitch,     size_t dst_slice_pitch,     size_t src_row_pitch,     size_t src_slice_pitch ); ``` |
| To | ``` void gcl_memcpy_rect (     void * _Nonnull dst,     const void * _Nonnull src,     const size_t dst_origin[3],     const size_t src_origin[3],     const size_t region[3],     size_t dst_row_pitch,     size_t dst_slice_pitch,     size_t src_row_pitch,     size_t src_slice_pitch ); ``` |

Modified gcl_release_image()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_release_image (     cl_image image ); ``` |
| To | ``` void gcl_release_image (     cl_image _Nonnull image ); ``` |

Modified gcl_retain_image()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_retain_image (     cl_image image ); ``` |
| To | ``` void gcl_retain_image (     cl_image _Nonnull image ); ``` |

Modified gcl_set_finalizer()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_set_finalizer (     void *object,     void (*cl_pfn_finalizer)(void *object, void *user_data),     void *user_data ); ``` |
| To | ``` void gcl_set_finalizer (     void * _Nonnull object,     void (* _Nonnullcl_pfn_finalizer)(void * _Nonnull object, void * _Nullable user_data),     void * _Nullable user_data ); ``` |

Modified gcl_unmap()

|  | Declaration |
| --- | --- |
| From | ``` void gcl_unmap (     void * ); ``` |
| To | ``` void gcl_unmap (     void * _Nonnull ); ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
