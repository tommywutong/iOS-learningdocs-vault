---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/Dispatch.html
archived_at: '2026-07-15T07:34:54.232611Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Dispatch Changes

## Dispatch (Added)

Added OS_dispatch_dataAdded OS_dispatch_groupAdded OS_dispatch_ioAdded OS_dispatch_objectAdded OS_dispatch_queueAdded OS_dispatch_queue_attrAdded OS_dispatch_semaphoreAdded OS_dispatch_sourceAdded dispatch_block_flags_t [struct]Added dispatch_block_flags_t.init(_: UInt)Added dispatch_block_flags_t.valueAdded DISPATCH_API_VERSIONAdded DISPATCH_BLOCK_ASSIGN_CURRENTAdded DISPATCH_BLOCK_BARRIERAdded DISPATCH_BLOCK_DETACHEDAdded DISPATCH_BLOCK_ENFORCE_QOS_CLASSAdded DISPATCH_BLOCK_INHERIT_QOS_CLASSAdded DISPATCH_BLOCK_NO_QOS_CLASSAdded DISPATCH_CURRENT_QUEUE_LABELAdded DISPATCH_IO_RANDOMAdded DISPATCH_IO_STOPAdded DISPATCH_IO_STREAMAdded DISPATCH_IO_STRICT_INTERVALAdded DISPATCH_MACH_SEND_DEADAdded DISPATCH_MEMORYPRESSURE_CRITICALAdded DISPATCH_MEMORYPRESSURE_NORMALAdded DISPATCH_MEMORYPRESSURE_WARNAdded DISPATCH_PROC_EXECAdded DISPATCH_PROC_EXITAdded DISPATCH_PROC_FORKAdded DISPATCH_PROC_SIGNALAdded DISPATCH_QUEUE_CONCURRENTAdded DISPATCH_QUEUE_PRIORITY_BACKGROUNDAdded DISPATCH_QUEUE_PRIORITY_DEFAULTAdded DISPATCH_QUEUE_PRIORITY_HIGHAdded DISPATCH_QUEUE_PRIORITY_LOWAdded DISPATCH_QUEUE_SERIALAdded DISPATCH_SOURCE_TYPE_DATA_ADDAdded DISPATCH_SOURCE_TYPE_DATA_ORAdded DISPATCH_SOURCE_TYPE_MACH_RECVAdded DISPATCH_SOURCE_TYPE_MACH_SENDAdded DISPATCH_SOURCE_TYPE_MEMORYPRESSUREAdded DISPATCH_SOURCE_TYPE_PROCAdded DISPATCH_SOURCE_TYPE_READAdded DISPATCH_SOURCE_TYPE_SIGNALAdded DISPATCH_SOURCE_TYPE_TIMERAdded DISPATCH_SOURCE_TYPE_VNODEAdded DISPATCH_SOURCE_TYPE_WRITEAdded DISPATCH_TARGET_QUEUE_DEFAULTAdded DISPATCH_TIMER_STRICTAdded DISPATCH_TIME_FOREVERAdded DISPATCH_TIME_NOWAdded DISPATCH_VNODE_ATTRIBAdded DISPATCH_VNODE_DELETEAdded DISPATCH_VNODE_EXTENDAdded DISPATCH_VNODE_LINKAdded DISPATCH_VNODE_RENAMEAdded DISPATCH_VNODE_REVOKEAdded DISPATCH_VNODE_WRITEAdded dispatch_after(dispatch_time_t, dispatch_queue_t!, dispatch_block_t!)Added dispatch_after_f(dispatch_time_t, dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_apply(UInt, dispatch_queue_t!,((UInt) -> Void)!)Added dispatch_apply_f(UInt, dispatch_queue_t!, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UInt) -> Void)>)Added dispatch_async(dispatch_queue_t!, dispatch_block_t!)Added dispatch_async_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_barrier_async(dispatch_queue_t!, dispatch_block_t!)Added dispatch_barrier_async_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_barrier_sync(dispatch_queue_t!, dispatch_block_t!)Added dispatch_barrier_sync_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_block_cancel(dispatch_block_t!)Added dispatch_block_create(dispatch_block_flags_t, dispatch_block_t!) -> dispatch_block_t!Added dispatch_block_create_with_qos_class(dispatch_block_flags_t, dispatch_qos_class_t, Int32, dispatch_block_t!) -> dispatch_block_t!Added dispatch_block_notify(dispatch_block_t!, dispatch_queue_t!, dispatch_block_t!)Added dispatch_block_perform(dispatch_block_flags_t, dispatch_block_t!)Added dispatch_block_tAdded dispatch_block_testcancel(dispatch_block_t!) -> IntAdded dispatch_block_wait(dispatch_block_t!, dispatch_time_t) -> IntAdded dispatch_data_applier_tAdded dispatch_data_apply(dispatch_data_t!, dispatch_data_applier_t!) -> BoolAdded dispatch_data_copy_region(dispatch_data_t!, UInt, UnsafeMutablePointer<UInt>) -> dispatch_data_t!Added dispatch_data_create(UnsafePointer<Void>, UInt, dispatch_queue_t!, dispatch_block_t!) -> dispatch_data_t!Added dispatch_data_create_concat(dispatch_data_t!, dispatch_data_t!) -> dispatch_data_t!Added dispatch_data_create_map(dispatch_data_t!, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt>) -> dispatch_data_t!Added dispatch_data_create_subrange(dispatch_data_t!, UInt, UInt) -> dispatch_data_t!Added dispatch_data_emptyAdded dispatch_data_get_size(dispatch_data_t!) -> UIntAdded dispatch_data_tAdded dispatch_fd_tAdded dispatch_function_tAdded dispatch_get_context(dispatch_object_t!) -> UnsafeMutablePointer<Void>Added dispatch_get_global_queue(Int, UInt) -> dispatch_queue_t!Added dispatch_get_global_queue(qos_class_t, UInt) -> dispatch_queue_tAdded dispatch_get_main_queue() -> dispatch_queue_t!Added dispatch_get_specific(UnsafePointer<Void>) -> UnsafeMutablePointer<Void>Added dispatch_group_async(dispatch_group_t!, dispatch_queue_t!, dispatch_block_t!)Added dispatch_group_async_f(dispatch_group_t!, dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_group_create() -> dispatch_group_t!Added dispatch_group_enter(dispatch_group_t!)Added dispatch_group_leave(dispatch_group_t!)Added dispatch_group_notify(dispatch_group_t!, dispatch_queue_t!, dispatch_block_t!)Added dispatch_group_notify_f(dispatch_group_t!, dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_group_tAdded dispatch_group_wait(dispatch_group_t!, dispatch_time_t) -> IntAdded dispatch_introspection_hook_queue_callout_begin(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_introspection_hook_queue_callout_end(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_introspection_hook_queue_create(dispatch_queue_t!)Added dispatch_introspection_hook_queue_destroy(dispatch_queue_t!)Added dispatch_introspection_hook_queue_item_complete(dispatch_object_t!)Added dispatch_introspection_hook_queue_item_dequeue(dispatch_queue_t!, dispatch_object_t!)Added dispatch_introspection_hook_queue_item_enqueue(dispatch_queue_t!, dispatch_object_t!)Added dispatch_io_barrier(dispatch_io_t!, dispatch_block_t!)Added dispatch_io_close(dispatch_io_t!, dispatch_io_close_flags_t)Added dispatch_io_close_flags_tAdded dispatch_io_create(dispatch_io_type_t, dispatch_fd_t, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!Added dispatch_io_create_with_io(dispatch_io_type_t, dispatch_io_t!, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!Added dispatch_io_create_with_path(dispatch_io_type_t, UnsafePointer<Int8>, Int32, mode_t, dispatch_queue_t!,((Int32) -> Void)!) -> dispatch_io_t!Added dispatch_io_get_descriptor(dispatch_io_t!) -> dispatch_fd_tAdded dispatch_io_handler_tAdded dispatch_io_interval_flags_tAdded dispatch_io_read(dispatch_io_t!, off_t, UInt, dispatch_queue_t!, dispatch_io_handler_t!)Added dispatch_io_set_high_water(dispatch_io_t!, UInt)Added dispatch_io_set_interval(dispatch_io_t!, UInt64, dispatch_io_interval_flags_t)Added dispatch_io_set_low_water(dispatch_io_t!, UInt)Added dispatch_io_tAdded dispatch_io_type_tAdded dispatch_io_write(dispatch_io_t!, off_t, dispatch_data_t!, dispatch_queue_t!, dispatch_io_handler_t!)Added dispatch_main()Added dispatch_object_tAdded dispatch_once(UnsafeMutablePointer<dispatch_once_t>, dispatch_block_t!)Added dispatch_once_f(UnsafeMutablePointer<dispatch_once_t>, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_once_tAdded dispatch_qos_class_tAdded dispatch_queue_attr_make_with_qos_class(dispatch_queue_attr_t!, dispatch_qos_class_t, Int32) -> dispatch_queue_attr_t!Added dispatch_queue_attr_tAdded dispatch_queue_create(UnsafePointer<Int8>, dispatch_queue_attr_t!) -> dispatch_queue_t!Added dispatch_queue_get_label(dispatch_queue_t!) -> UnsafePointer<Int8>Added dispatch_queue_get_qos_class(dispatch_queue_t!, UnsafeMutablePointer<Int32>) -> dispatch_qos_class_tAdded dispatch_queue_get_specific(dispatch_queue_t!, UnsafePointer<Void>) -> UnsafeMutablePointer<Void>Added dispatch_queue_priority_tAdded dispatch_queue_set_specific(dispatch_queue_t!, UnsafePointer<Void>, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_queue_tAdded dispatch_read(dispatch_fd_t, UInt, dispatch_queue_t!,((dispatch_data_t!, Int32) -> Void)!)Added dispatch_resume(dispatch_object_t!)Added dispatch_semaphore_create(Int) -> dispatch_semaphore_t!Added dispatch_semaphore_signal(dispatch_semaphore_t!) -> IntAdded dispatch_semaphore_tAdded dispatch_semaphore_wait(dispatch_semaphore_t!, dispatch_time_t) -> IntAdded dispatch_set_context(dispatch_object_t!, UnsafeMutablePointer<Void>)Added dispatch_set_finalizer_f(dispatch_object_t!, dispatch_function_t)Added dispatch_set_target_queue(dispatch_object_t!, dispatch_queue_t!)Added dispatch_source_cancel(dispatch_source_t!)Added dispatch_source_create(dispatch_source_type_t, UInt, UInt, dispatch_queue_t!) -> dispatch_source_t!Added dispatch_source_get_data(dispatch_source_t!) -> UIntAdded dispatch_source_get_handle(dispatch_source_t!) -> UIntAdded dispatch_source_get_mask(dispatch_source_t!) -> UIntAdded dispatch_source_mach_send_flags_tAdded dispatch_source_memorypressure_flags_tAdded dispatch_source_merge_data(dispatch_source_t!, UInt)Added dispatch_source_proc_flags_tAdded dispatch_source_set_cancel_handler(dispatch_source_t!, dispatch_block_t!)Added dispatch_source_set_cancel_handler_f(dispatch_source_t!, dispatch_function_t)Added dispatch_source_set_event_handler(dispatch_source_t!, dispatch_block_t!)Added dispatch_source_set_event_handler_f(dispatch_source_t!, dispatch_function_t)Added dispatch_source_set_registration_handler(dispatch_source_t!, dispatch_block_t!)Added dispatch_source_set_registration_handler_f(dispatch_source_t!, dispatch_function_t)Added dispatch_source_set_timer(dispatch_source_t!, dispatch_time_t, UInt64, UInt64)Added dispatch_source_tAdded dispatch_source_testcancel(dispatch_source_t!) -> IntAdded dispatch_source_timer_flags_tAdded dispatch_source_type_tAdded dispatch_source_vnode_flags_tAdded dispatch_suspend(dispatch_object_t!)Added dispatch_sync(dispatch_queue_t!, dispatch_block_t!)Added dispatch_sync_f(dispatch_queue_t!, UnsafeMutablePointer<Void>, dispatch_function_t)Added dispatch_time(dispatch_time_t, Int64) -> dispatch_time_tAdded dispatch_time_tAdded dispatch_walltime(UnsafePointer<timespec>, Int64) -> dispatch_time_tAdded dispatch_write(dispatch_fd_t, dispatch_data_t!, dispatch_queue_t!,((dispatch_data_t!, Int32) -> Void)!)

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
