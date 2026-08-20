---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/GSS.html
archived_at: '2026-07-18T02:54:01.306501Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# GSS Changes

## GSS

gssapi.hRemoved #def GSSAPI_DEPRECATEDRemoved gss_store_cred()Added #def GSSAPI_CALLCONVAdded #def GSS_C_ATTR_LOCAL_LOGIN_USERAdded [#def GSS_IOV_BUFFER_FLAG_ALLOCATE](https://developer.apple.com/documentation/gss/gss_iov_buffer_flag_allocate)Added [#def GSS_IOV_BUFFER_FLAG_ALLOCATED](https://developer.apple.com/documentation/gss/gss_iov_buffer_flag_allocated)Added [#def GSS_S_BAD_MECH_ATTR](https://developer.apple.com/documentation/gss/gss_s_bad_mech_attr)Added [#def GSS_S_CRED_UNAVAIL](https://developer.apple.com/documentation/gss/gss_s_cred_unavail)Added [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)Added [gss_const_OID](https://developer.apple.com/documentation/gss/gss_const_oid)Added [gss_const_OID_set](https://developer.apple.com/documentation/gss/gss_const_oid_set)Added [gss_const_buffer_t](https://developer.apple.com/documentation/gss/gss_const_buffer_t)Added [gss_const_channel_bindings_t](https://developer.apple.com/documentation/gss/gss_const_channel_bindings_t)Added [gss_const_cred_id_t](https://developer.apple.com/documentation/gss/gss_const_cred_id_t)Added [gss_const_ctx_id_t](https://developer.apple.com/documentation/gss/gss_const_ctx_id_t)Added [gss_const_name_t](https://developer.apple.com/documentation/gss/gss_const_name_t)Added #def gss_iter_OIDAdded [#def kGSSChangePasswordNewPassword](https://developer.apple.com/documentation/gss/kgsschangepasswordnewpassword)Added [#def kGSSChangePasswordOldPassword](https://developer.apple.com/documentation/gss/kgsschangepasswordoldpassword)Added [#def kGSSICVerifyCredential](https://developer.apple.com/documentation/gss/kgssicverifycredential)gssapi_apple.hAdded #def GSS_LIB_CALLAdded #def GSS_LIB_FUNCTIONAdded #def GSS_LIB_VARIABLEModified [gss_aapl_initial_cred()](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_aapl_initial_cred ( const gss_name_t, const gss_OID, CFDictionaryRef, gss_cred_id_t \*, CFErrorRef \*); |
| To | gssapi_apple.h | OM_uint32 gss_aapl_initial_cred ( const gss_name_t, gss_const_OID, CFDictionaryRef, gss_cred_id_t \*, CFErrorRef \*); |

gssapi_oid.hAdded #def GSSAPI_GSSAPI_OIDAdded #def GSS_APPL_LKDC_SUPPORTEDAdded #def GSS_C_CRED_CERTIFICATEAdded #def GSS_C_CRED_DIAGAdded #def GSS_C_CRED_GET_DEFAULTAdded #def GSS_C_CRED_PASSWORDAdded #def GSS_C_CRED_RENEWAdded #def GSS_C_CRED_SET_DEFAULTAdded #def GSS_C_CRED_SecIdentityAdded #def GSS_C_CRED_VALIDATEAdded #def GSS_C_MA_AUTH_INITAdded #def GSS_C_MA_AUTH_INIT_ANONAdded #def GSS_C_MA_AUTH_INIT_INITAdded #def GSS_C_MA_AUTH_TARGAdded #def GSS_C_MA_AUTH_TARG_ANONAdded #def GSS_C_MA_AUTH_TARG_INITAdded #def GSS_C_MA_CBINDINGSAdded #def GSS_C_MA_COMPRESSAdded #def GSS_C_MA_CONF_PROTAdded #def GSS_C_MA_CTX_TRANSAdded #def GSS_C_MA_DELEG_CREDAdded #def GSS_C_MA_DEPRECATEDAdded #def GSS_C_MA_INTEG_PROTAdded #def GSS_C_MA_ITOK_FRAMEDAdded #def GSS_C_MA_MECH_COMPOSITEAdded #def GSS_C_MA_MECH_CONCRETEAdded #def GSS_C_MA_MECH_DESCRIPTIONAdded #def GSS_C_MA_MECH_GLUEAdded #def GSS_C_MA_MECH_NAMEAdded #def GSS_C_MA_MECH_NEGOAdded #def GSS_C_MA_MECH_PSEUDOAdded #def GSS_C_MA_MICAdded #def GSS_C_MA_NOT_DFLT_MECHAdded #def GSS_C_MA_NOT_MECHAdded #def GSS_C_MA_OOS_DETAdded #def GSS_C_MA_PFSAdded #def GSS_C_MA_PROT_READYAdded #def GSS_C_MA_REPLAY_DETAdded #def GSS_C_MA_SASL_MECH_NAMEAdded #def GSS_C_MA_WRAPAdded #def GSS_C_NTLM_RESET_KEYSAdded #def GSS_C_NT_UUIDModified #def GSS_C_NTLM_V1

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_AUTHTIME_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_SERVICE_KEYBLOCK_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_IAKERB_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NTLM_SUPPORT_CHANNELBINDINGS

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SEND_TO_KDC_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_DEFAULT_REALM_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_IMPORT_CRED_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NT_NTLM

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_NETLOGON_SET_SESSION_KEY_X

