---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/GSS.html
archived_at: '2026-07-18T02:52:29.981352Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# GSS Changes

## GSS

Added gss_OID_desc_struct.init()Added gss_OID_desc_struct.init(length: OM_uint32, elements: UnsafeMutablePointer<Void>)Added gss_OID_set_desc_struct.init()Added gss_OID_set_desc_struct.init(count: Int, elements: gss_OID)Added gss_buffer_desc_struct.init()Added gss_buffer_desc_struct.init(length: Int, value: UnsafeMutablePointer<Void>)Added gss_buffer_set_desc_struct.init()Added gss_buffer_set_desc_struct.init(count: Int, elements: UnsafeMutablePointer<gss_buffer_desc>)Added gss_channel_bindings_struct.init()Added gss_channel_bindings_struct.init(initiator_addrtype: OM_uint32, initiator_address: gss_buffer_desc, acceptor_addrtype: OM_uint32, acceptor_address: gss_buffer_desc, application_data: gss_buffer_desc)Added gss_iov_buffer_desc_struct.init()Added gss_iov_buffer_desc_struct.init(type: OM_uint32, buffer: gss_buffer_desc)Added kGSSChangePasswordNewPasswordAdded kGSSChangePasswordOldPasswordAdded kGSSCredentialUsageAdded kGSSICAppIdentifierACLAdded kGSSICCertificateAdded kGSSICKerberosCacheNameAdded kGSSICLKDCHostnameAdded kGSSICPasswordAdded kGSSICVerifyCredentialAdded kGSS_C_ACCEPTAdded kGSS_C_BOTHAdded kGSS_C_INITIATEModified gss_OID_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_OID_desc_struct {     var length: OM_uint32     var elements: UnsafePointer<()> } ``` |
| To | ``` struct gss_OID_desc_struct {     var length: OM_uint32     var elements: UnsafeMutablePointer<Void>     init()     init(length length: OM_uint32, elements elements: UnsafeMutablePointer<Void>) } ``` |

Modified gss_OID_desc_struct.elements

|  | Declaration |
| --- | --- |
| From | ``` var elements: UnsafePointer<()> ``` |
| To | ``` var elements: UnsafeMutablePointer<Void> ``` |

Modified gss_OID_set_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_OID_set_desc_struct {     var count: UInt     var elements: gss_OID } ``` |
| To | ``` struct gss_OID_set_desc_struct {     var count: Int     var elements: gss_OID     init()     init(count count: Int, elements elements: gss_OID) } ``` |

Modified gss_OID_set_desc_struct.count

|  | Declaration |
| --- | --- |
| From | ``` var count: UInt ``` |
| To | ``` var count: Int ``` |

Modified gss_buffer_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_buffer_desc_struct {     var length: UInt     var value: UnsafePointer<()> } ``` |
| To | ``` struct gss_buffer_desc_struct {     var length: Int     var value: UnsafeMutablePointer<Void>     init()     init(length length: Int, value value: UnsafeMutablePointer<Void>) } ``` |

Modified gss_buffer_desc_struct.length

|  | Declaration |
| --- | --- |
| From | ``` var length: UInt ``` |
| To | ``` var length: Int ``` |

Modified gss_buffer_desc_struct.value

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafePointer<()> ``` |
| To | ``` var value: UnsafeMutablePointer<Void> ``` |

Modified gss_buffer_set_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_buffer_set_desc_struct {     var count: UInt     var elements: UnsafePointer<gss_buffer_desc> } ``` |
| To | ``` struct gss_buffer_set_desc_struct {     var count: Int     var elements: UnsafeMutablePointer<gss_buffer_desc>     init()     init(count count: Int, elements elements: UnsafeMutablePointer<gss_buffer_desc>) } ``` |

Modified gss_buffer_set_desc_struct.count

|  | Declaration |
| --- | --- |
| From | ``` var count: UInt ``` |
| To | ``` var count: Int ``` |

Modified gss_buffer_set_desc_struct.elements

|  | Declaration |
| --- | --- |
| From | ``` var elements: UnsafePointer<gss_buffer_desc> ``` |
| To | ``` var elements: UnsafeMutablePointer<gss_buffer_desc> ``` |

Modified gss_channel_bindings_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_channel_bindings_struct {     var initiator_addrtype: OM_uint32     var initiator_address: gss_buffer_desc     var acceptor_addrtype: OM_uint32     var acceptor_address: gss_buffer_desc     var application_data: gss_buffer_desc } ``` |
| To | ``` struct gss_channel_bindings_struct {     var initiator_addrtype: OM_uint32     var initiator_address: gss_buffer_desc     var acceptor_addrtype: OM_uint32     var acceptor_address: gss_buffer_desc     var application_data: gss_buffer_desc     init()     init(initiator_addrtype initiator_addrtype: OM_uint32, initiator_address initiator_address: gss_buffer_desc, acceptor_addrtype acceptor_addrtype: OM_uint32, acceptor_address acceptor_address: gss_buffer_desc, application_data application_data: gss_buffer_desc) } ``` |

