---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Security.html
archived_at: '2026-07-18T02:53:42.177356Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Security Changes for Swift

### Security

Removed AuthorizationItem.init()Removed AuthorizationItem.init(name: AuthorizationString, valueLength: Int, value: UnsafeMutablePointer<Void>, flags: UInt32)Removed AuthorizationItemSet.init()Removed AuthorizationItemSet.init(count: UInt32, items: UnsafeMutablePointer<AuthorizationItem>)Removed cssm_access_credentials.init(EntryTag: CSSM_STRING, BaseCerts: CSSM_BASE_CERTS, Samples: CSSM_SAMPLEGROUP, Callback: CSSM_CHALLENGE_CALLBACK, CallerCtx: UnsafeMutablePointer<Void>)Removed cssm_acl_entry_input.init(Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback: CSSM_ACL_SUBJECT_CALLBACK, CallerContext: UnsafeMutablePointer<Void>)Removed cssm_appledl_open_parameters_mask.valueRemoved cssm_crypto_data.init(Param: CSSM_DATA, Callback: CSSM_CALLBACK, CallerCtx: UnsafeMutablePointer<Void>)Removed cssm_func_name_addr.init(Name: CSSM_STRING, Address: CSSM_PROC_ADDR)Removed cssm_manager_registration_info.init(Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>, Terminate: CFunctionPointer<(() -> CSSM_RETURN)>, RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>, DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>, EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>, RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>)Removed cssm_memory_funcs.init(malloc_func: CSSM_MALLOC, free_func: CSSM_FREE, realloc_func: CSSM_REALLOC, calloc_func: CSSM_CALLOC, AllocRef: UnsafeMutablePointer<Void>)Removed cssm_module_funcs.init(ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs: uint32, ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR>)Removed cssm_spi_ac_funcs.init(AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Removed cssm_spi_cl_funcs.init(CertCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertGetAllTemplateFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)>, CertSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)>, CertVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>, CertGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CertGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CertAbortQuery: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, CertGetKeyInfo: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)>, CertGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)>, FreeFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)>, FreeFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertCache: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, CertGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CertGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CertAbortCache: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, CertGroupToSignedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertGroupFromVerifiedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)>, CertDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)>, CrlCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlSetFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlAddCert: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlRemoveCert: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)>, CrlVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>, IsCertInCrl: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, CrlGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CrlGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CrlAbortQuery: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, CrlGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)>, CrlCache: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, IsCertInCachedCrl: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CrlGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)>, CrlGetAllCachedRecordFields: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)>, CrlAbortCache: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, CrlDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Removed cssm_spi_dl_funcs.init(DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose: CFunctionPointer<((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)>, DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>, CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>, Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>, GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)>, ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)>, GetDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)>, ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)>, GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList: CFunctionPointer<((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Removed cssm_spi_kr_funcs.init(RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>, GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>, ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>, RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)>, GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Removed cssm_spi_tp_funcs.init(SubmitCredRequest: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)>, RetrieveCredResult: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)>, ConfirmCredResult: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)>, ReceiveConfirmation: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)>, CertReclaimKey: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)>, CertReclaimAbort: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)>, FormRequest: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)>, FormSubmit: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)>, CertGroupVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)>, CertCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertGetAllTemplateFields: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)>, CertSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)>, CrlCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertRevoke: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)>, CertRemoveFromCrlTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, CrlSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, ApplyCrlToDb: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)>, CertGroupConstruct: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)>, CertGroupPrune: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)>, CertGroupToTupleGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)>, TupleGroupToCertGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Removed cssm_state_funcs.init(cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>, cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>, cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>, cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>)Removed cssm_tp_callerauth_context.init(Policy: CSSM_TP_POLICYINFO, VerifyTime: CSSM_TIMESTRING, VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK, NumberOfAnchorCerts: uint32, AnchorCerts: CSSM_DATA_PTR, DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_upcalls.init(malloc_func: CSSM_UPCALLS_MALLOC, free_func: CSSM_UPCALLS_FREE, realloc_func: CSSM_UPCALLS_REALLOC, calloc_func: CSSM_UPCALLS_CALLOC, CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>, GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>)Removed extension_data_format.valueRemoved mds_funcs.init(DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>, GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>)Removed SecAccessControlCreateFlags.init(_: CFIndex)Removed SecAsn1Template_struct.init()Removed SecAsn1Template_struct.init(kind: UInt32, offset: UInt32, sub: UnsafePointer<Void>, size: UInt32)Removed SecItemImportExportKeyParameters.init()Removed SecItemImportExportKeyParameters.init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<AnyObject>!, alertTitle: Unmanaged<CFString>!, alertPrompt: Unmanaged<CFString>!, accessRef: Unmanaged<SecAccess>!, keyUsage: Unmanaged<CFArray>!, keyAttributes: Unmanaged<CFArray>!)Removed SecKeychainAttribute.init()Removed SecKeychainAttribute.init(tag: SecKeychainAttrType, length: UInt32, data: UnsafeMutablePointer<Void>)Removed SecKeychainAttributeInfo.init()Removed SecKeychainAttributeInfo.init(count: UInt32, tag: UnsafeMutablePointer<UInt32>, format: UnsafeMutablePointer<UInt32>)Removed SecKeychainAttributeList.init()Removed SecKeychainAttributeList.init(count: UInt32, attr: UnsafeMutablePointer<SecKeychainAttribute>)Removed SecKeychainCallbackInfo.init()Removed SecKeychainCallbackInfo.init(version: UInt32, item: Unmanaged<SecKeychainItem>!, keychain: Unmanaged<SecKeychain>!, pid: pid_t)Removed SecKeychainSettings.init(version: UInt32, lockOnSleep: Boolean, useLockInterval: Boolean, lockInterval: UInt32)Removed SecKeyImportExportParameters.init()Removed SecKeyImportExportParameters.init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<AnyObject>!, alertTitle: Unmanaged<CFString>!, alertPrompt: Unmanaged<CFString>!, accessRef: Unmanaged<SecAccess>!, keyUsage: CSSM_KEYUSE, keyAttributes: CSSM_KEYATTR_FLAGS)Removed SecPreferencesDomain [struct]Removed SecPreferencesDomain.init(_: UInt32)Removed SecPreferencesDomain.valueRemoved SSLAuthenticate [struct]Removed SSLAuthenticate.init(_: UInt32)Removed SSLAuthenticate.valueRemoved SSLClientCertificateState [struct]Removed SSLClientCertificateState.init(_: UInt32)Removed SSLClientCertificateState.valueRemoved SSLConnectionType [struct]Removed SSLConnectionType.init(_: UInt32)Removed SSLConnectionType.valueRemoved SSLProtocol [struct]Removed SSLProtocol.init(_: UInt32)Removed SSLProtocol.valueRemoved SSLProtocolSide [struct]Removed SSLProtocolSide.init(_: UInt32)Removed SSLProtocolSide.valueRemoved SSLSessionOption [struct]Removed SSLSessionOption.init(_: UInt32)Removed SSLSessionOption.valueRemoved SSLSessionState [struct]Removed SSLSessionState.init(_: UInt32)Removed SSLSessionState.valueRemoved AuthorizationFlagsRemoved CMSCertificateChainModeRemoved CMSSignedAttributesRemoved CMSSignerStatusRemoved errSecAllocateRemoved errSecAuthFailedRemoved errSecDecodeRemoved errSecDuplicateItemRemoved errSecInteractionNotAllowedRemoved errSecItemNotFoundRemoved errSecNotAvailableRemoved errSecParamRemoved errSecSuccessRemoved errSecUnimplementedRemoved kAlwaysAuthenticateRemoved kAuthorizationFlagDefaultsRemoved kAuthorizationFlagDestroyRightsRemoved kAuthorizationFlagExtendRightsRemoved kAuthorizationFlagInteractionAllowedRemoved kAuthorizationFlagNoDataRemoved kAuthorizationFlagPartialRightsRemoved kAuthorizationFlagPreAuthorizeRemoved kCMSAttrNoneRemoved kCMSAttrSigningTimeRemoved kCMSAttrSmimeCapabilitiesRemoved kCMSAttrSmimeEncryptionKeyPrefsRemoved kCMSAttrSmimeMSEncryptionKeyPrefsRemoved kCMSCertificateChainRemoved kCMSCertificateChainWithRootRemoved kCMSCertificateNoneRemoved kCMSCertificateSignerOnlyRemoved kCMSSignerInvalidCertRemoved kCMSSignerInvalidIndexRemoved kCMSSignerInvalidSignatureRemoved kCMSSignerNeedsDetachedContentRemoved kCMSSignerUnsignedRemoved kCMSSignerValidRemoved kDTLSProtocol1Removed kNeverAuthenticateRemoved kSec3DES192Removed kSecAccountItemAttrRemoved kSecAddEventRemoved kSecAddEventMaskRemoved kSecAddressItemAttrRemoved kSecAES128Removed kSecAES192Removed kSecAES256Removed kSecAliasRemoved kSecAuthenticationTypeAnyRemoved kSecAuthenticationTypeDefaultRemoved kSecAuthenticationTypeDPARemoved kSecAuthenticationTypeHTMLFormRemoved kSecAuthenticationTypeHTTPBasicRemoved kSecAuthenticationTypeHTTPDigestRemoved kSecAuthenticationTypeItemAttrRemoved kSecAuthenticationTypeMSNRemoved kSecAuthenticationTypeNTLMRemoved kSecAuthenticationTypeRPARemoved kSecCertificateEncodingRemoved kSecCertificateItemClassRemoved kSecCertificateTypeRemoved kSecCodeSignatureAdhocRemoved kSecCodeSignatureEnforcementRemoved kSecCodeSignatureForceExpirationRemoved kSecCodeSignatureForceHardRemoved kSecCodeSignatureForceKillRemoved kSecCodeSignatureHostRemoved kSecCodeSignatureLibraryValidationRemoved kSecCodeSignatureRestrictRemoved kSecCodeStatusHardRemoved kSecCodeStatusKillRemoved kSecCodeStatusValidRemoved kSecCommentItemAttrRemoved kSecCreationDateItemAttrRemoved kSecCreatorItemAttrRemoved kSecCredentialTypeDefaultRemoved kSecCredentialTypeNoUIRemoved kSecCredentialTypeWithUIRemoved kSecCrlEncodingRemoved kSecCrlTypeRemoved kSecCSConsiderExpirationRemoved kSecCSDefaultFlagsRemoved kSecCSEnforceRevocationChecksRemoved kSecCSNoNetworkAccessRemoved kSecCSReportProgressRemoved kSecCustomIconItemAttrRemoved kSecDataAccessEventRemoved kSecDataAccessEventMaskRemoved kSecDefaultChangedEventRemoved kSecDefaultChangedEventMaskRemoved kSecDefaultKeySizeRemoved kSecDeleteEventRemoved kSecDeleteEventMaskRemoved kSecDescriptionItemAttrRemoved kSecDesignatedRequirementTypeRemoved kSecEveryEventMaskRemoved kSecFormatBSAFERemoved kSecFormatNetscapeCertSequenceRemoved kSecFormatOpenSSLRemoved kSecFormatPEMSequenceRemoved kSecFormatPKCS12Removed kSecFormatPKCS7Removed kSecFormatRawKeyRemoved kSecFormatSSHRemoved kSecFormatSSHv2Removed kSecFormatUnknownRemoved kSecFormatWrappedLSHRemoved kSecFormatWrappedOpenSSLRemoved kSecFormatWrappedPKCS8Removed kSecFormatWrappedSSHRemoved kSecFormatX509CertRemoved kSecGenericItemAttrRemoved kSecGenericPasswordItemClassRemoved kSecGuestRequirementTypeRemoved kSecHostRequirementTypeRemoved kSecInternetPasswordItemClassRemoved kSecInvalidRequirementTypeRemoved kSecInvisibleItemAttrRemoved kSecItemPemArmourRemoved kSecItemTypeAggregateRemoved kSecItemTypeCertificateRemoved kSecItemTypePrivateKeyRemoved kSecItemTypePublicKeyRemoved kSecItemTypeSessionKeyRemoved kSecItemTypeUnknownRemoved kSecKeychainListChangedEventRemoved kSecKeychainListChangedMaskRemoved kSecKeychainPromptInvalidRemoved kSecKeychainPromptInvalidActRemoved kSecKeychainPromptRequirePassphaseRemoved kSecKeychainPromptUnsignedRemoved kSecKeychainPromptUnsignedActRemoved kSecKeyImportOnlyOneRemoved kSecKeyNoAccessControlRemoved kSecKeySecurePassphraseRemoved kSecLabelItemAttrRemoved kSecLibraryRequirementTypeRemoved kSecLockEventRemoved kSecLockEventMaskRemoved kSecModDateItemAttrRemoved kSecNegativeItemAttrRemoved kSecp192r1Removed kSecp256r1Removed kSecp384r1Removed kSecp521r1Removed kSecPaddingNoneRemoved kSecPaddingPKCS1Removed kSecPaddingPKCS1MD2Removed kSecPaddingPKCS1MD5Removed kSecPaddingPKCS1SHA1Removed kSecPasswordChangedEventRemoved kSecPasswordChangedEventMaskRemoved kSecPathItemAttrRemoved kSecPluginRequirementTypeRemoved kSecPortItemAttrRemoved kSecPreferencesDomainCommonRemoved kSecPreferencesDomainDynamicRemoved kSecPreferencesDomainSystemRemoved kSecPreferencesDomainUserRemoved kSecPrivateKeyItemClassRemoved kSecProtocolItemAttrRemoved kSecProtocolTypeAFPRemoved kSecProtocolTypeAnyRemoved kSecProtocolTypeAppleTalkRemoved kSecProtocolTypeCIFSRemoved kSecProtocolTypeCVSpserverRemoved kSecProtocolTypeDAAPRemoved kSecProtocolTypeEPPCRemoved kSecProtocolTypeFTPRemoved kSecProtocolTypeFTPAccountRemoved kSecProtocolTypeFTPProxyRemoved kSecProtocolTypeFTPSRemoved kSecProtocolTypeHTTPRemoved kSecProtocolTypeHTTPProxyRemoved kSecProtocolTypeHTTPSRemoved kSecProtocolTypeHTTPSProxyRemoved kSecProtocolTypeIMAPRemoved kSecProtocolTypeIMAPSRemoved kSecProtocolTypeIPPRemoved kSecProtocolTypeIRCRemoved kSecProtocolTypeIRCSRemoved kSecProtocolTypeLDAPRemoved kSecProtocolTypeLDAPSRemoved kSecProtocolTypeNNTPRemoved kSecProtocolTypeNNTPSRemoved kSecProtocolTypePOP3Removed kSecProtocolTypePOP3SRemoved kSecProtocolTypeRTSPRemoved kSecProtocolTypeRTSPProxyRemoved kSecProtocolTypeSMBRemoved kSecProtocolTypeSMTPRemoved kSecProtocolTypeSOCKSRemoved kSecProtocolTypeSSHRemoved kSecProtocolTypeSVNRemoved kSecProtocolTypeTelnetRemoved kSecProtocolTypeTelnetSRemoved kSecPublicKeyItemClassRemoved kSecRequirementTypeCountRemoved kSecRSAMaxRemoved kSecRSAMinRemoved kSecScriptCodeItemAttrRemoved kSecSecurityDomainItemAttrRemoved kSecServerItemAttrRemoved kSecServiceItemAttrRemoved kSecSignatureItemAttrRemoved kSecSymmetricKeyItemClassRemoved kSecTransformMetaAttributeCanCycleRemoved kSecTransformMetaAttributeDeferredRemoved kSecTransformMetaAttributeExternalizeRemoved kSecTransformMetaAttributeHasInboundConnectionRemoved kSecTransformMetaAttributeHasOutboundConnectionsRemoved kSecTransformMetaAttributeNameRemoved kSecTransformMetaAttributeRefRemoved kSecTransformMetaAttributeRequiredRemoved kSecTransformMetaAttributeRequiresOutboundConnectionRemoved kSecTransformMetaAttributeStreamRemoved kSecTransformMetaAttributeValueRemoved kSecTrustOptionAllowExpiredRemoved kSecTrustOptionAllowExpiredRootRemoved kSecTrustOptionFetchIssuerFromNetRemoved kSecTrustOptionImplicitAnchorsRemoved kSecTrustOptionLeafIsCARemoved kSecTrustOptionRequireRevPerCertRemoved kSecTrustOptionUseTrustSettingsRemoved kSecTrustSettingsChangedEventRemoved kSecTrustSettingsChangedEventMaskRemoved kSecTrustSettingsDomainAdminRemoved kSecTrustSettingsDomainSystemRemoved kSecTrustSettingsDomainUserRemoved kSecTrustSettingsKeyUseAnyRemoved kSecTrustSettingsKeyUseEnDecryptDataRemoved kSecTrustSettingsKeyUseEnDecryptKeyRemoved kSecTrustSettingsKeyUseKeyExchangeRemoved kSecTrustSettingsKeyUseSignatureRemoved kSecTrustSettingsKeyUseSignCertRemoved kSecTrustSettingsKeyUseSignRevocationRemoved kSecTrustSettingsResultDenyRemoved kSecTrustSettingsResultInvalidRemoved kSecTrustSettingsResultTrustAsRootRemoved kSecTrustSettingsResultTrustRootRemoved kSecTrustSettingsResultUnspecifiedRemoved kSecTypeItemAttrRemoved kSecUnlockEventRemoved kSecUnlockEventMaskRemoved kSecUpdateEventRemoved kSecUpdateEventMaskRemoved kSecVolumeItemAttrRemoved kSSLAbortedRemoved kSSLClientCertNoneRemoved kSSLClientCertRejectedRemoved kSSLClientCertRequestedRemoved kSSLClientCertSentRemoved kSSLClientSideRemoved kSSLClosedRemoved kSSLConnectedRemoved kSSLDatagramTypeRemoved kSSLHandshakeRemoved kSSLIdleRemoved kSSLProtocol2Removed kSSLProtocol3Removed kSSLProtocol3OnlyRemoved kSSLProtocolAllRemoved kSSLProtocolUnknownRemoved kSSLServerSideRemoved kSSLSessionOptionBreakOnCertRequestedRemoved kSSLSessionOptionBreakOnClientAuthRemoved kSSLSessionOptionBreakOnServerAuthRemoved kSSLSessionOptionFallbackRemoved kSSLSessionOptionFalseStartRemoved kSSLSessionOptionSendOneByteRecordRemoved kSSLStreamTypeRemoved kTLSProtocol1Removed kTLSProtocol11Removed kTLSProtocol12Removed kTLSProtocol1OnlyRemoved kTryAuthenticateRemoved SecAuthenticationTypeRemoved SecCodeSignatureFlagsRemoved SecCodeStatusRemoved SecCredentialTypeRemoved SecCSFlagsRemoved SecExternalFormatRemoved SecExternalItemTypeRemoved SecItemAttrRemoved SecItemClassRemoved SecItemImportExportFlagsRemoved SecKeychainEventRemoved SecKeychainEventMaskRemoved SecKeychainPromptSelectorRemoved SecKeyImportExportFlagsRemoved SecKeySizesRemoved SecPaddingRemoved SecProtocolTypeRemoved SecRequirementTypeRemoved SecTransformMetaAttributeTypeRemoved SecTrustOptionFlagsRemoved SecTrustSettingsDomainRemoved SecTrustSettingsKeyUsageRemoved SecTrustSettingsResultAdded [AuthorizationFlags [struct]](https://developer.apple.com/documentation/security/authorizationflags)Added [AuthorizationFlags.Defaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults)Added [AuthorizationFlags.DestroyRights](https://developer.apple.com/documentation/security/authorizationflags/1397545-destroyrights)Added [AuthorizationFlags.ExtendRights](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagextendrights)Added AuthorizationFlags.init(rawValue: UInt32)Added [AuthorizationFlags.InteractionAllowed](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflaginteractionallowed)Added [AuthorizationFlags.NoData](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagnodata)Added [AuthorizationFlags.PartialRights](https://developer.apple.com/documentation/security/authorizationflags/1394760-partialrights)Added [AuthorizationFlags.PreAuthorize](https://developer.apple.com/documentation/security/authorizationflags/1395827-preauthorize)Added [CMSCertificateChainMode [enum]](https://developer.apple.com/documentation/security/cmscertificatechainmode)Added [CMSCertificateChainMode.Chain](https://developer.apple.com/documentation/security/cmscertificatechainmode/chain)Added [CMSCertificateChainMode.ChainWithRoot](https://developer.apple.com/documentation/security/cmscertificatechainmode/chainwithroot)Added [CMSCertificateChainMode.None](https://developer.apple.com/documentation/security/cmscertificatechainmode/none)Added [CMSCertificateChainMode.SignerOnly](https://developer.apple.com/documentation/security/cmscertificatechainmode/signeronly)Added [CMSSignedAttributes [enum]](https://developer.apple.com/documentation/security/cmssignedattributes)Added [CMSSignedAttributes.AttrNone](https://developer.apple.com/documentation/security/cmssignedattributes/kcmsattrnone)Added [CMSSignedAttributes.AttrSigningTime](https://developer.apple.com/documentation/security/cmssignedattributes/1387157-attrsigningtime)Added [CMSSignedAttributes.AttrSmimeCapabilities](https://developer.apple.com/documentation/security/cmssignedattributes/1387181-attrsmimecapabilities)Added [CMSSignedAttributes.AttrSmimeEncryptionKeyPrefs](https://developer.apple.com/documentation/security/cmssignedattributes/1387149-attrsmimeencryptionkeyprefs)Added [CMSSignedAttributes.AttrSmimeMSEncryptionKeyPrefs](https://developer.apple.com/documentation/security/cmssignedattributes/kcmsattrsmimemsencryptionkeyprefs)Added [CMSSignerStatus [enum]](https://developer.apple.com/documentation/security/cmssignerstatus)Added [CMSSignerStatus.InvalidCert](https://developer.apple.com/documentation/security/cmssignerstatus/invalidcert)Added [CMSSignerStatus.InvalidIndex](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignerinvalidindex)Added [CMSSignerStatus.InvalidSignature](https://developer.apple.com/documentation/security/cmssignerstatus/invalidsignature)Added [CMSSignerStatus.NeedsDetachedContent](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignerneedsdetachedcontent)Added [CMSSignerStatus.Unsigned](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignerunsigned)Added [CMSSignerStatus.Valid](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignervalid)Added cssm_access_credentials.init(EntryTag: CSSM_STRING, BaseCerts: CSSM_BASE_CERTS, Samples: CSSM_SAMPLEGROUP, Callback: CSSM_CHALLENGE_CALLBACK!, CallerCtx: UnsafeMutablePointer<Void>)Added cssm_acl_entry_input.init(Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback: CSSM_ACL_SUBJECT_CALLBACK!, CallerContext: UnsafeMutablePointer<Void>)Added cssm_appledl_open_parameters_mask.init(rawValue: UInt32)Added cssm_appledl_open_parameters_mask.rawValueAdded cssm_crypto_data.init(Param: CSSM_DATA, Callback: CSSM_CALLBACK!, CallerCtx: UnsafeMutablePointer<Void>)Added cssm_func_name_addr.init(Name: CSSM_STRING, Address: CSSM_PROC_ADDR!)Added cssm_manager_registration_info.init(Initialize: ((uint32, uint32) -> CSSM_RETURN)!, Terminate: (() -> CSSM_RETURN)!, RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)!, DeregisterDispatchTable: (() -> CSSM_RETURN)!, EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!, RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!)Added cssm_memory_funcs.init(malloc_func: CSSM_MALLOC!, free_func: CSSM_FREE!, realloc_func: CSSM_REALLOC!, calloc_func: CSSM_CALLOC!, AllocRef: UnsafeMutablePointer<Void>)Added cssm_module_funcs.init(ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs: uint32, ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?>)Added cssm_spi_ac_funcs.init(AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)!, PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Added cssm_spi_cl_funcs.init(CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)!, CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Added cssm_spi_csp_funcs.init(EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)!, SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)!, SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!, DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)!, GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)!, WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)!, FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)!, PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!, Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)!, Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!, ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)!, RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)!, GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)!, GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!)Added cssm_spi_dl_funcs.init(DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)!, DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!, Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Added cssm_spi_kr_funcs.init(RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)!, GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)!, ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)!, GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Added cssm_spi_tp_funcs.init(SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)!, ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)!, ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)!, CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)!, CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!, FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)!, FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)!, CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)!, TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Added cssm_state_funcs.init(cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!, cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)!, cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)!, cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!)Added cssm_tp_callerauth_context.init(Policy: CSSM_TP_POLICYINFO, VerifyTime: CSSM_TIMESTRING, VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK!, NumberOfAnchorCerts: uint32, AnchorCerts: CSSM_DATA_PTR, DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_upcalls.init(malloc_func: CSSM_UPCALLS_MALLOC!, free_func: CSSM_UPCALLS_FREE!, realloc_func: CSSM_UPCALLS_REALLOC!, calloc_func: CSSM_UPCALLS_CALLOC!, CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)!, GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!)Added [DERItem [struct]](https://developer.apple.com/documentation/security/deritem)Added [DERItem.data](https://developer.apple.com/documentation/security/deritem/1396970-data)Added DERItem.init()Added DERItem.init(data: UnsafeMutablePointer<DERByte>, length: DERSize)Added [DERItem.length](https://developer.apple.com/documentation/security/deritem/1402148-length)Added extension_data_format.init(rawValue: UInt32)Added extension_data_format.rawValueAdded mds_funcs.init(DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!, GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!)Added [SecAccessControlCreateFlags.DevicePasscode](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1394326-devicepasscode)Added [SecAuthenticationType [enum]](https://developer.apple.com/documentation/security/secauthenticationtype)Added [SecAuthenticationType.Any](https://developer.apple.com/documentation/security/secauthenticationtype/any)Added [SecAuthenticationType.Default](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypedefault)Added [SecAuthenticationType.DPA](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypedpa)Added [SecAuthenticationType.HTMLForm](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypehtmlform)Added [SecAuthenticationType.HTTPBasic](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypehttpbasic)Added [SecAuthenticationType.HTTPDigest](https://developer.apple.com/documentation/security/secauthenticationtype/httpdigest)Added [SecAuthenticationType.MSN](https://developer.apple.com/documentation/security/secauthenticationtype/msn)Added [SecAuthenticationType.NTLM](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypentlm)Added [SecAuthenticationType.RPA](https://developer.apple.com/documentation/security/secauthenticationtype/rpa)Added [SecCodeSignatureFlags [struct]](https://developer.apple.com/documentation/security/seccodesignatureflags)Added [SecCodeSignatureFlags.Adhoc](https://developer.apple.com/documentation/security/seccodesignatureflags/1397793-adhoc)Added [SecCodeSignatureFlags.Enforcement](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignatureenforcement)Added [SecCodeSignatureFlags.ForceExpiration](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignatureforceexpiration)Added [SecCodeSignatureFlags.ForceHard](https://developer.apple.com/documentation/security/seccodesignatureflags/1400159-forcehard)Added [SecCodeSignatureFlags.ForceKill](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignatureforcekill)Added [SecCodeSignatureFlags.Host](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignaturehost)Added SecCodeSignatureFlags.init(rawValue: UInt32)Added [SecCodeSignatureFlags.LibraryValidation](https://developer.apple.com/documentation/security/seccodesignatureflags/1393810-libraryvalidation)Added [SecCodeSignatureFlags.Restrict](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignaturerestrict)Added [SecCodeStatus [struct]](https://developer.apple.com/documentation/security/seccodestatus)Added [SecCodeStatus.Hard](https://developer.apple.com/documentation/security/seccodestatus/1395917-hard)Added SecCodeStatus.init(rawValue: UInt32)Added [SecCodeStatus.Kill](https://developer.apple.com/documentation/security/seccodestatus/1398182-kill)Added [SecCodeStatus.Valid](https://developer.apple.com/documentation/security/seccodestatus/kseccodestatusvalid)Added [SecCredentialType [enum]](https://developer.apple.com/documentation/security/seccredentialtype)Added [SecCredentialType.Default](https://developer.apple.com/documentation/security/seccredentialtype/kseccredentialtypedefault)Added [SecCredentialType.NoUI](https://developer.apple.com/documentation/security/seccredentialtype/noui)Added [SecCredentialType.WithUI](https://developer.apple.com/documentation/security/seccredentialtype/withui)Added [SecCSFlags [struct]](https://developer.apple.com/documentation/security/seccsflags)Added [SecCSFlags.CheckTrustedAnchors](https://developer.apple.com/documentation/security/seccsflags/kseccschecktrustedanchors)Added [SecCSFlags.ConsiderExpiration](https://developer.apple.com/documentation/security/seccsflags/1400700-considerexpiration)Added [SecCSFlags.DefaultFlags](https://developer.apple.com/documentation/security/seccsflags/kseccsdefaultflags)Added [SecCSFlags.EnforceRevocationChecks](https://developer.apple.com/documentation/security/seccsflags/kseccsenforcerevocationchecks)Added SecCSFlags.init(rawValue: UInt32)Added [SecCSFlags.NoNetworkAccess](https://developer.apple.com/documentation/security/seccsflags/1397911-nonetworkaccess)Added [SecCSFlags.ReportProgress](https://developer.apple.com/documentation/security/seccsflags/kseccsreportprogress)Added [SecExternalFormat [enum]](https://developer.apple.com/documentation/security/secexternalformat)Added [SecExternalFormat.FormatBSAFE](https://developer.apple.com/documentation/security/secexternalformat/formatbsafe)Added [SecExternalFormat.FormatNetscapeCertSequence](https://developer.apple.com/documentation/security/secexternalformat/formatnetscapecertsequence)Added [SecExternalFormat.FormatOpenSSL](https://developer.apple.com/documentation/security/secexternalformat/formatopenssl)Added [SecExternalFormat.FormatPEMSequence](https://developer.apple.com/documentation/security/secexternalformat/ksecformatpemsequence)Added [SecExternalFormat.FormatPKCS12](https://developer.apple.com/documentation/security/secexternalformat/formatpkcs12)Added [SecExternalFormat.FormatPKCS7](https://developer.apple.com/documentation/security/secexternalformat/formatpkcs7)Added [SecExternalFormat.FormatRawKey](https://developer.apple.com/documentation/security/secexternalformat/ksecformatrawkey)Added [SecExternalFormat.FormatSSH](https://developer.apple.com/documentation/security/secexternalformat/ksecformatssh)Added [SecExternalFormat.FormatSSHv2](https://developer.apple.com/documentation/security/secexternalformat/ksecformatsshv2)Added [SecExternalFormat.FormatUnknown](https://developer.apple.com/documentation/security/secexternalformat/formatunknown)Added [SecExternalFormat.FormatWrappedLSH](https://developer.apple.com/documentation/security/secexternalformat/formatwrappedlsh)Added [SecExternalFormat.FormatWrappedOpenSSL](https://developer.apple.com/documentation/security/secexternalformat/ksecformatwrappedopenssl)Added [SecExternalFormat.FormatWrappedPKCS8](https://developer.apple.com/documentation/security/secexternalformat/ksecformatwrappedpkcs8)Added [SecExternalFormat.FormatWrappedSSH](https://developer.apple.com/documentation/security/secexternalformat/formatwrappedssh)Added [SecExternalFormat.FormatX509Cert](https://developer.apple.com/documentation/security/secexternalformat/ksecformatx509cert)Added [SecExternalItemType [enum]](https://developer.apple.com/documentation/security/secexternalitemtype)Added [SecExternalItemType.ItemTypeAggregate](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeaggregate)Added [SecExternalItemType.ItemTypeCertificate](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypecertificate)Added [SecExternalItemType.ItemTypePrivateKey](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeprivatekey)Added [SecExternalItemType.ItemTypePublicKey](https://developer.apple.com/documentation/security/secexternalitemtype/ksecitemtypepublickey)Added [SecExternalItemType.ItemTypeSessionKey](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypesessionkey)Added [SecExternalItemType.ItemTypeUnknown](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeunknown)Added [SecItemAttr [enum]](https://developer.apple.com/documentation/security/secitemattr)Added [SecItemAttr.AccountItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecaccountitemattr)Added [SecItemAttr.AddressItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecaddressitemattr)Added [SecItemAttr.Alias](https://developer.apple.com/documentation/security/secitemattr/alias)Added [SecItemAttr.AuthenticationTypeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecauthenticationtypeitemattr)Added [SecItemAttr.CertificateEncoding](https://developer.apple.com/documentation/security/secitemattr/certificateencoding)Added [SecItemAttr.CertificateType](https://developer.apple.com/documentation/security/secitemattr/kseccertificatetype)Added [SecItemAttr.CommentItemAttr](https://developer.apple.com/documentation/security/secitemattr/commentitemattr)Added [SecItemAttr.CreationDateItemAttr](https://developer.apple.com/documentation/security/secitemattr/kseccreationdateitemattr)Added [SecItemAttr.CreatorItemAttr](https://developer.apple.com/documentation/security/secitemattr/creatoritemattr)Added [SecItemAttr.CrlEncoding](https://developer.apple.com/documentation/security/secitemattr/crlencoding)Added [SecItemAttr.CrlType](https://developer.apple.com/documentation/security/secitemattr/crltype)Added [SecItemAttr.CustomIconItemAttr](https://developer.apple.com/documentation/security/secitemattr/customiconitemattr)Added [SecItemAttr.DescriptionItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecdescriptionitemattr)Added [SecItemAttr.GenericItemAttr](https://developer.apple.com/documentation/security/secitemattr/genericitemattr)Added [SecItemAttr.InvisibleItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecinvisibleitemattr)Added [SecItemAttr.LabelItemAttr](https://developer.apple.com/documentation/security/secitemattr/kseclabelitemattr)Added [SecItemAttr.ModDateItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecmoddateitemattr)Added [SecItemAttr.NegativeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecnegativeitemattr)Added [SecItemAttr.PathItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecpathitemattr)Added [SecItemAttr.PortItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecportitemattr)Added [SecItemAttr.ProtocolItemAttr](https://developer.apple.com/documentation/security/secitemattr/protocolitemattr)Added [SecItemAttr.ScriptCodeItemAttr](https://developer.apple.com/documentation/security/secitemattr/scriptcodeitemattr)Added [SecItemAttr.SecurityDomainItemAttr](https://developer.apple.com/documentation/security/secitemattr/securitydomainitemattr)Added [SecItemAttr.ServerItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecserveritemattr)Added [SecItemAttr.ServiceItemAttr](https://developer.apple.com/documentation/security/secitemattr/serviceitemattr)Added [SecItemAttr.SignatureItemAttr](https://developer.apple.com/documentation/security/secitemattr/signatureitemattr)Added [SecItemAttr.TypeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksectypeitemattr)Added [SecItemAttr.VolumeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecvolumeitemattr)Added [SecItemClass [enum]](https://developer.apple.com/documentation/security/secitemclass)Added [SecItemClass.CertificateItemClass](https://developer.apple.com/documentation/security/secitemclass/kseccertificateitemclass)Added [SecItemClass.GenericPasswordItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecgenericpassworditemclass)Added [SecItemClass.InternetPasswordItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecinternetpassworditemclass)Added [SecItemClass.PrivateKeyItemClass](https://developer.apple.com/documentation/security/secitemclass/privatekeyitemclass)Added [SecItemClass.PublicKeyItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecpublickeyitemclass)Added [SecItemClass.SymmetricKeyItemClass](https://developer.apple.com/documentation/security/secitemclass/symmetrickeyitemclass)Added [SecItemImportExportFlags [struct]](https://developer.apple.com/documentation/security/secitemimportexportflags)Added SecItemImportExportFlags.init(rawValue: UInt32)Added [SecItemImportExportFlags.PemArmour](https://developer.apple.com/documentation/security/secitemimportexportflags/1399536-pemarmour)Added [SecKeychainEvent [enum]](https://developer.apple.com/documentation/security/seckeychainevent)Added [SecKeychainEvent.AddEvent](https://developer.apple.com/documentation/security/seckeychainevent/addevent)Added [SecKeychainEvent.DataAccessEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecdataaccessevent)Added [SecKeychainEvent.DefaultChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecdefaultchangedevent)Added [SecKeychainEvent.DeleteEvent](https://developer.apple.com/documentation/security/seckeychainevent/deleteevent)Added [SecKeychainEvent.KeychainListChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/keychainlistchangedevent)Added [SecKeychainEvent.LockEvent](https://developer.apple.com/documentation/security/seckeychainevent/kseclockevent)Added [SecKeychainEvent.PasswordChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecpasswordchangedevent)Added [SecKeychainEvent.TrustSettingsChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksectrustsettingschangedevent)Added [SecKeychainEvent.UnlockEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecunlockevent)Added [SecKeychainEvent.UpdateEvent](https://developer.apple.com/documentation/security/seckeychainevent/updateevent)Added [SecKeychainEventMask [struct]](https://developer.apple.com/documentation/security/seckeychaineventmask)Added [SecKeychainEventMask.AddEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1399566-addeventmask)Added [SecKeychainEventMask.DataAccessEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecdataaccesseventmask)Added [SecKeychainEventMask.DefaultChangedEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecdefaultchangedeventmask)Added [SecKeychainEventMask.DeleteEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1392414-deleteeventmask)Added [SecKeychainEventMask.EveryEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/kseceveryeventmask)Added SecKeychainEventMask.init(rawValue: UInt32)Added [SecKeychainEventMask.KeychainListChangedMask](https://developer.apple.com/documentation/security/seckeychaineventmask/kseckeychainlistchangedmask)Added [SecKeychainEventMask.LockEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1398376-lockeventmask)Added [SecKeychainEventMask.PasswordChangedEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecpasswordchangedeventmask)Added [SecKeychainEventMask.TrustSettingsChangedEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksectrustsettingschangedeventmask)Added [SecKeychainEventMask.UnlockEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1392496-unlockeventmask)Added [SecKeychainEventMask.UpdateEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecupdateeventmask)Added [SecKeychainPromptSelector [struct]](https://developer.apple.com/documentation/security/seckeychainpromptselector)Added SecKeychainPromptSelector.init(rawValue: uint16)Added [SecKeychainPromptSelector.Invalid](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptinvalid)Added [SecKeychainPromptSelector.InvalidAct](https://developer.apple.com/documentation/security/seckeychainpromptselector/1395933-invalidact)Added [SecKeychainPromptSelector.RequirePassphase](https://developer.apple.com/documentation/security/seckeychainpromptselector/1396844-requirepassphase)Added [SecKeychainPromptSelector.Unsigned](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptunsigned)Added [SecKeychainPromptSelector.UnsignedAct](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptunsignedact)Added SecKeychainSettings.init(version: UInt32, lockOnSleep: DarwinBoolean, useLockInterval: DarwinBoolean, lockInterval: UInt32)Added [SecKeyImportExportFlags [struct]](https://developer.apple.com/documentation/security/seckeyimportexportflags)Added [SecKeyImportExportFlags.ImportOnlyOne](https://developer.apple.com/documentation/security/seckeyimportexportflags/1392169-importonlyone)Added SecKeyImportExportFlags.init(rawValue: UInt32)Added [SecKeyImportExportFlags.NoAccessControl](https://developer.apple.com/documentation/security/seckeyimportexportflags/kseckeynoaccesscontrol)Added [SecKeyImportExportFlags.SecurePassphrase](https://developer.apple.com/documentation/security/seckeyimportexportflags/kseckeysecurepassphrase)Added [SecKeySizes [enum]](https://developer.apple.com/documentation/security/seckeysizes)Added [SecKeySizes.Sec3DES192](https://developer.apple.com/documentation/security/seckeysizes/sec3des192)Added [SecKeySizes.SecAES128](https://developer.apple.com/documentation/security/seckeysizes/secaes128)Added [SecKeySizes.SecAES192](https://developer.apple.com/documentation/security/seckeysizes/1400540-secaes192)Added [SecKeySizes.SecAES256](https://developer.apple.com/documentation/security/seckeysizes/ksecaes256)Added [SecKeySizes.SecDefaultKeySize](https://developer.apple.com/documentation/security/seckeysizes/ksecdefaultkeysize)Added [SecKeySizes.Secp192r1](https://developer.apple.com/documentation/security/seckeysizes/1398550-secp192r1)Added [SecKeySizes.Secp256r1](https://developer.apple.com/documentation/security/seckeysizes/1398756-secp256r1)Added [SecKeySizes.Secp384r1](https://developer.apple.com/documentation/security/seckeysizes/ksecp384r1)Added [SecKeySizes.Secp521r1](https://developer.apple.com/documentation/security/seckeysizes/ksecp521r1)Added [SecKeySizes.SecRSAMax](https://developer.apple.com/documentation/security/seckeysizes/ksecrsamax)Added [SecKeySizes.SecRSAMin](https://developer.apple.com/documentation/security/seckeysizes/secrsamin)Added [SecPadding [enum]](https://developer.apple.com/documentation/security/secpadding)Added [SecPadding.None](https://developer.apple.com/documentation/security/secpadding/ksecpaddingnone)Added [SecPadding.PKCS1](https://developer.apple.com/documentation/security/secpadding/1401893-pkcs1)Added [SecPadding.PKCS1MD2](https://developer.apple.com/documentation/security/secpadding/1398958-pkcs1md2)Added [SecPadding.PKCS1MD5](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1md5)Added [SecPadding.PKCS1SHA1](https://developer.apple.com/documentation/security/secpadding/1392907-pkcs1sha1)Added [SecPadding.SigRaw](https://developer.apple.com/documentation/security/secpadding/1401132-sigraw)Added [SecPreferencesDomain [enum]](https://developer.apple.com/documentation/security/secpreferencesdomain)Added [SecPreferencesDomain.Common](https://developer.apple.com/documentation/security/secpreferencesdomain/ksecpreferencesdomaincommon)Added [SecPreferencesDomain.Dynamic](https://developer.apple.com/documentation/security/secpreferencesdomain/dynamic)Added [SecPreferencesDomain.System](https://developer.apple.com/documentation/security/secpreferencesdomain/ksecpreferencesdomainsystem)Added [SecPreferencesDomain.User](https://developer.apple.com/documentation/security/secpreferencesdomain/ksecpreferencesdomainuser)Added [SecProtocolType [enum]](https://developer.apple.com/documentation/security/secprotocoltype)Added [SecProtocolType.AFP](https://developer.apple.com/documentation/security/secprotocoltype/afp)Added [SecProtocolType.Any](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeany)Added [SecProtocolType.AppleTalk](https://developer.apple.com/documentation/security/secprotocoltype/appletalk)Added [SecProtocolType.CIFS](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypecifs)Added [SecProtocolType.CVSpserver](https://developer.apple.com/documentation/security/secprotocoltype/cvspserver)Added [SecProtocolType.DAAP](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypedaap)Added [SecProtocolType.EPPC](https://developer.apple.com/documentation/security/secprotocoltype/eppc)Added [SecProtocolType.FTP](https://developer.apple.com/documentation/security/secprotocoltype/ftp)Added [SecProtocolType.FTPAccount](https://developer.apple.com/documentation/security/secprotocoltype/ftpaccount)Added [SecProtocolType.FTPProxy](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeftpproxy)Added [SecProtocolType.FTPS](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeftps)Added [SecProtocolType.HTTP](https://developer.apple.com/documentation/security/secprotocoltype/http)Added [SecProtocolType.HTTPProxy](https://developer.apple.com/documentation/security/secprotocoltype/httpproxy)Added [SecProtocolType.HTTPS](https://developer.apple.com/documentation/security/secprotocoltype/https)Added [SecProtocolType.HTTPSProxy](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypehttpsproxy)Added [SecProtocolType.IMAP](https://developer.apple.com/documentation/security/secprotocoltype/imap)Added [SecProtocolType.IMAPS](https://developer.apple.com/documentation/security/secprotocoltype/imaps)Added [SecProtocolType.IPP](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeipp)Added [SecProtocolType.IRC](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeirc)Added [SecProtocolType.IRCS](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeircs)Added [SecProtocolType.LDAP](https://developer.apple.com/documentation/security/secprotocoltype/ldap)Added [SecProtocolType.LDAPS](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeldaps)Added [SecProtocolType.NNTP](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypenntp)Added [SecProtocolType.NNTPS](https://developer.apple.com/documentation/security/secprotocoltype/nntps)Added [SecProtocolType.POP3](https://developer.apple.com/documentation/security/secprotocoltype/pop3)Added [SecProtocolType.POP3S](https://developer.apple.com/documentation/security/secprotocoltype/pop3s)Added [SecProtocolType.RTSP](https://developer.apple.com/documentation/security/secprotocoltype/rtsp)Added [SecProtocolType.RTSPProxy](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypertspproxy)Added [SecProtocolType.SMB](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypesmb)Added [SecProtocolType.SMTP](https://developer.apple.com/documentation/security/secprotocoltype/smtp)Added [SecProtocolType.SOCKS](https://developer.apple.com/documentation/security/secprotocoltype/socks)Added [SecProtocolType.SSH](https://developer.apple.com/documentation/security/secprotocoltype/ssh)Added [SecProtocolType.SVN](https://developer.apple.com/documentation/security/secprotocoltype/svn)Added [SecProtocolType.Telnet](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypetelnet)Added [SecProtocolType.TelnetS](https://developer.apple.com/documentation/security/secprotocoltype/telnets)Added [SecRequirementType [enum]](https://developer.apple.com/documentation/security/secrequirementtype)Added [SecRequirementType.DesignatedRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/ksecdesignatedrequirementtype)Added [SecRequirementType.GuestRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/guestrequirementtype)Added [SecRequirementType.HostRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/hostrequirementtype)Added [SecRequirementType.InvalidRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/invalidrequirementtype)Added [SecRequirementType.LibraryRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/kseclibraryrequirementtype)Added [SecRequirementType.PluginRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/ksecpluginrequirementtype)Added [SecRequirementType.RequirementTypeCount](https://developer.apple.com/documentation/security/secrequirementtype/1401052-requirementtypecount)Added [SecTransformMetaAttributeType [enum]](https://developer.apple.com/documentation/security/sectransformmetaattributetype)Added [SecTransformMetaAttributeType.CanCycle](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributecancycle)Added [SecTransformMetaAttributeType.Deferred](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributedeferred)Added [SecTransformMetaAttributeType.Externalize](https://developer.apple.com/documentation/security/sectransformmetaattributetype/externalize)Added [SecTransformMetaAttributeType.HasInboundConnection](https://developer.apple.com/documentation/security/sectransformmetaattributetype/hasinboundconnection)Added [SecTransformMetaAttributeType.HasOutboundConnections](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributehasoutboundconnections)Added [SecTransformMetaAttributeType.Name](https://developer.apple.com/documentation/security/sectransformmetaattributetype/name)Added [SecTransformMetaAttributeType.Ref](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributeref)Added [SecTransformMetaAttributeType.Required](https://developer.apple.com/documentation/security/sectransformmetaattributetype/required)Added [SecTransformMetaAttributeType.RequiresOutboundConnection](https://developer.apple.com/documentation/security/sectransformmetaattributetype/requiresoutboundconnection)Added [SecTransformMetaAttributeType.Stream](https://developer.apple.com/documentation/security/sectransformmetaattributetype/stream)Added [SecTransformMetaAttributeType.Value](https://developer.apple.com/documentation/security/sectransformmetaattributetype/value)Added [SecTrustOptionFlags [struct]](https://developer.apple.com/documentation/security/sectrustoptionflags)Added [SecTrustOptionFlags.AllowExpired](https://developer.apple.com/documentation/security/sectrustoptionflags/1396581-allowexpired)Added [SecTrustOptionFlags.AllowExpiredRoot](https://developer.apple.com/documentation/security/sectrustoptionflags/1401432-allowexpiredroot)Added [SecTrustOptionFlags.FetchIssuerFromNet](https://developer.apple.com/documentation/security/sectrustoptionflags/1395949-fetchissuerfromnet)Added [SecTrustOptionFlags.ImplicitAnchors](https://developer.apple.com/documentation/security/sectrustoptionflags/1400933-implicitanchors)Added SecTrustOptionFlags.init(rawValue: UInt32)Added [SecTrustOptionFlags.LeafIsCA](https://developer.apple.com/documentation/security/sectrustoptionflags/1397419-leafisca)Added [SecTrustOptionFlags.RequireRevPerCert](https://developer.apple.com/documentation/security/sectrustoptionflags/ksectrustoptionrequirerevpercert)Added [SecTrustOptionFlags.UseTrustSettings](https://developer.apple.com/documentation/security/sectrustoptionflags/1398574-usetrustsettings)Added [SecTrustSettingsDomain [enum]](https://developer.apple.com/documentation/security/sectrustsettingsdomain)Added [SecTrustSettingsDomain.Admin](https://developer.apple.com/documentation/security/sectrustsettingsdomain/ksectrustsettingsdomainadmin)Added [SecTrustSettingsDomain.System](https://developer.apple.com/documentation/security/sectrustsettingsdomain/system)Added [SecTrustSettingsDomain.User](https://developer.apple.com/documentation/security/sectrustsettingsdomain/ksectrustsettingsdomainuser)Added [SecTrustSettingsKeyUsage [struct]](https://developer.apple.com/documentation/security/sectrustsettingskeyusage)Added SecTrustSettingsKeyUsage.init(rawValue: uint32)Added [SecTrustSettingsKeyUsage.UseAny](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/ksectrustsettingskeyuseany)Added [SecTrustSettingsKeyUsage.UseEnDecryptData](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1394291-useendecryptdata)Added [SecTrustSettingsKeyUsage.UseEnDecryptKey](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/ksectrustsettingskeyuseendecryptkey)Added [SecTrustSettingsKeyUsage.UseKeyExchange](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1392796-usekeyexchange)Added [SecTrustSettingsKeyUsage.UseSignature](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1392354-usesignature)Added [SecTrustSettingsKeyUsage.UseSignCert](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/ksectrustsettingskeyusesigncert)Added [SecTrustSettingsKeyUsage.UseSignRevocation](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1400014-usesignrevocation)Added [SecTrustSettingsResult [enum]](https://developer.apple.com/documentation/security/sectrustsettingsresult)Added [SecTrustSettingsResult.Deny](https://developer.apple.com/documentation/security/sectrustsettingsresult/deny)Added [SecTrustSettingsResult.Invalid](https://developer.apple.com/documentation/security/sectrustsettingsresult/invalid)Added [SecTrustSettingsResult.TrustAsRoot](https://developer.apple.com/documentation/security/sectrustsettingsresult/ksectrustsettingsresulttrustasroot)Added [SecTrustSettingsResult.TrustRoot](https://developer.apple.com/documentation/security/sectrustsettingsresult/ksectrustsettingsresulttrustroot)Added [SecTrustSettingsResult.Unspecified](https://developer.apple.com/documentation/security/sectrustsettingsresult/unspecified)Added [SSLAuthenticate [enum]](https://developer.apple.com/documentation/security/sslauthenticate)Added [SSLAuthenticate.AlwaysAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/alwaysauthenticate)Added [SSLAuthenticate.NeverAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/neverauthenticate)Added [SSLAuthenticate.TryAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/ktryauthenticate)Added [SSLClientCertificateState [enum]](https://developer.apple.com/documentation/security/sslclientcertificatestate)Added [SSLClientCertificateState.CertNone](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertnone)Added [SSLClientCertificateState.CertRejected](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertrejected)Added [SSLClientCertificateState.CertRequested](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertrequested)Added [SSLClientCertificateState.CertSent](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertsent)Added [SSLConnectionType [enum]](https://developer.apple.com/documentation/security/sslconnectiontype)Added [SSLConnectionType.DatagramType](https://developer.apple.com/documentation/security/sslconnectiontype/datagramtype)Added [SSLConnectionType.StreamType](https://developer.apple.com/documentation/security/sslconnectiontype/ksslstreamtype)Added [SSLProtocol [enum]](https://developer.apple.com/documentation/security/sslprotocol)Added [SSLProtocol.DTLSProtocol1](https://developer.apple.com/documentation/security/sslprotocol/dtlsprotocol1)Added [SSLProtocol.SSLProtocol2](https://developer.apple.com/documentation/security/sslprotocol/ksslprotocol2)Added [SSLProtocol.SSLProtocol3](https://developer.apple.com/documentation/security/sslprotocol/sslprotocol3)Added [SSLProtocol.SSLProtocol3Only](https://developer.apple.com/documentation/security/sslprotocol/sslprotocol3only)Added [SSLProtocol.SSLProtocolAll](https://developer.apple.com/documentation/security/sslprotocol/sslprotocolall)Added [SSLProtocol.SSLProtocolUnknown](https://developer.apple.com/documentation/security/sslprotocol/sslprotocolunknown)Added [SSLProtocol.TLSProtocol1](https://developer.apple.com/documentation/security/sslprotocol/ktlsprotocol1)Added [SSLProtocol.TLSProtocol11](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol11)Added [SSLProtocol.TLSProtocol12](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol12)Added [SSLProtocol.TLSProtocol1Only](https://developer.apple.com/documentation/security/sslprotocol/ktlsprotocol1only)Added [SSLProtocolSide [enum]](https://developer.apple.com/documentation/security/sslprotocolside)Added [SSLProtocolSide.ClientSide](https://developer.apple.com/documentation/security/sslprotocolside/ksslclientside)Added [SSLProtocolSide.ServerSide](https://developer.apple.com/documentation/security/sslprotocolside/serverside)Added [SSLSessionOption [enum]](https://developer.apple.com/documentation/security/sslsessionoption)Added [SSLSessionOption.AllowServerIdentityChange](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionallowserveridentitychange)Added [SSLSessionOption.BreakOnCertRequested](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakoncertrequested)Added [SSLSessionOption.BreakOnClientAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclientauth)Added [SSLSessionOption.BreakOnClientHello](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclienthello)Added [SSLSessionOption.BreakOnServerAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonserverauth)Added [SSLSessionOption.Fallback](https://developer.apple.com/documentation/security/sslsessionoption/fallback)Added [SSLSessionOption.FalseStart](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionfalsestart)Added [SSLSessionOption.SendOneByteRecord](https://developer.apple.com/documentation/security/sslsessionoption/sendonebyterecord)Added [SSLSessionState [enum]](https://developer.apple.com/documentation/security/sslsessionstate)Added [SSLSessionState.Aborted](https://developer.apple.com/documentation/security/sslsessionstate/ksslaborted)Added [SSLSessionState.Closed](https://developer.apple.com/documentation/security/sslsessionstate/ksslclosed)Added [SSLSessionState.Connected](https://developer.apple.com/documentation/security/sslsessionstate/connected)Added [SSLSessionState.Handshake](https://developer.apple.com/documentation/security/sslsessionstate/ksslhandshake)Added [SSLSessionState.Idle](https://developer.apple.com/documentation/security/sslsessionstate/ksslidle)Added SSLSessionStrengthPolicy [enum]Added SSLSessionStrengthPolicy.ATSv1Added SSLSessionStrengthPolicy.DefaultAdded [CMSEncoderSetSignerAlgorithm(_: CMSEncoder, _: CFString) -> OSStatus](https://developer.apple.com/documentation/security/1387135-cmsencodersetsigneralgorithm)Added [CSSM_PADDING_SIGRAW](https://developer.apple.com/documentation/security/1568331-anonymous/cssm_padding_sigraw)Added [DERByte](https://developer.apple.com/documentation/security/derbyte)Added [DERSize](https://developer.apple.com/documentation/security/dersize)Added [errSecCSInvalidPlatform](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidplatform)Added [errSecCSInvalidSymlink](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidsymlink)Added [errSecCSTooBig](https://developer.apple.com/documentation/security/errseccstoobig)Added [errSSLClientHelloReceived](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslclienthelloreceived)Added [errSSLWeakPeerEphemeralDHKey](https://developer.apple.com/documentation/security/errsslweakpeerephemeraldhkey)Added [kCMSEncoderDigestAlgorithmSHA1](https://developer.apple.com/documentation/security/kcmsencoderdigestalgorithmsha1)Added [kCMSEncoderDigestAlgorithmSHA256](https://developer.apple.com/documentation/security/kcmsencoderdigestalgorithmsha256)Added [kSecCodeInfoPlatformIdentifier](https://developer.apple.com/documentation/security/kseccodeinfoplatformidentifier)Added [kSecCSRestrictSymlinks](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsrestrictsymlinks)Added [kSecPolicyApplePayIssuerEncryption](https://developer.apple.com/documentation/security/ksecpolicyapplepayissuerencryption)Added [kSecUseAuthenticationContext](https://developer.apple.com/documentation/security/ksecuseauthenticationcontext)Added [kSecUseAuthenticationUI](https://developer.apple.com/documentation/security/ksecuseauthenticationui)Added [kSecUseAuthenticationUIAllow](https://developer.apple.com/documentation/security/ksecuseauthenticationuiallow)Added [kSecUseAuthenticationUIFail](https://developer.apple.com/documentation/security/ksecuseauthenticationuifail)Added [kSecUseAuthenticationUISkip](https://developer.apple.com/documentation/security/ksecuseauthenticationuiskip)Added [kSecUseOperationPrompt](https://developer.apple.com/documentation/security/ksecuseoperationprompt)Added [oidAdCAIssuer](https://developer.apple.com/documentation/security/oidadcaissuer)Added [oidAdOCSP](https://developer.apple.com/documentation/security/oidadocsp)Added [oidAnyExtendedKeyUsage](https://developer.apple.com/documentation/security/oidanyextendedkeyusage)Added [oidAnyPolicy](https://developer.apple.com/documentation/security/oidanypolicy)Added [oidAuthorityInfoAccess](https://developer.apple.com/documentation/security/oidauthorityinfoaccess)Added [oidAuthorityKeyIdentifier](https://developer.apple.com/documentation/security/oidauthoritykeyidentifier)Added [oidBasicConstraints](https://developer.apple.com/documentation/security/oidbasicconstraints)Added [oidCertificatePolicies](https://developer.apple.com/documentation/security/oidcertificatepolicies)Added [oidCommonName](https://developer.apple.com/documentation/security/oidcommonname)Added [oidCountryName](https://developer.apple.com/documentation/security/oidcountryname)Added [oidCrlDistributionPoints](https://developer.apple.com/documentation/security/oidcrldistributionpoints)Added [oidDescription](https://developer.apple.com/documentation/security/oiddescription)Added [oidEcPubKey](https://developer.apple.com/documentation/security/oidecpubkey)Added [oidEmailAddress](https://developer.apple.com/documentation/security/oidemailaddress)Added [oidEntrustVersInfo](https://developer.apple.com/documentation/security/oidentrustversinfo)Added [oidExtendedKeyUsage](https://developer.apple.com/documentation/security/oidextendedkeyusage)Added [oidExtendedKeyUsageClientAuth](https://developer.apple.com/documentation/security/oidextendedkeyusageclientauth)Added [oidExtendedKeyUsageCodeSigning](https://developer.apple.com/documentation/security/oidextendedkeyusagecodesigning)Added [oidExtendedKeyUsageEmailProtection](https://developer.apple.com/documentation/security/oidextendedkeyusageemailprotection)Added [oidExtendedKeyUsageIPSec](https://developer.apple.com/documentation/security/oidextendedkeyusageipsec)Added [oidExtendedKeyUsageMicrosoftSGC](https://developer.apple.com/documentation/security/oidextendedkeyusagemicrosoftsgc)Added [oidExtendedKeyUsageNetscapeSGC](https://developer.apple.com/documentation/security/oidextendedkeyusagenetscapesgc)Added [oidExtendedKeyUsageOCSPSigning](https://developer.apple.com/documentation/security/oidextendedkeyusageocspsigning)Added [oidExtendedKeyUsageServerAuth](https://developer.apple.com/documentation/security/oidextendedkeyusageserverauth)Added [oidExtendedKeyUsageTimeStamping](https://developer.apple.com/documentation/security/oidextendedkeyusagetimestamping)Added [oidFee](https://developer.apple.com/documentation/security/oidfee)Added [oidFriendlyName](https://developer.apple.com/documentation/security/oidfriendlyname)Added [oidGoogleEmbeddedSignedCertificateTimestamp](https://developer.apple.com/documentation/security/oidgoogleembeddedsignedcertificatetimestamp)Added [oidGoogleOCSPSignedCertificateTimestamp](https://developer.apple.com/documentation/security/oidgoogleocspsignedcertificatetimestamp)Added [oidInhibitAnyPolicy](https://developer.apple.com/documentation/security/oidinhibitanypolicy)Added [oidIssuerAltName](https://developer.apple.com/documentation/security/oidissueraltname)Added [oidKeyUsage](https://developer.apple.com/documentation/security/oidkeyusage)Added [oidLocalityName](https://developer.apple.com/documentation/security/oidlocalityname)Added [oidLocalKeyId](https://developer.apple.com/documentation/security/oidlocalkeyid)Added [oidMd2](https://developer.apple.com/documentation/security/oidmd2)Added [oidMd2Rsa](https://developer.apple.com/documentation/security/oidmd2rsa)Added [oidMd4](https://developer.apple.com/documentation/security/oidmd4)Added [oidMd4Rsa](https://developer.apple.com/documentation/security/oidmd4rsa)Added [oidMd5](https://developer.apple.com/documentation/security/oidmd5)Added [oidMd5Fee](https://developer.apple.com/documentation/security/oidmd5fee)Added [oidMd5Rsa](https://developer.apple.com/documentation/security/oidmd5rsa)Added [oidMSNTPrincipalName](https://developer.apple.com/documentation/security/oidmsntprincipalname)Added [oidNameConstraints](https://developer.apple.com/documentation/security/oidnameconstraints)Added [oidNetscapeCertType](https://developer.apple.com/documentation/security/oidnetscapecerttype)Added [oidOrganizationalUnitName](https://developer.apple.com/documentation/security/oidorganizationalunitname)Added [oidOrganizationName](https://developer.apple.com/documentation/security/oidorganizationname)Added [oidPolicyConstraints](https://developer.apple.com/documentation/security/oidpolicyconstraints)Added [oidPolicyMappings](https://developer.apple.com/documentation/security/oidpolicymappings)Added [oidPrivateKeyUsagePeriod](https://developer.apple.com/documentation/security/oidprivatekeyusageperiod)Added [oidQtCps](https://developer.apple.com/documentation/security/oidqtcps)Added [oidQtUNotice](https://developer.apple.com/documentation/security/oidqtunotice)Added [oidRsa](https://developer.apple.com/documentation/security/oidrsa)Added [oidSha1](https://developer.apple.com/documentation/security/oidsha1)Added [oidSha1Dsa](https://developer.apple.com/documentation/security/oidsha1dsa)Added [oidSha1DsaCommonOIW](https://developer.apple.com/documentation/security/oidsha1dsacommonoiw)Added [oidSha1DsaOIW](https://developer.apple.com/documentation/security/oidsha1dsaoiw)Added [oidSha1Ecdsa](https://developer.apple.com/documentation/security/oidsha1ecdsa)Added [oidSha1Fee](https://developer.apple.com/documentation/security/oidsha1fee)Added [oidSha1Rsa](https://developer.apple.com/documentation/security/oidsha1rsa)Added [oidSha1RsaOIW](https://developer.apple.com/documentation/security/oidsha1rsaoiw)Added [oidSha224](https://developer.apple.com/documentation/security/oidsha224)Added [oidSha224Ecdsa](https://developer.apple.com/documentation/security/oidsha224ecdsa)Added [oidSha224Rsa](https://developer.apple.com/documentation/security/oidsha224rsa)Added [oidSha256](https://developer.apple.com/documentation/security/oidsha256)Added [oidSha256Ecdsa](https://developer.apple.com/documentation/security/oidsha256ecdsa)Added [oidSha256Rsa](https://developer.apple.com/documentation/security/oidsha256rsa)Added [oidSha384](https://developer.apple.com/documentation/security/oidsha384)Added [oidSha384Ecdsa](https://developer.apple.com/documentation/security/oidsha384ecdsa)Added [oidSha384Rsa](https://developer.apple.com/documentation/security/oidsha384rsa)Added [oidSha512](https://developer.apple.com/documentation/security/oidsha512)Added [oidSha512Ecdsa](https://developer.apple.com/documentation/security/oidsha512ecdsa)Added [oidSha512Rsa](https://developer.apple.com/documentation/security/oidsha512rsa)Added [oidStateOrProvinceName](https://developer.apple.com/documentation/security/oidstateorprovincename)Added [oidSubjectAltName](https://developer.apple.com/documentation/security/oidsubjectaltname)Added [oidSubjectInfoAccess](https://developer.apple.com/documentation/security/oidsubjectinfoaccess)Added [oidSubjectKeyIdentifier](https://developer.apple.com/documentation/security/oidsubjectkeyidentifier)Added SSLSetSessionStrengthPolicy(_: SSLContext, _: SSLSessionStrengthPolicy) -> OSStatusModified [AuthorizationItem [struct]](https://developer.apple.com/documentation/security/authorizationitem)

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationItem {     var name: AuthorizationString     var valueLength: Int     var value: UnsafeMutablePointer<Void>     var flags: UInt32     init()     init(name name: AuthorizationString, valueLength valueLength: Int, value value: UnsafeMutablePointer<Void>, flags flags: UInt32) } ``` |
| To | ``` struct AuthorizationItem {     var name: AuthorizationString     var valueLength: Int     var value: UnsafeMutablePointer<Void>     var flags: UInt32 } ``` |

Modified [AuthorizationItemSet [struct]](https://developer.apple.com/documentation/security/authorizationitemset)

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationItemSet {     var count: UInt32     var items: UnsafeMutablePointer<AuthorizationItem>     init()     init(count count: UInt32, items items: UnsafeMutablePointer<AuthorizationItem>) } ``` |
| To | ``` struct AuthorizationItemSet {     var count: UInt32     var items: UnsafeMutablePointer<AuthorizationItem> } ``` |

Modified cssm_access_credentials [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_access_credentials {     var EntryTag: CSSM_STRING     var BaseCerts: CSSM_BASE_CERTS     var Samples: CSSM_SAMPLEGROUP     var Callback: CSSM_CHALLENGE_CALLBACK     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(EntryTag EntryTag: CSSM_STRING, BaseCerts BaseCerts: CSSM_BASE_CERTS, Samples Samples: CSSM_SAMPLEGROUP, Callback Callback: CSSM_CHALLENGE_CALLBACK, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_access_credentials {     var EntryTag: CSSM_STRING     var BaseCerts: CSSM_BASE_CERTS     var Samples: CSSM_SAMPLEGROUP     var Callback: CSSM_CHALLENGE_CALLBACK!     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(EntryTag EntryTag: CSSM_STRING, BaseCerts BaseCerts: CSSM_BASE_CERTS, Samples Samples: CSSM_SAMPLEGROUP, Callback Callback: CSSM_CHALLENGE_CALLBACK!, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_access_credentials.Callback

|  | Declaration |
| --- | --- |
| From | ``` var Callback: CSSM_CHALLENGE_CALLBACK ``` |
| To | ``` var Callback: CSSM_CHALLENGE_CALLBACK! ``` |

Modified cssm_acl_entry_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_input {     var Prototype: CSSM_ACL_ENTRY_PROTOTYPE     var Callback: CSSM_ACL_SUBJECT_CALLBACK     var CallerContext: UnsafeMutablePointer<Void>     init()     init(Prototype Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback Callback: CSSM_ACL_SUBJECT_CALLBACK, CallerContext CallerContext: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_acl_entry_input {     var Prototype: CSSM_ACL_ENTRY_PROTOTYPE     var Callback: CSSM_ACL_SUBJECT_CALLBACK!     var CallerContext: UnsafeMutablePointer<Void>     init()     init(Prototype Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback Callback: CSSM_ACL_SUBJECT_CALLBACK!, CallerContext CallerContext: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_acl_entry_input.Callback

|  | Declaration |
| --- | --- |
| From | ``` var Callback: CSSM_ACL_SUBJECT_CALLBACK ``` |
| To | ``` var Callback: CSSM_ACL_SUBJECT_CALLBACK! ``` |

Modified cssm_appledl_open_parameters_mask [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct cssm_appledl_open_parameters_mask {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct cssm_appledl_open_parameters_mask : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified cssm_crypto_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crypto_data {     var Param: CSSM_DATA     var Callback: CSSM_CALLBACK     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(Param Param: CSSM_DATA, Callback Callback: CSSM_CALLBACK, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_crypto_data {     var Param: CSSM_DATA     var Callback: CSSM_CALLBACK!     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(Param Param: CSSM_DATA, Callback Callback: CSSM_CALLBACK!, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_crypto_data.Callback

|  | Declaration |
| --- | --- |
| From | ``` var Callback: CSSM_CALLBACK ``` |
| To | ``` var Callback: CSSM_CALLBACK! ``` |

Modified [cssm_func_name_addr [struct]](https://developer.apple.com/documentation/security/cssm_func_name_addr)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_func_name_addr {     var Name: CSSM_STRING     var Address: CSSM_PROC_ADDR     init()     init(Name Name: CSSM_STRING, Address Address: CSSM_PROC_ADDR) } ``` |
| To | ``` struct cssm_func_name_addr {     var Name: CSSM_STRING     var Address: CSSM_PROC_ADDR!     init()     init(Name Name: CSSM_STRING, Address Address: CSSM_PROC_ADDR!) } ``` |

Modified cssm_func_name_addr.Address

|  | Declaration |
| --- | --- |
| From | ``` var Address: CSSM_PROC_ADDR ``` |
| To | ``` var Address: CSSM_PROC_ADDR! ``` |

Modified cssm_manager_registration_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_manager_registration_info {     var Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>     var Terminate: CFunctionPointer<(() -> CSSM_RETURN)>     var RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>     var DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>     var EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>     var RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>     init()     init(Initialize Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>, Terminate Terminate: CFunctionPointer<(() -> CSSM_RETURN)>, RegisterDispatchTable RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>, DeregisterDispatchTable DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>, EventNotifyManager EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>, RefreshFunctionTable RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>) } ``` |
| To | ``` struct cssm_manager_registration_info {     var Initialize: ((uint32, uint32) -> CSSM_RETURN)!     var Terminate: (() -> CSSM_RETURN)!     var RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)!     var DeregisterDispatchTable: (() -> CSSM_RETURN)!     var EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!     var RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!     init()     init(Initialize Initialize: ((uint32, uint32) -> CSSM_RETURN)!, Terminate Terminate: (() -> CSSM_RETURN)!, RegisterDispatchTable RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)!, DeregisterDispatchTable DeregisterDispatchTable: (() -> CSSM_RETURN)!, EventNotifyManager EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!, RefreshFunctionTable RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!) } ``` |

Modified cssm_manager_registration_info.DeregisterDispatchTable

|  | Declaration |
| --- | --- |
| From | ``` var DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)> ``` |
| To | ``` var DeregisterDispatchTable: (() -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.EventNotifyManager

|  | Declaration |
| --- | --- |
| From | ``` var EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> ``` |
| To | ``` var EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.Initialize

|  | Declaration |
| --- | --- |
| From | ``` var Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var Initialize: ((uint32, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.RefreshFunctionTable

|  | Declaration |
| --- | --- |
| From | ``` var RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.RegisterDispatchTable

|  | Declaration |
| --- | --- |
| From | ``` var RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.Terminate

|  | Declaration |
| --- | --- |
| From | ``` var Terminate: CFunctionPointer<(() -> CSSM_RETURN)> ``` |
| To | ``` var Terminate: (() -> CSSM_RETURN)! ``` |

Modified [cssm_memory_funcs [struct]](https://developer.apple.com/documentation/security/cssm_memory_funcs)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_memory_funcs {     var malloc_func: CSSM_MALLOC     var free_func: CSSM_FREE     var realloc_func: CSSM_REALLOC     var calloc_func: CSSM_CALLOC     var AllocRef: UnsafeMutablePointer<Void>     init()     init(malloc_func malloc_func: CSSM_MALLOC, free_func free_func: CSSM_FREE, realloc_func realloc_func: CSSM_REALLOC, calloc_func calloc_func: CSSM_CALLOC, AllocRef AllocRef: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_memory_funcs {     var malloc_func: CSSM_MALLOC!     var free_func: CSSM_FREE!     var realloc_func: CSSM_REALLOC!     var calloc_func: CSSM_CALLOC!     var AllocRef: UnsafeMutablePointer<Void>     init()     init(malloc_func malloc_func: CSSM_MALLOC!, free_func free_func: CSSM_FREE!, realloc_func realloc_func: CSSM_REALLOC!, calloc_func calloc_func: CSSM_CALLOC!, AllocRef AllocRef: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_memory_funcs.calloc_func

|  | Declaration |
| --- | --- |
| From | ``` var calloc_func: CSSM_CALLOC ``` |
| To | ``` var calloc_func: CSSM_CALLOC! ``` |

Modified cssm_memory_funcs.free_func

|  | Declaration |
| --- | --- |
| From | ``` var free_func: CSSM_FREE ``` |
| To | ``` var free_func: CSSM_FREE! ``` |

Modified cssm_memory_funcs.malloc_func

|  | Declaration |
| --- | --- |
| From | ``` var malloc_func: CSSM_MALLOC ``` |
| To | ``` var malloc_func: CSSM_MALLOC! ``` |

Modified cssm_memory_funcs.realloc_func

|  | Declaration |
| --- | --- |
| From | ``` var realloc_func: CSSM_REALLOC ``` |
| To | ``` var realloc_func: CSSM_REALLOC! ``` |

Modified cssm_module_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_module_funcs {     var ServiceType: CSSM_SERVICE_TYPE     var NumberOfServiceFuncs: uint32     var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR>     init()     init(ServiceType ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs NumberOfServiceFuncs: uint32, ServiceFuncs ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR>) } ``` |
| To | ``` struct cssm_module_funcs {     var ServiceType: CSSM_SERVICE_TYPE     var NumberOfServiceFuncs: uint32     var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?>     init()     init(ServiceType ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs NumberOfServiceFuncs: uint32, ServiceFuncs ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?>) } ``` |

Modified cssm_module_funcs.ServiceFuncs

|  | Declaration |
| --- | --- |
| From | ``` var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR> ``` |
| To | ``` var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?> ``` |

Modified cssm_spi_ac_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_ac_funcs {     var AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>     init()     init(AuthCompute AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>, PassThrough PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>) } ``` |
| To | ``` struct cssm_spi_ac_funcs {     var AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)!     var PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(AuthCompute AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_ac_funcs.AuthCompute

|  | Declaration |
| --- | --- |
| From | ``` var AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_ac_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ```  ``` |
| To | ``` struct cssm_spi_cl_funcs {     var CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!     var CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)!     var CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!     var CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!     var CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!     var CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!     var PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(CertCreateTemplate CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertVerify CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CertVerifyWithKey CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, CertGetFirstFieldValue CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextFieldValue CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortQuery CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGetKeyInfo CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)!, CertGetAllFields CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFields FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFieldValue FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertCache CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, CertGetFirstCachedFieldValue CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextCachedFieldValue CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortCache CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGroupToSignedBundle CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGroupFromVerifiedBundle CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertDescribeFormat CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, CrlCreateTemplate CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSetFields CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlAddCert CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlRemoveCert CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CrlVerifyWithKey CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, IsCertInCrl IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, CrlGetFirstFieldValue CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextFieldValue CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlAbortQuery CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlGetAllFields CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlCache CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, IsCertInCachedCrl IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlGetFirstCachedFieldValue CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextCachedFieldValue CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetAllCachedRecordFields CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlAbortCache CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlDescribeFormat CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_cl_funcs.CertAbortCache

|  | Declaration |
| --- | --- |
| From | ``` var CertAbortCache: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertAbortQuery

|  | Declaration |
| --- | --- |
| From | ``` var CertAbortQuery: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertCache

|  | Declaration |
| --- | --- |
| From | ``` var CertCache: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertDescribeFormat

|  | Declaration |
| --- | --- |
| From | ``` var CertDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetAllFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetAllTemplateFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllTemplateFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetFirstCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetFirstFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetKeyInfo

|  | Declaration |
| --- | --- |
| From | ``` var CertGetKeyInfo: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetNextCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetNextFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGroupFromVerifiedBundle

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupFromVerifiedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGroupToSignedBundle

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupToSignedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertSign

|  | Declaration |
| --- | --- |
| From | ``` var CertSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertVerify

|  | Declaration |
| --- | --- |
| From | ``` var CertVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertVerifyWithKey

|  | Declaration |
| --- | --- |
| From | ``` var CertVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlAbortCache

|  | Declaration |
| --- | --- |
| From | ``` var CrlAbortCache: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlAbortQuery

|  | Declaration |
| --- | --- |
| From | ``` var CrlAbortQuery: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlAddCert

|  | Declaration |
| --- | --- |
| From | ``` var CrlAddCert: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlCache

|  | Declaration |
| --- | --- |
| From | ``` var CrlCache: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CrlCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlDescribeFormat

|  | Declaration |
| --- | --- |
| From | ``` var CrlDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetAllCachedRecordFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetAllCachedRecordFields: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetAllFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetFirstCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetFirstFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetNextCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetNextFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlRemoveCert

|  | Declaration |
| --- | --- |
| From | ``` var CrlRemoveCert: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlSetFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlSetFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlSign

|  | Declaration |
| --- | --- |
| From | ``` var CrlSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlVerify

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlVerifyWithKey

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.FreeFields

|  | Declaration |
| --- | --- |
| From | ``` var FreeFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.FreeFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var FreeFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.IsCertInCachedCrl

|  | Declaration |
| --- | --- |
| From | ``` var IsCertInCachedCrl: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.IsCertInCrl

|  | Declaration |
| --- | --- |
| From | ``` var IsCertInCrl: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |
| To | ``` var IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ```  ``` |
| To | ``` struct cssm_spi_csp_funcs {     var EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)!     var SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)!     var SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!     var DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!     var EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!     var DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)!     var GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)!     var WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)!     var FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)!     var PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     var Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)!     var Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!     var ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!     var ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)!     var RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)!     var GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)!     var GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!     var GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!     var ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)!     var GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!     var ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!     var GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!     var ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!     init()     init(EventNotify EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, QuerySize QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)!, SignData SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)!, SignDataInit SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, SignDataUpdate SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, SignDataFinal SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyData VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyDataInit VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyDataUpdate VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyDataFinal VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, DigestData DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, DigestDataInit DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, DigestDataUpdate DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, DigestDataClone DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!, DigestDataFinal DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMac GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMacInit GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, GenerateMacUpdate GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, GenerateMacFinal GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyMac VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyMacInit VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyMacUpdate VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyMacFinal VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, EncryptData EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataInit EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataUpdate EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, EncryptDataFinal EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, DecryptData DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataInit DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataUpdate DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, DecryptDataFinal DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, QueryKeySizeInBits QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)!, GenerateKey GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateKeyPair GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateRandom GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateAlgorithmParams GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)!, WrapKey WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, UnwrapKey UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DeriveKey DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)!, FreeKey FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!, Login Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)!, Logout Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!, ChangeLoginAcl ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, ObtainPrivateKeyFromPublicKey ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)!, RetrieveUniqueId RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCounter RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyDevice VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetTimeValue GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetOperationalStatistics GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)!, GetLoginAcl GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, GetKeyAcl GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeKeyAcl ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)!, GetKeyOwner GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeKeyOwner ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetLoginOwner GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeLoginOwner ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_csp_funcs.ChangeKeyAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeKeyAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ChangeKeyOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeKeyOwner: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ChangeLoginAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeLoginAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ChangeLoginOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeLoginOwner: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptData

|  | Declaration |
| --- | --- |
| From | ``` var DecryptData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptDataInit

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DeriveKey

|  | Declaration |
| --- | --- |
| From | ``` var DeriveKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestData

|  | Declaration |
| --- | --- |
| From | ``` var DigestData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataClone

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataClone: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataInit

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptData

|  | Declaration |
| --- | --- |
| From | ``` var EncryptData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptDataInit

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EventNotify

|  | Declaration |
| --- | --- |
| From | ``` var EventNotify: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.FreeKey

|  | Declaration |
| --- | --- |
| From | ``` var FreeKey: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)> ``` |
| To | ``` var FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateAlgorithmParams

|  | Declaration |
| --- | --- |
| From | ``` var GenerateAlgorithmParams: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateKey

|  | Declaration |
| --- | --- |
| From | ``` var GenerateKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateKeyPair

|  | Declaration |
| --- | --- |
| From | ``` var GenerateKeyPair: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMac

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMac: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMacFinal

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMacInit

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMacUpdate

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateRandom

|  | Declaration |
| --- | --- |
| From | ``` var GenerateRandom: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetKeyAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetKeyAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetKeyOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetKeyOwner: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetLoginAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetLoginAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetLoginOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetLoginOwner: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetOperationalStatistics

|  | Declaration |
| --- | --- |
| From | ``` var GetOperationalStatistics: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)> ``` |
| To | ``` var GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetTimeValue

|  | Declaration |
| --- | --- |
| From | ``` var GetTimeValue: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.Login

|  | Declaration |
| --- | --- |
| From | ``` var Login: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)> ``` |
| To | ``` var Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.Logout

|  | Declaration |
| --- | --- |
| From | ``` var Logout: CFunctionPointer<((CSSM_CSP_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ObtainPrivateKeyFromPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var ObtainPrivateKeyFromPublicKey: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.QueryKeySizeInBits

|  | Declaration |
| --- | --- |
| From | ``` var QueryKeySizeInBits: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.QuerySize

|  | Declaration |
| --- | --- |
| From | ``` var QuerySize: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.RetrieveCounter

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveCounter: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.RetrieveUniqueId

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveUniqueId: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignData

|  | Declaration |
| --- | --- |
| From | ``` var SignData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var SignDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignDataInit

|  | Declaration |
| --- | --- |
| From | ``` var SignDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var SignDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.UnwrapKey

|  | Declaration |
| --- | --- |
| From | ``` var UnwrapKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyData

|  | Declaration |
| --- | --- |
| From | ``` var VerifyData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDataInit

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDevice

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDevice: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMac

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMac: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMacFinal

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMacInit

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMacUpdate

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.WrapKey

|  | Declaration |
| --- | --- |
| From | ``` var WrapKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_dl_funcs {     var DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbClose: CFunctionPointer<((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)>     var DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>     var CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>     var DestroyRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>     var Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>     var GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)>     var ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)>     var GetDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)>     var ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)>     var GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>     var GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>     var FreeNameList: CFunctionPointer<((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>     var DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>     var DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>     var DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataAbortQuery: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var FreeUniqueRecord: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>     init()     init(DbOpen DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose DbClose: CFunctionPointer<((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)>, DbCreate DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbDelete DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>, CreateRelation CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation DestroyRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>, Authenticate Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>, GetDbAcl GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)>, ChangeDbAcl ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)>, GetDbOwner GetDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)>, ChangeDbOwner ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)>, GetDbNames GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList FreeNameList: CFunctionPointer<((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery DataAbortQuery: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord FreeUniqueRecord: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, PassThrough PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>) } ``` |
| To | ``` struct cssm_spi_dl_funcs {     var DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!     var DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)!     var DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!     var DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!     var CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!     var DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!     var Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!     var GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!     var ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!     var GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!     var ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!     var GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!     var GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!     var FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!     var DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!     var DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!     var DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!     var PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(DbOpen DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)!, DbCreate DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbDelete DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, CreateRelation CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!, Authenticate Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, GetDbAcl GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeDbAcl ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, GetDbOwner GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeDbOwner ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetDbNames GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_dl_funcs.Authenticate

|  | Declaration |
| --- | --- |
| From | ``` var Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)> ``` |
| To | ``` var Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.ChangeDbAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.ChangeDbOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.CreateRelation

|  | Declaration |
| --- | --- |
| From | ``` var CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)> ``` |
| To | ``` var CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataAbortQuery

|  | Declaration |
| --- | --- |
| From | ``` var DataAbortQuery: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataDelete

|  | Declaration |
| --- | --- |
| From | ``` var DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)> ``` |
| To | ``` var DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataGetFirst

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataGetFromUniqueRecordId

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataGetNext

|  | Declaration |
| --- | --- |
| From | ``` var DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataInsert

|  | Declaration |
| --- | --- |
| From | ``` var DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataModify

|  | Declaration |
| --- | --- |
| From | ``` var DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)> ``` |
| To | ``` var DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbClose

|  | Declaration |
| --- | --- |
| From | ``` var DbClose: CFunctionPointer<((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbCreate

|  | Declaration |
| --- | --- |
| From | ``` var DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |
| To | ``` var DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbDelete

|  | Declaration |
| --- | --- |
| From | ``` var DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)> ``` |
| To | ``` var DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbOpen

|  | Declaration |
| --- | --- |
| From | ``` var DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |
| To | ``` var DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DestroyRelation

|  | Declaration |
| --- | --- |
| From | ``` var DestroyRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)> ``` |
| To | ``` var DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.FreeNameList

|  | Declaration |
| --- | --- |
| From | ``` var FreeNameList: CFunctionPointer<((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.FreeUniqueRecord

|  | Declaration |
| --- | --- |
| From | ``` var FreeUniqueRecord: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbNameFromHandle

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbNames

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_kr_funcs {     var RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>     var RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>     var GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>     var ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>     var RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>     var RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)>     var GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>     init()     init(RegistrationRequest RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RegistrationRetrieve RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>, GenerateRecoveryFields GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>, ProcessRecoveryFields ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>, RecoveryRequest RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RecoveryRetrieve RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)>, GetRecoveredObject GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, RecoveryRequestAbort RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, PassThrough PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>) } ``` |
| To | ``` struct cssm_spi_kr_funcs {     var RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)!     var GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)!     var ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)!     var GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(RegistrationRequest RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RegistrationRetrieve RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)!, GenerateRecoveryFields GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)!, ProcessRecoveryFields ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, RecoveryRequest RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RecoveryRetrieve RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)!, GetRecoveredObject GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, RecoveryRequestAbort RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_kr_funcs.GenerateRecoveryFields

|  | Declaration |
| --- | --- |
| From | ``` var GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.GetRecoveredObject

|  | Declaration |
| --- | --- |
| From | ``` var GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.ProcessRecoveryFields

|  | Declaration |
| --- | --- |
| From | ``` var ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RecoveryRequest

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RecoveryRequestAbort

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RecoveryRetrieve

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)> ``` |
| To | ``` var RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RegistrationRequest

|  | Declaration |
| --- | --- |
| From | ``` var RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RegistrationRetrieve

|  | Declaration |
| --- | --- |
| From | ``` var RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ```  ``` |
| To | ``` struct cssm_spi_tp_funcs {     var SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)!     var ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)!     var ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)!     var CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)!     var CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!     var FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)!     var CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!     var CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!     var CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!     var CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)!     var TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(SubmitCredRequest SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCredResult RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)!, ConfirmCredResult ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)!, ReceiveConfirmation ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)!, CertReclaimKey CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)!, CertReclaimAbort CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!, FormRequest FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)!, FormSubmit FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)!, CertGroupVerify CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertCreateTemplate CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CrlCreateTemplate CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRevoke CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRemoveFromCrlTemplate CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, ApplyCrlToDb ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertGroupConstruct CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupPrune CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupToTupleGroup CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)!, TupleGroupToCertGroup TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_tp_funcs.ApplyCrlToDb

|  | Declaration |
| --- | --- |
| From | ``` var ApplyCrlToDb: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGetAllTemplateFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllTemplateFields: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupConstruct

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupConstruct: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupPrune

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupPrune: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupToTupleGroup

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupToTupleGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupVerify

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertReclaimAbort

|  | Declaration |
| --- | --- |
| From | ``` var CertReclaimAbort: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertReclaimKey

|  | Declaration |
| --- | --- |
| From | ``` var CertReclaimKey: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertRemoveFromCrlTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertRemoveFromCrlTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertRevoke

|  | Declaration |
| --- | --- |
| From | ``` var CertRevoke: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertSign

|  | Declaration |
| --- | --- |
| From | ``` var CertSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.ConfirmCredResult

|  | Declaration |
| --- | --- |
| From | ``` var ConfirmCredResult: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)> ``` |
| To | ``` var ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CrlCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CrlCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CrlSign

|  | Declaration |
| --- | --- |
| From | ``` var CrlSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CrlVerify

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.FormRequest

|  | Declaration |
| --- | --- |
| From | ``` var FormRequest: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.FormSubmit

|  | Declaration |
| --- | --- |
| From | ``` var FormSubmit: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.ReceiveConfirmation

|  | Declaration |
| --- | --- |
| From | ``` var ReceiveConfirmation: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)> ``` |
| To | ``` var ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.RetrieveCredResult

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveCredResult: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.SubmitCredRequest

|  | Declaration |
| --- | --- |
| From | ``` var SubmitCredRequest: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.TupleGroupToCertGroup

|  | Declaration |
| --- | --- |
| From | ``` var TupleGroupToCertGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_state_funcs {     var cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>     var cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>     var cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>     var cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>     var cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>     var cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>     init()     init(cssm_GetAttachFunctions cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_ReleaseAttachFunctions cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>, cssm_GetAppMemoryFunctions cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>, cssm_IsFuncCallValid cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_DeregisterManagerServices cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>, cssm_DeliverModuleManagerEvent cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>) } ``` |
| To | ``` struct cssm_state_funcs {     var cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!     var cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!     var cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)!     var cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!     var cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)!     var cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!     init()     init(cssm_GetAttachFunctions cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_ReleaseAttachFunctions cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!, cssm_GetAppMemoryFunctions cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)!, cssm_IsFuncCallValid cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_DeregisterManagerServices cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)!, cssm_DeliverModuleManagerEvent cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!) } ``` |

Modified cssm_state_funcs.cssm_DeliverModuleManagerEvent

|  | Declaration |
| --- | --- |
| From | ``` var cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_DeregisterManagerServices

|  | Declaration |
| --- | --- |
| From | ``` var cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_GetAppMemoryFunctions

|  | Declaration |
| --- | --- |
| From | ``` var cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_GetAttachFunctions

|  | Declaration |
| --- | --- |
| From | ``` var cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_IsFuncCallValid

|  | Declaration |
| --- | --- |
| From | ``` var cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_ReleaseAttachFunctions

|  | Declaration |
| --- | --- |
| From | ``` var cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_tp_callerauth_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_callerauth_context {     var Policy: CSSM_TP_POLICYINFO     var VerifyTime: CSSM_TIMESTRING     var VerificationAbortOn: CSSM_TP_STOP_ON     var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK     var NumberOfAnchorCerts: uint32     var AnchorCerts: CSSM_DATA_PTR     var DBList: CSSM_DL_DB_LIST_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(Policy Policy: CSSM_TP_POLICYINFO, VerifyTime VerifyTime: CSSM_TIMESTRING, VerificationAbortOn VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK, NumberOfAnchorCerts NumberOfAnchorCerts: uint32, AnchorCerts AnchorCerts: CSSM_DATA_PTR, DBList DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_callerauth_context {     var Policy: CSSM_TP_POLICYINFO     var VerifyTime: CSSM_TIMESTRING     var VerificationAbortOn: CSSM_TP_STOP_ON     var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK!     var NumberOfAnchorCerts: uint32     var AnchorCerts: CSSM_DATA_PTR     var DBList: CSSM_DL_DB_LIST_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(Policy Policy: CSSM_TP_POLICYINFO, VerifyTime VerifyTime: CSSM_TIMESTRING, VerificationAbortOn VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK!, NumberOfAnchorCerts NumberOfAnchorCerts: uint32, AnchorCerts AnchorCerts: CSSM_DATA_PTR, DBList DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_callerauth_context.CallbackWithVerifiedCert

|  | Declaration |
| --- | --- |
| From | ``` var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK ``` |
| To | ``` var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK! ``` |

Modified cssm_upcalls [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_upcalls {     var malloc_func: CSSM_UPCALLS_MALLOC     var free_func: CSSM_UPCALLS_FREE     var realloc_func: CSSM_UPCALLS_REALLOC     var calloc_func: CSSM_UPCALLS_CALLOC     var CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>     var GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>     init()     init(malloc_func malloc_func: CSSM_UPCALLS_MALLOC, free_func free_func: CSSM_UPCALLS_FREE, realloc_func realloc_func: CSSM_UPCALLS_REALLOC, calloc_func calloc_func: CSSM_UPCALLS_CALLOC, CcToHandle_func CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>, GetModuleInfo_func GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>) } ``` |
| To | ``` struct cssm_upcalls {     var malloc_func: CSSM_UPCALLS_MALLOC!     var free_func: CSSM_UPCALLS_FREE!     var realloc_func: CSSM_UPCALLS_REALLOC!     var calloc_func: CSSM_UPCALLS_CALLOC!     var CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)!     var GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!     init()     init(malloc_func malloc_func: CSSM_UPCALLS_MALLOC!, free_func free_func: CSSM_UPCALLS_FREE!, realloc_func realloc_func: CSSM_UPCALLS_REALLOC!, calloc_func calloc_func: CSSM_UPCALLS_CALLOC!, CcToHandle_func CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)!, GetModuleInfo_func GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!) } ``` |

Modified cssm_upcalls.calloc_func

|  | Declaration |
| --- | --- |
| From | ``` var calloc_func: CSSM_UPCALLS_CALLOC ``` |
| To | ``` var calloc_func: CSSM_UPCALLS_CALLOC! ``` |

Modified cssm_upcalls.CcToHandle_func

|  | Declaration |
| --- | --- |
| From | ``` var CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)! ``` |

Modified cssm_upcalls.free_func

|  | Declaration |
| --- | --- |
| From | ``` var free_func: CSSM_UPCALLS_FREE ``` |
| To | ``` var free_func: CSSM_UPCALLS_FREE! ``` |

Modified cssm_upcalls.GetModuleInfo_func

|  | Declaration |
| --- | --- |
| From | ``` var GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_upcalls.malloc_func

|  | Declaration |
| --- | --- |
| From | ``` var malloc_func: CSSM_UPCALLS_MALLOC ``` |
| To | ``` var malloc_func: CSSM_UPCALLS_MALLOC! ``` |

Modified cssm_upcalls.realloc_func

|  | Declaration |
| --- | --- |
| From | ``` var realloc_func: CSSM_UPCALLS_REALLOC ``` |
| To | ``` var realloc_func: CSSM_UPCALLS_REALLOC! ``` |

Modified extension_data_format [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct extension_data_format {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct extension_data_format : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified mds_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mds_funcs {     var DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>     var GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>     var GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>     var FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>     var DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>     var DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>     var DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>     var CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>     var DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>     init()     init(DbOpen DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>, GetDbNames GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, CreateRelation CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>) } ``` |
| To | ``` struct mds_funcs {     var DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!     var DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!     var GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!     var GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!     var FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!     var DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!     var DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!     var DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!     var CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!     var DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!     init()     init(DbOpen DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!, GetDbNames GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, CreateRelation CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!) } ``` |

Modified mds_funcs.CreateRelation

|  | Declaration |
| --- | --- |
| From | ``` var CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)> ``` |
| To | ``` var CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataAbortQuery

|  | Declaration |
| --- | --- |
| From | ``` var DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataDelete

|  | Declaration |
| --- | --- |
| From | ``` var DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)> ``` |
| To | ``` var DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataGetFirst

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataGetFromUniqueRecordId

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataGetNext

|  | Declaration |
| --- | --- |
| From | ``` var DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataInsert

|  | Declaration |
| --- | --- |
| From | ``` var DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataModify

|  | Declaration |
| --- | --- |
| From | ``` var DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)> ``` |
| To | ``` var DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DbClose

|  | Declaration |
| --- | --- |
| From | ``` var DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)> ``` |
| To | ``` var DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DbOpen

|  | Declaration |
| --- | --- |
| From | ``` var DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |
| To | ``` var DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DestroyRelation

|  | Declaration |
| --- | --- |
| From | ``` var DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)> ``` |
| To | ``` var DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)! ``` |

Modified mds_funcs.FreeNameList

|  | Declaration |
| --- | --- |
| From | ``` var FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)! ``` |

Modified mds_funcs.FreeUniqueRecord

|  | Declaration |
| --- | --- |
| From | ``` var FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)! ``` |

Modified mds_funcs.GetDbNameFromHandle

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)! ``` |

Modified mds_funcs.GetDbNames

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)! ``` |

Modified [SecAccessControlCreateFlags [struct]](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecAccessControlCreateFlags : RawOptionSetType {     init(_ rawValue: CFIndex)     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get } } ``` | RawOptionSetType |
| To | ``` struct SecAccessControlCreateFlags : OptionSetType {     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get }     static var TouchIDAny: SecAccessControlCreateFlags { get }     static var TouchIDCurrentSet: SecAccessControlCreateFlags { get }     static var DevicePasscode: SecAccessControlCreateFlags { get }     static var Or: SecAccessControlCreateFlags { get }     static var And: SecAccessControlCreateFlags { get }     static var PrivateKeyUsage: SecAccessControlCreateFlags { get }     static var ApplicationPassword: SecAccessControlCreateFlags { get } } ``` | OptionSetType |

Modified [SecAsn1Template_struct [struct]](https://developer.apple.com/documentation/security/secasn1template)

|  | Declaration |
| --- | --- |
| From | ``` struct SecAsn1Template_struct {     var kind: UInt32     var offset: UInt32     var sub: UnsafePointer<Void>     var size: UInt32     init()     init(kind kind: UInt32, offset offset: UInt32, sub sub: UnsafePointer<Void>, size size: UInt32) } ``` |
| To | ``` struct SecAsn1Template_struct {     var kind: UInt32     var offset: UInt32     var sub: UnsafePointer<Void>     var size: UInt32 } ``` |

Modified [SecItemImportExportKeyParameters [struct]](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters)

|  | Declaration |
| --- | --- |
| From | ``` struct SecItemImportExportKeyParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>!     var alertTitle: Unmanaged<CFString>!     var alertPrompt: Unmanaged<CFString>!     var accessRef: Unmanaged<SecAccess>!     var keyUsage: Unmanaged<CFArray>!     var keyAttributes: Unmanaged<CFArray>!     init()     init(version version: UInt32, flags flags: SecKeyImportExportFlags, passphrase passphrase: Unmanaged<AnyObject>!, alertTitle alertTitle: Unmanaged<CFString>!, alertPrompt alertPrompt: Unmanaged<CFString>!, accessRef accessRef: Unmanaged<SecAccess>!, keyUsage keyUsage: Unmanaged<CFArray>!, keyAttributes keyAttributes: Unmanaged<CFArray>!) } ``` |
| To | ``` struct SecItemImportExportKeyParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>     var alertTitle: Unmanaged<CFString>     var alertPrompt: Unmanaged<CFString>     var accessRef: Unmanaged<SecAccess>?     var keyUsage: Unmanaged<CFArray>?     var keyAttributes: Unmanaged<CFArray>? } ``` |

Modified [SecItemImportExportKeyParameters.accessRef](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1398564-accessref)

|  | Declaration |
| --- | --- |
| From | ``` var accessRef: Unmanaged<SecAccess>! ``` |
| To | ``` var accessRef: Unmanaged<SecAccess>? ``` |

Modified [SecItemImportExportKeyParameters.alertPrompt](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1395301-alertprompt)

|  | Declaration |
| --- | --- |
| From | ``` var alertPrompt: Unmanaged<CFString>! ``` |
| To | ``` var alertPrompt: Unmanaged<CFString> ``` |

Modified [SecItemImportExportKeyParameters.alertTitle](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1395420-alerttitle)

|  | Declaration |
| --- | --- |
| From | ``` var alertTitle: Unmanaged<CFString>! ``` |
| To | ``` var alertTitle: Unmanaged<CFString> ``` |

Modified [SecItemImportExportKeyParameters.keyAttributes](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1400902-keyattributes)

|  | Declaration |
| --- | --- |
| From | ``` var keyAttributes: Unmanaged<CFArray>! ``` |
| To | ``` var keyAttributes: Unmanaged<CFArray>? ``` |

Modified [SecItemImportExportKeyParameters.keyUsage](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1401903-keyusage)

|  | Declaration |
| --- | --- |
| From | ``` var keyUsage: Unmanaged<CFArray>! ``` |
| To | ``` var keyUsage: Unmanaged<CFArray>? ``` |

Modified [SecItemImportExportKeyParameters.passphrase](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1395469-passphrase)

|  | Declaration |
| --- | --- |
| From | ``` var passphrase: Unmanaged<AnyObject>! ``` |
| To | ``` var passphrase: Unmanaged<AnyObject> ``` |

Modified [SecKeychainAttribute [struct]](https://developer.apple.com/documentation/security/seckeychainattribute)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttribute {     var tag: SecKeychainAttrType     var length: UInt32     var data: UnsafeMutablePointer<Void>     init()     init(tag tag: SecKeychainAttrType, length length: UInt32, data data: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct SecKeychainAttribute {     var tag: SecKeychainAttrType     var length: UInt32     var data: UnsafeMutablePointer<Void> } ``` |

Modified [SecKeychainAttributeInfo [struct]](https://developer.apple.com/documentation/security/seckeychainattributeinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttributeInfo {     var count: UInt32     var tag: UnsafeMutablePointer<UInt32>     var format: UnsafeMutablePointer<UInt32>     init()     init(count count: UInt32, tag tag: UnsafeMutablePointer<UInt32>, format format: UnsafeMutablePointer<UInt32>) } ``` |
| To | ``` struct SecKeychainAttributeInfo {     var count: UInt32     var tag: UnsafeMutablePointer<UInt32>     var format: UnsafeMutablePointer<UInt32> } ``` |

Modified [SecKeychainAttributeList [struct]](https://developer.apple.com/documentation/security/seckeychainattributelist)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttributeList {     var count: UInt32     var attr: UnsafeMutablePointer<SecKeychainAttribute>     init()     init(count count: UInt32, attr attr: UnsafeMutablePointer<SecKeychainAttribute>) } ``` |
| To | ``` struct SecKeychainAttributeList {     var count: UInt32     var attr: UnsafeMutablePointer<SecKeychainAttribute> } ``` |

Modified [SecKeychainCallbackInfo [struct]](https://developer.apple.com/documentation/security/seckeychaincallbackinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainCallbackInfo {     var version: UInt32     var item: Unmanaged<SecKeychainItem>!     var keychain: Unmanaged<SecKeychain>!     var pid: pid_t     init()     init(version version: UInt32, item item: Unmanaged<SecKeychainItem>!, keychain keychain: Unmanaged<SecKeychain>!, pid pid: pid_t) } ``` |
| To | ``` struct SecKeychainCallbackInfo {     var version: UInt32     var item: Unmanaged<SecKeychainItem>     var keychain: Unmanaged<SecKeychain>     var pid: pid_t } ``` |

Modified [SecKeychainCallbackInfo.item](https://developer.apple.com/documentation/security/seckeychaincallbackinfo/1396879-item)

|  | Declaration |
| --- | --- |
| From | ``` var item: Unmanaged<SecKeychainItem>! ``` |
| To | ``` var item: Unmanaged<SecKeychainItem> ``` |

Modified [SecKeychainCallbackInfo.keychain](https://developer.apple.com/documentation/security/seckeychaincallbackinfo/1398536-keychain)

|  | Declaration |
| --- | --- |
| From | ``` var keychain: Unmanaged<SecKeychain>! ``` |
| To | ``` var keychain: Unmanaged<SecKeychain> ``` |

Modified [SecKeychainSettings [struct]](https://developer.apple.com/documentation/security/seckeychainsettings)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainSettings {     var version: UInt32     var lockOnSleep: Boolean     var useLockInterval: Boolean     var lockInterval: UInt32     init()     init(version version: UInt32, lockOnSleep lockOnSleep: Boolean, useLockInterval useLockInterval: Boolean, lockInterval lockInterval: UInt32) } ``` |
| To | ``` struct SecKeychainSettings {     var version: UInt32     var lockOnSleep: DarwinBoolean     var useLockInterval: DarwinBoolean     var lockInterval: UInt32     init()     init(version version: UInt32, lockOnSleep lockOnSleep: DarwinBoolean, useLockInterval useLockInterval: DarwinBoolean, lockInterval lockInterval: UInt32) } ``` |

Modified [SecKeychainSettings.lockOnSleep](https://developer.apple.com/documentation/security/seckeychainsettings/1397550-lockonsleep)

|  | Declaration |
| --- | --- |
| From | ``` var lockOnSleep: Boolean ``` |
| To | ``` var lockOnSleep: DarwinBoolean ``` |

Modified [SecKeychainSettings.useLockInterval](https://developer.apple.com/documentation/security/seckeychainsettings/1397124-uselockinterval)

|  | Declaration |
| --- | --- |
| From | ``` var useLockInterval: Boolean ``` |
| To | ``` var useLockInterval: DarwinBoolean ``` |

Modified [SecKeyImportExportParameters [struct]](https://developer.apple.com/documentation/security/seckeyimportexportparameters)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeyImportExportParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>!     var alertTitle: Unmanaged<CFString>!     var alertPrompt: Unmanaged<CFString>!     var accessRef: Unmanaged<SecAccess>!     var keyUsage: CSSM_KEYUSE     var keyAttributes: CSSM_KEYATTR_FLAGS     init()     init(version version: UInt32, flags flags: SecKeyImportExportFlags, passphrase passphrase: Unmanaged<AnyObject>!, alertTitle alertTitle: Unmanaged<CFString>!, alertPrompt alertPrompt: Unmanaged<CFString>!, accessRef accessRef: Unmanaged<SecAccess>!, keyUsage keyUsage: CSSM_KEYUSE, keyAttributes keyAttributes: CSSM_KEYATTR_FLAGS) } ``` |
| To | ``` struct SecKeyImportExportParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>     var alertTitle: Unmanaged<CFString>     var alertPrompt: Unmanaged<CFString>     var accessRef: Unmanaged<SecAccess>?     var keyUsage: CSSM_KEYUSE     var keyAttributes: CSSM_KEYATTR_FLAGS } ``` |

Modified [SecKeyImportExportParameters.accessRef](https://developer.apple.com/documentation/security/seckeyimportexportparameters/1396858-accessref)

|  | Declaration |
| --- | --- |
| From | ``` var accessRef: Unmanaged<SecAccess>! ``` |
| To | ``` var accessRef: Unmanaged<SecAccess>? ``` |

Modified [SecKeyImportExportParameters.alertPrompt](https://developer.apple.com/documentation/security/seckeyimportexportparameters/1393068-alertprompt)

|  | Declaration |
| --- | --- |
| From | ``` var alertPrompt: Unmanaged<CFString>! ``` |
| To | ``` var alertPrompt: Unmanaged<CFString> ``` |

Modified [SecKeyImportExportParameters.alertTitle](https://developer.apple.com/documentation/security/seckeyimportexportparameters/1393955-alerttitle)

|  | Declaration |
| --- | --- |
| From | ``` var alertTitle: Unmanaged<CFString>! ``` |
| To | ``` var alertTitle: Unmanaged<CFString> ``` |

Modified [SecKeyImportExportParameters.passphrase](https://developer.apple.com/documentation/security/seckeyimportexportparameters/1399051-passphrase)

|  | Declaration |
| --- | --- |
| From | ``` var passphrase: Unmanaged<AnyObject>! ``` |
| To | ``` var passphrase: Unmanaged<AnyObject> ``` |

Modified [AuthorizationCopyRightsAsync(_: AuthorizationRef, _: UnsafePointer<AuthorizationRights>, _: UnsafePointer<AuthorizationEnvironment>, _: AuthorizationFlags, _: AuthorizationAsyncCallback)](https://developer.apple.com/documentation/security/1394914-authorizationcopyrightsasync)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyRightsAsync(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ callbackBlock: AuthorizationAsyncCallback!) ``` |
| To | ``` func AuthorizationCopyRightsAsync(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ callbackBlock: AuthorizationAsyncCallback) ``` |

Modified [AuthorizationRightGet(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](https://developer.apple.com/documentation/security/1397961-authorizationrightget)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightGet(_ rightName: UnsafePointer<Int8>, _ rightDefinition: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func AuthorizationRightGet(_ rightName: UnsafePointer<Int8>, _ rightDefinition: UnsafeMutablePointer<CFDictionary?>) -> OSStatus ``` |

Modified [AuthorizationRightSet(_: AuthorizationRef, _: UnsafePointer<Int8>, _: AnyObject, _: CFString?, _: CFBundle?, _: CFString?) -> OSStatus](https://developer.apple.com/documentation/security/1399311-authorizationrightset)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightSet(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<Int8>, _ rightDefinition: AnyObject!, _ descriptionKey: CFString!, _ bundle: CFBundle!, _ localeTableName: CFString!) -> OSStatus ``` |
| To | ``` func AuthorizationRightSet(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<Int8>, _ rightDefinition: AnyObject, _ descriptionKey: CFString?, _ bundle: CFBundle?, _ localeTableName: CFString?) -> OSStatus ``` |

Modified [CMSDecoderCopyAllCerts(_: CMSDecoder, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1396602-cmsdecodercopyallcerts)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder!, _ certsOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [CMSDecoderCopyContent(_: CMSDecoder, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1396553-cmsdecodercopycontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder!, _ contentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder, _ contentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSDecoderCopyDetachedContent(_: CMSDecoder, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1392572-cmsdecodercopydetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopyDetachedContent(_ cmsDecoder: CMSDecoder!, _ detachedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopyDetachedContent(_ cmsDecoder: CMSDecoder, _ detachedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSDecoderCopyEncapsulatedContentType(_: CMSDecoder, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1400582-cmsdecodercopyencapsulatedconten)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopyEncapsulatedContentType(_ cmsDecoder: CMSDecoder!, _ eContentTypeOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopyEncapsulatedContentType(_ cmsDecoder: CMSDecoder, _ eContentTypeOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerCert(_: CMSDecoder, _: Int, _: UnsafeMutablePointer<SecCertificate?>) -> OSStatus](https://developer.apple.com/documentation/security/1398566-cmsdecodercopysignercert)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ signerCertOut: UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signerCertOut: UnsafeMutablePointer<SecCertificate?>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerEmailAddress(_: CMSDecoder, _: Int, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/security/1400778-cmsdecodercopysigneremailaddress)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerEmailAddress(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ signerEmailAddressOut: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerEmailAddress(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signerEmailAddressOut: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerSigningTime(_: CMSDecoder, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1401770-cmsdecodercopysignersigningtime)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerSigningTime(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ signingTime: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerSigningTime(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signingTime: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerStatus(_: CMSDecoder, _: Int, _: AnyObject, _: Bool, _: UnsafeMutablePointer<CMSSignerStatus>, _: UnsafeMutablePointer<SecTrust?>, _: UnsafeMutablePointer<OSStatus>) -> OSStatus](https://developer.apple.com/documentation/security/1396762-cmsdecodercopysignerstatus)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ policyOrArray: AnyObject!, _ evaluateSecTrust: Boolean, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>, _ secTrustOut: UnsafeMutablePointer<Unmanaged<SecTrust>?>, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ policyOrArray: AnyObject, _ evaluateSecTrust: Bool, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>, _ secTrustOut: UnsafeMutablePointer<SecTrust?>, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerTimestamp(_: CMSDecoder, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1399271-cmsdecodercopysignertimestamp)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerTimestampCertificates(_: CMSDecoder, _: Int, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1392952-cmsdecodercopysignertimestampcer)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerTimestampCertificates(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ certificateRefs: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerTimestampCertificates(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ certificateRefs: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [CMSDecoderCopySignerTimestampWithPolicy(_: CMSDecoder, _: AnyObject?, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1395908-cmsdecodercopysignertimestampwit)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerTimestampWithPolicy(_ cmsDecoder: CMSDecoder!, _ timeStampPolicy: AnyObject!, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerTimestampWithPolicy(_ cmsDecoder: CMSDecoder, _ timeStampPolicy: AnyObject?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSDecoderCreate(_: UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](https://developer.apple.com/documentation/security/1392600-cmsdecodercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCreate(_ cmsDecoderOut: UnsafeMutablePointer<Unmanaged<CMSDecoder>?>) -> OSStatus ``` |
| To | ``` func CMSDecoderCreate(_ cmsDecoderOut: UnsafeMutablePointer<CMSDecoder?>) -> OSStatus ``` |

Modified [CMSDecoderFinalizeMessage(_: CMSDecoder) -> OSStatus](https://developer.apple.com/documentation/security/1398714-cmsdecoderfinalizemessage)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderFinalizeMessage(_ cmsDecoder: CMSDecoder!) -> OSStatus ``` |
| To | ``` func CMSDecoderFinalizeMessage(_ cmsDecoder: CMSDecoder) -> OSStatus ``` |

Modified [CMSDecoderGetNumSigners(_: CMSDecoder, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1395297-cmsdecodergetnumsigners)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderGetNumSigners(_ cmsDecoder: CMSDecoder!, _ numSignersOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func CMSDecoderGetNumSigners(_ cmsDecoder: CMSDecoder, _ numSignersOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [CMSDecoderIsContentEncrypted(_: CMSDecoder, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/security/1396082-cmsdecoderiscontentencrypted)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder!, _ isEncryptedOut: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder, _ isEncryptedOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [CMSDecoderSetDetachedContent(_: CMSDecoder, _: CFData) -> OSStatus](https://developer.apple.com/documentation/security/1402067-cmsdecodersetdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderSetDetachedContent(_ cmsDecoder: CMSDecoder!, _ detachedContent: CFData!) -> OSStatus ``` |
| To | ``` func CMSDecoderSetDetachedContent(_ cmsDecoder: CMSDecoder, _ detachedContent: CFData) -> OSStatus ``` |

Modified [CMSDecoderSetSearchKeychain(_: CMSDecoder, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1392933-cmsdecodersetsearchkeychain)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder!, _ keychainOrArray: AnyObject!) -> OSStatus ``` |
| To | ``` func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder, _ keychainOrArray: AnyObject) -> OSStatus ``` |

Modified [CMSDecoderUpdateMessage(_: CMSDecoder, _: UnsafePointer<Void>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1393876-cmsdecoderupdatemessage)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder!, _ msgBytes: UnsafePointer<Void>, _ msgBytesLen: Int) -> OSStatus ``` |
| To | ``` func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder, _ msgBytes: UnsafePointer<Void>, _ msgBytesLen: Int) -> OSStatus ``` |

Modified [CMSEncode(_: AnyObject?, _: AnyObject?, _: UnsafePointer<CSSM_OID>, _: Bool, _: CMSSignedAttributes, _: UnsafePointer<Void>, _: Int, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1387147-cmsencode)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncode(_ signers: AnyObject!, _ recipients: AnyObject!, _ eContentType: UnsafePointer<CSSM_OID>, _ detachedContent: Boolean, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSEncode(_ signers: AnyObject?, _ recipients: AnyObject?, _ eContentType: UnsafePointer<CSSM_OID>, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSEncodeContent(_: AnyObject?, _: AnyObject?, _: AnyObject?, _: Bool, _: CMSSignedAttributes, _: UnsafePointer<Void>, _: Int, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1387113-cmsencodecontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncodeContent(_ signers: AnyObject!, _ recipients: AnyObject!, _ eContentTypeOID: AnyObject!, _ detachedContent: Boolean, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSEncodeContent(_ signers: AnyObject?, _ recipients: AnyObject?, _ eContentTypeOID: AnyObject?, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSEncoderAddRecipients(_: CMSEncoder, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1387129-cmsencoderaddrecipients)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder!, _ recipientOrArray: AnyObject!) -> OSStatus ``` |
| To | ``` func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder, _ recipientOrArray: AnyObject) -> OSStatus ``` |

Modified [CMSEncoderAddSignedAttributes(_: CMSEncoder, _: CMSSignedAttributes) -> OSStatus](https://developer.apple.com/documentation/security/1387117-cmsencoderaddsignedattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddSignedAttributes(_ cmsEncoder: CMSEncoder!, _ signedAttributes: CMSSignedAttributes) -> OSStatus ``` |
| To | ``` func CMSEncoderAddSignedAttributes(_ cmsEncoder: CMSEncoder, _ signedAttributes: CMSSignedAttributes) -> OSStatus ``` |

Modified [CMSEncoderAddSigners(_: CMSEncoder, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1387177-cmsencoderaddsigners)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder!, _ signerOrArray: AnyObject!) -> OSStatus ``` |
| To | ``` func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder, _ signerOrArray: AnyObject) -> OSStatus ``` |

Modified [CMSEncoderAddSupportingCerts(_: CMSEncoder, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1387168-cmsencoderaddsupportingcerts)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddSupportingCerts(_ cmsEncoder: CMSEncoder!, _ certOrArray: AnyObject!) -> OSStatus ``` |
| To | ``` func CMSEncoderAddSupportingCerts(_ cmsEncoder: CMSEncoder, _ certOrArray: AnyObject) -> OSStatus ``` |

Modified [CMSEncoderCopyEncapsulatedContentType(_: CMSEncoder, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1387151-cmsencodercopyencapsulatedconten)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopyEncapsulatedContentType(_ cmsEncoder: CMSEncoder!, _ eContentTypeOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopyEncapsulatedContentType(_ cmsEncoder: CMSEncoder, _ eContentTypeOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSEncoderCopyEncodedContent(_: CMSEncoder, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1387145-cmsencodercopyencodedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopyEncodedContent(_ cmsEncoder: CMSEncoder!, _ encodedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopyEncodedContent(_ cmsEncoder: CMSEncoder, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSEncoderCopyRecipients(_: CMSEncoder, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1387125-cmsencodercopyrecipients)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopyRecipients(_ cmsEncoder: CMSEncoder!, _ recipientsOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopyRecipients(_ cmsEncoder: CMSEncoder, _ recipientsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [CMSEncoderCopySigners(_: CMSEncoder, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1387139-cmsencodercopysigners)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopySigners(_ cmsEncoder: CMSEncoder!, _ signersOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopySigners(_ cmsEncoder: CMSEncoder, _ signersOut: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [CMSEncoderCopySignerTimestamp(_: CMSEncoder, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1387179-cmsencodercopysignertimestamp)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopySignerTimestamp(_ cmsEncoder: CMSEncoder!, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopySignerTimestamp(_ cmsEncoder: CMSEncoder, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSEncoderCopySignerTimestampWithPolicy(_: CMSEncoder, _: AnyObject?, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1387162-cmsencodercopysignertimestampwit)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopySignerTimestampWithPolicy(_ cmsEncoder: CMSEncoder!, _ timeStampPolicy: AnyObject!, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopySignerTimestampWithPolicy(_ cmsEncoder: CMSEncoder, _ timeStampPolicy: AnyObject?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSEncoderCopySupportingCerts(_: CMSEncoder, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1387159-cmsencodercopysupportingcerts)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopySupportingCerts(_ cmsEncoder: CMSEncoder!, _ certsOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopySupportingCerts(_ cmsEncoder: CMSEncoder, _ certsOut: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [CMSEncoderCreate(_: UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](https://developer.apple.com/documentation/security/1387170-cmsencodercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCreate(_ cmsEncoderOut: UnsafeMutablePointer<Unmanaged<CMSEncoder>?>) -> OSStatus ``` |
| To | ``` func CMSEncoderCreate(_ cmsEncoderOut: UnsafeMutablePointer<CMSEncoder?>) -> OSStatus ``` |

Modified [CMSEncoderGetCertificateChainMode(_: CMSEncoder, _: UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus](https://developer.apple.com/documentation/security/1387173-cmsencodergetcertificatechainmod)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderGetCertificateChainMode(_ cmsEncoder: CMSEncoder!, _ chainModeOut: UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus ``` |
| To | ``` func CMSEncoderGetCertificateChainMode(_ cmsEncoder: CMSEncoder, _ chainModeOut: UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus ``` |

Modified [CMSEncoderGetHasDetachedContent(_: CMSEncoder, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/security/1387123-cmsencodergethasdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder!, _ detachedContentOut: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContentOut: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [CMSEncoderSetCertificateChainMode(_: CMSEncoder, _: CMSCertificateChainMode) -> OSStatus](https://developer.apple.com/documentation/security/1387160-cmsencodersetcertificatechainmod)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderSetCertificateChainMode(_ cmsEncoder: CMSEncoder!, _ chainMode: CMSCertificateChainMode) -> OSStatus ``` |
| To | ``` func CMSEncoderSetCertificateChainMode(_ cmsEncoder: CMSEncoder, _ chainMode: CMSCertificateChainMode) -> OSStatus ``` |

Modified [CMSEncoderSetEncapsulatedContentType(_: CMSEncoder, _: UnsafePointer<CSSM_OID>) -> OSStatus](https://developer.apple.com/documentation/security/1387172-cmsencodersetencapsulatedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderSetEncapsulatedContentType(_ cmsEncoder: CMSEncoder!, _ eContentType: UnsafePointer<CSSM_OID>) -> OSStatus ``` |
| To | ``` func CMSEncoderSetEncapsulatedContentType(_ cmsEncoder: CMSEncoder, _ eContentType: UnsafePointer<CSSM_OID>) -> OSStatus ``` |

Modified [CMSEncoderSetEncapsulatedContentTypeOID(_: CMSEncoder, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1387115-cmsencodersetencapsulatedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderSetEncapsulatedContentTypeOID(_ cmsEncoder: CMSEncoder!, _ eContentTypeOID: AnyObject!) -> OSStatus ``` |
| To | ``` func CMSEncoderSetEncapsulatedContentTypeOID(_ cmsEncoder: CMSEncoder, _ eContentTypeOID: AnyObject) -> OSStatus ``` |

Modified [CMSEncoderSetHasDetachedContent(_: CMSEncoder, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1387164-cmsencodersethasdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderSetHasDetachedContent(_ cmsEncoder: CMSEncoder!, _ detachedContent: Boolean) -> OSStatus ``` |
| To | ``` func CMSEncoderSetHasDetachedContent(_ cmsEncoder: CMSEncoder, _ detachedContent: Bool) -> OSStatus ``` |

Modified [CMSEncoderUpdateContent(_: CMSEncoder, _: UnsafePointer<Void>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1387141-cmsencoderupdatecontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder!, _ content: UnsafePointer<Void>, _ contentLen: Int) -> OSStatus ``` |
| To | ``` func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder, _ content: UnsafePointer<Void>, _ contentLen: Int) -> OSStatus ``` |

Modified CSSM_ACL_SUBJECT_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_ACL_SUBJECT_CALLBACK = CFunctionPointer<((UnsafePointer<CSSM_LIST>, CSSM_LIST_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_ACL_SUBJECT_CALLBACK = (UnsafePointer<CSSM_LIST>, CSSM_LIST_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN ``` |

Modified CSSM_API_ModuleEventHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_API_ModuleEventHandler = CFunctionPointer<((UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_API_ModuleEventHandler = (UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN ``` |

Modified CSSM_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CALLBACK = CFunctionPointer<((CSSM_DATA_PTR, UnsafeMutablePointer<Void>) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_CALLBACK = (CSSM_DATA_PTR, UnsafeMutablePointer<Void>) -> CSSM_RETURN ``` |

Modified CSSM_CALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CALLOC = CFunctionPointer<((uint32, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` typealias CSSM_CALLOC = (uint32, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified CSSM_CHALLENGE_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CHALLENGE_CALLBACK = CFunctionPointer<((UnsafePointer<CSSM_LIST>, CSSM_SAMPLEGROUP_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_CHALLENGE_CALLBACK = (UnsafePointer<CSSM_LIST>, CSSM_SAMPLEGROUP_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN ``` |

Modified CSSM_FREE

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_FREE = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CSSM_FREE = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |

Modified CSSM_MALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_MALLOC = CFunctionPointer<((CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` typealias CSSM_MALLOC = (CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified CSSM_PROC_ADDR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_PROC_ADDR = CFunctionPointer<(() -> Void)> ``` |
| To | ``` typealias CSSM_PROC_ADDR = () -> Void ``` |

Modified CSSM_PROC_ADDR_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_PROC_ADDR_PTR = UnsafeMutablePointer<CSSM_PROC_ADDR> ``` |
| To | ``` typealias CSSM_PROC_ADDR_PTR = UnsafeMutablePointer<CSSM_PROC_ADDR?> ``` |

Modified CSSM_REALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_REALLOC = CFunctionPointer<((UnsafeMutablePointer<Void>, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` typealias CSSM_REALLOC = (UnsafeMutablePointer<Void>, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |

Modified CSSM_SPI_ModuleEventHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_SPI_ModuleEventHandler = CFunctionPointer<((UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_SPI_ModuleEventHandler = (UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN ``` |

Modified CSSM_TP_VERIFICATION_RESULTS_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_TP_VERIFICATION_RESULTS_CALLBACK = CFunctionPointer<((CSSM_MODULE_HANDLE, UnsafeMutablePointer<Void>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_TP_VERIFICATION_RESULTS_CALLBACK = (CSSM_MODULE_HANDLE, UnsafeMutablePointer<Void>, CSSM_DATA_PTR) -> CSSM_RETURN ``` |

Modified [errAuthorizationBadAddress](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationbadaddress)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationBadAddress: Int { get } ``` |
| To | ``` var errAuthorizationBadAddress: OSStatus { get } ``` |

Modified [errAuthorizationCanceled](https://developer.apple.com/documentation/security/errauthorizationcanceled)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationCanceled: Int { get } ``` |
| To | ``` var errAuthorizationCanceled: OSStatus { get } ``` |

Modified [errAuthorizationDenied](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationdenied)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationDenied: Int { get } ``` |
| To | ``` var errAuthorizationDenied: OSStatus { get } ``` |

Modified [errAuthorizationExternalizeNotAllowed](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationexternalizenotallowed)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationExternalizeNotAllowed: Int { get } ``` |
| To | ``` var errAuthorizationExternalizeNotAllowed: OSStatus { get } ``` |

Modified [errAuthorizationInteractionNotAllowed](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationinteractionnotallowed)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInteractionNotAllowed: Int { get } ``` |
| To | ``` var errAuthorizationInteractionNotAllowed: OSStatus { get } ``` |

Modified [errAuthorizationInternal](https://developer.apple.com/documentation/security/errauthorizationinternal)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInternal: Int { get } ``` |
| To | ``` var errAuthorizationInternal: OSStatus { get } ``` |

Modified [errAuthorizationInternalizeNotAllowed](https://developer.apple.com/documentation/security/errauthorizationinternalizenotallowed)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInternalizeNotAllowed: Int { get } ``` |
| To | ``` var errAuthorizationInternalizeNotAllowed: OSStatus { get } ``` |

Modified [errAuthorizationInvalidFlags](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationinvalidflags)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInvalidFlags: Int { get } ``` |
| To | ``` var errAuthorizationInvalidFlags: OSStatus { get } ``` |

Modified [errAuthorizationInvalidPointer](https://developer.apple.com/documentation/security/errauthorizationinvalidpointer)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInvalidPointer: Int { get } ``` |
| To | ``` var errAuthorizationInvalidPointer: OSStatus { get } ``` |

Modified [errAuthorizationInvalidRef](https://developer.apple.com/documentation/security/errauthorizationinvalidref)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInvalidRef: Int { get } ``` |
| To | ``` var errAuthorizationInvalidRef: OSStatus { get } ``` |

Modified [errAuthorizationInvalidSet](https://developer.apple.com/documentation/security/errauthorizationinvalidset)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInvalidSet: Int { get } ``` |
| To | ``` var errAuthorizationInvalidSet: OSStatus { get } ``` |

Modified [errAuthorizationInvalidTag](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationinvalidtag)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationInvalidTag: Int { get } ``` |
| To | ``` var errAuthorizationInvalidTag: OSStatus { get } ``` |

Modified [errAuthorizationSuccess](https://developer.apple.com/documentation/security/errauthorizationsuccess)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationSuccess: Int { get } ``` |
| To | ``` var errAuthorizationSuccess: OSStatus { get } ``` |

Modified [errAuthorizationToolEnvironmentError](https://developer.apple.com/documentation/security/errauthorizationtoolenvironmenterror)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationToolEnvironmentError: Int { get } ``` |
| To | ``` var errAuthorizationToolEnvironmentError: OSStatus { get } ``` |

Modified [errAuthorizationToolExecuteFailure](https://developer.apple.com/documentation/security/1540004-authorization_services_result_co/errauthorizationtoolexecutefailure)

|  | Declaration |
| --- | --- |
| From | ``` var errAuthorizationToolExecuteFailure: Int { get } ``` |
| To | ``` var errAuthorizationToolExecuteFailure: OSStatus { get } ``` |

Modified [errSecACLAddFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecacladdfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecACLAddFailed: Int { get } ``` |
| To | ``` var errSecACLAddFailed: OSStatus { get } ``` |

Modified [errSecACLChangeFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecaclchangefailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecACLChangeFailed: Int { get } ``` |
| To | ``` var errSecACLChangeFailed: OSStatus { get } ``` |

Modified [errSecACLDeleteFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecacldeletefailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecACLDeleteFailed: Int { get } ``` |
| To | ``` var errSecACLDeleteFailed: OSStatus { get } ``` |

Modified [errSecACLNotSimple](https://developer.apple.com/documentation/security/errsecaclnotsimple)

|  | Declaration |
| --- | --- |
| From | ``` var errSecACLNotSimple: Int { get } ``` |
| To | ``` var errSecACLNotSimple: OSStatus { get } ``` |

Modified [errSecACLReplaceFailed](https://developer.apple.com/documentation/security/errsecaclreplacefailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecACLReplaceFailed: Int { get } ``` |
| To | ``` var errSecACLReplaceFailed: OSStatus { get } ``` |

Modified [errSecAddinLoadFailed](https://developer.apple.com/documentation/security/errsecaddinloadfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAddinLoadFailed: Int { get } ``` |
| To | ``` var errSecAddinLoadFailed: OSStatus { get } ``` |

Modified [errSecAddinUnloadFailed](https://developer.apple.com/documentation/security/errsecaddinunloadfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAddinUnloadFailed: Int { get } ``` |
| To | ``` var errSecAddinUnloadFailed: OSStatus { get } ``` |

Modified [errSecAlgorithmMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecalgorithmmismatch)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAlgorithmMismatch: Int { get } ``` |
| To | ``` var errSecAlgorithmMismatch: OSStatus { get } ``` |

Modified [errSecAllocate](https://developer.apple.com/documentation/security/errsecallocate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAllocate: Int { get } ``` |
| To | ``` var errSecAllocate: OSStatus { get } ``` |

Modified [errSecAlreadyLoggedIn](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecalreadyloggedin)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAlreadyLoggedIn: Int { get } ``` |
| To | ``` var errSecAlreadyLoggedIn: OSStatus { get } ``` |

Modified [errSecAppleAddAppACLSubject](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecappleaddappaclsubject)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAppleAddAppACLSubject: Int { get } ``` |
| To | ``` var errSecAppleAddAppACLSubject: OSStatus { get } ``` |

Modified [errSecAppleInvalidKeyEndDate](https://developer.apple.com/documentation/security/errsecappleinvalidkeyenddate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAppleInvalidKeyEndDate: Int { get } ``` |
| To | ``` var errSecAppleInvalidKeyEndDate: OSStatus { get } ``` |

Modified [errSecAppleInvalidKeyStartDate](https://developer.apple.com/documentation/security/errsecappleinvalidkeystartdate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAppleInvalidKeyStartDate: Int { get } ``` |
| To | ``` var errSecAppleInvalidKeyStartDate: OSStatus { get } ``` |

Modified [errSecApplePublicKeyIncomplete](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecapplepublickeyincomplete)

|  | Declaration |
| --- | --- |
| From | ``` var errSecApplePublicKeyIncomplete: Int { get } ``` |
| To | ``` var errSecApplePublicKeyIncomplete: OSStatus { get } ``` |

Modified [errSecAppleSignatureMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecapplesignaturemismatch)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAppleSignatureMismatch: Int { get } ``` |
| To | ``` var errSecAppleSignatureMismatch: OSStatus { get } ``` |

Modified [errSecAppleSSLv2Rollback](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecapplesslv2rollback)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAppleSSLv2Rollback: Int { get } ``` |
| To | ``` var errSecAppleSSLv2Rollback: OSStatus { get } ``` |

Modified [errSecAttachHandleBusy](https://developer.apple.com/documentation/security/errsecattachhandlebusy)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAttachHandleBusy: Int { get } ``` |
| To | ``` var errSecAttachHandleBusy: OSStatus { get } ``` |

Modified [errSecAttributeNotInContext](https://developer.apple.com/documentation/security/errsecattributenotincontext)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAttributeNotInContext: Int { get } ``` |
| To | ``` var errSecAttributeNotInContext: OSStatus { get } ``` |

Modified [errSecAuthFailed](https://developer.apple.com/documentation/security/errsecauthfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAuthFailed: Int { get } ``` |
| To | ``` var errSecAuthFailed: OSStatus { get } ``` |

Modified [errSecBadReq](https://developer.apple.com/documentation/security/errsecbadreq)

|  | Declaration |
| --- | --- |
| From | ``` var errSecBadReq: Int { get } ``` |
| To | ``` var errSecBadReq: OSStatus { get } ``` |

Modified [errSecBlockSizeMismatch](https://developer.apple.com/documentation/security/errsecblocksizemismatch)

|  | Declaration |
| --- | --- |
| From | ``` var errSecBlockSizeMismatch: Int { get } ``` |
| To | ``` var errSecBlockSizeMismatch: OSStatus { get } ``` |

Modified [errSecBufferTooSmall](https://developer.apple.com/documentation/security/errsecbuffertoosmall)

|  | Declaration |
| --- | --- |
| From | ``` var errSecBufferTooSmall: Int { get } ``` |
| To | ``` var errSecBufferTooSmall: OSStatus { get } ``` |

Modified [errSecCallbackFailed](https://developer.apple.com/documentation/security/errseccallbackfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCallbackFailed: Int { get } ``` |
| To | ``` var errSecCallbackFailed: OSStatus { get } ``` |

Modified [errSecCertificateCannotOperate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccertificatecannotoperate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCertificateCannotOperate: Int { get } ``` |
| To | ``` var errSecCertificateCannotOperate: OSStatus { get } ``` |

Modified [errSecCertificateExpired](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccertificateexpired)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCertificateExpired: Int { get } ``` |
| To | ``` var errSecCertificateExpired: OSStatus { get } ``` |

Modified [errSecCertificateNotValidYet](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccertificatenotvalidyet)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCertificateNotValidYet: Int { get } ``` |
| To | ``` var errSecCertificateNotValidYet: OSStatus { get } ``` |

Modified [errSecCertificateRevoked](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccertificaterevoked)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCertificateRevoked: Int { get } ``` |
| To | ``` var errSecCertificateRevoked: OSStatus { get } ``` |

Modified [errSecCertificateSuspended](https://developer.apple.com/documentation/security/errseccertificatesuspended)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCertificateSuspended: Int { get } ``` |
| To | ``` var errSecCertificateSuspended: OSStatus { get } ``` |

Modified [errSecCodeSigningBadCertChainLength](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningbadcertchainlength)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCodeSigningBadCertChainLength: Int { get } ``` |
| To | ``` var errSecCodeSigningBadCertChainLength: OSStatus { get } ``` |

Modified [errSecCodeSigningBadPathLengthConstraint](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningbadpathlengthconstraint)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCodeSigningBadPathLengthConstraint: Int { get } ``` |
| To | ``` var errSecCodeSigningBadPathLengthConstraint: OSStatus { get } ``` |

Modified [errSecCodeSigningDevelopment](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningdevelopment)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCodeSigningDevelopment: Int { get } ``` |
| To | ``` var errSecCodeSigningDevelopment: OSStatus { get } ``` |

Modified [errSecCodeSigningNoBasicConstraints](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningnobasicconstraints)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCodeSigningNoBasicConstraints: Int { get } ``` |
| To | ``` var errSecCodeSigningNoBasicConstraints: OSStatus { get } ``` |

Modified [errSecCodeSigningNoExtendedKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningnoextendedkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCodeSigningNoExtendedKeyUsage: Int { get } ``` |
| To | ``` var errSecCodeSigningNoExtendedKeyUsage: OSStatus { get } ``` |

Modified [errSecConversionError](https://developer.apple.com/documentation/security/errsecconversionerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecConversionError: Int { get } ``` |
| To | ``` var errSecConversionError: OSStatus { get } ``` |

Modified [errSecCoreFoundationUnknown](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccorefoundationunknown)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCoreFoundationUnknown: Int { get } ``` |
| To | ``` var errSecCoreFoundationUnknown: OSStatus { get } ``` |

Modified [errSecCreateChainFailed](https://developer.apple.com/documentation/security/errseccreatechainfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCreateChainFailed: Int { get } ``` |
| To | ``` var errSecCreateChainFailed: OSStatus { get } ``` |

Modified [errSecCRLAlreadySigned](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlalreadysigned)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLAlreadySigned: Int { get } ``` |
| To | ``` var errSecCRLAlreadySigned: OSStatus { get } ``` |

Modified [errSecCRLBadURI](https://developer.apple.com/documentation/security/errseccrlbaduri)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLBadURI: Int { get } ``` |
| To | ``` var errSecCRLBadURI: OSStatus { get } ``` |

Modified [errSecCRLExpired](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlexpired)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLExpired: Int { get } ``` |
| To | ``` var errSecCRLExpired: OSStatus { get } ``` |

Modified [errSecCRLNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLNotFound: Int { get } ``` |
| To | ``` var errSecCRLNotFound: OSStatus { get } ``` |

Modified [errSecCRLNotTrusted](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlnottrusted)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLNotTrusted: Int { get } ``` |
| To | ``` var errSecCRLNotTrusted: OSStatus { get } ``` |

Modified [errSecCRLNotValidYet](https://developer.apple.com/documentation/security/errseccrlnotvalidyet)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLNotValidYet: Int { get } ``` |
| To | ``` var errSecCRLNotValidYet: OSStatus { get } ``` |

Modified [errSecCRLPolicyFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlpolicyfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLPolicyFailed: Int { get } ``` |
| To | ``` var errSecCRLPolicyFailed: OSStatus { get } ``` |

Modified [errSecCRLServerDown](https://developer.apple.com/documentation/security/errseccrlserverdown)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCRLServerDown: Int { get } ``` |
| To | ``` var errSecCRLServerDown: OSStatus { get } ``` |

Modified [errSecCSAmbiguousBundleFormat](https://developer.apple.com/documentation/security/errseccsambiguousbundleformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSAmbiguousBundleFormat: Int { get } ``` |
| To | ``` var errSecCSAmbiguousBundleFormat: OSStatus { get } ``` |

Modified [errSecCSBadBundleFormat](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadbundleformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadBundleFormat: Int { get } ``` |
| To | ``` var errSecCSBadBundleFormat: OSStatus { get } ``` |

Modified [errSecCSBadCallbackValue](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadcallbackvalue)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadCallbackValue: Int { get } ``` |
| To | ``` var errSecCSBadCallbackValue: OSStatus { get } ``` |

Modified [errSecCSBadDictionaryFormat](https://developer.apple.com/documentation/security/errseccsbaddictionaryformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadDictionaryFormat: Int { get } ``` |
| To | ``` var errSecCSBadDictionaryFormat: OSStatus { get } ``` |

Modified [errSecCSBadFrameworkVersion](https://developer.apple.com/documentation/security/errseccsbadframeworkversion)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadFrameworkVersion: Int { get } ``` |
| To | ``` var errSecCSBadFrameworkVersion: OSStatus { get } ``` |

Modified [errSecCSBadLVArch](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadlvarch)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadLVArch: Int { get } ``` |
| To | ``` var errSecCSBadLVArch: OSStatus { get } ``` |

Modified [errSecCSBadMainExecutable](https://developer.apple.com/documentation/security/errseccsbadmainexecutable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadMainExecutable: Int { get } ``` |
| To | ``` var errSecCSBadMainExecutable: OSStatus { get } ``` |

Modified [errSecCSBadNestedCode](https://developer.apple.com/documentation/security/errseccsbadnestedcode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadNestedCode: Int { get } ``` |
| To | ``` var errSecCSBadNestedCode: OSStatus { get } ``` |

Modified [errSecCSBadObjectFormat](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadobjectformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadObjectFormat: Int { get } ``` |
| To | ``` var errSecCSBadObjectFormat: OSStatus { get } ``` |

Modified [errSecCSBadResource](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadresource)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSBadResource: Int { get } ``` |
| To | ``` var errSecCSBadResource: OSStatus { get } ``` |

Modified [errSecCSCancelled](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccscancelled)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSCancelled: Int { get } ``` |
| To | ``` var errSecCSCancelled: OSStatus { get } ``` |

Modified [errSecCSCMSTooLarge](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccscmstoolarge)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSCMSTooLarge: Int { get } ``` |
| To | ``` var errSecCSCMSTooLarge: OSStatus { get } ``` |

Modified [errSecCSDBAccess](https://developer.apple.com/documentation/security/errseccsdbaccess)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSDBAccess: Int { get } ``` |
| To | ``` var errSecCSDBAccess: OSStatus { get } ``` |

Modified [errSecCSDbCorrupt](https://developer.apple.com/documentation/security/errseccsdbcorrupt)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSDbCorrupt: Int { get } ``` |
| To | ``` var errSecCSDbCorrupt: OSStatus { get } ``` |

Modified [errSecCSDBDenied](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsdbdenied)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSDBDenied: Int { get } ``` |
| To | ``` var errSecCSDBDenied: OSStatus { get } ``` |

Modified [errSecCSDSStoreSymlink](https://developer.apple.com/documentation/security/errseccsdsstoresymlink)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSDSStoreSymlink: Int { get } ``` |
| To | ``` var errSecCSDSStoreSymlink: OSStatus { get } ``` |

Modified [errSecCSFileHardQuarantined](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsfilehardquarantined)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSFileHardQuarantined: Int { get } ``` |
| To | ``` var errSecCSFileHardQuarantined: OSStatus { get } ``` |

Modified [errSecCSGuestInvalid](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsguestinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSGuestInvalid: Int { get } ``` |
| To | ``` var errSecCSGuestInvalid: OSStatus { get } ``` |

Modified [errSecCSHelperFailed](https://developer.apple.com/documentation/security/errseccshelperfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHelperFailed: Int { get } ``` |
| To | ``` var errSecCSHelperFailed: OSStatus { get } ``` |

Modified [errSecCSHostProtocolContradiction](https://developer.apple.com/documentation/security/errseccshostprotocolcontradiction)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolContradiction: Int { get } ``` |
| To | ``` var errSecCSHostProtocolContradiction: OSStatus { get } ``` |

Modified [errSecCSHostProtocolDedicationError](https://developer.apple.com/documentation/security/errseccshostprotocoldedicationerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolDedicationError: Int { get } ``` |
| To | ``` var errSecCSHostProtocolDedicationError: OSStatus { get } ``` |

Modified [errSecCSHostProtocolInvalidAttribute](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccshostprotocolinvalidattribute)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolInvalidAttribute: Int { get } ``` |
| To | ``` var errSecCSHostProtocolInvalidAttribute: OSStatus { get } ``` |

Modified [errSecCSHostProtocolInvalidHash](https://developer.apple.com/documentation/security/errseccshostprotocolinvalidhash)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolInvalidHash: Int { get } ``` |
| To | ``` var errSecCSHostProtocolInvalidHash: OSStatus { get } ``` |

Modified [errSecCSHostProtocolNotProxy](https://developer.apple.com/documentation/security/errseccshostprotocolnotproxy)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolNotProxy: Int { get } ``` |
| To | ``` var errSecCSHostProtocolNotProxy: OSStatus { get } ``` |

Modified [errSecCSHostProtocolRelativePath](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccshostprotocolrelativepath)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolRelativePath: Int { get } ``` |
| To | ``` var errSecCSHostProtocolRelativePath: OSStatus { get } ``` |

Modified [errSecCSHostProtocolStateError](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccshostprotocolstateerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolStateError: Int { get } ``` |
| To | ``` var errSecCSHostProtocolStateError: OSStatus { get } ``` |

Modified [errSecCSHostProtocolUnrelated](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccshostprotocolunrelated)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostProtocolUnrelated: Int { get } ``` |
| To | ``` var errSecCSHostProtocolUnrelated: OSStatus { get } ``` |

Modified [errSecCSHostReject](https://developer.apple.com/documentation/security/errseccshostreject)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSHostReject: Int { get } ``` |
| To | ``` var errSecCSHostReject: OSStatus { get } ``` |

Modified [errSecCSInfoPlistFailed](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinfoplistfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSInfoPlistFailed: Int { get } ``` |
| To | ``` var errSecCSInfoPlistFailed: OSStatus { get } ``` |

Modified [errSecCSInternalError](https://developer.apple.com/documentation/security/errseccsinternalerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSInternalError: Int { get } ``` |
| To | ``` var errSecCSInternalError: OSStatus { get } ``` |

Modified [errSecCSInvalidAttributeValues](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidattributevalues)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSInvalidAttributeValues: Int { get } ``` |
| To | ``` var errSecCSInvalidAttributeValues: OSStatus { get } ``` |

Modified [errSecCSInvalidFlags](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidflags)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSInvalidFlags: Int { get } ``` |
| To | ``` var errSecCSInvalidFlags: OSStatus { get } ``` |

Modified [errSecCSInvalidObjectRef](https://developer.apple.com/documentation/security/errseccsinvalidobjectref)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSInvalidObjectRef: Int { get } ``` |
| To | ``` var errSecCSInvalidObjectRef: OSStatus { get } ``` |

Modified [errSecCSMultipleGuests](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsmultipleguests)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSMultipleGuests: Int { get } ``` |
| To | ``` var errSecCSMultipleGuests: OSStatus { get } ``` |

Modified [errSecCSNoMainExecutable](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsnomainexecutable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSNoMainExecutable: Int { get } ``` |
| To | ``` var errSecCSNoMainExecutable: OSStatus { get } ``` |

Modified [errSecCSNoMatches](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsnomatches)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSNoMatches: Int { get } ``` |
| To | ``` var errSecCSNoMatches: OSStatus { get } ``` |

Modified [errSecCSNoSuchCode](https://developer.apple.com/documentation/security/errseccsnosuchcode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSNoSuchCode: Int { get } ``` |
| To | ``` var errSecCSNoSuchCode: OSStatus { get } ``` |

Modified [errSecCSNotAHost](https://developer.apple.com/documentation/security/errseccsnotahost)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSNotAHost: Int { get } ``` |
| To | ``` var errSecCSNotAHost: OSStatus { get } ``` |

Modified [errSecCSNotSupported](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSNotSupported: Int { get } ``` |
| To | ``` var errSecCSNotSupported: OSStatus { get } ``` |

Modified [errSecCSObjectRequired](https://developer.apple.com/documentation/security/errseccsobjectrequired)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSObjectRequired: Int { get } ``` |
| To | ``` var errSecCSObjectRequired: OSStatus { get } ``` |

Modified [errSecCSOutdated](https://developer.apple.com/documentation/security/errseccsoutdated)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSOutdated: Int { get } ``` |
| To | ``` var errSecCSOutdated: OSStatus { get } ``` |

Modified [errSecCSRegularFile](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsregularfile)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSRegularFile: Int { get } ``` |
| To | ``` var errSecCSRegularFile: OSStatus { get } ``` |

Modified [errSecCSReqFailed](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsreqfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSReqFailed: Int { get } ``` |
| To | ``` var errSecCSReqFailed: OSStatus { get } ``` |

Modified [errSecCSReqInvalid](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsreqinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSReqInvalid: Int { get } ``` |
| To | ``` var errSecCSReqInvalid: OSStatus { get } ``` |

Modified [errSecCSReqUnsupported](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsrequnsupported)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSReqUnsupported: Int { get } ``` |
| To | ``` var errSecCSReqUnsupported: OSStatus { get } ``` |

Modified [errSecCSResourceDirectoryFailed](https://developer.apple.com/documentation/security/errseccsresourcedirectoryfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSResourceDirectoryFailed: Int { get } ``` |
| To | ``` var errSecCSResourceDirectoryFailed: OSStatus { get } ``` |

Modified [errSecCSResourceNotSupported](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsresourcenotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSResourceNotSupported: Int { get } ``` |
| To | ``` var errSecCSResourceNotSupported: OSStatus { get } ``` |

Modified [errSecCSResourceRulesInvalid](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsresourcerulesinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSResourceRulesInvalid: Int { get } ``` |
| To | ``` var errSecCSResourceRulesInvalid: OSStatus { get } ``` |

Modified [errSecCSResourcesInvalid](https://developer.apple.com/documentation/security/errseccsresourcesinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSResourcesInvalid: Int { get } ``` |
| To | ``` var errSecCSResourcesInvalid: OSStatus { get } ``` |

Modified [errSecCSResourcesNotFound](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsresourcesnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSResourcesNotFound: Int { get } ``` |
| To | ``` var errSecCSResourcesNotFound: OSStatus { get } ``` |

Modified [errSecCSResourcesNotSealed](https://developer.apple.com/documentation/security/errseccsresourcesnotsealed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSResourcesNotSealed: Int { get } ``` |
| To | ``` var errSecCSResourcesNotSealed: OSStatus { get } ``` |

Modified [errSecCSSigDBAccess](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccssigdbaccess)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSSigDBAccess: Int { get } ``` |
| To | ``` var errSecCSSigDBAccess: OSStatus { get } ``` |

Modified [errSecCSSigDBDenied](https://developer.apple.com/documentation/security/errseccssigdbdenied)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSSigDBDenied: Int { get } ``` |
| To | ``` var errSecCSSigDBDenied: OSStatus { get } ``` |

Modified [errSecCSSignatureFailed](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccssignaturefailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSSignatureFailed: Int { get } ``` |
| To | ``` var errSecCSSignatureFailed: OSStatus { get } ``` |

Modified [errSecCSSignatureInvalid](https://developer.apple.com/documentation/security/errseccssignatureinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSSignatureInvalid: Int { get } ``` |
| To | ``` var errSecCSSignatureInvalid: OSStatus { get } ``` |

Modified [errSecCSSignatureNotVerifiable](https://developer.apple.com/documentation/security/errseccssignaturenotverifiable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSSignatureNotVerifiable: Int { get } ``` |
| To | ``` var errSecCSSignatureNotVerifiable: OSStatus { get } ``` |

Modified [errSecCSSignatureUnsupported](https://developer.apple.com/documentation/security/errseccssignatureunsupported)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSSignatureUnsupported: Int { get } ``` |
| To | ``` var errSecCSSignatureUnsupported: OSStatus { get } ``` |

Modified [errSecCSStaticCodeChanged](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsstaticcodechanged)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSStaticCodeChanged: Int { get } ``` |
| To | ``` var errSecCSStaticCodeChanged: OSStatus { get } ``` |

Modified [errSecCSStaticCodeNotFound](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsstaticcodenotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSStaticCodeNotFound: Int { get } ``` |
| To | ``` var errSecCSStaticCodeNotFound: OSStatus { get } ``` |

Modified [errSecCSUnimplemented](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsunimplemented)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSUnimplemented: Int { get } ``` |
| To | ``` var errSecCSUnimplemented: OSStatus { get } ``` |

Modified [errSecCSUnsealedAppRoot](https://developer.apple.com/documentation/security/errseccsunsealedapproot)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSUnsealedAppRoot: Int { get } ``` |
| To | ``` var errSecCSUnsealedAppRoot: OSStatus { get } ``` |

Modified [errSecCSUnsealedFrameworkRoot](https://developer.apple.com/documentation/security/errseccsunsealedframeworkroot)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSUnsealedFrameworkRoot: Int { get } ``` |
| To | ``` var errSecCSUnsealedFrameworkRoot: OSStatus { get } ``` |

Modified [errSecCSUnsigned](https://developer.apple.com/documentation/security/errseccsunsigned)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSUnsigned: Int { get } ``` |
| To | ``` var errSecCSUnsigned: OSStatus { get } ``` |

Modified [errSecCSUnsignedNestedCode](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsunsignednestedcode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSUnsignedNestedCode: Int { get } ``` |
| To | ``` var errSecCSUnsignedNestedCode: OSStatus { get } ``` |

Modified [errSecCSUnsupportedGuestAttributes](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsunsupportedguestattributes)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSUnsupportedGuestAttributes: Int { get } ``` |
| To | ``` var errSecCSUnsupportedGuestAttributes: OSStatus { get } ``` |

Modified [errSecCSVetoed](https://developer.apple.com/documentation/security/errseccsvetoed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSVetoed: Int { get } ``` |
| To | ``` var errSecCSVetoed: OSStatus { get } ``` |

Modified [errSecCSWeakResourceEnvelope](https://developer.apple.com/documentation/security/errseccsweakresourceenvelope)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSWeakResourceEnvelope: Int { get } ``` |
| To | ``` var errSecCSWeakResourceEnvelope: OSStatus { get } ``` |

Modified [errSecCSWeakResourceRules](https://developer.apple.com/documentation/security/errseccsweakresourcerules)

|  | Declaration |
| --- | --- |
| From | ``` var errSecCSWeakResourceRules: Int { get } ``` |
| To | ``` var errSecCSWeakResourceRules: OSStatus { get } ``` |

Modified [errSecDatabaseLocked](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdatabaselocked)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDatabaseLocked: Int { get } ``` |
| To | ``` var errSecDatabaseLocked: OSStatus { get } ``` |

Modified [errSecDataNotAvailable](https://developer.apple.com/documentation/security/errsecdatanotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDataNotAvailable: Int { get } ``` |
| To | ``` var errSecDataNotAvailable: OSStatus { get } ``` |

Modified [errSecDataNotModifiable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdatanotmodifiable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDataNotModifiable: Int { get } ``` |
| To | ``` var errSecDataNotModifiable: OSStatus { get } ``` |

Modified [errSecDatastoreIsOpen](https://developer.apple.com/documentation/security/errsecdatastoreisopen)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDatastoreIsOpen: Int { get } ``` |
| To | ``` var errSecDatastoreIsOpen: OSStatus { get } ``` |

Modified [errSecDataTooLarge](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdatatoolarge)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDataTooLarge: Int { get } ``` |
| To | ``` var errSecDataTooLarge: OSStatus { get } ``` |

Modified [errSecDecode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdecode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDecode: Int { get } ``` |
| To | ``` var errSecDecode: OSStatus { get } ``` |

Modified [errSecDeviceError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdeviceerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDeviceError: Int { get } ``` |
| To | ``` var errSecDeviceError: OSStatus { get } ``` |

Modified [errSecDeviceFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdevicefailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDeviceFailed: Int { get } ``` |
| To | ``` var errSecDeviceFailed: OSStatus { get } ``` |

Modified [errSecDeviceReset](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdevicereset)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDeviceReset: Int { get } ``` |
| To | ``` var errSecDeviceReset: OSStatus { get } ``` |

Modified [errSecDeviceVerifyFailed](https://developer.apple.com/documentation/security/errsecdeviceverifyfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDeviceVerifyFailed: Int { get } ``` |
| To | ``` var errSecDeviceVerifyFailed: OSStatus { get } ``` |

Modified [errSecDiskFull](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdiskfull)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDiskFull: Int { get } ``` |
| To | ``` var errSecDiskFull: OSStatus { get } ``` |

Modified [errSecDskFull](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdskfull)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDskFull: Int { get } ``` |
| To | ``` var errSecDskFull: OSStatus { get } ``` |

Modified [errSecDuplicateCallback](https://developer.apple.com/documentation/security/errsecduplicatecallback)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDuplicateCallback: Int { get } ``` |
| To | ``` var errSecDuplicateCallback: OSStatus { get } ``` |

Modified [errSecDuplicateItem](https://developer.apple.com/documentation/security/errsecduplicateitem)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDuplicateItem: Int { get } ``` |
| To | ``` var errSecDuplicateItem: OSStatus { get } ``` |

Modified [errSecDuplicateKeychain](https://developer.apple.com/documentation/security/errsecduplicatekeychain)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDuplicateKeychain: Int { get } ``` |
| To | ``` var errSecDuplicateKeychain: OSStatus { get } ``` |

Modified [errSecEMMLoadFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecemmloadfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecEMMLoadFailed: Int { get } ``` |
| To | ``` var errSecEMMLoadFailed: OSStatus { get } ``` |

Modified [errSecEMMUnloadFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecemmunloadfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecEMMUnloadFailed: Int { get } ``` |
| To | ``` var errSecEMMUnloadFailed: OSStatus { get } ``` |

Modified [errSecEndOfData](https://developer.apple.com/documentation/security/errsecendofdata)

|  | Declaration |
| --- | --- |
| From | ``` var errSecEndOfData: Int { get } ``` |
| To | ``` var errSecEndOfData: OSStatus { get } ``` |

Modified [errSecEventNotificationCallbackNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseceventnotificationcallbacknotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecEventNotificationCallbackNotFound: Int { get } ``` |
| To | ``` var errSecEventNotificationCallbackNotFound: OSStatus { get } ``` |

Modified [errSecExtendedKeyUsageNotCritical](https://developer.apple.com/documentation/security/errsecextendedkeyusagenotcritical)

|  | Declaration |
| --- | --- |
| From | ``` var errSecExtendedKeyUsageNotCritical: Int { get } ``` |
| To | ``` var errSecExtendedKeyUsageNotCritical: OSStatus { get } ``` |

Modified [errSecFieldSpecifiedMultiple](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecfieldspecifiedmultiple)

|  | Declaration |
| --- | --- |
| From | ``` var errSecFieldSpecifiedMultiple: Int { get } ``` |
| To | ``` var errSecFieldSpecifiedMultiple: OSStatus { get } ``` |

Modified [errSecFileTooBig](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecfiletoobig)

|  | Declaration |
| --- | --- |
| From | ``` var errSecFileTooBig: Int { get } ``` |
| To | ``` var errSecFileTooBig: OSStatus { get } ``` |

Modified [errSecFunctionFailed](https://developer.apple.com/documentation/security/errsecfunctionfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecFunctionFailed: Int { get } ``` |
| To | ``` var errSecFunctionFailed: OSStatus { get } ``` |

Modified [errSecFunctionIntegrityFail](https://developer.apple.com/documentation/security/errsecfunctionintegrityfail)

|  | Declaration |
| --- | --- |
| From | ``` var errSecFunctionIntegrityFail: Int { get } ``` |
| To | ``` var errSecFunctionIntegrityFail: OSStatus { get } ``` |

Modified [errSecHostNameMismatch](https://developer.apple.com/documentation/security/errsechostnamemismatch)

|  | Declaration |
| --- | --- |
| From | ``` var errSecHostNameMismatch: Int { get } ``` |
| To | ``` var errSecHostNameMismatch: OSStatus { get } ``` |

Modified [errSecIDPFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecidpfailure)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIDPFailure: Int { get } ``` |
| To | ``` var errSecIDPFailure: OSStatus { get } ``` |

Modified [errSecIncompatibleDatabaseBlob](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatibledatabaseblob)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIncompatibleDatabaseBlob: Int { get } ``` |
| To | ``` var errSecIncompatibleDatabaseBlob: OSStatus { get } ``` |

Modified [errSecIncompatibleFieldFormat](https://developer.apple.com/documentation/security/errsecincompatiblefieldformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIncompatibleFieldFormat: Int { get } ``` |
| To | ``` var errSecIncompatibleFieldFormat: OSStatus { get } ``` |

Modified [errSecIncompatibleKeyBlob](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatiblekeyblob)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIncompatibleKeyBlob: Int { get } ``` |
| To | ``` var errSecIncompatibleKeyBlob: OSStatus { get } ``` |

Modified [errSecIncompatibleVersion](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatibleversion)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIncompatibleVersion: Int { get } ``` |
| To | ``` var errSecIncompatibleVersion: OSStatus { get } ``` |

Modified [errSecIncompleteCertRevocationCheck](https://developer.apple.com/documentation/security/errsecincompletecertrevocationcheck)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIncompleteCertRevocationCheck: Int { get } ``` |
| To | ``` var errSecIncompleteCertRevocationCheck: OSStatus { get } ``` |

Modified [errSecInDarkWake](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecindarkwake)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInDarkWake: Int { get } ``` |
| To | ``` var errSecInDarkWake: OSStatus { get } ``` |

Modified [errSecInputLengthError](https://developer.apple.com/documentation/security/errsecinputlengtherror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInputLengthError: Int { get } ``` |
| To | ``` var errSecInputLengthError: OSStatus { get } ``` |

Modified [errSecInsufficientClientID](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinsufficientclientid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInsufficientClientID: Int { get } ``` |
| To | ``` var errSecInsufficientClientID: OSStatus { get } ``` |

Modified [errSecInsufficientCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinsufficientcredentials)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInsufficientCredentials: Int { get } ``` |
| To | ``` var errSecInsufficientCredentials: OSStatus { get } ``` |

Modified [errSecInteractionNotAllowed](https://developer.apple.com/documentation/security/errsecinteractionnotallowed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInteractionNotAllowed: Int { get } ``` |
| To | ``` var errSecInteractionNotAllowed: OSStatus { get } ``` |

Modified [errSecInteractionRequired](https://developer.apple.com/documentation/security/errsecinteractionrequired)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInteractionRequired: Int { get } ``` |
| To | ``` var errSecInteractionRequired: OSStatus { get } ``` |

Modified [errSecInternalComponent](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinternalcomponent)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInternalComponent: Int { get } ``` |
| To | ``` var errSecInternalComponent: OSStatus { get } ``` |

Modified [errSecInternalError](https://developer.apple.com/documentation/security/errsecinternalerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInternalError: Int { get } ``` |
| To | ``` var errSecInternalError: OSStatus { get } ``` |

Modified [errSecInvaldCRLAuthority](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvaldcrlauthority)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvaldCRLAuthority: Int { get } ``` |
| To | ``` var errSecInvaldCRLAuthority: OSStatus { get } ``` |

Modified [errSecInvalidAccessCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidaccesscredentials)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAccessCredentials: Int { get } ``` |
| To | ``` var errSecInvalidAccessCredentials: OSStatus { get } ``` |

Modified [errSecInvalidAccessRequest](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidaccessrequest)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAccessRequest: Int { get } ``` |
| To | ``` var errSecInvalidAccessRequest: OSStatus { get } ``` |

Modified [errSecInvalidACL](https://developer.apple.com/documentation/security/errsecinvalidacl)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidACL: Int { get } ``` |
| To | ``` var errSecInvalidACL: OSStatus { get } ``` |

Modified [errSecInvalidAction](https://developer.apple.com/documentation/security/errsecinvalidaction)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAction: Int { get } ``` |
| To | ``` var errSecInvalidAction: OSStatus { get } ``` |

Modified [errSecInvalidAddinFunctionTable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidaddinfunctiontable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAddinFunctionTable: Int { get } ``` |
| To | ``` var errSecInvalidAddinFunctionTable: OSStatus { get } ``` |

Modified [errSecInvalidAlgorithm](https://developer.apple.com/documentation/security/errsecinvalidalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAlgorithm: Int { get } ``` |
| To | ``` var errSecInvalidAlgorithm: OSStatus { get } ``` |

Modified [errSecInvalidAlgorithmParms](https://developer.apple.com/documentation/security/errsecinvalidalgorithmparms)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAlgorithmParms: Int { get } ``` |
| To | ``` var errSecInvalidAlgorithmParms: OSStatus { get } ``` |

Modified [errSecInvalidAttributeAccessCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeaccesscredentials)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeAccessCredentials: Int { get } ``` |
| To | ``` var errSecInvalidAttributeAccessCredentials: OSStatus { get } ``` |

Modified [errSecInvalidAttributeBase](https://developer.apple.com/documentation/security/errsecinvalidattributebase)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeBase: Int { get } ``` |
| To | ``` var errSecInvalidAttributeBase: OSStatus { get } ``` |

Modified [errSecInvalidAttributeBlockSize](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeblocksize)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeBlockSize: Int { get } ``` |
| To | ``` var errSecInvalidAttributeBlockSize: OSStatus { get } ``` |

Modified [errSecInvalidAttributeDLDBHandle](https://developer.apple.com/documentation/security/errsecinvalidattributedldbhandle)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeDLDBHandle: Int { get } ``` |
| To | ``` var errSecInvalidAttributeDLDBHandle: OSStatus { get } ``` |

Modified [errSecInvalidAttributeEffectiveBits](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeeffectivebits)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeEffectiveBits: Int { get } ``` |
| To | ``` var errSecInvalidAttributeEffectiveBits: OSStatus { get } ``` |

Modified [errSecInvalidAttributeEndDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeenddate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeEndDate: Int { get } ``` |
| To | ``` var errSecInvalidAttributeEndDate: OSStatus { get } ``` |

Modified [errSecInvalidAttributeInitVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeinitvector)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeInitVector: Int { get } ``` |
| To | ``` var errSecInvalidAttributeInitVector: OSStatus { get } ``` |

Modified [errSecInvalidAttributeIterationCount](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeiterationcount)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeIterationCount: Int { get } ``` |
| To | ``` var errSecInvalidAttributeIterationCount: OSStatus { get } ``` |

Modified [errSecInvalidAttributeKey](https://developer.apple.com/documentation/security/errsecinvalidattributekey)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeKey: Int { get } ``` |
| To | ``` var errSecInvalidAttributeKey: OSStatus { get } ``` |

Modified [errSecInvalidAttributeKeyLength](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributekeylength)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeKeyLength: Int { get } ``` |
| To | ``` var errSecInvalidAttributeKeyLength: OSStatus { get } ``` |

Modified [errSecInvalidAttributeKeyType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributekeytype)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeKeyType: Int { get } ``` |
| To | ``` var errSecInvalidAttributeKeyType: OSStatus { get } ``` |

Modified [errSecInvalidAttributeLabel](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributelabel)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeLabel: Int { get } ``` |
| To | ``` var errSecInvalidAttributeLabel: OSStatus { get } ``` |

Modified [errSecInvalidAttributeMode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributemode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeMode: Int { get } ``` |
| To | ``` var errSecInvalidAttributeMode: OSStatus { get } ``` |

Modified [errSecInvalidAttributeOutputSize](https://developer.apple.com/documentation/security/errsecinvalidattributeoutputsize)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeOutputSize: Int { get } ``` |
| To | ``` var errSecInvalidAttributeOutputSize: OSStatus { get } ``` |

Modified [errSecInvalidAttributePadding](https://developer.apple.com/documentation/security/errsecinvalidattributepadding)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributePadding: Int { get } ``` |
| To | ``` var errSecInvalidAttributePadding: OSStatus { get } ``` |

Modified [errSecInvalidAttributePassphrase](https://developer.apple.com/documentation/security/errsecinvalidattributepassphrase)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributePassphrase: Int { get } ``` |
| To | ``` var errSecInvalidAttributePassphrase: OSStatus { get } ``` |

Modified [errSecInvalidAttributePrime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeprime)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributePrime: Int { get } ``` |
| To | ``` var errSecInvalidAttributePrime: OSStatus { get } ``` |

Modified [errSecInvalidAttributePrivateKeyFormat](https://developer.apple.com/documentation/security/errsecinvalidattributeprivatekeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributePrivateKeyFormat: Int { get } ``` |
| To | ``` var errSecInvalidAttributePrivateKeyFormat: OSStatus { get } ``` |

Modified [errSecInvalidAttributePublicKeyFormat](https://developer.apple.com/documentation/security/errsecinvalidattributepublickeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributePublicKeyFormat: Int { get } ``` |
| To | ``` var errSecInvalidAttributePublicKeyFormat: OSStatus { get } ``` |

Modified [errSecInvalidAttributeRandom](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributerandom)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeRandom: Int { get } ``` |
| To | ``` var errSecInvalidAttributeRandom: OSStatus { get } ``` |

Modified [errSecInvalidAttributeRounds](https://developer.apple.com/documentation/security/errsecinvalidattributerounds)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeRounds: Int { get } ``` |
| To | ``` var errSecInvalidAttributeRounds: OSStatus { get } ``` |

Modified [errSecInvalidAttributeSalt](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributesalt)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeSalt: Int { get } ``` |
| To | ``` var errSecInvalidAttributeSalt: OSStatus { get } ``` |

Modified [errSecInvalidAttributeSeed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeseed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeSeed: Int { get } ``` |
| To | ``` var errSecInvalidAttributeSeed: OSStatus { get } ``` |

Modified [errSecInvalidAttributeStartDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributestartdate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeStartDate: Int { get } ``` |
| To | ``` var errSecInvalidAttributeStartDate: OSStatus { get } ``` |

Modified [errSecInvalidAttributeSubprime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributesubprime)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeSubprime: Int { get } ``` |
| To | ``` var errSecInvalidAttributeSubprime: OSStatus { get } ``` |

Modified [errSecInvalidAttributeSymmetricKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributesymmetrickeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeSymmetricKeyFormat: Int { get } ``` |
| To | ``` var errSecInvalidAttributeSymmetricKeyFormat: OSStatus { get } ``` |

Modified [errSecInvalidAttributeVersion](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeversion)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeVersion: Int { get } ``` |
| To | ``` var errSecInvalidAttributeVersion: OSStatus { get } ``` |

Modified [errSecInvalidAttributeWrappedKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributewrappedkeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAttributeWrappedKeyFormat: Int { get } ``` |
| To | ``` var errSecInvalidAttributeWrappedKeyFormat: OSStatus { get } ``` |

Modified [errSecInvalidAuthority](https://developer.apple.com/documentation/security/errsecinvalidauthority)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAuthority: Int { get } ``` |
| To | ``` var errSecInvalidAuthority: OSStatus { get } ``` |

Modified [errSecInvalidAuthorityKeyID](https://developer.apple.com/documentation/security/errsecinvalidauthoritykeyid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidAuthorityKeyID: Int { get } ``` |
| To | ``` var errSecInvalidAuthorityKeyID: OSStatus { get } ``` |

Modified [errSecInvalidBaseACLs](https://developer.apple.com/documentation/security/errsecinvalidbaseacls)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidBaseACLs: Int { get } ``` |
| To | ``` var errSecInvalidBaseACLs: OSStatus { get } ``` |

Modified [errSecInvalidBundleInfo](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidbundleinfo)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidBundleInfo: Int { get } ``` |
| To | ``` var errSecInvalidBundleInfo: OSStatus { get } ``` |

Modified [errSecInvalidCallback](https://developer.apple.com/documentation/security/errsecinvalidcallback)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCallback: Int { get } ``` |
| To | ``` var errSecInvalidCallback: OSStatus { get } ``` |

Modified [errSecInvalidCertAuthority](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcertauthority)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCertAuthority: Int { get } ``` |
| To | ``` var errSecInvalidCertAuthority: OSStatus { get } ``` |

Modified [errSecInvalidCertificateGroup](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcertificategroup)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCertificateGroup: Int { get } ``` |
| To | ``` var errSecInvalidCertificateGroup: OSStatus { get } ``` |

Modified [errSecInvalidCertificateRef](https://developer.apple.com/documentation/security/errsecinvalidcertificateref)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCertificateRef: Int { get } ``` |
| To | ``` var errSecInvalidCertificateRef: OSStatus { get } ``` |

Modified [errSecInvalidContext](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcontext)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidContext: Int { get } ``` |
| To | ``` var errSecInvalidContext: OSStatus { get } ``` |

Modified [errSecInvalidCRL](https://developer.apple.com/documentation/security/errsecinvalidcrl)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCRL: Int { get } ``` |
| To | ``` var errSecInvalidCRL: OSStatus { get } ``` |

Modified [errSecInvalidCRLEncoding](https://developer.apple.com/documentation/security/errsecinvalidcrlencoding)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCRLEncoding: Int { get } ``` |
| To | ``` var errSecInvalidCRLEncoding: OSStatus { get } ``` |

Modified [errSecInvalidCRLGroup](https://developer.apple.com/documentation/security/errsecinvalidcrlgroup)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCRLGroup: Int { get } ``` |
| To | ``` var errSecInvalidCRLGroup: OSStatus { get } ``` |

Modified [errSecInvalidCRLIndex](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcrlindex)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCRLIndex: Int { get } ``` |
| To | ``` var errSecInvalidCRLIndex: OSStatus { get } ``` |

Modified [errSecInvalidCRLType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcrltype)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidCRLType: Int { get } ``` |
| To | ``` var errSecInvalidCRLType: OSStatus { get } ``` |

Modified [errSecInvalidData](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvaliddata)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidData: Int { get } ``` |
| To | ``` var errSecInvalidData: OSStatus { get } ``` |

Modified [errSecInvalidDatabaseBlob](https://developer.apple.com/documentation/security/errsecinvaliddatabaseblob)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidDatabaseBlob: Int { get } ``` |
| To | ``` var errSecInvalidDatabaseBlob: OSStatus { get } ``` |

Modified [errSecInvalidDBList](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvaliddblist)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidDBList: Int { get } ``` |
| To | ``` var errSecInvalidDBList: OSStatus { get } ``` |

Modified [errSecInvalidDBLocation](https://developer.apple.com/documentation/security/errsecinvaliddblocation)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidDBLocation: Int { get } ``` |
| To | ``` var errSecInvalidDBLocation: OSStatus { get } ``` |

Modified [errSecInvalidDigestAlgorithm](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvaliddigestalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidDigestAlgorithm: Int { get } ``` |
| To | ``` var errSecInvalidDigestAlgorithm: OSStatus { get } ``` |

Modified [errSecInvalidEncoding](https://developer.apple.com/documentation/security/errsecinvalidencoding)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidEncoding: Int { get } ``` |
| To | ``` var errSecInvalidEncoding: OSStatus { get } ``` |

Modified [errSecInvalidExtendedKeyUsage](https://developer.apple.com/documentation/security/errsecinvalidextendedkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidExtendedKeyUsage: Int { get } ``` |
| To | ``` var errSecInvalidExtendedKeyUsage: OSStatus { get } ``` |

Modified [errSecInvalidFormType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidformtype)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidFormType: Int { get } ``` |
| To | ``` var errSecInvalidFormType: OSStatus { get } ``` |

Modified [errSecInvalidGUID](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidguid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidGUID: Int { get } ``` |
| To | ``` var errSecInvalidGUID: OSStatus { get } ``` |

Modified [errSecInvalidHandle](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidhandle)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidHandle: Int { get } ``` |
| To | ``` var errSecInvalidHandle: OSStatus { get } ``` |

Modified [errSecInvalidHandleUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidhandleusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidHandleUsage: Int { get } ``` |
| To | ``` var errSecInvalidHandleUsage: OSStatus { get } ``` |

Modified [errSecInvalidID](https://developer.apple.com/documentation/security/errsecinvalidid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidID: Int { get } ``` |
| To | ``` var errSecInvalidID: OSStatus { get } ``` |

Modified [errSecInvalidIdentifier](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalididentifier)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidIdentifier: Int { get } ``` |
| To | ``` var errSecInvalidIdentifier: OSStatus { get } ``` |

Modified [errSecInvalidIDLinkage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalididlinkage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidIDLinkage: Int { get } ``` |
| To | ``` var errSecInvalidIDLinkage: OSStatus { get } ``` |

Modified [errSecInvalidIndex](https://developer.apple.com/documentation/security/errsecinvalidindex)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidIndex: Int { get } ``` |
| To | ``` var errSecInvalidIndex: OSStatus { get } ``` |

Modified [errSecInvalidIndexInfo](https://developer.apple.com/documentation/security/errsecinvalidindexinfo)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidIndexInfo: Int { get } ``` |
| To | ``` var errSecInvalidIndexInfo: OSStatus { get } ``` |

Modified [errSecInvalidInputVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidinputvector)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidInputVector: Int { get } ``` |
| To | ``` var errSecInvalidInputVector: OSStatus { get } ``` |

Modified [errSecInvalidItemRef](https://developer.apple.com/documentation/security/errsecinvaliditemref)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidItemRef: Int { get } ``` |
| To | ``` var errSecInvalidItemRef: OSStatus { get } ``` |

Modified [errSecInvalidKeyAttributeMask](https://developer.apple.com/documentation/security/errsecinvalidkeyattributemask)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyAttributeMask: Int { get } ``` |
| To | ``` var errSecInvalidKeyAttributeMask: OSStatus { get } ``` |

Modified [errSecInvalidKeyBlob](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyblob)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyBlob: Int { get } ``` |
| To | ``` var errSecInvalidKeyBlob: OSStatus { get } ``` |

Modified [errSecInvalidKeychain](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeychain)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeychain: Int { get } ``` |
| To | ``` var errSecInvalidKeychain: OSStatus { get } ``` |

Modified [errSecInvalidKeyFormat](https://developer.apple.com/documentation/security/errsecinvalidkeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyFormat: Int { get } ``` |
| To | ``` var errSecInvalidKeyFormat: OSStatus { get } ``` |

Modified [errSecInvalidKeyHierarchy](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyhierarchy)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyHierarchy: Int { get } ``` |
| To | ``` var errSecInvalidKeyHierarchy: OSStatus { get } ``` |

Modified [errSecInvalidKeyLabel](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeylabel)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyLabel: Int { get } ``` |
| To | ``` var errSecInvalidKeyLabel: OSStatus { get } ``` |

Modified [errSecInvalidKeyRef](https://developer.apple.com/documentation/security/errsecinvalidkeyref)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyRef: Int { get } ``` |
| To | ``` var errSecInvalidKeyRef: OSStatus { get } ``` |

Modified [errSecInvalidKeyUsageForPolicy](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyusageforpolicy)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyUsageForPolicy: Int { get } ``` |
| To | ``` var errSecInvalidKeyUsageForPolicy: OSStatus { get } ``` |

Modified [errSecInvalidKeyUsageMask](https://developer.apple.com/documentation/security/errsecinvalidkeyusagemask)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidKeyUsageMask: Int { get } ``` |
| To | ``` var errSecInvalidKeyUsageMask: OSStatus { get } ``` |

Modified [errSecInvalidLoginName](https://developer.apple.com/documentation/security/errsecinvalidloginname)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidLoginName: Int { get } ``` |
| To | ``` var errSecInvalidLoginName: OSStatus { get } ``` |

Modified [errSecInvalidModifyMode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidmodifymode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidModifyMode: Int { get } ``` |
| To | ``` var errSecInvalidModifyMode: OSStatus { get } ``` |

Modified [errSecInvalidName](https://developer.apple.com/documentation/security/errsecinvalidname)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidName: Int { get } ``` |
| To | ``` var errSecInvalidName: OSStatus { get } ``` |

Modified [errSecInvalidNetworkAddress](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidnetworkaddress)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidNetworkAddress: Int { get } ``` |
| To | ``` var errSecInvalidNetworkAddress: OSStatus { get } ``` |

Modified [errSecInvalidNewOwner](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidnewowner)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidNewOwner: Int { get } ``` |
| To | ``` var errSecInvalidNewOwner: OSStatus { get } ``` |

Modified [errSecInvalidNumberOfFields](https://developer.apple.com/documentation/security/errsecinvalidnumberoffields)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidNumberOfFields: Int { get } ``` |
| To | ``` var errSecInvalidNumberOfFields: OSStatus { get } ``` |

Modified [errSecInvalidOutputVector](https://developer.apple.com/documentation/security/errsecinvalidoutputvector)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidOutputVector: Int { get } ``` |
| To | ``` var errSecInvalidOutputVector: OSStatus { get } ``` |

Modified [errSecInvalidOwnerEdit](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidowneredit)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidOwnerEdit: Int { get } ``` |
| To | ``` var errSecInvalidOwnerEdit: OSStatus { get } ``` |

Modified [errSecInvalidParsingModule](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidparsingmodule)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidParsingModule: Int { get } ``` |
| To | ``` var errSecInvalidParsingModule: OSStatus { get } ``` |

Modified [errSecInvalidPassthroughID](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidpassthroughid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidPassthroughID: Int { get } ``` |
| To | ``` var errSecInvalidPassthroughID: OSStatus { get } ``` |

Modified [errSecInvalidPasswordRef](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidpasswordref)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidPasswordRef: Int { get } ``` |
| To | ``` var errSecInvalidPasswordRef: OSStatus { get } ``` |

Modified [errSecInvalidPointer](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidpointer)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidPointer: Int { get } ``` |
| To | ``` var errSecInvalidPointer: OSStatus { get } ``` |

Modified [errSecInvalidPolicyIdentifiers](https://developer.apple.com/documentation/security/errsecinvalidpolicyidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidPolicyIdentifiers: Int { get } ``` |
| To | ``` var errSecInvalidPolicyIdentifiers: OSStatus { get } ``` |

Modified [errSecInvalidPrefsDomain](https://developer.apple.com/documentation/security/errsecinvalidprefsdomain)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidPrefsDomain: Int { get } ``` |
| To | ``` var errSecInvalidPrefsDomain: OSStatus { get } ``` |

Modified [errSecInvalidPVC](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidpvc)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidPVC: Int { get } ``` |
| To | ``` var errSecInvalidPVC: OSStatus { get } ``` |

Modified [errSecInvalidQuery](https://developer.apple.com/documentation/security/errsecinvalidquery)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidQuery: Int { get } ``` |
| To | ``` var errSecInvalidQuery: OSStatus { get } ``` |

Modified [errSecInvalidReason](https://developer.apple.com/documentation/security/errsecinvalidreason)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidReason: Int { get } ``` |
| To | ``` var errSecInvalidReason: OSStatus { get } ``` |

Modified [errSecInvalidRecord](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidrecord)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidRecord: Int { get } ``` |
| To | ``` var errSecInvalidRecord: OSStatus { get } ``` |

Modified [errSecInvalidRequestInputs](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidrequestinputs)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidRequestInputs: Int { get } ``` |
| To | ``` var errSecInvalidRequestInputs: OSStatus { get } ``` |

Modified [errSecInvalidRequestor](https://developer.apple.com/documentation/security/errsecinvalidrequestor)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidRequestor: Int { get } ``` |
| To | ``` var errSecInvalidRequestor: OSStatus { get } ``` |

Modified [errSecInvalidResponseVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidresponsevector)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidResponseVector: Int { get } ``` |
| To | ``` var errSecInvalidResponseVector: OSStatus { get } ``` |

Modified [errSecInvalidRoot](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidroot)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidRoot: Int { get } ``` |
| To | ``` var errSecInvalidRoot: OSStatus { get } ``` |

Modified [errSecInvalidSampleValue](https://developer.apple.com/documentation/security/errsecinvalidsamplevalue)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidSampleValue: Int { get } ``` |
| To | ``` var errSecInvalidSampleValue: OSStatus { get } ``` |

Modified [errSecInvalidScope](https://developer.apple.com/documentation/security/errsecinvalidscope)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidScope: Int { get } ``` |
| To | ``` var errSecInvalidScope: OSStatus { get } ``` |

Modified [errSecInvalidSearchRef](https://developer.apple.com/documentation/security/errsecinvalidsearchref)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidSearchRef: Int { get } ``` |
| To | ``` var errSecInvalidSearchRef: OSStatus { get } ``` |

Modified [errSecInvalidServiceMask](https://developer.apple.com/documentation/security/errsecinvalidservicemask)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidServiceMask: Int { get } ``` |
| To | ``` var errSecInvalidServiceMask: OSStatus { get } ``` |

Modified [errSecInvalidSignature](https://developer.apple.com/documentation/security/errsecinvalidsignature)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidSignature: Int { get } ``` |
| To | ``` var errSecInvalidSignature: OSStatus { get } ``` |

Modified [errSecInvalidStopOnPolicy](https://developer.apple.com/documentation/security/errsecinvalidstoponpolicy)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidStopOnPolicy: Int { get } ``` |
| To | ``` var errSecInvalidStopOnPolicy: OSStatus { get } ``` |

Modified [errSecInvalidSubjectKeyID](https://developer.apple.com/documentation/security/errsecinvalidsubjectkeyid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidSubjectKeyID: Int { get } ``` |
| To | ``` var errSecInvalidSubjectKeyID: OSStatus { get } ``` |

Modified [errSecInvalidSubjectName](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidsubjectname)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidSubjectName: Int { get } ``` |
| To | ``` var errSecInvalidSubjectName: OSStatus { get } ``` |

Modified [errSecInvalidSubServiceID](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidsubserviceid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidSubServiceID: Int { get } ``` |
| To | ``` var errSecInvalidSubServiceID: OSStatus { get } ``` |

Modified [errSecInvalidTimeString](https://developer.apple.com/documentation/security/errsecinvalidtimestring)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidTimeString: Int { get } ``` |
| To | ``` var errSecInvalidTimeString: OSStatus { get } ``` |

Modified [errSecInvalidTrustSetting](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidtrustsetting)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidTrustSetting: Int { get } ``` |
| To | ``` var errSecInvalidTrustSetting: OSStatus { get } ``` |

Modified [errSecInvalidTrustSettings](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidtrustsettings)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidTrustSettings: Int { get } ``` |
| To | ``` var errSecInvalidTrustSettings: OSStatus { get } ``` |

Modified [errSecInvalidTuple](https://developer.apple.com/documentation/security/errsecinvalidtuple)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidTuple: Int { get } ``` |
| To | ``` var errSecInvalidTuple: OSStatus { get } ``` |

Modified [errSecInvalidTupleCredendtials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidtuplecredendtials)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidTupleCredendtials: Int { get } ``` |
| To | ``` var errSecInvalidTupleCredendtials: OSStatus { get } ``` |

Modified [errSecInvalidTupleGroup](https://developer.apple.com/documentation/security/errsecinvalidtuplegroup)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidTupleGroup: Int { get } ``` |
| To | ``` var errSecInvalidTupleGroup: OSStatus { get } ``` |

Modified [errSecInvalidValidityPeriod](https://developer.apple.com/documentation/security/errsecinvalidvalidityperiod)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidValidityPeriod: Int { get } ``` |
| To | ``` var errSecInvalidValidityPeriod: OSStatus { get } ``` |

Modified [errSecInvalidValue](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidvalue)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInvalidValue: Int { get } ``` |
| To | ``` var errSecInvalidValue: OSStatus { get } ``` |

Modified [errSecIO](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecio)

|  | Declaration |
| --- | --- |
| From | ``` var errSecIO: Int { get } ``` |
| To | ``` var errSecIO: OSStatus { get } ``` |

Modified [errSecItemNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecitemnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecItemNotFound: Int { get } ``` |
| To | ``` var errSecItemNotFound: OSStatus { get } ``` |

Modified [errSecKeyBlobTypeIncorrect](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseckeyblobtypeincorrect)

|  | Declaration |
| --- | --- |
| From | ``` var errSecKeyBlobTypeIncorrect: Int { get } ``` |
| To | ``` var errSecKeyBlobTypeIncorrect: OSStatus { get } ``` |

Modified [errSecKeyHeaderInconsistent](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseckeyheaderinconsistent)

|  | Declaration |
| --- | --- |
| From | ``` var errSecKeyHeaderInconsistent: Int { get } ``` |
| To | ``` var errSecKeyHeaderInconsistent: OSStatus { get } ``` |

Modified [errSecKeyIsSensitive](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseckeyissensitive)

|  | Declaration |
| --- | --- |
| From | ``` var errSecKeyIsSensitive: Int { get } ``` |
| To | ``` var errSecKeyIsSensitive: OSStatus { get } ``` |

Modified [errSecKeySizeNotAllowed](https://developer.apple.com/documentation/security/errseckeysizenotallowed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecKeySizeNotAllowed: Int { get } ``` |
| To | ``` var errSecKeySizeNotAllowed: OSStatus { get } ``` |

Modified [errSecKeyUsageIncorrect](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseckeyusageincorrect)

|  | Declaration |
| --- | --- |
| From | ``` var errSecKeyUsageIncorrect: Int { get } ``` |
| To | ``` var errSecKeyUsageIncorrect: OSStatus { get } ``` |

Modified [errSecLibraryReferenceNotFound](https://developer.apple.com/documentation/security/errseclibraryreferencenotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecLibraryReferenceNotFound: Int { get } ``` |
| To | ``` var errSecLibraryReferenceNotFound: OSStatus { get } ``` |

Modified [errSecMDSError](https://developer.apple.com/documentation/security/errsecmdserror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMDSError: Int { get } ``` |
| To | ``` var errSecMDSError: OSStatus { get } ``` |

Modified [errSecMemoryError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmemoryerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMemoryError: Int { get } ``` |
| To | ``` var errSecMemoryError: OSStatus { get } ``` |

Modified [errSecMissingAlgorithmParms](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingalgorithmparms)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAlgorithmParms: Int { get } ``` |
| To | ``` var errSecMissingAlgorithmParms: OSStatus { get } ``` |

Modified [errSecMissingAttributeAccessCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeaccesscredentials)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeAccessCredentials: Int { get } ``` |
| To | ``` var errSecMissingAttributeAccessCredentials: OSStatus { get } ``` |

Modified [errSecMissingAttributeBase](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributebase)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeBase: Int { get } ``` |
| To | ``` var errSecMissingAttributeBase: OSStatus { get } ``` |

Modified [errSecMissingAttributeBlockSize](https://developer.apple.com/documentation/security/errsecmissingattributeblocksize)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeBlockSize: Int { get } ``` |
| To | ``` var errSecMissingAttributeBlockSize: OSStatus { get } ``` |

Modified [errSecMissingAttributeDLDBHandle](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributedldbhandle)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeDLDBHandle: Int { get } ``` |
| To | ``` var errSecMissingAttributeDLDBHandle: OSStatus { get } ``` |

Modified [errSecMissingAttributeEffectiveBits](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeeffectivebits)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeEffectiveBits: Int { get } ``` |
| To | ``` var errSecMissingAttributeEffectiveBits: OSStatus { get } ``` |

Modified [errSecMissingAttributeEndDate](https://developer.apple.com/documentation/security/errsecmissingattributeenddate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeEndDate: Int { get } ``` |
| To | ``` var errSecMissingAttributeEndDate: OSStatus { get } ``` |

Modified [errSecMissingAttributeInitVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeinitvector)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeInitVector: Int { get } ``` |
| To | ``` var errSecMissingAttributeInitVector: OSStatus { get } ``` |

Modified [errSecMissingAttributeIterationCount](https://developer.apple.com/documentation/security/errsecmissingattributeiterationcount)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeIterationCount: Int { get } ``` |
| To | ``` var errSecMissingAttributeIterationCount: OSStatus { get } ``` |

Modified [errSecMissingAttributeKey](https://developer.apple.com/documentation/security/errsecmissingattributekey)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeKey: Int { get } ``` |
| To | ``` var errSecMissingAttributeKey: OSStatus { get } ``` |

Modified [errSecMissingAttributeKeyLength](https://developer.apple.com/documentation/security/errsecmissingattributekeylength)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeKeyLength: Int { get } ``` |
| To | ``` var errSecMissingAttributeKeyLength: OSStatus { get } ``` |

Modified [errSecMissingAttributeKeyType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributekeytype)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeKeyType: Int { get } ``` |
| To | ``` var errSecMissingAttributeKeyType: OSStatus { get } ``` |

Modified [errSecMissingAttributeLabel](https://developer.apple.com/documentation/security/errsecmissingattributelabel)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeLabel: Int { get } ``` |
| To | ``` var errSecMissingAttributeLabel: OSStatus { get } ``` |

Modified [errSecMissingAttributeMode](https://developer.apple.com/documentation/security/errsecmissingattributemode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeMode: Int { get } ``` |
| To | ``` var errSecMissingAttributeMode: OSStatus { get } ``` |

Modified [errSecMissingAttributeOutputSize](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeoutputsize)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeOutputSize: Int { get } ``` |
| To | ``` var errSecMissingAttributeOutputSize: OSStatus { get } ``` |

Modified [errSecMissingAttributePadding](https://developer.apple.com/documentation/security/errsecmissingattributepadding)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributePadding: Int { get } ``` |
| To | ``` var errSecMissingAttributePadding: OSStatus { get } ``` |

Modified [errSecMissingAttributePassphrase](https://developer.apple.com/documentation/security/errsecmissingattributepassphrase)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributePassphrase: Int { get } ``` |
| To | ``` var errSecMissingAttributePassphrase: OSStatus { get } ``` |

Modified [errSecMissingAttributePrime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeprime)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributePrime: Int { get } ``` |
| To | ``` var errSecMissingAttributePrime: OSStatus { get } ``` |

Modified [errSecMissingAttributePrivateKeyFormat](https://developer.apple.com/documentation/security/errsecmissingattributeprivatekeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributePrivateKeyFormat: Int { get } ``` |
| To | ``` var errSecMissingAttributePrivateKeyFormat: OSStatus { get } ``` |

Modified [errSecMissingAttributePublicKeyFormat](https://developer.apple.com/documentation/security/errsecmissingattributepublickeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributePublicKeyFormat: Int { get } ``` |
| To | ``` var errSecMissingAttributePublicKeyFormat: OSStatus { get } ``` |

Modified [errSecMissingAttributeRandom](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributerandom)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeRandom: Int { get } ``` |
| To | ``` var errSecMissingAttributeRandom: OSStatus { get } ``` |

Modified [errSecMissingAttributeRounds](https://developer.apple.com/documentation/security/errsecmissingattributerounds)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeRounds: Int { get } ``` |
| To | ``` var errSecMissingAttributeRounds: OSStatus { get } ``` |

Modified [errSecMissingAttributeSalt](https://developer.apple.com/documentation/security/errsecmissingattributesalt)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeSalt: Int { get } ``` |
| To | ``` var errSecMissingAttributeSalt: OSStatus { get } ``` |

Modified [errSecMissingAttributeSeed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeseed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeSeed: Int { get } ``` |
| To | ``` var errSecMissingAttributeSeed: OSStatus { get } ``` |

Modified [errSecMissingAttributeStartDate](https://developer.apple.com/documentation/security/errsecmissingattributestartdate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeStartDate: Int { get } ``` |
| To | ``` var errSecMissingAttributeStartDate: OSStatus { get } ``` |

Modified [errSecMissingAttributeSubprime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributesubprime)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeSubprime: Int { get } ``` |
| To | ``` var errSecMissingAttributeSubprime: OSStatus { get } ``` |

Modified [errSecMissingAttributeSymmetricKeyFormat](https://developer.apple.com/documentation/security/errsecmissingattributesymmetrickeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeSymmetricKeyFormat: Int { get } ``` |
| To | ``` var errSecMissingAttributeSymmetricKeyFormat: OSStatus { get } ``` |

Modified [errSecMissingAttributeVersion](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeversion)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeVersion: Int { get } ``` |
| To | ``` var errSecMissingAttributeVersion: OSStatus { get } ``` |

Modified [errSecMissingAttributeWrappedKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributewrappedkeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingAttributeWrappedKeyFormat: Int { get } ``` |
| To | ``` var errSecMissingAttributeWrappedKeyFormat: OSStatus { get } ``` |

Modified [errSecMissingRequiredExtension](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingrequiredextension)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingRequiredExtension: Int { get } ``` |
| To | ``` var errSecMissingRequiredExtension: OSStatus { get } ``` |

Modified [errSecMissingValue](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingvalue)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMissingValue: Int { get } ``` |
| To | ``` var errSecMissingValue: OSStatus { get } ``` |

Modified [errSecMobileMeCSRVerifyFailure](https://developer.apple.com/documentation/security/errsecmobilemecsrverifyfailure)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeCSRVerifyFailure: Int { get } ``` |
| To | ``` var errSecMobileMeCSRVerifyFailure: OSStatus { get } ``` |

Modified [errSecMobileMeFailedConsistencyCheck](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemefailedconsistencycheck)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeFailedConsistencyCheck: Int { get } ``` |
| To | ``` var errSecMobileMeFailedConsistencyCheck: OSStatus { get } ``` |

Modified [errSecMobileMeNoRequestPending](https://developer.apple.com/documentation/security/errsecmobilemenorequestpending)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeNoRequestPending: Int { get } ``` |
| To | ``` var errSecMobileMeNoRequestPending: OSStatus { get } ``` |

Modified [errSecMobileMeRequestAlreadyPending](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemerequestalreadypending)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeRequestAlreadyPending: Int { get } ``` |
| To | ``` var errSecMobileMeRequestAlreadyPending: OSStatus { get } ``` |

Modified [errSecMobileMeRequestQueued](https://developer.apple.com/documentation/security/errsecmobilemerequestqueued)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeRequestQueued: Int { get } ``` |
| To | ``` var errSecMobileMeRequestQueued: OSStatus { get } ``` |

Modified [errSecMobileMeRequestRedirected](https://developer.apple.com/documentation/security/errsecmobilemerequestredirected)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeRequestRedirected: Int { get } ``` |
| To | ``` var errSecMobileMeRequestRedirected: OSStatus { get } ``` |

Modified [errSecMobileMeServerAlreadyExists](https://developer.apple.com/documentation/security/errsecmobilemeserveralreadyexists)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeServerAlreadyExists: Int { get } ``` |
| To | ``` var errSecMobileMeServerAlreadyExists: OSStatus { get } ``` |

Modified [errSecMobileMeServerError](https://developer.apple.com/documentation/security/errsecmobilemeservererror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeServerError: Int { get } ``` |
| To | ``` var errSecMobileMeServerError: OSStatus { get } ``` |

Modified [errSecMobileMeServerNotAvailable](https://developer.apple.com/documentation/security/errsecmobilemeservernotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeServerNotAvailable: Int { get } ``` |
| To | ``` var errSecMobileMeServerNotAvailable: OSStatus { get } ``` |

Modified [errSecMobileMeServerServiceErr](https://developer.apple.com/documentation/security/errsecmobilemeserverserviceerr)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMobileMeServerServiceErr: Int { get } ``` |
| To | ``` var errSecMobileMeServerServiceErr: OSStatus { get } ``` |

Modified [errSecModuleManagerInitializeFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmodulemanagerinitializefailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecModuleManagerInitializeFailed: Int { get } ``` |
| To | ``` var errSecModuleManagerInitializeFailed: OSStatus { get } ``` |

Modified [errSecModuleManagerNotFound](https://developer.apple.com/documentation/security/errsecmodulemanagernotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecModuleManagerNotFound: Int { get } ``` |
| To | ``` var errSecModuleManagerNotFound: OSStatus { get } ``` |

Modified [errSecModuleManifestVerifyFailed](https://developer.apple.com/documentation/security/errsecmodulemanifestverifyfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecModuleManifestVerifyFailed: Int { get } ``` |
| To | ``` var errSecModuleManifestVerifyFailed: OSStatus { get } ``` |

Modified [errSecModuleNotLoaded](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmodulenotloaded)

|  | Declaration |
| --- | --- |
| From | ``` var errSecModuleNotLoaded: Int { get } ``` |
| To | ``` var errSecModuleNotLoaded: OSStatus { get } ``` |

Modified [errSecMultiplePrivKeys](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmultipleprivkeys)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMultiplePrivKeys: Int { get } ``` |
| To | ``` var errSecMultiplePrivKeys: OSStatus { get } ``` |

Modified [errSecMultipleValuesUnsupported](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmultiplevaluesunsupported)

|  | Declaration |
| --- | --- |
| From | ``` var errSecMultipleValuesUnsupported: Int { get } ``` |
| To | ``` var errSecMultipleValuesUnsupported: OSStatus { get } ``` |

Modified [errSecNetworkFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnetworkfailure)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNetworkFailure: Int { get } ``` |
| To | ``` var errSecNetworkFailure: OSStatus { get } ``` |

Modified [errSecNoAccessForItem](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnoaccessforitem)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoAccessForItem: Int { get } ``` |
| To | ``` var errSecNoAccessForItem: OSStatus { get } ``` |

Modified [errSecNoBasicConstraints](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnobasicconstraints)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoBasicConstraints: Int { get } ``` |
| To | ``` var errSecNoBasicConstraints: OSStatus { get } ``` |

Modified [errSecNoBasicConstraintsCA](https://developer.apple.com/documentation/security/errsecnobasicconstraintsca)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoBasicConstraintsCA: Int { get } ``` |
| To | ``` var errSecNoBasicConstraintsCA: OSStatus { get } ``` |

Modified [errSecNoCertificateModule](https://developer.apple.com/documentation/security/errsecnocertificatemodule)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoCertificateModule: Int { get } ``` |
| To | ``` var errSecNoCertificateModule: OSStatus { get } ``` |

Modified [errSecNoDefaultAuthority](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnodefaultauthority)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoDefaultAuthority: Int { get } ``` |
| To | ``` var errSecNoDefaultAuthority: OSStatus { get } ``` |

Modified [errSecNoDefaultKeychain](https://developer.apple.com/documentation/security/errsecnodefaultkeychain)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoDefaultKeychain: Int { get } ``` |
| To | ``` var errSecNoDefaultKeychain: OSStatus { get } ``` |

Modified [errSecNoFieldValues](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnofieldvalues)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoFieldValues: Int { get } ``` |
| To | ``` var errSecNoFieldValues: OSStatus { get } ``` |

Modified [errSecNoPolicyModule](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnopolicymodule)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoPolicyModule: Int { get } ``` |
| To | ``` var errSecNoPolicyModule: OSStatus { get } ``` |

Modified [errSecNoStorageModule](https://developer.apple.com/documentation/security/errsecnostoragemodule)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoStorageModule: Int { get } ``` |
| To | ``` var errSecNoStorageModule: OSStatus { get } ``` |

Modified [errSecNoSuchAttr](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnosuchattr)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoSuchAttr: Int { get } ``` |
| To | ``` var errSecNoSuchAttr: OSStatus { get } ``` |

Modified [errSecNoSuchClass](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnosuchclass)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoSuchClass: Int { get } ``` |
| To | ``` var errSecNoSuchClass: OSStatus { get } ``` |

Modified [errSecNoSuchKeychain](https://developer.apple.com/documentation/security/errsecnosuchkeychain)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoSuchKeychain: Int { get } ``` |
| To | ``` var errSecNoSuchKeychain: OSStatus { get } ``` |

Modified [errSecNotAvailable](https://developer.apple.com/documentation/security/errsecnotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotAvailable: Int { get } ``` |
| To | ``` var errSecNotAvailable: OSStatus { get } ``` |

Modified [errSecNotInitialized](https://developer.apple.com/documentation/security/errsecnotinitialized)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotInitialized: Int { get } ``` |
| To | ``` var errSecNotInitialized: OSStatus { get } ``` |

Modified [errSecNotLoggedIn](https://developer.apple.com/documentation/security/errsecnotloggedin)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotLoggedIn: Int { get } ``` |
| To | ``` var errSecNotLoggedIn: OSStatus { get } ``` |

Modified [errSecNoTrustSettings](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnotrustsettings)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNoTrustSettings: Int { get } ``` |
| To | ``` var errSecNoTrustSettings: OSStatus { get } ``` |

Modified [errSecNotSigner](https://developer.apple.com/documentation/security/errsecnotsigner)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotSigner: Int { get } ``` |
| To | ``` var errSecNotSigner: OSStatus { get } ``` |

Modified [errSecNotTrusted](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnottrusted)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotTrusted: Int { get } ``` |
| To | ``` var errSecNotTrusted: OSStatus { get } ``` |

Modified [errSecOCSPBadRequest](https://developer.apple.com/documentation/security/errsecocspbadrequest)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPBadRequest: Int { get } ``` |
| To | ``` var errSecOCSPBadRequest: OSStatus { get } ``` |

Modified [errSecOCSPBadResponse](https://developer.apple.com/documentation/security/errsecocspbadresponse)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPBadResponse: Int { get } ``` |
| To | ``` var errSecOCSPBadResponse: OSStatus { get } ``` |

Modified [errSecOCSPNoSigner](https://developer.apple.com/documentation/security/errsecocspnosigner)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPNoSigner: Int { get } ``` |
| To | ``` var errSecOCSPNoSigner: OSStatus { get } ``` |

Modified [errSecOCSPNotTrustedToAnchor](https://developer.apple.com/documentation/security/errsecocspnottrustedtoanchor)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPNotTrustedToAnchor: Int { get } ``` |
| To | ``` var errSecOCSPNotTrustedToAnchor: OSStatus { get } ``` |

Modified [errSecOCSPResponderInternalError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspresponderinternalerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPResponderInternalError: Int { get } ``` |
| To | ``` var errSecOCSPResponderInternalError: OSStatus { get } ``` |

Modified [errSecOCSPResponderMalformedReq](https://developer.apple.com/documentation/security/errsecocsprespondermalformedreq)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPResponderMalformedReq: Int { get } ``` |
| To | ``` var errSecOCSPResponderMalformedReq: OSStatus { get } ``` |

Modified [errSecOCSPResponderSignatureRequired](https://developer.apple.com/documentation/security/errsecocsprespondersignaturerequired)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPResponderSignatureRequired: Int { get } ``` |
| To | ``` var errSecOCSPResponderSignatureRequired: OSStatus { get } ``` |

Modified [errSecOCSPResponderTryLater](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocsprespondertrylater)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPResponderTryLater: Int { get } ``` |
| To | ``` var errSecOCSPResponderTryLater: OSStatus { get } ``` |

Modified [errSecOCSPResponderUnauthorized](https://developer.apple.com/documentation/security/errsecocspresponderunauthorized)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPResponderUnauthorized: Int { get } ``` |
| To | ``` var errSecOCSPResponderUnauthorized: OSStatus { get } ``` |

Modified [errSecOCSPResponseNonceMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspresponsenoncemismatch)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPResponseNonceMismatch: Int { get } ``` |
| To | ``` var errSecOCSPResponseNonceMismatch: OSStatus { get } ``` |

Modified [errSecOCSPSignatureError](https://developer.apple.com/documentation/security/errsecocspsignatureerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPSignatureError: Int { get } ``` |
| To | ``` var errSecOCSPSignatureError: OSStatus { get } ``` |

Modified [errSecOCSPStatusUnrecognized](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspstatusunrecognized)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPStatusUnrecognized: Int { get } ``` |
| To | ``` var errSecOCSPStatusUnrecognized: OSStatus { get } ``` |

Modified [errSecOCSPUnavailable](https://developer.apple.com/documentation/security/errsecocspunavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOCSPUnavailable: Int { get } ``` |
| To | ``` var errSecOCSPUnavailable: OSStatus { get } ``` |

Modified [errSecOutputLengthError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecoutputlengtherror)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOutputLengthError: Int { get } ``` |
| To | ``` var errSecOutputLengthError: OSStatus { get } ``` |

Modified [errSecParam](https://developer.apple.com/documentation/security/errsecparam)

|  | Declaration |
| --- | --- |
| From | ``` var errSecParam: Int { get } ``` |
| To | ``` var errSecParam: OSStatus { get } ``` |

Modified [errSecPassphraseRequired](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpassphraserequired)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPassphraseRequired: Int { get } ``` |
| To | ``` var errSecPassphraseRequired: OSStatus { get } ``` |

Modified [errSecPathLengthConstraintExceeded](https://developer.apple.com/documentation/security/errsecpathlengthconstraintexceeded)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPathLengthConstraintExceeded: Int { get } ``` |
| To | ``` var errSecPathLengthConstraintExceeded: OSStatus { get } ``` |

Modified [errSecPkcs12VerifyFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpkcs12verifyfailure)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPkcs12VerifyFailure: Int { get } ``` |
| To | ``` var errSecPkcs12VerifyFailure: OSStatus { get } ``` |

Modified [errSecPolicyNotFound](https://developer.apple.com/documentation/security/errsecpolicynotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPolicyNotFound: Int { get } ``` |
| To | ``` var errSecPolicyNotFound: OSStatus { get } ``` |

Modified [errSecPrivilegeNotGranted](https://developer.apple.com/documentation/security/errsecprivilegenotgranted)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPrivilegeNotGranted: Int { get } ``` |
| To | ``` var errSecPrivilegeNotGranted: OSStatus { get } ``` |

Modified [errSecPrivilegeNotSupported](https://developer.apple.com/documentation/security/errsecprivilegenotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPrivilegeNotSupported: Int { get } ``` |
| To | ``` var errSecPrivilegeNotSupported: OSStatus { get } ``` |

Modified [errSecPublicKeyInconsistent](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpublickeyinconsistent)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPublicKeyInconsistent: Int { get } ``` |
| To | ``` var errSecPublicKeyInconsistent: OSStatus { get } ``` |

Modified [errSecPVCAlreadyConfigured](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpvcalreadyconfigured)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPVCAlreadyConfigured: Int { get } ``` |
| To | ``` var errSecPVCAlreadyConfigured: OSStatus { get } ``` |

Modified [errSecPVCReferentNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpvcreferentnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecPVCReferentNotFound: Int { get } ``` |
| To | ``` var errSecPVCReferentNotFound: OSStatus { get } ``` |

Modified [errSecQuerySizeUnknown](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecquerysizeunknown)

|  | Declaration |
| --- | --- |
| From | ``` var errSecQuerySizeUnknown: Int { get } ``` |
| To | ``` var errSecQuerySizeUnknown: OSStatus { get } ``` |

Modified [errSecQuotaExceeded](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecquotaexceeded)

|  | Declaration |
| --- | --- |
| From | ``` var errSecQuotaExceeded: Int { get } ``` |
| To | ``` var errSecQuotaExceeded: OSStatus { get } ``` |

Modified [errSecReadOnly](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecreadonly)

|  | Declaration |
| --- | --- |
| From | ``` var errSecReadOnly: Int { get } ``` |
| To | ``` var errSecReadOnly: OSStatus { get } ``` |

Modified [errSecReadOnlyAttr](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecreadonlyattr)

|  | Declaration |
| --- | --- |
| From | ``` var errSecReadOnlyAttr: Int { get } ``` |
| To | ``` var errSecReadOnlyAttr: OSStatus { get } ``` |

Modified [errSecRecordModified](https://developer.apple.com/documentation/security/errsecrecordmodified)

|  | Declaration |
| --- | --- |
| From | ``` var errSecRecordModified: Int { get } ``` |
| To | ``` var errSecRecordModified: OSStatus { get } ``` |

Modified [errSecRejectedForm](https://developer.apple.com/documentation/security/errsecrejectedform)

|  | Declaration |
| --- | --- |
| From | ``` var errSecRejectedForm: Int { get } ``` |
| To | ``` var errSecRejectedForm: OSStatus { get } ``` |

Modified [errSecRequestDescriptor](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecrequestdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` var errSecRequestDescriptor: Int { get } ``` |
| To | ``` var errSecRequestDescriptor: OSStatus { get } ``` |

Modified [errSecRequestLost](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecrequestlost)

|  | Declaration |
| --- | --- |
| From | ``` var errSecRequestLost: Int { get } ``` |
| To | ``` var errSecRequestLost: OSStatus { get } ``` |

Modified [errSecRequestRejected](https://developer.apple.com/documentation/security/errsecrequestrejected)

|  | Declaration |
| --- | --- |
| From | ``` var errSecRequestRejected: Int { get } ``` |
| To | ``` var errSecRequestRejected: OSStatus { get } ``` |

Modified [errSecResourceSignBadCertChainLength](https://developer.apple.com/documentation/security/errsecresourcesignbadcertchainlength)

|  | Declaration |
| --- | --- |
| From | ``` var errSecResourceSignBadCertChainLength: Int { get } ``` |
| To | ``` var errSecResourceSignBadCertChainLength: OSStatus { get } ``` |

Modified [errSecResourceSignBadExtKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecresourcesignbadextkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecResourceSignBadExtKeyUsage: Int { get } ``` |
| To | ``` var errSecResourceSignBadExtKeyUsage: OSStatus { get } ``` |

Modified [errSecSelfCheckFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecselfcheckfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSelfCheckFailed: Int { get } ``` |
| To | ``` var errSecSelfCheckFailed: OSStatus { get } ``` |

Modified [errSecServiceNotAvailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecservicenotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecServiceNotAvailable: Int { get } ``` |
| To | ``` var errSecServiceNotAvailable: OSStatus { get } ``` |

Modified [errSecSigningTimeMissing](https://developer.apple.com/documentation/security/errsecsigningtimemissing)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSigningTimeMissing: Int { get } ``` |
| To | ``` var errSecSigningTimeMissing: OSStatus { get } ``` |

Modified [errSecSMIMEBadExtendedKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimebadextendedkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSMIMEBadExtendedKeyUsage: Int { get } ``` |
| To | ``` var errSecSMIMEBadExtendedKeyUsage: OSStatus { get } ``` |

Modified [errSecSMIMEBadKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimebadkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSMIMEBadKeyUsage: Int { get } ``` |
| To | ``` var errSecSMIMEBadKeyUsage: OSStatus { get } ``` |

Modified [errSecSMIMEEmailAddressesNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimeemailaddressesnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSMIMEEmailAddressesNotFound: Int { get } ``` |
| To | ``` var errSecSMIMEEmailAddressesNotFound: OSStatus { get } ``` |

Modified [errSecSMIMEKeyUsageNotCritical](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimekeyusagenotcritical)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSMIMEKeyUsageNotCritical: Int { get } ``` |
| To | ``` var errSecSMIMEKeyUsageNotCritical: OSStatus { get } ``` |

Modified [errSecSMIMENoEmailAddress](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimenoemailaddress)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSMIMENoEmailAddress: Int { get } ``` |
| To | ``` var errSecSMIMENoEmailAddress: OSStatus { get } ``` |

Modified [errSecSMIMESubjAltNameNotCritical](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimesubjaltnamenotcritical)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSMIMESubjAltNameNotCritical: Int { get } ``` |
| To | ``` var errSecSMIMESubjAltNameNotCritical: OSStatus { get } ``` |

Modified [errSecSSLBadExtendedKeyUsage](https://developer.apple.com/documentation/security/errsecsslbadextendedkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSSLBadExtendedKeyUsage: Int { get } ``` |
| To | ``` var errSecSSLBadExtendedKeyUsage: OSStatus { get } ``` |

Modified [errSecStagedOperationInProgress](https://developer.apple.com/documentation/security/errsecstagedoperationinprogress)

|  | Declaration |
| --- | --- |
| From | ``` var errSecStagedOperationInProgress: Int { get } ``` |
| To | ``` var errSecStagedOperationInProgress: OSStatus { get } ``` |

Modified [errSecStagedOperationNotStarted](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecstagedoperationnotstarted)

|  | Declaration |
| --- | --- |
| From | ``` var errSecStagedOperationNotStarted: Int { get } ``` |
| To | ``` var errSecStagedOperationNotStarted: OSStatus { get } ``` |

Modified [errSecSuccess](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsuccess)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSuccess: Int { get } ``` |
| To | ``` var errSecSuccess: OSStatus { get } ``` |

Modified [errSecTagNotFound](https://developer.apple.com/documentation/security/errsectagnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTagNotFound: Int { get } ``` |
| To | ``` var errSecTagNotFound: OSStatus { get } ``` |

Modified [errSecTimestampAddInfoNotAvailable](https://developer.apple.com/documentation/security/errsectimestampaddinfonotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampAddInfoNotAvailable: Int { get } ``` |
| To | ``` var errSecTimestampAddInfoNotAvailable: OSStatus { get } ``` |

Modified [errSecTimestampBadAlg](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampbadalg)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampBadAlg: Int { get } ``` |
| To | ``` var errSecTimestampBadAlg: OSStatus { get } ``` |

Modified [errSecTimestampBadDataFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampbaddataformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampBadDataFormat: Int { get } ``` |
| To | ``` var errSecTimestampBadDataFormat: OSStatus { get } ``` |

Modified [errSecTimestampBadRequest](https://developer.apple.com/documentation/security/errsectimestampbadrequest)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampBadRequest: Int { get } ``` |
| To | ``` var errSecTimestampBadRequest: OSStatus { get } ``` |

Modified [errSecTimestampInvalid](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampInvalid: Int { get } ``` |
| To | ``` var errSecTimestampInvalid: OSStatus { get } ``` |

Modified [errSecTimestampMissing](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampmissing)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampMissing: Int { get } ``` |
| To | ``` var errSecTimestampMissing: OSStatus { get } ``` |

Modified [errSecTimestampNotTrusted](https://developer.apple.com/documentation/security/errsectimestampnottrusted)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampNotTrusted: Int { get } ``` |
| To | ``` var errSecTimestampNotTrusted: OSStatus { get } ``` |

Modified [errSecTimestampRejection](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestamprejection)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampRejection: Int { get } ``` |
| To | ``` var errSecTimestampRejection: OSStatus { get } ``` |

Modified [errSecTimestampRevocationNotification](https://developer.apple.com/documentation/security/errsectimestamprevocationnotification)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampRevocationNotification: Int { get } ``` |
| To | ``` var errSecTimestampRevocationNotification: OSStatus { get } ``` |

Modified [errSecTimestampRevocationWarning](https://developer.apple.com/documentation/security/errsectimestamprevocationwarning)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampRevocationWarning: Int { get } ``` |
| To | ``` var errSecTimestampRevocationWarning: OSStatus { get } ``` |

Modified [errSecTimestampServiceNotAvailable](https://developer.apple.com/documentation/security/errsectimestampservicenotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampServiceNotAvailable: Int { get } ``` |
| To | ``` var errSecTimestampServiceNotAvailable: OSStatus { get } ``` |

Modified [errSecTimestampSystemFailure](https://developer.apple.com/documentation/security/errsectimestampsystemfailure)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampSystemFailure: Int { get } ``` |
| To | ``` var errSecTimestampSystemFailure: OSStatus { get } ``` |

Modified [errSecTimestampTimeNotAvailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestamptimenotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampTimeNotAvailable: Int { get } ``` |
| To | ``` var errSecTimestampTimeNotAvailable: OSStatus { get } ``` |

Modified [errSecTimestampUnacceptedExtension](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampunacceptedextension)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampUnacceptedExtension: Int { get } ``` |
| To | ``` var errSecTimestampUnacceptedExtension: OSStatus { get } ``` |

Modified [errSecTimestampUnacceptedPolicy](https://developer.apple.com/documentation/security/errsectimestampunacceptedpolicy)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampUnacceptedPolicy: Int { get } ``` |
| To | ``` var errSecTimestampUnacceptedPolicy: OSStatus { get } ``` |

Modified [errSecTimestampWaiting](https://developer.apple.com/documentation/security/errsectimestampwaiting)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTimestampWaiting: Int { get } ``` |
| To | ``` var errSecTimestampWaiting: OSStatus { get } ``` |

Modified [errSecTrustNotAvailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectrustnotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTrustNotAvailable: Int { get } ``` |
| To | ``` var errSecTrustNotAvailable: OSStatus { get } ``` |

Modified [errSecTrustSettingDeny](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectrustsettingdeny)

|  | Declaration |
| --- | --- |
| From | ``` var errSecTrustSettingDeny: Int { get } ``` |
| To | ``` var errSecTrustSettingDeny: OSStatus { get } ``` |

Modified [errSecUnimplemented](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunimplemented)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnimplemented: Int { get } ``` |
| To | ``` var errSecUnimplemented: OSStatus { get } ``` |

Modified [errSecUnknownCertExtension](https://developer.apple.com/documentation/security/errsecunknowncertextension)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnknownCertExtension: Int { get } ``` |
| To | ``` var errSecUnknownCertExtension: OSStatus { get } ``` |

Modified [errSecUnknownCriticalExtensionFlag](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunknowncriticalextensionflag)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnknownCriticalExtensionFlag: Int { get } ``` |
| To | ``` var errSecUnknownCriticalExtensionFlag: OSStatus { get } ``` |

Modified [errSecUnknownCRLExtension](https://developer.apple.com/documentation/security/errsecunknowncrlextension)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnknownCRLExtension: Int { get } ``` |
| To | ``` var errSecUnknownCRLExtension: OSStatus { get } ``` |

Modified [errSecUnknownFormat](https://developer.apple.com/documentation/security/errsecunknownformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnknownFormat: Int { get } ``` |
| To | ``` var errSecUnknownFormat: OSStatus { get } ``` |

Modified [errSecUnknownQualifiedCertStatement](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunknownqualifiedcertstatement)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnknownQualifiedCertStatement: Int { get } ``` |
| To | ``` var errSecUnknownQualifiedCertStatement: OSStatus { get } ``` |

Modified [errSecUnknownTag](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunknowntag)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnknownTag: Int { get } ``` |
| To | ``` var errSecUnknownTag: OSStatus { get } ``` |

Modified [errSecUnsupportedAddressType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedaddresstype)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedAddressType: Int { get } ``` |
| To | ``` var errSecUnsupportedAddressType: OSStatus { get } ``` |

Modified [errSecUnsupportedFieldFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedfieldformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedFieldFormat: Int { get } ``` |
| To | ``` var errSecUnsupportedFieldFormat: OSStatus { get } ``` |

Modified [errSecUnsupportedFormat](https://developer.apple.com/documentation/security/errsecunsupportedformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedFormat: Int { get } ``` |
| To | ``` var errSecUnsupportedFormat: OSStatus { get } ``` |

Modified [errSecUnsupportedIndexInfo](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedindexinfo)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedIndexInfo: Int { get } ``` |
| To | ``` var errSecUnsupportedIndexInfo: OSStatus { get } ``` |

Modified [errSecUnsupportedKeyAttributeMask](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedkeyattributemask)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedKeyAttributeMask: Int { get } ``` |
| To | ``` var errSecUnsupportedKeyAttributeMask: OSStatus { get } ``` |

Modified [errSecUnsupportedKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedkeyformat)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedKeyFormat: Int { get } ``` |
| To | ``` var errSecUnsupportedKeyFormat: OSStatus { get } ``` |

Modified [errSecUnsupportedKeyLabel](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedkeylabel)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedKeyLabel: Int { get } ``` |
| To | ``` var errSecUnsupportedKeyLabel: OSStatus { get } ``` |

Modified [errSecUnsupportedKeySize](https://developer.apple.com/documentation/security/errsecunsupportedkeysize)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedKeySize: Int { get } ``` |
| To | ``` var errSecUnsupportedKeySize: OSStatus { get } ``` |

Modified [errSecUnsupportedKeyUsageMask](https://developer.apple.com/documentation/security/errsecunsupportedkeyusagemask)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedKeyUsageMask: Int { get } ``` |
| To | ``` var errSecUnsupportedKeyUsageMask: OSStatus { get } ``` |

Modified [errSecUnsupportedLocality](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedlocality)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedLocality: Int { get } ``` |
| To | ``` var errSecUnsupportedLocality: OSStatus { get } ``` |

Modified [errSecUnsupportedNumAttributes](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportednumattributes)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedNumAttributes: Int { get } ``` |
| To | ``` var errSecUnsupportedNumAttributes: OSStatus { get } ``` |

Modified [errSecUnsupportedNumIndexes](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportednumindexes)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedNumIndexes: Int { get } ``` |
| To | ``` var errSecUnsupportedNumIndexes: OSStatus { get } ``` |

Modified [errSecUnsupportedNumRecordTypes](https://developer.apple.com/documentation/security/errsecunsupportednumrecordtypes)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedNumRecordTypes: Int { get } ``` |
| To | ``` var errSecUnsupportedNumRecordTypes: OSStatus { get } ``` |

Modified [errSecUnsupportedNumSelectionPreds](https://developer.apple.com/documentation/security/errsecunsupportednumselectionpreds)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedNumSelectionPreds: Int { get } ``` |
| To | ``` var errSecUnsupportedNumSelectionPreds: OSStatus { get } ``` |

Modified [errSecUnsupportedOperator](https://developer.apple.com/documentation/security/errsecunsupportedoperator)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedOperator: Int { get } ``` |
| To | ``` var errSecUnsupportedOperator: OSStatus { get } ``` |

Modified [errSecUnsupportedQueryLimits](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedquerylimits)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedQueryLimits: Int { get } ``` |
| To | ``` var errSecUnsupportedQueryLimits: OSStatus { get } ``` |

Modified [errSecUnsupportedService](https://developer.apple.com/documentation/security/errsecunsupportedservice)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedService: Int { get } ``` |
| To | ``` var errSecUnsupportedService: OSStatus { get } ``` |

Modified [errSecUnsupportedVectorOfBuffers](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedvectorofbuffers)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnsupportedVectorOfBuffers: Int { get } ``` |
| To | ``` var errSecUnsupportedVectorOfBuffers: OSStatus { get } ``` |

Modified [errSecUserCanceled](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecusercanceled)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUserCanceled: Int { get } ``` |
| To | ``` var errSecUserCanceled: OSStatus { get } ``` |

Modified [errSecVerificationFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecverificationfailure)

|  | Declaration |
| --- | --- |
| From | ``` var errSecVerificationFailure: Int { get } ``` |
| To | ``` var errSecVerificationFailure: OSStatus { get } ``` |

Modified [errSecVerifyActionFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecverifyactionfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecVerifyActionFailed: Int { get } ``` |
| To | ``` var errSecVerifyActionFailed: OSStatus { get } ``` |

Modified [errSecVerifyFailed](https://developer.apple.com/documentation/security/errsecverifyfailed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecVerifyFailed: Int { get } ``` |
| To | ``` var errSecVerifyFailed: OSStatus { get } ``` |

Modified [errSecWrongSecVersion](https://developer.apple.com/documentation/security/errsecwrongsecversion)

|  | Declaration |
| --- | --- |
| From | ``` var errSecWrongSecVersion: Int { get } ``` |
| To | ``` var errSecWrongSecVersion: OSStatus { get } ``` |

Modified [errSecWrPerm](https://developer.apple.com/documentation/security/errsecwrperm)

|  | Declaration |
| --- | --- |
| From | ``` var errSecWrPerm: Int { get } ``` |
| To | ``` var errSecWrPerm: OSStatus { get } ``` |

Modified [errSSLBadCert](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadcert)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLBadCert: Int { get } ``` |
| To | ``` var errSSLBadCert: OSStatus { get } ``` |

Modified [errSSLBadCipherSuite](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadciphersuite)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLBadCipherSuite: Int { get } ``` |
| To | ``` var errSSLBadCipherSuite: OSStatus { get } ``` |

Modified [errSSLBadConfiguration](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLBadConfiguration: Int { get } ``` |
| To | ``` var errSSLBadConfiguration: OSStatus { get } ``` |

Modified [errSSLBadRecordMac](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslbadrecordmac)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLBadRecordMac: Int { get } ``` |
| To | ``` var errSSLBadRecordMac: OSStatus { get } ``` |

Modified [errSSLBufferOverflow](https://developer.apple.com/documentation/security/errsslbufferoverflow)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLBufferOverflow: Int { get } ``` |
| To | ``` var errSSLBufferOverflow: OSStatus { get } ``` |

Modified [errSSLCertExpired](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslcertexpired)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLCertExpired: Int { get } ``` |
| To | ``` var errSSLCertExpired: OSStatus { get } ``` |

Modified [errSSLCertNotYetValid](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslcertnotyetvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLCertNotYetValid: Int { get } ``` |
| To | ``` var errSSLCertNotYetValid: OSStatus { get } ``` |

Modified [errSSLClientCertRequested](https://developer.apple.com/documentation/security/errsslclientcertrequested)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLClientCertRequested: Int { get } ``` |
| To | ``` var errSSLClientCertRequested: OSStatus { get } ``` |

Modified [errSSLClosedAbort](https://developer.apple.com/documentation/security/errsslclosedabort)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLClosedAbort: Int { get } ``` |
| To | ``` var errSSLClosedAbort: OSStatus { get } ``` |

Modified [errSSLClosedGraceful](https://developer.apple.com/documentation/security/errsslclosedgraceful)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLClosedGraceful: Int { get } ``` |
| To | ``` var errSSLClosedGraceful: OSStatus { get } ``` |

Modified [errSSLClosedNoNotify](https://developer.apple.com/documentation/security/errsslclosednonotify)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLClosedNoNotify: Int { get } ``` |
| To | ``` var errSSLClosedNoNotify: OSStatus { get } ``` |

Modified [errSSLConnectionRefused](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslconnectionrefused)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLConnectionRefused: Int { get } ``` |
| To | ``` var errSSLConnectionRefused: OSStatus { get } ``` |

Modified [errSSLCrypto](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslcrypto)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLCrypto: Int { get } ``` |
| To | ``` var errSSLCrypto: OSStatus { get } ``` |

Modified [errSSLDecryptionFail](https://developer.apple.com/documentation/security/errssldecryptionfail)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLDecryptionFail: Int { get } ``` |
| To | ``` var errSSLDecryptionFail: OSStatus { get } ``` |

Modified [errSSLFatalAlert](https://developer.apple.com/documentation/security/errsslfatalalert)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLFatalAlert: Int { get } ``` |
| To | ``` var errSSLFatalAlert: OSStatus { get } ``` |

Modified [errSSLHostNameMismatch](https://developer.apple.com/documentation/security/errsslhostnamemismatch)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLHostNameMismatch: Int { get } ``` |
| To | ``` var errSSLHostNameMismatch: OSStatus { get } ``` |

Modified [errSSLIllegalParam](https://developer.apple.com/documentation/security/errsslillegalparam)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLIllegalParam: Int { get } ``` |
| To | ``` var errSSLIllegalParam: OSStatus { get } ``` |

Modified [errSSLInternal](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslinternal)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLInternal: Int { get } ``` |
| To | ``` var errSSLInternal: OSStatus { get } ``` |

Modified [errSSLModuleAttach](https://developer.apple.com/documentation/security/errsslmoduleattach)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLModuleAttach: Int { get } ``` |
| To | ``` var errSSLModuleAttach: OSStatus { get } ``` |

Modified [errSSLNegotiation](https://developer.apple.com/documentation/security/errsslnegotiation)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLNegotiation: Int { get } ``` |
| To | ``` var errSSLNegotiation: OSStatus { get } ``` |

Modified [errSSLNoRootCert](https://developer.apple.com/documentation/security/errsslnorootcert)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLNoRootCert: Int { get } ``` |
| To | ``` var errSSLNoRootCert: OSStatus { get } ``` |

Modified [errSSLPeerAccessDenied](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeeraccessdenied)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerAccessDenied: Int { get } ``` |
| To | ``` var errSSLPeerAccessDenied: OSStatus { get } ``` |

Modified [errSSLPeerAuthCompleted](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerauthcompleted)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerAuthCompleted: Int { get } ``` |
| To | ``` var errSSLPeerAuthCompleted: OSStatus { get } ``` |

Modified [errSSLPeerBadCert](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerbadcert)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerBadCert: Int { get } ``` |
| To | ``` var errSSLPeerBadCert: OSStatus { get } ``` |

Modified [errSSLPeerBadRecordMac](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerbadrecordmac)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerBadRecordMac: Int { get } ``` |
| To | ``` var errSSLPeerBadRecordMac: OSStatus { get } ``` |

Modified [errSSLPeerCertExpired](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeercertexpired)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerCertExpired: Int { get } ``` |
| To | ``` var errSSLPeerCertExpired: OSStatus { get } ``` |

Modified [errSSLPeerCertRevoked](https://developer.apple.com/documentation/security/errsslpeercertrevoked)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerCertRevoked: Int { get } ``` |
| To | ``` var errSSLPeerCertRevoked: OSStatus { get } ``` |

Modified [errSSLPeerCertUnknown](https://developer.apple.com/documentation/security/errsslpeercertunknown)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerCertUnknown: Int { get } ``` |
| To | ``` var errSSLPeerCertUnknown: OSStatus { get } ``` |

Modified [errSSLPeerDecodeError](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecodeerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerDecodeError: Int { get } ``` |
| To | ``` var errSSLPeerDecodeError: OSStatus { get } ``` |

Modified [errSSLPeerDecompressFail](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecompressfail)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerDecompressFail: Int { get } ``` |
| To | ``` var errSSLPeerDecompressFail: OSStatus { get } ``` |

Modified [errSSLPeerDecryptError](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecrypterror)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerDecryptError: Int { get } ``` |
| To | ``` var errSSLPeerDecryptError: OSStatus { get } ``` |

Modified [errSSLPeerDecryptionFail](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerdecryptionfail)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerDecryptionFail: Int { get } ``` |
| To | ``` var errSSLPeerDecryptionFail: OSStatus { get } ``` |

Modified [errSSLPeerExportRestriction](https://developer.apple.com/documentation/security/errsslpeerexportrestriction)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerExportRestriction: Int { get } ``` |
| To | ``` var errSSLPeerExportRestriction: OSStatus { get } ``` |

Modified [errSSLPeerHandshakeFail](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerhandshakefail)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerHandshakeFail: Int { get } ``` |
| To | ``` var errSSLPeerHandshakeFail: OSStatus { get } ``` |

Modified [errSSLPeerInsufficientSecurity](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerinsufficientsecurity)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerInsufficientSecurity: Int { get } ``` |
| To | ``` var errSSLPeerInsufficientSecurity: OSStatus { get } ``` |

Modified [errSSLPeerInternalError](https://developer.apple.com/documentation/security/errsslpeerinternalerror)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerInternalError: Int { get } ``` |
| To | ``` var errSSLPeerInternalError: OSStatus { get } ``` |

Modified [errSSLPeerNoRenegotiation](https://developer.apple.com/documentation/security/errsslpeernorenegotiation)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerNoRenegotiation: Int { get } ``` |
| To | ``` var errSSLPeerNoRenegotiation: OSStatus { get } ``` |

Modified [errSSLPeerProtocolVersion](https://developer.apple.com/documentation/security/errsslpeerprotocolversion)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerProtocolVersion: Int { get } ``` |
| To | ``` var errSSLPeerProtocolVersion: OSStatus { get } ``` |

Modified [errSSLPeerRecordOverflow](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerrecordoverflow)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerRecordOverflow: Int { get } ``` |
| To | ``` var errSSLPeerRecordOverflow: OSStatus { get } ``` |

Modified [errSSLPeerUnexpectedMsg](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerunexpectedmsg)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerUnexpectedMsg: Int { get } ``` |
| To | ``` var errSSLPeerUnexpectedMsg: OSStatus { get } ``` |

Modified [errSSLPeerUnknownCA](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerunknownca)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerUnknownCA: Int { get } ``` |
| To | ``` var errSSLPeerUnknownCA: OSStatus { get } ``` |

Modified [errSSLPeerUnsupportedCert](https://developer.apple.com/documentation/security/errsslpeerunsupportedcert)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerUnsupportedCert: Int { get } ``` |
| To | ``` var errSSLPeerUnsupportedCert: OSStatus { get } ``` |

Modified [errSSLPeerUserCancelled](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerusercancelled)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLPeerUserCancelled: Int { get } ``` |
| To | ``` var errSSLPeerUserCancelled: OSStatus { get } ``` |

Modified [errSSLProtocol](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslprotocol)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLProtocol: Int { get } ``` |
| To | ``` var errSSLProtocol: OSStatus { get } ``` |

Modified [errSSLRecordOverflow](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslrecordoverflow)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLRecordOverflow: Int { get } ``` |
| To | ``` var errSSLRecordOverflow: OSStatus { get } ``` |

Modified [errSSLSessionNotFound](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslsessionnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLSessionNotFound: Int { get } ``` |
| To | ``` var errSSLSessionNotFound: OSStatus { get } ``` |

Modified [errSSLUnexpectedRecord](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslunexpectedrecord)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLUnexpectedRecord: Int { get } ``` |
| To | ``` var errSSLUnexpectedRecord: OSStatus { get } ``` |

Modified [errSSLUnknownRootCert](https://developer.apple.com/documentation/security/errsslunknownrootcert)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLUnknownRootCert: Int { get } ``` |
| To | ``` var errSSLUnknownRootCert: OSStatus { get } ``` |

Modified [errSSLWouldBlock](https://developer.apple.com/documentation/security/errsslwouldblock)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLWouldBlock: Int { get } ``` |
| To | ``` var errSSLWouldBlock: OSStatus { get } ``` |

Modified [errSSLXCertChainInvalid](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslxcertchaininvalid)

|  | Declaration |
| --- | --- |
| From | ``` var errSSLXCertChainInvalid: Int { get } ``` |
| To | ``` var errSSLXCertChainInvalid: OSStatus { get } ``` |

Modified [kSecACLAuthorizationAny](https://developer.apple.com/documentation/security/ksecaclauthorizationany)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationAny: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationAny: CFString ``` |

Modified [kSecACLAuthorizationChangeACL](https://developer.apple.com/documentation/security/ksecaclauthorizationchangeacl)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationChangeACL: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationChangeACL: CFString ``` |

Modified [kSecACLAuthorizationChangeOwner](https://developer.apple.com/documentation/security/ksecaclauthorizationchangeowner)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationChangeOwner: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationChangeOwner: CFString ``` |

Modified [kSecACLAuthorizationDecrypt](https://developer.apple.com/documentation/security/ksecaclauthorizationdecrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationDecrypt: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationDecrypt: CFString ``` |

Modified [kSecACLAuthorizationDelete](https://developer.apple.com/documentation/security/ksecaclauthorizationdelete)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationDelete: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationDelete: CFString ``` |

Modified [kSecACLAuthorizationDerive](https://developer.apple.com/documentation/security/ksecaclauthorizationderive)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationDerive: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationDerive: CFString ``` |

Modified [kSecACLAuthorizationEncrypt](https://developer.apple.com/documentation/security/ksecaclauthorizationencrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationEncrypt: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationEncrypt: CFString ``` |

Modified [kSecACLAuthorizationExportClear](https://developer.apple.com/documentation/security/ksecaclauthorizationexportclear)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationExportClear: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationExportClear: CFString ``` |

Modified [kSecACLAuthorizationExportWrapped](https://developer.apple.com/documentation/security/ksecaclauthorizationexportwrapped)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationExportWrapped: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationExportWrapped: CFString ``` |

Modified [kSecACLAuthorizationGenKey](https://developer.apple.com/documentation/security/ksecaclauthorizationgenkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationGenKey: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationGenKey: CFString ``` |

Modified [kSecACLAuthorizationImportClear](https://developer.apple.com/documentation/security/ksecaclauthorizationimportclear)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationImportClear: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationImportClear: CFString ``` |

Modified [kSecACLAuthorizationImportWrapped](https://developer.apple.com/documentation/security/ksecaclauthorizationimportwrapped)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationImportWrapped: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationImportWrapped: CFString ``` |

Modified [kSecACLAuthorizationKeychainCreate](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychaincreate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationKeychainCreate: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationKeychainCreate: CFString ``` |

Modified [kSecACLAuthorizationKeychainDelete](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychaindelete)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationKeychainDelete: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationKeychainDelete: CFString ``` |

Modified [kSecACLAuthorizationKeychainItemDelete](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainitemdelete)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationKeychainItemDelete: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationKeychainItemDelete: CFString ``` |

Modified [kSecACLAuthorizationKeychainItemInsert](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainiteminsert)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationKeychainItemInsert: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationKeychainItemInsert: CFString ``` |

Modified [kSecACLAuthorizationKeychainItemModify](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainitemmodify)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationKeychainItemModify: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationKeychainItemModify: CFString ``` |

Modified [kSecACLAuthorizationKeychainItemRead](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainitemread)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationKeychainItemRead: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationKeychainItemRead: CFString ``` |

Modified [kSecACLAuthorizationLogin](https://developer.apple.com/documentation/security/ksecaclauthorizationlogin)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationLogin: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationLogin: CFString ``` |

Modified [kSecACLAuthorizationMAC](https://developer.apple.com/documentation/security/ksecaclauthorizationmac)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationMAC: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationMAC: CFString ``` |

Modified [kSecACLAuthorizationSign](https://developer.apple.com/documentation/security/ksecaclauthorizationsign)

|  | Declaration |
| --- | --- |
| From | ``` var kSecACLAuthorizationSign: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecACLAuthorizationSign: CFString ``` |

Modified [kSecAttrAccess](https://developer.apple.com/documentation/security/ksecattraccess)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccess: CFStringRef ``` |
| To | ``` let kSecAttrAccess: CFString ``` |

Modified [kSecAttrAccessControl](https://developer.apple.com/documentation/security/ksecattraccesscontrol)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessControl: CFStringRef ``` |
| To | ``` let kSecAttrAccessControl: CFString ``` |

Modified [kSecAttrAccessGroup](https://developer.apple.com/documentation/security/ksecattraccessgroup)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessGroup: CFStringRef ``` |
| To | ``` let kSecAttrAccessGroup: CFString ``` |

Modified [kSecAttrAccessible](https://developer.apple.com/documentation/security/ksecattraccessible)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessible: CFStringRef ``` |
| To | ``` let kSecAttrAccessible: CFString ``` |

Modified [kSecAttrAccessibleAfterFirstUnlock](https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlock)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessibleAfterFirstUnlock: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAfterFirstUnlock: CFString ``` |

Modified [kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccessibleAlways](https://developer.apple.com/documentation/security/ksecattraccessiblealways)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessibleAlways: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAlways: CFString ``` |

Modified [kSecAttrAccessibleAlwaysThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblealwaysthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessibleAlwaysThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAlwaysThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccessibleWhenUnlocked](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlocked)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessibleWhenUnlocked: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleWhenUnlocked: CFString ``` |

Modified [kSecAttrAccessibleWhenUnlockedThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccount](https://developer.apple.com/documentation/security/ksecattraccount)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAccount: CFStringRef ``` |
| To | ``` let kSecAttrAccount: CFString ``` |

Modified [kSecAttrApplicationLabel](https://developer.apple.com/documentation/security/ksecattrapplicationlabel)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrApplicationLabel: CFStringRef ``` |
| To | ``` let kSecAttrApplicationLabel: CFString ``` |

Modified [kSecAttrApplicationTag](https://developer.apple.com/documentation/security/ksecattrapplicationtag)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrApplicationTag: CFStringRef ``` |
| To | ``` let kSecAttrApplicationTag: CFString ``` |

Modified [kSecAttrAuthenticationType](https://developer.apple.com/documentation/security/ksecattrauthenticationtype)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationType: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationType: CFString ``` |

Modified [kSecAttrAuthenticationTypeDefault](https://developer.apple.com/documentation/security/ksecattrauthenticationtypedefault)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeDefault: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeDefault: CFString ``` |

Modified [kSecAttrAuthenticationTypeDPA](https://developer.apple.com/documentation/security/ksecattrauthenticationtypedpa)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeDPA: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeDPA: CFString ``` |

Modified [kSecAttrAuthenticationTypeHTMLForm](https://developer.apple.com/documentation/security/ksecattrauthenticationtypehtmlform)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeHTMLForm: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeHTMLForm: CFString ``` |

Modified [kSecAttrAuthenticationTypeHTTPBasic](https://developer.apple.com/documentation/security/ksecattrauthenticationtypehttpbasic)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeHTTPBasic: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeHTTPBasic: CFString ``` |

Modified [kSecAttrAuthenticationTypeHTTPDigest](https://developer.apple.com/documentation/security/ksecattrauthenticationtypehttpdigest)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeHTTPDigest: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeHTTPDigest: CFString ``` |

Modified [kSecAttrAuthenticationTypeMSN](https://developer.apple.com/documentation/security/ksecattrauthenticationtypemsn)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeMSN: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeMSN: CFString ``` |

Modified [kSecAttrAuthenticationTypeNTLM](https://developer.apple.com/documentation/security/ksecattrauthenticationtypentlm)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeNTLM: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeNTLM: CFString ``` |

Modified [kSecAttrAuthenticationTypeRPA](https://developer.apple.com/documentation/security/ksecattrauthenticationtyperpa)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrAuthenticationTypeRPA: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeRPA: CFString ``` |

Modified [kSecAttrCanDecrypt](https://developer.apple.com/documentation/security/ksecattrcandecrypt)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanDecrypt: CFStringRef ``` |
| To | ``` let kSecAttrCanDecrypt: CFString ``` |

Modified [kSecAttrCanDerive](https://developer.apple.com/documentation/security/ksecattrcanderive)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanDerive: CFStringRef ``` |
| To | ``` let kSecAttrCanDerive: CFString ``` |

Modified [kSecAttrCanEncrypt](https://developer.apple.com/documentation/security/ksecattrcanencrypt)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanEncrypt: CFStringRef ``` |
| To | ``` let kSecAttrCanEncrypt: CFString ``` |

Modified [kSecAttrCanSign](https://developer.apple.com/documentation/security/ksecattrcansign)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanSign: CFStringRef ``` |
| To | ``` let kSecAttrCanSign: CFString ``` |

Modified [kSecAttrCanUnwrap](https://developer.apple.com/documentation/security/ksecattrcanunwrap)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanUnwrap: CFStringRef ``` |
| To | ``` let kSecAttrCanUnwrap: CFString ``` |

Modified [kSecAttrCanVerify](https://developer.apple.com/documentation/security/ksecattrcanverify)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanVerify: CFStringRef ``` |
| To | ``` let kSecAttrCanVerify: CFString ``` |

Modified [kSecAttrCanWrap](https://developer.apple.com/documentation/security/ksecattrcanwrap)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCanWrap: CFStringRef ``` |
| To | ``` let kSecAttrCanWrap: CFString ``` |

Modified [kSecAttrCertificateEncoding](https://developer.apple.com/documentation/security/ksecattrcertificateencoding)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCertificateEncoding: CFStringRef ``` |
| To | ``` let kSecAttrCertificateEncoding: CFString ``` |

Modified [kSecAttrCertificateType](https://developer.apple.com/documentation/security/ksecattrcertificatetype)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCertificateType: CFStringRef ``` |
| To | ``` let kSecAttrCertificateType: CFString ``` |

Modified [kSecAttrComment](https://developer.apple.com/documentation/security/ksecattrcomment)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrComment: CFStringRef ``` |
| To | ``` let kSecAttrComment: CFString ``` |

Modified [kSecAttrCreationDate](https://developer.apple.com/documentation/security/ksecattrcreationdate)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCreationDate: CFStringRef ``` |
| To | ``` let kSecAttrCreationDate: CFString ``` |

Modified [kSecAttrCreator](https://developer.apple.com/documentation/security/ksecattrcreator)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrCreator: CFStringRef ``` |
| To | ``` let kSecAttrCreator: CFString ``` |

Modified [kSecAttrDescription](https://developer.apple.com/documentation/security/ksecattrdescription)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrDescription: CFStringRef ``` |
| To | ``` let kSecAttrDescription: CFString ``` |

Modified [kSecAttrEffectiveKeySize](https://developer.apple.com/documentation/security/ksecattreffectivekeysize)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrEffectiveKeySize: CFStringRef ``` |
| To | ``` let kSecAttrEffectiveKeySize: CFString ``` |

Modified [kSecAttrGeneric](https://developer.apple.com/documentation/security/ksecattrgeneric)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrGeneric: CFStringRef ``` |
| To | ``` let kSecAttrGeneric: CFString ``` |

Modified [kSecAttrIsExtractable](https://developer.apple.com/documentation/security/ksecattrisextractable)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrIsExtractable: CFStringRef ``` |
| To | ``` let kSecAttrIsExtractable: CFString ``` |

Modified [kSecAttrIsInvisible](https://developer.apple.com/documentation/security/ksecattrisinvisible)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrIsInvisible: CFStringRef ``` |
| To | ``` let kSecAttrIsInvisible: CFString ``` |

Modified [kSecAttrIsNegative](https://developer.apple.com/documentation/security/ksecattrisnegative)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrIsNegative: CFStringRef ``` |
| To | ``` let kSecAttrIsNegative: CFString ``` |

Modified [kSecAttrIsPermanent](https://developer.apple.com/documentation/security/ksecattrispermanent)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrIsPermanent: CFStringRef ``` |
| To | ``` let kSecAttrIsPermanent: CFString ``` |

Modified [kSecAttrIsSensitive](https://developer.apple.com/documentation/security/ksecattrissensitive)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrIsSensitive: CFStringRef ``` |
| To | ``` let kSecAttrIsSensitive: CFString ``` |

Modified [kSecAttrIssuer](https://developer.apple.com/documentation/security/ksecattrissuer)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrIssuer: CFStringRef ``` |
| To | ``` let kSecAttrIssuer: CFString ``` |

Modified [kSecAttrKeyClass](https://developer.apple.com/documentation/security/ksecattrkeyclass)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyClass: CFStringRef ``` |
| To | ``` let kSecAttrKeyClass: CFString ``` |

Modified [kSecAttrKeyClassPrivate](https://developer.apple.com/documentation/security/ksecattrkeyclassprivate)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyClassPrivate: CFStringRef ``` |
| To | ``` let kSecAttrKeyClassPrivate: CFString ``` |

Modified [kSecAttrKeyClassPublic](https://developer.apple.com/documentation/security/ksecattrkeyclasspublic)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyClassPublic: CFStringRef ``` |
| To | ``` let kSecAttrKeyClassPublic: CFString ``` |

Modified [kSecAttrKeyClassSymmetric](https://developer.apple.com/documentation/security/ksecattrkeyclasssymmetric)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyClassSymmetric: CFStringRef ``` |
| To | ``` let kSecAttrKeyClassSymmetric: CFString ``` |

Modified [kSecAttrKeySizeInBits](https://developer.apple.com/documentation/security/ksecattrkeysizeinbits)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeySizeInBits: CFStringRef ``` |
| To | ``` let kSecAttrKeySizeInBits: CFString ``` |

Modified [kSecAttrKeyType](https://developer.apple.com/documentation/security/ksecattrkeytype)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyType: CFStringRef ``` |
| To | ``` let kSecAttrKeyType: CFString ``` |

Modified [kSecAttrKeyType3DES](https://developer.apple.com/documentation/security/ksecattrkeytype3des)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyType3DES: CFStringRef ``` |
| To | ``` let kSecAttrKeyType3DES: CFString ``` |

Modified [kSecAttrKeyTypeAES](https://developer.apple.com/documentation/security/ksecattrkeytypeaes)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeAES: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeAES: CFString ``` |

Modified [kSecAttrKeyTypeCAST](https://developer.apple.com/documentation/security/ksecattrkeytypecast)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeCAST: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeCAST: CFString ``` |

Modified [kSecAttrKeyTypeDES](https://developer.apple.com/documentation/security/ksecattrkeytypedes)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeDES: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeDES: CFString ``` |

Modified [kSecAttrKeyTypeDSA](https://developer.apple.com/documentation/security/ksecattrkeytypedsa)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeDSA: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeDSA: CFString ``` |

Modified [kSecAttrKeyTypeEC](https://developer.apple.com/documentation/security/ksecattrkeytypeec)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeEC: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeEC: CFString ``` |

Modified [kSecAttrKeyTypeECDSA](https://developer.apple.com/documentation/security/ksecattrkeytypeecdsa)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeECDSA: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeECDSA: CFString ``` |

Modified [kSecAttrKeyTypeRC2](https://developer.apple.com/documentation/security/ksecattrkeytyperc2)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeRC2: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeRC2: CFString ``` |

Modified [kSecAttrKeyTypeRC4](https://developer.apple.com/documentation/security/ksecattrkeytyperc4)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeRC4: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeRC4: CFString ``` |

Modified [kSecAttrKeyTypeRSA](https://developer.apple.com/documentation/security/ksecattrkeytypersa)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrKeyTypeRSA: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeRSA: CFString ``` |

Modified [kSecAttrLabel](https://developer.apple.com/documentation/security/ksecattrlabel)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrLabel: CFStringRef ``` |
| To | ``` let kSecAttrLabel: CFString ``` |

Modified [kSecAttrModificationDate](https://developer.apple.com/documentation/security/ksecattrmodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrModificationDate: CFStringRef ``` |
| To | ``` let kSecAttrModificationDate: CFString ``` |

Modified [kSecAttrPath](https://developer.apple.com/documentation/security/ksecattrpath)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPath: CFStringRef ``` |
| To | ``` let kSecAttrPath: CFString ``` |

Modified [kSecAttrPort](https://developer.apple.com/documentation/security/ksecattrport)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPort: CFStringRef ``` |
| To | ``` let kSecAttrPort: CFString ``` |

Modified [kSecAttrPRF](https://developer.apple.com/documentation/security/ksecattrprf)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPRF: CFStringRef ``` |
| To | ``` let kSecAttrPRF: CFString ``` |

Modified [kSecAttrPRFHmacAlgSHA1](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha1)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA1: CFStringRef ``` |
| To | ``` let kSecAttrPRFHmacAlgSHA1: CFString ``` |

Modified [kSecAttrPRFHmacAlgSHA224](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha224)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA224: CFStringRef ``` |
| To | ``` let kSecAttrPRFHmacAlgSHA224: CFString ``` |

Modified [kSecAttrPRFHmacAlgSHA256](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha256)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA256: CFStringRef ``` |
| To | ``` let kSecAttrPRFHmacAlgSHA256: CFString ``` |

Modified [kSecAttrPRFHmacAlgSHA384](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha384)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA384: CFStringRef ``` |
| To | ``` let kSecAttrPRFHmacAlgSHA384: CFString ``` |

Modified [kSecAttrPRFHmacAlgSHA512](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha512)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA512: CFStringRef ``` |
| To | ``` let kSecAttrPRFHmacAlgSHA512: CFString ``` |

Modified [kSecAttrProtocol](https://developer.apple.com/documentation/security/ksecattrprotocol)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocol: CFStringRef ``` |
| To | ``` let kSecAttrProtocol: CFString ``` |

Modified [kSecAttrProtocolAFP](https://developer.apple.com/documentation/security/ksecattrprotocolafp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolAFP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolAFP: CFString ``` |

Modified [kSecAttrProtocolAppleTalk](https://developer.apple.com/documentation/security/ksecattrprotocolappletalk)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolAppleTalk: CFStringRef ``` |
| To | ``` let kSecAttrProtocolAppleTalk: CFString ``` |

Modified [kSecAttrProtocolDAAP](https://developer.apple.com/documentation/security/ksecattrprotocoldaap)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolDAAP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolDAAP: CFString ``` |

Modified [kSecAttrProtocolEPPC](https://developer.apple.com/documentation/security/ksecattrprotocoleppc)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolEPPC: CFStringRef ``` |
| To | ``` let kSecAttrProtocolEPPC: CFString ``` |

Modified [kSecAttrProtocolFTP](https://developer.apple.com/documentation/security/ksecattrprotocolftp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolFTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTP: CFString ``` |

Modified [kSecAttrProtocolFTPAccount](https://developer.apple.com/documentation/security/ksecattrprotocolftpaccount)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolFTPAccount: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTPAccount: CFString ``` |

Modified [kSecAttrProtocolFTPProxy](https://developer.apple.com/documentation/security/ksecattrprotocolftpproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolFTPProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTPProxy: CFString ``` |

Modified [kSecAttrProtocolFTPS](https://developer.apple.com/documentation/security/ksecattrprotocolftps)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolFTPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTPS: CFString ``` |

Modified [kSecAttrProtocolHTTP](https://developer.apple.com/documentation/security/ksecattrprotocolhttp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolHTTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTP: CFString ``` |

Modified [kSecAttrProtocolHTTPProxy](https://developer.apple.com/documentation/security/ksecattrprotocolhttpproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolHTTPProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTPProxy: CFString ``` |

Modified [kSecAttrProtocolHTTPS](https://developer.apple.com/documentation/security/ksecattrprotocolhttps)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolHTTPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTPS: CFString ``` |

Modified [kSecAttrProtocolHTTPSProxy](https://developer.apple.com/documentation/security/ksecattrprotocolhttpsproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolHTTPSProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTPSProxy: CFString ``` |

Modified [kSecAttrProtocolIMAP](https://developer.apple.com/documentation/security/ksecattrprotocolimap)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolIMAP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIMAP: CFString ``` |

Modified [kSecAttrProtocolIMAPS](https://developer.apple.com/documentation/security/ksecattrprotocolimaps)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolIMAPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIMAPS: CFString ``` |

Modified [kSecAttrProtocolIPP](https://developer.apple.com/documentation/security/ksecattrprotocolipp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolIPP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIPP: CFString ``` |

Modified [kSecAttrProtocolIRC](https://developer.apple.com/documentation/security/ksecattrprotocolirc)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolIRC: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIRC: CFString ``` |

Modified [kSecAttrProtocolIRCS](https://developer.apple.com/documentation/security/ksecattrprotocolircs)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolIRCS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIRCS: CFString ``` |

Modified [kSecAttrProtocolLDAP](https://developer.apple.com/documentation/security/ksecattrprotocolldap)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolLDAP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolLDAP: CFString ``` |

Modified [kSecAttrProtocolLDAPS](https://developer.apple.com/documentation/security/ksecattrprotocolldaps)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolLDAPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolLDAPS: CFString ``` |

Modified [kSecAttrProtocolNNTP](https://developer.apple.com/documentation/security/ksecattrprotocolnntp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolNNTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolNNTP: CFString ``` |

Modified [kSecAttrProtocolNNTPS](https://developer.apple.com/documentation/security/ksecattrprotocolnntps)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolNNTPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolNNTPS: CFString ``` |

Modified [kSecAttrProtocolPOP3](https://developer.apple.com/documentation/security/ksecattrprotocolpop3)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolPOP3: CFStringRef ``` |
| To | ``` let kSecAttrProtocolPOP3: CFString ``` |

Modified [kSecAttrProtocolPOP3S](https://developer.apple.com/documentation/security/ksecattrprotocolpop3s)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolPOP3S: CFStringRef ``` |
| To | ``` let kSecAttrProtocolPOP3S: CFString ``` |

Modified [kSecAttrProtocolRTSP](https://developer.apple.com/documentation/security/ksecattrprotocolrtsp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolRTSP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolRTSP: CFString ``` |

Modified [kSecAttrProtocolRTSPProxy](https://developer.apple.com/documentation/security/ksecattrprotocolrtspproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolRTSPProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolRTSPProxy: CFString ``` |

Modified [kSecAttrProtocolSMB](https://developer.apple.com/documentation/security/ksecattrprotocolsmb)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolSMB: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSMB: CFString ``` |

Modified [kSecAttrProtocolSMTP](https://developer.apple.com/documentation/security/ksecattrprotocolsmtp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolSMTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSMTP: CFString ``` |

Modified [kSecAttrProtocolSOCKS](https://developer.apple.com/documentation/security/ksecattrprotocolsocks)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolSOCKS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSOCKS: CFString ``` |

Modified [kSecAttrProtocolSSH](https://developer.apple.com/documentation/security/ksecattrprotocolssh)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolSSH: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSSH: CFString ``` |

Modified [kSecAttrProtocolTelnet](https://developer.apple.com/documentation/security/ksecattrprotocoltelnet)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolTelnet: CFStringRef ``` |
| To | ``` let kSecAttrProtocolTelnet: CFString ``` |

Modified [kSecAttrProtocolTelnetS](https://developer.apple.com/documentation/security/ksecattrprotocoltelnets)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrProtocolTelnetS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolTelnetS: CFString ``` |

Modified [kSecAttrPublicKeyHash](https://developer.apple.com/documentation/security/ksecattrpublickeyhash)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrPublicKeyHash: CFStringRef ``` |
| To | ``` let kSecAttrPublicKeyHash: CFString ``` |

Modified [kSecAttrRounds](https://developer.apple.com/documentation/security/ksecattrrounds)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrRounds: CFStringRef ``` |
| To | ``` let kSecAttrRounds: CFString ``` |

Modified [kSecAttrSalt](https://developer.apple.com/documentation/security/ksecattrsalt)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSalt: CFStringRef ``` |
| To | ``` let kSecAttrSalt: CFString ``` |

Modified [kSecAttrSecurityDomain](https://developer.apple.com/documentation/security/ksecattrsecuritydomain)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSecurityDomain: CFStringRef ``` |
| To | ``` let kSecAttrSecurityDomain: CFString ``` |

Modified [kSecAttrSerialNumber](https://developer.apple.com/documentation/security/ksecattrserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSerialNumber: CFStringRef ``` |
| To | ``` let kSecAttrSerialNumber: CFString ``` |

Modified [kSecAttrServer](https://developer.apple.com/documentation/security/ksecattrserver)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrServer: CFStringRef ``` |
| To | ``` let kSecAttrServer: CFString ``` |

Modified [kSecAttrService](https://developer.apple.com/documentation/security/ksecattrservice)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrService: CFStringRef ``` |
| To | ``` let kSecAttrService: CFString ``` |

Modified [kSecAttrSubject](https://developer.apple.com/documentation/security/ksecattrsubject)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSubject: CFStringRef ``` |
| To | ``` let kSecAttrSubject: CFString ``` |

Modified [kSecAttrSubjectKeyID](https://developer.apple.com/documentation/security/ksecattrsubjectkeyid)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSubjectKeyID: CFStringRef ``` |
| To | ``` let kSecAttrSubjectKeyID: CFString ``` |

Modified [kSecAttrSynchronizable](https://developer.apple.com/documentation/security/ksecattrsynchronizable)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSynchronizable: CFStringRef ``` |
| To | ``` let kSecAttrSynchronizable: CFString ``` |

Modified [kSecAttrSynchronizableAny](https://developer.apple.com/documentation/security/ksecattrsynchronizableany)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrSynchronizableAny: CFStringRef ``` |
| To | ``` let kSecAttrSynchronizableAny: CFString ``` |

Modified [kSecAttrType](https://developer.apple.com/documentation/security/ksecattrtype)

|  | Declaration |
| --- | --- |
| From | ``` let kSecAttrType: CFStringRef ``` |
| To | ``` let kSecAttrType: CFString ``` |

Modified [kSecBase32Encoding](https://developer.apple.com/documentation/security/ksecbase32encoding)

|  | Declaration |
| --- | --- |
| From | ``` let kSecBase32Encoding: CFString! ``` |
| To | ``` let kSecBase32Encoding: CFString ``` |

Modified [kSecBase64Encoding](https://developer.apple.com/documentation/security/ksecbase64encoding)

|  | Declaration |
| --- | --- |
| From | ``` let kSecBase64Encoding: CFString! ``` |
| To | ``` let kSecBase64Encoding: CFString ``` |

Modified kSecCertificateUsageDeriveAndSign

|  | Declaration |
| --- | --- |
| From | ``` let kSecCertificateUsageDeriveAndSign: CFString! ``` |
| To | ``` let kSecCertificateUsageDeriveAndSign: CFString ``` |

Modified kSecCertificateUsageSigning

|  | Declaration |
| --- | --- |
| From | ``` let kSecCertificateUsageSigning: CFString! ``` |
| To | ``` let kSecCertificateUsageSigning: CFString ``` |

Modified kSecCertificateUsageSigningAndEncrypting

|  | Declaration |
| --- | --- |
| From | ``` let kSecCertificateUsageSigningAndEncrypting: CFString! ``` |
| To | ``` let kSecCertificateUsageSigningAndEncrypting: CFString ``` |

Modified [kSecCFErrorArchitecture](https://developer.apple.com/documentation/security/kseccferrorarchitecture)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorArchitecture: CFString! ``` |
| To | ``` let kSecCFErrorArchitecture: CFString ``` |

Modified [kSecCFErrorGuestAttributes](https://developer.apple.com/documentation/security/kseccferrorguestattributes)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorGuestAttributes: CFString! ``` |
| To | ``` let kSecCFErrorGuestAttributes: CFString ``` |

Modified [kSecCFErrorInfoPlist](https://developer.apple.com/documentation/security/kseccferrorinfoplist)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorInfoPlist: CFString! ``` |
| To | ``` let kSecCFErrorInfoPlist: CFString ``` |

Modified [kSecCFErrorPath](https://developer.apple.com/documentation/security/kseccferrorpath)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorPath: CFString! ``` |
| To | ``` let kSecCFErrorPath: CFString ``` |

Modified [kSecCFErrorPattern](https://developer.apple.com/documentation/security/kseccferrorpattern)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorPattern: CFString! ``` |
| To | ``` let kSecCFErrorPattern: CFString ``` |

Modified [kSecCFErrorRequirementSyntax](https://developer.apple.com/documentation/security/kseccferrorrequirementsyntax)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorRequirementSyntax: CFString! ``` |
| To | ``` let kSecCFErrorRequirementSyntax: CFString ``` |

Modified [kSecCFErrorResourceAdded](https://developer.apple.com/documentation/security/kseccferrorresourceadded)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorResourceAdded: CFString! ``` |
| To | ``` let kSecCFErrorResourceAdded: CFString ``` |

Modified [kSecCFErrorResourceAltered](https://developer.apple.com/documentation/security/kseccferrorresourcealtered)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorResourceAltered: CFString! ``` |
| To | ``` let kSecCFErrorResourceAltered: CFString ``` |

Modified [kSecCFErrorResourceMissing](https://developer.apple.com/documentation/security/kseccferrorresourcemissing)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorResourceMissing: CFString! ``` |
| To | ``` let kSecCFErrorResourceMissing: CFString ``` |

Modified [kSecCFErrorResourceSeal](https://developer.apple.com/documentation/security/kseccferrorresourceseal)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCFErrorResourceSeal: CFString! ``` |
| To | ``` let kSecCFErrorResourceSeal: CFString ``` |

Modified [kSecClass](https://developer.apple.com/documentation/security/ksecclass)

|  | Declaration |
| --- | --- |
| From | ``` let kSecClass: CFStringRef ``` |
| To | ``` let kSecClass: CFString ``` |

Modified [kSecClassCertificate](https://developer.apple.com/documentation/security/ksecclasscertificate)

|  | Declaration |
| --- | --- |
| From | ``` let kSecClassCertificate: CFStringRef ``` |
| To | ``` let kSecClassCertificate: CFString ``` |

Modified [kSecClassGenericPassword](https://developer.apple.com/documentation/security/ksecclassgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kSecClassGenericPassword: CFStringRef ``` |
| To | ``` let kSecClassGenericPassword: CFString ``` |

Modified [kSecClassIdentity](https://developer.apple.com/documentation/security/ksecclassidentity)

|  | Declaration |
| --- | --- |
| From | ``` let kSecClassIdentity: CFStringRef ``` |
| To | ``` let kSecClassIdentity: CFString ``` |

Modified [kSecClassInternetPassword](https://developer.apple.com/documentation/security/ksecclassinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kSecClassInternetPassword: CFStringRef ``` |
| To | ``` let kSecClassInternetPassword: CFString ``` |

Modified [kSecClassKey](https://developer.apple.com/documentation/security/ksecclasskey)

|  | Declaration |
| --- | --- |
| From | ``` let kSecClassKey: CFStringRef ``` |
| To | ``` let kSecClassKey: CFString ``` |

Modified [kSecCodeAttributeArchitecture](https://developer.apple.com/documentation/security/kseccodeattributearchitecture)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeAttributeArchitecture: CFString! ``` |
| To | ``` let kSecCodeAttributeArchitecture: CFString ``` |

Modified [kSecCodeAttributeBundleVersion](https://developer.apple.com/documentation/security/kseccodeattributebundleversion)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeAttributeBundleVersion: CFString! ``` |
| To | ``` let kSecCodeAttributeBundleVersion: CFString ``` |

Modified [kSecCodeAttributeSubarchitecture](https://developer.apple.com/documentation/security/kseccodeattributesubarchitecture)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeAttributeSubarchitecture: CFString! ``` |
| To | ``` let kSecCodeAttributeSubarchitecture: CFString ``` |

Modified [kSecCodeAttributeUniversalFileOffset](https://developer.apple.com/documentation/security/kseccodeattributeuniversalfileoffset)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeAttributeUniversalFileOffset: CFString! ``` |
| To | ``` let kSecCodeAttributeUniversalFileOffset: CFString ``` |

Modified [kSecCodeInfoCertificates](https://developer.apple.com/documentation/security/kseccodeinfocertificates)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoCertificates: CFString! ``` |
| To | ``` let kSecCodeInfoCertificates: CFString ``` |

Modified [kSecCodeInfoChangedFiles](https://developer.apple.com/documentation/security/kseccodeinfochangedfiles)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoChangedFiles: CFString! ``` |
| To | ``` let kSecCodeInfoChangedFiles: CFString ``` |

Modified [kSecCodeInfoCMS](https://developer.apple.com/documentation/security/kseccodeinfocms)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoCMS: CFString! ``` |
| To | ``` let kSecCodeInfoCMS: CFString ``` |

Modified [kSecCodeInfoDesignatedRequirement](https://developer.apple.com/documentation/security/kseccodeinfodesignatedrequirement)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoDesignatedRequirement: CFString! ``` |
| To | ``` let kSecCodeInfoDesignatedRequirement: CFString ``` |

Modified [kSecCodeInfoDigestAlgorithm](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoDigestAlgorithm: CFString! ``` |
| To | ``` let kSecCodeInfoDigestAlgorithm: CFString ``` |

Modified [kSecCodeInfoEntitlements](https://developer.apple.com/documentation/security/kseccodeinfoentitlements)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoEntitlements: CFString! ``` |
| To | ``` let kSecCodeInfoEntitlements: CFString ``` |

Modified [kSecCodeInfoEntitlementsDict](https://developer.apple.com/documentation/security/kseccodeinfoentitlementsdict)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoEntitlementsDict: CFString! ``` |
| To | ``` let kSecCodeInfoEntitlementsDict: CFString ``` |

Modified [kSecCodeInfoFlags](https://developer.apple.com/documentation/security/kseccodeinfoflags)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoFlags: CFString! ``` |
| To | ``` let kSecCodeInfoFlags: CFString ``` |

Modified [kSecCodeInfoFormat](https://developer.apple.com/documentation/security/kseccodeinfoformat)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoFormat: CFString! ``` |
| To | ``` let kSecCodeInfoFormat: CFString ``` |

Modified [kSecCodeInfoIdentifier](https://developer.apple.com/documentation/security/kseccodeinfoidentifier)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoIdentifier: CFString! ``` |
| To | ``` let kSecCodeInfoIdentifier: CFString ``` |

Modified [kSecCodeInfoImplicitDesignatedRequirement](https://developer.apple.com/documentation/security/kseccodeinfoimplicitdesignatedrequirement)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoImplicitDesignatedRequirement: CFString! ``` |
| To | ``` let kSecCodeInfoImplicitDesignatedRequirement: CFString ``` |

Modified [kSecCodeInfoMainExecutable](https://developer.apple.com/documentation/security/kseccodeinfomainexecutable)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoMainExecutable: CFString! ``` |
| To | ``` let kSecCodeInfoMainExecutable: CFString ``` |

Modified [kSecCodeInfoPList](https://developer.apple.com/documentation/security/kseccodeinfoplist)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoPList: CFString! ``` |
| To | ``` let kSecCodeInfoPList: CFString ``` |

Modified [kSecCodeInfoRequirementData](https://developer.apple.com/documentation/security/kseccodeinforequirementdata)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoRequirementData: CFString! ``` |
| To | ``` let kSecCodeInfoRequirementData: CFString ``` |

Modified [kSecCodeInfoRequirements](https://developer.apple.com/documentation/security/kseccodeinforequirements)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoRequirements: CFString! ``` |
| To | ``` let kSecCodeInfoRequirements: CFString ``` |

Modified [kSecCodeInfoSource](https://developer.apple.com/documentation/security/kseccodeinfosource)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoSource: CFString! ``` |
| To | ``` let kSecCodeInfoSource: CFString ``` |

Modified [kSecCodeInfoStatus](https://developer.apple.com/documentation/security/kseccodeinfostatus)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoStatus: CFString! ``` |
| To | ``` let kSecCodeInfoStatus: CFString ``` |

Modified [kSecCodeInfoTeamIdentifier](https://developer.apple.com/documentation/security/kseccodeinfoteamidentifier)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoTeamIdentifier: CFString! ``` |
| To | ``` let kSecCodeInfoTeamIdentifier: CFString ``` |

Modified [kSecCodeInfoTime](https://developer.apple.com/documentation/security/kseccodeinfotime)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoTime: CFString! ``` |
| To | ``` let kSecCodeInfoTime: CFString ``` |

Modified [kSecCodeInfoTimestamp](https://developer.apple.com/documentation/security/kseccodeinfotimestamp)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoTimestamp: CFString! ``` |
| To | ``` let kSecCodeInfoTimestamp: CFString ``` |

Modified [kSecCodeInfoTrust](https://developer.apple.com/documentation/security/kseccodeinfotrust)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoTrust: CFString! ``` |
| To | ``` let kSecCodeInfoTrust: CFString ``` |

Modified [kSecCodeInfoUnique](https://developer.apple.com/documentation/security/kseccodeinfounique)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCodeInfoUnique: CFString! ``` |
| To | ``` let kSecCodeInfoUnique: CFString ``` |

Modified [kSecCompressionRatio](https://developer.apple.com/documentation/security/kseccompressionratio)

|  | Declaration |
| --- | --- |
| From | ``` let kSecCompressionRatio: CFString! ``` |
| To | ``` let kSecCompressionRatio: CFString ``` |

Modified [kSecCSBasicValidateOnly](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsbasicvalidateonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSBasicValidateOnly: Int { get } ``` |
| To | ``` var kSecCSBasicValidateOnly: UInt32 { get } ``` |

Modified [kSecCSCheckAllArchitectures](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccscheckallarchitectures)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSCheckAllArchitectures: Int { get } ``` |
| To | ``` var kSecCSCheckAllArchitectures: UInt32 { get } ``` |

Modified [kSecCSCheckGatekeeperArchitectures](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccscheckgatekeeperarchitectures)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSCheckGatekeeperArchitectures: Int { get } ``` |
| To | ``` var kSecCSCheckGatekeeperArchitectures: UInt32 { get } ``` |

Modified [kSecCSCheckNestedCode](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccschecknestedcode)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSCheckNestedCode: Int { get } ``` |
| To | ``` var kSecCSCheckNestedCode: UInt32 { get } ``` |

Modified [kSecCSContentInformation](https://developer.apple.com/documentation/security/kseccscontentinformation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSContentInformation: Int { get } ``` |
| To | ``` var kSecCSContentInformation: UInt32 { get } ``` |

Modified [kSecCSDedicatedHost](https://developer.apple.com/documentation/security/kseccsdedicatedhost)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSDedicatedHost: Int { get } ``` |
| To | ``` var kSecCSDedicatedHost: UInt32 { get } ``` |

Modified [kSecCSDoNotValidateExecutable](https://developer.apple.com/documentation/security/kseccsdonotvalidateexecutable)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSDoNotValidateExecutable: Int { get } ``` |
| To | ``` var kSecCSDoNotValidateExecutable: UInt32 { get } ``` |

Modified [kSecCSDoNotValidateResources](https://developer.apple.com/documentation/security/kseccsdonotvalidateresources)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSDoNotValidateResources: Int { get } ``` |
| To | ``` var kSecCSDoNotValidateResources: UInt32 { get } ``` |

Modified [kSecCSDynamicInformation](https://developer.apple.com/documentation/security/1569509-code_signing_information_flags/kseccsdynamicinformation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSDynamicInformation: Int { get } ``` |
| To | ``` var kSecCSDynamicInformation: UInt32 { get } ``` |

Modified [kSecCSFullReport](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsfullreport)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSFullReport: Int { get } ``` |
| To | ``` var kSecCSFullReport: UInt32 { get } ``` |

Modified [kSecCSGenerateGuestHash](https://developer.apple.com/documentation/security/1560749-guest_creation_flags/kseccsgenerateguesthash)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSGenerateGuestHash: Int { get } ``` |
| To | ``` var kSecCSGenerateGuestHash: UInt32 { get } ``` |

Modified [kSecCSInternalInformation](https://developer.apple.com/documentation/security/1569509-code_signing_information_flags/kseccsinternalinformation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSInternalInformation: Int { get } ``` |
| To | ``` var kSecCSInternalInformation: UInt32 { get } ``` |

Modified [kSecCSRequirementInformation](https://developer.apple.com/documentation/security/kseccsrequirementinformation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSRequirementInformation: Int { get } ``` |
| To | ``` var kSecCSRequirementInformation: UInt32 { get } ``` |

Modified [kSecCSSigningInformation](https://developer.apple.com/documentation/security/kseccssigninginformation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSSigningInformation: Int { get } ``` |
| To | ``` var kSecCSSigningInformation: UInt32 { get } ``` |

Modified [kSecCSStrictValidate](https://developer.apple.com/documentation/security/kseccsstrictvalidate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSStrictValidate: Int { get } ``` |
| To | ``` var kSecCSStrictValidate: UInt32 { get } ``` |

Modified [kSecCSUseAllArchitectures](https://developer.apple.com/documentation/security/1569510-code_signing_architecture_flags/kseccsuseallarchitectures)

|  | Declaration |
| --- | --- |
| From | ``` var kSecCSUseAllArchitectures: Int { get } ``` |
| To | ``` var kSecCSUseAllArchitectures: UInt32 { get } ``` |

Modified [kSecDecodeTypeAttribute](https://developer.apple.com/documentation/security/ksecdecodetypeattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDecodeTypeAttribute: CFString! ``` |
| To | ``` let kSecDecodeTypeAttribute: CFString ``` |

Modified [kSecDigestHMACKeyAttribute](https://developer.apple.com/documentation/security/ksecdigesthmackeyattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestHMACKeyAttribute: CFString! ``` |
| To | ``` let kSecDigestHMACKeyAttribute: CFString ``` |

Modified [kSecDigestHMACMD5](https://developer.apple.com/documentation/security/ksecdigesthmacmd5)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestHMACMD5: CFString! ``` |
| To | ``` let kSecDigestHMACMD5: CFString ``` |

Modified [kSecDigestHMACSHA1](https://developer.apple.com/documentation/security/ksecdigesthmacsha1)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestHMACSHA1: CFString! ``` |
| To | ``` let kSecDigestHMACSHA1: CFString ``` |

Modified [kSecDigestHMACSHA2](https://developer.apple.com/documentation/security/ksecdigesthmacsha2)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestHMACSHA2: CFString! ``` |
| To | ``` let kSecDigestHMACSHA2: CFString ``` |

Modified [kSecDigestLengthAttribute](https://developer.apple.com/documentation/security/ksecdigestlengthattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestLengthAttribute: CFString! ``` |
| To | ``` let kSecDigestLengthAttribute: CFString ``` |

Modified [kSecDigestMD2](https://developer.apple.com/documentation/security/ksecdigestmd2)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestMD2: CFString! ``` |
| To | ``` let kSecDigestMD2: CFString ``` |

Modified [kSecDigestMD4](https://developer.apple.com/documentation/security/ksecdigestmd4)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestMD4: CFString! ``` |
| To | ``` let kSecDigestMD4: CFString ``` |

Modified [kSecDigestMD5](https://developer.apple.com/documentation/security/ksecdigestmd5)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestMD5: CFString! ``` |
| To | ``` let kSecDigestMD5: CFString ``` |

Modified [kSecDigestSHA1](https://developer.apple.com/documentation/security/ksecdigestsha1)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestSHA1: CFString! ``` |
| To | ``` let kSecDigestSHA1: CFString ``` |

Modified [kSecDigestSHA2](https://developer.apple.com/documentation/security/ksecdigestsha2)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestSHA2: CFString! ``` |
| To | ``` let kSecDigestSHA2: CFString ``` |

Modified [kSecDigestTypeAttribute](https://developer.apple.com/documentation/security/ksecdigesttypeattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecDigestTypeAttribute: CFString! ``` |
| To | ``` let kSecDigestTypeAttribute: CFString ``` |

Modified [kSecEncodeLineLengthAttribute](https://developer.apple.com/documentation/security/ksecencodelinelengthattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecEncodeLineLengthAttribute: CFString! ``` |
| To | ``` let kSecEncodeLineLengthAttribute: CFString ``` |

Modified [kSecEncodeTypeAttribute](https://developer.apple.com/documentation/security/ksecencodetypeattribute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecEncodeTypeAttribute: CFString! ``` |
| To | ``` let kSecEncodeTypeAttribute: CFString ``` |

Modified [kSecEncryptionMode](https://developer.apple.com/documentation/security/ksecencryptionmode)

|  | Declaration |
| --- | --- |
| From | ``` var kSecEncryptionMode: Unmanaged<CFString>! ``` |
| To | ``` let kSecEncryptionMode: CFString ``` |

Modified [kSecEncryptKey](https://developer.apple.com/documentation/security/ksecencryptkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecEncryptKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecEncryptKey: CFString ``` |

Modified [kSecGuestAttributeArchitecture](https://developer.apple.com/documentation/security/ksecguestattributearchitecture)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeArchitecture: CFString! ``` |
| To | ``` let kSecGuestAttributeArchitecture: CFString ``` |

Modified [kSecGuestAttributeCanonical](https://developer.apple.com/documentation/security/ksecguestattributecanonical)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeCanonical: CFString! ``` |
| To | ``` let kSecGuestAttributeCanonical: CFString ``` |

Modified [kSecGuestAttributeDynamicCode](https://developer.apple.com/documentation/security/ksecguestattributedynamiccode)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeDynamicCode: CFString! ``` |
| To | ``` let kSecGuestAttributeDynamicCode: CFString ``` |

Modified [kSecGuestAttributeDynamicCodeInfoPlist](https://developer.apple.com/documentation/security/ksecguestattributedynamiccodeinfoplist)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeDynamicCodeInfoPlist: CFString! ``` |
| To | ``` let kSecGuestAttributeDynamicCodeInfoPlist: CFString ``` |

Modified [kSecGuestAttributeHash](https://developer.apple.com/documentation/security/ksecguestattributehash)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeHash: CFString! ``` |
| To | ``` let kSecGuestAttributeHash: CFString ``` |

Modified [kSecGuestAttributeMachPort](https://developer.apple.com/documentation/security/ksecguestattributemachport)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeMachPort: CFString! ``` |
| To | ``` let kSecGuestAttributeMachPort: CFString ``` |

Modified [kSecGuestAttributePid](https://developer.apple.com/documentation/security/ksecguestattributepid)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributePid: CFString! ``` |
| To | ``` let kSecGuestAttributePid: CFString ``` |

Modified [kSecGuestAttributeSubarchitecture](https://developer.apple.com/documentation/security/ksecguestattributesubarchitecture)

|  | Declaration |
| --- | --- |
| From | ``` let kSecGuestAttributeSubarchitecture: CFString! ``` |
| To | ``` let kSecGuestAttributeSubarchitecture: CFString ``` |

Modified [kSecIdentityDomainDefault](https://developer.apple.com/documentation/security/ksecidentitydomaindefault)

|  | Declaration |
| --- | --- |
| From | ``` let kSecIdentityDomainDefault: CFString! ``` |
| To | ``` let kSecIdentityDomainDefault: CFString ``` |

Modified [kSecIdentityDomainKerberosKDC](https://developer.apple.com/documentation/security/ksecidentitydomainkerberoskdc)

|  | Declaration |
| --- | --- |
| From | ``` let kSecIdentityDomainKerberosKDC: CFString! ``` |
| To | ``` let kSecIdentityDomainKerberosKDC: CFString ``` |

Modified [kSecImportExportAccess](https://developer.apple.com/documentation/security/ksecimportexportaccess)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportExportAccess: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportExportAccess: CFString ``` |

Modified [kSecImportExportKeychain](https://developer.apple.com/documentation/security/ksecimportexportkeychain)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportExportKeychain: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportExportKeychain: CFString ``` |

Modified [kSecImportExportPassphrase](https://developer.apple.com/documentation/security/ksecimportexportpassphrase)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportExportPassphrase: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportExportPassphrase: CFString ``` |

Modified [kSecImportItemCertChain](https://developer.apple.com/documentation/security/ksecimportitemcertchain)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportItemCertChain: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportItemCertChain: CFString ``` |

Modified [kSecImportItemIdentity](https://developer.apple.com/documentation/security/ksecimportitemidentity)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportItemIdentity: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportItemIdentity: CFString ``` |

Modified [kSecImportItemKeyID](https://developer.apple.com/documentation/security/ksecimportitemkeyid)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportItemKeyID: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportItemKeyID: CFString ``` |

Modified [kSecImportItemLabel](https://developer.apple.com/documentation/security/ksecimportitemlabel)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportItemLabel: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportItemLabel: CFString ``` |

Modified [kSecImportItemTrust](https://developer.apple.com/documentation/security/ksecimportitemtrust)

|  | Declaration |
| --- | --- |
| From | ``` var kSecImportItemTrust: Unmanaged<CFString>! ``` |
| To | ``` let kSecImportItemTrust: CFString ``` |

Modified [kSecInputIsAttributeName](https://developer.apple.com/documentation/security/ksecinputisattributename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecInputIsAttributeName: Unmanaged<CFString>! ``` |
| To | ``` let kSecInputIsAttributeName: CFString ``` |

Modified [kSecInputIsDigest](https://developer.apple.com/documentation/security/ksecinputisdigest)

|  | Declaration |
| --- | --- |
| From | ``` var kSecInputIsDigest: Unmanaged<CFString>! ``` |
| To | ``` let kSecInputIsDigest: CFString ``` |

Modified [kSecInputIsPlainText](https://developer.apple.com/documentation/security/ksecinputisplaintext)

|  | Declaration |
| --- | --- |
| From | ``` var kSecInputIsPlainText: Unmanaged<CFString>! ``` |
| To | ``` let kSecInputIsPlainText: CFString ``` |

Modified [kSecInputIsRaw](https://developer.apple.com/documentation/security/ksecinputisraw)

|  | Declaration |
| --- | --- |
| From | ``` var kSecInputIsRaw: Unmanaged<CFString>! ``` |
| To | ``` let kSecInputIsRaw: CFString ``` |

Modified [kSecIVKey](https://developer.apple.com/documentation/security/ksecivkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecIVKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecIVKey: CFString ``` |

Modified [kSecKeyAlias](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyalias)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyAlias: Int { get } ``` |
| To | ``` var kSecKeyAlias: Int32 { get } ``` |

Modified [kSecKeyAlwaysSensitive](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyalwayssensitive)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyAlwaysSensitive: Int { get } ``` |
| To | ``` var kSecKeyAlwaysSensitive: Int32 { get } ``` |

Modified [kSecKeyApplicationTag](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyapplicationtag)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyApplicationTag: Int { get } ``` |
| To | ``` var kSecKeyApplicationTag: Int32 { get } ``` |

Modified [kSecKeyAttributeName](https://developer.apple.com/documentation/security/kseckeyattributename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyAttributeName: Unmanaged<CFString>! ``` |
| To | ``` let kSecKeyAttributeName: CFString ``` |

Modified [kSecKeyDecrypt](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeydecrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyDecrypt: Int { get } ``` |
| To | ``` var kSecKeyDecrypt: Int32 { get } ``` |

Modified [kSecKeyDerive](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyderive)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyDerive: Int { get } ``` |
| To | ``` var kSecKeyDerive: Int32 { get } ``` |

Modified [kSecKeyEffectiveKeySize](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyeffectivekeysize)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyEffectiveKeySize: Int { get } ``` |
| To | ``` var kSecKeyEffectiveKeySize: Int32 { get } ``` |

Modified [kSecKeyEncrypt](https://developer.apple.com/documentation/security/kseckeyencrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyEncrypt: Int { get } ``` |
| To | ``` var kSecKeyEncrypt: Int32 { get } ``` |

Modified [kSecKeyEndDate](https://developer.apple.com/documentation/security/kseckeyenddate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyEndDate: Int { get } ``` |
| To | ``` var kSecKeyEndDate: Int32 { get } ``` |

Modified [kSecKeyExtractable](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyextractable)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyExtractable: Int { get } ``` |
| To | ``` var kSecKeyExtractable: Int32 { get } ``` |

Modified [kSecKeyKeyClass](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeykeyclass)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyKeyClass: Int { get } ``` |
| To | ``` var kSecKeyKeyClass: Int32 { get } ``` |

Modified [kSecKeyKeyCreator](https://developer.apple.com/documentation/security/kseckeykeycreator)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyKeyCreator: Int { get } ``` |
| To | ``` var kSecKeyKeyCreator: Int32 { get } ``` |

Modified [kSecKeyKeySizeInBits](https://developer.apple.com/documentation/security/kseckeykeysizeinbits)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyKeySizeInBits: Int { get } ``` |
| To | ``` var kSecKeyKeySizeInBits: Int32 { get } ``` |

Modified [kSecKeyKeyType](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeykeytype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyKeyType: Int { get } ``` |
| To | ``` var kSecKeyKeyType: Int32 { get } ``` |

Modified [kSecKeyLabel](https://developer.apple.com/documentation/security/kseckeylabel)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyLabel: Int { get } ``` |
| To | ``` var kSecKeyLabel: Int32 { get } ``` |

Modified [kSecKeyModifiable](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeymodifiable)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyModifiable: Int { get } ``` |
| To | ``` var kSecKeyModifiable: Int32 { get } ``` |

Modified [kSecKeyNeverExtractable](https://developer.apple.com/documentation/security/kseckeyneverextractable)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyNeverExtractable: Int { get } ``` |
| To | ``` var kSecKeyNeverExtractable: Int32 { get } ``` |

Modified [kSecKeyPermanent](https://developer.apple.com/documentation/security/kseckeypermanent)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyPermanent: Int { get } ``` |
| To | ``` var kSecKeyPermanent: Int32 { get } ``` |

Modified [kSecKeyPrintName](https://developer.apple.com/documentation/security/kseckeyprintname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyPrintName: Int { get } ``` |
| To | ``` var kSecKeyPrintName: Int32 { get } ``` |

Modified [kSecKeyPrivate](https://developer.apple.com/documentation/security/kseckeyprivate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyPrivate: Int { get } ``` |
| To | ``` var kSecKeyPrivate: Int32 { get } ``` |

Modified [kSecKeySensitive](https://developer.apple.com/documentation/security/kseckeysensitive)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeySensitive: Int { get } ``` |
| To | ``` var kSecKeySensitive: Int32 { get } ``` |

Modified [kSecKeySign](https://developer.apple.com/documentation/security/kseckeysign)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeySign: Int { get } ``` |
| To | ``` var kSecKeySign: Int32 { get } ``` |

Modified [kSecKeySignRecover](https://developer.apple.com/documentation/security/kseckeysignrecover)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeySignRecover: Int { get } ``` |
| To | ``` var kSecKeySignRecover: Int32 { get } ``` |

Modified [kSecKeyStartDate](https://developer.apple.com/documentation/security/kseckeystartdate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyStartDate: Int { get } ``` |
| To | ``` var kSecKeyStartDate: Int32 { get } ``` |

Modified [kSecKeyUnwrap](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeyunwrap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyUnwrap: Int { get } ``` |
| To | ``` var kSecKeyUnwrap: Int32 { get } ``` |

Modified [kSecKeyVerify](https://developer.apple.com/documentation/security/kseckeyverify)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyVerify: Int { get } ``` |
| To | ``` var kSecKeyVerify: Int32 { get } ``` |

Modified [kSecKeyVerifyRecover](https://developer.apple.com/documentation/security/kseckeyverifyrecover)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyVerifyRecover: Int { get } ``` |
| To | ``` var kSecKeyVerifyRecover: Int32 { get } ``` |

Modified [kSecKeyWrap](https://developer.apple.com/documentation/security/1495743-keychain_item_attribute_constant/kseckeywrap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecKeyWrap: Int { get } ``` |
| To | ``` var kSecKeyWrap: Int32 { get } ``` |

Modified [kSecLineLength64](https://developer.apple.com/documentation/security/kseclinelength64)

|  | Declaration |
| --- | --- |
| From | ``` let kSecLineLength64: CFString! ``` |
| To | ``` let kSecLineLength64: CFString ``` |

Modified [kSecLineLength76](https://developer.apple.com/documentation/security/kseclinelength76)

|  | Declaration |
| --- | --- |
| From | ``` let kSecLineLength76: CFString! ``` |
| To | ``` let kSecLineLength76: CFString ``` |

Modified [kSecMatchCaseInsensitive](https://developer.apple.com/documentation/security/ksecmatchcaseinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchCaseInsensitive: CFStringRef ``` |
| To | ``` let kSecMatchCaseInsensitive: CFString ``` |

Modified [kSecMatchDiacriticInsensitive](https://developer.apple.com/documentation/security/ksecmatchdiacriticinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchDiacriticInsensitive: CFStringRef ``` |
| To | ``` let kSecMatchDiacriticInsensitive: CFString ``` |

Modified [kSecMatchEmailAddressIfPresent](https://developer.apple.com/documentation/security/ksecmatchemailaddressifpresent)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchEmailAddressIfPresent: CFStringRef ``` |
| To | ``` let kSecMatchEmailAddressIfPresent: CFString ``` |

Modified [kSecMatchIssuers](https://developer.apple.com/documentation/security/ksecmatchissuers)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchIssuers: CFStringRef ``` |
| To | ``` let kSecMatchIssuers: CFString ``` |

Modified [kSecMatchItemList](https://developer.apple.com/documentation/security/ksecmatchitemlist)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchItemList: CFStringRef ``` |
| To | ``` let kSecMatchItemList: CFString ``` |

Modified [kSecMatchLimit](https://developer.apple.com/documentation/security/ksecmatchlimit)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchLimit: CFStringRef ``` |
| To | ``` let kSecMatchLimit: CFString ``` |

Modified [kSecMatchLimitAll](https://developer.apple.com/documentation/security/ksecmatchlimitall)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchLimitAll: CFStringRef ``` |
| To | ``` let kSecMatchLimitAll: CFString ``` |

Modified [kSecMatchLimitOne](https://developer.apple.com/documentation/security/ksecmatchlimitone)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchLimitOne: CFStringRef ``` |
| To | ``` let kSecMatchLimitOne: CFString ``` |

Modified [kSecMatchPolicy](https://developer.apple.com/documentation/security/ksecmatchpolicy)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchPolicy: CFStringRef ``` |
| To | ``` let kSecMatchPolicy: CFString ``` |

Modified [kSecMatchSearchList](https://developer.apple.com/documentation/security/ksecmatchsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchSearchList: CFStringRef ``` |
| To | ``` let kSecMatchSearchList: CFString ``` |

Modified [kSecMatchSubjectContains](https://developer.apple.com/documentation/security/ksecmatchsubjectcontains)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchSubjectContains: CFStringRef ``` |
| To | ``` let kSecMatchSubjectContains: CFString ``` |

Modified [kSecMatchSubjectEndsWith](https://developer.apple.com/documentation/security/ksecmatchsubjectendswith)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchSubjectEndsWith: CFStringRef ``` |
| To | ``` let kSecMatchSubjectEndsWith: CFString ``` |

Modified [kSecMatchSubjectStartsWith](https://developer.apple.com/documentation/security/ksecmatchsubjectstartswith)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchSubjectStartsWith: CFStringRef ``` |
| To | ``` let kSecMatchSubjectStartsWith: CFString ``` |

Modified [kSecMatchSubjectWholeString](https://developer.apple.com/documentation/security/ksecmatchsubjectwholestring)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchSubjectWholeString: CFStringRef ``` |
| To | ``` let kSecMatchSubjectWholeString: CFString ``` |

Modified [kSecMatchTrustedOnly](https://developer.apple.com/documentation/security/ksecmatchtrustedonly)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchTrustedOnly: CFStringRef ``` |
| To | ``` let kSecMatchTrustedOnly: CFString ``` |

Modified [kSecMatchValidOnDate](https://developer.apple.com/documentation/security/ksecmatchvalidondate)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchValidOnDate: CFStringRef ``` |
| To | ``` let kSecMatchValidOnDate: CFString ``` |

Modified [kSecMatchWidthInsensitive](https://developer.apple.com/documentation/security/ksecmatchwidthinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` let kSecMatchWidthInsensitive: CFStringRef ``` |
| To | ``` let kSecMatchWidthInsensitive: CFString ``` |

Modified [kSecModeCBCKey](https://developer.apple.com/documentation/security/ksecmodecbckey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecModeCBCKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecModeCBCKey: CFString ``` |

Modified [kSecModeCFBKey](https://developer.apple.com/documentation/security/ksecmodecfbkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecModeCFBKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecModeCFBKey: CFString ``` |

Modified [kSecModeECBKey](https://developer.apple.com/documentation/security/ksecmodeecbkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecModeECBKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecModeECBKey: CFString ``` |

Modified [kSecModeNoneKey](https://developer.apple.com/documentation/security/ksecmodenonekey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecModeNoneKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecModeNoneKey: CFString ``` |

Modified [kSecModeOFBKey](https://developer.apple.com/documentation/security/ksecmodeofbkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecModeOFBKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecModeOFBKey: CFString ``` |

Modified [kSecNoGuest](https://developer.apple.com/documentation/security/ksecnoguest)

|  | Declaration |
| --- | --- |
| From | ``` var kSecNoGuest: Int { get } ``` |
| To | ``` var kSecNoGuest: SecGuestRef { get } ``` |

Modified [kSecOAEPEncodingParametersAttributeName](https://developer.apple.com/documentation/security/ksecoaepencodingparametersattributename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOAEPEncodingParametersAttributeName: Unmanaged<CFString>! ``` |
| To | ``` let kSecOAEPEncodingParametersAttributeName: CFString ``` |

Modified [kSecOAEPMessageLengthAttributeName](https://developer.apple.com/documentation/security/ksecoaepmessagelengthattributename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOAEPMessageLengthAttributeName: Unmanaged<CFString>! ``` |
| To | ``` let kSecOAEPMessageLengthAttributeName: CFString ``` |

Modified [kSecOAEPMGF1DigestAlgorithmAttributeName](https://developer.apple.com/documentation/security/ksecoaepmgf1digestalgorithmattributename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOAEPMGF1DigestAlgorithmAttributeName: Unmanaged<CFString>! ``` |
| To | ``` let kSecOAEPMGF1DigestAlgorithmAttributeName: CFString ``` |

Modified [kSecOIDADC_CERT_POLICY](https://developer.apple.com/documentation/security/ksecoidadc_cert_policy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDADC_CERT_POLICY: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDADC_CERT_POLICY: CFString ``` |

Modified [kSecOIDAPPLE_CERT_POLICY](https://developer.apple.com/documentation/security/ksecoidapple_cert_policy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_CERT_POLICY: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_CERT_POLICY: CFString ``` |

Modified [kSecOIDAPPLE_EKU_CODE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_eku_code_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EKU_CODE_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EKU_CODE_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EKU_CODE_SIGNING_DEV](https://developer.apple.com/documentation/security/ksecoidapple_eku_code_signing_dev)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EKU_CODE_SIGNING_DEV: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EKU_CODE_SIGNING_DEV: CFString ``` |

Modified [kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION](https://developer.apple.com/documentation/security/ksecoidapple_eku_ichat_encryption)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION: CFString ``` |

Modified [kSecOIDAPPLE_EKU_ICHAT_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_eku_ichat_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EKU_ICHAT_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EKU_ICHAT_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EKU_RESOURCE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_eku_resource_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EKU_RESOURCE_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EKU_RESOURCE_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EKU_SYSTEM_IDENTITY](https://developer.apple.com/documentation/security/ksecoidapple_eku_system_identity)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EKU_SYSTEM_IDENTITY: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EKU_SYSTEM_IDENTITY: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION](https://developer.apple.com/documentation/security/ksecoidapple_extension)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_aai_intermediate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_adc_apple_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_adc_dev_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_APPLE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_apple_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_APPLE_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_APPLE_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_appleid_intermediate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_CODE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_code_signing)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_CODE_SIGNING: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_CODE_SIGNING: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER](https://developer.apple.com/documentation/security/ksecoidapple_extension_intermediate_marker)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_itms_intermediate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE: CFString ``` |

Modified [kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_wwdr_intermediate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE: CFString ``` |

Modified [kSecOIDAuthorityInfoAccess](https://developer.apple.com/documentation/security/ksecoidauthorityinfoaccess)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAuthorityInfoAccess: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAuthorityInfoAccess: CFString ``` |

Modified [kSecOIDAuthorityKeyIdentifier](https://developer.apple.com/documentation/security/ksecoidauthoritykeyidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDAuthorityKeyIdentifier: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDAuthorityKeyIdentifier: CFString ``` |

Modified [kSecOIDBasicConstraints](https://developer.apple.com/documentation/security/ksecoidbasicconstraints)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDBasicConstraints: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDBasicConstraints: CFString ``` |

Modified [kSecOIDBiometricInfo](https://developer.apple.com/documentation/security/ksecoidbiometricinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDBiometricInfo: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDBiometricInfo: CFString ``` |

Modified [kSecOIDCertificatePolicies](https://developer.apple.com/documentation/security/ksecoidcertificatepolicies)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCertificatePolicies: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCertificatePolicies: CFString ``` |

Modified [kSecOIDCertIssuer](https://developer.apple.com/documentation/security/ksecoidcertissuer)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCertIssuer: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCertIssuer: CFString ``` |

Modified [kSecOIDClientAuth](https://developer.apple.com/documentation/security/ksecoidclientauth)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDClientAuth: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDClientAuth: CFString ``` |

Modified [kSecOIDCollectiveStateProvinceName](https://developer.apple.com/documentation/security/ksecoidcollectivestateprovincename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCollectiveStateProvinceName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCollectiveStateProvinceName: CFString ``` |

Modified [kSecOIDCollectiveStreetAddress](https://developer.apple.com/documentation/security/ksecoidcollectivestreetaddress)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCollectiveStreetAddress: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCollectiveStreetAddress: CFString ``` |

Modified [kSecOIDCommonName](https://developer.apple.com/documentation/security/ksecoidcommonname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCommonName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCommonName: CFString ``` |

Modified [kSecOIDCountryName](https://developer.apple.com/documentation/security/ksecoidcountryname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCountryName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCountryName: CFString ``` |

Modified [kSecOIDCrlDistributionPoints](https://developer.apple.com/documentation/security/ksecoidcrldistributionpoints)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCrlDistributionPoints: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCrlDistributionPoints: CFString ``` |

Modified [kSecOIDCrlNumber](https://developer.apple.com/documentation/security/ksecoidcrlnumber)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCrlNumber: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCrlNumber: CFString ``` |

Modified [kSecOIDCrlReason](https://developer.apple.com/documentation/security/ksecoidcrlreason)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCrlReason: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCrlReason: CFString ``` |

Modified [kSecOIDCSSMKeyStruct](https://developer.apple.com/documentation/security/ksecoidcssmkeystruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDCSSMKeyStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDCSSMKeyStruct: CFString ``` |

Modified [kSecOIDDeltaCrlIndicator](https://developer.apple.com/documentation/security/ksecoiddeltacrlindicator)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDeltaCrlIndicator: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDeltaCrlIndicator: CFString ``` |

Modified [kSecOIDDescription](https://developer.apple.com/documentation/security/ksecoiddescription)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDescription: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDescription: CFString ``` |

Modified [kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_email_encrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT: CFString ``` |

Modified [kSecOIDDOTMAC_CERT_EMAIL_SIGN](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_email_sign)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDOTMAC_CERT_EMAIL_SIGN: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDOTMAC_CERT_EMAIL_SIGN: CFString ``` |

Modified [kSecOIDDOTMAC_CERT_EXTENSION](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_extension)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDOTMAC_CERT_EXTENSION: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDOTMAC_CERT_EXTENSION: CFString ``` |

Modified [kSecOIDDOTMAC_CERT_IDENTITY](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_identity)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDOTMAC_CERT_IDENTITY: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDOTMAC_CERT_IDENTITY: CFString ``` |

Modified [kSecOIDDOTMAC_CERT_POLICY](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_policy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDDOTMAC_CERT_POLICY: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDDOTMAC_CERT_POLICY: CFString ``` |

Modified [kSecOIDEKU_IPSec](https://developer.apple.com/documentation/security/ksecoideku_ipsec)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDEKU_IPSec: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDEKU_IPSec: CFString ``` |

Modified [kSecOIDEmailAddress](https://developer.apple.com/documentation/security/ksecoidemailaddress)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDEmailAddress: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDEmailAddress: CFString ``` |

Modified [kSecOIDEmailProtection](https://developer.apple.com/documentation/security/ksecoidemailprotection)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDEmailProtection: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDEmailProtection: CFString ``` |

Modified [kSecOIDExtendedKeyUsage](https://developer.apple.com/documentation/security/ksecoidextendedkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDExtendedKeyUsage: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDExtendedKeyUsage: CFString ``` |

Modified [kSecOIDExtendedKeyUsageAny](https://developer.apple.com/documentation/security/ksecoidextendedkeyusageany)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDExtendedKeyUsageAny: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDExtendedKeyUsageAny: CFString ``` |

Modified [kSecOIDExtendedUseCodeSigning](https://developer.apple.com/documentation/security/ksecoidextendedusecodesigning)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDExtendedUseCodeSigning: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDExtendedUseCodeSigning: CFString ``` |

Modified [kSecOIDGivenName](https://developer.apple.com/documentation/security/ksecoidgivenname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDGivenName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDGivenName: CFString ``` |

Modified [kSecOIDHoldInstructionCode](https://developer.apple.com/documentation/security/ksecoidholdinstructioncode)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDHoldInstructionCode: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDHoldInstructionCode: CFString ``` |

Modified [kSecOIDInvalidityDate](https://developer.apple.com/documentation/security/ksecoidinvaliditydate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDInvalidityDate: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDInvalidityDate: CFString ``` |

Modified [kSecOIDIssuerAltName](https://developer.apple.com/documentation/security/ksecoidissueraltname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDIssuerAltName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDIssuerAltName: CFString ``` |

Modified [kSecOIDIssuingDistributionPoint](https://developer.apple.com/documentation/security/ksecoidissuingdistributionpoint)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDIssuingDistributionPoint: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDIssuingDistributionPoint: CFString ``` |

Modified [kSecOIDIssuingDistributionPoints](https://developer.apple.com/documentation/security/ksecoidissuingdistributionpoints)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDIssuingDistributionPoints: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDIssuingDistributionPoints: CFString ``` |

Modified [kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH](https://developer.apple.com/documentation/security/ksecoidkerbv5_pkinit_kp_client_auth)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH: CFString ``` |

Modified [kSecOIDKERBv5_PKINIT_KP_KDC](https://developer.apple.com/documentation/security/ksecoidkerbv5_pkinit_kp_kdc)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDKERBv5_PKINIT_KP_KDC: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDKERBv5_PKINIT_KP_KDC: CFString ``` |

Modified [kSecOIDKeyUsage](https://developer.apple.com/documentation/security/ksecoidkeyusage)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDKeyUsage: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDKeyUsage: CFString ``` |

Modified [kSecOIDLocalityName](https://developer.apple.com/documentation/security/ksecoidlocalityname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDLocalityName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDLocalityName: CFString ``` |

Modified [kSecOIDMicrosoftSGC](https://developer.apple.com/documentation/security/ksecoidmicrosoftsgc)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDMicrosoftSGC: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDMicrosoftSGC: CFString ``` |

Modified [kSecOIDMS_NTPrincipalName](https://developer.apple.com/documentation/security/ksecoidms_ntprincipalname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDMS_NTPrincipalName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDMS_NTPrincipalName: CFString ``` |

Modified [kSecOIDNameConstraints](https://developer.apple.com/documentation/security/ksecoidnameconstraints)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDNameConstraints: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDNameConstraints: CFString ``` |

Modified [kSecOIDNetscapeCertSequence](https://developer.apple.com/documentation/security/ksecoidnetscapecertsequence)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDNetscapeCertSequence: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDNetscapeCertSequence: CFString ``` |

Modified [kSecOIDNetscapeCertType](https://developer.apple.com/documentation/security/ksecoidnetscapecerttype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDNetscapeCertType: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDNetscapeCertType: CFString ``` |

Modified [kSecOIDNetscapeSGC](https://developer.apple.com/documentation/security/ksecoidnetscapesgc)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDNetscapeSGC: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDNetscapeSGC: CFString ``` |

Modified [kSecOIDOCSPSigning](https://developer.apple.com/documentation/security/ksecoidocspsigning)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDOCSPSigning: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDOCSPSigning: CFString ``` |

Modified [kSecOIDOrganizationalUnitName](https://developer.apple.com/documentation/security/ksecoidorganizationalunitname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDOrganizationalUnitName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDOrganizationalUnitName: CFString ``` |

Modified [kSecOIDOrganizationName](https://developer.apple.com/documentation/security/ksecoidorganizationname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDOrganizationName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDOrganizationName: CFString ``` |

Modified [kSecOIDPolicyConstraints](https://developer.apple.com/documentation/security/ksecoidpolicyconstraints)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDPolicyConstraints: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDPolicyConstraints: CFString ``` |

Modified [kSecOIDPolicyMappings](https://developer.apple.com/documentation/security/ksecoidpolicymappings)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDPolicyMappings: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDPolicyMappings: CFString ``` |

Modified [kSecOIDPrivateKeyUsagePeriod](https://developer.apple.com/documentation/security/ksecoidprivatekeyusageperiod)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDPrivateKeyUsagePeriod: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDPrivateKeyUsagePeriod: CFString ``` |

Modified [kSecOIDQC_Statements](https://developer.apple.com/documentation/security/ksecoidqc_statements)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDQC_Statements: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDQC_Statements: CFString ``` |

Modified [kSecOIDSerialNumber](https://developer.apple.com/documentation/security/ksecoidserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSerialNumber: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSerialNumber: CFString ``` |

Modified [kSecOIDServerAuth](https://developer.apple.com/documentation/security/ksecoidserverauth)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDServerAuth: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDServerAuth: CFString ``` |

Modified [kSecOIDSRVName](https://developer.apple.com/documentation/security/ksecoidsrvname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSRVName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSRVName: CFString ``` |

Modified [kSecOIDStateProvinceName](https://developer.apple.com/documentation/security/ksecoidstateprovincename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDStateProvinceName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDStateProvinceName: CFString ``` |

Modified [kSecOIDStreetAddress](https://developer.apple.com/documentation/security/ksecoidstreetaddress)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDStreetAddress: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDStreetAddress: CFString ``` |

Modified [kSecOIDSubjectAltName](https://developer.apple.com/documentation/security/ksecoidsubjectaltname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectAltName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectAltName: CFString ``` |

Modified [kSecOIDSubjectDirectoryAttributes](https://developer.apple.com/documentation/security/ksecoidsubjectdirectoryattributes)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectDirectoryAttributes: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectDirectoryAttributes: CFString ``` |

Modified [kSecOIDSubjectEmailAddress](https://developer.apple.com/documentation/security/ksecoidsubjectemailaddress)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectEmailAddress: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectEmailAddress: CFString ``` |

Modified [kSecOIDSubjectInfoAccess](https://developer.apple.com/documentation/security/ksecoidsubjectinfoaccess)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectInfoAccess: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectInfoAccess: CFString ``` |

Modified [kSecOIDSubjectKeyIdentifier](https://developer.apple.com/documentation/security/ksecoidsubjectkeyidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectKeyIdentifier: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectKeyIdentifier: CFString ``` |

Modified [kSecOIDSubjectPicture](https://developer.apple.com/documentation/security/ksecoidsubjectpicture)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectPicture: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectPicture: CFString ``` |

Modified [kSecOIDSubjectSignatureBitmap](https://developer.apple.com/documentation/security/ksecoidsubjectsignaturebitmap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSubjectSignatureBitmap: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSubjectSignatureBitmap: CFString ``` |

Modified [kSecOIDSurname](https://developer.apple.com/documentation/security/ksecoidsurname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDSurname: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDSurname: CFString ``` |

Modified [kSecOIDTimeStamping](https://developer.apple.com/documentation/security/ksecoidtimestamping)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDTimeStamping: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDTimeStamping: CFString ``` |

Modified [kSecOIDTitle](https://developer.apple.com/documentation/security/ksecoidtitle)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDTitle: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDTitle: CFString ``` |

Modified [kSecOIDUseExemptions](https://developer.apple.com/documentation/security/ksecoiduseexemptions)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDUseExemptions: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDUseExemptions: CFString ``` |

Modified [kSecOIDX509V1CertificateIssuerUniqueId](https://developer.apple.com/documentation/security/ksecoidx509v1certificateissueruniqueid)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1CertificateIssuerUniqueId: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1CertificateIssuerUniqueId: CFString ``` |

Modified [kSecOIDX509V1CertificateSubjectUniqueId](https://developer.apple.com/documentation/security/ksecoidx509v1certificatesubjectuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1CertificateSubjectUniqueId: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1CertificateSubjectUniqueId: CFString ``` |

Modified [kSecOIDX509V1IssuerName](https://developer.apple.com/documentation/security/ksecoidx509v1issuername)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1IssuerName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1IssuerName: CFString ``` |

Modified [kSecOIDX509V1IssuerNameCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1issuernamecstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1IssuerNameCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1IssuerNameCStruct: CFString ``` |

Modified [kSecOIDX509V1IssuerNameLDAP](https://developer.apple.com/documentation/security/ksecoidx509v1issuernameldap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1IssuerNameLDAP: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1IssuerNameLDAP: CFString ``` |

Modified [kSecOIDX509V1IssuerNameStd](https://developer.apple.com/documentation/security/ksecoidx509v1issuernamestd)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1IssuerNameStd: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1IssuerNameStd: CFString ``` |

Modified [kSecOIDX509V1SerialNumber](https://developer.apple.com/documentation/security/ksecoidx509v1serialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SerialNumber: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SerialNumber: CFString ``` |

Modified [kSecOIDX509V1Signature](https://developer.apple.com/documentation/security/ksecoidx509v1signature)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1Signature: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1Signature: CFString ``` |

Modified [kSecOIDX509V1SignatureAlgorithm](https://developer.apple.com/documentation/security/ksecoidx509v1signaturealgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SignatureAlgorithm: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SignatureAlgorithm: CFString ``` |

Modified [kSecOIDX509V1SignatureAlgorithmParameters](https://developer.apple.com/documentation/security/ksecoidx509v1signaturealgorithmparameters)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SignatureAlgorithmParameters: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SignatureAlgorithmParameters: CFString ``` |

Modified [kSecOIDX509V1SignatureAlgorithmTBS](https://developer.apple.com/documentation/security/ksecoidx509v1signaturealgorithmtbs)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SignatureAlgorithmTBS: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SignatureAlgorithmTBS: CFString ``` |

Modified [kSecOIDX509V1SignatureCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1signaturecstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SignatureCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SignatureCStruct: CFString ``` |

Modified [kSecOIDX509V1SignatureStruct](https://developer.apple.com/documentation/security/ksecoidx509v1signaturestruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SignatureStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SignatureStruct: CFString ``` |

Modified [kSecOIDX509V1SubjectName](https://developer.apple.com/documentation/security/ksecoidx509v1subjectname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectName: CFString ``` |

Modified [kSecOIDX509V1SubjectNameCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1subjectnamecstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectNameCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectNameCStruct: CFString ``` |

Modified [kSecOIDX509V1SubjectNameLDAP](https://developer.apple.com/documentation/security/ksecoidx509v1subjectnameldap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectNameLDAP: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectNameLDAP: CFString ``` |

Modified [kSecOIDX509V1SubjectNameStd](https://developer.apple.com/documentation/security/ksecoidx509v1subjectnamestd)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectNameStd: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectNameStd: CFString ``` |

Modified [kSecOIDX509V1SubjectPublicKey](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectPublicKey: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectPublicKey: CFString ``` |

Modified [kSecOIDX509V1SubjectPublicKeyAlgorithm](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickeyalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectPublicKeyAlgorithm: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectPublicKeyAlgorithm: CFString ``` |

Modified [kSecOIDX509V1SubjectPublicKeyAlgorithmParameters](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickeyalgorithmparameters)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectPublicKeyAlgorithmParameters: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectPublicKeyAlgorithmParameters: CFString ``` |

Modified [kSecOIDX509V1SubjectPublicKeyCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickeycstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1SubjectPublicKeyCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1SubjectPublicKeyCStruct: CFString ``` |

Modified [kSecOIDX509V1ValidityNotAfter](https://developer.apple.com/documentation/security/ksecoidx509v1validitynotafter)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1ValidityNotAfter: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1ValidityNotAfter: CFString ``` |

Modified [kSecOIDX509V1ValidityNotBefore](https://developer.apple.com/documentation/security/ksecoidx509v1validitynotbefore)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1ValidityNotBefore: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1ValidityNotBefore: CFString ``` |

Modified [kSecOIDX509V1Version](https://developer.apple.com/documentation/security/ksecoidx509v1version)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V1Version: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V1Version: CFString ``` |

Modified [kSecOIDX509V3Certificate](https://developer.apple.com/documentation/security/ksecoidx509v3certificate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3Certificate: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3Certificate: CFString ``` |

Modified [kSecOIDX509V3CertificateCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificatecstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateCStruct: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionCritical](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensioncritical)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionCritical: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionCritical: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensioncstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionCStruct: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionId](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionid)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionId: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionId: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionsCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionscstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionsCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionsCStruct: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionsStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionsstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionsStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionsStruct: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionStruct: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionType](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensiontype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionType: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionType: CFString ``` |

Modified [kSecOIDX509V3CertificateExtensionValue](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateExtensionValue: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateExtensionValue: CFString ``` |

Modified [kSecOIDX509V3CertificateNumberOfExtensions](https://developer.apple.com/documentation/security/ksecoidx509v3certificatenumberofextensions)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3CertificateNumberOfExtensions: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3CertificateNumberOfExtensions: CFString ``` |

Modified [kSecOIDX509V3SignedCertificate](https://developer.apple.com/documentation/security/ksecoidx509v3signedcertificate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3SignedCertificate: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3SignedCertificate: CFString ``` |

Modified [kSecOIDX509V3SignedCertificateCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3signedcertificatecstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kSecOIDX509V3SignedCertificateCStruct: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecOIDX509V3SignedCertificateCStruct: CFString ``` |

Modified [kSecPaddingKey](https://developer.apple.com/documentation/security/ksecpaddingkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPaddingKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecPaddingKey: CFString ``` |

Modified [kSecPaddingNoneKey](https://developer.apple.com/documentation/security/ksecpaddingnonekey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPaddingNoneKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecPaddingNoneKey: CFString ``` |

Modified [kSecPaddingOAEPKey](https://developer.apple.com/documentation/security/ksecpaddingoaepkey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPaddingOAEPKey: Unmanaged<CFString>! ``` |
| To | ``` let kSecPaddingOAEPKey: CFString ``` |

Modified [kSecPaddingPKCS1Key](https://developer.apple.com/documentation/security/ksecpaddingpkcs1key)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPaddingPKCS1Key: Unmanaged<CFString>! ``` |
| To | ``` let kSecPaddingPKCS1Key: CFString ``` |

Modified [kSecPaddingPKCS5Key](https://developer.apple.com/documentation/security/ksecpaddingpkcs5key)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPaddingPKCS5Key: Unmanaged<CFString>! ``` |
| To | ``` let kSecPaddingPKCS5Key: CFString ``` |

Modified [kSecPaddingPKCS7Key](https://developer.apple.com/documentation/security/ksecpaddingpkcs7key)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPaddingPKCS7Key: Unmanaged<CFString>! ``` |
| To | ``` let kSecPaddingPKCS7Key: CFString ``` |

Modified [kSecPolicyAppleCodeSigning](https://developer.apple.com/documentation/security/ksecpolicyapplecodesigning)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleCodeSigning: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleCodeSigning: CFString ``` |

Modified [kSecPolicyAppleEAP](https://developer.apple.com/documentation/security/ksecpolicyappleeap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleEAP: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleEAP: CFString ``` |

Modified [kSecPolicyAppleIDValidation](https://developer.apple.com/documentation/security/ksecpolicyappleidvalidation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleIDValidation: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleIDValidation: CFString ``` |

Modified [kSecPolicyAppleIPsec](https://developer.apple.com/documentation/security/ksecpolicyappleipsec)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleIPsec: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleIPsec: CFString ``` |

Modified [kSecPolicyApplePassbookSigning](https://developer.apple.com/documentation/security/ksecpolicyapplepassbooksigning)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyApplePassbookSigning: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyApplePassbookSigning: CFString ``` |

Modified [kSecPolicyApplePKINITClient](https://developer.apple.com/documentation/security/ksecpolicyapplepkinitclient)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyApplePKINITClient: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyApplePKINITClient: CFString ``` |

Modified [kSecPolicyApplePKINITServer](https://developer.apple.com/documentation/security/ksecpolicyapplepkinitserver)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyApplePKINITServer: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyApplePKINITServer: CFString ``` |

Modified [kSecPolicyAppleRevocation](https://developer.apple.com/documentation/security/ksecpolicyapplerevocation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleRevocation: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleRevocation: CFString ``` |

Modified [kSecPolicyAppleSMIME](https://developer.apple.com/documentation/security/ksecpolicyapplesmime)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleSMIME: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleSMIME: CFString ``` |

Modified [kSecPolicyAppleSSL](https://developer.apple.com/documentation/security/ksecpolicyapplessl)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleSSL: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleSSL: CFString ``` |

Modified [kSecPolicyAppleTimeStamping](https://developer.apple.com/documentation/security/ksecpolicyappletimestamping)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleTimeStamping: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleTimeStamping: CFString ``` |

Modified [kSecPolicyAppleX509Basic](https://developer.apple.com/documentation/security/ksecpolicyapplex509basic)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyAppleX509Basic: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyAppleX509Basic: CFString ``` |

Modified [kSecPolicyClient](https://developer.apple.com/documentation/security/ksecpolicyclient)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyClient: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyClient: CFString ``` |

Modified [kSecPolicyKU_CRLSign](https://developer.apple.com/documentation/security/ksecpolicyku_crlsign)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_CRLSign: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_CRLSign: CFString ``` |

Modified [kSecPolicyKU_DataEncipherment](https://developer.apple.com/documentation/security/ksecpolicyku_dataencipherment)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_DataEncipherment: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_DataEncipherment: CFString ``` |

Modified [kSecPolicyKU_DecipherOnly](https://developer.apple.com/documentation/security/ksecpolicyku_decipheronly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_DecipherOnly: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_DecipherOnly: CFString ``` |

Modified [kSecPolicyKU_DigitalSignature](https://developer.apple.com/documentation/security/ksecpolicyku_digitalsignature)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_DigitalSignature: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_DigitalSignature: CFString ``` |

Modified [kSecPolicyKU_EncipherOnly](https://developer.apple.com/documentation/security/ksecpolicyku_encipheronly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_EncipherOnly: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_EncipherOnly: CFString ``` |

Modified [kSecPolicyKU_KeyAgreement](https://developer.apple.com/documentation/security/ksecpolicyku_keyagreement)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_KeyAgreement: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_KeyAgreement: CFString ``` |

Modified [kSecPolicyKU_KeyCertSign](https://developer.apple.com/documentation/security/ksecpolicyku_keycertsign)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_KeyCertSign: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_KeyCertSign: CFString ``` |

Modified [kSecPolicyKU_KeyEncipherment](https://developer.apple.com/documentation/security/ksecpolicyku_keyencipherment)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_KeyEncipherment: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_KeyEncipherment: CFString ``` |

Modified [kSecPolicyKU_NonRepudiation](https://developer.apple.com/documentation/security/ksecpolicyku_nonrepudiation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyKU_NonRepudiation: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyKU_NonRepudiation: CFString ``` |

Modified [kSecPolicyMacAppStoreReceipt](https://developer.apple.com/documentation/security/ksecpolicymacappstorereceipt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyMacAppStoreReceipt: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyMacAppStoreReceipt: CFString ``` |

Modified [kSecPolicyName](https://developer.apple.com/documentation/security/ksecpolicyname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyName: CFString ``` |

Modified [kSecPolicyOid](https://developer.apple.com/documentation/security/ksecpolicyoid)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyOid: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyOid: CFString ``` |

Modified [kSecPolicyRevocationFlags](https://developer.apple.com/documentation/security/ksecpolicyrevocationflags)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyRevocationFlags: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyRevocationFlags: CFString ``` |

Modified [kSecPolicyTeamIdentifier](https://developer.apple.com/documentation/security/ksecpolicyteamidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPolicyTeamIdentifier: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPolicyTeamIdentifier: CFString ``` |

Modified [kSecPrivateKeyAttrs](https://developer.apple.com/documentation/security/ksecprivatekeyattrs)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPrivateKeyAttrs: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPrivateKeyAttrs: CFString ``` |

Modified [kSecPropertyKeyLabel](https://developer.apple.com/documentation/security/ksecpropertykeylabel)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyKeyLabel: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyKeyLabel: CFString ``` |

Modified [kSecPropertyKeyLocalizedLabel](https://developer.apple.com/documentation/security/ksecpropertykeylocalizedlabel)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyKeyLocalizedLabel: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyKeyLocalizedLabel: CFString ``` |

Modified [kSecPropertyKeyType](https://developer.apple.com/documentation/security/ksecpropertykeytype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyKeyType: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyKeyType: CFString ``` |

Modified [kSecPropertyKeyValue](https://developer.apple.com/documentation/security/ksecpropertykeyvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyKeyValue: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyKeyValue: CFString ``` |

Modified [kSecPropertyTypeData](https://developer.apple.com/documentation/security/ksecpropertytypedata)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeData: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeData: CFString ``` |

Modified [kSecPropertyTypeDate](https://developer.apple.com/documentation/security/ksecpropertytypedate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeDate: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeDate: CFString ``` |

Modified [kSecPropertyTypeError](https://developer.apple.com/documentation/security/ksecpropertytypeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeError: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPropertyTypeError: CFString ``` |

Modified [kSecPropertyTypeSection](https://developer.apple.com/documentation/security/ksecpropertytypesection)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeSection: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeSection: CFString ``` |

Modified [kSecPropertyTypeString](https://developer.apple.com/documentation/security/ksecpropertytypestring)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeString: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeString: CFString ``` |

Modified [kSecPropertyTypeSuccess](https://developer.apple.com/documentation/security/ksecpropertytypesuccess)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeSuccess: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeSuccess: CFString ``` |

Modified [kSecPropertyTypeTitle](https://developer.apple.com/documentation/security/ksecpropertytypetitle)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeTitle: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPropertyTypeTitle: CFString ``` |

Modified [kSecPropertyTypeURL](https://developer.apple.com/documentation/security/ksecpropertytypeurl)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeURL: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeURL: CFString ``` |

Modified [kSecPropertyTypeWarning](https://developer.apple.com/documentation/security/ksecpropertytypewarning)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeWarning: Unmanaged<CFString>! ``` |
| To | ``` let kSecPropertyTypeWarning: CFString ``` |

Modified [kSecPublicKeyAttrs](https://developer.apple.com/documentation/security/ksecpublickeyattrs)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPublicKeyAttrs: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPublicKeyAttrs: CFString ``` |

Modified [kSecReadPermStatus](https://developer.apple.com/documentation/security/ksecreadpermstatus)

|  | Declaration |
| --- | --- |
| From | ``` var kSecReadPermStatus: Int { get } ``` |
| To | ``` var kSecReadPermStatus: UInt32 { get } ``` |

Modified [kSecReturnAttributes](https://developer.apple.com/documentation/security/ksecreturnattributes)

|  | Declaration |
| --- | --- |
| From | ``` let kSecReturnAttributes: CFStringRef ``` |
| To | ``` let kSecReturnAttributes: CFString ``` |

Modified [kSecReturnData](https://developer.apple.com/documentation/security/ksecreturndata)

|  | Declaration |
| --- | --- |
| From | ``` let kSecReturnData: CFStringRef ``` |
| To | ``` let kSecReturnData: CFString ``` |

Modified [kSecReturnPersistentRef](https://developer.apple.com/documentation/security/ksecreturnpersistentref)

|  | Declaration |
| --- | --- |
| From | ``` let kSecReturnPersistentRef: CFStringRef ``` |
| To | ``` let kSecReturnPersistentRef: CFString ``` |

Modified [kSecReturnRef](https://developer.apple.com/documentation/security/ksecreturnref)

|  | Declaration |
| --- | --- |
| From | ``` let kSecReturnRef: CFStringRef ``` |
| To | ``` let kSecReturnRef: CFString ``` |

Modified [kSecSignatureAttributeName](https://developer.apple.com/documentation/security/ksecsignatureattributename)

|  | Declaration |
| --- | --- |
| From | ``` var kSecSignatureAttributeName: Unmanaged<CFString>! ``` |
| To | ``` let kSecSignatureAttributeName: CFString ``` |

Modified [kSecTransformAbortAttributeName](https://developer.apple.com/documentation/security/ksectransformabortattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformAbortAttributeName: CFString! ``` |
| To | ``` let kSecTransformAbortAttributeName: CFString ``` |

Modified [kSecTransformAbortOriginatorKey](https://developer.apple.com/documentation/security/ksectransformabortoriginatorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformAbortOriginatorKey: CFString! ``` |
| To | ``` let kSecTransformAbortOriginatorKey: CFString ``` |

Modified [kSecTransformActionAttributeNotification](https://developer.apple.com/documentation/security/ksectransformactionattributenotification)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionAttributeNotification: CFString! ``` |
| To | ``` let kSecTransformActionAttributeNotification: CFString ``` |

Modified [kSecTransformActionAttributeValidation](https://developer.apple.com/documentation/security/ksectransformactionattributevalidation)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionAttributeValidation: CFString! ``` |
| To | ``` let kSecTransformActionAttributeValidation: CFString ``` |

Modified [kSecTransformActionCanExecute](https://developer.apple.com/documentation/security/ksectransformactioncanexecute)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionCanExecute: CFString! ``` |
| To | ``` let kSecTransformActionCanExecute: CFString ``` |

Modified [kSecTransformActionExternalizeExtraData](https://developer.apple.com/documentation/security/ksectransformactionexternalizeextradata)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionExternalizeExtraData: CFString! ``` |
| To | ``` let kSecTransformActionExternalizeExtraData: CFString ``` |

Modified [kSecTransformActionFinalize](https://developer.apple.com/documentation/security/ksectransformactionfinalize)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionFinalize: CFString! ``` |
| To | ``` let kSecTransformActionFinalize: CFString ``` |

Modified [kSecTransformActionInternalizeExtraData](https://developer.apple.com/documentation/security/ksectransformactioninternalizeextradata)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionInternalizeExtraData: CFString! ``` |
| To | ``` let kSecTransformActionInternalizeExtraData: CFString ``` |

Modified [kSecTransformActionProcessData](https://developer.apple.com/documentation/security/ksectransformactionprocessdata)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionProcessData: CFString! ``` |
| To | ``` let kSecTransformActionProcessData: CFString ``` |

Modified [kSecTransformActionStartingExecution](https://developer.apple.com/documentation/security/ksectransformactionstartingexecution)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformActionStartingExecution: CFString! ``` |
| To | ``` let kSecTransformActionStartingExecution: CFString ``` |

Modified [kSecTransformDebugAttributeName](https://developer.apple.com/documentation/security/ksectransformdebugattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformDebugAttributeName: CFString! ``` |
| To | ``` let kSecTransformDebugAttributeName: CFString ``` |

Modified [kSecTransformErrorAborted](https://developer.apple.com/documentation/security/ksectransformerroraborted)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorAborted: Int { get } ``` |
| To | ``` var kSecTransformErrorAborted: CFIndex { get } ``` |

Modified [kSecTransformErrorAbortInProgress](https://developer.apple.com/documentation/security/ksectransformerrorabortinprogress)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorAbortInProgress: Int { get } ``` |
| To | ``` var kSecTransformErrorAbortInProgress: CFIndex { get } ``` |

Modified [kSecTransformErrorAttributeNotFound](https://developer.apple.com/documentation/security/ksectransformerrorattributenotfound)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorAttributeNotFound: Int { get } ``` |
| To | ``` var kSecTransformErrorAttributeNotFound: CFIndex { get } ``` |

Modified [kSecTransformErrorDomain](https://developer.apple.com/documentation/security/ksectransformerrordomain)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformErrorDomain: CFString! ``` |
| To | ``` let kSecTransformErrorDomain: CFString ``` |

Modified [kSecTransformErrorInvalidAlgorithm](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidAlgorithm: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidAlgorithm: CFIndex { get } ``` |

Modified [kSecTransformErrorInvalidConnection](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidconnection)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidConnection: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidConnection: CFIndex { get } ``` |

Modified [kSecTransformErrorInvalidInput](https://developer.apple.com/documentation/security/ksectransformerrorinvalidinput)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidInput: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidInput: CFIndex { get } ``` |

Modified [kSecTransformErrorInvalidInputDictionary](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidinputdictionary)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidInputDictionary: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidInputDictionary: CFIndex { get } ``` |

Modified [kSecTransformErrorInvalidLength](https://developer.apple.com/documentation/security/ksectransformerrorinvalidlength)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidLength: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidLength: CFIndex { get } ``` |

Modified [kSecTransformErrorInvalidOperation](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidoperation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidOperation: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidOperation: CFIndex { get } ``` |

Modified [kSecTransformErrorInvalidType](https://developer.apple.com/documentation/security/ksectransformerrorinvalidtype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorInvalidType: Int { get } ``` |
| To | ``` var kSecTransformErrorInvalidType: CFIndex { get } ``` |

Modified [kSecTransformErrorMissingParameter](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrormissingparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorMissingParameter: Int { get } ``` |
| To | ``` var kSecTransformErrorMissingParameter: CFIndex { get } ``` |

Modified [kSecTransformErrorMoreThanOneOutput](https://developer.apple.com/documentation/security/ksectransformerrormorethanoneoutput)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorMoreThanOneOutput: Int { get } ``` |
| To | ``` var kSecTransformErrorMoreThanOneOutput: CFIndex { get } ``` |

Modified [kSecTransformErrorNameAlreadyRegistered](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrornamealreadyregistered)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorNameAlreadyRegistered: Int { get } ``` |
| To | ``` var kSecTransformErrorNameAlreadyRegistered: CFIndex { get } ``` |

Modified [kSecTransformErrorNotInitializedCorrectly](https://developer.apple.com/documentation/security/ksectransformerrornotinitializedcorrectly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorNotInitializedCorrectly: Int { get } ``` |
| To | ``` var kSecTransformErrorNotInitializedCorrectly: CFIndex { get } ``` |

Modified [kSecTransformErrorUnsupportedAttribute](https://developer.apple.com/documentation/security/ksectransformerrorunsupportedattribute)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformErrorUnsupportedAttribute: Int { get } ``` |
| To | ``` var kSecTransformErrorUnsupportedAttribute: CFIndex { get } ``` |

Modified [kSecTransformInputAttributeName](https://developer.apple.com/documentation/security/ksectransforminputattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformInputAttributeName: CFString! ``` |
| To | ``` let kSecTransformInputAttributeName: CFString ``` |

Modified [kSecTransformInvalidArgument](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransforminvalidargument)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformInvalidArgument: Int { get } ``` |
| To | ``` var kSecTransformInvalidArgument: CFIndex { get } ``` |

Modified [kSecTransformInvalidOverride](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransforminvalidoverride)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformInvalidOverride: Int { get } ``` |
| To | ``` var kSecTransformInvalidOverride: CFIndex { get } ``` |

Modified [kSecTransformOperationNotSupportedOnGroup](https://developer.apple.com/documentation/security/ksectransformoperationnotsupportedongroup)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformOperationNotSupportedOnGroup: Int { get } ``` |
| To | ``` var kSecTransformOperationNotSupportedOnGroup: CFIndex { get } ``` |

Modified [kSecTransformOutputAttributeName](https://developer.apple.com/documentation/security/ksectransformoutputattributename)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformOutputAttributeName: CFString! ``` |
| To | ``` let kSecTransformOutputAttributeName: CFString ``` |

Modified [kSecTransformPreviousErrorKey](https://developer.apple.com/documentation/security/ksectransformpreviouserrorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformPreviousErrorKey: CFString! ``` |
| To | ``` let kSecTransformPreviousErrorKey: CFString ``` |

Modified [kSecTransformTransformIsExecuting](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformtransformisexecuting)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformTransformIsExecuting: Int { get } ``` |
| To | ``` var kSecTransformTransformIsExecuting: CFIndex { get } ``` |

Modified [kSecTransformTransformIsNotRegistered](https://developer.apple.com/documentation/security/ksectransformtransformisnotregistered)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTransformTransformIsNotRegistered: Int { get } ``` |
| To | ``` var kSecTransformTransformIsNotRegistered: CFIndex { get } ``` |

Modified [kSecTransformTransformName](https://developer.apple.com/documentation/security/ksectransformtransformname)

|  | Declaration |
| --- | --- |
| From | ``` let kSecTransformTransformName: CFString! ``` |
| To | ``` let kSecTransformTransformName: CFString ``` |

Modified [kSecTrustEvaluationDate](https://developer.apple.com/documentation/security/ksectrustevaluationdate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTrustEvaluationDate: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecTrustEvaluationDate: CFString ``` |

Modified [kSecTrustExtendedValidation](https://developer.apple.com/documentation/security/ksectrustextendedvalidation)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTrustExtendedValidation: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecTrustExtendedValidation: CFString ``` |

Modified [kSecTrustOrganizationName](https://developer.apple.com/documentation/security/ksectrustorganizationname)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTrustOrganizationName: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecTrustOrganizationName: CFString ``` |

Modified [kSecTrustResultValue](https://developer.apple.com/documentation/security/ksectrustresultvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTrustResultValue: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecTrustResultValue: CFString ``` |

Modified [kSecTrustRevocationChecked](https://developer.apple.com/documentation/security/ksectrustrevocationchecked)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTrustRevocationChecked: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecTrustRevocationChecked: CFString ``` |

Modified [kSecTrustRevocationValidUntilDate](https://developer.apple.com/documentation/security/ksectrustrevocationvaliduntildate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecTrustRevocationValidUntilDate: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecTrustRevocationValidUntilDate: CFString ``` |

Modified [kSecUnlockStateStatus](https://developer.apple.com/documentation/security/1536090-seckeychainstatus_values/ksecunlockstatestatus)

|  | Declaration |
| --- | --- |
| From | ``` var kSecUnlockStateStatus: Int { get } ``` |
| To | ``` var kSecUnlockStateStatus: UInt32 { get } ``` |

Modified [kSecUseItemList](https://developer.apple.com/documentation/security/ksecuseitemlist)

|  | Declaration |
| --- | --- |
| From | ``` let kSecUseItemList: CFStringRef ``` |
| To | ``` let kSecUseItemList: CFString ``` |

Modified [kSecUseKeychain](https://developer.apple.com/documentation/security/ksecusekeychain)

|  | Declaration |
| --- | --- |
| From | ``` let kSecUseKeychain: CFStringRef ``` |
| To | ``` let kSecUseKeychain: CFString ``` |

Modified [kSecValueData](https://developer.apple.com/documentation/security/ksecvaluedata)

|  | Declaration |
| --- | --- |
| From | ``` let kSecValueData: CFStringRef ``` |
| To | ``` let kSecValueData: CFString ``` |

Modified [kSecValuePersistentRef](https://developer.apple.com/documentation/security/ksecvaluepersistentref)

|  | Declaration |
| --- | --- |
| From | ``` let kSecValuePersistentRef: CFStringRef ``` |
| To | ``` let kSecValuePersistentRef: CFString ``` |

Modified [kSecValueRef](https://developer.apple.com/documentation/security/ksecvalueref)

|  | Declaration |
| --- | --- |
| From | ``` let kSecValueRef: CFStringRef ``` |
| To | ``` let kSecValueRef: CFString ``` |

Modified [kSecWritePermStatus](https://developer.apple.com/documentation/security/1536090-seckeychainstatus_values/ksecwritepermstatus)

|  | Declaration |
| --- | --- |
| From | ``` var kSecWritePermStatus: Int { get } ``` |
| To | ``` var kSecWritePermStatus: UInt32 { get } ``` |

Modified [kSecZLibEncoding](https://developer.apple.com/documentation/security/kseczlibencoding)

|  | Declaration |
| --- | --- |
| From | ``` let kSecZLibEncoding: CFString! ``` |
| To | ``` let kSecZLibEncoding: CFString ``` |

Modified [SecAccessControlCreateWithFlags(_: CFAllocator?, _: AnyObject, _: SecAccessControlCreateFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccessControl?](https://developer.apple.com/documentation/security/1394452-secaccesscontrolcreatewithflags)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator!, _ protection: AnyObject!, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccessControl>! ``` |
| To | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: AnyObject, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccessControl? ``` |

Modified [SecAccessCopyACLList(_: SecAccess, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1398213-secaccesscopyacllist)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCopyACLList(_ accessRef: SecAccess!, _ aclList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecAccessCopyACLList(_ accessRef: SecAccess, _ aclList: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecAccessCopyMatchingACLList(_: SecAccess, _: AnyObject) -> CFArray?](https://developer.apple.com/documentation/security/1400464-secaccesscopymatchingacllist)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCopyMatchingACLList(_ accessRef: SecAccess!, _ authorizationTag: AnyObject!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SecAccessCopyMatchingACLList(_ accessRef: SecAccess, _ authorizationTag: AnyObject) -> CFArray? ``` |

Modified [SecAccessCopyOwnerAndACL(_: SecAccess, _: UnsafeMutablePointer<uid_t>, _: UnsafeMutablePointer<gid_t>, _: UnsafeMutablePointer<SecAccessOwnerType>, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1402089-secaccesscopyownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess!, _ userId: UnsafeMutablePointer<uid_t>, _ groupId: UnsafeMutablePointer<gid_t>, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>, _ aclList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess, _ userId: UnsafeMutablePointer<uid_t>, _ groupId: UnsafeMutablePointer<gid_t>, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>, _ aclList: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecAccessCreate(_: CFString, _: CFArray?, _: UnsafeMutablePointer<SecAccess?>) -> OSStatus](https://developer.apple.com/documentation/security/1393522-secaccesscreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCreate(_ descriptor: CFString!, _ trustedlist: CFArray!, _ accessRef: UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |
| To | ``` func SecAccessCreate(_ descriptor: CFString, _ trustedlist: CFArray?, _ accessRef: UnsafeMutablePointer<SecAccess?>) -> OSStatus ``` |

Modified [SecAccessCreateWithOwnerAndACL(_: uid_t, _: gid_t, _: SecAccessOwnerType, _: CFArray?, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccess?](https://developer.apple.com/documentation/security/1395706-secaccesscreatewithownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccess>! ``` |
| To | ``` func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccess? ``` |

Modified [SecACLCopyAuthorizations(_: SecACL) -> CFArray](https://developer.apple.com/documentation/security/1396830-secaclcopyauthorizations)

|  | Declaration |
| --- | --- |
| From | ``` func SecACLCopyAuthorizations(_ acl: SecACL!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SecACLCopyAuthorizations(_ acl: SecACL) -> CFArray ``` |

Modified [SecACLCopyContents(_: SecACL, _: UnsafeMutablePointer<CFArray?>, _: UnsafeMutablePointer<CFString?>, _: UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus](https://developer.apple.com/documentation/security/1400970-secaclcopycontents)

|  | Declaration |
| --- | --- |
| From | ``` func SecACLCopyContents(_ acl: SecACL!, _ applicationList: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>, _ promptSelector: UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus ``` |
| To | ``` func SecACLCopyContents(_ acl: SecACL, _ applicationList: UnsafeMutablePointer<CFArray?>, _ description: UnsafeMutablePointer<CFString?>, _ promptSelector: UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus ``` |

Modified [SecACLCreateWithSimpleContents(_: SecAccess, _: CFArray?, _: CFString, _: SecKeychainPromptSelector, _: UnsafeMutablePointer<SecACL?>) -> OSStatus](https://developer.apple.com/documentation/security/1402295-secaclcreatewithsimplecontents)

|  | Declaration |
| --- | --- |
| From | ``` func SecACLCreateWithSimpleContents(_ access: SecAccess!, _ applicationList: CFArray!, _ description: CFString!, _ promptSelector: SecKeychainPromptSelector, _ newAcl: UnsafeMutablePointer<Unmanaged<SecACL>?>) -> OSStatus ``` |
| To | ``` func SecACLCreateWithSimpleContents(_ access: SecAccess, _ applicationList: CFArray?, _ description: CFString, _ promptSelector: SecKeychainPromptSelector, _ newAcl: UnsafeMutablePointer<SecACL?>) -> OSStatus ``` |

Modified [SecACLRemove(_: SecACL) -> OSStatus](https://developer.apple.com/documentation/security/1398788-secaclremove)

|  | Declaration |
| --- | --- |
| From | ``` func SecACLRemove(_ aclRef: SecACL!) -> OSStatus ``` |
| To | ``` func SecACLRemove(_ aclRef: SecACL) -> OSStatus ``` |

Modified [SecACLSetContents(_: SecACL, _: CFArray?, _: CFString, _: SecKeychainPromptSelector) -> OSStatus](https://developer.apple.com/documentation/security/1400997-secaclsetcontents)

|  | Declaration |
| --- | --- |
| From | ``` func SecACLSetContents(_ acl: SecACL!, _ applicationList: CFArray!, _ description: CFString!, _ promptSelector: SecKeychainPromptSelector) -> OSStatus ``` |
| To | ``` func SecACLSetContents(_ acl: SecACL, _ applicationList: CFArray?, _ description: CFString, _ promptSelector: SecKeychainPromptSelector) -> OSStatus ``` |

Modified [SecACLUpdateAuthorizations(_: SecACL, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/security/1392184-secaclupdateauthorizations)

|  | Declaration |
| --- | --- |
| From | ``` func SecACLUpdateAuthorizations(_ acl: SecACL!, _ authorizations: CFArray!) -> OSStatus ``` |
| To | ``` func SecACLUpdateAuthorizations(_ acl: SecACL, _ authorizations: CFArray) -> OSStatus ``` |

Modified [SecAsn1TemplateChooser](https://developer.apple.com/documentation/security/secasn1templatechooser)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1TemplateChooser = (UnsafeMutablePointer<Void>, Boolean, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> UnsafePointer<SecAsn1Template> ``` |
| To | ``` typealias SecAsn1TemplateChooser = (UnsafeMutablePointer<Void>, DarwinBoolean, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> UnsafePointer<SecAsn1Template> ``` |

Modified [SecAsn1TemplateChooserPtr](https://developer.apple.com/documentation/security/secasn1templatechooserptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1TemplateChooserPtr = CFunctionPointer<SecAsn1TemplateChooser> ``` |
| To | ``` typealias SecAsn1TemplateChooserPtr = (UnsafeMutablePointer<Void>, DarwinBoolean, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> UnsafePointer<SecAsn1Template> ``` |

Modified [SecCertificateAddToKeychain(_: SecCertificate, _: SecKeychain?) -> OSStatus](https://developer.apple.com/documentation/security/1396090-seccertificateaddtokeychain)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateAddToKeychain(_ certificate: SecCertificate!, _ keychain: SecKeychain!) -> OSStatus ``` |
| To | ``` func SecCertificateAddToKeychain(_ certificate: SecCertificate, _ keychain: SecKeychain?) -> OSStatus ``` |

Modified [SecCertificateCopyCommonName(_: SecCertificate, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/security/1394814-seccertificatecopycommonname)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyCommonName(_ certificate: SecCertificate!, _ commonName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func SecCertificateCopyCommonName(_ certificate: SecCertificate, _ commonName: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [SecCertificateCopyData(_: SecCertificate) -> CFData](https://developer.apple.com/documentation/security/1396080-seccertificatecopydata)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyData(_ certificate: SecCertificate!) -> Unmanaged<CFData>! ``` |
| To | ``` func SecCertificateCopyData(_ certificate: SecCertificate) -> CFData ``` |

Modified [SecCertificateCopyEmailAddresses(_: SecCertificate, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1396049-seccertificatecopyemailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyEmailAddresses(_ certificate: SecCertificate!, _ emailAddresses: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecCertificateCopyEmailAddresses(_ certificate: SecCertificate, _ emailAddresses: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecCertificateCopyLongDescription(_: CFAllocator?, _: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFString?](https://developer.apple.com/documentation/security/1396088-seccertificatecopylongdescriptio)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyLongDescription(_ alloc: CFAllocator!, _ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>! ``` |
| To | ``` func SecCertificateCopyLongDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFString? ``` |

Modified [SecCertificateCopyNormalizedIssuerContent(_: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData?](https://developer.apple.com/documentation/security/1392318-seccertificatecopynormalizedissu)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |

Modified [SecCertificateCopyNormalizedSubjectContent(_: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData?](https://developer.apple.com/documentation/security/1396030-seccertificatecopynormalizedsubj)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |

Modified [SecCertificateCopyPreferred(_: CFString, _: CFArray?) -> SecCertificate?](https://developer.apple.com/documentation/security/1396028-seccertificatecopypreferred)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyPreferred(_ name: CFString!, _ keyUsage: CFArray!) -> Unmanaged<SecCertificate>! ``` |
| To | ``` func SecCertificateCopyPreferred(_ name: CFString, _ keyUsage: CFArray?) -> SecCertificate? ``` |

Modified [SecCertificateCopyPublicKey(_: SecCertificate, _: UnsafeMutablePointer<SecKey?>) -> OSStatus](https://developer.apple.com/documentation/security/1396096-seccertificatecopypublickey)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyPublicKey(_ certificate: SecCertificate!, _ key: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` |
| To | ``` func SecCertificateCopyPublicKey(_ certificate: SecCertificate, _ key: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |

Modified [SecCertificateCopySerialNumber(_: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData?](https://developer.apple.com/documentation/security/1394241-seccertificatecopyserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopySerialNumber(_ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func SecCertificateCopySerialNumber(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |

Modified [SecCertificateCopyShortDescription(_: CFAllocator?, _: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFString?](https://developer.apple.com/documentation/security/1396036-seccertificatecopyshortdescripti)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyShortDescription(_ alloc: CFAllocator!, _ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>! ``` |
| To | ``` func SecCertificateCopyShortDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFString? ``` |

Modified [SecCertificateCopySubjectSummary(_: SecCertificate) -> CFString](https://developer.apple.com/documentation/security/1396041-seccertificatecopysubjectsummary)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopySubjectSummary(_ certificate: SecCertificate!) -> Unmanaged<CFString>! ``` |
| To | ``` func SecCertificateCopySubjectSummary(_ certificate: SecCertificate) -> CFString ``` |

Modified [SecCertificateCopyValues(_: SecCertificate, _: CFArray?, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary?](https://developer.apple.com/documentation/security/1396051-seccertificatecopyvalues)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyValues(_ certificate: SecCertificate!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SecCertificateCopyValues(_ certificate: SecCertificate, _ keys: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary? ``` |

Modified [SecCertificateCreateWithData(_: CFAllocator?, _: CFData) -> SecCertificate?](https://developer.apple.com/documentation/security/1396073-seccertificatecreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCreateWithData(_ allocator: CFAllocator!, _ data: CFData!) -> Unmanaged<SecCertificate>! ``` |
| To | ``` func SecCertificateCreateWithData(_ allocator: CFAllocator?, _ data: CFData) -> SecCertificate? ``` |

Modified [SecCertificateSetPreference(_: SecCertificate, _: CFString, _: uint32, _: CFDate?) -> OSStatus](https://developer.apple.com/documentation/security/1396063-seccertificatesetpreference)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateSetPreference(_ certificate: SecCertificate!, _ name: CFString!, _ keyUsage: uint32, _ date: CFDate!) -> OSStatus ``` |
| To | ``` func SecCertificateSetPreference(_ certificate: SecCertificate, _ name: CFString, _ keyUsage: uint32, _ date: CFDate?) -> OSStatus ``` |

Modified [SecCertificateSetPreferred(_: SecCertificate?, _: CFString, _: CFArray?) -> OSStatus](https://developer.apple.com/documentation/security/1393683-seccertificatesetpreferred)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateSetPreferred(_ certificate: SecCertificate!, _ name: CFString!, _ keyUsage: CFArray!) -> OSStatus ``` |
| To | ``` func SecCertificateSetPreferred(_ certificate: SecCertificate?, _ name: CFString, _ keyUsage: CFArray?) -> OSStatus ``` |

Modified [SecCodeCheckValidity(_: SecCode, _: SecCSFlags, _: SecRequirement?) -> OSStatus](https://developer.apple.com/documentation/security/1396726-seccodecheckvalidity)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCheckValidity(_ code: SecCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!) -> OSStatus ``` |
| To | ``` func SecCodeCheckValidity(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?) -> OSStatus ``` |

Modified [SecCodeCheckValidityWithErrors(_: SecCode, _: SecCSFlags, _: SecRequirement?, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus](https://developer.apple.com/documentation/security/1395272-seccodecheckvaliditywitherrors)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCheckValidityWithErrors(_ code: SecCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |
| To | ``` func SecCodeCheckValidityWithErrors(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |

Modified [SecCodeCopyDesignatedRequirement(_: SecStaticCode, _: SecCSFlags, _: UnsafeMutablePointer<SecRequirement?>) -> OSStatus](https://developer.apple.com/documentation/security/1397726-seccodecopydesignatedrequirement)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyDesignatedRequirement(_ code: SecStaticCode!, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyDesignatedRequirement(_ code: SecStaticCode, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus ``` |

Modified [SecCodeCopyGuestWithAttributes(_: SecCode?, _: CFDictionary?, _: SecCSFlags, _: UnsafeMutablePointer<SecCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1395560-seccodecopyguestwithattributes)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyGuestWithAttributes(_ host: SecCode!, _ attributes: CFDictionary!, _ flags: SecCSFlags, _ guest: UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyGuestWithAttributes(_ host: SecCode?, _ attributes: CFDictionary?, _ flags: SecCSFlags, _ guest: UnsafeMutablePointer<SecCode?>) -> OSStatus ``` |

Modified [SecCodeCopyHost(_: SecCode, _: SecCSFlags, _: UnsafeMutablePointer<SecCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1398794-seccodecopyhost)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyHost(_ guest: SecCode!, _ flags: SecCSFlags, _ host: UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyHost(_ guest: SecCode, _ flags: SecCSFlags, _ host: UnsafeMutablePointer<SecCode?>) -> OSStatus ``` |

Modified [SecCodeCopyPath(_: SecStaticCode, _: SecCSFlags, _: UnsafeMutablePointer<CFURL?>) -> OSStatus](https://developer.apple.com/documentation/security/1398853-seccodecopypath)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyPath(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ path: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyPath(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ path: UnsafeMutablePointer<CFURL?>) -> OSStatus ``` |

Modified [SecCodeCopySelf(_: SecCSFlags, _: UnsafeMutablePointer<SecCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1402140-seccodecopyself)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopySelf(_ flags: SecCSFlags, _ `self`: UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopySelf(_ flags: SecCSFlags, _ `self`: UnsafeMutablePointer<SecCode?>) -> OSStatus ``` |

Modified [SecCodeCopySigningInformation(_: SecStaticCode, _: SecCSFlags, _: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](https://developer.apple.com/documentation/security/1395809-seccodecopysigninginformation)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopySigningInformation(_ code: SecStaticCode!, _ flags: SecCSFlags, _ information: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopySigningInformation(_ code: SecStaticCode, _ flags: SecCSFlags, _ information: UnsafeMutablePointer<CFDictionary?>) -> OSStatus ``` |

Modified [SecCodeCopyStaticCode(_: SecCode, _: SecCSFlags, _: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1401695-seccodecopystaticcode)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyStaticCode(_ code: SecCode!, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyStaticCode(_ code: SecCode, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus ``` |

Modified [SecCodeMapMemory(_: SecStaticCode, _: SecCSFlags) -> OSStatus](https://developer.apple.com/documentation/security/1393719-seccodemapmemory)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeMapMemory(_ code: SecStaticCode!, _ flags: SecCSFlags) -> OSStatus ``` |
| To | ``` func SecCodeMapMemory(_ code: SecStaticCode, _ flags: SecCSFlags) -> OSStatus ``` |

Modified [SecCopyErrorMessageString(_: OSStatus, _: UnsafeMutablePointer<Void>) -> CFString?](https://developer.apple.com/documentation/security/1394686-seccopyerrormessagestring)

|  | Declaration |
| --- | --- |
| From | ``` func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutablePointer<Void>) -> Unmanaged<CFString>! ``` |
| To | ``` func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutablePointer<Void>) -> CFString? ``` |

Modified [SecDecodeTransformCreate(_: AnyObject, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform?](https://developer.apple.com/documentation/security/1395244-secdecodetransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecDecodeTransformCreate(_ DecodeType: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecDecodeTransformCreate(_ DecodeType: AnyObject, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |

Modified [SecDecryptTransformCreate(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform](https://developer.apple.com/documentation/security/1399526-secdecrypttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecDecryptTransformCreate(_ keyRef: SecKey!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecDecryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform ``` |

Modified [SecDigestTransformCreate(_: AnyObject?, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform](https://developer.apple.com/documentation/security/1394846-secdigesttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecDigestTransformCreate(_ digestType: AnyObject!, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecDigestTransformCreate(_ digestType: AnyObject?, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform ``` |

Modified [SecEncodeTransformCreate(_: AnyObject, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform?](https://developer.apple.com/documentation/security/1399382-secencodetransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecEncodeTransformCreate(_ encodeType: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecEncodeTransformCreate(_ encodeType: AnyObject, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |

Modified [SecEncryptTransformCreate(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform](https://developer.apple.com/documentation/security/1399605-secencrypttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecEncryptTransformCreate(_ keyRef: SecKey!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecEncryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform ``` |

Modified [SecHostCreateGuest(_: SecGuestRef, _: UInt32, _: CFURL, _: CFDictionary?, _: SecCSFlags, _: UnsafeMutablePointer<SecGuestRef>) -> OSStatus](https://developer.apple.com/documentation/security/1396597-sechostcreateguest)

|  | Declaration |
| --- | --- |
| From | ``` func SecHostCreateGuest(_ host: SecGuestRef, _ status: UInt32, _ path: CFURL!, _ attributes: CFDictionary!, _ flags: SecCSFlags, _ newGuest: UnsafeMutablePointer<SecGuestRef>) -> OSStatus ``` |
| To | ``` func SecHostCreateGuest(_ host: SecGuestRef, _ status: UInt32, _ path: CFURL, _ attributes: CFDictionary?, _ flags: SecCSFlags, _ newGuest: UnsafeMutablePointer<SecGuestRef>) -> OSStatus ``` |

Modified [SecHostSetGuestStatus(_: SecGuestRef, _: UInt32, _: CFDictionary?, _: SecCSFlags) -> OSStatus](https://developer.apple.com/documentation/security/1397494-sechostsetgueststatus)

|  | Declaration |
| --- | --- |
| From | ``` func SecHostSetGuestStatus(_ guestRef: SecGuestRef, _ status: UInt32, _ attributes: CFDictionary!, _ flags: SecCSFlags) -> OSStatus ``` |
| To | ``` func SecHostSetGuestStatus(_ guestRef: SecGuestRef, _ status: UInt32, _ attributes: CFDictionary?, _ flags: SecCSFlags) -> OSStatus ``` |

Modified [SecIdentityCopyCertificate(_: SecIdentity, _: UnsafeMutablePointer<SecCertificate?>) -> OSStatus](https://developer.apple.com/documentation/security/1401305-secidentitycopycertificate)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopyCertificate(_ identityRef: SecIdentity!, _ certificateRef: UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` |
| To | ``` func SecIdentityCopyCertificate(_ identityRef: SecIdentity, _ certificateRef: UnsafeMutablePointer<SecCertificate?>) -> OSStatus ``` |

Modified [SecIdentityCopyPreferred(_: CFString, _: CFArray?, _: CFArray?) -> SecIdentity?](https://developer.apple.com/documentation/security/1399556-secidentitycopypreferred)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopyPreferred(_ name: CFString!, _ keyUsage: CFArray!, _ validIssuers: CFArray!) -> Unmanaged<SecIdentity>! ``` |
| To | ``` func SecIdentityCopyPreferred(_ name: CFString, _ keyUsage: CFArray?, _ validIssuers: CFArray?) -> SecIdentity? ``` |

Modified [SecIdentityCopyPrivateKey(_: SecIdentity, _: UnsafeMutablePointer<SecKey?>) -> OSStatus](https://developer.apple.com/documentation/security/1392978-secidentitycopyprivatekey)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity!, _ privateKeyRef: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` |
| To | ``` func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity, _ privateKeyRef: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |

Modified [SecIdentityCopySystemIdentity(_: CFString, _: UnsafeMutablePointer<SecIdentity?>, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/security/1393646-secidentitycopysystemidentity)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopySystemIdentity(_ domain: CFString!, _ idRef: UnsafeMutablePointer<Unmanaged<SecIdentity>?>, _ actualDomain: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func SecIdentityCopySystemIdentity(_ domain: CFString, _ idRef: UnsafeMutablePointer<SecIdentity?>, _ actualDomain: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [SecIdentityCreateWithCertificate(_: AnyObject?, _: SecCertificate, _: UnsafeMutablePointer<SecIdentity?>) -> OSStatus](https://developer.apple.com/documentation/security/1401160-secidentitycreatewithcertificate)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCreateWithCertificate(_ keychainOrArray: AnyObject!, _ certificateRef: SecCertificate!, _ identityRef: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` |
| To | ``` func SecIdentityCreateWithCertificate(_ keychainOrArray: AnyObject?, _ certificateRef: SecCertificate, _ identityRef: UnsafeMutablePointer<SecIdentity?>) -> OSStatus ``` |

Modified [SecIdentitySetPreferred(_: SecIdentity?, _: CFString, _: CFArray?) -> OSStatus](https://developer.apple.com/documentation/security/1395862-secidentitysetpreferred)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentitySetPreferred(_ identity: SecIdentity!, _ name: CFString!, _ keyUsage: CFArray!) -> OSStatus ``` |
| To | ``` func SecIdentitySetPreferred(_ identity: SecIdentity?, _ name: CFString, _ keyUsage: CFArray?) -> OSStatus ``` |

Modified [SecIdentitySetSystemIdentity(_: CFString, _: SecIdentity?) -> OSStatus](https://developer.apple.com/documentation/security/1398082-secidentitysetsystemidentity)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentitySetSystemIdentity(_ domain: CFString!, _ idRef: SecIdentity!) -> OSStatus ``` |
| To | ``` func SecIdentitySetSystemIdentity(_ domain: CFString, _ idRef: SecIdentity?) -> OSStatus ``` |

Modified [SecItemAdd(_: CFDictionary, _: UnsafeMutablePointer<AnyObject?>) -> OSStatus](https://developer.apple.com/documentation/security/1401659-secitemadd)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemAdd(_ attributes: CFDictionary!, _ result: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func SecItemAdd(_ attributes: CFDictionary, _ result: UnsafeMutablePointer<AnyObject?>) -> OSStatus ``` |

Modified [SecItemCopyMatching(_: CFDictionary, _: UnsafeMutablePointer<AnyObject?>) -> OSStatus](https://developer.apple.com/documentation/security/1398306-secitemcopymatching)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemCopyMatching(_ query: CFDictionary!, _ result: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func SecItemCopyMatching(_ query: CFDictionary, _ result: UnsafeMutablePointer<AnyObject?>) -> OSStatus ``` |

Modified [SecItemDelete(_: CFDictionary) -> OSStatus](https://developer.apple.com/documentation/security/1395547-secitemdelete)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemDelete(_ query: CFDictionary!) -> OSStatus ``` |
| To | ``` func SecItemDelete(_ query: CFDictionary) -> OSStatus ``` |

Modified [SecItemExport(_: AnyObject, _: SecExternalFormat, _: SecItemImportExportFlags, _: UnsafePointer<SecItemImportExportKeyParameters>, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1394828-secitemexport)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemExport(_ secItemOrArray: AnyObject!, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ exportedData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecItemExport(_ secItemOrArray: AnyObject, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ exportedData: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [SecItemImport(_: CFData, _: CFString?, _: UnsafeMutablePointer<SecExternalFormat>, _: UnsafeMutablePointer<SecExternalItemType>, _: SecItemImportExportFlags, _: UnsafePointer<SecItemImportExportKeyParameters>, _: SecKeychain?, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1395728-secitemimport)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemImport(_ importedData: CFData!, _ fileNameOrExtension: CFString!, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>, _ itemType: UnsafeMutablePointer<SecExternalItemType>, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ importKeychain: SecKeychain!, _ outItems: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecItemImport(_ importedData: CFData, _ fileNameOrExtension: CFString?, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>, _ itemType: UnsafeMutablePointer<SecExternalItemType>, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ importKeychain: SecKeychain?, _ outItems: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecItemUpdate(_: CFDictionary, _: CFDictionary) -> OSStatus](https://developer.apple.com/documentation/security/1393617-secitemupdate)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemUpdate(_ query: CFDictionary!, _ attributesToUpdate: CFDictionary!) -> OSStatus ``` |
| To | ``` func SecItemUpdate(_ query: CFDictionary, _ attributesToUpdate: CFDictionary) -> OSStatus ``` |

Modified [SecKeychainAddGenericPassword(_: SecKeychain?, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Void>, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1398366-seckeychainaddgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddGenericPassword(_ keychain: SecKeychain!, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddGenericPassword(_ keychain: SecKeychain?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainAddInternetPassword(_: SecKeychain?, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt16, _: SecProtocolType, _: SecAuthenticationType, _: UInt32, _: UnsafePointer<Void>, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1393322-seckeychainaddinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain!, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainAttributeInfoForItemID(_: SecKeychain?, _: UInt32, _: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>>) -> OSStatus](https://developer.apple.com/documentation/security/1392372-seckeychainattributeinfoforitemi)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain!, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>>) -> OSStatus ``` |
| To | ``` func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain?, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>>) -> OSStatus ``` |

Modified [SecKeychainCallback](https://developer.apple.com/documentation/security/seckeychaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecKeychainCallback = CFunctionPointer<((SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias SecKeychainCallback = (SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [SecKeychainCopyAccess(_: SecKeychain?, _: UnsafeMutablePointer<SecAccess?>) -> OSStatus](https://developer.apple.com/documentation/security/1394733-seckeychaincopyaccess)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyAccess(_ keychain: SecKeychain!, _ access: UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyAccess(_ keychain: SecKeychain?, _ access: UnsafeMutablePointer<SecAccess?>) -> OSStatus ``` |

Modified [SecKeychainCopyDefault(_: UnsafeMutablePointer<SecKeychain?>) -> OSStatus](https://developer.apple.com/documentation/security/1400743-seckeychaincopydefault)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyDefault(_ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyDefault(_ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |

Modified [SecKeychainCopyDomainDefault(_: SecPreferencesDomain, _: UnsafeMutablePointer<SecKeychain?>) -> OSStatus](https://developer.apple.com/documentation/security/1401993-seckeychaincopydomaindefault)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyDomainDefault(_ domain: SecPreferencesDomain, _ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyDomainDefault(_ domain: SecPreferencesDomain, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |

Modified [SecKeychainCopyDomainSearchList(_: SecPreferencesDomain, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1396688-seckeychaincopydomainsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecKeychainCopySearchList(_: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1402440-seckeychaincopysearchlist)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopySearchList(_ searchList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopySearchList(_ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecKeychainCopySettings(_: SecKeychain?, _: UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus](https://developer.apple.com/documentation/security/1395746-seckeychaincopysettings)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopySettings(_ keychain: SecKeychain!, _ outSettings: UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus ``` |
| To | ``` func SecKeychainCopySettings(_ keychain: SecKeychain?, _ outSettings: UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus ``` |

Modified [SecKeychainCreate(_: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Void>, _: Bool, _: SecAccess?, _: UnsafeMutablePointer<SecKeychain?>) -> OSStatus](https://developer.apple.com/documentation/security/1401214-seckeychaincreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCreate(_ pathName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ promptUser: Boolean, _ initialAccess: SecAccess!, _ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCreate(_ pathName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ promptUser: Bool, _ initialAccess: SecAccess?, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |

Modified [SecKeychainDelete(_: SecKeychain?) -> OSStatus](https://developer.apple.com/documentation/security/1395206-seckeychaindelete)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainDelete(_ keychainOrArray: SecKeychain!) -> OSStatus ``` |
| To | ``` func SecKeychainDelete(_ keychainOrArray: SecKeychain?) -> OSStatus ``` |

Modified [SecKeychainFindGenericPassword(_: AnyObject?, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1397301-seckeychainfindgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindGenericPassword(_ keychainOrArray: AnyObject!, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindGenericPassword(_ keychainOrArray: AnyObject?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainFindInternetPassword(_: AnyObject?, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt16, _: SecProtocolType, _: SecAuthenticationType, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1397763-seckeychainfindinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject!, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainGetPath(_: SecKeychain?, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<Int8>) -> OSStatus](https://developer.apple.com/documentation/security/1401073-seckeychaingetpath)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetPath(_ keychain: SecKeychain!, _ ioPathLength: UnsafeMutablePointer<UInt32>, _ pathName: UnsafeMutablePointer<Int8>) -> OSStatus ``` |
| To | ``` func SecKeychainGetPath(_ keychain: SecKeychain?, _ ioPathLength: UnsafeMutablePointer<UInt32>, _ pathName: UnsafeMutablePointer<Int8>) -> OSStatus ``` |

Modified [SecKeychainGetStatus(_: SecKeychain?, _: UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus](https://developer.apple.com/documentation/security/1399085-seckeychaingetstatus)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetStatus(_ keychain: SecKeychain!, _ keychainStatus: UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus ``` |
| To | ``` func SecKeychainGetStatus(_ keychain: SecKeychain?, _ keychainStatus: UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus ``` |

Modified [SecKeychainGetUserInteractionAllowed(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/security/1393621-seckeychaingetuserinteractionall)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetUserInteractionAllowed(_ state: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func SecKeychainGetUserInteractionAllowed(_ state: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [SecKeychainItemCopyAccess(_: SecKeychainItem, _: UnsafeMutablePointer<SecAccess?>) -> OSStatus](https://developer.apple.com/documentation/security/1397585-seckeychainitemcopyaccess)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyAccess(_ itemRef: SecKeychainItem!, _ access: UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyAccess(_ itemRef: SecKeychainItem, _ access: UnsafeMutablePointer<SecAccess?>) -> OSStatus ``` |

Modified [SecKeychainItemCopyAttributesAndData(_: SecKeychainItem, _: UnsafeMutablePointer<SecKeychainAttributeInfo>, _: UnsafeMutablePointer<SecItemClass>, _: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>>, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus](https://developer.apple.com/documentation/security/1400528-seckeychainitemcopyattributesand)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem!, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |

Modified [SecKeychainItemCopyContent(_: SecKeychainItem, _: UnsafeMutablePointer<SecItemClass>, _: UnsafeMutablePointer<SecKeychainAttributeList>, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus](https://developer.apple.com/documentation/security/1401412-seckeychainitemcopycontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem!, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |

Modified [SecKeychainItemCopyFromPersistentReference(_: CFData, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1393535-seckeychainitemcopyfrompersisten)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyFromPersistentReference(_ persistentItemRef: CFData!, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyFromPersistentReference(_ persistentItemRef: CFData, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainItemCopyKeychain(_: SecKeychainItem, _: UnsafeMutablePointer<SecKeychain?>) -> OSStatus](https://developer.apple.com/documentation/security/1398355-seckeychainitemcopykeychain)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyKeychain(_ itemRef: SecKeychainItem!, _ keychainRef: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyKeychain(_ itemRef: SecKeychainItem, _ keychainRef: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |

Modified [SecKeychainItemCreateCopy(_: SecKeychainItem, _: SecKeychain?, _: SecAccess, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1396024-seckeychainitemcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem!, _ destKeychainRef: SecKeychain!, _ initialAccess: SecAccess!, _ itemCopy: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem, _ destKeychainRef: SecKeychain?, _ initialAccess: SecAccess, _ itemCopy: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainItemCreateFromContent(_: SecItemClass, _: UnsafeMutablePointer<SecKeychainAttributeList>, _: UInt32, _: UnsafePointer<Void>, _: SecKeychain?, _: SecAccess?, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1393225-seckeychainitemcreatefromcontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>, _ keychainRef: SecKeychain!, _ initialAccess: SecAccess!, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>, _ keychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainItemCreatePersistentReference(_: SecKeychainItem, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1400643-seckeychainitemcreatepersistentr)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreatePersistentReference(_ itemRef: SecKeychainItem!, _ persistentItemRef: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreatePersistentReference(_ itemRef: SecKeychainItem, _ persistentItemRef: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [SecKeychainItemDelete(_: SecKeychainItem) -> OSStatus](https://developer.apple.com/documentation/security/1400090-seckeychainitemdelete)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemDelete(_ itemRef: SecKeychainItem!) -> OSStatus ``` |
| To | ``` func SecKeychainItemDelete(_ itemRef: SecKeychainItem) -> OSStatus ``` |

Modified [SecKeychainItemModifyAttributesAndData(_: SecKeychainItem, _: UnsafePointer<SecKeychainAttributeList>, _: UInt32, _: UnsafePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/security/1399963-seckeychainitemmodifyattributesa)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem!, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |

Modified [SecKeychainItemModifyContent(_: SecKeychainItem, _: UnsafePointer<SecKeychainAttributeList>, _: UInt32, _: UnsafePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/security/1397154-seckeychainitemmodifycontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem!, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |

Modified [SecKeychainItemSetAccess(_: SecKeychainItem, _: SecAccess) -> OSStatus](https://developer.apple.com/documentation/security/1395210-seckeychainitemsetaccess)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemSetAccess(_ itemRef: SecKeychainItem!, _ access: SecAccess!) -> OSStatus ``` |
| To | ``` func SecKeychainItemSetAccess(_ itemRef: SecKeychainItem, _ access: SecAccess) -> OSStatus ``` |

Modified [SecKeychainLock(_: SecKeychain?) -> OSStatus](https://developer.apple.com/documentation/security/1402180-seckeychainlock)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainLock(_ keychain: SecKeychain!) -> OSStatus ``` |
| To | ``` func SecKeychainLock(_ keychain: SecKeychain?) -> OSStatus ``` |

Modified [SecKeychainOpen(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<SecKeychain?>) -> OSStatus](https://developer.apple.com/documentation/security/1396431-seckeychainopen)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainOpen(_ pathName: UnsafePointer<Int8>, _ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainOpen(_ pathName: UnsafePointer<Int8>, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |

Modified [SecKeychainSetAccess(_: SecKeychain?, _: SecAccess) -> OSStatus](https://developer.apple.com/documentation/security/1392434-seckeychainsetaccess)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetAccess(_ keychain: SecKeychain!, _ access: SecAccess!) -> OSStatus ``` |
| To | ``` func SecKeychainSetAccess(_ keychain: SecKeychain?, _ access: SecAccess) -> OSStatus ``` |

Modified [SecKeychainSetDefault(_: SecKeychain?) -> OSStatus](https://developer.apple.com/documentation/security/1393097-seckeychainsetdefault)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetDefault(_ keychain: SecKeychain!) -> OSStatus ``` |
| To | ``` func SecKeychainSetDefault(_ keychain: SecKeychain?) -> OSStatus ``` |

Modified [SecKeychainSetDomainDefault(_: SecPreferencesDomain, _: SecKeychain?) -> OSStatus](https://developer.apple.com/documentation/security/1398802-seckeychainsetdomaindefault)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetDomainDefault(_ domain: SecPreferencesDomain, _ keychain: SecKeychain!) -> OSStatus ``` |
| To | ``` func SecKeychainSetDomainDefault(_ domain: SecPreferencesDomain, _ keychain: SecKeychain?) -> OSStatus ``` |

Modified [SecKeychainSetDomainSearchList(_: SecPreferencesDomain, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/security/1398572-seckeychainsetdomainsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: CFArray!) -> OSStatus ``` |
| To | ``` func SecKeychainSetDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: CFArray) -> OSStatus ``` |

Modified [SecKeychainSetSearchList(_: CFArray) -> OSStatus](https://developer.apple.com/documentation/security/1397619-seckeychainsetsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetSearchList(_ searchList: CFArray!) -> OSStatus ``` |
| To | ``` func SecKeychainSetSearchList(_ searchList: CFArray) -> OSStatus ``` |

Modified [SecKeychainSetSettings(_: SecKeychain?, _: UnsafePointer<SecKeychainSettings>) -> OSStatus](https://developer.apple.com/documentation/security/1393109-seckeychainsetsettings)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetSettings(_ keychain: SecKeychain!, _ newSettings: UnsafePointer<SecKeychainSettings>) -> OSStatus ``` |
| To | ``` func SecKeychainSetSettings(_ keychain: SecKeychain?, _ newSettings: UnsafePointer<SecKeychainSettings>) -> OSStatus ``` |

Modified [SecKeychainSetUserInteractionAllowed(_: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1396453-seckeychainsetuserinteractionall)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetUserInteractionAllowed(_ state: Boolean) -> OSStatus ``` |
| To | ``` func SecKeychainSetUserInteractionAllowed(_ state: Bool) -> OSStatus ``` |

Modified [SecKeychainUnlock(_: SecKeychain?, _: UInt32, _: UnsafePointer<Void>, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1400341-seckeychainunlock)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainUnlock(_ keychain: SecKeychain!, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ usePassword: Boolean) -> OSStatus ``` |
| To | ``` func SecKeychainUnlock(_ keychain: SecKeychain?, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ usePassword: Bool) -> OSStatus ``` |

Modified [SecKeyCreateFromData(_: CFDictionary, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey?](https://developer.apple.com/documentation/security/1393853-seckeycreatefromdata)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyCreateFromData(_ parameters: CFDictionary!, _ keyData: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` |
| To | ``` func SecKeyCreateFromData(_ parameters: CFDictionary, _ keyData: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |

Modified [SecKeyDeriveFromPassword(_: CFString, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey?](https://developer.apple.com/documentation/security/1395028-seckeyderivefrompassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyDeriveFromPassword(_ password: CFString!, _ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` |
| To | ``` func SecKeyDeriveFromPassword(_ password: CFString, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |

Modified [SecKeyGeneratePair(_: CFDictionary, _: UnsafeMutablePointer<SecKey?>, _: UnsafeMutablePointer<SecKey?>) -> OSStatus](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGeneratePair(_ parameters: CFDictionary!, _ publicKey: UnsafeMutablePointer<Unmanaged<SecKey>?>, _ privateKey: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` |
| To | ``` func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>, _ privateKey: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |

Modified [SecKeyGeneratePairAsync(_: CFDictionary, _: dispatch_queue_t, _: SecKeyGeneratePairBlock)](https://developer.apple.com/documentation/security/1394698-seckeygeneratepairasync)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGeneratePairAsync(_ parameters: CFDictionary!, _ deliveryQueue: dispatch_queue_t!, _ result: SecKeyGeneratePairBlock!) ``` |
| To | ``` func SecKeyGeneratePairAsync(_ parameters: CFDictionary, _ deliveryQueue: dispatch_queue_t, _ result: SecKeyGeneratePairBlock) ``` |

Modified [SecKeyGeneratePairBlock](https://developer.apple.com/documentation/security/seckeygeneratepairblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecKeyGeneratePairBlock = (SecKey!, SecKey!, CFError!) -> Void ``` |
| To | ``` typealias SecKeyGeneratePairBlock = (SecKey, SecKey, CFError) -> Void ``` |

Modified [SecKeyGenerateSymmetric(_: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey?](https://developer.apple.com/documentation/security/1401861-seckeygeneratesymmetric)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGenerateSymmetric(_ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` |
| To | ``` func SecKeyGenerateSymmetric(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |

Modified [SecKeyGetBlockSize(_: SecKey) -> Int](https://developer.apple.com/documentation/security/1394222-seckeygetblocksize)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGetBlockSize(_ key: SecKey!) -> Int ``` |
| To | ``` func SecKeyGetBlockSize(_ key: SecKey) -> Int ``` |

Modified [SecKeyUnwrapSymmetric(_: UnsafeMutablePointer<Unmanaged<CFData>?>, _: SecKey, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey?](https://developer.apple.com/documentation/security/1394725-seckeyunwrapsymmetric)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey!, _ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` |
| To | ``` func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |

Modified [SecKeyWrapSymmetric(_: SecKey, _: SecKey, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData?](https://developer.apple.com/documentation/security/1396734-seckeywrapsymmetric)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyWrapSymmetric(_ keyToWrap: SecKey!, _ wrappingKey: SecKey!, _ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` |
| To | ``` func SecKeyWrapSymmetric(_ keyToWrap: SecKey, _ wrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |

Modified [SecMessageBlock](https://developer.apple.com/documentation/security/secmessageblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecMessageBlock = (AnyObject!, CFError!, Boolean) -> Void ``` |
| To | ``` typealias SecMessageBlock = (AnyObject?, CFError?, Bool) -> Void ``` |

Modified [SecPKCS12Import(_: CFData, _: CFDictionary, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1396915-secpkcs12import)

|  | Declaration |
| --- | --- |
| From | ``` func SecPKCS12Import(_ pkcs12_data: CFData!, _ options: CFDictionary!, _ items: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecPKCS12Import(_ pkcs12_data: CFData, _ options: CFDictionary, _ items: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecPolicyCopyProperties(_: SecPolicy) -> CFDictionary](https://developer.apple.com/documentation/security/1401915-secpolicycopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCopyProperties(_ policyRef: SecPolicy!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SecPolicyCopyProperties(_ policyRef: SecPolicy) -> CFDictionary ``` |

Modified [SecPolicyCreateBasicX509() -> SecPolicy](https://developer.apple.com/documentation/security/1397202-secpolicycreatebasicx509)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateBasicX509() -> Unmanaged<SecPolicy>! ``` |
| To | ``` func SecPolicyCreateBasicX509() -> SecPolicy ``` |

Modified [SecPolicyCreateRevocation(_: CFOptionFlags) -> SecPolicy](https://developer.apple.com/documentation/security/1400026-secpolicycreaterevocation)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateRevocation(_ revocationFlags: CFOptionFlags) -> Unmanaged<SecPolicy>! ``` |
| To | ``` func SecPolicyCreateRevocation(_ revocationFlags: CFOptionFlags) -> SecPolicy ``` |

Modified [SecPolicyCreateSSL(_: Bool, _: CFString?) -> SecPolicy](https://developer.apple.com/documentation/security/1392592-secpolicycreatessl)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateSSL(_ server: Boolean, _ hostname: CFString!) -> Unmanaged<SecPolicy>! ``` |
| To | ``` func SecPolicyCreateSSL(_ server: Bool, _ hostname: CFString?) -> SecPolicy ``` |

Modified [SecPolicyCreateWithProperties(_: AnyObject, _: CFDictionary?) -> SecPolicy?](https://developer.apple.com/documentation/security/1394568-secpolicycreatewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: AnyObject!, _ properties: CFDictionary!) -> Unmanaged<SecPolicy>! ``` |
| To | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: AnyObject, _ properties: CFDictionary?) -> SecPolicy? ``` |

Modified [SecRequirementCopyData(_: SecRequirement, _: SecCSFlags, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1401647-secrequirementcopydata)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCopyData(_ requirement: SecRequirement!, _ flags: SecCSFlags, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCopyData(_ requirement: SecRequirement, _ flags: SecCSFlags, _ data: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [SecRequirementCopyString(_: SecRequirement, _: SecCSFlags, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/security/1394253-secrequirementcopystring)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCopyString(_ requirement: SecRequirement!, _ flags: SecCSFlags, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCopyString(_ requirement: SecRequirement, _ flags: SecCSFlags, _ text: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [SecRequirementCreateWithData(_: CFData, _: SecCSFlags, _: UnsafeMutablePointer<SecRequirement?>) -> OSStatus](https://developer.apple.com/documentation/security/1396013-secrequirementcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithData(_ data: CFData!, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithData(_ data: CFData, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus ``` |

Modified [SecRequirementCreateWithString(_: CFString, _: SecCSFlags, _: UnsafeMutablePointer<SecRequirement?>) -> OSStatus](https://developer.apple.com/documentation/security/1394522-secrequirementcreatewithstring)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithString(_ text: CFString!, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithString(_ text: CFString, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus ``` |

Modified [SecRequirementCreateWithStringAndErrors(_: CFString, _: SecCSFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>, _: UnsafeMutablePointer<SecRequirement?>) -> OSStatus](https://developer.apple.com/documentation/security/1401166-secrequirementcreatewithstringan)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithStringAndErrors(_ text: CFString!, _ flags: SecCSFlags, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithStringAndErrors(_ text: CFString, _ flags: SecCSFlags, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus ``` |

Modified [SecSignTransformCreate(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform?](https://developer.apple.com/documentation/security/1398780-secsigntransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecSignTransformCreate(_ key: SecKey!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecSignTransformCreate(_ key: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |

Modified [SecStaticCodeCheckValidity(_: SecStaticCode, _: SecCSFlags, _: SecRequirement?) -> OSStatus](https://developer.apple.com/documentation/security/1395784-secstaticcodecheckvalidity)

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCheckValidity(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!) -> OSStatus ``` |
| To | ``` func SecStaticCodeCheckValidity(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ requirement: SecRequirement?) -> OSStatus ``` |

Modified [SecStaticCodeCheckValidityWithErrors(_: SecStaticCode, _: SecCSFlags, _: SecRequirement?, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus](https://developer.apple.com/documentation/security/1395252-secstaticcodecheckvaliditywither)

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |

Modified [SecStaticCodeCreateWithPath(_: CFURL, _: SecCSFlags, _: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1396899-secstaticcodecreatewithpath)

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCreateWithPath(_ path: CFURL!, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCreateWithPath(_ path: CFURL, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus ``` |

Modified [SecStaticCodeCreateWithPathAndAttributes(_: CFURL, _: SecCSFlags, _: CFDictionary, _: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1394237-secstaticcodecreatewithpathandat)

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCreateWithPathAndAttributes(_ path: CFURL!, _ flags: SecCSFlags, _ attributes: CFDictionary!, _ staticCode: UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCreateWithPathAndAttributes(_ path: CFURL, _ flags: SecCSFlags, _ attributes: CFDictionary, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus ``` |

Modified [SecTaskCopyValueForEntitlement(_: SecTask, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject?](https://developer.apple.com/documentation/security/1393461-sectaskcopyvalueforentitlement)

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCopyValueForEntitlement(_ task: SecTask!, _ entitlement: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTaskCopyValueForEntitlement(_ task: SecTask, _ entitlement: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject? ``` |

Modified [SecTaskCopyValuesForEntitlements(_: SecTask, _: CFArray, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary?](https://developer.apple.com/documentation/security/1397627-sectaskcopyvaluesforentitlements)

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCopyValuesForEntitlements(_ task: SecTask!, _ entitlements: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SecTaskCopyValuesForEntitlements(_ task: SecTask, _ entitlements: CFArray, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary? ``` |

Modified [SecTaskCreateFromSelf(_: CFAllocator?) -> SecTask?](https://developer.apple.com/documentation/security/1400321-sectaskcreatefromself)

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCreateFromSelf(_ allocator: CFAllocator!) -> Unmanaged<SecTask>! ``` |
| To | ``` func SecTaskCreateFromSelf(_ allocator: CFAllocator?) -> SecTask? ``` |

Modified [SecTaskCreateWithAuditToken(_: CFAllocator?, _: audit_token_t) -> SecTask?](https://developer.apple.com/documentation/security/1401168-sectaskcreatewithaudittoken)

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCreateWithAuditToken(_ allocator: CFAllocator!, _ token: audit_token_t) -> Unmanaged<SecTask>! ``` |
| To | ``` func SecTaskCreateWithAuditToken(_ allocator: CFAllocator?, _ token: audit_token_t) -> SecTask? ``` |

Modified [SecTransformActionBlock](https://developer.apple.com/documentation/security/sectransformactionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformActionBlock = () -> Unmanaged<AnyObject>! ``` |
| To | ``` typealias SecTransformActionBlock = () -> Unmanaged<AnyObject>? ``` |

Modified [SecTransformAttributeActionBlock](https://developer.apple.com/documentation/security/sectransformattributeactionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformAttributeActionBlock = (SecTransformAttribute!, AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` typealias SecTransformAttributeActionBlock = (SecTransformAttribute, AnyObject) -> Unmanaged<AnyObject>? ``` |

Modified [SecTransformConnectTransforms(_: SecTransform, _: CFString, _: SecTransform, _: CFString, _: SecGroupTransform, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecGroupTransform?](https://developer.apple.com/documentation/security/1401298-sectransformconnecttransforms)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformConnectTransforms(_ sourceTransformRef: SecTransform!, _ sourceAttributeName: CFString!, _ destinationTransformRef: SecTransform!, _ destinationAttributeName: CFString!, _ group: SecGroupTransform!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecGroupTransform>! ``` |
| To | ``` func SecTransformConnectTransforms(_ sourceTransformRef: SecTransform, _ sourceAttributeName: CFString, _ destinationTransformRef: SecTransform, _ destinationAttributeName: CFString, _ group: SecGroupTransform, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecGroupTransform? ``` |

Modified [SecTransformCopyExternalRepresentation(_: SecTransform) -> CFDictionary](https://developer.apple.com/documentation/security/1397283-sectransformcopyexternalrepresen)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCopyExternalRepresentation(_ transformRef: SecTransform!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SecTransformCopyExternalRepresentation(_ transformRef: SecTransform) -> CFDictionary ``` |

Modified [SecTransformCreate(_: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform?](https://developer.apple.com/documentation/security/1395256-sectransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreate(_ name: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecTransformCreate(_ name: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |

Modified [SecTransformCreateFP](https://developer.apple.com/documentation/security/sectransformcreatefp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformCreateFP = CFunctionPointer<((CFString!, SecTransform!, SecTransformImplementationRef) -> SecTransformInstanceBlock!)> ``` |
| To | ``` typealias SecTransformCreateFP = (CFString, SecTransform, SecTransformImplementationRef) -> SecTransformInstanceBlock ``` |

Modified [SecTransformCreateFromExternalRepresentation(_: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform?](https://developer.apple.com/documentation/security/1397563-sectransformcreatefromexternalre)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |

Modified [SecTransformCreateGroupTransform() -> SecGroupTransform](https://developer.apple.com/documentation/security/1400301-sectransformcreategrouptransform)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreateGroupTransform() -> Unmanaged<SecGroupTransform>! ``` |
| To | ``` func SecTransformCreateGroupTransform() -> SecGroupTransform ``` |

Modified [SecTransformCreateReadTransformWithReadStream(_: CFReadStream) -> SecTransform](https://developer.apple.com/documentation/security/1394302-sectransformcreatereadtransformw)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream!) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream) -> SecTransform ``` |

Modified [SecTransformCustomGetAttribute(_: SecTransformImplementationRef, _: SecTransformStringOrAttribute, _: SecTransformMetaAttributeType) -> AnyObject?](https://developer.apple.com/documentation/security/1397766-sectransformcustomgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute!, _ type: SecTransformMetaAttributeType) -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType) -> AnyObject? ``` |

Modified [SecTransformCustomSetAttribute(_: SecTransformImplementationRef, _: SecTransformStringOrAttribute, _: SecTransformMetaAttributeType, _: AnyObject?) -> AnyObject?](https://developer.apple.com/documentation/security/1392556-sectransformcustomsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute!, _ type: SecTransformMetaAttributeType, _ value: AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType, _ value: AnyObject?) -> AnyObject? ``` |

Modified [SecTransformDataBlock](https://developer.apple.com/documentation/security/sectransformdatablock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformDataBlock = (AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` typealias SecTransformDataBlock = (AnyObject) -> Unmanaged<AnyObject>? ``` |

Modified [SecTransformExecute(_: SecTransform, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject](https://developer.apple.com/documentation/security/1395776-sectransformexecute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformExecute(_ transformRef: SecTransform!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject! ``` |
| To | ``` func SecTransformExecute(_ transformRef: SecTransform, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject ``` |

Modified [SecTransformExecuteAsync(_: SecTransform, _: dispatch_queue_t, _: SecMessageBlock)](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformExecuteAsync(_ transformRef: SecTransform!, _ deliveryQueue: dispatch_queue_t!, _ deliveryBlock: SecMessageBlock!) ``` |
| To | ``` func SecTransformExecuteAsync(_ transformRef: SecTransform, _ deliveryQueue: dispatch_queue_t, _ deliveryBlock: SecMessageBlock) ``` |

Modified [SecTransformFindByName(_: SecGroupTransform, _: CFString) -> SecTransform?](https://developer.apple.com/documentation/security/1401448-sectransformfindbyname)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformFindByName(_ transform: SecGroupTransform!, _ name: CFString!) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecTransformFindByName(_ transform: SecGroupTransform, _ name: CFString) -> SecTransform? ``` |

Modified [SecTransformGetAttribute(_: SecTransform, _: CFString) -> AnyObject?](https://developer.apple.com/documentation/security/1398748-sectransformgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformGetAttribute(_ transformRef: SecTransform!, _ key: CFString!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTransformGetAttribute(_ transformRef: SecTransform, _ key: CFString) -> AnyObject? ``` |

Modified [SecTransformInstanceBlock](https://developer.apple.com/documentation/security/sectransforminstanceblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformInstanceBlock = () -> Unmanaged<CFError>! ``` |
| To | ``` typealias SecTransformInstanceBlock = () -> Unmanaged<CFError>? ``` |

Modified [SecTransformNoData() -> AnyObject](https://developer.apple.com/documentation/security/1393788-sectransformnodata)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformNoData() -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTransformNoData() -> AnyObject ``` |

Modified [SecTransformPushbackAttribute(_: SecTransformImplementationRef, _: SecTransformStringOrAttribute, _: AnyObject) -> AnyObject?](https://developer.apple.com/documentation/security/1400559-sectransformpushbackattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute!, _ value: AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ value: AnyObject) -> AnyObject? ``` |

Modified [SecTransformRegister(_: CFString, _: SecTransformCreateFP, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/security/1393997-sectransformregister)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformRegister(_ uniqueName: CFString!, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func SecTransformRegister(_ uniqueName: CFString, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [SecTransformSetAttribute(_: SecTransform, _: CFString, _: AnyObject, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/security/1393861-sectransformsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetAttribute(_ transformRef: SecTransform!, _ key: CFString!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` |
| To | ``` func SecTransformSetAttribute(_ transformRef: SecTransform, _ key: CFString, _ value: AnyObject, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [SecTransformSetAttributeAction(_: SecTransformImplementationRef, _: CFString, _: SecTransformStringOrAttribute?, _: SecTransformAttributeActionBlock) -> CFError?](https://developer.apple.com/documentation/security/1396035-sectransformsetattributeaction)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString!, _ attribute: SecTransformStringOrAttribute!, _ newAction: SecTransformAttributeActionBlock!) -> Unmanaged<CFError>! ``` |
| To | ``` func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ attribute: SecTransformStringOrAttribute?, _ newAction: SecTransformAttributeActionBlock) -> CFError? ``` |

Modified [SecTransformSetDataAction(_: SecTransformImplementationRef, _: CFString, _: SecTransformDataBlock) -> CFError?](https://developer.apple.com/documentation/security/1399597-sectransformsetdataaction)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetDataAction(_ ref: SecTransformImplementationRef, _ action: CFString!, _ newAction: SecTransformDataBlock!) -> Unmanaged<CFError>! ``` |
| To | ``` func SecTransformSetDataAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: SecTransformDataBlock) -> CFError? ``` |

Modified [SecTransformSetTransformAction(_: SecTransformImplementationRef, _: CFString, _: SecTransformActionBlock) -> CFError?](https://developer.apple.com/documentation/security/1402097-sectransformsettransformaction)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString!, _ newAction: SecTransformActionBlock!) -> Unmanaged<CFError>! ``` |
| To | ``` func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: SecTransformActionBlock) -> CFError? ``` |

Modified [SecTrustCallback](https://developer.apple.com/documentation/security/sectrustcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTrustCallback = (SecTrust!, SecTrustResultType) -> Void ``` |
| To | ``` typealias SecTrustCallback = (SecTrust, SecTrustResultType) -> Void ``` |

Modified [SecTrustCopyAnchorCertificates(_: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1401507-sectrustcopyanchorcertificates)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyAnchorCertificates(_ anchors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustCopyAnchorCertificates(_ anchors: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecTrustCopyCustomAnchorCertificates(_: SecTrust, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1401743-sectrustcopycustomanchorcertific)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyCustomAnchorCertificates(_ trust: SecTrust!, _ anchors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustCopyCustomAnchorCertificates(_ trust: SecTrust, _ anchors: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecTrustCopyExceptions(_: SecTrust) -> CFData](https://developer.apple.com/documentation/security/1400106-sectrustcopyexceptions)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyExceptions(_ trust: SecTrust!) -> Unmanaged<CFData>! ``` |
| To | ``` func SecTrustCopyExceptions(_ trust: SecTrust) -> CFData ``` |

Modified [SecTrustCopyPolicies(_: SecTrust, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1392716-sectrustcopypolicies)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyPolicies(_ trust: SecTrust!, _ policies: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustCopyPolicies(_ trust: SecTrust, _ policies: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecTrustCopyProperties(_: SecTrust) -> CFArray?](https://developer.apple.com/documentation/security/1401567-sectrustcopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyProperties(_ trust: SecTrust!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SecTrustCopyProperties(_ trust: SecTrust) -> CFArray? ``` |

Modified [SecTrustCopyPublicKey(_: SecTrust) -> SecKey?](https://developer.apple.com/documentation/security/1396135-sectrustcopypublickey)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyPublicKey(_ trust: SecTrust!) -> Unmanaged<SecKey>! ``` |
| To | ``` func SecTrustCopyPublicKey(_ trust: SecTrust) -> SecKey? ``` |

Modified [SecTrustCopyResult(_: SecTrust) -> CFDictionary?](https://developer.apple.com/documentation/security/1398612-sectrustcopyresult)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCopyResult(_ trust: SecTrust!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SecTrustCopyResult(_ trust: SecTrust) -> CFDictionary? ``` |

Modified [SecTrustCreateWithCertificates(_: AnyObject, _: AnyObject?, _: UnsafeMutablePointer<SecTrust?>) -> OSStatus](https://developer.apple.com/documentation/security/1401555-sectrustcreatewithcertificates)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCreateWithCertificates(_ certificates: AnyObject!, _ policies: AnyObject!, _ trust: UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus ``` |
| To | ``` func SecTrustCreateWithCertificates(_ certificates: AnyObject, _ policies: AnyObject?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus ``` |

Modified [SecTrustedApplicationCopyData(_: SecTrustedApplication, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1401737-sectrustedapplicationcopydata)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustedApplicationCopyData(_ appRef: SecTrustedApplication!, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecTrustedApplicationCopyData(_ appRef: SecTrustedApplication, _ data: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [SecTrustedApplicationCreateFromPath(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus](https://developer.apple.com/documentation/security/1400622-sectrustedapplicationcreatefromp)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<Int8>, _ app: UnsafeMutablePointer<Unmanaged<SecTrustedApplication>?>) -> OSStatus ``` |
| To | ``` func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<Int8>, _ app: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus ``` |

Modified [SecTrustedApplicationSetData(_: SecTrustedApplication, _: CFData) -> OSStatus](https://developer.apple.com/documentation/security/1397440-sectrustedapplicationsetdata)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustedApplicationSetData(_ appRef: SecTrustedApplication!, _ data: CFData!) -> OSStatus ``` |
| To | ``` func SecTrustedApplicationSetData(_ appRef: SecTrustedApplication, _ data: CFData) -> OSStatus ``` |

Modified [SecTrustEvaluate(_: SecTrust, _: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](https://developer.apple.com/documentation/security/1394363-sectrustevaluate)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustEvaluate(_ trust: SecTrust!, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` |
| To | ``` func SecTrustEvaluate(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` |

Modified [SecTrustEvaluateAsync(_: SecTrust, _: dispatch_queue_t?, _: SecTrustCallback) -> OSStatus](https://developer.apple.com/documentation/security/1400632-sectrustevaluateasync)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustEvaluateAsync(_ trust: SecTrust!, _ queue: dispatch_queue_t!, _ result: SecTrustCallback!) -> OSStatus ``` |
| To | ``` func SecTrustEvaluateAsync(_ trust: SecTrust, _ queue: dispatch_queue_t?, _ result: SecTrustCallback) -> OSStatus ``` |

Modified [SecTrustGetCertificateAtIndex(_: SecTrust, _: CFIndex) -> SecCertificate?](https://developer.apple.com/documentation/security/1395987-sectrustgetcertificateatindex)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustGetCertificateAtIndex(_ trust: SecTrust!, _ ix: CFIndex) -> Unmanaged<SecCertificate>! ``` |
| To | ``` func SecTrustGetCertificateAtIndex(_ trust: SecTrust, _ ix: CFIndex) -> SecCertificate? ``` |

Modified [SecTrustGetCertificateCount(_: SecTrust) -> CFIndex](https://developer.apple.com/documentation/security/1397024-sectrustgetcertificatecount)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustGetCertificateCount(_ trust: SecTrust!) -> CFIndex ``` |
| To | ``` func SecTrustGetCertificateCount(_ trust: SecTrust) -> CFIndex ``` |

Modified [SecTrustGetNetworkFetchAllowed(_: SecTrust, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/security/1400259-sectrustgetnetworkfetchallowed)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustGetNetworkFetchAllowed(_ trust: SecTrust!, _ allowFetch: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func SecTrustGetNetworkFetchAllowed(_ trust: SecTrust, _ allowFetch: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [SecTrustGetTrustResult(_: SecTrust, _: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](https://developer.apple.com/documentation/security/1396077-sectrustgettrustresult)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustGetTrustResult(_ trust: SecTrust!, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` |
| To | ``` func SecTrustGetTrustResult(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` |

Modified [SecTrustGetVerifyTime(_: SecTrust) -> CFAbsoluteTime](https://developer.apple.com/documentation/security/1395935-sectrustgetverifytime)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustGetVerifyTime(_ trust: SecTrust!) -> CFAbsoluteTime ``` |
| To | ``` func SecTrustGetVerifyTime(_ trust: SecTrust) -> CFAbsoluteTime ``` |

Modified [SecTrustSetAnchorCertificates(_: SecTrust, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/security/1396098-sectrustsetanchorcertificates)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetAnchorCertificates(_ trust: SecTrust!, _ anchorCertificates: CFArray!) -> OSStatus ``` |
| To | ``` func SecTrustSetAnchorCertificates(_ trust: SecTrust, _ anchorCertificates: CFArray) -> OSStatus ``` |

Modified [SecTrustSetAnchorCertificatesOnly(_: SecTrust, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1399071-sectrustsetanchorcertificatesonl)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetAnchorCertificatesOnly(_ trust: SecTrust!, _ anchorCertificatesOnly: Boolean) -> OSStatus ``` |
| To | ``` func SecTrustSetAnchorCertificatesOnly(_ trust: SecTrust, _ anchorCertificatesOnly: Bool) -> OSStatus ``` |

Modified [SecTrustSetExceptions(_: SecTrust, _: CFData) -> Bool](https://developer.apple.com/documentation/security/1395676-sectrustsetexceptions)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetExceptions(_ trust: SecTrust!, _ exceptions: CFData!) -> Bool ``` |
| To | ``` func SecTrustSetExceptions(_ trust: SecTrust, _ exceptions: CFData) -> Bool ``` |

Modified [SecTrustSetKeychains(_: SecTrust, _: AnyObject?) -> OSStatus](https://developer.apple.com/documentation/security/1395644-sectrustsetkeychains)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetKeychains(_ trust: SecTrust!, _ keychainOrArray: AnyObject!) -> OSStatus ``` |
| To | ``` func SecTrustSetKeychains(_ trust: SecTrust, _ keychainOrArray: AnyObject?) -> OSStatus ``` |

Modified [SecTrustSetNetworkFetchAllowed(_: SecTrust, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1395083-sectrustsetnetworkfetchallowed)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetNetworkFetchAllowed(_ trust: SecTrust!, _ allowFetch: Boolean) -> OSStatus ``` |
| To | ``` func SecTrustSetNetworkFetchAllowed(_ trust: SecTrust, _ allowFetch: Bool) -> OSStatus ``` |

Modified [SecTrustSetOCSPResponse(_: SecTrust, _: AnyObject?) -> OSStatus](https://developer.apple.com/documentation/security/1400880-sectrustsetocspresponse)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetOCSPResponse(_ trust: SecTrust!, _ responseData: AnyObject!) -> OSStatus ``` |
| To | ``` func SecTrustSetOCSPResponse(_ trust: SecTrust, _ responseData: AnyObject?) -> OSStatus ``` |

Modified [SecTrustSetOptions(_: SecTrust, _: SecTrustOptionFlags) -> OSStatus](https://developer.apple.com/documentation/security/1392875-sectrustsetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetOptions(_ trustRef: SecTrust!, _ options: SecTrustOptionFlags) -> OSStatus ``` |
| To | ``` func SecTrustSetOptions(_ trustRef: SecTrust, _ options: SecTrustOptionFlags) -> OSStatus ``` |

Modified [SecTrustSetPolicies(_: SecTrust, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1398399-sectrustsetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetPolicies(_ trust: SecTrust!, _ policies: AnyObject!) -> OSStatus ``` |
| To | ``` func SecTrustSetPolicies(_ trust: SecTrust, _ policies: AnyObject) -> OSStatus ``` |

Modified [SecTrustSettingsCopyCertificates(_: SecTrustSettingsDomain, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1397413-sectrustsettingscopycertificates)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecTrustSettingsCopyModificationDate(_: SecCertificate, _: SecTrustSettingsDomain, _: UnsafeMutablePointer<CFDate?>) -> OSStatus](https://developer.apple.com/documentation/security/1397941-sectrustsettingscopymodification)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyModificationDate(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ modificationDate: UnsafeMutablePointer<Unmanaged<CFDate>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyModificationDate(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ modificationDate: UnsafeMutablePointer<CFDate?>) -> OSStatus ``` |

Modified [SecTrustSettingsCopyTrustSettings(_: SecCertificate, _: SecTrustSettingsDomain, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1400261-sectrustsettingscopytrustsetting)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyTrustSettings(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SecTrustSettingsCreateExternalRepresentation(_: SecTrustSettingsDomain, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1402355-sectrustsettingscreateexternalre)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCreateExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCreateExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [SecTrustSettingsImportExternalRepresentation(_: SecTrustSettingsDomain, _: CFData) -> OSStatus](https://developer.apple.com/documentation/security/1392836-sectrustsettingsimportexternalre)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsImportExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: CFData!) -> OSStatus ``` |
| To | ``` func SecTrustSettingsImportExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: CFData) -> OSStatus ``` |

Modified [SecTrustSettingsRemoveTrustSettings(_: SecCertificate, _: SecTrustSettingsDomain) -> OSStatus](https://developer.apple.com/documentation/security/1395904-sectrustsettingsremovetrustsetti)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsRemoveTrustSettings(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain) -> OSStatus ``` |
| To | ``` func SecTrustSettingsRemoveTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain) -> OSStatus ``` |

Modified [SecTrustSettingsSetTrustSettings(_: SecCertificate, _: SecTrustSettingsDomain, _: AnyObject?) -> OSStatus](https://developer.apple.com/documentation/security/1399119-sectrustsettingssettrustsettings)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsSetTrustSettings(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ trustSettingsDictOrArray: AnyObject!) -> OSStatus ``` |
| To | ``` func SecTrustSettingsSetTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ trustSettingsDictOrArray: AnyObject?) -> OSStatus ``` |

Modified [SecTrustSetVerifyDate(_: SecTrust, _: CFDate) -> OSStatus](https://developer.apple.com/documentation/security/1397216-sectrustsetverifydate)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetVerifyDate(_ trust: SecTrust!, _ verifyDate: CFDate!) -> OSStatus ``` |
| To | ``` func SecTrustSetVerifyDate(_ trust: SecTrust, _ verifyDate: CFDate) -> OSStatus ``` |

Modified [SecVerifyTransformCreate(_: SecKey, _: CFData?, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform?](https://developer.apple.com/documentation/security/1393414-secverifytransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecVerifyTransformCreate(_ key: SecKey!, _ signature: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` |
| To | ``` func SecVerifyTransformCreate(_ key: SecKey, _ signature: CFData?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |

Modified [SSL_DH_anon_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_anon_export_with_des40_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_anon_EXPORT_WITH_DES40_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_anon_EXPORT_WITH_DES40_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_anon_EXPORT_WITH_RC4_40_MD5](https://developer.apple.com/documentation/security/ssl_dh_anon_export_with_rc4_40_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_anon_EXPORT_WITH_RC4_40_MD5: Int { get } ``` |
| To | ``` var SSL_DH_anon_EXPORT_WITH_RC4_40_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_DH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_anon_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_anon_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_anon_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_anon_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_anon_with_des_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_anon_WITH_DES_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_anon_WITH_DES_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_anon_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_anon_with_rc4_128_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_anon_WITH_RC4_128_MD5: Int { get } ``` |
| To | ``` var SSL_DH_anon_WITH_RC4_128_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_DH_DSS_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_dss_export_with_des40_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_DSS_EXPORT_WITH_DES40_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_DSS_EXPORT_WITH_DES40_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_dss_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_DSS_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_DSS_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_DSS_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_dss_with_des_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_DSS_WITH_DES_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_DSS_WITH_DES_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_RSA_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_rsa_export_with_des40_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_RSA_EXPORT_WITH_DES40_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_RSA_EXPORT_WITH_DES40_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dh_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DH_RSA_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dh_rsa_with_des_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DH_RSA_WITH_DES_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DH_RSA_WITH_DES_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dhe_dss_export_with_des40_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dhe_dss_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DHE_DSS_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/ssl_dhe_dss_with_des_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DHE_DSS_WITH_DES_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DHE_DSS_WITH_DES_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dhe_rsa_export_with_des40_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dhe_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_DHE_RSA_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_dhe_rsa_with_des_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_DHE_RSA_WITH_DES_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_DHE_RSA_WITH_DES_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_FORTEZZA_DMS_WITH_FORTEZZA_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_fortezza_dms_with_fortezza_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_FORTEZZA_DMS_WITH_FORTEZZA_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_FORTEZZA_DMS_WITH_FORTEZZA_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_FORTEZZA_DMS_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_fortezza_dms_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_FORTEZZA_DMS_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var SSL_FORTEZZA_DMS_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_NO_SUCH_CIPHERSUITE](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_no_such_ciphersuite)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_NO_SUCH_CIPHERSUITE: Int { get } ``` |
| To | ``` var SSL_NO_SUCH_CIPHERSUITE: SSLCipherSuite { get } ``` |

Modified [SSL_NULL_WITH_NULL_NULL](https://developer.apple.com/documentation/security/ssl_null_with_null_null)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_NULL_WITH_NULL_NULL: Int { get } ``` |
| To | ``` var SSL_NULL_WITH_NULL_NULL: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_EXPORT_WITH_DES40_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_export_with_des40_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_EXPORT_WITH_DES40_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_RSA_EXPORT_WITH_DES40_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_EXPORT_WITH_RC2_CBC_40_MD5](https://developer.apple.com/documentation/security/ssl_rsa_export_with_rc2_cbc_40_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_EXPORT_WITH_RC2_CBC_40_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_EXPORT_WITH_RC2_CBC_40_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_EXPORT_WITH_RC4_40_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_export_with_rc4_40_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_EXPORT_WITH_RC4_40_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_EXPORT_WITH_RC4_40_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_3DES_EDE_CBC_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_3des_ede_cbc_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_3DES_EDE_CBC_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_3DES_EDE_CBC_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_DES_CBC_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_des_cbc_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_DES_CBC_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_DES_CBC_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_DES_CBC_SHA](https://developer.apple.com/documentation/security/ssl_rsa_with_des_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_DES_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_DES_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_IDEA_CBC_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_idea_cbc_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_IDEA_CBC_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_IDEA_CBC_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_IDEA_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_idea_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_IDEA_CBC_SHA: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_IDEA_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_NULL_MD5](https://developer.apple.com/documentation/security/ssl_rsa_with_null_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_NULL_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_NULL_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/ssl_rsa_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_RC2_CBC_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_rc2_cbc_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_RC2_CBC_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_RC2_CBC_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_rc4_128_md5)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_RC4_128_MD5: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_RC4_128_MD5: SSLCipherSuite { get } ``` |

Modified [SSL_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/ssl_rsa_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var SSL_RSA_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var SSL_RSA_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [SSLAddDistinguishedName(_: SSLContext, _: UnsafePointer<Void>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1400906-ssladddistinguishedname)

|  | Declaration |
| --- | --- |
| From | ``` func SSLAddDistinguishedName(_ context: SSLContext!, _ derDN: UnsafePointer<Void>, _ derDNLen: Int) -> OSStatus ``` |
| To | ``` func SSLAddDistinguishedName(_ context: SSLContext, _ derDN: UnsafePointer<Void>, _ derDNLen: Int) -> OSStatus ``` |

Modified [SSLClose(_: SSLContext) -> OSStatus](https://developer.apple.com/documentation/security/1397869-sslclose)

|  | Declaration |
| --- | --- |
| From | ``` func SSLClose(_ context: SSLContext!) -> OSStatus ``` |
| To | ``` func SSLClose(_ context: SSLContext) -> OSStatus ``` |

Modified [SSLCopyCertificateAuthorities(_: SSLContext, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1401971-sslcopycertificateauthorities)

|  | Declaration |
| --- | --- |
| From | ``` func SSLCopyCertificateAuthorities(_ context: SSLContext!, _ certificates: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SSLCopyCertificateAuthorities(_ context: SSLContext, _ certificates: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SSLCopyDistinguishedNames(_: SSLContext, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/security/1398461-sslcopydistinguishednames)

|  | Declaration |
| --- | --- |
| From | ``` func SSLCopyDistinguishedNames(_ context: SSLContext!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SSLCopyDistinguishedNames(_ context: SSLContext, _ names: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [SSLCopyPeerTrust(_: SSLContext, _: UnsafeMutablePointer<SecTrust?>) -> OSStatus](https://developer.apple.com/documentation/security/1397674-sslcopypeertrust)

|  | Declaration |
| --- | --- |
| From | ``` func SSLCopyPeerTrust(_ context: SSLContext!, _ trust: UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus ``` |
| To | ``` func SSLCopyPeerTrust(_ context: SSLContext, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus ``` |

Modified [SSLCreateContext(_: CFAllocator?, _: SSLProtocolSide, _: SSLConnectionType) -> SSLContext?](https://developer.apple.com/documentation/security/1393063-sslcreatecontext)

|  | Declaration |
| --- | --- |
| From | ``` func SSLCreateContext(_ alloc: CFAllocator!, _ protocolSide: SSLProtocolSide, _ connectionType: SSLConnectionType) -> Unmanaged<SSLContext>! ``` |
| To | ``` func SSLCreateContext(_ alloc: CFAllocator?, _ protocolSide: SSLProtocolSide, _ connectionType: SSLConnectionType) -> SSLContext? ``` |

Modified [SSLGetBufferedReadSize(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1394958-sslgetbufferedreadsize)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetBufferedReadSize(_ context: SSLContext!, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetBufferedReadSize(_ context: SSLContext, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetClientCertificateState(_: SSLContext, _: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus](https://developer.apple.com/documentation/security/1396612-sslgetclientcertificatestate)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetClientCertificateState(_ context: SSLContext!, _ clientState: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus ``` |
| To | ``` func SSLGetClientCertificateState(_ context: SSLContext, _ clientState: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus ``` |

Modified [SSLGetConnection(_: SSLContext, _: UnsafeMutablePointer<SSLConnectionRef>) -> OSStatus](https://developer.apple.com/documentation/security/1397993-sslgetconnection)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetConnection(_ context: SSLContext!, _ connection: UnsafeMutablePointer<SSLConnectionRef>) -> OSStatus ``` |
| To | ``` func SSLGetConnection(_ context: SSLContext, _ connection: UnsafeMutablePointer<SSLConnectionRef>) -> OSStatus ``` |

Modified [SSLGetDatagramWriteSize(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1401259-sslgetdatagramwritesize)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetDatagramWriteSize(_ dtlsContext: SSLContext!, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetDatagramWriteSize(_ dtlsContext: SSLContext, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetDiffieHellmanParams(_: SSLContext, _: UnsafeMutablePointer<UnsafePointer<Void>>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1399892-sslgetdiffiehellmanparams)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetDiffieHellmanParams(_ context: SSLContext!, _ dhParams: UnsafeMutablePointer<UnsafePointer<Void>>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeMutablePointer<UnsafePointer<Void>>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetEnabledCiphers(_: SSLContext, _: UnsafeMutablePointer<SSLCipherSuite>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1399101-sslgetenabledciphers)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetEnabledCiphers(_ context: SSLContext!, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetEnabledCiphers(_ context: SSLContext, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetMaxDatagramRecordSize(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1399678-sslgetmaxdatagramrecordsize)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetMaxDatagramRecordSize(_ dtlsContext: SSLContext!, _ maxSize: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetMaxDatagramRecordSize(_ dtlsContext: SSLContext, _ maxSize: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetNegotiatedCipher(_: SSLContext, _: UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus](https://developer.apple.com/documentation/security/1394448-sslgetnegotiatedcipher)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetNegotiatedCipher(_ context: SSLContext!, _ cipherSuite: UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus ``` |
| To | ``` func SSLGetNegotiatedCipher(_ context: SSLContext, _ cipherSuite: UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus ``` |

Modified [SSLGetNegotiatedProtocolVersion(_: SSLContext, _: UnsafeMutablePointer<SSLProtocol>) -> OSStatus](https://developer.apple.com/documentation/security/1397382-sslgetnegotiatedprotocolversion)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetNegotiatedProtocolVersion(_ context: SSLContext!, _ `protocol`: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |
| To | ``` func SSLGetNegotiatedProtocolVersion(_ context: SSLContext, _ `protocol`: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |

Modified [SSLGetNumberEnabledCiphers(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1399570-sslgetnumberenabledciphers)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetNumberEnabledCiphers(_ context: SSLContext!, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetNumberEnabledCiphers(_ context: SSLContext, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetNumberSupportedCiphers(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1402304-sslgetnumbersupportedciphers)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetNumberSupportedCiphers(_ context: SSLContext!, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetNumberSupportedCiphers(_ context: SSLContext, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetPeerDomainName(_: SSLContext, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1400295-sslgetpeerdomainname)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetPeerDomainName(_ context: SSLContext!, _ peerName: UnsafeMutablePointer<Int8>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetPeerDomainName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<Int8>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetPeerDomainNameLength(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1398086-sslgetpeerdomainnamelength)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetPeerDomainNameLength(_ context: SSLContext!, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetPeerDomainNameLength(_ context: SSLContext, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetPeerID(_: SSLContext, _: UnsafeMutablePointer<UnsafePointer<Void>>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1395882-sslgetpeerid)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetPeerID(_ context: SSLContext!, _ peerID: UnsafeMutablePointer<UnsafePointer<Void>>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetPeerID(_ context: SSLContext, _ peerID: UnsafeMutablePointer<UnsafePointer<Void>>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetProtocolVersionMax(_: SSLContext, _: UnsafeMutablePointer<SSLProtocol>) -> OSStatus](https://developer.apple.com/documentation/security/1396167-sslgetprotocolversionmax)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetProtocolVersionMax(_ context: SSLContext!, _ maxVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |
| To | ``` func SSLGetProtocolVersionMax(_ context: SSLContext, _ maxVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |

Modified [SSLGetProtocolVersionMin(_: SSLContext, _: UnsafeMutablePointer<SSLProtocol>) -> OSStatus](https://developer.apple.com/documentation/security/1395690-sslgetprotocolversionmin)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetProtocolVersionMin(_ context: SSLContext!, _ minVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |
| To | ``` func SSLGetProtocolVersionMin(_ context: SSLContext, _ minVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |

Modified [SSLGetSessionOption(_: SSLContext, _: SSLSessionOption, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/security/1392604-sslgetsessionoption)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetSessionOption(_ context: SSLContext!, _ option: SSLSessionOption, _ value: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func SSLGetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [SSLGetSessionState(_: SSLContext, _: UnsafeMutablePointer<SSLSessionState>) -> OSStatus](https://developer.apple.com/documentation/security/1393517-sslgetsessionstate)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetSessionState(_ context: SSLContext!, _ state: UnsafeMutablePointer<SSLSessionState>) -> OSStatus ``` |
| To | ``` func SSLGetSessionState(_ context: SSLContext, _ state: UnsafeMutablePointer<SSLSessionState>) -> OSStatus ``` |

Modified [SSLGetSupportedCiphers(_: SSLContext, _: UnsafeMutablePointer<SSLCipherSuite>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1395230-sslgetsupportedciphers)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetSupportedCiphers(_ context: SSLContext!, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetSupportedCiphers(_ context: SSLContext, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLHandshake(_: SSLContext) -> OSStatus](https://developer.apple.com/documentation/security/1400161-sslhandshake)

|  | Declaration |
| --- | --- |
| From | ``` func SSLHandshake(_ context: SSLContext!) -> OSStatus ``` |
| To | ``` func SSLHandshake(_ context: SSLContext) -> OSStatus ``` |

Modified [SSLRead(_: SSLContext, _: UnsafeMutablePointer<Void>, _: Int, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1394324-sslread)

|  | Declaration |
| --- | --- |
| From | ``` func SSLRead(_ context: SSLContext!, _ data: UnsafeMutablePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLRead(_ context: SSLContext, _ data: UnsafeMutablePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLReadFunc](https://developer.apple.com/documentation/security/sslreadfunc)

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLReadFunc = CFunctionPointer<((SSLConnectionRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus)> ``` |
| To | ``` typealias SSLReadFunc = (SSLConnectionRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLSetCertificate(_: SSLContext, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/security/1392400-sslsetcertificate)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetCertificate(_ context: SSLContext!, _ certRefs: CFArray!) -> OSStatus ``` |
| To | ``` func SSLSetCertificate(_ context: SSLContext, _ certRefs: CFArray) -> OSStatus ``` |

Modified [SSLSetCertificateAuthorities(_: SSLContext, _: AnyObject, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1396770-sslsetcertificateauthorities)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetCertificateAuthorities(_ context: SSLContext!, _ certificateOrArray: AnyObject!, _ replaceExisting: Boolean) -> OSStatus ``` |
| To | ``` func SSLSetCertificateAuthorities(_ context: SSLContext, _ certificateOrArray: AnyObject, _ replaceExisting: Bool) -> OSStatus ``` |

Modified [SSLSetClientSideAuthenticate(_: SSLContext, _: SSLAuthenticate) -> OSStatus](https://developer.apple.com/documentation/security/1397567-sslsetclientsideauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetClientSideAuthenticate(_ context: SSLContext!, _ auth: SSLAuthenticate) -> OSStatus ``` |
| To | ``` func SSLSetClientSideAuthenticate(_ context: SSLContext, _ auth: SSLAuthenticate) -> OSStatus ``` |

Modified [SSLSetConnection(_: SSLContext, _: SSLConnectionRef) -> OSStatus](https://developer.apple.com/documentation/security/1398843-sslsetconnection)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetConnection(_ context: SSLContext!, _ connection: SSLConnectionRef) -> OSStatus ``` |
| To | ``` func SSLSetConnection(_ context: SSLContext, _ connection: SSLConnectionRef) -> OSStatus ``` |

Modified [SSLSetDatagramHelloCookie(_: SSLContext, _: UnsafePointer<Void>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1398936-sslsetdatagramhellocookie)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext!, _ cookie: UnsafePointer<Void>, _ cookieLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext, _ cookie: UnsafePointer<Void>, _ cookieLen: Int) -> OSStatus ``` |

Modified [SSLSetDiffieHellmanParams(_: SSLContext, _: UnsafePointer<Void>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1392524-sslsetdiffiehellmanparams)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetDiffieHellmanParams(_ context: SSLContext!, _ dhParams: UnsafePointer<Void>, _ dhParamsLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafePointer<Void>, _ dhParamsLen: Int) -> OSStatus ``` |

Modified [SSLSetEnabledCiphers(_: SSLContext, _: UnsafePointer<SSLCipherSuite>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1397188-sslsetenabledciphers)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetEnabledCiphers(_ context: SSLContext!, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: Int) -> OSStatus ``` |
| To | ``` func SSLSetEnabledCiphers(_ context: SSLContext, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: Int) -> OSStatus ``` |

Modified [SSLSetEncryptionCertificate(_: SSLContext, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/security/1398098-sslsetencryptioncertificate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func SSLSetEncryptionCertificate(_ context: SSLContext!, _ certRefs: CFArray!) -> OSStatus ``` | -- |
| To | ``` func SSLSetEncryptionCertificate(_ context: SSLContext, _ certRefs: CFArray) -> OSStatus ``` | OS X 10.11 |

Modified [SSLSetIOFuncs(_: SSLContext, _: SSLReadFunc, _: SSLWriteFunc) -> OSStatus](https://developer.apple.com/documentation/security/1396081-sslsetiofuncs)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetIOFuncs(_ context: SSLContext!, _ readFunc: SSLReadFunc, _ writeFunc: SSLWriteFunc) -> OSStatus ``` |
| To | ``` func SSLSetIOFuncs(_ context: SSLContext, _ readFunc: SSLReadFunc, _ writeFunc: SSLWriteFunc) -> OSStatus ``` |

Modified [SSLSetMaxDatagramRecordSize(_: SSLContext, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1394978-sslsetmaxdatagramrecordsize)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetMaxDatagramRecordSize(_ dtlsContext: SSLContext!, _ maxSize: Int) -> OSStatus ``` |
| To | ``` func SSLSetMaxDatagramRecordSize(_ dtlsContext: SSLContext, _ maxSize: Int) -> OSStatus ``` |

Modified [SSLSetPeerDomainName(_: SSLContext, _: UnsafePointer<Int8>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1393047-sslsetpeerdomainname)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetPeerDomainName(_ context: SSLContext!, _ peerName: UnsafePointer<Int8>, _ peerNameLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetPeerDomainName(_ context: SSLContext, _ peerName: UnsafePointer<Int8>, _ peerNameLen: Int) -> OSStatus ``` |

Modified [SSLSetPeerID(_: SSLContext, _: UnsafePointer<Void>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1400006-sslsetpeerid)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetPeerID(_ context: SSLContext!, _ peerID: UnsafePointer<Void>, _ peerIDLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetPeerID(_ context: SSLContext, _ peerID: UnsafePointer<Void>, _ peerIDLen: Int) -> OSStatus ``` |

Modified [SSLSetProtocolVersionMax(_: SSLContext, _: SSLProtocol) -> OSStatus](https://developer.apple.com/documentation/security/1393798-sslsetprotocolversionmax)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetProtocolVersionMax(_ context: SSLContext!, _ maxVersion: SSLProtocol) -> OSStatus ``` |
| To | ``` func SSLSetProtocolVersionMax(_ context: SSLContext, _ maxVersion: SSLProtocol) -> OSStatus ``` |

Modified [SSLSetProtocolVersionMin(_: SSLContext, _: SSLProtocol) -> OSStatus](https://developer.apple.com/documentation/security/1398139-sslsetprotocolversionmin)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetProtocolVersionMin(_ context: SSLContext!, _ minVersion: SSLProtocol) -> OSStatus ``` |
| To | ``` func SSLSetProtocolVersionMin(_ context: SSLContext, _ minVersion: SSLProtocol) -> OSStatus ``` |

Modified [SSLSetSessionOption(_: SSLContext, _: SSLSessionOption, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1399173-sslsetsessionoption)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetSessionOption(_ context: SSLContext!, _ option: SSLSessionOption, _ value: Boolean) -> OSStatus ``` |
| To | ``` func SSLSetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: Bool) -> OSStatus ``` |

Modified [SSLWrite(_: SSLContext, _: UnsafePointer<Void>, _: Int, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1400864-sslwrite)

|  | Declaration |
| --- | --- |
| From | ``` func SSLWrite(_ context: SSLContext!, _ data: UnsafePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLWrite(_ context: SSLContext, _ data: UnsafePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLWriteFunc](https://developer.apple.com/documentation/security/sslwritefunc)

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLWriteFunc = CFunctionPointer<((SSLConnectionRef, UnsafePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus)> ``` |
| To | ``` typealias SSLWriteFunc = (SSLConnectionRef, UnsafePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [TLS_DH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_anon_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_256_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_AES_256_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_AES_256_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DH_anon_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/tls_dh_anon_with_rc4_128_md5)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_anon_WITH_RC4_128_MD5: Int { get } ``` |
| To | ``` var TLS_DH_anon_WITH_RC4_128_MD5: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_dss_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_256_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_AES_256_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_AES_256_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_DSS_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_DSS_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_DH_DSS_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_256_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_AES_256_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_AES_256_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DH_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DH_RSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_DH_RSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_AES_256_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_AES_256_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_DSS_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_DSS_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_DHE_DSS_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_dhe_psk_with_null_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_NULL_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_NULL_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/tls_dhe_psk_with_null_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_NULL_SHA384: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_NULL_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_PSK_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_PSK_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_256_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_AES_256_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_AES_256_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_DHE_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_DHE_RSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_DHE_RSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_anon_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_anon_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_anon_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_anon_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_anon_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_anon_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_anon_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_anon_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_anon_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_anon_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_anon_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_anon_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_anon_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_anon_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_anon_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_anon_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_anon_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_ECDSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_ECDSA_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_ECDSA_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDH_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDH_RSA_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_ECDH_RSA_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_ECDSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_ECDSA_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_ECDSA_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_rsa_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_ECDHE_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_ECDHE_RSA_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_ECDHE_RSA_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_EMPTY_RENEGOTIATION_INFO_SCSV](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_empty_renegotiation_info_scsv)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_EMPTY_RENEGOTIATION_INFO_SCSV: Int { get } ``` |
| To | ``` var TLS_EMPTY_RENEGOTIATION_INFO_SCSV: SSLCipherSuite { get } ``` |

Modified [TLS_NULL_WITH_NULL_NULL](https://developer.apple.com/documentation/security/tls_null_with_null_null)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_NULL_WITH_NULL_NULL: Int { get } ``` |
| To | ``` var TLS_NULL_WITH_NULL_NULL: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_psk_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_psk_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_psk_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_null_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_NULL_SHA256: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_NULL_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_null_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_NULL_SHA384: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_NULL_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_psk_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_PSK_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_PSK_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_256_cbc_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_AES_256_CBC_SHA384: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_AES_256_CBC_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_rsa_psk_with_null_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_NULL_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_NULL_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/tls_rsa_psk_with_null_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_NULL_SHA384: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_NULL_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_PSK_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_PSK_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_3des_ede_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_3DES_EDE_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_3DES_EDE_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_aes_128_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_AES_128_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_AES_128_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_128_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_AES_128_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_AES_128_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_128_gcm_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_AES_128_GCM_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_AES_128_GCM_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_aes_256_cbc_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_AES_256_CBC_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_AES_256_CBC_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_256_cbc_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_AES_256_CBC_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_AES_256_CBC_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_aes_256_gcm_sha384)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_AES_256_GCM_SHA384: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_AES_256_GCM_SHA384: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_NULL_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_null_md5)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_NULL_MD5: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_NULL_MD5: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_null_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_NULL_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_NULL_SHA: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_null_sha256)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_NULL_SHA256: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_NULL_SHA256: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_rc4_128_md5)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_RC4_128_MD5: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_RC4_128_MD5: SSLCipherSuite { get } ``` |

Modified [TLS_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_rc4_128_sha)

|  | Declaration |
| --- | --- |
| From | ``` var TLS_RSA_WITH_RC4_128_SHA: Int { get } ``` |
| To | ``` var TLS_RSA_WITH_RC4_128_SHA: SSLCipherSuite { get } ``` |

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
