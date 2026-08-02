---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/OpenCL.html
archived_at: '2026-07-18T02:54:36.909943Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# OpenCL Changes

## OpenCL

cl.hRemoved cl_device_address_infoAdded #def CL_ADDRESS_MIRRORED_REPEATAdded #def CL_BLOCKINGAdded #def CL_BUFFER_CREATE_TYPE_REGIONAdded #def CL_COMMAND_COPY_BUFFER_RECTAdded #def CL_COMMAND_READ_BUFFER_RECTAdded #def CL_COMMAND_USERAdded #def CL_COMMAND_WRITE_BUFFER_RECTAdded #def CL_CONTEXT_NUM_DEVICESAdded #def CL_CbCr_APPLEAdded #def CL_CbYCrY_APPLEAdded #def CL_DEVICE_HOST_UNIFIED_MEMORYAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_CHARAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLEAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOATAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_HALFAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_INTAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_LONGAdded #def CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORTAdded #def CL_DEVICE_OPENCL_C_VERSIONAdded #def CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALFAdded #def CL_EVENT_CONTEXTAdded #def CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LISTAdded #def CL_FP_SOFT_FLOATAdded #def CL_INVALID_GLOBAL_WORK_SIZEAdded #def CL_INVALID_PROPERTYAdded #def CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLEAdded #def CL_KERNEL_PRIVATE_MEM_SIZEAdded #def CL_MEM_ASSOCIATED_MEMOBJECTAdded #def CL_MEM_OFFSETAdded #def CL_MISALIGNED_SUB_BUFFER_OFFSETAdded #def CL_NON_BLOCKINGAdded #def CL_RGBxAdded #def CL_RGxAdded #def CL_RxAdded #def CL_VERSION_1_1Added #def CL_YCbYCr_APPLEAdded #def CL_Y_APPLEAdded clCreateSubBuffer()Added clCreateUserEvent()Added clEnqueueCopyBufferRect()Added clEnqueueReadBufferRect()Added clEnqueueWriteBufferRect()Added clSetEventCallback()Added clSetMemObjectDestructorCallback()Added clSetUserEventStatus()Added cl_buffer_create_typeAdded cl_buffer_regionModified clCreateContext()

|  | Declaration |
| --- | --- |
| From | cl_context clCreateContext ( cl_context_properties \*, cl_uint, const cl_device_id \*, void (\*pfn_notify)(const char \*, const void \*, size_t, void \*), void \*, cl_int \*); |
| To | cl_context clCreateContext ( const cl_context_properties \*, cl_uint, const cl_device_id \*, void (\*)(const char \*, const void \*, size_t, void \*), void \*, cl_int \*); |

Modified clCreateContextFromType()

|  | Declaration |
| --- | --- |
| From | cl_context clCreateContextFromType ( cl_context_properties \*, cl_device_type, void (\*pfn_notify)(const char \*, const void \*, size_t, void \*), void \*, cl_int \*); |
| To | cl_context clCreateContextFromType ( const cl_context_properties \*, cl_device_type, void (\*)(const char \*, const void \*, size_t, void \*), void \*, cl_int \*); |

Modified clBuildProgram()

|  | Declaration |
| --- | --- |
| From | cl_int clBuildProgram ( cl_program, cl_uint, const cl_device_id \*, const char \*, void (\*pfn_notify)(cl_program, void \*), void \*); |
| To | cl_int clBuildProgram ( cl_program, cl_uint, const cl_device_id \*, const char \*, void (\*)(cl_program, void \*), void \*); |

Modified clSetCommandQueueProperty()

|  | 32/64-bit | Architectures | Declaration |
| --- | --- | --- | --- |
| From | Both | i386,x86_64 | cl_int clSetCommandQueueProperty ( cl_command_queue, cl_command_queue_properties, cl_bool, cl_command_queue_properties \*); |
| To | _Unknown_ | Unknown | CL_API_ENTRY cl_int CL_API_CALL clSetCommandQueueProperty ( cl_command_queue, cl_command_queue_properties, cl_bool, cl_command_queue_properties \*); |

