---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/usr_include.html
archived_at: '2026-07-18T02:57:28.794462Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# /usr/include Changes for Objective-C

### /usr/include

#### /usr/include/dispatch/base.h

Added #def DISPATCH_ALIAS_V2Added #def DISPATCH_ASSUME_NONNULL_BEGINAdded #def DISPATCH_ASSUME_NONNULL_ENDAdded #def dispatch_compiler_barrierAdded #def DISPATCH_COMPILER_CAN_ASSUMEAdded #def DISPATCH_ENUM_AVAILABLEAdded #def DISPATCH_LINUX_UNAVAILABLEAdded #def DISPATCH_NOESCAPEAdded #def DISPATCH_NOT_TAIL_CALLEDAdded #def DISPATCH_REFINED_FOR_SWIFTAdded [#def DISPATCH_SWIFT3_OVERLAY](https://developer.apple.com/documentation/dispatch/dispatch_swift3_overlay)Added #def DISPATCH_SWIFT3_UNAVAILABLEAdded #def DISPATCH_SWIFT_NAMEAdded #def DISPATCH_SWIFT_UNAVAILABLEAdded #def DISPATCH_UNAVAILABLE_MSG

#### /usr/include/dispatch/object.h

Added [dispatch_activate()](https://developer.apple.com/documentation/dispatch/dispatchobject/1641002-activate)Added #def DISPATCH_DATA_DECLAdded #def DISPATCH_SOURCE_DECLModified #def DISPATCH_SOURCE_TYPE_DECL

|  | Header |
| --- | --- |
| From | dispatch/source.h |
| To | dispatch/object.h |

#### /usr/include/dispatch/queue.h

Added [dispatch_assert_queue()](https://developer.apple.com/documentation/dispatch/1642201-dispatch_assert_queue)Added [dispatch_assert_queue_barrier()](https://developer.apple.com/documentation/dispatch/1642195-dispatch_assert_queue_barrier)Added #def dispatch_assert_queue_barrier_debugAdded #def dispatch_assert_queue_debugAdded [dispatch_assert_queue_not()](https://developer.apple.com/documentation/dispatch/1642199-dispatch_assert_queue_not)Added #def dispatch_assert_queue_not_debugAdded [DISPATCH_AUTORELEASE_FREQUENCY_INHERIT](https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_inherit)Added [DISPATCH_AUTORELEASE_FREQUENCY_NEVER](https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_never)Added [dispatch_autorelease_frequency_t](https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t)Added [DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM](https://developer.apple.com/documentation/dispatch/dispatch_autorelease_frequency_t/dispatch_autorelease_frequency_work_item)Added [dispatch_queue_attr_make_initially_inactive()](https://developer.apple.com/documentation/dispatch/1642194-dispatch_queue_attr_make_initial)Added [dispatch_queue_attr_make_with_autorelease_frequency()](https://developer.apple.com/documentation/dispatch/1642197-dispatch_queue_attr_make_with_au)Added #def DISPATCH_QUEUE_CONCURRENT_INACTIVEAdded #def DISPATCH_QUEUE_CONCURRENT_WITH_AUTORELEASE_POOLAdded [dispatch_queue_create_with_target()](https://developer.apple.com/documentation/dispatch/1642205-dispatch_queue_create_with_targe)Added #def DISPATCH_QUEUE_SERIAL_INACTIVEAdded #def DISPATCH_QUEUE_SERIAL_WITH_AUTORELEASE_POOL

#### /usr/include/dispatch/source.h

Added [#def DISPATCH_VNODE_FUNLOCK](https://developer.apple.com/documentation/dispatch/dispatch_vnode_funlock)Modified #def DISPATCH_SOURCE_TYPE_DECL

|  | Header |
| --- | --- |
| From | dispatch/source.h |
| To | dispatch/object.h |

#### /usr/include/mach-o/arch.h

Added NXFindBestFatArch_64()

#### /usr/include/mach-o/dyld_images.h

Added #def DYLD_MAX_PROCESS_INFO_NOTIFY_COUNT

#### /usr/include/mach-o/fat.h

Added fat_arch_64Added #def FAT_CIGAM_64Added #def FAT_MAGIC_64

#### /usr/include/mach-o/ranlib.h

Added ranlib_64Added #def SYMDEF_64Added #def SYMDEF_64_SORTED

#### /usr/include/mach-o/swap.h

Added swap_fat_arch_64()Added swap_ranlib_64()

#### /usr/include/objc/NSObject.h

Modified [-[NSObject finalize]](https://developer.apple.com/documentation/objectivec/nsobject/1418513-finalize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

#### /usr/include/objc/objc-api.h

Added #def OBJC_AVAILABLEAdded #def OBJC_DEPRECATEDAdded #def OBJC_UNAVAILABLE

#### /usr/include/objc/objc-auto.h

Added #def OBJC_GC_DEPRECATEDModified [objc_assign_threadlocal()](https://developer.apple.com/documentation/objectivec/1418937-objc_assign_threadlocal)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

#### /usr/include/objc/runtime.h

Added [object_setInstanceVariableWithStrongDefault()](https://developer.apple.com/documentation/objectivec/1644111-object_setinstancevariablewithst)Added [object_setIvarWithStrongDefault()](https://developer.apple.com/documentation/objectivec/1642779-object_setivarwithstrongdefault)Added [protocol_copyPropertyList2()](https://developer.apple.com/documentation/objectivec/1642782-protocol_copypropertylist2)Modified [class_setSuperclass()](https://developer.apple.com/documentation/objectivec/1441536-class_setsuperclass)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.0 |

#### /usr/include/os/activity.h

Removed [OS_ACTIVITY_FLAG_DEFAULT](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_default)Removed [OS_ACTIVITY_FLAG_DETACHED](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_detached)Added OS_os_activityAdded [os_activity_apply()](https://developer.apple.com/documentation/os/1772461-os_activity_apply)Added [os_activity_apply_f()](https://developer.apple.com/documentation/os/1772453-os_activity_apply_f)Added [#def os_activity_create](https://developer.apple.com/documentation/os/os_activity_create)Added [#def OS_ACTIVITY_CURRENT](https://developer.apple.com/reference/os/os_activity_current)Added [OS_ACTIVITY_FLAG_DEFAULT](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_default)Added [OS_ACTIVITY_FLAG_DETACHED](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_detached)Added [OS_ACTIVITY_FLAG_IF_NONE_PRESENT](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_if_none_present)Added [os_activity_get_identifier()](https://developer.apple.com/documentation/os/1772460-os_activity_get_identifier)Added [os_activity_id_t](https://developer.apple.com/documentation/os/os_activity_id_t)Added #def os_activity_label_useractionAdded [#def OS_ACTIVITY_NONE](https://developer.apple.com/reference/os/os_activity_none)Added #def OS_ACTIVITY_OBJECT_APIAdded #def os_activity_scopeAdded [os_activity_scope_enter()](https://developer.apple.com/documentation/os/1772456-os_activity_scope_enter)Added [os_activity_scope_leave()](https://developer.apple.com/documentation/os/1772455-os_activity_scope_leave)Added [os_activity_scope_state_t](https://developer.apple.com/documentation/os/os_activity_scope_state_t)Added #def OS_LOG_STRINGModified [os_activity_end()](https://developer.apple.com/documentation/os/1478194-os_activity_end)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` void os_activity_end (     os_activity_t activity_id ); ``` | tvOS 9.1 | -- |
| To | ``` void os_activity_end (     os_activity_t activity ); ``` | tvOS 9.0 | tvOS 10.0 |

Modified [os_activity_get_active()](https://developer.apple.com/documentation/os/1478192-os_activity_get_active)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` unsigned int os_activity_get_active (     os_activity_t *entries,     unsigned int *count ); ``` | tvOS 9.1 | -- |
| To | ``` unsigned int os_activity_get_active (     os_activity_id_t *entries,     unsigned int *count ); ``` | tvOS 9.0 | tvOS 10.0 |

Modified [os_breadcrumb_t](https://developer.apple.com/documentation/os/os_breadcrumb_t)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | tvOS 9.1 | -- |
| To | tvOS 9.0 | tvOS 10.0 |

#### /usr/include/os/availability.h (Added)

Added #def API_AVAILABLEAdded #def API_DEPRECATEDAdded #def API_DEPRECATED_WITH_REPLACEMENTAdded #def API_UNAVAILABLE

#### /usr/include/os/base.h

Added #def OS_ASSUME_NONNULL_BEGINAdded #def OS_ASSUME_NONNULL_ENDAdded [os_block_t](https://developer.apple.com/documentation/os/os_block_t)Added #def OS_COLDAdded #def os_compiler_barrierAdded #def OS_COMPILER_CAN_ASSUMEAdded [os_function_t](https://developer.apple.com/documentation/os/os_function_t)Added #def os_is_compile_time_constantAdded #def OS_NOESCAPEAdded #def OS_NOT_TAIL_CALLEDAdded #def os_prevent_tail_call_optimizationAdded #def OS_REFINED_FOR_SWIFTAdded #def OS_SWIFT_NAMEAdded #def OS_SWIFT_UNAVAILABLE

#### /usr/include/os/lock.h (Added)

Added #def OS_LOCK_API_VERSIONAdded [os_unfair_lock](https://developer.apple.com/documentation/os/os_unfair_lock)Added #def OS_UNFAIR_LOCK_AVAILABILITYAdded #def OS_UNFAIR_LOCK_INITAdded [os_unfair_lock_lock()](https://developer.apple.com/documentation/os/1646466-os_unfair_lock_lock)Added [os_unfair_lock_t](https://developer.apple.com/documentation/os/os_unfair_lock_t)Added [os_unfair_lock_trylock()](https://developer.apple.com/documentation/os/1646469-os_unfair_lock_trylock)Added [os_unfair_lock_unlock()](https://developer.apple.com/documentation/os/1646463-os_unfair_lock_unlock)

#### /usr/include/os/log.h (Added)

Added [OS_os_log](https://developer.apple.com/documentation/kernel/os_os_log)Added [#def os_log](https://developer.apple.com/documentation/os/os_log)Added [os_log_create()](https://developer.apple.com/documentation/os/oslog/1643744-init)Added [#def os_log_debug](https://developer.apple.com/documentation/os/os_log_debug)Added #def OS_LOG_DEBUGAdded [#def os_log_debug_enabled](https://developer.apple.com/documentation/os/os_log_debug_enabled)Added [#def OS_LOG_DEFAULT](https://developer.apple.com/documentation/os/os_log_default)Added [#def OS_LOG_DISABLED](https://developer.apple.com/documentation/os/os_log_disabled)Added #def OS_LOG_ERRORAdded [#def os_log_error](https://developer.apple.com/documentation/os/os_log_error)Added #def OS_LOG_FAULTAdded [#def os_log_fault](https://developer.apple.com/documentation/os/os_log_fault)Added #def OS_LOG_FORMAT_ERRORSAdded [#def os_log_info](https://developer.apple.com/documentation/os/os_log_info)Added [#def os_log_info_enabled](https://developer.apple.com/documentation/os/os_log_info_enabled)Added [os_log_is_debug_enabled()](https://developer.apple.com/documentation/os/1643748-os_log_is_debug_enabled)Added [os_log_is_enabled()](https://developer.apple.com/documentation/os/1643750-os_log_is_enabled)Added #def OS_LOG_RELEASEAdded #def os_log_sensitiveAdded #def os_log_sensitive_debugAdded [os_log_t](https://developer.apple.com/documentation/kernel/os_log_t)Added [OS_LOG_TYPE_DEBUG](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_debug)Added [OS_LOG_TYPE_DEFAULT](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_default)Added [os_log_type_enabled()](https://developer.apple.com/documentation/os/oslog/1643749-isenabled)Added [OS_LOG_TYPE_ERROR](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_error)Added [OS_LOG_TYPE_FAULT](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_fault)Added [OS_LOG_TYPE_INFO](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_info)Added [os_log_type_t](https://developer.apple.com/documentation/os/os_log_type_t)Added [#def os_log_with_type](https://developer.apple.com/documentation/os/os_log_with_type)

#### /usr/include/os/object.h

Added #def OS_OBJC_INDEPENDENT_CLASSAdded #def OS_OBJECT_CLASS_IMPLEMENTS_PROTOCOLAdded #def OS_OBJECT_CLASS_IMPLEMENTS_PROTOCOL_IMPLAdded #def OS_OBJECT_DECL_BASEAdded #def OS_OBJECT_DECL_CLASSAdded #def OS_OBJECT_DECL_IMPL_CLASSAdded #def OS_OBJECT_DECL_PROTOCOLAdded #def OS_OBJECT_OBJC_RUNTIME_VISIBLEAdded #def OS_OBJECT_SWIFT3

#### /usr/include/os/overflow.h (Added)

Added #def os_add3_overflowAdded #def os_add_and_mul_overflowAdded #def os_add_overflowAdded #def os_mul_and_add_overflowAdded #def os_mul_overflowAdded #def os_sub_overflow

#### /usr/include/os/trace.h

Added #def OS_TRACE_CALLAdded #def os_trace_infoAdded [os_trace_info_enabled()](https://developer.apple.com/documentation/os/1645631-os_trace_info_enabled)Added [os_trace_type_enabled()](https://developer.apple.com/documentation/os/1645627-os_trace_type_enabled)Added [#def OS_TRACE_TYPE_INFO](https://developer.apple.com/documentation/os/os_trace_type_info)

#### /usr/include/simd/geometry.h

Added [simd_incircle()](https://developer.apple.com/documentation/simd/1646495-simd_incircle)Added [simd_insphere()](https://developer.apple.com/documentation/simd/1646496-simd_insphere)Added [simd_orient()](https://developer.apple.com/documentation/simd/1646494-simd_orient)

#### /usr/include/simd/internal.h

Added [#def SIMD_LIBRARY_VERSION](https://developer.apple.com/documentation/simd/simd_library_version)

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
