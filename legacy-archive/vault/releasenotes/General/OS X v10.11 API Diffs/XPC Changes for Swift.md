---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/XPC.html
archived_at: '2026-07-18T02:53:47.928488Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# XPC Changes for Swift

### XPC

Removed launch_data_type_t.valueRemoved XPC_ACTIVITY_REQUIRE_BATTERY_LEVELRemoved XPC_ACTIVITY_REQUIRE_HDD_SPINNINGAdded launch_data_type_t.init(rawValue: UInt32)Added launch_data_type_t.rawValueAdded LAUNCH_JOBINETDCOMPATIBILITY_INSTANCESAdded [xpc_array_get_array(_: xpc_object_t, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505537-xpc_array_get_array)Added [xpc_array_get_dictionary(_: xpc_object_t, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505954-xpc_array_get_dictionary)Added [xpc_dictionary_get_array(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505498-xpc_dictionary_get_array)Added [xpc_dictionary_get_dictionary(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505379-xpc_dictionary_get_dictionary)Modified [launch_data_type_t [struct]](https://developer.apple.com/documentation/xpc/launch_data_type_t)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct launch_data_type_t {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct launch_data_type_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [OS_xpc_object](https://developer.apple.com/documentation/xpc/os_xpc_object)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol OS_xpc_object { } ``` | -- |
| To | ``` protocol OS_xpc_object : NSObjectProtocol { } ``` | NSObjectProtocol |

Modified [launch_activate_socket(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int32>>, _: UnsafeMutablePointer<Int>) -> Int32](https://developer.apple.com/documentation/xpc/1505523-launch_activate_socket)

|  | Declaration |
| --- | --- |
| From | ``` func launch_activate_socket(_ name: UnsafePointer<Int8>, _ fds: UnsafeMutablePointer<UnsafeMutablePointer<Int32>>, _ cnt: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` @warn_unused_result func launch_activate_socket(_ name: UnsafePointer<Int8>, _ fds: UnsafeMutablePointer<UnsafeMutablePointer<Int32>>, _ cnt: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified [launch_data_alloc(_: launch_data_type_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505398-launch_data_alloc)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_alloc(_ type: launch_data_type_t) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_alloc(_ type: launch_data_type_t) -> launch_data_t ``` |

Modified [launch_data_array_get_count(_: launch_data_t) -> Int](https://developer.apple.com/documentation/xpc/1505515-launch_data_array_get_count)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_array_get_count(_ larray: launch_data_t) -> Int ``` |
| To | ``` @warn_unused_result func launch_data_array_get_count(_ larray: launch_data_t) -> Int ``` |

Modified [launch_data_array_get_index(_: launch_data_t, _: Int) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505935-launch_data_array_get_index)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_array_get_index(_ larray: launch_data_t, _ idx: Int) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_array_get_index(_ larray: launch_data_t, _ idx: Int) -> launch_data_t ``` |

Modified [launch_data_copy(_: launch_data_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505864-launch_data_copy)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_copy(_ ld: launch_data_t) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_copy(_ ld: launch_data_t) -> launch_data_t ``` |

Modified [launch_data_dict_get_count(_: launch_data_t) -> Int](https://developer.apple.com/documentation/xpc/1505450-launch_data_dict_get_count)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_dict_get_count(_ ldict: launch_data_t) -> Int ``` |
| To | ``` @warn_unused_result func launch_data_dict_get_count(_ ldict: launch_data_t) -> Int ``` |

Modified [launch_data_dict_iterator_t](https://developer.apple.com/documentation/xpc/launch_data_dict_iterator_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias launch_data_dict_iterator_t = CFunctionPointer<((launch_data_t, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias launch_data_dict_iterator_t = (launch_data_t, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [launch_data_dict_lookup(_: launch_data_t, _: UnsafePointer<Int8>) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505396-launch_data_dict_lookup)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_dict_lookup(_ ldict: launch_data_t, _ key: UnsafePointer<Int8>) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_dict_lookup(_ ldict: launch_data_t, _ key: UnsafePointer<Int8>) -> launch_data_t ``` |

Modified [launch_data_get_bool(_: launch_data_t) -> Bool](https://developer.apple.com/documentation/xpc/1505971-launch_data_get_bool)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_bool(_ ld: launch_data_t) -> Bool ``` |
| To | ``` @warn_unused_result func launch_data_get_bool(_ ld: launch_data_t) -> Bool ``` |

Modified [launch_data_get_errno(_: launch_data_t) -> Int32](https://developer.apple.com/documentation/xpc/1505553-launch_data_get_errno)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_errno(_ ld: launch_data_t) -> Int32 ``` |
| To | ``` @warn_unused_result func launch_data_get_errno(_ ld: launch_data_t) -> Int32 ``` |

Modified [launch_data_get_fd(_: launch_data_t) -> Int32](https://developer.apple.com/documentation/xpc/1505810-launch_data_get_fd)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_fd(_ ld: launch_data_t) -> Int32 ``` |
| To | ``` @warn_unused_result func launch_data_get_fd(_ ld: launch_data_t) -> Int32 ``` |

Modified [launch_data_get_integer(_: launch_data_t) -> Int64](https://developer.apple.com/documentation/xpc/1505651-launch_data_get_integer)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_integer(_ ld: launch_data_t) -> Int64 ``` |
| To | ``` @warn_unused_result func launch_data_get_integer(_ ld: launch_data_t) -> Int64 ``` |

Modified [launch_data_get_machport(_: launch_data_t) -> mach_port_t](https://developer.apple.com/documentation/xpc/1505500-launch_data_get_machport)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_machport(_ ld: launch_data_t) -> mach_port_t ``` |
| To | ``` @warn_unused_result func launch_data_get_machport(_ ld: launch_data_t) -> mach_port_t ``` |

Modified [launch_data_get_opaque(_: launch_data_t) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/xpc/1505503-launch_data_get_opaque)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_opaque(_ ld: launch_data_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` @warn_unused_result func launch_data_get_opaque(_ ld: launch_data_t) -> UnsafeMutablePointer<Void> ``` |

Modified [launch_data_get_opaque_size(_: launch_data_t) -> Int](https://developer.apple.com/documentation/xpc/1505665-launch_data_get_opaque_size)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_opaque_size(_ ld: launch_data_t) -> Int ``` |
| To | ``` @warn_unused_result func launch_data_get_opaque_size(_ ld: launch_data_t) -> Int ``` |

Modified [launch_data_get_real(_: launch_data_t) -> Double](https://developer.apple.com/documentation/xpc/1505841-launch_data_get_real)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_real(_ ld: launch_data_t) -> Double ``` |
| To | ``` @warn_unused_result func launch_data_get_real(_ ld: launch_data_t) -> Double ``` |

Modified [launch_data_get_string(_: launch_data_t) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/xpc/1505866-launch_data_get_string)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_string(_ ld: launch_data_t) -> UnsafePointer<Int8> ``` |
| To | ``` @warn_unused_result func launch_data_get_string(_ ld: launch_data_t) -> UnsafePointer<Int8> ``` |

Modified [launch_data_get_type(_: launch_data_t) -> launch_data_type_t](https://developer.apple.com/documentation/xpc/1505680-launch_data_get_type)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_get_type(_ ld: launch_data_t) -> launch_data_type_t ``` |
| To | ``` @warn_unused_result func launch_data_get_type(_ ld: launch_data_t) -> launch_data_type_t ``` |

Modified [launch_data_new_bool(_: Bool) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505947-launch_data_new_bool)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_bool(_ val: Bool) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_bool(_ val: Bool) -> launch_data_t ``` |

Modified [launch_data_new_fd(_: Int32) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505647-launch_data_new_fd)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_fd(_ fd: Int32) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_fd(_ fd: Int32) -> launch_data_t ``` |

Modified [launch_data_new_integer(_: Int64) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505444-launch_data_new_integer)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_integer(_ val: Int64) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_integer(_ val: Int64) -> launch_data_t ``` |

Modified [launch_data_new_machport(_: mach_port_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505641-launch_data_new_machport)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_machport(_ val: mach_port_t) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_machport(_ val: mach_port_t) -> launch_data_t ``` |

Modified [launch_data_new_opaque(_: UnsafePointer<Void>, _: Int) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505806-launch_data_new_opaque)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_opaque(_ bytes: UnsafePointer<Void>, _ sz: Int) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_opaque(_ bytes: UnsafePointer<Void>, _ sz: Int) -> launch_data_t ``` |

Modified [launch_data_new_real(_: Double) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505926-launch_data_new_real)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_real(_ val: Double) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_real(_ val: Double) -> launch_data_t ``` |

Modified [launch_data_new_string(_: UnsafePointer<Int8>) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505574-launch_data_new_string)

|  | Declaration |
| --- | --- |
| From | ``` func launch_data_new_string(_ val: UnsafePointer<Int8>) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_data_new_string(_ val: UnsafePointer<Int8>) -> launch_data_t ``` |

Modified [launch_get_fd() -> Int32](https://developer.apple.com/documentation/xpc/1505462-launch_get_fd)

|  | Declaration |
| --- | --- |
| From | ``` func launch_get_fd() -> Int32 ``` |
| To | ``` @warn_unused_result func launch_get_fd() -> Int32 ``` |

Modified [launch_msg(_: launch_data_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505402-launch_msg)

|  | Declaration |
| --- | --- |
| From | ``` func launch_msg(_ request: launch_data_t) -> launch_data_t ``` |
| To | ``` @warn_unused_result func launch_msg(_ request: launch_data_t) -> launch_data_t ``` |

Modified [xpc_activity_copy_criteria(_: xpc_activity_t!) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1495802-xpc_activity_copy_criteria)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_activity_copy_criteria(_ activity: xpc_activity_t!) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_activity_copy_criteria(_ activity: xpc_activity_t!) -> xpc_object_t! ``` |

Modified [xpc_activity_get_state(_: xpc_activity_t) -> xpc_activity_state_t](https://developer.apple.com/documentation/xpc/1495816-xpc_activity_get_state)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_activity_get_state(_ activity: xpc_activity_t) -> xpc_activity_state_t ``` |
| To | ``` @warn_unused_result func xpc_activity_get_state(_ activity: xpc_activity_t) -> xpc_activity_state_t ``` |

Modified [xpc_activity_set_state(_: xpc_activity_t, _: xpc_activity_state_t) -> Bool](https://developer.apple.com/documentation/xpc/1495820-xpc_activity_set_state)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_activity_set_state(_ activity: xpc_activity_t, _ state: xpc_activity_state_t) -> Bool ``` |
| To | ``` @warn_unused_result func xpc_activity_set_state(_ activity: xpc_activity_t, _ state: xpc_activity_state_t) -> Bool ``` |

Modified [xpc_array_create(_: UnsafePointer<xpc_object_t?>, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505949-xpc_array_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_create(_ objects: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_array_create(_ objects: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` |

Modified [xpc_array_create_connection(_: xpc_object_t, _: Int) -> xpc_connection_t!](https://developer.apple.com/documentation/xpc/1505596-xpc_array_create_connection)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_create_connection(_ xarray: xpc_object_t, _ index: Int) -> xpc_connection_t! ``` |
| To | ``` @warn_unused_result func xpc_array_create_connection(_ xarray: xpc_object_t, _ index: Int) -> xpc_connection_t! ``` |

Modified [xpc_array_dup_fd(_: xpc_object_t, _: Int) -> Int32](https://developer.apple.com/documentation/xpc/1505545-xpc_array_dup_fd)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_dup_fd(_ xarray: xpc_object_t, _ index: Int) -> Int32 ``` |
| To | ``` @warn_unused_result func xpc_array_dup_fd(_ xarray: xpc_object_t, _ index: Int) -> Int32 ``` |

Modified [xpc_array_get_bool(_: xpc_object_t, _: Int) -> Bool](https://developer.apple.com/documentation/xpc/1505412-xpc_array_get_bool)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_bool(_ xarray: xpc_object_t, _ index: Int) -> Bool ``` |
| To | ``` @warn_unused_result func xpc_array_get_bool(_ xarray: xpc_object_t, _ index: Int) -> Bool ``` |

Modified [xpc_array_get_count(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505582-xpc_array_get_count)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_count(_ xarray: xpc_object_t) -> Int ``` |
| To | ``` @warn_unused_result func xpc_array_get_count(_ xarray: xpc_object_t) -> Int ``` |

Modified [xpc_array_get_data(_: xpc_object_t, _: Int, _: UnsafeMutablePointer<Int>) -> UnsafePointer<Void>](https://developer.apple.com/documentation/xpc/1505387-xpc_array_get_data)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_data(_ xarray: xpc_object_t, _ index: Int, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |
| To | ``` @warn_unused_result func xpc_array_get_data(_ xarray: xpc_object_t, _ index: Int, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |

Modified [xpc_array_get_date(_: xpc_object_t, _: Int) -> Int64](https://developer.apple.com/documentation/xpc/1505723-xpc_array_get_date)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_date(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |
| To | ``` @warn_unused_result func xpc_array_get_date(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |

Modified [xpc_array_get_double(_: xpc_object_t, _: Int) -> Double](https://developer.apple.com/documentation/xpc/1505910-xpc_array_get_double)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_double(_ xarray: xpc_object_t, _ index: Int) -> Double ``` |
| To | ``` @warn_unused_result func xpc_array_get_double(_ xarray: xpc_object_t, _ index: Int) -> Double ``` |

Modified [xpc_array_get_int64(_: xpc_object_t, _: Int) -> Int64](https://developer.apple.com/documentation/xpc/1505725-xpc_array_get_int64)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_int64(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |
| To | ``` @warn_unused_result func xpc_array_get_int64(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |

Modified [xpc_array_get_string(_: xpc_object_t, _: Int) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/xpc/1505643-xpc_array_get_string)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_string(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<Int8> ``` |
| To | ``` @warn_unused_result func xpc_array_get_string(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<Int8> ``` |

Modified [xpc_array_get_uint64(_: xpc_object_t, _: Int) -> UInt64](https://developer.apple.com/documentation/xpc/1505446-xpc_array_get_uint64)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_uint64(_ xarray: xpc_object_t, _ index: Int) -> UInt64 ``` |
| To | ``` @warn_unused_result func xpc_array_get_uint64(_ xarray: xpc_object_t, _ index: Int) -> UInt64 ``` |

Modified [xpc_array_get_uuid(_: xpc_object_t, _: Int) -> UnsafePointer<UInt8>](https://developer.apple.com/documentation/xpc/1505438-xpc_array_get_uuid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_uuid(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<UInt8> ``` |
| To | ``` @warn_unused_result func xpc_array_get_uuid(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<UInt8> ``` |

Modified [xpc_bool_create(_: Bool) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505838-xpc_bool_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_bool_create(_ value: Bool) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_bool_create(_ value: Bool) -> xpc_object_t! ``` |

Modified [xpc_connection_create(_: UnsafePointer<Int8>, _: dispatch_queue_t!) -> xpc_connection_t!](https://developer.apple.com/documentation/xpc/1448791-xpc_connection_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_create(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!) -> xpc_connection_t! ``` |
| To | ``` @warn_unused_result func xpc_connection_create(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!) -> xpc_connection_t! ``` |

Modified [xpc_connection_create_from_endpoint(_: xpc_endpoint_t) -> xpc_connection_t!](https://developer.apple.com/documentation/xpc/1448784-xpc_connection_create_from_endpo)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t) -> xpc_connection_t! ``` |
| To | ``` @warn_unused_result func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t) -> xpc_connection_t! ``` |

Modified [xpc_connection_create_mach_service(_: UnsafePointer<Int8>, _: dispatch_queue_t!, _: UInt64) -> xpc_connection_t!](https://developer.apple.com/documentation/xpc/1448783-xpc_connection_create_mach_servi)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_create_mach_service(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ flags: UInt64) -> xpc_connection_t! ``` |
| To | ``` @warn_unused_result func xpc_connection_create_mach_service(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ flags: UInt64) -> xpc_connection_t! ``` |

Modified [xpc_connection_get_asid(_: xpc_connection_t) -> au_asid_t](https://developer.apple.com/documentation/xpc/1448797-xpc_connection_get_asid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_get_asid(_ connection: xpc_connection_t) -> au_asid_t ``` |
| To | ``` @warn_unused_result func xpc_connection_get_asid(_ connection: xpc_connection_t) -> au_asid_t ``` |

Modified [xpc_connection_get_context(_: xpc_connection_t) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/xpc/1448806-xpc_connection_get_context)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_get_context(_ connection: xpc_connection_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` @warn_unused_result func xpc_connection_get_context(_ connection: xpc_connection_t) -> UnsafeMutablePointer<Void> ``` |

Modified [xpc_connection_get_egid(_: xpc_connection_t) -> gid_t](https://developer.apple.com/documentation/xpc/1448823-xpc_connection_get_egid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_get_egid(_ connection: xpc_connection_t) -> gid_t ``` |
| To | ``` @warn_unused_result func xpc_connection_get_egid(_ connection: xpc_connection_t) -> gid_t ``` |

Modified [xpc_connection_get_euid(_: xpc_connection_t) -> uid_t](https://developer.apple.com/documentation/xpc/1448801-xpc_connection_get_euid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_get_euid(_ connection: xpc_connection_t) -> uid_t ``` |
| To | ``` @warn_unused_result func xpc_connection_get_euid(_ connection: xpc_connection_t) -> uid_t ``` |

Modified [xpc_connection_get_name(_: xpc_connection_t) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/xpc/1448788-xpc_connection_get_name)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_get_name(_ connection: xpc_connection_t) -> UnsafePointer<Int8> ``` |
| To | ``` @warn_unused_result func xpc_connection_get_name(_ connection: xpc_connection_t) -> UnsafePointer<Int8> ``` |

Modified [xpc_connection_get_pid(_: xpc_connection_t) -> pid_t](https://developer.apple.com/documentation/xpc/1448779-xpc_connection_get_pid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_get_pid(_ connection: xpc_connection_t) -> pid_t ``` |
| To | ``` @warn_unused_result func xpc_connection_get_pid(_ connection: xpc_connection_t) -> pid_t ``` |

Modified [xpc_connection_handler_t](https://developer.apple.com/documentation/xpc/xpc_connection_handler_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_connection_handler_t = CFunctionPointer<((xpc_connection_t!) -> Void)> ``` |
| To | ``` typealias xpc_connection_handler_t = (xpc_connection_t!) -> Void ``` |

Modified [xpc_connection_send_message_with_reply_sync(_: xpc_connection_t, _: xpc_object_t) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1448790-xpc_connection_send_message_with)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_send_message_with_reply_sync(_ connection: xpc_connection_t, _ message: xpc_object_t) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_connection_send_message_with_reply_sync(_ connection: xpc_connection_t, _ message: xpc_object_t) -> xpc_object_t! ``` |

Modified [xpc_connection_set_finalizer_f(_: xpc_connection_t, _: xpc_finalizer_t!)](https://developer.apple.com/documentation/xpc/1448819-xpc_connection_set_finalizer_f)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t, _ finalizer: xpc_finalizer_t) ``` |
| To | ``` func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t, _ finalizer: xpc_finalizer_t!) ``` |

Modified [xpc_copy(_: xpc_object_t) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505584-xpc_copy)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_copy(_ object: xpc_object_t) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_copy(_ object: xpc_object_t) -> xpc_object_t! ``` |

Modified [xpc_copy_description(_: xpc_object_t) -> UnsafeMutablePointer<Int8>](https://developer.apple.com/documentation/xpc/1505870-xpc_copy_description)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_copy_description(_ object: xpc_object_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` @warn_unused_result func xpc_copy_description(_ object: xpc_object_t) -> UnsafeMutablePointer<Int8> ``` |

Modified [xpc_data_create(_: UnsafePointer<Void>, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505855-xpc_data_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_data_create(_ bytes: UnsafePointer<Void>, _ length: Int) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_data_create(_ bytes: UnsafePointer<Void>, _ length: Int) -> xpc_object_t! ``` |

Modified [xpc_data_create_with_dispatch_data(_: dispatch_data_t) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505684-xpc_data_create_with_dispatch_da)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t) -> xpc_object_t! ``` |

Modified [xpc_data_get_bytes(_: xpc_object_t, _: UnsafeMutablePointer<Void>, _: Int, _: Int) -> Int](https://developer.apple.com/documentation/xpc/1505745-xpc_data_get_bytes)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_data_get_bytes(_ xdata: xpc_object_t, _ buffer: UnsafeMutablePointer<Void>, _ off: Int, _ length: Int) -> Int ``` |
| To | ``` @warn_unused_result func xpc_data_get_bytes(_ xdata: xpc_object_t, _ buffer: UnsafeMutablePointer<Void>, _ off: Int, _ length: Int) -> Int ``` |

Modified [xpc_data_get_bytes_ptr(_: xpc_object_t) -> UnsafePointer<Void>](https://developer.apple.com/documentation/xpc/1505667-xpc_data_get_bytes_ptr)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t) -> UnsafePointer<Void> ``` |
| To | ``` @warn_unused_result func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t) -> UnsafePointer<Void> ``` |

Modified [xpc_data_get_length(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505737-xpc_data_get_length)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_data_get_length(_ xdata: xpc_object_t) -> Int ``` |
| To | ``` @warn_unused_result func xpc_data_get_length(_ xdata: xpc_object_t) -> Int ``` |

Modified [xpc_date_create(_: Int64) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505719-xpc_date_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_date_create(_ interval: Int64) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_date_create(_ interval: Int64) -> xpc_object_t! ``` |

Modified [xpc_date_create_from_current() -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505410-xpc_date_create_from_current)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_date_create_from_current() -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_date_create_from_current() -> xpc_object_t! ``` |

Modified [xpc_date_get_value(_: xpc_object_t) -> Int64](https://developer.apple.com/documentation/xpc/1505695-xpc_date_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_date_get_value(_ xdate: xpc_object_t) -> Int64 ``` |
| To | ``` @warn_unused_result func xpc_date_get_value(_ xdate: xpc_object_t) -> Int64 ``` |

Modified [xpc_dictionary_create(_: UnsafePointer<UnsafePointer<Int8>>, _: UnsafePointer<xpc_object_t?>, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505363-xpc_dictionary_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_create(_ keys: UnsafePointer<UnsafePointer<Int8>>, _ values: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_create(_ keys: UnsafePointer<UnsafePointer<Int8>>, _ values: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` |

Modified [xpc_dictionary_create_connection(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_connection_t!](https://developer.apple.com/documentation/xpc/1505590-xpc_dictionary_create_connection)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_create_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_connection_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_create_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_connection_t! ``` |

Modified [xpc_dictionary_create_reply(_: xpc_object_t) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505619-xpc_dictionary_create_reply)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_create_reply(_ original: xpc_object_t) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_create_reply(_ original: xpc_object_t) -> xpc_object_t! ``` |

Modified [xpc_dictionary_dup_fd(_: xpc_object_t, _: UnsafePointer<Int8>) -> Int32](https://developer.apple.com/documentation/xpc/1505576-xpc_dictionary_dup_fd)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_dup_fd(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` @warn_unused_result func xpc_dictionary_dup_fd(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int32 ``` |

Modified [xpc_dictionary_get_bool(_: xpc_object_t, _: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/xpc/1505843-xpc_dictionary_get_bool)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_bool(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_bool(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Bool ``` |

Modified [xpc_dictionary_get_count(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505735-xpc_dictionary_get_count)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_count(_ xdict: xpc_object_t) -> Int ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_count(_ xdict: xpc_object_t) -> Int ``` |

Modified [xpc_dictionary_get_data(_: xpc_object_t, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<Int>) -> UnsafePointer<Void>](https://developer.apple.com/documentation/xpc/1505900-xpc_dictionary_get_data)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |

Modified [xpc_dictionary_get_date(_: xpc_object_t, _: UnsafePointer<Int8>) -> Int64](https://developer.apple.com/documentation/xpc/1505693-xpc_dictionary_get_date)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_date(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_date(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |

Modified [xpc_dictionary_get_double(_: xpc_object_t, _: UnsafePointer<Int8>) -> Double](https://developer.apple.com/documentation/xpc/1505703-xpc_dictionary_get_double)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_double(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Double ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_double(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Double ``` |

Modified [xpc_dictionary_get_int64(_: xpc_object_t, _: UnsafePointer<Int8>) -> Int64](https://developer.apple.com/documentation/xpc/1505713-xpc_dictionary_get_int64)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_int64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_int64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |

Modified [xpc_dictionary_get_remote_connection(_: xpc_object_t) -> xpc_connection_t!](https://developer.apple.com/documentation/xpc/1505637-xpc_dictionary_get_remote_connec)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_remote_connection(_ xdict: xpc_object_t) -> xpc_connection_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_remote_connection(_ xdict: xpc_object_t) -> xpc_connection_t! ``` |

Modified [xpc_dictionary_get_string(_: xpc_object_t, _: UnsafePointer<Int8>) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/xpc/1505906-xpc_dictionary_get_string)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_string(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_string(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |

Modified [xpc_dictionary_get_uint64(_: xpc_object_t, _: UnsafePointer<Int8>) -> UInt64](https://developer.apple.com/documentation/xpc/1505365-xpc_dictionary_get_uint64)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_uint64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UInt64 ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_uint64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UInt64 ``` |

Modified [xpc_dictionary_get_uuid(_: xpc_object_t, _: UnsafePointer<Int8>) -> UnsafePointer<UInt8>](https://developer.apple.com/documentation/xpc/1505419-xpc_dictionary_get_uuid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<UInt8> ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<UInt8> ``` |

Modified [xpc_dictionary_get_value(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505779-xpc_dictionary_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_get_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_dictionary_get_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |

Modified [xpc_double_create(_: Double) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505375-xpc_double_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_double_create(_ value: Double) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_double_create(_ value: Double) -> xpc_object_t! ``` |

Modified [xpc_double_get_value(_: xpc_object_t) -> Double](https://developer.apple.com/documentation/xpc/1505853-xpc_double_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_double_get_value(_ xdouble: xpc_object_t) -> Double ``` |
| To | ``` @warn_unused_result func xpc_double_get_value(_ xdouble: xpc_object_t) -> Double ``` |

Modified [xpc_endpoint_create(_: xpc_connection_t) -> xpc_endpoint_t!](https://developer.apple.com/documentation/xpc/1388113-xpc_endpoint_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_endpoint_create(_ connection: xpc_connection_t) -> xpc_endpoint_t! ``` |
| To | ``` @warn_unused_result func xpc_endpoint_create(_ connection: xpc_connection_t) -> xpc_endpoint_t! ``` |

Modified [xpc_equal(_: xpc_object_t, _: xpc_object_t) -> Bool](https://developer.apple.com/documentation/xpc/1505753-xpc_equal)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_equal(_ object1: xpc_object_t, _ object2: xpc_object_t) -> Bool ``` |
| To | ``` @warn_unused_result func xpc_equal(_ object1: xpc_object_t, _ object2: xpc_object_t) -> Bool ``` |

Modified [xpc_fd_create(_: Int32) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505655-xpc_fd_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_fd_create(_ fd: Int32) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_fd_create(_ fd: Int32) -> xpc_object_t! ``` |

Modified [xpc_fd_dup(_: xpc_object_t) -> Int32](https://developer.apple.com/documentation/xpc/1505473-xpc_fd_dup)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_fd_dup(_ xfd: xpc_object_t) -> Int32 ``` |
| To | ``` @warn_unused_result func xpc_fd_dup(_ xfd: xpc_object_t) -> Int32 ``` |

Modified [xpc_finalizer_t](https://developer.apple.com/documentation/xpc/xpc_finalizer_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_finalizer_t = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias xpc_finalizer_t = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified [xpc_get_type(_: xpc_object_t) -> xpc_type_t](https://developer.apple.com/documentation/xpc/1505661-xpc_get_type)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t ``` |
| To | ``` @warn_unused_result func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t ``` |

Modified [xpc_hash(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505511-xpc_hash)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_hash(_ object: xpc_object_t) -> Int ``` |
| To | ``` @warn_unused_result func xpc_hash(_ object: xpc_object_t) -> Int ``` |

Modified [xpc_int64_create(_: Int64) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505600-xpc_int64_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_int64_create(_ value: Int64) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_int64_create(_ value: Int64) -> xpc_object_t! ``` |

Modified [xpc_int64_get_value(_: xpc_object_t) -> Int64](https://developer.apple.com/documentation/xpc/1505721-xpc_int64_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_int64_get_value(_ xint: xpc_object_t) -> Int64 ``` |
| To | ``` @warn_unused_result func xpc_int64_get_value(_ xint: xpc_object_t) -> Int64 ``` |

Modified [xpc_null_create() -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505464-xpc_null_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_null_create() -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_null_create() -> xpc_object_t! ``` |

Modified [xpc_object_t](https://developer.apple.com/documentation/xpc/xpc_object_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_object_t = NSObject ``` |
| To | ``` typealias xpc_object_t = OS_xpc_object ``` |

Modified [xpc_shmem_create(_: UnsafeMutablePointer<Void>, _: Int) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505572-xpc_shmem_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_shmem_create(_ region: UnsafeMutablePointer<Void>, _ length: Int) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_shmem_create(_ region: UnsafeMutablePointer<Void>, _ length: Int) -> xpc_object_t! ``` |

Modified [xpc_shmem_map(_: xpc_object_t, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int](https://developer.apple.com/documentation/xpc/1505369-xpc_shmem_map)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_shmem_map(_ xshmem: xpc_object_t, _ region: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int ``` |
| To | ``` @warn_unused_result func xpc_shmem_map(_ xshmem: xpc_object_t, _ region: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int ``` |

Modified [xpc_string_create(_: UnsafePointer<Int8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505517-xpc_string_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_string_create(_ string: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_string_create(_ string: UnsafePointer<Int8>) -> xpc_object_t! ``` |

Modified [xpc_string_create_with_format_and_arguments(_: UnsafePointer<Int8>, _: CVaListPointer) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505781-xpc_string_create_with_format_an)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_string_create_with_format_and_arguments(_ fmt: UnsafePointer<Int8>, _ ap: CVaListPointer) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_string_create_with_format_and_arguments(_ fmt: UnsafePointer<Int8>, _ ap: CVaListPointer) -> xpc_object_t! ``` |

Modified [xpc_string_get_length(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505908-xpc_string_get_length)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_string_get_length(_ xstring: xpc_object_t) -> Int ``` |
| To | ``` @warn_unused_result func xpc_string_get_length(_ xstring: xpc_object_t) -> Int ``` |

Modified [xpc_string_get_string_ptr(_: xpc_object_t) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/xpc/1505731-xpc_string_get_string_ptr)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_string_get_string_ptr(_ xstring: xpc_object_t) -> UnsafePointer<Int8> ``` |
| To | ``` @warn_unused_result func xpc_string_get_string_ptr(_ xstring: xpc_object_t) -> UnsafePointer<Int8> ``` |

Modified [xpc_uint64_create(_: UInt64) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505417-xpc_uint64_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_uint64_create(_ value: UInt64) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_uint64_create(_ value: UInt64) -> xpc_object_t! ``` |

Modified [xpc_uint64_get_value(_: xpc_object_t) -> UInt64](https://developer.apple.com/documentation/xpc/1505559-xpc_uint64_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_uint64_get_value(_ xuint: xpc_object_t) -> UInt64 ``` |
| To | ``` @warn_unused_result func xpc_uint64_get_value(_ xuint: xpc_object_t) -> UInt64 ``` |

Modified [xpc_uuid_create(_: UnsafePointer<UInt8>) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505804-xpc_uuid_create)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>) -> xpc_object_t! ``` |
| To | ``` @warn_unused_result func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>) -> xpc_object_t! ``` |

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
