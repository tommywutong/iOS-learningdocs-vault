---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Objective-C/GSS.html
archived_at: '2026-07-18T02:57:04.846777Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# GSS Changes for Objective-C

### GSS

#### gssapi_apple.h

Modified [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_aapl_change_password (     gss_name_t  _Nonnull const name,     gss_const_OID _Nonnull mech,     CFDictionaryRef _Nonnull attributes,     CFErrorRef  _Nullable * _Nullable error ); ``` |
| To | ``` OM_uint32 gss_aapl_change_password (     gss_name_t name,     gss_const_OID mech,     CFDictionaryRef attributes,     CFErrorRef  _Nullable *error ); ``` |

Modified [gss_aapl_initial_cred()](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_aapl_initial_cred (     gss_name_t  _Nonnull const desired_name,     gss_const_OID _Nonnull desired_mech,     CFDictionaryRef _Nullable attributes,     gss_cred_id_t  _Nonnull * _Nullable output_cred_handle,     CFErrorRef  _Nullable * _Nullable error ); ``` |
| To | ``` OM_uint32 gss_aapl_initial_cred (     gss_name_t desired_name,     gss_const_OID desired_mech,     CFDictionaryRef attributes,     gss_cred_id_t  _Nonnull *output_cred_handle,     CFErrorRef  _Nullable *error ); ``` |

#### gssapi_protos.h

Modified [gss_accept_sec_context()](https://developer.apple.com/documentation/gss/1438493-gss_accept_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_accept_sec_context (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull * _Nullable context_handle,     gss_cred_id_t  _Nullable const acceptor_cred_handle,     gss_buffer_t  _Nullable const input_token,     gss_channel_bindings_t  _Nullable const input_chan_bindings,     gss_name_t  _Nullable * _Nullable src_name,     gss_OID  _Nullable * _Nullable mech_type,     gss_buffer_t _Nonnull output_token,     OM_uint32 * _Nullable ret_flags,     OM_uint32 * _Nullable time_rec,     gss_cred_id_t  _Nullable * _Nullable delegated_cred_handle ); ``` |
| To | ``` OM_uint32 gss_accept_sec_context (     OM_uint32 *minor_status,     gss_ctx_id_t  _Nonnull *context_handle,     gss_cred_id_t acceptor_cred_handle,     gss_buffer_t input_token,     gss_channel_bindings_t input_chan_bindings,     gss_name_t  _Nullable *src_name,     gss_OID  _Nullable *mech_type,     gss_buffer_t output_token,     OM_uint32 *ret_flags,     OM_uint32 *time_rec,     gss_cred_id_t  _Nullable *delegated_cred_handle ); ``` |

Modified [gss_acquire_cred()](https://developer.apple.com/documentation/gss/1438466-gss_acquire_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_acquire_cred (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nullable const desired_name,     OM_uint32 time_req,     gss_OID_set  _Nullable const desired_mechs,     gss_cred_usage_t cred_usage,     gss_cred_id_t  _Nonnull * _Nullable output_cred_handle,     gss_OID_set  _Nullable * _Nullable actual_mechs,     OM_uint32 * _Nullable time_rec ); ``` |
| To | ``` OM_uint32 gss_acquire_cred (     OM_uint32 *minor_status,     gss_name_t desired_name,     OM_uint32 time_req,     gss_OID_set desired_mechs,     gss_cred_usage_t cred_usage,     gss_cred_id_t  _Nonnull *output_cred_handle,     gss_OID_set  _Nullable *actual_mechs,     OM_uint32 *time_rec ); ``` |

Modified [gss_acquire_cred_with_password()](https://developer.apple.com/documentation/gss/1438426-gss_acquire_cred_with_password)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_acquire_cred_with_password (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const desired_name,     gss_buffer_t  _Nonnull const password,     OM_uint32 time_req,     gss_OID_set  _Nullable const desired_mechs,     gss_cred_usage_t cred_usage,     gss_cred_id_t  _Nonnull * _Nullable output_cred_handle,     gss_OID_set  _Nullable * _Nullable actual_mechs,     OM_uint32 * _Nullable time_rec ); ``` |
| To | ``` OM_uint32 gss_acquire_cred_with_password (     OM_uint32 *minor_status,     gss_name_t desired_name,     gss_buffer_t password,     OM_uint32 time_req,     gss_OID_set desired_mechs,     gss_cred_usage_t cred_usage,     gss_cred_id_t  _Nonnull *output_cred_handle,     gss_OID_set  _Nullable *actual_mechs,     OM_uint32 *time_rec ); ``` |

Modified [gss_add_buffer_set_member()](https://developer.apple.com/documentation/gss/1438479-gss_add_buffer_set_member)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_add_buffer_set_member (     OM_uint32 * _Nonnull minor_status,     gss_buffer_t  _Nonnull const member_buffer,     gss_buffer_set_t  _Nonnull * _Nonnull buffer_set ); ``` |
| To | ``` OM_uint32 gss_add_buffer_set_member (     OM_uint32 *minor_status,     gss_buffer_t member_buffer,     gss_buffer_set_t  _Nonnull *buffer_set ); ``` |

Modified [gss_add_cred()](https://developer.apple.com/documentation/gss/1438473-gss_add_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_add_cred (     OM_uint32 * _Nonnull minor_status,     gss_cred_id_t  _Nullable const input_cred_handle,     gss_name_t  _Nullable const desired_name,     gss_OID  _Nullable const desired_mech,     gss_cred_usage_t cred_usage,     OM_uint32 initiator_time_req,     OM_uint32 acceptor_time_req,     gss_cred_id_t  _Nonnull * _Nullable output_cred_handle,     gss_OID_set  _Nullable * _Nullable actual_mechs,     OM_uint32 * _Nullable initiator_time_rec,     OM_uint32 * _Nullable acceptor_time_rec ); ``` |
| To | ``` OM_uint32 gss_add_cred (     OM_uint32 *minor_status,     gss_cred_id_t input_cred_handle,     gss_name_t desired_name,     gss_OID desired_mech,     gss_cred_usage_t cred_usage,     OM_uint32 initiator_time_req,     OM_uint32 acceptor_time_req,     gss_cred_id_t  _Nonnull *output_cred_handle,     gss_OID_set  _Nullable *actual_mechs,     OM_uint32 *initiator_time_rec,     OM_uint32 *acceptor_time_rec ); ``` |

Modified [gss_canonicalize_name()](https://developer.apple.com/documentation/gss/1438494-gss_canonicalize_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_canonicalize_name (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const input_name,     gss_OID  _Nonnull const mech_type,     gss_name_t  _Nonnull * _Nullable output_name ); ``` |
| To | ``` OM_uint32 gss_canonicalize_name (     OM_uint32 *minor_status,     gss_name_t input_name,     gss_OID mech_type,     gss_name_t  _Nonnull *output_name ); ``` |

Modified [gss_compare_name()](https://developer.apple.com/documentation/gss/1438437-gss_compare_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_compare_name (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const name1_arg,     gss_name_t  _Nonnull const name2_arg,     int * _Nonnull name_equal ); ``` |
| To | ``` OM_uint32 gss_compare_name (     OM_uint32 *minor_status,     gss_name_t name1_arg,     gss_name_t name2_arg,     int *name_equal ); ``` |

Modified [gss_context_time()](https://developer.apple.com/documentation/gss/1438487-gss_context_time)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_context_time (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     OM_uint32 * _Nonnull time_rec ); ``` |
| To | ``` OM_uint32 gss_context_time (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     OM_uint32 *time_rec ); ``` |

Modified [gss_display_name()](https://developer.apple.com/documentation/gss/1438464-gss_display_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_display_name (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const input_name,     gss_buffer_t _Nonnull output_name_buffer,     gss_OID  _Nullable * _Nullable output_name_type ); ``` |
| To | ``` OM_uint32 gss_display_name (     OM_uint32 *minor_status,     gss_name_t input_name,     gss_buffer_t output_name_buffer,     gss_OID  _Nullable *output_name_type ); ``` |

Modified [gss_display_status()](https://developer.apple.com/documentation/gss/1438535-gss_display_status)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_display_status (     OM_uint32 * _Nonnull minor_status,     OM_uint32 status_value,     int status_type,     gss_OID  _Nullable const mech_type,     OM_uint32 * _Nonnull message_content,     gss_buffer_t _Nonnull status_string ); ``` |
| To | ``` OM_uint32 gss_display_status (     OM_uint32 *minor_status,     OM_uint32 status_value,     int status_type,     gss_OID mech_type,     OM_uint32 *message_content,     gss_buffer_t status_string ); ``` |

Modified [gss_duplicate_name()](https://developer.apple.com/documentation/gss/1438418-gss_duplicate_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_duplicate_name (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const src_name,     gss_name_t  _Nonnull * _Nullable dest_name ); ``` |
| To | ``` OM_uint32 gss_duplicate_name (     OM_uint32 *minor_status,     gss_name_t src_name,     gss_name_t  _Nonnull *dest_name ); ``` |

Modified [gss_export_name()](https://developer.apple.com/documentation/gss/1438477-gss_export_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_export_name (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const input_name,     gss_buffer_t _Nonnull exported_name ); ``` |
| To | ``` OM_uint32 gss_export_name (     OM_uint32 *minor_status,     gss_name_t input_name,     gss_buffer_t exported_name ); ``` |

Modified [gss_get_mic()](https://developer.apple.com/documentation/gss/1438530-gss_get_mic)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_get_mic (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     gss_qop_t qop_req,     gss_buffer_t  _Nonnull const message_buffer,     gss_buffer_t _Nonnull message_token ); ``` |
| To | ``` OM_uint32 gss_get_mic (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     gss_qop_t qop_req,     gss_buffer_t message_buffer,     gss_buffer_t message_token ); ``` |

Modified [gss_import_name()](https://developer.apple.com/documentation/gss/1438453-gss_import_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_import_name (     OM_uint32 * _Nonnull minor_status,     gss_buffer_t  _Nonnull const input_name_buffer,     gss_const_OID _Nullable input_name_type,     gss_name_t  _Nonnull * _Nullable output_name ); ``` |
| To | ``` OM_uint32 gss_import_name (     OM_uint32 *minor_status,     gss_buffer_t input_name_buffer,     gss_const_OID input_name_type,     gss_name_t  _Nonnull *output_name ); ``` |

Modified [gss_import_sec_context()](https://developer.apple.com/documentation/gss/1438484-gss_import_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_import_sec_context (     OM_uint32 * _Nonnull minor_status,     gss_buffer_t  _Nonnull const interprocess_token,     gss_ctx_id_t  _Nonnull * _Nullable context_handle ); ``` |
| To | ``` OM_uint32 gss_import_sec_context (     OM_uint32 *minor_status,     gss_buffer_t interprocess_token,     gss_ctx_id_t  _Nonnull *context_handle ); ``` |

Modified [gss_init_sec_context()](https://developer.apple.com/documentation/gss/1438476-gss_init_sec_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_init_sec_context (     OM_uint32 * _Nonnull minor_status,     gss_cred_id_t  _Nullable const initiator_cred_handle,     gss_ctx_id_t  _Nonnull * _Nullable context_handle,     gss_name_t  _Nonnull const target_name,     gss_OID  _Nullable const input_mech_type,     OM_uint32 req_flags,     OM_uint32 time_req,     gss_channel_bindings_t  _Nullable const input_chan_bindings,     gss_buffer_t  _Nullable const input_token,     gss_OID  _Nullable * _Nullable actual_mech_type,     gss_buffer_t _Nonnull output_token,     OM_uint32 * _Nullable ret_flags,     OM_uint32 * _Nullable time_rec ); ``` |
| To | ``` OM_uint32 gss_init_sec_context (     OM_uint32 *minor_status,     gss_cred_id_t initiator_cred_handle,     gss_ctx_id_t  _Nonnull *context_handle,     gss_name_t target_name,     gss_OID input_mech_type,     OM_uint32 req_flags,     OM_uint32 time_req,     gss_channel_bindings_t input_chan_bindings,     gss_buffer_t input_token,     gss_OID  _Nullable *actual_mech_type,     gss_buffer_t output_token,     OM_uint32 *ret_flags,     OM_uint32 *time_rec ); ``` |

Modified [gss_inquire_context()](https://developer.apple.com/documentation/gss/1438458-gss_inquire_context)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_context (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     gss_name_t  _Nullable * _Nullable src_name,     gss_name_t  _Nullable * _Nullable targ_name,     OM_uint32 * _Nullable lifetime_rec,     gss_OID  _Nullable * _Nullable mech_type,     OM_uint32 * _Nullable ctx_flags,     int * _Nullable locally_initiated,     int * _Nullable xopen ); ``` |
| To | ``` OM_uint32 gss_inquire_context (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     gss_name_t  _Nullable *src_name,     gss_name_t  _Nullable *targ_name,     OM_uint32 *lifetime_rec,     gss_OID  _Nullable *mech_type,     OM_uint32 *ctx_flags,     int *locally_initiated,     int *xopen ); ``` |

Modified [gss_inquire_cred()](https://developer.apple.com/documentation/gss/1438531-gss_inquire_cred)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_cred (     OM_uint32 * _Nonnull minor_status,     gss_cred_id_t  _Nullable const cred_handle,     gss_name_t  _Nullable * _Nullable name_ret,     OM_uint32 * _Nullable lifetime,     gss_cred_usage_t * _Nullable cred_usage,     gss_OID_set  _Nullable * _Nullable mechanisms ); ``` |
| To | ``` OM_uint32 gss_inquire_cred (     OM_uint32 *minor_status,     gss_cred_id_t cred_handle,     gss_name_t  _Nullable *name_ret,     OM_uint32 *lifetime,     gss_cred_usage_t *cred_usage,     gss_OID_set  _Nullable *mechanisms ); ``` |

Modified [gss_inquire_cred_by_mech()](https://developer.apple.com/documentation/gss/1438518-gss_inquire_cred_by_mech)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_cred_by_mech (     OM_uint32 * _Nonnull minor_status,     gss_cred_id_t  _Nullable const cred_handle,     gss_OID  _Nonnull const mech_type,     gss_name_t  _Nullable * _Nullable cred_name,     OM_uint32 * _Nullable initiator_lifetime,     OM_uint32 * _Nullable acceptor_lifetime,     gss_cred_usage_t * _Nullable cred_usage ); ``` |
| To | ``` OM_uint32 gss_inquire_cred_by_mech (     OM_uint32 *minor_status,     gss_cred_id_t cred_handle,     gss_OID mech_type,     gss_name_t  _Nullable *cred_name,     OM_uint32 *initiator_lifetime,     OM_uint32 *acceptor_lifetime,     gss_cred_usage_t *cred_usage ); ``` |

Modified [gss_inquire_cred_by_oid()](https://developer.apple.com/documentation/gss/1438504-gss_inquire_cred_by_oid)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_cred_by_oid (     OM_uint32 * _Nonnull minor_status,     gss_cred_id_t  _Nonnull const cred_handle,     gss_OID  _Nonnull const desired_object,     gss_buffer_set_t  _Nonnull * _Nullable data_set ); ``` |
| To | ``` OM_uint32 gss_inquire_cred_by_oid (     OM_uint32 *minor_status,     gss_cred_id_t cred_handle,     gss_OID desired_object,     gss_buffer_set_t  _Nonnull *data_set ); ``` |

Modified [gss_inquire_mech_for_saslname()](https://developer.apple.com/documentation/gss/1438514-gss_inquire_mech_for_saslname)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_mech_for_saslname (     OM_uint32 * _Nonnull minor_status,     gss_buffer_t  _Nullable const sasl_mech_name,     gss_OID  _Nullable * _Nullable mech_type ); ``` |
| To | ``` OM_uint32 gss_inquire_mech_for_saslname (     OM_uint32 *minor_status,     gss_buffer_t sasl_mech_name,     gss_OID  _Nullable *mech_type ); ``` |

Modified [gss_inquire_mechs_for_name()](https://developer.apple.com/documentation/gss/1438481-gss_inquire_mechs_for_name)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_mechs_for_name (     OM_uint32 * _Nonnull minor_status,     gss_name_t  _Nonnull const input_name,     gss_OID_set  _Nonnull * _Nullable mech_types ); ``` |
| To | ``` OM_uint32 gss_inquire_mechs_for_name (     OM_uint32 *minor_status,     gss_name_t input_name,     gss_OID_set  _Nonnull *mech_types ); ``` |

Modified [gss_inquire_saslname_for_mech()](https://developer.apple.com/documentation/gss/1438445-gss_inquire_saslname_for_mech)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_saslname_for_mech (     OM_uint32 * _Nonnull minor_status,     gss_OID  _Nonnull const desired_mech,     gss_buffer_t _Nullable sasl_mech_name,     gss_buffer_t _Nullable mech_name,     gss_buffer_t _Nullable mech_description ); ``` |
| To | ``` OM_uint32 gss_inquire_saslname_for_mech (     OM_uint32 *minor_status,     gss_OID desired_mech,     gss_buffer_t sasl_mech_name,     gss_buffer_t mech_name,     gss_buffer_t mech_description ); ``` |

Modified [gss_inquire_sec_context_by_oid()](https://developer.apple.com/documentation/gss/1438525-gss_inquire_sec_context_by_oid)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_inquire_sec_context_by_oid (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     gss_OID  _Nonnull const desired_object,     gss_buffer_set_t  _Nonnull * _Nullable data_set ); ``` |
| To | ``` OM_uint32 gss_inquire_sec_context_by_oid (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     gss_OID desired_object,     gss_buffer_set_t  _Nonnull *data_set ); ``` |

Modified [gss_process_context_token()](https://developer.apple.com/documentation/gss/1438516-gss_process_context_token)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_process_context_token (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     gss_buffer_t  _Nonnull const token_buffer ); ``` |
| To | ``` OM_uint32 gss_process_context_token (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     gss_buffer_t token_buffer ); ``` |

Modified [gss_pseudo_random()](https://developer.apple.com/documentation/gss/1438496-gss_pseudo_random)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_pseudo_random (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t _Nonnull context,     int prf_key,     gss_buffer_t  _Nonnull const prf_in,     ssize_t desired_output_len,     gss_buffer_t _Nonnull prf_out ); ``` |
| To | ``` OM_uint32 gss_pseudo_random (     OM_uint32 *minor_status,     gss_ctx_id_t context,     int prf_key,     gss_buffer_t prf_in,     ssize_t desired_output_len,     gss_buffer_t prf_out ); ``` |

Modified [gss_set_cred_option()](https://developer.apple.com/documentation/gss/1438513-gss_set_cred_option)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_set_cred_option (     OM_uint32 * _Nonnull minor_status,     gss_cred_id_t  _Nullable * _Nullable cred_handle,     gss_OID  _Nonnull const object,     gss_buffer_t  _Nullable const value ); ``` |
| To | ``` OM_uint32 gss_set_cred_option (     OM_uint32 *minor_status,     gss_cred_id_t  _Nullable *cred_handle,     gss_OID object,     gss_buffer_t value ); ``` |

Modified [gss_set_sec_context_option()](https://developer.apple.com/documentation/gss/1438491-gss_set_sec_context_option)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_set_sec_context_option (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull * _Nullable context_handle,     gss_OID  _Nonnull const object,     gss_buffer_t  _Nullable const value ); ``` |
| To | ``` OM_uint32 gss_set_sec_context_option (     OM_uint32 *minor_status,     gss_ctx_id_t  _Nonnull *context_handle,     gss_OID object,     gss_buffer_t value ); ``` |

Modified [gss_test_oid_set_member()](https://developer.apple.com/documentation/gss/1438442-gss_test_oid_set_member)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_test_oid_set_member (     OM_uint32 * _Nonnull minor_status,     gss_const_OID _Nonnull member,     gss_OID_set  _Nonnull const set,     int * _Nonnull present ); ``` |
| To | ``` OM_uint32 gss_test_oid_set_member (     OM_uint32 *minor_status,     gss_const_OID member,     gss_OID_set set,     int *present ); ``` |

Modified [gss_unwrap()](https://developer.apple.com/documentation/gss/1438520-gss_unwrap)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_unwrap (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     gss_buffer_t  _Nonnull const input_message_buffer,     gss_buffer_t _Nonnull output_message_buffer,     int * _Nullable conf_state,     gss_qop_t * _Nullable qop_state ); ``` |
| To | ``` OM_uint32 gss_unwrap (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     gss_buffer_t input_message_buffer,     gss_buffer_t output_message_buffer,     int *conf_state,     gss_qop_t *qop_state ); ``` |

Modified [gss_userok()](https://developer.apple.com/documentation/gss/1438440-gss_userok)

|  | Declaration |
| --- | --- |
| From | ``` int gss_userok (     gss_name_t  _Nonnull const name,     const char * _Nonnull user ); ``` |
| To | ``` int gss_userok (     gss_name_t name,     const char *user ); ``` |

Modified [gss_verify_mic()](https://developer.apple.com/documentation/gss/1438447-gss_verify_mic)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_verify_mic (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     gss_buffer_t  _Nonnull const message_buffer,     gss_buffer_t  _Nonnull const token_buffer,     gss_qop_t * _Nullable qop_state ); ``` |
| To | ``` OM_uint32 gss_verify_mic (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     gss_buffer_t message_buffer,     gss_buffer_t token_buffer,     gss_qop_t *qop_state ); ``` |

Modified [gss_wrap()](https://developer.apple.com/documentation/gss/1438527-gss_wrap)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_wrap (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     int conf_req_flag,     gss_qop_t qop_req,     gss_buffer_t  _Nonnull const input_message_buffer,     int * _Nullable conf_state,     gss_buffer_t _Nonnull output_message_buffer ); ``` |
| To | ``` OM_uint32 gss_wrap (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     int conf_req_flag,     gss_qop_t qop_req,     gss_buffer_t input_message_buffer,     int *conf_state,     gss_buffer_t output_message_buffer ); ``` |

Modified [gss_wrap_size_limit()](https://developer.apple.com/documentation/gss/1438419-gss_wrap_size_limit)

|  | Declaration |
| --- | --- |
| From | ``` OM_uint32 gss_wrap_size_limit (     OM_uint32 * _Nonnull minor_status,     gss_ctx_id_t  _Nonnull const context_handle,     int conf_req_flag,     gss_qop_t qop_req,     OM_uint32 req_output_size,     OM_uint32 * _Nonnull max_input_size ); ``` |
| To | ``` OM_uint32 gss_wrap_size_limit (     OM_uint32 *minor_status,     gss_ctx_id_t context_handle,     int conf_req_flag,     gss_qop_t qop_req,     OM_uint32 req_output_size,     OM_uint32 *max_input_size ); ``` |

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
