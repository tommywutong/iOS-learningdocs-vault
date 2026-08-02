---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Dispatch.html
archived_at: '2026-07-18T02:56:11.547902Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Dispatch Changes

## Dispatch

Removed dispatch_release(dispatch_object_t!)Removed dispatch_retain(dispatch_object_t!)Added dispatch_data_emptyAdded dispatch_get_global_queue(qos_class_t, UInt) -> dispatch_queue_tModified dispatch_after(dispatch_time_t, dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_after_f(dispatch_time_t, dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_apply(UInt, dispatch_queue_t!,((UInt) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_apply_f(UInt, dispatch_queue_t!, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UInt) -> Void)>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_async(dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_async_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_barrier_async(dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified dispatch_barrier_async_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified dispatch_barrier_sync(dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified dispatch_barrier_sync_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified dispatch_data_apply(dispatch_data_t!, dispatch_data_applier_t!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_data_copy_region(dispatch_data_t!, UInt, UnsafeMutablePointer<UInt>) -> dispatch_data_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_data_create(UnsafePointer<Void>, UInt, dispatch_queue_t!, dispatch_block_t!) -> dispatch_data_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_data_create_concat(dispatch_data_t!, dispatch_data_t!) -> dispatch_data_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_data_create_map(dispatch_data_t!, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt>) -> dispatch_data_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_data_create_subrange(dispatch_data_t!, UInt, UInt) -> dispatch_data_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_data_get_size(dispatch_data_t!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_get_context(dispatch_object_t!) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_get_global_queue(Int, UInt) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_get_specific(UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_group_async(dispatch_group_t!, dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_async_f(dispatch_group_t!, dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_create() -> dispatch_group_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_enter(dispatch_group_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_leave(dispatch_group_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_notify(dispatch_group_t!, dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_notify_f(dispatch_group_t!, dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_group_wait(dispatch_group_t!, dispatch_time_t) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_introspection_hook_queue_callout_begin(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified dispatch_introspection_hook_queue_callout_end(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified dispatch_introspection_hook_queue_create(dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified dispatch_introspection_hook_queue_destroy(dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified dispatch_introspection_hook_queue_item_complete(dispatch_object_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified dispatch_introspection_hook_queue_item_dequeue(dispatch_queue_t!, dispatch_object_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified dispatch_introspection_hook_queue_item_enqueue(dispatch_queue_t!, dispatch_object_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified dispatch_io_barrier(dispatch_io_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_close(dispatch_io_t!, dispatch_io_close_flags_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_create(dispatch_io_type_t, dispatch_fd_t, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_create_with_io(dispatch_io_type_t, dispatch_io_t!, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_create_with_path(dispatch_io_type_t, UnsafePointer<Int8>, Int32, mode_t, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_get_descriptor(dispatch_io_t!) -> dispatch_fd_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_read(dispatch_io_t!, off_t, UInt, dispatch_queue_t!, dispatch_io_handler_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_set_high_water(dispatch_io_t!, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_set_interval(dispatch_io_t!, UInt64, dispatch_io_interval_flags_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_set_low_water(dispatch_io_t!, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_io_write(dispatch_io_t!, off_t, dispatch_data_t!, dispatch_queue_t!, dispatch_io_handler_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_main()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_once(UnsafeMutablePointer<dispatch_once_t>, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_once_f(UnsafeMutablePointer<dispatch_once_t>, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_queue_create(UnsafePointer<Int8>, dispatch_queue_attr_t!) -> dispatch_queue_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_queue_get_label(dispatch_queue_t!) -> UnsafePointer<Int8>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_queue_get_specific(dispatch_queue_t!, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_queue_set_specific(dispatch_queue_t!, UnsafePointer<Void>, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_read(dispatch_fd_t, UInt, dispatch_queue_t!,((dispatch_data_t!, Int32) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified dispatch_resume(dispatch_object_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_semaphore_create(Int) -> dispatch_semaphore_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_semaphore_signal(dispatch_semaphore_t!) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_semaphore_wait(dispatch_semaphore_t!, dispatch_time_t) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_set_context(dispatch_object_t!, UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_set_finalizer_f(dispatch_object_t!, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_set_target_queue(dispatch_object_t!, dispatch_queue_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_cancel(dispatch_source_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_create(dispatch_source_type_t, UInt, UInt, dispatch_queue_t!) -> dispatch_source_t!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_get_data(dispatch_source_t!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_get_handle(dispatch_source_t!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_get_mask(dispatch_source_t!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_merge_data(dispatch_source_t!, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_set_cancel_handler(dispatch_source_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_set_cancel_handler_f(dispatch_source_t!, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_set_event_handler(dispatch_source_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_set_event_handler_f(dispatch_source_t!, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_set_registration_handler(dispatch_source_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified dispatch_source_set_registration_handler_f(dispatch_source_t!, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified dispatch_source_set_timer(dispatch_source_t!, dispatch_time_t, UInt64, UInt64)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_source_testcancel(dispatch_source_t!) -> Int

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_suspend(dispatch_object_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_sync(dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_sync_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_time(dispatch_time_t, Int64) -> dispatch_time_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_walltime(UnsafePointer<timespec>, Int64) -> dispatch_time_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified dispatch_write(dispatch_fd_t, dispatch_data_t!, dispatch_queue_t!,((dispatch_data_t!, Int32) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

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