cl_ext.hAdded #def CL_1RGB_APPLEAdded #def CL_BGR1_APPLEAdded #def CL_DEVICE_DOUBLE_FP_CONFIGAdded #def CL_DEVICE_HALF_FP_CONFIGAdded #def CL_INVALID_ARG_NAME_APPLEAdded #def CL_PROGRAM_KERNEL_NAMES_APPLEAdded #def CL_PROGRAM_NUM_KERNELS_APPLEAdded #def CL_SFIXED14_APPLEAdded clCreateContextAndCommandQueueAPPLE()Added clCreateProgramAndKernelsWithSourceAPPLE()Added clSetKernelArgByNameAPPLE()Added clSetKernelArgsListAPPLE()Added clSetKernelArgsVaListAPPLE()cl_gl.hAdded cl_GLsyncModified clGetGLObjectInfo()

|  | Declaration |
| --- | --- |
| From | cl_int clGetGLObjectInfo ( cl_mem, cl_gl_object_type \*, GLuint \*); |
| To | cl_int clGetGLObjectInfo ( cl_mem, cl_gl_object_type \*, cl_GLuint \*); |

Modified clCreateFromGLBuffer()

|  | Declaration |
| --- | --- |
| From | cl_mem clCreateFromGLBuffer ( cl_context, cl_mem_flags, GLuint, int \*); |
| To | cl_mem clCreateFromGLBuffer ( cl_context, cl_mem_flags, cl_GLuint, int \*); |

Modified clCreateFromGLTexture3D()

|  | Declaration |
| --- | --- |
| From | cl_mem clCreateFromGLTexture3D ( cl_context, cl_mem_flags, GLenum, GLint, GLuint, cl_int \*); |
| To | cl_mem clCreateFromGLTexture3D ( cl_context, cl_mem_flags, cl_GLenum, cl_GLint, cl_GLuint, cl_int \*); |

Modified clCreateFromGLTexture2D()

|  | Declaration |
| --- | --- |
| From | cl_mem clCreateFromGLTexture2D ( cl_context, cl_mem_flags, GLenum, GLint, GLuint, cl_int \*); |
| To | cl_mem clCreateFromGLTexture2D ( cl_context, cl_mem_flags, cl_GLenum, cl_GLint, cl_GLuint, cl_int \*); |

Modified clCreateFromGLRenderbuffer()

|  | Declaration |
| --- | --- |
| From | cl_mem clCreateFromGLRenderbuffer ( cl_context, cl_mem_flags, GLuint, cl_int \*); |
| To | cl_mem clCreateFromGLRenderbuffer ( cl_context, cl_mem_flags, cl_GLuint, cl_int \*); |

