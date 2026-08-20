---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/XPC.html
archived_at: '2026-07-18T02:51:41.791193Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# XPC Changes for Swift

### XPC

Removed [launch_data_type_t [struct]](https://developer.apple.com/documentation/xpc/launch_data_type_t)Removed launch_data_type_t.init(_: UInt32)Removed launch_data_type_t.init(rawValue: UInt32)Removed launch_data_type_t.rawValueRemoved [launch_activate_socket(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int32>>, _: UnsafeMutablePointer<Int>) -> Int32](https://developer.apple.com/documentation/xpc/1505523-launch_activate_socket)Removed [launch_data_alloc(_: launch_data_type_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505398-launch_data_alloc)Removed [LAUNCH_DATA_ARRAY](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_array)Removed [launch_data_array_get_count(_: launch_data_t) -> Int](https://developer.apple.com/documentation/xpc/1505515-launch_data_array_get_count)Removed [launch_data_array_get_index(_: launch_data_t, _: Int) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505935-launch_data_array_get_index)Removed [launch_data_array_set_index(_: launch_data_t, _: launch_data_t, _: Int) -> Bool](https://developer.apple.com/documentation/xpc/1505624-launch_data_array_set_index)Removed [LAUNCH_DATA_BOOL](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_bool)Removed [launch_data_copy(_: launch_data_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505864-launch_data_copy)Removed [launch_data_dict_get_count(_: launch_data_t) -> Int](https://developer.apple.com/documentation/xpc/1505450-launch_data_dict_get_count)Removed [launch_data_dict_insert(_: launch_data_t, _: launch_data_t, _: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/xpc/1505566-launch_data_dict_insert)Removed [launch_data_dict_iterate(_: launch_data_t, _: launch_data_dict_iterator_t, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/xpc/1505787-launch_data_dict_iterate)Removed [launch_data_dict_iterator_t](https://developer.apple.com/documentation/xpc/launch_data_dict_iterator_t)Removed [launch_data_dict_lookup(_: launch_data_t, _: UnsafePointer<Int8>) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505396-launch_data_dict_lookup)Removed [launch_data_dict_remove(_: launch_data_t, _: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/xpc/1505490-launch_data_dict_remove)Removed [LAUNCH_DATA_DICTIONARY](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_dictionary)Removed [LAUNCH_DATA_ERRNO](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_errno)Removed [LAUNCH_DATA_FD](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_fd)Removed [launch_data_free(_: launch_data_t)](https://developer.apple.com/documentation/xpc/1505609-launch_data_free)Removed [launch_data_get_bool(_: launch_data_t) -> Bool](https://developer.apple.com/documentation/xpc/1505971-launch_data_get_bool)Removed [launch_data_get_errno(_: launch_data_t) -> Int32](https://developer.apple.com/documentation/xpc/1505553-launch_data_get_errno)Removed [launch_data_get_fd(_: launch_data_t) -> Int32](https://developer.apple.com/documentation/xpc/1505810-launch_data_get_fd)Removed [launch_data_get_integer(_: launch_data_t) -> Int64](https://developer.apple.com/documentation/xpc/1505651-launch_data_get_integer)Removed [launch_data_get_machport(_: launch_data_t) -> mach_port_t](https://developer.apple.com/documentation/xpc/1505500-launch_data_get_machport)Removed [launch_data_get_opaque(_: launch_data_t) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/xpc/1505503-launch_data_get_opaque)Removed [launch_data_get_opaque_size(_: launch_data_t) -> Int](https://developer.apple.com/documentation/xpc/1505665-launch_data_get_opaque_size)Removed [launch_data_get_real(_: launch_data_t) -> Double](https://developer.apple.com/documentation/xpc/1505841-launch_data_get_real)Removed [launch_data_get_string(_: launch_data_t) -> UnsafePointer<Int8>](https://developer.apple.com/documentation/xpc/1505866-launch_data_get_string)Removed [launch_data_get_type(_: launch_data_t) -> launch_data_type_t](https://developer.apple.com/documentation/xpc/1505680-launch_data_get_type)Removed [LAUNCH_DATA_INTEGER](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_integer)Removed [LAUNCH_DATA_MACHPORT](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_machport)Removed [launch_data_new_bool(_: Bool) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505947-launch_data_new_bool)Removed [launch_data_new_fd(_: Int32) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505647-launch_data_new_fd)Removed [launch_data_new_integer(_: Int64) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505444-launch_data_new_integer)Removed [launch_data_new_machport(_: mach_port_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505641-launch_data_new_machport)Removed [launch_data_new_opaque(_: UnsafePointer<Void>, _: Int) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505806-launch_data_new_opaque)Removed [launch_data_new_real(_: Double) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505926-launch_data_new_real)Removed [launch_data_new_string(_: UnsafePointer<Int8>) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505574-launch_data_new_string)Removed [LAUNCH_DATA_OPAQUE](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_opaque)Removed [LAUNCH_DATA_REAL](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_real)Removed [launch_data_set_bool(_: launch_data_t, _: Bool) -> Bool](https://developer.apple.com/documentation/xpc/1505509-launch_data_set_bool)Removed [launch_data_set_fd(_: launch_data_t, _: Int32) -> Bool](https://developer.apple.com/documentation/xpc/1505629-launch_data_set_fd)Removed [launch_data_set_integer(_: launch_data_t, _: Int64) -> Bool](https://developer.apple.com/documentation/xpc/1505961-launch_data_set_integer)Removed [launch_data_set_machport(_: launch_data_t, _: mach_port_t) -> Bool](https://developer.apple.com/documentation/xpc/1505455-launch_data_set_machport)Removed [launch_data_set_opaque(_: launch_data_t, _: UnsafePointer<Void>, _: Int) -> Bool](https://developer.apple.com/documentation/xpc/1505941-launch_data_set_opaque)Removed [launch_data_set_real(_: launch_data_t, _: Double) -> Bool](https://developer.apple.com/documentation/xpc/1505361-launch_data_set_real)Removed [launch_data_set_string(_: launch_data_t, _: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/xpc/1505613-launch_data_set_string)Removed [LAUNCH_DATA_STRING](https://developer.apple.com/documentation/xpc/launch_data_type_t/launch_data_string)Removed [launch_data_t](https://developer.apple.com/documentation/xpc/launch_data_t)Removed [launch_get_fd() -> Int32](https://developer.apple.com/documentation/xpc/1505462-launch_get_fd)Removed LAUNCH_JOBINETDCOMPATIBILITY_INSTANCESRemoved LAUNCH_JOBINETDCOMPATIBILITY_WAITRemoved LAUNCH_JOBKEY_ABANDONPROCESSGROUPRemoved LAUNCH_JOBKEY_BONJOURFDSRemoved LAUNCH_JOBKEY_CAL_DAYRemoved LAUNCH_JOBKEY_CAL_HOURRemoved LAUNCH_JOBKEY_CAL_MINUTERemoved LAUNCH_JOBKEY_CAL_MONTHRemoved LAUNCH_JOBKEY_CAL_WEEKDAYRemoved LAUNCH_JOBKEY_DEBUGRemoved LAUNCH_JOBKEY_DISABLEDRemoved LAUNCH_JOBKEY_DISABLED_MACHINETYPERemoved LAUNCH_JOBKEY_DISABLED_MODELNAMERemoved LAUNCH_JOBKEY_DRAINMESSAGESONFAILEDINITRemoved LAUNCH_JOBKEY_ENABLEGLOBBINGRemoved LAUNCH_JOBKEY_ENABLEPRESSUREDEXITRemoved LAUNCH_JOBKEY_ENABLETRANSACTIONSRemoved LAUNCH_JOBKEY_ENVIRONMENTVARIABLESRemoved LAUNCH_JOBKEY_EXITTIMEOUTRemoved LAUNCH_JOBKEY_GROUPNAMERemoved LAUNCH_JOBKEY_HARDRESOURCELIMITSRemoved LAUNCH_JOBKEY_HOPEFULLYEXITSFIRSTRemoved LAUNCH_JOBKEY_HOPEFULLYEXITSLASTRemoved LAUNCH_JOBKEY_IGNOREPROCESSGROUPATSHUTDOWNRemoved LAUNCH_JOBKEY_INETDCOMPATIBILITYRemoved LAUNCH_JOBKEY_INITGROUPSRemoved LAUNCH_JOBKEY_KEEPALIVERemoved LAUNCH_JOBKEY_KEEPALIVE_AFTERINITIALDEMANDRemoved LAUNCH_JOBKEY_KEEPALIVE_CRASHEDRemoved LAUNCH_JOBKEY_KEEPALIVE_NETWORKSTATERemoved LAUNCH_JOBKEY_KEEPALIVE_OTHERJOBACTIVERemoved LAUNCH_JOBKEY_KEEPALIVE_OTHERJOBENABLEDRemoved LAUNCH_JOBKEY_KEEPALIVE_PATHSTATERemoved LAUNCH_JOBKEY_KEEPALIVE_SUCCESSFULEXITRemoved LAUNCH_JOBKEY_LABELRemoved LAUNCH_JOBKEY_LASTEXITSTATUSRemoved LAUNCH_JOBKEY_LAUNCHEVENTSRemoved LAUNCH_JOBKEY_LAUNCHONLYONCERemoved LAUNCH_JOBKEY_LEGACYTIMERSRemoved LAUNCH_JOBKEY_LIMITLOADFROMHARDWARERemoved LAUNCH_JOBKEY_LIMITLOADFROMHOSTSRemoved LAUNCH_JOBKEY_LIMITLOADTOHARDWARERemoved LAUNCH_JOBKEY_LIMITLOADTOHOSTSRemoved LAUNCH_JOBKEY_LIMITLOADTOSESSIONTYPERemoved LAUNCH_JOBKEY_LOWPRIORITYBACKGROUNDIORemoved LAUNCH_JOBKEY_LOWPRIORITYIORemoved LAUNCH_JOBKEY_MACH_DRAINMESSAGESONCRASHRemoved LAUNCH_JOBKEY_MACH_HIDEUNTILCHECKINRemoved LAUNCH_JOBKEY_MACH_PINGEVENTUPDATESRemoved LAUNCH_JOBKEY_MACH_RESETATCLOSERemoved LAUNCH_JOBKEY_MACHSERVICELOOKUPPOLICIESRemoved LAUNCH_JOBKEY_MACHSERVICESRemoved LAUNCH_JOBKEY_NICERemoved LAUNCH_JOBKEY_ONDEMANDRemoved LAUNCH_JOBKEY_PIDRemoved LAUNCH_JOBKEY_POLICIESRemoved LAUNCH_JOBKEY_PROCESSTYPERemoved LAUNCH_JOBKEY_PROGRAMRemoved LAUNCH_JOBKEY_PROGRAMARGUMENTSRemoved LAUNCH_JOBKEY_QUEUEDIRECTORIESRemoved LAUNCH_JOBKEY_RESOURCELIMIT_CORERemoved LAUNCH_JOBKEY_RESOURCELIMIT_CPURemoved LAUNCH_JOBKEY_RESOURCELIMIT_DATARemoved LAUNCH_JOBKEY_RESOURCELIMIT_FSIZERemoved LAUNCH_JOBKEY_RESOURCELIMIT_MEMLOCKRemoved LAUNCH_JOBKEY_RESOURCELIMIT_NOFILERemoved LAUNCH_JOBKEY_RESOURCELIMIT_NPROCRemoved LAUNCH_JOBKEY_RESOURCELIMIT_RSSRemoved LAUNCH_JOBKEY_RESOURCELIMIT_STACKRemoved LAUNCH_JOBKEY_ROOTDIRECTORYRemoved LAUNCH_JOBKEY_RUNATLOADRemoved LAUNCH_JOBKEY_SESSIONCREATERemoved LAUNCH_JOBKEY_SOCKETSRemoved LAUNCH_JOBKEY_SOFTRESOURCELIMITSRemoved LAUNCH_JOBKEY_STANDARDERRORPATHRemoved LAUNCH_JOBKEY_STANDARDINPATHRemoved LAUNCH_JOBKEY_STANDARDOUTPATHRemoved LAUNCH_JOBKEY_STARTCALENDARINTERVALRemoved LAUNCH_JOBKEY_STARTINTERVALRemoved LAUNCH_JOBKEY_STARTONMOUNTRemoved LAUNCH_JOBKEY_THROTTLEINTERVALRemoved LAUNCH_JOBKEY_TIMEOUTRemoved LAUNCH_JOBKEY_UMASKRemoved LAUNCH_JOBKEY_USERENVIRONMENTVARIABLESRemoved LAUNCH_JOBKEY_USERNAMERemoved LAUNCH_JOBKEY_WAITFORDEBUGGERRemoved LAUNCH_JOBKEY_WATCHPATHSRemoved LAUNCH_JOBKEY_WORKINGDIRECTORYRemoved LAUNCH_JOBPOLICY_DENYCREATINGOTHERJOBSRemoved LAUNCH_JOBSOCKETKEY_BONJOURRemoved LAUNCH_JOBSOCKETKEY_FAMILYRemoved LAUNCH_JOBSOCKETKEY_MULTICASTGROUPRemoved LAUNCH_JOBSOCKETKEY_NODENAMERemoved LAUNCH_JOBSOCKETKEY_PASSIVERemoved LAUNCH_JOBSOCKETKEY_PATHGROUPRemoved LAUNCH_JOBSOCKETKEY_PATHMODERemoved LAUNCH_JOBSOCKETKEY_PATHNAMERemoved LAUNCH_JOBSOCKETKEY_PATHOWNERRemoved LAUNCH_JOBSOCKETKEY_PROTOCOLRemoved LAUNCH_JOBSOCKETKEY_SECUREWITHKEYRemoved LAUNCH_JOBSOCKETKEY_SERVICENAMERemoved LAUNCH_JOBSOCKETKEY_TYPERemoved LAUNCH_KEY_CHECKINRemoved LAUNCH_KEY_GETJOBRemoved LAUNCH_KEY_GETJOBSRemoved LAUNCH_KEY_PROCESSTYPE_ADAPTIVERemoved LAUNCH_KEY_PROCESSTYPE_APPRemoved LAUNCH_KEY_PROCESSTYPE_BACKGROUNDRemoved LAUNCH_KEY_PROCESSTYPE_INTERACTIVERemoved LAUNCH_KEY_PROCESSTYPE_STANDARDRemoved LAUNCH_KEY_REMOVEJOBRemoved LAUNCH_KEY_STARTJOBRemoved LAUNCH_KEY_STOPJOBRemoved LAUNCH_KEY_SUBMITJOBRemoved [launch_msg(_: launch_data_t) -> launch_data_t](https://developer.apple.com/documentation/xpc/1505402-launch_msg)Removed [xpc_release(_: xpc_object_t)](https://developer.apple.com/documentation/xpc/1505851-xpc_release)Removed [xpc_retain(_: xpc_object_t) -> xpc_object_t!](https://developer.apple.com/documentation/xpc/1505873-xpc_retain)Added [XPC_ARRAY_APPEND](https://developer.apple.com/documentation/xpc/xpc_array_append)Added [XPC_BOOL_FALSE](https://developer.apple.com/documentation/xpc/xpc_bool_false)Added [XPC_BOOL_TRUE](https://developer.apple.com/documentation/xpc/xpc_bool_true)Added [xpc_connection_activate(_: xpc_connection_t)](https://developer.apple.com/documentation/xpc/1641851-xpc_connection_activate)Added [XPC_ERROR_CONNECTION_INTERRUPTED](https://developer.apple.com/documentation/xpc/xpc_error_connection_interrupted)Added [XPC_ERROR_CONNECTION_INVALID](https://developer.apple.com/documentation/xpc/xpc_error_connection_invalid)Added [XPC_ERROR_KEY_DESCRIPTION](https://developer.apple.com/documentation/xpc/xpc_error_key_description)Added [XPC_ERROR_TERMINATION_IMMINENT](https://developer.apple.com/documentation/xpc/xpc_error_termination_imminent)Added [XPC_EVENT_KEY_NAME](https://developer.apple.com/documentation/xpc/xpc_event_key_name)Added [XPC_TYPE_ACTIVITY](https://developer.apple.com/documentation/xpc/xpc_type_activity)Added [XPC_TYPE_ARRAY](https://developer.apple.com/documentation/xpc/xpc_type_array)Added [XPC_TYPE_BOOL](https://developer.apple.com/documentation/xpc/xpc_type_bool)Added [XPC_TYPE_CONNECTION](https://developer.apple.com/documentation/xpc/xpc_type_connection)Added [XPC_TYPE_DATA](https://developer.apple.com/documentation/xpc/xpc_type_data)Added [XPC_TYPE_DATE](https://developer.apple.com/documentation/xpc/xpc_type_date)Added [XPC_TYPE_DICTIONARY](https://developer.apple.com/documentation/xpc/xpc_type_dictionary)Added [XPC_TYPE_DOUBLE](https://developer.apple.com/documentation/xpc/xpc_type_double)Added [XPC_TYPE_ENDPOINT](https://developer.apple.com/documentation/xpc/xpc_type_endpoint)Added [XPC_TYPE_ERROR](https://developer.apple.com/documentation/xpc/xpc_type_error)Added [XPC_TYPE_FD](https://developer.apple.com/documentation/xpc/xpc_type_fd)Added [XPC_TYPE_INT64](https://developer.apple.com/documentation/xpc/xpc_type_int64)Added [XPC_TYPE_NULL](https://developer.apple.com/documentation/xpc/xpc_type_null)Added [XPC_TYPE_SHMEM](https://developer.apple.com/documentation/xpc/xpc_type_shmem)Added [XPC_TYPE_STRING](https://developer.apple.com/documentation/xpc/xpc_type_string)Added [XPC_TYPE_UINT64](https://developer.apple.com/documentation/xpc/xpc_type_uint64)Added [XPC_TYPE_UUID](https://developer.apple.com/documentation/xpc/xpc_type_uuid)Modified [XPC_ACTIVITY_CHECK_IN](https://developer.apple.com/documentation/xpc/xpc_activity_check_in)

|  | Declaration |
| --- | --- |
| From | ``` let XPC_ACTIVITY_CHECK_IN: xpc_object_t! ``` |
| To | ``` let XPC_ACTIVITY_CHECK_IN: xpc_object_t ``` |

Modified [xpc_activity_copy_criteria(_: xpc_activity_t) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1495802-xpc_activity_copy_criteria)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_activity_copy_criteria(_ activity: xpc_activity_t!) -> xpc_object_t! ``` |
| To | ``` func xpc_activity_copy_criteria(_ activity: xpc_activity_t) -> xpc_object_t? ``` |

Modified [xpc_activity_get_state(_: xpc_activity_t) -> xpc_activity_state_t](https://developer.apple.com/documentation/xpc/1495816-xpc_activity_get_state)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_activity_get_state(_ activity: xpc_activity_t) -> xpc_activity_state_t ``` |
| To | ``` func xpc_activity_get_state(_ activity: xpc_activity_t) -> xpc_activity_state_t ``` |

Modified [xpc_activity_handler_t](https://developer.apple.com/documentation/xpc/xpc_activity_handler_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_activity_handler_t = (xpc_activity_t!) -> Void ``` |
| To | ``` typealias xpc_activity_handler_t = (xpc_activity_t) -> Swift.Void ``` |

Modified [xpc_activity_register(_: UnsafePointer<Int8>, _: xpc_object_t, _: XPC.xpc_activity_handler_t)](https://developer.apple.com/documentation/xpc/1495824-xpc_activity_register)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_activity_register(_ identifier: UnsafePointer<Int8>, _ criteria: xpc_object_t, _ handler: xpc_activity_handler_t) ``` |
| To | ``` func xpc_activity_register(_ identifier: UnsafePointer<Int8>, _ criteria: xpc_object_t, _ handler: XPC.xpc_activity_handler_t) ``` |

Modified [xpc_activity_set_state(_: xpc_activity_t, _: xpc_activity_state_t) -> Bool](https://developer.apple.com/documentation/xpc/1495820-xpc_activity_set_state)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_activity_set_state(_ activity: xpc_activity_t, _ state: xpc_activity_state_t) -> Bool ``` |
| To | ``` func xpc_activity_set_state(_ activity: xpc_activity_t, _ state: xpc_activity_state_t) -> Bool ``` |

Modified [xpc_activity_should_defer(_: xpc_activity_t) -> Bool](https://developer.apple.com/documentation/xpc/1495839-xpc_activity_should_defer)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_activity_should_defer(_ activity: xpc_activity_t!) -> Bool ``` |
| To | ``` func xpc_activity_should_defer(_ activity: xpc_activity_t) -> Bool ``` |

Modified [xpc_array_applier_t](https://developer.apple.com/documentation/xpc/xpc_array_applier_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_array_applier_t = (Int, xpc_object_t!) -> Bool ``` |
| To | ``` typealias xpc_array_applier_t = (Int, xpc_object_t) -> Bool ``` |

Modified [xpc_array_apply(_: xpc_object_t, _: XPC.xpc_array_applier_t) -> Bool](https://developer.apple.com/documentation/xpc/1505727-xpc_array_apply)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_apply(_ xarray: xpc_object_t, _ applier: xpc_array_applier_t) -> Bool ``` |
| To | ``` func xpc_array_apply(_ xarray: xpc_object_t, _ applier: XPC.xpc_array_applier_t) -> Bool ``` |

Modified [xpc_array_create(_: UnsafePointer<xpc_object_t>?, _: Int) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505949-xpc_array_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_create(_ objects: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_array_create(_ objects: UnsafePointer<xpc_object_t>?, _ count: Int) -> xpc_object_t ``` |

Modified [xpc_array_create_connection(_: xpc_object_t, _: Int) -> xpc_connection_t?](https://developer.apple.com/documentation/xpc/1505596-xpc_array_create_connection)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_create_connection(_ xarray: xpc_object_t, _ index: Int) -> xpc_connection_t! ``` |
| To | ``` func xpc_array_create_connection(_ xarray: xpc_object_t, _ index: Int) -> xpc_connection_t? ``` |

Modified [xpc_array_dup_fd(_: xpc_object_t, _: Int) -> Int32](https://developer.apple.com/documentation/xpc/1505545-xpc_array_dup_fd)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_dup_fd(_ xarray: xpc_object_t, _ index: Int) -> Int32 ``` |
| To | ``` func xpc_array_dup_fd(_ xarray: xpc_object_t, _ index: Int) -> Int32 ``` |

Modified [xpc_array_get_array(_: xpc_object_t, _: Int) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505537-xpc_array_get_array)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_array(_ self: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_array_get_array(_ self: xpc_object_t, _ index: Int) -> xpc_object_t? ``` |

Modified [xpc_array_get_bool(_: xpc_object_t, _: Int) -> Bool](https://developer.apple.com/documentation/xpc/1505412-xpc_array_get_bool)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_bool(_ xarray: xpc_object_t, _ index: Int) -> Bool ``` |
| To | ``` func xpc_array_get_bool(_ xarray: xpc_object_t, _ index: Int) -> Bool ``` |

Modified [xpc_array_get_count(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505582-xpc_array_get_count)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_count(_ xarray: xpc_object_t) -> Int ``` |
| To | ``` func xpc_array_get_count(_ xarray: xpc_object_t) -> Int ``` |

Modified [xpc_array_get_data(_: xpc_object_t, _: Int, _: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](https://developer.apple.com/documentation/xpc/1505387-xpc_array_get_data)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_data(_ xarray: xpc_object_t, _ index: Int, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |
| To | ``` func xpc_array_get_data(_ xarray: xpc_object_t, _ index: Int, _ length: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer? ``` |

Modified [xpc_array_get_date(_: xpc_object_t, _: Int) -> Int64](https://developer.apple.com/documentation/xpc/1505723-xpc_array_get_date)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_date(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |
| To | ``` func xpc_array_get_date(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |

Modified [xpc_array_get_dictionary(_: xpc_object_t, _: Int) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505954-xpc_array_get_dictionary)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_dictionary(_ self: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_array_get_dictionary(_ self: xpc_object_t, _ index: Int) -> xpc_object_t? ``` |

Modified [xpc_array_get_double(_: xpc_object_t, _: Int) -> Double](https://developer.apple.com/documentation/xpc/1505910-xpc_array_get_double)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_double(_ xarray: xpc_object_t, _ index: Int) -> Double ``` |
| To | ``` func xpc_array_get_double(_ xarray: xpc_object_t, _ index: Int) -> Double ``` |

Modified [xpc_array_get_int64(_: xpc_object_t, _: Int) -> Int64](https://developer.apple.com/documentation/xpc/1505725-xpc_array_get_int64)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_int64(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |
| To | ``` func xpc_array_get_int64(_ xarray: xpc_object_t, _ index: Int) -> Int64 ``` |

Modified [xpc_array_get_string(_: xpc_object_t, _: Int) -> UnsafePointer<Int8>?](https://developer.apple.com/documentation/xpc/1505643-xpc_array_get_string)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_string(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<Int8> ``` |
| To | ``` func xpc_array_get_string(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<Int8>? ``` |

Modified [xpc_array_get_uint64(_: xpc_object_t, _: Int) -> UInt64](https://developer.apple.com/documentation/xpc/1505446-xpc_array_get_uint64)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_uint64(_ xarray: xpc_object_t, _ index: Int) -> UInt64 ``` |
| To | ``` func xpc_array_get_uint64(_ xarray: xpc_object_t, _ index: Int) -> UInt64 ``` |

Modified [xpc_array_get_uuid(_: xpc_object_t, _: Int) -> UnsafePointer<UInt8>?](https://developer.apple.com/documentation/xpc/1505438-xpc_array_get_uuid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_array_get_uuid(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<UInt8> ``` |
| To | ``` func xpc_array_get_uuid(_ xarray: xpc_object_t, _ index: Int) -> UnsafePointer<UInt8>? ``` |

Modified [xpc_array_get_value(_: xpc_object_t, _: Int) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505377-xpc_array_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_get_value(_ xarray: xpc_object_t, _ index: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_array_get_value(_ xarray: xpc_object_t, _ index: Int) -> xpc_object_t ``` |

Modified [xpc_array_set_connection(_: xpc_object_t, _: Int, _: xpc_connection_t)](https://developer.apple.com/documentation/xpc/1505592-xpc_array_set_connection)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_set_connection(_ xarray: xpc_object_t, _ index: Int, _ connection: xpc_connection_t!) ``` |
| To | ``` func xpc_array_set_connection(_ xarray: xpc_object_t, _ index: Int, _ connection: xpc_connection_t) ``` |

Modified [xpc_array_set_data(_: xpc_object_t, _: Int, _: UnsafeRawPointer, _: Int)](https://developer.apple.com/documentation/xpc/1505937-xpc_array_set_data)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_set_data(_ xarray: xpc_object_t, _ index: Int, _ bytes: UnsafePointer<Void>, _ length: Int) ``` |
| To | ``` func xpc_array_set_data(_ xarray: xpc_object_t, _ index: Int, _ bytes: UnsafeRawPointer, _ length: Int) ``` |

Modified [xpc_array_set_uuid(_: xpc_object_t, _: Int, _: UnsafePointer<UInt8>!)](https://developer.apple.com/documentation/xpc/1505749-xpc_array_set_uuid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_array_set_uuid(_ xarray: xpc_object_t, _ index: Int, _ uuid: UnsafePointer<UInt8>) ``` |
| To | ``` func xpc_array_set_uuid(_ xarray: xpc_object_t, _ index: Int, _ uuid: UnsafePointer<UInt8>!) ``` |

Modified [xpc_bool_create(_: Bool) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505838-xpc_bool_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_bool_create(_ value: Bool) -> xpc_object_t! ``` |
| To | ``` func xpc_bool_create(_ value: Bool) -> xpc_object_t ``` |

Modified [xpc_bool_get_value(_: xpc_object_t) -> Bool](https://developer.apple.com/documentation/xpc/1505533-xpc_bool_get_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_bool_get_value(_ xbool: xpc_object_t!) -> Bool ``` |
| To | ``` func xpc_bool_get_value(_ xbool: xpc_object_t) -> Bool ``` |

Modified [xpc_connection_create(_: UnsafePointer<Int8>?, _: DispatchQueue?) -> xpc_connection_t](https://developer.apple.com/documentation/xpc/1448791-xpc_connection_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_create(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!) -> xpc_connection_t! ``` |
| To | ``` func xpc_connection_create(_ name: UnsafePointer<Int8>?, _ targetq: DispatchQueue?) -> xpc_connection_t ``` |

Modified [xpc_connection_create_from_endpoint(_: xpc_endpoint_t) -> xpc_connection_t](https://developer.apple.com/documentation/xpc/1448784-xpc_connection_create_from_endpo)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t) -> xpc_connection_t! ``` |
| To | ``` func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t) -> xpc_connection_t ``` |

Modified [xpc_connection_create_mach_service(_: UnsafePointer<Int8>, _: DispatchQueue?, _: UInt64) -> xpc_connection_t](https://developer.apple.com/documentation/xpc/1448783-xpc_connection_create_mach_servi)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_create_mach_service(_ name: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ flags: UInt64) -> xpc_connection_t! ``` |
| To | ``` func xpc_connection_create_mach_service(_ name: UnsafePointer<Int8>, _ targetq: DispatchQueue?, _ flags: UInt64) -> xpc_connection_t ``` |

Modified [xpc_connection_get_asid(_: xpc_connection_t) -> au_asid_t](https://developer.apple.com/documentation/xpc/1448797-xpc_connection_get_asid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_get_asid(_ connection: xpc_connection_t) -> au_asid_t ``` |
| To | ``` func xpc_connection_get_asid(_ connection: xpc_connection_t) -> au_asid_t ``` |

Modified [xpc_connection_get_context(_: xpc_connection_t) -> UnsafeMutableRawPointer?](https://developer.apple.com/documentation/xpc/1448806-xpc_connection_get_context)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_get_context(_ connection: xpc_connection_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func xpc_connection_get_context(_ connection: xpc_connection_t) -> UnsafeMutableRawPointer? ``` |

Modified [xpc_connection_get_egid(_: xpc_connection_t) -> gid_t](https://developer.apple.com/documentation/xpc/1448823-xpc_connection_get_egid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_get_egid(_ connection: xpc_connection_t) -> gid_t ``` |
| To | ``` func xpc_connection_get_egid(_ connection: xpc_connection_t) -> gid_t ``` |

Modified [xpc_connection_get_euid(_: xpc_connection_t) -> uid_t](https://developer.apple.com/documentation/xpc/1448801-xpc_connection_get_euid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_get_euid(_ connection: xpc_connection_t) -> uid_t ``` |
| To | ``` func xpc_connection_get_euid(_ connection: xpc_connection_t) -> uid_t ``` |

Modified [xpc_connection_get_name(_: xpc_connection_t) -> UnsafePointer<Int8>?](https://developer.apple.com/documentation/xpc/1448788-xpc_connection_get_name)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_get_name(_ connection: xpc_connection_t) -> UnsafePointer<Int8> ``` |
| To | ``` func xpc_connection_get_name(_ connection: xpc_connection_t) -> UnsafePointer<Int8>? ``` |

Modified [xpc_connection_get_pid(_: xpc_connection_t) -> pid_t](https://developer.apple.com/documentation/xpc/1448779-xpc_connection_get_pid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_get_pid(_ connection: xpc_connection_t) -> pid_t ``` |
| To | ``` func xpc_connection_get_pid(_ connection: xpc_connection_t) -> pid_t ``` |

Modified [xpc_connection_handler_t](https://developer.apple.com/documentation/xpc/xpc_connection_handler_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_connection_handler_t = (xpc_connection_t!) -> Void ``` |
| To | ``` typealias xpc_connection_handler_t = (xpc_connection_t) -> Swift.Void ``` |

Modified [xpc_connection_send_barrier(_: xpc_connection_t, _: () -> Swift.Void)](https://developer.apple.com/documentation/xpc/1448808-xpc_connection_send_barrier)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_send_barrier(_ connection: xpc_connection_t, _ barrier: dispatch_block_t) ``` |
| To | ``` func xpc_connection_send_barrier(_ connection: xpc_connection_t, _ barrier: @escaping () -> Swift.Void) ``` |

Modified [xpc_connection_send_message_with_reply(_: xpc_connection_t, _: xpc_object_t, _: DispatchQueue?, _: XPC.xpc_handler_t)](https://developer.apple.com/documentation/xpc/1448795-xpc_connection_send_message_with)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_send_message_with_reply(_ connection: xpc_connection_t, _ message: xpc_object_t, _ replyq: dispatch_queue_t!, _ handler: xpc_handler_t) ``` |
| To | ``` func xpc_connection_send_message_with_reply(_ connection: xpc_connection_t, _ message: xpc_object_t, _ replyq: DispatchQueue?, _ handler: XPC.xpc_handler_t) ``` |

Modified [xpc_connection_send_message_with_reply_sync(_: xpc_connection_t, _: xpc_object_t) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1448790-xpc_connection_send_message_with)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_connection_send_message_with_reply_sync(_ connection: xpc_connection_t, _ message: xpc_object_t) -> xpc_object_t! ``` |
| To | ``` func xpc_connection_send_message_with_reply_sync(_ connection: xpc_connection_t, _ message: xpc_object_t) -> xpc_object_t ``` |

Modified [xpc_connection_set_context(_: xpc_connection_t, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/xpc/1448814-xpc_connection_set_context)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_set_context(_ connection: xpc_connection_t, _ context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func xpc_connection_set_context(_ connection: xpc_connection_t, _ context: UnsafeMutableRawPointer?) ``` |

Modified [xpc_connection_set_event_handler(_: xpc_connection_t, _: XPC.xpc_handler_t)](https://developer.apple.com/documentation/xpc/1448805-xpc_connection_set_event_handler)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_set_event_handler(_ connection: xpc_connection_t, _ handler: xpc_handler_t) ``` |
| To | ``` func xpc_connection_set_event_handler(_ connection: xpc_connection_t, _ handler: XPC.xpc_handler_t) ``` |

Modified [xpc_connection_set_finalizer_f(_: xpc_connection_t, _: XPC.xpc_finalizer_t?)](https://developer.apple.com/documentation/xpc/1448819-xpc_connection_set_finalizer_f)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t, _ finalizer: xpc_finalizer_t!) ``` |
| To | ``` func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t, _ finalizer: XPC.xpc_finalizer_t?) ``` |

Modified [xpc_connection_set_target_queue(_: xpc_connection_t, _: DispatchQueue?)](https://developer.apple.com/documentation/xpc/1448786-xpc_connection_set_target_queue)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_connection_set_target_queue(_ connection: xpc_connection_t, _ targetq: dispatch_queue_t!) ``` |
| To | ``` func xpc_connection_set_target_queue(_ connection: xpc_connection_t, _ targetq: DispatchQueue?) ``` |

Modified [xpc_copy(_: xpc_object_t) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505584-xpc_copy)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_copy(_ object: xpc_object_t) -> xpc_object_t! ``` |
| To | ``` func xpc_copy(_ object: xpc_object_t) -> xpc_object_t? ``` |

Modified [xpc_copy_description(_: xpc_object_t) -> UnsafeMutablePointer<Int8>](https://developer.apple.com/documentation/xpc/1505870-xpc_copy_description)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_copy_description(_ object: xpc_object_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func xpc_copy_description(_ object: xpc_object_t) -> UnsafeMutablePointer<Int8> ``` |

Modified [xpc_data_create(_: UnsafeRawPointer, _: Int) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505855-xpc_data_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_data_create(_ bytes: UnsafePointer<Void>, _ length: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_data_create(_ bytes: UnsafeRawPointer, _ length: Int) -> xpc_object_t ``` |

Modified [xpc_data_create_with_dispatch_data(_: __DispatchData) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505684-xpc_data_create_with_dispatch_da)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t) -> xpc_object_t! ``` |
| To | ``` func xpc_data_create_with_dispatch_data(_ ddata: __DispatchData) -> xpc_object_t ``` |

Modified [xpc_data_get_bytes(_: xpc_object_t, _: UnsafeMutableRawPointer, _: Int, _: Int) -> Int](https://developer.apple.com/documentation/xpc/1505745-xpc_data_get_bytes)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_data_get_bytes(_ xdata: xpc_object_t, _ buffer: UnsafeMutablePointer<Void>, _ off: Int, _ length: Int) -> Int ``` |
| To | ``` func xpc_data_get_bytes(_ xdata: xpc_object_t, _ buffer: UnsafeMutableRawPointer, _ off: Int, _ length: Int) -> Int ``` |

Modified [xpc_data_get_bytes_ptr(_: xpc_object_t) -> UnsafeRawPointer?](https://developer.apple.com/documentation/xpc/1505667-xpc_data_get_bytes_ptr)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t) -> UnsafePointer<Void> ``` |
| To | ``` func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t) -> UnsafeRawPointer? ``` |

Modified [xpc_data_get_length(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505737-xpc_data_get_length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_data_get_length(_ xdata: xpc_object_t) -> Int ``` |
| To | ``` func xpc_data_get_length(_ xdata: xpc_object_t) -> Int ``` |

Modified [xpc_date_create(_: Int64) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505719-xpc_date_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_date_create(_ interval: Int64) -> xpc_object_t! ``` |
| To | ``` func xpc_date_create(_ interval: Int64) -> xpc_object_t ``` |

Modified [xpc_date_create_from_current() -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505410-xpc_date_create_from_current)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_date_create_from_current() -> xpc_object_t! ``` |
| To | ``` func xpc_date_create_from_current() -> xpc_object_t ``` |

Modified [xpc_date_get_value(_: xpc_object_t) -> Int64](https://developer.apple.com/documentation/xpc/1505695-xpc_date_get_value)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_date_get_value(_ xdate: xpc_object_t) -> Int64 ``` |
| To | ``` func xpc_date_get_value(_ xdate: xpc_object_t) -> Int64 ``` |

Modified [xpc_debugger_api_misuse_info() -> UnsafePointer<Int8>!](https://developer.apple.com/documentation/xpc/1505415-xpc_debugger_api_misuse_info)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_debugger_api_misuse_info() -> UnsafePointer<Int8> ``` |
| To | ``` func xpc_debugger_api_misuse_info() -> UnsafePointer<Int8>! ``` |

Modified [xpc_dictionary_applier_t](https://developer.apple.com/documentation/xpc/xpc_dictionary_applier_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_dictionary_applier_t = (UnsafePointer<Int8>, xpc_object_t!) -> Bool ``` |
| To | ``` typealias xpc_dictionary_applier_t = (UnsafePointer<Int8>, xpc_object_t) -> Bool ``` |

Modified [xpc_dictionary_apply(_: xpc_object_t, _: XPC.xpc_dictionary_applier_t) -> Bool](https://developer.apple.com/documentation/xpc/1505404-xpc_dictionary_apply)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_apply(_ xdict: xpc_object_t, _ applier: xpc_dictionary_applier_t) -> Bool ``` |
| To | ``` func xpc_dictionary_apply(_ xdict: xpc_object_t, _ applier: XPC.xpc_dictionary_applier_t) -> Bool ``` |

Modified [xpc_dictionary_create(_: UnsafePointer<UnsafePointer<Int8>>?, _: UnsafePointer<xpc_object_t?>?, _: Int) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505363-xpc_dictionary_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_create(_ keys: UnsafePointer<UnsafePointer<Int8>>, _ values: UnsafePointer<xpc_object_t?>, _ count: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_dictionary_create(_ keys: UnsafePointer<UnsafePointer<Int8>>?, _ values: UnsafePointer<xpc_object_t?>?, _ count: Int) -> xpc_object_t ``` |

Modified [xpc_dictionary_create_connection(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_connection_t?](https://developer.apple.com/documentation/xpc/1505590-xpc_dictionary_create_connection)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_create_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_connection_t! ``` |
| To | ``` func xpc_dictionary_create_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_connection_t? ``` |

Modified [xpc_dictionary_create_reply(_: xpc_object_t) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505619-xpc_dictionary_create_reply)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_create_reply(_ original: xpc_object_t) -> xpc_object_t! ``` |
| To | ``` func xpc_dictionary_create_reply(_ original: xpc_object_t) -> xpc_object_t? ``` |

Modified [xpc_dictionary_dup_fd(_: xpc_object_t, _: UnsafePointer<Int8>) -> Int32](https://developer.apple.com/documentation/xpc/1505576-xpc_dictionary_dup_fd)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_dup_fd(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func xpc_dictionary_dup_fd(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int32 ``` |

Modified [xpc_dictionary_get_array(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505498-xpc_dictionary_get_array)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_array(_ self: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` func xpc_dictionary_get_array(_ self: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t? ``` |

Modified [xpc_dictionary_get_bool(_: xpc_object_t, _: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/xpc/1505843-xpc_dictionary_get_bool)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_bool(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func xpc_dictionary_get_bool(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Bool ``` |

Modified [xpc_dictionary_get_count(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505735-xpc_dictionary_get_count)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_count(_ xdict: xpc_object_t) -> Int ``` |
| To | ``` func xpc_dictionary_get_count(_ xdict: xpc_object_t) -> Int ``` |

Modified [xpc_dictionary_get_data(_: xpc_object_t, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer?](https://developer.apple.com/documentation/xpc/1505900-xpc_dictionary_get_data)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ length: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |
| To | ``` func xpc_dictionary_get_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ length: UnsafeMutablePointer<Int>?) -> UnsafeRawPointer? ``` |

Modified [xpc_dictionary_get_date(_: xpc_object_t, _: UnsafePointer<Int8>) -> Int64](https://developer.apple.com/documentation/xpc/1505693-xpc_dictionary_get_date)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_date(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |
| To | ``` func xpc_dictionary_get_date(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |

Modified [xpc_dictionary_get_dictionary(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505379-xpc_dictionary_get_dictionary)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_dictionary(_ self: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` func xpc_dictionary_get_dictionary(_ self: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t? ``` |

Modified [xpc_dictionary_get_double(_: xpc_object_t, _: UnsafePointer<Int8>) -> Double](https://developer.apple.com/documentation/xpc/1505703-xpc_dictionary_get_double)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_double(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Double ``` |
| To | ``` func xpc_dictionary_get_double(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Double ``` |

Modified [xpc_dictionary_get_int64(_: xpc_object_t, _: UnsafePointer<Int8>) -> Int64](https://developer.apple.com/documentation/xpc/1505713-xpc_dictionary_get_int64)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_int64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |
| To | ``` func xpc_dictionary_get_int64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> Int64 ``` |

Modified [xpc_dictionary_get_remote_connection(_: xpc_object_t) -> xpc_connection_t?](https://developer.apple.com/documentation/xpc/1505637-xpc_dictionary_get_remote_connec)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_remote_connection(_ xdict: xpc_object_t) -> xpc_connection_t! ``` |
| To | ``` func xpc_dictionary_get_remote_connection(_ xdict: xpc_object_t) -> xpc_connection_t? ``` |

Modified [xpc_dictionary_get_string(_: xpc_object_t, _: UnsafePointer<Int8>) -> UnsafePointer<Int8>?](https://developer.apple.com/documentation/xpc/1505906-xpc_dictionary_get_string)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_string(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |
| To | ``` func xpc_dictionary_get_string(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<Int8>? ``` |

Modified [xpc_dictionary_get_uint64(_: xpc_object_t, _: UnsafePointer<Int8>) -> UInt64](https://developer.apple.com/documentation/xpc/1505365-xpc_dictionary_get_uint64)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_uint64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UInt64 ``` |
| To | ``` func xpc_dictionary_get_uint64(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UInt64 ``` |

Modified [xpc_dictionary_get_uuid(_: xpc_object_t, _: UnsafePointer<Int8>) -> UnsafePointer<UInt8>?](https://developer.apple.com/documentation/xpc/1505419-xpc_dictionary_get_uuid)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<UInt8> ``` |
| To | ``` func xpc_dictionary_get_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> UnsafePointer<UInt8>? ``` |

Modified [xpc_dictionary_get_value(_: xpc_object_t, _: UnsafePointer<Int8>) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505779-xpc_dictionary_get_value)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_dictionary_get_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` func xpc_dictionary_get_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>) -> xpc_object_t? ``` |

Modified [xpc_dictionary_set_connection(_: xpc_object_t, _: UnsafePointer<Int8>, _: xpc_connection_t)](https://developer.apple.com/documentation/xpc/1505914-xpc_dictionary_set_connection)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_set_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ connection: xpc_connection_t!) ``` |
| To | ``` func xpc_dictionary_set_connection(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ connection: xpc_connection_t) ``` |

Modified [xpc_dictionary_set_data(_: xpc_object_t, _: UnsafePointer<Int8>, _: UnsafeRawPointer, _: Int)](https://developer.apple.com/documentation/xpc/1505820-xpc_dictionary_set_data)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_set_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ bytes: UnsafePointer<Void>, _ length: Int) ``` |
| To | ``` func xpc_dictionary_set_data(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ bytes: UnsafeRawPointer, _ length: Int) ``` |

Modified [xpc_dictionary_set_uuid(_: xpc_object_t, _: UnsafePointer<Int8>, _: UnsafePointer<UInt8>!)](https://developer.apple.com/documentation/xpc/1505912-xpc_dictionary_set_uuid)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_set_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ uuid: UnsafePointer<UInt8>) ``` |
| To | ``` func xpc_dictionary_set_uuid(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ uuid: UnsafePointer<UInt8>!) ``` |

Modified [xpc_dictionary_set_value(_: xpc_object_t, _: UnsafePointer<Int8>, _: xpc_object_t?)](https://developer.apple.com/documentation/xpc/1505605-xpc_dictionary_set_value)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_dictionary_set_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: xpc_object_t!) ``` |
| To | ``` func xpc_dictionary_set_value(_ xdict: xpc_object_t, _ key: UnsafePointer<Int8>, _ value: xpc_object_t?) ``` |

Modified [xpc_double_create(_: Double) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505375-xpc_double_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_double_create(_ value: Double) -> xpc_object_t! ``` |
| To | ``` func xpc_double_create(_ value: Double) -> xpc_object_t ``` |

Modified [xpc_double_get_value(_: xpc_object_t) -> Double](https://developer.apple.com/documentation/xpc/1505853-xpc_double_get_value)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_double_get_value(_ xdouble: xpc_object_t) -> Double ``` |
| To | ``` func xpc_double_get_value(_ xdouble: xpc_object_t) -> Double ``` |

Modified [xpc_endpoint_create(_: xpc_connection_t) -> xpc_endpoint_t](https://developer.apple.com/documentation/xpc/1388113-xpc_endpoint_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_endpoint_create(_ connection: xpc_connection_t) -> xpc_endpoint_t! ``` |
| To | ``` func xpc_endpoint_create(_ connection: xpc_connection_t) -> xpc_endpoint_t ``` |

Modified [xpc_equal(_: xpc_object_t, _: xpc_object_t) -> Bool](https://developer.apple.com/documentation/xpc/1505753-xpc_equal)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_equal(_ object1: xpc_object_t, _ object2: xpc_object_t) -> Bool ``` |
| To | ``` func xpc_equal(_ object1: xpc_object_t, _ object2: xpc_object_t) -> Bool ``` |

Modified [xpc_fd_create(_: Int32) -> xpc_object_t?](https://developer.apple.com/documentation/xpc/1505655-xpc_fd_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_fd_create(_ fd: Int32) -> xpc_object_t! ``` |
| To | ``` func xpc_fd_create(_ fd: Int32) -> xpc_object_t? ``` |

Modified [xpc_fd_dup(_: xpc_object_t) -> Int32](https://developer.apple.com/documentation/xpc/1505473-xpc_fd_dup)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_fd_dup(_ xfd: xpc_object_t) -> Int32 ``` |
| To | ``` func xpc_fd_dup(_ xfd: xpc_object_t) -> Int32 ``` |

Modified [xpc_finalizer_t](https://developer.apple.com/documentation/xpc/xpc_finalizer_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_finalizer_t = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias xpc_finalizer_t = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [xpc_get_type(_: xpc_object_t) -> xpc_type_t](https://developer.apple.com/documentation/xpc/1505661-xpc_get_type)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t ``` |
| To | ``` func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t ``` |

Modified [xpc_handler_t](https://developer.apple.com/documentation/xpc/xpc_handler_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_handler_t = (xpc_object_t!) -> Void ``` |
| To | ``` typealias xpc_handler_t = (xpc_object_t) -> Swift.Void ``` |

Modified [xpc_hash(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505511-xpc_hash)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_hash(_ object: xpc_object_t) -> Int ``` |
| To | ``` func xpc_hash(_ object: xpc_object_t) -> Int ``` |

Modified [xpc_int64_create(_: Int64) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505600-xpc_int64_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_int64_create(_ value: Int64) -> xpc_object_t! ``` |
| To | ``` func xpc_int64_create(_ value: Int64) -> xpc_object_t ``` |

Modified [xpc_int64_get_value(_: xpc_object_t) -> Int64](https://developer.apple.com/documentation/xpc/1505721-xpc_int64_get_value)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_int64_get_value(_ xint: xpc_object_t) -> Int64 ``` |
| To | ``` func xpc_int64_get_value(_ xint: xpc_object_t) -> Int64 ``` |

Modified [xpc_main(_: XPC.xpc_connection_handler_t) -> Never](https://developer.apple.com/documentation/xpc/1505740-xpc_main)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func xpc_main(_ handler: xpc_connection_handler_t) ``` |
| To | ``` func xpc_main(_ handler: XPC.xpc_connection_handler_t) -> Never ``` |

Modified [xpc_null_create() -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505464-xpc_null_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_null_create() -> xpc_object_t! ``` |
| To | ``` func xpc_null_create() -> xpc_object_t ``` |

Modified [xpc_set_event_stream_handler(_: UnsafePointer<Int8>, _: DispatchQueue?, _: XPC.xpc_handler_t)](https://developer.apple.com/documentation/xpc/1505578-xpc_set_event_stream_handler)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_set_event_stream_handler(_ stream: UnsafePointer<Int8>, _ targetq: dispatch_queue_t!, _ handler: xpc_handler_t) ``` |
| To | ``` func xpc_set_event_stream_handler(_ stream: UnsafePointer<Int8>, _ targetq: DispatchQueue?, _ handler: XPC.xpc_handler_t) ``` |

Modified [xpc_shmem_create(_: UnsafeMutableRawPointer, _: Int) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505572-xpc_shmem_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_shmem_create(_ region: UnsafeMutablePointer<Void>, _ length: Int) -> xpc_object_t! ``` |
| To | ``` func xpc_shmem_create(_ region: UnsafeMutableRawPointer, _ length: Int) -> xpc_object_t ``` |

Modified [xpc_shmem_map(_: xpc_object_t, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int](https://developer.apple.com/documentation/xpc/1505369-xpc_shmem_map)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_shmem_map(_ xshmem: xpc_object_t, _ region: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int ``` |
| To | ``` func xpc_shmem_map(_ xshmem: xpc_object_t, _ region: UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int ``` |

Modified [xpc_string_create(_: UnsafePointer<Int8>) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505517-xpc_string_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_string_create(_ string: UnsafePointer<Int8>) -> xpc_object_t! ``` |
| To | ``` func xpc_string_create(_ string: UnsafePointer<Int8>) -> xpc_object_t ``` |

Modified [xpc_string_create_with_format_and_arguments(_: UnsafePointer<Int8>, _: CVaListPointer) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505781-xpc_string_create_with_format_an)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_string_create_with_format_and_arguments(_ fmt: UnsafePointer<Int8>, _ ap: CVaListPointer) -> xpc_object_t! ``` |
| To | ``` func xpc_string_create_with_format_and_arguments(_ fmt: UnsafePointer<Int8>, _ ap: CVaListPointer) -> xpc_object_t ``` |

Modified [xpc_string_get_length(_: xpc_object_t) -> Int](https://developer.apple.com/documentation/xpc/1505908-xpc_string_get_length)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_string_get_length(_ xstring: xpc_object_t) -> Int ``` |
| To | ``` func xpc_string_get_length(_ xstring: xpc_object_t) -> Int ``` |

Modified [xpc_string_get_string_ptr(_: xpc_object_t) -> UnsafePointer<Int8>?](https://developer.apple.com/documentation/xpc/1505731-xpc_string_get_string_ptr)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_string_get_string_ptr(_ xstring: xpc_object_t) -> UnsafePointer<Int8> ``` |
| To | ``` func xpc_string_get_string_ptr(_ xstring: xpc_object_t) -> UnsafePointer<Int8>? ``` |

Modified [xpc_type_t](https://developer.apple.com/documentation/xpc/xpc_type_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias xpc_type_t = COpaquePointer ``` |
| To | ``` typealias xpc_type_t = OpaquePointer ``` |

Modified [xpc_uint64_create(_: UInt64) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505417-xpc_uint64_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_uint64_create(_ value: UInt64) -> xpc_object_t! ``` |
| To | ``` func xpc_uint64_create(_ value: UInt64) -> xpc_object_t ``` |

Modified [xpc_uint64_get_value(_: xpc_object_t) -> UInt64](https://developer.apple.com/documentation/xpc/1505559-xpc_uint64_get_value)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_uint64_get_value(_ xuint: xpc_object_t) -> UInt64 ``` |
| To | ``` func xpc_uint64_get_value(_ xuint: xpc_object_t) -> UInt64 ``` |

Modified [xpc_uuid_create(_: UnsafePointer<UInt8>!) -> xpc_object_t](https://developer.apple.com/documentation/xpc/1505804-xpc_uuid_create)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>) -> xpc_object_t! ``` |
| To | ``` func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>!) -> xpc_object_t ``` |

Modified [xpc_uuid_get_bytes(_: xpc_object_t) -> UnsafePointer<UInt8>?](https://developer.apple.com/documentation/xpc/1505479-xpc_uuid_get_bytes)

|  | Declaration |
| --- | --- |
| From | ``` func xpc_uuid_get_bytes(_ xuuid: xpc_object_t) -> UnsafePointer<UInt8> ``` |
| To | ``` func xpc_uuid_get_bytes(_ xuuid: xpc_object_t) -> UnsafePointer<UInt8>? ``` |

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
