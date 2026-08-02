---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Security.html
archived_at: '2026-07-18T02:52:39.068951Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Security Changes

## Security

Removed SecAccessControlCreateFlags.valueAdded AuthorizationExternalForm.init()Added AuthorizationExternalForm.init(bytes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added AuthorizationItem.init()Added AuthorizationItem.init(name: AuthorizationString, valueLength: Int, value: UnsafeMutablePointer<Void>, flags: UInt32)Added AuthorizationItemSet.init()Added AuthorizationItemSet.init(count: UInt32, items: UnsafeMutablePointer<AuthorizationItem>)Added CSSM_APPLE_CL_CSR_REQUEST.init()Added CSSM_APPLE_CL_CSR_REQUEST.init(subjectNameX509: CSSM_X509_NAME_PTR, signatureAlg: CSSM_ALGORITHMS, signatureOid: CSSM_OID, cspHand: CSSM_CSP_HANDLE, subjectPublicKey: UnsafePointer<CSSM_KEY>, subjectPrivateKey: UnsafePointer<CSSM_KEY>, challengeString: UnsafePointer<Int8>)Added CSSM_APPLE_TP_ACTION_DATA.init()Added CSSM_APPLE_TP_ACTION_DATA.init(Version: uint32, ActionFlags: CSSM_APPLE_TP_ACTION_FLAGS)Added CSSM_APPLE_TP_CERT_REQUEST.init()Added CSSM_APPLE_TP_CERT_REQUEST.init(cspHand: CSSM_CSP_HANDLE, clHand: CSSM_CL_HANDLE, serialNumber: uint32, numSubjectNames: uint32, subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, numIssuerNames: uint32, issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, issuerNameX509: CSSM_X509_NAME_PTR, certPublicKey: UnsafePointer<CSSM_KEY>, issuerPrivateKey: UnsafePointer<CSSM_KEY>, signatureAlg: CSSM_ALGORITHMS, signatureOid: CSSM_OID, notBefore: uint32, notAfter: uint32, numExtensions: uint32, extensions: UnsafeMutablePointer<CE_DataAndType>, challengeString: UnsafePointer<Int8>)Added CSSM_APPLE_TP_CRL_OPTIONS.init()Added CSSM_APPLE_TP_CRL_OPTIONS.init(Version: uint32, CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore: CSSM_DL_DB_HANDLE_PTR)Added CSSM_APPLE_TP_NAME_OID.init()Added CSSM_APPLE_TP_NAME_OID.init(string: UnsafePointer<Int8>, oid: UnsafePointer<CSSM_OID>)Added CSSM_APPLE_TP_SMIME_OPTIONS.init()Added CSSM_APPLE_TP_SMIME_OPTIONS.init(Version: uint32, IntendedUsage: CE_KeyUsage, SenderEmailLen: uint32, SenderEmail: UnsafePointer<Int8>)Added CSSM_APPLE_TP_SSL_OPTIONS.init()Added CSSM_APPLE_TP_SSL_OPTIONS.init(Version: uint32, ServerNameLen: uint32, ServerName: UnsafePointer<Int8>, Flags: uint32)Added CSSM_TP_APPLE_EVIDENCE_HEADER.init()Added CSSM_TP_APPLE_EVIDENCE_HEADER.init(Version: uint32)Added CSSM_TP_APPLE_EVIDENCE_INFO.init()Added CSSM_TP_APPLE_EVIDENCE_INFO.init(StatusBits: CSSM_TP_APPLE_CERT_STATUS, NumStatusCodes: uint32, StatusCodes: UnsafeMutablePointer<CSSM_RETURN>, Index: uint32, DlDbHandle: CSSM_DL_DB_HANDLE, UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR)Added SecAccessControlCreateFlags.init(rawValue: CFIndex)Added SecAsn1Template_struct.init()Added SecAsn1Template_struct.init(kind: UInt32, offset: UInt32, sub: UnsafePointer<Void>, size: UInt32)Added SecItemImportExportKeyParameters.init()Added SecItemImportExportKeyParameters.init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<AnyObject>!, alertTitle: Unmanaged<CFString>!, alertPrompt: Unmanaged<CFString>!, accessRef: Unmanaged<SecAccess>!, keyUsage: Unmanaged<CFArray>!, keyAttributes: Unmanaged<CFArray>!)Added SecKeyImportExportParameters.init()Added SecKeyImportExportParameters.init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<AnyObject>!, alertTitle: Unmanaged<CFString>!, alertPrompt: Unmanaged<CFString>!, accessRef: Unmanaged<SecAccess>!, keyUsage: CSSM_KEYUSE, keyAttributes: CSSM_KEYATTR_FLAGS)Added SecKeychainAttribute.init()Added SecKeychainAttribute.init(tag: SecKeychainAttrType, length: UInt32, data: UnsafeMutablePointer<Void>)Added SecKeychainAttributeInfo.init()Added SecKeychainAttributeInfo.init(count: UInt32, tag: UnsafeMutablePointer<UInt32>, format: UnsafeMutablePointer<UInt32>)Added SecKeychainAttributeList.init()Added SecKeychainAttributeList.init(count: UInt32, attr: UnsafeMutablePointer<SecKeychainAttribute>)Added SecKeychainCallbackInfo.init()Added SecKeychainCallbackInfo.init(version: UInt32, item: Unmanaged<SecKeychainItem>!, keychain: Unmanaged<SecKeychain>!, pid: pid_t)Added SecKeychainSettings.init()Added SecKeychainSettings.init(version: UInt32, lockOnSleep: Boolean, useLockInterval: Boolean, lockInterval: UInt32)Added cssm_access_credentials.init()Added cssm_access_credentials.init(EntryTag: CSSM_STRING, BaseCerts: CSSM_BASE_CERTS, Samples: CSSM_SAMPLEGROUP, Callback: CSSM_CHALLENGE_CALLBACK, CallerCtx: UnsafeMutablePointer<Void>)Added cssm_acl_edit.init()Added cssm_acl_edit.init(EditMode: CSSM_ACL_EDIT_MODE, OldEntryHandle: CSSM_ACL_HANDLE, NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT>)Added cssm_acl_entry_info.init()Added cssm_acl_entry_info.init(EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE, EntryHandle: CSSM_ACL_HANDLE)Added cssm_acl_entry_input.init()Added cssm_acl_entry_input.init(Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback: CSSM_ACL_SUBJECT_CALLBACK, CallerContext: UnsafeMutablePointer<Void>)Added cssm_acl_entry_prototype.init()Added cssm_acl_entry_prototype.init(TypedSubject: CSSM_LIST, Delegate: CSSM_BOOL, Authorization: CSSM_AUTHORIZATIONGROUP, TimeRange: CSSM_ACL_VALIDITY_PERIOD, EntryTag: CSSM_STRING)Added cssm_acl_keychain_prompt_selector.init()Added cssm_acl_keychain_prompt_selector.init(version: uint16, flags: uint16)Added cssm_acl_owner_prototype.init()Added cssm_acl_owner_prototype.init(TypedSubject: CSSM_LIST, Delegate: CSSM_BOOL)Added cssm_acl_process_subject_selector.init()Added cssm_acl_process_subject_selector.init(version: uint16, mask: uint16, uid: uint32, gid: uint32)Added cssm_acl_validity_period.init()Added cssm_acl_validity_period.init(StartDate: CSSM_DATA, EndDate: CSSM_DATA)Added cssm_applecspdl_db_change_password_parameters.init()Added cssm_applecspdl_db_change_password_parameters.init(accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS>)Added cssm_applecspdl_db_is_locked_parameters.init()Added cssm_applecspdl_db_is_locked_parameters.init(isLocked: uint8)Added cssm_applecspdl_db_settings_parameters.init()Added cssm_applecspdl_db_settings_parameters.init(idleTimeout: uint32, lockOnSleep: uint8)Added cssm_appledl_open_parameters.init()Added cssm_appledl_open_parameters.init(length: uint32, version: uint32, autoCommit: CSSM_BOOL, mask: uint32, mode: mode_t)Added cssm_authorizationgroup.init()Added cssm_authorizationgroup.init(NumberOfAuthTags: uint32, AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>)Added cssm_base_certs.init()Added cssm_base_certs.init(TPHandle: CSSM_TP_HANDLE, CLHandle: CSSM_CL_HANDLE, Certs: CSSM_CERTGROUP)Added cssm_cert_bundle.init()Added cssm_cert_bundle.init(BundleHeader: CSSM_CERT_BUNDLE_HEADER, Bundle: CSSM_DATA)Added cssm_cert_bundle_header.init()Added cssm_cert_bundle_header.init(BundleType: CSSM_CERT_BUNDLE_TYPE, BundleEncoding: CSSM_CERT_BUNDLE_ENCODING)Added cssm_cert_pair.init()Added cssm_cert_pair.init(EncodedCert: CSSM_ENCODED_CERT, ParsedCert: CSSM_PARSED_CERT)Added cssm_certgroup.init()Added cssm_context.init()Added cssm_context.init(ContextType: CSSM_CONTEXT_TYPE, AlgorithmType: CSSM_ALGORITHMS, NumberOfAttributes: uint32, ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR, CSPHandle: CSSM_CSP_HANDLE, Privileged: CSSM_BOOL, EncryptionProhibited: uint32, WorkFactor: uint32, Reserved: uint32)Added cssm_context_attribute.init()Added cssm_context_attribute.AttributeAdded cssm_context_attribute.init(AttributeType: CSSM_ATTRIBUTE_TYPE, AttributeLength: uint32, Attribute: cssm_context_attribute_value)Added cssm_crl_pair.init()Added cssm_crl_pair.init(EncodedCrl: CSSM_ENCODED_CRL, ParsedCrl: CSSM_PARSED_CRL)Added cssm_crlgroup.init()Added cssm_crypto_data.init()Added cssm_crypto_data.init(Param: CSSM_DATA, Callback: CSSM_CALLBACK, CallerCtx: UnsafeMutablePointer<Void>)Added cssm_csp_operational_statistics.init()Added cssm_csp_operational_statistics.init(UserAuthenticated: CSSM_BOOL, DeviceFlags: CSSM_CSP_FLAGS, TokenMaxSessionCount: uint32, TokenOpenedSessionCount: uint32, TokenMaxRWSessionCount: uint32, TokenOpenedRWSessionCount: uint32, TokenTotalPublicMem: uint32, TokenFreePublicMem: uint32, TokenTotalPrivateMem: uint32, TokenFreePrivateMem: uint32)Added cssm_data.init()Added cssm_data.init(Length: CSSM_SIZE, Data: UnsafeMutablePointer<uint8>)Added cssm_date.init()Added cssm_date.init(Year: (uint8, uint8, uint8, uint8), Month:(uint8, uint8), Day:(uint8, uint8))Added cssm_db_attribute_data.init()Added cssm_db_attribute_data.init(Info: CSSM_DB_ATTRIBUTE_INFO, NumberOfValues: uint32, Value: CSSM_DATA_PTR)Added cssm_db_attribute_info.init()Added cssm_db_attribute_info.init(AttributeNameFormat: CSSM_DB_ATTRIBUTE_NAME_FORMAT, Label: cssm_db_attribute_label, AttributeFormat: CSSM_DB_ATTRIBUTE_FORMAT)Added cssm_db_attribute_info.LabelAdded cssm_db_index_info.init()Added cssm_db_index_info.init(IndexType: CSSM_DB_INDEX_TYPE, IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION, Info: CSSM_DB_ATTRIBUTE_INFO)Added cssm_db_parsing_module_info.init()Added cssm_db_parsing_module_info.init(RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid: CSSM_SUBSERVICE_UID)Added cssm_db_record_attribute_data.init()Added cssm_db_record_attribute_data.init(DataRecordType: CSSM_DB_RECORDTYPE, SemanticInformation: uint32, NumberOfAttributes: uint32, AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR)Added cssm_db_record_attribute_info.init()Added cssm_db_record_attribute_info.init(DataRecordType: CSSM_DB_RECORDTYPE, NumberOfAttributes: uint32, AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR)Added cssm_db_record_index_info.init()Added cssm_db_record_index_info.init(DataRecordType: CSSM_DB_RECORDTYPE, NumberOfIndexes: uint32, IndexInfo: CSSM_DB_INDEX_INFO_PTR)Added cssm_db_schema_attribute_info.init()Added cssm_db_schema_attribute_info.init(AttributeId: uint32, AttributeName: UnsafeMutablePointer<Int8>, AttributeNameID: CSSM_OID, DataType: CSSM_DB_ATTRIBUTE_FORMAT)Added cssm_db_schema_index_info.init()Added cssm_db_schema_index_info.init(AttributeId: uint32, IndexId: uint32, IndexType: CSSM_DB_INDEX_TYPE, IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION)Added cssm_db_unique_record.init()Added cssm_db_unique_record.init(RecordLocator: CSSM_DB_INDEX_INFO, RecordIdentifier: CSSM_DATA)Added cssm_dbinfo.init()Added cssm_dbinfo.init(NumberOfRecordTypes: uint32, DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR, RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR, RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR, IsLocal: CSSM_BOOL, AccessPath: UnsafeMutablePointer<Int8>, Reserved: UnsafeMutablePointer<Void>)Added cssm_dl_db_handle.init()Added cssm_dl_db_handle.init(DLHandle: CSSM_DL_HANDLE, DBHandle: CSSM_DB_HANDLE)Added cssm_dl_db_list.init()Added cssm_dl_db_list.init(NumHandles: uint32, DLDBHandle: CSSM_DL_DB_HANDLE_PTR)Added cssm_dl_pkcs11_attributes.init()Added cssm_dl_pkcs11_attributes.init(DeviceAccessFlags: uint32)Added cssm_encoded_cert.init()Added cssm_encoded_cert.init(CertType: CSSM_CERT_TYPE, CertEncoding: CSSM_CERT_ENCODING, CertBlob: CSSM_DATA)Added cssm_encoded_crl.init()Added cssm_encoded_crl.init(CrlType: CSSM_CRL_TYPE, CrlEncoding: CSSM_CRL_ENCODING, CrlBlob: CSSM_DATA)Added cssm_evidence.init()Added cssm_evidence.init(EvidenceForm: CSSM_EVIDENCE_FORM, Evidence: UnsafeMutablePointer<Void>)Added cssm_field.init()Added cssm_field.init(FieldOid: CSSM_OID, FieldValue: CSSM_DATA)Added cssm_fieldgroup.init()Added cssm_fieldgroup.init(NumberOfFields: Int32, Fields: CSSM_FIELD_PTR)Added cssm_func_name_addr.init()Added cssm_func_name_addr.init(Name: CSSM_STRING, Address: CSSM_PROC_ADDR)Added cssm_guid.init()Added cssm_guid.init(Data1: uint32, Data2: uint16, Data3: uint16, Data4:(uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8))Added cssm_kea_derive_params.init()Added cssm_kea_derive_params.init(Rb: CSSM_DATA, Yb: CSSM_DATA)Added cssm_key.init()Added cssm_key.init(KeyHeader: CSSM_KEYHEADER, KeyData: CSSM_DATA)Added cssm_key_size.init()Added cssm_key_size.init(LogicalKeySizeInBits: uint32, EffectiveKeySizeInBits: uint32)Added cssm_keyheader.init()Added cssm_keyheader.init(HeaderVersion: CSSM_HEADERVERSION, CspId: CSSM_GUID, BlobType: CSSM_KEYBLOB_TYPE, Format: CSSM_KEYBLOB_FORMAT, AlgorithmId: CSSM_ALGORITHMS, KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits: uint32, KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage: CSSM_KEYUSE, StartDate: CSSM_DATE, EndDate: CSSM_DATE, WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode: CSSM_ENCRYPT_MODE, Reserved: uint32)Added cssm_kr_name.init()Added cssm_kr_name.init(Type: uint8, Length: uint8, Name: UnsafeMutablePointer<Int8>)Added cssm_kr_policy_info.init()Added cssm_kr_policy_info.init(krbNotAllowed: CSSM_BOOL, numberOfEntries: uint32, policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM>)Added cssm_kr_policy_list_item.init()Added cssm_kr_profile.init()Added cssm_kr_profile.init(UserName: CSSM_KR_NAME, UserCertificate: CSSM_CERTGROUP_PTR, KRSCertChain: CSSM_CERTGROUP_PTR, LE_KRANum: uint8, LE_KRACertChainList: CSSM_CERTGROUP_PTR, ENT_KRANum: uint8, ENT_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_KRANum: uint8, INDIV_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_AuthenticationInfo: CSSM_DATA_PTR, KRSPFlags: uint32, KRSPExtensions: CSSM_DATA_PTR)Added cssm_kr_wrappedproductinfo.init()Added cssm_kr_wrappedproductinfo.init(StandardVersion: CSSM_VERSION, StandardDescription: CSSM_STRING, ProductVersion: CSSM_VERSION, ProductDescription: CSSM_STRING, ProductVendor: CSSM_STRING, ProductFlags: uint32)Added cssm_krsubservice.init()Added cssm_krsubservice.init(SubServiceId: uint32, Description: UnsafeMutablePointer<Int8>, WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO)Added cssm_list.init()Added cssm_list.init(ListType: CSSM_LIST_TYPE, Head: CSSM_LIST_ELEMENT_PTR, Tail: CSSM_LIST_ELEMENT_PTR)Added cssm_list_element.init()Added cssm_manager_event_notification.init()Added cssm_manager_event_notification.init(DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType: CSSM_SERVICE_MASK, Event: CSSM_MANAGER_EVENT_TYPES, EventId: uint32, EventData: CSSM_DATA)Added cssm_manager_registration_info.init()Added cssm_manager_registration_info.init(Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>, Terminate: CFunctionPointer<(() -> CSSM_RETURN)>, RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>, DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>, EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>, RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>)Added cssm_memory_funcs.init()Added cssm_memory_funcs.init(malloc_func: CSSM_MALLOC, free_func: CSSM_FREE, realloc_func: CSSM_REALLOC, calloc_func: CSSM_CALLOC, AllocRef: UnsafeMutablePointer<Void>)Added cssm_module_funcs.init()Added cssm_module_funcs.init(ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs: uint32, ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR>)Added cssm_name_list.init()Added cssm_name_list.init(NumStrings: uint32, String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)Added cssm_net_address.init()Added cssm_net_address.init(AddressType: CSSM_NET_ADDRESS_TYPE, Address: CSSM_DATA)Added cssm_parsed_cert.init()Added cssm_parsed_cert.init(CertType: CSSM_CERT_TYPE, ParsedCertFormat: CSSM_CERT_PARSE_FORMAT, ParsedCert: UnsafeMutablePointer<Void>)Added cssm_parsed_crl.init()Added cssm_parsed_crl.init(CrlType: CSSM_CRL_TYPE, ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT, ParsedCrl: UnsafeMutablePointer<Void>)Added cssm_pkcs1_oaep_params.init()Added cssm_pkcs1_oaep_params.init(HashAlgorithm: uint32, HashParams: CSSM_DATA, MGF: CSSM_PKCS_OAEP_MGF, MGFParams: CSSM_DATA, PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams: CSSM_DATA)Added cssm_pkcs5_pbkdf1_params.init()Added cssm_pkcs5_pbkdf1_params.init(Passphrase: CSSM_DATA, InitVector: CSSM_DATA)Added cssm_pkcs5_pbkdf2_params.init()Added cssm_pkcs5_pbkdf2_params.init(Passphrase: CSSM_DATA, PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF)Added cssm_query.init()Added cssm_query.init(RecordType: CSSM_DB_RECORDTYPE, Conjunctive: CSSM_DB_CONJUNCTIVE, NumSelectionPredicates: uint32, SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR, QueryLimits: CSSM_QUERY_LIMITS, QueryFlags: CSSM_QUERY_FLAGS)Added cssm_query_limits.init()Added cssm_query_limits.init(TimeLimit: uint32, SizeLimit: uint32)Added cssm_query_size_data.init()Added cssm_query_size_data.init(SizeInputBlock: uint32, SizeOutputBlock: uint32)Added cssm_range.init()Added cssm_range.init(Min: uint32, Max: uint32)Added cssm_resource_control_context.init()Added cssm_resource_control_context.init(AccessCred: CSSM_ACCESS_CREDENTIALS_PTR, InitialAclEntry: CSSM_ACL_ENTRY_INPUT)Added cssm_sample.init()Added cssm_sample.init(TypedSample: CSSM_LIST, Verifier: UnsafePointer<CSSM_SUBSERVICE_UID>)Added cssm_samplegroup.init()Added cssm_samplegroup.init(NumberOfSamples: uint32, Samples: UnsafePointer<CSSM_SAMPLE>)Added cssm_selection_predicate.init()Added cssm_selection_predicate.init(DbOperator: CSSM_DB_OPERATOR, Attribute: CSSM_DB_ATTRIBUTE_DATA)Added cssm_spi_ac_funcs.init()Added cssm_spi_ac_funcs.init(AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Added cssm_spi_cl_funcs.init()Added cssm_spi_csp_funcs.init()Added cssm_spi_dl_funcs.init()Added cssm_spi_dl_funcs.init(DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose: CFunctionPointer<((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)>, DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>, CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>, Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>, GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)>, ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)>, GetDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)>, ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)>, GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList: CFunctionPointer<((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Added cssm_spi_kr_funcs.init()Added cssm_spi_kr_funcs.init(RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>, GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>, ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>, RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)>, GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>)Added cssm_spi_tp_funcs.init()Added cssm_state_funcs.init()Added cssm_state_funcs.init(cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>, cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>, cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>, cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>)Added cssm_subservice_uid.init()Added cssm_subservice_uid.init(Guid: CSSM_GUID, Version: CSSM_VERSION, SubserviceId: uint32, SubserviceType: CSSM_SERVICE_TYPE)Added cssm_tp_authority_id.init()Added cssm_tp_authority_id.init(AuthorityCert: UnsafeMutablePointer<CSSM_DATA>, AuthorityLocation: CSSM_NET_ADDRESS_PTR)Added cssm_tp_callerauth_context.init()Added cssm_tp_callerauth_context.init(Policy: CSSM_TP_POLICYINFO, VerifyTime: CSSM_TIMESTRING, VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK, NumberOfAnchorCerts: uint32, AnchorCerts: CSSM_DATA_PTR, DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_tp_certchange_input.init()Added cssm_tp_certchange_input.init(Action: CSSM_TP_CERTCHANGE_ACTION, Reason: CSSM_TP_CERTCHANGE_REASON, CLHandle: CSSM_CL_HANDLE, Cert: CSSM_DATA_PTR, ChangeInfo: CSSM_FIELD_PTR, StartTime: CSSM_TIMESTRING, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_tp_certchange_output.init()Added cssm_tp_certchange_output.init(ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo: CSSM_FIELD)Added cssm_tp_certissue_input.init()Added cssm_tp_certissue_input.init(CSPSubserviceUid: CSSM_SUBSERVICE_UID, CLHandle: CSSM_CL_HANDLE, NumberOfTemplateFields: uint32, SubjectCertFields: CSSM_FIELD_PTR, MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls: uint32, ServiceControls: CSSM_FIELD_PTR, UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_tp_certissue_output.init()Added cssm_tp_certissue_output.init(IssueStatus: CSSM_TP_CERTISSUE_STATUS, CertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests: CSSM_TP_SERVICES)Added cssm_tp_certnotarize_input.init()Added cssm_tp_certnotarize_input.init(CLHandle: CSSM_CL_HANDLE, NumberOfFields: uint32, MoreFields: CSSM_FIELD_PTR, SignScope: CSSM_FIELD_PTR, ScopeSize: uint32, MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls: uint32, ServiceControls: CSSM_FIELD_PTR, UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_tp_certnotarize_output.init()Added cssm_tp_certnotarize_output.init(NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS, NotarizedCertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests: CSSM_TP_SERVICES)Added cssm_tp_certreclaim_input.init()Added cssm_tp_certreclaim_input.init(CLHandle: CSSM_CL_HANDLE, NumberOfSelectionFields: uint32, SelectionFields: CSSM_FIELD_PTR, UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_tp_certreclaim_output.init()Added cssm_tp_certreclaim_output.init(ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS, ReclaimedCertGroup: CSSM_CERTGROUP_PTR, KeyCacheHandle: CSSM_LONG_HANDLE)Added cssm_tp_certverify_input.init()Added cssm_tp_certverify_input.init(CLHandle: CSSM_CL_HANDLE, Cert: CSSM_DATA_PTR, VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR)Added cssm_tp_certverify_output.init()Added cssm_tp_certverify_output.init(VerifyStatus: CSSM_TP_CERTVERIFY_STATUS, NumberOfEvidence: uint32, Evidence: CSSM_EVIDENCE_PTR)Added cssm_tp_confirm_response.init()Added cssm_tp_confirm_response.init(NumberOfResponses: uint32, Responses: CSSM_TP_CONFIRM_STATUS_PTR)Added cssm_tp_crlissue_input.init()Added cssm_tp_crlissue_input.init(CLHandle: CSSM_CL_HANDLE, CrlIdentifier: uint32, CrlThisTime: CSSM_TIMESTRING, PolicyIdentifier: CSSM_FIELD_PTR, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_tp_crlissue_output.init()Added cssm_tp_crlissue_output.init(IssueStatus: CSSM_TP_CRLISSUE_STATUS, Crl: CSSM_ENCODED_CRL_PTR, CrlNextTime: CSSM_TIMESTRING)Added cssm_tp_policyinfo.init()Added cssm_tp_policyinfo.init(NumberOfPolicyIds: uint32, PolicyIds: CSSM_FIELD_PTR, PolicyControl: UnsafeMutablePointer<Void>)Added cssm_tp_request_set.init()Added cssm_tp_request_set.init(NumberOfRequests: uint32, Requests: UnsafeMutablePointer<Void>)Added cssm_tp_result_set.init()Added cssm_tp_result_set.init(NumberOfResults: uint32, Results: UnsafeMutablePointer<Void>)Added cssm_tp_verify_context.init()Added cssm_tp_verify_context.init(Action: CSSM_TP_ACTION, ActionData: CSSM_DATA, Crls: CSSM_CRLGROUP, Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR)Added cssm_tp_verify_context_result.init()Added cssm_tp_verify_context_result.init(NumberOfEvidences: uint32, Evidence: CSSM_EVIDENCE_PTR)Added cssm_tuplegroup.init()Added cssm_tuplegroup.init(NumberOfTuples: uint32, Tuples: CSSM_TUPLE_PTR)Added cssm_upcalls.init()Added cssm_upcalls.init(malloc_func: CSSM_UPCALLS_MALLOC, free_func: CSSM_UPCALLS_FREE, realloc_func: CSSM_UPCALLS_REALLOC, calloc_func: CSSM_UPCALLS_CALLOC, CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>, GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>)Added cssm_version.init()Added cssm_version.init(Major: uint32, Minor: uint32)Added cssm_x509_algorithm_identifier.init()Added cssm_x509_algorithm_identifier.init(algorithm: CSSM_OID, parameters: CSSM_DATA)Added cssm_x509_extension.init()Added cssm_x509_extension.init(extnId: CSSM_OID, critical: CSSM_BOOL, format: CSSM_X509EXT_DATA_FORMAT, value: cssm_x509ext_value, BERvalue: CSSM_DATA)Added cssm_x509_extension.valueAdded cssm_x509_extensionTagAndValue.init()Added cssm_x509_extensionTagAndValue.init(type: CSSM_BER_TAG, value: CSSM_DATA)Added cssm_x509_extensions.init()Added cssm_x509_extensions.init(numberOfExtensions: uint32, extensions: CSSM_X509_EXTENSION_PTR)Added cssm_x509_name.init()Added cssm_x509_name.init(numberOfRDNs: uint32, RelativeDistinguishedName: CSSM_X509_RDN_PTR)Added cssm_x509_rdn.init()Added cssm_x509_rdn.init(numberOfPairs: uint32, AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR)Added cssm_x509_revoked_cert_entry.init()Added cssm_x509_revoked_cert_entry.init(certificateSerialNumber: CSSM_DATA, revocationDate: CSSM_X509_TIME, extensions: CSSM_X509_EXTENSIONS)Added cssm_x509_revoked_cert_list.init()Added cssm_x509_revoked_cert_list.init(numberOfRevokedCertEntries: uint32, revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR)Added cssm_x509_signature.init()Added cssm_x509_signature.init(algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER, encrypted: CSSM_DATA)Added cssm_x509_signed_certificate.init()Added cssm_x509_signed_certificate.init(certificate: CSSM_X509_TBS_CERTIFICATE, signature: CSSM_X509_SIGNATURE)Added cssm_x509_signed_crl.init()Added cssm_x509_signed_crl.init(tbsCertList: CSSM_X509_TBS_CERTLIST, signature: CSSM_X509_SIGNATURE)Added cssm_x509_subject_public_key_info.init()Added cssm_x509_subject_public_key_info.init(algorithm: CSSM_X509_ALGORITHM_IDENTIFIER, subjectPublicKey: CSSM_DATA)Added cssm_x509_tbs_certificate.init()Added cssm_x509_tbs_certificate.init(version: CSSM_DATA, serialNumber: CSSM_DATA, signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer: CSSM_X509_NAME, validity: CSSM_X509_VALIDITY, subject: CSSM_X509_NAME, subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO, issuerUniqueIdentifier: CSSM_DATA, subjectUniqueIdentifier: CSSM_DATA, extensions: CSSM_X509_EXTENSIONS)Added cssm_x509_tbs_certlist.init()Added cssm_x509_tbs_certlist.init(version: CSSM_DATA, signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer: CSSM_X509_NAME, thisUpdate: CSSM_X509_TIME, nextUpdate: CSSM_X509_TIME, revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR, extensions: CSSM_X509_EXTENSIONS)Added cssm_x509_time.init()Added cssm_x509_time.init(timeType: CSSM_BER_TAG, time: CSSM_DATA)Added cssm_x509_type_value_pair.init()Added cssm_x509_type_value_pair.init(type: CSSM_OID, valueType: CSSM_BER_TAG, value: CSSM_DATA)Added cssm_x509ext_basicConstraints.init()Added cssm_x509ext_basicConstraints.init(cA: CSSM_BOOL, pathLenConstraintPresent: CSSM_X509_OPTION, pathLenConstraint: uint32)Added cssm_x509ext_pair.init()Added cssm_x509ext_pair.init(tagAndValue: CSSM_X509EXT_TAGandVALUE, parsedValue: UnsafeMutablePointer<Void>)Added cssm_x509ext_policyInfo.init()Added cssm_x509ext_policyInfo.init(policyIdentifier: CSSM_OID, policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS)Added cssm_x509ext_policyQualifierInfo.init()Added cssm_x509ext_policyQualifierInfo.init(policyQualifierId: CSSM_OID, value: CSSM_DATA)Added cssm_x509ext_policyQualifiers.init()Added cssm_x509ext_policyQualifiers.init(numberOfPolicyQualifiers: uint32, policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO>)Added mds_funcs.init()Added mds_funcs.init(DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>, GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>)Added x509_validity.init()Added x509_validity.init(notBefore: CSSM_X509_TIME, notAfter: CSSM_X509_TIME)Added CMSDecoderCopySignerTimestampWithPolicy(CMSDecoder!, AnyObject!, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatusAdded CMSEncoderCopySignerTimestampWithPolicy(CMSEncoder!, AnyObject!, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatusAdded CSSMERR_APPLETP_CA_PIN_MISMATCHAdded errSecCSAmbiguousBundleFormatAdded errSecCSBadFrameworkVersionAdded errSecCSBadMainExecutableAdded errSecCSCancelledAdded errSecCSDSStoreSymlinkAdded errSecCSUnsealedFrameworkRootAdded errSecCSWeakResourceEnvelopeAdded errSecCSWeakResourceRulesAdded kSSLSessionOptionFallbackAdded kSecCSCheckGatekeeperArchitecturesAdded kSecCSFullReportAdded kSecCSNoNetworkAccessAdded kSecCSReportProgressAdded kSecCSStrictValidateAdded kSecTrustSettingsAllowedErrorAdded kSecTrustSettingsApplicationAdded kSecTrustSettingsKeyUsageAdded kSecTrustSettingsPolicyAdded kSecTrustSettingsPolicyStringAdded kSecTrustSettingsResultModified AuthorizationExternalForm [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationExternalForm {     var bytes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct AuthorizationExternalForm {     var bytes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(bytes bytes: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified AuthorizationItem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationItem {     var name: AuthorizationString     var valueLength: UInt     var value: UnsafePointer<()>     var flags: UInt32 } ``` |
| To | ``` struct AuthorizationItem {     var name: AuthorizationString     var valueLength: Int     var value: UnsafeMutablePointer<Void>     var flags: UInt32     init()     init(name name: AuthorizationString, valueLength valueLength: Int, value value: UnsafeMutablePointer<Void>, flags flags: UInt32) } ``` |

Modified AuthorizationItem.value

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafePointer<()> ``` |
| To | ``` var value: UnsafeMutablePointer<Void> ``` |

Modified AuthorizationItem.valueLength

|  | Declaration |
| --- | --- |
| From | ``` var valueLength: UInt ``` |
| To | ``` var valueLength: Int ``` |

Modified AuthorizationItemSet [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationItemSet {     var count: UInt32     var items: UnsafePointer<AuthorizationItem> } ``` |
| To | ``` struct AuthorizationItemSet {     var count: UInt32     var items: UnsafeMutablePointer<AuthorizationItem>     init()     init(count count: UInt32, items items: UnsafeMutablePointer<AuthorizationItem>) } ``` |

Modified AuthorizationItemSet.items

|  | Declaration |
| --- | --- |
| From | ``` var items: UnsafePointer<AuthorizationItem> ``` |
| To | ``` var items: UnsafeMutablePointer<AuthorizationItem> ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_CL_CSR_REQUEST {     var subjectNameX509: CSSM_X509_NAME_PTR     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var cspHand: CSSM_CSP_HANDLE     var subjectPublicKey: ConstUnsafePointer<CSSM_KEY>     var subjectPrivateKey: ConstUnsafePointer<CSSM_KEY>     var challengeString: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct CSSM_APPLE_CL_CSR_REQUEST {     var subjectNameX509: CSSM_X509_NAME_PTR     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var cspHand: CSSM_CSP_HANDLE     var subjectPublicKey: UnsafePointer<CSSM_KEY>     var subjectPrivateKey: UnsafePointer<CSSM_KEY>     var challengeString: UnsafePointer<Int8>     init()     init(subjectNameX509 subjectNameX509: CSSM_X509_NAME_PTR, signatureAlg signatureAlg: CSSM_ALGORITHMS, signatureOid signatureOid: CSSM_OID, cspHand cspHand: CSSM_CSP_HANDLE, subjectPublicKey subjectPublicKey: UnsafePointer<CSSM_KEY>, subjectPrivateKey subjectPrivateKey: UnsafePointer<CSSM_KEY>, challengeString challengeString: UnsafePointer<Int8>) } ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.challengeString

|  | Declaration |
| --- | --- |
| From | ``` var challengeString: ConstUnsafePointer<Int8> ``` |
| To | ``` var challengeString: UnsafePointer<Int8> ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.subjectPrivateKey

|  | Declaration |
| --- | --- |
| From | ``` var subjectPrivateKey: ConstUnsafePointer<CSSM_KEY> ``` |
| To | ``` var subjectPrivateKey: UnsafePointer<CSSM_KEY> ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.subjectPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var subjectPublicKey: ConstUnsafePointer<CSSM_KEY> ``` |
| To | ``` var subjectPublicKey: UnsafePointer<CSSM_KEY> ``` |

Modified CSSM_APPLE_TP_ACTION_DATA [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_ACTION_DATA {     var Version: uint32     var ActionFlags: CSSM_APPLE_TP_ACTION_FLAGS } ``` |
| To | ``` struct CSSM_APPLE_TP_ACTION_DATA {     var Version: uint32     var ActionFlags: CSSM_APPLE_TP_ACTION_FLAGS     init()     init(Version Version: uint32, ActionFlags ActionFlags: CSSM_APPLE_TP_ACTION_FLAGS) } ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_CERT_REQUEST {     var cspHand: CSSM_CSP_HANDLE     var clHand: CSSM_CL_HANDLE     var serialNumber: uint32     var numSubjectNames: uint32     var subjectNames: UnsafePointer<CSSM_APPLE_TP_NAME_OID>     var numIssuerNames: uint32     var issuerNames: UnsafePointer<CSSM_APPLE_TP_NAME_OID>     var issuerNameX509: CSSM_X509_NAME_PTR     var certPublicKey: ConstUnsafePointer<CSSM_KEY>     var issuerPrivateKey: ConstUnsafePointer<CSSM_KEY>     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var notBefore: uint32     var notAfter: uint32     var numExtensions: uint32     var extensions: UnsafePointer<CE_DataAndType>     var challengeString: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct CSSM_APPLE_TP_CERT_REQUEST {     var cspHand: CSSM_CSP_HANDLE     var clHand: CSSM_CL_HANDLE     var serialNumber: uint32     var numSubjectNames: uint32     var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>     var numIssuerNames: uint32     var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>     var issuerNameX509: CSSM_X509_NAME_PTR     var certPublicKey: UnsafePointer<CSSM_KEY>     var issuerPrivateKey: UnsafePointer<CSSM_KEY>     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var notBefore: uint32     var notAfter: uint32     var numExtensions: uint32     var extensions: UnsafeMutablePointer<CE_DataAndType>     var challengeString: UnsafePointer<Int8>     init()     init(cspHand cspHand: CSSM_CSP_HANDLE, clHand clHand: CSSM_CL_HANDLE, serialNumber serialNumber: uint32, numSubjectNames numSubjectNames: uint32, subjectNames subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, numIssuerNames numIssuerNames: uint32, issuerNames issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, issuerNameX509 issuerNameX509: CSSM_X509_NAME_PTR, certPublicKey certPublicKey: UnsafePointer<CSSM_KEY>, issuerPrivateKey issuerPrivateKey: UnsafePointer<CSSM_KEY>, signatureAlg signatureAlg: CSSM_ALGORITHMS, signatureOid signatureOid: CSSM_OID, notBefore notBefore: uint32, notAfter notAfter: uint32, numExtensions numExtensions: uint32, extensions extensions: UnsafeMutablePointer<CE_DataAndType>, challengeString challengeString: UnsafePointer<Int8>) } ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.certPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var certPublicKey: ConstUnsafePointer<CSSM_KEY> ``` |
| To | ``` var certPublicKey: UnsafePointer<CSSM_KEY> ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.challengeString

|  | Declaration |
| --- | --- |
| From | ``` var challengeString: ConstUnsafePointer<Int8> ``` |
| To | ``` var challengeString: UnsafePointer<Int8> ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.extensions

|  | Declaration |
| --- | --- |
| From | ``` var extensions: UnsafePointer<CE_DataAndType> ``` |
| To | ``` var extensions: UnsafeMutablePointer<CE_DataAndType> ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.issuerNames

|  | Declaration |
| --- | --- |
| From | ``` var issuerNames: UnsafePointer<CSSM_APPLE_TP_NAME_OID> ``` |
| To | ``` var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID> ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.issuerPrivateKey

|  | Declaration |
| --- | --- |
| From | ``` var issuerPrivateKey: ConstUnsafePointer<CSSM_KEY> ``` |
| To | ``` var issuerPrivateKey: UnsafePointer<CSSM_KEY> ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.subjectNames

|  | Declaration |
| --- | --- |
| From | ``` var subjectNames: UnsafePointer<CSSM_APPLE_TP_NAME_OID> ``` |
| To | ``` var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID> ``` |

Modified CSSM_APPLE_TP_CRL_OPTIONS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_CRL_OPTIONS {     var Version: uint32     var CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS     var crlStore: CSSM_DL_DB_HANDLE_PTR } ``` |
| To | ``` struct CSSM_APPLE_TP_CRL_OPTIONS {     var Version: uint32     var CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS     var crlStore: CSSM_DL_DB_HANDLE_PTR     init()     init(Version Version: uint32, CrlFlags CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore crlStore: CSSM_DL_DB_HANDLE_PTR) } ``` |

Modified CSSM_APPLE_TP_NAME_OID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_NAME_OID {     var string: ConstUnsafePointer<Int8>     var oid: ConstUnsafePointer<CSSM_OID> } ``` |
| To | ``` struct CSSM_APPLE_TP_NAME_OID {     var string: UnsafePointer<Int8>     var oid: UnsafePointer<CSSM_OID>     init()     init(string string: UnsafePointer<Int8>, oid oid: UnsafePointer<CSSM_OID>) } ``` |

Modified CSSM_APPLE_TP_NAME_OID.oid

|  | Declaration |
| --- | --- |
| From | ``` var oid: ConstUnsafePointer<CSSM_OID> ``` |
| To | ``` var oid: UnsafePointer<CSSM_OID> ``` |

Modified CSSM_APPLE_TP_NAME_OID.string

|  | Declaration |
| --- | --- |
| From | ``` var string: ConstUnsafePointer<Int8> ``` |
| To | ``` var string: UnsafePointer<Int8> ``` |

Modified CSSM_APPLE_TP_SMIME_OPTIONS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_SMIME_OPTIONS {     var Version: uint32     var IntendedUsage: CE_KeyUsage     var SenderEmailLen: uint32     var SenderEmail: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct CSSM_APPLE_TP_SMIME_OPTIONS {     var Version: uint32     var IntendedUsage: CE_KeyUsage     var SenderEmailLen: uint32     var SenderEmail: UnsafePointer<Int8>     init()     init(Version Version: uint32, IntendedUsage IntendedUsage: CE_KeyUsage, SenderEmailLen SenderEmailLen: uint32, SenderEmail SenderEmail: UnsafePointer<Int8>) } ``` |

Modified CSSM_APPLE_TP_SMIME_OPTIONS.SenderEmail

|  | Declaration |
| --- | --- |
| From | ``` var SenderEmail: ConstUnsafePointer<Int8> ``` |
| To | ``` var SenderEmail: UnsafePointer<Int8> ``` |

Modified CSSM_APPLE_TP_SSL_OPTIONS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_SSL_OPTIONS {     var Version: uint32     var ServerNameLen: uint32     var ServerName: ConstUnsafePointer<Int8>     var Flags: uint32 } ``` |
| To | ``` struct CSSM_APPLE_TP_SSL_OPTIONS {     var Version: uint32     var ServerNameLen: uint32     var ServerName: UnsafePointer<Int8>     var Flags: uint32     init()     init(Version Version: uint32, ServerNameLen ServerNameLen: uint32, ServerName ServerName: UnsafePointer<Int8>, Flags Flags: uint32) } ``` |

Modified CSSM_APPLE_TP_SSL_OPTIONS.ServerName

|  | Declaration |
| --- | --- |
| From | ``` var ServerName: ConstUnsafePointer<Int8> ``` |
| To | ``` var ServerName: UnsafePointer<Int8> ``` |

Modified CSSM_TP_APPLE_EVIDENCE_HEADER [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_TP_APPLE_EVIDENCE_HEADER {     var Version: uint32 } ``` |
| To | ``` struct CSSM_TP_APPLE_EVIDENCE_HEADER {     var Version: uint32     init()     init(Version Version: uint32) } ``` |

Modified CSSM_TP_APPLE_EVIDENCE_INFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_TP_APPLE_EVIDENCE_INFO {     var StatusBits: CSSM_TP_APPLE_CERT_STATUS     var NumStatusCodes: uint32     var StatusCodes: UnsafePointer<CSSM_RETURN>     var Index: uint32     var DlDbHandle: CSSM_DL_DB_HANDLE     var UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR } ``` |
| To | ``` struct CSSM_TP_APPLE_EVIDENCE_INFO {     var StatusBits: CSSM_TP_APPLE_CERT_STATUS     var NumStatusCodes: uint32     var StatusCodes: UnsafeMutablePointer<CSSM_RETURN>     var Index: uint32     var DlDbHandle: CSSM_DL_DB_HANDLE     var UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR     init()     init(StatusBits StatusBits: CSSM_TP_APPLE_CERT_STATUS, NumStatusCodes NumStatusCodes: uint32, StatusCodes StatusCodes: UnsafeMutablePointer<CSSM_RETURN>, Index Index: uint32, DlDbHandle DlDbHandle: CSSM_DL_DB_HANDLE, UniqueRecord UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR) } ``` |

Modified CSSM_TP_APPLE_EVIDENCE_INFO.StatusCodes

|  | Declaration |
| --- | --- |
| From | ``` var StatusCodes: UnsafePointer<CSSM_RETURN> ``` |
| To | ``` var StatusCodes: UnsafeMutablePointer<CSSM_RETURN> ``` |

Modified SecAccessControlCreateFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecAccessControlCreateFlags : RawOptionSet {     init(_ value: CFIndex)     var value: CFIndex     static var UserPresence: SecAccessControlCreateFlags { get } } ``` | RawOptionSet |
| To | ``` struct SecAccessControlCreateFlags : RawOptionSetType {     init(_ rawValue: CFIndex)     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get } } ``` | RawOptionSetType |

Modified SecAccessControlCreateFlags.init(_: CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFIndex) ``` |
| To | ``` init(_ rawValue: CFIndex) ``` |

Modified SecAsn1Template_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecAsn1Template_struct {     var kind: UInt32     var offset: UInt32     var sub: ConstUnsafePointer<()>     var size: UInt32 } ``` |
| To | ``` struct SecAsn1Template_struct {     var kind: UInt32     var offset: UInt32     var sub: UnsafePointer<Void>     var size: UInt32     init()     init(kind kind: UInt32, offset offset: UInt32, sub sub: UnsafePointer<Void>, size size: UInt32) } ``` |

Modified SecAsn1Template_struct.sub

|  | Declaration |
| --- | --- |
| From | ``` var sub: ConstUnsafePointer<()> ``` |
| To | ``` var sub: UnsafePointer<Void> ``` |

Modified SecItemImportExportKeyParameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecItemImportExportKeyParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>!     var alertTitle: Unmanaged<CFString>!     var alertPrompt: Unmanaged<CFString>!     var accessRef: Unmanaged<SecAccess>!     var keyUsage: Unmanaged<CFArray>!     var keyAttributes: Unmanaged<CFArray>! } ``` |
| To | ``` struct SecItemImportExportKeyParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>!     var alertTitle: Unmanaged<CFString>!     var alertPrompt: Unmanaged<CFString>!     var accessRef: Unmanaged<SecAccess>!     var keyUsage: Unmanaged<CFArray>!     var keyAttributes: Unmanaged<CFArray>!     init()     init(version version: UInt32, flags flags: SecKeyImportExportFlags, passphrase passphrase: Unmanaged<AnyObject>!, alertTitle alertTitle: Unmanaged<CFString>!, alertPrompt alertPrompt: Unmanaged<CFString>!, accessRef accessRef: Unmanaged<SecAccess>!, keyUsage keyUsage: Unmanaged<CFArray>!, keyAttributes keyAttributes: Unmanaged<CFArray>!) } ``` |

Modified SecKeyImportExportParameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeyImportExportParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>!     var alertTitle: Unmanaged<CFString>!     var alertPrompt: Unmanaged<CFString>!     var accessRef: Unmanaged<SecAccess>!     var keyUsage: CSSM_KEYUSE     var keyAttributes: CSSM_KEYATTR_FLAGS } ``` |
| To | ``` struct SecKeyImportExportParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>!     var alertTitle: Unmanaged<CFString>!     var alertPrompt: Unmanaged<CFString>!     var accessRef: Unmanaged<SecAccess>!     var keyUsage: CSSM_KEYUSE     var keyAttributes: CSSM_KEYATTR_FLAGS     init()     init(version version: UInt32, flags flags: SecKeyImportExportFlags, passphrase passphrase: Unmanaged<AnyObject>!, alertTitle alertTitle: Unmanaged<CFString>!, alertPrompt alertPrompt: Unmanaged<CFString>!, accessRef accessRef: Unmanaged<SecAccess>!, keyUsage keyUsage: CSSM_KEYUSE, keyAttributes keyAttributes: CSSM_KEYATTR_FLAGS) } ``` |

Modified SecKeychainAttribute [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttribute {     var tag: SecKeychainAttrType     var length: UInt32     var data: UnsafePointer<()> } ``` |
| To | ``` struct SecKeychainAttribute {     var tag: SecKeychainAttrType     var length: UInt32     var data: UnsafeMutablePointer<Void>     init()     init(tag tag: SecKeychainAttrType, length length: UInt32, data data: UnsafeMutablePointer<Void>) } ``` |

Modified SecKeychainAttribute.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafePointer<()> ``` |
| To | ``` var data: UnsafeMutablePointer<Void> ``` |

Modified SecKeychainAttributeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttributeInfo {     var count: UInt32     var tag: UnsafePointer<UInt32>     var format: UnsafePointer<UInt32> } ``` |
| To | ``` struct SecKeychainAttributeInfo {     var count: UInt32     var tag: UnsafeMutablePointer<UInt32>     var format: UnsafeMutablePointer<UInt32>     init()     init(count count: UInt32, tag tag: UnsafeMutablePointer<UInt32>, format format: UnsafeMutablePointer<UInt32>) } ``` |

Modified SecKeychainAttributeInfo.format

|  | Declaration |
| --- | --- |
| From | ``` var format: UnsafePointer<UInt32> ``` |
| To | ``` var format: UnsafeMutablePointer<UInt32> ``` |

Modified SecKeychainAttributeInfo.tag

|  | Declaration |
| --- | --- |
| From | ``` var tag: UnsafePointer<UInt32> ``` |
| To | ``` var tag: UnsafeMutablePointer<UInt32> ``` |

Modified SecKeychainAttributeList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttributeList {     var count: UInt32     var attr: UnsafePointer<SecKeychainAttribute> } ``` |
| To | ``` struct SecKeychainAttributeList {     var count: UInt32     var attr: UnsafeMutablePointer<SecKeychainAttribute>     init()     init(count count: UInt32, attr attr: UnsafeMutablePointer<SecKeychainAttribute>) } ``` |

Modified SecKeychainAttributeList.attr

|  | Declaration |
| --- | --- |
| From | ``` var attr: UnsafePointer<SecKeychainAttribute> ``` |
| To | ``` var attr: UnsafeMutablePointer<SecKeychainAttribute> ``` |

Modified SecKeychainCallbackInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainCallbackInfo {     var version: UInt32     var item: Unmanaged<SecKeychainItem>!     var keychain: Unmanaged<SecKeychain>!     var pid: pid_t } ``` |
| To | ``` struct SecKeychainCallbackInfo {     var version: UInt32     var item: Unmanaged<SecKeychainItem>!     var keychain: Unmanaged<SecKeychain>!     var pid: pid_t     init()     init(version version: UInt32, item item: Unmanaged<SecKeychainItem>!, keychain keychain: Unmanaged<SecKeychain>!, pid pid: pid_t) } ``` |

Modified SecKeychainSettings [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainSettings {     var version: UInt32     var lockOnSleep: Boolean     var useLockInterval: Boolean     var lockInterval: UInt32 } ``` |
| To | ``` struct SecKeychainSettings {     var version: UInt32     var lockOnSleep: Boolean     var useLockInterval: Boolean     var lockInterval: UInt32     init()     init(version version: UInt32, lockOnSleep lockOnSleep: Boolean, useLockInterval useLockInterval: Boolean, lockInterval lockInterval: UInt32) } ``` |

Modified cssm_access_credentials [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_access_credentials {     var EntryTag: CSSM_STRING     var BaseCerts: CSSM_BASE_CERTS     var Samples: CSSM_SAMPLEGROUP     var Callback: CSSM_CHALLENGE_CALLBACK     var CallerCtx: UnsafePointer<()> } ``` |
| To | ``` struct cssm_access_credentials {     var EntryTag: CSSM_STRING     var BaseCerts: CSSM_BASE_CERTS     var Samples: CSSM_SAMPLEGROUP     var Callback: CSSM_CHALLENGE_CALLBACK     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(EntryTag EntryTag: CSSM_STRING, BaseCerts BaseCerts: CSSM_BASE_CERTS, Samples Samples: CSSM_SAMPLEGROUP, Callback Callback: CSSM_CHALLENGE_CALLBACK, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_access_credentials.CallerCtx

|  | Declaration |
| --- | --- |
| From | ``` var CallerCtx: UnsafePointer<()> ``` |
| To | ``` var CallerCtx: UnsafeMutablePointer<Void> ``` |

Modified cssm_acl_edit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_edit {     var EditMode: CSSM_ACL_EDIT_MODE     var OldEntryHandle: CSSM_ACL_HANDLE     var NewEntry: ConstUnsafePointer<CSSM_ACL_ENTRY_INPUT> } ``` |
| To | ``` struct cssm_acl_edit {     var EditMode: CSSM_ACL_EDIT_MODE     var OldEntryHandle: CSSM_ACL_HANDLE     var NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT>     init()     init(EditMode EditMode: CSSM_ACL_EDIT_MODE, OldEntryHandle OldEntryHandle: CSSM_ACL_HANDLE, NewEntry NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT>) } ``` |

Modified cssm_acl_edit.NewEntry

|  | Declaration |
| --- | --- |
| From | ``` var NewEntry: ConstUnsafePointer<CSSM_ACL_ENTRY_INPUT> ``` |
| To | ``` var NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT> ``` |

Modified cssm_acl_entry_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_info {     var EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE     var EntryHandle: CSSM_ACL_HANDLE } ``` |
| To | ``` struct cssm_acl_entry_info {     var EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE     var EntryHandle: CSSM_ACL_HANDLE     init()     init(EntryPublicInfo EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE, EntryHandle EntryHandle: CSSM_ACL_HANDLE) } ``` |

Modified cssm_acl_entry_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_input {     var Prototype: CSSM_ACL_ENTRY_PROTOTYPE     var Callback: CSSM_ACL_SUBJECT_CALLBACK     var CallerContext: UnsafePointer<()> } ``` |
| To | ``` struct cssm_acl_entry_input {     var Prototype: CSSM_ACL_ENTRY_PROTOTYPE     var Callback: CSSM_ACL_SUBJECT_CALLBACK     var CallerContext: UnsafeMutablePointer<Void>     init()     init(Prototype Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback Callback: CSSM_ACL_SUBJECT_CALLBACK, CallerContext CallerContext: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_acl_entry_input.CallerContext

|  | Declaration |
| --- | --- |
| From | ``` var CallerContext: UnsafePointer<()> ``` |
| To | ``` var CallerContext: UnsafeMutablePointer<Void> ``` |

Modified cssm_acl_entry_prototype [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_prototype {     var TypedSubject: CSSM_LIST     var Delegate: CSSM_BOOL     var Authorization: CSSM_AUTHORIZATIONGROUP     var TimeRange: CSSM_ACL_VALIDITY_PERIOD     var EntryTag: CSSM_STRING } ``` |
| To | ``` struct cssm_acl_entry_prototype {     var TypedSubject: CSSM_LIST     var Delegate: CSSM_BOOL     var Authorization: CSSM_AUTHORIZATIONGROUP     var TimeRange: CSSM_ACL_VALIDITY_PERIOD     var EntryTag: CSSM_STRING     init()     init(TypedSubject TypedSubject: CSSM_LIST, Delegate Delegate: CSSM_BOOL, Authorization Authorization: CSSM_AUTHORIZATIONGROUP, TimeRange TimeRange: CSSM_ACL_VALIDITY_PERIOD, EntryTag EntryTag: CSSM_STRING) } ``` |

Modified cssm_acl_keychain_prompt_selector [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_keychain_prompt_selector {     var version: uint16     var flags: uint16 } ``` |
| To | ``` struct cssm_acl_keychain_prompt_selector {     var version: uint16     var flags: uint16     init()     init(version version: uint16, flags flags: uint16) } ``` |

Modified cssm_acl_owner_prototype [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_owner_prototype {     var TypedSubject: CSSM_LIST     var Delegate: CSSM_BOOL } ``` |
| To | ``` struct cssm_acl_owner_prototype {     var TypedSubject: CSSM_LIST     var Delegate: CSSM_BOOL     init()     init(TypedSubject TypedSubject: CSSM_LIST, Delegate Delegate: CSSM_BOOL) } ``` |

Modified cssm_acl_process_subject_selector [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_process_subject_selector {     var version: uint16     var mask: uint16     var uid: uint32     var gid: uint32 } ``` |
| To | ``` struct cssm_acl_process_subject_selector {     var version: uint16     var mask: uint16     var uid: uint32     var gid: uint32     init()     init(version version: uint16, mask mask: uint16, uid uid: uint32, gid gid: uint32) } ``` |

Modified cssm_acl_validity_period [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_validity_period {     var StartDate: CSSM_DATA     var EndDate: CSSM_DATA } ``` |
| To | ``` struct cssm_acl_validity_period {     var StartDate: CSSM_DATA     var EndDate: CSSM_DATA     init()     init(StartDate StartDate: CSSM_DATA, EndDate EndDate: CSSM_DATA) } ``` |

Modified cssm_applecspdl_db_change_password_parameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_applecspdl_db_change_password_parameters {     var accessCredentials: UnsafePointer<CSSM_ACCESS_CREDENTIALS> } ``` |
| To | ``` struct cssm_applecspdl_db_change_password_parameters {     var accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS>     init()     init(accessCredentials accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS>) } ``` |

Modified cssm_applecspdl_db_change_password_parameters.accessCredentials

|  | Declaration |
| --- | --- |
| From | ``` var accessCredentials: UnsafePointer<CSSM_ACCESS_CREDENTIALS> ``` |
| To | ``` var accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS> ``` |

Modified cssm_applecspdl_db_is_locked_parameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_applecspdl_db_is_locked_parameters {     var isLocked: uint8 } ``` |
| To | ``` struct cssm_applecspdl_db_is_locked_parameters {     var isLocked: uint8     init()     init(isLocked isLocked: uint8) } ``` |

Modified cssm_applecspdl_db_settings_parameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_applecspdl_db_settings_parameters {     var idleTimeout: uint32     var lockOnSleep: uint8 } ``` |
| To | ``` struct cssm_applecspdl_db_settings_parameters {     var idleTimeout: uint32     var lockOnSleep: uint8     init()     init(idleTimeout idleTimeout: uint32, lockOnSleep lockOnSleep: uint8) } ``` |

Modified cssm_appledl_open_parameters [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_appledl_open_parameters {     var length: uint32     var version: uint32     var autoCommit: CSSM_BOOL     var mask: uint32     var mode: mode_t } ``` |
| To | ``` struct cssm_appledl_open_parameters {     var length: uint32     var version: uint32     var autoCommit: CSSM_BOOL     var mask: uint32     var mode: mode_t     init()     init(length length: uint32, version version: uint32, autoCommit autoCommit: CSSM_BOOL, mask mask: uint32, mode mode: mode_t) } ``` |

Modified cssm_authorizationgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_authorizationgroup {     var NumberOfAuthTags: uint32     var AuthTags: UnsafePointer<CSSM_ACL_AUTHORIZATION_TAG> } ``` |
| To | ``` struct cssm_authorizationgroup {     var NumberOfAuthTags: uint32     var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>     init()     init(NumberOfAuthTags NumberOfAuthTags: uint32, AuthTags AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>) } ``` |

Modified cssm_authorizationgroup.AuthTags

|  | Declaration |
| --- | --- |
| From | ``` var AuthTags: UnsafePointer<CSSM_ACL_AUTHORIZATION_TAG> ``` |
| To | ``` var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG> ``` |

Modified cssm_base_certs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_base_certs {     var TPHandle: CSSM_TP_HANDLE     var CLHandle: CSSM_CL_HANDLE     var Certs: CSSM_CERTGROUP } ``` |
| To | ``` struct cssm_base_certs {     var TPHandle: CSSM_TP_HANDLE     var CLHandle: CSSM_CL_HANDLE     var Certs: CSSM_CERTGROUP     init()     init(TPHandle TPHandle: CSSM_TP_HANDLE, CLHandle CLHandle: CSSM_CL_HANDLE, Certs Certs: CSSM_CERTGROUP) } ``` |

Modified cssm_cert_bundle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_cert_bundle {     var BundleHeader: CSSM_CERT_BUNDLE_HEADER     var Bundle: CSSM_DATA } ``` |
| To | ``` struct cssm_cert_bundle {     var BundleHeader: CSSM_CERT_BUNDLE_HEADER     var Bundle: CSSM_DATA     init()     init(BundleHeader BundleHeader: CSSM_CERT_BUNDLE_HEADER, Bundle Bundle: CSSM_DATA) } ``` |

Modified cssm_cert_bundle_header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_cert_bundle_header {     var BundleType: CSSM_CERT_BUNDLE_TYPE     var BundleEncoding: CSSM_CERT_BUNDLE_ENCODING } ``` |
| To | ``` struct cssm_cert_bundle_header {     var BundleType: CSSM_CERT_BUNDLE_TYPE     var BundleEncoding: CSSM_CERT_BUNDLE_ENCODING     init()     init(BundleType BundleType: CSSM_CERT_BUNDLE_TYPE, BundleEncoding BundleEncoding: CSSM_CERT_BUNDLE_ENCODING) } ``` |

Modified cssm_cert_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_cert_pair {     var EncodedCert: CSSM_ENCODED_CERT     var ParsedCert: CSSM_PARSED_CERT } ``` |
| To | ``` struct cssm_cert_pair {     var EncodedCert: CSSM_ENCODED_CERT     var ParsedCert: CSSM_PARSED_CERT     init()     init(EncodedCert EncodedCert: CSSM_ENCODED_CERT, ParsedCert ParsedCert: CSSM_PARSED_CERT) } ``` |

Modified cssm_certgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_certgroup {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var NumCerts: uint32     var CertGroupType: CSSM_CERTGROUP_TYPE     var Reserved: UnsafePointer<()> } ``` |
| To | ``` struct cssm_certgroup {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var NumCerts: uint32     var CertGroupType: CSSM_CERTGROUP_TYPE     var Reserved: UnsafeMutablePointer<Void>     init() } ``` |

Modified cssm_certgroup.Reserved

|  | Declaration |
| --- | --- |
| From | ``` var Reserved: UnsafePointer<()> ``` |
| To | ``` var Reserved: UnsafeMutablePointer<Void> ``` |

Modified cssm_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_context {     var ContextType: CSSM_CONTEXT_TYPE     var AlgorithmType: CSSM_ALGORITHMS     var NumberOfAttributes: uint32     var ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR     var CSPHandle: CSSM_CSP_HANDLE     var Privileged: CSSM_BOOL     var EncryptionProhibited: uint32     var WorkFactor: uint32     var Reserved: uint32 } ``` |
| To | ``` struct cssm_context {     var ContextType: CSSM_CONTEXT_TYPE     var AlgorithmType: CSSM_ALGORITHMS     var NumberOfAttributes: uint32     var ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR     var CSPHandle: CSSM_CSP_HANDLE     var Privileged: CSSM_BOOL     var EncryptionProhibited: uint32     var WorkFactor: uint32     var Reserved: uint32     init()     init(ContextType ContextType: CSSM_CONTEXT_TYPE, AlgorithmType AlgorithmType: CSSM_ALGORITHMS, NumberOfAttributes NumberOfAttributes: uint32, ContextAttributes ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR, CSPHandle CSPHandle: CSSM_CSP_HANDLE, Privileged Privileged: CSSM_BOOL, EncryptionProhibited EncryptionProhibited: uint32, WorkFactor WorkFactor: uint32, Reserved Reserved: uint32) } ``` |

Modified cssm_context_attribute [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_context_attribute {     var AttributeType: CSSM_ATTRIBUTE_TYPE     var AttributeLength: uint32 } ``` |
| To | ``` struct cssm_context_attribute {     var AttributeType: CSSM_ATTRIBUTE_TYPE     var AttributeLength: uint32     var Attribute: cssm_context_attribute_value     init()     init(AttributeType AttributeType: CSSM_ATTRIBUTE_TYPE, AttributeLength AttributeLength: uint32, Attribute Attribute: cssm_context_attribute_value) } ``` |

Modified cssm_crl_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crl_pair {     var EncodedCrl: CSSM_ENCODED_CRL     var ParsedCrl: CSSM_PARSED_CRL } ``` |
| To | ``` struct cssm_crl_pair {     var EncodedCrl: CSSM_ENCODED_CRL     var ParsedCrl: CSSM_PARSED_CRL     init()     init(EncodedCrl EncodedCrl: CSSM_ENCODED_CRL, ParsedCrl ParsedCrl: CSSM_PARSED_CRL) } ``` |

Modified cssm_crlgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crlgroup {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var NumberOfCrls: uint32     var CrlGroupType: CSSM_CRLGROUP_TYPE } ``` |
| To | ``` struct cssm_crlgroup {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var NumberOfCrls: uint32     var CrlGroupType: CSSM_CRLGROUP_TYPE     init() } ``` |

Modified cssm_crypto_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crypto_data {     var Param: CSSM_DATA     var Callback: CSSM_CALLBACK     var CallerCtx: UnsafePointer<()> } ``` |
| To | ``` struct cssm_crypto_data {     var Param: CSSM_DATA     var Callback: CSSM_CALLBACK     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(Param Param: CSSM_DATA, Callback Callback: CSSM_CALLBACK, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_crypto_data.CallerCtx

|  | Declaration |
| --- | --- |
| From | ``` var CallerCtx: UnsafePointer<()> ``` |
| To | ``` var CallerCtx: UnsafeMutablePointer<Void> ``` |

Modified cssm_csp_operational_statistics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_csp_operational_statistics {     var UserAuthenticated: CSSM_BOOL     var DeviceFlags: CSSM_CSP_FLAGS     var TokenMaxSessionCount: uint32     var TokenOpenedSessionCount: uint32     var TokenMaxRWSessionCount: uint32     var TokenOpenedRWSessionCount: uint32     var TokenTotalPublicMem: uint32     var TokenFreePublicMem: uint32     var TokenTotalPrivateMem: uint32     var TokenFreePrivateMem: uint32 } ``` |
| To | ``` struct cssm_csp_operational_statistics {     var UserAuthenticated: CSSM_BOOL     var DeviceFlags: CSSM_CSP_FLAGS     var TokenMaxSessionCount: uint32     var TokenOpenedSessionCount: uint32     var TokenMaxRWSessionCount: uint32     var TokenOpenedRWSessionCount: uint32     var TokenTotalPublicMem: uint32     var TokenFreePublicMem: uint32     var TokenTotalPrivateMem: uint32     var TokenFreePrivateMem: uint32     init()     init(UserAuthenticated UserAuthenticated: CSSM_BOOL, DeviceFlags DeviceFlags: CSSM_CSP_FLAGS, TokenMaxSessionCount TokenMaxSessionCount: uint32, TokenOpenedSessionCount TokenOpenedSessionCount: uint32, TokenMaxRWSessionCount TokenMaxRWSessionCount: uint32, TokenOpenedRWSessionCount TokenOpenedRWSessionCount: uint32, TokenTotalPublicMem TokenTotalPublicMem: uint32, TokenFreePublicMem TokenFreePublicMem: uint32, TokenTotalPrivateMem TokenTotalPrivateMem: uint32, TokenFreePrivateMem TokenFreePrivateMem: uint32) } ``` |

Modified cssm_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_data {     var Length: CSSM_SIZE     var Data: UnsafePointer<uint8> } ``` |
| To | ``` struct cssm_data {     var Length: CSSM_SIZE     var Data: UnsafeMutablePointer<uint8>     init()     init(Length Length: CSSM_SIZE, Data Data: UnsafeMutablePointer<uint8>) } ``` |

Modified cssm_data.Data

|  | Declaration |
| --- | --- |
| From | ``` var Data: UnsafePointer<uint8> ``` |
| To | ``` var Data: UnsafeMutablePointer<uint8> ``` |

Modified cssm_date [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_date {     var Year: (uint8, uint8, uint8, uint8)     var Month: (uint8, uint8)     var Day: (uint8, uint8) } ``` |
| To | ``` struct cssm_date {     var Year: (uint8, uint8, uint8, uint8)     var Month: (uint8, uint8)     var Day: (uint8, uint8)     init()     init(Year Year: (uint8, uint8, uint8, uint8), Month Month: (uint8, uint8), Day Day: (uint8, uint8)) } ``` |

Modified cssm_db_attribute_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_attribute_data {     var Info: CSSM_DB_ATTRIBUTE_INFO     var NumberOfValues: uint32     var Value: CSSM_DATA_PTR } ``` |
| To | ``` struct cssm_db_attribute_data {     var Info: CSSM_DB_ATTRIBUTE_INFO     var NumberOfValues: uint32     var Value: CSSM_DATA_PTR     init()     init(Info Info: CSSM_DB_ATTRIBUTE_INFO, NumberOfValues NumberOfValues: uint32, Value Value: CSSM_DATA_PTR) } ``` |

Modified cssm_db_attribute_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_attribute_info {     var AttributeNameFormat: CSSM_DB_ATTRIBUTE_NAME_FORMAT     var AttributeFormat: CSSM_DB_ATTRIBUTE_FORMAT } ``` |
| To | ``` struct cssm_db_attribute_info {     var AttributeNameFormat: CSSM_DB_ATTRIBUTE_NAME_FORMAT     var Label: cssm_db_attribute_label     var AttributeFormat: CSSM_DB_ATTRIBUTE_FORMAT     init()     init(AttributeNameFormat AttributeNameFormat: CSSM_DB_ATTRIBUTE_NAME_FORMAT, Label Label: cssm_db_attribute_label, AttributeFormat AttributeFormat: CSSM_DB_ATTRIBUTE_FORMAT) } ``` |

Modified cssm_db_index_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_index_info {     var IndexType: CSSM_DB_INDEX_TYPE     var IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION     var Info: CSSM_DB_ATTRIBUTE_INFO } ``` |
| To | ``` struct cssm_db_index_info {     var IndexType: CSSM_DB_INDEX_TYPE     var IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION     var Info: CSSM_DB_ATTRIBUTE_INFO     init()     init(IndexType IndexType: CSSM_DB_INDEX_TYPE, IndexedDataLocation IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION, Info Info: CSSM_DB_ATTRIBUTE_INFO) } ``` |

Modified cssm_db_parsing_module_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_parsing_module_info {     var RecordType: CSSM_DB_RECORDTYPE     var ModuleSubserviceUid: CSSM_SUBSERVICE_UID } ``` |
| To | ``` struct cssm_db_parsing_module_info {     var RecordType: CSSM_DB_RECORDTYPE     var ModuleSubserviceUid: CSSM_SUBSERVICE_UID     init()     init(RecordType RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid ModuleSubserviceUid: CSSM_SUBSERVICE_UID) } ``` |

Modified cssm_db_record_attribute_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_record_attribute_data {     var DataRecordType: CSSM_DB_RECORDTYPE     var SemanticInformation: uint32     var NumberOfAttributes: uint32     var AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR } ``` |
| To | ``` struct cssm_db_record_attribute_data {     var DataRecordType: CSSM_DB_RECORDTYPE     var SemanticInformation: uint32     var NumberOfAttributes: uint32     var AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, SemanticInformation SemanticInformation: uint32, NumberOfAttributes NumberOfAttributes: uint32, AttributeData AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR) } ``` |

Modified cssm_db_record_attribute_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_record_attribute_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfAttributes: uint32     var AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR } ``` |
| To | ``` struct cssm_db_record_attribute_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfAttributes: uint32     var AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, NumberOfAttributes NumberOfAttributes: uint32, AttributeInfo AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR) } ``` |

Modified cssm_db_record_index_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_record_index_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfIndexes: uint32     var IndexInfo: CSSM_DB_INDEX_INFO_PTR } ``` |
| To | ``` struct cssm_db_record_index_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfIndexes: uint32     var IndexInfo: CSSM_DB_INDEX_INFO_PTR     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, NumberOfIndexes NumberOfIndexes: uint32, IndexInfo IndexInfo: CSSM_DB_INDEX_INFO_PTR) } ``` |

Modified cssm_db_schema_attribute_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_schema_attribute_info {     var AttributeId: uint32     var AttributeName: UnsafePointer<Int8>     var AttributeNameID: CSSM_OID     var DataType: CSSM_DB_ATTRIBUTE_FORMAT } ``` |
| To | ``` struct cssm_db_schema_attribute_info {     var AttributeId: uint32     var AttributeName: UnsafeMutablePointer<Int8>     var AttributeNameID: CSSM_OID     var DataType: CSSM_DB_ATTRIBUTE_FORMAT     init()     init(AttributeId AttributeId: uint32, AttributeName AttributeName: UnsafeMutablePointer<Int8>, AttributeNameID AttributeNameID: CSSM_OID, DataType DataType: CSSM_DB_ATTRIBUTE_FORMAT) } ``` |

Modified cssm_db_schema_attribute_info.AttributeName

|  | Declaration |
| --- | --- |
| From | ``` var AttributeName: UnsafePointer<Int8> ``` |
| To | ``` var AttributeName: UnsafeMutablePointer<Int8> ``` |

Modified cssm_db_schema_index_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_schema_index_info {     var AttributeId: uint32     var IndexId: uint32     var IndexType: CSSM_DB_INDEX_TYPE     var IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION } ``` |
| To | ``` struct cssm_db_schema_index_info {     var AttributeId: uint32     var IndexId: uint32     var IndexType: CSSM_DB_INDEX_TYPE     var IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION     init()     init(AttributeId AttributeId: uint32, IndexId IndexId: uint32, IndexType IndexType: CSSM_DB_INDEX_TYPE, IndexedDataLocation IndexedDataLocation: CSSM_DB_INDEXED_DATA_LOCATION) } ``` |

Modified cssm_db_unique_record [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_unique_record {     var RecordLocator: CSSM_DB_INDEX_INFO     var RecordIdentifier: CSSM_DATA } ``` |
| To | ``` struct cssm_db_unique_record {     var RecordLocator: CSSM_DB_INDEX_INFO     var RecordIdentifier: CSSM_DATA     init()     init(RecordLocator RecordLocator: CSSM_DB_INDEX_INFO, RecordIdentifier RecordIdentifier: CSSM_DATA) } ``` |

Modified cssm_dbinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_dbinfo {     var NumberOfRecordTypes: uint32     var DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR     var RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR     var RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR     var IsLocal: CSSM_BOOL     var AccessPath: UnsafePointer<Int8>     var Reserved: UnsafePointer<()> } ``` |
| To | ``` struct cssm_dbinfo {     var NumberOfRecordTypes: uint32     var DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR     var RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR     var RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR     var IsLocal: CSSM_BOOL     var AccessPath: UnsafeMutablePointer<Int8>     var Reserved: UnsafeMutablePointer<Void>     init()     init(NumberOfRecordTypes NumberOfRecordTypes: uint32, DefaultParsingModules DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR, RecordAttributeNames RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR, RecordIndexes RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR, IsLocal IsLocal: CSSM_BOOL, AccessPath AccessPath: UnsafeMutablePointer<Int8>, Reserved Reserved: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_dbinfo.AccessPath

|  | Declaration |
| --- | --- |
| From | ``` var AccessPath: UnsafePointer<Int8> ``` |
| To | ``` var AccessPath: UnsafeMutablePointer<Int8> ``` |

Modified cssm_dbinfo.Reserved

|  | Declaration |
| --- | --- |
| From | ``` var Reserved: UnsafePointer<()> ``` |
| To | ``` var Reserved: UnsafeMutablePointer<Void> ``` |

Modified cssm_dl_db_handle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_dl_db_handle {     var DLHandle: CSSM_DL_HANDLE     var DBHandle: CSSM_DB_HANDLE } ``` |
| To | ``` struct cssm_dl_db_handle {     var DLHandle: CSSM_DL_HANDLE     var DBHandle: CSSM_DB_HANDLE     init()     init(DLHandle DLHandle: CSSM_DL_HANDLE, DBHandle DBHandle: CSSM_DB_HANDLE) } ``` |

Modified cssm_dl_db_list [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_dl_db_list {     var NumHandles: uint32     var DLDBHandle: CSSM_DL_DB_HANDLE_PTR } ``` |
| To | ``` struct cssm_dl_db_list {     var NumHandles: uint32     var DLDBHandle: CSSM_DL_DB_HANDLE_PTR     init()     init(NumHandles NumHandles: uint32, DLDBHandle DLDBHandle: CSSM_DL_DB_HANDLE_PTR) } ``` |

Modified cssm_dl_pkcs11_attributes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_dl_pkcs11_attributes {     var DeviceAccessFlags: uint32 } ``` |
| To | ``` struct cssm_dl_pkcs11_attributes {     var DeviceAccessFlags: uint32     init()     init(DeviceAccessFlags DeviceAccessFlags: uint32) } ``` |

Modified cssm_encoded_cert [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_encoded_cert {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var CertBlob: CSSM_DATA } ``` |
| To | ``` struct cssm_encoded_cert {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var CertBlob: CSSM_DATA     init()     init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, CertBlob CertBlob: CSSM_DATA) } ``` |

Modified cssm_encoded_crl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_encoded_crl {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var CrlBlob: CSSM_DATA } ``` |
| To | ``` struct cssm_encoded_crl {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var CrlBlob: CSSM_DATA     init()     init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, CrlBlob CrlBlob: CSSM_DATA) } ``` |

Modified cssm_evidence [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_evidence {     var EvidenceForm: CSSM_EVIDENCE_FORM     var Evidence: UnsafePointer<()> } ``` |
| To | ``` struct cssm_evidence {     var EvidenceForm: CSSM_EVIDENCE_FORM     var Evidence: UnsafeMutablePointer<Void>     init()     init(EvidenceForm EvidenceForm: CSSM_EVIDENCE_FORM, Evidence Evidence: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_evidence.Evidence

|  | Declaration |
| --- | --- |
| From | ``` var Evidence: UnsafePointer<()> ``` |
| To | ``` var Evidence: UnsafeMutablePointer<Void> ``` |

Modified cssm_field [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_field {     var FieldOid: CSSM_OID     var FieldValue: CSSM_DATA } ``` |
| To | ``` struct cssm_field {     var FieldOid: CSSM_OID     var FieldValue: CSSM_DATA     init()     init(FieldOid FieldOid: CSSM_OID, FieldValue FieldValue: CSSM_DATA) } ``` |

Modified cssm_fieldgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_fieldgroup {     var NumberOfFields: Int32     var Fields: CSSM_FIELD_PTR } ``` |
| To | ``` struct cssm_fieldgroup {     var NumberOfFields: Int32     var Fields: CSSM_FIELD_PTR     init()     init(NumberOfFields NumberOfFields: Int32, Fields Fields: CSSM_FIELD_PTR) } ``` |

Modified cssm_func_name_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_func_name_addr {     var Name: CSSM_STRING     var Address: CSSM_PROC_ADDR } ``` |
| To | ``` struct cssm_func_name_addr {     var Name: CSSM_STRING     var Address: CSSM_PROC_ADDR     init()     init(Name Name: CSSM_STRING, Address Address: CSSM_PROC_ADDR) } ``` |

Modified cssm_guid [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_guid {     var Data1: uint32     var Data2: uint16     var Data3: uint16     var Data4: (uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8) } ``` |
| To | ``` struct cssm_guid {     var Data1: uint32     var Data2: uint16     var Data3: uint16     var Data4: (uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8)     init()     init(Data1 Data1: uint32, Data2 Data2: uint16, Data3 Data3: uint16, Data4 Data4: (uint8, uint8, uint8, uint8, uint8, uint8, uint8, uint8)) } ``` |

Modified cssm_kea_derive_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kea_derive_params {     var Rb: CSSM_DATA     var Yb: CSSM_DATA } ``` |
| To | ``` struct cssm_kea_derive_params {     var Rb: CSSM_DATA     var Yb: CSSM_DATA     init()     init(Rb Rb: CSSM_DATA, Yb Yb: CSSM_DATA) } ``` |

Modified cssm_key [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_key {     var KeyHeader: CSSM_KEYHEADER     var KeyData: CSSM_DATA } ``` |
| To | ``` struct cssm_key {     var KeyHeader: CSSM_KEYHEADER     var KeyData: CSSM_DATA     init()     init(KeyHeader KeyHeader: CSSM_KEYHEADER, KeyData KeyData: CSSM_DATA) } ``` |

Modified cssm_key_size [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_key_size {     var LogicalKeySizeInBits: uint32     var EffectiveKeySizeInBits: uint32 } ``` |
| To | ``` struct cssm_key_size {     var LogicalKeySizeInBits: uint32     var EffectiveKeySizeInBits: uint32     init()     init(LogicalKeySizeInBits LogicalKeySizeInBits: uint32, EffectiveKeySizeInBits EffectiveKeySizeInBits: uint32) } ``` |

Modified cssm_keyheader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_keyheader {     var HeaderVersion: CSSM_HEADERVERSION     var CspId: CSSM_GUID     var BlobType: CSSM_KEYBLOB_TYPE     var Format: CSSM_KEYBLOB_FORMAT     var AlgorithmId: CSSM_ALGORITHMS     var KeyClass: CSSM_KEYCLASS     var LogicalKeySizeInBits: uint32     var KeyAttr: CSSM_KEYATTR_FLAGS     var KeyUsage: CSSM_KEYUSE     var StartDate: CSSM_DATE     var EndDate: CSSM_DATE     var WrapAlgorithmId: CSSM_ALGORITHMS     var WrapMode: CSSM_ENCRYPT_MODE     var Reserved: uint32 } ``` |
| To | ``` struct cssm_keyheader {     var HeaderVersion: CSSM_HEADERVERSION     var CspId: CSSM_GUID     var BlobType: CSSM_KEYBLOB_TYPE     var Format: CSSM_KEYBLOB_FORMAT     var AlgorithmId: CSSM_ALGORITHMS     var KeyClass: CSSM_KEYCLASS     var LogicalKeySizeInBits: uint32     var KeyAttr: CSSM_KEYATTR_FLAGS     var KeyUsage: CSSM_KEYUSE     var StartDate: CSSM_DATE     var EndDate: CSSM_DATE     var WrapAlgorithmId: CSSM_ALGORITHMS     var WrapMode: CSSM_ENCRYPT_MODE     var Reserved: uint32     init()     init(HeaderVersion HeaderVersion: CSSM_HEADERVERSION, CspId CspId: CSSM_GUID, BlobType BlobType: CSSM_KEYBLOB_TYPE, Format Format: CSSM_KEYBLOB_FORMAT, AlgorithmId AlgorithmId: CSSM_ALGORITHMS, KeyClass KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits LogicalKeySizeInBits: uint32, KeyAttr KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage KeyUsage: CSSM_KEYUSE, StartDate StartDate: CSSM_DATE, EndDate EndDate: CSSM_DATE, WrapAlgorithmId WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode WrapMode: CSSM_ENCRYPT_MODE, Reserved Reserved: uint32) } ``` |

Modified cssm_kr_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_name {     var Type: uint8     var Length: uint8     var Name: UnsafePointer<Int8> } ``` |
| To | ``` struct cssm_kr_name {     var Type: uint8     var Length: uint8     var Name: UnsafeMutablePointer<Int8>     init()     init(Type Type: uint8, Length Length: uint8, Name Name: UnsafeMutablePointer<Int8>) } ``` |

Modified cssm_kr_name.Name

|  | Declaration |
| --- | --- |
| From | ``` var Name: UnsafePointer<Int8> ``` |
| To | ``` var Name: UnsafeMutablePointer<Int8> ``` |

Modified cssm_kr_policy_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_policy_info {     var krbNotAllowed: CSSM_BOOL     var numberOfEntries: uint32     var policyEntry: UnsafePointer<CSSM_KR_POLICY_LIST_ITEM> } ``` |
| To | ``` struct cssm_kr_policy_info {     var krbNotAllowed: CSSM_BOOL     var numberOfEntries: uint32     var policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM>     init()     init(krbNotAllowed krbNotAllowed: CSSM_BOOL, numberOfEntries numberOfEntries: uint32, policyEntry policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM>) } ``` |

Modified cssm_kr_policy_info.policyEntry

|  | Declaration |
| --- | --- |
| From | ``` var policyEntry: UnsafePointer<CSSM_KR_POLICY_LIST_ITEM> ``` |
| To | ``` var policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM> ``` |

Modified cssm_kr_policy_list_item [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_policy_list_item {     var next: COpaquePointer     var AlgorithmId: CSSM_ALGORITHMS     var Mode: CSSM_ENCRYPT_MODE     var MaxKeyLength: uint32     var MaxRounds: uint32     var WorkFactor: uint8     var PolicyFlags: CSSM_KR_POLICY_FLAGS     var AlgClass: CSSM_CONTEXT_TYPE } ``` |
| To | ``` struct cssm_kr_policy_list_item {     var next: COpaquePointer     var AlgorithmId: CSSM_ALGORITHMS     var Mode: CSSM_ENCRYPT_MODE     var MaxKeyLength: uint32     var MaxRounds: uint32     var WorkFactor: uint8     var PolicyFlags: CSSM_KR_POLICY_FLAGS     var AlgClass: CSSM_CONTEXT_TYPE     init() } ``` |

Modified cssm_kr_profile [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_profile {     var UserName: CSSM_KR_NAME     var UserCertificate: CSSM_CERTGROUP_PTR     var KRSCertChain: CSSM_CERTGROUP_PTR     var LE_KRANum: uint8     var LE_KRACertChainList: CSSM_CERTGROUP_PTR     var ENT_KRANum: uint8     var ENT_KRACertChainList: CSSM_CERTGROUP_PTR     var INDIV_KRANum: uint8     var INDIV_KRACertChainList: CSSM_CERTGROUP_PTR     var INDIV_AuthenticationInfo: CSSM_DATA_PTR     var KRSPFlags: uint32     var KRSPExtensions: CSSM_DATA_PTR } ``` |
| To | ``` struct cssm_kr_profile {     var UserName: CSSM_KR_NAME     var UserCertificate: CSSM_CERTGROUP_PTR     var KRSCertChain: CSSM_CERTGROUP_PTR     var LE_KRANum: uint8     var LE_KRACertChainList: CSSM_CERTGROUP_PTR     var ENT_KRANum: uint8     var ENT_KRACertChainList: CSSM_CERTGROUP_PTR     var INDIV_KRANum: uint8     var INDIV_KRACertChainList: CSSM_CERTGROUP_PTR     var INDIV_AuthenticationInfo: CSSM_DATA_PTR     var KRSPFlags: uint32     var KRSPExtensions: CSSM_DATA_PTR     init()     init(UserName UserName: CSSM_KR_NAME, UserCertificate UserCertificate: CSSM_CERTGROUP_PTR, KRSCertChain KRSCertChain: CSSM_CERTGROUP_PTR, LE_KRANum LE_KRANum: uint8, LE_KRACertChainList LE_KRACertChainList: CSSM_CERTGROUP_PTR, ENT_KRANum ENT_KRANum: uint8, ENT_KRACertChainList ENT_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_KRANum INDIV_KRANum: uint8, INDIV_KRACertChainList INDIV_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_AuthenticationInfo INDIV_AuthenticationInfo: CSSM_DATA_PTR, KRSPFlags KRSPFlags: uint32, KRSPExtensions KRSPExtensions: CSSM_DATA_PTR) } ``` |

Modified cssm_kr_wrappedproductinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_wrappedproductinfo {     var StandardVersion: CSSM_VERSION     var StandardDescription: CSSM_STRING     var ProductVersion: CSSM_VERSION     var ProductDescription: CSSM_STRING     var ProductVendor: CSSM_STRING     var ProductFlags: uint32 } ``` |
| To | ``` struct cssm_kr_wrappedproductinfo {     var StandardVersion: CSSM_VERSION     var StandardDescription: CSSM_STRING     var ProductVersion: CSSM_VERSION     var ProductDescription: CSSM_STRING     var ProductVendor: CSSM_STRING     var ProductFlags: uint32     init()     init(StandardVersion StandardVersion: CSSM_VERSION, StandardDescription StandardDescription: CSSM_STRING, ProductVersion ProductVersion: CSSM_VERSION, ProductDescription ProductDescription: CSSM_STRING, ProductVendor ProductVendor: CSSM_STRING, ProductFlags ProductFlags: uint32) } ``` |

Modified cssm_krsubservice [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_krsubservice {     var SubServiceId: uint32     var Description: UnsafePointer<Int8>     var WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO } ``` |
| To | ``` struct cssm_krsubservice {     var SubServiceId: uint32     var Description: UnsafeMutablePointer<Int8>     var WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO     init()     init(SubServiceId SubServiceId: uint32, Description Description: UnsafeMutablePointer<Int8>, WrappedProduct WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO) } ``` |

Modified cssm_krsubservice.Description

|  | Declaration |
| --- | --- |
| From | ``` var Description: UnsafePointer<Int8> ``` |
| To | ``` var Description: UnsafeMutablePointer<Int8> ``` |

Modified cssm_list [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_list {     var ListType: CSSM_LIST_TYPE     var Head: CSSM_LIST_ELEMENT_PTR     var Tail: CSSM_LIST_ELEMENT_PTR } ``` |
| To | ``` struct cssm_list {     var ListType: CSSM_LIST_TYPE     var Head: CSSM_LIST_ELEMENT_PTR     var Tail: CSSM_LIST_ELEMENT_PTR     init()     init(ListType ListType: CSSM_LIST_TYPE, Head Head: CSSM_LIST_ELEMENT_PTR, Tail Tail: CSSM_LIST_ELEMENT_PTR) } ``` |

Modified cssm_list_element [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_list_element {     var NextElement: UnsafePointer<cssm_list_element>     var WordID: CSSM_WORDID_TYPE     var ElementType: CSSM_LIST_ELEMENT_TYPE } ``` |
| To | ``` struct cssm_list_element {     var NextElement: UnsafeMutablePointer<cssm_list_element>     var WordID: CSSM_WORDID_TYPE     var ElementType: CSSM_LIST_ELEMENT_TYPE     init() } ``` |

Modified cssm_list_element.NextElement

|  | Declaration |
| --- | --- |
| From | ``` var NextElement: UnsafePointer<cssm_list_element> ``` |
| To | ``` var NextElement: UnsafeMutablePointer<cssm_list_element> ``` |

Modified cssm_manager_event_notification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_manager_event_notification {     var DestinationModuleManagerType: CSSM_SERVICE_MASK     var SourceModuleManagerType: CSSM_SERVICE_MASK     var Event: CSSM_MANAGER_EVENT_TYPES     var EventId: uint32     var EventData: CSSM_DATA } ``` |
| To | ``` struct cssm_manager_event_notification {     var DestinationModuleManagerType: CSSM_SERVICE_MASK     var SourceModuleManagerType: CSSM_SERVICE_MASK     var Event: CSSM_MANAGER_EVENT_TYPES     var EventId: uint32     var EventData: CSSM_DATA     init()     init(DestinationModuleManagerType DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType SourceModuleManagerType: CSSM_SERVICE_MASK, Event Event: CSSM_MANAGER_EVENT_TYPES, EventId EventId: uint32, EventData EventData: CSSM_DATA) } ``` |

Modified cssm_manager_registration_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_manager_registration_info {     var Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>     var Terminate: CFunctionPointer<(() -> CSSM_RETURN)>     var RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>     var DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>     var EventNotifyManager: CFunctionPointer<((ConstUnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>     var RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)> } ``` |
| To | ``` struct cssm_manager_registration_info {     var Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>     var Terminate: CFunctionPointer<(() -> CSSM_RETURN)>     var RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>     var DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>     var EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>     var RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>     init()     init(Initialize Initialize: CFunctionPointer<((uint32, uint32) -> CSSM_RETURN)>, Terminate Terminate: CFunctionPointer<(() -> CSSM_RETURN)>, RegisterDispatchTable RegisterDispatchTable: CFunctionPointer<((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)>, DeregisterDispatchTable DeregisterDispatchTable: CFunctionPointer<(() -> CSSM_RETURN)>, EventNotifyManager EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>, RefreshFunctionTable RefreshFunctionTable: CFunctionPointer<((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>) } ``` |

Modified cssm_manager_registration_info.EventNotifyManager

|  | Declaration |
| --- | --- |
| From | ``` var EventNotifyManager: CFunctionPointer<((ConstUnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> ``` |
| To | ``` var EventNotifyManager: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> ``` |

Modified cssm_memory_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_memory_funcs {     var malloc_func: CSSM_MALLOC     var free_func: CSSM_FREE     var realloc_func: CSSM_REALLOC     var calloc_func: CSSM_CALLOC     var AllocRef: UnsafePointer<()> } ``` |
| To | ``` struct cssm_memory_funcs {     var malloc_func: CSSM_MALLOC     var free_func: CSSM_FREE     var realloc_func: CSSM_REALLOC     var calloc_func: CSSM_CALLOC     var AllocRef: UnsafeMutablePointer<Void>     init()     init(malloc_func malloc_func: CSSM_MALLOC, free_func free_func: CSSM_FREE, realloc_func realloc_func: CSSM_REALLOC, calloc_func calloc_func: CSSM_CALLOC, AllocRef AllocRef: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_memory_funcs.AllocRef

|  | Declaration |
| --- | --- |
| From | ``` var AllocRef: UnsafePointer<()> ``` |
| To | ``` var AllocRef: UnsafeMutablePointer<Void> ``` |

Modified cssm_module_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_module_funcs {     var ServiceType: CSSM_SERVICE_TYPE     var NumberOfServiceFuncs: uint32     var ServiceFuncs: ConstUnsafePointer<CSSM_PROC_ADDR> } ``` |
| To | ``` struct cssm_module_funcs {     var ServiceType: CSSM_SERVICE_TYPE     var NumberOfServiceFuncs: uint32     var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR>     init()     init(ServiceType ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs NumberOfServiceFuncs: uint32, ServiceFuncs ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR>) } ``` |

Modified cssm_module_funcs.ServiceFuncs

|  | Declaration |
| --- | --- |
| From | ``` var ServiceFuncs: ConstUnsafePointer<CSSM_PROC_ADDR> ``` |
| To | ``` var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR> ``` |

Modified cssm_name_list [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_name_list {     var NumStrings: uint32     var String: UnsafePointer<UnsafePointer<Int8>> } ``` |
| To | ``` struct cssm_name_list {     var NumStrings: uint32     var String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     init()     init(NumStrings NumStrings: uint32, String String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) } ``` |

Modified cssm_name_list.String

|  | Declaration |
| --- | --- |
| From | ``` var String: UnsafePointer<UnsafePointer<Int8>> ``` |
| To | ``` var String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |

Modified cssm_net_address [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_net_address {     var AddressType: CSSM_NET_ADDRESS_TYPE     var Address: CSSM_DATA } ``` |
| To | ``` struct cssm_net_address {     var AddressType: CSSM_NET_ADDRESS_TYPE     var Address: CSSM_DATA     init()     init(AddressType AddressType: CSSM_NET_ADDRESS_TYPE, Address Address: CSSM_DATA) } ``` |

Modified cssm_parsed_cert [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_parsed_cert {     var CertType: CSSM_CERT_TYPE     var ParsedCertFormat: CSSM_CERT_PARSE_FORMAT     var ParsedCert: UnsafePointer<()> } ``` |
| To | ``` struct cssm_parsed_cert {     var CertType: CSSM_CERT_TYPE     var ParsedCertFormat: CSSM_CERT_PARSE_FORMAT     var ParsedCert: UnsafeMutablePointer<Void>     init()     init(CertType CertType: CSSM_CERT_TYPE, ParsedCertFormat ParsedCertFormat: CSSM_CERT_PARSE_FORMAT, ParsedCert ParsedCert: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_parsed_cert.ParsedCert

|  | Declaration |
| --- | --- |
| From | ``` var ParsedCert: UnsafePointer<()> ``` |
| To | ``` var ParsedCert: UnsafeMutablePointer<Void> ``` |

Modified cssm_parsed_crl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_parsed_crl {     var CrlType: CSSM_CRL_TYPE     var ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT     var ParsedCrl: UnsafePointer<()> } ``` |
| To | ``` struct cssm_parsed_crl {     var CrlType: CSSM_CRL_TYPE     var ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT     var ParsedCrl: UnsafeMutablePointer<Void>     init()     init(CrlType CrlType: CSSM_CRL_TYPE, ParsedCrlFormat ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT, ParsedCrl ParsedCrl: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_parsed_crl.ParsedCrl

|  | Declaration |
| --- | --- |
| From | ``` var ParsedCrl: UnsafePointer<()> ``` |
| To | ``` var ParsedCrl: UnsafeMutablePointer<Void> ``` |

Modified cssm_pkcs1_oaep_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_pkcs1_oaep_params {     var HashAlgorithm: uint32     var HashParams: CSSM_DATA     var MGF: CSSM_PKCS_OAEP_MGF     var MGFParams: CSSM_DATA     var PSource: CSSM_PKCS_OAEP_PSOURCE     var PSourceParams: CSSM_DATA } ``` |
| To | ``` struct cssm_pkcs1_oaep_params {     var HashAlgorithm: uint32     var HashParams: CSSM_DATA     var MGF: CSSM_PKCS_OAEP_MGF     var MGFParams: CSSM_DATA     var PSource: CSSM_PKCS_OAEP_PSOURCE     var PSourceParams: CSSM_DATA     init()     init(HashAlgorithm HashAlgorithm: uint32, HashParams HashParams: CSSM_DATA, MGF MGF: CSSM_PKCS_OAEP_MGF, MGFParams MGFParams: CSSM_DATA, PSource PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams PSourceParams: CSSM_DATA) } ``` |

Modified cssm_pkcs5_pbkdf1_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_pkcs5_pbkdf1_params {     var Passphrase: CSSM_DATA     var InitVector: CSSM_DATA } ``` |
| To | ``` struct cssm_pkcs5_pbkdf1_params {     var Passphrase: CSSM_DATA     var InitVector: CSSM_DATA     init()     init(Passphrase Passphrase: CSSM_DATA, InitVector InitVector: CSSM_DATA) } ``` |

Modified cssm_pkcs5_pbkdf2_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_pkcs5_pbkdf2_params {     var Passphrase: CSSM_DATA     var PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF } ``` |
| To | ``` struct cssm_pkcs5_pbkdf2_params {     var Passphrase: CSSM_DATA     var PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF     init()     init(Passphrase Passphrase: CSSM_DATA, PseudoRandomFunction PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF) } ``` |

Modified cssm_query [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_query {     var RecordType: CSSM_DB_RECORDTYPE     var Conjunctive: CSSM_DB_CONJUNCTIVE     var NumSelectionPredicates: uint32     var SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR     var QueryLimits: CSSM_QUERY_LIMITS     var QueryFlags: CSSM_QUERY_FLAGS } ``` |
| To | ``` struct cssm_query {     var RecordType: CSSM_DB_RECORDTYPE     var Conjunctive: CSSM_DB_CONJUNCTIVE     var NumSelectionPredicates: uint32     var SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR     var QueryLimits: CSSM_QUERY_LIMITS     var QueryFlags: CSSM_QUERY_FLAGS     init()     init(RecordType RecordType: CSSM_DB_RECORDTYPE, Conjunctive Conjunctive: CSSM_DB_CONJUNCTIVE, NumSelectionPredicates NumSelectionPredicates: uint32, SelectionPredicate SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR, QueryLimits QueryLimits: CSSM_QUERY_LIMITS, QueryFlags QueryFlags: CSSM_QUERY_FLAGS) } ``` |

Modified cssm_query_limits [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_query_limits {     var TimeLimit: uint32     var SizeLimit: uint32 } ``` |
| To | ``` struct cssm_query_limits {     var TimeLimit: uint32     var SizeLimit: uint32     init()     init(TimeLimit TimeLimit: uint32, SizeLimit SizeLimit: uint32) } ``` |

Modified cssm_query_size_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_query_size_data {     var SizeInputBlock: uint32     var SizeOutputBlock: uint32 } ``` |
| To | ``` struct cssm_query_size_data {     var SizeInputBlock: uint32     var SizeOutputBlock: uint32     init()     init(SizeInputBlock SizeInputBlock: uint32, SizeOutputBlock SizeOutputBlock: uint32) } ``` |

Modified cssm_range [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_range {     var Min: uint32     var Max: uint32 } ``` |
| To | ``` struct cssm_range {     var Min: uint32     var Max: uint32     init()     init(Min Min: uint32, Max Max: uint32) } ``` |

Modified cssm_resource_control_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_resource_control_context {     var AccessCred: CSSM_ACCESS_CREDENTIALS_PTR     var InitialAclEntry: CSSM_ACL_ENTRY_INPUT } ``` |
| To | ``` struct cssm_resource_control_context {     var AccessCred: CSSM_ACCESS_CREDENTIALS_PTR     var InitialAclEntry: CSSM_ACL_ENTRY_INPUT     init()     init(AccessCred AccessCred: CSSM_ACCESS_CREDENTIALS_PTR, InitialAclEntry InitialAclEntry: CSSM_ACL_ENTRY_INPUT) } ``` |

Modified cssm_sample [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_sample {     var TypedSample: CSSM_LIST     var Verifier: ConstUnsafePointer<CSSM_SUBSERVICE_UID> } ``` |
| To | ``` struct cssm_sample {     var TypedSample: CSSM_LIST     var Verifier: UnsafePointer<CSSM_SUBSERVICE_UID>     init()     init(TypedSample TypedSample: CSSM_LIST, Verifier Verifier: UnsafePointer<CSSM_SUBSERVICE_UID>) } ``` |

Modified cssm_sample.Verifier

|  | Declaration |
| --- | --- |
| From | ``` var Verifier: ConstUnsafePointer<CSSM_SUBSERVICE_UID> ``` |
| To | ``` var Verifier: UnsafePointer<CSSM_SUBSERVICE_UID> ``` |

Modified cssm_samplegroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_samplegroup {     var NumberOfSamples: uint32     var Samples: ConstUnsafePointer<CSSM_SAMPLE> } ``` |
| To | ``` struct cssm_samplegroup {     var NumberOfSamples: uint32     var Samples: UnsafePointer<CSSM_SAMPLE>     init()     init(NumberOfSamples NumberOfSamples: uint32, Samples Samples: UnsafePointer<CSSM_SAMPLE>) } ``` |

Modified cssm_samplegroup.Samples

|  | Declaration |
| --- | --- |
| From | ``` var Samples: ConstUnsafePointer<CSSM_SAMPLE> ``` |
| To | ``` var Samples: UnsafePointer<CSSM_SAMPLE> ``` |

Modified cssm_selection_predicate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_selection_predicate {     var DbOperator: CSSM_DB_OPERATOR     var Attribute: CSSM_DB_ATTRIBUTE_DATA } ``` |
| To | ``` struct cssm_selection_predicate {     var DbOperator: CSSM_DB_OPERATOR     var Attribute: CSSM_DB_ATTRIBUTE_DATA     init()     init(DbOperator DbOperator: CSSM_DB_OPERATOR, Attribute Attribute: CSSM_DB_ATTRIBUTE_DATA) } ``` |

Modified cssm_spi_ac_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_ac_funcs {     var AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, ConstUnsafePointer<CSSM_TUPLEGROUP>, ConstUnsafePointer<CSSM_TUPLEGROUP>, uint32, ConstUnsafePointer<CSSM_LIST>, ConstUnsafePointer<CSSM_LIST>, ConstUnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DL_DB_LIST>, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> } ``` |
| To | ``` struct cssm_spi_ac_funcs {     var AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>     init()     init(AuthCompute AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)>, PassThrough PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>) } ``` |

Modified cssm_spi_ac_funcs.AuthCompute

|  | Declaration |
| --- | --- |
| From | ``` var AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, ConstUnsafePointer<CSSM_TUPLEGROUP>, ConstUnsafePointer<CSSM_TUPLEGROUP>, uint32, ConstUnsafePointer<CSSM_LIST>, ConstUnsafePointer<CSSM_LIST>, ConstUnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var AuthCompute: CFunctionPointer<((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_ac_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DL_DB_LIST>, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: CFunctionPointer<((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertCache

|  | Declaration |
| --- | --- |
| From | ``` var CertCache: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertCache: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, ConstUnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertDescribeFormat

|  | Declaration |
| --- | --- |
| From | ``` var CertDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<uint32>, UnsafePointer<CSSM_OID_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetAllFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<uint32>, UnsafePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetAllTemplateFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllTemplateFields: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<uint32>, UnsafePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetAllTemplateFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetFirstCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, ConstUnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetFirstFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetKeyInfo

|  | Declaration |
| --- | --- |
| From | ``` var CertGetKeyInfo: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetKeyInfo: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetNextCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGetNextFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGroupFromVerifiedBundle

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupFromVerifiedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CERT_BUNDLE>, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupFromVerifiedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertGroupToSignedBundle

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupToSignedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupToSignedBundle: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertSign

|  | Declaration |
| --- | --- |
| From | ``` var CertSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertVerify

|  | Declaration |
| --- | --- |
| From | ``` var CertVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var CertVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CertVerifyWithKey

|  | Declaration |
| --- | --- |
| From | ``` var CertVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var CertVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlAddCert

|  | Declaration |
| --- | --- |
| From | ``` var CrlAddCert: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32, ConstUnsafePointer<CSSM_FIELD>, ConstUnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlAddCert: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlCache

|  | Declaration |
| --- | --- |
| From | ``` var CrlCache: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlCache: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CrlCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, ConstUnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlCreateTemplate: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlDescribeFormat

|  | Declaration |
| --- | --- |
| From | ``` var CrlDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<uint32>, UnsafePointer<CSSM_OID_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlDescribeFormat: CFunctionPointer<((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlGetAllCachedRecordFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetAllCachedRecordFields: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<uint32>, UnsafePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetAllCachedRecordFields: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlGetAllFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<uint32>, UnsafePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetAllFields: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlGetFirstCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetFirstCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlGetFirstFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetFirstFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlGetNextCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetNextCachedFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlGetNextFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlGetNextFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlRemoveCert

|  | Declaration |
| --- | --- |
| From | ``` var CrlRemoveCert: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlRemoveCert: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlSetFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlSetFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, ConstUnsafePointer<CSSM_FIELD>, ConstUnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlSetFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlSign

|  | Declaration |
| --- | --- |
| From | ``` var CrlSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlSign: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlVerify

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var CrlVerify: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.CrlVerifyWithKey

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var CrlVerifyWithKey: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.FreeFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var FreeFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FreeFieldValue: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.FreeFields

|  | Declaration |
| --- | --- |
| From | ``` var FreeFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var FreeFields: CFunctionPointer<((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.IsCertInCachedCrl

|  | Declaration |
| --- | --- |
| From | ``` var IsCertInCachedCrl: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var IsCertInCachedCrl: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.IsCertInCrl

|  | Declaration |
| --- | --- |
| From | ``` var IsCertInCrl: CFunctionPointer<((CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |
| To | ``` var IsCertInCrl: CFunctionPointer<((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_cl_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: CFunctionPointer<((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.ChangeKeyAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeKeyAcl: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_EDIT>, ConstUnsafePointer<CSSM_KEY>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeKeyAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.ChangeKeyOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeKeyOwner: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_KEY>, ConstUnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeKeyOwner: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.ChangeLoginAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeLoginAcl: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeLoginAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.ChangeLoginOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeLoginOwner: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeLoginOwner: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DecryptData

|  | Declaration |
| --- | --- |
| From | ``` var DecryptData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DecryptDataInit

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DecryptDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafePointer<CSSM_SIZE>) -> CSSM_RETURN)> ``` |
| To | ``` var DecryptDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DeriveKey

|  | Declaration |
| --- | --- |
| From | ``` var DeriveKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DeriveKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DigestData

|  | Declaration |
| --- | --- |
| From | ``` var DigestData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DigestData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DigestDataInit

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var DigestDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.DigestDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var DigestDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.EncryptData

|  | Declaration |
| --- | --- |
| From | ``` var EncryptData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.EncryptDataInit

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.EncryptDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafePointer<CSSM_SIZE>) -> CSSM_RETURN)> ``` |
| To | ``` var EncryptDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.EventNotify

|  | Declaration |
| --- | --- |
| From | ``` var EventNotify: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var EventNotify: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.FreeKey

|  | Declaration |
| --- | --- |
| From | ``` var FreeKey: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)> ``` |
| To | ``` var FreeKey: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateAlgorithmParams

|  | Declaration |
| --- | --- |
| From | ``` var GenerateAlgorithmParams: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateAlgorithmParams: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateKey

|  | Declaration |
| --- | --- |
| From | ``` var GenerateKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, uint32, uint32, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateKeyPair

|  | Declaration |
| --- | --- |
| From | ``` var GenerateKeyPair: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, uint32, uint32, ConstUnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateKeyPair: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateMac

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMac: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMac: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateMacInit

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMacInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateMacUpdate

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateMacUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GenerateRandom

|  | Declaration |
| --- | --- |
| From | ``` var GenerateRandom: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateRandom: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GetKeyAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetKeyAcl: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_KEY>, ConstUnsafePointer<CSSM_STRING>, UnsafePointer<uint32>, UnsafePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetKeyAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GetKeyOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetKeyOwner: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GetKeyOwner: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GetLoginAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetLoginAcl: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_STRING>, UnsafePointer<uint32>, UnsafePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetLoginAcl: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GetOperationalStatistics

|  | Declaration |
| --- | --- |
| From | ``` var GetOperationalStatistics: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)> ``` |
| To | ``` var GetOperationalStatistics: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.GetTimeValue

|  | Declaration |
| --- | --- |
| From | ``` var GetTimeValue: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var GetTimeValue: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.Login

|  | Declaration |
| --- | --- |
| From | ``` var Login: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<()>) -> CSSM_RETURN)> ``` |
| To | ``` var Login: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.ObtainPrivateKeyFromPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var ObtainPrivateKeyFromPublicKey: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var ObtainPrivateKeyFromPublicKey: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.QueryKeySizeInBits

|  | Declaration |
| --- | --- |
| From | ``` var QueryKeySizeInBits: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var QueryKeySizeInBits: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.QuerySize

|  | Declaration |
| --- | --- |
| From | ``` var QuerySize: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var QuerySize: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.SignData

|  | Declaration |
| --- | --- |
| From | ``` var SignData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var SignData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.SignDataInit

|  | Declaration |
| --- | --- |
| From | ``` var SignDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var SignDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.SignDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var SignDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var SignDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.UnwrapKey

|  | Declaration |
| --- | --- |
| From | ``` var UnwrapKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_KEY>, ConstUnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var UnwrapKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyData

|  | Declaration |
| --- | --- |
| From | ``` var VerifyData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyData: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDataFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyDataInit

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDataInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDataUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyDevice

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDevice: CFunctionPointer<((CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyDevice: CFunctionPointer<((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyMac

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMac: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, uint32, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMac: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyMacFinal

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMacFinal: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyMacInit

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMacInit: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.VerifyMacUpdate

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var VerifyMacUpdate: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_spi_csp_funcs.WrapKey

|  | Declaration |
| --- | --- |
| From | ``` var WrapKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_KEY>, ConstUnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |
| To | ``` var WrapKey: CFunctionPointer<((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_dl_funcs {     var DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<()>, UnsafePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbClose: CFunctionPointer<((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)>     var DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, ConstUnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, ConstUnsafePointer<()>, UnsafePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>     var CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<Int8>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>     var DestroyRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>     var Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)>     var GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_STRING>, UnsafePointer<uint32>, UnsafePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)>     var ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)>     var GetDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)>     var ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)>     var GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>     var GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<UnsafePointer<Int8>>) -> CSSM_RETURN)>     var FreeNameList: CFunctionPointer<((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>     var DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>     var DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>     var DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataAbortQuery: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var FreeUniqueRecord: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> } ``` |
| To | ```  ``` |

Modified cssm_spi_dl_funcs.Authenticate

|  | Declaration |
| --- | --- |
| From | ``` var Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)> ``` |
| To | ``` var Authenticate: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.ChangeDbAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.ChangeDbOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |
| To | ``` var ChangeDbOwner: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.CreateRelation

|  | Declaration |
| --- | --- |
| From | ``` var CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<Int8>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)> ``` |
| To | ``` var CreateRelation: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DataDelete

|  | Declaration |
| --- | --- |
| From | ``` var DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)> ``` |
| To | ``` var DataDelete: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DataGetFirst

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFirst: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DataGetFromUniqueRecordId

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFromUniqueRecordId: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DataGetNext

|  | Declaration |
| --- | --- |
| From | ``` var DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetNext: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DataInsert

|  | Declaration |
| --- | --- |
| From | ``` var DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataInsert: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DataModify

|  | Declaration |
| --- | --- |
| From | ``` var DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)> ``` |
| To | ``` var DataModify: CFunctionPointer<((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DbCreate

|  | Declaration |
| --- | --- |
| From | ``` var DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, ConstUnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, ConstUnsafePointer<()>, UnsafePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |
| To | ``` var DbCreate: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DbDelete

|  | Declaration |
| --- | --- |
| From | ``` var DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)> ``` |
| To | ``` var DbDelete: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.DbOpen

|  | Declaration |
| --- | --- |
| From | ``` var DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<()>, UnsafePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |
| To | ``` var DbOpen: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.GetDbAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, ConstUnsafePointer<CSSM_STRING>, UnsafePointer<uint32>, UnsafePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbAcl: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.GetDbNameFromHandle

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafePointer<UnsafePointer<Int8>>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNameFromHandle: CFunctionPointer<((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.GetDbNames

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNames: CFunctionPointer<((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_dl_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: CFunctionPointer<((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_kr_funcs {     var RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>     var RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>     var GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>     var ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>     var RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>     var RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafePointer<sint32>, CSSM_HANDLE_PTR, UnsafePointer<uint32>) -> CSSM_RETURN)>     var GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> } ``` |
| To | ``` struct cssm_spi_kr_funcs {     var RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>     var RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>     var GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>     var ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>     var RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>     var RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)>     var GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>     init()     init(RegistrationRequest RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RegistrationRetrieve RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)>, GenerateRecoveryFields GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)>, ProcessRecoveryFields ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)>, RecoveryRequest RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)>, RecoveryRetrieve RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)>, GetRecoveredObject GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, RecoveryRequestAbort RecoveryRequestAbort: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, PassThrough PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)>) } ``` |

Modified cssm_spi_kr_funcs.GenerateRecoveryFields

|  | Declaration |
| --- | --- |
| From | ``` var GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GenerateRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.GetRecoveredObject

|  | Declaration |
| --- | --- |
| From | ``` var GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var GetRecoveredObject: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.ProcessRecoveryFields

|  | Declaration |
| --- | --- |
| From | ``` var ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, ConstUnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |
| To | ``` var ProcessRecoveryFields: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.RecoveryRequest

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RecoveryRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.RecoveryRetrieve

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafePointer<sint32>, CSSM_HANDLE_PTR, UnsafePointer<uint32>) -> CSSM_RETURN)> ``` |
| To | ``` var RecoveryRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.RegistrationRequest

|  | Declaration |
| --- | --- |
| From | ``` var RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_CONTEXT>, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RegistrationRequest: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_kr_funcs.RegistrationRetrieve

|  | Declaration |
| --- | --- |
| From | ``` var RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var RegistrationRetrieve: CFunctionPointer<((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.ApplyCrlToDb

|  | Declaration |
| --- | --- |
| From | ``` var ApplyCrlToDb: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ENCODED_CRL>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var ApplyCrlToDb: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, ConstUnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertGetAllTemplateFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllTemplateFields: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<uint32>, UnsafePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGetAllTemplateFields: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertGroupConstruct

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupConstruct: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_DL_DB_LIST>, ConstUnsafePointer<()>, ConstUnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupConstruct: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertGroupPrune

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupPrune: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_DL_DB_LIST>, ConstUnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupPrune: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertGroupToTupleGroup

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupToTupleGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupToTupleGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertGroupVerify

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertGroupVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertReclaimKey

|  | Declaration |
| --- | --- |
| From | ``` var CertReclaimKey: CFunctionPointer<((CSSM_TP_HANDLE, ConstUnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)> ``` |
| To | ``` var CertReclaimKey: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertRemoveFromCrlTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertRemoveFromCrlTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertRemoveFromCrlTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertRevoke

|  | Declaration |
| --- | --- |
| From | ``` var CertRevoke: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertRevoke: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CertSign

|  | Declaration |
| --- | --- |
| From | ``` var CertSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CertSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.ConfirmCredResult

|  | Declaration |
| --- | --- |
| From | ``` var ConfirmCredResult: CFunctionPointer<((CSSM_TP_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, ConstUnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, ConstUnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)> ``` |
| To | ``` var ConfirmCredResult: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CrlCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CrlCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, ConstUnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlCreateTemplate: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CrlSign

|  | Declaration |
| --- | --- |
| From | ``` var CrlSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_ENCODED_CRL>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlSign: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.CrlVerify

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, ConstUnsafePointer<CSSM_ENCODED_CRL>, ConstUnsafePointer<CSSM_CERTGROUP>, ConstUnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var CrlVerify: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.FormRequest

|  | Declaration |
| --- | --- |
| From | ``` var FormRequest: CFunctionPointer<((CSSM_TP_HANDLE, ConstUnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FormRequest: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.FormSubmit

|  | Declaration |
| --- | --- |
| From | ``` var FormSubmit: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_TP_AUTHORITY_ID>, ConstUnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var FormSubmit: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, ConstUnsafePointer<CSSM_DL_DB_LIST>, uint32, ConstUnsafePointer<()>, UnsafePointer<UnsafePointer<()>>) -> CSSM_RETURN)> ``` |
| To | ``` var PassThrough: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.ReceiveConfirmation

|  | Declaration |
| --- | --- |
| From | ``` var ReceiveConfirmation: CFunctionPointer<((CSSM_TP_HANDLE, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafePointer<sint32>) -> CSSM_RETURN)> ``` |
| To | ``` var ReceiveConfirmation: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.RetrieveCredResult

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveCredResult: CFunctionPointer<((CSSM_TP_HANDLE, ConstUnsafePointer<CSSM_DATA>, ConstUnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<sint32>, UnsafePointer<CSSM_BOOL>, UnsafePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var RetrieveCredResult: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.SubmitCredRequest

|  | Declaration |
| --- | --- |
| From | ``` var SubmitCredRequest: CFunctionPointer<((CSSM_TP_HANDLE, ConstUnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, ConstUnsafePointer<CSSM_TP_REQUEST_SET>, ConstUnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var SubmitCredRequest: CFunctionPointer<((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified cssm_spi_tp_funcs.TupleGroupToCertGroup

|  | Declaration |
| --- | --- |
| From | ``` var TupleGroupToCertGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, ConstUnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var TupleGroupToCertGroup: CFunctionPointer<((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)> ``` |

Modified cssm_state_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_state_funcs {     var cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafePointer<UnsafePointer<()>>, CSSM_GUID_PTR, UnsafePointer<CSSM_BOOL>) -> CSSM_RETURN)>     var cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>     var cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>     var cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafePointer<CSSM_BOOL>) -> CSSM_RETURN)>     var cssm_DeregisterManagerServices: CFunctionPointer<((ConstUnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>     var cssm_DeliverModuleManagerEvent: CFunctionPointer<((ConstUnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> } ``` |
| To | ``` struct cssm_state_funcs {     var cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>     var cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>     var cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>     var cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>     var cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>     var cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>     init()     init(cssm_GetAttachFunctions cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_ReleaseAttachFunctions cssm_ReleaseAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE) -> CSSM_RETURN)>, cssm_GetAppMemoryFunctions cssm_GetAppMemoryFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)>, cssm_IsFuncCallValid cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)>, cssm_DeregisterManagerServices cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)>, cssm_DeliverModuleManagerEvent cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)>) } ``` |

Modified cssm_state_funcs.cssm_DeliverModuleManagerEvent

|  | Declaration |
| --- | --- |
| From | ``` var cssm_DeliverModuleManagerEvent: CFunctionPointer<((ConstUnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_DeliverModuleManagerEvent: CFunctionPointer<((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)> ``` |

Modified cssm_state_funcs.cssm_DeregisterManagerServices

|  | Declaration |
| --- | --- |
| From | ``` var cssm_DeregisterManagerServices: CFunctionPointer<((ConstUnsafePointer<CSSM_GUID>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_DeregisterManagerServices: CFunctionPointer<((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)> ``` |

Modified cssm_state_funcs.cssm_GetAttachFunctions

|  | Declaration |
| --- | --- |
| From | ``` var cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafePointer<UnsafePointer<()>>, CSSM_GUID_PTR, UnsafePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_GetAttachFunctions: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |

Modified cssm_state_funcs.cssm_IsFuncCallValid

|  | Declaration |
| --- | --- |
| From | ``` var cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |
| To | ``` var cssm_IsFuncCallValid: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR, CSSM_PROC_ADDR, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)> ``` |

Modified cssm_subservice_uid [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_subservice_uid {     var Guid: CSSM_GUID     var Version: CSSM_VERSION     var SubserviceId: uint32     var SubserviceType: CSSM_SERVICE_TYPE } ``` |
| To | ``` struct cssm_subservice_uid {     var Guid: CSSM_GUID     var Version: CSSM_VERSION     var SubserviceId: uint32     var SubserviceType: CSSM_SERVICE_TYPE     init()     init(Guid Guid: CSSM_GUID, Version Version: CSSM_VERSION, SubserviceId SubserviceId: uint32, SubserviceType SubserviceType: CSSM_SERVICE_TYPE) } ``` |

Modified cssm_tp_authority_id [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_authority_id {     var AuthorityCert: UnsafePointer<CSSM_DATA>     var AuthorityLocation: CSSM_NET_ADDRESS_PTR } ``` |
| To | ``` struct cssm_tp_authority_id {     var AuthorityCert: UnsafeMutablePointer<CSSM_DATA>     var AuthorityLocation: CSSM_NET_ADDRESS_PTR     init()     init(AuthorityCert AuthorityCert: UnsafeMutablePointer<CSSM_DATA>, AuthorityLocation AuthorityLocation: CSSM_NET_ADDRESS_PTR) } ``` |

Modified cssm_tp_authority_id.AuthorityCert

|  | Declaration |
| --- | --- |
| From | ``` var AuthorityCert: UnsafePointer<CSSM_DATA> ``` |
| To | ``` var AuthorityCert: UnsafeMutablePointer<CSSM_DATA> ``` |

Modified cssm_tp_callerauth_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_callerauth_context {     var Policy: CSSM_TP_POLICYINFO     var VerifyTime: CSSM_TIMESTRING     var VerificationAbortOn: CSSM_TP_STOP_ON     var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK     var NumberOfAnchorCerts: uint32     var AnchorCerts: CSSM_DATA_PTR     var DBList: CSSM_DL_DB_LIST_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR } ``` |
| To | ``` struct cssm_tp_callerauth_context {     var Policy: CSSM_TP_POLICYINFO     var VerifyTime: CSSM_TIMESTRING     var VerificationAbortOn: CSSM_TP_STOP_ON     var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK     var NumberOfAnchorCerts: uint32     var AnchorCerts: CSSM_DATA_PTR     var DBList: CSSM_DL_DB_LIST_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(Policy Policy: CSSM_TP_POLICYINFO, VerifyTime VerifyTime: CSSM_TIMESTRING, VerificationAbortOn VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK, NumberOfAnchorCerts NumberOfAnchorCerts: uint32, AnchorCerts AnchorCerts: CSSM_DATA_PTR, DBList DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_certchange_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certchange_input {     var Action: CSSM_TP_CERTCHANGE_ACTION     var Reason: CSSM_TP_CERTCHANGE_REASON     var CLHandle: CSSM_CL_HANDLE     var Cert: CSSM_DATA_PTR     var ChangeInfo: CSSM_FIELD_PTR     var StartTime: CSSM_TIMESTRING     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR } ``` |
| To | ``` struct cssm_tp_certchange_input {     var Action: CSSM_TP_CERTCHANGE_ACTION     var Reason: CSSM_TP_CERTCHANGE_REASON     var CLHandle: CSSM_CL_HANDLE     var Cert: CSSM_DATA_PTR     var ChangeInfo: CSSM_FIELD_PTR     var StartTime: CSSM_TIMESTRING     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(Action Action: CSSM_TP_CERTCHANGE_ACTION, Reason Reason: CSSM_TP_CERTCHANGE_REASON, CLHandle CLHandle: CSSM_CL_HANDLE, Cert Cert: CSSM_DATA_PTR, ChangeInfo ChangeInfo: CSSM_FIELD_PTR, StartTime StartTime: CSSM_TIMESTRING, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_certchange_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certchange_output {     var ActionStatus: CSSM_TP_CERTCHANGE_STATUS     var RevokeInfo: CSSM_FIELD } ``` |
| To | ``` struct cssm_tp_certchange_output {     var ActionStatus: CSSM_TP_CERTCHANGE_STATUS     var RevokeInfo: CSSM_FIELD     init()     init(ActionStatus ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo RevokeInfo: CSSM_FIELD) } ``` |

Modified cssm_tp_certissue_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certissue_input {     var CSPSubserviceUid: CSSM_SUBSERVICE_UID     var CLHandle: CSSM_CL_HANDLE     var NumberOfTemplateFields: uint32     var SubjectCertFields: CSSM_FIELD_PTR     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR } ``` |
| To | ``` struct cssm_tp_certissue_input {     var CSPSubserviceUid: CSSM_SUBSERVICE_UID     var CLHandle: CSSM_CL_HANDLE     var NumberOfTemplateFields: uint32     var SubjectCertFields: CSSM_FIELD_PTR     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CSPSubserviceUid CSPSubserviceUid: CSSM_SUBSERVICE_UID, CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfTemplateFields NumberOfTemplateFields: uint32, SubjectCertFields SubjectCertFields: CSSM_FIELD_PTR, MoreServiceRequests MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls NumberOfServiceControls: uint32, ServiceControls ServiceControls: CSSM_FIELD_PTR, UserCredentials UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_certissue_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certissue_output {     var IssueStatus: CSSM_TP_CERTISSUE_STATUS     var CertGroup: CSSM_CERTGROUP_PTR     var PerformedServiceRequests: CSSM_TP_SERVICES } ``` |
| To | ``` struct cssm_tp_certissue_output {     var IssueStatus: CSSM_TP_CERTISSUE_STATUS     var CertGroup: CSSM_CERTGROUP_PTR     var PerformedServiceRequests: CSSM_TP_SERVICES     init()     init(IssueStatus IssueStatus: CSSM_TP_CERTISSUE_STATUS, CertGroup CertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests PerformedServiceRequests: CSSM_TP_SERVICES) } ``` |

Modified cssm_tp_certnotarize_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certnotarize_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfFields: uint32     var MoreFields: CSSM_FIELD_PTR     var SignScope: CSSM_FIELD_PTR     var ScopeSize: uint32     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR } ``` |
| To | ``` struct cssm_tp_certnotarize_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfFields: uint32     var MoreFields: CSSM_FIELD_PTR     var SignScope: CSSM_FIELD_PTR     var ScopeSize: uint32     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfFields NumberOfFields: uint32, MoreFields MoreFields: CSSM_FIELD_PTR, SignScope SignScope: CSSM_FIELD_PTR, ScopeSize ScopeSize: uint32, MoreServiceRequests MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls NumberOfServiceControls: uint32, ServiceControls ServiceControls: CSSM_FIELD_PTR, UserCredentials UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_certnotarize_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certnotarize_output {     var NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS     var NotarizedCertGroup: CSSM_CERTGROUP_PTR     var PerformedServiceRequests: CSSM_TP_SERVICES } ``` |
| To | ``` struct cssm_tp_certnotarize_output {     var NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS     var NotarizedCertGroup: CSSM_CERTGROUP_PTR     var PerformedServiceRequests: CSSM_TP_SERVICES     init()     init(NotarizeStatus NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS, NotarizedCertGroup NotarizedCertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests PerformedServiceRequests: CSSM_TP_SERVICES) } ``` |

Modified cssm_tp_certreclaim_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certreclaim_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfSelectionFields: uint32     var SelectionFields: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR } ``` |
| To | ``` struct cssm_tp_certreclaim_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfSelectionFields: uint32     var SelectionFields: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfSelectionFields NumberOfSelectionFields: uint32, SelectionFields SelectionFields: CSSM_FIELD_PTR, UserCredentials UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_certreclaim_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certreclaim_output {     var ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS     var ReclaimedCertGroup: CSSM_CERTGROUP_PTR     var KeyCacheHandle: CSSM_LONG_HANDLE } ``` |
| To | ``` struct cssm_tp_certreclaim_output {     var ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS     var ReclaimedCertGroup: CSSM_CERTGROUP_PTR     var KeyCacheHandle: CSSM_LONG_HANDLE     init()     init(ReclaimStatus ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS, ReclaimedCertGroup ReclaimedCertGroup: CSSM_CERTGROUP_PTR, KeyCacheHandle KeyCacheHandle: CSSM_LONG_HANDLE) } ``` |

Modified cssm_tp_certverify_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certverify_input {     var CLHandle: CSSM_CL_HANDLE     var Cert: CSSM_DATA_PTR     var VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR } ``` |
| To | ``` struct cssm_tp_certverify_input {     var CLHandle: CSSM_CL_HANDLE     var Cert: CSSM_DATA_PTR     var VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, Cert Cert: CSSM_DATA_PTR, VerifyContext VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR) } ``` |

Modified cssm_tp_certverify_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certverify_output {     var VerifyStatus: CSSM_TP_CERTVERIFY_STATUS     var NumberOfEvidence: uint32     var Evidence: CSSM_EVIDENCE_PTR } ``` |
| To | ``` struct cssm_tp_certverify_output {     var VerifyStatus: CSSM_TP_CERTVERIFY_STATUS     var NumberOfEvidence: uint32     var Evidence: CSSM_EVIDENCE_PTR     init()     init(VerifyStatus VerifyStatus: CSSM_TP_CERTVERIFY_STATUS, NumberOfEvidence NumberOfEvidence: uint32, Evidence Evidence: CSSM_EVIDENCE_PTR) } ``` |

Modified cssm_tp_confirm_response [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_confirm_response {     var NumberOfResponses: uint32     var Responses: CSSM_TP_CONFIRM_STATUS_PTR } ``` |
| To | ``` struct cssm_tp_confirm_response {     var NumberOfResponses: uint32     var Responses: CSSM_TP_CONFIRM_STATUS_PTR     init()     init(NumberOfResponses NumberOfResponses: uint32, Responses Responses: CSSM_TP_CONFIRM_STATUS_PTR) } ``` |

Modified cssm_tp_crlissue_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_crlissue_input {     var CLHandle: CSSM_CL_HANDLE     var CrlIdentifier: uint32     var CrlThisTime: CSSM_TIMESTRING     var PolicyIdentifier: CSSM_FIELD_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR } ``` |
| To | ``` struct cssm_tp_crlissue_input {     var CLHandle: CSSM_CL_HANDLE     var CrlIdentifier: uint32     var CrlThisTime: CSSM_TIMESTRING     var PolicyIdentifier: CSSM_FIELD_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, CrlIdentifier CrlIdentifier: uint32, CrlThisTime CrlThisTime: CSSM_TIMESTRING, PolicyIdentifier PolicyIdentifier: CSSM_FIELD_PTR, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |

Modified cssm_tp_crlissue_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_crlissue_output {     var IssueStatus: CSSM_TP_CRLISSUE_STATUS     var Crl: CSSM_ENCODED_CRL_PTR     var CrlNextTime: CSSM_TIMESTRING } ``` |
| To | ``` struct cssm_tp_crlissue_output {     var IssueStatus: CSSM_TP_CRLISSUE_STATUS     var Crl: CSSM_ENCODED_CRL_PTR     var CrlNextTime: CSSM_TIMESTRING     init()     init(IssueStatus IssueStatus: CSSM_TP_CRLISSUE_STATUS, Crl Crl: CSSM_ENCODED_CRL_PTR, CrlNextTime CrlNextTime: CSSM_TIMESTRING) } ``` |

Modified cssm_tp_policyinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_policyinfo {     var NumberOfPolicyIds: uint32     var PolicyIds: CSSM_FIELD_PTR     var PolicyControl: UnsafePointer<()> } ``` |
| To | ``` struct cssm_tp_policyinfo {     var NumberOfPolicyIds: uint32     var PolicyIds: CSSM_FIELD_PTR     var PolicyControl: UnsafeMutablePointer<Void>     init()     init(NumberOfPolicyIds NumberOfPolicyIds: uint32, PolicyIds PolicyIds: CSSM_FIELD_PTR, PolicyControl PolicyControl: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_tp_policyinfo.PolicyControl

|  | Declaration |
| --- | --- |
| From | ``` var PolicyControl: UnsafePointer<()> ``` |
| To | ``` var PolicyControl: UnsafeMutablePointer<Void> ``` |

Modified cssm_tp_request_set [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_request_set {     var NumberOfRequests: uint32     var Requests: UnsafePointer<()> } ``` |
| To | ``` struct cssm_tp_request_set {     var NumberOfRequests: uint32     var Requests: UnsafeMutablePointer<Void>     init()     init(NumberOfRequests NumberOfRequests: uint32, Requests Requests: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_tp_request_set.Requests

|  | Declaration |
| --- | --- |
| From | ``` var Requests: UnsafePointer<()> ``` |
| To | ``` var Requests: UnsafeMutablePointer<Void> ``` |

Modified cssm_tp_result_set [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_result_set {     var NumberOfResults: uint32     var Results: UnsafePointer<()> } ``` |
| To | ``` struct cssm_tp_result_set {     var NumberOfResults: uint32     var Results: UnsafeMutablePointer<Void>     init()     init(NumberOfResults NumberOfResults: uint32, Results Results: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_tp_result_set.Results

|  | Declaration |
| --- | --- |
| From | ``` var Results: UnsafePointer<()> ``` |
| To | ``` var Results: UnsafeMutablePointer<Void> ``` |

Modified cssm_tp_verify_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_verify_context {     var Action: CSSM_TP_ACTION     var ActionData: CSSM_DATA     var Crls: CSSM_CRLGROUP     var Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR } ``` |
| To | ``` struct cssm_tp_verify_context {     var Action: CSSM_TP_ACTION     var ActionData: CSSM_DATA     var Crls: CSSM_CRLGROUP     var Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR     init()     init(Action Action: CSSM_TP_ACTION, ActionData ActionData: CSSM_DATA, Crls Crls: CSSM_CRLGROUP, Cred Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR) } ``` |

Modified cssm_tp_verify_context_result [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_verify_context_result {     var NumberOfEvidences: uint32     var Evidence: CSSM_EVIDENCE_PTR } ``` |
| To | ``` struct cssm_tp_verify_context_result {     var NumberOfEvidences: uint32     var Evidence: CSSM_EVIDENCE_PTR     init()     init(NumberOfEvidences NumberOfEvidences: uint32, Evidence Evidence: CSSM_EVIDENCE_PTR) } ``` |

Modified cssm_tuplegroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tuplegroup {     var NumberOfTuples: uint32     var Tuples: CSSM_TUPLE_PTR } ``` |
| To | ``` struct cssm_tuplegroup {     var NumberOfTuples: uint32     var Tuples: CSSM_TUPLE_PTR     init()     init(NumberOfTuples NumberOfTuples: uint32, Tuples Tuples: CSSM_TUPLE_PTR) } ``` |

Modified cssm_upcalls [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_upcalls {     var malloc_func: CSSM_UPCALLS_MALLOC     var free_func: CSSM_UPCALLS_FREE     var realloc_func: CSSM_UPCALLS_REALLOC     var calloc_func: CSSM_UPCALLS_CALLOC     var CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>     var GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_SERVICE_TYPE>, UnsafePointer<CSSM_ATTACH_FLAGS>, UnsafePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)> } ``` |
| To | ``` struct cssm_upcalls {     var malloc_func: CSSM_UPCALLS_MALLOC     var free_func: CSSM_UPCALLS_FREE     var realloc_func: CSSM_UPCALLS_REALLOC     var calloc_func: CSSM_UPCALLS_CALLOC     var CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>     var GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>     init()     init(malloc_func malloc_func: CSSM_UPCALLS_MALLOC, free_func free_func: CSSM_UPCALLS_FREE, realloc_func realloc_func: CSSM_UPCALLS_REALLOC, calloc_func calloc_func: CSSM_UPCALLS_CALLOC, CcToHandle_func CcToHandle_func: CFunctionPointer<((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)>, GetModuleInfo_func GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)>) } ``` |

Modified cssm_upcalls.GetModuleInfo_func

|  | Declaration |
| --- | --- |
| From | ``` var GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafePointer<uint32>, UnsafePointer<CSSM_SERVICE_TYPE>, UnsafePointer<CSSM_ATTACH_FLAGS>, UnsafePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)> ``` |
| To | ``` var GetModuleInfo_func: CFunctionPointer<((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)> ``` |

Modified cssm_version [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_version {     var Major: uint32     var Minor: uint32 } ``` |
| To | ``` struct cssm_version {     var Major: uint32     var Minor: uint32     init()     init(Major Major: uint32, Minor Minor: uint32) } ``` |

Modified cssm_x509_algorithm_identifier [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_algorithm_identifier {     var algorithm: CSSM_OID     var parameters: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_algorithm_identifier {     var algorithm: CSSM_OID     var parameters: CSSM_DATA     init()     init(algorithm algorithm: CSSM_OID, parameters parameters: CSSM_DATA) } ``` |

Modified cssm_x509_extension [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_extension {     var extnId: CSSM_OID     var critical: CSSM_BOOL     var format: CSSM_X509EXT_DATA_FORMAT     var BERvalue: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_extension {     var extnId: CSSM_OID     var critical: CSSM_BOOL     var format: CSSM_X509EXT_DATA_FORMAT     var value: cssm_x509ext_value     var BERvalue: CSSM_DATA     init()     init(extnId extnId: CSSM_OID, critical critical: CSSM_BOOL, format format: CSSM_X509EXT_DATA_FORMAT, value value: cssm_x509ext_value, BERvalue BERvalue: CSSM_DATA) } ``` |

Modified cssm_x509_extensionTagAndValue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_extensionTagAndValue {     var type: CSSM_BER_TAG     var value: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_extensionTagAndValue {     var type: CSSM_BER_TAG     var value: CSSM_DATA     init()     init(type type: CSSM_BER_TAG, value value: CSSM_DATA) } ``` |

Modified cssm_x509_extensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_extensions {     var numberOfExtensions: uint32     var extensions: CSSM_X509_EXTENSION_PTR } ``` |
| To | ``` struct cssm_x509_extensions {     var numberOfExtensions: uint32     var extensions: CSSM_X509_EXTENSION_PTR     init()     init(numberOfExtensions numberOfExtensions: uint32, extensions extensions: CSSM_X509_EXTENSION_PTR) } ``` |

Modified cssm_x509_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_name {     var numberOfRDNs: uint32     var RelativeDistinguishedName: CSSM_X509_RDN_PTR } ``` |
| To | ``` struct cssm_x509_name {     var numberOfRDNs: uint32     var RelativeDistinguishedName: CSSM_X509_RDN_PTR     init()     init(numberOfRDNs numberOfRDNs: uint32, RelativeDistinguishedName RelativeDistinguishedName: CSSM_X509_RDN_PTR) } ``` |

Modified cssm_x509_rdn [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_rdn {     var numberOfPairs: uint32     var AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR } ``` |
| To | ``` struct cssm_x509_rdn {     var numberOfPairs: uint32     var AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR     init()     init(numberOfPairs numberOfPairs: uint32, AttributeTypeAndValue AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR) } ``` |

Modified cssm_x509_revoked_cert_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_revoked_cert_entry {     var certificateSerialNumber: CSSM_DATA     var revocationDate: CSSM_X509_TIME     var extensions: CSSM_X509_EXTENSIONS } ``` |
| To | ``` struct cssm_x509_revoked_cert_entry {     var certificateSerialNumber: CSSM_DATA     var revocationDate: CSSM_X509_TIME     var extensions: CSSM_X509_EXTENSIONS     init()     init(certificateSerialNumber certificateSerialNumber: CSSM_DATA, revocationDate revocationDate: CSSM_X509_TIME, extensions extensions: CSSM_X509_EXTENSIONS) } ``` |

Modified cssm_x509_revoked_cert_list [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_revoked_cert_list {     var numberOfRevokedCertEntries: uint32     var revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR } ``` |
| To | ``` struct cssm_x509_revoked_cert_list {     var numberOfRevokedCertEntries: uint32     var revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR     init()     init(numberOfRevokedCertEntries numberOfRevokedCertEntries: uint32, revokedCertEntry revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR) } ``` |

Modified cssm_x509_signature [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_signature {     var algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER     var encrypted: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_signature {     var algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER     var encrypted: CSSM_DATA     init()     init(algorithmIdentifier algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER, encrypted encrypted: CSSM_DATA) } ``` |

Modified cssm_x509_signed_certificate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_signed_certificate {     var certificate: CSSM_X509_TBS_CERTIFICATE     var signature: CSSM_X509_SIGNATURE } ``` |
| To | ``` struct cssm_x509_signed_certificate {     var certificate: CSSM_X509_TBS_CERTIFICATE     var signature: CSSM_X509_SIGNATURE     init()     init(certificate certificate: CSSM_X509_TBS_CERTIFICATE, signature signature: CSSM_X509_SIGNATURE) } ``` |

Modified cssm_x509_signed_crl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_signed_crl {     var tbsCertList: CSSM_X509_TBS_CERTLIST     var signature: CSSM_X509_SIGNATURE } ``` |
| To | ``` struct cssm_x509_signed_crl {     var tbsCertList: CSSM_X509_TBS_CERTLIST     var signature: CSSM_X509_SIGNATURE     init()     init(tbsCertList tbsCertList: CSSM_X509_TBS_CERTLIST, signature signature: CSSM_X509_SIGNATURE) } ``` |

Modified cssm_x509_subject_public_key_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_subject_public_key_info {     var algorithm: CSSM_X509_ALGORITHM_IDENTIFIER     var subjectPublicKey: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_subject_public_key_info {     var algorithm: CSSM_X509_ALGORITHM_IDENTIFIER     var subjectPublicKey: CSSM_DATA     init()     init(algorithm algorithm: CSSM_X509_ALGORITHM_IDENTIFIER, subjectPublicKey subjectPublicKey: CSSM_DATA) } ``` |

Modified cssm_x509_tbs_certificate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_tbs_certificate {     var version: CSSM_DATA     var serialNumber: CSSM_DATA     var signature: CSSM_X509_ALGORITHM_IDENTIFIER     var issuer: CSSM_X509_NAME     var validity: CSSM_X509_VALIDITY     var subject: CSSM_X509_NAME     var subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO     var issuerUniqueIdentifier: CSSM_DATA     var subjectUniqueIdentifier: CSSM_DATA     var extensions: CSSM_X509_EXTENSIONS } ``` |
| To | ``` struct cssm_x509_tbs_certificate {     var version: CSSM_DATA     var serialNumber: CSSM_DATA     var signature: CSSM_X509_ALGORITHM_IDENTIFIER     var issuer: CSSM_X509_NAME     var validity: CSSM_X509_VALIDITY     var subject: CSSM_X509_NAME     var subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO     var issuerUniqueIdentifier: CSSM_DATA     var subjectUniqueIdentifier: CSSM_DATA     var extensions: CSSM_X509_EXTENSIONS     init()     init(version version: CSSM_DATA, serialNumber serialNumber: CSSM_DATA, signature signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer issuer: CSSM_X509_NAME, validity validity: CSSM_X509_VALIDITY, subject subject: CSSM_X509_NAME, subjectPublicKeyInfo subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO, issuerUniqueIdentifier issuerUniqueIdentifier: CSSM_DATA, subjectUniqueIdentifier subjectUniqueIdentifier: CSSM_DATA, extensions extensions: CSSM_X509_EXTENSIONS) } ``` |

Modified cssm_x509_tbs_certlist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_tbs_certlist {     var version: CSSM_DATA     var signature: CSSM_X509_ALGORITHM_IDENTIFIER     var issuer: CSSM_X509_NAME     var thisUpdate: CSSM_X509_TIME     var nextUpdate: CSSM_X509_TIME     var revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR     var extensions: CSSM_X509_EXTENSIONS } ``` |
| To | ``` struct cssm_x509_tbs_certlist {     var version: CSSM_DATA     var signature: CSSM_X509_ALGORITHM_IDENTIFIER     var issuer: CSSM_X509_NAME     var thisUpdate: CSSM_X509_TIME     var nextUpdate: CSSM_X509_TIME     var revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR     var extensions: CSSM_X509_EXTENSIONS     init()     init(version version: CSSM_DATA, signature signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer issuer: CSSM_X509_NAME, thisUpdate thisUpdate: CSSM_X509_TIME, nextUpdate nextUpdate: CSSM_X509_TIME, revokedCertificates revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR, extensions extensions: CSSM_X509_EXTENSIONS) } ``` |

Modified cssm_x509_time [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_time {     var timeType: CSSM_BER_TAG     var time: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_time {     var timeType: CSSM_BER_TAG     var time: CSSM_DATA     init()     init(timeType timeType: CSSM_BER_TAG, time time: CSSM_DATA) } ``` |

Modified cssm_x509_type_value_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_type_value_pair {     var type: CSSM_OID     var valueType: CSSM_BER_TAG     var value: CSSM_DATA } ``` |
| To | ``` struct cssm_x509_type_value_pair {     var type: CSSM_OID     var valueType: CSSM_BER_TAG     var value: CSSM_DATA     init()     init(type type: CSSM_OID, valueType valueType: CSSM_BER_TAG, value value: CSSM_DATA) } ``` |

Modified cssm_x509ext_basicConstraints [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_basicConstraints {     var cA: CSSM_BOOL     var pathLenConstraintPresent: CSSM_X509_OPTION     var pathLenConstraint: uint32 } ``` |
| To | ``` struct cssm_x509ext_basicConstraints {     var cA: CSSM_BOOL     var pathLenConstraintPresent: CSSM_X509_OPTION     var pathLenConstraint: uint32     init()     init(cA cA: CSSM_BOOL, pathLenConstraintPresent pathLenConstraintPresent: CSSM_X509_OPTION, pathLenConstraint pathLenConstraint: uint32) } ``` |

Modified cssm_x509ext_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_pair {     var tagAndValue: CSSM_X509EXT_TAGandVALUE     var parsedValue: UnsafePointer<()> } ``` |
| To | ``` struct cssm_x509ext_pair {     var tagAndValue: CSSM_X509EXT_TAGandVALUE     var parsedValue: UnsafeMutablePointer<Void>     init()     init(tagAndValue tagAndValue: CSSM_X509EXT_TAGandVALUE, parsedValue parsedValue: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_x509ext_pair.parsedValue

|  | Declaration |
| --- | --- |
| From | ``` var parsedValue: UnsafePointer<()> ``` |
| To | ``` var parsedValue: UnsafeMutablePointer<Void> ``` |

Modified cssm_x509ext_policyInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_policyInfo {     var policyIdentifier: CSSM_OID     var policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS } ``` |
| To | ``` struct cssm_x509ext_policyInfo {     var policyIdentifier: CSSM_OID     var policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS     init()     init(policyIdentifier policyIdentifier: CSSM_OID, policyQualifiers policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS) } ``` |

Modified cssm_x509ext_policyQualifierInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_policyQualifierInfo {     var policyQualifierId: CSSM_OID     var value: CSSM_DATA } ``` |
| To | ``` struct cssm_x509ext_policyQualifierInfo {     var policyQualifierId: CSSM_OID     var value: CSSM_DATA     init()     init(policyQualifierId policyQualifierId: CSSM_OID, value value: CSSM_DATA) } ``` |

Modified cssm_x509ext_policyQualifiers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_policyQualifiers {     var numberOfPolicyQualifiers: uint32     var policyQualifier: UnsafePointer<CSSM_X509EXT_POLICYQUALIFIERINFO> } ``` |
| To | ``` struct cssm_x509ext_policyQualifiers {     var numberOfPolicyQualifiers: uint32     var policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO>     init()     init(numberOfPolicyQualifiers numberOfPolicyQualifiers: uint32, policyQualifier policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO>) } ``` |

Modified cssm_x509ext_policyQualifiers.policyQualifier

|  | Declaration |
| --- | --- |
| From | ``` var policyQualifier: UnsafePointer<CSSM_X509EXT_POLICYQUALIFIERINFO> ``` |
| To | ``` var policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO> ``` |

Modified mds_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mds_funcs {     var DbOpen: CFunctionPointer<((MDS_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<()>, UnsafePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>     var GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>     var GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<UnsafePointer<Int8>>) -> CSSM_RETURN)>     var FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>     var DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataDelete: CFunctionPointer<((MDS_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>     var DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>     var DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, ConstUnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>     var CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<Int8>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>     var DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)> } ``` |
| To | ``` struct mds_funcs {     var DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>     var DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>     var GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>     var GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>     var FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>     var DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>     var DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>     var DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>     var DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>     var DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>     var FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>     var CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>     var DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>     init()     init(DbOpen DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)>, DbClose DbClose: CFunctionPointer<((MDS_DB_HANDLE) -> CSSM_RETURN)>, GetDbNames GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)>, GetDbNameFromHandle GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)>, FreeNameList FreeNameList: CFunctionPointer<((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)>, DataInsert DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataDelete DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)>, DataModify DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)>, DataGetFirst DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataGetNext DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)>, DataAbortQuery DataAbortQuery: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)>, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)>, FreeUniqueRecord FreeUniqueRecord: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)>, CreateRelation CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)>, DestroyRelation DestroyRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)>) } ``` |

Modified mds_funcs.CreateRelation

|  | Declaration |
| --- | --- |
| From | ``` var CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<Int8>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, ConstUnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)> ``` |
| To | ``` var CreateRelation: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DataDelete

|  | Declaration |
| --- | --- |
| From | ``` var DataDelete: CFunctionPointer<((MDS_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)> ``` |
| To | ``` var DataDelete: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DataGetFirst

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, ConstUnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFirst: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DataGetFromUniqueRecordId

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, ConstUnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetFromUniqueRecordId: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DataGetNext

|  | Declaration |
| --- | --- |
| From | ``` var DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataGetNext: CFunctionPointer<((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DataInsert

|  | Declaration |
| --- | --- |
| From | ``` var DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var DataInsert: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DataModify

|  | Declaration |
| --- | --- |
| From | ``` var DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, ConstUnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, ConstUnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)> ``` |
| To | ``` var DataModify: CFunctionPointer<((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)> ``` |

Modified mds_funcs.DbOpen

|  | Declaration |
| --- | --- |
| From | ``` var DbOpen: CFunctionPointer<((MDS_HANDLE, ConstUnsafePointer<Int8>, ConstUnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, ConstUnsafePointer<CSSM_ACCESS_CREDENTIALS>, ConstUnsafePointer<()>, UnsafePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |
| To | ``` var DbOpen: CFunctionPointer<((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.GetDbNameFromHandle

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafePointer<UnsafePointer<Int8>>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNameFromHandle: CFunctionPointer<((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)> ``` |

Modified mds_funcs.GetDbNames

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)> ``` |
| To | ``` var GetDbNames: CFunctionPointer<((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)> ``` |

Modified x509_validity [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x509_validity {     var notBefore: CSSM_X509_TIME     var notAfter: CSSM_X509_TIME } ``` |
| To | ``` struct x509_validity {     var notBefore: CSSM_X509_TIME     var notAfter: CSSM_X509_TIME     init()     init(notBefore notBefore: CSSM_X509_TIME, notAfter notAfter: CSSM_X509_TIME) } ``` |

Modified AuthorizationAsyncCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AuthorizationAsyncCallback = (OSStatus, UnsafePointer<AuthorizationRights>) -> Void ``` |
| To | ``` typealias AuthorizationAsyncCallback = (OSStatus, UnsafeMutablePointer<AuthorizationRights>) -> Void ``` |

Modified AuthorizationCopyInfo(AuthorizationRef, AuthorizationString, UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyInfo(_ authorization: Authorization!, _ tag: AuthorizationString, _ info: UnsafePointer<UnsafePointer<AuthorizationItemSet>>) -> OSStatus ``` |
| To | ``` func AuthorizationCopyInfo(_ authorization: AuthorizationRef, _ tag: AuthorizationString, _ info: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>>) -> OSStatus ``` |

Modified AuthorizationCopyRights(AuthorizationRef, UnsafePointer<AuthorizationRights>, UnsafePointer<AuthorizationEnvironment>, AuthorizationFlags, UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyRights(_ authorization: Authorization!, _ rights: ConstUnsafePointer<AuthorizationRights>, _ environment: ConstUnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ authorizedRights: UnsafePointer<UnsafePointer<AuthorizationRights>>) -> OSStatus ``` |
| To | ``` func AuthorizationCopyRights(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) -> OSStatus ``` |

Modified AuthorizationCopyRightsAsync(AuthorizationRef, UnsafePointer<AuthorizationRights>, UnsafePointer<AuthorizationEnvironment>, AuthorizationFlags, AuthorizationAsyncCallback!)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyRightsAsync(_ authorization: Authorization!, _ rights: ConstUnsafePointer<AuthorizationRights>, _ environment: ConstUnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ callbackBlock: AuthorizationAsyncCallback!) ``` |
| To | ``` func AuthorizationCopyRightsAsync(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ callbackBlock: AuthorizationAsyncCallback!) ``` |

Modified AuthorizationCreate(UnsafePointer<AuthorizationRights>, UnsafePointer<AuthorizationEnvironment>, AuthorizationFlags, UnsafeMutablePointer<AuthorizationRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCreate(_ rights: ConstUnsafePointer<AuthorizationRights>, _ environment: ConstUnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ authorization: UnsafePointer<Unmanaged<Authorization>?>) -> OSStatus ``` |
| To | ``` func AuthorizationCreate(_ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ authorization: UnsafeMutablePointer<AuthorizationRef>) -> OSStatus ``` |

Modified AuthorizationCreateFromExternalForm(UnsafePointer<AuthorizationExternalForm>, UnsafeMutablePointer<AuthorizationRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCreateFromExternalForm(_ extForm: ConstUnsafePointer<AuthorizationExternalForm>, _ authorization: UnsafePointer<Unmanaged<Authorization>?>) -> OSStatus ``` |
| To | ``` func AuthorizationCreateFromExternalForm(_ extForm: UnsafePointer<AuthorizationExternalForm>, _ authorization: UnsafeMutablePointer<AuthorizationRef>) -> OSStatus ``` |

Modified AuthorizationFree(AuthorizationRef, AuthorizationFlags) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationFree(_ authorization: Authorization!, _ flags: AuthorizationFlags) -> OSStatus ``` |
| To | ``` func AuthorizationFree(_ authorization: AuthorizationRef, _ flags: AuthorizationFlags) -> OSStatus ``` |

Modified AuthorizationFreeItemSet(UnsafeMutablePointer<AuthorizationItemSet>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationFreeItemSet(_ set: UnsafePointer<AuthorizationItemSet>) -> OSStatus ``` |
| To | ``` func AuthorizationFreeItemSet(_ set: UnsafeMutablePointer<AuthorizationItemSet>) -> OSStatus ``` |

Modified AuthorizationMakeExternalForm(AuthorizationRef, UnsafeMutablePointer<AuthorizationExternalForm>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationMakeExternalForm(_ authorization: Authorization!, _ extForm: UnsafePointer<AuthorizationExternalForm>) -> OSStatus ``` |
| To | ``` func AuthorizationMakeExternalForm(_ authorization: AuthorizationRef, _ extForm: UnsafeMutablePointer<AuthorizationExternalForm>) -> OSStatus ``` |

Modified AuthorizationRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AuthorizationRef = Authorization ``` |
| To | ``` typealias AuthorizationRef = COpaquePointer ``` |

Modified AuthorizationRightGet(UnsafePointer<Int8>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightGet(_ rightName: ConstUnsafePointer<Int8>, _ rightDefinition: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func AuthorizationRightGet(_ rightName: UnsafePointer<Int8>, _ rightDefinition: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |

Modified AuthorizationRightRemove(AuthorizationRef, UnsafePointer<Int8>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightRemove(_ authRef: Authorization!, _ rightName: ConstUnsafePointer<Int8>) -> OSStatus ``` |
| To | ``` func AuthorizationRightRemove(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<Int8>) -> OSStatus ``` |

Modified AuthorizationRightSet(AuthorizationRef, UnsafePointer<Int8>, AnyObject!, CFString!, CFBundle!, CFString!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightSet(_ authRef: Authorization!, _ rightName: ConstUnsafePointer<Int8>, _ rightDefinition: AnyObject!, _ descriptionKey: CFString!, _ bundle: CFBundle!, _ localeTableName: CFString!) -> OSStatus ``` |
| To | ``` func AuthorizationRightSet(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<Int8>, _ rightDefinition: AnyObject!, _ descriptionKey: CFString!, _ bundle: CFBundle!, _ localeTableName: CFString!) -> OSStatus ``` |

Modified AuthorizationString

|  | Declaration |
| --- | --- |
| From | ``` typealias AuthorizationString = ConstUnsafePointer<Int8> ``` |
| To | ``` typealias AuthorizationString = UnsafePointer<Int8> ``` |

Modified CMSDecoderCopyAllCerts(CMSDecoder!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder!, _ certsOut: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopyAllCerts(_ cmsDecoder: CMSDecoder!, _ certsOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopyContent(CMSDecoder!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder!, _ contentOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopyContent(_ cmsDecoder: CMSDecoder!, _ contentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopyDetachedContent(CMSDecoder!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopyDetachedContent(_ cmsDecoder: CMSDecoder!, _ detachedContentOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopyDetachedContent(_ cmsDecoder: CMSDecoder!, _ detachedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopyEncapsulatedContentType(CMSDecoder!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopyEncapsulatedContentType(_ cmsDecoder: CMSDecoder!, _ eContentTypeOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopyEncapsulatedContentType(_ cmsDecoder: CMSDecoder!, _ eContentTypeOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopySignerCert(CMSDecoder!, Int, UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder!, _ signerIndex: UInt, _ signerCertOut: UnsafePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopySignerCert(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ signerCertOut: UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopySignerEmailAddress(CMSDecoder!, Int, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopySignerEmailAddress(_ cmsDecoder: CMSDecoder!, _ signerIndex: UInt, _ signerEmailAddressOut: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopySignerEmailAddress(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ signerEmailAddressOut: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopySignerSigningTime(CMSDecoder!, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopySignerSigningTime(_ cmsDecoder: CMSDecoder!, _ signerIndex: UInt, _ signingTime: UnsafePointer<CFAbsoluteTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopySignerSigningTime(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ signingTime: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` | OS X 10.8 |

Modified CMSDecoderCopySignerStatus(CMSDecoder!, Int, AnyObject!, Boolean, UnsafeMutablePointer<CMSSignerStatus>, UnsafeMutablePointer<Unmanaged<SecTrust>?>, UnsafeMutablePointer<OSStatus>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder!, _ signerIndex: UInt, _ policyOrArray: AnyObject!, _ evaluateSecTrust: Boolean, _ signerStatusOut: UnsafePointer<CMSSignerStatus>, _ secTrustOut: UnsafePointer<Unmanaged<SecTrust>?>, _ certVerifyResultCodeOut: UnsafePointer<OSStatus>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ policyOrArray: AnyObject!, _ evaluateSecTrust: Boolean, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>, _ secTrustOut: UnsafeMutablePointer<Unmanaged<SecTrust>?>, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderCopySignerTimestamp(CMSDecoder!, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder!, _ signerIndex: UInt, _ timestamp: UnsafePointer<CFAbsoluteTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` | OS X 10.8 |

Modified CMSDecoderCopySignerTimestampCertificates(CMSDecoder!, Int, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCopySignerTimestampCertificates(_ cmsDecoder: CMSDecoder!, _ signerIndex: UInt, _ certificateRefs: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCopySignerTimestampCertificates(_ cmsDecoder: CMSDecoder!, _ signerIndex: Int, _ certificateRefs: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.8 |

Modified CMSDecoderCreate(UnsafeMutablePointer<Unmanaged<CMSDecoder>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderCreate(_ cmsDecoderOut: UnsafePointer<Unmanaged<CMSDecoder>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderCreate(_ cmsDecoderOut: UnsafeMutablePointer<Unmanaged<CMSDecoder>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderFinalizeMessage(CMSDecoder!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSDecoderGetNumSigners(CMSDecoder!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderGetNumSigners(_ cmsDecoder: CMSDecoder!, _ numSignersOut: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderGetNumSigners(_ cmsDecoder: CMSDecoder!, _ numSignersOut: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderIsContentEncrypted(CMSDecoder!, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder!, _ isEncryptedOut: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderIsContentEncrypted(_ cmsDecoder: CMSDecoder!, _ isEncryptedOut: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified CMSDecoderSetDetachedContent(CMSDecoder!, CFData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSDecoderSetSearchKeychain(CMSDecoder!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSDecoderUpdateMessage(CMSDecoder!, UnsafePointer<Void>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder!, _ msgBytes: ConstUnsafePointer<()>, _ msgBytesLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder!, _ msgBytes: UnsafePointer<Void>, _ msgBytesLen: Int) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncode(AnyObject!, AnyObject!, UnsafePointer<CSSM_OID>, Boolean, CMSSignedAttributes, UnsafePointer<Void>, Int, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncode(_ signers: AnyObject!, _ recipients: AnyObject!, _ eContentType: ConstUnsafePointer<CSSM_OID>, _ detachedContent: Boolean, _ signedAttributes: CMSSignedAttributes, _ content: ConstUnsafePointer<()>, _ contentLen: UInt, _ encodedContentOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncode(_ signers: AnyObject!, _ recipients: AnyObject!, _ eContentType: UnsafePointer<CSSM_OID>, _ detachedContent: Boolean, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncodeContent(AnyObject!, AnyObject!, AnyObject!, Boolean, CMSSignedAttributes, UnsafePointer<Void>, Int, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncodeContent(_ signers: AnyObject!, _ recipients: AnyObject!, _ eContentTypeOID: AnyObject!, _ detachedContent: Boolean, _ signedAttributes: CMSSignedAttributes, _ content: ConstUnsafePointer<()>, _ contentLen: UInt, _ encodedContentOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncodeContent(_ signers: AnyObject!, _ recipients: AnyObject!, _ eContentTypeOID: AnyObject!, _ detachedContent: Boolean, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSEncoderAddRecipients(CMSEncoder!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderAddSignedAttributes(CMSEncoder!, CMSSignedAttributes) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderAddSigners(CMSEncoder!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderAddSupportingCerts(CMSEncoder!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderCopyEncapsulatedContentType(CMSEncoder!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCopyEncapsulatedContentType(_ cmsEncoder: CMSEncoder!, _ eContentTypeOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCopyEncapsulatedContentType(_ cmsEncoder: CMSEncoder!, _ eContentTypeOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderCopyEncodedContent(CMSEncoder!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCopyEncodedContent(_ cmsEncoder: CMSEncoder!, _ encodedContentOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCopyEncodedContent(_ cmsEncoder: CMSEncoder!, _ encodedContentOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderCopyRecipients(CMSEncoder!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCopyRecipients(_ cmsEncoder: CMSEncoder!, _ recipientsOut: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCopyRecipients(_ cmsEncoder: CMSEncoder!, _ recipientsOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderCopySignerTimestamp(CMSEncoder!, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCopySignerTimestamp(_ cmsEncoder: CMSEncoder!, _ signerIndex: UInt, _ timestamp: UnsafePointer<CFAbsoluteTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCopySignerTimestamp(_ cmsEncoder: CMSEncoder!, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` | OS X 10.8 |

Modified CMSEncoderCopySigners(CMSEncoder!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCopySigners(_ cmsEncoder: CMSEncoder!, _ signersOut: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCopySigners(_ cmsEncoder: CMSEncoder!, _ signersOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderCopySupportingCerts(CMSEncoder!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCopySupportingCerts(_ cmsEncoder: CMSEncoder!, _ certsOut: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCopySupportingCerts(_ cmsEncoder: CMSEncoder!, _ certsOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderCreate(UnsafeMutablePointer<Unmanaged<CMSEncoder>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderCreate(_ cmsEncoderOut: UnsafePointer<Unmanaged<CMSEncoder>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderCreate(_ cmsEncoderOut: UnsafeMutablePointer<Unmanaged<CMSEncoder>?>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderGetCertificateChainMode(CMSEncoder!, UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderGetCertificateChainMode(_ cmsEncoder: CMSEncoder!, _ chainModeOut: UnsafePointer<CMSCertificateChainMode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderGetCertificateChainMode(_ cmsEncoder: CMSEncoder!, _ chainModeOut: UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderGetHasDetachedContent(CMSEncoder!, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder!, _ detachedContentOut: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderGetHasDetachedContent(_ cmsEncoder: CMSEncoder!, _ detachedContentOut: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderSetCertificateChainMode(CMSEncoder!, CMSCertificateChainMode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderSetEncapsulatedContentType(CMSEncoder!, UnsafePointer<CSSM_OID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderSetEncapsulatedContentType(_ cmsEncoder: CMSEncoder!, _ eContentType: ConstUnsafePointer<CSSM_OID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderSetEncapsulatedContentType(_ cmsEncoder: CMSEncoder!, _ eContentType: UnsafePointer<CSSM_OID>) -> OSStatus ``` | OS X 10.5 |

Modified CMSEncoderSetEncapsulatedContentTypeOID(CMSEncoder!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSEncoderSetHasDetachedContent(CMSEncoder!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CMSEncoderUpdateContent(CMSEncoder!, UnsafePointer<Void>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder!, _ content: ConstUnsafePointer<()>, _ contentLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder!, _ content: UnsafePointer<Void>, _ contentLen: Int) -> OSStatus ``` | OS X 10.5 |

Modified CSSM_ACL_SUBJECT_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_ACL_SUBJECT_CALLBACK = CFunctionPointer<((ConstUnsafePointer<CSSM_LIST>, CSSM_LIST_PTR, UnsafePointer<()>, ConstUnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_ACL_SUBJECT_CALLBACK = CFunctionPointer<((UnsafePointer<CSSM_LIST>, CSSM_LIST_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN)> ``` |

Modified CSSM_API_MEMORY_FUNCS_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_API_MEMORY_FUNCS_PTR = UnsafePointer<CSSM_API_MEMORY_FUNCS> ``` |
| To | ``` typealias CSSM_API_MEMORY_FUNCS_PTR = UnsafeMutablePointer<CSSM_API_MEMORY_FUNCS> ``` |

Modified CSSM_API_ModuleEventHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_API_ModuleEventHandler = CFunctionPointer<((ConstUnsafePointer<CSSM_GUID>, UnsafePointer<()>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_API_ModuleEventHandler = CFunctionPointer<((UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN)> ``` |

Modified CSSM_APPLECSPDL_DB_CHANGE_PASSWORD_PARAMETERS_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_APPLECSPDL_DB_CHANGE_PASSWORD_PARAMETERS_PTR = UnsafePointer<cssm_applecspdl_db_change_password_parameters> ``` |
| To | ``` typealias CSSM_APPLECSPDL_DB_CHANGE_PASSWORD_PARAMETERS_PTR = UnsafeMutablePointer<cssm_applecspdl_db_change_password_parameters> ``` |

Modified CSSM_APPLECSPDL_DB_IS_LOCKED_PARAMETERS_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_APPLECSPDL_DB_IS_LOCKED_PARAMETERS_PTR = UnsafePointer<cssm_applecspdl_db_is_locked_parameters> ``` |
| To | ``` typealias CSSM_APPLECSPDL_DB_IS_LOCKED_PARAMETERS_PTR = UnsafeMutablePointer<cssm_applecspdl_db_is_locked_parameters> ``` |

Modified CSSM_APPLECSPDL_DB_SETTINGS_PARAMETERS_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_APPLECSPDL_DB_SETTINGS_PARAMETERS_PTR = UnsafePointer<cssm_applecspdl_db_settings_parameters> ``` |
| To | ``` typealias CSSM_APPLECSPDL_DB_SETTINGS_PARAMETERS_PTR = UnsafeMutablePointer<cssm_applecspdl_db_settings_parameters> ``` |

Modified CSSM_APPLEDL_OPEN_PARAMETERS_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_APPLEDL_OPEN_PARAMETERS_PTR = UnsafePointer<cssm_appledl_open_parameters> ``` |
| To | ``` typealias CSSM_APPLEDL_OPEN_PARAMETERS_PTR = UnsafeMutablePointer<cssm_appledl_open_parameters> ``` |

Modified CSSM_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CALLBACK = CFunctionPointer<((CSSM_DATA_PTR, UnsafePointer<()>) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_CALLBACK = CFunctionPointer<((CSSM_DATA_PTR, UnsafeMutablePointer<Void>) -> CSSM_RETURN)> ``` |

Modified CSSM_CALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CALLOC = CFunctionPointer<((uint32, CSSM_SIZE, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CSSM_CALLOC = CFunctionPointer<((uint32, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CSSM_CERTGROUP_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CERTGROUP_PTR = UnsafePointer<cssm_certgroup> ``` |
| To | ``` typealias CSSM_CERTGROUP_PTR = UnsafeMutablePointer<cssm_certgroup> ``` |

Modified CSSM_CERTGROUP_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CERTGROUP_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CERTGROUP_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CERT_ENCODING_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CERT_ENCODING_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CERT_ENCODING_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CERT_PARSE_FORMAT_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CERT_PARSE_FORMAT_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CERT_PARSE_FORMAT_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CERT_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CERT_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CERT_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CHALLENGE_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CHALLENGE_CALLBACK = CFunctionPointer<((ConstUnsafePointer<CSSM_LIST>, CSSM_SAMPLEGROUP_PTR, UnsafePointer<()>, ConstUnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_CHALLENGE_CALLBACK = CFunctionPointer<((UnsafePointer<CSSM_LIST>, CSSM_SAMPLEGROUP_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN)> ``` |

Modified CSSM_CONTEXT_ATTRIBUTE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CONTEXT_ATTRIBUTE_PTR = UnsafePointer<cssm_context_attribute> ``` |
| To | ``` typealias CSSM_CONTEXT_ATTRIBUTE_PTR = UnsafeMutablePointer<cssm_context_attribute> ``` |

Modified CSSM_CRLGROUP_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CRLGROUP_PTR = UnsafePointer<cssm_crlgroup> ``` |
| To | ``` typealias CSSM_CRLGROUP_PTR = UnsafeMutablePointer<cssm_crlgroup> ``` |

Modified CSSM_CRLGROUP_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CRLGROUP_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CRLGROUP_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CRL_ENCODING_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CRL_ENCODING_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CRL_ENCODING_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CRL_PARSE_FORMAT_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CRL_PARSE_FORMAT_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CRL_PARSE_FORMAT_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_CRL_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CRL_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_CRL_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DB_ACCESS_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DB_ACCESS_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_DB_ACCESS_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DB_ATTRIBUTE_FORMAT_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DB_ATTRIBUTE_FORMAT_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_DB_ATTRIBUTE_FORMAT_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DB_ATTRIBUTE_INFO_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DB_ATTRIBUTE_INFO_PTR = UnsafePointer<cssm_db_attribute_info> ``` |
| To | ``` typealias CSSM_DB_ATTRIBUTE_INFO_PTR = UnsafeMutablePointer<cssm_db_attribute_info> ``` |

Modified CSSM_DB_ATTRIBUTE_NAME_FORMAT_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DB_ATTRIBUTE_NAME_FORMAT_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_DB_ATTRIBUTE_NAME_FORMAT_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DB_CONJUNCTIVE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DB_CONJUNCTIVE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_DB_CONJUNCTIVE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DB_OPERATOR_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DB_OPERATOR_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_DB_OPERATOR_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DLTYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DLTYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_DLTYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_DL_CUSTOM_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_CUSTOM_ATTRIBUTES = UnsafePointer<()> ``` |
| To | ``` typealias CSSM_DL_CUSTOM_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |

Modified CSSM_DL_FFS_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_FFS_ATTRIBUTES = UnsafePointer<()> ``` |
| To | ``` typealias CSSM_DL_FFS_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |

Modified CSSM_DL_LDAP_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_LDAP_ATTRIBUTES = UnsafePointer<()> ``` |
| To | ``` typealias CSSM_DL_LDAP_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |

Modified CSSM_DL_ODBC_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_ODBC_ATTRIBUTES = UnsafePointer<()> ``` |
| To | ``` typealias CSSM_DL_ODBC_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |

Modified CSSM_DL_PKCS11_ATTRIBUTE

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_PKCS11_ATTRIBUTE = UnsafePointer<cssm_dl_pkcs11_attributes> ``` |
| To | ``` typealias CSSM_DL_PKCS11_ATTRIBUTE = UnsafeMutablePointer<cssm_dl_pkcs11_attributes> ``` |

Modified CSSM_DL_PKCS11_ATTRIBUTE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_PKCS11_ATTRIBUTE_PTR = UnsafePointer<cssm_dl_pkcs11_attributes> ``` |
| To | ``` typealias CSSM_DL_PKCS11_ATTRIBUTE_PTR = UnsafeMutablePointer<cssm_dl_pkcs11_attributes> ``` |

Modified CSSM_FREE

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_FREE = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CSSM_FREE = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CSSM_HANDLE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_HANDLE_PTR = UnsafePointer<CSSM_INTPTR> ``` |
| To | ``` typealias CSSM_HANDLE_PTR = UnsafeMutablePointer<CSSM_INTPTR> ``` |

Modified CSSM_KRSUBSERVICE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_KRSUBSERVICE_PTR = UnsafePointer<cssm_krsubservice> ``` |
| To | ``` typealias CSSM_KRSUBSERVICE_PTR = UnsafeMutablePointer<cssm_krsubservice> ``` |

Modified CSSM_LIST_ELEMENT_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_LIST_ELEMENT_PTR = UnsafePointer<cssm_list_element> ``` |
| To | ``` typealias CSSM_LIST_ELEMENT_PTR = UnsafeMutablePointer<cssm_list_element> ``` |

Modified CSSM_LIST_ELEMENT_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_LIST_ELEMENT_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_LIST_ELEMENT_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_LIST_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_LIST_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_LIST_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_LONG_HANDLE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_LONG_HANDLE_PTR = UnsafePointer<uint64> ``` |
| To | ``` typealias CSSM_LONG_HANDLE_PTR = UnsafeMutablePointer<uint64> ``` |

Modified CSSM_MALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_MALLOC = CFunctionPointer<((CSSM_SIZE, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CSSM_MALLOC = CFunctionPointer<((CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CSSM_MODULE_EVENT_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_MODULE_EVENT_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_MODULE_EVENT_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_MODULE_HANDLE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_MODULE_HANDLE_PTR = UnsafePointer<CSSM_HANDLE> ``` |
| To | ``` typealias CSSM_MODULE_HANDLE_PTR = UnsafeMutablePointer<CSSM_HANDLE> ``` |

Modified CSSM_OID_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_OID_PTR = UnsafePointer<CSSM_DATA> ``` |
| To | ``` typealias CSSM_OID_PTR = UnsafeMutablePointer<CSSM_DATA> ``` |

Modified CSSM_PROC_ADDR_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_PROC_ADDR_PTR = UnsafePointer<CSSM_PROC_ADDR> ``` |
| To | ``` typealias CSSM_PROC_ADDR_PTR = UnsafeMutablePointer<CSSM_PROC_ADDR> ``` |

Modified CSSM_REALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_REALLOC = CFunctionPointer<((UnsafePointer<()>, CSSM_SIZE, UnsafePointer<()>) -> UnsafePointer<()>)> ``` |
| To | ``` typealias CSSM_REALLOC = CFunctionPointer<((UnsafeMutablePointer<Void>, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)> ``` |

Modified CSSM_SIZE

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_SIZE = UInt ``` |
| To | ``` typealias CSSM_SIZE = Int ``` |

Modified CSSM_SPI_ModuleEventHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_SPI_ModuleEventHandler = CFunctionPointer<((ConstUnsafePointer<CSSM_GUID>, UnsafePointer<()>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_SPI_ModuleEventHandler = CFunctionPointer<((UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN)> ``` |

Modified CSSM_TIMESTRING

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_TIMESTRING = UnsafePointer<Int8> ``` |
| To | ``` typealias CSSM_TIMESTRING = UnsafeMutablePointer<Int8> ``` |

Modified CSSM_TP_AUTHORITY_REQUEST_TYPE_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_TP_AUTHORITY_REQUEST_TYPE_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_TP_AUTHORITY_REQUEST_TYPE_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_TP_CONFIRM_STATUS_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_TP_CONFIRM_STATUS_PTR = UnsafePointer<uint32> ``` |
| To | ``` typealias CSSM_TP_CONFIRM_STATUS_PTR = UnsafeMutablePointer<uint32> ``` |

Modified CSSM_TP_VERIFICATION_RESULTS_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_TP_VERIFICATION_RESULTS_CALLBACK = CFunctionPointer<((CSSM_MODULE_HANDLE, UnsafePointer<()>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |
| To | ``` typealias CSSM_TP_VERIFICATION_RESULTS_CALLBACK = CFunctionPointer<((CSSM_MODULE_HANDLE, UnsafeMutablePointer<Void>, CSSM_DATA_PTR) -> CSSM_RETURN)> ``` |

Modified CSSM_WRAP_KEY_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_WRAP_KEY_PTR = UnsafePointer<CSSM_KEY> ``` |
| To | ``` typealias CSSM_WRAP_KEY_PTR = UnsafeMutablePointer<CSSM_KEY> ``` |

Modified SSLAddDistinguishedName(SSLContext!, UnsafePointer<Void>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLAddDistinguishedName(_ context: SSLContext!, _ derDN: ConstUnsafePointer<()>, _ derDNLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLAddDistinguishedName(_ context: SSLContext!, _ derDN: UnsafePointer<Void>, _ derDNLen: Int) -> OSStatus ``` | OS X 10.4 |

Modified SSLClose(SSLContext!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLConnectionRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLConnectionRef = ConstUnsafePointer<()> ``` |
| To | ``` typealias SSLConnectionRef = UnsafePointer<Void> ``` |

Modified SSLContextGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SSLCopyCertificateAuthorities(SSLContext!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLCopyCertificateAuthorities(_ context: SSLContext!, _ certificates: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLCopyCertificateAuthorities(_ context: SSLContext!, _ certificates: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified SSLCopyDistinguishedNames(SSLContext!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLCopyDistinguishedNames(_ context: SSLContext!, _ names: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLCopyDistinguishedNames(_ context: SSLContext!, _ names: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified SSLCopyPeerTrust(SSLContext!, UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLCopyPeerTrust(_ context: SSLContext!, _ trust: UnsafePointer<Unmanaged<SecTrust>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLCopyPeerTrust(_ context: SSLContext!, _ trust: UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus ``` | OS X 10.6 |

Modified SSLCreateContext(CFAllocator!, SSLProtocolSide, SSLConnectionType) -> Unmanaged<SSLContext>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SSLGetBufferedReadSize(SSLContext!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetBufferedReadSize(_ context: SSLContext!, _ bufSize: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetBufferedReadSize(_ context: SSLContext!, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetClientCertificateState(SSLContext!, UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetClientCertificateState(_ context: SSLContext!, _ clientState: UnsafePointer<SSLClientCertificateState>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetClientCertificateState(_ context: SSLContext!, _ clientState: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus ``` | OS X 10.3 |

Modified SSLGetConnection(SSLContext!, UnsafeMutablePointer<SSLConnectionRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetConnection(_ context: SSLContext!, _ connection: UnsafePointer<SSLConnectionRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetConnection(_ context: SSLContext!, _ connection: UnsafeMutablePointer<SSLConnectionRef>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetDatagramWriteSize(SSLContext!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetDatagramWriteSize(_ dtlsContext: SSLContext!, _ bufSize: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetDatagramWriteSize(_ dtlsContext: SSLContext!, _ bufSize: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.8 |

Modified SSLGetDiffieHellmanParams(SSLContext!, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetDiffieHellmanParams(_ context: SSLContext!, _ dhParams: UnsafePointer<ConstUnsafePointer<()>>, _ dhParamsLen: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetDiffieHellmanParams(_ context: SSLContext!, _ dhParams: UnsafeMutablePointer<UnsafePointer<Void>>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetEnabledCiphers(SSLContext!, UnsafeMutablePointer<SSLCipherSuite>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetEnabledCiphers(_ context: SSLContext!, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetEnabledCiphers(_ context: SSLContext!, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetMaxDatagramRecordSize(SSLContext!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetMaxDatagramRecordSize(_ dtlsContext: SSLContext!, _ maxSize: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetMaxDatagramRecordSize(_ dtlsContext: SSLContext!, _ maxSize: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.8 |

Modified SSLGetNegotiatedCipher(SSLContext!, UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetNegotiatedCipher(_ context: SSLContext!, _ cipherSuite: UnsafePointer<SSLCipherSuite>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetNegotiatedCipher(_ context: SSLContext!, _ cipherSuite: UnsafeMutablePointer<SSLCipherSuite>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetNegotiatedProtocolVersion(SSLContext!, UnsafeMutablePointer<SSLProtocol>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetNegotiatedProtocolVersion(_ context: SSLContext!, _ `protocol`: UnsafePointer<SSLProtocol>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetNegotiatedProtocolVersion(_ context: SSLContext!, _ `protocol`: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetNumberEnabledCiphers(SSLContext!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetNumberEnabledCiphers(_ context: SSLContext!, _ numCiphers: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetNumberEnabledCiphers(_ context: SSLContext!, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetNumberSupportedCiphers(SSLContext!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetNumberSupportedCiphers(_ context: SSLContext!, _ numCiphers: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetNumberSupportedCiphers(_ context: SSLContext!, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetPeerDomainName(SSLContext!, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetPeerDomainName(_ context: SSLContext!, _ peerName: UnsafePointer<Int8>, _ peerNameLen: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetPeerDomainName(_ context: SSLContext!, _ peerName: UnsafeMutablePointer<Int8>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetPeerDomainNameLength(SSLContext!, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetPeerDomainNameLength(_ context: SSLContext!, _ peerNameLen: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetPeerDomainNameLength(_ context: SSLContext!, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetPeerID(SSLContext!, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetPeerID(_ context: SSLContext!, _ peerID: UnsafePointer<ConstUnsafePointer<()>>, _ peerIDLen: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetPeerID(_ context: SSLContext!, _ peerID: UnsafeMutablePointer<UnsafePointer<Void>>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetProtocolVersionMax(SSLContext!, UnsafeMutablePointer<SSLProtocol>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetProtocolVersionMax(_ context: SSLContext!, _ maxVersion: UnsafePointer<SSLProtocol>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetProtocolVersionMax(_ context: SSLContext!, _ maxVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` | OS X 10.8 |

Modified SSLGetProtocolVersionMin(SSLContext!, UnsafeMutablePointer<SSLProtocol>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetProtocolVersionMin(_ context: SSLContext!, _ minVersion: UnsafePointer<SSLProtocol>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetProtocolVersionMin(_ context: SSLContext!, _ minVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` | OS X 10.8 |

Modified SSLGetSessionOption(SSLContext!, SSLSessionOption, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetSessionOption(_ context: SSLContext!, _ option: SSLSessionOption, _ value: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetSessionOption(_ context: SSLContext!, _ option: SSLSessionOption, _ value: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.6 |

Modified SSLGetSessionState(SSLContext!, UnsafeMutablePointer<SSLSessionState>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetSessionState(_ context: SSLContext!, _ state: UnsafePointer<SSLSessionState>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetSessionState(_ context: SSLContext!, _ state: UnsafeMutablePointer<SSLSessionState>) -> OSStatus ``` | OS X 10.2 |

Modified SSLGetSupportedCiphers(SSLContext!, UnsafeMutablePointer<SSLCipherSuite>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLGetSupportedCiphers(_ context: SSLContext!, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLGetSupportedCiphers(_ context: SSLContext!, _ ciphers: UnsafeMutablePointer<SSLCipherSuite>, _ numCiphers: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLHandshake(SSLContext!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLRead(SSLContext!, UnsafeMutablePointer<Void>, Int, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLRead(_ context: SSLContext!, _ data: UnsafePointer<()>, _ dataLength: UInt, _ processed: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLRead(_ context: SSLContext!, _ data: UnsafeMutablePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLReadFunc

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLReadFunc = CFunctionPointer<((SSLConnectionRef, UnsafePointer<()>, UnsafePointer<UInt>) -> OSStatus)> ``` |
| To | ``` typealias SSLReadFunc = CFunctionPointer<((SSLConnectionRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus)> ``` |

Modified SSLSetCertificate(SSLContext!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLSetCertificateAuthorities(SSLContext!, AnyObject!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SSLSetClientSideAuthenticate(SSLContext!, SSLAuthenticate) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLSetConnection(SSLContext!, SSLConnectionRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLSetDatagramHelloCookie(SSLContext!, UnsafePointer<Void>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext!, _ cookie: ConstUnsafePointer<()>, _ cookieLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext!, _ cookie: UnsafePointer<Void>, _ cookieLen: Int) -> OSStatus ``` | OS X 10.8 |

Modified SSLSetDiffieHellmanParams(SSLContext!, UnsafePointer<Void>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLSetDiffieHellmanParams(_ context: SSLContext!, _ dhParams: ConstUnsafePointer<()>, _ dhParamsLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLSetDiffieHellmanParams(_ context: SSLContext!, _ dhParams: UnsafePointer<Void>, _ dhParamsLen: Int) -> OSStatus ``` | OS X 10.2 |

Modified SSLSetEnabledCiphers(SSLContext!, UnsafePointer<SSLCipherSuite>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLSetEnabledCiphers(_ context: SSLContext!, _ ciphers: ConstUnsafePointer<SSLCipherSuite>, _ numCiphers: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLSetEnabledCiphers(_ context: SSLContext!, _ ciphers: UnsafePointer<SSLCipherSuite>, _ numCiphers: Int) -> OSStatus ``` | OS X 10.2 |

Modified SSLSetEncryptionCertificate(SSLContext!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLSetIOFuncs(SSLContext!, SSLReadFunc, SSLWriteFunc) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SSLSetMaxDatagramRecordSize(SSLContext!, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLSetMaxDatagramRecordSize(_ dtlsContext: SSLContext!, _ maxSize: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLSetMaxDatagramRecordSize(_ dtlsContext: SSLContext!, _ maxSize: Int) -> OSStatus ``` | OS X 10.8 |

Modified SSLSetPeerDomainName(SSLContext!, UnsafePointer<Int8>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLSetPeerDomainName(_ context: SSLContext!, _ peerName: ConstUnsafePointer<Int8>, _ peerNameLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLSetPeerDomainName(_ context: SSLContext!, _ peerName: UnsafePointer<Int8>, _ peerNameLen: Int) -> OSStatus ``` | OS X 10.2 |

Modified SSLSetPeerID(SSLContext!, UnsafePointer<Void>, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLSetPeerID(_ context: SSLContext!, _ peerID: ConstUnsafePointer<()>, _ peerIDLen: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLSetPeerID(_ context: SSLContext!, _ peerID: UnsafePointer<Void>, _ peerIDLen: Int) -> OSStatus ``` | OS X 10.2 |

Modified SSLSetProtocolVersionMax(SSLContext!, SSLProtocol) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SSLSetProtocolVersionMin(SSLContext!, SSLProtocol) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SSLSetSessionOption(SSLContext!, SSLSessionOption, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SSLWrite(SSLContext!, UnsafePointer<Void>, Int, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SSLWrite(_ context: SSLContext!, _ data: ConstUnsafePointer<()>, _ dataLength: UInt, _ processed: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SSLWrite(_ context: SSLContext!, _ data: UnsafePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.2 |

Modified SSLWriteFunc

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLWriteFunc = CFunctionPointer<((SSLConnectionRef, ConstUnsafePointer<()>, UnsafePointer<UInt>) -> OSStatus)> ``` |
| To | ``` typealias SSLWriteFunc = CFunctionPointer<((SSLConnectionRef, UnsafePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus)> ``` |

Modified SecACLCopyAuthorizations(SecACL!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecACLCopyContents(SecACL!, UnsafeMutablePointer<Unmanaged<CFArray>?>, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecACLCopyContents(_ acl: SecACL!, _ applicationList: UnsafePointer<Unmanaged<CFArray>?>, _ description: UnsafePointer<Unmanaged<CFString>?>, _ promptSelector: UnsafePointer<SecKeychainPromptSelector>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecACLCopyContents(_ acl: SecACL!, _ applicationList: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>, _ promptSelector: UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus ``` | OS X 10.7 |

Modified SecACLCreateWithSimpleContents(SecAccess!, CFArray!, CFString!, SecKeychainPromptSelector, UnsafeMutablePointer<Unmanaged<SecACL>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecACLCreateWithSimpleContents(_ access: SecAccess!, _ applicationList: CFArray!, _ description: CFString!, _ promptSelector: SecKeychainPromptSelector, _ newAcl: UnsafePointer<Unmanaged<SecACL>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecACLCreateWithSimpleContents(_ access: SecAccess!, _ applicationList: CFArray!, _ description: CFString!, _ promptSelector: SecKeychainPromptSelector, _ newAcl: UnsafeMutablePointer<Unmanaged<SecACL>?>) -> OSStatus ``` | OS X 10.7 |

Modified SecACLGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecACLRemove(SecACL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecACLSetContents(SecACL!, CFArray!, CFString!, SecKeychainPromptSelector) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecACLUpdateAuthorizations(SecACL!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecAccessControlCreateWithFlags(CFAllocator!, AnyObject!, SecAccessControlCreateFlags, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccessControl>!

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator!, _ protection: AnyObject!, _ flags: SecAccessControlCreateFlags, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccessControl>! ``` |
| To | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator!, _ protection: AnyObject!, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccessControl>! ``` |

Modified SecAccessCopyACLList(SecAccess!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCopyACLList(_ accessRef: SecAccess!, _ aclList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecAccessCopyACLList(_ accessRef: SecAccess!, _ aclList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified SecAccessCopyMatchingACLList(SecAccess!, AnyObject!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecAccessCopyOwnerAndACL(SecAccess!, UnsafeMutablePointer<uid_t>, UnsafeMutablePointer<gid_t>, UnsafeMutablePointer<SecAccessOwnerType>, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess!, _ userId: UnsafePointer<uid_t>, _ groupId: UnsafePointer<gid_t>, _ ownerType: UnsafePointer<SecAccessOwnerType>, _ aclList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess!, _ userId: UnsafeMutablePointer<uid_t>, _ groupId: UnsafeMutablePointer<gid_t>, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>, _ aclList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.7 |

Modified SecAccessCreate(CFString!, CFArray!, UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCreate(_ descriptor: CFString!, _ trustedlist: CFArray!, _ accessRef: UnsafePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |
| To | ``` func SecAccessCreate(_ descriptor: CFString!, _ trustedlist: CFArray!, _ accessRef: UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |

Modified SecAccessCreateWithOwnerAndACL(uid_t, gid_t, SecAccessOwnerType, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccess>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccess>! ``` | OS X 10.10 |
| To | ``` func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccess>! ``` | OS X 10.7 |

Modified SecAsn1TemplateChooser

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1TemplateChooser = (UnsafePointer<()>, Boolean, ConstUnsafePointer<Int8>, UnsafePointer<()>) -> ConstUnsafePointer<SecAsn1Template> ``` |
| To | ``` typealias SecAsn1TemplateChooser = (UnsafeMutablePointer<Void>, Boolean, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> UnsafePointer<SecAsn1Template> ``` |

Modified SecCertificateAddToKeychain(SecCertificate!, SecKeychain!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecCertificateCopyCommonName(SecCertificate!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyCommonName(_ certificate: SecCertificate!, _ commonName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyCommonName(_ certificate: SecCertificate!, _ commonName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified SecCertificateCopyData(SecCertificate!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecCertificateCopyEmailAddresses(SecCertificate!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyEmailAddresses(_ certificate: SecCertificate!, _ emailAddresses: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyEmailAddresses(_ certificate: SecCertificate!, _ emailAddresses: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified SecCertificateCopyLongDescription(CFAllocator!, SecCertificate!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyLongDescription(_ alloc: CFAllocator!, _ certificate: SecCertificate!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyLongDescription(_ alloc: CFAllocator!, _ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>! ``` | OS X 10.7 |

Modified SecCertificateCopyNormalizedIssuerContent(SecCertificate!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.7 |

Modified SecCertificateCopyNormalizedSubjectContent(SecCertificate!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.7 |

Modified SecCertificateCopyPreferred(CFString!, CFArray!) -> Unmanaged<SecCertificate>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecCertificateCopyPublicKey(SecCertificate!, UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyPublicKey(_ certificate: SecCertificate!, _ key: UnsafePointer<Unmanaged<SecKey>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyPublicKey(_ certificate: SecCertificate!, _ key: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` | OS X 10.3 |

Modified SecCertificateCopySerialNumber(SecCertificate!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopySerialNumber(_ certificate: SecCertificate!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func SecCertificateCopySerialNumber(_ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.7 |

Modified SecCertificateCopyShortDescription(CFAllocator!, SecCertificate!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyShortDescription(_ alloc: CFAllocator!, _ certificate: SecCertificate!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyShortDescription(_ alloc: CFAllocator!, _ certificate: SecCertificate!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFString>! ``` | OS X 10.7 |

Modified SecCertificateCopySubjectSummary(SecCertificate!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecCertificateCopyValues(SecCertificate!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCertificateCopyValues(_ certificate: SecCertificate!, _ keys: CFArray!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func SecCertificateCopyValues(_ certificate: SecCertificate!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` | OS X 10.7 |

Modified SecCertificateCreateWithData(CFAllocator!, CFData!) -> Unmanaged<SecCertificate>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecCertificateGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecCertificateSetPreference(SecCertificate!, CFString!, uint32, CFDate!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SecCertificateSetPreferred(SecCertificate!, CFString!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecCodeCheckValidityWithErrors(SecCode!, SecCSFlags, SecRequirement!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCheckValidityWithErrors(_ code: SecCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!, _ errors: UnsafePointer<Unmanaged<CFError>?>) -> OSStatus ``` |
| To | ``` func SecCodeCheckValidityWithErrors(_ code: SecCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |

Modified SecCodeCopyDesignatedRequirement(SecStaticCode!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyDesignatedRequirement(_ code: SecStaticCode!, _ flags: SecCSFlags, _ requirement: UnsafePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyDesignatedRequirement(_ code: SecStaticCode!, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |

Modified SecCodeCopyGuestWithAttributes(SecCode!, CFDictionary!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyGuestWithAttributes(_ host: SecCode!, _ attributes: CFDictionary!, _ flags: SecCSFlags, _ guest: UnsafePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyGuestWithAttributes(_ host: SecCode!, _ attributes: CFDictionary!, _ flags: SecCSFlags, _ guest: UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |

Modified SecCodeCopyHost(SecCode!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyHost(_ guest: SecCode!, _ flags: SecCSFlags, _ host: UnsafePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyHost(_ guest: SecCode!, _ flags: SecCSFlags, _ host: UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |

Modified SecCodeCopyPath(SecStaticCode!, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyPath(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ path: UnsafePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyPath(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ path: UnsafeMutablePointer<Unmanaged<CFURL>?>) -> OSStatus ``` |

Modified SecCodeCopySelf(SecCSFlags, UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopySelf(_ flags: SecCSFlags, _ `self`: UnsafePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopySelf(_ flags: SecCSFlags, _ `self`: UnsafeMutablePointer<Unmanaged<SecCode>?>) -> OSStatus ``` |

Modified SecCodeCopySigningInformation(SecStaticCode!, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopySigningInformation(_ code: SecStaticCode!, _ flags: SecCSFlags, _ information: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopySigningInformation(_ code: SecStaticCode!, _ flags: SecCSFlags, _ information: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |

Modified SecCodeCopyStaticCode(SecCode!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopyStaticCode(_ code: SecCode!, _ flags: SecCSFlags, _ staticCode: UnsafePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |
| To | ``` func SecCodeCopyStaticCode(_ code: SecCode!, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |

Modified SecCopyErrorMessageString(OSStatus, UnsafeMutablePointer<Void>) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafePointer<()>) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutablePointer<Void>) -> Unmanaged<CFString>! ``` | OS X 10.3 |

Modified SecDecodeTransformCreate(AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecDecodeTransformCreate(_ DecodeType: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecDecodeTransformCreate(_ DecodeType: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecDecryptTransformCreate(SecKey!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecDecryptTransformCreate(_ keyRef: SecKey!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecDecryptTransformCreate(_ keyRef: SecKey!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecDecryptTransformGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecDigestTransformCreate(AnyObject!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecDigestTransformCreate(_ digestType: AnyObject!, _ digestLength: CFIndex, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecDigestTransformCreate(_ digestType: AnyObject!, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecDigestTransformGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecEncodeTransformCreate(AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecEncodeTransformCreate(_ encodeType: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecEncodeTransformCreate(_ encodeType: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecEncryptTransformCreate(SecKey!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecEncryptTransformCreate(_ keyRef: SecKey!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecEncryptTransformCreate(_ keyRef: SecKey!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecEncryptTransformGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecGroupTransformRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecGroupTransformRef = AnyObject ``` |
| To | ``` typealias SecGroupTransformRef = SecGroupTransform ``` |

Modified SecHostCreateGuest(SecGuestRef, UInt32, CFURL!, CFDictionary!, SecCSFlags, UnsafeMutablePointer<SecGuestRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecHostCreateGuest(_ host: SecGuestRef, _ status: UInt32, _ path: CFURL!, _ attributes: CFDictionary!, _ flags: SecCSFlags, _ newGuest: UnsafePointer<SecGuestRef>) -> OSStatus ``` |
| To | ``` func SecHostCreateGuest(_ host: SecGuestRef, _ status: UInt32, _ path: CFURL!, _ attributes: CFDictionary!, _ flags: SecCSFlags, _ newGuest: UnsafeMutablePointer<SecGuestRef>) -> OSStatus ``` |

Modified SecHostSelectedGuest(SecCSFlags, UnsafeMutablePointer<SecGuestRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecHostSelectedGuest(_ flags: SecCSFlags, _ guestRef: UnsafePointer<SecGuestRef>) -> OSStatus ``` |
| To | ``` func SecHostSelectedGuest(_ flags: SecCSFlags, _ guestRef: UnsafeMutablePointer<SecGuestRef>) -> OSStatus ``` |

Modified SecIdentityCopyCertificate(SecIdentity!, UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecIdentityCopyCertificate(_ identityRef: SecIdentity!, _ certificateRef: UnsafePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecIdentityCopyCertificate(_ identityRef: SecIdentity!, _ certificateRef: UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` | OS X 10.3 |

Modified SecIdentityCopyPreferred(CFString!, CFArray!, CFArray!) -> Unmanaged<SecIdentity>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecIdentityCopyPrivateKey(SecIdentity!, UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity!, _ privateKeyRef: UnsafePointer<Unmanaged<SecKey>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity!, _ privateKeyRef: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` | OS X 10.3 |

Modified SecIdentityCopySystemIdentity(CFString!, UnsafeMutablePointer<Unmanaged<SecIdentity>?>, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecIdentityCopySystemIdentity(_ domain: CFString!, _ idRef: UnsafePointer<Unmanaged<SecIdentity>?>, _ actualDomain: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecIdentityCopySystemIdentity(_ domain: CFString!, _ idRef: UnsafeMutablePointer<Unmanaged<SecIdentity>?>, _ actualDomain: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified SecIdentityCreateWithCertificate(AnyObject!, SecCertificate!, UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecIdentityCreateWithCertificate(_ keychainOrArray: AnyObject!, _ certificateRef: SecCertificate!, _ identityRef: UnsafePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecIdentityCreateWithCertificate(_ keychainOrArray: AnyObject!, _ certificateRef: SecCertificate!, _ identityRef: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` | OS X 10.5 |

Modified SecIdentityGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecIdentitySetPreferred(SecIdentity!, CFString!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecIdentitySetSystemIdentity(CFString!, SecIdentity!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SecItemAdd(CFDictionary!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecItemAdd(_ attributes: CFDictionary!, _ result: UnsafePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecItemAdd(_ attributes: CFDictionary!, _ result: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.6 |

Modified SecItemCopyMatching(CFDictionary!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecItemCopyMatching(_ query: CFDictionary!, _ result: UnsafePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecItemCopyMatching(_ query: CFDictionary!, _ result: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` | OS X 10.6 |

Modified SecItemDelete(CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecItemExport(AnyObject!, SecExternalFormat, SecItemImportExportFlags, UnsafePointer<SecItemImportExportKeyParameters>, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecItemExport(_ secItemOrArray: AnyObject!, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: ConstUnsafePointer<SecItemImportExportKeyParameters>, _ exportedData: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecItemExport(_ secItemOrArray: AnyObject!, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ exportedData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.7 |

Modified SecItemImport(CFData!, CFString!, UnsafeMutablePointer<SecExternalFormat>, UnsafeMutablePointer<SecExternalItemType>, SecItemImportExportFlags, UnsafePointer<SecItemImportExportKeyParameters>, SecKeychain!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecItemImport(_ importedData: CFData!, _ fileNameOrExtension: CFString!, _ inputFormat: UnsafePointer<SecExternalFormat>, _ itemType: UnsafePointer<SecExternalItemType>, _ flags: SecItemImportExportFlags, _ keyParams: ConstUnsafePointer<SecItemImportExportKeyParameters>, _ importKeychain: SecKeychain!, _ outItems: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecItemImport(_ importedData: CFData!, _ fileNameOrExtension: CFString!, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>, _ itemType: UnsafeMutablePointer<SecExternalItemType>, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ importKeychain: SecKeychain!, _ outItems: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.7 |

Modified SecItemUpdate(CFDictionary!, CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecKeyCreateFromData(CFDictionary!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyCreateFromData(_ parameters: CFDictionary!, _ keyData: CFData!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.10 |
| To | ``` func SecKeyCreateFromData(_ parameters: CFDictionary!, _ keyData: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.7 |

Modified SecKeyDeriveFromPassword(CFString!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyDeriveFromPassword(_ password: CFString!, _ parameters: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.10 |
| To | ``` func SecKeyDeriveFromPassword(_ password: CFString!, _ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.7 |

Modified SecKeyGeneratePair(CFDictionary!, UnsafeMutablePointer<Unmanaged<SecKey>?>, UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyGeneratePair(_ parameters: CFDictionary!, _ publicKey: UnsafePointer<Unmanaged<SecKey>?>, _ privateKey: UnsafePointer<Unmanaged<SecKey>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecKeyGeneratePair(_ parameters: CFDictionary!, _ publicKey: UnsafeMutablePointer<Unmanaged<SecKey>?>, _ privateKey: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` | OS X 10.7 |

Modified SecKeyGeneratePairAsync(CFDictionary!, dispatch_queue_t!, SecKeyGeneratePairBlock!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecKeyGenerateSymmetric(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyGenerateSymmetric(_ parameters: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.10 |
| To | ``` func SecKeyGenerateSymmetric(_ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.7 |

Modified SecKeyGetBlockSize(SecKey!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyGetBlockSize(_ key: SecKey!) -> UInt ``` | OS X 10.10 |
| To | ``` func SecKeyGetBlockSize(_ key: SecKey!) -> Int ``` | OS X 10.6 |

Modified SecKeyGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecKeyUnwrapSymmetric(UnsafeMutablePointer<Unmanaged<CFData>?>, SecKey!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey!, _ parameters: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.10 |
| To | ``` func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey!, _ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecKey>! ``` | OS X 10.7 |

Modified SecKeyWrapSymmetric(SecKey!, SecKey!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecKeyWrapSymmetric(_ keyToWrap: SecKey!, _ wrappingKey: SecKey!, _ parameters: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func SecKeyWrapSymmetric(_ keyToWrap: SecKey!, _ wrappingKey: SecKey!, _ parameters: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFData>! ``` | OS X 10.7 |

Modified SecKeychainAddCallback(SecKeychainCallback, SecKeychainEventMask, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddCallback(_ callbackFunction: SecKeychainCallback, _ eventMask: SecKeychainEventMask, _ userContext: UnsafePointer<()>) -> OSStatus ``` |
| To | ``` func SecKeychainAddCallback(_ callbackFunction: SecKeychainCallback, _ eventMask: SecKeychainEventMask, _ userContext: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified SecKeychainAddGenericPassword(SecKeychain!, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddGenericPassword(_ keychain: SecKeychain!, _ serviceNameLength: UInt32, _ serviceName: ConstUnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: ConstUnsafePointer<Int8>, _ passwordLength: UInt32, _ passwordData: ConstUnsafePointer<()>, _ itemRef: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddGenericPassword(_ keychain: SecKeychain!, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainAddInternetPassword(SecKeychain!, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt16, SecProtocolType, SecAuthenticationType, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain!, _ serverNameLength: UInt32, _ serverName: ConstUnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: ConstUnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: ConstUnsafePointer<Int8>, _ pathLength: UInt32, _ path: ConstUnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: ConstUnsafePointer<()>, _ itemRef: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain!, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainAttributeInfoForItemID(SecKeychain!, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain!, _ itemID: UInt32, _ info: UnsafePointer<UnsafePointer<SecKeychainAttributeInfo>>) -> OSStatus ``` |
| To | ``` func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain!, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>>) -> OSStatus ``` |

Modified SecKeychainAttributePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias SecKeychainAttributePtr = UnsafePointer<SecKeychainAttribute> ``` |
| To | ``` typealias SecKeychainAttributePtr = UnsafeMutablePointer<SecKeychainAttribute> ``` |

Modified SecKeychainCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias SecKeychainCallback = CFunctionPointer<((SecKeychainEvent, UnsafePointer<SecKeychainCallbackInfo>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias SecKeychainCallback = CFunctionPointer<((SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified SecKeychainCopyAccess(SecKeychain!, UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyAccess(_ keychain: SecKeychain!, _ access: UnsafePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyAccess(_ keychain: SecKeychain!, _ access: UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |

Modified SecKeychainCopyDefault(UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyDefault(_ keychain: UnsafePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyDefault(_ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |

Modified SecKeychainCopyDomainDefault(SecPreferencesDomain, UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyDomainDefault(_ domain: SecPreferencesDomain, _ keychain: UnsafePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyDomainDefault(_ domain: SecPreferencesDomain, _ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |

Modified SecKeychainCopyDomainSearchList(SecPreferencesDomain, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopyDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopyDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified SecKeychainCopySearchList(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopySearchList(_ searchList: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCopySearchList(_ searchList: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified SecKeychainCopySettings(SecKeychain!, UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCopySettings(_ keychain: SecKeychain!, _ outSettings: UnsafePointer<SecKeychainSettings>) -> OSStatus ``` |
| To | ``` func SecKeychainCopySettings(_ keychain: SecKeychain!, _ outSettings: UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus ``` |

Modified SecKeychainCreate(UnsafePointer<Int8>, UInt32, UnsafePointer<Void>, Boolean, SecAccess!, UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCreate(_ pathName: ConstUnsafePointer<Int8>, _ passwordLength: UInt32, _ password: ConstUnsafePointer<()>, _ promptUser: Boolean, _ initialAccess: SecAccess!, _ keychain: UnsafePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainCreate(_ pathName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ promptUser: Boolean, _ initialAccess: SecAccess!, _ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |

Modified SecKeychainFindGenericPassword(AnyObject!, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindGenericPassword(_ keychainOrArray: AnyObject!, _ serviceNameLength: UInt32, _ serviceName: ConstUnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: ConstUnsafePointer<Int8>, _ passwordLength: UnsafePointer<UInt32>, _ passwordData: UnsafePointer<UnsafePointer<()>>, _ itemRef: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindGenericPassword(_ keychainOrArray: AnyObject!, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainFindInternetPassword(AnyObject!, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt32, UnsafePointer<Int8>, UInt16, SecProtocolType, SecAuthenticationType, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject!, _ serverNameLength: UInt32, _ serverName: ConstUnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: ConstUnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: ConstUnsafePointer<Int8>, _ pathLength: UInt32, _ path: ConstUnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafePointer<UInt32>, _ passwordData: UnsafePointer<UnsafePointer<()>>, _ itemRef: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject!, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainFreeAttributeInfo(UnsafeMutablePointer<SecKeychainAttributeInfo>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFreeAttributeInfo(_ info: UnsafePointer<SecKeychainAttributeInfo>) -> OSStatus ``` |
| To | ``` func SecKeychainFreeAttributeInfo(_ info: UnsafeMutablePointer<SecKeychainAttributeInfo>) -> OSStatus ``` |

Modified SecKeychainGetPath(SecKeychain!, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Int8>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetPath(_ keychain: SecKeychain!, _ ioPathLength: UnsafePointer<UInt32>, _ pathName: UnsafePointer<Int8>) -> OSStatus ``` |
| To | ``` func SecKeychainGetPath(_ keychain: SecKeychain!, _ ioPathLength: UnsafeMutablePointer<UInt32>, _ pathName: UnsafeMutablePointer<Int8>) -> OSStatus ``` |

Modified SecKeychainGetPreferenceDomain(UnsafeMutablePointer<SecPreferencesDomain>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetPreferenceDomain(_ domain: UnsafePointer<SecPreferencesDomain>) -> OSStatus ``` |
| To | ``` func SecKeychainGetPreferenceDomain(_ domain: UnsafeMutablePointer<SecPreferencesDomain>) -> OSStatus ``` |

Modified SecKeychainGetStatus(SecKeychain!, UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetStatus(_ keychain: SecKeychain!, _ keychainStatus: UnsafePointer<SecKeychainStatus>) -> OSStatus ``` |
| To | ``` func SecKeychainGetStatus(_ keychain: SecKeychain!, _ keychainStatus: UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus ``` |

Modified SecKeychainGetUserInteractionAllowed(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetUserInteractionAllowed(_ state: UnsafePointer<Boolean>) -> OSStatus ``` |
| To | ``` func SecKeychainGetUserInteractionAllowed(_ state: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |

Modified SecKeychainGetVersion(UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainGetVersion(_ returnVers: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func SecKeychainGetVersion(_ returnVers: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified SecKeychainItemCopyAccess(SecKeychainItem!, UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyAccess(_ itemRef: SecKeychainItem!, _ access: UnsafePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyAccess(_ itemRef: SecKeychainItem!, _ access: UnsafeMutablePointer<Unmanaged<SecAccess>?>) -> OSStatus ``` |

Modified SecKeychainItemCopyAttributesAndData(SecKeychainItem!, UnsafeMutablePointer<SecKeychainAttributeInfo>, UnsafeMutablePointer<SecItemClass>, UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem!, _ info: UnsafePointer<SecKeychainAttributeInfo>, _ itemClass: UnsafePointer<SecItemClass>, _ attrList: UnsafePointer<UnsafePointer<SecKeychainAttributeList>>, _ length: UnsafePointer<UInt32>, _ outData: UnsafePointer<UnsafePointer<()>>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem!, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |

Modified SecKeychainItemCopyContent(SecKeychainItem!, UnsafeMutablePointer<SecItemClass>, UnsafeMutablePointer<SecKeychainAttributeList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem!, _ itemClass: UnsafePointer<SecItemClass>, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UnsafePointer<UInt32>, _ outData: UnsafePointer<UnsafePointer<()>>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem!, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |

Modified SecKeychainItemCopyFromPersistentReference(CFData!, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyFromPersistentReference(_ persistentItemRef: CFData!, _ itemRef: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyFromPersistentReference(_ persistentItemRef: CFData!, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainItemCopyKeychain(SecKeychainItem!, UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyKeychain(_ itemRef: SecKeychainItem!, _ keychainRef: UnsafePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyKeychain(_ itemRef: SecKeychainItem!, _ keychainRef: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |

Modified SecKeychainItemCreateCopy(SecKeychainItem!, SecKeychain!, SecAccess!, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem!, _ destKeychainRef: SecKeychain!, _ initialAccess: SecAccess!, _ itemCopy: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem!, _ destKeychainRef: SecKeychain!, _ initialAccess: SecAccess!, _ itemCopy: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainItemCreateFromContent(SecItemClass, UnsafeMutablePointer<SecKeychainAttributeList>, UInt32, UnsafePointer<Void>, SecKeychain!, SecAccess!, UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: ConstUnsafePointer<()>, _ keychainRef: SecKeychain!, _ initialAccess: SecAccess!, _ itemRef: UnsafePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>, _ keychainRef: SecKeychain!, _ initialAccess: SecAccess!, _ itemRef: UnsafeMutablePointer<Unmanaged<SecKeychainItem>?>) -> OSStatus ``` |

Modified SecKeychainItemCreatePersistentReference(SecKeychainItem!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreatePersistentReference(_ itemRef: SecKeychainItem!, _ persistentItemRef: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreatePersistentReference(_ itemRef: SecKeychainItem!, _ persistentItemRef: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified SecKeychainItemFreeAttributesAndData(UnsafeMutablePointer<SecKeychainAttributeList>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemFreeAttributesAndData(_ attrList: UnsafePointer<SecKeychainAttributeList>, _ data: UnsafePointer<()>) -> OSStatus ``` |
| To | ``` func SecKeychainItemFreeAttributesAndData(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ data: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified SecKeychainItemFreeContent(UnsafeMutablePointer<SecKeychainAttributeList>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemFreeContent(_ attrList: UnsafePointer<SecKeychainAttributeList>, _ data: UnsafePointer<()>) -> OSStatus ``` |
| To | ``` func SecKeychainItemFreeContent(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ data: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified SecKeychainItemModifyAttributesAndData(SecKeychainItem!, UnsafePointer<SecKeychainAttributeList>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem!, _ attrList: ConstUnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: ConstUnsafePointer<()>) -> OSStatus ``` |
| To | ``` func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem!, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |

Modified SecKeychainItemModifyContent(SecKeychainItem!, UnsafePointer<SecKeychainAttributeList>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem!, _ attrList: ConstUnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: ConstUnsafePointer<()>) -> OSStatus ``` |
| To | ``` func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem!, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |

Modified SecKeychainOpen(UnsafePointer<Int8>, UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainOpen(_ pathName: ConstUnsafePointer<Int8>, _ keychain: UnsafePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |
| To | ``` func SecKeychainOpen(_ pathName: UnsafePointer<Int8>, _ keychain: UnsafeMutablePointer<Unmanaged<SecKeychain>?>) -> OSStatus ``` |

Modified SecKeychainSetSettings(SecKeychain!, UnsafePointer<SecKeychainSettings>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainSetSettings(_ keychain: SecKeychain!, _ newSettings: ConstUnsafePointer<SecKeychainSettings>) -> OSStatus ``` |
| To | ``` func SecKeychainSetSettings(_ keychain: SecKeychain!, _ newSettings: UnsafePointer<SecKeychainSettings>) -> OSStatus ``` |

Modified SecKeychainUnlock(SecKeychain!, UInt32, UnsafePointer<Void>, Boolean) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainUnlock(_ keychain: SecKeychain!, _ passwordLength: UInt32, _ password: ConstUnsafePointer<()>, _ usePassword: Boolean) -> OSStatus ``` |
| To | ``` func SecKeychainUnlock(_ keychain: SecKeychain!, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ usePassword: Boolean) -> OSStatus ``` |

Modified SecPKCS12Import(CFData!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecPKCS12Import(_ pkcs12_data: CFData!, _ options: CFDictionary!, _ items: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecPKCS12Import(_ pkcs12_data: CFData!, _ options: CFDictionary!, _ items: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified SecPolicyCopyProperties(SecPolicy!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecPolicyCreateBasicX509() -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecPolicyCreateRevocation(CFOptionFlags) -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecPolicyCreateSSL(Boolean, CFString!) -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecPolicyCreateWithProperties(AnyObject!, CFDictionary!) -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecPolicyGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecRandomCopyBytes(SecRandomRef, Int, UnsafeMutablePointer<UInt8>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecRandomCopyBytes(_ rnd: SecRandom!, _ count: UInt, _ bytes: UnsafePointer<UInt8>) -> Int32 ``` | OS X 10.10 |
| To | ``` func SecRandomCopyBytes(_ rnd: SecRandomRef, _ count: Int, _ bytes: UnsafeMutablePointer<UInt8>) -> Int32 ``` | OS X 10.7 |

Modified SecRandomRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecRandomRef = SecRandom ``` |
| To | ``` typealias SecRandomRef = COpaquePointer ``` |

Modified SecRequirementCopyData(SecRequirement!, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCopyData(_ requirement: SecRequirement!, _ flags: SecCSFlags, _ data: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCopyData(_ requirement: SecRequirement!, _ flags: SecCSFlags, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified SecRequirementCopyString(SecRequirement!, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCopyString(_ requirement: SecRequirement!, _ flags: SecCSFlags, _ text: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCopyString(_ requirement: SecRequirement!, _ flags: SecCSFlags, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |

Modified SecRequirementCreateWithData(CFData!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithData(_ data: CFData!, _ flags: SecCSFlags, _ requirement: UnsafePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithData(_ data: CFData!, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |

Modified SecRequirementCreateWithString(CFString!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithString(_ text: CFString!, _ flags: SecCSFlags, _ requirement: UnsafePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithString(_ text: CFString!, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |

Modified SecRequirementCreateWithStringAndErrors(CFString!, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFError>?>, UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithStringAndErrors(_ text: CFString!, _ flags: SecCSFlags, _ errors: UnsafePointer<Unmanaged<CFError>?>, _ requirement: UnsafePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithStringAndErrors(_ text: CFString!, _ flags: SecCSFlags, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>, _ requirement: UnsafeMutablePointer<Unmanaged<SecRequirement>?>) -> OSStatus ``` |

Modified SecSignTransformCreate(SecKey!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecSignTransformCreate(_ key: SecKey!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecSignTransformCreate(_ key: SecKey!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecStaticCodeCheckValidityWithErrors(SecStaticCode!, SecCSFlags, SecRequirement!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!, _ errors: UnsafePointer<Unmanaged<CFError>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode!, _ flags: SecCSFlags, _ requirement: SecRequirement!, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |

Modified SecStaticCodeCreateWithPath(CFURL!, SecCSFlags, UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCreateWithPath(_ path: CFURL!, _ flags: SecCSFlags, _ staticCode: UnsafePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCreateWithPath(_ path: CFURL!, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |

Modified SecStaticCodeCreateWithPathAndAttributes(CFURL!, SecCSFlags, CFDictionary!, UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCreateWithPathAndAttributes(_ path: CFURL!, _ flags: SecCSFlags, _ attributes: CFDictionary!, _ staticCode: UnsafePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCreateWithPathAndAttributes(_ path: CFURL!, _ flags: SecCSFlags, _ attributes: CFDictionary!, _ staticCode: UnsafeMutablePointer<Unmanaged<SecStaticCode>?>) -> OSStatus ``` |

Modified SecTaskCopyValueForEntitlement(SecTask!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<AnyObject>!

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCopyValueForEntitlement(_ task: SecTask!, _ entitlement: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<AnyObject>! ``` |
| To | ``` func SecTaskCopyValueForEntitlement(_ task: SecTask!, _ entitlement: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<AnyObject>! ``` |

Modified SecTaskCopyValuesForEntitlements(SecTask!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCopyValuesForEntitlements(_ task: SecTask!, _ entitlements: CFArray!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SecTaskCopyValuesForEntitlements(_ task: SecTask!, _ entitlements: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified SecTransformAttributeActionBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformAttributeActionBlock = (SecTransformAttributeRef!, AnyObject!) -> Unmanaged<AnyObject>! ``` |
| To | ``` typealias SecTransformAttributeActionBlock = (SecTransformAttribute!, AnyObject!) -> Unmanaged<AnyObject>! ``` |

Modified SecTransformAttributeRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformAttributeRef = AnyObject ``` |
| To | ``` typealias SecTransformAttributeRef = SecTransformAttribute ``` |

Modified SecTransformConnectTransforms(SecTransform!, CFString!, SecTransform!, CFString!, SecGroupTransform!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecGroupTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformConnectTransforms(_ sourceTransformRef: SecTransformRef!, _ sourceAttributeName: CFString!, _ destinationTransformRef: SecTransformRef!, _ destinationAttributeName: CFString!, _ group: SecGroupTransformRef!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecGroupTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecTransformConnectTransforms(_ sourceTransformRef: SecTransform!, _ sourceAttributeName: CFString!, _ destinationTransformRef: SecTransform!, _ destinationAttributeName: CFString!, _ group: SecGroupTransform!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecGroupTransform>! ``` | OS X 10.7 |

Modified SecTransformCopyExternalRepresentation(SecTransform!) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformCopyExternalRepresentation(_ transformRef: SecTransformRef!) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func SecTransformCopyExternalRepresentation(_ transformRef: SecTransform!) -> Unmanaged<CFDictionary>! ``` | OS X 10.7 |

Modified SecTransformCreate(CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformCreate(_ name: CFString!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecTransformCreate(_ name: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecTransformCreateFP

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformCreateFP = CFunctionPointer<((CFString!, SecTransformRef!, SecTransformImplementation!) -> SecTransformInstanceBlock!)> ``` |
| To | ``` typealias SecTransformCreateFP = CFunctionPointer<((CFString!, SecTransform!, SecTransformImplementationRef) -> SecTransformInstanceBlock!)> ``` |

Modified SecTransformCreateFromExternalRepresentation(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecTransformCreateGroupTransform() -> Unmanaged<SecGroupTransform>!

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreateGroupTransform() -> Unmanaged<SecGroupTransformRef>! ``` |
| To | ``` func SecTransformCreateGroupTransform() -> Unmanaged<SecGroupTransform>! ``` |

Modified SecTransformCreateReadTransformWithReadStream(CFReadStream!) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream!) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream!) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecTransformCustomGetAttribute(SecTransformImplementationRef, SecTransformStringOrAttribute!, SecTransformMetaAttributeType) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformCustomGetAttribute(_ ref: SecTransformImplementation!, _ attribute: SecTransformStringOrAttributeRef!, _ type: SecTransformMetaAttributeType) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute!, _ type: SecTransformMetaAttributeType) -> Unmanaged<AnyObject>! ``` | OS X 10.10.3 |

Modified SecTransformCustomSetAttribute(SecTransformImplementationRef, SecTransformStringOrAttribute!, SecTransformMetaAttributeType, AnyObject!) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformCustomSetAttribute(_ ref: SecTransformImplementation!, _ attribute: SecTransformStringOrAttributeRef!, _ type: SecTransformMetaAttributeType, _ value: AnyObject!) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute!, _ type: SecTransformMetaAttributeType, _ value: AnyObject!) -> Unmanaged<AnyObject>! ``` | OS X 10.10.3 |

Modified SecTransformExecute(SecTransform!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformExecute(_ transformRef: SecTransformRef!, _ errorRef: UnsafePointer<Unmanaged<CFError>?>) -> AnyObject! ``` | OS X 10.10 |
| To | ``` func SecTransformExecute(_ transformRef: SecTransform!, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject! ``` | OS X 10.7 |

Modified SecTransformExecuteAsync(SecTransform!, dispatch_queue_t!, SecMessageBlock!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformExecuteAsync(_ transformRef: SecTransformRef!, _ deliveryQueue: dispatch_queue_t!, _ deliveryBlock: SecMessageBlock!) ``` | OS X 10.10 |
| To | ``` func SecTransformExecuteAsync(_ transformRef: SecTransform!, _ deliveryQueue: dispatch_queue_t!, _ deliveryBlock: SecMessageBlock!) ``` | OS X 10.7 |

Modified SecTransformFindByName(SecGroupTransform!, CFString!) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformFindByName(_ transform: SecGroupTransformRef!, _ name: CFString!) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecTransformFindByName(_ transform: SecGroupTransform!, _ name: CFString!) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified SecTransformGetAttribute(SecTransform!, CFString!) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformGetAttribute(_ transformRef: SecTransformRef!, _ key: CFString!) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func SecTransformGetAttribute(_ transformRef: SecTransform!, _ key: CFString!) -> Unmanaged<AnyObject>! ``` | OS X 10.7 |

Modified SecTransformImplementationRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformImplementationRef = SecTransformImplementation ``` |
| To | ``` typealias SecTransformImplementationRef = COpaquePointer ``` |

Modified SecTransformPushbackAttribute(SecTransformImplementationRef, SecTransformStringOrAttribute!, AnyObject!) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformPushbackAttribute(_ ref: SecTransformImplementation!, _ attribute: SecTransformStringOrAttributeRef!, _ value: AnyObject!) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute!, _ value: AnyObject!) -> Unmanaged<AnyObject>! ``` | OS X 10.10.3 |

Modified SecTransformRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformRef = AnyObject ``` |
| To | ``` typealias SecTransformRef = SecTransform ``` |

Modified SecTransformRegister(CFString!, SecTransformCreateFP, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformRegister(_ uniqueName: CFString!, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SecTransformRegister(_ uniqueName: CFString!, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.7 |

Modified SecTransformSetAttribute(SecTransform!, CFString!, AnyObject!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformSetAttribute(_ transformRef: SecTransformRef!, _ key: CFString!, _ value: AnyObject!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SecTransformSetAttribute(_ transformRef: SecTransform!, _ key: CFString!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Boolean ``` | OS X 10.7 |

Modified SecTransformSetAttributeAction(SecTransformImplementationRef, CFString!, SecTransformStringOrAttribute!, SecTransformAttributeActionBlock!) -> Unmanaged<CFError>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformSetAttributeAction(_ ref: SecTransformImplementation!, _ action: CFString!, _ attribute: SecTransformStringOrAttributeRef!, _ newAction: SecTransformAttributeActionBlock!) -> Unmanaged<CFError>! ``` | OS X 10.10 |
| To | ``` func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString!, _ attribute: SecTransformStringOrAttribute!, _ newAction: SecTransformAttributeActionBlock!) -> Unmanaged<CFError>! ``` | OS X 10.10.3 |

Modified SecTransformSetDataAction(SecTransformImplementationRef, CFString!, SecTransformDataBlock!) -> Unmanaged<CFError>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformSetDataAction(_ ref: SecTransformImplementation!, _ action: CFString!, _ newAction: SecTransformDataBlock!) -> Unmanaged<CFError>! ``` | OS X 10.10 |
| To | ``` func SecTransformSetDataAction(_ ref: SecTransformImplementationRef, _ action: CFString!, _ newAction: SecTransformDataBlock!) -> Unmanaged<CFError>! ``` | OS X 10.10.3 |

Modified SecTransformSetTransformAction(SecTransformImplementationRef, CFString!, SecTransformActionBlock!) -> Unmanaged<CFError>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTransformSetTransformAction(_ ref: SecTransformImplementation!, _ action: CFString!, _ newAction: SecTransformActionBlock!) -> Unmanaged<CFError>! ``` | OS X 10.10 |
| To | ``` func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString!, _ newAction: SecTransformActionBlock!) -> Unmanaged<CFError>! ``` | OS X 10.10.3 |

Modified SecTransformStringOrAttributeRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformStringOrAttributeRef = AnyObject ``` |
| To | ``` typealias SecTransformStringOrAttributeRef = SecTransformStringOrAttribute ``` |

Modified SecTrustCopyAnchorCertificates(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustCopyAnchorCertificates(_ anchors: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustCopyAnchorCertificates(_ anchors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified SecTrustCopyCustomAnchorCertificates(SecTrust!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustCopyCustomAnchorCertificates(_ trust: SecTrust!, _ anchors: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustCopyCustomAnchorCertificates(_ trust: SecTrust!, _ anchors: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.5 |

Modified SecTrustCopyExceptions(SecTrust!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecTrustCopyPolicies(SecTrust!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustCopyPolicies(_ trust: SecTrust!, _ policies: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustCopyPolicies(_ trust: SecTrust!, _ policies: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.3 |

Modified SecTrustCopyProperties(SecTrust!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecTrustCopyPublicKey(SecTrust!) -> Unmanaged<SecKey>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecTrustCopyResult(SecTrust!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecTrustCreateWithCertificates(AnyObject!, AnyObject!, UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustCreateWithCertificates(_ certificates: AnyObject!, _ policies: AnyObject!, _ trust: UnsafePointer<Unmanaged<SecTrust>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustCreateWithCertificates(_ certificates: AnyObject!, _ policies: AnyObject!, _ trust: UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus ``` | OS X 10.3 |

Modified SecTrustEvaluate(SecTrust!, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustEvaluate(_ trust: SecTrust!, _ result: UnsafePointer<SecTrustResultType>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustEvaluate(_ trust: SecTrust!, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` | OS X 10.3 |

Modified SecTrustEvaluateAsync(SecTrust!, dispatch_queue_t!, SecTrustCallback!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecTrustGetCertificateAtIndex(SecTrust!, CFIndex) -> Unmanaged<SecCertificate>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecTrustGetCertificateCount(SecTrust!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecTrustGetNetworkFetchAllowed(SecTrust!, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustGetNetworkFetchAllowed(_ trust: SecTrust!, _ allowFetch: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustGetNetworkFetchAllowed(_ trust: SecTrust!, _ allowFetch: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.9 |

Modified SecTrustGetTrustResult(SecTrust!, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecTrustGetTrustResult(_ trust: SecTrust!, _ result: UnsafePointer<SecTrustResultType>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func SecTrustGetTrustResult(_ trust: SecTrust!, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` | OS X 10.7 |

Modified SecTrustGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecTrustGetVerifyTime(SecTrust!) -> CFAbsoluteTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecTrustSetAnchorCertificates(SecTrust!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecTrustSetAnchorCertificatesOnly(SecTrust!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SecTrustSetExceptions(SecTrust!, CFData!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecTrustSetKeychains(SecTrust!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecTrustSetNetworkFetchAllowed(SecTrust!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecTrustSetOCSPResponse(SecTrust!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SecTrustSetOptions(SecTrust!, SecTrustOptionFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SecTrustSetPolicies(SecTrust!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecTrustSetVerifyDate(SecTrust!, CFDate!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SecTrustSettingsCopyCertificates(SecTrustSettingsDomain, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified SecTrustSettingsCopyModificationDate(SecCertificate!, SecTrustSettingsDomain, UnsafeMutablePointer<Unmanaged<CFDate>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyModificationDate(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ modificationDate: UnsafePointer<Unmanaged<CFDate>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyModificationDate(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ modificationDate: UnsafeMutablePointer<Unmanaged<CFDate>?>) -> OSStatus ``` |

Modified SecTrustSettingsCopyTrustSettings(SecCertificate!, SecTrustSettingsDomain, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyTrustSettings(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ trustSettings: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyTrustSettings(_ certRef: SecCertificate!, _ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified SecTrustSettingsCreateExternalRepresentation(SecTrustSettingsDomain, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCreateExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCreateExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified SecTrustedApplicationCopyData(SecTrustedApplication!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustedApplicationCopyData(_ appRef: SecTrustedApplication!, _ data: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func SecTrustedApplicationCopyData(_ appRef: SecTrustedApplication!, _ data: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified SecTrustedApplicationCreateFromPath(UnsafePointer<Int8>, UnsafeMutablePointer<Unmanaged<SecTrustedApplication>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustedApplicationCreateFromPath(_ path: ConstUnsafePointer<Int8>, _ app: UnsafePointer<Unmanaged<SecTrustedApplication>?>) -> OSStatus ``` |
| To | ``` func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<Int8>, _ app: UnsafeMutablePointer<Unmanaged<SecTrustedApplication>?>) -> OSStatus ``` |

Modified SecVerifyTransformCreate(SecKey!, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SecVerifyTransformCreate(_ key: SecKey!, _ signature: CFData!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransformRef>! ``` | OS X 10.10 |
| To | ``` func SecVerifyTransformCreate(_ key: SecKey!, _ signature: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecTransform>! ``` | OS X 10.7 |

Modified cssmAlgToOid(CSSM_ALGORITHMS) -> UnsafePointer<CSSM_OID>

|  | Declaration |
| --- | --- |
| From | ``` func cssmAlgToOid(_ algId: CSSM_ALGORITHMS) -> ConstUnsafePointer<CSSM_OID> ``` |
| To | ``` func cssmAlgToOid(_ algId: CSSM_ALGORITHMS) -> UnsafePointer<CSSM_OID> ``` |

Modified cssmOidToAlg(UnsafePointer<CSSM_OID>, UnsafeMutablePointer<CSSM_ALGORITHMS>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func cssmOidToAlg(_ oid: ConstUnsafePointer<CSSM_OID>, _ alg: UnsafePointer<CSSM_ALGORITHMS>) -> Bool ``` |
| To | ``` func cssmOidToAlg(_ oid: UnsafePointer<CSSM_OID>, _ alg: UnsafeMutablePointer<CSSM_ALGORITHMS>) -> Bool ``` |

Modified cssmPerror(UnsafePointer<Int8>, CSSM_RETURN)

|  | Declaration |
| --- | --- |
| From | ``` func cssmPerror(_ how: ConstUnsafePointer<Int8>, _ error: CSSM_RETURN) ``` |
| To | ``` func cssmPerror(_ how: UnsafePointer<Int8>, _ error: CSSM_RETURN) ``` |

Modified errSecAllocate

|  | Declaration |
| --- | --- |
| From | ``` var errSecAllocate: Int { get } ``` |
| To | ``` let errSecAllocate: OSStatus ``` |

Modified errSecAuthFailed

|  | Declaration |
| --- | --- |
| From | ``` var errSecAuthFailed: Int { get } ``` |
| To | ``` let errSecAuthFailed: OSStatus ``` |

Modified errSecDecode

|  | Declaration |
| --- | --- |
| From | ``` var errSecDecode: Int { get } ``` |
| To | ``` let errSecDecode: OSStatus ``` |

Modified errSecDuplicateItem

|  | Declaration |
| --- | --- |
| From | ``` var errSecDuplicateItem: Int { get } ``` |
| To | ``` let errSecDuplicateItem: OSStatus ``` |

Modified errSecInteractionNotAllowed

|  | Declaration |
| --- | --- |
| From | ``` var errSecInteractionNotAllowed: Int { get } ``` |
| To | ``` let errSecInteractionNotAllowed: OSStatus ``` |

Modified errSecItemNotFound

|  | Declaration |
| --- | --- |
| From | ``` var errSecItemNotFound: Int { get } ``` |
| To | ``` let errSecItemNotFound: OSStatus ``` |

Modified errSecNotAvailable

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotAvailable: Int { get } ``` |
| To | ``` let errSecNotAvailable: OSStatus ``` |

Modified errSecParam

|  | Declaration |
| --- | --- |
| From | ``` var errSecParam: Int { get } ``` |
| To | ``` let errSecParam: OSStatus ``` |

Modified errSecSuccess

|  | Declaration |
| --- | --- |
| From | ``` var errSecSuccess: Int { get } ``` |
| To | ``` let errSecSuccess: OSStatus ``` |

Modified errSecUnimplemented

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnimplemented: Int { get } ``` |
| To | ``` let errSecUnimplemented: OSStatus ``` |

Modified kSecACLAuthorizationAny

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationChangeACL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationChangeOwner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationDecrypt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationDelete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationDerive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationEncrypt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationExportClear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationExportWrapped

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationGenKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationImportClear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationImportWrapped

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationKeychainCreate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationKeychainDelete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationKeychainItemDelete

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationKeychainItemInsert

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationKeychainItemModify

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationKeychainItemRead

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationLogin

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationMAC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecACLAuthorizationSign

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecAttrAccess

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccess: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccess: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrAccessControl

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessControl: Unmanaged<AnyObject>! ``` |
| To | ``` var kSecAttrAccessControl: CFStringRef ``` |

Modified kSecAttrAccessGroup

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessGroup: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessGroup: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessible

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessible: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessible: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessibleAfterFirstUnlock

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessibleAfterFirstUnlock: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessibleAfterFirstUnlock: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessibleAlways

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessibleAlways: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessibleAlways: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessibleAlwaysThisDeviceOnly

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessibleAlwaysThisDeviceOnly: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessibleAlwaysThisDeviceOnly: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: Unmanaged<AnyObject>! ``` |
| To | ``` var kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFStringRef ``` |

Modified kSecAttrAccessibleWhenUnlocked

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessibleWhenUnlocked: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessibleWhenUnlocked: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccessibleWhenUnlockedThisDeviceOnly

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrAccount

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAccount: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAccount: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrApplicationLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrApplicationLabel: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrApplicationLabel: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrApplicationTag

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrApplicationTag: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrApplicationTag: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationType: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationType: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeDPA

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeDPA: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeDPA: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeDefault

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeDefault: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeDefault: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeHTMLForm

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeHTMLForm: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeHTMLForm: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeHTTPBasic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeHTTPBasic: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeHTTPBasic: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeHTTPDigest

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeHTTPDigest: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeHTTPDigest: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeMSN

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeMSN: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeMSN: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeNTLM

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeNTLM: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeNTLM: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrAuthenticationTypeRPA

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrAuthenticationTypeRPA: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrAuthenticationTypeRPA: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanDecrypt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanDecrypt: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanDecrypt: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanDerive

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanDerive: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanDerive: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanEncrypt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanEncrypt: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanEncrypt: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanSign

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanSign: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanSign: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanUnwrap

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanUnwrap: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanUnwrap: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanVerify

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanVerify: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanVerify: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCanWrap

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCanWrap: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCanWrap: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCertificateEncoding

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCertificateEncoding: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCertificateEncoding: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCertificateType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCertificateType: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCertificateType: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrComment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrComment: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrComment: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCreationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCreationDate: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCreationDate: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrCreator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrCreator: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrCreator: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrDescription: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrDescription: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrEffectiveKeySize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrEffectiveKeySize: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrEffectiveKeySize: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrGeneric

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrGeneric: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrGeneric: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrIsExtractable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrIsExtractable: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrIsExtractable: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrIsInvisible

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrIsInvisible: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrIsInvisible: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrIsNegative

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrIsNegative: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrIsNegative: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrIsPermanent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrIsPermanent: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrIsPermanent: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrIsSensitive

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrIsSensitive: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrIsSensitive: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrIssuer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrIssuer: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrIssuer: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrKeyClass

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyClass: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyClass: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrKeyClassPrivate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyClassPrivate: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyClassPrivate: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyClassPublic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyClassPublic: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyClassPublic: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyClassSymmetric

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyClassSymmetric: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyClassSymmetric: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeySizeInBits

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeySizeInBits: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeySizeInBits: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrKeyType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyType: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyType: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrKeyType3DES

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyType3DES: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyType3DES: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeAES

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeAES: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeAES: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeCAST

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeCAST: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeCAST: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeDES

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeDES: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeDES: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeDSA

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeDSA: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeDSA: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeEC

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeEC: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeEC: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrKeyTypeECDSA

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeECDSA: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeECDSA: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeRC2

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeRC2: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeRC2: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeRC4

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeRC4: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeRC4: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrKeyTypeRSA

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrKeyTypeRSA: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrKeyTypeRSA: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrLabel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrLabel: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrLabel: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrModificationDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrModificationDate: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrModificationDate: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrPRF

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPRF: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPRF: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrPRFHmacAlgSHA1

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA1: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPRFHmacAlgSHA1: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrPRFHmacAlgSHA224

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA224: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPRFHmacAlgSHA224: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrPRFHmacAlgSHA256

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA256: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPRFHmacAlgSHA256: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrPRFHmacAlgSHA384

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA384: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPRFHmacAlgSHA384: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrPRFHmacAlgSHA512

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPRFHmacAlgSHA512: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPRFHmacAlgSHA512: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrPath

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPath: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPath: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrPort

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPort: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPort: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocol

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocol: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocol: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolAFP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolAFP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolAFP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolAppleTalk

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolAppleTalk: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolAppleTalk: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolDAAP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolDAAP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolDAAP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolEPPC

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolEPPC: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolEPPC: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolFTP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolFTP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolFTP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolFTPAccount

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolFTPAccount: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolFTPAccount: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolFTPProxy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolFTPProxy: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolFTPProxy: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolFTPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolFTPS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolFTPS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolHTTP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolHTTP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolHTTP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolHTTPProxy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolHTTPProxy: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolHTTPProxy: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolHTTPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolHTTPS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolHTTPS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolHTTPSProxy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolHTTPSProxy: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolHTTPSProxy: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolIMAP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolIMAP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolIMAP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolIMAPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolIMAPS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolIMAPS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolIPP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolIPP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolIPP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolIRC

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolIRC: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolIRC: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolIRCS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolIRCS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolIRCS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolLDAP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolLDAP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolLDAP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolLDAPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolLDAPS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolLDAPS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolNNTP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolNNTP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolNNTP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolNNTPS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolNNTPS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolNNTPS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolPOP3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolPOP3: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolPOP3: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolPOP3S

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolPOP3S: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolPOP3S: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolRTSP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolRTSP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolRTSP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolRTSPProxy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolRTSPProxy: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolRTSPProxy: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolSMB

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolSMB: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolSMB: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolSMTP

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolSMTP: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolSMTP: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolSOCKS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolSOCKS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolSOCKS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolSSH

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolSSH: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolSSH: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolTelnet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolTelnet: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolTelnet: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrProtocolTelnetS

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrProtocolTelnetS: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrProtocolTelnetS: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrPublicKeyHash

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrPublicKeyHash: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrPublicKeyHash: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrRounds

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrRounds: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrRounds: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrSalt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSalt: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSalt: CFStringRef ``` | OS X 10.7 |

Modified kSecAttrSecurityDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSecurityDomain: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSecurityDomain: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrSerialNumber

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSerialNumber: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSerialNumber: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrServer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrServer: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrServer: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrService

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrService: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrService: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrSubject

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSubject: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSubject: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrSubjectKeyID

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSubjectKeyID: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSubjectKeyID: CFStringRef ``` | OS X 10.6 |

Modified kSecAttrSynchronizable

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSynchronizable: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSynchronizable: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrSynchronizableAny

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrSynchronizableAny: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrSynchronizableAny: CFStringRef ``` | OS X 10.9 |

Modified kSecAttrType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecAttrType: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecAttrType: CFStringRef ``` | OS X 10.6 |

Modified kSecCertificateUsageDeriveAndSign

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecCertificateUsageSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecCertificateUsageSigningAndEncrypting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecClass

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecClass: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecClass: CFStringRef ``` | OS X 10.6 |

Modified kSecClassCertificate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecClassCertificate: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecClassCertificate: CFStringRef ``` | OS X 10.7 |

Modified kSecClassGenericPassword

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecClassGenericPassword: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecClassGenericPassword: CFStringRef ``` | OS X 10.7 |

Modified kSecClassIdentity

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecClassIdentity: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecClassIdentity: CFStringRef ``` | OS X 10.7 |

Modified kSecClassInternetPassword

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecClassInternetPassword: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecClassInternetPassword: CFStringRef ``` | OS X 10.6 |

Modified kSecClassKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecClassKey: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecClassKey: CFStringRef ``` | OS X 10.7 |

Modified kSecIdentityDomainDefault

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSecIdentityDomainKerberosKDC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSecMatchCaseInsensitive

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchCaseInsensitive: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchCaseInsensitive: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchDiacriticInsensitive

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchDiacriticInsensitive: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchDiacriticInsensitive: CFStringRef ``` | OS X 10.7 |

Modified kSecMatchEmailAddressIfPresent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchEmailAddressIfPresent: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchEmailAddressIfPresent: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchIssuers

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchIssuers: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchIssuers: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchItemList

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchItemList: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchItemList: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchLimit

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchLimit: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchLimit: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchLimitAll

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchLimitAll: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchLimitAll: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchLimitOne

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchLimitOne: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchLimitOne: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchPolicy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchPolicy: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchPolicy: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchSearchList

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchSearchList: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchSearchList: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchSubjectContains

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchSubjectContains: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchSubjectContains: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchSubjectEndsWith

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchSubjectEndsWith: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchSubjectEndsWith: CFStringRef ``` | OS X 10.7 |

Modified kSecMatchSubjectStartsWith

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchSubjectStartsWith: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchSubjectStartsWith: CFStringRef ``` | OS X 10.7 |

Modified kSecMatchSubjectWholeString

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchSubjectWholeString: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchSubjectWholeString: CFStringRef ``` | OS X 10.7 |

Modified kSecMatchTrustedOnly

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchTrustedOnly: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchTrustedOnly: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchValidOnDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchValidOnDate: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchValidOnDate: CFStringRef ``` | OS X 10.6 |

Modified kSecMatchWidthInsensitive

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecMatchWidthInsensitive: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecMatchWidthInsensitive: CFStringRef ``` | OS X 10.7 |

Modified kSecOAEPEncodingParametersAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecOAEPMGF1DigestAlgorithmAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecOAEPMessageLengthAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecOIDADC_CERT_POLICY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_CERT_POLICY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EKU_CODE_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EKU_CODE_SIGNING_DEV

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EKU_ICHAT_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EKU_RESOURCE_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EKU_SYSTEM_IDENTITY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_APPLE_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_CODE_SIGNING

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAuthorityInfoAccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDAuthorityKeyIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDBasicConstraints

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDBiometricInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCSSMKeyStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCertIssuer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCertificatePolicies

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDClientAuth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCollectiveStateProvinceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCollectiveStreetAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCommonName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCountryName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCrlDistributionPoints

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCrlNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDCrlReason

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDOTMAC_CERT_EMAIL_SIGN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDOTMAC_CERT_EXTENSION

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDOTMAC_CERT_IDENTITY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDOTMAC_CERT_POLICY

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDeltaCrlIndicator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDEKU_IPSec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDEmailAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDEmailProtection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDExtendedKeyUsage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDExtendedKeyUsageAny

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDExtendedUseCodeSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDGivenName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDHoldInstructionCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDInvalidityDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDIssuerAltName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDIssuingDistributionPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDIssuingDistributionPoints

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDKERBv5_PKINIT_KP_KDC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDKeyUsage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDLocalityName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDMS_NTPrincipalName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDMicrosoftSGC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDNameConstraints

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDNetscapeCertSequence

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDNetscapeCertType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDNetscapeSGC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDOCSPSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDOrganizationName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDOrganizationalUnitName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDPolicyConstraints

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDPolicyMappings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDPrivateKeyUsagePeriod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDQC_Statements

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSRVName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecOIDSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDServerAuth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDStateProvinceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDStreetAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectAltName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectDirectoryAttributes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectEmailAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectInfoAccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectKeyIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectPicture

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSubjectSignatureBitmap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDSurname

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDTimeStamping

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDTitle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDUseExemptions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1CertificateIssuerUniqueId

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1CertificateSubjectUniqueId

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1IssuerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1IssuerNameCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1IssuerNameLDAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1IssuerNameStd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1Signature

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SignatureAlgorithm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SignatureAlgorithmParameters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SignatureAlgorithmTBS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SignatureCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SignatureStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectNameCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectNameLDAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectNameStd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectPublicKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectPublicKeyAlgorithm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectPublicKeyAlgorithmParameters

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1SubjectPublicKeyCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1ValidityNotAfter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1ValidityNotBefore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V1Version

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3Certificate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionCritical

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionId

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionsCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateExtensionsStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3CertificateNumberOfExtensions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3SignedCertificate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecOIDX509V3SignedCertificateCStruct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPaddingOAEPKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecPolicyAppleCodeSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyAppleEAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyAppleIDValidation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyAppleIPsec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyApplePKINITClient

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyApplePKINITServer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyApplePassbookSigning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecPolicyAppleRevocation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecPolicyAppleSMIME

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyAppleSSL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyAppleTimeStamping

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecPolicyAppleX509Basic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyClient

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_CRLSign

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_DataEncipherment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_DecipherOnly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_DigitalSignature

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_EncipherOnly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_KeyAgreement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_KeyCertSign

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_KeyEncipherment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyKU_NonRepudiation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyMacAppStoreReceipt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyOid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPolicyRevocationFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecPolicyTeamIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecPrivateKeyAttrs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecPropertyKeyLabel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyKeyLocalizedLabel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyKeyType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyKeyValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeSection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeSuccess

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeTitle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeURL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPropertyTypeWarning

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecPublicKeyAttrs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kSecRandomDefault

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecRandomDefault: SecRandom! ``` | OS X 10.10 |
| To | ``` let kSecRandomDefault: SecRandomRef ``` | OS X 10.7 |

Modified kSecReturnAttributes

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecReturnAttributes: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecReturnAttributes: CFStringRef ``` | OS X 10.6 |

Modified kSecReturnData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecReturnData: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecReturnData: CFStringRef ``` | OS X 10.6 |

Modified kSecReturnPersistentRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecReturnPersistentRef: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecReturnPersistentRef: CFStringRef ``` | OS X 10.6 |

Modified kSecReturnRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecReturnRef: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecReturnRef: CFStringRef ``` | OS X 10.6 |

Modified kSecTransformAbortAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecTransformDebugAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecTransformInputAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecTransformOutputAttributeName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecTransformTransformName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSecTrustEvaluationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecTrustExtendedValidation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecTrustOrganizationName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecTrustResultValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecTrustRevocationChecked

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecTrustRevocationValidUntilDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kSecUseItemList

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecUseItemList: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecUseItemList: CFStringRef ``` | OS X 10.6 |

Modified kSecUseKeychain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecUseKeychain: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecUseKeychain: CFStringRef ``` | OS X 10.7 |

Modified kSecValueData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecValueData: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecValueData: CFStringRef ``` | OS X 10.6 |

Modified kSecValuePersistentRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecValuePersistentRef: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecValuePersistentRef: CFStringRef ``` | OS X 10.6 |

Modified kSecValueRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kSecValueRef: AnyObject! ``` | OS X 10.10 |
| To | ``` let kSecValueRef: CFStringRef ``` | OS X 10.6 |

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