|  | Header |
| --- | --- |
| From | gssapi_netlogon.h |
| To | gssapi_oid.h |

Modified #def GSS_NETLOGON_NT_NETBIOS_DNS_NAME

|  | Header |
| --- | --- |
| From | gssapi_netlogon.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_CCACHE_NAME_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_NTLM_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_NETLOGON_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_netlogon.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_TKT_FLAGS_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NT_DN

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_TIME_OFFSET_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_NTLM_GET_SESSION_KEY_X

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_PKU2U_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_COMPAT_DES3_MIC_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_EXPORT_LUCID_CONTEXT_V1_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_PEER_HAS_UPDATED_SPNEGO

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NTLM_SUPPORT_LM2

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_EXPORT_LUCID_CONTEXT_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_SUBKEY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_DNS_CANONICALIZE_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_TIME_OFFSET_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_PLUGIN_REGISTER_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NTLM_V2

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NTLM_GUEST

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_CRED_NO_CI_FLAGS_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_COPY_CCACHE_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NTLM_SESSION_KEY

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_EXTRACT_AUTHZ_DATA_FROM_SEC_CONTEXT_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_C_NTLM_FORCE_V1

|  | Header |
| --- | --- |
| From | gssapi_ntlm.h |
| To | gssapi_oid.h |

Modified #def GSS_SPNEGO_MECHANISM

|  | Header |
| --- | --- |
| From | gssapi_spnego.h |
| To | gssapi_oid.h |

Modified #def GSS_NETLOGON_SET_SIGN_ALGORITHM_X

|  | Header |
| --- | --- |
| From | gssapi_netlogon.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_INITIATOR_SUBKEY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_SET_ALLOWABLE_ENCTYPES_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_GET_ACCEPTOR_SUBKEY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

Modified #def GSS_KRB5_REGISTER_ACCEPTOR_IDENTITY_X

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_oid.h |

