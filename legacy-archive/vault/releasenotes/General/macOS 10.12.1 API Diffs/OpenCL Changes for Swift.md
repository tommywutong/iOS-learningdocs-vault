---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/OpenCL.html
archived_at: '2026-07-18T02:51:47.071602Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# OpenCL Changes for Swift

### OpenCL

Modified clBuildProgram(_: cl_program!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: ((cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clBuildProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: (@escaping (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |
| To | ``` func clBuildProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: ((cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clCompileProgram(_: cl_program!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: cl_uint, _: UnsafePointer<cl_program?>!, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: ((cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCompileProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafePointer<cl_program?>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: (@escaping (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |
| To | ``` func clCompileProgram(_ _: cl_program!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafePointer<cl_program?>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: ((cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clCreateContext(_: UnsafePointer<cl_context_properties>!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: ((UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_context!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_context! ``` |
| To | ``` func clCreateContext(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: ((UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_context! ``` |

Modified clCreateContextAndCommandQueueAPPLE(_: UnsafePointer<cl_context_properties>!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: ((UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: cl_command_queue_properties, _: UnsafeMutablePointer<cl_context?>!, _: UnsafeMutablePointer<cl_command_queue?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context?>!, _ _: UnsafeMutablePointer<cl_command_queue?>!) -> cl_int ``` |
| To | ``` func clCreateContextAndCommandQueueAPPLE(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: ((UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: cl_command_queue_properties, _ _: UnsafeMutablePointer<cl_context?>!, _ _: UnsafeMutablePointer<cl_command_queue?>!) -> cl_int ``` |

Modified clCreateContextFromType(_: UnsafePointer<cl_context_properties>!, _: cl_device_type, _: ((UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_context!

|  | Declaration |
| --- | --- |
| From | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_device_type, _ _: (@escaping (UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_context! ``` |
| To | ``` func clCreateContextFromType(_ _: UnsafePointer<cl_context_properties>!, _ _: cl_device_type, _ _: ((UnsafePointer<Int8>?, UnsafeRawPointer?, Int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_context! ``` |

Modified clEnqueueNativeKernel(_: cl_command_queue!, _: ((UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: Int, _: cl_uint, _: UnsafePointer<cl_mem?>!, _: UnsafeMutablePointer<UnsafeRawPointer?>!, _: cl_uint, _: UnsafePointer<cl_event?>!, _: UnsafeMutablePointer<cl_event?>!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clEnqueueNativeKernel(_ _: cl_command_queue!, _ _: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem?>!, _ _: UnsafeMutablePointer<UnsafeRawPointer?>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |
| To | ``` func clEnqueueNativeKernel(_ _: cl_command_queue!, _ _: ((UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: cl_uint, _ _: UnsafePointer<cl_mem?>!, _ _: UnsafeMutablePointer<UnsafeRawPointer?>!, _ _: cl_uint, _ _: UnsafePointer<cl_event?>!, _ _: UnsafeMutablePointer<cl_event?>!) -> cl_int ``` |

Modified clLinkProgram(_: cl_context!, _: cl_uint, _: UnsafePointer<cl_device_id?>!, _: UnsafePointer<Int8>!, _: cl_uint, _: UnsafePointer<cl_program?>!, _: ((cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<cl_int>!) -> cl_program!

|  | Declaration |
| --- | --- |
| From | ``` func clLinkProgram(_ _: cl_context!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafePointer<cl_program?>!, _ _: (@escaping (cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_program! ``` |
| To | ``` func clLinkProgram(_ _: cl_context!, _ _: cl_uint, _ _: UnsafePointer<cl_device_id?>!, _ _: UnsafePointer<Int8>!, _ _: cl_uint, _ _: UnsafePointer<cl_program?>!, _ _: ((cl_program?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<cl_int>!) -> cl_program! ``` |

Modified clSetEventCallback(_: cl_event!, _: cl_int, _: ((cl_event?, cl_int, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetEventCallback(_ _: cl_event!, _ _: cl_int, _ _: (@escaping (cl_event?, cl_int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |
| To | ``` func clSetEventCallback(_ _: cl_event!, _ _: cl_int, _ _: ((cl_event?, cl_int, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

Modified clSetMemObjectDestructorCallback(_: cl_mem!, _: ((cl_mem?, UnsafeMutableRawPointer?) -> Swift.Void)!, _: UnsafeMutableRawPointer!) -> cl_int

|  | Declaration |
| --- | --- |
| From | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem!, _ _: (@escaping (cl_mem?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |
| To | ``` func clSetMemObjectDestructorCallback(_ _: cl_mem!, _ _: ((cl_mem?, UnsafeMutableRawPointer?) -> Swift.Void)!, _ _: UnsafeMutableRawPointer!) -> cl_int ``` |

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
