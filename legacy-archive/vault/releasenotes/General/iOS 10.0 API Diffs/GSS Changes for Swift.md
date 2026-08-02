---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/GSS.html
archived_at: '2026-07-18T02:55:26.893757Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# GSS Changes for Swift

### GSS

Removed gss_buffer_desc_struct.init(length: Int, value: UnsafeMutablePointer<Void>)Removed [gss_buffer_set_desc_struct.init(count: Int, elements: UnsafeMutablePointer<gss_buffer_desc>)](https://developer.apple.com/documentation/gss/gss_buffer_set_desc_struct/1544026-init)Removed gss_OID_desc_struct.init(length: OM_uint32, elements: UnsafeMutablePointer<Void>)Removed [gss_OID_set_desc_struct.init(count: Int, elements: gss_OID)](https://developer.apple.com/documentation/gss/gss_oid_set_desc_struct/1544142-init)Added [gss_buffer_desc_struct.init(length: Int, value: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/gss/gss_buffer_desc_struct/2475517-init)Added [gss_buffer_set_desc_struct.init(count: Int, elements: UnsafeMutablePointer<gss_buffer_desc>!)](https://developer.apple.com/documentation/gss/gss_buffer_set_desc_struct/1544026-init)Added [gss_OID_desc_struct.init(length: OM_uint32, elements: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/gss/gss_oid_desc_struct/2475518-init)Added [gss_OID_set_desc_struct.init(count: Int, elements: gss_OID!)](https://developer.apple.com/documentation/gss/gss_oid_set_desc_struct/1544142-init)Modified [gss_buffer_desc_struct [struct]](https://developer.apple.com/documentation/gss/gss_buffer_desc_struct)

|  | Declaration |
| --- | --- |
| From | ``` struct gss_buffer_desc_struct {     var length: Int     var value: UnsafeMutablePointer<Void>     init()     init(length length: Int, value value: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct gss_buffer_desc_struct {     var length: Int     var value: UnsafeMutableRawPointer!     init()     init(length length: Int, value value: UnsafeMutableRawPointer!) } ``` |

Modified [gss_buffer_desc_struct.value](https://developer.apple.com/documentation/gss/gss_buffer_desc/1543897-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafeMutablePointer<Void> ``` |
| To | ``` var value: UnsafeMutableRawPointer! ``` |

Modified [gss_buffer_set_desc_struct [struct]](https://developer.apple.com/documentation/gss/gss_buffer_set_desc_struct)

|  | Declaration |
| --- | --- |
| From | ``` struct gss_buffer_set_desc_struct {     var count: Int     var elements: UnsafeMutablePointer<gss_buffer_desc>     init()     init(count count: Int, elements elements: UnsafeMutablePointer<gss_buffer_desc>) } ``` |
| To | ``` struct gss_buffer_set_desc_struct {     var count: Int     var elements: UnsafeMutablePointer<gss_buffer_desc>!     init()     init(count count: Int, elements elements: UnsafeMutablePointer<gss_buffer_desc>!) } ``` |

Modified [gss_buffer_set_desc_struct.elements](https://developer.apple.com/documentation/gss/gss_buffer_set_desc/1543930-elements)

|  | Declaration |
| --- | --- |
| From | ``` var elements: UnsafeMutablePointer<gss_buffer_desc> ``` |
| To | ``` var elements: UnsafeMutablePointer<gss_buffer_desc>! ``` |

Modified [gss_OID_desc_struct [struct]](https://developer.apple.com/documentation/gss/gss_oid_desc_struct)

|  | Declaration |
| --- | --- |
| From | ``` struct gss_OID_desc_struct {     var length: OM_uint32     var elements: UnsafeMutablePointer<Void>     init()     init(length length: OM_uint32, elements elements: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct gss_OID_desc_struct {     var length: OM_uint32     var elements: UnsafeMutableRawPointer!     init()     init(length length: OM_uint32, elements elements: UnsafeMutableRawPointer!) } ``` |

Modified [gss_OID_desc_struct.elements](https://developer.apple.com/documentation/gss/gss_oid_desc_struct/1544024-elements)

|  | Declaration |
| --- | --- |
| From | ``` var elements: UnsafeMutablePointer<Void> ``` |
| To | ``` var elements: UnsafeMutableRawPointer! ``` |

Modified [gss_OID_set_desc_struct [struct]](https://developer.apple.com/documentation/gss/gss_oid_set_desc_struct)

|  | Declaration |
| --- | --- |
| From | ``` struct gss_OID_set_desc_struct {     var count: Int     var elements: gss_OID     init()     init(count count: Int, elements elements: gss_OID) } ``` |
| To | ``` struct gss_OID_set_desc_struct {     var count: Int     var elements: gss_OID!     init()     init(count count: Int, elements elements: gss_OID!) } ``` |

Modified [gss_OID_set_desc_struct.elements](https://developer.apple.com/documentation/gss/gss_oid_set_desc_struct/1544029-elements)

|  | Declaration |
| --- | --- |
| From | ``` var elements: gss_OID ``` |
| To | ``` var elements: gss_OID! ``` |

Modified [gss_aapl_change_password(_: gss_name_t, _: gss_const_OID, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Declaration |
| --- | --- |
| From | ``` func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` |
| To | ``` func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32 ``` |

Modified [gss_aapl_initial_cred(_: gss_name_t, _: gss_const_OID, _: CFDictionary?, _: UnsafeMutablePointer<gss_cred_id_t>?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary?, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` |
| To | ``` func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary?, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OM_uint32 ``` |

Modified [gss_accept_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_ctx_id_t>?, _: gss_cred_id_t?, _: gss_buffer_t?, _: gss_channel_bindings_t?, _: UnsafeMutablePointer<gss_name_t?>?, _: UnsafeMutablePointer<gss_OID?>?, _: gss_buffer_t, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438493-gss_accept_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_accept_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ acceptor_cred_handle: gss_cred_id_t, _ input_token: gss_buffer_t, _ input_chan_bindings: gss_channel_bindings_t, _ src_name: UnsafeMutablePointer<gss_name_t>, _ mech_type: UnsafeMutablePointer<gss_OID>, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>, _ time_rec: UnsafeMutablePointer<OM_uint32>, _ delegated_cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` |
| To | ``` func gss_accept_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?, _ acceptor_cred_handle: gss_cred_id_t?, _ input_token: gss_buffer_t?, _ input_chan_bindings: gss_channel_bindings_t?, _ src_name: UnsafeMutablePointer<gss_name_t?>?, _ mech_type: UnsafeMutablePointer<gss_OID?>?, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?, _ delegated_cred_handle: UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32 ``` |

Modified [gss_acquire_cred(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t?, _: OM_uint32, _: gss_OID_set?, _: gss_cred_usage_t, _: UnsafeMutablePointer<gss_cred_id_t>?, _: UnsafeMutablePointer<gss_OID_set?>?, _: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438466-gss_acquire_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_acquire_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set>, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` |
| To | ``` func gss_acquire_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t?, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set?, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>?, _ actual_mechs: UnsafeMutablePointer<gss_OID_set?>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32 ``` |

Modified [gss_acquire_cred_with_password(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t, _: gss_buffer_t, _: OM_uint32, _: gss_OID_set?, _: gss_cred_usage_t, _: UnsafeMutablePointer<gss_cred_id_t>?, _: UnsafeMutablePointer<gss_OID_set?>?, _: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438426-gss_acquire_cred_with_password)

|  | Declaration |
| --- | --- |
| From | ``` func gss_acquire_cred_with_password(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t, _ password: gss_buffer_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set>, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` |
| To | ``` func gss_acquire_cred_with_password(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_name: gss_name_t, _ password: gss_buffer_t, _ time_req: OM_uint32, _ desired_mechs: gss_OID_set?, _ cred_usage: gss_cred_usage_t, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>?, _ actual_mechs: UnsafeMutablePointer<gss_OID_set?>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32 ``` |

Modified [gss_add_cred(_: UnsafeMutablePointer<OM_uint32>, _: gss_cred_id_t?, _: gss_name_t?, _: gss_OID?, _: gss_cred_usage_t, _: OM_uint32, _: OM_uint32, _: UnsafeMutablePointer<gss_cred_id_t>?, _: UnsafeMutablePointer<gss_OID_set?>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438473-gss_add_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_add_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_cred_handle: gss_cred_id_t, _ desired_name: gss_name_t, _ desired_mech: gss_OID, _ cred_usage: gss_cred_usage_t, _ initiator_time_req: OM_uint32, _ acceptor_time_req: OM_uint32, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ actual_mechs: UnsafeMutablePointer<gss_OID_set>, _ initiator_time_rec: UnsafeMutablePointer<OM_uint32>, _ acceptor_time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` |
| To | ``` func gss_add_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_cred_handle: gss_cred_id_t?, _ desired_name: gss_name_t?, _ desired_mech: gss_OID?, _ cred_usage: gss_cred_usage_t, _ initiator_time_req: OM_uint32, _ acceptor_time_req: OM_uint32, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>?, _ actual_mechs: UnsafeMutablePointer<gss_OID_set?>?, _ initiator_time_rec: UnsafeMutablePointer<OM_uint32>?, _ acceptor_time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32 ``` |

Modified [gss_auth_identity_t](https://developer.apple.com/documentation/gss/gss_auth_identity_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_auth_identity_t = COpaquePointer ``` |
| To | ``` typealias gss_auth_identity_t = OpaquePointer ``` |

Modified [gss_canonicalize_name(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t, _: gss_OID, _: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438494-gss_canonicalize_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_canonicalize_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_type: gss_OID, _ output_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` |
| To | ``` func gss_canonicalize_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_type: gss_OID, _ output_name: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32 ``` |

Modified [gss_const_cred_id_t](https://developer.apple.com/documentation/gss/gss_const_cred_id_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_const_cred_id_t = COpaquePointer ``` |
| To | ``` typealias gss_const_cred_id_t = OpaquePointer ``` |

Modified [gss_const_name_t](https://developer.apple.com/documentation/gss/gss_const_name_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_const_name_t = COpaquePointer ``` |
| To | ``` typealias gss_const_name_t = OpaquePointer ``` |

Modified [gss_create_empty_buffer_set(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438537-gss_create_empty_buffer_set)

|  | Declaration |
| --- | --- |
| From | ``` func gss_create_empty_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` |
| To | ``` func gss_create_empty_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32 ``` |

Modified [gss_create_empty_oid_set(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438489-gss_create_empty_oid_set)

|  | Declaration |
| --- | --- |
| From | ``` func gss_create_empty_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid_set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_create_empty_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ oid_set: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32 ``` |

Modified [gss_cred_id_t](https://developer.apple.com/documentation/gss/gss_cred_id_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_cred_id_t = COpaquePointer ``` |
| To | ``` typealias gss_cred_id_t = OpaquePointer ``` |

Modified [gss_ctx_id_t](https://developer.apple.com/documentation/gss/gss_ctx_id_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_ctx_id_t = COpaquePointer ``` |
| To | ``` typealias gss_ctx_id_t = OpaquePointer ``` |

Modified [gss_delete_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_ctx_id_t>?, _: gss_buffer_t?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438435-gss_delete_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_delete_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ output_token: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_delete_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?, _ output_token: gss_buffer_t?) -> OM_uint32 ``` |

Modified [gss_destroy_cred(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_cred_id_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438521-gss_destroy_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_destroy_cred(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` |
| To | ``` func gss_destroy_cred(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>?) -> OM_uint32 ``` |

Modified [gss_display_mech_attr(_: UnsafeMutablePointer<OM_uint32>, _: gss_const_OID, _: gss_buffer_t?, _: gss_buffer_t?, _: gss_buffer_t?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438475-gss_display_mech_attr)

|  | Declaration |
| --- | --- |
| From | ``` func gss_display_mech_attr(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_attr: gss_const_OID, _ name: gss_buffer_t, _ short_desc: gss_buffer_t, _ long_desc: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_display_mech_attr(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_attr: gss_const_OID, _ name: gss_buffer_t?, _ short_desc: gss_buffer_t?, _ long_desc: gss_buffer_t?) -> OM_uint32 ``` |

Modified [gss_display_name(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t, _: gss_buffer_t, _: UnsafeMutablePointer<gss_OID?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438464-gss_display_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_display_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ output_name_buffer: gss_buffer_t, _ output_name_type: UnsafeMutablePointer<gss_OID>) -> OM_uint32 ``` |
| To | ``` func gss_display_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ output_name_buffer: gss_buffer_t, _ output_name_type: UnsafeMutablePointer<gss_OID?>?) -> OM_uint32 ``` |

Modified [gss_display_status(_: UnsafeMutablePointer<OM_uint32>, _: OM_uint32, _: Int32, _: gss_OID?, _: UnsafeMutablePointer<OM_uint32>, _: gss_buffer_t) -> OM_uint32](https://developer.apple.com/documentation/gss/1438535-gss_display_status)

|  | Declaration |
| --- | --- |
| From | ``` func gss_display_status(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ status_value: OM_uint32, _ status_type: Int32, _ mech_type: gss_OID, _ message_content: UnsafeMutablePointer<OM_uint32>, _ status_string: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_display_status(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ status_value: OM_uint32, _ status_type: Int32, _ mech_type: gss_OID?, _ message_content: UnsafeMutablePointer<OM_uint32>, _ status_string: gss_buffer_t) -> OM_uint32 ``` |

Modified [gss_duplicate_name(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t, _: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438418-gss_duplicate_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_duplicate_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ src_name: gss_name_t, _ dest_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` |
| To | ``` func gss_duplicate_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ src_name: gss_name_t, _ dest_name: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32 ``` |

Modified [gss_export_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_ctx_id_t>?, _: gss_buffer_t?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438449-gss_export_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_export_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ interprocess_token: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_export_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?, _ interprocess_token: gss_buffer_t?) -> OM_uint32 ``` |

Modified [gss_import_cred(_: UnsafeMutablePointer<OM_uint32>, _: gss_buffer_t, _: UnsafeMutablePointer<gss_cred_id_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438510-gss_import_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_import_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ token: gss_buffer_t, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` |
| To | ``` func gss_import_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ token: gss_buffer_t, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>?) -> OM_uint32 ``` |

Modified [gss_import_name(_: UnsafeMutablePointer<OM_uint32>, _: gss_buffer_t, _: gss_const_OID?, _: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438453-gss_import_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_import_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name_buffer: gss_buffer_t, _ input_name_type: gss_const_OID, _ output_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` |
| To | ``` func gss_import_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name_buffer: gss_buffer_t, _ input_name_type: gss_const_OID?, _ output_name: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32 ``` |

Modified [gss_import_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: gss_buffer_t, _: UnsafeMutablePointer<gss_ctx_id_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438484-gss_import_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_import_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ interprocess_token: gss_buffer_t, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>) -> OM_uint32 ``` |
| To | ``` func gss_import_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ interprocess_token: gss_buffer_t, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?) -> OM_uint32 ``` |

Modified [gss_indicate_mechs(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438424-gss_indicate_mechs)

|  | Declaration |
| --- | --- |
| From | ``` func gss_indicate_mechs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_indicate_mechs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_set: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32 ``` |

Modified [gss_indicate_mechs_by_attrs(_: UnsafeMutablePointer<OM_uint32>, _: gss_const_OID_set?, _: gss_const_OID_set?, _: gss_const_OID_set?, _: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438413-gss_indicate_mechs_by_attrs)

|  | Declaration |
| --- | --- |
| From | ``` func gss_indicate_mechs_by_attrs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech_attrs: gss_const_OID_set, _ except_mech_attrs: gss_const_OID_set, _ critical_mech_attrs: gss_const_OID_set, _ mechs: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_indicate_mechs_by_attrs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech_attrs: gss_const_OID_set?, _ except_mech_attrs: gss_const_OID_set?, _ critical_mech_attrs: gss_const_OID_set?, _ mechs: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32 ``` |

Modified [gss_init_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: gss_cred_id_t?, _: UnsafeMutablePointer<gss_ctx_id_t>?, _: gss_name_t, _: gss_OID?, _: OM_uint32, _: OM_uint32, _: gss_channel_bindings_t?, _: gss_buffer_t?, _: UnsafeMutablePointer<gss_OID?>?, _: gss_buffer_t, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438476-gss_init_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_init_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ initiator_cred_handle: gss_cred_id_t, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ target_name: gss_name_t, _ input_mech_type: gss_OID, _ req_flags: OM_uint32, _ time_req: OM_uint32, _ input_chan_bindings: gss_channel_bindings_t, _ input_token: gss_buffer_t, _ actual_mech_type: UnsafeMutablePointer<gss_OID>, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>, _ time_rec: UnsafeMutablePointer<OM_uint32>) -> OM_uint32 ``` |
| To | ``` func gss_init_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ initiator_cred_handle: gss_cred_id_t?, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?, _ target_name: gss_name_t, _ input_mech_type: gss_OID?, _ req_flags: OM_uint32, _ time_req: OM_uint32, _ input_chan_bindings: gss_channel_bindings_t?, _ input_token: gss_buffer_t?, _ actual_mech_type: UnsafeMutablePointer<gss_OID?>?, _ output_token: gss_buffer_t, _ ret_flags: UnsafeMutablePointer<OM_uint32>?, _ time_rec: UnsafeMutablePointer<OM_uint32>?) -> OM_uint32 ``` |

Modified [gss_inquire_attrs_for_mech(_: UnsafeMutablePointer<OM_uint32>, _: gss_const_OID, _: UnsafeMutablePointer<gss_OID_set?>?, _: UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438417-gss_inquire_attrs_for_mech)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_attrs_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech: gss_const_OID, _ mech_attr: UnsafeMutablePointer<gss_OID_set>, _ known_mech_attrs: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_attrs_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech: gss_const_OID, _ mech_attr: UnsafeMutablePointer<gss_OID_set?>?, _ known_mech_attrs: UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32 ``` |

Modified [gss_inquire_context(_: UnsafeMutablePointer<OM_uint32>, _: gss_ctx_id_t, _: UnsafeMutablePointer<gss_name_t?>?, _: UnsafeMutablePointer<gss_name_t?>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<gss_OID?>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<Int32>?, _: UnsafeMutablePointer<Int32>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438458-gss_inquire_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ src_name: UnsafeMutablePointer<gss_name_t>, _ targ_name: UnsafeMutablePointer<gss_name_t>, _ lifetime_rec: UnsafeMutablePointer<OM_uint32>, _ mech_type: UnsafeMutablePointer<gss_OID>, _ ctx_flags: UnsafeMutablePointer<OM_uint32>, _ locally_initiated: UnsafeMutablePointer<Int32>, _ xopen: UnsafeMutablePointer<Int32>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ src_name: UnsafeMutablePointer<gss_name_t?>?, _ targ_name: UnsafeMutablePointer<gss_name_t?>?, _ lifetime_rec: UnsafeMutablePointer<OM_uint32>?, _ mech_type: UnsafeMutablePointer<gss_OID?>?, _ ctx_flags: UnsafeMutablePointer<OM_uint32>?, _ locally_initiated: UnsafeMutablePointer<Int32>?, _ xopen: UnsafeMutablePointer<Int32>?) -> OM_uint32 ``` |

Modified [gss_inquire_cred(_: UnsafeMutablePointer<OM_uint32>, _: gss_cred_id_t?, _: UnsafeMutablePointer<gss_name_t?>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<gss_cred_usage_t>?, _: UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438531-gss_inquire_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ name_ret: UnsafeMutablePointer<gss_name_t>, _ lifetime: UnsafeMutablePointer<OM_uint32>, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>, _ mechanisms: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t?, _ name_ret: UnsafeMutablePointer<gss_name_t?>?, _ lifetime: UnsafeMutablePointer<OM_uint32>?, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>?, _ mechanisms: UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32 ``` |

Modified [gss_inquire_cred_by_mech(_: UnsafeMutablePointer<OM_uint32>, _: gss_cred_id_t?, _: gss_OID, _: UnsafeMutablePointer<gss_name_t?>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<OM_uint32>?, _: UnsafeMutablePointer<gss_cred_usage_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438518-gss_inquire_cred_by_mech)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_cred_by_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ mech_type: gss_OID, _ cred_name: UnsafeMutablePointer<gss_name_t>, _ initiator_lifetime: UnsafeMutablePointer<OM_uint32>, _ acceptor_lifetime: UnsafeMutablePointer<OM_uint32>, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_cred_by_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t?, _ mech_type: gss_OID, _ cred_name: UnsafeMutablePointer<gss_name_t?>?, _ initiator_lifetime: UnsafeMutablePointer<OM_uint32>?, _ acceptor_lifetime: UnsafeMutablePointer<OM_uint32>?, _ cred_usage: UnsafeMutablePointer<gss_cred_usage_t>?) -> OM_uint32 ``` |

Modified [gss_inquire_cred_by_oid(_: UnsafeMutablePointer<OM_uint32>, _: gss_cred_id_t, _: gss_OID, _: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438504-gss_inquire_cred_by_oid)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_cred_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_cred_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: gss_cred_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32 ``` |

Modified [gss_inquire_mech_for_saslname(_: UnsafeMutablePointer<OM_uint32>, _: gss_buffer_t?, _: UnsafeMutablePointer<gss_OID?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438514-gss_inquire_mech_for_saslname)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_mech_for_saslname(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ sasl_mech_name: gss_buffer_t, _ mech_type: UnsafeMutablePointer<gss_OID>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_mech_for_saslname(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ sasl_mech_name: gss_buffer_t?, _ mech_type: UnsafeMutablePointer<gss_OID?>?) -> OM_uint32 ``` |

Modified [gss_inquire_mechs_for_name(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t, _: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438481-gss_inquire_mechs_for_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_mechs_for_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_types: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_mechs_for_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ mech_types: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32 ``` |

Modified [gss_inquire_name(_: UnsafeMutablePointer<OM_uint32>, _: gss_name_t, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<gss_OID?>?, _: UnsafeMutablePointer<gss_buffer_set_t?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438422-gss_inquire_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ name_is_MN: UnsafeMutablePointer<Int32>, _ MN_mech: UnsafeMutablePointer<gss_OID>, _ attrs: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: gss_name_t, _ name_is_MN: UnsafeMutablePointer<Int32>, _ MN_mech: UnsafeMutablePointer<gss_OID?>?, _ attrs: UnsafeMutablePointer<gss_buffer_set_t?>?) -> OM_uint32 ``` |

Modified [gss_inquire_names_for_mech(_: UnsafeMutablePointer<OM_uint32>, _: gss_const_OID, _: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438523-gss_inquire_names_for_mech)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_names_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mechanism: gss_const_OID, _ name_types: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_names_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mechanism: gss_const_OID, _ name_types: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32 ``` |

Modified [gss_inquire_saslname_for_mech(_: UnsafeMutablePointer<OM_uint32>, _: gss_OID, _: gss_buffer_t?, _: gss_buffer_t?, _: gss_buffer_t?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438445-gss_inquire_saslname_for_mech)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_saslname_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech: gss_OID, _ sasl_mech_name: gss_buffer_t, _ mech_name: gss_buffer_t, _ mech_description: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_inquire_saslname_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech: gss_OID, _ sasl_mech_name: gss_buffer_t?, _ mech_name: gss_buffer_t?, _ mech_description: gss_buffer_t?) -> OM_uint32 ``` |

Modified [gss_inquire_sec_context_by_oid(_: UnsafeMutablePointer<OM_uint32>, _: gss_ctx_id_t, _: gss_OID, _: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438525-gss_inquire_sec_context_by_oid)

|  | Declaration |
| --- | --- |
| From | ``` func gss_inquire_sec_context_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` |
| To | ``` func gss_inquire_sec_context_by_oid(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ desired_object: gss_OID, _ data_set: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32 ``` |

Modified [gss_iter_creds(_: UnsafeMutablePointer<OM_uint32>, _: OM_uint32, _: gss_const_OID?, _: (gss_OID?, gss_cred_id_t?) -> Swift.Void) -> OM_uint32](https://developer.apple.com/documentation/gss/1438515-gss_iter_creds)

|  | Declaration |
| --- | --- |
| From | ``` func gss_iter_creds(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ useriter: (gss_OID, gss_cred_id_t) -> Void) -> OM_uint32 ``` |
| To | ``` func gss_iter_creds(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID?, _ useriter: @escaping (gss_OID?, gss_cred_id_t?) -> Swift.Void) -> OM_uint32 ``` |

Modified [gss_iter_creds_f(_: UnsafeMutablePointer<OM_uint32>, _: OM_uint32, _: gss_const_OID?, _: UnsafeMutableRawPointer?, _: (UnsafeMutableRawPointer?, gss_OID?, gss_cred_id_t?) -> Swift.Void) -> OM_uint32](https://developer.apple.com/documentation/gss/1438438-gss_iter_creds_f)

|  | Declaration |
| --- | --- |
| From | ``` func gss_iter_creds_f(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ userctx: UnsafeMutablePointer<Void>, _ useriter: (UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void) -> OM_uint32 ``` |
| To | ``` func gss_iter_creds_f(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID?, _ userctx: UnsafeMutableRawPointer?, _ useriter: @escaping (UnsafeMutableRawPointer?, gss_OID?, gss_cred_id_t?) -> Swift.Void) -> OM_uint32 ``` |

Modified [gss_krb5_ccache_name(_: UnsafeMutablePointer<OM_uint32>, _: UnsafePointer<Int8>?, _: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438472-gss_krb5_ccache_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_krb5_ccache_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ name: UnsafePointer<Int8>, _ out_name: UnsafeMutablePointer<UnsafePointer<Int8>>) -> OM_uint32 ``` |
| To | ``` func gss_krb5_ccache_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ name: UnsafePointer<Int8>?, _ out_name: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> OM_uint32 ``` |

Modified [gss_krb5_export_lucid_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_ctx_id_t>?, _: OM_uint32, _: UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438433-gss_krb5_export_lucid_sec_contex)

|  | Declaration |
| --- | --- |
| From | ``` func gss_krb5_export_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ version: OM_uint32, _ rctx: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OM_uint32 ``` |
| To | ``` func gss_krb5_export_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?, _ version: OM_uint32, _ rctx: UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OM_uint32 ``` |

Modified [gss_krb5_free_lucid_sec_context(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutableRawPointer) -> OM_uint32](https://developer.apple.com/documentation/gss/1438483-gss_krb5_free_lucid_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` func gss_krb5_free_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ c: UnsafeMutablePointer<Void>) -> OM_uint32 ``` |
| To | ``` func gss_krb5_free_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ c: UnsafeMutableRawPointer) -> OM_uint32 ``` |

Modified [gss_name_t](https://developer.apple.com/documentation/gss/gss_name_t)

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_name_t = COpaquePointer ``` |
| To | ``` typealias gss_name_t = OpaquePointer ``` |

Modified [gss_oid_equal(_: gss_const_OID?, _: gss_const_OID?) -> Int32](https://developer.apple.com/documentation/gss/1438498-gss_oid_equal)

|  | Declaration |
| --- | --- |
| From | ``` func gss_oid_equal(_ a: gss_const_OID, _ b: gss_const_OID) -> Int32 ``` |
| To | ``` func gss_oid_equal(_ a: gss_const_OID?, _ b: gss_const_OID?) -> Int32 ``` |

Modified [gss_release_buffer_set(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438428-gss_release_buffer_set)

|  | Declaration |
| --- | --- |
| From | ``` func gss_release_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32 ``` |
| To | ``` func gss_release_buffer_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ buffer_set: UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32 ``` |

Modified [gss_release_cred(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_cred_id_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438461-gss_release_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_release_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32 ``` |
| To | ``` func gss_release_cred(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>?) -> OM_uint32 ``` |

Modified [gss_release_name(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438451-gss_release_name)

|  | Declaration |
| --- | --- |
| From | ``` func gss_release_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: UnsafeMutablePointer<gss_name_t>) -> OM_uint32 ``` |
| To | ``` func gss_release_name(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ input_name: UnsafeMutablePointer<gss_name_t>?) -> OM_uint32 ``` |

Modified [gss_release_oid_set(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438480-gss_release_oid_set)

|  | Declaration |
| --- | --- |
| From | ``` func gss_release_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ set: UnsafeMutablePointer<gss_OID_set>) -> OM_uint32 ``` |
| To | ``` func gss_release_oid_set(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ set: UnsafeMutablePointer<gss_OID_set>?) -> OM_uint32 ``` |

Modified [gss_set_cred_option(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_cred_id_t?>?, _: gss_OID, _: gss_buffer_t?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438513-gss_set_cred_option)

|  | Declaration |
| --- | --- |
| From | ``` func gss_set_cred_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ object: gss_OID, _ value: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_set_cred_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ cred_handle: UnsafeMutablePointer<gss_cred_id_t?>?, _ object: gss_OID, _ value: gss_buffer_t?) -> OM_uint32 ``` |

Modified [gss_set_sec_context_option(_: UnsafeMutablePointer<OM_uint32>, _: UnsafeMutablePointer<gss_ctx_id_t>?, _: gss_OID, _: gss_buffer_t?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438491-gss_set_sec_context_option)

|  | Declaration |
| --- | --- |
| From | ``` func gss_set_sec_context_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>, _ object: gss_OID, _ value: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_set_sec_context_option(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t>?, _ object: gss_OID, _ value: gss_buffer_t?) -> OM_uint32 ``` |

Modified [gss_unwrap(_: UnsafeMutablePointer<OM_uint32>, _: gss_ctx_id_t, _: gss_buffer_t, _: gss_buffer_t, _: UnsafeMutablePointer<Int32>?, _: UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438520-gss_unwrap)

|  | Declaration |
| --- | --- |
| From | ``` func gss_unwrap(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ input_message_buffer: gss_buffer_t, _ output_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>, _ qop_state: UnsafeMutablePointer<gss_qop_t>) -> OM_uint32 ``` |
| To | ``` func gss_unwrap(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ input_message_buffer: gss_buffer_t, _ output_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>?, _ qop_state: UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32 ``` |

Modified [gss_verify_mic(_: UnsafeMutablePointer<OM_uint32>, _: gss_ctx_id_t, _: gss_buffer_t, _: gss_buffer_t, _: UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32](https://developer.apple.com/documentation/gss/1438447-gss_verify_mic)

|  | Declaration |
| --- | --- |
| From | ``` func gss_verify_mic(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ message_buffer: gss_buffer_t, _ token_buffer: gss_buffer_t, _ qop_state: UnsafeMutablePointer<gss_qop_t>) -> OM_uint32 ``` |
| To | ``` func gss_verify_mic(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ message_buffer: gss_buffer_t, _ token_buffer: gss_buffer_t, _ qop_state: UnsafeMutablePointer<gss_qop_t>?) -> OM_uint32 ``` |

Modified [gss_wrap(_: UnsafeMutablePointer<OM_uint32>, _: gss_ctx_id_t, _: Int32, _: gss_qop_t, _: gss_buffer_t, _: UnsafeMutablePointer<Int32>?, _: gss_buffer_t) -> OM_uint32](https://developer.apple.com/documentation/gss/1438527-gss_wrap)

|  | Declaration |
| --- | --- |
| From | ``` func gss_wrap(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ input_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>, _ output_message_buffer: gss_buffer_t) -> OM_uint32 ``` |
| To | ``` func gss_wrap(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: gss_ctx_id_t, _ conf_req_flag: Int32, _ qop_req: gss_qop_t, _ input_message_buffer: gss_buffer_t, _ conf_state: UnsafeMutablePointer<Int32>?, _ output_message_buffer: gss_buffer_t) -> OM_uint32 ``` |

Modified [GSSCreateCredentialFromUUID(_: CFUUID) -> gss_cred_id_t?](https://developer.apple.com/documentation/gss/1411915-gsscreatecredentialfromuuid)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCreateCredentialFromUUID(_ uuid: CFUUID) -> gss_cred_id_t ``` |
| To | ``` func GSSCreateCredentialFromUUID(_ uuid: CFUUID) -> gss_cred_id_t? ``` |

Modified [GSSCreateName(_: CFTypeRef, _: gss_const_OID, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t?](https://developer.apple.com/documentation/gss/1411907-gsscreatename)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCreateName(_ name: AnyObject, _ name_type: gss_const_OID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t ``` |
| To | ``` func GSSCreateName(_ name: CFTypeRef, _ name_type: gss_const_OID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> gss_name_t? ``` |

Modified [GSSCredentialCopyName(_: gss_cred_id_t) -> gss_name_t?](https://developer.apple.com/documentation/gss/1411911-gsscredentialcopyname)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCredentialCopyName(_ cred: gss_cred_id_t) -> gss_name_t ``` |
| To | ``` func GSSCredentialCopyName(_ cred: gss_cred_id_t) -> gss_name_t? ``` |

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