gssapi_protos.hAdded [gss_acquire_cred_with_password()](https://developer.apple.com/documentation/gss/1438426-gss_acquire_cred_with_password)Added [gss_decapsulate_token()](https://developer.apple.com/documentation/gss/1438529-gss_decapsulate_token)Added [gss_display_mech_attr()](https://developer.apple.com/documentation/gss/1438475-gss_display_mech_attr)Added [gss_encapsulate_token()](https://developer.apple.com/documentation/gss/1438463-gss_encapsulate_token)Added [gss_export_cred()](https://developer.apple.com/documentation/gss/1438500-gss_export_cred)Added [gss_import_cred()](https://developer.apple.com/documentation/gss/1438510-gss_import_cred)Added [gss_inquire_attrs_for_mech()](https://developer.apple.com/documentation/gss/1438417-gss_inquire_attrs_for_mech)Modified [gss_pseudo_random()](https://developer.apple.com/documentation/gss/1438496-gss_pseudo_random)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_pseudo_random ( OM_uint32 \*minor_status, gss_ctx_id_t context, int prf_key, const gss_buffer_t prf_in, ssize_t desired_output_len, gss_buffer_t prf_out); |
| To | gssapi_protos.h | OM_uint32 gss_pseudo_random ( OM_uint32 \*, gss_ctx_id_t, int, const gss_buffer_t, ssize_t, gss_buffer_t); |

Modified [gss_inquire_cred_by_oid()](https://developer.apple.com/documentation/gss/1438504-gss_inquire_cred_by_oid)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_inquire_cred_by_oid ( OM_uint32 \*minor_status, const gss_cred_id_t cred_handle, const gss_OID desired_object, gss_buffer_set_t \*data_set); |
| To | gssapi_protos.h | OM_uint32 gss_inquire_cred_by_oid ( OM_uint32 \*, const gss_cred_id_t, const gss_OID, gss_buffer_set_t \*); |

Modified [gss_set_sec_context_option()](https://developer.apple.com/documentation/gss/1438491-gss_set_sec_context_option)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_set_sec_context_option ( OM_uint32 \*minor_status, gss_ctx_id_t \*context_handle, const gss_OID desired_object, const gss_buffer_t value); |
| To | gssapi_protos.h | OM_uint32 gss_set_sec_context_option ( OM_uint32 \*, gss_ctx_id_t \*, const gss_OID, const gss_buffer_t); |

Modified [gss_release_buffer()](https://developer.apple.com/documentation/gss/1438486-gss_release_buffer)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_acquire_cred()](https://developer.apple.com/documentation/gss/1438466-gss_acquire_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_duplicate_oid()](https://developer.apple.com/documentation/gss/1438533-gss_duplicate_oid)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_duplicate_oid ( OM_uint32 \*, gss_OID, gss_OID \*); |
| To | gssapi_protos.h | OM_uint32 gss_duplicate_oid ( OM_uint32 \*, gss_OID, gss_OID \*dest_oid); |

Modified [gss_add_oid_set_member()](https://developer.apple.com/documentation/gss/1438411-gss_add_oid_set_member)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_add_oid_set_member ( OM_uint32 \*, const gss_OID, gss_OID_set \*); |
| To | gssapi_protos.h | OM_uint32 gss_add_oid_set_member ( OM_uint32 \*, gss_const_OID, gss_OID_set \*); |

Modified [gss_wrap()](https://developer.apple.com/documentation/gss/1438527-gss_wrap)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_wrap_size_limit()](https://developer.apple.com/documentation/gss/1438419-gss_wrap_size_limit)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_oid()](https://developer.apple.com/documentation/gss/1438455-gss_release_oid)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_free_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438483-gss_krb5_free_lucid_sec_context)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi_krb5.h | OM_uint32 gss_krb5_free_lucid_sec_context ( OM_uint32 \*minor_status, void \*kctx); |
| To | gssapi_protos.h | OM_uint32 gss_krb5_free_lucid_sec_context ( OM_uint32 \*, void \*); |

Modified [gss_verify()](https://developer.apple.com/documentation/gss/1438414-gss_verify)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_name()](https://developer.apple.com/documentation/gss/1438451-gss_release_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_display_status()](https://developer.apple.com/documentation/gss/1438535-gss_display_status)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_duplicate_name()](https://developer.apple.com/documentation/gss/1438418-gss_duplicate_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_create_empty_oid_set()](https://developer.apple.com/documentation/gss/1438489-gss_create_empty_oid_set)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_ccache_name()](https://developer.apple.com/documentation/gss/1438472-gss_krb5_ccache_name)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_sign()](https://developer.apple.com/documentation/gss/1438416-gss_sign)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gsskrb5_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438421-gsskrb5_register_acceptor_identi)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_verify_mic()](https://developer.apple.com/documentation/gss/1438447-gss_verify_mic)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_destroy_cred()](https://developer.apple.com/documentation/gss/1438521-gss_destroy_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_add_cred()](https://developer.apple.com/documentation/gss/1438473-gss_add_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_context()](https://developer.apple.com/documentation/gss/1438458-gss_inquire_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_export_name()](https://developer.apple.com/documentation/gss/1438477-gss_export_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_cred()](https://developer.apple.com/documentation/gss/1438461-gss_release_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_iter_creds()](https://developer.apple.com/documentation/gss/1438515-gss_iter_creds)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_iter_creds ( OM_uint32 \*, OM_uint32 flags, gss_OID mech, void (^useriter)(gss_OID, gss_cred_id_t)); |
| To | gssapi_protos.h | OM_uint32 gss_iter_creds ( OM_uint32 \*, OM_uint32, gss_const_OID, void (^useriter)(gss_OID, gss_cred_id_t)); |

Modified [gss_create_empty_buffer_set()](https://developer.apple.com/documentation/gss/1438537-gss_create_empty_buffer_set)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_create_empty_buffer_set ( OM_uint32 \*minor_status, gss_buffer_set_t \*buffer_set); |
| To | gssapi_protos.h | OM_uint32 gss_create_empty_buffer_set ( OM_uint32 \*, gss_buffer_set_t \*); |

Modified [gss_display_name()](https://developer.apple.com/documentation/gss/1438464-gss_display_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_seal()](https://developer.apple.com/documentation/gss/1438459-gss_seal)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_oid_equal()](https://developer.apple.com/documentation/gss/1438498-gss_oid_equal)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | int gss_oid_equal ( const gss_OID a, const gss_OID b); |
| To | gssapi_protos.h | int gss_oid_equal ( gss_const_OID, gss_const_OID); |

Modified [gss_test_oid_set_member()](https://developer.apple.com/documentation/gss/1438442-gss_test_oid_set_member)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_test_oid_set_member ( OM_uint32 \*, const gss_OID, const gss_OID_set, int \*); |
| To | gssapi_protos.h | OM_uint32 gss_test_oid_set_member ( OM_uint32 \*, gss_const_OID, const gss_OID_set, int \*); |

Modified [gss_inquire_cred()](https://developer.apple.com/documentation/gss/1438531-gss_inquire_cred)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_get_mic()](https://developer.apple.com/documentation/gss/1438530-gss_get_mic)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_context_time()](https://developer.apple.com/documentation/gss/1438487-gss_context_time)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_krb5_copy_ccache()](https://developer.apple.com/documentation/gss/1438508-gss_krb5_copy_ccache)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_add_buffer_set_member()](https://developer.apple.com/documentation/gss/1438479-gss_add_buffer_set_member)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_add_buffer_set_member ( OM_uint32 \*minor_status, const gss_buffer_t member_buffer, gss_buffer_set_t \*buffer_set); |
| To | gssapi_protos.h | OM_uint32 gss_add_buffer_set_member ( OM_uint32 \*, const gss_buffer_t, gss_buffer_set_t \*); |

Modified [gsskrb5_extract_authz_data_from_sec_context()](https://developer.apple.com/documentation/gss/1438468-gsskrb5_extract_authz_data_from_)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_inquire_names_for_mech()](https://developer.apple.com/documentation/gss/1438523-gss_inquire_names_for_mech)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_inquire_names_for_mech ( OM_uint32 \*, const gss_OID, gss_OID_set \*); |
| To | gssapi_protos.h | OM_uint32 gss_inquire_names_for_mech ( OM_uint32 \*, gss_const_OID, gss_OID_set \*); |

Modified [gss_inquire_mechs_for_name()](https://developer.apple.com/documentation/gss/1438481-gss_inquire_mechs_for_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_compare_name()](https://developer.apple.com/documentation/gss/1438437-gss_compare_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_inquire_cred_by_mech()](https://developer.apple.com/documentation/gss/1438518-gss_inquire_cred_by_mech)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_init_sec_context()](https://developer.apple.com/documentation/gss/1438476-gss_init_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_unseal()](https://developer.apple.com/documentation/gss/1438456-gss_unseal)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_iter_creds_f()](https://developer.apple.com/documentation/gss/1438438-gss_iter_creds_f)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_iter_creds_f ( OM_uint32 \*, OM_uint32, gss_OID, void \*, void (\*)(void \*, gss_OID, gss_cred_id_t)); |
| To | gssapi_protos.h | OM_uint32 gss_iter_creds_f ( OM_uint32 \*, OM_uint32, gss_const_OID, void \*, void (\*)(void \*, gss_OID, gss_cred_id_t)); |

Modified [gss_release_oid_set()](https://developer.apple.com/documentation/gss/1438480-gss_release_oid_set)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_delete_sec_context()](https://developer.apple.com/documentation/gss/1438435-gss_delete_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [krb5_gss_register_acceptor_identity()](https://developer.apple.com/documentation/gss/1438470-krb5_gss_register_acceptor_ident)

|  | Header |
| --- | --- |
| From | gssapi_krb5.h |
| To | gssapi_protos.h |

Modified [gss_krb5_export_lucid_sec_context()](https://developer.apple.com/documentation/gss/1438433-gss_krb5_export_lucid_sec_contex)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi_krb5.h | OM_uint32 gss_krb5_export_lucid_sec_context ( OM_uint32 \*minor_status, gss_ctx_id_t \*context_handle, OM_uint32 version, void \*\*kctx); |
| To | gssapi_protos.h | OM_uint32 gss_krb5_export_lucid_sec_context ( OM_uint32 \*, gss_ctx_id_t \*, OM_uint32, void \*\*); |

Modified [gss_krb5_set_allowable_enctypes()](https://developer.apple.com/documentation/gss/1438431-gss_krb5_set_allowable_enctypes)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi_krb5.h | OM_uint32 gss_krb5_set_allowable_enctypes ( OM_uint32 \*minor_status, gss_cred_id_t cred, OM_uint32 num_enctypes, int32_t \*enctypes); |
| To | gssapi_protos.h | OM_uint32 gss_krb5_set_allowable_enctypes ( OM_uint32 \*, gss_cred_id_t, OM_uint32, int32_t \*); |

Modified [gss_import_name()](https://developer.apple.com/documentation/gss/1438453-gss_import_name)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_import_name ( OM_uint32 \*, const gss_buffer_t, const gss_OID, gss_name_t \*); |
| To | gssapi_protos.h | OM_uint32 gss_import_name ( OM_uint32 \*, const gss_buffer_t, gss_const_OID, gss_name_t \*); |

Modified [gss_unwrap()](https://developer.apple.com/documentation/gss/1438520-gss_unwrap)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_process_context_token()](https://developer.apple.com/documentation/gss/1438516-gss_process_context_token)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_release_buffer_set()](https://developer.apple.com/documentation/gss/1438428-gss_release_buffer_set)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_release_buffer_set ( OM_uint32 \*minor_status, gss_buffer_set_t \*buffer_set); |
| To | gssapi_protos.h | OM_uint32 gss_release_buffer_set ( OM_uint32 \*, gss_buffer_set_t \*); |

Modified [gss_inquire_sec_context_by_oid()](https://developer.apple.com/documentation/gss/1438525-gss_inquire_sec_context_by_oid)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_inquire_sec_context_by_oid ( OM_uint32 \*minor_status, const gss_ctx_id_t context_handle, const gss_OID desired_object, gss_buffer_set_t \*data_set); |
| To | gssapi_protos.h | OM_uint32 gss_inquire_sec_context_by_oid ( OM_uint32 \*, const gss_ctx_id_t, const gss_OID, gss_buffer_set_t \*); |

Modified [gss_import_sec_context()](https://developer.apple.com/documentation/gss/1438484-gss_import_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_accept_sec_context()](https://developer.apple.com/documentation/gss/1438493-gss_accept_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_set_cred_option()](https://developer.apple.com/documentation/gss/1438513-gss_set_cred_option)

|  | Header | Declaration |
| --- | --- | --- |
| From | gssapi.h | OM_uint32 gss_set_cred_option ( OM_uint32 \*minor_status, gss_cred_id_t \*cred_handle, const gss_OID object, const gss_buffer_t value); |
| To | gssapi_protos.h | OM_uint32 gss_set_cred_option ( OM_uint32 \*, gss_cred_id_t \*, const gss_OID, const gss_buffer_t); |

Modified [gss_export_sec_context()](https://developer.apple.com/documentation/gss/1438449-gss_export_sec_context)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_oid_to_str()](https://developer.apple.com/documentation/gss/1438512-gss_oid_to_str)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_canonicalize_name()](https://developer.apple.com/documentation/gss/1438494-gss_canonicalize_name)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

Modified [gss_indicate_mechs()](https://developer.apple.com/documentation/gss/1438424-gss_indicate_mechs)

|  | Header |
| --- | --- |
| From | gssapi.h |
| To | gssapi_protos.h |

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
