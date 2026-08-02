---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/OpenCL.html
archived_at: '2026-07-18T02:53:40.333774Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OpenCL Changes for Swift

### OpenCL

Removed clk_sampler_type.valueRemoved openCLOverlayWorksAdded clk_sampler_type.init(rawValue: UInt32)Added clk_sampler_type.rawValueModified clk_sampler_type [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct clk_sampler_type {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct clk_sampler_type : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified clBuildProgram(_: cl_program, _: cl_uint, _: UnsafePointer<cl_device_id>, _: UnsafePointer<Int8>, _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clBuildProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clBuildProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |

Modified clCompileProgram(_: cl_program, _: cl_uint, _: UnsafePointer<cl_device_id>, _: UnsafePointer<Int8>, _: cl_uint, _: UnsafePointer<cl_program>, _: UnsafeMutablePointer<UnsafePointer<Int8>>, _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCompileProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clCompileProgram(_ _: cl_program, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |

Modified clCreateContext(_: UnsafePointer<cl_context_properties>, _: cl_uint, _: UnsafePointer<cl_device_id>, _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<cl_int>) -> cl_context

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` |
| To | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` |

Modified clCreateContextAndCommandQueueAPPLE(_: UnsafePointer<cl_context_properties>, _: cl_uint, _: UnsafePointer<cl_device_id>, _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>, _: cl_command_queue_properties, _: UnsafeMutablePointer<cl_context>, _: UnsafeMutablePointer<cl_command_queue>) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context>, _ _: UnsafeMutablePointer<cl_command_queue>) -> cl_int ``` |
| To | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context>, _ _: UnsafeMutablePointer<cl_command_queue>) -> cl_int ``` |

Modified clCreateContextFromType(_: UnsafePointer<cl_context_properties>, _: cl_device_type, _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<cl_int>) -> cl_context

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>, _ _: cl_device_type, _ _: CFunctionPointer<((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` |
| To | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>, _ _: cl_device_type, _ _: ((UnsafePointer<Int8>, UnsafePointer<Void>, Int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_context ``` |

Modified clCreateImageFromIOSurface2DAPPLE(_: cl_context, _: cl_mem_flags, _: UnsafePointer<cl_image_format>, _: Int, _: Int, _: IOSurface, _: UnsafeMutablePointer<cl_int>) -> cl_mem

|  | Declaration |
| --- | --- |
| From | ``` func clCreateImageFromIOSurface2DAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: Int, _ _: Int, _ _: IOSurface!, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |
| To | ``` func clCreateImageFromIOSurface2DAPPLE(_ _: cl_context, _ _: cl_mem_flags, _ _: UnsafePointer<cl_image_format>, _ _: Int, _ _: Int, _ _: IOSurface, _ _: UnsafeMutablePointer<cl_int>) -> cl_mem ``` |

Modified clEnqueueNativeKernel(_: cl_command_queue, _: ((UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>, _: Int, _: cl_uint, _: UnsafePointer<cl_mem>, _: UnsafeMutablePointer<UnsafePointer<Void>>, _: cl_uint, _: UnsafePointer<cl_event>, _: UnsafeMutablePointer<cl_event>) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueNativeKernel(_ _: cl_command_queue, _ _: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: UnsafeMutablePointer<UnsafePointer<Void>>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |
| To | ``` func clEnqueueNativeKernel(_ _: cl_command_queue, _ _: ((UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem>, _ _: UnsafeMutablePointer<UnsafePointer<Void>>, _ _: cl_uint, _ _: UnsafePointer<cl_event>, _ _: UnsafeMutablePointer<cl_event>) -> cl_int ``` |

Modified clLinkProgram(_: cl_context, _: cl_uint, _: UnsafePointer<cl_device_id>, _: UnsafePointer<Int8>, _: cl_uint, _: UnsafePointer<cl_program>, _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<cl_int>) -> cl_program

|  | Declaration |
| --- | --- |
| From | ``` func clLinkProgram(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: CFunctionPointer<((cl_program, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` |
| To | ``` func clLinkProgram(_ _: cl_context, _ _: cl_uint, _ _: UnsafePointer<cl_device_id>, _ _: UnsafePointer<Int8>, _ _: cl_uint, _ _: UnsafePointer<cl_program>, _ _: ((cl_program, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<cl_int>) -> cl_program ``` |

Modified clSetEventCallback(_: cl_event, _: cl_int, _: ((cl_event, cl_int, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetEventCallback(_ _: cl_event, _ _: cl_int, _ _: CFunctionPointer<((cl_event, cl_int, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clSetEventCallback(_ _: cl_event, _ _: cl_int, _ _: ((cl_event, cl_int, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |

Modified clSetMemObjectDestructorCallback(_: cl_mem, _: ((cl_mem, UnsafeMutablePointer<Void>) -> Void)!, _: UnsafeMutablePointer<Void>) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem, _ _: CFunctionPointer<((cl_mem, UnsafeMutablePointer<Void>) -> Void)>, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |
| To | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem, _ _: ((cl_mem, UnsafeMutablePointer<Void>) -> Void)!, _ _: UnsafeMutablePointer<Void>) -> cl_int ``` |

Modified gcl_create_dispatch_queue(_: cl_queue_flags, _: cl_device_id) -> dispatch_queue_t?

|  | Declaration |
| --- | --- |
| From | ``` func gcl_create_dispatch_queue(_ flags: cl_queue_flags, _ device_id: cl_device_id) -> dispatch_queue_t! ``` |
| To | ``` func gcl_create_dispatch_queue(_ flags: cl_queue_flags, _ device_id: cl_device_id) -> dispatch_queue_t? ``` |

Modified gcl_create_image(_: UnsafePointer<cl_image_format>, _: Int, _: Int, _: Int, _: IOSurface?) -> cl_image

|  | Declaration |
| --- | --- |
| From | ``` func gcl_create_image(_ image_format: UnsafePointer<cl_image_format>, _ image_width: Int, _ image_height: Int, _ image_depth: Int, _ io_surface: IOSurface!) -> cl_image ``` |
| To | ``` func gcl_create_image(_ image_format: UnsafePointer<cl_image_format>, _ image_width: Int, _ image_height: Int, _ image_depth: Int, _ io_surface: IOSurface?) -> cl_image ``` |

Modified gcl_get_device_id_with_dispatch_queue(_: dispatch_queue_t) -> cl_device_id

|  | Declaration |
| --- | --- |
| From | ``` func gcl_get_device_id_with_dispatch_queue(_ queue: dispatch_queue_t!) -> cl_device_id ``` |
| To | ``` func gcl_get_device_id_with_dispatch_queue(_ queue: dispatch_queue_t) -> cl_device_id ``` |

Modified gcl_set_finalizer(_: UnsafeMutablePointer<Void>, _: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void, _: UnsafeMutablePointer<Void>)

|  | Declaration |
| --- | --- |
| From | ``` func gcl_set_finalizer(_ object: UnsafeMutablePointer<Void>, _ cl_pfn_finalizer: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>, _ user_data: UnsafeMutablePointer<Void>) ``` |
| To | ``` func gcl_set_finalizer(_ object: UnsafeMutablePointer<Void>, _ cl_pfn_finalizer: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void, _ user_data: UnsafeMutablePointer<Void>) ``` |

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
