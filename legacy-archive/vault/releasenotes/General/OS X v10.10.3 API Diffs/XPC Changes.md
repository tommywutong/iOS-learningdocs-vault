---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/XPC.html
archived_at: '2026-07-18T02:52:45.956996Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# XPC Changes

## XPC

Modified XPC_ACTIVITY_ALLOW_BATTERY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_ALLOW_BATTERY: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_ALLOW_BATTERY: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_CHECK_IN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_DELAY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_DELAY: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_DELAY: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_GRACE_PERIOD

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_GRACE_PERIOD: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_GRACE_PERIOD: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_INTERVAL: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_INTERVAL: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_15_MIN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_1_DAY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_1_HOUR

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_1_MIN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_30_MIN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_4_HOURS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_5_MIN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_7_DAYS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_INTERVAL_8_HOURS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified XPC_ACTIVITY_PRIORITY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_PRIORITY: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_PRIORITY: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_PRIORITY_MAINTENANCE

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_PRIORITY_MAINTENANCE: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_PRIORITY_MAINTENANCE: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_PRIORITY_UTILITY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_PRIORITY_UTILITY: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_PRIORITY_UTILITY: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_REPEATING

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_REPEATING: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_REPEATING: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_REQUIRE_HDD_SPINNING

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_REQUIRE_HDD_SPINNING: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_REQUIRE_HDD_SPINNING: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP: ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` var XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP: UnsafePointer<Int8> ``` | OS X 10.9 |

