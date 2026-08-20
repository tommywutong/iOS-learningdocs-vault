---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/headers/System.html
archived_at: '2026-07-15T07:34:47.968880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# System Headers Changes

## System Headers

/usr/include/MacTypes.hRemoved StrLength()Added #def StrLengthModified [#def nil](https://developer.apple.com/documentation/objectivec/nil-2gl)

|  | Removal | Architectures |
| --- | --- | --- |
| From | OS X 10.7 | i386,x86_64 |
| To | OS X 10.10 | i386 |

/usr/include/NSSystemDirectories.hModified NSGetNextSearchPathEnumeration()

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.0 |

Modified NSStartSearchPathEnumeration()

|  | Introduction |
| --- | --- |
| From | OS X 10.6 |
| To | OS X 10.0 |

/usr/include/dispatch/base.hAdded #def DISPATCH_ENUM_AVAILABLE_STARTINGAdded #def DISPATCH_RETURNS_RETAINED_BLOCKAdded #def DISPATCH_UNAVAILABLE/usr/include/dispatch/block.h (Added)Added [DISPATCH_BLOCK_ASSIGN_CURRENT](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_assign_current)Added [DISPATCH_BLOCK_BARRIER](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_barrier)Added [DISPATCH_BLOCK_DETACHED](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_detached)Added [DISPATCH_BLOCK_ENFORCE_QOS_CLASS](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_enforce_qos_class)Added [DISPATCH_BLOCK_INHERIT_QOS_CLASS](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_inherit_qos_class)Added [DISPATCH_BLOCK_NO_QOS_CLASS](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t/dispatch_block_no_qos_class)Added [dispatch_block_cancel()](https://developer.apple.com/documentation/dispatch/1431058-dispatch_block_cancel)Added [dispatch_block_create()](https://developer.apple.com/documentation/dispatch/1431050-dispatch_block_create)Added [dispatch_block_create_with_qos_class()](https://developer.apple.com/documentation/dispatch/1431068-dispatch_block_create_with_qos_c)Added [dispatch_block_flags_t](https://developer.apple.com/documentation/dispatch/dispatch_block_flags_t)Added [dispatch_block_notify()](https://developer.apple.com/documentation/dispatch/1431042-dispatch_block_notify)Added [dispatch_block_perform()](https://developer.apple.com/documentation/dispatch/1431048-dispatch_block_perform)Added [dispatch_block_testcancel()](https://developer.apple.com/documentation/dispatch/1431046-dispatch_block_testcancel)Added [dispatch_block_wait()](https://developer.apple.com/documentation/dispatch/1431064-dispatch_block_wait)/usr/include/dispatch/introspection.hAdded [dispatch_introspection_hook_queue_item_complete()](https://developer.apple.com/documentation/dispatch/1452972-dispatch_introspection_hook_queu)/usr/include/dispatch/object.hAdded #def dispatch_cancelAdded #def dispatch_notifyAdded #def dispatch_testcancelAdded #def dispatch_waitModified [dispatch_block_t](https://developer.apple.com/documentation/dispatch/dispatch_block_t)

|  | Header |
| --- | --- |
| From | dispatch/queue.h |
| To | dispatch/object.h |

/usr/include/dispatch/queue.hRemoved #def dispatch_get_main_queueAdded [dispatch_get_main_queue()](https://developer.apple.com/documentation/dispatch/1452921-dispatch_get_main_queue)Added [dispatch_qos_class_t](https://developer.apple.com/documentation/dispatch/dispatch_qos_class_t)Added [dispatch_queue_attr_make_with_qos_class()](https://developer.apple.com/documentation/dispatch/1453028-dispatch_queue_attr_make_with_qo)Added [dispatch_queue_get_qos_class()](https://developer.apple.com/documentation/dispatch/1452829-dispatch_queue_get_qos_class)Modified [dispatch_get_global_queue()](https://developer.apple.com/documentation/dispatch/1452927-dispatch_get_global_queue)

|  | Declaration |
| --- | --- |
| From | ``` dispatch_queue_t dispatch_get_global_queue (	dispatch_queue_priority_t priority,	unsigned long flags); ``` |
| To | ``` dispatch_queue_t dispatch_get_global_queue (	long identifier,	unsigned long flags); ``` |

