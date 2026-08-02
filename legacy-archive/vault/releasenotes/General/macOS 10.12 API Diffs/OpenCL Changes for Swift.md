---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/OpenCL.html
archived_at: '2026-07-18T02:51:31.675982Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# OpenCL Changes for Swift

### OpenCL

Removed clSetKernelArgsListAPPLE(_: cl_kernel, _: cl_uint, _: CVarArgType) -> cl_intAdded CL_DEVICE_TYPE_USE_IDAdded CL_DISPATCH_QUEUE_PRIORITY_BACKGROUNDAdded CL_DISPATCH_QUEUE_PRIORITY_DEFAULTAdded CL_DISPATCH_QUEUE_PRIORITY_HIGHAdded CL_DISPATCH_QUEUE_PRIORITY_LOWAdded CL_LONG_MAXAdded CL_ULONG_MAXAdded clSetKernelArgsListAPPLE(_: cl_kernel, _: cl_uint, _: CVarArg) -> cl_intModified cl_command_queue

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_command_queue = COpaquePointer ``` |
| To | ``` typealias cl_command_queue = OpaquePointer ``` |

Modified cl_context

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_context = COpaquePointer ``` |
| To | ``` typealias cl_context = OpaquePointer ``` |

Modified cl_dag

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_dag = COpaquePointer ``` |
| To | ``` typealias cl_dag = OpaquePointer ``` |

Modified cl_event

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_event = COpaquePointer ``` |
| To | ``` typealias cl_event = OpaquePointer ``` |

Modified cl_GLsync

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_GLsync = COpaquePointer ``` |
| To | ``` typealias cl_GLsync = OpaquePointer ``` |

Modified cl_kernel

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_kernel = COpaquePointer ``` |
| To | ``` typealias cl_kernel = OpaquePointer ``` |

Modified cl_mem

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_mem = COpaquePointer ``` |
| To | ``` typealias cl_mem = OpaquePointer ``` |

Modified cl_platform_id

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_platform_id = COpaquePointer ``` |
| To | ``` typealias cl_platform_id = OpaquePointer ``` |

Modified cl_program

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_program = COpaquePointer ``` |
| To | ``` typealias cl_program = OpaquePointer ``` |

Modified cl_sampler

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_sampler = COpaquePointer ``` |
| To | ``` typealias cl_sampler = OpaquePointer ``` |

