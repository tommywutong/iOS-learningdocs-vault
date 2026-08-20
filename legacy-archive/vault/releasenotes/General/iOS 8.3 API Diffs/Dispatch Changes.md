---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Dispatch.html
archived_at: '2026-07-18T02:56:24.526939Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Dispatch Changes

## Dispatch

Added NSEC_PER_MSECAdded NSEC_PER_SECAdded NSEC_PER_USECAdded USEC_PER_SECModified dispatch_after(dispatch_time_t, dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_after(_ when: dispatch_time_t, _ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_after(_ when: dispatch_time_t, _ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_after_f(dispatch_time_t, dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_after_f(_ when: dispatch_time_t, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_after_f(_ when: dispatch_time_t, _ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_apply(Int, dispatch_queue_t!,(Int) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_apply(_ iterations: UInt, _ queue: dispatch_queue_t!, _ block: ((UInt) -> Void)!) ``` |
| To | ``` func dispatch_apply(_ iterations: Int, _ queue: dispatch_queue_t!, _ block: (Int) -> Void) ``` |

Modified dispatch_apply_f(Int, dispatch_queue_t!, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> Void)>)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_apply_f(_ iterations: UInt, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt) -> Void)>) ``` |
| To | ``` func dispatch_apply_f(_ iterations: Int, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> Void)>) ``` |

Modified dispatch_async(dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_async(_ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_async(_ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_async_f(dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_async_f(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_async_f(_ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_barrier_async(dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_barrier_async(_ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_barrier_async(_ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_barrier_async_f(dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_barrier_async_f(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_barrier_async_f(_ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_barrier_sync(dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_barrier_sync(_ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_barrier_sync(_ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_barrier_sync_f(dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_barrier_sync_f(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_barrier_sync_f(_ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_block_cancel(dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_cancel(_ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_block_cancel(_ block: dispatch_block_t) ``` |

Modified dispatch_block_create(dispatch_block_flags_t, dispatch_block_t) -> dispatch_block_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_create(_ flags: dispatch_block_flags_t, _ block: dispatch_block_t!) -> dispatch_block_t! ``` |
| To | ``` func dispatch_block_create(_ flags: dispatch_block_flags_t, _ block: dispatch_block_t) -> dispatch_block_t! ``` |

Modified dispatch_block_create_with_qos_class(dispatch_block_flags_t, dispatch_qos_class_t, Int32, dispatch_block_t) -> dispatch_block_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_create_with_qos_class(_ flags: dispatch_block_flags_t, _ qos_class: dispatch_qos_class_t, _ relative_priority: Int32, _ block: dispatch_block_t!) -> dispatch_block_t! ``` |
| To | ``` func dispatch_block_create_with_qos_class(_ flags: dispatch_block_flags_t, _ qos_class: dispatch_qos_class_t, _ relative_priority: Int32, _ block: dispatch_block_t) -> dispatch_block_t! ``` |

Modified dispatch_block_notify(dispatch_block_t, dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_notify(_ block: dispatch_block_t!, _ queue: dispatch_queue_t!, _ notification_block: dispatch_block_t!) ``` |
| To | ``` func dispatch_block_notify(_ block: dispatch_block_t, _ queue: dispatch_queue_t, _ notification_block: dispatch_block_t) ``` |

Modified dispatch_block_perform(dispatch_block_flags_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_perform(_ flags: dispatch_block_flags_t, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_block_perform(_ flags: dispatch_block_flags_t, _ block: dispatch_block_t) ``` |

Modified dispatch_block_testcancel(dispatch_block_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_testcancel(_ block: dispatch_block_t!) -> Int ``` |
| To | ``` func dispatch_block_testcancel(_ block: dispatch_block_t) -> Int ``` |

Modified dispatch_block_wait(dispatch_block_t, dispatch_time_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_block_wait(_ block: dispatch_block_t!, _ timeout: dispatch_time_t) -> Int ``` |
| To | ``` func dispatch_block_wait(_ block: dispatch_block_t, _ timeout: dispatch_time_t) -> Int ``` |

Modified dispatch_data_applier_t

|  | Declaration |
| --- | --- |
| From | ``` typealias dispatch_data_applier_t = (dispatch_data_t!, UInt, UnsafePointer<Void>, UInt) -> Bool ``` |
| To | ``` typealias dispatch_data_applier_t = (dispatch_data_t!, Int, UnsafePointer<Void>, Int) -> Bool ``` |

Modified dispatch_data_apply(dispatch_data_t, dispatch_data_applier_t) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_apply(_ data: dispatch_data_t!, _ applier: dispatch_data_applier_t!) -> Bool ``` |
| To | ``` func dispatch_data_apply(_ data: dispatch_data_t, _ applier: dispatch_data_applier_t) -> Bool ``` |

Modified dispatch_data_copy_region(dispatch_data_t, Int, UnsafeMutablePointer<Int>) -> dispatch_data_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_copy_region(_ data: dispatch_data_t!, _ location: UInt, _ offset_ptr: UnsafeMutablePointer<UInt>) -> dispatch_data_t! ``` |
| To | ``` func dispatch_data_copy_region(_ data: dispatch_data_t, _ location: Int, _ offset_ptr: UnsafeMutablePointer<Int>) -> dispatch_data_t! ``` |

Modified dispatch_data_create(UnsafePointer<Void>, Int, dispatch_queue_t!, dispatch_block_t!) -> dispatch_data_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create(_ buffer: UnsafePointer<Void>, _ size: UInt, _ queue: dispatch_queue_t!, _ destructor: dispatch_block_t!) -> dispatch_data_t! ``` |
| To | ``` func dispatch_data_create(_ buffer: UnsafePointer<Void>, _ size: Int, _ queue: dispatch_queue_t!, _ destructor: dispatch_block_t!) -> dispatch_data_t! ``` |

Modified dispatch_data_create_concat(dispatch_data_t, dispatch_data_t) -> dispatch_data_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create_concat(_ data1: dispatch_data_t!, _ data2: dispatch_data_t!) -> dispatch_data_t! ``` |
| To | ``` func dispatch_data_create_concat(_ data1: dispatch_data_t, _ data2: dispatch_data_t) -> dispatch_data_t! ``` |

Modified dispatch_data_create_map(dispatch_data_t, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<Int>) -> dispatch_data_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create_map(_ data: dispatch_data_t!, _ buffer_ptr: UnsafeMutablePointer<UnsafePointer<Void>>, _ size_ptr: UnsafeMutablePointer<UInt>) -> dispatch_data_t! ``` |
| To | ``` func dispatch_data_create_map(_ data: dispatch_data_t, _ buffer_ptr: UnsafeMutablePointer<UnsafePointer<Void>>, _ size_ptr: UnsafeMutablePointer<Int>) -> dispatch_data_t! ``` |

Modified dispatch_data_create_subrange(dispatch_data_t, Int, Int) -> dispatch_data_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_create_subrange(_ data: dispatch_data_t!, _ offset: UInt, _ length: UInt) -> dispatch_data_t! ``` |
| To | ``` func dispatch_data_create_subrange(_ data: dispatch_data_t, _ offset: Int, _ length: Int) -> dispatch_data_t! ``` |

Modified dispatch_data_get_size(dispatch_data_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_data_get_size(_ data: dispatch_data_t!) -> UInt ``` |
| To | ``` func dispatch_data_get_size(_ data: dispatch_data_t) -> Int ``` |

Modified dispatch_get_context(dispatch_object_t) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_get_context(_ object: dispatch_object_t!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func dispatch_get_context(_ object: dispatch_object_t) -> UnsafeMutablePointer<Void> ``` |

Modified dispatch_group_async(dispatch_group_t, dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_async(_ group: dispatch_group_t!, _ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_group_async(_ group: dispatch_group_t, _ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_group_async_f(dispatch_group_t, dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_async_f(_ group: dispatch_group_t!, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_group_async_f(_ group: dispatch_group_t, _ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_group_enter(dispatch_group_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_enter(_ group: dispatch_group_t!) ``` |
| To | ``` func dispatch_group_enter(_ group: dispatch_group_t) ``` |

Modified dispatch_group_leave(dispatch_group_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_leave(_ group: dispatch_group_t!) ``` |
| To | ``` func dispatch_group_leave(_ group: dispatch_group_t) ``` |

Modified dispatch_group_notify(dispatch_group_t, dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_notify(_ group: dispatch_group_t!, _ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_group_notify(_ group: dispatch_group_t, _ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_group_notify_f(dispatch_group_t, dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_notify_f(_ group: dispatch_group_t!, _ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_group_notify_f(_ group: dispatch_group_t, _ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_group_wait(dispatch_group_t, dispatch_time_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_group_wait(_ group: dispatch_group_t!, _ timeout: dispatch_time_t) -> Int ``` |
| To | ``` func dispatch_group_wait(_ group: dispatch_group_t, _ timeout: dispatch_time_t) -> Int ``` |

Modified dispatch_io_barrier(dispatch_io_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_barrier(_ channel: dispatch_io_t!, _ barrier: dispatch_block_t!) ``` |
| To | ``` func dispatch_io_barrier(_ channel: dispatch_io_t, _ barrier: dispatch_block_t) ``` |

Modified dispatch_io_close(dispatch_io_t, dispatch_io_close_flags_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_close(_ channel: dispatch_io_t!, _ flags: dispatch_io_close_flags_t) ``` |
| To | ``` func dispatch_io_close(_ channel: dispatch_io_t, _ flags: dispatch_io_close_flags_t) ``` |

Modified dispatch_io_create_with_io(dispatch_io_type_t, dispatch_io_t, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_create_with_io(_ type: dispatch_io_type_t, _ io: dispatch_io_t!, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |
| To | ``` func dispatch_io_create_with_io(_ type: dispatch_io_type_t, _ io: dispatch_io_t, _ queue: dispatch_queue_t!, _ cleanup_handler: ((Int32) -> Void)!) -> dispatch_io_t! ``` |

Modified dispatch_io_get_descriptor(dispatch_io_t) -> dispatch_fd_t

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_get_descriptor(_ channel: dispatch_io_t!) -> dispatch_fd_t ``` |
| To | ``` func dispatch_io_get_descriptor(_ channel: dispatch_io_t) -> dispatch_fd_t ``` |

Modified dispatch_io_read(dispatch_io_t, off_t, Int, dispatch_queue_t, dispatch_io_handler_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_read(_ channel: dispatch_io_t!, _ offset: off_t, _ length: UInt, _ queue: dispatch_queue_t!, _ io_handler: dispatch_io_handler_t!) ``` |
| To | ``` func dispatch_io_read(_ channel: dispatch_io_t, _ offset: off_t, _ length: Int, _ queue: dispatch_queue_t, _ io_handler: dispatch_io_handler_t) ``` |

Modified dispatch_io_set_high_water(dispatch_io_t, Int)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_set_high_water(_ channel: dispatch_io_t!, _ high_water: UInt) ``` |
| To | ``` func dispatch_io_set_high_water(_ channel: dispatch_io_t, _ high_water: Int) ``` |

Modified dispatch_io_set_interval(dispatch_io_t, UInt64, dispatch_io_interval_flags_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_set_interval(_ channel: dispatch_io_t!, _ interval: UInt64, _ flags: dispatch_io_interval_flags_t) ``` |
| To | ``` func dispatch_io_set_interval(_ channel: dispatch_io_t, _ interval: UInt64, _ flags: dispatch_io_interval_flags_t) ``` |

Modified dispatch_io_set_low_water(dispatch_io_t, Int)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_set_low_water(_ channel: dispatch_io_t!, _ low_water: UInt) ``` |
| To | ``` func dispatch_io_set_low_water(_ channel: dispatch_io_t, _ low_water: Int) ``` |

Modified dispatch_io_write(dispatch_io_t, off_t, dispatch_data_t, dispatch_queue_t, dispatch_io_handler_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_io_write(_ channel: dispatch_io_t!, _ offset: off_t, _ data: dispatch_data_t!, _ queue: dispatch_queue_t!, _ io_handler: dispatch_io_handler_t!) ``` |
| To | ``` func dispatch_io_write(_ channel: dispatch_io_t, _ offset: off_t, _ data: dispatch_data_t, _ queue: dispatch_queue_t, _ io_handler: dispatch_io_handler_t) ``` |

Modified dispatch_once(UnsafeMutablePointer<dispatch_once_t>, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_once(_ predicate: UnsafeMutablePointer<dispatch_once_t>, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_once(_ predicate: UnsafeMutablePointer<dispatch_once_t>, _ block: dispatch_block_t) ``` |

Modified dispatch_queue_get_qos_class(dispatch_queue_t, UnsafeMutablePointer<Int32>) -> dispatch_qos_class_t

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_get_qos_class(_ queue: dispatch_queue_t!, _ relative_priority_ptr: UnsafeMutablePointer<Int32>) -> dispatch_qos_class_t ``` |
| To | ``` func dispatch_queue_get_qos_class(_ queue: dispatch_queue_t, _ relative_priority_ptr: UnsafeMutablePointer<Int32>) -> dispatch_qos_class_t ``` |

Modified dispatch_queue_get_specific(dispatch_queue_t, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_get_specific(_ queue: dispatch_queue_t!, _ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func dispatch_queue_get_specific(_ queue: dispatch_queue_t, _ key: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified dispatch_queue_set_specific(dispatch_queue_t, UnsafePointer<Void>, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_queue_set_specific(_ queue: dispatch_queue_t!, _ key: UnsafePointer<Void>, _ context: UnsafeMutablePointer<Void>, _ destructor: dispatch_function_t) ``` |
| To | ``` func dispatch_queue_set_specific(_ queue: dispatch_queue_t, _ key: UnsafePointer<Void>, _ context: UnsafeMutablePointer<Void>, _ destructor: dispatch_function_t) ``` |

Modified dispatch_read(dispatch_fd_t, Int, dispatch_queue_t,(dispatch_data_t!, Int32) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_read(_ fd: dispatch_fd_t, _ length: UInt, _ queue: dispatch_queue_t!, _ handler: ((dispatch_data_t!, Int32) -> Void)!) ``` |
| To | ``` func dispatch_read(_ fd: dispatch_fd_t, _ length: Int, _ queue: dispatch_queue_t, _ handler: (dispatch_data_t!, Int32) -> Void) ``` |

Modified dispatch_resume(dispatch_object_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_resume(_ object: dispatch_object_t!) ``` |
| To | ``` func dispatch_resume(_ object: dispatch_object_t) ``` |

Modified dispatch_semaphore_signal(dispatch_semaphore_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_semaphore_signal(_ dsema: dispatch_semaphore_t!) -> Int ``` |
| To | ``` func dispatch_semaphore_signal(_ dsema: dispatch_semaphore_t) -> Int ``` |

Modified dispatch_semaphore_wait(dispatch_semaphore_t, dispatch_time_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_semaphore_wait(_ dsema: dispatch_semaphore_t!, _ timeout: dispatch_time_t) -> Int ``` |
| To | ``` func dispatch_semaphore_wait(_ dsema: dispatch_semaphore_t, _ timeout: dispatch_time_t) -> Int ``` |

Modified dispatch_source_cancel(dispatch_source_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_cancel(_ source: dispatch_source_t!) ``` |
| To | ``` func dispatch_source_cancel(_ source: dispatch_source_t) ``` |

Modified dispatch_source_get_data(dispatch_source_t) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_get_data(_ source: dispatch_source_t!) -> UInt ``` |
| To | ``` func dispatch_source_get_data(_ source: dispatch_source_t) -> UInt ``` |

Modified dispatch_source_get_handle(dispatch_source_t) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_get_handle(_ source: dispatch_source_t!) -> UInt ``` |
| To | ``` func dispatch_source_get_handle(_ source: dispatch_source_t) -> UInt ``` |

Modified dispatch_source_get_mask(dispatch_source_t) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_get_mask(_ source: dispatch_source_t!) -> UInt ``` |
| To | ``` func dispatch_source_get_mask(_ source: dispatch_source_t) -> UInt ``` |

Modified dispatch_source_merge_data(dispatch_source_t, UInt)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_merge_data(_ source: dispatch_source_t!, _ value: UInt) ``` |
| To | ``` func dispatch_source_merge_data(_ source: dispatch_source_t, _ value: UInt) ``` |

Modified dispatch_source_set_cancel_handler(dispatch_source_t, dispatch_block_t!)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_cancel_handler(_ source: dispatch_source_t!, _ handler: dispatch_block_t!) ``` |
| To | ``` func dispatch_source_set_cancel_handler(_ source: dispatch_source_t, _ handler: dispatch_block_t!) ``` |

Modified dispatch_source_set_cancel_handler_f(dispatch_source_t, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_cancel_handler_f(_ source: dispatch_source_t!, _ handler: dispatch_function_t) ``` |
| To | ``` func dispatch_source_set_cancel_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t) ``` |

Modified dispatch_source_set_event_handler(dispatch_source_t, dispatch_block_t!)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_event_handler(_ source: dispatch_source_t!, _ handler: dispatch_block_t!) ``` |
| To | ``` func dispatch_source_set_event_handler(_ source: dispatch_source_t, _ handler: dispatch_block_t!) ``` |

Modified dispatch_source_set_event_handler_f(dispatch_source_t, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_event_handler_f(_ source: dispatch_source_t!, _ handler: dispatch_function_t) ``` |
| To | ``` func dispatch_source_set_event_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t) ``` |

Modified dispatch_source_set_registration_handler(dispatch_source_t, dispatch_block_t!)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_registration_handler(_ source: dispatch_source_t!, _ handler: dispatch_block_t!) ``` |
| To | ``` func dispatch_source_set_registration_handler(_ source: dispatch_source_t, _ handler: dispatch_block_t!) ``` |

Modified dispatch_source_set_registration_handler_f(dispatch_source_t, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_registration_handler_f(_ source: dispatch_source_t!, _ handler: dispatch_function_t) ``` |
| To | ``` func dispatch_source_set_registration_handler_f(_ source: dispatch_source_t, _ handler: dispatch_function_t) ``` |

Modified dispatch_source_set_timer(dispatch_source_t, dispatch_time_t, UInt64, UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_set_timer(_ source: dispatch_source_t!, _ start: dispatch_time_t, _ interval: UInt64, _ leeway: UInt64) ``` |
| To | ``` func dispatch_source_set_timer(_ source: dispatch_source_t, _ start: dispatch_time_t, _ interval: UInt64, _ leeway: UInt64) ``` |

Modified dispatch_source_testcancel(dispatch_source_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_source_testcancel(_ source: dispatch_source_t!) -> Int ``` |
| To | ``` func dispatch_source_testcancel(_ source: dispatch_source_t) -> Int ``` |

Modified dispatch_suspend(dispatch_object_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_suspend(_ object: dispatch_object_t!) ``` |
| To | ``` func dispatch_suspend(_ object: dispatch_object_t) ``` |

Modified dispatch_sync(dispatch_queue_t, dispatch_block_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_sync(_ queue: dispatch_queue_t!, _ block: dispatch_block_t!) ``` |
| To | ``` func dispatch_sync(_ queue: dispatch_queue_t, _ block: dispatch_block_t) ``` |

Modified dispatch_sync_f(dispatch_queue_t, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_sync_f(_ queue: dispatch_queue_t!, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |
| To | ``` func dispatch_sync_f(_ queue: dispatch_queue_t, _ context: UnsafeMutablePointer<Void>, _ work: dispatch_function_t) ``` |

Modified dispatch_write(dispatch_fd_t, dispatch_data_t, dispatch_queue_t,(dispatch_data_t!, Int32) -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func dispatch_write(_ fd: dispatch_fd_t, _ data: dispatch_data_t!, _ queue: dispatch_queue_t!, _ handler: ((dispatch_data_t!, Int32) -> Void)!) ``` |
| To | ``` func dispatch_write(_ fd: dispatch_fd_t, _ data: dispatch_data_t, _ queue: dispatch_queue_t, _ handler: (dispatch_data_t!, Int32) -> Void) ``` |

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