cl_gl_ext.hAdded #def CL_COMMAND_GL_FENCE_SYNC_OBJECT_KHRAdded #def CL_SYNC_CL_EVENT_ARBAdded #def CL_SYNC_CL_EVENT_COMPLETE_ARBAdded [IOSurfaceRef](https://developer.apple.com/documentation/iosurface/iosurfaceref)Added clCreateEventFromGLsyncKHR()Added clCreateImageFromIOSurface2DAPPLE()Added clCreateSyncFromCLeventARB()cl_platform.hRemoved cl_char16Removed cl_char2Removed cl_char4Removed cl_char8Removed cl_double16Removed cl_double2Removed cl_double4Removed cl_double8Removed cl_float16Removed cl_float2Removed cl_float4Removed cl_float8Removed cl_int16Removed cl_int2Removed cl_int4Removed cl_int8Removed cl_long16Removed cl_long2Removed cl_long4Removed cl_long8Removed cl_short16Removed cl_short2Removed cl_short4Removed cl_short8Removed cl_uchar16Removed cl_uchar2Removed cl_uchar4Removed cl_uchar8Removed cl_uint16Removed cl_uint2Removed cl_uint4Removed cl_uint8Removed cl_ulong16Removed cl_ulong2Removed cl_ulong4Removed cl_ulong8Removed cl_ushort16Removed cl_ushort2Removed cl_ushort4Removed cl_ushort8Added CL_ALIGNED() (no architecture available)Added #def CL_ALIGNEDAdded #def CL_API_SUFFIX__VERSION_1_1Added #def CL_CALLBACKAdded #def CL_EXT_SUFFIX__VERSION_1_0Added #def CL_EXT_SUFFIX__VERSION_1_0_DEPRECATEDAdded #def CL_EXT_SUFFIX__VERSION_1_1Added #def CL_HAS_HI_LO_VECTOR_FIELDSAdded #def CL_HAS_NAMED_VECTOR_FIELDSAdded #def CL_HUGE_VALAdded #def CL_HUGE_VALFAdded #def CL_INFINITYAdded #def CL_MAXFLOATAdded #def CL_M_1_PIAdded #def CL_M_1_PI_FAdded #def CL_M_2_PIAdded #def CL_M_2_PI_FAdded #def CL_M_2_SQRTPIAdded #def CL_M_2_SQRTPI_FAdded #def CL_M_EAdded #def CL_M_E_FAdded #def CL_M_LN10Added #def CL_M_LN10_FAdded #def CL_M_LN2Added #def CL_M_LN2_FAdded #def CL_M_LOG10EAdded #def CL_M_LOG10E_FAdded #def CL_M_LOG2EAdded #def CL_M_LOG2E_FAdded #def CL_M_PIAdded #def CL_M_PI_2Added #def CL_M_PI_2_FAdded #def CL_M_PI_4Added #def CL_M_PI_4_FAdded #def CL_M_PI_FAdded #def CL_M_SQRT1_2Added #def CL_M_SQRT1_2_FAdded #def CL_M_SQRT2Added #def CL_M_SQRT2_FAdded #def CL_NANAdded #def CL_PROGRAM_STRING_DEBUG_INFOAdded #def GCL_API_SUFFIX__VERSION_1_1Added cl_GLenumAdded cl_GLintAdded cl_GLuintAdded cl_char3Added cl_double3Added cl_float3Added cl_int3Added cl_long3Added cl_short3Added cl_uchar3Added cl_uint3Added cl_ulong3Added cl_ushort3Added [nanf()](https://developer.apple.com/documentation/kernel/1557309-nanf) (no architecture available)Modified #def CL_SHRT_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MIN_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_SCHAR_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_INT_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MAX_10_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MAX_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_ULONG_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_UCHAR_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_RADIX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_SHRT_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_CHAR_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_LONG_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MIN_10_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_EPSILON

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_DIG

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_CHAR_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_DIG

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_LONG_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MIN

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MANT_DIG

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_EPSILON

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_RADIX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_UINT_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_INT_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MANT_DIG

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_USHRT_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_CHAR_BIT

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MIN_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_DBL_MAX_10_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MAX_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_FLT_MIN_10_EXP

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

Modified #def CL_SCHAR_MAX

|  | Header |
| --- | --- |
| From | cl.h |
| To | cl_platform.h |

gcl.hAdded CLK_ADDRESS_CLAMPAdded CLK_ADDRESS_CLAMP_TO_EDGEAdded CLK_ADDRESS_MIRRORED_REPEATAdded CLK_ADDRESS_NONEAdded CLK_ADDRESS_REPEATAdded CLK_FILTER_LINEARAdded CLK_FILTER_NEARESTAdded CLK_NORMALIZED_COORDS_FALSEAdded CLK_NORMALIZED_COORDS_TRUEAdded #def CL_DEVICE_TYPE_USE_IDAdded #def CL_DISPATCH_QUEUE_PRIORITY_DEFAULTAdded #def CL_DISPATCH_QUEUE_PRIORITY_HIGHAdded #def CL_DISPATCH_QUEUE_PRIORITY_LOWAdded #def CL_IMAGE_2DAdded #def CL_IMAGE_3DAdded cl_imageAdded cl_image_typeAdded cl_malloc_flagsAdded cl_ndrangeAdded cl_queue_flagsAdded cl_timerAdded clk_sampler_typeAdded sampler_tgcl_priv.hAdded block_kernel_mapAdded block_kernel_map_tableAdded block_kernel_pairAdded gclBuildProgramAPPLE()Added gclBuildProgramBinaryAPPLE()Added gclCreateArgsAPPLE()Added gclDeleteArgsAPPLE()Added gclExecKernelAPPLE()Added gclRegisterBlockKernelMap()Added gclReleaseSampler()Added gclSetKernelArgAPPLE()Added gclSetKernelArgMemAPPLE()Added gclSetKernelArgSamplerAPPLE()Added gcl_log_cl_error()Added gcl_log_cl_fatal()Added gcl_log_error()Added gcl_log_fatal()Added gcl_log_warning()Added kargs_structopencl.hRemoved #def CL_DEVICE_COMPILER_NOT_AVAILABLE

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