Modified gss_iov_buffer_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_iov_buffer_desc_struct {     var type: OM_uint32     var buffer: gss_buffer_desc } ``` |
| To | ``` struct gss_iov_buffer_desc_struct {     var type: OM_uint32     var buffer: gss_buffer_desc     init()     init(type type: OM_uint32, buffer buffer: gss_buffer_desc) } ``` |

Modified GSSCreateCredentialFromUUID(CFUUID!) -> gss_cred_id_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GSSCreateName(AnyObject!, gss_const_OID, UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func GSSCreateName(_ name: AnyObject!, _ name_type: gss_const_OID, _ error: UnsafePointer<Unmanaged<CFError>?>) -> gss_name_t ``` | OS X 10.10 |
| To | ``` func GSSCreateName(_ name: AnyObject!, _ name_type: gss_const_OID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t ``` | OS X 10.9 |

Modified GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GSSCredentialCopyUUID(gss_cred_id_t) -> Unmanaged<CFUUID>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GSSCredentialGetLifetime(gss_cred_id_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GSSNameCreateDisplayString(gss_name_t) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified gss_OID

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_OID = UnsafePointer<gss_OID_desc_struct> ``` |
| To | ``` typealias gss_OID = UnsafeMutablePointer<gss_OID_desc_struct> ``` |

Modified gss_OID_set

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_OID_set = UnsafePointer<gss_OID_set_desc_struct> ``` |
| To | ``` typealias gss_OID_set = UnsafeMutablePointer<gss_OID_set_desc_struct> ``` |

Modified gss_aapl_change_password(gss_name_t, gss_const_OID, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` | OS X 10.9 |

Modified gss_aapl_initial_cred(gss_name_t, gss_const_OID, CFDictionary!, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary!, _ output_cred_handle: UnsafePointer<gss_cred_id_t>, _ error: UnsafePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary!, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_cred_id_t, gss_buffer_t, gss_channel_bindings_t, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<gss_OID>, gss_buffer_t, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_accept_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: UnsafePointer<gss_ctx_id_t>, _ acceptor_cred_handle: gss_cred_id_t, _ input_token: gss_buffer_t, _ input_chan_bindings: gss_channel_bindings_t, _ src_name: UnsafePointer<gss_name_t>, _ mech_type: UnsafePointer<gss_OID>, _ output_token: gss_buffer_t, _ ret_flags: UnsafePointer<OM_uint32>, _ time_rec: UnsafePointer<OM_uint32>, _ delegated_cred_handle: UnsafePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_accept_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ acceptor_cred_handle: gss_cred_id_t, _ input_token: gss_buffer_t, _ input_chan_bindings: gss_channel_bindings_t, _ src_name: UnsafeMutablePointer<gss_name_t>, _ mech_type: UnsafeMutablePointer<gss_OID>, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>, _ time_rec: UnsafeMutablePointer<OM_uint32>, _ delegated_cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t, OM_uint32, gss_OID_set, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_acquire_cred(_ minor_status: UnsafePointer<OM_uint32>, _ desired_name: gss_name_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafePointer<gss_cred_id_t>, _ actual_mechs: UnsafePointer<gss_OID_set>, _ time_rec: UnsafePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_acquire_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set>, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_acquire_cred_with_password(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, OM_uint32, gss_OID_set, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_acquire_cred_with_password(_ minor_status: UnsafePointer<OM_uint32>, _ desired_name: gss_name_t, _ password: gss_buffer_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafePointer<gss_cred_id_t>, _ actual_mechs: UnsafePointer<gss_OID_set>, _ time_rec: UnsafePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_acquire_cred_with_password(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t, _ password: gss_buffer_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set>, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_add_buffer_set_member(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_add_buffer_set_member(_ minor_status: UnsafePointer<OM_uint32>, _ member_buffer: gss_buffer_t, _ buffer_set: UnsafePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_add_buffer_set_member(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ member_buffer: gss_buffer_t, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_add_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_name_t, gss_OID, gss_cred_usage_t, OM_uint32, OM_uint32, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_add_cred(_ minor_status: UnsafePointer<OM_uint32>, _ input_cred_handle: gss_cred_id_t, _ desired_name: gss_name_t, _ desired_mech: gss_OID, _ cred_usage: gss_cred_usage_t, _ initiator_time_req: OM_uint32, _ acceptor_time_req: OM_uint32, _ output_cred_handle: UnsafePointer<gss_cred_id_t>, _ actual_mechs: UnsafePointer<gss_OID_set>, _ initiator_time_rec: UnsafePointer<OM_uint32>, _ acceptor_time_rec: UnsafePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_add_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_cred_handle: gss_cred_id_t, _ desired_name: gss_name_t, _ desired_mech: gss_OID, _ cred_usage: gss_cred_usage_t, _ initiator_time_req: OM_uint32, _ acceptor_time_req: OM_uint32, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set>, _ initiator_time_rec: UnsafeMutablePointer<OM_uint32>, _ acceptor_time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_add_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_add_oid_set_member(_ minor_status: UnsafePointer<OM_uint32>, _ member_oid: gss_const_OID, _ oid_set: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_add_oid_set_member(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ member_oid: gss_const_OID, _ oid_set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_buffer_set_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_buffer_set_t = UnsafePointer<gss_buffer_set_desc_struct> ``` |
| To | ``` typealias gss_buffer_set_t = UnsafeMutablePointer<gss_buffer_set_desc_struct> ``` |

Modified gss_buffer_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_buffer_t = UnsafePointer<gss_buffer_desc_struct> ``` |
| To | ``` typealias gss_buffer_t = UnsafeMutablePointer<gss_buffer_desc_struct> ``` |

Modified gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_canonicalize_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_type: gss_OID, _ output_name: UnsafePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_canonicalize_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_type: gss_OID, _ output_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_channel_bindings_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_channel_bindings_t = UnsafePointer<gss_channel_bindings_struct> ``` |
| To | ``` typealias gss_channel_bindings_t = UnsafeMutablePointer<gss_channel_bindings_struct> ``` |

Modified gss_compare_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_name_t, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_compare_name(_ minor_status: UnsafePointer<OM_uint32>, _ name1_arg: gss_name_t, _ name2_arg: gss_name_t, _ name_equal: UnsafePointer<Int32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_compare_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ name1_arg: gss_name_t, _ name2_arg: gss_name_t, _ name_equal: UnsafeMutablePointer<Int32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_const_OID

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_const_OID = ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` typealias gss_const_OID = UnsafePointer<gss_OID_desc> ``` |

Modified gss_const_OID_set

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_const_OID_set = ConstUnsafePointer<gss_OID_set_desc> ``` |
| To | ``` typealias gss_const_OID_set = UnsafePointer<gss_OID_set_desc> ``` |

Modified gss_const_buffer_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_const_buffer_t = ConstUnsafePointer<gss_buffer_desc> ``` |
| To | ``` typealias gss_const_buffer_t = UnsafePointer<gss_buffer_desc> ``` |

Modified gss_const_channel_bindings_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_const_channel_bindings_t = ConstUnsafePointer<gss_channel_bindings_struct> ``` |
| To | ``` typealias gss_const_channel_bindings_t = UnsafePointer<gss_channel_bindings_struct> ``` |

Modified gss_context_time(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_context_time(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ time_rec: UnsafePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_context_time(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_create_empty_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_create_empty_buffer_set(_ minor_status: UnsafePointer<OM_uint32>, _ buffer_set: UnsafePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_create_empty_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_create_empty_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_create_empty_oid_set(_ minor_status: UnsafePointer<OM_uint32>, _ oid_set: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_create_empty_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid_set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_decapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_delete_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: UnsafePointer<gss_ctx_id_t>, _ output_token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_delete_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ output_token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_destroy_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_destroy_cred(_ min_stat: UnsafePointer<OM_uint32>, _ cred_handle: UnsafePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_destroy_cred(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_display_mech_attr(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_buffer_t, gss_buffer_t, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_display_mech_attr(_ minor_status: UnsafePointer<OM_uint32>, _ mech_attr: gss_const_OID, _ name: gss_buffer_t, _ short_desc: gss_buffer_t, _ long_desc: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_display_mech_attr(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_attr: gss_const_OID, _ name: gss_buffer_t, _ short_desc: gss_buffer_t, _ long_desc: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_display_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, UnsafeMutablePointer<gss_OID>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_display_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name: gss_name_t, _ output_name_buffer: gss_buffer_t, _ output_name_type: UnsafePointer<gss_OID>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_display_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ output_name_buffer: gss_buffer_t, _ output_name_type: UnsafeMutablePointer<gss_OID>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_display_status(UnsafeMutablePointer<OM_uint32>, OM_uint32, Int32, gss_OID, UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_display_status(_ minor_status: UnsafePointer<OM_uint32>, _ status_value: OM_uint32, _ status_type: Int32, _ mech_type: gss_OID, _ message_content: UnsafePointer<OM_uint32>, _ status_string: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_display_status(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ status_value: OM_uint32, _ status_type: Int32, _ mech_type: gss_OID, _ message_content: UnsafeMutablePointer<OM_uint32>, _ status_string: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_duplicate_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_duplicate_name(_ minor_status: UnsafePointer<OM_uint32>, _ src_name: gss_name_t, _ dest_name: UnsafePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_duplicate_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ src_name: gss_name_t, _ dest_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_encapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gss_export_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_export_cred(_ minor_status: UnsafePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_export_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_export_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_export_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name: gss_name_t, _ exported_name: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_export_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ exported_name: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_export_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_export_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: UnsafePointer<gss_ctx_id_t>, _ interprocess_token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_export_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ interprocess_token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_get_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_qop_t, gss_buffer_t, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_get_mic(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ qop_req: gss_qop_t, _ message_buffer: gss_buffer_t, _ message_token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_get_mic(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ qop_req: gss_qop_t, _ message_buffer: gss_buffer_t, _ message_token: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_import_cred(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_import_cred(_ minor_status: UnsafePointer<OM_uint32>, _ token: gss_buffer_t, _ cred_handle: UnsafePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_import_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ token: gss_buffer_t, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_import_name(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, gss_const_OID, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_import_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name_buffer: gss_buffer_t, _ input_name_type: gss_const_OID, _ output_name: UnsafePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_import_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name_buffer: gss_buffer_t, _ input_name_type: gss_const_OID, _ output_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_import_sec_context(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_ctx_id_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_import_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ interprocess_token: gss_buffer_t, _ context_handle: UnsafePointer<gss_ctx_id_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_import_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ interprocess_token: gss_buffer_t, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_indicate_mechs(_ minor_status: UnsafePointer<OM_uint32>, _ mech_set: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_indicate_mechs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_indicate_mechs_by_attrs(UnsafeMutablePointer<OM_uint32>, gss_const_OID_set, gss_const_OID_set, gss_const_OID_set, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration |
| --- | --- |
| From | ``` func gss_indicate_mechs_by_attrs(_ minor_status: UnsafePointer<OM_uint32>, _ desired_mech_attrs: gss_const_OID_set, _ except_mech_attrs: gss_const_OID_set, _ critical_mech_attrs: gss_const_OID_set, _ mechs: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_indicate_mechs_by_attrs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech_attrs: gss_const_OID_set, _ except_mech_attrs: gss_const_OID_set, _ critical_mech_attrs: gss_const_OID_set, _ mechs: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |

Modified gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, UnsafeMutablePointer<gss_ctx_id_t>, gss_name_t, gss_OID, OM_uint32, OM_uint32, gss_channel_bindings_t, gss_buffer_t, UnsafeMutablePointer<gss_OID>, gss_buffer_t, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_init_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ initiator_cred_handle: gss_cred_id_t, _ context_handle: UnsafePointer<gss_ctx_id_t>, _ target_name: gss_name_t, _ input_mech_type: gss_OID, _ req_flags: OM_uint32, _ time_req: OM_uint32, _ input_chan_bindings: gss_channel_bindings_t, _ input_token: gss_buffer_t, _ actual_mech_type: UnsafePointer<gss_OID>, _ output_token: gss_buffer_t, _ ret_flags: UnsafePointer<OM_uint32>, _ time_rec: UnsafePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_init_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ initiator_cred_handle: gss_cred_id_t, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ target_name: gss_name_t, _ input_mech_type: gss_OID, _ req_flags: OM_uint32, _ time_req: OM_uint32, _ input_chan_bindings: gss_channel_bindings_t, _ input_token: gss_buffer_t, _ actual_mech_type: UnsafeMutablePointer<gss_OID>, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_attrs_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_attrs_for_mech(_ minor_status: UnsafePointer<OM_uint32>, _ mech: gss_const_OID, _ mech_attr: UnsafePointer<gss_OID_set>, _ known_mech_attrs: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_attrs_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech: gss_const_OID, _ mech_attr: UnsafeMutablePointer<gss_OID_set>, _ known_mech_attrs: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_context(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ src_name: UnsafePointer<gss_name_t>, _ targ_name: UnsafePointer<gss_name_t>, _ lifetime_rec: UnsafePointer<OM_uint32>, _ mech_type: UnsafePointer<gss_OID>, _ ctx_flags: UnsafePointer<OM_uint32>, _ locally_initiated: UnsafePointer<Int32>, _ xopen: UnsafePointer<Int32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ src_name: UnsafeMutablePointer<gss_name_t>, _ targ_name: UnsafeMutablePointer<gss_name_t>, _ lifetime_rec: UnsafeMutablePointer<OM_uint32>, _ mech_type: UnsafeMutablePointer<gss_OID>, _ ctx_flags: UnsafeMutablePointer<OM_uint32>, _ locally_initiated: UnsafeMutablePointer<Int32>, _ xopen: UnsafeMutablePointer<Int32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_usage_t>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_cred(_ minor_status: UnsafePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ name_ret: UnsafePointer<gss_name_t>, _ lifetime: UnsafePointer<OM_uint32>, _ cred_usage: UnsafePointer<gss_cred_usage_t>, _ mechanisms: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ name_ret: UnsafeMutablePointer<gss_name_t>, _ lifetime: UnsafeMutablePointer<OM_uint32>, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>, _ mechanisms: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_cred_by_mech(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_usage_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_cred_by_mech(_ minor_status: UnsafePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ mech_type: gss_OID, _ cred_name: UnsafePointer<gss_name_t>, _ initiator_lifetime: UnsafePointer<OM_uint32>, _ acceptor_lifetime: UnsafePointer<OM_uint32>, _ cred_usage: UnsafePointer<gss_cred_usage_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_cred_by_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ mech_type: gss_OID, _ cred_name: UnsafeMutablePointer<gss_name_t>, _ initiator_lifetime: UnsafeMutablePointer<OM_uint32>, _ acceptor_lifetime: UnsafeMutablePointer<OM_uint32>, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_cred_by_oid(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_cred_by_oid(_ minor_status: UnsafePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ desired_object: gss_OID, _ data_set: UnsafePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_cred_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_mech_for_saslname(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_OID>) -> OM_uint32

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_mech_for_saslname(_ minor_status: UnsafePointer<OM_uint32>, _ sasl_mech_name: gss_buffer_t, _ mech_type: UnsafePointer<gss_OID>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_mech_for_saslname(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ sasl_mech_name: gss_buffer_t, _ mech_type: UnsafeMutablePointer<gss_OID>) -> OM_uint32 ``` |

Modified gss_inquire_mechs_for_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_mechs_for_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_types: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_mechs_for_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_types: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<gss_OID>, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name: gss_name_t, _ name_is_MN: UnsafePointer<Int32>, _ MN_mech: UnsafePointer<gss_OID>, _ attrs: UnsafePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ name_is_MN: UnsafeMutablePointer<Int32>, _ MN_mech: UnsafeMutablePointer<gss_OID>, _ attrs: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_names_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_names_for_mech(_ minor_status: UnsafePointer<OM_uint32>, _ mechanism: gss_const_OID, _ name_types: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_names_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mechanism: gss_const_OID, _ name_types: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_inquire_saslname_for_mech(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t, gss_buffer_t, gss_buffer_t) -> OM_uint32

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_saslname_for_mech(_ minor_status: UnsafePointer<OM_uint32>, _ desired_mech: gss_OID, _ sasl_mech_name: gss_buffer_t, _ mech_name: gss_buffer_t, _ mech_description: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_inquire_saslname_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech: gss_OID, _ sasl_mech_name: gss_buffer_t, _ mech_name: gss_buffer_t, _ mech_description: gss_buffer_t) -> OM_uint32 ``` |

Modified gss_inquire_sec_context_by_oid(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_inquire_sec_context_by_oid(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ desired_object: gss_OID, _ data_set: UnsafePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_inquire_sec_context_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_iov_buffer_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_iov_buffer_t = UnsafePointer<gss_iov_buffer_desc_struct> ``` |
| To | ``` typealias gss_iov_buffer_t = UnsafeMutablePointer<gss_iov_buffer_desc_struct> ``` |

Modified gss_iter_creds(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID,((gss_OID, gss_cred_id_t) -> Void)!) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_iter_creds(_ min_stat: UnsafePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ useriter: ((gss_OID, gss_cred_id_t) -> Void)!) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_iter_creds(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ useriter: ((gss_OID, gss_cred_id_t) -> Void)!) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_iter_creds_f(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void)>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_iter_creds_f(_ min_stat: UnsafePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ userctx: UnsafePointer<()>, _ useriter: CFunctionPointer<((UnsafePointer<()>, gss_OID, gss_cred_id_t) -> Void)>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_iter_creds_f(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ userctx: UnsafeMutablePointer<Void>, _ useriter: CFunctionPointer<((UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void)>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_krb5_ccache_name(UnsafeMutablePointer<OM_uint32>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_krb5_ccache_name(_ minor_status: UnsafePointer<OM_uint32>, _ name: ConstUnsafePointer<Int8>, _ out_name: UnsafePointer<ConstUnsafePointer<Int8>>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_krb5_ccache_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ name: UnsafePointer<Int8>, _ out_name: UnsafeMutablePointer<UnsafePointer<Int8>>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_krb5_export_lucid_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, OM_uint32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_krb5_export_lucid_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: UnsafePointer<gss_ctx_id_t>, _ version: OM_uint32, _ rctx: UnsafePointer<UnsafePointer<()>>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_krb5_export_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ version: OM_uint32, _ rctx: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_krb5_free_lucid_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<Void>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_krb5_free_lucid_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ c: UnsafePointer<()>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_krb5_free_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ c: UnsafeMutablePointer<Void>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_krb5_set_allowable_enctypes(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, OM_uint32, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_krb5_set_allowable_enctypes(_ minor_status: UnsafePointer<OM_uint32>, _ cred: gss_cred_id_t, _ num_enctypes: OM_uint32, _ enctypes: UnsafePointer<Int32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_krb5_set_allowable_enctypes(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred: gss_cred_id_t, _ num_enctypes: OM_uint32, _ enctypes: UnsafeMutablePointer<Int32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_oid_equal(gss_const_OID, gss_const_OID) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_oid_to_str(_ minor_status: UnsafePointer<OM_uint32>, _ oid: gss_OID, _ oid_str: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_oid_to_str(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid: gss_OID, _ oid_str: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_process_context_token(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ token_buffer: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_process_context_token(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ token_buffer: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_pseudo_random(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, Int, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_pseudo_random(_ minor_status: UnsafePointer<OM_uint32>, _ context: gss_ctx_id_t, _ prf_key: Int32, _ prf_in: gss_buffer_t, _ desired_output_len: Int, _ prf_out: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_pseudo_random(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context: gss_ctx_id_t, _ prf_key: Int32, _ prf_in: gss_buffer_t, _ desired_output_len: Int, _ prf_out: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_release_buffer(UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_release_buffer(_ minor_status: UnsafePointer<OM_uint32>, _ buffer: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_release_buffer(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_release_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_release_buffer_set(_ minor_status: UnsafePointer<OM_uint32>, _ buffer_set: UnsafePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_release_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_release_cred(_ minor_status: UnsafePointer<OM_uint32>, _ cred_handle: UnsafePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_release_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_release_name(_ minor_status: UnsafePointer<OM_uint32>, _ input_name: UnsafePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_release_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_release_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_release_oid_set(_ minor_status: UnsafePointer<OM_uint32>, _ set: UnsafePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_release_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_set_cred_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>, gss_OID, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_set_cred_option(_ minor_status: UnsafePointer<OM_uint32>, _ cred_handle: UnsafePointer<gss_cred_id_t>, _ object: gss_OID, _ value: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_set_cred_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ object: gss_OID, _ value: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_OID, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_set_sec_context_option(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: UnsafePointer<gss_ctx_id_t>, _ object: gss_OID, _ value: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_set_sec_context_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ object: gss_OID, _ value: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_status_id_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_status_id_t = UnsafePointer<OM_uint32> ``` |
| To | ``` typealias gss_status_id_t = UnsafeMutablePointer<OM_uint32> ``` |

Modified gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_test_oid_set_member(_ minor_status: UnsafePointer<OM_uint32>, _ member: gss_const_OID, _ set: gss_OID_set, _ present: UnsafePointer<Int32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_test_oid_set_member(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ member: gss_const_OID, _ set: gss_OID_set, _ present: UnsafeMutablePointer<Int32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_unwrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<gss_qop_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_unwrap(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ input_message_buffer: gss_buffer_t, _ output_message_buffer: gss_buffer_t, _ conf_state: UnsafePointer<Int32>, _ qop_state: UnsafePointer<gss_qop_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_unwrap(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ input_message_buffer: gss_buffer_t, _ output_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>, _ qop_state: UnsafeMutablePointer<gss_qop_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_userok(gss_name_t, UnsafePointer<Int8>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_userok(_ name: gss_name_t, _ user: ConstUnsafePointer<Int8>) -> Int32 ``` | OS X 10.10 |
| To | ``` func gss_userok(_ name: gss_name_t, _ user: UnsafePointer<Int8>) -> Int32 ``` | OS X 10.9 |

Modified gss_verify_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<gss_qop_t>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_verify_mic(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ message_buffer: gss_buffer_t, _ token_buffer: gss_buffer_t, _ qop_state: UnsafePointer<gss_qop_t>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_verify_mic(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ message_buffer: gss_buffer_t, _ token_buffer: gss_buffer_t, _ qop_state: UnsafeMutablePointer<gss_qop_t>) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_wrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, gss_buffer_t, UnsafeMutablePointer<Int32>, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_wrap(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ input_message_buffer: gss_buffer_t, _ conf_state: UnsafePointer<Int32>, _ output_message_buffer: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_wrap(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ input_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>, _ output_message_buffer: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gss_wrap_size_limit(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, OM_uint32, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gss_wrap_size_limit(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ req_output_size: OM_uint32, _ max_input_size: UnsafePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gss_wrap_size_limit(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ req_output_size: OM_uint32, _ max_input_size: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` | OS X 10.7 |

Modified gsskrb5_extract_authz_data_from_sec_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gsskrb5_extract_authz_data_from_sec_context(_ minor_status: UnsafePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ ad_type: Int32, _ ad_data: gss_buffer_t) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gsskrb5_extract_authz_data_from_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ ad_type: Int32, _ ad_data: gss_buffer_t) -> OM_uint32 ``` | OS X 10.7 |

Modified gsskrb5_register_acceptor_identity(UnsafePointer<Int8>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gsskrb5_register_acceptor_identity(_ identity: ConstUnsafePointer<Int8>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func gsskrb5_register_acceptor_identity(_ identity: UnsafePointer<Int8>) -> OM_uint32 ``` | OS X 10.7 |

Modified krb5_gss_register_acceptor_identity(UnsafePointer<Int8>) -> OM_uint32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func krb5_gss_register_acceptor_identity(_ identity: ConstUnsafePointer<Int8>) -> OM_uint32 ``` | OS X 10.10 |
| To | ``` func krb5_gss_register_acceptor_identity(_ identity: UnsafePointer<Int8>) -> OM_uint32 ``` | OS X 10.7 |

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