Modified clBuildProgram(_: cl_program!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: ( (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clBuildProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clBuildProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: (@escaping (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clCompileProgram(_: cl_program!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: cl_uint, _: UnsafePointer<cl_program?>!, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: ( (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCompileProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clCompileProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafePointer<cl_program?>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: (@escaping (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clCreateBuffer(_: cl_context!, _: cl_mem_flags, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_mem!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateBuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateBuffer(_ _: cl_context!, _ _: cl_mem_flags, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_mem! ``` |

Modified clCreateCommandQueue(_: cl_context!, _: cl_device_id!, _: cl_command_queue_properties, _: UnsafeMutablePointer<cl_int>!) -> cl_command_queue!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateCommandQueue(_ _: cl_context, _ _: cl_device_id, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_int>) -> cl_command_queue ``` |
| To | ``` func clCreateCommandQueue(_ _: cl_context!, _ _: cl_device_id!, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_int>!) -> cl_command_queue! ``` |

Modified clCreateCommandQueueWithPropertiesAPPLE(_: cl_context!, _: cl_device_id!, _: UnsafePointer<cl_queue_properties_APPLE>!, _: UnsafeMutablePointer<cl_int>!) -> cl_command_queue!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateCommandQueueWithPropertiesAPPLE(_ _: cl_context, _ _: cl_device_id, _ _: UnsafePointer<cl_queue_properties_APPLE>, _ _: UnsafeMutablePointer<cl_int>) -> cl_command_queue ``` |
| To | ``` func clCreateCommandQueueWithPropertiesAPPLE(_ _: cl_context!, _ _: cl_device_id!, _ _: UnsafePointer<cl_queue_properties_APPLE>!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_command_queue! ``` |

Modified clCreateContext(_: UnsafePointer<cl_context_properties>!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: ( (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_context!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` |
| To | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_context! ``` |

Modified clCreateContextAndCommandQueueAPPLE(_: UnsafePointer<cl_context_properties>!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: ( (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: cl_command_queue_properties, _: UnsafeMutablePointer<cl_context?>!, _: UnsafeMutablePointer<cl_command_queue?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context>, _ _: UnsafeMutablePointer<cl_command_queue>) -> cl_int ``` |
| To | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context?>!, _ _: UnsafeMutablePointer<cl_command_queue?>!) -> cl_int ``` |

Modified clCreateContextFromType(_: UnsafePointer<cl_context_properties>!, _: cl_device_type, _: ( (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_context!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>, _ _: cl_device_type, _ _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` |
| To | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_device_type, _ _: (@escaping (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_context! ``` |

Modified clCreateDAGAPPLE(_: cl_context!) -> cl_dag!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateDAGAPPLE(_ c: cl_context) -> cl_dag ``` |
| To | ``` func clCreateDAGAPPLE(_ c: cl_context!) -> cl_dag! ``` |

Modified clCreateEventFromGLsyncKHR(_: cl_context, _: cl_GLsync, _: UnsafeMutablePointer<cl_int>?) -> cl_event?

|  | Declaration |
| --- | --- |
| From | ``` func clCreateEventFromGLsyncKHR(_ _: cl_context, _ _: cl_GLsync, _ _: UnsafeMutablePointer<cl_int>) -> cl_event ``` |
| To | ``` func clCreateEventFromGLsyncKHR(_ _: cl_context, _ _: cl_GLsync, _ _: UnsafeMutablePointer<cl_int>?) -> cl_event? ``` |

Modified clCreateFromGLBuffer(_: cl_context!, _: cl_mem_flags, _: cl_GLuint, _: UnsafeMutablePointer<Int32>!) -> cl_mem!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateFromGLBuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafeMutablePointer<Int32>) -> cl_mem ``` |
| To | ``` func clCreateFromGLBuffer(_ _: cl_context!, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafeMutablePointer<Int32>!) -> cl_mem! ``` |

Modified clCreateFromGLRenderbuffer(_: cl_context!, _: cl_mem_flags, _: cl_GLuint, _: UnsafeMutablePointer<cl_int>!) -> cl_mem!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateFromGLRenderbuffer(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateFromGLRenderbuffer(_ _: cl_context!, _ _: cl_mem_flags, _ _: cl_GLuint, _ _: UnsafeMutablePointer<cl_int>!) -> cl_mem! ``` |

Modified clCreateFromGLTexture(_: cl_context!, _: cl_mem_flags, _: cl_GLenum, _: cl_GLint, _: cl_GLuint, _: UnsafeMutablePointer<cl_int>!) -> cl_mem!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateFromGLTexture(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_GLenum, _ _: cl_GLint, _ _: cl_GLuint, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateFromGLTexture(_ _: cl_context!, _ _: cl_mem_flags, _ _: cl_GLenum, _ _: cl_GLint, _ _: cl_GLuint, _ _: UnsafeMutablePointer<cl_int>!) -> cl_mem! ``` |

Modified clCreateImage(_: cl_context!, _: cl_mem_flags, _: UnsafePointer<cl_image_format>!, _: UnsafePointer<cl_image_desc>!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_mem!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateImage(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: UnsafePointer<cl_image_desc>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateImage(_ _: cl_context!, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>!, _ _: UnsafePointer<cl_image_desc>!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_mem! ``` |

Modified clCreateImageFromIOSurface2DAPPLE(_: cl_context, _: cl_mem_flags, _: UnsafePointer<cl_image_format>, _: Int, _: Int, _: IOSurfaceRef, _: UnsafeMutablePointer<cl_int>?) -> cl_mem?

|  | Declaration |
| --- | --- |
| From | ``` func clCreateImageFromIOSurface2DAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: Int, _ _: Int, _ _: IOSurface, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateImageFromIOSurface2DAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: Int, _ _: Int, _ _: IOSurfaceRef, _ _: UnsafeMutablePointer<cl_int>?) -> cl_mem? ``` |

Modified clCreateImageFromIOSurfaceWithPropertiesAPPLE(_: cl_context, _: cl_mem_flags, _: UnsafePointer<cl_image_format>, _: UnsafePointer<cl_image_desc>, _: UnsafeMutablePointer<cl_iosurface_properties_APPLE>, _: UnsafeMutablePointer<cl_int>?) -> cl_mem?

|  | Declaration |
| --- | --- |
| From | ``` func clCreateImageFromIOSurfaceWithPropertiesAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: UnsafePointer<cl_image_desc>, _ _: UnsafeMutablePointer<cl_iosurface_properties_APPLE>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateImageFromIOSurfaceWithPropertiesAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: UnsafePointer<cl_image_desc>, _ _: UnsafeMutablePointer<cl_iosurface_properties_APPLE>, _ _: UnsafeMutablePointer<cl_int>?) -> cl_mem? ``` |

Modified clCreateKernel(_: cl_program!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<cl_int>!) -> cl_kernel!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateKernel(_ _: cl_program, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<cl_int>) -> cl_kernel ``` |
| To | ``` func clCreateKernel(_ _: cl_program!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_kernel! ``` |

Modified clCreateKernelFromDAGAPPLE(_: cl_dag!, _: cl_uint, _: UnsafePointer<cl_device_id?>!) -> cl_kernel!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateKernelFromDAGAPPLE(_ d: cl_dag, _ n: cl_uint, _ list: UnsafePointer<cl_device_id>) -> cl_kernel ``` |
| To | ``` func clCreateKernelFromDAGAPPLE(_ d: cl_dag!, _ n: cl_uint, _ list: UnsafePointer<cl_device_id?>!) -> cl_kernel! ``` |

Modified clCreateKernelsInProgram(_: cl_program!, _: cl_uint, _: UnsafeMutablePointer<cl_kernel?>!, _: UnsafeMutablePointer<cl_uint>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCreateKernelsInProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_kernel>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` |
| To | ``` func clCreateKernelsInProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_kernel?>!, _ _: UnsafeMutablePointer<cl_uint>!) -> cl_int ``` |

Modified clCreateProgramAndKernelsWithSourceAPPLE(_: cl_context!, _: cl_uint, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: UnsafePointer<Int>!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: cl_uint, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: UnsafeMutablePointer<cl_program?>!, _: UnsafeMutablePointer<cl_kernel?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCreateProgramAndKernelsWithSourceAPPLE(_ _: cl_context, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UnsafeMutablePointer<cl_program>, _ _: UnsafeMutablePointer<cl_kernel>) -> cl_int ``` |
| To | ``` func clCreateProgramAndKernelsWithSourceAPPLE(_ _: cl_context!, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: UnsafePointer<Int>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: UnsafeMutablePointer<cl_program?>!, _ _: UnsafeMutablePointer<cl_kernel?>!) -> cl_int ``` |

Modified clCreateProgramWithBinary(_: cl_context!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int>!, _: UnsafeMutablePointer<UnsafePointer<UInt8>?>!, _: UnsafeMutablePointer<cl_int>!, _: UnsafeMutablePointer<cl_int>!) -> cl_program!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateProgramWithBinary(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int>, _ _: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ _: UnsafeMutablePointer<cl_int>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` |
| To | ``` func clCreateProgramWithBinary(_ _: cl_context!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int>!, _ _: UnsafeMutablePointer<UnsafePointer<UInt8>?>!, _ _: UnsafeMutablePointer<cl_int>!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_program! ``` |

Modified clCreateProgramWithBuiltInKernels(_: cl_context!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<cl_int>!) -> cl_program!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateProgramWithBuiltInKernels(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` |
| To | ``` func clCreateProgramWithBuiltInKernels(_ _: cl_context!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_program! ``` |

Modified clCreateProgramWithSource(_: cl_context!, _: cl_uint, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: UnsafePointer<Int>!, _: UnsafeMutablePointer<cl_int>!) -> cl_program!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateProgramWithSource(_ _: cl_context, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UnsafePointer<Int>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` |
| To | ``` func clCreateProgramWithSource(_ _: cl_context!, _ _: cl_uint, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: UnsafePointer<Int>!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_program! ``` |

Modified clCreateSampler(_: cl_context!, _: cl_bool, _: cl_addressing_mode, _: cl_filter_mode, _: UnsafeMutablePointer<cl_int>!) -> cl_sampler!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateSampler(_ _: cl_context, _ _: cl_bool, _ _: cl_addressing_mode, _ _: cl_filter_mode, _ _: UnsafeMutablePointer<cl_int>) -> cl_sampler ``` |
| To | ``` func clCreateSampler(_ _: cl_context!, _ _: cl_bool, _ _: cl_addressing_mode, _ _: cl_filter_mode, _ _: UnsafeMutablePointer<cl_int>!) -> cl_sampler! ``` |

Modified clCreateSubBuffer(_: cl_mem!, _: cl_mem_flags, _: cl_buffer_create_type, _: UnsafeRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_mem!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateSubBuffer(_ _: cl_mem, _ _: cl_mem_flags, _ _: cl_buffer_create_type, _ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateSubBuffer(_ _: cl_mem!, _ _: cl_mem_flags, _ _: cl_buffer_create_type, _ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_mem! ``` |

Modified clCreateSubDevices(_: cl_device_id!, _: UnsafePointer<cl_device_partition_property>!, _: cl_uint, _: UnsafeMutablePointer<cl_device_id?>!, _: UnsafeMutablePointer<cl_uint>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCreateSubDevices(_ _: cl_device_id, _ _: UnsafePointer<cl_device_partition_property>, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_device_id>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` |
| To | ``` func clCreateSubDevices(_ _: cl_device_id!, _ _: UnsafePointer<cl_device_partition_property>!, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_device_id?>!, _ _: UnsafeMutablePointer<cl_uint>!) -> cl_int ``` |

Modified clCreateUserEvent(_: cl_context!, _: UnsafeMutablePointer<cl_int>!) -> cl_event!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateUserEvent(_ _: cl_context, _ _: UnsafeMutablePointer<cl_int>) -> cl_event ``` |
| To | ``` func clCreateUserEvent(_ _: cl_context!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_event! ``` |

Modified clEnqueueAcquireGLObjects(_: cl_command_queue!, _: cl_uint, _: UnsafePointer<cl_mem?>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueAcquireGLObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueAcquireGLObjects(_ _: cl_command_queue!, _ _: cl_uint, _ _: UnsafePointer<cl_mem?>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueBarrierWithWaitList(_: cl_command_queue!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueBarrierWithWaitList(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueBarrierWithWaitList(_ _: cl_command_queue!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueCopyBuffer(_: cl_command_queue!, _: cl_mem!, _: cl_mem!, _: Int, _: Int, _: Int, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueCopyBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueCopyBuffer(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_mem!, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueCopyBufferRect(_: cl_command_queue!, _: cl_mem!, _: cl_mem!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: Int, _: Int, _: Int, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueCopyBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueCopyBufferRect(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_mem!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueCopyBufferToImage(_: cl_command_queue!, _: cl_mem!, _: cl_mem!, _: Int, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueCopyBufferToImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: Int, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueCopyBufferToImage(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_mem!, _ _: Int, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueCopyImage(_: cl_command_queue!, _: cl_mem!, _: cl_mem!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueCopyImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueCopyImage(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_mem!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueCopyImageToBuffer(_: cl_command_queue!, _: cl_mem!, _: cl_mem!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueCopyImageToBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_mem, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueCopyImageToBuffer(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_mem!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueFillBuffer(_: cl_command_queue!, _: cl_mem!, _: UnsafeRawPointer!, _: Int, _: Int, _: Int, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueFillBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueFillBuffer(_ _: cl_command_queue!, _ _: cl_mem!, _ _: UnsafeRawPointer!, _ _: Int, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueFillImage(_: cl_command_queue!, _: cl_mem!, _: UnsafeRawPointer!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueFillImage(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafePointer<Void>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueFillImage(_ _: cl_command_queue!, _ _: cl_mem!, _ _: UnsafeRawPointer!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueMapBuffer(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: cl_map_flags, _: Int, _: Int, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!, _: UnsafeMutablePointer<cl_int>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueMapBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: cl_map_flags, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>, _ _: UnsafeMutablePointer<cl_int>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func clEnqueueMapBuffer(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: cl_map_flags, _ _: Int, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_int>!) -> UnsafeMutableRawPointer! ``` |

Modified clEnqueueMapImage(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: cl_map_flags, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<Int>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!, _: UnsafeMutablePointer<cl_int>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueMapImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: cl_map_flags, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>, _ _: UnsafeMutablePointer<cl_int>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func clEnqueueMapImage(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: cl_map_flags, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafeMutablePointer<Int>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_int>!) -> UnsafeMutableRawPointer! ``` |

Modified clEnqueueMarkerWithWaitList(_: cl_command_queue!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueMarkerWithWaitList(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueMarkerWithWaitList(_ _: cl_command_queue!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueMigrateMemObjects(_: cl_command_queue!, _: cl_uint, _: UnsafePointer<cl_mem?>!, _: cl_mem_migration_flags, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueMigrateMemObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: cl_mem_migration_flags, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueMigrateMemObjects(_ _: cl_command_queue!, _ _: cl_uint, _ _: UnsafePointer<cl_mem?>!, _ _: cl_mem_migration_flags, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueNativeKernel(_: cl_command_queue!, _: ( (UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: Int, _: cl_uint, _: UnsafePointer<cl_mem?>!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueNativeKernel(_ _: cl_command_queue, _ _: ((UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: UnsafeMutablePointer<UnsafePointer<Void>>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueNativeKernel(_ _: cl_command_queue!, _ _: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem?>!, _ _: UnsafeMutablePointer<UnsafeRawPointer?>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueNDRangeKernel(_: cl_command_queue!, _: cl_kernel!, _: cl_uint, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueNDRangeKernel(_ _: cl_command_queue, _ _: cl_kernel, _ _: cl_uint, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueNDRangeKernel(_ _: cl_command_queue!, _ _: cl_kernel!, _ _: cl_uint, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueReadBuffer(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: Int, _: Int, _: UnsafeMutableRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueReadBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueReadBuffer(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: Int, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueReadBufferRect(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: Int, _: Int, _: Int, _: UnsafeMutableRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueReadBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueReadBufferRect(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueReadImage(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: Int, _: UnsafeMutableRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueReadImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueReadImage(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: Int, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueReleaseGLObjects(_: cl_command_queue!, _: cl_uint, _: UnsafePointer<cl_mem?>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueReleaseGLObjects(_ _: cl_command_queue, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueReleaseGLObjects(_ _: cl_command_queue!, _ _: cl_uint, _ _: UnsafePointer<cl_mem?>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueTask(_: cl_command_queue!, _: cl_kernel!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueTask(_ _: cl_command_queue, _ _: cl_kernel, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueTask(_ _: cl_command_queue!, _ _: cl_kernel!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueUnmapMemObject(_: cl_command_queue!, _: cl_mem!, _: UnsafeMutableRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueUnmapMemObject(_ _: cl_command_queue, _ _: cl_mem, _ _: UnsafeMutablePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueUnmapMemObject(_ _: cl_command_queue!, _ _: cl_mem!, _ _: UnsafeMutableRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueWriteBuffer(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: Int, _: Int, _: UnsafeRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueWriteBuffer(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: Int, _ _: Int, _ _: UnsafePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueWriteBuffer(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: Int, _ _: Int, _ _: UnsafeRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueWriteBufferRect(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: Int, _: Int, _: Int, _: UnsafeRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueWriteBufferRect(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: UnsafePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueWriteBufferRect(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: Int, _ _: Int, _ _: Int, _ _: Int, _ _: UnsafeRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clEnqueueWriteImage(_: cl_command_queue!, _: cl_mem!, _: cl_bool, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: Int, _: UnsafeRawPointer!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueWriteImage(_ _: cl_command_queue, _ _: cl_mem, _ _: cl_bool, _ _: UnsafePointer<Int>, _ _: UnsafePointer<Int>, _ _: Int, _ _: Int, _ _: UnsafePointer<Void>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueWriteImage(_ _: cl_command_queue!, _ _: cl_mem!, _ _: cl_bool, _ _: UnsafePointer<Int>!, _ _: UnsafePointer<Int>!, _ _: Int, _ _: Int, _ _: UnsafeRawPointer!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clFinish(_: cl_command_queue!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clFinish(_ _: cl_command_queue) -> cl_int ``` |
| To | ``` func clFinish(_ _: cl_command_queue!) -> cl_int ``` |

Modified clFlush(_: cl_command_queue!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clFlush(_ _: cl_command_queue) -> cl_int ``` |
| To | ``` func clFlush(_ _: cl_command_queue!) -> cl_int ``` |

Modified clGetCommandQueueInfo(_: cl_command_queue!, _: cl_command_queue_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetCommandQueueInfo(_ _: cl_command_queue, _ _: cl_command_queue_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetCommandQueueInfo(_ _: cl_command_queue!, _ _: cl_command_queue_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetContextInfo(_: cl_context!, _: cl_context_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetContextInfo(_ _: cl_context, _ _: cl_context_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetContextInfo(_ _: cl_context!, _ _: cl_context_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetDAGNodeAPPLE(_: cl_dag!, _: cl_kernel!, _: UnsafeMutablePointer<cl_dag_node>!, _: UnsafeMutablePointer<UInt32>!, _: UInt32) -> cl_dag_node

|  | Declaration |
| --- | --- |
| From | ``` func clGetDAGNodeAPPLE(_ d: cl_dag, _ f: cl_kernel, _ args: UnsafeMutablePointer<cl_dag_node>, _ arg_indices: UnsafeMutablePointer<UInt32>, _ nargs: UInt32) -> cl_dag_node ``` |
| To | ``` func clGetDAGNodeAPPLE(_ d: cl_dag!, _ f: cl_kernel!, _ args: UnsafeMutablePointer<cl_dag_node>!, _ arg_indices: UnsafeMutablePointer<UInt32>!, _ nargs: UInt32) -> cl_dag_node ``` |

Modified clGetDeviceIDs(_: cl_platform_id!, _: cl_device_type, _: cl_uint, _: UnsafeMutablePointer<cl_device_id?>!, _: UnsafeMutablePointer<cl_uint>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetDeviceIDs(_ _: cl_platform_id, _ _: cl_device_type, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_device_id>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` |
| To | ``` func clGetDeviceIDs(_ _: cl_platform_id!, _ _: cl_device_type, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_device_id?>!, _ _: UnsafeMutablePointer<cl_uint>!) -> cl_int ``` |

Modified clGetDeviceInfo(_: cl_device_id!, _: cl_device_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetDeviceInfo(_ _: cl_device_id, _ _: cl_device_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetDeviceInfo(_ _: cl_device_id!, _ _: cl_device_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetEventInfo(_: cl_event!, _: cl_event_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetEventInfo(_ _: cl_event, _ _: cl_event_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetEventInfo(_ _: cl_event!, _ _: cl_event_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetEventProfilingInfo(_: cl_event!, _: cl_profiling_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetEventProfilingInfo(_ _: cl_event, _ _: cl_profiling_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetEventProfilingInfo(_ _: cl_event!, _ _: cl_profiling_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetExtensionFunctionAddressForPlatform(_: cl_platform_id!, _: UnsafePointer<Int8>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func clGetExtensionFunctionAddressForPlatform(_ _: cl_platform_id, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func clGetExtensionFunctionAddressForPlatform(_ _: cl_platform_id!, _ _: UnsafePointer<Int8>!) -> UnsafeMutableRawPointer! ``` |

Modified clGetGLContextInfoAPPLE(_: cl_context, _: UnsafeMutableRawPointer, _: cl_gl_platform_info, _: Int, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<Int>?) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetGLContextInfoAPPLE(_ _: cl_context, _ _: UnsafeMutablePointer<Void>, _ _: cl_gl_platform_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetGLContextInfoAPPLE(_ _: cl_context, _ _: UnsafeMutableRawPointer, _ _: cl_gl_platform_info, _ _: Int, _ _: UnsafeMutableRawPointer?, _ _: UnsafeMutablePointer<Int>?) -> cl_int ``` |

Modified clGetGLObjectInfo(_: cl_mem!, _: UnsafeMutablePointer<cl_gl_object_type>!, _: UnsafeMutablePointer<cl_GLuint>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetGLObjectInfo(_ _: cl_mem, _ _: UnsafeMutablePointer<cl_gl_object_type>, _ _: UnsafeMutablePointer<cl_GLuint>) -> cl_int ``` |
| To | ``` func clGetGLObjectInfo(_ _: cl_mem!, _ _: UnsafeMutablePointer<cl_gl_object_type>!, _ _: UnsafeMutablePointer<cl_GLuint>!) -> cl_int ``` |

Modified clGetGLTextureInfo(_: cl_mem!, _: cl_gl_texture_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetGLTextureInfo(_ _: cl_mem, _ _: cl_gl_texture_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetGLTextureInfo(_ _: cl_mem!, _ _: cl_gl_texture_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetImageInfo(_: cl_mem!, _: cl_image_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetImageInfo(_ _: cl_mem, _ _: cl_image_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetImageInfo(_ _: cl_mem!, _ _: cl_image_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetKernelArgInfo(_: cl_kernel!, _: cl_uint, _: cl_kernel_arg_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetKernelArgInfo(_ _: cl_kernel, _ _: cl_uint, _ _: cl_kernel_arg_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetKernelArgInfo(_ _: cl_kernel!, _ _: cl_uint, _ _: cl_kernel_arg_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetKernelInfo(_: cl_kernel!, _: cl_kernel_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetKernelInfo(_ _: cl_kernel, _ _: cl_kernel_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetKernelInfo(_ _: cl_kernel!, _ _: cl_kernel_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetKernelWorkGroupInfo(_: cl_kernel!, _: cl_device_id!, _: cl_kernel_work_group_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetKernelWorkGroupInfo(_ _: cl_kernel, _ _: cl_device_id, _ _: cl_kernel_work_group_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetKernelWorkGroupInfo(_ _: cl_kernel!, _ _: cl_device_id!, _ _: cl_kernel_work_group_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetMemObjectInfo(_: cl_mem!, _: cl_mem_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetMemObjectInfo(_ _: cl_mem, _ _: cl_mem_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetMemObjectInfo(_ _: cl_mem!, _ _: cl_mem_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetPlatformIDs(_: cl_uint, _: UnsafeMutablePointer<cl_platform_id?>!, _: UnsafeMutablePointer<cl_uint>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetPlatformIDs(_ _: cl_uint, _ _: UnsafeMutablePointer<cl_platform_id>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` |
| To | ``` func clGetPlatformIDs(_ _: cl_uint, _ _: UnsafeMutablePointer<cl_platform_id?>!, _ _: UnsafeMutablePointer<cl_uint>!) -> cl_int ``` |

Modified clGetPlatformInfo(_: cl_platform_id!, _: cl_platform_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetPlatformInfo(_ _: cl_platform_id, _ _: cl_platform_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetPlatformInfo(_ _: cl_platform_id!, _ _: cl_platform_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetProgramBuildInfo(_: cl_program!, _: cl_device_id!, _: cl_program_build_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetProgramBuildInfo(_ _: cl_program, _ _: cl_device_id, _ _: cl_program_build_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetProgramBuildInfo(_ _: cl_program!, _ _: cl_device_id!, _ _: cl_program_build_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetProgramInfo(_: cl_program!, _: cl_program_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetProgramInfo(_ _: cl_program, _ _: cl_program_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetProgramInfo(_ _: cl_program!, _ _: cl_program_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetSamplerInfo(_: cl_sampler!, _: cl_sampler_info, _: Int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetSamplerInfo(_ _: cl_sampler, _ _: cl_sampler_info, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>) -> cl_int ``` |
| To | ``` func clGetSamplerInfo(_ _: cl_sampler!, _ _: cl_sampler_info, _ _: Int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!) -> cl_int ``` |

Modified clGetSupportedImageFormats(_: cl_context!, _: cl_mem_flags, _: cl_mem_object_type, _: cl_uint, _: UnsafeMutablePointer<cl_image_format>!, _: UnsafeMutablePointer<cl_uint>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clGetSupportedImageFormats(_ _: cl_context, _ _: cl_mem_flags, _ _: cl_mem_object_type, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_image_format>, _ _: UnsafeMutablePointer<cl_uint>) -> cl_int ``` |
| To | ``` func clGetSupportedImageFormats(_ _: cl_context!, _ _: cl_mem_flags, _ _: cl_mem_object_type, _ _: cl_uint, _ _: UnsafeMutablePointer<cl_image_format>!, _ _: UnsafeMutablePointer<cl_uint>!) -> cl_int ``` |

Modified clLinkProgram(_: cl_context!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: cl_uint, _: UnsafePointer<cl_program?>!, _: ( (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_program!

|  | Declaration |
| --- | --- |
| From | ``` func clLinkProgram(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` |
| To | ``` func clLinkProgram(_ _: cl_context!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafePointer<cl_program?>!, _ _: (@escaping (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_program! ``` |

Modified clLogMessagesToStderrAPPLE(_: UnsafePointer<Int8>!, _: UnsafeRawPointer!, _: Int, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func clLogMessagesToStderrAPPLE(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func clLogMessagesToStderrAPPLE(_ _: UnsafePointer<Int8>!, _ _: UnsafeRawPointer!, _ _: Int, _ _: UnsafeMutableRawPointer!) ``` |

Modified clLogMessagesToStdoutAPPLE(_: UnsafePointer<Int8>!, _: UnsafeRawPointer!, _: Int, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func clLogMessagesToStdoutAPPLE(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func clLogMessagesToStdoutAPPLE(_ _: UnsafePointer<Int8>!, _ _: UnsafeRawPointer!, _ _: Int, _ _: UnsafeMutableRawPointer!) ``` |

Modified clLogMessagesToSystemLogAPPLE(_: UnsafePointer<Int8>!, _: UnsafeRawPointer!, _: Int, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func clLogMessagesToSystemLogAPPLE(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func clLogMessagesToSystemLogAPPLE(_ _: UnsafePointer<Int8>!, _ _: UnsafeRawPointer!, _ _: Int, _ _: UnsafeMutableRawPointer!) ``` |

Modified clReleaseCommandQueue(_: cl_command_queue!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseCommandQueue(_ _: cl_command_queue) -> cl_int ``` |
| To | ``` func clReleaseCommandQueue(_ _: cl_command_queue!) -> cl_int ``` |

Modified clReleaseContext(_: cl_context!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseContext(_ _: cl_context) -> cl_int ``` |
| To | ``` func clReleaseContext(_ _: cl_context!) -> cl_int ``` |

Modified clReleaseDAGAPPLE(_: cl_dag!)

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseDAGAPPLE(_ dag: cl_dag) ``` |
| To | ``` func clReleaseDAGAPPLE(_ dag: cl_dag!) ``` |

Modified clReleaseDevice(_: cl_device_id!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseDevice(_ _: cl_device_id) -> cl_int ``` |
| To | ``` func clReleaseDevice(_ _: cl_device_id!) -> cl_int ``` |

Modified clReleaseEvent(_: cl_event!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseEvent(_ _: cl_event) -> cl_int ``` |
| To | ``` func clReleaseEvent(_ _: cl_event!) -> cl_int ``` |

Modified clReleaseKernel(_: cl_kernel!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseKernel(_ _: cl_kernel) -> cl_int ``` |
| To | ``` func clReleaseKernel(_ _: cl_kernel!) -> cl_int ``` |

Modified clReleaseMemObject(_: cl_mem!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseMemObject(_ _: cl_mem) -> cl_int ``` |
| To | ``` func clReleaseMemObject(_ _: cl_mem!) -> cl_int ``` |

Modified clReleaseProgram(_: cl_program!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseProgram(_ _: cl_program) -> cl_int ``` |
| To | ``` func clReleaseProgram(_ _: cl_program!) -> cl_int ``` |

Modified clReleaseSampler(_: cl_sampler!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clReleaseSampler(_ _: cl_sampler) -> cl_int ``` |
| To | ``` func clReleaseSampler(_ _: cl_sampler!) -> cl_int ``` |

Modified clRetainCommandQueue(_: cl_command_queue!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainCommandQueue(_ _: cl_command_queue) -> cl_int ``` |
| To | ``` func clRetainCommandQueue(_ _: cl_command_queue!) -> cl_int ``` |

Modified clRetainContext(_: cl_context!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainContext(_ _: cl_context) -> cl_int ``` |
| To | ``` func clRetainContext(_ _: cl_context!) -> cl_int ``` |

Modified clRetainDevice(_: cl_device_id!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainDevice(_ _: cl_device_id) -> cl_int ``` |
| To | ``` func clRetainDevice(_ _: cl_device_id!) -> cl_int ``` |

Modified clRetainEvent(_: cl_event!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainEvent(_ _: cl_event) -> cl_int ``` |
| To | ``` func clRetainEvent(_ _: cl_event!) -> cl_int ``` |

Modified clRetainKernel(_: cl_kernel!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainKernel(_ _: cl_kernel) -> cl_int ``` |
| To | ``` func clRetainKernel(_ _: cl_kernel!) -> cl_int ``` |

Modified clRetainMemObject(_: cl_mem!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainMemObject(_ _: cl_mem) -> cl_int ``` |
| To | ``` func clRetainMemObject(_ _: cl_mem!) -> cl_int ``` |

Modified clRetainProgram(_: cl_program!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainProgram(_ _: cl_program) -> cl_int ``` |
| To | ``` func clRetainProgram(_ _: cl_program!) -> cl_int ``` |

Modified clRetainSampler(_: cl_sampler!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clRetainSampler(_ _: cl_sampler) -> cl_int ``` |
| To | ``` func clRetainSampler(_ _: cl_sampler!) -> cl_int ``` |

Modified clSetEventCallback(_: cl_event!, _: cl_int, _: ( (cl_event?, cl_int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetEventCallback(_ _: cl_event, _ _: cl_int, _ _: ((cl_event, cl_int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clSetEventCallback(_ _: cl_event!, _ _: cl_int, _ _: (@escaping (cl_event?, cl_int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clSetKernelArg(_: cl_kernel!, _: cl_uint, _: Int, _: UnsafeRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetKernelArg(_ _: cl_kernel, _ _: cl_uint, _ _: Int, _ _: UnsafePointer<Void>) -> cl_int ``` |
| To | ``` func clSetKernelArg(_ _: cl_kernel!, _ _: cl_uint, _ _: Int, _ _: UnsafeRawPointer!) -> cl_int ``` |

Modified clSetKernelArgByNameAPPLE(_: cl_kernel!, _: UnsafePointer<Int8>!, _: Int, _: UnsafeRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetKernelArgByNameAPPLE(_ _: cl_kernel, _ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafePointer<Void>) -> cl_int ``` |
| To | ``` func clSetKernelArgByNameAPPLE(_ _: cl_kernel!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: UnsafeRawPointer!) -> cl_int ``` |

Modified clSetKernelArgsVaListAPPLE(_: cl_kernel!, _: cl_uint, _: CVaListPointer) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetKernelArgsVaListAPPLE(_ _: cl_kernel, _ _: cl_uint, _ _: CVaListPointer) -> cl_int ``` |
| To | ``` func clSetKernelArgsVaListAPPLE(_ _: cl_kernel!, _ _: cl_uint, _ _: CVaListPointer) -> cl_int ``` |

Modified clSetMemObjectDestructorCallback(_: cl_mem!, _: ( (cl_mem?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem, _ _: ((cl_mem, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem!, _ _: (@escaping (cl_mem?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clSetUserEventStatus(_: cl_event!, _: cl_int) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetUserEventStatus(_ _: cl_event, _ _: cl_int) -> cl_int ``` |
| To | ``` func clSetUserEventStatus(_ _: cl_event!, _ _: cl_int) -> cl_int ``` |

Modified clUnloadPlatformCompiler(_: cl_platform_id!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clUnloadPlatformCompiler(_ _: cl_platform_id) -> cl_int ``` |
| To | ``` func clUnloadPlatformCompiler(_ _: cl_platform_id!) -> cl_int ``` |

Modified clWaitForEvents(_: cl_uint, _: UnsafePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clWaitForEvents(_ _: cl_uint, _ _: UnsafePointer<cl_event>) -> cl_int ``` |
| To | ``` func clWaitForEvents(_ _: cl_uint, _ _: UnsafePointer<cl_event?>!) -> cl_int ``` |

Modified gcl_copy_image(_: cl_image, _: cl_image, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_copy_image(_ dst_image: cl_image, _ src_image: cl_image, _ dst_origin: UnsafePointer<Int>, _ src_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) ``` |
| To | ``` func gcl_copy_image(_ dst_image: cl_image, _ src_image: cl_image, _ dst_origin: UnsafePointer<Int>!, _ src_origin: UnsafePointer<Int>!, _ region: UnsafePointer<Int>!) ``` |

Modified gcl_copy_image_to_ptr(_: UnsafeMutableRawPointer, _: cl_image, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_copy_image_to_ptr(_ dst_ptr: UnsafeMutablePointer<Void>, _ src_image: cl_image, _ src_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) ``` |
| To | ``` func gcl_copy_image_to_ptr(_ dst_ptr: UnsafeMutableRawPointer, _ src_image: cl_image, _ src_origin: UnsafePointer<Int>!, _ region: UnsafePointer<Int>!) ``` |

Modified gcl_copy_ptr_to_image(_: cl_mem, _: UnsafeMutableRawPointer, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_copy_ptr_to_image(_ dst_image: cl_mem, _ src_ptr: UnsafeMutablePointer<Void>, _ dst_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) ``` |
| To | ``` func gcl_copy_ptr_to_image(_ dst_image: cl_mem, _ src_ptr: UnsafeMutableRawPointer, _ dst_origin: UnsafePointer<Int>!, _ region: UnsafePointer<Int>!) ``` |

Modified gcl_create_buffer_from_ptr(_: UnsafeMutableRawPointer) -> cl_mem?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_create_buffer_from_ptr(_ ptr: UnsafeMutablePointer<Void>) -> cl_mem ``` |
| To | ``` func gcl_create_buffer_from_ptr(_ ptr: UnsafeMutableRawPointer) -> cl_mem? ``` |

Modified gcl_create_dispatch_queue(_: cl_queue_flags, _: cl_device_id?) -> DispatchQueue?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_create_dispatch_queue(_ flags: cl_queue_flags, _ device_id: cl_device_id) -> dispatch_queue_t? ``` |
| To | ``` func gcl_create_dispatch_queue(_ flags: cl_queue_flags, _ device_id: cl_device_id?) -> DispatchQueue? ``` |

Modified gcl_create_image(_: UnsafePointer<cl_image_format>, _: Int, _: Int, _: Int, _: IOSurfaceRef?) -> cl_image?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_create_image(_ image_format: UnsafePointer<cl_image_format>, _ image_width: Int, _ image_height: Int, _ image_depth: Int, _ io_surface: IOSurface?) -> cl_image ``` |
| To | ``` func gcl_create_image(_ image_format: UnsafePointer<cl_image_format>, _ image_width: Int, _ image_height: Int, _ image_depth: Int, _ io_surface: IOSurfaceRef?) -> cl_image? ``` |

Modified gcl_create_kernel_from_block(_: UnsafeMutableRawPointer) -> cl_kernel?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_create_kernel_from_block(_ kernel_block_ptr: UnsafeMutablePointer<Void>) -> cl_kernel ``` |
| To | ``` func gcl_create_kernel_from_block(_ kernel_block_ptr: UnsafeMutableRawPointer) -> cl_kernel? ``` |

Modified gcl_free(_: UnsafeMutableRawPointer)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_free(_ ptr: UnsafeMutablePointer<Void>) ``` |
| To | ``` func gcl_free(_ ptr: UnsafeMutableRawPointer) ``` |

Modified gcl_get_context() -> cl_context?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_get_context() -> cl_context ``` |
| To | ``` func gcl_get_context() -> cl_context? ``` |

Modified gcl_get_device_id_with_dispatch_queue(_: DispatchQueue) -> cl_device_id?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_get_device_id_with_dispatch_queue(_ queue: dispatch_queue_t) -> cl_device_id ``` |
| To | ``` func gcl_get_device_id_with_dispatch_queue(_ queue: DispatchQueue) -> cl_device_id? ``` |

Modified gcl_get_kernel_block_workgroup_info(_: UnsafeMutableRawPointer, _: cl_kernel_work_group_info, _: Int, _: UnsafeMutableRawPointer, _: UnsafeMutablePointer<Int>?)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_get_kernel_block_workgroup_info(_ kernel_block_ptr: UnsafeMutablePointer<Void>, _ param_name: cl_kernel_work_group_info, _ param_value_size: Int, _ param_value: UnsafeMutablePointer<Void>, _ param_value_size_ret: UnsafeMutablePointer<Int>) ``` |
| To | ``` func gcl_get_kernel_block_workgroup_info(_ kernel_block_ptr: UnsafeMutableRawPointer, _ param_name: cl_kernel_work_group_info, _ param_value_size: Int, _ param_value: UnsafeMutableRawPointer, _ param_value_size_ret: UnsafeMutablePointer<Int>?) ``` |

Modified gcl_get_supported_image_formats(_: cl_device_id, _: cl_image_type, _: UInt32, _: UnsafeMutablePointer<cl_image_format>, _: UnsafeMutablePointer<UInt32>?)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_get_supported_image_formats(_ device_id: cl_device_id, _ image_type: cl_image_type, _ num_entries: UInt32, _ image_formats: UnsafeMutablePointer<cl_image_format>, _ num_image_formats: UnsafeMutablePointer<UInt32>) ``` |
| To | ``` func gcl_get_supported_image_formats(_ device_id: cl_device_id, _ image_type: cl_image_type, _ num_entries: UInt32, _ image_formats: UnsafeMutablePointer<cl_image_format>, _ num_image_formats: UnsafeMutablePointer<UInt32>?) ``` |

Modified gcl_gl_create_image_from_renderbuffer(_: GLuint) -> cl_image?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_gl_create_image_from_renderbuffer(_ render_buffer: GLuint) -> cl_image ``` |
| To | ``` func gcl_gl_create_image_from_renderbuffer(_ render_buffer: GLuint) -> cl_image? ``` |

Modified gcl_gl_create_image_from_texture(_: GLenum, _: GLint, _: GLuint) -> cl_image?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_gl_create_image_from_texture(_ texture_target: GLenum, _ mip_level: GLint, _ texture: GLuint) -> cl_image ``` |
| To | ``` func gcl_gl_create_image_from_texture(_ texture_target: GLenum, _ mip_level: GLint, _ texture: GLuint) -> cl_image? ``` |

Modified gcl_gl_create_ptr_from_buffer(_: GLuint) -> UnsafeMutableRawPointer?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_gl_create_ptr_from_buffer(_ bufobj: GLuint) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func gcl_gl_create_ptr_from_buffer(_ bufobj: GLuint) -> UnsafeMutableRawPointer? ``` |

Modified gcl_gl_set_sharegroup(_: UnsafeMutableRawPointer)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_gl_set_sharegroup(_ share: UnsafeMutablePointer<Void>) ``` |
| To | ``` func gcl_gl_set_sharegroup(_ share: UnsafeMutableRawPointer) ``` |

Modified gcl_malloc(_: Int, _: UnsafeMutableRawPointer?, _: cl_malloc_flags) -> UnsafeMutableRawPointer?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_malloc(_ bytes: Int, _ host_ptr: UnsafeMutablePointer<Void>, _ flags: cl_malloc_flags) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func gcl_malloc(_ bytes: Int, _ host_ptr: UnsafeMutableRawPointer?, _ flags: cl_malloc_flags) -> UnsafeMutableRawPointer? ``` |

Modified gcl_map_image(_: cl_image, _: cl_map_flags, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!) -> UnsafeMutableRawPointer?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_map_image(_ image: cl_image, _ map_flags: cl_map_flags, _ origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func gcl_map_image(_ image: cl_image, _ map_flags: cl_map_flags, _ origin: UnsafePointer<Int>!, _ region: UnsafePointer<Int>!) -> UnsafeMutableRawPointer? ``` |

Modified gcl_map_ptr(_: UnsafeMutableRawPointer, _: cl_map_flags, _: Int) -> UnsafeMutableRawPointer?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_map_ptr(_ ptr: UnsafeMutablePointer<Void>, _ map_flags: cl_map_flags, _ cb: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func gcl_map_ptr(_ ptr: UnsafeMutableRawPointer, _ map_flags: cl_map_flags, _ cb: Int) -> UnsafeMutableRawPointer? ``` |

Modified gcl_memcpy(_: UnsafeMutableRawPointer, _: UnsafeRawPointer, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_memcpy(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ size: Int) ``` |
| To | ``` func gcl_memcpy(_ dst: UnsafeMutableRawPointer, _ src: UnsafeRawPointer, _ size: Int) ``` |

Modified gcl_memcpy_rect(_: UnsafeMutableRawPointer, _: UnsafeRawPointer, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: UnsafePointer<Int>!, _: Int, _: Int, _: Int, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_memcpy_rect(_ dst: UnsafeMutablePointer<Void>, _ src: UnsafePointer<Void>, _ dst_origin: UnsafePointer<Int>, _ src_origin: UnsafePointer<Int>, _ region: UnsafePointer<Int>, _ dst_row_pitch: Int, _ dst_slice_pitch: Int, _ src_row_pitch: Int, _ src_slice_pitch: Int) ``` |
| To | ``` func gcl_memcpy_rect(_ dst: UnsafeMutableRawPointer, _ src: UnsafeRawPointer, _ dst_origin: UnsafePointer<Int>!, _ src_origin: UnsafePointer<Int>!, _ region: UnsafePointer<Int>!, _ dst_row_pitch: Int, _ dst_slice_pitch: Int, _ src_row_pitch: Int, _ src_slice_pitch: Int) ``` |

Modified gcl_set_finalizer(_: UnsafeMutableRawPointer, _: (UnsafeMutableRawPointer, UnsafeMutableRawPointer?) -> Swift.Void, _: UnsafeMutableRawPointer?)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_set_finalizer(_ object: UnsafeMutablePointer<Void>, _ cl_pfn_finalizer: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void, _ user_data: UnsafeMutablePointer<Void>) ``` |
| To | ``` func gcl_set_finalizer(_ object: UnsafeMutableRawPointer, _ cl_pfn_finalizer: @escaping (UnsafeMutableRawPointer, UnsafeMutableRawPointer?) -> Swift.Void, _ user_data: UnsafeMutableRawPointer?) ``` |

Modified gcl_unmap(_: UnsafeMutableRawPointer)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_unmap(_ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func gcl_unmap(_ _: UnsafeMutableRawPointer) ``` |

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
