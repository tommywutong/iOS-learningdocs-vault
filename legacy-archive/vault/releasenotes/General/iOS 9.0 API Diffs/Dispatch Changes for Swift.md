---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Dispatch.html
archived_at: '2026-07-18T02:56:48.456968Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Dispatch Changes for Swift

### Dispatch

Removed dispatch_block_flags_t.valueAdded dispatch_block_flags_t.init(rawValue: UInt)Added dispatch_block_flags_t.rawValueModified [dispatch_block_flags_t [struct]](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct dispatch_block_flags_t {     init(_ value: UInt)     var value: UInt } ``` | -- |
| To | ``` struct dispatch_block_flags_t : RawRepresentable {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     var rawValue: UInt } ``` | RawRepresentable |

Modified [OS_dispatch_data](https://developer.apple.com/documentation/dispatch/os_dispatch_data)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_data : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_data : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [OS_dispatch_group](https://developer.apple.com/documentation/dispatch/os_dispatch_group)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_group : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_group : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [OS_dispatch_io](https://developer.apple.com/documentation/dispatch/os_dispatch_io)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_io : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_io : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [OS_dispatch_object](https://developer.apple.com/documentation/dispatch/os_dispatch_object)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_object { } ``` | -- |
| To | ``` protocol OS_dispatch_object : NSObjectProtocol { } ``` | NSObjectProtocol |

Modified [OS_dispatch_queue](https://developer.apple.com/documentation/dispatch/os_dispatch_queue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_queue : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_queue : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [OS_dispatch_queue_attr](https://developer.apple.com/documentation/dispatch/os_dispatch_queue_attr)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_queue_attr : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_queue_attr : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [OS_dispatch_semaphore](https://developer.apple.com/documentation/dispatch/os_dispatch_semaphore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_semaphore : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_semaphore : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [OS_dispatch_source](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_dispatch_source : OS_dispatch_object { } ``` | OS_dispatch_object |
| To | ``` protocol OS_dispatch_source : OS_dispatch_object, NSObjectProtocol { } ``` | NSObjectProtocol, OS_dispatch_object |

Modified [dispatch_apply_f(_: Int, _: dispatch_queue_t!, _: UnsafeMutablePointer<Void>, _: (UnsafeMutablePointer<Void>, Int) -> Void)](https://developer.apple.com/documentation/dispatch/1452846-dispatch_apply_f)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_apply_f(_ iterations: Int, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> Void)>) ``` |
| To | ``` func dispatch_apply_f(_ iterations: Int, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: (UnsafeMutablePointer<Void>, Int) -> Void) ``` |

Modified [dispatch_block_create(_: dispatch_block_flags_t, _: dispatch_block_t) -> dispatch_block_t!](https://developer.apple.com/documentation/dispatch/1431050-dispatch_block_create)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_create(_ flags: dispatch_block_flags_t, _ block: dispatch_block_t) -> dispatch_block_t! ``` |
| To | ``` @warn_unused_result func dispatch_block_create(_ flags: dispatch_block_flags_t, _ block: dispatch_block_t) -> dispatch_block_t! ``` |

Modified [dispatch_block_create_with_qos_class(_: dispatch_block_flags_t, _: dispatch_qos_class_t, _: Int32, _: dispatch_block_t) -> dispatch_block_t!](https://developer.apple.com/documentation/dispatch/1431068-dispatch_block_create_with_qos_c)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_create_with_qos_class(_ flags: dispatch_block_flags_t, _ qos_class: dispatch_qos_class_t, _ relative_priority: Int32, _ block: dispatch_block_t) -> dispatch_block_t! ``` |
| To | ``` @warn_unused_result func dispatch_block_create_with_qos_class(_ flags: dispatch_block_flags_t, _ qos_class: dispatch_qos_class_t, _ relative_priority: Int32, _ block: dispatch_block_t) -> dispatch_block_t! ``` |

Modified [dispatch_block_testcancel(_: dispatch_block_t) -> Int](https://developer.apple.com/documentation/dispatch/1431046-dispatch_block_testcancel)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_testcancel(_ block: dispatch_block_t) -> Int ``` |
| To | ``` @warn_unused_result func dispatch_block_testcancel(_ block: dispatch_block_t) -> Int ``` |

Modified DISPATCH_CURRENT_QUEUE_LABEL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [dispatch_data_copy_region(_: dispatch_data_t, _: Int, _: UnsafeMutablePointer<Int>) -> dispatch_data_t!](https://developer.apple.com/documentation/dispatch/1452810-dispatch_data_copy_region)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_copy_region(_ data: dispatch_data_t, _ location: Int, _ offset_ptr: UnsafeMutablePointer<Int>) -> dispatch_data_t! ``` |
| To | ``` @warn_unused_result func dispatch_data_copy_region(_ data: dispatch_data_t, _ location: Int, _ offset_ptr: UnsafeMutablePointer<Int>) -> dispatch_data_t! ``` |

Modified [dispatch_data_create(_: UnsafePointer<Void>, _: Int, _: dispatch_queue_t!, _: dispatch_block_t!) -> dispatch_data_t!](https://developer.apple.com/documentation/dispatch/1452970-dispatch_data_create)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create(_ buffer: UnsafePointer<Void>, _ size: Int, _ queue: dispatch_queue_t!, _ destructor: dispatch_block_t!) -> dispatch_data_t! ``` |
| To | ``` @warn_unused_result func dispatch_data_create(_ buffer: UnsafePointer<Void>, _ size: Int, _ queue: dispatch_queue_t!, _ destructor: dispatch_block_t!) -> dispatch_data_t! ``` |

Modified [dispatch_data_create_concat(_: dispatch_data_t, _: dispatch_data_t) -> dispatch_data_t!](https://developer.apple.com/documentation/dispatch/1453003-dispatch_data_create_concat)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create_concat(_ data1: dispatch_data_t, _ data2: dispatch_data_t) -> dispatch_data_t! ``` |
| To | ``` @warn_unused_result func dispatch_data_create_concat(_ data1: dispatch_data_t, _ data2: dispatch_data_t) -> dispatch_data_t! ``` |

Modified [dispatch_data_create_map(_: dispatch_data_t, _: UnsafeMutablePointer<UnsafePointer<Void>>, _: UnsafeMutablePointer<Int>) -> dispatch_data_t!](https://developer.apple.com/documentation/dispatch/1452937-dispatch_data_create_map)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create_map(_ data: dispatch_data_t, _ buffer_ptr: UnsafeMutablePointer<UnsafePointer<Void>>, _ size_ptr: UnsafeMutablePointer<Int>) -> dispatch_data_t! ``` |
| To | ``` @warn_unused_result func dispatch_data_create_map(_ data: dispatch_data_t, _ buffer_ptr: UnsafeMutablePointer<UnsafePointer<Void>>, _ size_ptr: UnsafeMutablePointer<Int>) -> dispatch_data_t! ``` |

Modified [dispatch_data_create_subrange(_: dispatch_data_t, _: Int, _: Int) -> dispatch_data_t!](https://developer.apple.com/documentation/dispatch/1452961-dispatch_data_create_subrange)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create_subrange(_ data: dispatch_data_t, _ offset: Int, _ length: Int) -> dispatch_data_t! ``` |
| To | ``` @warn_unused_result func dispatch_data_create_subrange(_ data: dispatch_data_t, _ offset: Int, _ length: Int) -> dispatch_data_t! ``` |

Modified dispatch_data_empty

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified [dispatch_data_t](https://developer.apple.com/documentation/dispatch/dispatch_data_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_data_t = NSObject ``` |
| To | ``` typealias dispatch_data_t = OS_dispatch_data ``` |

Modified [dispatch_function_t](https://developer.apple.com/documentation/dispatch/dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_function_t = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias dispatch_function_t = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [dispatch_get_context(_: dispatch_object_t) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/dispatch/1453005-dispatch_get_context)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_get_context(_ object: dispatch_object_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` @warn_unused_result func dispatch_get_context(_ object: dispatch_object_t) -> UnsafeMutablePointer<Void> ``` |

Modified [dispatch_get_global_queue(_: Int, _: UInt) -> dispatch_queue_t!](https://developer.apple.com/documentation/dispatch/1452927-dispatch_get_global_queue)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_get_global_queue(_ identifier: Int, _ flags: UInt) -> dispatch_queue_t! ``` |
| To | ``` @warn_unused_result func dispatch_get_global_queue(_ identifier: Int, _ flags: UInt) -> dispatch_queue_t! ``` |

Modified dispatch_get_global_queue(_: qos_class_t, _: UInt) -> dispatch_queue_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func dispatch_get_global_queue(_ identifier: qos_class_t, _ flags: UInt) -> dispatch_queue_t ``` | iOS 8.1 |
| To | ``` @warn_unused_result func dispatch_get_global_queue(_ identifier: qos_class_t, _ flags: UInt) -> dispatch_queue_t ``` | iOS 9.0 |

Modified [dispatch_get_specific(_: UnsafePointer<Void>) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/dispatch/1453125-dispatch_get_specific)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_get_specific(_ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` @warn_unused_result func dispatch_get_specific(_ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified [dispatch_group_create() -> dispatch_group_t!](https://developer.apple.com/documentation/dispatch/1452975-dispatch_group_create)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_create() -> dispatch_group_t! ``` |
| To | ``` @warn_unused_result func dispatch_group_create() -> dispatch_group_t! ``` |

Modified [dispatch_group_t](https://developer.apple.com/documentation/dispatch/dispatch_group_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_group_t = NSObject ``` |
| To | ``` typealias dispatch_group_t = OS_dispatch_group ``` |

Modified [dispatch_introspection_hook_queue_callout_begin(_: dispatch_queue_t!, _: UnsafeMutablePointer<Void>, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1452899-dispatch_introspection_hook_queu)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_introspection_hook_queue_callout_begin(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ function: dispatch_function_t) ``` |
| To | ``` func dispatch_introspection_hook_queue_callout_begin(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ function: dispatch_function_t!) ``` |

Modified [dispatch_introspection_hook_queue_callout_end(_: dispatch_queue_t!, _: UnsafeMutablePointer<Void>, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1453081-dispatch_introspection_hook_queu)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_introspection_hook_queue_callout_end(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ function: dispatch_function_t) ``` |
| To | ``` func dispatch_introspection_hook_queue_callout_end(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ function: dispatch_function_t!) ``` |

Modified [dispatch_io_create(_: dispatch_io_type_t, _: dispatch_fd_t, _: dispatch_queue_t!, _: ((Int32) -> Void)!) -> dispatch_io_t!](https://developer.apple.com/documentation/dispatch/dispatchio/1388976-init)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_create(_ type: dispatch_io_type_t, _ fd: dispatch_fd_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |
| To | ``` @warn_unused_result func dispatch_io_create(_ type: dispatch_io_type_t, _ fd: dispatch_fd_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |

Modified [dispatch_io_create_with_io(_: dispatch_io_type_t, _: dispatch_io_t, _: dispatch_queue_t!, _: ((Int32) -> Void)!) -> dispatch_io_t!](https://developer.apple.com/documentation/dispatch/dispatchio/1388935-init)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_create_with_io(_ type: dispatch_io_type_t, _ io: dispatch_io_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |
| To | ``` @warn_unused_result func dispatch_io_create_with_io(_ type: dispatch_io_type_t, _ io: dispatch_io_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |

Modified [dispatch_io_create_with_path(_: dispatch_io_type_t, _: UnsafePointer<Int8>, _: Int32, _: mode_t, _: dispatch_queue_t!, _: ((Int32) -> Void)!) -> dispatch_io_t!](https://developer.apple.com/documentation/dispatch/1388955-dispatch_io_create_with_path)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_create_with_path(_ type: dispatch_io_type_t, _ path: UnsafePointer<Int8>, _ oflag: Int32, _ mode: mode_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |
| To | ``` @warn_unused_result func dispatch_io_create_with_path(_ type: dispatch_io_type_t, _ path: UnsafePointer<Int8>, _ oflag: Int32, _ mode: mode_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |

Modified [dispatch_io_get_descriptor(_: dispatch_io_t) -> dispatch_fd_t](https://developer.apple.com/documentation/dispatch/dispatchio/1388951-filedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_get_descriptor(_ channel: dispatch_io_t) -> dispatch_fd_t ``` |
| To | ``` @warn_unused_result func dispatch_io_get_descriptor(_ channel: dispatch_io_t) -> dispatch_fd_t ``` |

Modified DISPATCH_IO_RANDOM

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_RANDOM: UInt ``` |
| To | ``` let DISPATCH_IO_RANDOM: dispatch_io_type_t ``` |

Modified DISPATCH_IO_STOP

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_STOP: UInt ``` |
| To | ``` let DISPATCH_IO_STOP: dispatch_io_close_flags_t ``` |

Modified DISPATCH_IO_STREAM

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_STREAM: UInt ``` |
| To | ``` let DISPATCH_IO_STREAM: dispatch_io_type_t ``` |

Modified DISPATCH_IO_STRICT_INTERVAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_IO_STRICT_INTERVAL: UInt ``` |
| To | ``` let DISPATCH_IO_STRICT_INTERVAL: dispatch_io_interval_flags_t ``` |

Modified [dispatch_io_t](https://developer.apple.com/documentation/dispatch/dispatch_io_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_io_t = NSObject ``` |
| To | ``` typealias dispatch_io_t = OS_dispatch_io ``` |

Modified DISPATCH_MACH_SEND_DEAD

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MACH_SEND_DEAD: UInt ``` |
| To | ``` let DISPATCH_MACH_SEND_DEAD: dispatch_source_mach_send_flags_t ``` |

Modified DISPATCH_MEMORYPRESSURE_CRITICAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MEMORYPRESSURE_CRITICAL: UInt ``` |
| To | ``` let DISPATCH_MEMORYPRESSURE_CRITICAL: dispatch_source_memorypressure_flags_t ``` |

Modified DISPATCH_MEMORYPRESSURE_NORMAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MEMORYPRESSURE_NORMAL: UInt ``` |
| To | ``` let DISPATCH_MEMORYPRESSURE_NORMAL: dispatch_source_memorypressure_flags_t ``` |

Modified DISPATCH_MEMORYPRESSURE_WARN

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_MEMORYPRESSURE_WARN: UInt ``` |
| To | ``` let DISPATCH_MEMORYPRESSURE_WARN: dispatch_source_memorypressure_flags_t ``` |

Modified [dispatch_object_t](https://developer.apple.com/documentation/dispatch/dispatch_object_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_object_t = NSObject ``` |
| To | ``` typealias dispatch_object_t = OS_dispatch_object ``` |

Modified DISPATCH_PROC_EXEC

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_EXEC: UInt ``` |
| To | ``` let DISPATCH_PROC_EXEC: dispatch_source_proc_flags_t ``` |

Modified DISPATCH_PROC_FORK

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_FORK: UInt ``` |
| To | ``` let DISPATCH_PROC_FORK: dispatch_source_proc_flags_t ``` |

Modified DISPATCH_PROC_SIGNAL

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_PROC_SIGNAL: UInt ``` |
| To | ``` let DISPATCH_PROC_SIGNAL: dispatch_source_proc_flags_t ``` |

Modified [dispatch_queue_attr_make_with_qos_class(_: dispatch_queue_attr_t!, _: dispatch_qos_class_t, _: Int32) -> dispatch_queue_attr_t!](https://developer.apple.com/documentation/dispatch/1453028-dispatch_queue_attr_make_with_qo)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_attr_make_with_qos_class(_ attr: dispatch_queue_attr_t!, _ qos_class: dispatch_qos_class_t, _ relative_priority: Int32) -> dispatch_queue_attr_t! ``` |
| To | ``` @warn_unused_result func dispatch_queue_attr_make_with_qos_class(_ attr: dispatch_queue_attr_t!, _ qos_class: dispatch_qos_class_t, _ relative_priority: Int32) -> dispatch_queue_attr_t! ``` |

Modified [dispatch_queue_attr_t](https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_queue_attr_t = NSObject ``` |
| To | ``` typealias dispatch_queue_attr_t = OS_dispatch_queue_attr ``` |

Modified DISPATCH_QUEUE_CONCURRENT

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [dispatch_queue_create(_: UnsafePointer<Int8>, _: dispatch_queue_attr_t!) -> dispatch_queue_t!](https://developer.apple.com/documentation/dispatch/dispatchqueue/1453030-init)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_create(_ label: UnsafePointer<Int8>, _ attr: dispatch_queue_attr_t!) -> dispatch_queue_t! ``` |
| To | ``` @warn_unused_result func dispatch_queue_create(_ label: UnsafePointer<Int8>, _ attr: dispatch_queue_attr_t!) -> dispatch_queue_t! ``` |

Modified [dispatch_queue_get_label(_: dispatch_queue_t!) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/dispatch/1452939-dispatch_queue_get_label)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_get_label(_ queue: dispatch_queue_t!) -> UnsafePointer<Int8> ``` |
| To | ``` @warn_unused_result func dispatch_queue_get_label(_ queue: dispatch_queue_t!) -> UnsafePointer<Int8> ``` |

Modified [dispatch_queue_get_qos_class(_: dispatch_queue_t, _: UnsafeMutablePointer<Int32>) -> dispatch_qos_class_t](https://developer.apple.com/documentation/dispatch/1452829-dispatch_queue_get_qos_class)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_get_qos_class(_ queue: dispatch_queue_t, _ relative_priority_ptr: UnsafeMutablePointer<Int32>) -> dispatch_qos_class_t ``` |
| To | ``` @warn_unused_result func dispatch_queue_get_qos_class(_ queue: dispatch_queue_t, _ relative_priority_ptr: UnsafeMutablePointer<Int32>) -> dispatch_qos_class_t ``` |

Modified [dispatch_queue_get_specific(_: dispatch_queue_t, _: UnsafePointer<Void>) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/dispatch/1453067-dispatch_queue_get_specific)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_get_specific(_ queue: dispatch_queue_t, _ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` @warn_unused_result func dispatch_queue_get_specific(_ queue: dispatch_queue_t, _ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified DISPATCH_QUEUE_PRIORITY_BACKGROUND

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_BACKGROUND: (Int) ``` |
| To | ``` let DISPATCH_QUEUE_PRIORITY_BACKGROUND: dispatch_queue_priority_t ``` |

Modified DISPATCH_QUEUE_PRIORITY_DEFAULT

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_DEFAULT: (Int) ``` |
| To | ``` let DISPATCH_QUEUE_PRIORITY_DEFAULT: dispatch_queue_priority_t ``` |

Modified DISPATCH_QUEUE_PRIORITY_HIGH

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_HIGH: (Int) ``` |
| To | ``` let DISPATCH_QUEUE_PRIORITY_HIGH: dispatch_queue_priority_t ``` |

Modified DISPATCH_QUEUE_PRIORITY_LOW

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_QUEUE_PRIORITY_LOW: (Int) ``` |
| To | ``` let DISPATCH_QUEUE_PRIORITY_LOW: dispatch_queue_priority_t ``` |

Modified DISPATCH_QUEUE_SERIAL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [dispatch_queue_set_specific(_: dispatch_queue_t, _: UnsafePointer<Void>, _: UnsafeMutablePointer<Void>, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1452967-dispatch_queue_set_specific)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_set_specific(_ queue: dispatch_queue_t, _ key: UnsafePointer<Void>, _ context: UnsafeMutablePointer<Void>, _ destructor: dispatch_function_t) ``` |
| To | ``` func dispatch_queue_set_specific(_ queue: dispatch_queue_t, _ key: UnsafePointer<Void>, _ context: UnsafeMutablePointer<Void>, _ destructor: dispatch_function_t!) ``` |

Modified [dispatch_queue_t](https://developer.apple.com/documentation/dispatch/dispatch_queue_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_queue_t = NSObject ``` |
| To | ``` typealias dispatch_queue_t = OS_dispatch_queue ``` |

Modified [dispatch_semaphore_create(_: Int) -> dispatch_semaphore_t!](https://developer.apple.com/documentation/dispatch/dispatchsemaphore/1452955-init)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_semaphore_create(_ value: Int) -> dispatch_semaphore_t! ``` |
| To | ``` @warn_unused_result func dispatch_semaphore_create(_ value: Int) -> dispatch_semaphore_t! ``` |

Modified [dispatch_semaphore_t](https://developer.apple.com/documentation/dispatch/dispatch_semaphore_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_semaphore_t = NSObject ``` |
| To | ``` typealias dispatch_semaphore_t = OS_dispatch_semaphore ``` |

Modified [dispatch_set_finalizer_f(_: dispatch_object_t!, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1453100-dispatch_set_finalizer_f)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_set_finalizer_f(_ object: dispatch_object_t!, _ finalizer: dispatch_function_t) ``` |
| To | ``` func dispatch_set_finalizer_f(_ object: dispatch_object_t!, _ finalizer: dispatch_function_t!) ``` |

Modified [dispatch_source_create(_: dispatch_source_type_t, _: UInt, _: UInt, _: dispatch_queue_t!) -> dispatch_source_t!](https://developer.apple.com/documentation/dispatch/1385630-dispatch_source_create)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_create(_ type: dispatch_source_type_t, _ handle: UInt, _ mask: UInt, _ queue: dispatch_queue_t!) -> dispatch_source_t! ``` |
| To | ``` @warn_unused_result func dispatch_source_create(_ type: dispatch_source_type_t, _ handle: UInt, _ mask: UInt, _ queue: dispatch_queue_t!) -> dispatch_source_t! ``` |

Modified [dispatch_source_get_data(_: dispatch_source_t) -> UInt](https://developer.apple.com/documentation/dispatch/1385658-dispatch_source_get_data)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_get_data(_ source: dispatch_source_t) -> UInt ``` |
| To | ``` @warn_unused_result func dispatch_source_get_data(_ source: dispatch_source_t) -> UInt ``` |

Modified [dispatch_source_get_handle(_: dispatch_source_t) -> UInt](https://developer.apple.com/documentation/dispatch/1385670-dispatch_source_get_handle)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_get_handle(_ source: dispatch_source_t) -> UInt ``` |
| To | ``` @warn_unused_result func dispatch_source_get_handle(_ source: dispatch_source_t) -> UInt ``` |

Modified [dispatch_source_get_mask(_: dispatch_source_t) -> UInt](https://developer.apple.com/documentation/dispatch/1385612-dispatch_source_get_mask)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_get_mask(_ source: dispatch_source_t) -> UInt ``` |
| To | ``` @warn_unused_result func dispatch_source_get_mask(_ source: dispatch_source_t) -> UInt ``` |

Modified [dispatch_source_set_cancel_handler_f(_: dispatch_source_t, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1385592-dispatch_source_set_cancel_handl)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_cancel_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t) ``` |
| To | ``` func dispatch_source_set_cancel_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t!) ``` |

Modified [dispatch_source_set_event_handler_f(_: dispatch_source_t, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1385660-dispatch_source_set_event_handle)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_event_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t) ``` |
| To | ``` func dispatch_source_set_event_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t!) ``` |

Modified [dispatch_source_set_registration_handler_f(_: dispatch_source_t, _: dispatch_function_t!)](https://developer.apple.com/documentation/dispatch/1385662-dispatch_source_set_registration)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_registration_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t) ``` |
| To | ``` func dispatch_source_set_registration_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t!) ``` |

Modified [dispatch_source_t](https://developer.apple.com/documentation/dispatch/dispatch_source_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_source_t = NSObject ``` |
| To | ``` typealias dispatch_source_t = OS_dispatch_source ``` |

Modified [dispatch_source_testcancel(_: dispatch_source_t) -> Int](https://developer.apple.com/documentation/dispatch/1385616-dispatch_source_testcancel)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_testcancel(_ source: dispatch_source_t) -> Int ``` |
| To | ``` @warn_unused_result func dispatch_source_testcancel(_ source: dispatch_source_t) -> Int ``` |

Modified DISPATCH_TARGET_QUEUE_DEFAULT

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [dispatch_time(_: dispatch_time_t, _: Int64) -> dispatch_time_t](https://developer.apple.com/documentation/dispatch/1420519-dispatch_time)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_time(_ when: dispatch_time_t, _ delta: Int64) -> dispatch_time_t ``` |
| To | ``` @warn_unused_result func dispatch_time(_ when: dispatch_time_t, _ delta: Int64) -> dispatch_time_t ``` |

Modified DISPATCH_TIMER_STRICT

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_TIMER_STRICT: UInt ``` |
| To | ``` let DISPATCH_TIMER_STRICT: dispatch_source_timer_flags_t ``` |

Modified DISPATCH_VNODE_ATTRIB

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_ATTRIB: UInt ``` |
| To | ``` let DISPATCH_VNODE_ATTRIB: dispatch_source_vnode_flags_t ``` |

Modified DISPATCH_VNODE_DELETE

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_DELETE: UInt ``` |
| To | ``` let DISPATCH_VNODE_DELETE: dispatch_source_vnode_flags_t ``` |

Modified DISPATCH_VNODE_EXTEND

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_EXTEND: UInt ``` |
| To | ``` let DISPATCH_VNODE_EXTEND: dispatch_source_vnode_flags_t ``` |

Modified DISPATCH_VNODE_LINK

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_LINK: UInt ``` |
| To | ``` let DISPATCH_VNODE_LINK: dispatch_source_vnode_flags_t ``` |

Modified DISPATCH_VNODE_RENAME

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_RENAME: UInt ``` |
| To | ``` let DISPATCH_VNODE_RENAME: dispatch_source_vnode_flags_t ``` |

Modified DISPATCH_VNODE_REVOKE

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_REVOKE: UInt ``` |
| To | ``` let DISPATCH_VNODE_REVOKE: dispatch_source_vnode_flags_t ``` |

Modified DISPATCH_VNODE_WRITE

|  | Declaration |
| --- | --- |
| From | ``` let DISPATCH_VNODE_WRITE: UInt ``` |
| To | ``` let DISPATCH_VNODE_WRITE: dispatch_source_vnode_flags_t ``` |

Modified [dispatch_walltime(_: UnsafePointer<timespec>, _: Int64) -> dispatch_time_t](https://developer.apple.com/documentation/dispatch/1420517-dispatch_walltime)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_walltime(_ when: UnsafePointer<timespec>, _ delta: Int64) -> dispatch_time_t ``` |
| To | ``` @warn_unused_result func dispatch_walltime(_ when: UnsafePointer<timespec>, _ delta: Int64) -> dispatch_time_t ``` |

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
