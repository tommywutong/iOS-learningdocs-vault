---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/GSS.html
archived_at: '2026-07-15T07:34:46.035205Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# GSS Changes

## GSS

gssapi.hRemoved #def GSS_C_INQ_SSPI_SESSION_KEYRemoved #def GSS_C_INQ_WIN2K_PAC_XRemoved #def GSS_SASL_DIGEST_MD5_MECHANISMgssapi_apple.hAdded [GSSCreateError()](https://developer.apple.com/documentation/gss/1411913-gsscreateerror)Modified [GSSCreateCredentialFromUUID()](https://developer.apple.com/documentation/gss/1411915-gsscreatecredentialfromuuid)

|  | Declaration |
| --- | --- |
| From | ``` gss_cred_id_t GSSCreateCredentialFromUUID (	CFUUIDRef); ``` |
| To | ``` gss_cred_id_t GSSCreateCredentialFromUUID (	CFUUIDRef uuid); ``` |

Modified [GSSCreateName()](https://developer.apple.com/documentation/gss/1411907-gsscreatename)

|  | Declaration |
| --- | --- |
| From | ``` gss_name_t GSSCreateName (	CFTypeRef,	gss_const_OID,	CFErrorRef *); ``` |
| To | ``` gss_name_t GSSCreateName (	CFTypeRef name,	gss_const_OID name_type,	CFErrorRef *error); ``` |

Modified [GSSCredentialCopyName()](https://developer.apple.com/documentation/gss/1411911-gsscredentialcopyname)

|  | Declaration |
| --- | --- |
| From | ``` gss_name_t GSSCredentialCopyName (	gss_cred_id_t); ``` |
| To | ``` gss_name_t GSSCredentialCopyName (	gss_cred_id_t cred); ``` |

Modified [GSSCredentialCopyUUID()](https://developer.apple.com/documentation/gss/1411905-gsscredentialcopyuuid)

|  | Declaration |
| --- | --- |
| From | ``` CFUUIDRef GSSCredentialCopyUUID (	gss_cred_id_t); ``` |
| To | ``` CFUUIDRef GSSCredentialCopyUUID (	gss_cred_id_t credential); ``` |

Modified [GSSCredentialGetLifetime()](https://developer.apple.com/documentation/gss/1411899-gsscredentialgetlifetime)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 GSSCredentialGetLifetime (	gss_cred_id_t); ``` |
| To | ``` OM_uint32 GSSCredentialGetLifetime (	gss_cred_id_t cred); ``` |

Modified [GSSNameCreateDisplayString()](https://developer.apple.com/documentation/gss/1411901-gssnamecreatedisplaystring)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef GSSNameCreateDisplayString (	gss_name_t); ``` |
| To | ``` CFStringRef GSSNameCreateDisplayString (	gss_name_t name); ``` |

Modified [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_aapl_change_password (	const gss_name_t,	gss_const_OID,	CFDictionaryRef,	CFErrorRef *); ``` |
| To | ``` OM_uint32 gss_aapl_change_password (	const gss_name_t name,	gss_const_OID mech,	CFDictionaryRef attributes,	CFErrorRef *error); ``` |

Modified [gss_aapl_initial_cred()](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_aapl_initial_cred (	const gss_name_t,	gss_const_OID,	CFDictionaryRef,	gss_cred_id_t *,	CFErrorRef *); ``` |
| To | ``` OM_uint32 gss_aapl_initial_cred (	const gss_name_t desired_name,	gss_const_OID desired_mech,	CFDictionaryRef attributes,	gss_cred_id_t *output_cred_handle,	CFErrorRef *error); ``` |

gssapi_oid.hAdded #def GSS_KRB5_NT_PRINCIPALAdded #def GSS_KRB5_NT_PRINCIPAL_NAMEAdded #def GSS_SCRAM_MECHANISMModified #def GSS_C_NT_ANONYMOUS

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

Modified #def GSS_C_NT_EXPORT_NAME

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

Modified #def GSS_C_NT_HOSTBASED_SERVICE

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

Modified #def GSS_C_NT_HOSTBASED_SERVICE_X

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

Modified #def GSS_C_NT_MACHINE_UID_NAME

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

Modified #def GSS_C_NT_STRING_UID_NAME

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

Modified #def GSS_C_NT_USER_NAME

|  | Header |
| --- | --- |
| From | GSS/gssapi.h |
| To | GSS/gssapi_oid.h |

gssapi_protos.hRemoved #def GSSAPI_DEPRECATED_FUNCTIONAdded #def HEIMDAL_PRINTF_ATTRIBUTEAdded [gss_indicate_mechs_by_attrs()](https://developer.apple.com/documentation/gss/1438413-gss_indicate_mechs_by_attrs)Added [gss_inquire_mech_for_saslname()](https://developer.apple.com/documentation/gss/1438514-gss_inquire_mech_for_saslname)Added [gss_inquire_name()](https://developer.apple.com/documentation/gss/1438422-gss_inquire_name)Added [gss_inquire_saslname_for_mech()](https://developer.apple.com/documentation/gss/1438445-gss_inquire_saslname_for_mech)Modified [gss_accept_sec_context()](https://developer.apple.com/documentation/gss/1438493-gss_accept_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_accept_sec_context (	OM_uint32 *,	gss_ctx_id_t *,	const gss_cred_id_t,	const gss_buffer_t,	const gss_channel_bindings_t,	gss_name_t *,	gss_OID *,	gss_buffer_t,	OM_uint32 *,	OM_uint32 *,	gss_cred_id_t *); ``` |
| To | ``` OM_uint32 gss_accept_sec_context (	OM_uint32 *minor_status,	gss_ctx_id_t *context_handle,	const gss_cred_id_t acceptor_cred_handle,	const gss_buffer_t input_token,	const gss_channel_bindings_t input_chan_bindings,	gss_name_t *src_name,	gss_OID *mech_type,	gss_buffer_t output_token,	OM_uint32 *ret_flags,	OM_uint32 *time_rec,	gss_cred_id_t *delegated_cred_handle); ``` |

Modified [gss_acquire_cred()](https://developer.apple.com/documentation/gss/1438466-gss_acquire_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_acquire_cred (	OM_uint32 *,	const gss_name_t,	OM_uint32,	const gss_OID_set,	gss_cred_usage_t,	gss_cred_id_t *,	gss_OID_set *,	OM_uint32 *); ``` |
| To | ``` OM_uint32 gss_acquire_cred (	OM_uint32 *minor_status,	const gss_name_t desired_name,	OM_uint32 time_req,	const gss_OID_set desired_mechs,	gss_cred_usage_t cred_usage,	gss_cred_id_t *output_cred_handle,	gss_OID_set *actual_mechs,	OM_uint32 *time_rec); ``` |

Modified [gss_acquire_cred_with_password()](https://developer.apple.com/documentation/gss/1438426-gss_acquire_cred_with_password)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_acquire_cred_with_password (	OM_uint32 *,	const gss_name_t,	const gss_buffer_t,	OM_uint32,	const gss_OID_set,	gss_cred_usage_t,	gss_cred_id_t *,	gss_OID_set *,	OM_uint32 *); ``` |
| To | ``` OM_uint32 gss_acquire_cred_with_password (	OM_uint32 *minor_status,	const gss_name_t desired_name,	const gss_buffer_t password,	OM_uint32 time_req,	const gss_OID_set desired_mechs,	gss_cred_usage_t cred_usage,	gss_cred_id_t *output_cred_handle,	gss_OID_set *actual_mechs,	OM_uint32 *time_rec); ``` |

Modified [gss_add_buffer_set_member()](https://developer.apple.com/documentation/gss/1438479-gss_add_buffer_set_member)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_add_buffer_set_member (	OM_uint32 *,	const gss_buffer_t,	gss_buffer_set_t *); ``` |
| To | ``` OM_uint32 gss_add_buffer_set_member (	OM_uint32 *minor_status,	const gss_buffer_t member_buffer,	gss_buffer_set_t *buffer_set); ``` |

Modified [gss_add_cred()](https://developer.apple.com/documentation/gss/1438473-gss_add_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_add_cred (	OM_uint32 *,	const gss_cred_id_t,	const gss_name_t,	const gss_OID,	gss_cred_usage_t,	OM_uint32,	OM_uint32,	gss_cred_id_t *,	gss_OID_set *,	OM_uint32 *,	OM_uint32 *); ``` |
| To | ``` OM_uint32 gss_add_cred (	OM_uint32 *minor_status,	const gss_cred_id_t input_cred_handle,	const gss_name_t desired_name,	const gss_OID desired_mech,	gss_cred_usage_t cred_usage,	OM_uint32 initiator_time_req,	OM_uint32 acceptor_time_req,	gss_cred_id_t *output_cred_handle,	gss_OID_set *actual_mechs,	OM_uint32 *initiator_time_rec,	OM_uint32 *acceptor_time_rec); ``` |

Modified [gss_add_oid_set_member()](https://developer.apple.com/documentation/gss/1438411-gss_add_oid_set_member)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_add_oid_set_member (	OM_uint32 *,	gss_const_OID,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_add_oid_set_member (	OM_uint32 *minor_status,	gss_const_OID member_oid,	gss_OID_set *oid_set); ``` |

Modified [gss_canonicalize_name()](https://developer.apple.com/documentation/gss/1438494-gss_canonicalize_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_canonicalize_name (	OM_uint32 *,	const gss_name_t,	const gss_OID,	gss_name_t *); ``` |
| To | ``` OM_uint32 gss_canonicalize_name (	OM_uint32 *minor_status,	const gss_name_t input_name,	const gss_OID mech_type,	gss_name_t *output_name); ``` |

Modified [gss_compare_name()](https://developer.apple.com/documentation/gss/1438437-gss_compare_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_compare_name (	OM_uint32 *,	const gss_name_t,	const gss_name_t,	int *); ``` |
| To | ``` OM_uint32 gss_compare_name (	OM_uint32 *minor_status,	const gss_name_t name1_arg,	const gss_name_t name2_arg,	int *name_equal); ``` |

Modified [gss_context_time()](https://developer.apple.com/documentation/gss/1438487-gss_context_time)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_context_time (	OM_uint32 *,	const gss_ctx_id_t,	OM_uint32 *); ``` |
| To | ``` OM_uint32 gss_context_time (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	OM_uint32 *time_rec); ``` |

Modified [gss_create_empty_buffer_set()](https://developer.apple.com/documentation/gss/1438537-gss_create_empty_buffer_set)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_create_empty_buffer_set (	OM_uint32 *,	gss_buffer_set_t *); ``` |
| To | ``` OM_uint32 gss_create_empty_buffer_set (	OM_uint32 *minor_status,	gss_buffer_set_t *buffer_set); ``` |

Modified [gss_create_empty_oid_set()](https://developer.apple.com/documentation/gss/1438489-gss_create_empty_oid_set)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_create_empty_oid_set (	OM_uint32 *,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_create_empty_oid_set (	OM_uint32 *minor_status,	gss_OID_set *oid_set); ``` |

Modified [gss_decapsulate_token()](https://developer.apple.com/documentation/gss/1438529-gss_decapsulate_token)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_decapsulate_token (	gss_const_buffer_t,	gss_const_OID,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_decapsulate_token (	gss_const_buffer_t input_token,	gss_const_OID oid,	gss_buffer_t output_token); ``` |

Modified [gss_delete_sec_context()](https://developer.apple.com/documentation/gss/1438435-gss_delete_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_delete_sec_context (	OM_uint32 *,	gss_ctx_id_t *,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_delete_sec_context (	OM_uint32 *minor_status,	gss_ctx_id_t *context_handle,	gss_buffer_t output_token); ``` |

Modified [gss_destroy_cred()](https://developer.apple.com/documentation/gss/1438521-gss_destroy_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_destroy_cred (	OM_uint32 *,	gss_cred_id_t *); ``` |
| To | ``` OM_uint32 gss_destroy_cred (	OM_uint32 *min_stat,	gss_cred_id_t *cred_handle); ``` |

Modified [gss_display_mech_attr()](https://developer.apple.com/documentation/gss/1438475-gss_display_mech_attr)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_display_mech_attr (	OM_uint32 *,	gss_const_OID,	gss_buffer_t,	gss_buffer_t,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_display_mech_attr (	OM_uint32 *minor_status,	gss_const_OID mech_attr,	gss_buffer_t name,	gss_buffer_t short_desc,	gss_buffer_t long_desc); ``` |

Modified [gss_display_name()](https://developer.apple.com/documentation/gss/1438464-gss_display_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_display_name (	OM_uint32 *,	const gss_name_t,	gss_buffer_t,	gss_OID *); ``` |
| To | ``` OM_uint32 gss_display_name (	OM_uint32 *minor_status,	const gss_name_t input_name,	gss_buffer_t output_name_buffer,	gss_OID *output_name_type); ``` |

Modified [gss_display_status()](https://developer.apple.com/documentation/gss/1438535-gss_display_status)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_display_status (	OM_uint32 *,	OM_uint32,	int,	const gss_OID,	OM_uint32 *,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_display_status (	OM_uint32 *minor_status,	OM_uint32 status_value,	int status_type,	const gss_OID mech_type,	OM_uint32 *message_content,	gss_buffer_t status_string); ``` |

Modified [gss_duplicate_name()](https://developer.apple.com/documentation/gss/1438418-gss_duplicate_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_duplicate_name (	OM_uint32 *,	const gss_name_t,	gss_name_t *); ``` |
| To | ``` OM_uint32 gss_duplicate_name (	OM_uint32 *minor_status,	const gss_name_t src_name,	gss_name_t *dest_name); ``` |

Modified [gss_duplicate_oid()](https://developer.apple.com/documentation/gss/1438533-gss_duplicate_oid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_duplicate_oid (	OM_uint32 *,	gss_OID,	gss_OID *dest_oid); ``` | -- |
| To | ``` OM_uint32 gss_duplicate_oid (	OM_uint32 *minor_status,	gss_OID src_oid,	gss_OID *dest_oid); ``` | OS X 10.9 |

Modified [gss_encapsulate_token()](https://developer.apple.com/documentation/gss/1438463-gss_encapsulate_token)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_encapsulate_token (	gss_const_buffer_t,	gss_const_OID,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_encapsulate_token (	gss_const_buffer_t input_token,	gss_const_OID oid,	gss_buffer_t output_token); ``` |

Modified [gss_export_cred()](https://developer.apple.com/documentation/gss/1438500-gss_export_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_export_cred (	OM_uint32 *,	gss_cred_id_t,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_export_cred (	OM_uint32 *minor_status,	gss_cred_id_t cred_handle,	gss_buffer_t token); ``` |

Modified [gss_export_name()](https://developer.apple.com/documentation/gss/1438477-gss_export_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_export_name (	OM_uint32 *,	const gss_name_t,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_export_name (	OM_uint32 *minor_status,	const gss_name_t input_name,	gss_buffer_t exported_name); ``` |

Modified [gss_export_sec_context()](https://developer.apple.com/documentation/gss/1438449-gss_export_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_export_sec_context (	OM_uint32 *,	gss_ctx_id_t *,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_export_sec_context (	OM_uint32 *minor_status,	gss_ctx_id_t *context_handle,	gss_buffer_t interprocess_token); ``` |

Modified [gss_get_mic()](https://developer.apple.com/documentation/gss/1438530-gss_get_mic)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_get_mic (	OM_uint32 *,	const gss_ctx_id_t,	gss_qop_t,	const gss_buffer_t,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_get_mic (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	gss_qop_t qop_req,	const gss_buffer_t message_buffer,	gss_buffer_t message_token); ``` |

Modified [gss_import_cred()](https://developer.apple.com/documentation/gss/1438510-gss_import_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_import_cred (	OM_uint32 *,	gss_buffer_t,	gss_cred_id_t *); ``` |
| To | ``` OM_uint32 gss_import_cred (	OM_uint32 *minor_status,	gss_buffer_t token,	gss_cred_id_t *cred_handle); ``` |

Modified [gss_import_name()](https://developer.apple.com/documentation/gss/1438453-gss_import_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_import_name (	OM_uint32 *,	const gss_buffer_t,	gss_const_OID,	gss_name_t *); ``` |
| To | ``` OM_uint32 gss_import_name (	OM_uint32 *minor_status,	const gss_buffer_t input_name_buffer,	gss_const_OID input_name_type,	gss_name_t *output_name); ``` |

Modified [gss_import_sec_context()](https://developer.apple.com/documentation/gss/1438484-gss_import_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_import_sec_context (	OM_uint32 *,	const gss_buffer_t,	gss_ctx_id_t *); ``` |
| To | ``` OM_uint32 gss_import_sec_context (	OM_uint32 *minor_status,	const gss_buffer_t interprocess_token,	gss_ctx_id_t *context_handle); ``` |

Modified [gss_indicate_mechs()](https://developer.apple.com/documentation/gss/1438424-gss_indicate_mechs)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_indicate_mechs (	OM_uint32 *,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_indicate_mechs (	OM_uint32 *minor_status,	gss_OID_set *mech_set); ``` |

Modified [gss_init_sec_context()](https://developer.apple.com/documentation/gss/1438476-gss_init_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_init_sec_context (	OM_uint32 *,	const gss_cred_id_t,	gss_ctx_id_t *,	const gss_name_t,	const gss_OID,	OM_uint32,	OM_uint32,	const gss_channel_bindings_t,	const gss_buffer_t,	gss_OID *,	gss_buffer_t,	OM_uint32 *,	OM_uint32 *); ``` |
| To | ``` OM_uint32 gss_init_sec_context (	OM_uint32 *minor_status,	const gss_cred_id_t initiator_cred_handle,	gss_ctx_id_t *context_handle,	const gss_name_t target_name,	const gss_OID input_mech_type,	OM_uint32 req_flags,	OM_uint32 time_req,	const gss_channel_bindings_t input_chan_bindings,	const gss_buffer_t input_token,	gss_OID *actual_mech_type,	gss_buffer_t output_token,	OM_uint32 *ret_flags,	OM_uint32 *time_rec); ``` |

Modified [gss_inquire_attrs_for_mech()](https://developer.apple.com/documentation/gss/1438417-gss_inquire_attrs_for_mech)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_attrs_for_mech (	OM_uint32 *,	gss_const_OID,	gss_OID_set *,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_inquire_attrs_for_mech (	OM_uint32 *minor_status,	gss_const_OID mech,	gss_OID_set *mech_attr,	gss_OID_set *known_mech_attrs); ``` |

Modified [gss_inquire_context()](https://developer.apple.com/documentation/gss/1438458-gss_inquire_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_context (	OM_uint32 *,	const gss_ctx_id_t,	gss_name_t *,	gss_name_t *,	OM_uint32 *,	gss_OID *,	OM_uint32 *,	int *,	int *); ``` |
| To | ``` OM_uint32 gss_inquire_context (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	gss_name_t *src_name,	gss_name_t *targ_name,	OM_uint32 *lifetime_rec,	gss_OID *mech_type,	OM_uint32 *ctx_flags,	int *locally_initiated,	int *xopen); ``` |

Modified [gss_inquire_cred()](https://developer.apple.com/documentation/gss/1438531-gss_inquire_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_cred (	OM_uint32 *,	const gss_cred_id_t,	gss_name_t *,	OM_uint32 *,	gss_cred_usage_t *,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_inquire_cred (	OM_uint32 *minor_status,	const gss_cred_id_t cred_handle,	gss_name_t *name_ret,	OM_uint32 *lifetime,	gss_cred_usage_t *cred_usage,	gss_OID_set *mechanisms); ``` |

Modified [gss_inquire_cred_by_mech()](https://developer.apple.com/documentation/gss/1438518-gss_inquire_cred_by_mech)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_cred_by_mech (	OM_uint32 *,	const gss_cred_id_t,	const gss_OID,	gss_name_t *,	OM_uint32 *,	OM_uint32 *,	gss_cred_usage_t *); ``` |
| To | ``` OM_uint32 gss_inquire_cred_by_mech (	OM_uint32 *minor_status,	const gss_cred_id_t cred_handle,	const gss_OID mech_type,	gss_name_t *cred_name,	OM_uint32 *initiator_lifetime,	OM_uint32 *acceptor_lifetime,	gss_cred_usage_t *cred_usage); ``` |

Modified [gss_inquire_cred_by_oid()](https://developer.apple.com/documentation/gss/1438504-gss_inquire_cred_by_oid)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_cred_by_oid (	OM_uint32 *,	const gss_cred_id_t,	const gss_OID,	gss_buffer_set_t *); ``` |
| To | ``` OM_uint32 gss_inquire_cred_by_oid (	OM_uint32 *minor_status,	const gss_cred_id_t cred_handle,	const gss_OID desired_object,	gss_buffer_set_t *data_set); ``` |

Modified [gss_inquire_mechs_for_name()](https://developer.apple.com/documentation/gss/1438481-gss_inquire_mechs_for_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_mechs_for_name (	OM_uint32 *,	const gss_name_t,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_inquire_mechs_for_name (	OM_uint32 *minor_status,	const gss_name_t input_name,	gss_OID_set *mech_types); ``` |

Modified [gss_inquire_names_for_mech()](https://developer.apple.com/documentation/gss/1438523-gss_inquire_names_for_mech)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_names_for_mech (	OM_uint32 *,	gss_const_OID,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_inquire_names_for_mech (	OM_uint32 *minor_status,	gss_const_OID mechanism,	gss_OID_set *name_types); ``` |

Modified [gss_inquire_sec_context_by_oid()](https://developer.apple.com/documentation/gss/1438525-gss_inquire_sec_context_by_oid)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_sec_context_by_oid (	OM_uint32 *,	const gss_ctx_id_t,	const gss_OID,	gss_buffer_set_t *); ``` |
| To | ``` OM_uint32 gss_inquire_sec_context_by_oid (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	const gss_OID desired_object,	gss_buffer_set_t *data_set); ``` |

Modified [gss_iter_creds()](https://developer.apple.com/documentation/gss/1438515-gss_iter_creds)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_iter_creds (	OM_uint32 *,	OM_uint32,	gss_const_OID,	void (^useriter)(gss_OID, gss_cred_id_t)); ``` |
| To | ``` OM_uint32 gss_iter_creds (	OM_uint32 *min_stat,	OM_uint32 flags,	gss_const_OID mech,	void (^useriter)(gss_OID, gss_cred_id_t)); ``` |

Modified [gss_iter_creds_f()](https://developer.apple.com/documentation/gss/1438438-gss_iter_creds_f)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_iter_creds_f (	OM_uint32 *,	OM_uint32,	gss_const_OID,	void *,	void (*)(void *, gss_OID, gss_cred_id_t)); ``` |
| To | ``` OM_uint32 gss_iter_creds_f (	OM_uint32 *min_stat,	OM_uint32 flags,	gss_const_OID mech,	void *userctx,	void (*useriter)(void *, gss_OID, gss_cred_id_t)); ``` |

Modified [gss_krb5_ccache_name()](https://developer.apple.com/documentation/gss/1438472-gss_krb5_ccache_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_krb5_ccache_name (	OM_uint32 *,	const char *,	const char **); ``` |
| To | ``` OM_uint32 gss_krb5_ccache_name (	OM_uint32 *minor_status,	const char *name,	const char **out_name); ``` |

Modified [gss_krb5_copy_ccache()](https://developer.apple.com/documentation/gss/1438508-gss_krb5_copy_ccache)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_krb5_copy_ccache (	OM_uint32 *,	gss_cred_id_t,	struct krb5_ccache_data *); ``` | OS X 10.8 |
| To | ``` OM_uint32 gss_krb5_copy_ccache (	OM_uint32 *minor_status,	gss_cred_id_t cred,	struct krb5_ccache_data *out); ``` | OS X 10.9 |

Modified [gss_krb5_export_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438433-gss_krb5_export_lucid_sec_contex)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_krb5_export_lucid_sec_context (	OM_uint32 *,	gss_ctx_id_t *,	OM_uint32,	void **); ``` |
| To | ``` OM_uint32 gss_krb5_export_lucid_sec_context (	OM_uint32 *minor_status,	gss_ctx_id_t *context_handle,	OM_uint32 version,	void **rctx); ``` |

Modified [gss_krb5_free_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438483-gss_krb5_free_lucid_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_krb5_free_lucid_sec_context (	OM_uint32 *,	void *); ``` |
| To | ``` OM_uint32 gss_krb5_free_lucid_sec_context (	OM_uint32 *minor_status,	void *c); ``` |

Modified [gss_krb5_set_allowable_enctypes()](https://developer.apple.com/documentation/gss/1438431-gss_krb5_set_allowable_enctypes)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_krb5_set_allowable_enctypes (	OM_uint32 *,	gss_cred_id_t,	OM_uint32,	int32_t *); ``` |
| To | ``` OM_uint32 gss_krb5_set_allowable_enctypes (	OM_uint32 *minor_status,	gss_cred_id_t cred,	OM_uint32 num_enctypes,	int32_t *enctypes); ``` |

Modified [gss_oid_equal()](https://developer.apple.com/documentation/gss/1438498-gss_oid_equal)

|  | Declaration |
| --- | --- |
| From | ``` int gss_oid_equal (	gss_const_OID,	gss_const_OID); ``` |
| To | ``` int gss_oid_equal (	gss_const_OID a,	gss_const_OID b); ``` |

Modified [gss_oid_to_str()](https://developer.apple.com/documentation/gss/1438512-gss_oid_to_str)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_oid_to_str (	OM_uint32 *,	gss_OID,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_oid_to_str (	OM_uint32 *minor_status,	gss_OID oid,	gss_buffer_t oid_str); ``` |

Modified [gss_process_context_token()](https://developer.apple.com/documentation/gss/1438516-gss_process_context_token)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_process_context_token (	OM_uint32 *,	const gss_ctx_id_t,	const gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_process_context_token (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	const gss_buffer_t token_buffer); ``` |

Modified [gss_pseudo_random()](https://developer.apple.com/documentation/gss/1438496-gss_pseudo_random)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_pseudo_random (	OM_uint32 *,	gss_ctx_id_t,	int,	const gss_buffer_t,	ssize_t,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_pseudo_random (	OM_uint32 *minor_status,	gss_ctx_id_t context,	int prf_key,	const gss_buffer_t prf_in,	ssize_t desired_output_len,	gss_buffer_t prf_out); ``` |

Modified [gss_release_buffer()](https://developer.apple.com/documentation/gss/1438486-gss_release_buffer)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_release_buffer (	OM_uint32 *,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_release_buffer (	OM_uint32 *minor_status,	gss_buffer_t buffer); ``` |

Modified [gss_release_buffer_set()](https://developer.apple.com/documentation/gss/1438428-gss_release_buffer_set)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_release_buffer_set (	OM_uint32 *,	gss_buffer_set_t *); ``` |
| To | ``` OM_uint32 gss_release_buffer_set (	OM_uint32 *minor_status,	gss_buffer_set_t *buffer_set); ``` |

Modified [gss_release_cred()](https://developer.apple.com/documentation/gss/1438461-gss_release_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_release_cred (	OM_uint32 *,	gss_cred_id_t *); ``` |
| To | ``` OM_uint32 gss_release_cred (	OM_uint32 *minor_status,	gss_cred_id_t *cred_handle); ``` |

Modified [gss_release_name()](https://developer.apple.com/documentation/gss/1438451-gss_release_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_release_name (	OM_uint32 *,	gss_name_t *); ``` |
| To | ``` OM_uint32 gss_release_name (	OM_uint32 *minor_status,	gss_name_t *input_name); ``` |

Modified [gss_release_oid()](https://developer.apple.com/documentation/gss/1438455-gss_release_oid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_release_oid (	OM_uint32 *,	gss_OID *); ``` | -- |
| To | ``` OM_uint32 gss_release_oid (	OM_uint32 *minor_status,	gss_OID *oid); ``` | OS X 10.9 |

Modified [gss_release_oid_set()](https://developer.apple.com/documentation/gss/1438480-gss_release_oid_set)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_release_oid_set (	OM_uint32 *,	gss_OID_set *); ``` |
| To | ``` OM_uint32 gss_release_oid_set (	OM_uint32 *minor_status,	gss_OID_set *set); ``` |

Modified [gss_seal()](https://developer.apple.com/documentation/gss/1438459-gss_seal)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_seal (	OM_uint32 *,	gss_ctx_id_t,	int,	int,	gss_buffer_t,	int *,	gss_buffer_t); ``` | OS X 10.7 |
| To | ``` OM_uint32 gss_seal (	OM_uint32 *minor_status,	gss_ctx_id_t context_handle,	int conf_req_flag,	int qop_req,	gss_buffer_t input_message_buffer,	int *conf_state,	gss_buffer_t output_message_buffer); ``` | OS X 10.9 |

Modified [gss_set_cred_option()](https://developer.apple.com/documentation/gss/1438513-gss_set_cred_option)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_set_cred_option (	OM_uint32 *,	gss_cred_id_t *,	const gss_OID,	const gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_set_cred_option (	OM_uint32 *minor_status,	gss_cred_id_t *cred_handle,	const gss_OID object,	const gss_buffer_t value); ``` |

Modified [gss_set_sec_context_option()](https://developer.apple.com/documentation/gss/1438491-gss_set_sec_context_option)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_set_sec_context_option (	OM_uint32 *,	gss_ctx_id_t *,	const gss_OID,	const gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_set_sec_context_option (	OM_uint32 *minor_status,	gss_ctx_id_t *context_handle,	const gss_OID object,	const gss_buffer_t value); ``` |

Modified [gss_sign()](https://developer.apple.com/documentation/gss/1438416-gss_sign)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_sign (	OM_uint32 *,	gss_ctx_id_t,	int,	gss_buffer_t,	gss_buffer_t); ``` | OS X 10.7 |
| To | ``` OM_uint32 gss_sign (	OM_uint32 *minor_status,	gss_ctx_id_t context_handle,	int qop_req,	gss_buffer_t message_buffer,	gss_buffer_t message_token); ``` | OS X 10.9 |

Modified [gss_test_oid_set_member()](https://developer.apple.com/documentation/gss/1438442-gss_test_oid_set_member)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_test_oid_set_member (	OM_uint32 *,	gss_const_OID,	const gss_OID_set,	int *); ``` |
| To | ``` OM_uint32 gss_test_oid_set_member (	OM_uint32 *minor_status,	gss_const_OID member,	const gss_OID_set set,	int *present); ``` |

Modified [gss_unseal()](https://developer.apple.com/documentation/gss/1438456-gss_unseal)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_unseal (	OM_uint32 *,	gss_ctx_id_t,	gss_buffer_t,	gss_buffer_t,	int *,	int *); ``` | OS X 10.7 |
| To | ``` OM_uint32 gss_unseal (	OM_uint32 *minor_status,	gss_ctx_id_t context_handle,	gss_buffer_t input_message_buffer,	gss_buffer_t output_message_buffer,	int *conf_state,	int *qop_state); ``` | OS X 10.9 |

Modified [gss_unwrap()](https://developer.apple.com/documentation/gss/1438520-gss_unwrap)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_unwrap (	OM_uint32 *,	const gss_ctx_id_t,	const gss_buffer_t,	gss_buffer_t,	int *,	gss_qop_t *); ``` |
| To | ``` OM_uint32 gss_unwrap (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	const gss_buffer_t input_message_buffer,	gss_buffer_t output_message_buffer,	int *conf_state,	gss_qop_t *qop_state); ``` |

Modified [gss_userok()](https://developer.apple.com/documentation/gss/1438440-gss_userok)

|  | Declaration |
| --- | --- |
| From | ``` int gss_userok (	const gss_name_t,	const char *); ``` |
| To | ``` int gss_userok (	const gss_name_t name,	const char *user); ``` |

Modified [gss_verify()](https://developer.apple.com/documentation/gss/1438414-gss_verify)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OM_uint32 gss_verify (	OM_uint32 *,	gss_ctx_id_t,	gss_buffer_t,	gss_buffer_t,	int *); ``` | OS X 10.7 |
| To | ``` OM_uint32 gss_verify (	OM_uint32 *minor_status,	gss_ctx_id_t context_handle,	gss_buffer_t message_buffer,	gss_buffer_t token_buffer,	int *qop_state); ``` | OS X 10.9 |

Modified [gss_verify_mic()](https://developer.apple.com/documentation/gss/1438447-gss_verify_mic)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_verify_mic (	OM_uint32 *,	const gss_ctx_id_t,	const gss_buffer_t,	const gss_buffer_t,	gss_qop_t *); ``` |
| To | ``` OM_uint32 gss_verify_mic (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	const gss_buffer_t message_buffer,	const gss_buffer_t token_buffer,	gss_qop_t *qop_state); ``` |

Modified [gss_wrap()](https://developer.apple.com/documentation/gss/1438527-gss_wrap)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_wrap (	OM_uint32 *,	const gss_ctx_id_t,	int,	gss_qop_t,	const gss_buffer_t,	int *,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gss_wrap (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	int conf_req_flag,	gss_qop_t qop_req,	const gss_buffer_t input_message_buffer,	int *conf_state,	gss_buffer_t output_message_buffer); ``` |

Modified [gss_wrap_size_limit()](https://developer.apple.com/documentation/gss/1438419-gss_wrap_size_limit)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_wrap_size_limit (	OM_uint32 *,	const gss_ctx_id_t,	int,	gss_qop_t,	OM_uint32,	OM_uint32 *); ``` |
| To | ``` OM_uint32 gss_wrap_size_limit (	OM_uint32 *minor_status,	const gss_ctx_id_t context_handle,	int conf_req_flag,	gss_qop_t qop_req,	OM_uint32 req_output_size,	OM_uint32 *max_input_size); ``` |

Modified [gsskrb5_extract_authz_data_from_sec_context()](https://developer.apple.com/documentation/gss/1438468-gsskrb5_extract_authz_data_from_)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gsskrb5_extract_authz_data_from_sec_context (	OM_uint32 *,	gss_ctx_id_t,	int,	gss_buffer_t); ``` |
| To | ``` OM_uint32 gsskrb5_extract_authz_data_from_sec_context (	OM_uint32 *minor_status,	gss_ctx_id_t context_handle,	int ad_type,	gss_buffer_t ad_data); ``` |

Modified [gsskrb5_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438421-gsskrb5_register_acceptor_identi)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gsskrb5_register_acceptor_identity (	const char *); ``` |
| To | ``` OM_uint32 gsskrb5_register_acceptor_identity (	const char *identity); ``` |

Modified [krb5_gss_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438470-krb5_gss_register_acceptor_ident)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 krb5_gss_register_acceptor_identity (	const char *); ``` |
| To | ``` OM_uint32 krb5_gss_register_acceptor_identity (	const char *identity); ``` |

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