/usr/include/dispatch/source.hModified [dispatch_source_set_cancel_handler()](https://developer.apple.com/documentation/dispatch/1385648-dispatch_source_set_cancel_handl)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_cancel_handler (	dispatch_source_t source,	dispatch_block_t cancel_handler); ``` |
| To | ``` void dispatch_source_set_cancel_handler (	dispatch_source_t source,	dispatch_block_t handler); ``` |

Modified [dispatch_source_set_cancel_handler_f()](https://developer.apple.com/documentation/dispatch/1385592-dispatch_source_set_cancel_handl)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_cancel_handler_f (	dispatch_source_t source,	dispatch_function_t cancel_handler); ``` |
| To | ``` void dispatch_source_set_cancel_handler_f (	dispatch_source_t source,	dispatch_function_t handler); ``` |

Modified [dispatch_source_set_registration_handler()](https://developer.apple.com/documentation/dispatch/1385674-dispatch_source_set_registration)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_registration_handler (	dispatch_source_t source,	dispatch_block_t registration_handler); ``` |
| To | ``` void dispatch_source_set_registration_handler (	dispatch_source_t source,	dispatch_block_t handler); ``` |

Modified [dispatch_source_set_registration_handler_f()](https://developer.apple.com/documentation/dispatch/1385662-dispatch_source_set_registration)

|  | Declaration |
| --- | --- |
| From | ``` void dispatch_source_set_registration_handler_f (	dispatch_source_t source,	dispatch_function_t registration_handler); ``` |
| To | ``` void dispatch_source_set_registration_handler_f (	dispatch_source_t source,	dispatch_function_t handler); ``` |

/usr/include/launch.hRemoved #def LAUNCH_JOBKEY_CFBUNDLEIDENTIFIERRemoved #def LAUNCH_JOBKEY_DEFAULTSAdded #def LAUNCH_JOBKEY_DRAINMESSAGESONFAILEDINITAdded #def LAUNCH_JOBKEY_ENABLEPRESSUREDEXITAdded #def LAUNCH_JOBKEY_LEGACYTIMERSAdded #def LAUNCH_JOBKEY_LOWPRIORITYBACKGROUNDIOAdded #def LAUNCH_JOBSOCKETKEY_PATHGROUPAdded #def LAUNCH_JOBSOCKETKEY_PATHOWNERAdded [launch_activate_socket()](https://developer.apple.com/documentation/xpc/1505523-launch_activate_socket)Added [launch_data_dict_iterator_t](https://developer.apple.com/documentation/xpc/launch_data_dict_iterator_t)Modified [launch_data_alloc()](https://developer.apple.com/documentation/xpc/1505398-launch_data_alloc)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_alloc (	launch_data_type_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_alloc (	launch_data_type_t type); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_array_get_count()](https://developer.apple.com/documentation/xpc/1505515-launch_data_array_get_count)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` size_t launch_data_array_get_count (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` size_t launch_data_array_get_count (	const launch_data_t larray); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_array_get_index()](https://developer.apple.com/documentation/xpc/1505935-launch_data_array_get_index)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_array_get_index (	const launch_data_t,	size_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_array_get_index (	const launch_data_t larray,	size_t idx); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_array_set_index()](https://developer.apple.com/documentation/xpc/1505624-launch_data_array_set_index)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_array_set_index (	launch_data_t,	const launch_data_t,	size_t); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_array_set_index (	launch_data_t larray,	const launch_data_t lval,	size_t idx); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_copy()](https://developer.apple.com/documentation/xpc/1505864-launch_data_copy)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_copy (	launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_copy (	launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_dict_get_count()](https://developer.apple.com/documentation/xpc/1505450-launch_data_dict_get_count)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` size_t launch_data_dict_get_count (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` size_t launch_data_dict_get_count (	const launch_data_t ldict); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_dict_insert()](https://developer.apple.com/documentation/xpc/1505566-launch_data_dict_insert)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_dict_insert (	launch_data_t,	const launch_data_t,	const char *); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_dict_insert (	launch_data_t ldict,	const launch_data_t lval,	const char *key); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_dict_iterate()](https://developer.apple.com/documentation/xpc/1505787-launch_data_dict_iterate)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` void launch_data_dict_iterate (	const launch_data_t,	void (*)(const launch_data_t, const char *, void *),	void *); ``` | OS X 10.6 | -- |
| To | ``` void launch_data_dict_iterate (	const launch_data_t ldict,	launch_data_dict_iterator_t iterator,	void *ctx); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_dict_lookup()](https://developer.apple.com/documentation/xpc/1505396-launch_data_dict_lookup)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_dict_lookup (	const launch_data_t,	const char *); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_dict_lookup (	const launch_data_t ldict,	const char *key); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_dict_remove()](https://developer.apple.com/documentation/xpc/1505490-launch_data_dict_remove)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_dict_remove (	launch_data_t,	const char *); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_dict_remove (	launch_data_t ldict,	const char *key); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_free()](https://developer.apple.com/documentation/xpc/1505609-launch_data_free)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` void launch_data_free (	launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` void launch_data_free (	launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_bool()](https://developer.apple.com/documentation/xpc/1505971-launch_data_get_bool)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_get_bool (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_get_bool (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_errno()](https://developer.apple.com/documentation/xpc/1505553-launch_data_get_errno)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` int launch_data_get_errno (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` int launch_data_get_errno (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_fd()](https://developer.apple.com/documentation/xpc/1505810-launch_data_get_fd)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` int launch_data_get_fd (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` int launch_data_get_fd (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_integer()](https://developer.apple.com/documentation/xpc/1505651-launch_data_get_integer)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` long long launch_data_get_integer (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` long long launch_data_get_integer (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_machport()](https://developer.apple.com/documentation/xpc/1505500-launch_data_get_machport)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` mach_port_t launch_data_get_machport (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` mach_port_t launch_data_get_machport (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_opaque()](https://developer.apple.com/documentation/xpc/1505503-launch_data_get_opaque)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` void * launch_data_get_opaque (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` void * launch_data_get_opaque (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_opaque_size()](https://developer.apple.com/documentation/xpc/1505665-launch_data_get_opaque_size)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` size_t launch_data_get_opaque_size (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` size_t launch_data_get_opaque_size (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_real()](https://developer.apple.com/documentation/xpc/1505841-launch_data_get_real)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` double launch_data_get_real (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` double launch_data_get_real (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_string()](https://developer.apple.com/documentation/xpc/1505866-launch_data_get_string)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` const char * launch_data_get_string (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` const char * launch_data_get_string (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_get_type()](https://developer.apple.com/documentation/xpc/1505680-launch_data_get_type)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_type_t launch_data_get_type (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_type_t launch_data_get_type (	const launch_data_t ld); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_bool()](https://developer.apple.com/documentation/xpc/1505947-launch_data_new_bool)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_bool (	bool); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_bool (	bool val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_fd()](https://developer.apple.com/documentation/xpc/1505647-launch_data_new_fd)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_fd (	int); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_fd (	int fd); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_integer()](https://developer.apple.com/documentation/xpc/1505444-launch_data_new_integer)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_integer (	long long); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_integer (	long long val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_machport()](https://developer.apple.com/documentation/xpc/1505641-launch_data_new_machport)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_machport (	mach_port_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_machport (	mach_port_t val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_opaque()](https://developer.apple.com/documentation/xpc/1505806-launch_data_new_opaque)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_opaque (	const void *,	size_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_opaque (	const void *bytes,	size_t sz); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_real()](https://developer.apple.com/documentation/xpc/1505926-launch_data_new_real)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_real (	double); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_real (	double val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_new_string()](https://developer.apple.com/documentation/xpc/1505574-launch_data_new_string)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_data_new_string (	const char *); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_data_new_string (	const char *val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_bool()](https://developer.apple.com/documentation/xpc/1505509-launch_data_set_bool)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_bool (	launch_data_t,	bool); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_bool (	launch_data_t ld,	bool val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_fd()](https://developer.apple.com/documentation/xpc/1505629-launch_data_set_fd)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_fd (	launch_data_t,	int); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_fd (	launch_data_t ld,	int fd); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_integer()](https://developer.apple.com/documentation/xpc/1505961-launch_data_set_integer)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_integer (	launch_data_t,	long long); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_integer (	launch_data_t ld,	long long val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_machport()](https://developer.apple.com/documentation/xpc/1505455-launch_data_set_machport)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_machport (	launch_data_t,	mach_port_t); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_machport (	launch_data_t ld,	mach_port_t mp); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_opaque()](https://developer.apple.com/documentation/xpc/1505941-launch_data_set_opaque)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_opaque (	launch_data_t,	const void *,	size_t); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_opaque (	launch_data_t ld,	const void *bytes,	size_t sz); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_real()](https://developer.apple.com/documentation/xpc/1505361-launch_data_set_real)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_real (	launch_data_t,	double); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_real (	launch_data_t ld,	double val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_data_set_string()](https://developer.apple.com/documentation/xpc/1505613-launch_data_set_string)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` bool launch_data_set_string (	launch_data_t,	const char *); ``` | OS X 10.6 | -- |
| To | ``` bool launch_data_set_string (	launch_data_t ld,	const char *val); ``` | OS X 10.4 | OS X 10.10 |

Modified [launch_get_fd()](https://developer.apple.com/documentation/xpc/1505462-launch_get_fd)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.6 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified [launch_msg()](https://developer.apple.com/documentation/xpc/1505402-launch_msg)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` launch_data_t launch_msg (	const launch_data_t); ``` | OS X 10.6 | -- |
| To | ``` launch_data_t launch_msg (	const launch_data_t request); ``` | OS X 10.4 | OS X 10.10 |

/usr/include/notify.hAdded #def NOTIFY_TOKEN_INVALIDAdded [notify_is_valid_token()](https://developer.apple.com/documentation/darwinnotify/1433468-notify_is_valid_token)/usr/include/objc/NSObject.hRemoved [-[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)Removed [-[NSObject description]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/description)Removed [-[NSObject hash]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/hash)Removed [-[NSObject superclass]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/superclass)Added [+[NSObject debugDescription]](https://developer.apple.com/documentation/objectivec/nsobject/1418711-debugdescription)Added [NSObject.debugDescription](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418703-debugdescription)Added [NSObject.description](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418746-description)Added [+[NSObject hash]](https://developer.apple.com/documentation/objectivec/nsobject/1418561-hash)Added [NSObject.hash](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418859-hash)Added [NSObject.superclass](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1418793-superclass)Modified [+[NSObject alloc]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/alloc)

|  | Declaration |
| --- | --- |
| From | ``` + (id)alloc ``` |
| To | ``` + (instancetype)alloc ``` |

Modified [+[NSObject allocWithZone:]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/allocWithZone:)

|  | Declaration |
| --- | --- |
| From | ``` + (id)allocWithZone:(struct _NSZone *)zone ``` |
| To | ``` + (instancetype)allocWithZone:(struct _NSZone *)zone ``` |

Modified [-[NSObject autorelease]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease)

|  | Declaration |
| --- | --- |
| From | ``` - (id)autorelease ``` |
| To | ``` - (instancetype)autorelease ``` |

Modified [-[NSObject init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [+[NSObject new]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/new)

|  | Declaration |
| --- | --- |
| From | ``` + (id)new ``` |
| To | ``` + (instancetype)new ``` |

Modified [-[NSObject retain]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain)

|  | Declaration |
| --- | --- |
| From | ``` - (id)retain ``` |
| To | ``` - (instancetype)retain ``` |

Modified [-[NSObject self]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/self)

|  | Declaration |
| --- | --- |
| From | ``` - (id)self ``` |
| To | ``` - (instancetype)self ``` |

/usr/include/objc/message.hModified [objc_msgSend_fp2ret()](https://developer.apple.com/documentation/objectivec/1456706-objc_msgsend_fp2ret)

|  | Declaration |
| --- | --- |
| From | ``` void objc_msgSend_fp2ret (	id self,	SEL op,	...); ``` |
| To | ``` _Complex long double objc_msgSend_fp2ret (	id self,	SEL op,	...); ``` |

/usr/include/objc/objc-api.hAdded #def OBJC_ARM64_UNAVAILABLE/usr/include/objc/objc.hAdded [#def nil](https://developer.apple.com/documentation/objectivec/nil-2gl)/usr/include/objc/runtime.hAdded [object_isClass()](https://developer.apple.com/documentation/objectivec/1418659-object_isclass)/usr/include/xpc/availability.h (Added)Added [#def IPHONE_SIMULATOR_HOST_MIN_VERSION_REQUIRED](https://developer.apple.com/documentation/xpc/iphone_simulator_host_min_version_required)Added #def XPC_SIMULATOR_AVAILABILITY_STRING/usr/include/xpc/base.hRemoved #def XPC_PROJECT_EXPORTAdded [#def XPC_HOSTING_OLD_MAIN](https://developer.apple.com/documentation/xpc/xpc_hosting_old_main)

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
