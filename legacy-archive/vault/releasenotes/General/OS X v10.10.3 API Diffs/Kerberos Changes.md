---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Kerberos.html
archived_at: '2026-07-18T02:52:32.979451Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Kerberos Changes

## Kerberos

Removed SALT_TYPE_AFS_LENGTHRemoved SALT_TYPE_NO_LENGTHRemoved VALID_UINT_BITSAdded apple_gss_krb5_authdata_if_relevant_key.init()Added apple_gss_krb5_authdata_if_relevant_key.init(type: OM_uint32, length: OM_uint32, data: UnsafeMutablePointer<Void>)Added cc_ccache_d.init()Added cc_ccache_d.init(functions: UnsafePointer<cc_ccache_f>, vector_functions: UnsafePointer<cc_ccache_f>)Added cc_ccache_f.init()Added cc_ccache_f.init(release: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, destroy: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, set_default: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, get_credentials_version: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>, get_name: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>, get_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>, set_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<Int8>) -> cc_int32)>, store_credentials: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_credentials_union>) -> cc_int32)>, remove_credentials: CFunctionPointer<((cc_ccache_t, cc_credentials_t) -> cc_int32)>, new_credentials_iterator: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)>, move: CFunctionPointer<((cc_ccache_t, cc_ccache_t) -> cc_int32)>, lock: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_uint32) -> cc_int32)>, unlock: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, get_last_default_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, get_change_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, compare: CFunctionPointer<((cc_ccache_t, cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>, get_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, set_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_time_t) -> cc_int32)>, clear_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32) -> cc_int32)>, wait_for_change: CFunctionPointer<((cc_ccache_t) -> cc_int32)>)Added cc_ccache_iterator_d.init()Added cc_ccache_iterator_d.init(functions: UnsafePointer<cc_ccache_iterator_f>, vector_functions: UnsafePointer<cc_ccache_iterator_f>)Added cc_ccache_iterator_f.init()Added cc_ccache_iterator_f.init(release: CFunctionPointer<((cc_ccache_iterator_t) -> cc_int32)>, next: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, clone: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)>)Added cc_context_d.init()Added cc_context_d.init(functions: UnsafePointer<cc_context_f>, vector_functions: UnsafePointer<cc_context_f>)Added cc_context_f.init()Added cc_context_f.init(release: CFunctionPointer<((cc_context_t) -> cc_int32)>, get_change_time: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, get_default_ccache_name: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>, open_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, open_default_ccache: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, create_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, create_default_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, create_new_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, new_ccache_iterator: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)>, lock: CFunctionPointer<((cc_context_t, cc_uint32, cc_uint32) -> cc_int32)>, unlock: CFunctionPointer<((cc_context_t) -> cc_int32)>, compare: CFunctionPointer<((cc_context_t, cc_context_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>, wait_for_change: CFunctionPointer<((cc_context_t) -> cc_int32)>)Added cc_credentials_d.init()Added cc_credentials_d.init(data: UnsafePointer<cc_credentials_union>, functions: UnsafePointer<cc_credentials_f>, otherFunctions: UnsafePointer<cc_credentials_f>)Added cc_credentials_f.init()Added cc_credentials_f.init(release: CFunctionPointer<((cc_credentials_t) -> cc_int32)>, compare: CFunctionPointer<((cc_credentials_t, cc_credentials_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>)Added cc_credentials_iterator_d.init()Added cc_credentials_iterator_d.init(functions: UnsafePointer<cc_credentials_iterator_f>, vector_functions: UnsafePointer<cc_credentials_iterator_f>)Added cc_credentials_iterator_f.init()Added cc_credentials_iterator_f.init(release: CFunctionPointer<((cc_credentials_iterator_t) -> cc_int32)>, next: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_t>) -> cc_int32)>, clone: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)>)Added cc_credentials_union.init()Added cc_credentials_v4_t.init()Added cc_credentials_v5_t.init()Added cc_credentials_v5_t.init(client: UnsafeMutablePointer<Int8>, server: UnsafeMutablePointer<Int8>, keyblock: cc_data, authtime: cc_time_t, starttime: cc_time_t, endtime: cc_time_t, renew_till: cc_time_t, is_skey: cc_uint32, ticket_flags: cc_uint32, addresses: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>>, ticket: cc_data, second_ticket: cc_data, authdata: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>>)Added cc_data.init()Added cc_data.init(type: cc_uint32, length: cc_uint32, data: UnsafeMutablePointer<Void>)Added cc_string_d.init()Added cc_string_d.init(data: UnsafePointer<Int8>, functions: UnsafePointer<cc_string_f>, vector_functions: UnsafePointer<cc_string_f>)Added cc_string_f.init()Added cc_string_f.init(release: CFunctionPointer<((cc_string_t) -> cc_int32)>)Added error_table.init()Added error_table.init(messages: UnsafePointer<UnsafePointer<Int8>>, base: Int32, count: Int32)Added gss_OID_desc_struct.init()Added gss_OID_desc_struct.init(length: OM_uint32, elements: UnsafeMutablePointer<Void>)Added gss_OID_set_desc_struct.init()Added gss_OID_set_desc_struct.init(count: Int, elements: gss_OID)Added gss_buffer_desc_struct.init()Added gss_buffer_desc_struct.init(length: Int, value: UnsafeMutablePointer<Void>)Added gss_channel_bindings_struct.init()Added gss_channel_bindings_struct.init(initiator_addrtype: OM_uint32, initiator_address: gss_buffer_desc, acceptor_addrtype: OM_uint32, acceptor_address: gss_buffer_desc, application_data: gss_buffer_desc)Added gss_krb5_cfx_keydata.init()Added gss_krb5_cfx_keydata.init(have_acceptor_subkey: OM_uint32, ctx_key: gss_krb5_lucid_key_t, acceptor_subkey: gss_krb5_lucid_key_t)Added gss_krb5_lucid_context_v1.init()Added gss_krb5_lucid_context_v1.init(version: OM_uint32, initiate: OM_uint32, endtime: OM_uint32, send_seq: gss_uint64, recv_seq: gss_uint64, protocol: OM_uint32, rfc1964_kd: gss_krb5_rfc1964_keydata_t, cfx_kd: gss_krb5_cfx_keydata_t)Added gss_krb5_lucid_context_version.init()Added gss_krb5_lucid_context_version.init(version: OM_uint32)Added gss_krb5_lucid_key.init()Added gss_krb5_lucid_key.init(type: OM_uint32, length: OM_uint32, data: UnsafeMutablePointer<Void>)Added gss_krb5_rfc1964_keydata.init()Added gss_krb5_rfc1964_keydata.init(sign_alg: OM_uint32, seal_alg: OM_uint32, ctx_key: gss_krb5_lucid_key_t)Added krb5_keytab_entry_st.init()Added krb5_keytab_entry_st.init(magic: krb5_magic, principal: krb5_principal, timestamp: krb5_timestamp, vno: krb5_kvno, key: krb5_keyblock)Added krb5_principal_data.init()Added krb5_principal_data.init(magic: krb5_magic, realm: krb5_data, data: UnsafeMutablePointer<krb5_data>, length: krb5_int32, type: krb5_int32)Added krb5_replay_data.init()Added krb5_replay_data.init(timestamp: krb5_timestamp, usec: krb5_int32, seq: krb5_ui_4)Added kCCAPICCacheChangedNotificationAdded kCCAPICacheCollectionChangedNotificationModified apple_gss_krb5_authdata_if_relevant_key [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct apple_gss_krb5_authdata_if_relevant_key {     var type: OM_uint32     var length: OM_uint32     var data: UnsafePointer<()> } ``` |
| To | ``` struct apple_gss_krb5_authdata_if_relevant_key {     var type: OM_uint32     var length: OM_uint32     var data: UnsafeMutablePointer<Void>     init()     init(type type: OM_uint32, length length: OM_uint32, data data: UnsafeMutablePointer<Void>) } ``` |

Modified apple_gss_krb5_authdata_if_relevant_key.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<()> ``` |
| To | ``` var data: UnsafeMutablePointer<Void> ``` |

Modified cc_ccache_d [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_ccache_d {     var functions: ConstUnsafePointer<cc_ccache_f>     var vector_functions: ConstUnsafePointer<cc_ccache_f> } ``` |
| To | ``` struct cc_ccache_d {     var functions: UnsafePointer<cc_ccache_f>     var vector_functions: UnsafePointer<cc_ccache_f>     init()     init(functions functions: UnsafePointer<cc_ccache_f>, vector_functions vector_functions: UnsafePointer<cc_ccache_f>) } ``` |

Modified cc_ccache_d.functions

|  | Declaration |
| --- | --- |
| From | ``` var functions: ConstUnsafePointer<cc_ccache_f> ``` |
| To | ``` var functions: UnsafePointer<cc_ccache_f> ``` |

Modified cc_ccache_d.vector_functions

|  | Declaration |
| --- | --- |
| From | ``` var vector_functions: ConstUnsafePointer<cc_ccache_f> ``` |
| To | ``` var vector_functions: UnsafePointer<cc_ccache_f> ``` |

Modified cc_ccache_f [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_ccache_f {     var release: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var destroy: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var set_default: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var get_credentials_version: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_uint32>) -> cc_int32)>     var get_name: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_string_t>) -> cc_int32)>     var get_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<cc_string_t>) -> cc_int32)>     var set_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, ConstUnsafePointer<Int8>) -> cc_int32)>     var store_credentials: CFunctionPointer<((cc_ccache_t, ConstUnsafePointer<cc_credentials_union>) -> cc_int32)>     var remove_credentials: CFunctionPointer<((cc_ccache_t, cc_credentials_t) -> cc_int32)>     var new_credentials_iterator: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_credentials_iterator_t>) -> cc_int32)>     var move: CFunctionPointer<((cc_ccache_t, cc_ccache_t) -> cc_int32)>     var lock: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_uint32) -> cc_int32)>     var unlock: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var get_last_default_time: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_time_t>) -> cc_int32)>     var get_change_time: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_time_t>) -> cc_int32)>     var compare: CFunctionPointer<((cc_ccache_t, cc_ccache_t, UnsafePointer<cc_uint32>) -> cc_int32)>     var get_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<cc_time_t>) -> cc_int32)>     var set_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_time_t) -> cc_int32)>     var clear_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32) -> cc_int32)>     var wait_for_change: CFunctionPointer<((cc_ccache_t) -> cc_int32)> } ``` |
| To | ``` struct cc_ccache_f {     var release: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var destroy: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var set_default: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var get_credentials_version: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>     var get_name: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>     var get_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>     var set_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<Int8>) -> cc_int32)>     var store_credentials: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_credentials_union>) -> cc_int32)>     var remove_credentials: CFunctionPointer<((cc_ccache_t, cc_credentials_t) -> cc_int32)>     var new_credentials_iterator: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)>     var move: CFunctionPointer<((cc_ccache_t, cc_ccache_t) -> cc_int32)>     var lock: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_uint32) -> cc_int32)>     var unlock: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     var get_last_default_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>     var get_change_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>     var compare: CFunctionPointer<((cc_ccache_t, cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>     var get_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>     var set_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_time_t) -> cc_int32)>     var clear_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32) -> cc_int32)>     var wait_for_change: CFunctionPointer<((cc_ccache_t) -> cc_int32)>     init()     init(release release: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, destroy destroy: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, set_default set_default: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, get_credentials_version get_credentials_version: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>, get_name get_name: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>, get_principal get_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>, set_principal set_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<Int8>) -> cc_int32)>, store_credentials store_credentials: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_credentials_union>) -> cc_int32)>, remove_credentials remove_credentials: CFunctionPointer<((cc_ccache_t, cc_credentials_t) -> cc_int32)>, new_credentials_iterator new_credentials_iterator: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)>, move move: CFunctionPointer<((cc_ccache_t, cc_ccache_t) -> cc_int32)>, lock lock: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_uint32) -> cc_int32)>, unlock unlock: CFunctionPointer<((cc_ccache_t) -> cc_int32)>, get_last_default_time get_last_default_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, get_change_time get_change_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, compare compare: CFunctionPointer<((cc_ccache_t, cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>, get_kdc_time_offset get_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, set_kdc_time_offset set_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, cc_time_t) -> cc_int32)>, clear_kdc_time_offset clear_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32) -> cc_int32)>, wait_for_change wait_for_change: CFunctionPointer<((cc_ccache_t) -> cc_int32)>) } ``` |

Modified cc_ccache_f.compare

|  | Declaration |
| --- | --- |
| From | ``` var compare: CFunctionPointer<((cc_ccache_t, cc_ccache_t, UnsafePointer<cc_uint32>) -> cc_int32)> ``` |
| To | ``` var compare: CFunctionPointer<((cc_ccache_t, cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)> ``` |

Modified cc_ccache_f.get_change_time

|  | Declaration |
| --- | --- |
| From | ``` var get_change_time: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_time_t>) -> cc_int32)> ``` |
| To | ``` var get_change_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)> ``` |

Modified cc_ccache_f.get_credentials_version

|  | Declaration |
| --- | --- |
| From | ``` var get_credentials_version: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_uint32>) -> cc_int32)> ``` |
| To | ``` var get_credentials_version: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)> ``` |

Modified cc_ccache_f.get_kdc_time_offset

|  | Declaration |
| --- | --- |
| From | ``` var get_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<cc_time_t>) -> cc_int32)> ``` |
| To | ``` var get_kdc_time_offset: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_time_t>) -> cc_int32)> ``` |

Modified cc_ccache_f.get_last_default_time

|  | Declaration |
| --- | --- |
| From | ``` var get_last_default_time: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_time_t>) -> cc_int32)> ``` |
| To | ``` var get_last_default_time: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)> ``` |

Modified cc_ccache_f.get_name

|  | Declaration |
| --- | --- |
| From | ``` var get_name: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_string_t>) -> cc_int32)> ``` |
| To | ``` var get_name: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)> ``` |

Modified cc_ccache_f.get_principal

|  | Declaration |
| --- | --- |
| From | ``` var get_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<cc_string_t>) -> cc_int32)> ``` |
| To | ``` var get_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafeMutablePointer<cc_string_t>) -> cc_int32)> ``` |

Modified cc_ccache_f.new_credentials_iterator

|  | Declaration |
| --- | --- |
| From | ``` var new_credentials_iterator: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_credentials_iterator_t>) -> cc_int32)> ``` |
| To | ``` var new_credentials_iterator: CFunctionPointer<((cc_ccache_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)> ``` |

Modified cc_ccache_f.set_principal

|  | Declaration |
| --- | --- |
| From | ``` var set_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, ConstUnsafePointer<Int8>) -> cc_int32)> ``` |
| To | ``` var set_principal: CFunctionPointer<((cc_ccache_t, cc_uint32, UnsafePointer<Int8>) -> cc_int32)> ``` |

Modified cc_ccache_f.store_credentials

|  | Declaration |
| --- | --- |
| From | ``` var store_credentials: CFunctionPointer<((cc_ccache_t, ConstUnsafePointer<cc_credentials_union>) -> cc_int32)> ``` |
| To | ``` var store_credentials: CFunctionPointer<((cc_ccache_t, UnsafePointer<cc_credentials_union>) -> cc_int32)> ``` |

Modified cc_ccache_iterator_d [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_ccache_iterator_d {     var functions: ConstUnsafePointer<cc_ccache_iterator_f>     var vector_functions: ConstUnsafePointer<cc_ccache_iterator_f> } ``` |
| To | ``` struct cc_ccache_iterator_d {     var functions: UnsafePointer<cc_ccache_iterator_f>     var vector_functions: UnsafePointer<cc_ccache_iterator_f>     init()     init(functions functions: UnsafePointer<cc_ccache_iterator_f>, vector_functions vector_functions: UnsafePointer<cc_ccache_iterator_f>) } ``` |

Modified cc_ccache_iterator_d.functions

|  | Declaration |
| --- | --- |
| From | ``` var functions: ConstUnsafePointer<cc_ccache_iterator_f> ``` |
| To | ``` var functions: UnsafePointer<cc_ccache_iterator_f> ``` |

Modified cc_ccache_iterator_d.vector_functions

|  | Declaration |
| --- | --- |
| From | ``` var vector_functions: ConstUnsafePointer<cc_ccache_iterator_f> ``` |
| To | ``` var vector_functions: UnsafePointer<cc_ccache_iterator_f> ``` |

Modified cc_ccache_iterator_f [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_ccache_iterator_f {     var release: CFunctionPointer<((cc_ccache_iterator_t) -> cc_int32)>     var next: CFunctionPointer<((cc_ccache_iterator_t, UnsafePointer<cc_ccache_t>) -> cc_int32)>     var clone: CFunctionPointer<((cc_ccache_iterator_t, UnsafePointer<cc_ccache_iterator_t>) -> cc_int32)> } ``` |
| To | ``` struct cc_ccache_iterator_f {     var release: CFunctionPointer<((cc_ccache_iterator_t) -> cc_int32)>     var next: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>     var clone: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)>     init()     init(release release: CFunctionPointer<((cc_ccache_iterator_t) -> cc_int32)>, next next: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, clone clone: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)>) } ``` |

Modified cc_ccache_iterator_f.clone

|  | Declaration |
| --- | --- |
| From | ``` var clone: CFunctionPointer<((cc_ccache_iterator_t, UnsafePointer<cc_ccache_iterator_t>) -> cc_int32)> ``` |
| To | ``` var clone: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)> ``` |

Modified cc_ccache_iterator_f.next

|  | Declaration |
| --- | --- |
| From | ``` var next: CFunctionPointer<((cc_ccache_iterator_t, UnsafePointer<cc_ccache_t>) -> cc_int32)> ``` |
| To | ``` var next: CFunctionPointer<((cc_ccache_iterator_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)> ``` |

Modified cc_context_d [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_context_d {     var functions: ConstUnsafePointer<cc_context_f>     var vector_functions: ConstUnsafePointer<cc_context_f> } ``` |
| To | ``` struct cc_context_d {     var functions: UnsafePointer<cc_context_f>     var vector_functions: UnsafePointer<cc_context_f>     init()     init(functions functions: UnsafePointer<cc_context_f>, vector_functions vector_functions: UnsafePointer<cc_context_f>) } ``` |

Modified cc_context_d.functions

|  | Declaration |
| --- | --- |
| From | ``` var functions: ConstUnsafePointer<cc_context_f> ``` |
| To | ``` var functions: UnsafePointer<cc_context_f> ``` |

Modified cc_context_d.vector_functions

|  | Declaration |
| --- | --- |
| From | ``` var vector_functions: ConstUnsafePointer<cc_context_f> ``` |
| To | ``` var vector_functions: UnsafePointer<cc_context_f> ``` |

Modified cc_context_f [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_context_f {     var release: CFunctionPointer<((cc_context_t) -> cc_int32)>     var get_change_time: CFunctionPointer<((cc_context_t, UnsafePointer<cc_time_t>) -> cc_int32)>     var get_default_ccache_name: CFunctionPointer<((cc_context_t, UnsafePointer<cc_string_t>) -> cc_int32)>     var open_ccache: CFunctionPointer<((cc_context_t, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)>     var open_default_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<cc_ccache_t>) -> cc_int32)>     var create_ccache: CFunctionPointer<((cc_context_t, ConstUnsafePointer<Int8>, cc_uint32, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)>     var create_default_ccache: CFunctionPointer<((cc_context_t, cc_uint32, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)>     var create_new_ccache: CFunctionPointer<((cc_context_t, cc_uint32, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)>     var new_ccache_iterator: CFunctionPointer<((cc_context_t, UnsafePointer<cc_ccache_iterator_t>) -> cc_int32)>     var lock: CFunctionPointer<((cc_context_t, cc_uint32, cc_uint32) -> cc_int32)>     var unlock: CFunctionPointer<((cc_context_t) -> cc_int32)>     var compare: CFunctionPointer<((cc_context_t, cc_context_t, UnsafePointer<cc_uint32>) -> cc_int32)>     var wait_for_change: CFunctionPointer<((cc_context_t) -> cc_int32)> } ``` |
| To | ``` struct cc_context_f {     var release: CFunctionPointer<((cc_context_t) -> cc_int32)>     var get_change_time: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>     var get_default_ccache_name: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>     var open_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>     var open_default_ccache: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>     var create_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>     var create_default_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>     var create_new_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>     var new_ccache_iterator: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)>     var lock: CFunctionPointer<((cc_context_t, cc_uint32, cc_uint32) -> cc_int32)>     var unlock: CFunctionPointer<((cc_context_t) -> cc_int32)>     var compare: CFunctionPointer<((cc_context_t, cc_context_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>     var wait_for_change: CFunctionPointer<((cc_context_t) -> cc_int32)>     init()     init(release release: CFunctionPointer<((cc_context_t) -> cc_int32)>, get_change_time get_change_time: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)>, get_default_ccache_name get_default_ccache_name: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)>, open_ccache open_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, open_default_ccache open_default_ccache: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, create_ccache create_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, create_default_ccache create_default_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, create_new_ccache create_new_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)>, new_ccache_iterator new_ccache_iterator: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)>, lock lock: CFunctionPointer<((cc_context_t, cc_uint32, cc_uint32) -> cc_int32)>, unlock unlock: CFunctionPointer<((cc_context_t) -> cc_int32)>, compare compare: CFunctionPointer<((cc_context_t, cc_context_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>, wait_for_change wait_for_change: CFunctionPointer<((cc_context_t) -> cc_int32)>) } ``` |

Modified cc_context_f.compare

|  | Declaration |
| --- | --- |
| From | ``` var compare: CFunctionPointer<((cc_context_t, cc_context_t, UnsafePointer<cc_uint32>) -> cc_int32)> ``` |
| To | ``` var compare: CFunctionPointer<((cc_context_t, cc_context_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)> ``` |

Modified cc_context_f.create_ccache

|  | Declaration |
| --- | --- |
| From | ``` var create_ccache: CFunctionPointer<((cc_context_t, ConstUnsafePointer<Int8>, cc_uint32, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)> ``` |
| To | ``` var create_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)> ``` |

Modified cc_context_f.create_default_ccache

|  | Declaration |
| --- | --- |
| From | ``` var create_default_ccache: CFunctionPointer<((cc_context_t, cc_uint32, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)> ``` |
| To | ``` var create_default_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)> ``` |

Modified cc_context_f.create_new_ccache

|  | Declaration |
| --- | --- |
| From | ``` var create_new_ccache: CFunctionPointer<((cc_context_t, cc_uint32, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)> ``` |
| To | ``` var create_new_ccache: CFunctionPointer<((cc_context_t, cc_uint32, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)> ``` |

Modified cc_context_f.get_change_time

|  | Declaration |
| --- | --- |
| From | ``` var get_change_time: CFunctionPointer<((cc_context_t, UnsafePointer<cc_time_t>) -> cc_int32)> ``` |
| To | ``` var get_change_time: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_time_t>) -> cc_int32)> ``` |

Modified cc_context_f.get_default_ccache_name

|  | Declaration |
| --- | --- |
| From | ``` var get_default_ccache_name: CFunctionPointer<((cc_context_t, UnsafePointer<cc_string_t>) -> cc_int32)> ``` |
| To | ``` var get_default_ccache_name: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_string_t>) -> cc_int32)> ``` |

Modified cc_context_f.new_ccache_iterator

|  | Declaration |
| --- | --- |
| From | ``` var new_ccache_iterator: CFunctionPointer<((cc_context_t, UnsafePointer<cc_ccache_iterator_t>) -> cc_int32)> ``` |
| To | ``` var new_ccache_iterator: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_iterator_t>) -> cc_int32)> ``` |

Modified cc_context_f.open_ccache

|  | Declaration |
| --- | --- |
| From | ``` var open_ccache: CFunctionPointer<((cc_context_t, ConstUnsafePointer<Int8>, UnsafePointer<cc_ccache_t>) -> cc_int32)> ``` |
| To | ``` var open_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<Int8>, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)> ``` |

Modified cc_context_f.open_default_ccache

|  | Declaration |
| --- | --- |
| From | ``` var open_default_ccache: CFunctionPointer<((cc_context_t, UnsafePointer<cc_ccache_t>) -> cc_int32)> ``` |
| To | ``` var open_default_ccache: CFunctionPointer<((cc_context_t, UnsafeMutablePointer<cc_ccache_t>) -> cc_int32)> ``` |

Modified cc_credentials_d [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_credentials_d {     var data: ConstUnsafePointer<cc_credentials_union>     var functions: ConstUnsafePointer<cc_credentials_f>     var otherFunctions: ConstUnsafePointer<cc_credentials_f> } ``` |
| To | ``` struct cc_credentials_d {     var data: UnsafePointer<cc_credentials_union>     var functions: UnsafePointer<cc_credentials_f>     var otherFunctions: UnsafePointer<cc_credentials_f>     init()     init(data data: UnsafePointer<cc_credentials_union>, functions functions: UnsafePointer<cc_credentials_f>, otherFunctions otherFunctions: UnsafePointer<cc_credentials_f>) } ``` |

Modified cc_credentials_d.data

|  | Declaration |
| --- | --- |
| From | ``` var data: ConstUnsafePointer<cc_credentials_union> ``` |
| To | ``` var data: UnsafePointer<cc_credentials_union> ``` |

Modified cc_credentials_d.functions

|  | Declaration |
| --- | --- |
| From | ``` var functions: ConstUnsafePointer<cc_credentials_f> ``` |
| To | ``` var functions: UnsafePointer<cc_credentials_f> ``` |

Modified cc_credentials_d.otherFunctions

|  | Declaration |
| --- | --- |
| From | ``` var otherFunctions: ConstUnsafePointer<cc_credentials_f> ``` |
| To | ``` var otherFunctions: UnsafePointer<cc_credentials_f> ``` |

Modified cc_credentials_f [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_credentials_f {     var release: CFunctionPointer<((cc_credentials_t) -> cc_int32)>     var compare: CFunctionPointer<((cc_credentials_t, cc_credentials_t, UnsafePointer<cc_uint32>) -> cc_int32)> } ``` |
| To | ``` struct cc_credentials_f {     var release: CFunctionPointer<((cc_credentials_t) -> cc_int32)>     var compare: CFunctionPointer<((cc_credentials_t, cc_credentials_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>     init()     init(release release: CFunctionPointer<((cc_credentials_t) -> cc_int32)>, compare compare: CFunctionPointer<((cc_credentials_t, cc_credentials_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)>) } ``` |

Modified cc_credentials_f.compare

|  | Declaration |
| --- | --- |
| From | ``` var compare: CFunctionPointer<((cc_credentials_t, cc_credentials_t, UnsafePointer<cc_uint32>) -> cc_int32)> ``` |
| To | ``` var compare: CFunctionPointer<((cc_credentials_t, cc_credentials_t, UnsafeMutablePointer<cc_uint32>) -> cc_int32)> ``` |

Modified cc_credentials_iterator_d [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_credentials_iterator_d {     var functions: ConstUnsafePointer<cc_credentials_iterator_f>     var vector_functions: ConstUnsafePointer<cc_credentials_iterator_f> } ``` |
| To | ``` struct cc_credentials_iterator_d {     var functions: UnsafePointer<cc_credentials_iterator_f>     var vector_functions: UnsafePointer<cc_credentials_iterator_f>     init()     init(functions functions: UnsafePointer<cc_credentials_iterator_f>, vector_functions vector_functions: UnsafePointer<cc_credentials_iterator_f>) } ``` |

Modified cc_credentials_iterator_d.functions

|  | Declaration |
| --- | --- |
| From | ``` var functions: ConstUnsafePointer<cc_credentials_iterator_f> ``` |
| To | ``` var functions: UnsafePointer<cc_credentials_iterator_f> ``` |

Modified cc_credentials_iterator_d.vector_functions

|  | Declaration |
| --- | --- |
| From | ``` var vector_functions: ConstUnsafePointer<cc_credentials_iterator_f> ``` |
| To | ``` var vector_functions: UnsafePointer<cc_credentials_iterator_f> ``` |

Modified cc_credentials_iterator_f [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_credentials_iterator_f {     var release: CFunctionPointer<((cc_credentials_iterator_t) -> cc_int32)>     var next: CFunctionPointer<((cc_credentials_iterator_t, UnsafePointer<cc_credentials_t>) -> cc_int32)>     var clone: CFunctionPointer<((cc_credentials_iterator_t, UnsafePointer<cc_credentials_iterator_t>) -> cc_int32)> } ``` |
| To | ``` struct cc_credentials_iterator_f {     var release: CFunctionPointer<((cc_credentials_iterator_t) -> cc_int32)>     var next: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_t>) -> cc_int32)>     var clone: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)>     init()     init(release release: CFunctionPointer<((cc_credentials_iterator_t) -> cc_int32)>, next next: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_t>) -> cc_int32)>, clone clone: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)>) } ``` |

Modified cc_credentials_iterator_f.clone

|  | Declaration |
| --- | --- |
| From | ``` var clone: CFunctionPointer<((cc_credentials_iterator_t, UnsafePointer<cc_credentials_iterator_t>) -> cc_int32)> ``` |
| To | ``` var clone: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_iterator_t>) -> cc_int32)> ``` |

Modified cc_credentials_iterator_f.next

|  | Declaration |
| --- | --- |
| From | ``` var next: CFunctionPointer<((cc_credentials_iterator_t, UnsafePointer<cc_credentials_t>) -> cc_int32)> ``` |
| To | ``` var next: CFunctionPointer<((cc_credentials_iterator_t, UnsafeMutablePointer<cc_credentials_t>) -> cc_int32)> ``` |

Modified cc_credentials_union [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_credentials_union {     var version: cc_uint32 } ``` |
| To | ``` struct cc_credentials_union {     var version: cc_uint32     init() } ``` |

Modified cc_credentials_v5_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_credentials_v5_t {     var client: UnsafePointer<Int8>     var server: UnsafePointer<Int8>     var keyblock: cc_data     var authtime: cc_time_t     var starttime: cc_time_t     var endtime: cc_time_t     var renew_till: cc_time_t     var is_skey: cc_uint32     var ticket_flags: cc_uint32     var addresses: UnsafePointer<UnsafePointer<cc_data>>     var ticket: cc_data     var second_ticket: cc_data     var authdata: UnsafePointer<UnsafePointer<cc_data>> } ``` |
| To | ``` struct cc_credentials_v5_t {     var client: UnsafeMutablePointer<Int8>     var server: UnsafeMutablePointer<Int8>     var keyblock: cc_data     var authtime: cc_time_t     var starttime: cc_time_t     var endtime: cc_time_t     var renew_till: cc_time_t     var is_skey: cc_uint32     var ticket_flags: cc_uint32     var addresses: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>>     var ticket: cc_data     var second_ticket: cc_data     var authdata: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>>     init()     init(client client: UnsafeMutablePointer<Int8>, server server: UnsafeMutablePointer<Int8>, keyblock keyblock: cc_data, authtime authtime: cc_time_t, starttime starttime: cc_time_t, endtime endtime: cc_time_t, renew_till renew_till: cc_time_t, is_skey is_skey: cc_uint32, ticket_flags ticket_flags: cc_uint32, addresses addresses: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>>, ticket ticket: cc_data, second_ticket second_ticket: cc_data, authdata authdata: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>>) } ``` |

Modified cc_credentials_v5_t.addresses

|  | Declaration |
| --- | --- |
| From | ``` var addresses: UnsafePointer<UnsafePointer<cc_data>> ``` |
| To | ``` var addresses: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>> ``` |

Modified cc_credentials_v5_t.authdata

|  | Declaration |
| --- | --- |
| From | ``` var authdata: UnsafePointer<UnsafePointer<cc_data>> ``` |
| To | ``` var authdata: UnsafeMutablePointer<UnsafeMutablePointer<cc_data>> ``` |

Modified cc_credentials_v5_t.client

|  | Declaration |
| --- | --- |
| From | ``` var client: UnsafePointer<Int8> ``` |
| To | ``` var client: UnsafeMutablePointer<Int8> ``` |

Modified cc_credentials_v5_t.server

|  | Declaration |
| --- | --- |
| From | ``` var server: UnsafePointer<Int8> ``` |
| To | ``` var server: UnsafeMutablePointer<Int8> ``` |

Modified cc_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_data {     var type: cc_uint32     var length: cc_uint32     var data: UnsafePointer<()> } ``` |
| To | ``` struct cc_data {     var type: cc_uint32     var length: cc_uint32     var data: UnsafeMutablePointer<Void>     init()     init(type type: cc_uint32, length length: cc_uint32, data data: UnsafeMutablePointer<Void>) } ``` |

Modified cc_data.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<()> ``` |
| To | ``` var data: UnsafeMutablePointer<Void> ``` |

Modified cc_string_d [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_string_d {     var data: ConstUnsafePointer<Int8>     var functions: ConstUnsafePointer<cc_string_f>     var vector_functions: ConstUnsafePointer<cc_string_f> } ``` |
| To | ``` struct cc_string_d {     var data: UnsafePointer<Int8>     var functions: UnsafePointer<cc_string_f>     var vector_functions: UnsafePointer<cc_string_f>     init()     init(data data: UnsafePointer<Int8>, functions functions: UnsafePointer<cc_string_f>, vector_functions vector_functions: UnsafePointer<cc_string_f>) } ``` |

Modified cc_string_d.data

|  | Declaration |
| --- | --- |
| From | ``` var data: ConstUnsafePointer<Int8> ``` |
| To | ``` var data: UnsafePointer<Int8> ``` |

Modified cc_string_d.functions

|  | Declaration |
| --- | --- |
| From | ``` var functions: ConstUnsafePointer<cc_string_f> ``` |
| To | ``` var functions: UnsafePointer<cc_string_f> ``` |

Modified cc_string_d.vector_functions

|  | Declaration |
| --- | --- |
| From | ``` var vector_functions: ConstUnsafePointer<cc_string_f> ``` |
| To | ``` var vector_functions: UnsafePointer<cc_string_f> ``` |

Modified cc_string_f [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cc_string_f {     var release: CFunctionPointer<((cc_string_t) -> cc_int32)> } ``` |
| To | ``` struct cc_string_f {     var release: CFunctionPointer<((cc_string_t) -> cc_int32)>     init()     init(release release: CFunctionPointer<((cc_string_t) -> cc_int32)>) } ``` |

Modified error_table [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct error_table {     var messages: ConstUnsafePointer<ConstUnsafePointer<Int8>>     var base: Int32     var count: Int32 } ``` |
| To | ``` struct error_table {     var messages: UnsafePointer<UnsafePointer<Int8>>     var base: Int32     var count: Int32     init()     init(messages messages: UnsafePointer<UnsafePointer<Int8>>, base base: Int32, count count: Int32) } ``` |

Modified error_table.messages

|  | Declaration |
| --- | --- |
| From | ``` var messages: ConstUnsafePointer<ConstUnsafePointer<Int8>> ``` |
| To | ``` var messages: UnsafePointer<UnsafePointer<Int8>> ``` |

Modified gss_OID_desc_struct [struct]

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

Modified gss_channel_bindings_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_channel_bindings_struct {     var initiator_addrtype: OM_uint32     var initiator_address: gss_buffer_desc     var acceptor_addrtype: OM_uint32     var acceptor_address: gss_buffer_desc     var application_data: gss_buffer_desc } ``` |
| To | ``` struct gss_channel_bindings_struct {     var initiator_addrtype: OM_uint32     var initiator_address: gss_buffer_desc     var acceptor_addrtype: OM_uint32     var acceptor_address: gss_buffer_desc     var application_data: gss_buffer_desc     init()     init(initiator_addrtype initiator_addrtype: OM_uint32, initiator_address initiator_address: gss_buffer_desc, acceptor_addrtype acceptor_addrtype: OM_uint32, acceptor_address acceptor_address: gss_buffer_desc, application_data application_data: gss_buffer_desc) } ``` |

Modified gss_krb5_cfx_keydata [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_krb5_cfx_keydata {     var have_acceptor_subkey: OM_uint32     var ctx_key: gss_krb5_lucid_key_t     var acceptor_subkey: gss_krb5_lucid_key_t } ``` |
| To | ``` struct gss_krb5_cfx_keydata {     var have_acceptor_subkey: OM_uint32     var ctx_key: gss_krb5_lucid_key_t     var acceptor_subkey: gss_krb5_lucid_key_t     init()     init(have_acceptor_subkey have_acceptor_subkey: OM_uint32, ctx_key ctx_key: gss_krb5_lucid_key_t, acceptor_subkey acceptor_subkey: gss_krb5_lucid_key_t) } ``` |

Modified gss_krb5_lucid_context_v1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_krb5_lucid_context_v1 {     var version: OM_uint32     var initiate: OM_uint32     var endtime: OM_uint32     var send_seq: gss_uint64     var recv_seq: gss_uint64     var `protocol`: OM_uint32     var rfc1964_kd: gss_krb5_rfc1964_keydata_t     var cfx_kd: gss_krb5_cfx_keydata_t } ``` |
| To | ``` struct gss_krb5_lucid_context_v1 {     var version: OM_uint32     var initiate: OM_uint32     var endtime: OM_uint32     var send_seq: gss_uint64     var recv_seq: gss_uint64     var `protocol`: OM_uint32     var rfc1964_kd: gss_krb5_rfc1964_keydata_t     var cfx_kd: gss_krb5_cfx_keydata_t     init()     init(version version: OM_uint32, initiate initiate: OM_uint32, endtime endtime: OM_uint32, send_seq send_seq: gss_uint64, recv_seq recv_seq: gss_uint64, `protocol` `protocol`: OM_uint32, rfc1964_kd rfc1964_kd: gss_krb5_rfc1964_keydata_t, cfx_kd cfx_kd: gss_krb5_cfx_keydata_t) } ``` |

Modified gss_krb5_lucid_context_version [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_krb5_lucid_context_version {     var version: OM_uint32 } ``` |
| To | ``` struct gss_krb5_lucid_context_version {     var version: OM_uint32     init()     init(version version: OM_uint32) } ``` |

Modified gss_krb5_lucid_key [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_krb5_lucid_key {     var type: OM_uint32     var length: OM_uint32     var data: UnsafePointer<()> } ``` |
| To | ``` struct gss_krb5_lucid_key {     var type: OM_uint32     var length: OM_uint32     var data: UnsafeMutablePointer<Void>     init()     init(type type: OM_uint32, length length: OM_uint32, data data: UnsafeMutablePointer<Void>) } ``` |

Modified gss_krb5_lucid_key.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<()> ``` |
| To | ``` var data: UnsafeMutablePointer<Void> ``` |

Modified gss_krb5_rfc1964_keydata [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_krb5_rfc1964_keydata {     var sign_alg: OM_uint32     var seal_alg: OM_uint32     var ctx_key: gss_krb5_lucid_key_t } ``` |
| To | ``` struct gss_krb5_rfc1964_keydata {     var sign_alg: OM_uint32     var seal_alg: OM_uint32     var ctx_key: gss_krb5_lucid_key_t     init()     init(sign_alg sign_alg: OM_uint32, seal_alg seal_alg: OM_uint32, ctx_key ctx_key: gss_krb5_lucid_key_t) } ``` |

Modified krb5_keytab_entry_st [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct krb5_keytab_entry_st {     var magic: krb5_magic     var principal: krb5_principal     var timestamp: krb5_timestamp     var vno: krb5_kvno     var key: krb5_keyblock } ``` |
| To | ``` struct krb5_keytab_entry_st {     var magic: krb5_magic     var principal: krb5_principal     var timestamp: krb5_timestamp     var vno: krb5_kvno     var key: krb5_keyblock     init()     init(magic magic: krb5_magic, principal principal: krb5_principal, timestamp timestamp: krb5_timestamp, vno vno: krb5_kvno, key key: krb5_keyblock) } ``` |

Modified krb5_principal_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct krb5_principal_data {     var magic: krb5_magic     var realm: krb5_data     var data: UnsafePointer<krb5_data>     var length: krb5_int32     var type: krb5_int32 } ``` |
| To | ``` struct krb5_principal_data {     var magic: krb5_magic     var realm: krb5_data     var data: UnsafeMutablePointer<krb5_data>     var length: krb5_int32     var type: krb5_int32     init()     init(magic magic: krb5_magic, realm realm: krb5_data, data data: UnsafeMutablePointer<krb5_data>, length length: krb5_int32, type type: krb5_int32) } ``` |

Modified krb5_principal_data.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<krb5_data> ``` |
| To | ``` var data: UnsafeMutablePointer<krb5_data> ``` |

Modified krb5_replay_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct krb5_replay_data {     var timestamp: krb5_timestamp     var usec: krb5_int32     var seq: krb5_ui_4 } ``` |
| To | ``` struct krb5_replay_data {     var timestamp: krb5_timestamp     var usec: krb5_int32     var seq: krb5_ui_4     init()     init(timestamp timestamp: krb5_timestamp, usec usec: krb5_int32, seq seq: krb5_ui_4) } ``` |

Modified GSS_KRB5_NT_PRINCIPAL_NAME

|  | Declaration |
| --- | --- |
| From | ``` let GSS_KRB5_NT_PRINCIPAL_NAME: ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` let GSS_KRB5_NT_PRINCIPAL_NAME: UnsafePointer<gss_OID_desc> ``` |

Modified add_error_table(UnsafePointer<error_table>) -> errcode_t

|  | Declaration |
| --- | --- |
| From | ``` func add_error_table(_ et: ConstUnsafePointer<error_table>) -> errcode_t ``` |
| To | ``` func add_error_table(_ et: UnsafePointer<error_table>) -> errcode_t ``` |

Modified cc_ccache_iterator_t

|  | Declaration |
| --- | --- |
| From | ``` typealias cc_ccache_iterator_t = UnsafePointer<cc_ccache_iterator_d> ``` |
| To | ``` typealias cc_ccache_iterator_t = UnsafeMutablePointer<cc_ccache_iterator_d> ``` |

Modified cc_ccache_t

|  | Declaration |
| --- | --- |
| From | ``` typealias cc_ccache_t = UnsafePointer<cc_ccache_d> ``` |
| To | ``` typealias cc_ccache_t = UnsafeMutablePointer<cc_ccache_d> ``` |

Modified cc_context_t

|  | Declaration |
| --- | --- |
| From | ``` typealias cc_context_t = UnsafePointer<cc_context_d> ``` |
| To | ``` typealias cc_context_t = UnsafeMutablePointer<cc_context_d> ``` |

Modified cc_credentials_iterator_t

|  | Declaration |
| --- | --- |
| From | ``` typealias cc_credentials_iterator_t = UnsafePointer<cc_credentials_iterator_d> ``` |
| To | ``` typealias cc_credentials_iterator_t = UnsafeMutablePointer<cc_credentials_iterator_d> ``` |

Modified cc_credentials_t

|  | Declaration |
| --- | --- |
| From | ``` typealias cc_credentials_t = UnsafePointer<cc_credentials_d> ``` |
| To | ``` typealias cc_credentials_t = UnsafeMutablePointer<cc_credentials_d> ``` |

Modified cc_string_t

|  | Declaration |
| --- | --- |
| From | ``` typealias cc_string_t = UnsafePointer<cc_string_d> ``` |
| To | ``` typealias cc_string_t = UnsafeMutablePointer<cc_string_d> ``` |

Modified com_err_handler_t

|  | Declaration |
| --- | --- |
| From | ``` typealias com_err_handler_t = CFunctionPointer<((ConstUnsafePointer<Int8>, errcode_t, ConstUnsafePointer<Int8>, CVaListPointer) -> Void)> ``` |
| To | ``` typealias com_err_handler_t = CFunctionPointer<((UnsafePointer<Int8>, errcode_t, UnsafePointer<Int8>, CVaListPointer) -> Void)> ``` |

Modified com_err_va(UnsafePointer<Int8>, errcode_t, UnsafePointer<Int8>, CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` func com_err_va(_ progname: ConstUnsafePointer<Int8>, _ code: errcode_t, _ format: ConstUnsafePointer<Int8>, _ args: CVaListPointer) ``` |
| To | ``` func com_err_va(_ progname: UnsafePointer<Int8>, _ code: errcode_t, _ format: UnsafePointer<Int8>, _ args: CVaListPointer) ``` |

Modified const_profile_filespec_list_t

|  | Declaration |
| --- | --- |
| From | ``` typealias const_profile_filespec_list_t = ConstUnsafePointer<Int8> ``` |
| To | ``` typealias const_profile_filespec_list_t = UnsafePointer<Int8> ``` |

Modified const_profile_filespec_t

|  | Declaration |
| --- | --- |
| From | ``` typealias const_profile_filespec_t = ConstUnsafePointer<Int8> ``` |
| To | ``` typealias const_profile_filespec_t = UnsafePointer<Int8> ``` |

Modified error_manager(errcode_t) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func error_manager(_ code: errcode_t) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func error_manager(_ code: errcode_t) -> UnsafePointer<Int8> ``` |

Modified error_message(errcode_t) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func error_message(_ code: errcode_t) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func error_message(_ code: errcode_t) -> UnsafePointer<Int8> ``` |

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

Modified gss_buffer_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_buffer_t = UnsafePointer<gss_buffer_desc_struct> ``` |
| To | ``` typealias gss_buffer_t = UnsafeMutablePointer<gss_buffer_desc_struct> ``` |

Modified gss_channel_bindings_t

|  | Declaration |
| --- | --- |
| From | ``` typealias gss_channel_bindings_t = UnsafePointer<gss_channel_bindings_struct> ``` |
| To | ``` typealias gss_channel_bindings_t = UnsafeMutablePointer<gss_channel_bindings_struct> ``` |

Modified gss_mech_krb5

|  | Declaration |
| --- | --- |
| From | ``` let gss_mech_krb5: ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` let gss_mech_krb5: UnsafePointer<gss_OID_desc> ``` |

Modified gss_mech_krb5_old

|  | Declaration |
| --- | --- |
| From | ``` let gss_mech_krb5_old: ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` let gss_mech_krb5_old: UnsafePointer<gss_OID_desc> ``` |

Modified gss_mech_krb5_wrong

|  | Declaration |
| --- | --- |
| From | ``` let gss_mech_krb5_wrong: ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` let gss_mech_krb5_wrong: UnsafePointer<gss_OID_desc> ``` |

Modified gss_mech_set_krb5

|  | Declaration |
| --- | --- |
| From | ``` let gss_mech_set_krb5: ConstUnsafePointer<gss_OID_set_desc> ``` |
| To | ``` let gss_mech_set_krb5: UnsafePointer<gss_OID_set_desc> ``` |

Modified gss_mech_set_krb5_both

|  | Declaration |
| --- | --- |
| From | ``` let gss_mech_set_krb5_both: ConstUnsafePointer<gss_OID_set_desc> ``` |
| To | ``` let gss_mech_set_krb5_both: UnsafePointer<gss_OID_set_desc> ``` |

Modified gss_mech_set_krb5_old

|  | Declaration |
| --- | --- |
| From | ``` let gss_mech_set_krb5_old: ConstUnsafePointer<gss_OID_set_desc> ``` |
| To | ``` let gss_mech_set_krb5_old: UnsafePointer<gss_OID_set_desc> ``` |

Modified gss_nt_krb5_name

|  | Declaration |
| --- | --- |
| From | ``` let gss_nt_krb5_name: ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` let gss_nt_krb5_name: UnsafePointer<gss_OID_desc> ``` |

Modified gss_nt_krb5_principal

|  | Declaration |
| --- | --- |
| From | ``` let gss_nt_krb5_principal: ConstUnsafePointer<gss_OID_desc> ``` |
| To | ``` let gss_nt_krb5_principal: UnsafePointer<gss_OID_desc> ``` |

Modified krb5_const_pointer

|  | Declaration |
| --- | --- |
| From | ``` typealias krb5_const_pointer = ConstUnsafePointer<()> ``` |
| To | ``` typealias krb5_const_pointer = UnsafePointer<Void> ``` |

Modified krb5_const_principal

|  | Declaration |
| --- | --- |
| From | ``` typealias krb5_const_principal = ConstUnsafePointer<krb5_principal_data> ``` |
| To | ``` typealias krb5_const_principal = UnsafePointer<krb5_principal_data> ``` |

Modified krb5_pointer

|  | Declaration |
| --- | --- |
| From | ``` typealias krb5_pointer = UnsafePointer<()> ``` |
| To | ``` typealias krb5_pointer = UnsafeMutablePointer<Void> ``` |

Modified krb5_principal

|  | Declaration |
| --- | --- |
| From | ``` typealias krb5_principal = UnsafePointer<krb5_principal_data> ``` |
| To | ``` typealias krb5_principal = UnsafeMutablePointer<krb5_principal_data> ``` |

Modified krb5_vset_error_message(krb5_context, krb5_error_code, UnsafePointer<Int8>, CVaListPointer)

|  | Declaration |
| --- | --- |
| From | ``` func krb5_vset_error_message(_ _: krb5_context, _ _: krb5_error_code, _ _: ConstUnsafePointer<Int8>, _ _: CVaListPointer) ``` |
| To | ``` func krb5_vset_error_message(_ _: krb5_context, _ _: krb5_error_code, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) ``` |

Modified profile_add_relation(profile_t, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_add_relation(_ profile: profile_t, _ names: UnsafePointer<ConstUnsafePointer<Int8>>, _ new_value: ConstUnsafePointer<Int8>) -> Int ``` |
| To | ``` func profile_add_relation(_ profile: profile_t, _ names: UnsafeMutablePointer<UnsafePointer<Int8>>, _ new_value: UnsafePointer<Int8>) -> Int ``` |

Modified profile_clear_relation(profile_t, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_clear_relation(_ profile: profile_t, _ names: UnsafePointer<ConstUnsafePointer<Int8>>) -> Int ``` |
| To | ``` func profile_clear_relation(_ profile: profile_t, _ names: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Int ``` |

Modified profile_filespec_list_t

|  | Declaration |
| --- | --- |
| From | ``` typealias profile_filespec_list_t = UnsafePointer<Int8> ``` |
| To | ``` typealias profile_filespec_list_t = UnsafeMutablePointer<Int8> ``` |

Modified profile_filespec_t

|  | Declaration |
| --- | --- |
| From | ``` typealias profile_filespec_t = UnsafePointer<Int8> ``` |
| To | ``` typealias profile_filespec_t = UnsafeMutablePointer<Int8> ``` |

Modified profile_flush_to_buffer(profile_t, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_flush_to_buffer(_ profile: profile_t, _ bufp: UnsafePointer<UnsafePointer<Int8>>) -> Int ``` |
| To | ``` func profile_flush_to_buffer(_ profile: profile_t, _ bufp: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int ``` |

Modified profile_free_buffer(profile_t, UnsafeMutablePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func profile_free_buffer(_ profile: profile_t, _ buf: UnsafePointer<Int8>) ``` |
| To | ``` func profile_free_buffer(_ profile: profile_t, _ buf: UnsafeMutablePointer<Int8>) ``` |

Modified profile_free_list(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)

|  | Declaration |
| --- | --- |
| From | ``` func profile_free_list(_ list: UnsafePointer<UnsafePointer<Int8>>) ``` |
| To | ``` func profile_free_list(_ list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) ``` |

Modified profile_get_boolean(profile_t, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_get_boolean(_ profile: profile_t, _ name: ConstUnsafePointer<Int8>, _ subname: ConstUnsafePointer<Int8>, _ subsubname: ConstUnsafePointer<Int8>, _ def_val: Int32, _ ret_default: UnsafePointer<Int32>) -> Int ``` |
| To | ``` func profile_get_boolean(_ profile: profile_t, _ name: UnsafePointer<Int8>, _ subname: UnsafePointer<Int8>, _ subsubname: UnsafePointer<Int8>, _ def_val: Int32, _ ret_default: UnsafeMutablePointer<Int32>) -> Int ``` |

Modified profile_get_integer(profile_t, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int32>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_get_integer(_ profile: profile_t, _ name: ConstUnsafePointer<Int8>, _ subname: ConstUnsafePointer<Int8>, _ subsubname: ConstUnsafePointer<Int8>, _ def_val: Int32, _ ret_default: UnsafePointer<Int32>) -> Int ``` |
| To | ``` func profile_get_integer(_ profile: profile_t, _ name: UnsafePointer<Int8>, _ subname: UnsafePointer<Int8>, _ subsubname: UnsafePointer<Int8>, _ def_val: Int32, _ ret_default: UnsafeMutablePointer<Int32>) -> Int ``` |

Modified profile_get_relation_names(profile_t, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Int8>>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_get_relation_names(_ profile: profile_t, _ names: UnsafePointer<ConstUnsafePointer<Int8>>, _ ret_names: UnsafePointer<UnsafePointer<UnsafePointer<Int8>>>) -> Int ``` |
| To | ``` func profile_get_relation_names(_ profile: profile_t, _ names: UnsafeMutablePointer<UnsafePointer<Int8>>, _ ret_names: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Int8>>>) -> Int ``` |

Modified profile_get_string(profile_t, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_get_string(_ profile: profile_t, _ name: ConstUnsafePointer<Int8>, _ subname: ConstUnsafePointer<Int8>, _ subsubname: ConstUnsafePointer<Int8>, _ def_val: ConstUnsafePointer<Int8>, _ ret_string: UnsafePointer<UnsafePointer<Int8>>) -> Int ``` |
| To | ``` func profile_get_string(_ profile: profile_t, _ name: UnsafePointer<Int8>, _ subname: UnsafePointer<Int8>, _ subsubname: UnsafePointer<Int8>, _ def_val: UnsafePointer<Int8>, _ ret_string: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int ``` |

Modified profile_get_subsection_names(profile_t, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Int8>>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_get_subsection_names(_ profile: profile_t, _ names: UnsafePointer<ConstUnsafePointer<Int8>>, _ ret_names: UnsafePointer<UnsafePointer<UnsafePointer<Int8>>>) -> Int ``` |
| To | ``` func profile_get_subsection_names(_ profile: profile_t, _ names: UnsafeMutablePointer<UnsafePointer<Int8>>, _ ret_names: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Int8>>>) -> Int ``` |

Modified profile_get_values(profile_t, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Int8>>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_get_values(_ profile: profile_t, _ names: ConstUnsafePointer<ConstUnsafePointer<Int8>>, _ ret_values: UnsafePointer<UnsafePointer<UnsafePointer<Int8>>>) -> Int ``` |
| To | ``` func profile_get_values(_ profile: profile_t, _ names: UnsafePointer<UnsafePointer<Int8>>, _ ret_values: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<Int8>>>) -> Int ``` |

Modified profile_init(UnsafeMutablePointer<const_profile_filespec_t>, UnsafeMutablePointer<profile_t>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_init(_ files: UnsafePointer<const_profile_filespec_t>, _ ret_profile: UnsafePointer<profile_t>) -> Int ``` |
| To | ``` func profile_init(_ files: UnsafeMutablePointer<const_profile_filespec_t>, _ ret_profile: UnsafeMutablePointer<profile_t>) -> Int ``` |

Modified profile_init_path(const_profile_filespec_list_t, UnsafeMutablePointer<profile_t>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_init_path(_ filelist: const_profile_filespec_list_t, _ ret_profile: UnsafePointer<profile_t>) -> Int ``` |
| To | ``` func profile_init_path(_ filelist: const_profile_filespec_list_t, _ ret_profile: UnsafeMutablePointer<profile_t>) -> Int ``` |

Modified profile_is_modified(profile_t, UnsafeMutablePointer<Int32>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_is_modified(_ profile: profile_t, _ modified: UnsafePointer<Int32>) -> Int ``` |
| To | ``` func profile_is_modified(_ profile: profile_t, _ modified: UnsafeMutablePointer<Int32>) -> Int ``` |

Modified profile_is_writable(profile_t, UnsafeMutablePointer<Int32>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_is_writable(_ profile: profile_t, _ writable: UnsafePointer<Int32>) -> Int ``` |
| To | ``` func profile_is_writable(_ profile: profile_t, _ writable: UnsafeMutablePointer<Int32>) -> Int ``` |

Modified profile_iterator(UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_iterator(_ iter_p: UnsafePointer<UnsafePointer<()>>, _ ret_name: UnsafePointer<UnsafePointer<Int8>>, _ ret_value: UnsafePointer<UnsafePointer<Int8>>) -> Int ``` |
| To | ``` func profile_iterator(_ iter_p: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ ret_name: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ ret_value: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int ``` |

Modified profile_iterator_create(profile_t, UnsafePointer<UnsafePointer<Int8>>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_iterator_create(_ profile: profile_t, _ names: ConstUnsafePointer<ConstUnsafePointer<Int8>>, _ flags: Int32, _ ret_iter: UnsafePointer<UnsafePointer<()>>) -> Int ``` |
| To | ``` func profile_iterator_create(_ profile: profile_t, _ names: UnsafePointer<UnsafePointer<Int8>>, _ flags: Int32, _ ret_iter: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int ``` |

Modified profile_iterator_free(UnsafeMutablePointer<UnsafeMutablePointer<Void>>)

|  | Declaration |
| --- | --- |
| From | ``` func profile_iterator_free(_ iter_p: UnsafePointer<UnsafePointer<()>>) ``` |
| To | ``` func profile_iterator_free(_ iter_p: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) ``` |

Modified profile_release_string(UnsafeMutablePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func profile_release_string(_ str: UnsafePointer<Int8>) ``` |
| To | ``` func profile_release_string(_ str: UnsafeMutablePointer<Int8>) ``` |

Modified profile_rename_section(profile_t, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_rename_section(_ profile: profile_t, _ names: UnsafePointer<ConstUnsafePointer<Int8>>, _ new_name: ConstUnsafePointer<Int8>) -> Int ``` |
| To | ``` func profile_rename_section(_ profile: profile_t, _ names: UnsafeMutablePointer<UnsafePointer<Int8>>, _ new_name: UnsafePointer<Int8>) -> Int ``` |

Modified profile_update_relation(profile_t, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func profile_update_relation(_ profile: profile_t, _ names: UnsafePointer<ConstUnsafePointer<Int8>>, _ old_value: ConstUnsafePointer<Int8>, _ new_value: ConstUnsafePointer<Int8>) -> Int ``` |
| To | ``` func profile_update_relation(_ profile: profile_t, _ names: UnsafeMutablePointer<UnsafePointer<Int8>>, _ old_value: UnsafePointer<Int8>, _ new_value: UnsafePointer<Int8>) -> Int ``` |

Modified remove_error_table(UnsafePointer<error_table>) -> errcode_t

|  | Declaration |
| --- | --- |
| From | ``` func remove_error_table(_ et: ConstUnsafePointer<error_table>) -> errcode_t ``` |
| To | ``` func remove_error_table(_ et: UnsafePointer<error_table>) -> errcode_t ``` |

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