Modified launch_activate_socket(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int32>>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func launch_activate_socket(_ name: ConstUnsafePointer<Int8>, _ fds: UnsafePointer<UnsafePointer<Int32>>, _ cnt: UnsafePointer<UInt>) -> Int32 ``` |
| To | ``` func launch_activate_socket(_ name: UnsafePointer<Int8>, _ fds: UnsafeMutablePointer<UnsafeMutablePointer<Int32>>, _ cnt: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified launch_data_alloc(launch_data_type_t) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_array_get_count(launch_data_t) -> Int

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_array_get_count(_ larray: launch_data_t) -> UInt ``` | OS X 10.10 | -- |
| To | ``` func launch_data_array_get_count(_ larray: launch_data_t) -> Int ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_array_get_index(launch_data_t, Int) -> launch_data_t

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_array_get_index(_ larray: launch_data_t, _ idx: UInt) -> launch_data_t ``` | OS X 10.10 | -- |
| To | ``` func launch_data_array_get_index(_ larray: launch_data_t, _ idx: Int) -> launch_data_t ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_array_set_index(launch_data_t, launch_data_t, Int) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_array_set_index(_ larray: launch_data_t, _ lval: launch_data_t, _ idx: UInt) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func launch_data_array_set_index(_ larray: launch_data_t, _ lval: launch_data_t, _ idx: Int) -> Bool ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_copy(launch_data_t) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_dict_get_count(launch_data_t) -> Int

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_dict_get_count(_ ldict: launch_data_t) -> UInt ``` | OS X 10.10 | -- |
| To | ``` func launch_data_dict_get_count(_ ldict: launch_data_t) -> Int ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_dict_insert(launch_data_t, launch_data_t, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_dict_insert(_ ldict: launch_data_t, _ lval: launch_data_t, _ key: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func launch_data_dict_insert(_ ldict: launch_data_t, _ lval: launch_data_t, _ key: UnsafePointer<Int8>) -> Bool ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_dict_iterate(launch_data_t, launch_data_dict_iterator_t, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_dict_iterate(_ ldict: launch_data_t, _ iterator: launch_data_dict_iterator_t, _ ctx: UnsafePointer<()>) ``` | OS X 10.10 | -- |
| To | ``` func launch_data_dict_iterate(_ ldict: launch_data_t, _ iterator: launch_data_dict_iterator_t, _ ctx: UnsafeMutablePointer<Void>) ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_dict_iterator_t

|  | Declaration |
| --- | --- |
| From | ``` typealias launch_data_dict_iterator_t = CFunctionPointer<((launch_data_t, ConstUnsafePointer<Int8>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias launch_data_dict_iterator_t = CFunctionPointer<((launch_data_t, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified launch_data_dict_lookup(launch_data_t, UnsafePointer<Int8>) -> launch_data_t

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_dict_lookup(_ ldict: launch_data_t, _ key: ConstUnsafePointer<Int8>) -> launch_data_t ``` | OS X 10.10 | -- |
| To | ``` func launch_data_dict_lookup(_ ldict: launch_data_t, _ key: UnsafePointer<Int8>) -> launch_data_t ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_dict_remove(launch_data_t, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_dict_remove(_ ldict: launch_data_t, _ key: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func launch_data_dict_remove(_ ldict: launch_data_t, _ key: UnsafePointer<Int8>) -> Bool ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_free(launch_data_t)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_bool(launch_data_t) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_errno(launch_data_t) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_fd(launch_data_t) -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_integer(launch_data_t) -> Int64

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_machport(launch_data_t) -> mach_port_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_opaque(launch_data_t) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_get_opaque(_ ld: launch_data_t) -> UnsafePointer<()> ``` | OS X 10.10 | -- |
| To | ``` func launch_data_get_opaque(_ ld: launch_data_t) -> UnsafeMutablePointer<Void> ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_opaque_size(launch_data_t) -> Int

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_get_opaque_size(_ ld: launch_data_t) -> UInt ``` | OS X 10.10 | -- |
| To | ``` func launch_data_get_opaque_size(_ ld: launch_data_t) -> Int ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_real(launch_data_t) -> Double

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_string(launch_data_t) -> UnsafePointer<Int8>

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_get_string(_ ld: launch_data_t) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 | -- |
| To | ``` func launch_data_get_string(_ ld: launch_data_t) -> UnsafePointer<Int8> ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_get_type(launch_data_t) -> launch_data_type_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_bool(Bool) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_fd(Int32) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_integer(Int64) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_machport(mach_port_t) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_opaque(UnsafePointer<Void>, Int) -> launch_data_t

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_new_opaque(_ bytes: ConstUnsafePointer<()>, _ sz: UInt) -> launch_data_t ``` | OS X 10.10 | -- |
| To | ``` func launch_data_new_opaque(_ bytes: UnsafePointer<Void>, _ sz: Int) -> launch_data_t ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_real(Double) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_new_string(UnsafePointer<Int8>) -> launch_data_t

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_new_string(_ val: ConstUnsafePointer<Int8>) -> launch_data_t ``` | OS X 10.10 | -- |
| To | ``` func launch_data_new_string(_ val: UnsafePointer<Int8>) -> launch_data_t ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_bool(launch_data_t, Bool) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_fd(launch_data_t, Int32) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_integer(launch_data_t, Int64) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_machport(launch_data_t, mach_port_t) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_opaque(launch_data_t, UnsafePointer<Void>, Int) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_set_opaque(_ ld: launch_data_t, _ bytes: ConstUnsafePointer<()>, _ sz: UInt) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func launch_data_set_opaque(_ ld: launch_data_t, _ bytes: UnsafePointer<Void>, _ sz: Int) -> Bool ``` | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_real(launch_data_t, Double) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_data_set_string(launch_data_t, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func launch_data_set_string(_ ld: launch_data_t, _ val: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 | -- |
| To | ``` func launch_data_set_string(_ ld: launch_data_t, _ val: UnsafePointer<Int8>) -> Bool ``` | OS X 10.4 | OS X 10.10 |

Modified launch_get_fd() -> Int32

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified launch_msg(launch_data_t) -> launch_data_t

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.4 | OS X 10.10 |

Modified xpc_activity_copy_criteria(xpc_activity_t!) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified xpc_activity_get_state(xpc_activity_t) -> xpc_activity_state_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_activity_get_state(_ activity: xpc_activity_t!) -> xpc_activity_state_t ``` | OS X 10.10 |
| To | ``` func xpc_activity_get_state(_ activity: xpc_activity_t) -> xpc_activity_state_t ``` | OS X 10.9 |

Modified xpc_activity_register(UnsafePointer<Int8>, xpc_object_t, xpc_activity_handler_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_activity_register(_ identifier: ConstUnsafePointer<Int8>, _ criteria: xpc_object_t!, _ handler: xpc_activity_handler_t!) ``` | OS X 10.10 |
| To | ``` func xpc_activity_register(_ identifier: UnsafePointer<Int8>, _ criteria: xpc_object_t, _ handler: xpc_activity_handler_t) ``` | OS X 10.9 |

Modified xpc_activity_set_criteria(xpc_activity_t, xpc_object_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_activity_set_criteria(_ activity: xpc_activity_t!, _ criteria: xpc_object_t!) ``` | OS X 10.10 |
| To | ``` func xpc_activity_set_criteria(_ activity: xpc_activity_t, _ criteria: xpc_object_t) ``` | OS X 10.9 |

Modified xpc_activity_set_state(xpc_activity_t, xpc_activity_state_t) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_activity_set_state(_ activity: xpc_activity_t!, _ state: xpc_activity_state_t) -> Bool ``` | OS X 10.10 |
| To | ``` func xpc_activity_set_state(_ activity: xpc_activity_t, _ state: xpc_activity_state_t) -> Bool ``` | OS X 10.9 |

Modified xpc_activity_should_defer(xpc_activity_t!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified xpc_activity_unregister(UnsafePointer<Int8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_activity_unregister(_ identifier: ConstUnsafePointer<Int8>) ``` | OS X 10.10 |
| To | ``` func xpc_activity_unregister(_ identifier: UnsafePointer<Int8>) ``` | OS X 10.9 |

Modified xpc_array_append_value(xpc_object_t, xpc_object_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_append_value(_ xarray: xpc_object_t!, _ value: xpc_object_t!) ``` | OS X 10.10 |
| To | ``` func xpc_array_append_value(_ xarray: xpc_object_t, _ value: xpc_object_t) ``` | OS X 10.7 |

Modified xpc_array_applier_t

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_array_applier_t = (UInt, xpc_object_t!) -> Bool ``` |
| To | ``` typealias xpc_array_applier_t = (Int, xpc_object_t!) -> Bool ``` |

Modified xpc_array_apply(xpc_object_t, xpc_array_applier_t) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_apply(_ xarray: xpc_object_t!, _ applier: xpc_array_applier_t!) -> Bool ``` | OS X 10.10 |
| To | ``` func xpc_array_apply(_ xarray: xpc_object_t, _ applier: xpc_array_applier_t) -> Bool ``` | OS X 10.7 |

Modified xpc_array_create(UnsafePointer<xpc_object_t?>, Int) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_create(_ objects: ConstUnsafePointer<xpc_object_t?>, _ count: UInt) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_array_create(_ objects: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_array_create_connection(xpc_object_t, Int) -> xpc_connection_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_create_connection(_ xarray: xpc_object_t!, _ index: UInt) -> xpc_connection_t! ``` | OS X 10.10 |
| To | ``` func xpc_array_create_connection(_ xarray: xpc_object_t, _ index: Int) -> xpc_connection_t! ``` | OS X 10.7 |

Modified xpc_array_dup_fd(xpc_object_t, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_dup_fd(_ xarray: xpc_object_t!, _ index: UInt) -> Int32 ``` | OS X 10.10 |
| To | ``` func xpc_array_dup_fd(_ xarray: xpc_object_t, _ index: Int) -> Int32 ``` | OS X 10.7 |

Modified xpc_array_get_bool(xpc_object_t, Int) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_bool(_ xarray: xpc_object_t!, _ index: UInt) -> Bool ``` | OS X 10.10 |
| To | ``` func xpc_array_get_bool(_ xarray: xpc_object_t, _ index: Int) -> Bool ``` | OS X 10.7 |

Modified xpc_array_get_count(xpc_object_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_count(_ xarray: xpc_object_t!) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_array_get_count(_ xarray: xpc_object_t) -> Int ``` | OS X 10.7 |

Modified xpc_array_get_data(xpc_object_t, Int, UnsafeMutablePointer<Int>) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_data(_ xarray: xpc_object_t!, _ index: UInt, _ length: UnsafePointer<UInt>) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func xpc_array_get_data(_ xarray: xpc_object_t, _ index: Int, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` | OS X 10.7 |

Modified xpc_array_get_date(xpc_object_t, Int) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_date(_ xarray: xpc_object_t!, _ index: UInt) -> Int64 ``` | OS X 10.10 |
| To | ``` func xpc_array_get_date(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` | OS X 10.7 |

Modified xpc_array_get_double(xpc_object_t, Int) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_double(_ xarray: xpc_object_t!, _ index: UInt) -> Double ``` | OS X 10.10 |
| To | ``` func xpc_array_get_double(_ xarray: xpc_object_t, _ index: Int) -> Double ``` | OS X 10.7 |

Modified xpc_array_get_int64(xpc_object_t, Int) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_int64(_ xarray: xpc_object_t!, _ index: UInt) -> Int64 ``` | OS X 10.10 |
| To | ``` func xpc_array_get_int64(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` | OS X 10.7 |

Modified xpc_array_get_string(xpc_object_t, Int) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_string(_ xarray: xpc_object_t!, _ index: UInt) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func xpc_array_get_string(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<Int8> ``` | OS X 10.7 |

Modified xpc_array_get_uint64(xpc_object_t, Int) -> UInt64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_uint64(_ xarray: xpc_object_t!, _ index: UInt) -> UInt64 ``` | OS X 10.10 |
| To | ``` func xpc_array_get_uint64(_ xarray: xpc_object_t, _ index: Int) -> UInt64 ``` | OS X 10.7 |

Modified xpc_array_get_uuid(xpc_object_t, Int) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_uuid(_ xarray: xpc_object_t!, _ index: UInt) -> ConstUnsafePointer<UInt8> ``` | OS X 10.10 |
| To | ``` func xpc_array_get_uuid(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<UInt8> ``` | OS X 10.7 |

Modified xpc_array_get_value(xpc_object_t, Int) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_get_value(_ xarray: xpc_object_t!, _ index: UInt) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_array_get_value(_ xarray: xpc_object_t, _ index: Int) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_array_set_bool(xpc_object_t, Int, Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_bool(_ xarray: xpc_object_t!, _ index: UInt, _ value: Bool) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_bool(_ xarray: xpc_object_t, _ index: Int, _ value: Bool) ``` | OS X 10.7 |

Modified xpc_array_set_connection(xpc_object_t, Int, xpc_connection_t!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_connection(_ xarray: xpc_object_t!, _ index: UInt, _ connection: xpc_connection_t!) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_connection(_ xarray: xpc_object_t, _ index: Int, _ connection: xpc_connection_t!) ``` | OS X 10.7 |

Modified xpc_array_set_data(xpc_object_t, Int, UnsafePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_data(_ xarray: xpc_object_t!, _ index: UInt, _ bytes: ConstUnsafePointer<()>, _ length: UInt) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_data(_ xarray: xpc_object_t, _ index: Int, _ bytes: UnsafePointer<Void>, _ length: Int) ``` | OS X 10.7 |

Modified xpc_array_set_date(xpc_object_t, Int, Int64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_date(_ xarray: xpc_object_t!, _ index: UInt, _ value: Int64) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_date(_ xarray: xpc_object_t, _ index: Int, _ value: Int64) ``` | OS X 10.7 |

Modified xpc_array_set_double(xpc_object_t, Int, Double)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_double(_ xarray: xpc_object_t!, _ index: UInt, _ value: Double) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_double(_ xarray: xpc_object_t, _ index: Int, _ value: Double) ``` | OS X 10.7 |

Modified xpc_array_set_fd(xpc_object_t, Int, Int32)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_fd(_ xarray: xpc_object_t!, _ index: UInt, _ fd: Int32) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_fd(_ xarray: xpc_object_t, _ index: Int, _ fd: Int32) ``` | OS X 10.7 |

Modified xpc_array_set_int64(xpc_object_t, Int, Int64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_int64(_ xarray: xpc_object_t!, _ index: UInt, _ value: Int64) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_int64(_ xarray: xpc_object_t, _ index: Int, _ value: Int64) ``` | OS X 10.7 |

Modified xpc_array_set_string(xpc_object_t, Int, UnsafePointer<Int8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_string(_ xarray: xpc_object_t!, _ index: UInt, _ string: ConstUnsafePointer<Int8>) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_string(_ xarray: xpc_object_t, _ index: Int, _ string: UnsafePointer<Int8>) ``` | OS X 10.7 |

Modified xpc_array_set_uint64(xpc_object_t, Int, UInt64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_uint64(_ xarray: xpc_object_t!, _ index: UInt, _ value: UInt64) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_uint64(_ xarray: xpc_object_t, _ index: Int, _ value: UInt64) ``` | OS X 10.7 |

Modified xpc_array_set_uuid(xpc_object_t, Int, UnsafePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_uuid(_ xarray: xpc_object_t!, _ index: UInt, _ uuid: ConstUnsafePointer<UInt8>) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_uuid(_ xarray: xpc_object_t, _ index: Int, _ uuid: UnsafePointer<UInt8>) ``` | OS X 10.7 |

Modified xpc_array_set_value(xpc_object_t, Int, xpc_object_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_array_set_value(_ xarray: xpc_object_t!, _ index: UInt, _ value: xpc_object_t!) ``` | OS X 10.10 |
| To | ``` func xpc_array_set_value(_ xarray: xpc_object_t, _ index: Int, _ value: xpc_object_t) ``` | OS X 10.7 |

Modified xpc_bool_create(Bool) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_bool_get_value(xpc_object_t!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_connection_cancel(xpc_connection_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_cancel(_ connection: xpc_connection_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_cancel(_ connection: xpc_connection_t) ``` | OS X 10.7 |

Modified xpc_connection_create(UnsafePointer<Int8>, dispatch_queue_t!) -> xpc_connection_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_create(_ name: ConstUnsafePointer<Int8>, _ targetq: dispatch_queue_t!) -> xpc_connection_t! ``` | OS X 10.10 |
| To | ``` func xpc_connection_create(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!) -> xpc_connection_t! ``` | OS X 10.7 |

Modified xpc_connection_create_from_endpoint(xpc_endpoint_t) -> xpc_connection_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t!) -> xpc_connection_t! ``` | OS X 10.10 |
| To | ``` func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t) -> xpc_connection_t! ``` | OS X 10.7 |

Modified xpc_connection_create_mach_service(UnsafePointer<Int8>, dispatch_queue_t!, UInt64) -> xpc_connection_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_create_mach_service(_ name: ConstUnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ flags: UInt64) -> xpc_connection_t! ``` | OS X 10.10 |
| To | ``` func xpc_connection_create_mach_service(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ flags: UInt64) -> xpc_connection_t! ``` | OS X 10.7 |

Modified xpc_connection_get_asid(xpc_connection_t) -> au_asid_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_get_asid(_ connection: xpc_connection_t!) -> au_asid_t ``` | OS X 10.10 |
| To | ``` func xpc_connection_get_asid(_ connection: xpc_connection_t) -> au_asid_t ``` | OS X 10.7 |

Modified xpc_connection_get_context(xpc_connection_t) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_get_context(_ connection: xpc_connection_t!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func xpc_connection_get_context(_ connection: xpc_connection_t) -> UnsafeMutablePointer<Void> ``` | OS X 10.7 |

Modified xpc_connection_get_egid(xpc_connection_t) -> gid_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_get_egid(_ connection: xpc_connection_t!) -> gid_t ``` | OS X 10.10 |
| To | ``` func xpc_connection_get_egid(_ connection: xpc_connection_t) -> gid_t ``` | OS X 10.7 |

Modified xpc_connection_get_euid(xpc_connection_t) -> uid_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_get_euid(_ connection: xpc_connection_t!) -> uid_t ``` | OS X 10.10 |
| To | ``` func xpc_connection_get_euid(_ connection: xpc_connection_t) -> uid_t ``` | OS X 10.7 |

Modified xpc_connection_get_name(xpc_connection_t) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_get_name(_ connection: xpc_connection_t!) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func xpc_connection_get_name(_ connection: xpc_connection_t) -> UnsafePointer<Int8> ``` | OS X 10.7 |

Modified xpc_connection_get_pid(xpc_connection_t) -> pid_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_get_pid(_ connection: xpc_connection_t!) -> pid_t ``` | OS X 10.10 |
| To | ``` func xpc_connection_get_pid(_ connection: xpc_connection_t) -> pid_t ``` | OS X 10.7 |

Modified xpc_connection_resume(xpc_connection_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_resume(_ connection: xpc_connection_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_resume(_ connection: xpc_connection_t) ``` | OS X 10.7 |

Modified xpc_connection_send_barrier(xpc_connection_t, dispatch_block_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_send_barrier(_ connection: xpc_connection_t!, _ barrier: dispatch_block_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_send_barrier(_ connection: xpc_connection_t, _ barrier: dispatch_block_t) ``` | OS X 10.7 |

Modified xpc_connection_send_message(xpc_connection_t, xpc_object_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_send_message(_ connection: xpc_connection_t!, _ message: xpc_object_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_send_message(_ connection: xpc_connection_t, _ message: xpc_object_t) ``` | OS X 10.7 |

Modified xpc_connection_send_message_with_reply(xpc_connection_t, xpc_object_t, dispatch_queue_t!, xpc_handler_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_send_message_with_reply(_ connection: xpc_connection_t!, _ message: xpc_object_t!, _ replyq: dispatch_queue_t!, _ handler: xpc_handler_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_send_message_with_reply(_ connection: xpc_connection_t, _ message: xpc_object_t, _ replyq: dispatch_queue_t!, _ handler: xpc_handler_t) ``` | OS X 10.7 |

Modified xpc_connection_send_message_with_reply_sync(xpc_connection_t, xpc_object_t) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_send_message_with_reply_sync(_ connection: xpc_connection_t!, _ message: xpc_object_t!) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_connection_send_message_with_reply_sync(_ connection: xpc_connection_t, _ message: xpc_object_t) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_connection_set_context(xpc_connection_t, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_set_context(_ connection: xpc_connection_t!, _ context: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func xpc_connection_set_context(_ connection: xpc_connection_t, _ context: UnsafeMutablePointer<Void>) ``` | OS X 10.7 |

Modified xpc_connection_set_event_handler(xpc_connection_t, xpc_handler_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_set_event_handler(_ connection: xpc_connection_t!, _ handler: xpc_handler_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_set_event_handler(_ connection: xpc_connection_t, _ handler: xpc_handler_t) ``` | OS X 10.7 |

Modified xpc_connection_set_finalizer_f(xpc_connection_t, xpc_finalizer_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t!, _ finalizer: xpc_finalizer_t) ``` | OS X 10.10 |
| To | ``` func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t, _ finalizer: xpc_finalizer_t) ``` | OS X 10.7 |

Modified xpc_connection_set_target_queue(xpc_connection_t, dispatch_queue_t!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_set_target_queue(_ connection: xpc_connection_t!, _ targetq: dispatch_queue_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_set_target_queue(_ connection: xpc_connection_t, _ targetq: dispatch_queue_t!) ``` | OS X 10.7 |

Modified xpc_connection_suspend(xpc_connection_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_connection_suspend(_ connection: xpc_connection_t!) ``` | OS X 10.10 |
| To | ``` func xpc_connection_suspend(_ connection: xpc_connection_t) ``` | OS X 10.7 |

Modified xpc_copy(xpc_object_t) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_copy(_ object: xpc_object_t!) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_copy(_ object: xpc_object_t) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_copy_description(xpc_object_t) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_copy_description(_ object: xpc_object_t!) -> UnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func xpc_copy_description(_ object: xpc_object_t) -> UnsafeMutablePointer<Int8> ``` | OS X 10.7 |

Modified xpc_data_create(UnsafePointer<Void>, Int) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_data_create(_ bytes: ConstUnsafePointer<()>, _ length: UInt) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_data_create(_ bytes: UnsafePointer<Void>, _ length: Int) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_data_create_with_dispatch_data(dispatch_data_t) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t!) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_data_get_bytes(xpc_object_t, UnsafeMutablePointer<Void>, Int, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_data_get_bytes(_ xdata: xpc_object_t!, _ buffer: UnsafePointer<()>, _ off: UInt, _ length: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_data_get_bytes(_ xdata: xpc_object_t, _ buffer: UnsafeMutablePointer<Void>, _ off: Int, _ length: Int) -> Int ``` | OS X 10.7 |

Modified xpc_data_get_bytes_ptr(xpc_object_t) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t!) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t) -> UnsafePointer<Void> ``` | OS X 10.7 |

Modified xpc_data_get_length(xpc_object_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_data_get_length(_ xdata: xpc_object_t!) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_data_get_length(_ xdata: xpc_object_t) -> Int ``` | OS X 10.7 |

Modified xpc_date_create(Int64) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_date_create_from_current() -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_date_get_value(xpc_object_t) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_date_get_value(_ xdate: xpc_object_t!) -> Int64 ``` | OS X 10.10 |
| To | ``` func xpc_date_get_value(_ xdate: xpc_object_t) -> Int64 ``` | OS X 10.7 |

Modified xpc_debugger_api_misuse_info() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func xpc_debugger_api_misuse_info() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func xpc_debugger_api_misuse_info() -> UnsafePointer<Int8> ``` |

Modified xpc_dictionary_applier_t

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_dictionary_applier_t = (ConstUnsafePointer<Int8>, xpc_object_t!) -> Bool ``` |
| To | ``` typealias xpc_dictionary_applier_t = (UnsafePointer<Int8>, xpc_object_t!) -> Bool ``` |

Modified xpc_dictionary_apply(xpc_object_t, xpc_dictionary_applier_t) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_apply(_ xdict: xpc_object_t!, _ applier: xpc_dictionary_applier_t!) -> Bool ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_apply(_ xdict: xpc_object_t, _ applier: xpc_dictionary_applier_t) -> Bool ``` | OS X 10.7 |

Modified xpc_dictionary_create(UnsafePointer<UnsafePointer<Int8>>, UnsafePointer<xpc_object_t?>, Int) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_create(_ keys: ConstUnsafePointer<ConstUnsafePointer<Int8>>, _ values: ConstUnsafePointer<xpc_object_t?>, _ count: UInt) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_create(_ keys: UnsafePointer<UnsafePointer<Int8>>, _ values: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_dictionary_create_connection(xpc_object_t, UnsafePointer<Int8>) -> xpc_connection_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_create_connection(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> xpc_connection_t! ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_create_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_connection_t! ``` | OS X 10.7 |

Modified xpc_dictionary_create_reply(xpc_object_t) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_create_reply(_ original: xpc_object_t!) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_create_reply(_ original: xpc_object_t) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_dictionary_dup_fd(xpc_object_t, UnsafePointer<Int8>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_dup_fd(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> Int32 ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_dup_fd(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int32 ``` | OS X 10.7 |

Modified xpc_dictionary_get_bool(xpc_object_t, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_bool(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_bool(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Bool ``` | OS X 10.7 |

Modified xpc_dictionary_get_count(xpc_object_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_count(_ xdict: xpc_object_t!) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_count(_ xdict: xpc_object_t) -> Int ``` | OS X 10.7 |

Modified xpc_dictionary_get_data(xpc_object_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int>) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_data(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ length: UnsafePointer<UInt>) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` | OS X 10.7 |

Modified xpc_dictionary_get_date(xpc_object_t, UnsafePointer<Int8>) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_date(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> Int64 ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_date(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` | OS X 10.7 |

Modified xpc_dictionary_get_double(xpc_object_t, UnsafePointer<Int8>) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_double(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> Double ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_double(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Double ``` | OS X 10.7 |

Modified xpc_dictionary_get_int64(xpc_object_t, UnsafePointer<Int8>) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_int64(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> Int64 ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_int64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` | OS X 10.7 |

Modified xpc_dictionary_get_remote_connection(xpc_object_t) -> xpc_connection_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_remote_connection(_ xdict: xpc_object_t!) -> xpc_connection_t! ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_remote_connection(_ xdict: xpc_object_t) -> xpc_connection_t! ``` | OS X 10.7 |

Modified xpc_dictionary_get_string(xpc_object_t, UnsafePointer<Int8>) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_string(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_string(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` | OS X 10.7 |

Modified xpc_dictionary_get_uint64(xpc_object_t, UnsafePointer<Int8>) -> UInt64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_uint64(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> UInt64 ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_uint64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UInt64 ``` | OS X 10.7 |

Modified xpc_dictionary_get_uuid(xpc_object_t, UnsafePointer<Int8>) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_uuid(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> ConstUnsafePointer<UInt8> ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<UInt8> ``` | OS X 10.7 |

Modified xpc_dictionary_get_value(xpc_object_t, UnsafePointer<Int8>) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_get_value(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_get_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_dictionary_set_bool(xpc_object_t, UnsafePointer<Int8>, Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_bool(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ value: Bool) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_bool(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: Bool) ``` | OS X 10.7 |

Modified xpc_dictionary_set_connection(xpc_object_t, UnsafePointer<Int8>, xpc_connection_t!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_connection(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ connection: xpc_connection_t!) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ connection: xpc_connection_t!) ``` | OS X 10.7 |

Modified xpc_dictionary_set_data(xpc_object_t, UnsafePointer<Int8>, UnsafePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_data(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ bytes: ConstUnsafePointer<()>, _ length: UInt) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ bytes: UnsafePointer<Void>, _ length: Int) ``` | OS X 10.7 |

Modified xpc_dictionary_set_date(xpc_object_t, UnsafePointer<Int8>, Int64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_date(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ value: Int64) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_date(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: Int64) ``` | OS X 10.7 |

Modified xpc_dictionary_set_double(xpc_object_t, UnsafePointer<Int8>, Double)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_double(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ value: Double) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_double(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: Double) ``` | OS X 10.7 |

Modified xpc_dictionary_set_fd(xpc_object_t, UnsafePointer<Int8>, Int32)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_fd(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ fd: Int32) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_fd(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ fd: Int32) ``` | OS X 10.7 |

Modified xpc_dictionary_set_int64(xpc_object_t, UnsafePointer<Int8>, Int64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_int64(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ value: Int64) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_int64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: Int64) ``` | OS X 10.7 |

Modified xpc_dictionary_set_string(xpc_object_t, UnsafePointer<Int8>, UnsafePointer<Int8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_string(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ string: ConstUnsafePointer<Int8>) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_string(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ string: UnsafePointer<Int8>) ``` | OS X 10.7 |

Modified xpc_dictionary_set_uint64(xpc_object_t, UnsafePointer<Int8>, UInt64)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_uint64(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ value: UInt64) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_uint64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: UInt64) ``` | OS X 10.7 |

Modified xpc_dictionary_set_uuid(xpc_object_t, UnsafePointer<Int8>, UnsafePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_uuid(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ uuid: ConstUnsafePointer<UInt8>) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ uuid: UnsafePointer<UInt8>) ``` | OS X 10.7 |

Modified xpc_dictionary_set_value(xpc_object_t, UnsafePointer<Int8>, xpc_object_t!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_dictionary_set_value(_ xdict: xpc_object_t!, _ key: ConstUnsafePointer<Int8>, _ value: xpc_object_t!) ``` | OS X 10.10 |
| To | ``` func xpc_dictionary_set_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: xpc_object_t!) ``` | OS X 10.7 |

Modified xpc_double_create(Double) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_double_get_value(xpc_object_t) -> Double

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_double_get_value(_ xdouble: xpc_object_t!) -> Double ``` | OS X 10.10 |
| To | ``` func xpc_double_get_value(_ xdouble: xpc_object_t) -> Double ``` | OS X 10.7 |

Modified xpc_endpoint_create(xpc_connection_t) -> xpc_endpoint_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_endpoint_create(_ connection: xpc_connection_t!) -> xpc_endpoint_t! ``` | OS X 10.10 |
| To | ``` func xpc_endpoint_create(_ connection: xpc_connection_t) -> xpc_endpoint_t! ``` | OS X 10.7 |

Modified xpc_equal(xpc_object_t, xpc_object_t) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_equal(_ object1: xpc_object_t!, _ object2: xpc_object_t!) -> Bool ``` | OS X 10.10 |
| To | ``` func xpc_equal(_ object1: xpc_object_t, _ object2: xpc_object_t) -> Bool ``` | OS X 10.7 |

Modified xpc_fd_create(Int32) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_fd_dup(xpc_object_t) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_fd_dup(_ xfd: xpc_object_t!) -> Int32 ``` | OS X 10.10 |
| To | ``` func xpc_fd_dup(_ xfd: xpc_object_t) -> Int32 ``` | OS X 10.7 |

Modified xpc_finalizer_t

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_finalizer_t = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias xpc_finalizer_t = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified xpc_get_type(xpc_object_t) -> xpc_type_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_get_type(_ object: xpc_object_t!) -> xpc_type_t ``` | OS X 10.10 |
| To | ``` func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t ``` | OS X 10.7 |

Modified xpc_hash(xpc_object_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_hash(_ object: xpc_object_t!) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_hash(_ object: xpc_object_t) -> Int ``` | OS X 10.7 |

Modified xpc_int64_create(Int64) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_int64_get_value(xpc_object_t) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_int64_get_value(_ xint: xpc_object_t!) -> Int64 ``` | OS X 10.10 |
| To | ``` func xpc_int64_get_value(_ xint: xpc_object_t) -> Int64 ``` | OS X 10.7 |

Modified xpc_main(xpc_connection_handler_t)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_null_create() -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_release(xpc_object_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_release(_ object: xpc_object_t!) ``` | OS X 10.10 |
| To | ``` func xpc_release(_ object: xpc_object_t) ``` | OS X 10.7 |

Modified xpc_retain(xpc_object_t) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_retain(_ object: xpc_object_t!) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_retain(_ object: xpc_object_t) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_set_event_stream_handler(UnsafePointer<Int8>, dispatch_queue_t!, xpc_handler_t)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_set_event_stream_handler(_ stream: ConstUnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ handler: xpc_handler_t!) ``` | OS X 10.10 |
| To | ``` func xpc_set_event_stream_handler(_ stream: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ handler: xpc_handler_t) ``` | OS X 10.7 |

Modified xpc_shmem_create(UnsafeMutablePointer<Void>, Int) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_shmem_create(_ region: UnsafePointer<()>, _ length: UInt) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_shmem_create(_ region: UnsafeMutablePointer<Void>, _ length: Int) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_shmem_map(xpc_object_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_shmem_map(_ xshmem: xpc_object_t!, _ region: UnsafePointer<UnsafePointer<()>>) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_shmem_map(_ xshmem: xpc_object_t, _ region: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int ``` | OS X 10.7 |

Modified xpc_string_create(UnsafePointer<Int8>) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_string_create(_ string: ConstUnsafePointer<Int8>) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_string_create(_ string: UnsafePointer<Int8>) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_string_create_with_format_and_arguments(UnsafePointer<Int8>, CVaListPointer) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_string_create_with_format_and_arguments(_ fmt: ConstUnsafePointer<Int8>, _ ap: CVaListPointer) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_string_create_with_format_and_arguments(_ fmt: UnsafePointer<Int8>, _ ap: CVaListPointer) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_string_get_length(xpc_object_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_string_get_length(_ xstring: xpc_object_t!) -> UInt ``` | OS X 10.10 |
| To | ``` func xpc_string_get_length(_ xstring: xpc_object_t) -> Int ``` | OS X 10.7 |

Modified xpc_string_get_string_ptr(xpc_object_t) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_string_get_string_ptr(_ xstring: xpc_object_t!) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func xpc_string_get_string_ptr(_ xstring: xpc_object_t) -> UnsafePointer<Int8> ``` | OS X 10.7 |

Modified xpc_transaction_begin()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_transaction_end()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_uint64_create(UInt64) -> xpc_object_t!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified xpc_uint64_get_value(xpc_object_t) -> UInt64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_uint64_get_value(_ xuint: xpc_object_t!) -> UInt64 ``` | OS X 10.10 |
| To | ``` func xpc_uint64_get_value(_ xuint: xpc_object_t) -> UInt64 ``` | OS X 10.7 |

Modified xpc_uuid_create(UnsafePointer<UInt8>) -> xpc_object_t!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_uuid_create(_ uuid: ConstUnsafePointer<UInt8>) -> xpc_object_t! ``` | OS X 10.10 |
| To | ``` func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>) -> xpc_object_t! ``` | OS X 10.7 |

Modified xpc_uuid_get_bytes(xpc_object_t) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func xpc_uuid_get_bytes(_ xuuid: xpc_object_t!) -> ConstUnsafePointer<UInt8> ``` | OS X 10.10 |
| To | ``` func xpc_uuid_get_bytes(_ xuuid: xpc_object_t) -> UnsafePointer<UInt8> ``` | OS X 10.7 |

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
