---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/OpenCL.html
archived_at: '2026-07-18T02:52:34.563763Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# OpenCL Changes

## OpenCL

Added cl_char16 [struct]Added cl_char16.init()Added cl_char2 [struct]Added cl_char2.init()Added cl_char4 [struct]Added cl_char4.init()Added cl_char8 [struct]Added cl_char8.init()Added cl_double16 [struct]Added cl_double16.init()Added cl_double2 [struct]Added cl_double2.init()Added cl_double4 [struct]Added cl_double4.init()Added cl_double8 [struct]Added cl_double8.init()Added cl_float16 [struct]Added cl_float16.init()Added cl_float2 [struct]Added cl_float2.init()Added cl_float4 [struct]Added cl_float4.init()Added cl_float8 [struct]Added cl_float8.init()Added cl_int16 [struct]Added cl_int16.init()Added cl_int2 [struct]Added cl_int2.init()Added cl_int4 [struct]Added cl_int4.init()Added cl_int8 [struct]Added cl_int8.init()Added cl_long16 [struct]Added cl_long16.init()Added cl_long2 [struct]Added cl_long2.init()Added cl_long4 [struct]Added cl_long4.init()Added cl_long8 [struct]Added cl_long8.init()Added cl_short16 [struct]Added cl_short16.init()Added cl_short2 [struct]Added cl_short2.init()Added cl_short4 [struct]Added cl_short4.init()Added cl_short8 [struct]Added cl_short8.init()Added cl_uchar16 [struct]Added cl_uchar16.init()Added cl_uchar2 [struct]Added cl_uchar2.init()Added cl_uchar4 [struct]Added cl_uchar4.init()Added cl_uchar8 [struct]Added cl_uchar8.init()Added cl_uint16 [struct]Added cl_uint16.init()Added cl_uint2 [struct]Added cl_uint2.init()Added cl_uint4 [struct]Added cl_uint4.init()Added cl_uint8 [struct]Added cl_uint8.init()Added cl_ulong16 [struct]Added cl_ulong16.init()Added cl_ulong2 [struct]Added cl_ulong2.init()Added cl_ulong4 [struct]Added cl_ulong4.init()Added cl_ulong8 [struct]Added cl_ulong8.init()Added cl_ushort16 [struct]Added cl_ushort16.init()Added cl_ushort2 [struct]Added cl_ushort2.init()Added cl_ushort4 [struct]Added cl_ushort4.init()Added cl_ushort8 [struct]Added cl_ushort8.init()Added clSetKernelArgsListAPPLE(cl_kernel, cl_uint, CVarArgType) -> cl_intAdded cl_char3Added cl_double3Added cl_float3Added cl_int3Added cl_long3Added cl_short3Added cl_uchar3Added cl_uint3Added cl_ulong3Added cl_ushort3Added openCLOverlayWorksModified clBuildProgram(cl_program, cl_uint, UnsafePointer<cl_device_id>, UnsafePointer<Int8>, CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clBuildProgram(_ _: cl_program, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: ConstUnsafePointer<Int8>, _ _: CFunctionPointer<((cl_program, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clBuildProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` | OS X 10.6 |

Modified clCompileProgram(cl_program, cl_uint, UnsafePointer<cl_device_id>, UnsafePointer<Int8>, cl_uint, UnsafePointer<cl_program>, UnsafeMutablePointer<UnsafePointer<Int8>>, CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCompileProgram(_ _: cl_program, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: ConstUnsafePointer<Int8>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_program>, _ _: UnsafePointer<ConstUnsafePointer<Int8>>, _ _: CFunctionPointer<((cl_program, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clCompileProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` | OS X 10.8 |

Modified clCreateBuffer(cl_context, cl_mem_flags, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateBuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateBuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.6 |

Modified clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, UnsafeMutablePointer<cl_int>) -> cl_command_queue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateCommandQueue(_ _: cl_context, _ _: cl_device_id, _ _: cl_command_queue_properties, _ _: UnsafePointer<cl_int>) -> cl_command_queue ``` | OS X 10.10 |
| To | ``` func clCreateCommandQueue(_ _: cl_context, _ _: cl_device_id, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_int>) -> cl_command_queue ``` | OS X 10.6 |

Modified clCreateCommandQueueWithPropertiesAPPLE(cl_context, cl_device_id, UnsafePointer<cl_queue_properties_APPLE>, UnsafeMutablePointer<cl_int>) -> cl_command_queue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateCommandQueueWithPropertiesAPPLE(_ _: cl_context, _ _: cl_device_id, _ _: ConstUnsafePointer<cl_queue_properties_APPLE>, _ _: UnsafePointer<cl_int>) -> cl_command_queue ``` | OS X 10.10 |
| To | ``` func clCreateCommandQueueWithPropertiesAPPLE(_ _: cl_context, _ _: cl_device_id, _ _: UnsafePointer<cl_queue_properties_APPLE>, _ _: UnsafeMutablePointer<cl_int>) -> cl_command_queue ``` | OS X 10.8 |

Modified clCreateContext(UnsafePointer<cl_context_properties>, cl_uint, UnsafePointer<cl_device_id>, CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<cl_int>) -> cl_context

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateContext(_ _: ConstUnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<()>, UInt, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>, _ _: UnsafePointer<cl_int>) -> cl_context ``` | OS X 10.10 |
| To | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` | OS X 10.6 |

Modified clCreateContextAndCommandQueueAPPLE(UnsafePointer<cl_context_properties>, cl_uint, UnsafePointer<cl_device_id>, CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, cl_command_queue_properties, UnsafeMutablePointer<cl_context>, UnsafeMutablePointer<cl_command_queue>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateContextAndCommandQueueAPPLE(_ _: ConstUnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<()>, UInt, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>, _ _: cl_command_queue_properties, _ _: UnsafePointer<cl_context>, _ _: UnsafePointer<cl_command_queue>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context>, _ _: UnsafeMutablePointer<cl_command_queue>) -> cl_int ``` | OS X 10.7 |

Modified clCreateContextFromType(UnsafePointer<cl_context_properties>, cl_device_type, CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<cl_int>) -> cl_context

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateContextFromType(_ _: ConstUnsafePointer<cl_context_properties>, _ _: cl_device_type, _ _: CFunctionPointer<((ConstUnsafePointer<Int8>, ConstUnsafePointer<()>, UInt, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>, _ _: UnsafePointer<cl_int>) -> cl_context ``` | OS X 10.10 |
| To | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>, _ _: cl_device_type, _ _: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` | OS X 10.6 |

Modified clCreateDAGAPPLE(cl_context) -> cl_dag

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified clCreateEventFromGLsyncKHR(cl_context, cl_GLsync, UnsafeMutablePointer<cl_int>) -> cl_event

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateEventFromGLsyncKHR(_ _: cl_context, _ _: cl_GLsync, _ _: UnsafePointer<cl_int>) -> cl_event ``` | OS X 10.10 |
| To | ``` func clCreateEventFromGLsyncKHR(_ _: cl_context, _ _: cl_GLsync, _ _: UnsafeMutablePointer<cl_int>) -> cl_event ``` | OS X 10.7 |

Modified clCreateFromGLBuffer(cl_context, cl_mem_flags, cl_GLuint, UnsafeMutablePointer<Int32>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateFromGLBuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafePointer<Int32>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateFromGLBuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafeMutablePointer<Int32>) -> cl_mem ``` | OS X 10.6 |

Modified clCreateFromGLRenderbuffer(cl_context, cl_mem_flags, cl_GLuint, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateFromGLRenderbuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateFromGLRenderbuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.6 |

Modified clCreateFromGLTexture(cl_context, cl_mem_flags, cl_GLenum, cl_GLint, cl_GLuint, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateFromGLTexture(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLenum, _ _: cl_GLint, _ _: cl_GLuint, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateFromGLTexture(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLenum, _ _: cl_GLint, _ _: cl_GLuint, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.8 |

Modified clCreateImage(cl_context, cl_mem_flags, UnsafePointer<cl_image_format>, UnsafePointer<cl_image_desc>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateImage(_ _: cl_context, _ _: cl_mem_flags, _ _: ConstUnsafePointer<cl_image_format>, _ _: ConstUnsafePointer<cl_image_desc>, _ _: UnsafePointer<()>, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateImage(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: UnsafePointer<cl_image_desc>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.8 |

Modified clCreateImageFromIOSurface2DAPPLE(cl_context, cl_mem_flags, UnsafePointer<cl_image_format>, Int, Int, IOSurface!, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateImageFromIOSurface2DAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: ConstUnsafePointer<cl_image_format>, _ _: UInt, _ _: UInt, _ _: IOSurface!, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateImageFromIOSurface2DAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: Int, _ _: Int, _ _: IOSurface!, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.7 |

Modified clCreateImageFromIOSurfaceWithPropertiesAPPLE(cl_context, cl_mem_flags, UnsafePointer<cl_image_format>, UnsafePointer<cl_image_desc>, UnsafeMutablePointer<cl_iosurface_properties_APPLE>, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateImageFromIOSurfaceWithPropertiesAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: ConstUnsafePointer<cl_image_format>, _ _: ConstUnsafePointer<cl_image_desc>, _ _: UnsafePointer<cl_iosurface_properties_APPLE>, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateImageFromIOSurfaceWithPropertiesAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: UnsafePointer<cl_image_desc>, _ _: UnsafeMutablePointer<cl_iosurface_properties_APPLE>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.8 |

Modified clCreateKernel(cl_program, UnsafePointer<Int8>, UnsafeMutablePointer<cl_int>) -> cl_kernel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateKernel(_ _: cl_program, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<cl_int>) -> cl_kernel ``` | OS X 10.10 |
| To | ``` func clCreateKernel(_ _: cl_program, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<cl_int>) -> cl_kernel ``` | OS X 10.6 |

Modified clCreateKernelFromDAGAPPLE(cl_dag, cl_uint, UnsafePointer<cl_device_id>) -> cl_kernel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateKernelFromDAGAPPLE(_ d: cl_dag, _ n: cl_uint, _ list: ConstUnsafePointer<cl_device_id>) -> cl_kernel ``` | OS X 10.10 |
| To | ``` func clCreateKernelFromDAGAPPLE(_ d: cl_dag, _ n: cl_uint, _ list: UnsafePointer<cl_device_id>) -> cl_kernel ``` | OS X 10.8 |

Modified clCreateKernelsInProgram(cl_program, cl_uint, UnsafeMutablePointer<cl_kernel>, UnsafeMutablePointer<cl_uint>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateKernelsInProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_kernel>, _ _: UnsafePointer<cl_uint>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clCreateKernelsInProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_kernel>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` | OS X 10.6 |

Modified clCreateProgramAndKernelsWithSourceAPPLE(cl_context, cl_uint, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int>, cl_uint, UnsafePointer<cl_device_id>, UnsafePointer<Int8>, cl_uint, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<cl_program>, UnsafeMutablePointer<cl_kernel>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateProgramAndKernelsWithSourceAPPLE(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<ConstUnsafePointer<Int8>>, _ _: ConstUnsafePointer<UInt>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: ConstUnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<ConstUnsafePointer<Int8>>, _ _: UnsafePointer<cl_program>, _ _: UnsafePointer<cl_kernel>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clCreateProgramAndKernelsWithSourceAPPLE(_ _: cl_context, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UnsafeMutablePointer<cl_program>, _ _: UnsafeMutablePointer<cl_kernel>) -> cl_int ``` | OS X 10.7 |

Modified clCreateProgramWithBinary(cl_context, cl_uint, UnsafePointer<cl_device_id>, UnsafePointer<Int>, UnsafeMutablePointer<UnsafePointer<UInt8>>, UnsafeMutablePointer<cl_int>, UnsafeMutablePointer<cl_int>) -> cl_program

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateProgramWithBinary(_ _: cl_context, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: ConstUnsafePointer<UInt>, _ _: UnsafePointer<ConstUnsafePointer<UInt8>>, _ _: UnsafePointer<cl_int>, _ _: UnsafePointer<cl_int>) -> cl_program ``` | OS X 10.10 |
| To | ``` func clCreateProgramWithBinary(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int>, _ _: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ _: UnsafeMutablePointer<cl_int>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` | OS X 10.6 |

Modified clCreateProgramWithBuiltInKernels(cl_context, cl_uint, UnsafePointer<cl_device_id>, UnsafePointer<Int8>, UnsafeMutablePointer<cl_int>) -> cl_program

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateProgramWithBuiltInKernels(_ _: cl_context, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<cl_int>) -> cl_program ``` | OS X 10.10 |
| To | ``` func clCreateProgramWithBuiltInKernels(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` | OS X 10.8 |

Modified clCreateProgramWithSource(cl_context, cl_uint, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int>, UnsafeMutablePointer<cl_int>) -> cl_program

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateProgramWithSource(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<ConstUnsafePointer<Int8>>, _ _: ConstUnsafePointer<UInt>, _ _: UnsafePointer<cl_int>) -> cl_program ``` | OS X 10.10 |
| To | ``` func clCreateProgramWithSource(_ _: cl_context, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UnsafePointer<Int>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` | OS X 10.6 |

Modified clCreateSampler(cl_context, cl_bool, cl_addressing_mode, cl_filter_mode, UnsafeMutablePointer<cl_int>) -> cl_sampler

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateSampler(_ _: cl_context, _ _: cl_bool, _ _: cl_addressing_mode, _ _: cl_filter_mode, _ _: UnsafePointer<cl_int>) -> cl_sampler ``` | OS X 10.10 |
| To | ``` func clCreateSampler(_ _: cl_context, _ _: cl_bool, _ _: cl_addressing_mode, _ _: cl_filter_mode, _ _: UnsafeMutablePointer<cl_int>) -> cl_sampler ``` | OS X 10.6 |

Modified clCreateSubBuffer(cl_mem, cl_mem_flags, cl_buffer_create_type, UnsafePointer<Void>, UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateSubBuffer(_ _: cl_mem, _ _: cl_mem_flags, _ _: cl_buffer_create_type, _ _: ConstUnsafePointer<()>, _ _: UnsafePointer<cl_int>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func clCreateSubBuffer(_ _: cl_mem, _ _: cl_mem_flags, _ _: cl_buffer_create_type, _ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` | OS X 10.7 |

Modified clCreateSubDevices(cl_device_id, UnsafePointer<cl_device_partition_property>, cl_uint, UnsafeMutablePointer<cl_device_id>, UnsafeMutablePointer<cl_uint>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateSubDevices(_ _: cl_device_id, _ _: ConstUnsafePointer<cl_device_partition_property>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<cl_uint>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clCreateSubDevices(_ _: cl_device_id, _ _: UnsafePointer<cl_device_partition_property>, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_device_id>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` | OS X 10.8 |

Modified clCreateUserEvent(cl_context, UnsafeMutablePointer<cl_int>) -> cl_event

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clCreateUserEvent(_ _: cl_context, _ _: UnsafePointer<cl_int>) -> cl_event ``` | OS X 10.10 |
| To | ``` func clCreateUserEvent(_ _: cl_context, _ _: UnsafeMutablePointer<cl_int>) -> cl_event ``` | OS X 10.7 |

Modified clEnqueueAcquireGLObjects(cl_command_queue, cl_uint, UnsafePointer<cl_mem>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueAcquireGLObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: ConstUnsafePointer<cl_mem>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueAcquireGLObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueBarrierWithWaitList(cl_command_queue, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueBarrierWithWaitList(_ _: cl_command_queue, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueBarrierWithWaitList(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.8 |

Modified clEnqueueCopyBuffer(cl_command_queue, cl_mem, cl_mem, Int, Int, Int, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueCopyBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UInt, _ _: UInt, _ _: UInt, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueCopyBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueCopyBufferRect(cl_command_queue, cl_mem, cl_mem, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>, Int, Int, Int, Int, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueCopyBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UInt, _ _: UInt, _ _: UInt, _ _: UInt, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueCopyBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.7 |

Modified clEnqueueCopyBufferToImage(cl_command_queue, cl_mem, cl_mem, Int, UnsafePointer<Int>, UnsafePointer<Int>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueCopyBufferToImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UInt, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueCopyBufferToImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: Int, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueCopyImage(cl_command_queue, cl_mem, cl_mem, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueCopyImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueCopyImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueCopyImageToBuffer(cl_command_queue, cl_mem, cl_mem, UnsafePointer<Int>, UnsafePointer<Int>, Int, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueCopyImageToBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UInt, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueCopyImageToBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueFillBuffer(cl_command_queue, cl_mem, UnsafePointer<Void>, Int, Int, Int, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueFillBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: ConstUnsafePointer<()>, _ _: UInt, _ _: UInt, _ _: UInt, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueFillBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.8 |

Modified clEnqueueFillImage(cl_command_queue, cl_mem, UnsafePointer<Void>, UnsafePointer<Int>, UnsafePointer<Int>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueFillImage(_ _: cl_command_queue, _ _: cl_mem, _ _: ConstUnsafePointer<()>, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueFillImage(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafePointer<Void>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.8 |

Modified clEnqueueMapBuffer(cl_command_queue, cl_mem, cl_bool, cl_map_flags, Int, Int, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>, UnsafeMutablePointer<cl_int>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueMapBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: cl_map_flags, _ _: UInt, _ _: UInt, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>, _ _: UnsafePointer<cl_int>) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func clEnqueueMapBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: cl_map_flags, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>, _ _: UnsafeMutablePointer<cl_int>) -> UnsafeMutablePointer<Void> ``` | OS X 10.6 |

Modified clEnqueueMapImage(cl_command_queue, cl_mem, cl_bool, cl_map_flags, UnsafePointer<Int>, UnsafePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>, UnsafeMutablePointer<cl_int>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueMapImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: cl_map_flags, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UnsafePointer<UInt>, _ _: UnsafePointer<UInt>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>, _ _: UnsafePointer<cl_int>) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func clEnqueueMapImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: cl_map_flags, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>, _ _: UnsafeMutablePointer<cl_int>) -> UnsafeMutablePointer<Void> ``` | OS X 10.6 |

Modified clEnqueueMarkerWithWaitList(cl_command_queue, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueMarkerWithWaitList(_ _: cl_command_queue, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueMarkerWithWaitList(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.8 |

Modified clEnqueueMigrateMemObjects(cl_command_queue, cl_uint, UnsafePointer<cl_mem>, cl_mem_migration_flags, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueMigrateMemObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: ConstUnsafePointer<cl_mem>, _ _: cl_mem_migration_flags, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueMigrateMemObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: cl_mem_migration_flags, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.8 |

Modified clEnqueueNDRangeKernel(cl_command_queue, cl_kernel, cl_uint, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueNDRangeKernel(_ _: cl_command_queue, _ _: cl_kernel, _ _: cl_uint, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueNDRangeKernel(_ _: cl_command_queue, _ _: cl_kernel, _ _: cl_uint, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueNativeKernel(cl_command_queue, CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, Int, cl_uint, UnsafePointer<cl_mem>, UnsafeMutablePointer<UnsafePointer<Void>>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueNativeKernel(_ _: cl_command_queue, _ _: CFunctionPointer<((UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>, _ _: UInt, _ _: cl_uint, _ _: ConstUnsafePointer<cl_mem>, _ _: UnsafePointer<ConstUnsafePointer<()>>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueNativeKernel(_ _: cl_command_queue, _ _: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: UnsafeMutablePointer<UnsafePointer<Void>>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueReadBuffer(cl_command_queue, cl_mem, cl_bool, Int, Int, UnsafeMutablePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueReadBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UInt, _ _: UInt, _ _: UnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueReadBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueReadBufferRect(cl_command_queue, cl_mem, cl_bool, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>, Int, Int, Int, Int, UnsafeMutablePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueReadBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UInt, _ _: UInt, _ _: UInt, _ _: UInt, _ _: UnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueReadBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.7 |

Modified clEnqueueReadImage(cl_command_queue, cl_mem, cl_bool, UnsafePointer<Int>, UnsafePointer<Int>, Int, Int, UnsafeMutablePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueReadImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UInt, _ _: UInt, _ _: UnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueReadImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueReleaseGLObjects(cl_command_queue, cl_uint, UnsafePointer<cl_mem>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueReleaseGLObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: ConstUnsafePointer<cl_mem>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueReleaseGLObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueTask(cl_command_queue, cl_kernel, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueTask(_ _: cl_command_queue, _ _: cl_kernel, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueTask(_ _: cl_command_queue, _ _: cl_kernel, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueUnmapMemObject(cl_command_queue, cl_mem, UnsafeMutablePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueUnmapMemObject(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueUnmapMemObject(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueWriteBuffer(cl_command_queue, cl_mem, cl_bool, Int, Int, UnsafePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueWriteBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UInt, _ _: UInt, _ _: ConstUnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueWriteBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: Int, _ _: Int, _ _: UnsafePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clEnqueueWriteBufferRect(cl_command_queue, cl_mem, cl_bool, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>, Int, Int, Int, Int, UnsafePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueWriteBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UInt, _ _: UInt, _ _: UInt, _ _: UInt, _ _: ConstUnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueWriteBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: UnsafePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.7 |

Modified clEnqueueWriteImage(cl_command_queue, cl_mem, cl_bool, UnsafePointer<Int>, UnsafePointer<Int>, Int, Int, UnsafePointer<Void>, cl_uint, UnsafePointer<cl_event>, UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clEnqueueWriteImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: ConstUnsafePointer<UInt>, _ _: ConstUnsafePointer<UInt>, _ _: UInt, _ _: UInt, _ _: ConstUnsafePointer<()>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_event>, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clEnqueueWriteImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: UnsafePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified clFinish() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clFlush() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clGetCommandQueueInfo(cl_command_queue, cl_command_queue_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetCommandQueueInfo(_ _: cl_command_queue, _ _: cl_command_queue_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetCommandQueueInfo(_ _: cl_command_queue, _ _: cl_command_queue_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetContextInfo(cl_context, cl_context_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetContextInfo(_ _: cl_context, _ _: cl_context_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetContextInfo(_ _: cl_context, _ _: cl_context_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetDAGNodeAPPLE(cl_dag, cl_kernel, UnsafeMutablePointer<cl_dag_node>, UnsafeMutablePointer<UInt32>, UInt32) -> cl_dag_node

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetDAGNodeAPPLE(_ d: cl_dag, _ f: cl_kernel, _ args: UnsafePointer<cl_dag_node>, _ arg_indices: UnsafePointer<UInt32>, _ nargs: UInt32) -> cl_dag_node ``` | OS X 10.10 |
| To | ``` func clGetDAGNodeAPPLE(_ d: cl_dag, _ f: cl_kernel, _ args: UnsafeMutablePointer<cl_dag_node>, _ arg_indices: UnsafeMutablePointer<UInt32>, _ nargs: UInt32) -> cl_dag_node ``` | OS X 10.8 |

Modified clGetDeviceIDs(cl_platform_id, cl_device_type, cl_uint, UnsafeMutablePointer<cl_device_id>, UnsafeMutablePointer<cl_uint>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetDeviceIDs(_ _: cl_platform_id, _ _: cl_device_type, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<cl_uint>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetDeviceIDs(_ _: cl_platform_id, _ _: cl_device_type, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_device_id>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` | OS X 10.6 |

Modified clGetDeviceInfo(cl_device_id, cl_device_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetDeviceInfo(_ _: cl_device_id, _ _: cl_device_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetDeviceInfo(_ _: cl_device_id, _ _: cl_device_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetEventInfo(cl_event, cl_event_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetEventInfo(_ _: cl_event, _ _: cl_event_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetEventInfo(_ _: cl_event, _ _: cl_event_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetEventProfilingInfo(cl_event, cl_profiling_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetEventProfilingInfo(_ _: cl_event, _ _: cl_profiling_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetEventProfilingInfo(_ _: cl_event, _ _: cl_profiling_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetExtensionFunctionAddressForPlatform(cl_platform_id, UnsafePointer<Int8>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetExtensionFunctionAddressForPlatform(_ _: cl_platform_id, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func clGetExtensionFunctionAddressForPlatform(_ _: cl_platform_id, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Void> ``` | OS X 10.8 |

Modified clGetGLContextInfoAPPLE(cl_context, UnsafeMutablePointer<Void>, cl_gl_platform_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetGLContextInfoAPPLE(_ _: cl_context, _ _: UnsafePointer<()>, _ _: cl_gl_platform_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetGLContextInfoAPPLE(_ _: cl_context, _ _: UnsafeMutablePointer<Void>, _ _: cl_gl_platform_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetGLObjectInfo(cl_mem, UnsafeMutablePointer<cl_gl_object_type>, UnsafeMutablePointer<cl_GLuint>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetGLObjectInfo(_ _: cl_mem, _ _: UnsafePointer<cl_gl_object_type>, _ _: UnsafePointer<cl_GLuint>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetGLObjectInfo(_ _: cl_mem, _ _: UnsafeMutablePointer<cl_gl_object_type>, _ _: UnsafeMutablePointer<cl_GLuint>) -> cl_int ``` | OS X 10.6 |

Modified clGetGLTextureInfo(cl_mem, cl_gl_texture_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetGLTextureInfo(_ _: cl_mem, _ _: cl_gl_texture_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetGLTextureInfo(_ _: cl_mem, _ _: cl_gl_texture_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetImageInfo(cl_mem, cl_image_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetImageInfo(_ _: cl_mem, _ _: cl_image_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetImageInfo(_ _: cl_mem, _ _: cl_image_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetKernelArgInfo(cl_kernel, cl_uint, cl_kernel_arg_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetKernelArgInfo(_ _: cl_kernel, _ _: cl_uint, _ _: cl_kernel_arg_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetKernelArgInfo(_ _: cl_kernel, _ _: cl_uint, _ _: cl_kernel_arg_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.8 |

Modified clGetKernelInfo(cl_kernel, cl_kernel_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetKernelInfo(_ _: cl_kernel, _ _: cl_kernel_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetKernelInfo(_ _: cl_kernel, _ _: cl_kernel_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetKernelWorkGroupInfo(cl_kernel, cl_device_id, cl_kernel_work_group_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetKernelWorkGroupInfo(_ _: cl_kernel, _ _: cl_device_id, _ _: cl_kernel_work_group_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetKernelWorkGroupInfo(_ _: cl_kernel, _ _: cl_device_id, _ _: cl_kernel_work_group_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetMemObjectInfo(cl_mem, cl_mem_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetMemObjectInfo(_ _: cl_mem, _ _: cl_mem_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetMemObjectInfo(_ _: cl_mem, _ _: cl_mem_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetPlatformIDs(cl_uint, UnsafeMutablePointer<cl_platform_id>, UnsafeMutablePointer<cl_uint>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetPlatformIDs(_ _: cl_uint, _ _: UnsafePointer<cl_platform_id>, _ _: UnsafePointer<cl_uint>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetPlatformIDs(_ _: cl_uint, _ _: UnsafeMutablePointer<cl_platform_id>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` | OS X 10.6 |

Modified clGetPlatformInfo(cl_platform_id, cl_platform_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetPlatformInfo(_ _: cl_platform_id, _ _: cl_platform_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetPlatformInfo(_ _: cl_platform_id, _ _: cl_platform_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetProgramBuildInfo(cl_program, cl_device_id, cl_program_build_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetProgramBuildInfo(_ _: cl_program, _ _: cl_device_id, _ _: cl_program_build_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetProgramBuildInfo(_ _: cl_program, _ _: cl_device_id, _ _: cl_program_build_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetProgramInfo(cl_program, cl_program_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetProgramInfo(_ _: cl_program, _ _: cl_program_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetProgramInfo(_ _: cl_program, _ _: cl_program_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetSamplerInfo(cl_sampler, cl_sampler_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetSamplerInfo(_ _: cl_sampler, _ _: cl_sampler_info, _ _: UInt, _ _: UnsafePointer<()>, _ _: UnsafePointer<UInt>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetSamplerInfo(_ _: cl_sampler, _ _: cl_sampler_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` | OS X 10.6 |

Modified clGetSupportedImageFormats(cl_context, cl_mem_flags, cl_mem_object_type, cl_uint, UnsafeMutablePointer<cl_image_format>, UnsafeMutablePointer<cl_uint>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clGetSupportedImageFormats(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_mem_object_type, _ _: cl_uint, _ _: UnsafePointer<cl_image_format>, _ _: UnsafePointer<cl_uint>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clGetSupportedImageFormats(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_mem_object_type, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_image_format>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` | OS X 10.6 |

Modified clLinkProgram(cl_context, cl_uint, UnsafePointer<cl_device_id>, UnsafePointer<Int8>, cl_uint, UnsafePointer<cl_program>, CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<cl_int>) -> cl_program

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clLinkProgram(_ _: cl_context, _ _: cl_uint, _ _: ConstUnsafePointer<cl_device_id>, _ _: ConstUnsafePointer<Int8>, _ _: cl_uint, _ _: ConstUnsafePointer<cl_program>, _ _: CFunctionPointer<((cl_program, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>, _ _: UnsafePointer<cl_int>) -> cl_program ``` | OS X 10.10 |
| To | ``` func clLinkProgram(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` | OS X 10.8 |

Modified clLogMessagesToStderrAPPLE(UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clLogMessagesToStderrAPPLE(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<()>, _ _: UInt, _ _: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func clLogMessagesToStderrAPPLE(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Void>) ``` | OS X 10.6 |

Modified clLogMessagesToStdoutAPPLE(UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clLogMessagesToStdoutAPPLE(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<()>, _ _: UInt, _ _: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func clLogMessagesToStdoutAPPLE(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Void>) ``` | OS X 10.6 |

Modified clLogMessagesToSystemLogAPPLE(UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clLogMessagesToSystemLogAPPLE(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<()>, _ _: UInt, _ _: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func clLogMessagesToSystemLogAPPLE(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Void>) ``` | OS X 10.6 |

Modified clReleaseCommandQueue() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clReleaseContext() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clReleaseDAGAPPLE(cl_dag)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified clReleaseDevice() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified clReleaseEvent() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clReleaseKernel() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clReleaseMemObject() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clReleaseProgram() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clReleaseSampler() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainCommandQueue() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainContext() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainDevice() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified clRetainEvent() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainKernel() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainMemObject() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainProgram() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clRetainSampler() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified clSetEventCallback(cl_event, cl_int, CFunctionPointer<((cl_event, cl_int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clSetEventCallback(_ _: cl_event, _ _: cl_int, _ _: CFunctionPointer<((cl_event, cl_int, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clSetEventCallback(_ _: cl_event, _ _: cl_int, _ _: CFunctionPointer<((cl_event, cl_int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` | OS X 10.7 |

Modified clSetKernelArg(cl_kernel, cl_uint, Int, UnsafePointer<Void>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clSetKernelArg(_ _: cl_kernel, _ _: cl_uint, _ _: UInt, _ _: ConstUnsafePointer<()>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clSetKernelArg(_ _: cl_kernel, _ _: cl_uint, _ _: Int, _ _: UnsafePointer<Void>) -> cl_int ``` | OS X 10.6 |

Modified clSetKernelArgByNameAPPLE(cl_kernel, UnsafePointer<Int8>, Int, UnsafePointer<Void>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clSetKernelArgByNameAPPLE(_ _: cl_kernel, _ _: ConstUnsafePointer<Int8>, _ _: UInt, _ _: ConstUnsafePointer<()>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clSetKernelArgByNameAPPLE(_ _: cl_kernel, _ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafePointer<Void>) -> cl_int ``` | OS X 10.7 |

Modified clSetKernelArgsVaListAPPLE(cl_kernel, cl_uint, CVaListPointer) -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified clSetMemObjectDestructorCallback(cl_mem, CFunctionPointer<((cl_mem, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem, _ _: CFunctionPointer<((cl_mem, UnsafePointer<()>) -> Void)>, _ _: UnsafePointer<()>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem, _ _: CFunctionPointer<((cl_mem, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` | OS X 10.7 |

Modified clSetUserEventStatus(cl_event, cl_int) -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified clUnloadPlatformCompiler() -> cl_int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified clWaitForEvents(cl_uint, UnsafePointer<cl_event>) -> cl_int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clWaitForEvents(_ _: cl_uint, _ _: ConstUnsafePointer<cl_event>) -> cl_int ``` | OS X 10.10 |
| To | ``` func clWaitForEvents(_ _: cl_uint, _ _: UnsafePointer<cl_event>) -> cl_int ``` | OS X 10.6 |

Modified gcl_copy_image(cl_image, cl_image, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_copy_image(_ dst_image: cl_image, _ src_image: cl_image, _ dst_origin: ConstUnsafePointer<UInt>, _ src_origin: ConstUnsafePointer<UInt>, _ region: ConstUnsafePointer<UInt>) ``` | OS X 10.10 |
| To | ``` func gcl_copy_image(_ dst_image: cl_image, _ src_image: cl_image, _ dst_origin: UnsafePointer<Int>, _ src_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) ``` | OS X 10.7 |

Modified gcl_copy_image_to_ptr(UnsafeMutablePointer<Void>, cl_image, UnsafePointer<Int>, UnsafePointer<Int>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_copy_image_to_ptr(_ dst_ptr: UnsafePointer<()>, _ src_image: cl_image, _ src_origin: ConstUnsafePointer<UInt>, _ region: ConstUnsafePointer<UInt>) ``` | OS X 10.10 |
| To | ``` func gcl_copy_image_to_ptr(_ dst_ptr: UnsafeMutablePointer<Void>, _ src_image: cl_image, _ src_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) ``` | OS X 10.7 |

Modified gcl_copy_ptr_to_image(cl_mem, UnsafeMutablePointer<Void>, UnsafePointer<Int>, UnsafePointer<Int>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_copy_ptr_to_image(_ dst_image: cl_mem, _ src_ptr: UnsafePointer<()>, _ dst_origin: ConstUnsafePointer<UInt>, _ region: ConstUnsafePointer<UInt>) ``` | OS X 10.10 |
| To | ``` func gcl_copy_ptr_to_image(_ dst_image: cl_mem, _ src_ptr: UnsafeMutablePointer<Void>, _ dst_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) ``` | OS X 10.7 |

Modified gcl_create_buffer_from_ptr(UnsafeMutablePointer<Void>) -> cl_mem

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_create_buffer_from_ptr(_ ptr: UnsafePointer<()>) -> cl_mem ``` | OS X 10.10 |
| To | ``` func gcl_create_buffer_from_ptr(_ ptr: UnsafeMutablePointer<Void>) -> cl_mem ``` | OS X 10.7 |

Modified gcl_create_dispatch_queue(cl_queue_flags, cl_device_id) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_create_image(UnsafePointer<cl_image_format>, Int, Int, Int, IOSurface!) -> cl_image

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_create_image(_ image_format: ConstUnsafePointer<cl_image_format>, _ image_width: UInt, _ image_height: UInt, _ image_depth: UInt, _ io_surface: IOSurface!) -> cl_image ``` | OS X 10.10 |
| To | ``` func gcl_create_image(_ image_format: UnsafePointer<cl_image_format>, _ image_width: Int, _ image_height: Int, _ image_depth: Int, _ io_surface: IOSurface!) -> cl_image ``` | OS X 10.7 |

Modified gcl_create_kernel_from_block(UnsafeMutablePointer<Void>) -> cl_kernel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_create_kernel_from_block(_ kernel_block_ptr: UnsafePointer<()>) -> cl_kernel ``` | OS X 10.10 |
| To | ``` func gcl_create_kernel_from_block(_ kernel_block_ptr: UnsafeMutablePointer<Void>) -> cl_kernel ``` | OS X 10.7 |

Modified gcl_free(UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_free(_ ptr: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func gcl_free(_ ptr: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified gcl_get_context() -> cl_context

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_get_device_id_with_dispatch_queue(dispatch_queue_t!) -> cl_device_id

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_get_kernel_block_workgroup_info(UnsafeMutablePointer<Void>, cl_kernel_work_group_info, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_get_kernel_block_workgroup_info(_ kernel_block_ptr: UnsafePointer<()>, _ param_name: cl_kernel_work_group_info, _ param_value_size: UInt, _ param_value: UnsafePointer<()>, _ param_value_size_ret: UnsafePointer<UInt>) ``` | OS X 10.10 |
| To | ``` func gcl_get_kernel_block_workgroup_info(_ kernel_block_ptr: UnsafeMutablePointer<Void>, _ param_name: cl_kernel_work_group_info, _ param_value_size: Int, _ param_value: UnsafeMutablePointer<Void>, _ param_value_size_ret: UnsafeMutablePointer<Int>) ``` | OS X 10.7 |

Modified gcl_get_supported_image_formats(cl_device_id, cl_image_type, UInt32, UnsafeMutablePointer<cl_image_format>, UnsafeMutablePointer<UInt32>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_get_supported_image_formats(_ device_id: cl_device_id, _ image_type: cl_image_type, _ num_entries: UInt32, _ image_formats: UnsafePointer<cl_image_format>, _ num_image_formats: UnsafePointer<UInt32>) ``` | OS X 10.10 |
| To | ``` func gcl_get_supported_image_formats(_ device_id: cl_device_id, _ image_type: cl_image_type, _ num_entries: UInt32, _ image_formats: UnsafeMutablePointer<cl_image_format>, _ num_image_formats: UnsafeMutablePointer<UInt32>) ``` | OS X 10.7 |

Modified gcl_gl_create_image_from_renderbuffer(GLuint) -> cl_image

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_gl_create_image_from_texture(GLenum, GLint, GLuint) -> cl_image

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_gl_create_ptr_from_buffer(GLuint) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_gl_create_ptr_from_buffer(_ bufobj: GLuint) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func gcl_gl_create_ptr_from_buffer(_ bufobj: GLuint) -> UnsafeMutablePointer<Void> ``` | OS X 10.7 |

Modified gcl_gl_set_sharegroup(UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_gl_set_sharegroup(_ share: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func gcl_gl_set_sharegroup(_ share: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified gcl_malloc(Int, UnsafeMutablePointer<Void>, cl_malloc_flags) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_malloc(_ bytes: UInt, _ host_ptr: UnsafePointer<()>, _ flags: cl_malloc_flags) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func gcl_malloc(_ bytes: Int, _ host_ptr: UnsafeMutablePointer<Void>, _ flags: cl_malloc_flags) -> UnsafeMutablePointer<Void> ``` | OS X 10.7 |

Modified gcl_map_image(cl_image, cl_map_flags, UnsafePointer<Int>, UnsafePointer<Int>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_map_image(_ image: cl_image, _ map_flags: cl_map_flags, _ origin: ConstUnsafePointer<UInt>, _ region: ConstUnsafePointer<UInt>) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func gcl_map_image(_ image: cl_image, _ map_flags: cl_map_flags, _ origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) -> UnsafeMutablePointer<Void> ``` | OS X 10.7 |

Modified gcl_map_ptr(UnsafeMutablePointer<Void>, cl_map_flags, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_map_ptr(_ ptr: UnsafePointer<()>, _ map_flags: cl_map_flags, _ cb: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func gcl_map_ptr(_ ptr: UnsafeMutablePointer<Void>, _ map_flags: cl_map_flags, _ cb: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.7 |

Modified gcl_memcpy(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_memcpy(_ dst: UnsafePointer<()>, _ src: ConstUnsafePointer<()>, _ size: UInt) ``` | OS X 10.10 |
| To | ``` func gcl_memcpy(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ size: Int) ``` | OS X 10.7 |

Modified gcl_memcpy_rect(UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Int>, UnsafePointer<Int>, UnsafePointer<Int>, Int, Int, Int, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_memcpy_rect(_ dst: UnsafePointer<()>, _ src: ConstUnsafePointer<()>, _ dst_origin: ConstUnsafePointer<UInt>, _ src_origin: ConstUnsafePointer<UInt>, _ region: ConstUnsafePointer<UInt>, _ dst_row_pitch: UInt, _ dst_slice_pitch: UInt, _ src_row_pitch: UInt, _ src_slice_pitch: UInt) ``` | OS X 10.10 |
| To | ``` func gcl_memcpy_rect(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ dst_origin: UnsafePointer<Int>, _ src_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>, _ dst_row_pitch: Int, _ dst_slice_pitch: Int, _ src_row_pitch: Int, _ src_slice_pitch: Int) ``` | OS X 10.7 |

Modified gcl_release_image(cl_image)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_retain_image(cl_image)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_set_finalizer(UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_set_finalizer(_ object: UnsafePointer<()>, _ cl_pfn_finalizer: CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>) -> Void)>, _ user_data: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func gcl_set_finalizer(_ object: UnsafeMutablePointer<Void>, _ cl_pfn_finalizer: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>, _ user_data: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified gcl_start_timer() -> cl_timer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_stop_timer(cl_timer) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gcl_unmap()

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gcl_unmap(_ _: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func gcl_unmap(_ _: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

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
