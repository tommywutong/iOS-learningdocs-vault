---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/Security.html
archived_at: '2026-07-18T02:51:34.970522Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Security Changes for Swift

### Security

Removed [AuthorizationFlags.Defaults](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagdefaults)Removed cssm_access_credentials.init(EntryTag: CSSM_STRING, BaseCerts: CSSM_BASE_CERTS, Samples: CSSM_SAMPLEGROUP, Callback: CSSM_CHALLENGE_CALLBACK!, CallerCtx: UnsafeMutablePointer<Void>)Removed cssm_acl_edit.init(EditMode: CSSM_ACL_EDIT_MODE, OldEntryHandle: CSSM_ACL_HANDLE, NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT>)Removed cssm_acl_entry_input.init(Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback: CSSM_ACL_SUBJECT_CALLBACK!, CallerContext: UnsafeMutablePointer<Void>)Removed CSSM_APPLE_CL_CSR_REQUEST.init(subjectNameX509: CSSM_X509_NAME_PTR, signatureAlg: CSSM_ALGORITHMS, signatureOid: CSSM_OID, cspHand: CSSM_CSP_HANDLE, subjectPublicKey: UnsafePointer<CSSM_KEY>, subjectPrivateKey: UnsafePointer<CSSM_KEY>, challengeString: UnsafePointer<Int8>)Removed CSSM_APPLE_TP_CERT_REQUEST.init(cspHand: CSSM_CSP_HANDLE, clHand: CSSM_CL_HANDLE, serialNumber: uint32, numSubjectNames: uint32, subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, numIssuerNames: uint32, issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, issuerNameX509: CSSM_X509_NAME_PTR, certPublicKey: UnsafePointer<CSSM_KEY>, issuerPrivateKey: UnsafePointer<CSSM_KEY>, signatureAlg: CSSM_ALGORITHMS, signatureOid: CSSM_OID, notBefore: uint32, notAfter: uint32, numExtensions: uint32, extensions: UnsafeMutablePointer<CE_DataAndType>, challengeString: UnsafePointer<Int8>)Removed CSSM_APPLE_TP_CRL_OPTIONS.init(Version: uint32, CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore: CSSM_DL_DB_HANDLE_PTR)Removed CSSM_APPLE_TP_NAME_OID.init(string: UnsafePointer<Int8>, oid: UnsafePointer<CSSM_OID>)Removed CSSM_APPLE_TP_SMIME_OPTIONS.init(Version: uint32, IntendedUsage: CE_KeyUsage, SenderEmailLen: uint32, SenderEmail: UnsafePointer<Int8>)Removed CSSM_APPLE_TP_SSL_OPTIONS.init(Version: uint32, ServerNameLen: uint32, ServerName: UnsafePointer<Int8>, Flags: uint32)Removed [cssm_applecspdl_db_change_password_parameters.init(accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS>)](https://developer.apple.com/documentation/security/cssm_applecspdl_db_change_password_parameters/1399634-init)Removed [cssm_authorizationgroup.init(NumberOfAuthTags: uint32, AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>)](https://developer.apple.com/documentation/security/cssm_authorizationgroup/1401385-init)Removed cssm_certgroup.init(CertType: CSSM_CERT_TYPE, CertEncoding: CSSM_CERT_ENCODING, NumCerts: uint32, GroupList: cssm_certgroup.__Unnamed_union_GroupList, CertGroupType: CSSM_CERTGROUP_TYPE, Reserved: UnsafeMutablePointer<Void>)Removed cssm_context.init(ContextType: CSSM_CONTEXT_TYPE, AlgorithmType: CSSM_ALGORITHMS, NumberOfAttributes: uint32, ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR, CSPHandle: CSSM_CSP_HANDLE, Privileged: CSSM_BOOL, EncryptionProhibited: uint32, WorkFactor: uint32, Reserved: uint32)Removed cssm_context_attribute_value.init(AccessCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_context_attribute_value.init(CryptoData: CSSM_CRYPTO_DATA_PTR)Removed cssm_context_attribute_value.init(Data: CSSM_DATA_PTR)Removed cssm_context_attribute_value.init(Date: CSSM_DATE_PTR)Removed cssm_context_attribute_value.init(DLDBHandle: CSSM_DL_DB_HANDLE_PTR)Removed cssm_context_attribute_value.init(Key: CSSM_KEY_PTR)Removed cssm_context_attribute_value.init(KRProfile: UnsafeMutablePointer<cssm_kr_profile>)Removed cssm_context_attribute_value.init(Range: CSSM_RANGE_PTR)Removed cssm_context_attribute_value.init(String: UnsafeMutablePointer<Int8>)Removed cssm_context_attribute_value.init(Version: CSSM_VERSION_PTR)Removed cssm_crypto_data.init(Param: CSSM_DATA, Callback: CSSM_CALLBACK!, CallerCtx: UnsafeMutablePointer<Void>)Removed [cssm_data.init(Length: CSSM_SIZE, Data: UnsafeMutablePointer<uint8>)](https://developer.apple.com/documentation/security/cssm_data/1397180-init)Removed cssm_db_attribute_data.init(Info: CSSM_DB_ATTRIBUTE_INFO, NumberOfValues: uint32, Value: CSSM_DATA_PTR)Removed cssm_db_attribute_label.init(AttributeName: UnsafeMutablePointer<Int8>)Removed cssm_db_record_attribute_data.init(DataRecordType: CSSM_DB_RECORDTYPE, SemanticInformation: uint32, NumberOfAttributes: uint32, AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR)Removed cssm_db_record_attribute_info.init(DataRecordType: CSSM_DB_RECORDTYPE, NumberOfAttributes: uint32, AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR)Removed cssm_db_record_index_info.init(DataRecordType: CSSM_DB_RECORDTYPE, NumberOfIndexes: uint32, IndexInfo: CSSM_DB_INDEX_INFO_PTR)Removed cssm_db_schema_attribute_info.init(AttributeId: uint32, AttributeName: UnsafeMutablePointer<Int8>, AttributeNameID: CSSM_OID, DataType: CSSM_DB_ATTRIBUTE_FORMAT)Removed cssm_dbinfo.init(NumberOfRecordTypes: uint32, DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR, RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR, RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR, IsLocal: CSSM_BOOL, AccessPath: UnsafeMutablePointer<Int8>, Reserved: UnsafeMutablePointer<Void>)Removed cssm_dl_db_list.init(NumHandles: uint32, DLDBHandle: CSSM_DL_DB_HANDLE_PTR)Removed cssm_evidence.init(EvidenceForm: CSSM_EVIDENCE_FORM, Evidence: UnsafeMutablePointer<Void>)Removed cssm_fieldgroup.init(NumberOfFields: Int32, Fields: CSSM_FIELD_PTR)Removed cssm_kr_name.init(Type: uint8, Length: uint8, Name: UnsafeMutablePointer<Int8>)Removed cssm_kr_policy_info.init(krbNotAllowed: CSSM_BOOL, numberOfEntries: uint32, policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM>)Removed cssm_kr_profile.init(UserName: CSSM_KR_NAME, UserCertificate: CSSM_CERTGROUP_PTR, KRSCertChain: CSSM_CERTGROUP_PTR, LE_KRANum: uint8, LE_KRACertChainList: CSSM_CERTGROUP_PTR, ENT_KRANum: uint8, ENT_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_KRANum: uint8, INDIV_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_AuthenticationInfo: CSSM_DATA_PTR, KRSPFlags: uint32, KRSPExtensions: CSSM_DATA_PTR)Removed cssm_krsubservice.init(SubServiceId: uint32, Description: UnsafeMutablePointer<Int8>, WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO)Removed [cssm_list.init(ListType: CSSM_LIST_TYPE, Head: CSSM_LIST_ELEMENT_PTR, Tail: CSSM_LIST_ELEMENT_PTR)](https://developer.apple.com/documentation/security/cssm_list/1395497-init)Removed cssm_list_element.init(NextElement: UnsafeMutablePointer<cssm_list_element>, WordID: CSSM_WORDID_TYPE, ElementType: CSSM_LIST_ELEMENT_TYPE, Element: cssm_list_element.__Unnamed_union_Element)Removed cssm_manager_registration_info.init(Initialize: ((uint32, uint32) -> CSSM_RETURN)!, Terminate: (() -> CSSM_RETURN)!, RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)!, DeregisterDispatchTable: (() -> CSSM_RETURN)!, EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!, RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!)Removed cssm_memory_funcs.init(malloc_func: CSSM_MALLOC!, free_func: CSSM_FREE!, realloc_func: CSSM_REALLOC!, calloc_func: CSSM_CALLOC!, AllocRef: UnsafeMutablePointer<Void>)Removed cssm_module_funcs.init(ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs: uint32, ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?>)Removed [cssm_name_list.init(NumStrings: uint32, String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)](https://developer.apple.com/documentation/security/cssm_name_list/1401788-init)Removed [cssm_parsed_cert.init(CertType: CSSM_CERT_TYPE, ParsedCertFormat: CSSM_CERT_PARSE_FORMAT, ParsedCert: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/security/cssm_parsed_cert/1395174-init)Removed [cssm_parsed_crl.init(CrlType: CSSM_CRL_TYPE, ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT, ParsedCrl: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/security/cssm_parsed_crl/1394664-init)Removed cssm_query.init(RecordType: CSSM_DB_RECORDTYPE, Conjunctive: CSSM_DB_CONJUNCTIVE, NumSelectionPredicates: uint32, SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR, QueryLimits: CSSM_QUERY_LIMITS, QueryFlags: CSSM_QUERY_FLAGS)Removed cssm_resource_control_context.init(AccessCred: CSSM_ACCESS_CREDENTIALS_PTR, InitialAclEntry: CSSM_ACL_ENTRY_INPUT)Removed cssm_sample.init(TypedSample: CSSM_LIST, Verifier: UnsafePointer<CSSM_SUBSERVICE_UID>)Removed cssm_samplegroup.init(NumberOfSamples: uint32, Samples: UnsafePointer<CSSM_SAMPLE>)Removed cssm_spi_ac_funcs.init(AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)!, PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Removed cssm_spi_cl_funcs.init(CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)!, CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Removed cssm_spi_csp_funcs.init(EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)!, SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)!, SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!, DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)!, GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)!, WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)!, FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)!, PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!, Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)!, Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!, ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)!, RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)!, GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)!, GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!)Removed cssm_spi_dl_funcs.init(DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)!, DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!, Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Removed cssm_spi_kr_funcs.init(RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)!, GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)!, ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)!, GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Removed cssm_spi_tp_funcs.init(SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)!, ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)!, ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)!, CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)!, CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!, FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)!, FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)!, CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)!, TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!)Removed cssm_state_funcs.init(cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!, cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)!, cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)!, cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!)Removed CSSM_TP_APPLE_EVIDENCE_INFO.init(StatusBits: CSSM_TP_APPLE_CERT_STATUS, NumStatusCodes: uint32, StatusCodes: UnsafeMutablePointer<CSSM_RETURN>, Index: uint32, DlDbHandle: CSSM_DL_DB_HANDLE, UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR)Removed cssm_tp_authority_id.init(AuthorityCert: UnsafeMutablePointer<CSSM_DATA>, AuthorityLocation: CSSM_NET_ADDRESS_PTR)Removed cssm_tp_callerauth_context.init(Policy: CSSM_TP_POLICYINFO, VerifyTime: CSSM_TIMESTRING, VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK!, NumberOfAnchorCerts: uint32, AnchorCerts: CSSM_DATA_PTR, DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_tp_certchange_input.init(Action: CSSM_TP_CERTCHANGE_ACTION, Reason: CSSM_TP_CERTCHANGE_REASON, CLHandle: CSSM_CL_HANDLE, Cert: CSSM_DATA_PTR, ChangeInfo: CSSM_FIELD_PTR, StartTime: CSSM_TIMESTRING, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_tp_certissue_input.init(CSPSubserviceUid: CSSM_SUBSERVICE_UID, CLHandle: CSSM_CL_HANDLE, NumberOfTemplateFields: uint32, SubjectCertFields: CSSM_FIELD_PTR, MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls: uint32, ServiceControls: CSSM_FIELD_PTR, UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_tp_certissue_output.init(IssueStatus: CSSM_TP_CERTISSUE_STATUS, CertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests: CSSM_TP_SERVICES)Removed cssm_tp_certnotarize_input.init(CLHandle: CSSM_CL_HANDLE, NumberOfFields: uint32, MoreFields: CSSM_FIELD_PTR, SignScope: CSSM_FIELD_PTR, ScopeSize: uint32, MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls: uint32, ServiceControls: CSSM_FIELD_PTR, UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_tp_certnotarize_output.init(NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS, NotarizedCertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests: CSSM_TP_SERVICES)Removed cssm_tp_certreclaim_input.init(CLHandle: CSSM_CL_HANDLE, NumberOfSelectionFields: uint32, SelectionFields: CSSM_FIELD_PTR, UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_tp_certreclaim_output.init(ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS, ReclaimedCertGroup: CSSM_CERTGROUP_PTR, KeyCacheHandle: CSSM_LONG_HANDLE)Removed cssm_tp_certverify_input.init(CLHandle: CSSM_CL_HANDLE, Cert: CSSM_DATA_PTR, VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR)Removed cssm_tp_certverify_output.init(VerifyStatus: CSSM_TP_CERTVERIFY_STATUS, NumberOfEvidence: uint32, Evidence: CSSM_EVIDENCE_PTR)Removed cssm_tp_confirm_response.init(NumberOfResponses: uint32, Responses: CSSM_TP_CONFIRM_STATUS_PTR)Removed cssm_tp_crlissue_input.init(CLHandle: CSSM_CL_HANDLE, CrlIdentifier: uint32, CrlThisTime: CSSM_TIMESTRING, PolicyIdentifier: CSSM_FIELD_PTR, CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Removed cssm_tp_crlissue_output.init(IssueStatus: CSSM_TP_CRLISSUE_STATUS, Crl: CSSM_ENCODED_CRL_PTR, CrlNextTime: CSSM_TIMESTRING)Removed cssm_tp_policyinfo.init(NumberOfPolicyIds: uint32, PolicyIds: CSSM_FIELD_PTR, PolicyControl: UnsafeMutablePointer<Void>)Removed cssm_tp_request_set.init(NumberOfRequests: uint32, Requests: UnsafeMutablePointer<Void>)Removed [cssm_tp_result_set.init(NumberOfResults: uint32, Results: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/security/cssm_tp_result_set/1395819-init)Removed cssm_tp_verify_context.init(Action: CSSM_TP_ACTION, ActionData: CSSM_DATA, Crls: CSSM_CRLGROUP, Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR)Removed cssm_tp_verify_context_result.init(NumberOfEvidences: uint32, Evidence: CSSM_EVIDENCE_PTR)Removed cssm_tuplegroup.init(NumberOfTuples: uint32, Tuples: CSSM_TUPLE_PTR)Removed cssm_upcalls.init(malloc_func: CSSM_UPCALLS_MALLOC!, free_func: CSSM_UPCALLS_FREE!, realloc_func: CSSM_UPCALLS_REALLOC!, calloc_func: CSSM_UPCALLS_CALLOC!, CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)!, GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!)Removed cssm_x509_extensions.init(numberOfExtensions: uint32, extensions: CSSM_X509_EXTENSION_PTR)Removed cssm_x509_name.init(numberOfRDNs: uint32, RelativeDistinguishedName: CSSM_X509_RDN_PTR)Removed cssm_x509_rdn.init(numberOfPairs: uint32, AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR)Removed cssm_x509_revoked_cert_list.init(numberOfRevokedCertEntries: uint32, revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR)Removed cssm_x509_tbs_certlist.init(version: CSSM_DATA, signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer: CSSM_X509_NAME, thisUpdate: CSSM_X509_TIME, nextUpdate: CSSM_X509_TIME, revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR, extensions: CSSM_X509_EXTENSIONS)Removed cssm_x509ext_pair.init(tagAndValue: CSSM_X509EXT_TAGandVALUE, parsedValue: UnsafeMutablePointer<Void>)Removed cssm_x509ext_policyQualifiers.init(numberOfPolicyQualifiers: uint32, policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO>)Removed cssm_x509ext_value.init(parsedValue: UnsafeMutablePointer<Void>)Removed cssm_x509ext_value.init(tagAndValue: UnsafeMutablePointer<CSSM_X509EXT_TAGandVALUE>)Removed cssm_x509ext_value.init(valuePair: UnsafeMutablePointer<CSSM_X509EXT_PAIR>)Removed [DERItem.init(data: UnsafeMutablePointer<DERByte>, length: DERSize)](https://developer.apple.com/documentation/security/deritem/1398217-init)Removed mds_funcs.init(DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!, GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!)Removed [SecAccessControlCreateFlags.init(rawValue: CFIndex)](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1395038-init)Removed [SecCSFlags.DefaultFlags](https://developer.apple.com/documentation/security/seccsflags/kseccsdefaultflags)Removed SSLSessionStrengthPolicy [enum]Removed SSLSessionStrengthPolicy.ATSv1Removed SSLSessionStrengthPolicy.ATSv1_noPFSRemoved SSLSessionStrengthPolicy.DefaultRemoved [kSecTrustResultDeny](https://developer.apple.com/documentation/security/sectrustresulttype/deny)Removed [kSecTrustResultFatalTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultfataltrustfailure)Removed [kSecTrustResultInvalid](https://developer.apple.com/documentation/security/sectrustresulttype/invalid)Removed [kSecTrustResultOtherError](https://developer.apple.com/documentation/security/sectrustresulttype/othererror)Removed [kSecTrustResultProceed](https://developer.apple.com/documentation/security/sectrustresulttype/proceed)Removed [kSecTrustResultRecoverableTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultrecoverabletrustfailure)Removed [kSecTrustResultUnspecified](https://developer.apple.com/documentation/security/sectrustresulttype/unspecified)Removed [SecTrustResultType](https://developer.apple.com/documentation/security/sectrustresulttype)Removed SSLSetSessionStrengthPolicy(_: SSLContext, _: SSLSessionStrengthPolicy) -> OSStatusAdded [AuthorizationItemSet.init()](https://developer.apple.com/documentation/security/authorizationitemset/1644014-init)Added [AuthorizationItemSet.init(count: UInt32, items: UnsafeMutablePointer<AuthorizationItem>?)](https://developer.apple.com/documentation/security/authorizationitemset/1644007-init)Added cssm_access_credentials.init(EntryTag: Security.CSSM_STRING, BaseCerts: cssm_base_certs, Samples: cssm_samplegroup, Callback: Security.CSSM_CHALLENGE_CALLBACK!, CallerCtx: UnsafeMutableRawPointer!)Added cssm_acl_edit.init(EditMode: CSSM_ACL_EDIT_MODE, OldEntryHandle: CSSM_ACL_HANDLE, NewEntry: UnsafePointer<cssm_acl_entry_input>!)Added cssm_acl_entry_input.init(Prototype: cssm_acl_entry_prototype, Callback: Security.CSSM_ACL_SUBJECT_CALLBACK!, CallerContext: UnsafeMutableRawPointer!)Added CSSM_APPLE_CL_CSR_REQUEST.init(subjectNameX509: UnsafeMutablePointer<cssm_x509_name>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: CSSM_OID, cspHand: CSSM_CSP_HANDLE, subjectPublicKey: UnsafePointer<cssm_key>!, subjectPrivateKey: UnsafePointer<cssm_key>!, challengeString: UnsafePointer<Int8>!)Added CSSM_APPLE_TP_CERT_REQUEST.init(cspHand: CSSM_CSP_HANDLE, clHand: CSSM_CL_HANDLE, serialNumber: uint32, numSubjectNames: uint32, subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, numIssuerNames: uint32, issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!, certPublicKey: UnsafePointer<cssm_key>!, issuerPrivateKey: UnsafePointer<cssm_key>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: CSSM_OID, notBefore: uint32, notAfter: uint32, numExtensions: uint32, extensions: UnsafeMutablePointer<__CE_DataAndType>!, challengeString: UnsafePointer<Int8>!)Added CSSM_APPLE_TP_CRL_OPTIONS.init(Version: uint32, CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore: UnsafeMutablePointer<cssm_dl_db_handle>!)Added CSSM_APPLE_TP_NAME_OID.init(string: UnsafePointer<Int8>!, oid: UnsafePointer<CSSM_OID>!)Added CSSM_APPLE_TP_SMIME_OPTIONS.init(Version: uint32, IntendedUsage: uint16, SenderEmailLen: uint32, SenderEmail: UnsafePointer<Int8>!)Added CSSM_APPLE_TP_SSL_OPTIONS.init(Version: uint32, ServerNameLen: uint32, ServerName: UnsafePointer<Int8>!, Flags: uint32)Added [cssm_applecspdl_db_change_password_parameters.init(accessCredentials: UnsafeMutablePointer<cssm_access_credentials>!)](https://developer.apple.com/documentation/security/cssm_applecspdl_db_change_password_parameters/1399634-init)Added [cssm_authorizationgroup.init(NumberOfAuthTags: uint32, AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>!)](https://developer.apple.com/documentation/security/cssm_authorizationgroup/1401385-init)Added cssm_certgroup.init(CertType: CSSM_CERT_TYPE, CertEncoding: CSSM_CERT_ENCODING, NumCerts: uint32, GroupList: cssm_certgroup.__Unnamed_union_GroupList, CertGroupType: CSSM_CERTGROUP_TYPE, Reserved: UnsafeMutableRawPointer!)Added cssm_context.init(ContextType: CSSM_CONTEXT_TYPE, AlgorithmType: CSSM_ALGORITHMS, NumberOfAttributes: uint32, ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR!, CSPHandle: CSSM_CSP_HANDLE, Privileged: CSSM_BOOL, EncryptionProhibited: uint32, WorkFactor: uint32, Reserved: uint32)Added cssm_context_attribute_value.init(AccessCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_context_attribute_value.init(CryptoData: UnsafeMutablePointer<cssm_crypto_data>!)Added cssm_context_attribute_value.init(Data: UnsafeMutablePointer<cssm_data>!)Added cssm_context_attribute_value.init(Date: UnsafeMutablePointer<cssm_date>!)Added cssm_context_attribute_value.init(DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>!)Added cssm_context_attribute_value.init(Key: UnsafeMutablePointer<cssm_key>!)Added cssm_context_attribute_value.init(KRProfile: UnsafeMutablePointer<cssm_kr_profile>!)Added cssm_context_attribute_value.init(Range: UnsafeMutablePointer<cssm_range>!)Added cssm_context_attribute_value.init(String: UnsafeMutablePointer<Int8>!)Added cssm_context_attribute_value.init(Version: UnsafeMutablePointer<cssm_version>!)Added cssm_crypto_data.init(Param: cssm_data, Callback: Security.CSSM_CALLBACK!, CallerCtx: UnsafeMutableRawPointer!)Added [cssm_data.init(Length: CSSM_SIZE, Data: UnsafeMutablePointer<uint8>!)](https://developer.apple.com/documentation/security/cssm_data/1397180-init)Added cssm_db_attribute_data.init(Info: CSSM_DB_ATTRIBUTE_INFO, NumberOfValues: uint32, Value: UnsafeMutablePointer<cssm_data>!)Added cssm_db_attribute_label.init(AttributeName: UnsafeMutablePointer<Int8>!)Added cssm_db_record_attribute_data.init(DataRecordType: CSSM_DB_RECORDTYPE, SemanticInformation: uint32, NumberOfAttributes: uint32, AttributeData: UnsafeMutablePointer<cssm_db_attribute_data>!)Added cssm_db_record_attribute_info.init(DataRecordType: CSSM_DB_RECORDTYPE, NumberOfAttributes: uint32, AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR!)Added cssm_db_record_index_info.init(DataRecordType: CSSM_DB_RECORDTYPE, NumberOfIndexes: uint32, IndexInfo: UnsafeMutablePointer<cssm_db_index_info>!)Added cssm_db_schema_attribute_info.init(AttributeId: uint32, AttributeName: UnsafeMutablePointer<Int8>!, AttributeNameID: CSSM_OID, DataType: CSSM_DB_ATTRIBUTE_FORMAT)Added cssm_dbinfo.init(NumberOfRecordTypes: uint32, DefaultParsingModules: UnsafeMutablePointer<cssm_db_parsing_module_info>!, RecordAttributeNames: UnsafeMutablePointer<cssm_db_record_attribute_info>!, RecordIndexes: UnsafeMutablePointer<cssm_db_record_index_info>!, IsLocal: CSSM_BOOL, AccessPath: UnsafeMutablePointer<Int8>!, Reserved: UnsafeMutableRawPointer!)Added cssm_dl_db_list.init(NumHandles: uint32, DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>!)Added cssm_evidence.init(EvidenceForm: CSSM_EVIDENCE_FORM, Evidence: UnsafeMutableRawPointer!)Added cssm_fieldgroup.init(NumberOfFields: Int32, Fields: UnsafeMutablePointer<cssm_field>!)Added cssm_kr_name.init(Type: uint8, Length: uint8, Name: UnsafeMutablePointer<Int8>!)Added cssm_kr_policy_info.init(krbNotAllowed: CSSM_BOOL, numberOfEntries: uint32, policyEntry: UnsafeMutablePointer<cssm_kr_policy_list_item>!)Added cssm_kr_profile.init(UserName: cssm_kr_name, UserCertificate: CSSM_CERTGROUP_PTR!, KRSCertChain: CSSM_CERTGROUP_PTR!, LE_KRANum: uint8, LE_KRACertChainList: CSSM_CERTGROUP_PTR!, ENT_KRANum: uint8, ENT_KRACertChainList: CSSM_CERTGROUP_PTR!, INDIV_KRANum: uint8, INDIV_KRACertChainList: CSSM_CERTGROUP_PTR!, INDIV_AuthenticationInfo: UnsafeMutablePointer<cssm_data>!, KRSPFlags: uint32, KRSPExtensions: UnsafeMutablePointer<cssm_data>!)Added cssm_krsubservice.init(SubServiceId: uint32, Description: UnsafeMutablePointer<Int8>!, WrappedProduct: cssm_kr_wrappedproductinfo)Added [cssm_list.init(ListType: CSSM_LIST_TYPE, Head: CSSM_LIST_ELEMENT_PTR!, Tail: CSSM_LIST_ELEMENT_PTR!)](https://developer.apple.com/documentation/security/cssm_list/1395497-init)Added cssm_list_element.init(NextElement: UnsafeMutablePointer<cssm_list_element>!, WordID: CSSM_WORDID_TYPE, ElementType: CSSM_LIST_ELEMENT_TYPE, Element: cssm_list_element.__Unnamed_union_Element)Added cssm_manager_registration_info.init(Initialize: ( (uint32, uint32) -> CSSM_RETURN)!, Terminate: ( () -> CSSM_RETURN)!, RegisterDispatchTable: ( (UnsafeMutablePointer<cssm_state_funcs>?) -> CSSM_RETURN)!, DeregisterDispatchTable: ( () -> CSSM_RETURN)!, EventNotifyManager: ( (UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)!, RefreshFunctionTable: ( (UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)!)Added [cssm_memory_funcs.init(malloc_func: Security.CSSM_MALLOC!, free_func: Security.CSSM_FREE!, realloc_func: Security.CSSM_REALLOC!, calloc_func: Security.CSSM_CALLOC!, AllocRef: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/security/cssm_memory_funcs/1792121-init)Added cssm_module_funcs.init(ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs: uint32, ServiceFuncs: UnsafePointer<Security.CSSM_PROC_ADDR?>!)Added [cssm_name_list.init(NumStrings: uint32, String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!)](https://developer.apple.com/documentation/security/cssm_name_list/1401788-init)Added [cssm_parsed_cert.init(CertType: CSSM_CERT_TYPE, ParsedCertFormat: CSSM_CERT_PARSE_FORMAT, ParsedCert: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/security/cssm_parsed_cert/1395174-init)Added [cssm_parsed_crl.init(CrlType: CSSM_CRL_TYPE, ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT, ParsedCrl: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/security/cssm_parsed_crl/1394664-init)Added cssm_query.init(RecordType: CSSM_DB_RECORDTYPE, Conjunctive: CSSM_DB_CONJUNCTIVE, NumSelectionPredicates: uint32, SelectionPredicate: UnsafeMutablePointer<cssm_selection_predicate>!, QueryLimits: cssm_query_limits, QueryFlags: CSSM_QUERY_FLAGS)Added cssm_resource_control_context.init(AccessCred: UnsafeMutablePointer<cssm_access_credentials>!, InitialAclEntry: cssm_acl_entry_input)Added cssm_sample.init(TypedSample: cssm_list, Verifier: UnsafePointer<cssm_subservice_uid>!)Added cssm_samplegroup.init(NumberOfSamples: uint32, Samples: UnsafePointer<cssm_sample>!)Added cssm_spi_ac_funcs.init(AuthCompute: ( (CSSM_AC_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafePointer<cssm_tuplegroup>?, uint32, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafeMutablePointer<cssm_tuplegroup>?) -> CSSM_RETURN)!, PassThrough: ( (CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!)Added cssm_spi_cl_funcs.init(CertCreateTemplate: ( (CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertGetAllTemplateFields: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CertSign: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertVerify: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)!, CertVerifyWithKey: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, CertGetFirstFieldValue: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertGetNextFieldValue: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertAbortQuery: ( (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGetKeyInfo: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_key>?>?) -> CSSM_RETURN)!, CertGetAllFields: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, FreeFields: ( (CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, FreeFieldValue: ( (CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertCache: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, CertGetFirstCachedFieldValue: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertGetNextCachedFieldValue: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertAbortCache: ( (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGroupToSignedBundle: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_cert_bundle_header>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertGroupFromVerifiedBundle: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_cert_bundle>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, CertDescribeFormat: ( (CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)!, CrlCreateTemplate: ( (CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlSetFields: ( (CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlAddCert: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlRemoveCert: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlSign: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlVerify: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)!, CrlVerifyWithKey: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, IsCertInCrl: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!, CrlGetFirstFieldValue: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlGetNextFieldValue: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlAbortQuery: ( (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlGetAllFields: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CrlCache: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, IsCertInCachedCrl: ( (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlGetFirstCachedFieldValue: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlGetNextCachedFieldValue: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlGetAllCachedRecordFields: ( (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CrlAbortCache: ( (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlDescribeFormat: ( (CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)!, PassThrough: ( (CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!)Added cssm_spi_csp_funcs.init(EventNotify: ( (CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, QuerySize: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_BOOL, uint32, UnsafeMutablePointer<cssm_query_size_data>?) -> CSSM_RETURN)!, SignData: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, SignDataInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, SignDataUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, SignDataFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyData: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyDataInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, VerifyDataUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, VerifyDataFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, DigestData: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, DigestDataInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, DigestDataUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, DigestDataClone: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!, DigestDataFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GenerateMac: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GenerateMacInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, GenerateMacUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, GenerateMacFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyMac: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyMacInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, VerifyMacUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, VerifyMacFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, EncryptData: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)!, EncryptDataFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, DecryptData: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataInit: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataUpdate: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)!, DecryptDataFinal: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, QueryKeySizeInBits: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key_size>?) -> CSSM_RETURN)!, GenerateKey: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateKeyPair: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_key>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateRandom: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GenerateAlgorithmParams: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR?>?) -> CSSM_RETURN)!, WrapKey: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_data>?, CSSM_WRAP_KEY_PTR?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, UnwrapKey: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafePointer<CSSM_WRAP_KEY>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DeriveKey: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)!, FreeKey: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<cssm_key>?, CSSM_BOOL) -> CSSM_RETURN)!, PassThrough: ( (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!, Login: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_data>?, UnsafeRawPointer?) -> CSSM_RETURN)!, Logout: ( (CSSM_CSP_HANDLE) -> CSSM_RETURN)!, ChangeLoginAcl: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)!, ObtainPrivateKeyFromPublicKey: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)!, RetrieveUniqueId: ( (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, RetrieveCounter: ( (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyDevice: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, GetTimeValue: ( (CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GetOperationalStatistics: ( (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_csp_operational_statistics>?) -> CSSM_RETURN)!, GetLoginAcl: ( (CSSM_CSP_HANDLE, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!, GetKeyAcl: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!, ChangeKeyAcl: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?, UnsafePointer<cssm_key>?) -> CSSM_RETURN)!, GetKeyOwner: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, ChangeKeyOwner: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, GetLoginOwner: ( (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, ChangeLoginOwner: ( (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!)Added cssm_spi_dl_funcs.init(DbOpen: ( (CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!, DbClose: ( (cssm_dl_db_handle) -> CSSM_RETURN)!, DbCreate: ( (CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_dbinfo>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_resource_control_context>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!, DbDelete: ( (CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)!, CreateRelation: ( (cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)!, DestroyRelation: ( (cssm_dl_db_handle, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!, Authenticate: ( (cssm_dl_db_handle, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)!, GetDbAcl: ( (cssm_dl_db_handle, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!, ChangeDbAcl: ( (cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)!, GetDbOwner: ( (cssm_dl_db_handle, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, ChangeDbOwner: ( (cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, GetDbNames: ( (CSSM_DL_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)!, GetDbNameFromHandle: ( (cssm_dl_db_handle, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)!, FreeNameList: ( (CSSM_DL_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)!, DataInsert: ( (cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataDelete: ( (cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, DataModify: ( (cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst: ( (cssm_dl_db_handle, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataGetNext: ( (cssm_dl_db_handle, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataAbortQuery: ( (cssm_dl_db_handle, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId: ( (cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, FreeUniqueRecord: ( (cssm_dl_db_handle, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, PassThrough: ( (cssm_dl_db_handle, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!)Added cssm_spi_kr_funcs.init(RegistrationRequest: ( (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, RegistrationRetrieve: ( (CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_kr_profile>?) -> CSSM_RETURN)!, GenerateRecoveryFields: ( (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, ProcessRecoveryFields: ( (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, RecoveryRequest: ( (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, RecoveryRetrieve: ( (CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?) -> CSSM_RETURN)!, GetRecoveredObject: ( (CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?, uint32, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, RecoveryRequestAbort: ( (CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, PassThrough: ( (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!)Added cssm_spi_tp_funcs.init(SubmitCredRequest: ( (CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<cssm_tp_request_set>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, RetrieveCredResult: ( (CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_result_set>?>?) -> CSSM_RETURN)!, ConfirmCredResult: ( (CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafePointer<cssm_tp_confirm_response>?, UnsafePointer<cssm_tp_authority_id>?) -> CSSM_RETURN)!, ReceiveConfirmation: ( (CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_confirm_response>?>?, UnsafeMutablePointer<sint32>?) -> CSSM_RETURN)!, CertReclaimKey: ( (CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?) -> CSSM_RETURN)!, CertReclaimAbort: ( (CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!, FormRequest: ( (CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_FORM_TYPE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, FormSubmit: ( (CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_authority_id>?, UnsafePointer<cssm_tp_authority_id>?, UnsafeMutablePointer<cssm_access_credentials>?) -> CSSM_RETURN)!, CertGroupVerify: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!, CertCreateTemplate: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertGetAllTemplateFields: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CertSign: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlVerify: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!, CrlCreateTemplate: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertRevoke: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, CSSM_TP_CERTCHANGE_REASON, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertRemoveFromCrlTemplate: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlSign: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, ApplyCrlToDb: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!, CertGroupConstruct: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafeRawPointer?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, CertGroupPrune: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, CertGroupToTupleGroup: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tuplegroup>?>?) -> CSSM_RETURN)!, TupleGroupToCertGroup: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, PassThrough: ( (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!)Added cssm_state_funcs.init(cssm_GetAttachFunctions: ( (CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!, cssm_ReleaseAttachFunctions: ( (CSSM_MODULE_HANDLE) -> CSSM_RETURN)!, cssm_GetAppMemoryFunctions: ( (CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_upcalls>?) -> CSSM_RETURN)!, cssm_IsFuncCallValid: ( (CSSM_MODULE_HANDLE, Security.CSSM_PROC_ADDR?, Security.CSSM_PROC_ADDR?, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>?, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!, cssm_DeregisterManagerServices: ( (UnsafePointer<cssm_guid>?) -> CSSM_RETURN)!, cssm_DeliverModuleManagerEvent: ( (UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)!)Added CSSM_TP_APPLE_EVIDENCE_INFO.init(StatusBits: CSSM_TP_APPLE_CERT_STATUS, NumStatusCodes: uint32, StatusCodes: UnsafeMutablePointer<CSSM_RETURN>!, Index: uint32, DlDbHandle: cssm_dl_db_handle, UniqueRecord: UnsafeMutablePointer<cssm_db_unique_record>!)Added cssm_tp_authority_id.init(AuthorityCert: UnsafeMutablePointer<cssm_data>!, AuthorityLocation: UnsafeMutablePointer<cssm_net_address>!)Added cssm_tp_callerauth_context.init(Policy: cssm_tp_policyinfo, VerifyTime: CSSM_TIMESTRING!, VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert: Security.CSSM_TP_VERIFICATION_RESULTS_CALLBACK!, NumberOfAnchorCerts: uint32, AnchorCerts: UnsafeMutablePointer<cssm_data>!, DBList: UnsafeMutablePointer<cssm_dl_db_list>!, CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_tp_certchange_input.init(Action: CSSM_TP_CERTCHANGE_ACTION, Reason: CSSM_TP_CERTCHANGE_REASON, CLHandle: CSSM_CL_HANDLE, Cert: UnsafeMutablePointer<cssm_data>!, ChangeInfo: UnsafeMutablePointer<cssm_field>!, StartTime: CSSM_TIMESTRING!, CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_tp_certissue_input.init(CSPSubserviceUid: cssm_subservice_uid, CLHandle: CSSM_CL_HANDLE, NumberOfTemplateFields: uint32, SubjectCertFields: UnsafeMutablePointer<cssm_field>!, MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls: uint32, ServiceControls: UnsafeMutablePointer<cssm_field>!, UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_tp_certissue_output.init(IssueStatus: CSSM_TP_CERTISSUE_STATUS, CertGroup: CSSM_CERTGROUP_PTR!, PerformedServiceRequests: CSSM_TP_SERVICES)Added cssm_tp_certnotarize_input.init(CLHandle: CSSM_CL_HANDLE, NumberOfFields: uint32, MoreFields: UnsafeMutablePointer<cssm_field>!, SignScope: UnsafeMutablePointer<cssm_field>!, ScopeSize: uint32, MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls: uint32, ServiceControls: UnsafeMutablePointer<cssm_field>!, UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_tp_certnotarize_output.init(NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS, NotarizedCertGroup: CSSM_CERTGROUP_PTR!, PerformedServiceRequests: CSSM_TP_SERVICES)Added cssm_tp_certreclaim_input.init(CLHandle: CSSM_CL_HANDLE, NumberOfSelectionFields: uint32, SelectionFields: UnsafeMutablePointer<cssm_field>!, UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_tp_certreclaim_output.init(ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS, ReclaimedCertGroup: CSSM_CERTGROUP_PTR!, KeyCacheHandle: CSSM_LONG_HANDLE)Added cssm_tp_certverify_input.init(CLHandle: CSSM_CL_HANDLE, Cert: UnsafeMutablePointer<cssm_data>!, VerifyContext: UnsafeMutablePointer<cssm_tp_verify_context>!)Added cssm_tp_certverify_output.init(VerifyStatus: CSSM_TP_CERTVERIFY_STATUS, NumberOfEvidence: uint32, Evidence: UnsafeMutablePointer<cssm_evidence>!)Added cssm_tp_confirm_response.init(NumberOfResponses: uint32, Responses: CSSM_TP_CONFIRM_STATUS_PTR!)Added cssm_tp_crlissue_input.init(CLHandle: CSSM_CL_HANDLE, CrlIdentifier: uint32, CrlThisTime: CSSM_TIMESTRING!, PolicyIdentifier: UnsafeMutablePointer<cssm_field>!, CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!)Added cssm_tp_crlissue_output.init(IssueStatus: CSSM_TP_CRLISSUE_STATUS, Crl: UnsafeMutablePointer<cssm_encoded_crl>!, CrlNextTime: CSSM_TIMESTRING!)Added cssm_tp_policyinfo.init(NumberOfPolicyIds: uint32, PolicyIds: UnsafeMutablePointer<cssm_field>!, PolicyControl: UnsafeMutableRawPointer!)Added cssm_tp_request_set.init(NumberOfRequests: uint32, Requests: UnsafeMutableRawPointer!)Added [cssm_tp_result_set.init(NumberOfResults: uint32, Results: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/security/cssm_tp_result_set/1395819-init)Added cssm_tp_verify_context.init(Action: CSSM_TP_ACTION, ActionData: cssm_data, Crls: CSSM_CRLGROUP, Cred: UnsafeMutablePointer<cssm_tp_callerauth_context>!)Added cssm_tp_verify_context_result.init(NumberOfEvidences: uint32, Evidence: UnsafeMutablePointer<cssm_evidence>!)Added cssm_tuplegroup.init(NumberOfTuples: uint32, Tuples: UnsafeMutablePointer<CSSM_TUPLE>!)Added cssm_upcalls.init(malloc_func: ( (CSSM_HANDLE, Int) -> UnsafeMutableRawPointer?)!, free_func: ( (CSSM_HANDLE, UnsafeMutableRawPointer?) -> Swift.Void)!, realloc_func: ( (CSSM_HANDLE, UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)!, calloc_func: ( (CSSM_HANDLE, Int, Int) -> UnsafeMutableRawPointer?)!, CcToHandle_func: ( (CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR?) -> CSSM_RETURN)!, GetModuleInfo_func: ( (CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<cssm_version>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_SERVICE_TYPE>?, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>?, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>?, CSSM_API_MEMORY_FUNCS_PTR?, UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)!)Added cssm_x509_extensions.init(numberOfExtensions: uint32, extensions: UnsafeMutablePointer<cssm_x509_extension>!)Added cssm_x509_name.init(numberOfRDNs: uint32, RelativeDistinguishedName: UnsafeMutablePointer<cssm_x509_rdn>!)Added cssm_x509_rdn.init(numberOfPairs: uint32, AttributeTypeAndValue: UnsafeMutablePointer<cssm_x509_type_value_pair>!)Added cssm_x509_revoked_cert_list.init(numberOfRevokedCertEntries: uint32, revokedCertEntry: UnsafeMutablePointer<cssm_x509_revoked_cert_entry>!)Added cssm_x509_tbs_certlist.init(version: cssm_data, signature: cssm_x509_algorithm_identifier, issuer: cssm_x509_name, thisUpdate: cssm_x509_time, nextUpdate: cssm_x509_time, revokedCertificates: UnsafeMutablePointer<cssm_x509_revoked_cert_list>!, extensions: cssm_x509_extensions)Added cssm_x509ext_pair.init(tagAndValue: cssm_x509_extensionTagAndValue, parsedValue: UnsafeMutableRawPointer!)Added cssm_x509ext_policyQualifiers.init(numberOfPolicyQualifiers: uint32, policyQualifier: UnsafeMutablePointer<cssm_x509ext_policyQualifierInfo>!)Added cssm_x509ext_value.init(parsedValue: UnsafeMutableRawPointer!)Added cssm_x509ext_value.init(tagAndValue: UnsafeMutablePointer<cssm_x509_extensionTagAndValue>!)Added cssm_x509ext_value.init(valuePair: UnsafeMutablePointer<cssm_x509ext_pair>!)Added [DERItem.init(data: UnsafeMutablePointer<DERByte>!, length: DERSize)](https://developer.apple.com/documentation/security/deritem/1398217-init)Added mds_funcs.init(DbOpen: ( (MDS_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!, DbClose: ( (MDS_DB_HANDLE) -> CSSM_RETURN)!, GetDbNames: ( (MDS_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)!, GetDbNameFromHandle: ( (MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)!, FreeNameList: ( (MDS_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)!, DataInsert: ( (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataDelete: ( (MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, DataModify: ( (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst: ( (MDS_DB_HANDLE, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataGetNext: ( (MDS_DB_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataAbortQuery: ( (MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId: ( (MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, FreeUniqueRecord: ( (MDS_DB_HANDLE, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, CreateRelation: ( (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)!, DestroyRelation: ( (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!)Added [SecAccessControlCreateFlags.init(rawValue: CFOptionFlags)](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1395038-init)Added [SecCSFlags.quickCheck](https://developer.apple.com/documentation/security/seccsflags/1643705-quickcheck)Added [SecKeyAlgorithm [struct]](https://developer.apple.com/documentation/security/seckeyalgorithm)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactor](https://developer.apple.com/documentation/security/seckeyalgorithm/1643706-ecdhkeyexchangecofactor)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643700-ecdhkeyexchangecofactorx963sha1)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha224)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha256)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643670-ecdhkeyexchangecofactorx963sha38)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha512)Added [SecKeyAlgorithm.ecdhKeyExchangeStandard](https://developer.apple.com/documentation/security/seckeyalgorithm/1644051-ecdhkeyexchangestandard)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643695-ecdhkeyexchangestandardx963sha1)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha224)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha256)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643783-ecdhkeyexchangestandardx963sha38)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha512)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643707-ecdsasignaturedigestx962sha1)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha224)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha256)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644044-ecdsasignaturedigestx962sha384)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha512)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha1)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643717-ecdsasignaturemessagex962sha224)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha256)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA384](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha384)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha512)Added [SecKeyAlgorithm.ecdsaSignatureRFC4754](https://developer.apple.com/documentation/security/seckeyalgorithm/1643720-ecdsasignaturerfc4754)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA1AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091904-eciesencryptioncofactorx963sha1a)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha224aesgcm)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA256AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091905-eciesencryptioncofactorx963sha25)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA384AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha384aesgcm)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA512AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091900-eciesencryptioncofactorx963sha51)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA1AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091894-eciesencryptionstandardx963sha1a)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA224AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091909-eciesencryptionstandardx963sha22)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA256AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha256aesgcm)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA384AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091903-eciesencryptionstandardx963sha38)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA512AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha512aesgcm)Added [SecKeyAlgorithm.init(rawValue: CFString)](https://developer.apple.com/documentation/security/seckeyalgorithm/1779565-init)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha1)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA1AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha1aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643788-rsaencryptionoaepsha224)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha224aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA256](https://developer.apple.com/documentation/security/seckeyalgorithm/1643688-rsaencryptionoaepsha256)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA256AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha256aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644049-rsaencryptionoaepsha384)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA384AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091906-rsaencryptionoaepsha384aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha512)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA512AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091902-rsaencryptionoaepsha512aesgcm)Added [SecKeyAlgorithm.rsaEncryptionPKCS1](https://developer.apple.com/documentation/security/seckeyalgorithm/1644055-rsaencryptionpkcs1)Added [SecKeyAlgorithm.rsaEncryptionRaw](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionraw)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15Raw](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15raw)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha1)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643784-rsasignaturedigestpkcs1v15sha224)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha256)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643724-rsasignaturedigestpkcs1v15sha384)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha512)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha1)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643795-rsasignaturemessagepkcs1v15sha22)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA256](https://developer.apple.com/documentation/security/seckeyalgorithm/1644047-rsasignaturemessagepkcs1v15sha25)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA384](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha384)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha512)Added [SecKeyAlgorithm.rsaSignatureRaw](https://developer.apple.com/documentation/security/seckeyalgorithm/1643780-rsasignatureraw)Added [SecKeyKeyExchangeParameter [struct]](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter)Added [SecKeyKeyExchangeParameter.init(rawValue: CFString)](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter/1779566-init)Added [SecKeyKeyExchangeParameter.requestedSize](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter/1643708-requestedsize)Added [SecKeyKeyExchangeParameter.sharedInfo](https://developer.apple.com/documentation/security/kseckeykeyexchangeparametersharedinfo)Added [SecKeyOperationType [enum]](https://developer.apple.com/documentation/security/seckeyoperationtype)Added [SecKeyOperationType.decrypt](https://developer.apple.com/documentation/security/seckeyoperationtype/decrypt)Added [SecKeyOperationType.encrypt](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypeencrypt)Added [SecKeyOperationType.keyExchange](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypekeyexchange)Added [SecKeyOperationType.sign](https://developer.apple.com/documentation/security/seckeyoperationtype/sign)Added [SecKeyOperationType.verify](https://developer.apple.com/documentation/security/seckeyoperationtype/verify)Added [SecKeyUsage [struct]](https://developer.apple.com/documentation/security/seckeyusage)Added [SecKeyUsage.all](https://developer.apple.com/documentation/security/seckeyusage/1643249-all)Added [SecKeyUsage.contentCommitment](https://developer.apple.com/documentation/security/seckeyusage/1643244-contentcommitment)Added [SecKeyUsage.critical](https://developer.apple.com/documentation/security/seckeyusage/1643252-critical)Added [SecKeyUsage.crlSign](https://developer.apple.com/documentation/security/seckeyusage/1643245-crlsign)Added [SecKeyUsage.dataEncipherment](https://developer.apple.com/documentation/security/seckeyusage/1643243-dataencipherment)Added [SecKeyUsage.decipherOnly](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagedecipheronly)Added [SecKeyUsage.digitalSignature](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagedigitalsignature)Added [SecKeyUsage.encipherOnly](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusageencipheronly)Added [SecKeyUsage.init(rawValue: UInt32)](https://developer.apple.com/documentation/security/seckeyusage/1644034-init)Added [SecKeyUsage.keyAgreement](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagekeyagreement)Added [SecKeyUsage.keyCertSign](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagekeycertsign)Added [SecKeyUsage.keyEncipherment](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagekeyencipherment)Added [SecKeyUsage.nonRepudiation](https://developer.apple.com/documentation/security/seckeyusage/1643256-nonrepudiation)Added [SecTrustResultType [enum]](https://developer.apple.com/documentation/security/sectrustresulttype)Added [SecTrustResultType.deny](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultdeny)Added [SecTrustResultType.fatalTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultfataltrustfailure)Added [SecTrustResultType.invalid](https://developer.apple.com/documentation/security/sectrustresulttype/invalid)Added [SecTrustResultType.otherError](https://developer.apple.com/documentation/security/sectrustresulttype/othererror)Added [SecTrustResultType.proceed](https://developer.apple.com/documentation/security/sectrustresulttype/proceed)Added [SecTrustResultType.recoverableTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultrecoverabletrustfailure)Added [SecTrustResultType.unspecified](https://developer.apple.com/documentation/security/sectrustresulttype/unspecified)Added [SSLSessionOption.allowRenegotiation](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionallowrenegotiation)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_24](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_24)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_25](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_25)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_26](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_26)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_27](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_27)Added [CSSM_APPLEFILEDL_DELETE_FILE](https://developer.apple.com/documentation/security/cssm_applefiledl_delete_file)Added [CSSM_APPLEFILEDL_MAKE_COPY](https://developer.apple.com/documentation/security/cssm_applefiledl_make_copy)Added [errSecCSBadTeamIdentifier](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadteamidentifier)Added [errSecCSInvalidAssociatedFileData](https://developer.apple.com/documentation/security/errseccsinvalidassociatedfiledata)Added [errSecCSInvalidTeamIdentifier](https://developer.apple.com/documentation/security/errseccsinvalidteamidentifier)Added [kKeychainDbSuffix](https://developer.apple.com/documentation/security/kkeychaindbsuffix)Added [kSecAttrAccessGroupToken](https://developer.apple.com/documentation/security/ksecattraccessgrouptoken)Added [kSecAttrKeyTypeECSECPrimeRandom](https://developer.apple.com/documentation/security/ksecattrkeytypeecsecprimerandom)Added [kSecAttrTokenID](https://developer.apple.com/documentation/security/ksecattrtokenid)Added [kSecCFErrorResourceSideband](https://developer.apple.com/documentation/security/kseccferrorresourcesideband)Added [kSecCSRestrictSidebandData](https://developer.apple.com/documentation/security/kseccsrestrictsidebanddata)Added [kSecGuestAttributeAudit](https://developer.apple.com/documentation/security/ksecguestattributeaudit)Added [kSecTrustCertificateTransparency](https://developer.apple.com/documentation/security/ksectrustcertificatetransparency)Added [kSecTrustCertificateTransparencyWhiteList](https://developer.apple.com/documentation/security/ksectrustcertificatetransparencywhitelist)Added [kSSLSessionConfig_anonymous](https://developer.apple.com/documentation/security/ksslsessionconfig_anonymous)Added [kSSLSessionConfig_ATSv1](https://developer.apple.com/documentation/security/ksslsessionconfig_atsv1)Added [kSSLSessionConfig_ATSv1_noPFS](https://developer.apple.com/documentation/security/ksslsessionconfig_atsv1_nopfs)Added [kSSLSessionConfig_default](https://developer.apple.com/documentation/security/ksslsessionconfig_default)Added [kSSLSessionConfig_legacy](https://developer.apple.com/documentation/security/ksslsessionconfig_legacy)Added [kSSLSessionConfig_legacy_DHE](https://developer.apple.com/documentation/security/ksslsessionconfig_legacy_dhe)Added [kSSLSessionConfig_RC4_fallback](https://developer.apple.com/documentation/security/ksslsessionconfig_rc4_fallback)Added [kSSLSessionConfig_standard](https://developer.apple.com/documentation/security/ksslsessionconfig_standard)Added [kSSLSessionConfig_TLSv1_fallback](https://developer.apple.com/documentation/security/ksslsessionconfig_tlsv1_fallback)Added [kSSLSessionConfig_TLSv1_RC4_fallback](https://developer.apple.com/documentation/security/ksslsessionconfig_tlsv1_rc4_fallback)Added [oidAnsip384r1](https://developer.apple.com/documentation/security/oidansip384r1)Added [oidAnsip521r1](https://developer.apple.com/documentation/security/oidansip521r1)Added [oidEcPrime192v1](https://developer.apple.com/documentation/security/oidecprime192v1)Added [oidEcPrime256v1](https://developer.apple.com/documentation/security/oidecprime256v1)Added [SecKeyCopyAttributes(_: SecKey) -> CFDictionary?](https://developer.apple.com/documentation/security/1643699-seckeycopyattributes)Added [SecKeyCopyExternalRepresentation(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1643698-seckeycopyexternalrepresentation)Added [SecKeyCopyKeyExchangeResult(_: SecKey, _: SecKeyAlgorithm, _: SecKey, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1644033-seckeycopykeyexchangeresult)Added [SecKeyCopyPublicKey(_: SecKey) -> SecKey?](https://developer.apple.com/documentation/security/1643774-seckeycopypublickey)Added [SecKeyCreateDecryptedData(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1644043-seckeycreatedecrypteddata)Added [SecKeyCreateEncryptedData(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1643957-seckeycreateencrypteddata)Added [SecKeyCreateRandomKey(_: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1823694-seckeycreaterandomkey)Added [SecKeyCreateSignature(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1643916-seckeycreatesignature)Added [SecKeyCreateWithData(_: CFData, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1643701-seckeycreatewithdata)Added [SecKeyIsAlgorithmSupported(_: SecKey, _: SecKeyOperationType, _: SecKeyAlgorithm) -> Bool](https://developer.apple.com/documentation/security/1644057-seckeyisalgorithmsupported)Added [SecKeyVerifySignature(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/security/1643715-seckeyverifysignature)Added [SecTaskCopySigningIdentifier(_: SecTask, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?](https://developer.apple.com/documentation/security/1643737-sectaskcopysigningidentifier)Added SECURITY_LEGACY_CSSMAdded SECURITY_LEGACY_SECURE_TRANSPORTAdded [SSLCopyRequestedPeerName(_: SSLContext, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1845288-sslcopyrequestedpeername)Added [SSLCopyRequestedPeerNameLength(_: SSLContext, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1845290-sslcopyrequestedpeernamelength)Added [SSLReHandshake(_: SSLContext) -> OSStatus](https://developer.apple.com/documentation/security/1638073-sslrehandshake)Added [SSLSetSessionConfig(_: SSLContext, _: CFString) -> OSStatus](https://developer.apple.com/documentation/security/1638095-sslsetsessionconfig)Modified [AuthorizationFlags [struct]](https://developer.apple.com/documentation/security/authorizationflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AuthorizationFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Defaults: AuthorizationFlags { get }     static var InteractionAllowed: AuthorizationFlags { get }     static var ExtendRights: AuthorizationFlags { get }     static var PartialRights: AuthorizationFlags { get }     static var DestroyRights: AuthorizationFlags { get }     static var PreAuthorize: AuthorizationFlags { get }     static var NoData: AuthorizationFlags { get } } ``` | OptionSetType |
| To | ``` struct AuthorizationFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var defaults: AuthorizationFlags { get }     static var interactionAllowed: AuthorizationFlags { get }     static var extendRights: AuthorizationFlags { get }     static var partialRights: AuthorizationFlags { get }     static var destroyRights: AuthorizationFlags { get }     static var preAuthorize: AuthorizationFlags { get }     static var noData: AuthorizationFlags { get }     func intersect(_ other: AuthorizationFlags) -> AuthorizationFlags     func exclusiveOr(_ other: AuthorizationFlags) -> AuthorizationFlags     mutating func unionInPlace(_ other: AuthorizationFlags)     mutating func intersectInPlace(_ other: AuthorizationFlags)     mutating func exclusiveOrInPlace(_ other: AuthorizationFlags)     func isSubsetOf(_ other: AuthorizationFlags) -> Bool     func isDisjointWith(_ other: AuthorizationFlags) -> Bool     func isSupersetOf(_ other: AuthorizationFlags) -> Bool     mutating func subtractInPlace(_ other: AuthorizationFlags)     func isStrictSupersetOf(_ other: AuthorizationFlags) -> Bool     func isStrictSubsetOf(_ other: AuthorizationFlags) -> Bool } extension AuthorizationFlags {     func union(_ other: AuthorizationFlags) -> AuthorizationFlags     func intersection(_ other: AuthorizationFlags) -> AuthorizationFlags     func symmetricDifference(_ other: AuthorizationFlags) -> AuthorizationFlags } extension AuthorizationFlags {     func contains(_ member: AuthorizationFlags) -> Bool     mutating func insert(_ newMember: AuthorizationFlags) -> (inserted: Bool, memberAfterInsert: AuthorizationFlags)     mutating func remove(_ member: AuthorizationFlags) -> AuthorizationFlags?     mutating func update(with newMember: AuthorizationFlags) -> AuthorizationFlags? } extension AuthorizationFlags {     convenience init()     mutating func formUnion(_ other: AuthorizationFlags)     mutating func formIntersection(_ other: AuthorizationFlags)     mutating func formSymmetricDifference(_ other: AuthorizationFlags) } extension AuthorizationFlags {     convenience init<S : Sequence where S.Iterator.Element == AuthorizationFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AuthorizationFlags...)     mutating func subtract(_ other: AuthorizationFlags)     func isSubset(of other: AuthorizationFlags) -> Bool     func isSuperset(of other: AuthorizationFlags) -> Bool     func isDisjoint(with other: AuthorizationFlags) -> Bool     func subtracting(_ other: AuthorizationFlags) -> AuthorizationFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AuthorizationFlags) -> Bool     func isStrictSubset(of other: AuthorizationFlags) -> Bool } ``` | OptionSet |

Modified [AuthorizationFlags.destroyRights](https://developer.apple.com/documentation/security/authorizationflags/1397545-destroyrights)

|  | Declaration |
| --- | --- |
| From | ``` static var DestroyRights: AuthorizationFlags { get } ``` |
| To | ``` static var destroyRights: AuthorizationFlags { get } ``` |

Modified [AuthorizationFlags.extendRights](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagextendrights)

|  | Declaration |
| --- | --- |
| From | ``` static var ExtendRights: AuthorizationFlags { get } ``` |
| To | ``` static var extendRights: AuthorizationFlags { get } ``` |

Modified [AuthorizationFlags.interactionAllowed](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflaginteractionallowed)

|  | Declaration |
| --- | --- |
| From | ``` static var InteractionAllowed: AuthorizationFlags { get } ``` |
| To | ``` static var interactionAllowed: AuthorizationFlags { get } ``` |

Modified [AuthorizationFlags.noData](https://developer.apple.com/documentation/security/authorizationflags/kauthorizationflagnodata)

|  | Declaration |
| --- | --- |
| From | ``` static var NoData: AuthorizationFlags { get } ``` |
| To | ``` static var noData: AuthorizationFlags { get } ``` |

Modified [AuthorizationFlags.partialRights](https://developer.apple.com/documentation/security/authorizationflags/1394760-partialrights)

|  | Declaration |
| --- | --- |
| From | ``` static var PartialRights: AuthorizationFlags { get } ``` |
| To | ``` static var partialRights: AuthorizationFlags { get } ``` |

Modified [AuthorizationFlags.preAuthorize](https://developer.apple.com/documentation/security/authorizationflags/1395827-preauthorize)

|  | Declaration |
| --- | --- |
| From | ``` static var PreAuthorize: AuthorizationFlags { get } ``` |
| To | ``` static var preAuthorize: AuthorizationFlags { get } ``` |

Modified [AuthorizationItem [struct]](https://developer.apple.com/documentation/security/authorizationitem)

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationItem {     var name: AuthorizationString     var valueLength: Int     var value: UnsafeMutablePointer<Void>     var flags: UInt32 } ``` |
| To | ``` struct AuthorizationItem {     var name: AuthorizationString     var valueLength: Int     var value: UnsafeMutableRawPointer?     var flags: UInt32 } ``` |

Modified [AuthorizationItem.value](https://developer.apple.com/documentation/security/authorizationitem/1395014-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafeMutablePointer<Void> ``` |
| To | ``` var value: UnsafeMutableRawPointer? ``` |

Modified [AuthorizationItemSet [struct]](https://developer.apple.com/documentation/security/authorizationitemset)

|  | Declaration |
| --- | --- |
| From | ``` struct AuthorizationItemSet {     var count: UInt32     var items: UnsafeMutablePointer<AuthorizationItem> } ``` |
| To | ``` struct AuthorizationItemSet {     var count: UInt32     var items: UnsafeMutablePointer<AuthorizationItem>?     init()     init(count count: UInt32, items items: UnsafeMutablePointer<AuthorizationItem>?) } ``` |

Modified [AuthorizationItemSet.items](https://developer.apple.com/documentation/security/authorizationitemset/1397498-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: UnsafeMutablePointer<AuthorizationItem> ``` |
| To | ``` var items: UnsafeMutablePointer<AuthorizationItem>? ``` |

Modified [CMSCertificateChainMode [enum]](https://developer.apple.com/documentation/security/cmscertificatechainmode)

|  | Declaration |
| --- | --- |
| From | ``` enum CMSCertificateChainMode : UInt32 {     case None     case SignerOnly     case Chain     case ChainWithRoot } ``` |
| To | ``` enum CMSCertificateChainMode : UInt32 {     case none     case signerOnly     case chain     case chainWithRoot } ``` |

Modified [CMSCertificateChainMode.chain](https://developer.apple.com/documentation/security/cmscertificatechainmode/chain)

|  | Declaration |
| --- | --- |
| From | ``` case Chain ``` |
| To | ``` case chain ``` |

Modified [CMSCertificateChainMode.chainWithRoot](https://developer.apple.com/documentation/security/cmscertificatechainmode/chainwithroot)

|  | Declaration |
| --- | --- |
| From | ``` case ChainWithRoot ``` |
| To | ``` case chainWithRoot ``` |

Modified [CMSCertificateChainMode.none](https://developer.apple.com/documentation/security/cmscertificatechainmode/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CMSCertificateChainMode.signerOnly](https://developer.apple.com/documentation/security/cmscertificatechainmode/signeronly)

|  | Declaration |
| --- | --- |
| From | ``` case SignerOnly ``` |
| To | ``` case signerOnly ``` |

Modified [CMSSignedAttributes [enum]](https://developer.apple.com/documentation/security/cmssignedattributes)

|  | Declaration |
| --- | --- |
| From | ``` enum CMSSignedAttributes : UInt32 {     case AttrNone     case AttrSmimeCapabilities     case AttrSmimeEncryptionKeyPrefs     case AttrSmimeMSEncryptionKeyPrefs     case AttrSigningTime     case AttrAppleCodesigningHashAgility } ``` |
| To | ``` enum CMSSignedAttributes : UInt32 {     case attrNone     case attrSmimeCapabilities     case attrSmimeEncryptionKeyPrefs     case attrSmimeMSEncryptionKeyPrefs     case attrSigningTime     case attrAppleCodesigningHashAgility } ``` |

Modified [CMSSignedAttributes.attrAppleCodesigningHashAgility](https://developer.apple.com/documentation/security/cmssignedattributes/1387155-attrapplecodesigninghashagility)

|  | Declaration |
| --- | --- |
| From | ``` case AttrAppleCodesigningHashAgility ``` |
| To | ``` case attrAppleCodesigningHashAgility ``` |

Modified [CMSSignedAttributes.attrNone](https://developer.apple.com/documentation/security/cmssignedattributes/kcmsattrnone)

|  | Declaration |
| --- | --- |
| From | ``` case AttrNone ``` |
| To | ``` case attrNone ``` |

Modified [CMSSignedAttributes.attrSigningTime](https://developer.apple.com/documentation/security/cmssignedattributes/1387157-attrsigningtime)

|  | Declaration |
| --- | --- |
| From | ``` case AttrSigningTime ``` |
| To | ``` case attrSigningTime ``` |

Modified [CMSSignedAttributes.attrSmimeCapabilities](https://developer.apple.com/documentation/security/cmssignedattributes/1387181-attrsmimecapabilities)

|  | Declaration |
| --- | --- |
| From | ``` case AttrSmimeCapabilities ``` |
| To | ``` case attrSmimeCapabilities ``` |

Modified [CMSSignedAttributes.attrSmimeEncryptionKeyPrefs](https://developer.apple.com/documentation/security/cmssignedattributes/1387149-attrsmimeencryptionkeyprefs)

|  | Declaration |
| --- | --- |
| From | ``` case AttrSmimeEncryptionKeyPrefs ``` |
| To | ``` case attrSmimeEncryptionKeyPrefs ``` |

Modified [CMSSignedAttributes.attrSmimeMSEncryptionKeyPrefs](https://developer.apple.com/documentation/security/cmssignedattributes/kcmsattrsmimemsencryptionkeyprefs)

|  | Declaration |
| --- | --- |
| From | ``` case AttrSmimeMSEncryptionKeyPrefs ``` |
| To | ``` case attrSmimeMSEncryptionKeyPrefs ``` |

Modified [CMSSignerStatus [enum]](https://developer.apple.com/documentation/security/cmssignerstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CMSSignerStatus : UInt32 {     case Unsigned     case Valid     case NeedsDetachedContent     case InvalidSignature     case InvalidCert     case InvalidIndex } ``` |
| To | ``` enum CMSSignerStatus : UInt32 {     case unsigned     case valid     case needsDetachedContent     case invalidSignature     case invalidCert     case invalidIndex } ``` |

Modified [CMSSignerStatus.invalidCert](https://developer.apple.com/documentation/security/cmssignerstatus/invalidcert)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidCert ``` |
| To | ``` case invalidCert ``` |

Modified [CMSSignerStatus.invalidIndex](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignerinvalidindex)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidIndex ``` |
| To | ``` case invalidIndex ``` |

Modified [CMSSignerStatus.invalidSignature](https://developer.apple.com/documentation/security/cmssignerstatus/invalidsignature)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidSignature ``` |
| To | ``` case invalidSignature ``` |

Modified [CMSSignerStatus.needsDetachedContent](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignerneedsdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` case NeedsDetachedContent ``` |
| To | ``` case needsDetachedContent ``` |

Modified [CMSSignerStatus.unsigned](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignerunsigned)

|  | Declaration |
| --- | --- |
| From | ``` case Unsigned ``` |
| To | ``` case unsigned ``` |

Modified [CMSSignerStatus.valid](https://developer.apple.com/documentation/security/cmssignerstatus/kcmssignervalid)

|  | Declaration |
| --- | --- |
| From | ``` case Valid ``` |
| To | ``` case valid ``` |

Modified cssm_access_credentials [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_access_credentials {     var EntryTag: CSSM_STRING     var BaseCerts: CSSM_BASE_CERTS     var Samples: CSSM_SAMPLEGROUP     var Callback: CSSM_CHALLENGE_CALLBACK!     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(EntryTag EntryTag: CSSM_STRING, BaseCerts BaseCerts: CSSM_BASE_CERTS, Samples Samples: CSSM_SAMPLEGROUP, Callback Callback: CSSM_CHALLENGE_CALLBACK!, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_access_credentials {     var EntryTag: Security.CSSM_STRING     var BaseCerts: cssm_base_certs     var Samples: cssm_samplegroup     var Callback: Security.CSSM_CHALLENGE_CALLBACK!     var CallerCtx: UnsafeMutableRawPointer!     init()     init(EntryTag EntryTag: Security.CSSM_STRING, BaseCerts BaseCerts: cssm_base_certs, Samples Samples: cssm_samplegroup, Callback Callback: Security.CSSM_CHALLENGE_CALLBACK!, CallerCtx CallerCtx: UnsafeMutableRawPointer!) } ``` |

Modified cssm_access_credentials.BaseCerts

|  | Declaration |
| --- | --- |
| From | ``` var BaseCerts: CSSM_BASE_CERTS ``` |
| To | ``` var BaseCerts: cssm_base_certs ``` |

Modified cssm_access_credentials.Callback

|  | Declaration |
| --- | --- |
| From | ``` var Callback: CSSM_CHALLENGE_CALLBACK! ``` |
| To | ``` var Callback: Security.CSSM_CHALLENGE_CALLBACK! ``` |

Modified cssm_access_credentials.CallerCtx

|  | Declaration |
| --- | --- |
| From | ``` var CallerCtx: UnsafeMutablePointer<Void> ``` |
| To | ``` var CallerCtx: UnsafeMutableRawPointer! ``` |

Modified cssm_access_credentials.EntryTag

|  | Declaration |
| --- | --- |
| From | ``` var EntryTag: CSSM_STRING ``` |
| To | ``` var EntryTag: Security.CSSM_STRING ``` |

Modified cssm_access_credentials.Samples

|  | Declaration |
| --- | --- |
| From | ``` var Samples: CSSM_SAMPLEGROUP ``` |
| To | ``` var Samples: cssm_samplegroup ``` |

Modified cssm_acl_edit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_edit {     var EditMode: CSSM_ACL_EDIT_MODE     var OldEntryHandle: CSSM_ACL_HANDLE     var NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT>     init()     init(EditMode EditMode: CSSM_ACL_EDIT_MODE, OldEntryHandle OldEntryHandle: CSSM_ACL_HANDLE, NewEntry NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT>) } ``` |
| To | ``` struct cssm_acl_edit {     var EditMode: CSSM_ACL_EDIT_MODE     var OldEntryHandle: CSSM_ACL_HANDLE     var NewEntry: UnsafePointer<cssm_acl_entry_input>!     init()     init(EditMode EditMode: CSSM_ACL_EDIT_MODE, OldEntryHandle OldEntryHandle: CSSM_ACL_HANDLE, NewEntry NewEntry: UnsafePointer<cssm_acl_entry_input>!) } ``` |

Modified cssm_acl_edit.NewEntry

|  | Declaration |
| --- | --- |
| From | ``` var NewEntry: UnsafePointer<CSSM_ACL_ENTRY_INPUT> ``` |
| To | ``` var NewEntry: UnsafePointer<cssm_acl_entry_input>! ``` |

Modified cssm_acl_entry_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_info {     var EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE     var EntryHandle: CSSM_ACL_HANDLE     init()     init(EntryPublicInfo EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE, EntryHandle EntryHandle: CSSM_ACL_HANDLE) } ``` |
| To | ``` struct cssm_acl_entry_info {     var EntryPublicInfo: cssm_acl_entry_prototype     var EntryHandle: CSSM_ACL_HANDLE     init()     init(EntryPublicInfo EntryPublicInfo: cssm_acl_entry_prototype, EntryHandle EntryHandle: CSSM_ACL_HANDLE) } ``` |

Modified cssm_acl_entry_info.EntryPublicInfo

|  | Declaration |
| --- | --- |
| From | ``` var EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE ``` |
| To | ``` var EntryPublicInfo: cssm_acl_entry_prototype ``` |

Modified cssm_acl_entry_info.init(EntryPublicInfo: cssm_acl_entry_prototype, EntryHandle: CSSM_ACL_HANDLE)

|  | Declaration |
| --- | --- |
| From | ``` init(EntryPublicInfo EntryPublicInfo: CSSM_ACL_ENTRY_PROTOTYPE, EntryHandle EntryHandle: CSSM_ACL_HANDLE) ``` |
| To | ``` init(EntryPublicInfo EntryPublicInfo: cssm_acl_entry_prototype, EntryHandle EntryHandle: CSSM_ACL_HANDLE) ``` |

Modified cssm_acl_entry_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_input {     var Prototype: CSSM_ACL_ENTRY_PROTOTYPE     var Callback: CSSM_ACL_SUBJECT_CALLBACK!     var CallerContext: UnsafeMutablePointer<Void>     init()     init(Prototype Prototype: CSSM_ACL_ENTRY_PROTOTYPE, Callback Callback: CSSM_ACL_SUBJECT_CALLBACK!, CallerContext CallerContext: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_acl_entry_input {     var Prototype: cssm_acl_entry_prototype     var Callback: Security.CSSM_ACL_SUBJECT_CALLBACK!     var CallerContext: UnsafeMutableRawPointer!     init()     init(Prototype Prototype: cssm_acl_entry_prototype, Callback Callback: Security.CSSM_ACL_SUBJECT_CALLBACK!, CallerContext CallerContext: UnsafeMutableRawPointer!) } ``` |

Modified cssm_acl_entry_input.Callback

|  | Declaration |
| --- | --- |
| From | ``` var Callback: CSSM_ACL_SUBJECT_CALLBACK! ``` |
| To | ``` var Callback: Security.CSSM_ACL_SUBJECT_CALLBACK! ``` |

Modified cssm_acl_entry_input.CallerContext

|  | Declaration |
| --- | --- |
| From | ``` var CallerContext: UnsafeMutablePointer<Void> ``` |
| To | ``` var CallerContext: UnsafeMutableRawPointer! ``` |

Modified cssm_acl_entry_input.Prototype

|  | Declaration |
| --- | --- |
| From | ``` var Prototype: CSSM_ACL_ENTRY_PROTOTYPE ``` |
| To | ``` var Prototype: cssm_acl_entry_prototype ``` |

Modified cssm_acl_entry_prototype [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_entry_prototype {     var TypedSubject: CSSM_LIST     var Delegate: CSSM_BOOL     var Authorization: CSSM_AUTHORIZATIONGROUP     var TimeRange: CSSM_ACL_VALIDITY_PERIOD     var EntryTag: CSSM_STRING     init()     init(TypedSubject TypedSubject: CSSM_LIST, Delegate Delegate: CSSM_BOOL, Authorization Authorization: CSSM_AUTHORIZATIONGROUP, TimeRange TimeRange: CSSM_ACL_VALIDITY_PERIOD, EntryTag EntryTag: CSSM_STRING) } ``` |
| To | ``` struct cssm_acl_entry_prototype {     var TypedSubject: cssm_list     var Delegate: CSSM_BOOL     var Authorization: cssm_authorizationgroup     var TimeRange: cssm_acl_validity_period     var EntryTag: Security.CSSM_STRING     init()     init(TypedSubject TypedSubject: cssm_list, Delegate Delegate: CSSM_BOOL, Authorization Authorization: cssm_authorizationgroup, TimeRange TimeRange: cssm_acl_validity_period, EntryTag EntryTag: Security.CSSM_STRING) } ``` |

Modified cssm_acl_entry_prototype.Authorization

|  | Declaration |
| --- | --- |
| From | ``` var Authorization: CSSM_AUTHORIZATIONGROUP ``` |
| To | ``` var Authorization: cssm_authorizationgroup ``` |

Modified cssm_acl_entry_prototype.EntryTag

|  | Declaration |
| --- | --- |
| From | ``` var EntryTag: CSSM_STRING ``` |
| To | ``` var EntryTag: Security.CSSM_STRING ``` |

Modified cssm_acl_entry_prototype.init(TypedSubject: cssm_list, Delegate: CSSM_BOOL, Authorization: cssm_authorizationgroup, TimeRange: cssm_acl_validity_period, EntryTag: Security.CSSM_STRING)

|  | Declaration |
| --- | --- |
| From | ``` init(TypedSubject TypedSubject: CSSM_LIST, Delegate Delegate: CSSM_BOOL, Authorization Authorization: CSSM_AUTHORIZATIONGROUP, TimeRange TimeRange: CSSM_ACL_VALIDITY_PERIOD, EntryTag EntryTag: CSSM_STRING) ``` |
| To | ``` init(TypedSubject TypedSubject: cssm_list, Delegate Delegate: CSSM_BOOL, Authorization Authorization: cssm_authorizationgroup, TimeRange TimeRange: cssm_acl_validity_period, EntryTag EntryTag: Security.CSSM_STRING) ``` |

Modified cssm_acl_entry_prototype.TimeRange

|  | Declaration |
| --- | --- |
| From | ``` var TimeRange: CSSM_ACL_VALIDITY_PERIOD ``` |
| To | ``` var TimeRange: cssm_acl_validity_period ``` |

Modified cssm_acl_entry_prototype.TypedSubject

|  | Declaration |
| --- | --- |
| From | ``` var TypedSubject: CSSM_LIST ``` |
| To | ``` var TypedSubject: cssm_list ``` |

Modified cssm_acl_owner_prototype [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_owner_prototype {     var TypedSubject: CSSM_LIST     var Delegate: CSSM_BOOL     init()     init(TypedSubject TypedSubject: CSSM_LIST, Delegate Delegate: CSSM_BOOL) } ``` |
| To | ``` struct cssm_acl_owner_prototype {     var TypedSubject: cssm_list     var Delegate: CSSM_BOOL     init()     init(TypedSubject TypedSubject: cssm_list, Delegate Delegate: CSSM_BOOL) } ``` |

Modified cssm_acl_owner_prototype.init(TypedSubject: cssm_list, Delegate: CSSM_BOOL)

|  | Declaration |
| --- | --- |
| From | ``` init(TypedSubject TypedSubject: CSSM_LIST, Delegate Delegate: CSSM_BOOL) ``` |
| To | ``` init(TypedSubject TypedSubject: cssm_list, Delegate Delegate: CSSM_BOOL) ``` |

Modified cssm_acl_owner_prototype.TypedSubject

|  | Declaration |
| --- | --- |
| From | ``` var TypedSubject: CSSM_LIST ``` |
| To | ``` var TypedSubject: cssm_list ``` |

Modified cssm_acl_validity_period [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_acl_validity_period {     var StartDate: CSSM_DATA     var EndDate: CSSM_DATA     init()     init(StartDate StartDate: CSSM_DATA, EndDate EndDate: CSSM_DATA) } ``` |
| To | ``` struct cssm_acl_validity_period {     var StartDate: cssm_data     var EndDate: cssm_data     init()     init(StartDate StartDate: cssm_data, EndDate EndDate: cssm_data) } ``` |

Modified cssm_acl_validity_period.EndDate

|  | Declaration |
| --- | --- |
| From | ``` var EndDate: CSSM_DATA ``` |
| To | ``` var EndDate: cssm_data ``` |

Modified cssm_acl_validity_period.init(StartDate: cssm_data, EndDate: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(StartDate StartDate: CSSM_DATA, EndDate EndDate: CSSM_DATA) ``` |
| To | ``` init(StartDate StartDate: cssm_data, EndDate EndDate: cssm_data) ``` |

Modified cssm_acl_validity_period.StartDate

|  | Declaration |
| --- | --- |
| From | ``` var StartDate: CSSM_DATA ``` |
| To | ``` var StartDate: cssm_data ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_CL_CSR_REQUEST {     var subjectNameX509: CSSM_X509_NAME_PTR     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var cspHand: CSSM_CSP_HANDLE     var subjectPublicKey: UnsafePointer<CSSM_KEY>     var subjectPrivateKey: UnsafePointer<CSSM_KEY>     var challengeString: UnsafePointer<Int8>     init()     init(subjectNameX509 subjectNameX509: CSSM_X509_NAME_PTR, signatureAlg signatureAlg: CSSM_ALGORITHMS, signatureOid signatureOid: CSSM_OID, cspHand cspHand: CSSM_CSP_HANDLE, subjectPublicKey subjectPublicKey: UnsafePointer<CSSM_KEY>, subjectPrivateKey subjectPrivateKey: UnsafePointer<CSSM_KEY>, challengeString challengeString: UnsafePointer<Int8>) } ``` |
| To | ``` struct CSSM_APPLE_CL_CSR_REQUEST {     var subjectNameX509: UnsafeMutablePointer<cssm_x509_name>!     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var cspHand: CSSM_CSP_HANDLE     var subjectPublicKey: UnsafePointer<cssm_key>!     var subjectPrivateKey: UnsafePointer<cssm_key>!     var challengeString: UnsafePointer<Int8>!     init()     init(subjectNameX509 subjectNameX509: UnsafeMutablePointer<cssm_x509_name>!, signatureAlg signatureAlg: CSSM_ALGORITHMS, signatureOid signatureOid: CSSM_OID, cspHand cspHand: CSSM_CSP_HANDLE, subjectPublicKey subjectPublicKey: UnsafePointer<cssm_key>!, subjectPrivateKey subjectPrivateKey: UnsafePointer<cssm_key>!, challengeString challengeString: UnsafePointer<Int8>!) } ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.challengeString

|  | Declaration |
| --- | --- |
| From | ``` var challengeString: UnsafePointer<Int8> ``` |
| To | ``` var challengeString: UnsafePointer<Int8>! ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.subjectNameX509

|  | Declaration |
| --- | --- |
| From | ``` var subjectNameX509: CSSM_X509_NAME_PTR ``` |
| To | ``` var subjectNameX509: UnsafeMutablePointer<cssm_x509_name>! ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.subjectPrivateKey

|  | Declaration |
| --- | --- |
| From | ``` var subjectPrivateKey: UnsafePointer<CSSM_KEY> ``` |
| To | ``` var subjectPrivateKey: UnsafePointer<cssm_key>! ``` |

Modified CSSM_APPLE_CL_CSR_REQUEST.subjectPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var subjectPublicKey: UnsafePointer<CSSM_KEY> ``` |
| To | ``` var subjectPublicKey: UnsafePointer<cssm_key>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_CERT_REQUEST {     var cspHand: CSSM_CSP_HANDLE     var clHand: CSSM_CL_HANDLE     var serialNumber: uint32     var numSubjectNames: uint32     var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>     var numIssuerNames: uint32     var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>     var issuerNameX509: CSSM_X509_NAME_PTR     var certPublicKey: UnsafePointer<CSSM_KEY>     var issuerPrivateKey: UnsafePointer<CSSM_KEY>     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var notBefore: uint32     var notAfter: uint32     var numExtensions: uint32     var extensions: UnsafeMutablePointer<CE_DataAndType>     var challengeString: UnsafePointer<Int8>     init()     init(cspHand cspHand: CSSM_CSP_HANDLE, clHand clHand: CSSM_CL_HANDLE, serialNumber serialNumber: uint32, numSubjectNames numSubjectNames: uint32, subjectNames subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, numIssuerNames numIssuerNames: uint32, issuerNames issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>, issuerNameX509 issuerNameX509: CSSM_X509_NAME_PTR, certPublicKey certPublicKey: UnsafePointer<CSSM_KEY>, issuerPrivateKey issuerPrivateKey: UnsafePointer<CSSM_KEY>, signatureAlg signatureAlg: CSSM_ALGORITHMS, signatureOid signatureOid: CSSM_OID, notBefore notBefore: uint32, notAfter notAfter: uint32, numExtensions numExtensions: uint32, extensions extensions: UnsafeMutablePointer<CE_DataAndType>, challengeString challengeString: UnsafePointer<Int8>) } ``` |
| To | ``` struct CSSM_APPLE_TP_CERT_REQUEST {     var cspHand: CSSM_CSP_HANDLE     var clHand: CSSM_CL_HANDLE     var serialNumber: uint32     var numSubjectNames: uint32     var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!     var numIssuerNames: uint32     var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!     var issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!     var certPublicKey: UnsafePointer<cssm_key>!     var issuerPrivateKey: UnsafePointer<cssm_key>!     var signatureAlg: CSSM_ALGORITHMS     var signatureOid: CSSM_OID     var notBefore: uint32     var notAfter: uint32     var numExtensions: uint32     var extensions: UnsafeMutablePointer<__CE_DataAndType>!     var challengeString: UnsafePointer<Int8>!     init()     init(cspHand cspHand: CSSM_CSP_HANDLE, clHand clHand: CSSM_CL_HANDLE, serialNumber serialNumber: uint32, numSubjectNames numSubjectNames: uint32, subjectNames subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, numIssuerNames numIssuerNames: uint32, issuerNames issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, issuerNameX509 issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!, certPublicKey certPublicKey: UnsafePointer<cssm_key>!, issuerPrivateKey issuerPrivateKey: UnsafePointer<cssm_key>!, signatureAlg signatureAlg: CSSM_ALGORITHMS, signatureOid signatureOid: CSSM_OID, notBefore notBefore: uint32, notAfter notAfter: uint32, numExtensions numExtensions: uint32, extensions extensions: UnsafeMutablePointer<__CE_DataAndType>!, challengeString challengeString: UnsafePointer<Int8>!) } ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.certPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var certPublicKey: UnsafePointer<CSSM_KEY> ``` |
| To | ``` var certPublicKey: UnsafePointer<cssm_key>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.challengeString

|  | Declaration |
| --- | --- |
| From | ``` var challengeString: UnsafePointer<Int8> ``` |
| To | ``` var challengeString: UnsafePointer<Int8>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.extensions

|  | Declaration |
| --- | --- |
| From | ``` var extensions: UnsafeMutablePointer<CE_DataAndType> ``` |
| To | ``` var extensions: UnsafeMutablePointer<__CE_DataAndType>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.issuerNames

|  | Declaration |
| --- | --- |
| From | ``` var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID> ``` |
| To | ``` var issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.issuerNameX509

|  | Declaration |
| --- | --- |
| From | ``` var issuerNameX509: CSSM_X509_NAME_PTR ``` |
| To | ``` var issuerNameX509: UnsafeMutablePointer<cssm_x509_name>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.issuerPrivateKey

|  | Declaration |
| --- | --- |
| From | ``` var issuerPrivateKey: UnsafePointer<CSSM_KEY> ``` |
| To | ``` var issuerPrivateKey: UnsafePointer<cssm_key>! ``` |

Modified CSSM_APPLE_TP_CERT_REQUEST.subjectNames

|  | Declaration |
| --- | --- |
| From | ``` var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID> ``` |
| To | ``` var subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>! ``` |

Modified CSSM_APPLE_TP_CRL_OPTIONS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_CRL_OPTIONS {     var Version: uint32     var CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS     var crlStore: CSSM_DL_DB_HANDLE_PTR     init()     init(Version Version: uint32, CrlFlags CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore crlStore: CSSM_DL_DB_HANDLE_PTR) } ``` |
| To | ``` struct CSSM_APPLE_TP_CRL_OPTIONS {     var Version: uint32     var CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS     var crlStore: UnsafeMutablePointer<cssm_dl_db_handle>!     init()     init(Version Version: uint32, CrlFlags CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore crlStore: UnsafeMutablePointer<cssm_dl_db_handle>!) } ``` |

Modified CSSM_APPLE_TP_CRL_OPTIONS.crlStore

|  | Declaration |
| --- | --- |
| From | ``` var crlStore: CSSM_DL_DB_HANDLE_PTR ``` |
| To | ``` var crlStore: UnsafeMutablePointer<cssm_dl_db_handle>! ``` |

Modified CSSM_APPLE_TP_NAME_OID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_NAME_OID {     var string: UnsafePointer<Int8>     var oid: UnsafePointer<CSSM_OID>     init()     init(string string: UnsafePointer<Int8>, oid oid: UnsafePointer<CSSM_OID>) } ``` |
| To | ``` struct CSSM_APPLE_TP_NAME_OID {     var string: UnsafePointer<Int8>!     var oid: UnsafePointer<CSSM_OID>!     init()     init(string string: UnsafePointer<Int8>!, oid oid: UnsafePointer<CSSM_OID>!) } ``` |

Modified CSSM_APPLE_TP_NAME_OID.oid

|  | Declaration |
| --- | --- |
| From | ``` var oid: UnsafePointer<CSSM_OID> ``` |
| To | ``` var oid: UnsafePointer<CSSM_OID>! ``` |

Modified CSSM_APPLE_TP_NAME_OID.string

|  | Declaration |
| --- | --- |
| From | ``` var string: UnsafePointer<Int8> ``` |
| To | ``` var string: UnsafePointer<Int8>! ``` |

Modified CSSM_APPLE_TP_SMIME_OPTIONS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_SMIME_OPTIONS {     var Version: uint32     var IntendedUsage: CE_KeyUsage     var SenderEmailLen: uint32     var SenderEmail: UnsafePointer<Int8>     init()     init(Version Version: uint32, IntendedUsage IntendedUsage: CE_KeyUsage, SenderEmailLen SenderEmailLen: uint32, SenderEmail SenderEmail: UnsafePointer<Int8>) } ``` |
| To | ``` struct CSSM_APPLE_TP_SMIME_OPTIONS {     var Version: uint32     var IntendedUsage: uint16     var SenderEmailLen: uint32     var SenderEmail: UnsafePointer<Int8>!     init()     init(Version Version: uint32, IntendedUsage IntendedUsage: uint16, SenderEmailLen SenderEmailLen: uint32, SenderEmail SenderEmail: UnsafePointer<Int8>!) } ``` |

Modified CSSM_APPLE_TP_SMIME_OPTIONS.IntendedUsage

|  | Declaration |
| --- | --- |
| From | ``` var IntendedUsage: CE_KeyUsage ``` |
| To | ``` var IntendedUsage: uint16 ``` |

Modified CSSM_APPLE_TP_SMIME_OPTIONS.SenderEmail

|  | Declaration |
| --- | --- |
| From | ``` var SenderEmail: UnsafePointer<Int8> ``` |
| To | ``` var SenderEmail: UnsafePointer<Int8>! ``` |

Modified CSSM_APPLE_TP_SSL_OPTIONS [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_APPLE_TP_SSL_OPTIONS {     var Version: uint32     var ServerNameLen: uint32     var ServerName: UnsafePointer<Int8>     var Flags: uint32     init()     init(Version Version: uint32, ServerNameLen ServerNameLen: uint32, ServerName ServerName: UnsafePointer<Int8>, Flags Flags: uint32) } ``` |
| To | ``` struct CSSM_APPLE_TP_SSL_OPTIONS {     var Version: uint32     var ServerNameLen: uint32     var ServerName: UnsafePointer<Int8>!     var Flags: uint32     init()     init(Version Version: uint32, ServerNameLen ServerNameLen: uint32, ServerName ServerName: UnsafePointer<Int8>!, Flags Flags: uint32) } ``` |

Modified CSSM_APPLE_TP_SSL_OPTIONS.ServerName

|  | Declaration |
| --- | --- |
| From | ``` var ServerName: UnsafePointer<Int8> ``` |
| To | ``` var ServerName: UnsafePointer<Int8>! ``` |

Modified [cssm_applecspdl_db_change_password_parameters [struct]](https://developer.apple.com/documentation/security/cssm_applecspdl_db_change_password_parameters)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_applecspdl_db_change_password_parameters {     var accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS>     init()     init(accessCredentials accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS>) } ``` |
| To | ``` struct cssm_applecspdl_db_change_password_parameters {     var accessCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(accessCredentials accessCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_applecspdl_db_change_password_parameters.accessCredentials

|  | Declaration |
| --- | --- |
| From | ``` var accessCredentials: UnsafeMutablePointer<CSSM_ACCESS_CREDENTIALS> ``` |
| To | ``` var accessCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified [cssm_authorizationgroup [struct]](https://developer.apple.com/documentation/security/cssm_authorizationgroup)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_authorizationgroup {     var NumberOfAuthTags: uint32     var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>     init()     init(NumberOfAuthTags NumberOfAuthTags: uint32, AuthTags AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>) } ``` |
| To | ``` struct cssm_authorizationgroup {     var NumberOfAuthTags: uint32     var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>!     init()     init(NumberOfAuthTags NumberOfAuthTags: uint32, AuthTags AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>!) } ``` |

Modified cssm_authorizationgroup.AuthTags

|  | Declaration |
| --- | --- |
| From | ``` var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG> ``` |
| To | ``` var AuthTags: UnsafeMutablePointer<CSSM_ACL_AUTHORIZATION_TAG>! ``` |

Modified cssm_cert_bundle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_cert_bundle {     var BundleHeader: CSSM_CERT_BUNDLE_HEADER     var Bundle: CSSM_DATA     init()     init(BundleHeader BundleHeader: CSSM_CERT_BUNDLE_HEADER, Bundle Bundle: CSSM_DATA) } ``` |
| To | ``` struct cssm_cert_bundle {     var BundleHeader: cssm_cert_bundle_header     var Bundle: cssm_data     init()     init(BundleHeader BundleHeader: cssm_cert_bundle_header, Bundle Bundle: cssm_data) } ``` |

Modified cssm_cert_bundle.Bundle

|  | Declaration |
| --- | --- |
| From | ``` var Bundle: CSSM_DATA ``` |
| To | ``` var Bundle: cssm_data ``` |

Modified cssm_cert_bundle.BundleHeader

|  | Declaration |
| --- | --- |
| From | ``` var BundleHeader: CSSM_CERT_BUNDLE_HEADER ``` |
| To | ``` var BundleHeader: cssm_cert_bundle_header ``` |

Modified cssm_cert_bundle.init(BundleHeader: cssm_cert_bundle_header, Bundle: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(BundleHeader BundleHeader: CSSM_CERT_BUNDLE_HEADER, Bundle Bundle: CSSM_DATA) ``` |
| To | ``` init(BundleHeader BundleHeader: cssm_cert_bundle_header, Bundle Bundle: cssm_data) ``` |

Modified cssm_cert_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_cert_pair {     var EncodedCert: CSSM_ENCODED_CERT     var ParsedCert: CSSM_PARSED_CERT     init()     init(EncodedCert EncodedCert: CSSM_ENCODED_CERT, ParsedCert ParsedCert: CSSM_PARSED_CERT) } ``` |
| To | ``` struct cssm_cert_pair {     var EncodedCert: cssm_encoded_cert     var ParsedCert: cssm_parsed_cert     init()     init(EncodedCert EncodedCert: cssm_encoded_cert, ParsedCert ParsedCert: cssm_parsed_cert) } ``` |

Modified cssm_cert_pair.EncodedCert

|  | Declaration |
| --- | --- |
| From | ``` var EncodedCert: CSSM_ENCODED_CERT ``` |
| To | ``` var EncodedCert: cssm_encoded_cert ``` |

Modified cssm_cert_pair.init(EncodedCert: cssm_encoded_cert, ParsedCert: cssm_parsed_cert)

|  | Declaration |
| --- | --- |
| From | ``` init(EncodedCert EncodedCert: CSSM_ENCODED_CERT, ParsedCert ParsedCert: CSSM_PARSED_CERT) ``` |
| To | ``` init(EncodedCert EncodedCert: cssm_encoded_cert, ParsedCert ParsedCert: cssm_parsed_cert) ``` |

Modified cssm_cert_pair.ParsedCert

|  | Declaration |
| --- | --- |
| From | ``` var ParsedCert: CSSM_PARSED_CERT ``` |
| To | ``` var ParsedCert: cssm_parsed_cert ``` |

Modified cssm_certgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_certgroup {     struct __Unnamed_union_GroupList {         var CertList: CSSM_DATA_PTR         var EncodedCertList: CSSM_ENCODED_CERT_PTR         var ParsedCertList: CSSM_PARSED_CERT_PTR         var PairCertList: CSSM_CERT_PAIR_PTR         init(CertList CertList: CSSM_DATA_PTR)         init(EncodedCertList EncodedCertList: CSSM_ENCODED_CERT_PTR)         init(ParsedCertList ParsedCertList: CSSM_PARSED_CERT_PTR)         init(PairCertList PairCertList: CSSM_CERT_PAIR_PTR)         init()     }     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var NumCerts: uint32     var GroupList: cssm_certgroup.__Unnamed_union_GroupList     var CertGroupType: CSSM_CERTGROUP_TYPE     var Reserved: UnsafeMutablePointer<Void>     init()     init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, NumCerts NumCerts: uint32, GroupList GroupList: cssm_certgroup.__Unnamed_union_GroupList, CertGroupType CertGroupType: CSSM_CERTGROUP_TYPE, Reserved Reserved: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_certgroup {     struct __Unnamed_union_GroupList {         var CertList: UnsafeMutablePointer<cssm_data>!         var EncodedCertList: UnsafeMutablePointer<cssm_encoded_cert>!         var ParsedCertList: UnsafeMutablePointer<cssm_parsed_cert>!         var PairCertList: UnsafeMutablePointer<cssm_cert_pair>!         init(CertList CertList: UnsafeMutablePointer<cssm_data>!)         init(EncodedCertList EncodedCertList: UnsafeMutablePointer<cssm_encoded_cert>!)         init(ParsedCertList ParsedCertList: UnsafeMutablePointer<cssm_parsed_cert>!)         init(PairCertList PairCertList: UnsafeMutablePointer<cssm_cert_pair>!)         init()     }     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var NumCerts: uint32     var GroupList: cssm_certgroup.__Unnamed_union_GroupList     var CertGroupType: CSSM_CERTGROUP_TYPE     var Reserved: UnsafeMutableRawPointer!     init()     init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, NumCerts NumCerts: uint32, GroupList GroupList: cssm_certgroup.__Unnamed_union_GroupList, CertGroupType CertGroupType: CSSM_CERTGROUP_TYPE, Reserved Reserved: UnsafeMutableRawPointer!) } ``` |

Modified cssm_certgroup.Reserved

|  | Declaration |
| --- | --- |
| From | ``` var Reserved: UnsafeMutablePointer<Void> ``` |
| To | ``` var Reserved: UnsafeMutableRawPointer! ``` |

Modified cssm_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_context {     var ContextType: CSSM_CONTEXT_TYPE     var AlgorithmType: CSSM_ALGORITHMS     var NumberOfAttributes: uint32     var ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR     var CSPHandle: CSSM_CSP_HANDLE     var Privileged: CSSM_BOOL     var EncryptionProhibited: uint32     var WorkFactor: uint32     var Reserved: uint32     init()     init(ContextType ContextType: CSSM_CONTEXT_TYPE, AlgorithmType AlgorithmType: CSSM_ALGORITHMS, NumberOfAttributes NumberOfAttributes: uint32, ContextAttributes ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR, CSPHandle CSPHandle: CSSM_CSP_HANDLE, Privileged Privileged: CSSM_BOOL, EncryptionProhibited EncryptionProhibited: uint32, WorkFactor WorkFactor: uint32, Reserved Reserved: uint32) } ``` |
| To | ``` struct cssm_context {     var ContextType: CSSM_CONTEXT_TYPE     var AlgorithmType: CSSM_ALGORITHMS     var NumberOfAttributes: uint32     var ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR!     var CSPHandle: CSSM_CSP_HANDLE     var Privileged: CSSM_BOOL     var EncryptionProhibited: uint32     var WorkFactor: uint32     var Reserved: uint32     init()     init(ContextType ContextType: CSSM_CONTEXT_TYPE, AlgorithmType AlgorithmType: CSSM_ALGORITHMS, NumberOfAttributes NumberOfAttributes: uint32, ContextAttributes ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR!, CSPHandle CSPHandle: CSSM_CSP_HANDLE, Privileged Privileged: CSSM_BOOL, EncryptionProhibited EncryptionProhibited: uint32, WorkFactor WorkFactor: uint32, Reserved Reserved: uint32) } ``` |

Modified cssm_context.ContextAttributes

|  | Declaration |
| --- | --- |
| From | ``` var ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR ``` |
| To | ``` var ContextAttributes: CSSM_CONTEXT_ATTRIBUTE_PTR! ``` |

Modified cssm_context_attribute_value [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_context_attribute_value {     var String: UnsafeMutablePointer<Int8>     var Uint32: uint32     var AccessCredentials: CSSM_ACCESS_CREDENTIALS_PTR     var Key: CSSM_KEY_PTR     var Data: CSSM_DATA_PTR     var Padding: CSSM_PADDING     var Date: CSSM_DATE_PTR     var Range: CSSM_RANGE_PTR     var CryptoData: CSSM_CRYPTO_DATA_PTR     var Version: CSSM_VERSION_PTR     var DLDBHandle: CSSM_DL_DB_HANDLE_PTR     var KRProfile: UnsafeMutablePointer<cssm_kr_profile>     init(String String: UnsafeMutablePointer<Int8>)     init(Uint32 Uint32: uint32)     init(AccessCredentials AccessCredentials: CSSM_ACCESS_CREDENTIALS_PTR)     init(Key Key: CSSM_KEY_PTR)     init(Data Data: CSSM_DATA_PTR)     init(Padding Padding: CSSM_PADDING)     init(Date Date: CSSM_DATE_PTR)     init(Range Range: CSSM_RANGE_PTR)     init(CryptoData CryptoData: CSSM_CRYPTO_DATA_PTR)     init(Version Version: CSSM_VERSION_PTR)     init(DLDBHandle DLDBHandle: CSSM_DL_DB_HANDLE_PTR)     init(KRProfile KRProfile: UnsafeMutablePointer<cssm_kr_profile>)     init() } ``` |
| To | ``` struct cssm_context_attribute_value {     var String: UnsafeMutablePointer<Int8>!     var Uint32: uint32     var AccessCredentials: UnsafeMutablePointer<cssm_access_credentials>!     var Key: UnsafeMutablePointer<cssm_key>!     var Data: UnsafeMutablePointer<cssm_data>!     var Padding: CSSM_PADDING     var Date: UnsafeMutablePointer<cssm_date>!     var Range: UnsafeMutablePointer<cssm_range>!     var CryptoData: UnsafeMutablePointer<cssm_crypto_data>!     var Version: UnsafeMutablePointer<cssm_version>!     var DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>!     var KRProfile: UnsafeMutablePointer<cssm_kr_profile>!     init(String String: UnsafeMutablePointer<Int8>!)     init(Uint32 Uint32: uint32)     init(AccessCredentials AccessCredentials: UnsafeMutablePointer<cssm_access_credentials>!)     init(Key Key: UnsafeMutablePointer<cssm_key>!)     init(Data Data: UnsafeMutablePointer<cssm_data>!)     init(Padding Padding: CSSM_PADDING)     init(Date Date: UnsafeMutablePointer<cssm_date>!)     init(Range Range: UnsafeMutablePointer<cssm_range>!)     init(CryptoData CryptoData: UnsafeMutablePointer<cssm_crypto_data>!)     init(Version Version: UnsafeMutablePointer<cssm_version>!)     init(DLDBHandle DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>!)     init(KRProfile KRProfile: UnsafeMutablePointer<cssm_kr_profile>!)     init() } ``` |

Modified cssm_context_attribute_value.AccessCredentials

|  | Declaration |
| --- | --- |
| From | ``` var AccessCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var AccessCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_context_attribute_value.CryptoData

|  | Declaration |
| --- | --- |
| From | ``` var CryptoData: CSSM_CRYPTO_DATA_PTR ``` |
| To | ``` var CryptoData: UnsafeMutablePointer<cssm_crypto_data>! ``` |

Modified cssm_context_attribute_value.Data

|  | Declaration |
| --- | --- |
| From | ``` var Data: CSSM_DATA_PTR ``` |
| To | ``` var Data: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_context_attribute_value.Date

|  | Declaration |
| --- | --- |
| From | ``` var Date: CSSM_DATE_PTR ``` |
| To | ``` var Date: UnsafeMutablePointer<cssm_date>! ``` |

Modified cssm_context_attribute_value.DLDBHandle

|  | Declaration |
| --- | --- |
| From | ``` var DLDBHandle: CSSM_DL_DB_HANDLE_PTR ``` |
| To | ``` var DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>! ``` |

Modified cssm_context_attribute_value.Key

|  | Declaration |
| --- | --- |
| From | ``` var Key: CSSM_KEY_PTR ``` |
| To | ``` var Key: UnsafeMutablePointer<cssm_key>! ``` |

Modified cssm_context_attribute_value.KRProfile

|  | Declaration |
| --- | --- |
| From | ``` var KRProfile: UnsafeMutablePointer<cssm_kr_profile> ``` |
| To | ``` var KRProfile: UnsafeMutablePointer<cssm_kr_profile>! ``` |

Modified cssm_context_attribute_value.Range

|  | Declaration |
| --- | --- |
| From | ``` var Range: CSSM_RANGE_PTR ``` |
| To | ``` var Range: UnsafeMutablePointer<cssm_range>! ``` |

Modified cssm_context_attribute_value.String

|  | Declaration |
| --- | --- |
| From | ``` var String: UnsafeMutablePointer<Int8> ``` |
| To | ``` var String: UnsafeMutablePointer<Int8>! ``` |

Modified cssm_context_attribute_value.Version

|  | Declaration |
| --- | --- |
| From | ``` var Version: CSSM_VERSION_PTR ``` |
| To | ``` var Version: UnsafeMutablePointer<cssm_version>! ``` |

Modified cssm_crl_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crl_pair {     var EncodedCrl: CSSM_ENCODED_CRL     var ParsedCrl: CSSM_PARSED_CRL     init()     init(EncodedCrl EncodedCrl: CSSM_ENCODED_CRL, ParsedCrl ParsedCrl: CSSM_PARSED_CRL) } ``` |
| To | ``` struct cssm_crl_pair {     var EncodedCrl: cssm_encoded_crl     var ParsedCrl: cssm_parsed_crl     init()     init(EncodedCrl EncodedCrl: cssm_encoded_crl, ParsedCrl ParsedCrl: cssm_parsed_crl) } ``` |

Modified cssm_crl_pair.EncodedCrl

|  | Declaration |
| --- | --- |
| From | ``` var EncodedCrl: CSSM_ENCODED_CRL ``` |
| To | ``` var EncodedCrl: cssm_encoded_crl ``` |

Modified cssm_crl_pair.init(EncodedCrl: cssm_encoded_crl, ParsedCrl: cssm_parsed_crl)

|  | Declaration |
| --- | --- |
| From | ``` init(EncodedCrl EncodedCrl: CSSM_ENCODED_CRL, ParsedCrl ParsedCrl: CSSM_PARSED_CRL) ``` |
| To | ``` init(EncodedCrl EncodedCrl: cssm_encoded_crl, ParsedCrl ParsedCrl: cssm_parsed_crl) ``` |

Modified cssm_crl_pair.ParsedCrl

|  | Declaration |
| --- | --- |
| From | ``` var ParsedCrl: CSSM_PARSED_CRL ``` |
| To | ``` var ParsedCrl: cssm_parsed_crl ``` |

Modified cssm_crlgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crlgroup {     struct __Unnamed_union_GroupCrlList {         var CrlList: CSSM_DATA_PTR         var EncodedCrlList: CSSM_ENCODED_CRL_PTR         var ParsedCrlList: CSSM_PARSED_CRL_PTR         var PairCrlList: CSSM_CRL_PAIR_PTR         init(CrlList CrlList: CSSM_DATA_PTR)         init(EncodedCrlList EncodedCrlList: CSSM_ENCODED_CRL_PTR)         init(ParsedCrlList ParsedCrlList: CSSM_PARSED_CRL_PTR)         init(PairCrlList PairCrlList: CSSM_CRL_PAIR_PTR)         init()     }     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var NumberOfCrls: uint32     var GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList     var CrlGroupType: CSSM_CRLGROUP_TYPE     init()     init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, NumberOfCrls NumberOfCrls: uint32, GroupCrlList GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList, CrlGroupType CrlGroupType: CSSM_CRLGROUP_TYPE) } ``` |
| To | ``` struct cssm_crlgroup {     struct __Unnamed_union_GroupCrlList {         var CrlList: UnsafeMutablePointer<cssm_data>!         var EncodedCrlList: UnsafeMutablePointer<cssm_encoded_crl>!         var ParsedCrlList: UnsafeMutablePointer<cssm_parsed_crl>!         var PairCrlList: UnsafeMutablePointer<cssm_crl_pair>!         init(CrlList CrlList: UnsafeMutablePointer<cssm_data>!)         init(EncodedCrlList EncodedCrlList: UnsafeMutablePointer<cssm_encoded_crl>!)         init(ParsedCrlList ParsedCrlList: UnsafeMutablePointer<cssm_parsed_crl>!)         init(PairCrlList PairCrlList: UnsafeMutablePointer<cssm_crl_pair>!)         init()     }     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var NumberOfCrls: uint32     var GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList     var CrlGroupType: CSSM_CRLGROUP_TYPE     init()     init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, NumberOfCrls NumberOfCrls: uint32, GroupCrlList GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList, CrlGroupType CrlGroupType: CSSM_CRLGROUP_TYPE) } ``` |

Modified cssm_crypto_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crypto_data {     var Param: CSSM_DATA     var Callback: CSSM_CALLBACK!     var CallerCtx: UnsafeMutablePointer<Void>     init()     init(Param Param: CSSM_DATA, Callback Callback: CSSM_CALLBACK!, CallerCtx CallerCtx: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_crypto_data {     var Param: cssm_data     var Callback: Security.CSSM_CALLBACK!     var CallerCtx: UnsafeMutableRawPointer!     init()     init(Param Param: cssm_data, Callback Callback: Security.CSSM_CALLBACK!, CallerCtx CallerCtx: UnsafeMutableRawPointer!) } ``` |

Modified cssm_crypto_data.Callback

|  | Declaration |
| --- | --- |
| From | ``` var Callback: CSSM_CALLBACK! ``` |
| To | ``` var Callback: Security.CSSM_CALLBACK! ``` |

Modified cssm_crypto_data.CallerCtx

|  | Declaration |
| --- | --- |
| From | ``` var CallerCtx: UnsafeMutablePointer<Void> ``` |
| To | ``` var CallerCtx: UnsafeMutableRawPointer! ``` |

Modified cssm_crypto_data.Param

|  | Declaration |
| --- | --- |
| From | ``` var Param: CSSM_DATA ``` |
| To | ``` var Param: cssm_data ``` |

Modified [cssm_data [struct]](https://developer.apple.com/documentation/security/cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_data {     var Length: CSSM_SIZE     var Data: UnsafeMutablePointer<uint8>     init()     init(Length Length: CSSM_SIZE, Data Data: UnsafeMutablePointer<uint8>) } ``` |
| To | ``` struct cssm_data {     var Length: CSSM_SIZE     var Data: UnsafeMutablePointer<uint8>!     init()     init(Length Length: CSSM_SIZE, Data Data: UnsafeMutablePointer<uint8>!) } ``` |

Modified cssm_data.Data

|  | Declaration |
| --- | --- |
| From | ``` var Data: UnsafeMutablePointer<uint8> ``` |
| To | ``` var Data: UnsafeMutablePointer<uint8>! ``` |

Modified cssm_db_attribute_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_attribute_data {     var Info: CSSM_DB_ATTRIBUTE_INFO     var NumberOfValues: uint32     var Value: CSSM_DATA_PTR     init()     init(Info Info: CSSM_DB_ATTRIBUTE_INFO, NumberOfValues NumberOfValues: uint32, Value Value: CSSM_DATA_PTR) } ``` |
| To | ``` struct cssm_db_attribute_data {     var Info: CSSM_DB_ATTRIBUTE_INFO     var NumberOfValues: uint32     var Value: UnsafeMutablePointer<cssm_data>!     init()     init(Info Info: CSSM_DB_ATTRIBUTE_INFO, NumberOfValues NumberOfValues: uint32, Value Value: UnsafeMutablePointer<cssm_data>!) } ``` |

Modified cssm_db_attribute_data.Value

|  | Declaration |
| --- | --- |
| From | ``` var Value: CSSM_DATA_PTR ``` |
| To | ``` var Value: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_db_attribute_label [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_attribute_label {     var AttributeName: UnsafeMutablePointer<Int8>     var AttributeOID: CSSM_OID     var AttributeID: uint32     init(AttributeName AttributeName: UnsafeMutablePointer<Int8>)     init(AttributeOID AttributeOID: CSSM_OID)     init(AttributeID AttributeID: uint32)     init() } ``` |
| To | ``` struct cssm_db_attribute_label {     var AttributeName: UnsafeMutablePointer<Int8>!     var AttributeOID: CSSM_OID     var AttributeID: uint32     init(AttributeName AttributeName: UnsafeMutablePointer<Int8>!)     init(AttributeOID AttributeOID: CSSM_OID)     init(AttributeID AttributeID: uint32)     init() } ``` |

Modified cssm_db_attribute_label.AttributeName

|  | Declaration |
| --- | --- |
| From | ``` var AttributeName: UnsafeMutablePointer<Int8> ``` |
| To | ``` var AttributeName: UnsafeMutablePointer<Int8>! ``` |

Modified cssm_db_parsing_module_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_parsing_module_info {     var RecordType: CSSM_DB_RECORDTYPE     var ModuleSubserviceUid: CSSM_SUBSERVICE_UID     init()     init(RecordType RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid ModuleSubserviceUid: CSSM_SUBSERVICE_UID) } ``` |
| To | ``` struct cssm_db_parsing_module_info {     var RecordType: CSSM_DB_RECORDTYPE     var ModuleSubserviceUid: cssm_subservice_uid     init()     init(RecordType RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid ModuleSubserviceUid: cssm_subservice_uid) } ``` |

Modified cssm_db_parsing_module_info.init(RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid: cssm_subservice_uid)

|  | Declaration |
| --- | --- |
| From | ``` init(RecordType RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid ModuleSubserviceUid: CSSM_SUBSERVICE_UID) ``` |
| To | ``` init(RecordType RecordType: CSSM_DB_RECORDTYPE, ModuleSubserviceUid ModuleSubserviceUid: cssm_subservice_uid) ``` |

Modified cssm_db_parsing_module_info.ModuleSubserviceUid

|  | Declaration |
| --- | --- |
| From | ``` var ModuleSubserviceUid: CSSM_SUBSERVICE_UID ``` |
| To | ``` var ModuleSubserviceUid: cssm_subservice_uid ``` |

Modified cssm_db_record_attribute_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_record_attribute_data {     var DataRecordType: CSSM_DB_RECORDTYPE     var SemanticInformation: uint32     var NumberOfAttributes: uint32     var AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, SemanticInformation SemanticInformation: uint32, NumberOfAttributes NumberOfAttributes: uint32, AttributeData AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR) } ``` |
| To | ``` struct cssm_db_record_attribute_data {     var DataRecordType: CSSM_DB_RECORDTYPE     var SemanticInformation: uint32     var NumberOfAttributes: uint32     var AttributeData: UnsafeMutablePointer<cssm_db_attribute_data>!     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, SemanticInformation SemanticInformation: uint32, NumberOfAttributes NumberOfAttributes: uint32, AttributeData AttributeData: UnsafeMutablePointer<cssm_db_attribute_data>!) } ``` |

Modified cssm_db_record_attribute_data.AttributeData

|  | Declaration |
| --- | --- |
| From | ``` var AttributeData: CSSM_DB_ATTRIBUTE_DATA_PTR ``` |
| To | ``` var AttributeData: UnsafeMutablePointer<cssm_db_attribute_data>! ``` |

Modified cssm_db_record_attribute_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_record_attribute_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfAttributes: uint32     var AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, NumberOfAttributes NumberOfAttributes: uint32, AttributeInfo AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR) } ``` |
| To | ``` struct cssm_db_record_attribute_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfAttributes: uint32     var AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR!     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, NumberOfAttributes NumberOfAttributes: uint32, AttributeInfo AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR!) } ``` |

Modified cssm_db_record_attribute_info.AttributeInfo

|  | Declaration |
| --- | --- |
| From | ``` var AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR ``` |
| To | ``` var AttributeInfo: CSSM_DB_ATTRIBUTE_INFO_PTR! ``` |

Modified cssm_db_record_index_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_record_index_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfIndexes: uint32     var IndexInfo: CSSM_DB_INDEX_INFO_PTR     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, NumberOfIndexes NumberOfIndexes: uint32, IndexInfo IndexInfo: CSSM_DB_INDEX_INFO_PTR) } ``` |
| To | ``` struct cssm_db_record_index_info {     var DataRecordType: CSSM_DB_RECORDTYPE     var NumberOfIndexes: uint32     var IndexInfo: UnsafeMutablePointer<cssm_db_index_info>!     init()     init(DataRecordType DataRecordType: CSSM_DB_RECORDTYPE, NumberOfIndexes NumberOfIndexes: uint32, IndexInfo IndexInfo: UnsafeMutablePointer<cssm_db_index_info>!) } ``` |

Modified cssm_db_record_index_info.IndexInfo

|  | Declaration |
| --- | --- |
| From | ``` var IndexInfo: CSSM_DB_INDEX_INFO_PTR ``` |
| To | ``` var IndexInfo: UnsafeMutablePointer<cssm_db_index_info>! ``` |

Modified cssm_db_schema_attribute_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_schema_attribute_info {     var AttributeId: uint32     var AttributeName: UnsafeMutablePointer<Int8>     var AttributeNameID: CSSM_OID     var DataType: CSSM_DB_ATTRIBUTE_FORMAT     init()     init(AttributeId AttributeId: uint32, AttributeName AttributeName: UnsafeMutablePointer<Int8>, AttributeNameID AttributeNameID: CSSM_OID, DataType DataType: CSSM_DB_ATTRIBUTE_FORMAT) } ``` |
| To | ``` struct cssm_db_schema_attribute_info {     var AttributeId: uint32     var AttributeName: UnsafeMutablePointer<Int8>!     var AttributeNameID: CSSM_OID     var DataType: CSSM_DB_ATTRIBUTE_FORMAT     init()     init(AttributeId AttributeId: uint32, AttributeName AttributeName: UnsafeMutablePointer<Int8>!, AttributeNameID AttributeNameID: CSSM_OID, DataType DataType: CSSM_DB_ATTRIBUTE_FORMAT) } ``` |

Modified cssm_db_schema_attribute_info.AttributeName

|  | Declaration |
| --- | --- |
| From | ``` var AttributeName: UnsafeMutablePointer<Int8> ``` |
| To | ``` var AttributeName: UnsafeMutablePointer<Int8>! ``` |

Modified cssm_db_unique_record [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_db_unique_record {     var RecordLocator: CSSM_DB_INDEX_INFO     var RecordIdentifier: CSSM_DATA     init()     init(RecordLocator RecordLocator: CSSM_DB_INDEX_INFO, RecordIdentifier RecordIdentifier: CSSM_DATA) } ``` |
| To | ``` struct cssm_db_unique_record {     var RecordLocator: cssm_db_index_info     var RecordIdentifier: cssm_data     init()     init(RecordLocator RecordLocator: cssm_db_index_info, RecordIdentifier RecordIdentifier: cssm_data) } ``` |

Modified cssm_db_unique_record.init(RecordLocator: cssm_db_index_info, RecordIdentifier: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(RecordLocator RecordLocator: CSSM_DB_INDEX_INFO, RecordIdentifier RecordIdentifier: CSSM_DATA) ``` |
| To | ``` init(RecordLocator RecordLocator: cssm_db_index_info, RecordIdentifier RecordIdentifier: cssm_data) ``` |

Modified cssm_db_unique_record.RecordIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var RecordIdentifier: CSSM_DATA ``` |
| To | ``` var RecordIdentifier: cssm_data ``` |

Modified cssm_db_unique_record.RecordLocator

|  | Declaration |
| --- | --- |
| From | ``` var RecordLocator: CSSM_DB_INDEX_INFO ``` |
| To | ``` var RecordLocator: cssm_db_index_info ``` |

Modified cssm_dbinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_dbinfo {     var NumberOfRecordTypes: uint32     var DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR     var RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR     var RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR     var IsLocal: CSSM_BOOL     var AccessPath: UnsafeMutablePointer<Int8>     var Reserved: UnsafeMutablePointer<Void>     init()     init(NumberOfRecordTypes NumberOfRecordTypes: uint32, DefaultParsingModules DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR, RecordAttributeNames RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR, RecordIndexes RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR, IsLocal IsLocal: CSSM_BOOL, AccessPath AccessPath: UnsafeMutablePointer<Int8>, Reserved Reserved: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_dbinfo {     var NumberOfRecordTypes: uint32     var DefaultParsingModules: UnsafeMutablePointer<cssm_db_parsing_module_info>!     var RecordAttributeNames: UnsafeMutablePointer<cssm_db_record_attribute_info>!     var RecordIndexes: UnsafeMutablePointer<cssm_db_record_index_info>!     var IsLocal: CSSM_BOOL     var AccessPath: UnsafeMutablePointer<Int8>!     var Reserved: UnsafeMutableRawPointer!     init()     init(NumberOfRecordTypes NumberOfRecordTypes: uint32, DefaultParsingModules DefaultParsingModules: UnsafeMutablePointer<cssm_db_parsing_module_info>!, RecordAttributeNames RecordAttributeNames: UnsafeMutablePointer<cssm_db_record_attribute_info>!, RecordIndexes RecordIndexes: UnsafeMutablePointer<cssm_db_record_index_info>!, IsLocal IsLocal: CSSM_BOOL, AccessPath AccessPath: UnsafeMutablePointer<Int8>!, Reserved Reserved: UnsafeMutableRawPointer!) } ``` |

Modified cssm_dbinfo.AccessPath

|  | Declaration |
| --- | --- |
| From | ``` var AccessPath: UnsafeMutablePointer<Int8> ``` |
| To | ``` var AccessPath: UnsafeMutablePointer<Int8>! ``` |

Modified cssm_dbinfo.DefaultParsingModules

|  | Declaration |
| --- | --- |
| From | ``` var DefaultParsingModules: CSSM_DB_PARSING_MODULE_INFO_PTR ``` |
| To | ``` var DefaultParsingModules: UnsafeMutablePointer<cssm_db_parsing_module_info>! ``` |

Modified cssm_dbinfo.RecordAttributeNames

|  | Declaration |
| --- | --- |
| From | ``` var RecordAttributeNames: CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR ``` |
| To | ``` var RecordAttributeNames: UnsafeMutablePointer<cssm_db_record_attribute_info>! ``` |

Modified cssm_dbinfo.RecordIndexes

|  | Declaration |
| --- | --- |
| From | ``` var RecordIndexes: CSSM_DB_RECORD_INDEX_INFO_PTR ``` |
| To | ``` var RecordIndexes: UnsafeMutablePointer<cssm_db_record_index_info>! ``` |

Modified cssm_dbinfo.Reserved

|  | Declaration |
| --- | --- |
| From | ``` var Reserved: UnsafeMutablePointer<Void> ``` |
| To | ``` var Reserved: UnsafeMutableRawPointer! ``` |

Modified cssm_dl_db_list [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_dl_db_list {     var NumHandles: uint32     var DLDBHandle: CSSM_DL_DB_HANDLE_PTR     init()     init(NumHandles NumHandles: uint32, DLDBHandle DLDBHandle: CSSM_DL_DB_HANDLE_PTR) } ``` |
| To | ``` struct cssm_dl_db_list {     var NumHandles: uint32     var DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>!     init()     init(NumHandles NumHandles: uint32, DLDBHandle DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>!) } ``` |

Modified cssm_dl_db_list.DLDBHandle

|  | Declaration |
| --- | --- |
| From | ``` var DLDBHandle: CSSM_DL_DB_HANDLE_PTR ``` |
| To | ``` var DLDBHandle: UnsafeMutablePointer<cssm_dl_db_handle>! ``` |

Modified cssm_encoded_cert [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_encoded_cert {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var CertBlob: CSSM_DATA     init()     init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, CertBlob CertBlob: CSSM_DATA) } ``` |
| To | ``` struct cssm_encoded_cert {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var CertBlob: cssm_data     init()     init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, CertBlob CertBlob: cssm_data) } ``` |

Modified cssm_encoded_cert.CertBlob

|  | Declaration |
| --- | --- |
| From | ``` var CertBlob: CSSM_DATA ``` |
| To | ``` var CertBlob: cssm_data ``` |

Modified cssm_encoded_cert.init(CertType: CSSM_CERT_TYPE, CertEncoding: CSSM_CERT_ENCODING, CertBlob: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, CertBlob CertBlob: CSSM_DATA) ``` |
| To | ``` init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, CertBlob CertBlob: cssm_data) ``` |

Modified cssm_encoded_crl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_encoded_crl {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var CrlBlob: CSSM_DATA     init()     init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, CrlBlob CrlBlob: CSSM_DATA) } ``` |
| To | ``` struct cssm_encoded_crl {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var CrlBlob: cssm_data     init()     init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, CrlBlob CrlBlob: cssm_data) } ``` |

Modified cssm_encoded_crl.CrlBlob

|  | Declaration |
| --- | --- |
| From | ``` var CrlBlob: CSSM_DATA ``` |
| To | ``` var CrlBlob: cssm_data ``` |

Modified cssm_encoded_crl.init(CrlType: CSSM_CRL_TYPE, CrlEncoding: CSSM_CRL_ENCODING, CrlBlob: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, CrlBlob CrlBlob: CSSM_DATA) ``` |
| To | ``` init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, CrlBlob CrlBlob: cssm_data) ``` |

Modified cssm_evidence [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_evidence {     var EvidenceForm: CSSM_EVIDENCE_FORM     var Evidence: UnsafeMutablePointer<Void>     init()     init(EvidenceForm EvidenceForm: CSSM_EVIDENCE_FORM, Evidence Evidence: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_evidence {     var EvidenceForm: CSSM_EVIDENCE_FORM     var Evidence: UnsafeMutableRawPointer!     init()     init(EvidenceForm EvidenceForm: CSSM_EVIDENCE_FORM, Evidence Evidence: UnsafeMutableRawPointer!) } ``` |

Modified cssm_evidence.Evidence

|  | Declaration |
| --- | --- |
| From | ``` var Evidence: UnsafeMutablePointer<Void> ``` |
| To | ``` var Evidence: UnsafeMutableRawPointer! ``` |

Modified cssm_field [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_field {     var FieldOid: CSSM_OID     var FieldValue: CSSM_DATA     init()     init(FieldOid FieldOid: CSSM_OID, FieldValue FieldValue: CSSM_DATA) } ``` |
| To | ``` struct cssm_field {     var FieldOid: CSSM_OID     var FieldValue: cssm_data     init()     init(FieldOid FieldOid: CSSM_OID, FieldValue FieldValue: cssm_data) } ``` |

Modified cssm_field.FieldValue

|  | Declaration |
| --- | --- |
| From | ``` var FieldValue: CSSM_DATA ``` |
| To | ``` var FieldValue: cssm_data ``` |

Modified cssm_field.init(FieldOid: CSSM_OID, FieldValue: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(FieldOid FieldOid: CSSM_OID, FieldValue FieldValue: CSSM_DATA) ``` |
| To | ``` init(FieldOid FieldOid: CSSM_OID, FieldValue FieldValue: cssm_data) ``` |

Modified cssm_fieldgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_fieldgroup {     var NumberOfFields: Int32     var Fields: CSSM_FIELD_PTR     init()     init(NumberOfFields NumberOfFields: Int32, Fields Fields: CSSM_FIELD_PTR) } ``` |
| To | ``` struct cssm_fieldgroup {     var NumberOfFields: Int32     var Fields: UnsafeMutablePointer<cssm_field>!     init()     init(NumberOfFields NumberOfFields: Int32, Fields Fields: UnsafeMutablePointer<cssm_field>!) } ``` |

Modified cssm_fieldgroup.Fields

|  | Declaration |
| --- | --- |
| From | ``` var Fields: CSSM_FIELD_PTR ``` |
| To | ``` var Fields: UnsafeMutablePointer<cssm_field>! ``` |

Modified [cssm_func_name_addr [struct]](https://developer.apple.com/documentation/security/cssm_func_name_addr)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_func_name_addr {     var Name: CSSM_STRING     var Address: CSSM_PROC_ADDR!     init()     init(Name Name: CSSM_STRING, Address Address: CSSM_PROC_ADDR!) } ``` |
| To | ``` struct cssm_func_name_addr {     var Name: Security.CSSM_STRING     var Address: Security.CSSM_PROC_ADDR!     init()     init(Name Name: Security.CSSM_STRING, Address Address: Security.CSSM_PROC_ADDR!) } ``` |

Modified cssm_func_name_addr.Address

|  | Declaration |
| --- | --- |
| From | ``` var Address: CSSM_PROC_ADDR! ``` |
| To | ``` var Address: Security.CSSM_PROC_ADDR! ``` |

Modified [cssm_func_name_addr.init(Name: Security.CSSM_STRING, Address: Security.CSSM_PROC_ADDR!)](https://developer.apple.com/documentation/security/cssm_func_name_addr/1392053-init)

|  | Declaration |
| --- | --- |
| From | ``` init(Name Name: CSSM_STRING, Address Address: CSSM_PROC_ADDR!) ``` |
| To | ``` init(Name Name: Security.CSSM_STRING, Address Address: Security.CSSM_PROC_ADDR!) ``` |

Modified cssm_func_name_addr.Name

|  | Declaration |
| --- | --- |
| From | ``` var Name: CSSM_STRING ``` |
| To | ``` var Name: Security.CSSM_STRING ``` |

Modified cssm_kea_derive_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kea_derive_params {     var Rb: CSSM_DATA     var Yb: CSSM_DATA     init()     init(Rb Rb: CSSM_DATA, Yb Yb: CSSM_DATA) } ``` |
| To | ``` struct cssm_kea_derive_params {     var Rb: cssm_data     var Yb: cssm_data     init()     init(Rb Rb: cssm_data, Yb Yb: cssm_data) } ``` |

Modified cssm_kea_derive_params.init(Rb: cssm_data, Yb: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(Rb Rb: CSSM_DATA, Yb Yb: CSSM_DATA) ``` |
| To | ``` init(Rb Rb: cssm_data, Yb Yb: cssm_data) ``` |

Modified cssm_kea_derive_params.Rb

|  | Declaration |
| --- | --- |
| From | ``` var Rb: CSSM_DATA ``` |
| To | ``` var Rb: cssm_data ``` |

Modified cssm_kea_derive_params.Yb

|  | Declaration |
| --- | --- |
| From | ``` var Yb: CSSM_DATA ``` |
| To | ``` var Yb: cssm_data ``` |

Modified cssm_key [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_key {     var KeyHeader: CSSM_KEYHEADER     var KeyData: CSSM_DATA     init()     init(KeyHeader KeyHeader: CSSM_KEYHEADER, KeyData KeyData: CSSM_DATA) } ``` |
| To | ``` struct cssm_key {     var KeyHeader: cssm_keyheader     var KeyData: cssm_data     init()     init(KeyHeader KeyHeader: cssm_keyheader, KeyData KeyData: cssm_data) } ``` |

Modified cssm_key.init(KeyHeader: cssm_keyheader, KeyData: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(KeyHeader KeyHeader: CSSM_KEYHEADER, KeyData KeyData: CSSM_DATA) ``` |
| To | ``` init(KeyHeader KeyHeader: cssm_keyheader, KeyData KeyData: cssm_data) ``` |

Modified cssm_key.KeyData

|  | Declaration |
| --- | --- |
| From | ``` var KeyData: CSSM_DATA ``` |
| To | ``` var KeyData: cssm_data ``` |

Modified cssm_key.KeyHeader

|  | Declaration |
| --- | --- |
| From | ``` var KeyHeader: CSSM_KEYHEADER ``` |
| To | ``` var KeyHeader: cssm_keyheader ``` |

Modified cssm_keyheader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_keyheader {     var HeaderVersion: CSSM_HEADERVERSION     var CspId: CSSM_GUID     var BlobType: CSSM_KEYBLOB_TYPE     var Format: CSSM_KEYBLOB_FORMAT     var AlgorithmId: CSSM_ALGORITHMS     var KeyClass: CSSM_KEYCLASS     var LogicalKeySizeInBits: uint32     var KeyAttr: CSSM_KEYATTR_FLAGS     var KeyUsage: CSSM_KEYUSE     var StartDate: CSSM_DATE     var EndDate: CSSM_DATE     var WrapAlgorithmId: CSSM_ALGORITHMS     var WrapMode: CSSM_ENCRYPT_MODE     var Reserved: uint32     init()     init(HeaderVersion HeaderVersion: CSSM_HEADERVERSION, CspId CspId: CSSM_GUID, BlobType BlobType: CSSM_KEYBLOB_TYPE, Format Format: CSSM_KEYBLOB_FORMAT, AlgorithmId AlgorithmId: CSSM_ALGORITHMS, KeyClass KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits LogicalKeySizeInBits: uint32, KeyAttr KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage KeyUsage: CSSM_KEYUSE, StartDate StartDate: CSSM_DATE, EndDate EndDate: CSSM_DATE, WrapAlgorithmId WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode WrapMode: CSSM_ENCRYPT_MODE, Reserved Reserved: uint32) } ``` |
| To | ``` struct cssm_keyheader {     var HeaderVersion: CSSM_HEADERVERSION     var CspId: cssm_guid     var BlobType: CSSM_KEYBLOB_TYPE     var Format: CSSM_KEYBLOB_FORMAT     var AlgorithmId: CSSM_ALGORITHMS     var KeyClass: CSSM_KEYCLASS     var LogicalKeySizeInBits: uint32     var KeyAttr: CSSM_KEYATTR_FLAGS     var KeyUsage: CSSM_KEYUSE     var StartDate: cssm_date     var EndDate: cssm_date     var WrapAlgorithmId: CSSM_ALGORITHMS     var WrapMode: CSSM_ENCRYPT_MODE     var Reserved: uint32     init()     init(HeaderVersion HeaderVersion: CSSM_HEADERVERSION, CspId CspId: cssm_guid, BlobType BlobType: CSSM_KEYBLOB_TYPE, Format Format: CSSM_KEYBLOB_FORMAT, AlgorithmId AlgorithmId: CSSM_ALGORITHMS, KeyClass KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits LogicalKeySizeInBits: uint32, KeyAttr KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage KeyUsage: CSSM_KEYUSE, StartDate StartDate: cssm_date, EndDate EndDate: cssm_date, WrapAlgorithmId WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode WrapMode: CSSM_ENCRYPT_MODE, Reserved Reserved: uint32) } ``` |

Modified cssm_keyheader.CspId

|  | Declaration |
| --- | --- |
| From | ``` var CspId: CSSM_GUID ``` |
| To | ``` var CspId: cssm_guid ``` |

Modified cssm_keyheader.EndDate

|  | Declaration |
| --- | --- |
| From | ``` var EndDate: CSSM_DATE ``` |
| To | ``` var EndDate: cssm_date ``` |

Modified cssm_keyheader.init(HeaderVersion: CSSM_HEADERVERSION, CspId: cssm_guid, BlobType: CSSM_KEYBLOB_TYPE, Format: CSSM_KEYBLOB_FORMAT, AlgorithmId: CSSM_ALGORITHMS, KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits: uint32, KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage: CSSM_KEYUSE, StartDate: cssm_date, EndDate: cssm_date, WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode: CSSM_ENCRYPT_MODE, Reserved: uint32)

|  | Declaration |
| --- | --- |
| From | ``` init(HeaderVersion HeaderVersion: CSSM_HEADERVERSION, CspId CspId: CSSM_GUID, BlobType BlobType: CSSM_KEYBLOB_TYPE, Format Format: CSSM_KEYBLOB_FORMAT, AlgorithmId AlgorithmId: CSSM_ALGORITHMS, KeyClass KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits LogicalKeySizeInBits: uint32, KeyAttr KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage KeyUsage: CSSM_KEYUSE, StartDate StartDate: CSSM_DATE, EndDate EndDate: CSSM_DATE, WrapAlgorithmId WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode WrapMode: CSSM_ENCRYPT_MODE, Reserved Reserved: uint32) ``` |
| To | ``` init(HeaderVersion HeaderVersion: CSSM_HEADERVERSION, CspId CspId: cssm_guid, BlobType BlobType: CSSM_KEYBLOB_TYPE, Format Format: CSSM_KEYBLOB_FORMAT, AlgorithmId AlgorithmId: CSSM_ALGORITHMS, KeyClass KeyClass: CSSM_KEYCLASS, LogicalKeySizeInBits LogicalKeySizeInBits: uint32, KeyAttr KeyAttr: CSSM_KEYATTR_FLAGS, KeyUsage KeyUsage: CSSM_KEYUSE, StartDate StartDate: cssm_date, EndDate EndDate: cssm_date, WrapAlgorithmId WrapAlgorithmId: CSSM_ALGORITHMS, WrapMode WrapMode: CSSM_ENCRYPT_MODE, Reserved Reserved: uint32) ``` |

Modified cssm_keyheader.StartDate

|  | Declaration |
| --- | --- |
| From | ``` var StartDate: CSSM_DATE ``` |
| To | ``` var StartDate: cssm_date ``` |

Modified cssm_kr_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_name {     var Type: uint8     var Length: uint8     var Name: UnsafeMutablePointer<Int8>     init()     init(Type Type: uint8, Length Length: uint8, Name Name: UnsafeMutablePointer<Int8>) } ``` |
| To | ``` struct cssm_kr_name {     var Type: uint8     var Length: uint8     var Name: UnsafeMutablePointer<Int8>!     init()     init(Type Type: uint8, Length Length: uint8, Name Name: UnsafeMutablePointer<Int8>!) } ``` |

Modified cssm_kr_name.Name

|  | Declaration |
| --- | --- |
| From | ``` var Name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var Name: UnsafeMutablePointer<Int8>! ``` |

Modified cssm_kr_policy_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_policy_info {     var krbNotAllowed: CSSM_BOOL     var numberOfEntries: uint32     var policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM>     init()     init(krbNotAllowed krbNotAllowed: CSSM_BOOL, numberOfEntries numberOfEntries: uint32, policyEntry policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM>) } ``` |
| To | ``` struct cssm_kr_policy_info {     var krbNotAllowed: CSSM_BOOL     var numberOfEntries: uint32     var policyEntry: UnsafeMutablePointer<cssm_kr_policy_list_item>!     init()     init(krbNotAllowed krbNotAllowed: CSSM_BOOL, numberOfEntries numberOfEntries: uint32, policyEntry policyEntry: UnsafeMutablePointer<cssm_kr_policy_list_item>!) } ``` |

Modified cssm_kr_policy_info.policyEntry

|  | Declaration |
| --- | --- |
| From | ``` var policyEntry: UnsafeMutablePointer<CSSM_KR_POLICY_LIST_ITEM> ``` |
| To | ``` var policyEntry: UnsafeMutablePointer<cssm_kr_policy_list_item>! ``` |

Modified cssm_kr_policy_list_item [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_policy_list_item {     var next: COpaquePointer     var AlgorithmId: CSSM_ALGORITHMS     var Mode: CSSM_ENCRYPT_MODE     var MaxKeyLength: uint32     var MaxRounds: uint32     var WorkFactor: uint8     var PolicyFlags: CSSM_KR_POLICY_FLAGS     var AlgClass: CSSM_CONTEXT_TYPE     init() } ``` |
| To | ``` struct cssm_kr_policy_list_item {     var next: OpaquePointer!     var AlgorithmId: CSSM_ALGORITHMS     var Mode: CSSM_ENCRYPT_MODE     var MaxKeyLength: uint32     var MaxRounds: uint32     var WorkFactor: uint8     var PolicyFlags: CSSM_KR_POLICY_FLAGS     var AlgClass: CSSM_CONTEXT_TYPE     init() } ``` |

Modified cssm_kr_policy_list_item.next

|  | Declaration |
| --- | --- |
| From | ``` var next: COpaquePointer ``` |
| To | ``` var next: OpaquePointer! ``` |

Modified cssm_kr_profile [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_profile {     var UserName: CSSM_KR_NAME     var UserCertificate: CSSM_CERTGROUP_PTR     var KRSCertChain: CSSM_CERTGROUP_PTR     var LE_KRANum: uint8     var LE_KRACertChainList: CSSM_CERTGROUP_PTR     var ENT_KRANum: uint8     var ENT_KRACertChainList: CSSM_CERTGROUP_PTR     var INDIV_KRANum: uint8     var INDIV_KRACertChainList: CSSM_CERTGROUP_PTR     var INDIV_AuthenticationInfo: CSSM_DATA_PTR     var KRSPFlags: uint32     var KRSPExtensions: CSSM_DATA_PTR     init()     init(UserName UserName: CSSM_KR_NAME, UserCertificate UserCertificate: CSSM_CERTGROUP_PTR, KRSCertChain KRSCertChain: CSSM_CERTGROUP_PTR, LE_KRANum LE_KRANum: uint8, LE_KRACertChainList LE_KRACertChainList: CSSM_CERTGROUP_PTR, ENT_KRANum ENT_KRANum: uint8, ENT_KRACertChainList ENT_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_KRANum INDIV_KRANum: uint8, INDIV_KRACertChainList INDIV_KRACertChainList: CSSM_CERTGROUP_PTR, INDIV_AuthenticationInfo INDIV_AuthenticationInfo: CSSM_DATA_PTR, KRSPFlags KRSPFlags: uint32, KRSPExtensions KRSPExtensions: CSSM_DATA_PTR) } ``` |
| To | ``` struct cssm_kr_profile {     var UserName: cssm_kr_name     var UserCertificate: CSSM_CERTGROUP_PTR!     var KRSCertChain: CSSM_CERTGROUP_PTR!     var LE_KRANum: uint8     var LE_KRACertChainList: CSSM_CERTGROUP_PTR!     var ENT_KRANum: uint8     var ENT_KRACertChainList: CSSM_CERTGROUP_PTR!     var INDIV_KRANum: uint8     var INDIV_KRACertChainList: CSSM_CERTGROUP_PTR!     var INDIV_AuthenticationInfo: UnsafeMutablePointer<cssm_data>!     var KRSPFlags: uint32     var KRSPExtensions: UnsafeMutablePointer<cssm_data>!     init()     init(UserName UserName: cssm_kr_name, UserCertificate UserCertificate: CSSM_CERTGROUP_PTR!, KRSCertChain KRSCertChain: CSSM_CERTGROUP_PTR!, LE_KRANum LE_KRANum: uint8, LE_KRACertChainList LE_KRACertChainList: CSSM_CERTGROUP_PTR!, ENT_KRANum ENT_KRANum: uint8, ENT_KRACertChainList ENT_KRACertChainList: CSSM_CERTGROUP_PTR!, INDIV_KRANum INDIV_KRANum: uint8, INDIV_KRACertChainList INDIV_KRACertChainList: CSSM_CERTGROUP_PTR!, INDIV_AuthenticationInfo INDIV_AuthenticationInfo: UnsafeMutablePointer<cssm_data>!, KRSPFlags KRSPFlags: uint32, KRSPExtensions KRSPExtensions: UnsafeMutablePointer<cssm_data>!) } ``` |

Modified cssm_kr_profile.ENT_KRACertChainList

|  | Declaration |
| --- | --- |
| From | ``` var ENT_KRACertChainList: CSSM_CERTGROUP_PTR ``` |
| To | ``` var ENT_KRACertChainList: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_kr_profile.INDIV_AuthenticationInfo

|  | Declaration |
| --- | --- |
| From | ``` var INDIV_AuthenticationInfo: CSSM_DATA_PTR ``` |
| To | ``` var INDIV_AuthenticationInfo: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_kr_profile.INDIV_KRACertChainList

|  | Declaration |
| --- | --- |
| From | ``` var INDIV_KRACertChainList: CSSM_CERTGROUP_PTR ``` |
| To | ``` var INDIV_KRACertChainList: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_kr_profile.KRSCertChain

|  | Declaration |
| --- | --- |
| From | ``` var KRSCertChain: CSSM_CERTGROUP_PTR ``` |
| To | ``` var KRSCertChain: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_kr_profile.KRSPExtensions

|  | Declaration |
| --- | --- |
| From | ``` var KRSPExtensions: CSSM_DATA_PTR ``` |
| To | ``` var KRSPExtensions: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_kr_profile.LE_KRACertChainList

|  | Declaration |
| --- | --- |
| From | ``` var LE_KRACertChainList: CSSM_CERTGROUP_PTR ``` |
| To | ``` var LE_KRACertChainList: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_kr_profile.UserCertificate

|  | Declaration |
| --- | --- |
| From | ``` var UserCertificate: CSSM_CERTGROUP_PTR ``` |
| To | ``` var UserCertificate: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_kr_profile.UserName

|  | Declaration |
| --- | --- |
| From | ``` var UserName: CSSM_KR_NAME ``` |
| To | ``` var UserName: cssm_kr_name ``` |

Modified cssm_kr_wrappedproductinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_kr_wrappedproductinfo {     var StandardVersion: CSSM_VERSION     var StandardDescription: CSSM_STRING     var ProductVersion: CSSM_VERSION     var ProductDescription: CSSM_STRING     var ProductVendor: CSSM_STRING     var ProductFlags: uint32     init()     init(StandardVersion StandardVersion: CSSM_VERSION, StandardDescription StandardDescription: CSSM_STRING, ProductVersion ProductVersion: CSSM_VERSION, ProductDescription ProductDescription: CSSM_STRING, ProductVendor ProductVendor: CSSM_STRING, ProductFlags ProductFlags: uint32) } ``` |
| To | ``` struct cssm_kr_wrappedproductinfo {     var StandardVersion: cssm_version     var StandardDescription: Security.CSSM_STRING     var ProductVersion: cssm_version     var ProductDescription: Security.CSSM_STRING     var ProductVendor: Security.CSSM_STRING     var ProductFlags: uint32     init()     init(StandardVersion StandardVersion: cssm_version, StandardDescription StandardDescription: Security.CSSM_STRING, ProductVersion ProductVersion: cssm_version, ProductDescription ProductDescription: Security.CSSM_STRING, ProductVendor ProductVendor: Security.CSSM_STRING, ProductFlags ProductFlags: uint32) } ``` |

Modified cssm_kr_wrappedproductinfo.init(StandardVersion: cssm_version, StandardDescription: Security.CSSM_STRING, ProductVersion: cssm_version, ProductDescription: Security.CSSM_STRING, ProductVendor: Security.CSSM_STRING, ProductFlags: uint32)

|  | Declaration |
| --- | --- |
| From | ``` init(StandardVersion StandardVersion: CSSM_VERSION, StandardDescription StandardDescription: CSSM_STRING, ProductVersion ProductVersion: CSSM_VERSION, ProductDescription ProductDescription: CSSM_STRING, ProductVendor ProductVendor: CSSM_STRING, ProductFlags ProductFlags: uint32) ``` |
| To | ``` init(StandardVersion StandardVersion: cssm_version, StandardDescription StandardDescription: Security.CSSM_STRING, ProductVersion ProductVersion: cssm_version, ProductDescription ProductDescription: Security.CSSM_STRING, ProductVendor ProductVendor: Security.CSSM_STRING, ProductFlags ProductFlags: uint32) ``` |

Modified cssm_kr_wrappedproductinfo.ProductDescription

|  | Declaration |
| --- | --- |
| From | ``` var ProductDescription: CSSM_STRING ``` |
| To | ``` var ProductDescription: Security.CSSM_STRING ``` |

Modified cssm_kr_wrappedproductinfo.ProductVendor

|  | Declaration |
| --- | --- |
| From | ``` var ProductVendor: CSSM_STRING ``` |
| To | ``` var ProductVendor: Security.CSSM_STRING ``` |

Modified cssm_kr_wrappedproductinfo.ProductVersion

|  | Declaration |
| --- | --- |
| From | ``` var ProductVersion: CSSM_VERSION ``` |
| To | ``` var ProductVersion: cssm_version ``` |

Modified cssm_kr_wrappedproductinfo.StandardDescription

|  | Declaration |
| --- | --- |
| From | ``` var StandardDescription: CSSM_STRING ``` |
| To | ``` var StandardDescription: Security.CSSM_STRING ``` |

Modified cssm_kr_wrappedproductinfo.StandardVersion

|  | Declaration |
| --- | --- |
| From | ``` var StandardVersion: CSSM_VERSION ``` |
| To | ``` var StandardVersion: cssm_version ``` |

Modified cssm_krsubservice [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_krsubservice {     var SubServiceId: uint32     var Description: UnsafeMutablePointer<Int8>     var WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO     init()     init(SubServiceId SubServiceId: uint32, Description Description: UnsafeMutablePointer<Int8>, WrappedProduct WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO) } ``` |
| To | ``` struct cssm_krsubservice {     var SubServiceId: uint32     var Description: UnsafeMutablePointer<Int8>!     var WrappedProduct: cssm_kr_wrappedproductinfo     init()     init(SubServiceId SubServiceId: uint32, Description Description: UnsafeMutablePointer<Int8>!, WrappedProduct WrappedProduct: cssm_kr_wrappedproductinfo) } ``` |

Modified cssm_krsubservice.Description

|  | Declaration |
| --- | --- |
| From | ``` var Description: UnsafeMutablePointer<Int8> ``` |
| To | ``` var Description: UnsafeMutablePointer<Int8>! ``` |

Modified cssm_krsubservice.WrappedProduct

|  | Declaration |
| --- | --- |
| From | ``` var WrappedProduct: CSSM_KR_WRAPPEDPRODUCT_INFO ``` |
| To | ``` var WrappedProduct: cssm_kr_wrappedproductinfo ``` |

Modified [cssm_list [struct]](https://developer.apple.com/documentation/security/cssm_list)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_list {     var ListType: CSSM_LIST_TYPE     var Head: CSSM_LIST_ELEMENT_PTR     var Tail: CSSM_LIST_ELEMENT_PTR     init()     init(ListType ListType: CSSM_LIST_TYPE, Head Head: CSSM_LIST_ELEMENT_PTR, Tail Tail: CSSM_LIST_ELEMENT_PTR) } ``` |
| To | ``` struct cssm_list {     var ListType: CSSM_LIST_TYPE     var Head: CSSM_LIST_ELEMENT_PTR!     var Tail: CSSM_LIST_ELEMENT_PTR!     init()     init(ListType ListType: CSSM_LIST_TYPE, Head Head: CSSM_LIST_ELEMENT_PTR!, Tail Tail: CSSM_LIST_ELEMENT_PTR!) } ``` |

Modified cssm_list.Head

|  | Declaration |
| --- | --- |
| From | ``` var Head: CSSM_LIST_ELEMENT_PTR ``` |
| To | ``` var Head: CSSM_LIST_ELEMENT_PTR! ``` |

Modified cssm_list.Tail

|  | Declaration |
| --- | --- |
| From | ``` var Tail: CSSM_LIST_ELEMENT_PTR ``` |
| To | ``` var Tail: CSSM_LIST_ELEMENT_PTR! ``` |

Modified cssm_list_element [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_list_element {     struct __Unnamed_union_Element {         var Sublist: CSSM_LIST         var Word: CSSM_DATA         init(Sublist Sublist: CSSM_LIST)         init(Word Word: CSSM_DATA)         init()     }     var NextElement: UnsafeMutablePointer<cssm_list_element>     var WordID: CSSM_WORDID_TYPE     var ElementType: CSSM_LIST_ELEMENT_TYPE     var Element: cssm_list_element.__Unnamed_union_Element     init()     init(NextElement NextElement: UnsafeMutablePointer<cssm_list_element>, WordID WordID: CSSM_WORDID_TYPE, ElementType ElementType: CSSM_LIST_ELEMENT_TYPE, Element Element: cssm_list_element.__Unnamed_union_Element) } ``` |
| To | ``` struct cssm_list_element {     struct __Unnamed_union_Element {         var Sublist: cssm_list         var Word: cssm_data         init(Sublist Sublist: cssm_list)         init(Word Word: cssm_data)         init()     }     var NextElement: UnsafeMutablePointer<cssm_list_element>!     var WordID: CSSM_WORDID_TYPE     var ElementType: CSSM_LIST_ELEMENT_TYPE     var Element: cssm_list_element.__Unnamed_union_Element     init()     init(NextElement NextElement: UnsafeMutablePointer<cssm_list_element>!, WordID WordID: CSSM_WORDID_TYPE, ElementType ElementType: CSSM_LIST_ELEMENT_TYPE, Element Element: cssm_list_element.__Unnamed_union_Element) } ``` |

Modified cssm_list_element.NextElement

|  | Declaration |
| --- | --- |
| From | ``` var NextElement: UnsafeMutablePointer<cssm_list_element> ``` |
| To | ``` var NextElement: UnsafeMutablePointer<cssm_list_element>! ``` |

Modified cssm_manager_event_notification [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_manager_event_notification {     var DestinationModuleManagerType: CSSM_SERVICE_MASK     var SourceModuleManagerType: CSSM_SERVICE_MASK     var Event: CSSM_MANAGER_EVENT_TYPES     var EventId: uint32     var EventData: CSSM_DATA     init()     init(DestinationModuleManagerType DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType SourceModuleManagerType: CSSM_SERVICE_MASK, Event Event: CSSM_MANAGER_EVENT_TYPES, EventId EventId: uint32, EventData EventData: CSSM_DATA) } ``` |
| To | ``` struct cssm_manager_event_notification {     var DestinationModuleManagerType: CSSM_SERVICE_MASK     var SourceModuleManagerType: CSSM_SERVICE_MASK     var Event: CSSM_MANAGER_EVENT_TYPES     var EventId: uint32     var EventData: cssm_data     init()     init(DestinationModuleManagerType DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType SourceModuleManagerType: CSSM_SERVICE_MASK, Event Event: CSSM_MANAGER_EVENT_TYPES, EventId EventId: uint32, EventData EventData: cssm_data) } ``` |

Modified cssm_manager_event_notification.EventData

|  | Declaration |
| --- | --- |
| From | ``` var EventData: CSSM_DATA ``` |
| To | ``` var EventData: cssm_data ``` |

Modified cssm_manager_event_notification.init(DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType: CSSM_SERVICE_MASK, Event: CSSM_MANAGER_EVENT_TYPES, EventId: uint32, EventData: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(DestinationModuleManagerType DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType SourceModuleManagerType: CSSM_SERVICE_MASK, Event Event: CSSM_MANAGER_EVENT_TYPES, EventId EventId: uint32, EventData EventData: CSSM_DATA) ``` |
| To | ``` init(DestinationModuleManagerType DestinationModuleManagerType: CSSM_SERVICE_MASK, SourceModuleManagerType SourceModuleManagerType: CSSM_SERVICE_MASK, Event Event: CSSM_MANAGER_EVENT_TYPES, EventId EventId: uint32, EventData EventData: cssm_data) ``` |

Modified cssm_manager_registration_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_manager_registration_info {     var Initialize: ((uint32, uint32) -> CSSM_RETURN)!     var Terminate: (() -> CSSM_RETURN)!     var RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)!     var DeregisterDispatchTable: (() -> CSSM_RETURN)!     var EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!     var RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!     init()     init(Initialize Initialize: ((uint32, uint32) -> CSSM_RETURN)!, Terminate Terminate: (() -> CSSM_RETURN)!, RegisterDispatchTable RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)!, DeregisterDispatchTable DeregisterDispatchTable: (() -> CSSM_RETURN)!, EventNotifyManager EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!, RefreshFunctionTable RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_manager_registration_info {     var Initialize: ((uint32, uint32) -> CSSM_RETURN)!     var Terminate: (() -> CSSM_RETURN)!     var RegisterDispatchTable: ((UnsafeMutablePointer<cssm_state_funcs>?) -> CSSM_RETURN)!     var DeregisterDispatchTable: (() -> CSSM_RETURN)!     var EventNotifyManager: ((UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)!     var RefreshFunctionTable: ((UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)!     init()     init(Initialize Initialize: (@escaping (uint32, uint32) -> CSSM_RETURN)!, Terminate Terminate: (@escaping () -> CSSM_RETURN)!, RegisterDispatchTable RegisterDispatchTable: (@escaping (UnsafeMutablePointer<cssm_state_funcs>?) -> CSSM_RETURN)!, DeregisterDispatchTable DeregisterDispatchTable: (@escaping () -> CSSM_RETURN)!, EventNotifyManager EventNotifyManager: (@escaping (UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)!, RefreshFunctionTable RefreshFunctionTable: (@escaping (UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)!) } ``` |

Modified cssm_manager_registration_info.EventNotifyManager

|  | Declaration |
| --- | --- |
| From | ``` var EventNotifyManager: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)! ``` |
| To | ``` var EventNotifyManager: ((UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.RefreshFunctionTable

|  | Declaration |
| --- | --- |
| From | ``` var RefreshFunctionTable: ((CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var RefreshFunctionTable: ((UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_manager_registration_info.RegisterDispatchTable

|  | Declaration |
| --- | --- |
| From | ``` var RegisterDispatchTable: ((CSSM_STATE_FUNCS_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var RegisterDispatchTable: ((UnsafeMutablePointer<cssm_state_funcs>?) -> CSSM_RETURN)! ``` |

Modified [cssm_memory_funcs [struct]](https://developer.apple.com/documentation/security/cssm_memory_funcs)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_memory_funcs {     var malloc_func: CSSM_MALLOC!     var free_func: CSSM_FREE!     var realloc_func: CSSM_REALLOC!     var calloc_func: CSSM_CALLOC!     var AllocRef: UnsafeMutablePointer<Void>     init()     init(malloc_func malloc_func: CSSM_MALLOC!, free_func free_func: CSSM_FREE!, realloc_func realloc_func: CSSM_REALLOC!, calloc_func calloc_func: CSSM_CALLOC!, AllocRef AllocRef: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_memory_funcs {     var malloc_func: Security.CSSM_MALLOC!     var free_func: Security.CSSM_FREE!     var realloc_func: Security.CSSM_REALLOC!     var calloc_func: Security.CSSM_CALLOC!     var AllocRef: UnsafeMutableRawPointer!     init()     init(malloc_func malloc_func: Security.CSSM_MALLOC!, free_func free_func: Security.CSSM_FREE!, realloc_func realloc_func: Security.CSSM_REALLOC!, calloc_func calloc_func: Security.CSSM_CALLOC!, AllocRef AllocRef: UnsafeMutableRawPointer!) } ``` |

Modified cssm_memory_funcs.AllocRef

|  | Declaration |
| --- | --- |
| From | ``` var AllocRef: UnsafeMutablePointer<Void> ``` |
| To | ``` var AllocRef: UnsafeMutableRawPointer! ``` |

Modified cssm_memory_funcs.calloc_func

|  | Declaration |
| --- | --- |
| From | ``` var calloc_func: CSSM_CALLOC! ``` |
| To | ``` var calloc_func: Security.CSSM_CALLOC! ``` |

Modified cssm_memory_funcs.free_func

|  | Declaration |
| --- | --- |
| From | ``` var free_func: CSSM_FREE! ``` |
| To | ``` var free_func: Security.CSSM_FREE! ``` |

Modified cssm_memory_funcs.malloc_func

|  | Declaration |
| --- | --- |
| From | ``` var malloc_func: CSSM_MALLOC! ``` |
| To | ``` var malloc_func: Security.CSSM_MALLOC! ``` |

Modified cssm_memory_funcs.realloc_func

|  | Declaration |
| --- | --- |
| From | ``` var realloc_func: CSSM_REALLOC! ``` |
| To | ``` var realloc_func: Security.CSSM_REALLOC! ``` |

Modified cssm_module_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_module_funcs {     var ServiceType: CSSM_SERVICE_TYPE     var NumberOfServiceFuncs: uint32     var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?>     init()     init(ServiceType ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs NumberOfServiceFuncs: uint32, ServiceFuncs ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?>) } ``` |
| To | ``` struct cssm_module_funcs {     var ServiceType: CSSM_SERVICE_TYPE     var NumberOfServiceFuncs: uint32     var ServiceFuncs: UnsafePointer<Security.CSSM_PROC_ADDR?>!     init()     init(ServiceType ServiceType: CSSM_SERVICE_TYPE, NumberOfServiceFuncs NumberOfServiceFuncs: uint32, ServiceFuncs ServiceFuncs: UnsafePointer<Security.CSSM_PROC_ADDR?>!) } ``` |

Modified cssm_module_funcs.ServiceFuncs

|  | Declaration |
| --- | --- |
| From | ``` var ServiceFuncs: UnsafePointer<CSSM_PROC_ADDR?> ``` |
| To | ``` var ServiceFuncs: UnsafePointer<Security.CSSM_PROC_ADDR?>! ``` |

Modified [cssm_name_list [struct]](https://developer.apple.com/documentation/security/cssm_name_list)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_name_list {     var NumStrings: uint32     var String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     init()     init(NumStrings NumStrings: uint32, String String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) } ``` |
| To | ``` struct cssm_name_list {     var NumStrings: uint32     var String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     init()     init(NumStrings NumStrings: uint32, String String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) } ``` |

Modified cssm_name_list.String

|  | Declaration |
| --- | --- |
| From | ``` var String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var String: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified cssm_net_address [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_net_address {     var AddressType: CSSM_NET_ADDRESS_TYPE     var Address: CSSM_DATA     init()     init(AddressType AddressType: CSSM_NET_ADDRESS_TYPE, Address Address: CSSM_DATA) } ``` |
| To | ``` struct cssm_net_address {     var AddressType: CSSM_NET_ADDRESS_TYPE     var Address: cssm_data     init()     init(AddressType AddressType: CSSM_NET_ADDRESS_TYPE, Address Address: cssm_data) } ``` |

Modified cssm_net_address.Address

|  | Declaration |
| --- | --- |
| From | ``` var Address: CSSM_DATA ``` |
| To | ``` var Address: cssm_data ``` |

Modified cssm_net_address.init(AddressType: CSSM_NET_ADDRESS_TYPE, Address: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(AddressType AddressType: CSSM_NET_ADDRESS_TYPE, Address Address: CSSM_DATA) ``` |
| To | ``` init(AddressType AddressType: CSSM_NET_ADDRESS_TYPE, Address Address: cssm_data) ``` |

Modified [cssm_parsed_cert [struct]](https://developer.apple.com/documentation/security/cssm_parsed_cert)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_parsed_cert {     var CertType: CSSM_CERT_TYPE     var ParsedCertFormat: CSSM_CERT_PARSE_FORMAT     var ParsedCert: UnsafeMutablePointer<Void>     init()     init(CertType CertType: CSSM_CERT_TYPE, ParsedCertFormat ParsedCertFormat: CSSM_CERT_PARSE_FORMAT, ParsedCert ParsedCert: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_parsed_cert {     var CertType: CSSM_CERT_TYPE     var ParsedCertFormat: CSSM_CERT_PARSE_FORMAT     var ParsedCert: UnsafeMutableRawPointer!     init()     init(CertType CertType: CSSM_CERT_TYPE, ParsedCertFormat ParsedCertFormat: CSSM_CERT_PARSE_FORMAT, ParsedCert ParsedCert: UnsafeMutableRawPointer!) } ``` |

Modified cssm_parsed_cert.ParsedCert

|  | Declaration |
| --- | --- |
| From | ``` var ParsedCert: UnsafeMutablePointer<Void> ``` |
| To | ``` var ParsedCert: UnsafeMutableRawPointer! ``` |

Modified [cssm_parsed_crl [struct]](https://developer.apple.com/documentation/security/cssm_parsed_crl)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_parsed_crl {     var CrlType: CSSM_CRL_TYPE     var ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT     var ParsedCrl: UnsafeMutablePointer<Void>     init()     init(CrlType CrlType: CSSM_CRL_TYPE, ParsedCrlFormat ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT, ParsedCrl ParsedCrl: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_parsed_crl {     var CrlType: CSSM_CRL_TYPE     var ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT     var ParsedCrl: UnsafeMutableRawPointer!     init()     init(CrlType CrlType: CSSM_CRL_TYPE, ParsedCrlFormat ParsedCrlFormat: CSSM_CRL_PARSE_FORMAT, ParsedCrl ParsedCrl: UnsafeMutableRawPointer!) } ``` |

Modified cssm_parsed_crl.ParsedCrl

|  | Declaration |
| --- | --- |
| From | ``` var ParsedCrl: UnsafeMutablePointer<Void> ``` |
| To | ``` var ParsedCrl: UnsafeMutableRawPointer! ``` |

Modified cssm_pkcs1_oaep_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_pkcs1_oaep_params {     var HashAlgorithm: uint32     var HashParams: CSSM_DATA     var MGF: CSSM_PKCS_OAEP_MGF     var MGFParams: CSSM_DATA     var PSource: CSSM_PKCS_OAEP_PSOURCE     var PSourceParams: CSSM_DATA     init()     init(HashAlgorithm HashAlgorithm: uint32, HashParams HashParams: CSSM_DATA, MGF MGF: CSSM_PKCS_OAEP_MGF, MGFParams MGFParams: CSSM_DATA, PSource PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams PSourceParams: CSSM_DATA) } ``` |
| To | ``` struct cssm_pkcs1_oaep_params {     var HashAlgorithm: uint32     var HashParams: cssm_data     var MGF: CSSM_PKCS_OAEP_MGF     var MGFParams: cssm_data     var PSource: CSSM_PKCS_OAEP_PSOURCE     var PSourceParams: cssm_data     init()     init(HashAlgorithm HashAlgorithm: uint32, HashParams HashParams: cssm_data, MGF MGF: CSSM_PKCS_OAEP_MGF, MGFParams MGFParams: cssm_data, PSource PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams PSourceParams: cssm_data) } ``` |

Modified cssm_pkcs1_oaep_params.HashParams

|  | Declaration |
| --- | --- |
| From | ``` var HashParams: CSSM_DATA ``` |
| To | ``` var HashParams: cssm_data ``` |

Modified cssm_pkcs1_oaep_params.init(HashAlgorithm: uint32, HashParams: cssm_data, MGF: CSSM_PKCS_OAEP_MGF, MGFParams: cssm_data, PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(HashAlgorithm HashAlgorithm: uint32, HashParams HashParams: CSSM_DATA, MGF MGF: CSSM_PKCS_OAEP_MGF, MGFParams MGFParams: CSSM_DATA, PSource PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams PSourceParams: CSSM_DATA) ``` |
| To | ``` init(HashAlgorithm HashAlgorithm: uint32, HashParams HashParams: cssm_data, MGF MGF: CSSM_PKCS_OAEP_MGF, MGFParams MGFParams: cssm_data, PSource PSource: CSSM_PKCS_OAEP_PSOURCE, PSourceParams PSourceParams: cssm_data) ``` |

Modified cssm_pkcs1_oaep_params.MGFParams

|  | Declaration |
| --- | --- |
| From | ``` var MGFParams: CSSM_DATA ``` |
| To | ``` var MGFParams: cssm_data ``` |

Modified cssm_pkcs1_oaep_params.PSourceParams

|  | Declaration |
| --- | --- |
| From | ``` var PSourceParams: CSSM_DATA ``` |
| To | ``` var PSourceParams: cssm_data ``` |

Modified cssm_pkcs5_pbkdf1_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_pkcs5_pbkdf1_params {     var Passphrase: CSSM_DATA     var InitVector: CSSM_DATA     init()     init(Passphrase Passphrase: CSSM_DATA, InitVector InitVector: CSSM_DATA) } ``` |
| To | ``` struct cssm_pkcs5_pbkdf1_params {     var Passphrase: cssm_data     var InitVector: cssm_data     init()     init(Passphrase Passphrase: cssm_data, InitVector InitVector: cssm_data) } ``` |

Modified cssm_pkcs5_pbkdf1_params.init(Passphrase: cssm_data, InitVector: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(Passphrase Passphrase: CSSM_DATA, InitVector InitVector: CSSM_DATA) ``` |
| To | ``` init(Passphrase Passphrase: cssm_data, InitVector InitVector: cssm_data) ``` |

Modified cssm_pkcs5_pbkdf1_params.InitVector

|  | Declaration |
| --- | --- |
| From | ``` var InitVector: CSSM_DATA ``` |
| To | ``` var InitVector: cssm_data ``` |

Modified cssm_pkcs5_pbkdf1_params.Passphrase

|  | Declaration |
| --- | --- |
| From | ``` var Passphrase: CSSM_DATA ``` |
| To | ``` var Passphrase: cssm_data ``` |

Modified cssm_pkcs5_pbkdf2_params [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_pkcs5_pbkdf2_params {     var Passphrase: CSSM_DATA     var PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF     init()     init(Passphrase Passphrase: CSSM_DATA, PseudoRandomFunction PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF) } ``` |
| To | ``` struct cssm_pkcs5_pbkdf2_params {     var Passphrase: cssm_data     var PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF     init()     init(Passphrase Passphrase: cssm_data, PseudoRandomFunction PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF) } ``` |

Modified cssm_pkcs5_pbkdf2_params.init(Passphrase: cssm_data, PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF)

|  | Declaration |
| --- | --- |
| From | ``` init(Passphrase Passphrase: CSSM_DATA, PseudoRandomFunction PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF) ``` |
| To | ``` init(Passphrase Passphrase: cssm_data, PseudoRandomFunction PseudoRandomFunction: CSSM_PKCS5_PBKDF2_PRF) ``` |

Modified cssm_pkcs5_pbkdf2_params.Passphrase

|  | Declaration |
| --- | --- |
| From | ``` var Passphrase: CSSM_DATA ``` |
| To | ``` var Passphrase: cssm_data ``` |

Modified cssm_query [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_query {     var RecordType: CSSM_DB_RECORDTYPE     var Conjunctive: CSSM_DB_CONJUNCTIVE     var NumSelectionPredicates: uint32     var SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR     var QueryLimits: CSSM_QUERY_LIMITS     var QueryFlags: CSSM_QUERY_FLAGS     init()     init(RecordType RecordType: CSSM_DB_RECORDTYPE, Conjunctive Conjunctive: CSSM_DB_CONJUNCTIVE, NumSelectionPredicates NumSelectionPredicates: uint32, SelectionPredicate SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR, QueryLimits QueryLimits: CSSM_QUERY_LIMITS, QueryFlags QueryFlags: CSSM_QUERY_FLAGS) } ``` |
| To | ``` struct cssm_query {     var RecordType: CSSM_DB_RECORDTYPE     var Conjunctive: CSSM_DB_CONJUNCTIVE     var NumSelectionPredicates: uint32     var SelectionPredicate: UnsafeMutablePointer<cssm_selection_predicate>!     var QueryLimits: cssm_query_limits     var QueryFlags: CSSM_QUERY_FLAGS     init()     init(RecordType RecordType: CSSM_DB_RECORDTYPE, Conjunctive Conjunctive: CSSM_DB_CONJUNCTIVE, NumSelectionPredicates NumSelectionPredicates: uint32, SelectionPredicate SelectionPredicate: UnsafeMutablePointer<cssm_selection_predicate>!, QueryLimits QueryLimits: cssm_query_limits, QueryFlags QueryFlags: CSSM_QUERY_FLAGS) } ``` |

Modified cssm_query.QueryLimits

|  | Declaration |
| --- | --- |
| From | ``` var QueryLimits: CSSM_QUERY_LIMITS ``` |
| To | ``` var QueryLimits: cssm_query_limits ``` |

Modified cssm_query.SelectionPredicate

|  | Declaration |
| --- | --- |
| From | ``` var SelectionPredicate: CSSM_SELECTION_PREDICATE_PTR ``` |
| To | ``` var SelectionPredicate: UnsafeMutablePointer<cssm_selection_predicate>! ``` |

Modified cssm_resource_control_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_resource_control_context {     var AccessCred: CSSM_ACCESS_CREDENTIALS_PTR     var InitialAclEntry: CSSM_ACL_ENTRY_INPUT     init()     init(AccessCred AccessCred: CSSM_ACCESS_CREDENTIALS_PTR, InitialAclEntry InitialAclEntry: CSSM_ACL_ENTRY_INPUT) } ``` |
| To | ``` struct cssm_resource_control_context {     var AccessCred: UnsafeMutablePointer<cssm_access_credentials>!     var InitialAclEntry: cssm_acl_entry_input     init()     init(AccessCred AccessCred: UnsafeMutablePointer<cssm_access_credentials>!, InitialAclEntry InitialAclEntry: cssm_acl_entry_input) } ``` |

Modified cssm_resource_control_context.AccessCred

|  | Declaration |
| --- | --- |
| From | ``` var AccessCred: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var AccessCred: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_resource_control_context.InitialAclEntry

|  | Declaration |
| --- | --- |
| From | ``` var InitialAclEntry: CSSM_ACL_ENTRY_INPUT ``` |
| To | ``` var InitialAclEntry: cssm_acl_entry_input ``` |

Modified cssm_sample [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_sample {     var TypedSample: CSSM_LIST     var Verifier: UnsafePointer<CSSM_SUBSERVICE_UID>     init()     init(TypedSample TypedSample: CSSM_LIST, Verifier Verifier: UnsafePointer<CSSM_SUBSERVICE_UID>) } ``` |
| To | ``` struct cssm_sample {     var TypedSample: cssm_list     var Verifier: UnsafePointer<cssm_subservice_uid>!     init()     init(TypedSample TypedSample: cssm_list, Verifier Verifier: UnsafePointer<cssm_subservice_uid>!) } ``` |

Modified cssm_sample.TypedSample

|  | Declaration |
| --- | --- |
| From | ``` var TypedSample: CSSM_LIST ``` |
| To | ``` var TypedSample: cssm_list ``` |

Modified cssm_sample.Verifier

|  | Declaration |
| --- | --- |
| From | ``` var Verifier: UnsafePointer<CSSM_SUBSERVICE_UID> ``` |
| To | ``` var Verifier: UnsafePointer<cssm_subservice_uid>! ``` |

Modified cssm_samplegroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_samplegroup {     var NumberOfSamples: uint32     var Samples: UnsafePointer<CSSM_SAMPLE>     init()     init(NumberOfSamples NumberOfSamples: uint32, Samples Samples: UnsafePointer<CSSM_SAMPLE>) } ``` |
| To | ``` struct cssm_samplegroup {     var NumberOfSamples: uint32     var Samples: UnsafePointer<cssm_sample>!     init()     init(NumberOfSamples NumberOfSamples: uint32, Samples Samples: UnsafePointer<cssm_sample>!) } ``` |

Modified cssm_samplegroup.Samples

|  | Declaration |
| --- | --- |
| From | ``` var Samples: UnsafePointer<CSSM_SAMPLE> ``` |
| To | ``` var Samples: UnsafePointer<cssm_sample>! ``` |

Modified cssm_selection_predicate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_selection_predicate {     var DbOperator: CSSM_DB_OPERATOR     var Attribute: CSSM_DB_ATTRIBUTE_DATA     init()     init(DbOperator DbOperator: CSSM_DB_OPERATOR, Attribute Attribute: CSSM_DB_ATTRIBUTE_DATA) } ``` |
| To | ``` struct cssm_selection_predicate {     var DbOperator: CSSM_DB_OPERATOR     var Attribute: cssm_db_attribute_data     init()     init(DbOperator DbOperator: CSSM_DB_OPERATOR, Attribute Attribute: cssm_db_attribute_data) } ``` |

Modified cssm_selection_predicate.Attribute

|  | Declaration |
| --- | --- |
| From | ``` var Attribute: CSSM_DB_ATTRIBUTE_DATA ``` |
| To | ``` var Attribute: cssm_db_attribute_data ``` |

Modified cssm_selection_predicate.init(DbOperator: CSSM_DB_OPERATOR, Attribute: cssm_db_attribute_data)

|  | Declaration |
| --- | --- |
| From | ``` init(DbOperator DbOperator: CSSM_DB_OPERATOR, Attribute Attribute: CSSM_DB_ATTRIBUTE_DATA) ``` |
| To | ``` init(DbOperator DbOperator: CSSM_DB_OPERATOR, Attribute Attribute: cssm_db_attribute_data) ``` |

Modified cssm_spi_ac_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_ac_funcs {     var AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)!     var PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(AuthCompute AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_spi_ac_funcs {     var AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafePointer<cssm_tuplegroup>?, uint32, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafeMutablePointer<cssm_tuplegroup>?) -> CSSM_RETURN)!     var PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!     init()     init(AuthCompute AuthCompute: (@escaping (CSSM_AC_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafePointer<cssm_tuplegroup>?, uint32, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafeMutablePointer<cssm_tuplegroup>?) -> CSSM_RETURN)!, PassThrough PassThrough: (@escaping (CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_ac_funcs.AuthCompute

|  | Declaration |
| --- | --- |
| From | ``` var AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafePointer<CSSM_TUPLEGROUP>, uint32, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, UnsafePointer<CSSM_LIST>, CSSM_TUPLEGROUP_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var AuthCompute: ((CSSM_AC_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafePointer<cssm_tuplegroup>?, uint32, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafePointer<cssm_list>?, UnsafeMutablePointer<cssm_tuplegroup>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_ac_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |
| To | ``` var PassThrough: ((CSSM_AC_HANDLE, CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_cl_funcs {     var CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!     var CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)!     var CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!     var CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!     var CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!     var CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!     var CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!     var PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(CertCreateTemplate CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertVerify CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CertVerifyWithKey CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, CertGetFirstFieldValue CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextFieldValue CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortQuery CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGetKeyInfo CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)!, CertGetAllFields CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFields FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, FreeFieldValue FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertCache CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, CertGetFirstCachedFieldValue CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertGetNextCachedFieldValue CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CertAbortCache CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGroupToSignedBundle CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGroupFromVerifiedBundle CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertDescribeFormat CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, CrlCreateTemplate CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSetFields CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlAddCert CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlRemoveCert CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)!, CrlVerifyWithKey CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, IsCertInCrl IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, CrlGetFirstFieldValue CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextFieldValue CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlAbortQuery CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlGetAllFields CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlCache CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, IsCertInCachedCrl IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlGetFirstCachedFieldValue CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetNextCachedFieldValue CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)!, CrlGetAllCachedRecordFields CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CrlAbortCache CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlDescribeFormat CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_spi_cl_funcs {     var CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!     var CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)!     var CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CertAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_key>?>?) -> CSSM_RETURN)!     var CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!     var FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!     var FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertCache: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!     var CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CertAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_cert_bundle_header>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_cert_bundle>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!     var CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)!     var CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)!     var CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!     var CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CrlAbortQuery: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!     var CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!     var IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!     var CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!     var CrlAbortCache: ((CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)!     var PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!     init()     init(CertCreateTemplate CertCreateTemplate: (@escaping (CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertGetAllTemplateFields CertGetAllTemplateFields: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CertSign CertSign: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertVerify CertVerify: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)!, CertVerifyWithKey CertVerifyWithKey: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, CertGetFirstFieldValue CertGetFirstFieldValue: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertGetNextFieldValue CertGetNextFieldValue: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertAbortQuery CertAbortQuery: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGetKeyInfo CertGetKeyInfo: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_key>?>?) -> CSSM_RETURN)!, CertGetAllFields CertGetAllFields: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, FreeFields FreeFields: (@escaping (CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, FreeFieldValue FreeFieldValue: (@escaping (CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertCache CertCache: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, CertGetFirstCachedFieldValue CertGetFirstCachedFieldValue: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertGetNextCachedFieldValue CertGetNextCachedFieldValue: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CertAbortCache CertAbortCache: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CertGroupToSignedBundle CertGroupToSignedBundle: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_cert_bundle_header>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertGroupFromVerifiedBundle CertGroupFromVerifiedBundle: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_cert_bundle>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, CertDescribeFormat CertDescribeFormat: (@escaping (CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)!, CrlCreateTemplate CrlCreateTemplate: (@escaping (CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlSetFields CrlSetFields: (@escaping (CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlAddCert CrlAddCert: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlRemoveCert CrlRemoveCert: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlSign CrlSign: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlVerify CrlVerify: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)!, CrlVerifyWithKey CrlVerifyWithKey: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, IsCertInCrl IsCertInCrl: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!, CrlGetFirstFieldValue CrlGetFirstFieldValue: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlGetNextFieldValue CrlGetNextFieldValue: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlAbortQuery CrlAbortQuery: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlGetAllFields CrlGetAllFields: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CrlCache CrlCache: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, IsCertInCachedCrl IsCertInCachedCrl: (@escaping (CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlGetFirstCachedFieldValue CrlGetFirstCachedFieldValue: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlGetNextCachedFieldValue CrlGetNextCachedFieldValue: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)!, CrlGetAllCachedRecordFields CrlGetAllCachedRecordFields: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CrlAbortCache CrlAbortCache: (@escaping (CSSM_CL_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, CrlDescribeFormat CrlDescribeFormat: (@escaping (CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)!, PassThrough PassThrough: (@escaping (CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_cl_funcs.CertCache

|  | Declaration |
| --- | --- |
| From | ``` var CertCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertCache: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertDescribeFormat

|  | Declaration |
| --- | --- |
| From | ``` var CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetAllFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetAllTemplateFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetAllTemplateFields: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetFirstCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetFirstFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetKeyInfo

|  | Declaration |
| --- | --- |
| From | ``` var CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_KEY_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetKeyInfo: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_key>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetNextCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGetNextFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGroupFromVerifiedBundle

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERT_BUNDLE>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGroupFromVerifiedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_cert_bundle>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertGroupToSignedBundle

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERT_BUNDLE_HEADER>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertGroupToSignedBundle: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_cert_bundle_header>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertSign

|  | Declaration |
| --- | --- |
| From | ``` var CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertVerify

|  | Declaration |
| --- | --- |
| From | ``` var CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var CertVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CertVerifyWithKey

|  | Declaration |
| --- | --- |
| From | ``` var CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var CertVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlAddCert

|  | Declaration |
| --- | --- |
| From | ``` var CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlAddCert: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlCache

|  | Declaration |
| --- | --- |
| From | ``` var CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlCache: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlCreateTemplate: ((CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlDescribeFormat

|  | Declaration |
| --- | --- |
| From | ``` var CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_OID_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlDescribeFormat: ((CSSM_CL_HANDLE, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_OID_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetAllCachedRecordFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlGetAllCachedRecordFields: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetAllFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlGetAllFields: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetFirstCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlGetFirstCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetFirstFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_OID>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlGetFirstFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_OID>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetNextCachedFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlGetNextCachedFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlGetNextFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<CSSM_DATA_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlGetNextFieldValue: ((CSSM_CL_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_data>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlRemoveCert

|  | Declaration |
| --- | --- |
| From | ``` var CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlRemoveCert: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlSetFields

|  | Declaration |
| --- | --- |
| From | ``` var CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, UnsafePointer<CSSM_DATA>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlSetFields: ((CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlSign

|  | Declaration |
| --- | --- |
| From | ``` var CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlSign: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlVerify

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_FIELD>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var CrlVerify: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_field>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.CrlVerifyWithKey

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var CrlVerifyWithKey: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.FreeFields

|  | Declaration |
| --- | --- |
| From | ``` var FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var FreeFields: ((CSSM_CL_HANDLE, uint32, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.FreeFieldValue

|  | Declaration |
| --- | --- |
| From | ``` var FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FreeFieldValue: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_OID>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.IsCertInCachedCrl

|  | Declaration |
| --- | --- |
| From | ``` var IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var IsCertInCachedCrl: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, CSSM_HANDLE, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.IsCertInCrl

|  | Declaration |
| --- | --- |
| From | ``` var IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)! ``` |
| To | ``` var IsCertInCrl: ((CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_cl_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |
| To | ``` var PassThrough: ((CSSM_CL_HANDLE, CSSM_CC_HANDLE, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_csp_funcs {     var EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)!     var SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)!     var SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!     var DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!     var GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!     var VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!     var VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!     var EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!     var DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)!     var GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)!     var WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)!     var FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)!     var PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     var Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)!     var Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!     var ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!     var ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)!     var RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)!     var GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)!     var GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!     var GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!     var ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)!     var GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!     var ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!     var GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!     var ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!     init()     init(EventNotify EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, QuerySize QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)!, SignData SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)!, SignDataInit SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, SignDataUpdate SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, SignDataFinal SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyData VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyDataInit VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyDataUpdate VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyDataFinal VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, DigestData DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, DigestDataInit DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, DigestDataUpdate DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, DigestDataClone DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!, DigestDataFinal DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMac GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateMacInit GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, GenerateMacUpdate GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, GenerateMacFinal GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyMac VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, VerifyMacInit VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)!, VerifyMacUpdate VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)!, VerifyMacFinal VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, EncryptData EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataInit EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataUpdate EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, EncryptDataFinal EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, DecryptData DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataInit DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataUpdate DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)!, DecryptDataFinal DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, QueryKeySizeInBits QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)!, GenerateKey GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateKeyPair GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateRandom GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)!, GenerateAlgorithmParams GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)!, WrapKey WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, UnwrapKey UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DeriveKey DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)!, FreeKey FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!, Login Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)!, Logout Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!, ChangeLoginAcl ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, ObtainPrivateKeyFromPublicKey ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)!, RetrieveUniqueId RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCounter RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)!, VerifyDevice VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetTimeValue GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)!, GetOperationalStatistics GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)!, GetLoginAcl GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, GetKeyAcl GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeKeyAcl ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)!, GetKeyOwner GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeKeyOwner ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetLoginOwner GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeLoginOwner ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_spi_csp_funcs {     var EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!     var QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_BOOL, uint32, UnsafeMutablePointer<cssm_query_size_data>?) -> CSSM_RETURN)!     var SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!     var SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!     var SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!     var VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!     var VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!     var DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!     var DigestDataClone: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!     var DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!     var GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!     var GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!     var VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!     var VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)!     var EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)!     var DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key_size>?) -> CSSM_RETURN)!     var GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_key>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR?>?) -> CSSM_RETURN)!     var WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_data>?, CSSM_WRAP_KEY_PTR?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafePointer<CSSM_WRAP_KEY>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!     var DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)!     var FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<cssm_key>?, CSSM_BOOL) -> CSSM_RETURN)!     var PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!     var Login: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_data>?, UnsafeRawPointer?) -> CSSM_RETURN)!     var Logout: ((CSSM_CSP_HANDLE) -> CSSM_RETURN)!     var ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)!     var ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)!     var RetrieveUniqueId: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var RetrieveCounter: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_csp_operational_statistics>?) -> CSSM_RETURN)!     var GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!     var GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!     var ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?, UnsafePointer<cssm_key>?) -> CSSM_RETURN)!     var GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!     var ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!     var GetLoginOwner: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!     var ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!     init()     init(EventNotify EventNotify: (@escaping (CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, QuerySize QuerySize: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_BOOL, uint32, UnsafeMutablePointer<cssm_query_size_data>?) -> CSSM_RETURN)!, SignData SignData: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, SignDataInit SignDataInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, SignDataUpdate SignDataUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, SignDataFinal SignDataFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyData VerifyData: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyDataInit VerifyDataInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, VerifyDataUpdate VerifyDataUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, VerifyDataFinal VerifyDataFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, DigestData DigestData: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, DigestDataInit DigestDataInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, DigestDataUpdate DigestDataUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, DigestDataClone DigestDataClone: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_CC_HANDLE) -> CSSM_RETURN)!, DigestDataFinal DigestDataFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GenerateMac GenerateMac: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GenerateMacInit GenerateMacInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, GenerateMacUpdate GenerateMacUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, GenerateMacFinal GenerateMacFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyMac VerifyMac: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyMacInit VerifyMacInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)!, VerifyMacUpdate VerifyMacUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)!, VerifyMacFinal VerifyMacFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, EncryptData EncryptData: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataInit EncryptDataInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, EncryptDataUpdate EncryptDataUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)!, EncryptDataFinal EncryptDataFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, DecryptData DecryptData: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataInit DecryptDataInit: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DecryptDataUpdate DecryptDataUpdate: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)!, DecryptDataFinal DecryptDataFinal: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, QueryKeySizeInBits QueryKeySizeInBits: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key_size>?) -> CSSM_RETURN)!, GenerateKey GenerateKey: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateKeyPair GenerateKeyPair: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_key>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, GenerateRandom GenerateRandom: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GenerateAlgorithmParams GenerateAlgorithmParams: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR?>?) -> CSSM_RETURN)!, WrapKey WrapKey: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_data>?, CSSM_WRAP_KEY_PTR?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, UnwrapKey UnwrapKey: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafePointer<CSSM_WRAP_KEY>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)!, DeriveKey DeriveKey: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)!, FreeKey FreeKey: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<cssm_key>?, CSSM_BOOL) -> CSSM_RETURN)!, PassThrough PassThrough: (@escaping (CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!, Login Login: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_data>?, UnsafeRawPointer?) -> CSSM_RETURN)!, Logout Logout: (@escaping (CSSM_CSP_HANDLE) -> CSSM_RETURN)!, ChangeLoginAcl ChangeLoginAcl: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)!, ObtainPrivateKeyFromPublicKey ObtainPrivateKeyFromPublicKey: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)!, RetrieveUniqueId RetrieveUniqueId: (@escaping (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, RetrieveCounter RetrieveCounter: (@escaping (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, VerifyDevice VerifyDevice: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, GetTimeValue GetTimeValue: (@escaping (CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, GetOperationalStatistics GetOperationalStatistics: (@escaping (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_csp_operational_statistics>?) -> CSSM_RETURN)!, GetLoginAcl GetLoginAcl: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!, GetKeyAcl GetKeyAcl: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!, ChangeKeyAcl ChangeKeyAcl: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?, UnsafePointer<cssm_key>?) -> CSSM_RETURN)!, GetKeyOwner GetKeyOwner: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, ChangeKeyOwner ChangeKeyOwner: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, GetLoginOwner GetLoginOwner: (@escaping (CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, ChangeLoginOwner ChangeLoginOwner: (@escaping (CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_csp_funcs.ChangeKeyAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>, UnsafePointer<CSSM_KEY>) -> CSSM_RETURN)! ``` |
| To | ``` var ChangeKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?, UnsafePointer<cssm_key>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ChangeKeyOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)! ``` |
| To | ``` var ChangeKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ChangeLoginAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)! ``` |
| To | ``` var ChangeLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ChangeLoginOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)! ``` |
| To | ``` var ChangeLoginOwner: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptData

|  | Declaration |
| --- | --- |
| From | ``` var DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var DecryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var DecryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptDataInit

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var DecryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DecryptDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)! ``` |
| To | ``` var DecryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DeriveKey

|  | Declaration |
| --- | --- |
| From | ``` var DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var DeriveKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestData

|  | Declaration |
| --- | --- |
| From | ``` var DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var DigestData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var DigestDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataInit

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var DigestDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.DigestDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var DigestDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptData

|  | Declaration |
| --- | --- |
| From | ``` var EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var EncryptData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var EncryptDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptDataInit

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var EncryptDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EncryptDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR, uint32, UnsafeMutablePointer<CSSM_SIZE>) -> CSSM_RETURN)! ``` |
| To | ``` var EncryptDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?, uint32, UnsafeMutablePointer<CSSM_SIZE>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.EventNotify

|  | Declaration |
| --- | --- |
| From | ``` var EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var EventNotify: ((CSSM_CSP_HANDLE, CSSM_CONTEXT_EVENT, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.FreeKey

|  | Declaration |
| --- | --- |
| From | ``` var FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KEY_PTR, CSSM_BOOL) -> CSSM_RETURN)! ``` |
| To | ``` var FreeKey: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<cssm_key>?, CSSM_BOOL) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateAlgorithmParams

|  | Declaration |
| --- | --- |
| From | ``` var GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, CSSM_DATA_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateAlgorithmParams: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_CONTEXT_ATTRIBUTE_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateKey

|  | Declaration |
| --- | --- |
| From | ``` var GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateKeyPair

|  | Declaration |
| --- | --- |
| From | ``` var GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, uint32, UnsafePointer<CSSM_DATA>, CSSM_KEY_PTR, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateKeyPair: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafeMutablePointer<cssm_key>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMac

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMacFinal

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMacInit

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateMacUpdate

|  | Declaration |
| --- | --- |
| From | ``` var GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GenerateRandom

|  | Declaration |
| --- | --- |
| From | ``` var GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateRandom: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetKeyAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var GetKeyAcl: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetKeyOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GetKeyOwner: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetLoginAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var GetLoginAcl: ((CSSM_CSP_HANDLE, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetLoginOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetLoginOwner: ((CSSM_CSP_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GetLoginOwner: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetOperationalStatistics

|  | Declaration |
| --- | --- |
| From | ``` var GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<CSSM_CSP_OPERATIONAL_STATISTICS>) -> CSSM_RETURN)! ``` |
| To | ``` var GetOperationalStatistics: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_csp_operational_statistics>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.GetTimeValue

|  | Declaration |
| --- | --- |
| From | ``` var GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var GetTimeValue: ((CSSM_CSP_HANDLE, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.Login

|  | Declaration |
| --- | --- |
| From | ``` var Login: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_DATA>, UnsafePointer<Void>) -> CSSM_RETURN)! ``` |
| To | ``` var Login: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_data>?, UnsafeRawPointer?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.ObtainPrivateKeyFromPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_KEY>, CSSM_KEY_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var ObtainPrivateKeyFromPublicKey: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |
| To | ``` var PassThrough: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.QueryKeySizeInBits

|  | Declaration |
| --- | --- |
| From | ``` var QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, CSSM_KEY_SIZE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var QueryKeySizeInBits: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafeMutablePointer<cssm_key_size>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.QuerySize

|  | Declaration |
| --- | --- |
| From | ``` var QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_BOOL, uint32, CSSM_QUERY_SIZE_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var QuerySize: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_BOOL, uint32, UnsafeMutablePointer<cssm_query_size_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.RetrieveCounter

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveCounter: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var RetrieveCounter: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.RetrieveUniqueId

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveUniqueId: ((CSSM_CSP_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var RetrieveUniqueId: ((CSSM_CSP_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignData

|  | Declaration |
| --- | --- |
| From | ``` var SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var SignData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var SignDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignDataInit

|  | Declaration |
| --- | --- |
| From | ``` var SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var SignDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.SignDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var SignDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.UnwrapKey

|  | Declaration |
| --- | --- |
| From | ``` var UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_WRAP_KEY>, uint32, uint32, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, CSSM_KEY_PTR, CSSM_DATA_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var UnwrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_key>?, UnsafePointer<CSSM_WRAP_KEY>?, uint32, uint32, UnsafePointer<cssm_data>?, UnsafePointer<cssm_resource_control_context>?, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyData

|  | Declaration |
| --- | --- |
| From | ``` var VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, CSSM_ALGORITHMS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyData: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, CSSM_ALGORITHMS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDataFinal

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyDataFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDataInit

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyDataInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDataUpdate

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyDataUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyDevice

|  | Declaration |
| --- | --- |
| From | ``` var VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyDevice: ((CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMac

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, uint32, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyMac: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, uint32, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMacFinal

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyMacFinal: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMacInit

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyMacInit: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.VerifyMacUpdate

|  | Declaration |
| --- | --- |
| From | ``` var VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var VerifyMacUpdate: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_spi_csp_funcs.WrapKey

|  | Declaration |
| --- | --- |
| From | ``` var WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_KEY>, UnsafePointer<CSSM_DATA>, CSSM_WRAP_KEY_PTR, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |
| To | ``` var WrapKey: ((CSSM_CSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_key>?, UnsafePointer<cssm_data>?, CSSM_WRAP_KEY_PTR?, CSSM_PRIVILEGE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_dl_funcs {     var DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!     var DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)!     var DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!     var DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!     var CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!     var DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!     var Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!     var GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!     var ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!     var GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!     var ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!     var GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!     var GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!     var FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!     var DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!     var DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!     var DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!     var PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(DbOpen DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)!, DbCreate DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbDelete DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, CreateRelation CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!, Authenticate Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)!, GetDbAcl GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)!, ChangeDbAcl ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)!, GetDbOwner GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)!, ChangeDbOwner ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)!, GetDbNames GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_spi_dl_funcs {     var DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!     var DbClose: ((cssm_dl_db_handle) -> CSSM_RETURN)!     var DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_dbinfo>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_resource_control_context>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!     var DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)!     var CreateRelation: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)!     var DestroyRelation: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!     var Authenticate: ((cssm_dl_db_handle, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)!     var GetDbAcl: ((cssm_dl_db_handle, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!     var ChangeDbAcl: ((cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)!     var GetDbOwner: ((cssm_dl_db_handle, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!     var ChangeDbOwner: ((cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!     var GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)!     var GetDbNameFromHandle: ((cssm_dl_db_handle, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)!     var FreeNameList: ((CSSM_DL_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)!     var DataInsert: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!     var DataDelete: ((cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!     var DataModify: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!     var DataGetFirst: ((cssm_dl_db_handle, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!     var DataGetNext: ((cssm_dl_db_handle, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!     var DataAbortQuery: ((cssm_dl_db_handle, CSSM_HANDLE) -> CSSM_RETURN)!     var DataGetFromUniqueRecordId: ((cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var FreeUniqueRecord: ((cssm_dl_db_handle, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!     var PassThrough: ((cssm_dl_db_handle, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!     init()     init(DbOpen DbOpen: (@escaping (CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!, DbClose DbClose: (@escaping (cssm_dl_db_handle) -> CSSM_RETURN)!, DbCreate DbCreate: (@escaping (CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_dbinfo>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_resource_control_context>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!, DbDelete DbDelete: (@escaping (CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)!, CreateRelation CreateRelation: (@escaping (cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)!, DestroyRelation DestroyRelation: (@escaping (cssm_dl_db_handle, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!, Authenticate Authenticate: (@escaping (cssm_dl_db_handle, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)!, GetDbAcl GetDbAcl: (@escaping (cssm_dl_db_handle, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)!, ChangeDbAcl ChangeDbAcl: (@escaping (cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)!, GetDbOwner GetDbOwner: (@escaping (cssm_dl_db_handle, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, ChangeDbOwner ChangeDbOwner: (@escaping (cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)!, GetDbNames GetDbNames: (@escaping (CSSM_DL_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)!, GetDbNameFromHandle GetDbNameFromHandle: (@escaping (cssm_dl_db_handle, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)!, FreeNameList FreeNameList: (@escaping (CSSM_DL_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)!, DataInsert DataInsert: (@escaping (cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataDelete DataDelete: (@escaping (cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, DataModify DataModify: (@escaping (cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst DataGetFirst: (@escaping (cssm_dl_db_handle, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataGetNext DataGetNext: (@escaping (cssm_dl_db_handle, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataAbortQuery DataAbortQuery: (@escaping (cssm_dl_db_handle, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: (@escaping (cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, FreeUniqueRecord FreeUniqueRecord: (@escaping (cssm_dl_db_handle, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, PassThrough PassThrough: (@escaping (cssm_dl_db_handle, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_dl_funcs.Authenticate

|  | Declaration |
| --- | --- |
| From | ``` var Authenticate: ((CSSM_DL_DB_HANDLE, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)! ``` |
| To | ``` var Authenticate: ((cssm_dl_db_handle, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.ChangeDbAcl

|  | Declaration |
| --- | --- |
| From | ``` var ChangeDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_EDIT>) -> CSSM_RETURN)! ``` |
| To | ``` var ChangeDbAcl: ((cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_edit>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.ChangeDbOwner

|  | Declaration |
| --- | --- |
| From | ``` var ChangeDbOwner: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<CSSM_ACL_OWNER_PROTOTYPE>) -> CSSM_RETURN)! ``` |
| To | ``` var ChangeDbOwner: ((cssm_dl_db_handle, UnsafePointer<cssm_access_credentials>?, UnsafePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.CreateRelation

|  | Declaration |
| --- | --- |
| From | ``` var CreateRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)! ``` |
| To | ``` var CreateRelation: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataAbortQuery

|  | Declaration |
| --- | --- |
| From | ``` var DataAbortQuery: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)! ``` |
| To | ``` var DataAbortQuery: ((cssm_dl_db_handle, CSSM_HANDLE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataDelete

|  | Declaration |
| --- | --- |
| From | ``` var DataDelete: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)! ``` |
| To | ``` var DataDelete: ((cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataGetFirst

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFirst: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var DataGetFirst: ((cssm_dl_db_handle, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataGetFromUniqueRecordId

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFromUniqueRecordId: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var DataGetFromUniqueRecordId: ((cssm_dl_db_handle, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataGetNext

|  | Declaration |
| --- | --- |
| From | ``` var DataGetNext: ((CSSM_DL_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var DataGetNext: ((cssm_dl_db_handle, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataInsert

|  | Declaration |
| --- | --- |
| From | ``` var DataInsert: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var DataInsert: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DataModify

|  | Declaration |
| --- | --- |
| From | ``` var DataModify: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)! ``` |
| To | ``` var DataModify: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbClose

|  | Declaration |
| --- | --- |
| From | ``` var DbClose: ((CSSM_DL_DB_HANDLE) -> CSSM_RETURN)! ``` |
| To | ``` var DbClose: ((cssm_dl_db_handle) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbCreate

|  | Declaration |
| --- | --- |
| From | ``` var DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_DBINFO>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)! ``` |
| To | ``` var DbCreate: ((CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_dbinfo>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_resource_control_context>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbDelete

|  | Declaration |
| --- | --- |
| From | ``` var DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>) -> CSSM_RETURN)! ``` |
| To | ``` var DbDelete: ((CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, UnsafePointer<cssm_access_credentials>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DbOpen

|  | Declaration |
| --- | --- |
| From | ``` var DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)! ``` |
| To | ``` var DbOpen: ((CSSM_DL_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.DestroyRelation

|  | Declaration |
| --- | --- |
| From | ``` var DestroyRelation: ((CSSM_DL_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)! ``` |
| To | ``` var DestroyRelation: ((cssm_dl_db_handle, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.FreeNameList

|  | Declaration |
| --- | --- |
| From | ``` var FreeNameList: ((CSSM_DL_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FreeNameList: ((CSSM_DL_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.FreeUniqueRecord

|  | Declaration |
| --- | --- |
| From | ``` var FreeUniqueRecord: ((CSSM_DL_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FreeUniqueRecord: ((cssm_dl_db_handle, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbAcl

|  | Declaration |
| --- | --- |
| From | ``` var GetDbAcl: ((CSSM_DL_DB_HANDLE, UnsafePointer<CSSM_STRING>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_ACL_ENTRY_INFO_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var GetDbAcl: ((cssm_dl_db_handle, UnsafePointer<Security.CSSM_STRING>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_acl_entry_info>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbNameFromHandle

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNameFromHandle: ((CSSM_DL_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)! ``` |
| To | ``` var GetDbNameFromHandle: ((cssm_dl_db_handle, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbNames

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var GetDbNames: ((CSSM_DL_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.GetDbOwner

|  | Declaration |
| --- | --- |
| From | ``` var GetDbOwner: ((CSSM_DL_DB_HANDLE, CSSM_ACL_OWNER_PROTOTYPE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GetDbOwner: ((cssm_dl_db_handle, UnsafeMutablePointer<cssm_acl_owner_prototype>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_dl_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: ((CSSM_DL_DB_HANDLE, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |
| To | ``` var PassThrough: ((cssm_dl_db_handle, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_kr_funcs {     var RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)!     var GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)!     var ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!     var RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!     var RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)!     var GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(RegistrationRequest RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RegistrationRetrieve RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)!, GenerateRecoveryFields GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)!, ProcessRecoveryFields ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)!, RecoveryRequest RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)!, RecoveryRetrieve RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)!, GetRecoveredObject GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, RecoveryRequestAbort RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_spi_kr_funcs {     var RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!     var RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_kr_profile>?) -> CSSM_RETURN)!     var GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!     var RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!     var RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?) -> CSSM_RETURN)!     var GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?, uint32, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var RecoveryRequestAbort: ((CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!     init()     init(RegistrationRequest RegistrationRequest: (@escaping (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, RegistrationRetrieve RegistrationRetrieve: (@escaping (CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_kr_profile>?) -> CSSM_RETURN)!, GenerateRecoveryFields GenerateRecoveryFields: (@escaping (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, ProcessRecoveryFields ProcessRecoveryFields: (@escaping (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)!, RecoveryRequest RecoveryRequest: (@escaping (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)!, RecoveryRetrieve RecoveryRetrieve: (@escaping (CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?) -> CSSM_RETURN)!, GetRecoveredObject GetRecoveredObject: (@escaping (CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?, uint32, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, RecoveryRequestAbort RecoveryRequestAbort: (@escaping (CSSM_KRSP_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, PassThrough PassThrough: (@escaping (CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_kr_funcs.GenerateRecoveryFields

|  | Declaration |
| --- | --- |
| From | ``` var GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GenerateRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.GetRecoveredObject

|  | Declaration |
| --- | --- |
| From | ``` var GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>, uint32, CSSM_KEY_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var GetRecoveredObject: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, uint32, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?, uint32, UnsafeMutablePointer<cssm_key>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |
| To | ``` var PassThrough: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.ProcessRecoveryFields

|  | Declaration |
| --- | --- |
| From | ``` var ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, CSSM_KR_POLICY_FLAGS, UnsafePointer<CSSM_DATA>) -> CSSM_RETURN)! ``` |
| To | ``` var ProcessRecoveryFields: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, CSSM_KR_POLICY_FLAGS, UnsafePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RecoveryRequest

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var RecoveryRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RecoveryRetrieve

|  | Declaration |
| --- | --- |
| From | ``` var RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR, UnsafeMutablePointer<uint32>) -> CSSM_RETURN)! ``` |
| To | ``` var RecoveryRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<uint32>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RegistrationRequest

|  | Declaration |
| --- | --- |
| From | ``` var RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_CONTEXT>, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>, CSSM_HANDLE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var RegistrationRequest: ((CSSM_KRSP_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_context>?, UnsafePointer<cssm_data>?, UnsafePointer<cssm_access_credentials>?, CSSM_KR_POLICY_FLAGS, UnsafeMutablePointer<sint32>?, CSSM_HANDLE_PTR?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_kr_funcs.RegistrationRetrieve

|  | Declaration |
| --- | --- |
| From | ``` var RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>, CSSM_KR_PROFILE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var RegistrationRetrieve: ((CSSM_KRSP_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_kr_profile>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_spi_tp_funcs {     var SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)!     var ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)!     var ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)!     var CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)!     var CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!     var FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)!     var FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)!     var CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!     var CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!     var CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!     var CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!     var CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)!     var TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!     var PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!     init()     init(SubmitCredRequest SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)!, RetrieveCredResult RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)!, ConfirmCredResult ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)!, ReceiveConfirmation ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)!, CertReclaimKey CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)!, CertReclaimAbort CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!, FormRequest FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)!, FormSubmit FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)!, CertGroupVerify CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertCreateTemplate CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertGetAllTemplateFields CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)!, CertSign CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlVerify CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CrlCreateTemplate CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRevoke CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)!, CertRemoveFromCrlTemplate CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, CrlSign CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, ApplyCrlToDb ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)!, CertGroupConstruct CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupPrune CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, CertGroupToTupleGroup CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)!, TupleGroupToCertGroup TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)!, PassThrough PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_spi_tp_funcs {     var SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<cssm_tp_request_set>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_result_set>?>?) -> CSSM_RETURN)!     var ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafePointer<cssm_tp_confirm_response>?, UnsafePointer<cssm_tp_authority_id>?) -> CSSM_RETURN)!     var ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_confirm_response>?>?, UnsafeMutablePointer<sint32>?) -> CSSM_RETURN)!     var CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?) -> CSSM_RETURN)!     var CertReclaimAbort: ((CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!     var FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_FORM_TYPE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_authority_id>?, UnsafePointer<cssm_tp_authority_id>?, UnsafeMutablePointer<cssm_access_credentials>?) -> CSSM_RETURN)!     var CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!     var CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!     var CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!     var CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, CSSM_TP_CERTCHANGE_REASON, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!     var CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafeRawPointer?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!     var CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!     var CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tuplegroup>?>?) -> CSSM_RETURN)!     var TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!     var PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!     init()     init(SubmitCredRequest SubmitCredRequest: (@escaping (CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<cssm_tp_request_set>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, RetrieveCredResult RetrieveCredResult: (@escaping (CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_result_set>?>?) -> CSSM_RETURN)!, ConfirmCredResult ConfirmCredResult: (@escaping (CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafePointer<cssm_tp_confirm_response>?, UnsafePointer<cssm_tp_authority_id>?) -> CSSM_RETURN)!, ReceiveConfirmation ReceiveConfirmation: (@escaping (CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_confirm_response>?>?, UnsafeMutablePointer<sint32>?) -> CSSM_RETURN)!, CertReclaimKey CertReclaimKey: (@escaping (CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?) -> CSSM_RETURN)!, CertReclaimAbort CertReclaimAbort: (@escaping (CSSM_TP_HANDLE, CSSM_LONG_HANDLE) -> CSSM_RETURN)!, FormRequest FormRequest: (@escaping (CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_FORM_TYPE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, FormSubmit FormSubmit: (@escaping (CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_authority_id>?, UnsafePointer<cssm_tp_authority_id>?, UnsafeMutablePointer<cssm_access_credentials>?) -> CSSM_RETURN)!, CertGroupVerify CertGroupVerify: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!, CertCreateTemplate CertCreateTemplate: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertGetAllTemplateFields CertGetAllTemplateFields: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)!, CertSign CertSign: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlVerify CrlVerify: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!, CrlCreateTemplate CrlCreateTemplate: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertRevoke CertRevoke: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, CSSM_TP_CERTCHANGE_REASON, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CertRemoveFromCrlTemplate CertRemoveFromCrlTemplate: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, CrlSign CrlSign: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, ApplyCrlToDb ApplyCrlToDb: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)!, CertGroupConstruct CertGroupConstruct: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafeRawPointer?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, CertGroupPrune CertGroupPrune: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, CertGroupToTupleGroup CertGroupToTupleGroup: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tuplegroup>?>?) -> CSSM_RETURN)!, TupleGroupToCertGroup TupleGroupToCertGroup: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)!, PassThrough PassThrough: (@escaping (CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_spi_tp_funcs.ApplyCrlToDb

|  | Declaration |
| --- | --- |
| From | ``` var ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var ApplyCrlToDb: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGetAllTemplateFields

|  | Declaration |
| --- | --- |
| From | ``` var CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_FIELD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGetAllTemplateFields: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_field>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupConstruct

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<Void>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGroupConstruct: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafeRawPointer?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupPrune

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGroupPrune: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_dl_db_list>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupToTupleGroup

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafeMutablePointer<CSSM_TUPLEGROUP_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var CertGroupToTupleGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tuplegroup>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertGroupVerify

|  | Declaration |
| --- | --- |
| From | ``` var CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertGroupVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertReclaimKey

|  | Declaration |
| --- | --- |
| From | ``` var CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_RESOURCE_CONTROL_CONTEXT>) -> CSSM_RETURN)! ``` |
| To | ``` var CertReclaimKey: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_CERTGROUP>?, uint32, CSSM_LONG_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_resource_control_context>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertRemoveFromCrlTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertRemoveFromCrlTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertRevoke

|  | Declaration |
| --- | --- |
| From | ``` var CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_TP_CERTCHANGE_REASON, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertRevoke: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, CSSM_TP_CERTCHANGE_REASON, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CertSign

|  | Declaration |
| --- | --- |
| From | ``` var CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CertSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.ConfirmCredResult

|  | Declaration |
| --- | --- |
| From | ``` var ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafePointer<CSSM_TP_CONFIRM_RESPONSE>, UnsafePointer<CSSM_TP_AUTHORITY_ID>) -> CSSM_RETURN)! ``` |
| To | ``` var ConfirmCredResult: ((CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafePointer<cssm_tp_confirm_response>?, UnsafePointer<cssm_tp_authority_id>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CrlCreateTemplate

|  | Declaration |
| --- | --- |
| From | ``` var CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<CSSM_FIELD>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlCreateTemplate: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, uint32, UnsafePointer<cssm_field>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CrlSign

|  | Declaration |
| --- | --- |
| From | ``` var CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlSign: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.CrlVerify

|  | Declaration |
| --- | --- |
| From | ``` var CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<CSSM_ENCODED_CRL>, UnsafePointer<CSSM_CERTGROUP>, UnsafePointer<CSSM_TP_VERIFY_CONTEXT>, CSSM_TP_VERIFY_CONTEXT_RESULT_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CrlVerify: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CSP_HANDLE, UnsafePointer<cssm_encoded_crl>?, UnsafePointer<CSSM_CERTGROUP>?, UnsafePointer<cssm_tp_verify_context>?, UnsafeMutablePointer<cssm_tp_verify_context_result>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.FormRequest

|  | Declaration |
| --- | --- |
| From | ``` var FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_FORM_TYPE, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FormRequest: ((CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_FORM_TYPE, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.FormSubmit

|  | Declaration |
| --- | --- |
| From | ``` var FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_ACCESS_CREDENTIALS_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FormSubmit: ((CSSM_TP_HANDLE, CSSM_TP_FORM_TYPE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_authority_id>?, UnsafePointer<cssm_tp_authority_id>?, UnsafeMutablePointer<cssm_access_credentials>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.PassThrough

|  | Declaration |
| --- | --- |
| From | ``` var PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<CSSM_DL_DB_LIST>, uint32, UnsafePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> CSSM_RETURN)! ``` |
| To | ``` var PassThrough: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, CSSM_CC_HANDLE, UnsafePointer<cssm_dl_db_list>?, uint32, UnsafeRawPointer?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.ReceiveConfirmation

|  | Declaration |
| --- | --- |
| From | ``` var ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_TP_CONFIRM_RESPONSE_PTR>, UnsafeMutablePointer<sint32>) -> CSSM_RETURN)! ``` |
| To | ``` var ReceiveConfirmation: ((CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_confirm_response>?>?, UnsafeMutablePointer<sint32>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.RetrieveCredResult

|  | Declaration |
| --- | --- |
| From | ``` var RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_DATA>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, UnsafeMutablePointer<CSSM_BOOL>, UnsafeMutablePointer<CSSM_TP_RESULT_SET_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var RetrieveCredResult: ((CSSM_TP_HANDLE, UnsafePointer<cssm_data>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<CSSM_BOOL>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_tp_result_set>?>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.SubmitCredRequest

|  | Declaration |
| --- | --- |
| From | ``` var SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<CSSM_TP_AUTHORITY_ID>, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<CSSM_TP_REQUEST_SET>, UnsafePointer<CSSM_TP_CALLERAUTH_CONTEXT>, UnsafeMutablePointer<sint32>, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var SubmitCredRequest: ((CSSM_TP_HANDLE, UnsafePointer<cssm_tp_authority_id>?, CSSM_TP_AUTHORITY_REQUEST_TYPE, UnsafePointer<cssm_tp_request_set>?, UnsafePointer<cssm_tp_callerauth_context>?, UnsafeMutablePointer<sint32>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified cssm_spi_tp_funcs.TupleGroupToCertGroup

|  | Declaration |
| --- | --- |
| From | ``` var TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<CSSM_TUPLEGROUP>, UnsafeMutablePointer<CSSM_CERTGROUP_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var TupleGroupToCertGroup: ((CSSM_TP_HANDLE, CSSM_CL_HANDLE, UnsafePointer<cssm_tuplegroup>?, UnsafeMutablePointer<CSSM_CERTGROUP_PTR?>?) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_state_funcs {     var cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!     var cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!     var cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)!     var cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!     var cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)!     var cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!     init()     init(cssm_GetAttachFunctions cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_ReleaseAttachFunctions cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!, cssm_GetAppMemoryFunctions cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)!, cssm_IsFuncCallValid cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)!, cssm_DeregisterManagerServices cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)!, cssm_DeliverModuleManagerEvent cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_state_funcs {     var cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!     var cssm_ReleaseAttachFunctions: ((CSSM_MODULE_HANDLE) -> CSSM_RETURN)!     var cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_upcalls>?) -> CSSM_RETURN)!     var cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, Security.CSSM_PROC_ADDR?, Security.CSSM_PROC_ADDR?, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>?, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!     var cssm_DeregisterManagerServices: ((UnsafePointer<cssm_guid>?) -> CSSM_RETURN)!     var cssm_DeliverModuleManagerEvent: ((UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)!     init()     init(cssm_GetAttachFunctions cssm_GetAttachFunctions: (@escaping (CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!, cssm_ReleaseAttachFunctions cssm_ReleaseAttachFunctions: (@escaping (CSSM_MODULE_HANDLE) -> CSSM_RETURN)!, cssm_GetAppMemoryFunctions cssm_GetAppMemoryFunctions: (@escaping (CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_upcalls>?) -> CSSM_RETURN)!, cssm_IsFuncCallValid cssm_IsFuncCallValid: (@escaping (CSSM_MODULE_HANDLE, Security.CSSM_PROC_ADDR?, Security.CSSM_PROC_ADDR?, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>?, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)!, cssm_DeregisterManagerServices cssm_DeregisterManagerServices: (@escaping (UnsafePointer<cssm_guid>?) -> CSSM_RETURN)!, cssm_DeliverModuleManagerEvent cssm_DeliverModuleManagerEvent: (@escaping (UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)!) } ``` |

Modified cssm_state_funcs.cssm_DeliverModuleManagerEvent

|  | Declaration |
| --- | --- |
| From | ``` var cssm_DeliverModuleManagerEvent: ((UnsafePointer<CSSM_MANAGER_EVENT_NOTIFICATION>) -> CSSM_RETURN)! ``` |
| To | ``` var cssm_DeliverModuleManagerEvent: ((UnsafePointer<cssm_manager_event_notification>?) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_DeregisterManagerServices

|  | Declaration |
| --- | --- |
| From | ``` var cssm_DeregisterManagerServices: ((UnsafePointer<CSSM_GUID>) -> CSSM_RETURN)! ``` |
| To | ``` var cssm_DeregisterManagerServices: ((UnsafePointer<cssm_guid>?) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_GetAppMemoryFunctions

|  | Declaration |
| --- | --- |
| From | ``` var cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, CSSM_UPCALLS_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var cssm_GetAppMemoryFunctions: ((CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_upcalls>?) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_GetAttachFunctions

|  | Declaration |
| --- | --- |
| From | ``` var cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, CSSM_GUID_PTR, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)! ``` |
| To | ``` var cssm_GetAttachFunctions: ((CSSM_MODULE_HANDLE, CSSM_SERVICE_MASK, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)! ``` |

Modified cssm_state_funcs.cssm_IsFuncCallValid

|  | Declaration |
| --- | --- |
| From | ``` var cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, CSSM_PROC_ADDR!, CSSM_PROC_ADDR!, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>) -> CSSM_RETURN)! ``` |
| To | ``` var cssm_IsFuncCallValid: ((CSSM_MODULE_HANDLE, Security.CSSM_PROC_ADDR?, Security.CSSM_PROC_ADDR?, CSSM_PRIVILEGE, UnsafeMutablePointer<CSSM_PRIVILEGE>?, CSSM_BITMASK, UnsafeMutablePointer<CSSM_BOOL>?) -> CSSM_RETURN)! ``` |

Modified cssm_subservice_uid [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_subservice_uid {     var Guid: CSSM_GUID     var Version: CSSM_VERSION     var SubserviceId: uint32     var SubserviceType: CSSM_SERVICE_TYPE     init()     init(Guid Guid: CSSM_GUID, Version Version: CSSM_VERSION, SubserviceId SubserviceId: uint32, SubserviceType SubserviceType: CSSM_SERVICE_TYPE) } ``` |
| To | ``` struct cssm_subservice_uid {     var Guid: cssm_guid     var Version: cssm_version     var SubserviceId: uint32     var SubserviceType: CSSM_SERVICE_TYPE     init()     init(Guid Guid: cssm_guid, Version Version: cssm_version, SubserviceId SubserviceId: uint32, SubserviceType SubserviceType: CSSM_SERVICE_TYPE) } ``` |

Modified cssm_subservice_uid.Guid

|  | Declaration |
| --- | --- |
| From | ``` var Guid: CSSM_GUID ``` |
| To | ``` var Guid: cssm_guid ``` |

Modified cssm_subservice_uid.init(Guid: cssm_guid, Version: cssm_version, SubserviceId: uint32, SubserviceType: CSSM_SERVICE_TYPE)

|  | Declaration |
| --- | --- |
| From | ``` init(Guid Guid: CSSM_GUID, Version Version: CSSM_VERSION, SubserviceId SubserviceId: uint32, SubserviceType SubserviceType: CSSM_SERVICE_TYPE) ``` |
| To | ``` init(Guid Guid: cssm_guid, Version Version: cssm_version, SubserviceId SubserviceId: uint32, SubserviceType SubserviceType: CSSM_SERVICE_TYPE) ``` |

Modified cssm_subservice_uid.Version

|  | Declaration |
| --- | --- |
| From | ``` var Version: CSSM_VERSION ``` |
| To | ``` var Version: cssm_version ``` |

Modified CSSM_TP_APPLE_EVIDENCE_INFO [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CSSM_TP_APPLE_EVIDENCE_INFO {     var StatusBits: CSSM_TP_APPLE_CERT_STATUS     var NumStatusCodes: uint32     var StatusCodes: UnsafeMutablePointer<CSSM_RETURN>     var Index: uint32     var DlDbHandle: CSSM_DL_DB_HANDLE     var UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR     init()     init(StatusBits StatusBits: CSSM_TP_APPLE_CERT_STATUS, NumStatusCodes NumStatusCodes: uint32, StatusCodes StatusCodes: UnsafeMutablePointer<CSSM_RETURN>, Index Index: uint32, DlDbHandle DlDbHandle: CSSM_DL_DB_HANDLE, UniqueRecord UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR) } ``` |
| To | ``` struct CSSM_TP_APPLE_EVIDENCE_INFO {     var StatusBits: CSSM_TP_APPLE_CERT_STATUS     var NumStatusCodes: uint32     var StatusCodes: UnsafeMutablePointer<CSSM_RETURN>!     var Index: uint32     var DlDbHandle: cssm_dl_db_handle     var UniqueRecord: UnsafeMutablePointer<cssm_db_unique_record>!     init()     init(StatusBits StatusBits: CSSM_TP_APPLE_CERT_STATUS, NumStatusCodes NumStatusCodes: uint32, StatusCodes StatusCodes: UnsafeMutablePointer<CSSM_RETURN>!, Index Index: uint32, DlDbHandle DlDbHandle: cssm_dl_db_handle, UniqueRecord UniqueRecord: UnsafeMutablePointer<cssm_db_unique_record>!) } ``` |

Modified CSSM_TP_APPLE_EVIDENCE_INFO.DlDbHandle

|  | Declaration |
| --- | --- |
| From | ``` var DlDbHandle: CSSM_DL_DB_HANDLE ``` |
| To | ``` var DlDbHandle: cssm_dl_db_handle ``` |

Modified CSSM_TP_APPLE_EVIDENCE_INFO.StatusCodes

|  | Declaration |
| --- | --- |
| From | ``` var StatusCodes: UnsafeMutablePointer<CSSM_RETURN> ``` |
| To | ``` var StatusCodes: UnsafeMutablePointer<CSSM_RETURN>! ``` |

Modified CSSM_TP_APPLE_EVIDENCE_INFO.UniqueRecord

|  | Declaration |
| --- | --- |
| From | ``` var UniqueRecord: CSSM_DB_UNIQUE_RECORD_PTR ``` |
| To | ``` var UniqueRecord: UnsafeMutablePointer<cssm_db_unique_record>! ``` |

Modified cssm_tp_authority_id [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_authority_id {     var AuthorityCert: UnsafeMutablePointer<CSSM_DATA>     var AuthorityLocation: CSSM_NET_ADDRESS_PTR     init()     init(AuthorityCert AuthorityCert: UnsafeMutablePointer<CSSM_DATA>, AuthorityLocation AuthorityLocation: CSSM_NET_ADDRESS_PTR) } ``` |
| To | ``` struct cssm_tp_authority_id {     var AuthorityCert: UnsafeMutablePointer<cssm_data>!     var AuthorityLocation: UnsafeMutablePointer<cssm_net_address>!     init()     init(AuthorityCert AuthorityCert: UnsafeMutablePointer<cssm_data>!, AuthorityLocation AuthorityLocation: UnsafeMutablePointer<cssm_net_address>!) } ``` |

Modified cssm_tp_authority_id.AuthorityCert

|  | Declaration |
| --- | --- |
| From | ``` var AuthorityCert: UnsafeMutablePointer<CSSM_DATA> ``` |
| To | ``` var AuthorityCert: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_tp_authority_id.AuthorityLocation

|  | Declaration |
| --- | --- |
| From | ``` var AuthorityLocation: CSSM_NET_ADDRESS_PTR ``` |
| To | ``` var AuthorityLocation: UnsafeMutablePointer<cssm_net_address>! ``` |

Modified cssm_tp_callerauth_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_callerauth_context {     var Policy: CSSM_TP_POLICYINFO     var VerifyTime: CSSM_TIMESTRING     var VerificationAbortOn: CSSM_TP_STOP_ON     var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK!     var NumberOfAnchorCerts: uint32     var AnchorCerts: CSSM_DATA_PTR     var DBList: CSSM_DL_DB_LIST_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(Policy Policy: CSSM_TP_POLICYINFO, VerifyTime VerifyTime: CSSM_TIMESTRING, VerificationAbortOn VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK!, NumberOfAnchorCerts NumberOfAnchorCerts: uint32, AnchorCerts AnchorCerts: CSSM_DATA_PTR, DBList DBList: CSSM_DL_DB_LIST_PTR, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_callerauth_context {     var Policy: cssm_tp_policyinfo     var VerifyTime: CSSM_TIMESTRING!     var VerificationAbortOn: CSSM_TP_STOP_ON     var CallbackWithVerifiedCert: Security.CSSM_TP_VERIFICATION_RESULTS_CALLBACK!     var NumberOfAnchorCerts: uint32     var AnchorCerts: UnsafeMutablePointer<cssm_data>!     var DBList: UnsafeMutablePointer<cssm_dl_db_list>!     var CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(Policy Policy: cssm_tp_policyinfo, VerifyTime VerifyTime: CSSM_TIMESTRING!, VerificationAbortOn VerificationAbortOn: CSSM_TP_STOP_ON, CallbackWithVerifiedCert CallbackWithVerifiedCert: Security.CSSM_TP_VERIFICATION_RESULTS_CALLBACK!, NumberOfAnchorCerts NumberOfAnchorCerts: uint32, AnchorCerts AnchorCerts: UnsafeMutablePointer<cssm_data>!, DBList DBList: UnsafeMutablePointer<cssm_dl_db_list>!, CallerCredentials CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_tp_callerauth_context.AnchorCerts

|  | Declaration |
| --- | --- |
| From | ``` var AnchorCerts: CSSM_DATA_PTR ``` |
| To | ``` var AnchorCerts: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_tp_callerauth_context.CallbackWithVerifiedCert

|  | Declaration |
| --- | --- |
| From | ``` var CallbackWithVerifiedCert: CSSM_TP_VERIFICATION_RESULTS_CALLBACK! ``` |
| To | ``` var CallbackWithVerifiedCert: Security.CSSM_TP_VERIFICATION_RESULTS_CALLBACK! ``` |

Modified cssm_tp_callerauth_context.CallerCredentials

|  | Declaration |
| --- | --- |
| From | ``` var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_tp_callerauth_context.DBList

|  | Declaration |
| --- | --- |
| From | ``` var DBList: CSSM_DL_DB_LIST_PTR ``` |
| To | ``` var DBList: UnsafeMutablePointer<cssm_dl_db_list>! ``` |

Modified cssm_tp_callerauth_context.Policy

|  | Declaration |
| --- | --- |
| From | ``` var Policy: CSSM_TP_POLICYINFO ``` |
| To | ``` var Policy: cssm_tp_policyinfo ``` |

Modified cssm_tp_callerauth_context.VerifyTime

|  | Declaration |
| --- | --- |
| From | ``` var VerifyTime: CSSM_TIMESTRING ``` |
| To | ``` var VerifyTime: CSSM_TIMESTRING! ``` |

Modified cssm_tp_certchange_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certchange_input {     var Action: CSSM_TP_CERTCHANGE_ACTION     var Reason: CSSM_TP_CERTCHANGE_REASON     var CLHandle: CSSM_CL_HANDLE     var Cert: CSSM_DATA_PTR     var ChangeInfo: CSSM_FIELD_PTR     var StartTime: CSSM_TIMESTRING     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(Action Action: CSSM_TP_CERTCHANGE_ACTION, Reason Reason: CSSM_TP_CERTCHANGE_REASON, CLHandle CLHandle: CSSM_CL_HANDLE, Cert Cert: CSSM_DATA_PTR, ChangeInfo ChangeInfo: CSSM_FIELD_PTR, StartTime StartTime: CSSM_TIMESTRING, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_certchange_input {     var Action: CSSM_TP_CERTCHANGE_ACTION     var Reason: CSSM_TP_CERTCHANGE_REASON     var CLHandle: CSSM_CL_HANDLE     var Cert: UnsafeMutablePointer<cssm_data>!     var ChangeInfo: UnsafeMutablePointer<cssm_field>!     var StartTime: CSSM_TIMESTRING!     var CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(Action Action: CSSM_TP_CERTCHANGE_ACTION, Reason Reason: CSSM_TP_CERTCHANGE_REASON, CLHandle CLHandle: CSSM_CL_HANDLE, Cert Cert: UnsafeMutablePointer<cssm_data>!, ChangeInfo ChangeInfo: UnsafeMutablePointer<cssm_field>!, StartTime StartTime: CSSM_TIMESTRING!, CallerCredentials CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_tp_certchange_input.CallerCredentials

|  | Declaration |
| --- | --- |
| From | ``` var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_tp_certchange_input.Cert

|  | Declaration |
| --- | --- |
| From | ``` var Cert: CSSM_DATA_PTR ``` |
| To | ``` var Cert: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_tp_certchange_input.ChangeInfo

|  | Declaration |
| --- | --- |
| From | ``` var ChangeInfo: CSSM_FIELD_PTR ``` |
| To | ``` var ChangeInfo: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certchange_input.StartTime

|  | Declaration |
| --- | --- |
| From | ``` var StartTime: CSSM_TIMESTRING ``` |
| To | ``` var StartTime: CSSM_TIMESTRING! ``` |

Modified cssm_tp_certchange_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certchange_output {     var ActionStatus: CSSM_TP_CERTCHANGE_STATUS     var RevokeInfo: CSSM_FIELD     init()     init(ActionStatus ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo RevokeInfo: CSSM_FIELD) } ``` |
| To | ``` struct cssm_tp_certchange_output {     var ActionStatus: CSSM_TP_CERTCHANGE_STATUS     var RevokeInfo: cssm_field     init()     init(ActionStatus ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo RevokeInfo: cssm_field) } ``` |

Modified cssm_tp_certchange_output.init(ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo: cssm_field)

|  | Declaration |
| --- | --- |
| From | ``` init(ActionStatus ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo RevokeInfo: CSSM_FIELD) ``` |
| To | ``` init(ActionStatus ActionStatus: CSSM_TP_CERTCHANGE_STATUS, RevokeInfo RevokeInfo: cssm_field) ``` |

Modified cssm_tp_certchange_output.RevokeInfo

|  | Declaration |
| --- | --- |
| From | ``` var RevokeInfo: CSSM_FIELD ``` |
| To | ``` var RevokeInfo: cssm_field ``` |

Modified cssm_tp_certissue_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certissue_input {     var CSPSubserviceUid: CSSM_SUBSERVICE_UID     var CLHandle: CSSM_CL_HANDLE     var NumberOfTemplateFields: uint32     var SubjectCertFields: CSSM_FIELD_PTR     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CSPSubserviceUid CSPSubserviceUid: CSSM_SUBSERVICE_UID, CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfTemplateFields NumberOfTemplateFields: uint32, SubjectCertFields SubjectCertFields: CSSM_FIELD_PTR, MoreServiceRequests MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls NumberOfServiceControls: uint32, ServiceControls ServiceControls: CSSM_FIELD_PTR, UserCredentials UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_certissue_input {     var CSPSubserviceUid: cssm_subservice_uid     var CLHandle: CSSM_CL_HANDLE     var NumberOfTemplateFields: uint32     var SubjectCertFields: UnsafeMutablePointer<cssm_field>!     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: UnsafeMutablePointer<cssm_field>!     var UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(CSPSubserviceUid CSPSubserviceUid: cssm_subservice_uid, CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfTemplateFields NumberOfTemplateFields: uint32, SubjectCertFields SubjectCertFields: UnsafeMutablePointer<cssm_field>!, MoreServiceRequests MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls NumberOfServiceControls: uint32, ServiceControls ServiceControls: UnsafeMutablePointer<cssm_field>!, UserCredentials UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_tp_certissue_input.CSPSubserviceUid

|  | Declaration |
| --- | --- |
| From | ``` var CSPSubserviceUid: CSSM_SUBSERVICE_UID ``` |
| To | ``` var CSPSubserviceUid: cssm_subservice_uid ``` |

Modified cssm_tp_certissue_input.ServiceControls

|  | Declaration |
| --- | --- |
| From | ``` var ServiceControls: CSSM_FIELD_PTR ``` |
| To | ``` var ServiceControls: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certissue_input.SubjectCertFields

|  | Declaration |
| --- | --- |
| From | ``` var SubjectCertFields: CSSM_FIELD_PTR ``` |
| To | ``` var SubjectCertFields: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certissue_input.UserCredentials

|  | Declaration |
| --- | --- |
| From | ``` var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var UserCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_tp_certissue_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certissue_output {     var IssueStatus: CSSM_TP_CERTISSUE_STATUS     var CertGroup: CSSM_CERTGROUP_PTR     var PerformedServiceRequests: CSSM_TP_SERVICES     init()     init(IssueStatus IssueStatus: CSSM_TP_CERTISSUE_STATUS, CertGroup CertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests PerformedServiceRequests: CSSM_TP_SERVICES) } ``` |
| To | ``` struct cssm_tp_certissue_output {     var IssueStatus: CSSM_TP_CERTISSUE_STATUS     var CertGroup: CSSM_CERTGROUP_PTR!     var PerformedServiceRequests: CSSM_TP_SERVICES     init()     init(IssueStatus IssueStatus: CSSM_TP_CERTISSUE_STATUS, CertGroup CertGroup: CSSM_CERTGROUP_PTR!, PerformedServiceRequests PerformedServiceRequests: CSSM_TP_SERVICES) } ``` |

Modified cssm_tp_certissue_output.CertGroup

|  | Declaration |
| --- | --- |
| From | ``` var CertGroup: CSSM_CERTGROUP_PTR ``` |
| To | ``` var CertGroup: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_tp_certnotarize_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certnotarize_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfFields: uint32     var MoreFields: CSSM_FIELD_PTR     var SignScope: CSSM_FIELD_PTR     var ScopeSize: uint32     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfFields NumberOfFields: uint32, MoreFields MoreFields: CSSM_FIELD_PTR, SignScope SignScope: CSSM_FIELD_PTR, ScopeSize ScopeSize: uint32, MoreServiceRequests MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls NumberOfServiceControls: uint32, ServiceControls ServiceControls: CSSM_FIELD_PTR, UserCredentials UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_certnotarize_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfFields: uint32     var MoreFields: UnsafeMutablePointer<cssm_field>!     var SignScope: UnsafeMutablePointer<cssm_field>!     var ScopeSize: uint32     var MoreServiceRequests: CSSM_TP_SERVICES     var NumberOfServiceControls: uint32     var ServiceControls: UnsafeMutablePointer<cssm_field>!     var UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfFields NumberOfFields: uint32, MoreFields MoreFields: UnsafeMutablePointer<cssm_field>!, SignScope SignScope: UnsafeMutablePointer<cssm_field>!, ScopeSize ScopeSize: uint32, MoreServiceRequests MoreServiceRequests: CSSM_TP_SERVICES, NumberOfServiceControls NumberOfServiceControls: uint32, ServiceControls ServiceControls: UnsafeMutablePointer<cssm_field>!, UserCredentials UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_tp_certnotarize_input.MoreFields

|  | Declaration |
| --- | --- |
| From | ``` var MoreFields: CSSM_FIELD_PTR ``` |
| To | ``` var MoreFields: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certnotarize_input.ServiceControls

|  | Declaration |
| --- | --- |
| From | ``` var ServiceControls: CSSM_FIELD_PTR ``` |
| To | ``` var ServiceControls: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certnotarize_input.SignScope

|  | Declaration |
| --- | --- |
| From | ``` var SignScope: CSSM_FIELD_PTR ``` |
| To | ``` var SignScope: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certnotarize_input.UserCredentials

|  | Declaration |
| --- | --- |
| From | ``` var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var UserCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_tp_certnotarize_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certnotarize_output {     var NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS     var NotarizedCertGroup: CSSM_CERTGROUP_PTR     var PerformedServiceRequests: CSSM_TP_SERVICES     init()     init(NotarizeStatus NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS, NotarizedCertGroup NotarizedCertGroup: CSSM_CERTGROUP_PTR, PerformedServiceRequests PerformedServiceRequests: CSSM_TP_SERVICES) } ``` |
| To | ``` struct cssm_tp_certnotarize_output {     var NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS     var NotarizedCertGroup: CSSM_CERTGROUP_PTR!     var PerformedServiceRequests: CSSM_TP_SERVICES     init()     init(NotarizeStatus NotarizeStatus: CSSM_TP_CERTNOTARIZE_STATUS, NotarizedCertGroup NotarizedCertGroup: CSSM_CERTGROUP_PTR!, PerformedServiceRequests PerformedServiceRequests: CSSM_TP_SERVICES) } ``` |

Modified cssm_tp_certnotarize_output.NotarizedCertGroup

|  | Declaration |
| --- | --- |
| From | ``` var NotarizedCertGroup: CSSM_CERTGROUP_PTR ``` |
| To | ``` var NotarizedCertGroup: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_tp_certreclaim_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certreclaim_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfSelectionFields: uint32     var SelectionFields: CSSM_FIELD_PTR     var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfSelectionFields NumberOfSelectionFields: uint32, SelectionFields SelectionFields: CSSM_FIELD_PTR, UserCredentials UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_certreclaim_input {     var CLHandle: CSSM_CL_HANDLE     var NumberOfSelectionFields: uint32     var SelectionFields: UnsafeMutablePointer<cssm_field>!     var UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, NumberOfSelectionFields NumberOfSelectionFields: uint32, SelectionFields SelectionFields: UnsafeMutablePointer<cssm_field>!, UserCredentials UserCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_tp_certreclaim_input.SelectionFields

|  | Declaration |
| --- | --- |
| From | ``` var SelectionFields: CSSM_FIELD_PTR ``` |
| To | ``` var SelectionFields: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_certreclaim_input.UserCredentials

|  | Declaration |
| --- | --- |
| From | ``` var UserCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var UserCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_tp_certreclaim_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certreclaim_output {     var ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS     var ReclaimedCertGroup: CSSM_CERTGROUP_PTR     var KeyCacheHandle: CSSM_LONG_HANDLE     init()     init(ReclaimStatus ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS, ReclaimedCertGroup ReclaimedCertGroup: CSSM_CERTGROUP_PTR, KeyCacheHandle KeyCacheHandle: CSSM_LONG_HANDLE) } ``` |
| To | ``` struct cssm_tp_certreclaim_output {     var ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS     var ReclaimedCertGroup: CSSM_CERTGROUP_PTR!     var KeyCacheHandle: CSSM_LONG_HANDLE     init()     init(ReclaimStatus ReclaimStatus: CSSM_TP_CERTRECLAIM_STATUS, ReclaimedCertGroup ReclaimedCertGroup: CSSM_CERTGROUP_PTR!, KeyCacheHandle KeyCacheHandle: CSSM_LONG_HANDLE) } ``` |

Modified cssm_tp_certreclaim_output.ReclaimedCertGroup

|  | Declaration |
| --- | --- |
| From | ``` var ReclaimedCertGroup: CSSM_CERTGROUP_PTR ``` |
| To | ``` var ReclaimedCertGroup: CSSM_CERTGROUP_PTR! ``` |

Modified cssm_tp_certverify_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certverify_input {     var CLHandle: CSSM_CL_HANDLE     var Cert: CSSM_DATA_PTR     var VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, Cert Cert: CSSM_DATA_PTR, VerifyContext VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR) } ``` |
| To | ``` struct cssm_tp_certverify_input {     var CLHandle: CSSM_CL_HANDLE     var Cert: UnsafeMutablePointer<cssm_data>!     var VerifyContext: UnsafeMutablePointer<cssm_tp_verify_context>!     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, Cert Cert: UnsafeMutablePointer<cssm_data>!, VerifyContext VerifyContext: UnsafeMutablePointer<cssm_tp_verify_context>!) } ``` |

Modified cssm_tp_certverify_input.Cert

|  | Declaration |
| --- | --- |
| From | ``` var Cert: CSSM_DATA_PTR ``` |
| To | ``` var Cert: UnsafeMutablePointer<cssm_data>! ``` |

Modified cssm_tp_certverify_input.VerifyContext

|  | Declaration |
| --- | --- |
| From | ``` var VerifyContext: CSSM_TP_VERIFY_CONTEXT_PTR ``` |
| To | ``` var VerifyContext: UnsafeMutablePointer<cssm_tp_verify_context>! ``` |

Modified cssm_tp_certverify_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_certverify_output {     var VerifyStatus: CSSM_TP_CERTVERIFY_STATUS     var NumberOfEvidence: uint32     var Evidence: CSSM_EVIDENCE_PTR     init()     init(VerifyStatus VerifyStatus: CSSM_TP_CERTVERIFY_STATUS, NumberOfEvidence NumberOfEvidence: uint32, Evidence Evidence: CSSM_EVIDENCE_PTR) } ``` |
| To | ``` struct cssm_tp_certverify_output {     var VerifyStatus: CSSM_TP_CERTVERIFY_STATUS     var NumberOfEvidence: uint32     var Evidence: UnsafeMutablePointer<cssm_evidence>!     init()     init(VerifyStatus VerifyStatus: CSSM_TP_CERTVERIFY_STATUS, NumberOfEvidence NumberOfEvidence: uint32, Evidence Evidence: UnsafeMutablePointer<cssm_evidence>!) } ``` |

Modified cssm_tp_certverify_output.Evidence

|  | Declaration |
| --- | --- |
| From | ``` var Evidence: CSSM_EVIDENCE_PTR ``` |
| To | ``` var Evidence: UnsafeMutablePointer<cssm_evidence>! ``` |

Modified cssm_tp_confirm_response [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_confirm_response {     var NumberOfResponses: uint32     var Responses: CSSM_TP_CONFIRM_STATUS_PTR     init()     init(NumberOfResponses NumberOfResponses: uint32, Responses Responses: CSSM_TP_CONFIRM_STATUS_PTR) } ``` |
| To | ``` struct cssm_tp_confirm_response {     var NumberOfResponses: uint32     var Responses: CSSM_TP_CONFIRM_STATUS_PTR!     init()     init(NumberOfResponses NumberOfResponses: uint32, Responses Responses: CSSM_TP_CONFIRM_STATUS_PTR!) } ``` |

Modified cssm_tp_confirm_response.Responses

|  | Declaration |
| --- | --- |
| From | ``` var Responses: CSSM_TP_CONFIRM_STATUS_PTR ``` |
| To | ``` var Responses: CSSM_TP_CONFIRM_STATUS_PTR! ``` |

Modified cssm_tp_crlissue_input [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_crlissue_input {     var CLHandle: CSSM_CL_HANDLE     var CrlIdentifier: uint32     var CrlThisTime: CSSM_TIMESTRING     var PolicyIdentifier: CSSM_FIELD_PTR     var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, CrlIdentifier CrlIdentifier: uint32, CrlThisTime CrlThisTime: CSSM_TIMESTRING, PolicyIdentifier PolicyIdentifier: CSSM_FIELD_PTR, CallerCredentials CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR) } ``` |
| To | ``` struct cssm_tp_crlissue_input {     var CLHandle: CSSM_CL_HANDLE     var CrlIdentifier: uint32     var CrlThisTime: CSSM_TIMESTRING!     var PolicyIdentifier: UnsafeMutablePointer<cssm_field>!     var CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!     init()     init(CLHandle CLHandle: CSSM_CL_HANDLE, CrlIdentifier CrlIdentifier: uint32, CrlThisTime CrlThisTime: CSSM_TIMESTRING!, PolicyIdentifier PolicyIdentifier: UnsafeMutablePointer<cssm_field>!, CallerCredentials CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>!) } ``` |

Modified cssm_tp_crlissue_input.CallerCredentials

|  | Declaration |
| --- | --- |
| From | ``` var CallerCredentials: CSSM_ACCESS_CREDENTIALS_PTR ``` |
| To | ``` var CallerCredentials: UnsafeMutablePointer<cssm_access_credentials>! ``` |

Modified cssm_tp_crlissue_input.CrlThisTime

|  | Declaration |
| --- | --- |
| From | ``` var CrlThisTime: CSSM_TIMESTRING ``` |
| To | ``` var CrlThisTime: CSSM_TIMESTRING! ``` |

Modified cssm_tp_crlissue_input.PolicyIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var PolicyIdentifier: CSSM_FIELD_PTR ``` |
| To | ``` var PolicyIdentifier: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_crlissue_output [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_crlissue_output {     var IssueStatus: CSSM_TP_CRLISSUE_STATUS     var Crl: CSSM_ENCODED_CRL_PTR     var CrlNextTime: CSSM_TIMESTRING     init()     init(IssueStatus IssueStatus: CSSM_TP_CRLISSUE_STATUS, Crl Crl: CSSM_ENCODED_CRL_PTR, CrlNextTime CrlNextTime: CSSM_TIMESTRING) } ``` |
| To | ``` struct cssm_tp_crlissue_output {     var IssueStatus: CSSM_TP_CRLISSUE_STATUS     var Crl: UnsafeMutablePointer<cssm_encoded_crl>!     var CrlNextTime: CSSM_TIMESTRING!     init()     init(IssueStatus IssueStatus: CSSM_TP_CRLISSUE_STATUS, Crl Crl: UnsafeMutablePointer<cssm_encoded_crl>!, CrlNextTime CrlNextTime: CSSM_TIMESTRING!) } ``` |

Modified cssm_tp_crlissue_output.Crl

|  | Declaration |
| --- | --- |
| From | ``` var Crl: CSSM_ENCODED_CRL_PTR ``` |
| To | ``` var Crl: UnsafeMutablePointer<cssm_encoded_crl>! ``` |

Modified cssm_tp_crlissue_output.CrlNextTime

|  | Declaration |
| --- | --- |
| From | ``` var CrlNextTime: CSSM_TIMESTRING ``` |
| To | ``` var CrlNextTime: CSSM_TIMESTRING! ``` |

Modified cssm_tp_policyinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_policyinfo {     var NumberOfPolicyIds: uint32     var PolicyIds: CSSM_FIELD_PTR     var PolicyControl: UnsafeMutablePointer<Void>     init()     init(NumberOfPolicyIds NumberOfPolicyIds: uint32, PolicyIds PolicyIds: CSSM_FIELD_PTR, PolicyControl PolicyControl: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_tp_policyinfo {     var NumberOfPolicyIds: uint32     var PolicyIds: UnsafeMutablePointer<cssm_field>!     var PolicyControl: UnsafeMutableRawPointer!     init()     init(NumberOfPolicyIds NumberOfPolicyIds: uint32, PolicyIds PolicyIds: UnsafeMutablePointer<cssm_field>!, PolicyControl PolicyControl: UnsafeMutableRawPointer!) } ``` |

Modified cssm_tp_policyinfo.PolicyControl

|  | Declaration |
| --- | --- |
| From | ``` var PolicyControl: UnsafeMutablePointer<Void> ``` |
| To | ``` var PolicyControl: UnsafeMutableRawPointer! ``` |

Modified cssm_tp_policyinfo.PolicyIds

|  | Declaration |
| --- | --- |
| From | ``` var PolicyIds: CSSM_FIELD_PTR ``` |
| To | ``` var PolicyIds: UnsafeMutablePointer<cssm_field>! ``` |

Modified cssm_tp_request_set [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_request_set {     var NumberOfRequests: uint32     var Requests: UnsafeMutablePointer<Void>     init()     init(NumberOfRequests NumberOfRequests: uint32, Requests Requests: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_tp_request_set {     var NumberOfRequests: uint32     var Requests: UnsafeMutableRawPointer!     init()     init(NumberOfRequests NumberOfRequests: uint32, Requests Requests: UnsafeMutableRawPointer!) } ``` |

Modified cssm_tp_request_set.Requests

|  | Declaration |
| --- | --- |
| From | ``` var Requests: UnsafeMutablePointer<Void> ``` |
| To | ``` var Requests: UnsafeMutableRawPointer! ``` |

Modified [cssm_tp_result_set [struct]](https://developer.apple.com/documentation/security/cssm_tp_result_set)

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_result_set {     var NumberOfResults: uint32     var Results: UnsafeMutablePointer<Void>     init()     init(NumberOfResults NumberOfResults: uint32, Results Results: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_tp_result_set {     var NumberOfResults: uint32     var Results: UnsafeMutableRawPointer!     init()     init(NumberOfResults NumberOfResults: uint32, Results Results: UnsafeMutableRawPointer!) } ``` |

Modified cssm_tp_result_set.Results

|  | Declaration |
| --- | --- |
| From | ``` var Results: UnsafeMutablePointer<Void> ``` |
| To | ``` var Results: UnsafeMutableRawPointer! ``` |

Modified cssm_tp_verify_context [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_verify_context {     var Action: CSSM_TP_ACTION     var ActionData: CSSM_DATA     var Crls: CSSM_CRLGROUP     var Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR     init()     init(Action Action: CSSM_TP_ACTION, ActionData ActionData: CSSM_DATA, Crls Crls: CSSM_CRLGROUP, Cred Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR) } ``` |
| To | ``` struct cssm_tp_verify_context {     var Action: CSSM_TP_ACTION     var ActionData: cssm_data     var Crls: CSSM_CRLGROUP     var Cred: UnsafeMutablePointer<cssm_tp_callerauth_context>!     init()     init(Action Action: CSSM_TP_ACTION, ActionData ActionData: cssm_data, Crls Crls: CSSM_CRLGROUP, Cred Cred: UnsafeMutablePointer<cssm_tp_callerauth_context>!) } ``` |

Modified cssm_tp_verify_context.ActionData

|  | Declaration |
| --- | --- |
| From | ``` var ActionData: CSSM_DATA ``` |
| To | ``` var ActionData: cssm_data ``` |

Modified cssm_tp_verify_context.Cred

|  | Declaration |
| --- | --- |
| From | ``` var Cred: CSSM_TP_CALLERAUTH_CONTEXT_PTR ``` |
| To | ``` var Cred: UnsafeMutablePointer<cssm_tp_callerauth_context>! ``` |

Modified cssm_tp_verify_context_result [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tp_verify_context_result {     var NumberOfEvidences: uint32     var Evidence: CSSM_EVIDENCE_PTR     init()     init(NumberOfEvidences NumberOfEvidences: uint32, Evidence Evidence: CSSM_EVIDENCE_PTR) } ``` |
| To | ``` struct cssm_tp_verify_context_result {     var NumberOfEvidences: uint32     var Evidence: UnsafeMutablePointer<cssm_evidence>!     init()     init(NumberOfEvidences NumberOfEvidences: uint32, Evidence Evidence: UnsafeMutablePointer<cssm_evidence>!) } ``` |

Modified cssm_tp_verify_context_result.Evidence

|  | Declaration |
| --- | --- |
| From | ``` var Evidence: CSSM_EVIDENCE_PTR ``` |
| To | ``` var Evidence: UnsafeMutablePointer<cssm_evidence>! ``` |

Modified cssm_tuplegroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_tuplegroup {     var NumberOfTuples: uint32     var Tuples: CSSM_TUPLE_PTR     init()     init(NumberOfTuples NumberOfTuples: uint32, Tuples Tuples: CSSM_TUPLE_PTR) } ``` |
| To | ``` struct cssm_tuplegroup {     var NumberOfTuples: uint32     var Tuples: UnsafeMutablePointer<CSSM_TUPLE>!     init()     init(NumberOfTuples NumberOfTuples: uint32, Tuples Tuples: UnsafeMutablePointer<CSSM_TUPLE>!) } ``` |

Modified cssm_tuplegroup.Tuples

|  | Declaration |
| --- | --- |
| From | ``` var Tuples: CSSM_TUPLE_PTR ``` |
| To | ``` var Tuples: UnsafeMutablePointer<CSSM_TUPLE>! ``` |

Modified cssm_upcalls [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_upcalls {     var malloc_func: CSSM_UPCALLS_MALLOC!     var free_func: CSSM_UPCALLS_FREE!     var realloc_func: CSSM_UPCALLS_REALLOC!     var calloc_func: CSSM_UPCALLS_CALLOC!     var CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)!     var GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!     init()     init(malloc_func malloc_func: CSSM_UPCALLS_MALLOC!, free_func free_func: CSSM_UPCALLS_FREE!, realloc_func realloc_func: CSSM_UPCALLS_REALLOC!, calloc_func calloc_func: CSSM_UPCALLS_CALLOC!, CcToHandle_func CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)!, GetModuleInfo_func GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)!) } ``` |
| To | ``` struct cssm_upcalls {     var malloc_func: ((CSSM_HANDLE, Int) -> UnsafeMutableRawPointer?)!     var free_func: ((CSSM_HANDLE, UnsafeMutableRawPointer?) -> Swift.Void)!     var realloc_func: ((CSSM_HANDLE, UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)!     var calloc_func: ((CSSM_HANDLE, Int, Int) -> UnsafeMutableRawPointer?)!     var CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR?) -> CSSM_RETURN)!     var GetModuleInfo_func: ((CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<cssm_version>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_SERVICE_TYPE>?, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>?, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>?, CSSM_API_MEMORY_FUNCS_PTR?, UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)!     init()     init(malloc_func malloc_func: (@escaping (CSSM_HANDLE, Int) -> UnsafeMutableRawPointer?)!, free_func free_func: (@escaping (CSSM_HANDLE, UnsafeMutableRawPointer?) -> Swift.Void)!, realloc_func realloc_func: (@escaping (CSSM_HANDLE, UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)!, calloc_func calloc_func: (@escaping (CSSM_HANDLE, Int, Int) -> UnsafeMutableRawPointer?)!, CcToHandle_func CcToHandle_func: (@escaping (CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR?) -> CSSM_RETURN)!, GetModuleInfo_func GetModuleInfo_func: (@escaping (CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<cssm_version>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_SERVICE_TYPE>?, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>?, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>?, CSSM_API_MEMORY_FUNCS_PTR?, UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)!) } ``` |

Modified cssm_upcalls.calloc_func

|  | Declaration |
| --- | --- |
| From | ``` var calloc_func: CSSM_UPCALLS_CALLOC! ``` |
| To | ``` var calloc_func: ((CSSM_HANDLE, Int, Int) -> UnsafeMutableRawPointer?)! ``` |

Modified cssm_upcalls.CcToHandle_func

|  | Declaration |
| --- | --- |
| From | ``` var CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var CcToHandle_func: ((CSSM_CC_HANDLE, CSSM_MODULE_HANDLE_PTR?) -> CSSM_RETURN)! ``` |

Modified cssm_upcalls.free_func

|  | Declaration |
| --- | --- |
| From | ``` var free_func: CSSM_UPCALLS_FREE! ``` |
| To | ``` var free_func: ((CSSM_HANDLE, UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified cssm_upcalls.GetModuleInfo_func

|  | Declaration |
| --- | --- |
| From | ``` var GetModuleInfo_func: ((CSSM_MODULE_HANDLE, CSSM_GUID_PTR, CSSM_VERSION_PTR, UnsafeMutablePointer<uint32>, UnsafeMutablePointer<CSSM_SERVICE_TYPE>, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>, CSSM_API_MEMORY_FUNCS_PTR, CSSM_FUNC_NAME_ADDR_PTR, uint32) -> CSSM_RETURN)! ``` |
| To | ``` var GetModuleInfo_func: ((CSSM_MODULE_HANDLE, UnsafeMutablePointer<cssm_guid>?, UnsafeMutablePointer<cssm_version>?, UnsafeMutablePointer<uint32>?, UnsafeMutablePointer<CSSM_SERVICE_TYPE>?, UnsafeMutablePointer<CSSM_ATTACH_FLAGS>?, UnsafeMutablePointer<CSSM_KEY_HIERARCHY>?, CSSM_API_MEMORY_FUNCS_PTR?, UnsafeMutablePointer<cssm_func_name_addr>?, uint32) -> CSSM_RETURN)! ``` |

Modified cssm_upcalls.malloc_func

|  | Declaration |
| --- | --- |
| From | ``` var malloc_func: CSSM_UPCALLS_MALLOC! ``` |
| To | ``` var malloc_func: ((CSSM_HANDLE, Int) -> UnsafeMutableRawPointer?)! ``` |

Modified cssm_upcalls.realloc_func

|  | Declaration |
| --- | --- |
| From | ``` var realloc_func: CSSM_UPCALLS_REALLOC! ``` |
| To | ``` var realloc_func: ((CSSM_HANDLE, UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)! ``` |

Modified cssm_x509_algorithm_identifier [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_algorithm_identifier {     var algorithm: CSSM_OID     var parameters: CSSM_DATA     init()     init(algorithm algorithm: CSSM_OID, parameters parameters: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_algorithm_identifier {     var algorithm: CSSM_OID     var parameters: cssm_data     init()     init(algorithm algorithm: CSSM_OID, parameters parameters: cssm_data) } ``` |

Modified cssm_x509_algorithm_identifier.init(algorithm: CSSM_OID, parameters: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(algorithm algorithm: CSSM_OID, parameters parameters: CSSM_DATA) ``` |
| To | ``` init(algorithm algorithm: CSSM_OID, parameters parameters: cssm_data) ``` |

Modified cssm_x509_algorithm_identifier.parameters

|  | Declaration |
| --- | --- |
| From | ``` var parameters: CSSM_DATA ``` |
| To | ``` var parameters: cssm_data ``` |

Modified cssm_x509_extension [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_extension {     var extnId: CSSM_OID     var critical: CSSM_BOOL     var format: CSSM_X509EXT_DATA_FORMAT     var value: cssm_x509ext_value     var BERvalue: CSSM_DATA     init()     init(extnId extnId: CSSM_OID, critical critical: CSSM_BOOL, format format: CSSM_X509EXT_DATA_FORMAT, value value: cssm_x509ext_value, BERvalue BERvalue: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_extension {     var extnId: CSSM_OID     var critical: CSSM_BOOL     var format: CSSM_X509EXT_DATA_FORMAT     var value: cssm_x509ext_value     var BERvalue: cssm_data     init()     init(extnId extnId: CSSM_OID, critical critical: CSSM_BOOL, format format: CSSM_X509EXT_DATA_FORMAT, value value: cssm_x509ext_value, BERvalue BERvalue: cssm_data) } ``` |

Modified cssm_x509_extension.BERvalue

|  | Declaration |
| --- | --- |
| From | ``` var BERvalue: CSSM_DATA ``` |
| To | ``` var BERvalue: cssm_data ``` |

Modified cssm_x509_extension.init(extnId: CSSM_OID, critical: CSSM_BOOL, format: CSSM_X509EXT_DATA_FORMAT, value: cssm_x509ext_value, BERvalue: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(extnId extnId: CSSM_OID, critical critical: CSSM_BOOL, format format: CSSM_X509EXT_DATA_FORMAT, value value: cssm_x509ext_value, BERvalue BERvalue: CSSM_DATA) ``` |
| To | ``` init(extnId extnId: CSSM_OID, critical critical: CSSM_BOOL, format format: CSSM_X509EXT_DATA_FORMAT, value value: cssm_x509ext_value, BERvalue BERvalue: cssm_data) ``` |

Modified cssm_x509_extensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_extensions {     var numberOfExtensions: uint32     var extensions: CSSM_X509_EXTENSION_PTR     init()     init(numberOfExtensions numberOfExtensions: uint32, extensions extensions: CSSM_X509_EXTENSION_PTR) } ``` |
| To | ``` struct cssm_x509_extensions {     var numberOfExtensions: uint32     var extensions: UnsafeMutablePointer<cssm_x509_extension>!     init()     init(numberOfExtensions numberOfExtensions: uint32, extensions extensions: UnsafeMutablePointer<cssm_x509_extension>!) } ``` |

Modified cssm_x509_extensions.extensions

|  | Declaration |
| --- | --- |
| From | ``` var extensions: CSSM_X509_EXTENSION_PTR ``` |
| To | ``` var extensions: UnsafeMutablePointer<cssm_x509_extension>! ``` |

Modified cssm_x509_extensionTagAndValue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_extensionTagAndValue {     var type: CSSM_BER_TAG     var value: CSSM_DATA     init()     init(type type: CSSM_BER_TAG, value value: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_extensionTagAndValue {     var type: CSSM_BER_TAG     var value: cssm_data     init()     init(type type: CSSM_BER_TAG, value value: cssm_data) } ``` |

Modified cssm_x509_extensionTagAndValue.init(type: CSSM_BER_TAG, value: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: CSSM_BER_TAG, value value: CSSM_DATA) ``` |
| To | ``` init(type type: CSSM_BER_TAG, value value: cssm_data) ``` |

Modified cssm_x509_extensionTagAndValue.value

|  | Declaration |
| --- | --- |
| From | ``` var value: CSSM_DATA ``` |
| To | ``` var value: cssm_data ``` |

Modified cssm_x509_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_name {     var numberOfRDNs: uint32     var RelativeDistinguishedName: CSSM_X509_RDN_PTR     init()     init(numberOfRDNs numberOfRDNs: uint32, RelativeDistinguishedName RelativeDistinguishedName: CSSM_X509_RDN_PTR) } ``` |
| To | ``` struct cssm_x509_name {     var numberOfRDNs: uint32     var RelativeDistinguishedName: UnsafeMutablePointer<cssm_x509_rdn>!     init()     init(numberOfRDNs numberOfRDNs: uint32, RelativeDistinguishedName RelativeDistinguishedName: UnsafeMutablePointer<cssm_x509_rdn>!) } ``` |

Modified cssm_x509_name.RelativeDistinguishedName

|  | Declaration |
| --- | --- |
| From | ``` var RelativeDistinguishedName: CSSM_X509_RDN_PTR ``` |
| To | ``` var RelativeDistinguishedName: UnsafeMutablePointer<cssm_x509_rdn>! ``` |

Modified cssm_x509_rdn [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_rdn {     var numberOfPairs: uint32     var AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR     init()     init(numberOfPairs numberOfPairs: uint32, AttributeTypeAndValue AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR) } ``` |
| To | ``` struct cssm_x509_rdn {     var numberOfPairs: uint32     var AttributeTypeAndValue: UnsafeMutablePointer<cssm_x509_type_value_pair>!     init()     init(numberOfPairs numberOfPairs: uint32, AttributeTypeAndValue AttributeTypeAndValue: UnsafeMutablePointer<cssm_x509_type_value_pair>!) } ``` |

Modified cssm_x509_rdn.AttributeTypeAndValue

|  | Declaration |
| --- | --- |
| From | ``` var AttributeTypeAndValue: CSSM_X509_TYPE_VALUE_PAIR_PTR ``` |
| To | ``` var AttributeTypeAndValue: UnsafeMutablePointer<cssm_x509_type_value_pair>! ``` |

Modified cssm_x509_revoked_cert_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_revoked_cert_entry {     var certificateSerialNumber: CSSM_DATA     var revocationDate: CSSM_X509_TIME     var extensions: CSSM_X509_EXTENSIONS     init()     init(certificateSerialNumber certificateSerialNumber: CSSM_DATA, revocationDate revocationDate: CSSM_X509_TIME, extensions extensions: CSSM_X509_EXTENSIONS) } ``` |
| To | ``` struct cssm_x509_revoked_cert_entry {     var certificateSerialNumber: cssm_data     var revocationDate: cssm_x509_time     var extensions: cssm_x509_extensions     init()     init(certificateSerialNumber certificateSerialNumber: cssm_data, revocationDate revocationDate: cssm_x509_time, extensions extensions: cssm_x509_extensions) } ``` |

Modified cssm_x509_revoked_cert_entry.certificateSerialNumber

|  | Declaration |
| --- | --- |
| From | ``` var certificateSerialNumber: CSSM_DATA ``` |
| To | ``` var certificateSerialNumber: cssm_data ``` |

Modified cssm_x509_revoked_cert_entry.extensions

|  | Declaration |
| --- | --- |
| From | ``` var extensions: CSSM_X509_EXTENSIONS ``` |
| To | ``` var extensions: cssm_x509_extensions ``` |

Modified cssm_x509_revoked_cert_entry.init(certificateSerialNumber: cssm_data, revocationDate: cssm_x509_time, extensions: cssm_x509_extensions)

|  | Declaration |
| --- | --- |
| From | ``` init(certificateSerialNumber certificateSerialNumber: CSSM_DATA, revocationDate revocationDate: CSSM_X509_TIME, extensions extensions: CSSM_X509_EXTENSIONS) ``` |
| To | ``` init(certificateSerialNumber certificateSerialNumber: cssm_data, revocationDate revocationDate: cssm_x509_time, extensions extensions: cssm_x509_extensions) ``` |

Modified cssm_x509_revoked_cert_entry.revocationDate

|  | Declaration |
| --- | --- |
| From | ``` var revocationDate: CSSM_X509_TIME ``` |
| To | ``` var revocationDate: cssm_x509_time ``` |

Modified cssm_x509_revoked_cert_list [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_revoked_cert_list {     var numberOfRevokedCertEntries: uint32     var revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR     init()     init(numberOfRevokedCertEntries numberOfRevokedCertEntries: uint32, revokedCertEntry revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR) } ``` |
| To | ``` struct cssm_x509_revoked_cert_list {     var numberOfRevokedCertEntries: uint32     var revokedCertEntry: UnsafeMutablePointer<cssm_x509_revoked_cert_entry>!     init()     init(numberOfRevokedCertEntries numberOfRevokedCertEntries: uint32, revokedCertEntry revokedCertEntry: UnsafeMutablePointer<cssm_x509_revoked_cert_entry>!) } ``` |

Modified cssm_x509_revoked_cert_list.revokedCertEntry

|  | Declaration |
| --- | --- |
| From | ``` var revokedCertEntry: CSSM_X509_REVOKED_CERT_ENTRY_PTR ``` |
| To | ``` var revokedCertEntry: UnsafeMutablePointer<cssm_x509_revoked_cert_entry>! ``` |

Modified cssm_x509_signature [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_signature {     var algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER     var encrypted: CSSM_DATA     init()     init(algorithmIdentifier algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER, encrypted encrypted: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_signature {     var algorithmIdentifier: cssm_x509_algorithm_identifier     var encrypted: cssm_data     init()     init(algorithmIdentifier algorithmIdentifier: cssm_x509_algorithm_identifier, encrypted encrypted: cssm_data) } ``` |

Modified cssm_x509_signature.algorithmIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER ``` |
| To | ``` var algorithmIdentifier: cssm_x509_algorithm_identifier ``` |

Modified cssm_x509_signature.encrypted

|  | Declaration |
| --- | --- |
| From | ``` var encrypted: CSSM_DATA ``` |
| To | ``` var encrypted: cssm_data ``` |

Modified cssm_x509_signature.init(algorithmIdentifier: cssm_x509_algorithm_identifier, encrypted: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(algorithmIdentifier algorithmIdentifier: CSSM_X509_ALGORITHM_IDENTIFIER, encrypted encrypted: CSSM_DATA) ``` |
| To | ``` init(algorithmIdentifier algorithmIdentifier: cssm_x509_algorithm_identifier, encrypted encrypted: cssm_data) ``` |

Modified cssm_x509_signed_certificate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_signed_certificate {     var certificate: CSSM_X509_TBS_CERTIFICATE     var signature: CSSM_X509_SIGNATURE     init()     init(certificate certificate: CSSM_X509_TBS_CERTIFICATE, signature signature: CSSM_X509_SIGNATURE) } ``` |
| To | ``` struct cssm_x509_signed_certificate {     var certificate: cssm_x509_tbs_certificate     var signature: cssm_x509_signature     init()     init(certificate certificate: cssm_x509_tbs_certificate, signature signature: cssm_x509_signature) } ``` |

Modified cssm_x509_signed_certificate.certificate

|  | Declaration |
| --- | --- |
| From | ``` var certificate: CSSM_X509_TBS_CERTIFICATE ``` |
| To | ``` var certificate: cssm_x509_tbs_certificate ``` |

Modified cssm_x509_signed_certificate.init(certificate: cssm_x509_tbs_certificate, signature: cssm_x509_signature)

|  | Declaration |
| --- | --- |
| From | ``` init(certificate certificate: CSSM_X509_TBS_CERTIFICATE, signature signature: CSSM_X509_SIGNATURE) ``` |
| To | ``` init(certificate certificate: cssm_x509_tbs_certificate, signature signature: cssm_x509_signature) ``` |

Modified cssm_x509_signed_certificate.signature

|  | Declaration |
| --- | --- |
| From | ``` var signature: CSSM_X509_SIGNATURE ``` |
| To | ``` var signature: cssm_x509_signature ``` |

Modified cssm_x509_signed_crl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_signed_crl {     var tbsCertList: CSSM_X509_TBS_CERTLIST     var signature: CSSM_X509_SIGNATURE     init()     init(tbsCertList tbsCertList: CSSM_X509_TBS_CERTLIST, signature signature: CSSM_X509_SIGNATURE) } ``` |
| To | ``` struct cssm_x509_signed_crl {     var tbsCertList: cssm_x509_tbs_certlist     var signature: cssm_x509_signature     init()     init(tbsCertList tbsCertList: cssm_x509_tbs_certlist, signature signature: cssm_x509_signature) } ``` |

Modified cssm_x509_signed_crl.init(tbsCertList: cssm_x509_tbs_certlist, signature: cssm_x509_signature)

|  | Declaration |
| --- | --- |
| From | ``` init(tbsCertList tbsCertList: CSSM_X509_TBS_CERTLIST, signature signature: CSSM_X509_SIGNATURE) ``` |
| To | ``` init(tbsCertList tbsCertList: cssm_x509_tbs_certlist, signature signature: cssm_x509_signature) ``` |

Modified cssm_x509_signed_crl.signature

|  | Declaration |
| --- | --- |
| From | ``` var signature: CSSM_X509_SIGNATURE ``` |
| To | ``` var signature: cssm_x509_signature ``` |

Modified cssm_x509_signed_crl.tbsCertList

|  | Declaration |
| --- | --- |
| From | ``` var tbsCertList: CSSM_X509_TBS_CERTLIST ``` |
| To | ``` var tbsCertList: cssm_x509_tbs_certlist ``` |

Modified cssm_x509_subject_public_key_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_subject_public_key_info {     var algorithm: CSSM_X509_ALGORITHM_IDENTIFIER     var subjectPublicKey: CSSM_DATA     init()     init(algorithm algorithm: CSSM_X509_ALGORITHM_IDENTIFIER, subjectPublicKey subjectPublicKey: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_subject_public_key_info {     var algorithm: cssm_x509_algorithm_identifier     var subjectPublicKey: cssm_data     init()     init(algorithm algorithm: cssm_x509_algorithm_identifier, subjectPublicKey subjectPublicKey: cssm_data) } ``` |

Modified cssm_x509_subject_public_key_info.algorithm

|  | Declaration |
| --- | --- |
| From | ``` var algorithm: CSSM_X509_ALGORITHM_IDENTIFIER ``` |
| To | ``` var algorithm: cssm_x509_algorithm_identifier ``` |

Modified cssm_x509_subject_public_key_info.init(algorithm: cssm_x509_algorithm_identifier, subjectPublicKey: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(algorithm algorithm: CSSM_X509_ALGORITHM_IDENTIFIER, subjectPublicKey subjectPublicKey: CSSM_DATA) ``` |
| To | ``` init(algorithm algorithm: cssm_x509_algorithm_identifier, subjectPublicKey subjectPublicKey: cssm_data) ``` |

Modified cssm_x509_subject_public_key_info.subjectPublicKey

|  | Declaration |
| --- | --- |
| From | ``` var subjectPublicKey: CSSM_DATA ``` |
| To | ``` var subjectPublicKey: cssm_data ``` |

Modified cssm_x509_tbs_certificate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_tbs_certificate {     var version: CSSM_DATA     var serialNumber: CSSM_DATA     var signature: CSSM_X509_ALGORITHM_IDENTIFIER     var issuer: CSSM_X509_NAME     var validity: CSSM_X509_VALIDITY     var subject: CSSM_X509_NAME     var subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO     var issuerUniqueIdentifier: CSSM_DATA     var subjectUniqueIdentifier: CSSM_DATA     var extensions: CSSM_X509_EXTENSIONS     init()     init(version version: CSSM_DATA, serialNumber serialNumber: CSSM_DATA, signature signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer issuer: CSSM_X509_NAME, validity validity: CSSM_X509_VALIDITY, subject subject: CSSM_X509_NAME, subjectPublicKeyInfo subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO, issuerUniqueIdentifier issuerUniqueIdentifier: CSSM_DATA, subjectUniqueIdentifier subjectUniqueIdentifier: CSSM_DATA, extensions extensions: CSSM_X509_EXTENSIONS) } ``` |
| To | ``` struct cssm_x509_tbs_certificate {     var version: cssm_data     var serialNumber: cssm_data     var signature: cssm_x509_algorithm_identifier     var issuer: cssm_x509_name     var validity: x509_validity     var subject: cssm_x509_name     var subjectPublicKeyInfo: cssm_x509_subject_public_key_info     var issuerUniqueIdentifier: cssm_data     var subjectUniqueIdentifier: cssm_data     var extensions: cssm_x509_extensions     init()     init(version version: cssm_data, serialNumber serialNumber: cssm_data, signature signature: cssm_x509_algorithm_identifier, issuer issuer: cssm_x509_name, validity validity: x509_validity, subject subject: cssm_x509_name, subjectPublicKeyInfo subjectPublicKeyInfo: cssm_x509_subject_public_key_info, issuerUniqueIdentifier issuerUniqueIdentifier: cssm_data, subjectUniqueIdentifier subjectUniqueIdentifier: cssm_data, extensions extensions: cssm_x509_extensions) } ``` |

Modified cssm_x509_tbs_certificate.extensions

|  | Declaration |
| --- | --- |
| From | ``` var extensions: CSSM_X509_EXTENSIONS ``` |
| To | ``` var extensions: cssm_x509_extensions ``` |

Modified cssm_x509_tbs_certificate.init(version: cssm_data, serialNumber: cssm_data, signature: cssm_x509_algorithm_identifier, issuer: cssm_x509_name, validity: x509_validity, subject: cssm_x509_name, subjectPublicKeyInfo: cssm_x509_subject_public_key_info, issuerUniqueIdentifier: cssm_data, subjectUniqueIdentifier: cssm_data, extensions: cssm_x509_extensions)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: CSSM_DATA, serialNumber serialNumber: CSSM_DATA, signature signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer issuer: CSSM_X509_NAME, validity validity: CSSM_X509_VALIDITY, subject subject: CSSM_X509_NAME, subjectPublicKeyInfo subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO, issuerUniqueIdentifier issuerUniqueIdentifier: CSSM_DATA, subjectUniqueIdentifier subjectUniqueIdentifier: CSSM_DATA, extensions extensions: CSSM_X509_EXTENSIONS) ``` |
| To | ``` init(version version: cssm_data, serialNumber serialNumber: cssm_data, signature signature: cssm_x509_algorithm_identifier, issuer issuer: cssm_x509_name, validity validity: x509_validity, subject subject: cssm_x509_name, subjectPublicKeyInfo subjectPublicKeyInfo: cssm_x509_subject_public_key_info, issuerUniqueIdentifier issuerUniqueIdentifier: cssm_data, subjectUniqueIdentifier subjectUniqueIdentifier: cssm_data, extensions extensions: cssm_x509_extensions) ``` |

Modified cssm_x509_tbs_certificate.issuer

|  | Declaration |
| --- | --- |
| From | ``` var issuer: CSSM_X509_NAME ``` |
| To | ``` var issuer: cssm_x509_name ``` |

Modified cssm_x509_tbs_certificate.issuerUniqueIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var issuerUniqueIdentifier: CSSM_DATA ``` |
| To | ``` var issuerUniqueIdentifier: cssm_data ``` |

Modified cssm_x509_tbs_certificate.serialNumber

|  | Declaration |
| --- | --- |
| From | ``` var serialNumber: CSSM_DATA ``` |
| To | ``` var serialNumber: cssm_data ``` |

Modified cssm_x509_tbs_certificate.signature

|  | Declaration |
| --- | --- |
| From | ``` var signature: CSSM_X509_ALGORITHM_IDENTIFIER ``` |
| To | ``` var signature: cssm_x509_algorithm_identifier ``` |

Modified cssm_x509_tbs_certificate.subject

|  | Declaration |
| --- | --- |
| From | ``` var subject: CSSM_X509_NAME ``` |
| To | ``` var subject: cssm_x509_name ``` |

Modified cssm_x509_tbs_certificate.subjectPublicKeyInfo

|  | Declaration |
| --- | --- |
| From | ``` var subjectPublicKeyInfo: CSSM_X509_SUBJECT_PUBLIC_KEY_INFO ``` |
| To | ``` var subjectPublicKeyInfo: cssm_x509_subject_public_key_info ``` |

Modified cssm_x509_tbs_certificate.subjectUniqueIdentifier

|  | Declaration |
| --- | --- |
| From | ``` var subjectUniqueIdentifier: CSSM_DATA ``` |
| To | ``` var subjectUniqueIdentifier: cssm_data ``` |

Modified cssm_x509_tbs_certificate.validity

|  | Declaration |
| --- | --- |
| From | ``` var validity: CSSM_X509_VALIDITY ``` |
| To | ``` var validity: x509_validity ``` |

Modified cssm_x509_tbs_certificate.version

|  | Declaration |
| --- | --- |
| From | ``` var version: CSSM_DATA ``` |
| To | ``` var version: cssm_data ``` |

Modified cssm_x509_tbs_certlist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_tbs_certlist {     var version: CSSM_DATA     var signature: CSSM_X509_ALGORITHM_IDENTIFIER     var issuer: CSSM_X509_NAME     var thisUpdate: CSSM_X509_TIME     var nextUpdate: CSSM_X509_TIME     var revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR     var extensions: CSSM_X509_EXTENSIONS     init()     init(version version: CSSM_DATA, signature signature: CSSM_X509_ALGORITHM_IDENTIFIER, issuer issuer: CSSM_X509_NAME, thisUpdate thisUpdate: CSSM_X509_TIME, nextUpdate nextUpdate: CSSM_X509_TIME, revokedCertificates revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR, extensions extensions: CSSM_X509_EXTENSIONS) } ``` |
| To | ``` struct cssm_x509_tbs_certlist {     var version: cssm_data     var signature: cssm_x509_algorithm_identifier     var issuer: cssm_x509_name     var thisUpdate: cssm_x509_time     var nextUpdate: cssm_x509_time     var revokedCertificates: UnsafeMutablePointer<cssm_x509_revoked_cert_list>!     var extensions: cssm_x509_extensions     init()     init(version version: cssm_data, signature signature: cssm_x509_algorithm_identifier, issuer issuer: cssm_x509_name, thisUpdate thisUpdate: cssm_x509_time, nextUpdate nextUpdate: cssm_x509_time, revokedCertificates revokedCertificates: UnsafeMutablePointer<cssm_x509_revoked_cert_list>!, extensions extensions: cssm_x509_extensions) } ``` |

Modified cssm_x509_tbs_certlist.extensions

|  | Declaration |
| --- | --- |
| From | ``` var extensions: CSSM_X509_EXTENSIONS ``` |
| To | ``` var extensions: cssm_x509_extensions ``` |

Modified cssm_x509_tbs_certlist.issuer

|  | Declaration |
| --- | --- |
| From | ``` var issuer: CSSM_X509_NAME ``` |
| To | ``` var issuer: cssm_x509_name ``` |

Modified cssm_x509_tbs_certlist.nextUpdate

|  | Declaration |
| --- | --- |
| From | ``` var nextUpdate: CSSM_X509_TIME ``` |
| To | ``` var nextUpdate: cssm_x509_time ``` |

Modified cssm_x509_tbs_certlist.revokedCertificates

|  | Declaration |
| --- | --- |
| From | ``` var revokedCertificates: CSSM_X509_REVOKED_CERT_LIST_PTR ``` |
| To | ``` var revokedCertificates: UnsafeMutablePointer<cssm_x509_revoked_cert_list>! ``` |

Modified cssm_x509_tbs_certlist.signature

|  | Declaration |
| --- | --- |
| From | ``` var signature: CSSM_X509_ALGORITHM_IDENTIFIER ``` |
| To | ``` var signature: cssm_x509_algorithm_identifier ``` |

Modified cssm_x509_tbs_certlist.thisUpdate

|  | Declaration |
| --- | --- |
| From | ``` var thisUpdate: CSSM_X509_TIME ``` |
| To | ``` var thisUpdate: cssm_x509_time ``` |

Modified cssm_x509_tbs_certlist.version

|  | Declaration |
| --- | --- |
| From | ``` var version: CSSM_DATA ``` |
| To | ``` var version: cssm_data ``` |

Modified cssm_x509_time [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_time {     var timeType: CSSM_BER_TAG     var time: CSSM_DATA     init()     init(timeType timeType: CSSM_BER_TAG, time time: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_time {     var timeType: CSSM_BER_TAG     var time: cssm_data     init()     init(timeType timeType: CSSM_BER_TAG, time time: cssm_data) } ``` |

Modified cssm_x509_time.init(timeType: CSSM_BER_TAG, time: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(timeType timeType: CSSM_BER_TAG, time time: CSSM_DATA) ``` |
| To | ``` init(timeType timeType: CSSM_BER_TAG, time time: cssm_data) ``` |

Modified cssm_x509_time.time

|  | Declaration |
| --- | --- |
| From | ``` var time: CSSM_DATA ``` |
| To | ``` var time: cssm_data ``` |

Modified cssm_x509_type_value_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509_type_value_pair {     var type: CSSM_OID     var valueType: CSSM_BER_TAG     var value: CSSM_DATA     init()     init(type type: CSSM_OID, valueType valueType: CSSM_BER_TAG, value value: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509_type_value_pair {     var type: CSSM_OID     var valueType: CSSM_BER_TAG     var value: cssm_data     init()     init(type type: CSSM_OID, valueType valueType: CSSM_BER_TAG, value value: cssm_data) } ``` |

Modified cssm_x509_type_value_pair.init(type: CSSM_OID, valueType: CSSM_BER_TAG, value: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: CSSM_OID, valueType valueType: CSSM_BER_TAG, value value: CSSM_DATA) ``` |
| To | ``` init(type type: CSSM_OID, valueType valueType: CSSM_BER_TAG, value value: cssm_data) ``` |

Modified cssm_x509_type_value_pair.value

|  | Declaration |
| --- | --- |
| From | ``` var value: CSSM_DATA ``` |
| To | ``` var value: cssm_data ``` |

Modified cssm_x509ext_pair [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_pair {     var tagAndValue: CSSM_X509EXT_TAGandVALUE     var parsedValue: UnsafeMutablePointer<Void>     init()     init(tagAndValue tagAndValue: CSSM_X509EXT_TAGandVALUE, parsedValue parsedValue: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct cssm_x509ext_pair {     var tagAndValue: cssm_x509_extensionTagAndValue     var parsedValue: UnsafeMutableRawPointer!     init()     init(tagAndValue tagAndValue: cssm_x509_extensionTagAndValue, parsedValue parsedValue: UnsafeMutableRawPointer!) } ``` |

Modified cssm_x509ext_pair.parsedValue

|  | Declaration |
| --- | --- |
| From | ``` var parsedValue: UnsafeMutablePointer<Void> ``` |
| To | ``` var parsedValue: UnsafeMutableRawPointer! ``` |

Modified cssm_x509ext_pair.tagAndValue

|  | Declaration |
| --- | --- |
| From | ``` var tagAndValue: CSSM_X509EXT_TAGandVALUE ``` |
| To | ``` var tagAndValue: cssm_x509_extensionTagAndValue ``` |

Modified cssm_x509ext_policyInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_policyInfo {     var policyIdentifier: CSSM_OID     var policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS     init()     init(policyIdentifier policyIdentifier: CSSM_OID, policyQualifiers policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS) } ``` |
| To | ``` struct cssm_x509ext_policyInfo {     var policyIdentifier: CSSM_OID     var policyQualifiers: cssm_x509ext_policyQualifiers     init()     init(policyIdentifier policyIdentifier: CSSM_OID, policyQualifiers policyQualifiers: cssm_x509ext_policyQualifiers) } ``` |

Modified cssm_x509ext_policyInfo.init(policyIdentifier: CSSM_OID, policyQualifiers: cssm_x509ext_policyQualifiers)

|  | Declaration |
| --- | --- |
| From | ``` init(policyIdentifier policyIdentifier: CSSM_OID, policyQualifiers policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS) ``` |
| To | ``` init(policyIdentifier policyIdentifier: CSSM_OID, policyQualifiers policyQualifiers: cssm_x509ext_policyQualifiers) ``` |

Modified cssm_x509ext_policyInfo.policyQualifiers

|  | Declaration |
| --- | --- |
| From | ``` var policyQualifiers: CSSM_X509EXT_POLICYQUALIFIERS ``` |
| To | ``` var policyQualifiers: cssm_x509ext_policyQualifiers ``` |

Modified cssm_x509ext_policyQualifierInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_policyQualifierInfo {     var policyQualifierId: CSSM_OID     var value: CSSM_DATA     init()     init(policyQualifierId policyQualifierId: CSSM_OID, value value: CSSM_DATA) } ``` |
| To | ``` struct cssm_x509ext_policyQualifierInfo {     var policyQualifierId: CSSM_OID     var value: cssm_data     init()     init(policyQualifierId policyQualifierId: CSSM_OID, value value: cssm_data) } ``` |

Modified cssm_x509ext_policyQualifierInfo.init(policyQualifierId: CSSM_OID, value: cssm_data)

|  | Declaration |
| --- | --- |
| From | ``` init(policyQualifierId policyQualifierId: CSSM_OID, value value: CSSM_DATA) ``` |
| To | ``` init(policyQualifierId policyQualifierId: CSSM_OID, value value: cssm_data) ``` |

Modified cssm_x509ext_policyQualifierInfo.value

|  | Declaration |
| --- | --- |
| From | ``` var value: CSSM_DATA ``` |
| To | ``` var value: cssm_data ``` |

Modified cssm_x509ext_policyQualifiers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_policyQualifiers {     var numberOfPolicyQualifiers: uint32     var policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO>     init()     init(numberOfPolicyQualifiers numberOfPolicyQualifiers: uint32, policyQualifier policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO>) } ``` |
| To | ``` struct cssm_x509ext_policyQualifiers {     var numberOfPolicyQualifiers: uint32     var policyQualifier: UnsafeMutablePointer<cssm_x509ext_policyQualifierInfo>!     init()     init(numberOfPolicyQualifiers numberOfPolicyQualifiers: uint32, policyQualifier policyQualifier: UnsafeMutablePointer<cssm_x509ext_policyQualifierInfo>!) } ``` |

Modified cssm_x509ext_policyQualifiers.policyQualifier

|  | Declaration |
| --- | --- |
| From | ``` var policyQualifier: UnsafeMutablePointer<CSSM_X509EXT_POLICYQUALIFIERINFO> ``` |
| To | ``` var policyQualifier: UnsafeMutablePointer<cssm_x509ext_policyQualifierInfo>! ``` |

Modified cssm_x509ext_value [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_x509ext_value {     var tagAndValue: UnsafeMutablePointer<CSSM_X509EXT_TAGandVALUE>     var parsedValue: UnsafeMutablePointer<Void>     var valuePair: UnsafeMutablePointer<CSSM_X509EXT_PAIR>     init(tagAndValue tagAndValue: UnsafeMutablePointer<CSSM_X509EXT_TAGandVALUE>)     init(parsedValue parsedValue: UnsafeMutablePointer<Void>)     init(valuePair valuePair: UnsafeMutablePointer<CSSM_X509EXT_PAIR>)     init() } ``` |
| To | ``` struct cssm_x509ext_value {     var tagAndValue: UnsafeMutablePointer<cssm_x509_extensionTagAndValue>!     var parsedValue: UnsafeMutableRawPointer!     var valuePair: UnsafeMutablePointer<cssm_x509ext_pair>!     init(tagAndValue tagAndValue: UnsafeMutablePointer<cssm_x509_extensionTagAndValue>!)     init(parsedValue parsedValue: UnsafeMutableRawPointer!)     init(valuePair valuePair: UnsafeMutablePointer<cssm_x509ext_pair>!)     init() } ``` |

Modified cssm_x509ext_value.parsedValue

|  | Declaration |
| --- | --- |
| From | ``` var parsedValue: UnsafeMutablePointer<Void> ``` |
| To | ``` var parsedValue: UnsafeMutableRawPointer! ``` |

Modified cssm_x509ext_value.tagAndValue

|  | Declaration |
| --- | --- |
| From | ``` var tagAndValue: UnsafeMutablePointer<CSSM_X509EXT_TAGandVALUE> ``` |
| To | ``` var tagAndValue: UnsafeMutablePointer<cssm_x509_extensionTagAndValue>! ``` |

Modified cssm_x509ext_value.valuePair

|  | Declaration |
| --- | --- |
| From | ``` var valuePair: UnsafeMutablePointer<CSSM_X509EXT_PAIR> ``` |
| To | ``` var valuePair: UnsafeMutablePointer<cssm_x509ext_pair>! ``` |

Modified [DERItem [struct]](https://developer.apple.com/documentation/security/deritem)

|  | Declaration |
| --- | --- |
| From | ``` struct DERItem {     var data: UnsafeMutablePointer<DERByte>     var length: DERSize     init()     init(data data: UnsafeMutablePointer<DERByte>, length length: DERSize) } ``` |
| To | ``` struct DERItem {     var data: UnsafeMutablePointer<DERByte>!     var length: DERSize     init()     init(data data: UnsafeMutablePointer<DERByte>!, length length: DERSize) } ``` |

Modified [DERItem.data](https://developer.apple.com/documentation/security/deritem/1396970-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<DERByte> ``` |
| To | ``` var data: UnsafeMutablePointer<DERByte>! ``` |

Modified mds_funcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mds_funcs {     var DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!     var DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!     var GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!     var GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!     var FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!     var DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!     var DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!     var DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!     var DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!     var FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!     var CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!     var DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!     init()     init(DbOpen DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)!, DbClose DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!, GetDbNames GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)!, GetDbNameFromHandle GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)!, FreeNameList FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)!, DataInsert DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataDelete DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)!, DataModify DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataGetNext DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)!, DataAbortQuery DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)!, FreeUniqueRecord FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)!, CreateRelation CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)!, DestroyRelation DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!) } ``` |
| To | ``` struct mds_funcs {     var DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!     var DbClose: ((MDS_DB_HANDLE) -> CSSM_RETURN)!     var GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)!     var GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)!     var FreeNameList: ((MDS_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)!     var DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!     var DataDelete: ((MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!     var DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!     var DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!     var DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!     var DataAbortQuery: ((MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!     var DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!     var FreeUniqueRecord: ((MDS_DB_HANDLE, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!     var CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)!     var DestroyRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!     init()     init(DbOpen DbOpen: (@escaping (MDS_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)!, DbClose DbClose: (@escaping (MDS_DB_HANDLE) -> CSSM_RETURN)!, GetDbNames GetDbNames: (@escaping (MDS_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)!, GetDbNameFromHandle GetDbNameFromHandle: (@escaping (MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)!, FreeNameList FreeNameList: (@escaping (MDS_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)!, DataInsert DataInsert: (@escaping (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataDelete DataDelete: (@escaping (MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, DataModify DataModify: (@escaping (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)!, DataGetFirst DataGetFirst: (@escaping (MDS_DB_HANDLE, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataGetNext DataGetNext: (@escaping (MDS_DB_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)!, DataAbortQuery DataAbortQuery: (@escaping (MDS_DB_HANDLE, CSSM_HANDLE) -> CSSM_RETURN)!, DataGetFromUniqueRecordId DataGetFromUniqueRecordId: (@escaping (MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)!, FreeUniqueRecord FreeUniqueRecord: (@escaping (MDS_DB_HANDLE, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)!, CreateRelation CreateRelation: (@escaping (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)!, DestroyRelation DestroyRelation: (@escaping (MDS_DB_HANDLE, CSSM_DB_RECORDTYPE) -> CSSM_RETURN)!) } ``` |

Modified mds_funcs.CreateRelation

|  | Declaration |
| --- | --- |
| From | ``` var CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>, uint32, UnsafePointer<CSSM_DB_SCHEMA_ATTRIBUTE_INFO>, uint32, UnsafePointer<CSSM_DB_SCHEMA_INDEX_INFO>) -> CSSM_RETURN)! ``` |
| To | ``` var CreateRelation: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<Int8>?, uint32, UnsafePointer<cssm_db_schema_attribute_info>?, uint32, UnsafePointer<cssm_db_schema_index_info>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataDelete

|  | Declaration |
| --- | --- |
| From | ``` var DataDelete: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>) -> CSSM_RETURN)! ``` |
| To | ``` var DataDelete: ((MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataGetFirst

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<CSSM_QUERY>, CSSM_HANDLE_PTR, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var DataGetFirst: ((MDS_DB_HANDLE, UnsafePointer<cssm_query>?, CSSM_HANDLE_PTR?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataGetFromUniqueRecordId

|  | Declaration |
| --- | --- |
| From | ``` var DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<CSSM_DB_UNIQUE_RECORD>, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var DataGetFromUniqueRecordId: ((MDS_DB_HANDLE, UnsafePointer<cssm_db_unique_record>?, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataGetNext

|  | Declaration |
| --- | --- |
| From | ``` var DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR, CSSM_DATA_PTR, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var DataGetNext: ((MDS_DB_HANDLE, CSSM_HANDLE, UnsafeMutablePointer<cssm_db_record_attribute_data>?, UnsafeMutablePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataInsert

|  | Declaration |
| --- | --- |
| From | ``` var DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, UnsafeMutablePointer<CSSM_DB_UNIQUE_RECORD_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var DataInsert: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, UnsafeMutablePointer<UnsafeMutablePointer<cssm_db_unique_record>?>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DataModify

|  | Declaration |
| --- | --- |
| From | ``` var DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, CSSM_DB_UNIQUE_RECORD_PTR, UnsafePointer<CSSM_DB_RECORD_ATTRIBUTE_DATA>, UnsafePointer<CSSM_DATA>, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)! ``` |
| To | ``` var DataModify: ((MDS_DB_HANDLE, CSSM_DB_RECORDTYPE, UnsafeMutablePointer<cssm_db_unique_record>?, UnsafePointer<cssm_db_record_attribute_data>?, UnsafePointer<cssm_data>?, CSSM_DB_MODIFY_MODE) -> CSSM_RETURN)! ``` |

Modified mds_funcs.DbOpen

|  | Declaration |
| --- | --- |
| From | ``` var DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>, UnsafePointer<CSSM_NET_ADDRESS>, CSSM_DB_ACCESS_TYPE, UnsafePointer<CSSM_ACCESS_CREDENTIALS>, UnsafePointer<Void>, UnsafeMutablePointer<CSSM_DB_HANDLE>) -> CSSM_RETURN)! ``` |
| To | ``` var DbOpen: ((MDS_HANDLE, UnsafePointer<Int8>?, UnsafePointer<cssm_net_address>?, CSSM_DB_ACCESS_TYPE, UnsafePointer<cssm_access_credentials>?, UnsafeRawPointer?, UnsafeMutablePointer<CSSM_DB_HANDLE>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.FreeNameList

|  | Declaration |
| --- | --- |
| From | ``` var FreeNameList: ((MDS_HANDLE, CSSM_NAME_LIST_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FreeNameList: ((MDS_HANDLE, UnsafeMutablePointer<cssm_name_list>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.FreeUniqueRecord

|  | Declaration |
| --- | --- |
| From | ``` var FreeUniqueRecord: ((MDS_DB_HANDLE, CSSM_DB_UNIQUE_RECORD_PTR) -> CSSM_RETURN)! ``` |
| To | ``` var FreeUniqueRecord: ((MDS_DB_HANDLE, UnsafeMutablePointer<cssm_db_unique_record>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.GetDbNameFromHandle

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> CSSM_RETURN)! ``` |
| To | ``` var GetDbNameFromHandle: ((MDS_DB_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>?) -> CSSM_RETURN)! ``` |

Modified mds_funcs.GetDbNames

|  | Declaration |
| --- | --- |
| From | ``` var GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<CSSM_NAME_LIST_PTR>) -> CSSM_RETURN)! ``` |
| To | ``` var GetDbNames: ((MDS_HANDLE, UnsafeMutablePointer<UnsafeMutablePointer<cssm_name_list>?>?) -> CSSM_RETURN)! ``` |

Modified [SecAccessControlCreateFlags [struct]](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecAccessControlCreateFlags : OptionSetType {     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get }     static var TouchIDAny: SecAccessControlCreateFlags { get }     static var TouchIDCurrentSet: SecAccessControlCreateFlags { get }     static var DevicePasscode: SecAccessControlCreateFlags { get }     static var Or: SecAccessControlCreateFlags { get }     static var And: SecAccessControlCreateFlags { get }     static var PrivateKeyUsage: SecAccessControlCreateFlags { get }     static var ApplicationPassword: SecAccessControlCreateFlags { get } } ``` | OptionSetType |
| To | ``` struct SecAccessControlCreateFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var userPresence: SecAccessControlCreateFlags { get }     static var touchIDAny: SecAccessControlCreateFlags { get }     static var touchIDCurrentSet: SecAccessControlCreateFlags { get }     static var devicePasscode: SecAccessControlCreateFlags { get }     static var or: SecAccessControlCreateFlags { get }     static var and: SecAccessControlCreateFlags { get }     static var privateKeyUsage: SecAccessControlCreateFlags { get }     static var applicationPassword: SecAccessControlCreateFlags { get }     func intersect(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     func exclusiveOr(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     mutating func unionInPlace(_ other: SecAccessControlCreateFlags)     mutating func intersectInPlace(_ other: SecAccessControlCreateFlags)     mutating func exclusiveOrInPlace(_ other: SecAccessControlCreateFlags)     func isSubsetOf(_ other: SecAccessControlCreateFlags) -> Bool     func isDisjointWith(_ other: SecAccessControlCreateFlags) -> Bool     func isSupersetOf(_ other: SecAccessControlCreateFlags) -> Bool     mutating func subtractInPlace(_ other: SecAccessControlCreateFlags)     func isStrictSupersetOf(_ other: SecAccessControlCreateFlags) -> Bool     func isStrictSubsetOf(_ other: SecAccessControlCreateFlags) -> Bool } extension SecAccessControlCreateFlags {     func union(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     func intersection(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     func symmetricDifference(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags } extension SecAccessControlCreateFlags {     func contains(_ member: SecAccessControlCreateFlags) -> Bool     mutating func insert(_ newMember: SecAccessControlCreateFlags) -> (inserted: Bool, memberAfterInsert: SecAccessControlCreateFlags)     mutating func remove(_ member: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags?     mutating func update(with newMember: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags? } extension SecAccessControlCreateFlags {     convenience init()     mutating func formUnion(_ other: SecAccessControlCreateFlags)     mutating func formIntersection(_ other: SecAccessControlCreateFlags)     mutating func formSymmetricDifference(_ other: SecAccessControlCreateFlags) } extension SecAccessControlCreateFlags {     convenience init<S : Sequence where S.Iterator.Element == SecAccessControlCreateFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecAccessControlCreateFlags...)     mutating func subtract(_ other: SecAccessControlCreateFlags)     func isSubset(of other: SecAccessControlCreateFlags) -> Bool     func isSuperset(of other: SecAccessControlCreateFlags) -> Bool     func isDisjoint(with other: SecAccessControlCreateFlags) -> Bool     func subtracting(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecAccessControlCreateFlags) -> Bool     func isStrictSubset(of other: SecAccessControlCreateFlags) -> Bool } ``` | OptionSet |

Modified [SecAccessControlCreateFlags.devicePasscode](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1394326-devicepasscode)

|  | Declaration |
| --- | --- |
| From | ``` static var DevicePasscode: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var devicePasscode: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.userPresence](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroluserpresence)

|  | Declaration |
| --- | --- |
| From | ``` static var UserPresence: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var userPresence: SecAccessControlCreateFlags { get } ``` |

Modified [SecAsn1Template_struct [struct]](https://developer.apple.com/documentation/security/secasn1template)

|  | Declaration |
| --- | --- |
| From | ``` struct SecAsn1Template_struct {     var kind: UInt32     var offset: UInt32     var sub: UnsafePointer<Void>     var size: UInt32 } ``` |
| To | ``` struct SecAsn1Template_struct {     var kind: UInt32     var offset: UInt32     var sub: UnsafeRawPointer     var size: UInt32 } ``` |

Modified [SecAsn1Template_struct.sub](https://developer.apple.com/documentation/security/secasn1template_struct/1398515-sub)

|  | Declaration |
| --- | --- |
| From | ``` var sub: UnsafePointer<Void> ``` |
| To | ``` var sub: UnsafeRawPointer ``` |

Modified [SecAuthenticationType [enum]](https://developer.apple.com/documentation/security/secauthenticationtype)

|  | Declaration |
| --- | --- |
| From | ``` enum SecAuthenticationType : FourCharCode {     case NTLM     case MSN     case DPA     case RPA     case HTTPBasic     case HTTPDigest     case HTMLForm     case Default     case Any } ``` |
| To | ``` enum SecAuthenticationType : FourCharCode {     case NTLM     case MSN     case DPA     case RPA     case httpBasic     case httpDigest     case htmlForm     case `default`     case any } ``` |

Modified [SecAuthenticationType.any](https://developer.apple.com/documentation/security/secauthenticationtype/any)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [SecAuthenticationType.default](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypedefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [SecAuthenticationType.htmlForm](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypehtmlform)

|  | Declaration |
| --- | --- |
| From | ``` case HTMLForm ``` |
| To | ``` case htmlForm ``` |

Modified [SecAuthenticationType.httpBasic](https://developer.apple.com/documentation/security/secauthenticationtype/ksecauthenticationtypehttpbasic)

|  | Declaration |
| --- | --- |
| From | ``` case HTTPBasic ``` |
| To | ``` case httpBasic ``` |

Modified [SecAuthenticationType.httpDigest](https://developer.apple.com/documentation/security/secauthenticationtype/httpdigest)

|  | Declaration |
| --- | --- |
| From | ``` case HTTPDigest ``` |
| To | ``` case httpDigest ``` |

Modified [SecCodeSignatureFlags [struct]](https://developer.apple.com/documentation/security/seccodesignatureflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecCodeSignatureFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Host: SecCodeSignatureFlags { get }     static var Adhoc: SecCodeSignatureFlags { get }     static var ForceHard: SecCodeSignatureFlags { get }     static var ForceKill: SecCodeSignatureFlags { get }     static var ForceExpiration: SecCodeSignatureFlags { get }     static var Restrict: SecCodeSignatureFlags { get }     static var Enforcement: SecCodeSignatureFlags { get }     static var LibraryValidation: SecCodeSignatureFlags { get } } ``` | OptionSetType |
| To | ``` struct SecCodeSignatureFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var host: SecCodeSignatureFlags { get }     static var adhoc: SecCodeSignatureFlags { get }     static var forceHard: SecCodeSignatureFlags { get }     static var forceKill: SecCodeSignatureFlags { get }     static var forceExpiration: SecCodeSignatureFlags { get }     static var restrict: SecCodeSignatureFlags { get }     static var enforcement: SecCodeSignatureFlags { get }     static var libraryValidation: SecCodeSignatureFlags { get }     func intersect(_ other: SecCodeSignatureFlags) -> SecCodeSignatureFlags     func exclusiveOr(_ other: SecCodeSignatureFlags) -> SecCodeSignatureFlags     mutating func unionInPlace(_ other: SecCodeSignatureFlags)     mutating func intersectInPlace(_ other: SecCodeSignatureFlags)     mutating func exclusiveOrInPlace(_ other: SecCodeSignatureFlags)     func isSubsetOf(_ other: SecCodeSignatureFlags) -> Bool     func isDisjointWith(_ other: SecCodeSignatureFlags) -> Bool     func isSupersetOf(_ other: SecCodeSignatureFlags) -> Bool     mutating func subtractInPlace(_ other: SecCodeSignatureFlags)     func isStrictSupersetOf(_ other: SecCodeSignatureFlags) -> Bool     func isStrictSubsetOf(_ other: SecCodeSignatureFlags) -> Bool } extension SecCodeSignatureFlags {     func union(_ other: SecCodeSignatureFlags) -> SecCodeSignatureFlags     func intersection(_ other: SecCodeSignatureFlags) -> SecCodeSignatureFlags     func symmetricDifference(_ other: SecCodeSignatureFlags) -> SecCodeSignatureFlags } extension SecCodeSignatureFlags {     func contains(_ member: SecCodeSignatureFlags) -> Bool     mutating func insert(_ newMember: SecCodeSignatureFlags) -> (inserted: Bool, memberAfterInsert: SecCodeSignatureFlags)     mutating func remove(_ member: SecCodeSignatureFlags) -> SecCodeSignatureFlags?     mutating func update(with newMember: SecCodeSignatureFlags) -> SecCodeSignatureFlags? } extension SecCodeSignatureFlags {     convenience init()     mutating func formUnion(_ other: SecCodeSignatureFlags)     mutating func formIntersection(_ other: SecCodeSignatureFlags)     mutating func formSymmetricDifference(_ other: SecCodeSignatureFlags) } extension SecCodeSignatureFlags {     convenience init<S : Sequence where S.Iterator.Element == SecCodeSignatureFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecCodeSignatureFlags...)     mutating func subtract(_ other: SecCodeSignatureFlags)     func isSubset(of other: SecCodeSignatureFlags) -> Bool     func isSuperset(of other: SecCodeSignatureFlags) -> Bool     func isDisjoint(with other: SecCodeSignatureFlags) -> Bool     func subtracting(_ other: SecCodeSignatureFlags) -> SecCodeSignatureFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecCodeSignatureFlags) -> Bool     func isStrictSubset(of other: SecCodeSignatureFlags) -> Bool } ``` | OptionSet |

Modified [SecCodeSignatureFlags.adhoc](https://developer.apple.com/documentation/security/seccodesignatureflags/1397793-adhoc)

|  | Declaration |
| --- | --- |
| From | ``` static var Adhoc: SecCodeSignatureFlags { get } ``` |
| To | ``` static var adhoc: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.enforcement](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignatureenforcement)

|  | Declaration |
| --- | --- |
| From | ``` static var Enforcement: SecCodeSignatureFlags { get } ``` |
| To | ``` static var enforcement: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.forceExpiration](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignatureforceexpiration)

|  | Declaration |
| --- | --- |
| From | ``` static var ForceExpiration: SecCodeSignatureFlags { get } ``` |
| To | ``` static var forceExpiration: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.forceHard](https://developer.apple.com/documentation/security/seccodesignatureflags/1400159-forcehard)

|  | Declaration |
| --- | --- |
| From | ``` static var ForceHard: SecCodeSignatureFlags { get } ``` |
| To | ``` static var forceHard: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.forceKill](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignatureforcekill)

|  | Declaration |
| --- | --- |
| From | ``` static var ForceKill: SecCodeSignatureFlags { get } ``` |
| To | ``` static var forceKill: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.host](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignaturehost)

|  | Declaration |
| --- | --- |
| From | ``` static var Host: SecCodeSignatureFlags { get } ``` |
| To | ``` static var host: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.libraryValidation](https://developer.apple.com/documentation/security/seccodesignatureflags/1393810-libraryvalidation)

|  | Declaration |
| --- | --- |
| From | ``` static var LibraryValidation: SecCodeSignatureFlags { get } ``` |
| To | ``` static var libraryValidation: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeSignatureFlags.restrict](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignaturerestrict)

|  | Declaration |
| --- | --- |
| From | ``` static var Restrict: SecCodeSignatureFlags { get } ``` |
| To | ``` static var restrict: SecCodeSignatureFlags { get } ``` |

Modified [SecCodeStatus [struct]](https://developer.apple.com/documentation/security/seccodestatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecCodeStatus : OptionSetType {     init(rawValue rawValue: UInt32)     static var Valid: SecCodeStatus { get }     static var Hard: SecCodeStatus { get }     static var Kill: SecCodeStatus { get } } ``` | OptionSetType |
| To | ``` struct SecCodeStatus : OptionSet {     init(rawValue rawValue: UInt32)     static var valid: SecCodeStatus { get }     static var hard: SecCodeStatus { get }     static var kill: SecCodeStatus { get }     func intersect(_ other: SecCodeStatus) -> SecCodeStatus     func exclusiveOr(_ other: SecCodeStatus) -> SecCodeStatus     mutating func unionInPlace(_ other: SecCodeStatus)     mutating func intersectInPlace(_ other: SecCodeStatus)     mutating func exclusiveOrInPlace(_ other: SecCodeStatus)     func isSubsetOf(_ other: SecCodeStatus) -> Bool     func isDisjointWith(_ other: SecCodeStatus) -> Bool     func isSupersetOf(_ other: SecCodeStatus) -> Bool     mutating func subtractInPlace(_ other: SecCodeStatus)     func isStrictSupersetOf(_ other: SecCodeStatus) -> Bool     func isStrictSubsetOf(_ other: SecCodeStatus) -> Bool } extension SecCodeStatus {     func union(_ other: SecCodeStatus) -> SecCodeStatus     func intersection(_ other: SecCodeStatus) -> SecCodeStatus     func symmetricDifference(_ other: SecCodeStatus) -> SecCodeStatus } extension SecCodeStatus {     func contains(_ member: SecCodeStatus) -> Bool     mutating func insert(_ newMember: SecCodeStatus) -> (inserted: Bool, memberAfterInsert: SecCodeStatus)     mutating func remove(_ member: SecCodeStatus) -> SecCodeStatus?     mutating func update(with newMember: SecCodeStatus) -> SecCodeStatus? } extension SecCodeStatus {     convenience init()     mutating func formUnion(_ other: SecCodeStatus)     mutating func formIntersection(_ other: SecCodeStatus)     mutating func formSymmetricDifference(_ other: SecCodeStatus) } extension SecCodeStatus {     convenience init<S : Sequence where S.Iterator.Element == SecCodeStatus>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecCodeStatus...)     mutating func subtract(_ other: SecCodeStatus)     func isSubset(of other: SecCodeStatus) -> Bool     func isSuperset(of other: SecCodeStatus) -> Bool     func isDisjoint(with other: SecCodeStatus) -> Bool     func subtracting(_ other: SecCodeStatus) -> SecCodeStatus     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecCodeStatus) -> Bool     func isStrictSubset(of other: SecCodeStatus) -> Bool } ``` | OptionSet |

Modified [SecCodeStatus.hard](https://developer.apple.com/documentation/security/seccodestatus/1395917-hard)

|  | Declaration |
| --- | --- |
| From | ``` static var Hard: SecCodeStatus { get } ``` |
| To | ``` static var hard: SecCodeStatus { get } ``` |

Modified [SecCodeStatus.kill](https://developer.apple.com/documentation/security/seccodestatus/1398182-kill)

|  | Declaration |
| --- | --- |
| From | ``` static var Kill: SecCodeStatus { get } ``` |
| To | ``` static var kill: SecCodeStatus { get } ``` |

Modified [SecCodeStatus.valid](https://developer.apple.com/documentation/security/seccodestatus/kseccodestatusvalid)

|  | Declaration |
| --- | --- |
| From | ``` static var Valid: SecCodeStatus { get } ``` |
| To | ``` static var valid: SecCodeStatus { get } ``` |

Modified [SecCredentialType [enum]](https://developer.apple.com/documentation/security/seccredentialtype)

|  | Declaration |
| --- | --- |
| From | ``` enum SecCredentialType : uint32 {     case Default     case WithUI     case NoUI } ``` |
| To | ``` enum SecCredentialType : uint32 {     case `default`     case withUI     case noUI } ``` |

Modified [SecCredentialType.default](https://developer.apple.com/documentation/security/seccredentialtype/kseccredentialtypedefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [SecCredentialType.noUI](https://developer.apple.com/documentation/security/seccredentialtype/noui)

|  | Declaration |
| --- | --- |
| From | ``` case NoUI ``` |
| To | ``` case noUI ``` |

Modified [SecCredentialType.withUI](https://developer.apple.com/documentation/security/seccredentialtype/withui)

|  | Declaration |
| --- | --- |
| From | ``` case WithUI ``` |
| To | ``` case withUI ``` |

Modified [SecCSDigestAlgorithm [enum]](https://developer.apple.com/documentation/security/seccsdigestalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` enum SecCSDigestAlgorithm : UInt32 {     case CodeSignatureNoHash     case CodeSignatureHashSHA1     case CodeSignatureHashSHA256     case CodeSignatureHashSHA256Truncated     case CodeSignatureHashSHA384 } ``` |
| To | ``` enum SecCSDigestAlgorithm : UInt32 {     case codeSignatureNoHash     case codeSignatureHashSHA1     case codeSignatureHashSHA256     case codeSignatureHashSHA256Truncated     case codeSignatureHashSHA384 } ``` |

Modified [SecCSDigestAlgorithm.codeSignatureHashSHA1](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha1)

|  | Declaration |
| --- | --- |
| From | ``` case CodeSignatureHashSHA1 ``` |
| To | ``` case codeSignatureHashSHA1 ``` |

Modified [SecCSDigestAlgorithm.codeSignatureHashSHA256](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha256)

|  | Declaration |
| --- | --- |
| From | ``` case CodeSignatureHashSHA256 ``` |
| To | ``` case codeSignatureHashSHA256 ``` |

Modified [SecCSDigestAlgorithm.codeSignatureHashSHA256Truncated](https://developer.apple.com/documentation/security/seccsdigestalgorithm/codesignaturehashsha256truncated)

|  | Declaration |
| --- | --- |
| From | ``` case CodeSignatureHashSHA256Truncated ``` |
| To | ``` case codeSignatureHashSHA256Truncated ``` |

Modified [SecCSDigestAlgorithm.codeSignatureHashSHA384](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha384)

|  | Declaration |
| --- | --- |
| From | ``` case CodeSignatureHashSHA384 ``` |
| To | ``` case codeSignatureHashSHA384 ``` |

Modified [SecCSDigestAlgorithm.codeSignatureNoHash](https://developer.apple.com/documentation/security/seccsdigestalgorithm/codesignaturenohash)

|  | Declaration |
| --- | --- |
| From | ``` case CodeSignatureNoHash ``` |
| To | ``` case codeSignatureNoHash ``` |

Modified [SecCSFlags [struct]](https://developer.apple.com/documentation/security/seccsflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecCSFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var DefaultFlags: SecCSFlags { get }     static var ConsiderExpiration: SecCSFlags { get }     static var EnforceRevocationChecks: SecCSFlags { get }     static var NoNetworkAccess: SecCSFlags { get }     static var ReportProgress: SecCSFlags { get }     static var CheckTrustedAnchors: SecCSFlags { get } } ``` | OptionSetType |
| To | ``` struct SecCSFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var defaultFlags: SecCSFlags { get }     static var considerExpiration: SecCSFlags { get }     static var enforceRevocationChecks: SecCSFlags { get }     static var noNetworkAccess: SecCSFlags { get }     static var reportProgress: SecCSFlags { get }     static var checkTrustedAnchors: SecCSFlags { get }     static var quickCheck: SecCSFlags { get }     func intersect(_ other: SecCSFlags) -> SecCSFlags     func exclusiveOr(_ other: SecCSFlags) -> SecCSFlags     mutating func unionInPlace(_ other: SecCSFlags)     mutating func intersectInPlace(_ other: SecCSFlags)     mutating func exclusiveOrInPlace(_ other: SecCSFlags)     func isSubsetOf(_ other: SecCSFlags) -> Bool     func isDisjointWith(_ other: SecCSFlags) -> Bool     func isSupersetOf(_ other: SecCSFlags) -> Bool     mutating func subtractInPlace(_ other: SecCSFlags)     func isStrictSupersetOf(_ other: SecCSFlags) -> Bool     func isStrictSubsetOf(_ other: SecCSFlags) -> Bool } extension SecCSFlags {     func union(_ other: SecCSFlags) -> SecCSFlags     func intersection(_ other: SecCSFlags) -> SecCSFlags     func symmetricDifference(_ other: SecCSFlags) -> SecCSFlags } extension SecCSFlags {     func contains(_ member: SecCSFlags) -> Bool     mutating func insert(_ newMember: SecCSFlags) -> (inserted: Bool, memberAfterInsert: SecCSFlags)     mutating func remove(_ member: SecCSFlags) -> SecCSFlags?     mutating func update(with newMember: SecCSFlags) -> SecCSFlags? } extension SecCSFlags {     convenience init()     mutating func formUnion(_ other: SecCSFlags)     mutating func formIntersection(_ other: SecCSFlags)     mutating func formSymmetricDifference(_ other: SecCSFlags) } extension SecCSFlags {     convenience init<S : Sequence where S.Iterator.Element == SecCSFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecCSFlags...)     mutating func subtract(_ other: SecCSFlags)     func isSubset(of other: SecCSFlags) -> Bool     func isSuperset(of other: SecCSFlags) -> Bool     func isDisjoint(with other: SecCSFlags) -> Bool     func subtracting(_ other: SecCSFlags) -> SecCSFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecCSFlags) -> Bool     func isStrictSubset(of other: SecCSFlags) -> Bool } ``` | OptionSet |

Modified [SecCSFlags.checkTrustedAnchors](https://developer.apple.com/documentation/security/seccsflags/kseccschecktrustedanchors)

|  | Declaration |
| --- | --- |
| From | ``` static var CheckTrustedAnchors: SecCSFlags { get } ``` |
| To | ``` static var checkTrustedAnchors: SecCSFlags { get } ``` |

Modified [SecCSFlags.considerExpiration](https://developer.apple.com/documentation/security/seccsflags/1400700-considerexpiration)

|  | Declaration |
| --- | --- |
| From | ``` static var ConsiderExpiration: SecCSFlags { get } ``` |
| To | ``` static var considerExpiration: SecCSFlags { get } ``` |

Modified [SecCSFlags.enforceRevocationChecks](https://developer.apple.com/documentation/security/seccsflags/kseccsenforcerevocationchecks)

|  | Declaration |
| --- | --- |
| From | ``` static var EnforceRevocationChecks: SecCSFlags { get } ``` |
| To | ``` static var enforceRevocationChecks: SecCSFlags { get } ``` |

Modified [SecCSFlags.noNetworkAccess](https://developer.apple.com/documentation/security/seccsflags/1397911-nonetworkaccess)

|  | Declaration |
| --- | --- |
| From | ``` static var NoNetworkAccess: SecCSFlags { get } ``` |
| To | ``` static var noNetworkAccess: SecCSFlags { get } ``` |

Modified [SecCSFlags.reportProgress](https://developer.apple.com/documentation/security/seccsflags/kseccsreportprogress)

|  | Declaration |
| --- | --- |
| From | ``` static var ReportProgress: SecCSFlags { get } ``` |
| To | ``` static var reportProgress: SecCSFlags { get } ``` |

Modified [SecExternalFormat [enum]](https://developer.apple.com/documentation/security/secexternalformat)

|  | Declaration |
| --- | --- |
| From | ``` enum SecExternalFormat : UInt32 {     case FormatUnknown     case FormatOpenSSL     case FormatSSH     case FormatBSAFE     case FormatRawKey     case FormatWrappedPKCS8     case FormatWrappedOpenSSL     case FormatWrappedSSH     case FormatWrappedLSH     case FormatX509Cert     case FormatPEMSequence     case FormatPKCS7     case FormatPKCS12     case FormatNetscapeCertSequence     case FormatSSHv2 } ``` |
| To | ``` enum SecExternalFormat : UInt32 {     case formatUnknown     case formatOpenSSL     case formatSSH     case formatBSAFE     case formatRawKey     case formatWrappedPKCS8     case formatWrappedOpenSSL     case formatWrappedSSH     case formatWrappedLSH     case formatX509Cert     case formatPEMSequence     case formatPKCS7     case formatPKCS12     case formatNetscapeCertSequence     case formatSSHv2 } ``` |

Modified [SecExternalFormat.formatBSAFE](https://developer.apple.com/documentation/security/secexternalformat/formatbsafe)

|  | Declaration |
| --- | --- |
| From | ``` case FormatBSAFE ``` |
| To | ``` case formatBSAFE ``` |

Modified [SecExternalFormat.formatNetscapeCertSequence](https://developer.apple.com/documentation/security/secexternalformat/formatnetscapecertsequence)

|  | Declaration |
| --- | --- |
| From | ``` case FormatNetscapeCertSequence ``` |
| To | ``` case formatNetscapeCertSequence ``` |

Modified [SecExternalFormat.formatOpenSSL](https://developer.apple.com/documentation/security/secexternalformat/formatopenssl)

|  | Declaration |
| --- | --- |
| From | ``` case FormatOpenSSL ``` |
| To | ``` case formatOpenSSL ``` |

Modified [SecExternalFormat.formatPEMSequence](https://developer.apple.com/documentation/security/secexternalformat/ksecformatpemsequence)

|  | Declaration |
| --- | --- |
| From | ``` case FormatPEMSequence ``` |
| To | ``` case formatPEMSequence ``` |

Modified [SecExternalFormat.formatPKCS12](https://developer.apple.com/documentation/security/secexternalformat/formatpkcs12)

|  | Declaration |
| --- | --- |
| From | ``` case FormatPKCS12 ``` |
| To | ``` case formatPKCS12 ``` |

Modified [SecExternalFormat.formatPKCS7](https://developer.apple.com/documentation/security/secexternalformat/formatpkcs7)

|  | Declaration |
| --- | --- |
| From | ``` case FormatPKCS7 ``` |
| To | ``` case formatPKCS7 ``` |

Modified [SecExternalFormat.formatRawKey](https://developer.apple.com/documentation/security/secexternalformat/ksecformatrawkey)

|  | Declaration |
| --- | --- |
| From | ``` case FormatRawKey ``` |
| To | ``` case formatRawKey ``` |

Modified [SecExternalFormat.formatSSH](https://developer.apple.com/documentation/security/secexternalformat/ksecformatssh)

|  | Declaration |
| --- | --- |
| From | ``` case FormatSSH ``` |
| To | ``` case formatSSH ``` |

Modified [SecExternalFormat.formatSSHv2](https://developer.apple.com/documentation/security/secexternalformat/ksecformatsshv2)

|  | Declaration |
| --- | --- |
| From | ``` case FormatSSHv2 ``` |
| To | ``` case formatSSHv2 ``` |

Modified [SecExternalFormat.formatUnknown](https://developer.apple.com/documentation/security/secexternalformat/formatunknown)

|  | Declaration |
| --- | --- |
| From | ``` case FormatUnknown ``` |
| To | ``` case formatUnknown ``` |

Modified [SecExternalFormat.formatWrappedLSH](https://developer.apple.com/documentation/security/secexternalformat/formatwrappedlsh)

|  | Declaration |
| --- | --- |
| From | ``` case FormatWrappedLSH ``` |
| To | ``` case formatWrappedLSH ``` |

Modified [SecExternalFormat.formatWrappedOpenSSL](https://developer.apple.com/documentation/security/secexternalformat/ksecformatwrappedopenssl)

|  | Declaration |
| --- | --- |
| From | ``` case FormatWrappedOpenSSL ``` |
| To | ``` case formatWrappedOpenSSL ``` |

Modified [SecExternalFormat.formatWrappedPKCS8](https://developer.apple.com/documentation/security/secexternalformat/ksecformatwrappedpkcs8)

|  | Declaration |
| --- | --- |
| From | ``` case FormatWrappedPKCS8 ``` |
| To | ``` case formatWrappedPKCS8 ``` |

Modified [SecExternalFormat.formatWrappedSSH](https://developer.apple.com/documentation/security/secexternalformat/formatwrappedssh)

|  | Declaration |
| --- | --- |
| From | ``` case FormatWrappedSSH ``` |
| To | ``` case formatWrappedSSH ``` |

Modified [SecExternalFormat.formatX509Cert](https://developer.apple.com/documentation/security/secexternalformat/ksecformatx509cert)

|  | Declaration |
| --- | --- |
| From | ``` case FormatX509Cert ``` |
| To | ``` case formatX509Cert ``` |

Modified [SecExternalItemType [enum]](https://developer.apple.com/documentation/security/secexternalitemtype)

|  | Declaration |
| --- | --- |
| From | ``` enum SecExternalItemType : UInt32 {     case ItemTypeUnknown     case ItemTypePrivateKey     case ItemTypePublicKey     case ItemTypeSessionKey     case ItemTypeCertificate     case ItemTypeAggregate } ``` |
| To | ``` enum SecExternalItemType : UInt32 {     case itemTypeUnknown     case itemTypePrivateKey     case itemTypePublicKey     case itemTypeSessionKey     case itemTypeCertificate     case itemTypeAggregate } ``` |

Modified [SecExternalItemType.itemTypeAggregate](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeaggregate)

|  | Declaration |
| --- | --- |
| From | ``` case ItemTypeAggregate ``` |
| To | ``` case itemTypeAggregate ``` |

Modified [SecExternalItemType.itemTypeCertificate](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypecertificate)

|  | Declaration |
| --- | --- |
| From | ``` case ItemTypeCertificate ``` |
| To | ``` case itemTypeCertificate ``` |

Modified [SecExternalItemType.itemTypePrivateKey](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeprivatekey)

|  | Declaration |
| --- | --- |
| From | ``` case ItemTypePrivateKey ``` |
| To | ``` case itemTypePrivateKey ``` |

Modified [SecExternalItemType.itemTypePublicKey](https://developer.apple.com/documentation/security/secexternalitemtype/ksecitemtypepublickey)

|  | Declaration |
| --- | --- |
| From | ``` case ItemTypePublicKey ``` |
| To | ``` case itemTypePublicKey ``` |

Modified [SecExternalItemType.itemTypeSessionKey](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypesessionkey)

|  | Declaration |
| --- | --- |
| From | ``` case ItemTypeSessionKey ``` |
| To | ``` case itemTypeSessionKey ``` |

Modified [SecExternalItemType.itemTypeUnknown](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeunknown)

|  | Declaration |
| --- | --- |
| From | ``` case ItemTypeUnknown ``` |
| To | ``` case itemTypeUnknown ``` |

Modified [SecItemAttr [enum]](https://developer.apple.com/documentation/security/secitemattr)

|  | Declaration |
| --- | --- |
| From | ``` enum SecItemAttr : FourCharCode {     case CreationDateItemAttr     case ModDateItemAttr     case DescriptionItemAttr     case CommentItemAttr     case CreatorItemAttr     case TypeItemAttr     case ScriptCodeItemAttr     case LabelItemAttr     case InvisibleItemAttr     case NegativeItemAttr     case CustomIconItemAttr     case AccountItemAttr     case ServiceItemAttr     case GenericItemAttr     case SecurityDomainItemAttr     case ServerItemAttr     case AuthenticationTypeItemAttr     case PortItemAttr     case PathItemAttr     case VolumeItemAttr     case AddressItemAttr     case SignatureItemAttr     case ProtocolItemAttr     case CertificateType     case CertificateEncoding     case CrlType     case CrlEncoding     case Alias } ``` |
| To | ``` enum SecItemAttr : FourCharCode {     case creationDateItemAttr     case modDateItemAttr     case descriptionItemAttr     case commentItemAttr     case creatorItemAttr     case typeItemAttr     case scriptCodeItemAttr     case labelItemAttr     case invisibleItemAttr     case negativeItemAttr     case customIconItemAttr     case accountItemAttr     case serviceItemAttr     case genericItemAttr     case securityDomainItemAttr     case serverItemAttr     case authenticationTypeItemAttr     case portItemAttr     case pathItemAttr     case volumeItemAttr     case addressItemAttr     case signatureItemAttr     case protocolItemAttr     case certificateType     case certificateEncoding     case crlType     case crlEncoding     case alias } ``` |

Modified [SecItemAttr.accountItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecaccountitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case AccountItemAttr ``` |
| To | ``` case accountItemAttr ``` |

Modified [SecItemAttr.addressItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecaddressitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case AddressItemAttr ``` |
| To | ``` case addressItemAttr ``` |

Modified [SecItemAttr.alias](https://developer.apple.com/documentation/security/secitemattr/alias)

|  | Declaration |
| --- | --- |
| From | ``` case Alias ``` |
| To | ``` case alias ``` |

Modified [SecItemAttr.authenticationTypeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecauthenticationtypeitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticationTypeItemAttr ``` |
| To | ``` case authenticationTypeItemAttr ``` |

Modified [SecItemAttr.certificateEncoding](https://developer.apple.com/documentation/security/secitemattr/certificateencoding)

|  | Declaration |
| --- | --- |
| From | ``` case CertificateEncoding ``` |
| To | ``` case certificateEncoding ``` |

Modified [SecItemAttr.certificateType](https://developer.apple.com/documentation/security/secitemattr/kseccertificatetype)

|  | Declaration |
| --- | --- |
| From | ``` case CertificateType ``` |
| To | ``` case certificateType ``` |

Modified [SecItemAttr.commentItemAttr](https://developer.apple.com/documentation/security/secitemattr/commentitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case CommentItemAttr ``` |
| To | ``` case commentItemAttr ``` |

Modified [SecItemAttr.creationDateItemAttr](https://developer.apple.com/documentation/security/secitemattr/kseccreationdateitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case CreationDateItemAttr ``` |
| To | ``` case creationDateItemAttr ``` |

Modified [SecItemAttr.creatorItemAttr](https://developer.apple.com/documentation/security/secitemattr/creatoritemattr)

|  | Declaration |
| --- | --- |
| From | ``` case CreatorItemAttr ``` |
| To | ``` case creatorItemAttr ``` |

Modified [SecItemAttr.crlEncoding](https://developer.apple.com/documentation/security/secitemattr/crlencoding)

|  | Declaration |
| --- | --- |
| From | ``` case CrlEncoding ``` |
| To | ``` case crlEncoding ``` |

Modified [SecItemAttr.crlType](https://developer.apple.com/documentation/security/secitemattr/crltype)

|  | Declaration |
| --- | --- |
| From | ``` case CrlType ``` |
| To | ``` case crlType ``` |

Modified [SecItemAttr.customIconItemAttr](https://developer.apple.com/documentation/security/secitemattr/customiconitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case CustomIconItemAttr ``` |
| To | ``` case customIconItemAttr ``` |

Modified [SecItemAttr.descriptionItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecdescriptionitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case DescriptionItemAttr ``` |
| To | ``` case descriptionItemAttr ``` |

Modified [SecItemAttr.genericItemAttr](https://developer.apple.com/documentation/security/secitemattr/genericitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case GenericItemAttr ``` |
| To | ``` case genericItemAttr ``` |

Modified [SecItemAttr.invisibleItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecinvisibleitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case InvisibleItemAttr ``` |
| To | ``` case invisibleItemAttr ``` |

Modified [SecItemAttr.labelItemAttr](https://developer.apple.com/documentation/security/secitemattr/kseclabelitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case LabelItemAttr ``` |
| To | ``` case labelItemAttr ``` |

Modified [SecItemAttr.modDateItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecmoddateitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case ModDateItemAttr ``` |
| To | ``` case modDateItemAttr ``` |

Modified [SecItemAttr.negativeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecnegativeitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case NegativeItemAttr ``` |
| To | ``` case negativeItemAttr ``` |

Modified [SecItemAttr.pathItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecpathitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case PathItemAttr ``` |
| To | ``` case pathItemAttr ``` |

Modified [SecItemAttr.portItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecportitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case PortItemAttr ``` |
| To | ``` case portItemAttr ``` |

Modified [SecItemAttr.protocolItemAttr](https://developer.apple.com/documentation/security/secitemattr/protocolitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case ProtocolItemAttr ``` |
| To | ``` case protocolItemAttr ``` |

Modified [SecItemAttr.scriptCodeItemAttr](https://developer.apple.com/documentation/security/secitemattr/scriptcodeitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case ScriptCodeItemAttr ``` |
| To | ``` case scriptCodeItemAttr ``` |

Modified [SecItemAttr.securityDomainItemAttr](https://developer.apple.com/documentation/security/secitemattr/securitydomainitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case SecurityDomainItemAttr ``` |
| To | ``` case securityDomainItemAttr ``` |

Modified [SecItemAttr.serverItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecserveritemattr)

|  | Declaration |
| --- | --- |
| From | ``` case ServerItemAttr ``` |
| To | ``` case serverItemAttr ``` |

Modified [SecItemAttr.serviceItemAttr](https://developer.apple.com/documentation/security/secitemattr/serviceitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case ServiceItemAttr ``` |
| To | ``` case serviceItemAttr ``` |

Modified [SecItemAttr.signatureItemAttr](https://developer.apple.com/documentation/security/secitemattr/signatureitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case SignatureItemAttr ``` |
| To | ``` case signatureItemAttr ``` |

Modified [SecItemAttr.typeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksectypeitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case TypeItemAttr ``` |
| To | ``` case typeItemAttr ``` |

Modified [SecItemAttr.volumeItemAttr](https://developer.apple.com/documentation/security/secitemattr/ksecvolumeitemattr)

|  | Declaration |
| --- | --- |
| From | ``` case VolumeItemAttr ``` |
| To | ``` case volumeItemAttr ``` |

Modified [SecItemClass [enum]](https://developer.apple.com/documentation/security/secitemclass)

|  | Declaration |
| --- | --- |
| From | ``` enum SecItemClass : FourCharCode {     case InternetPasswordItemClass     case GenericPasswordItemClass     case AppleSharePasswordItemClass     case CertificateItemClass     case PublicKeyItemClass     case PrivateKeyItemClass     case SymmetricKeyItemClass } ``` |
| To | ``` enum SecItemClass : FourCharCode {     case internetPasswordItemClass     case genericPasswordItemClass     case appleSharePasswordItemClass     case certificateItemClass     case publicKeyItemClass     case privateKeyItemClass     case symmetricKeyItemClass } ``` |

Modified [SecItemClass.certificateItemClass](https://developer.apple.com/documentation/security/secitemclass/kseccertificateitemclass)

|  | Declaration |
| --- | --- |
| From | ``` case CertificateItemClass ``` |
| To | ``` case certificateItemClass ``` |

Modified [SecItemClass.genericPasswordItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecgenericpassworditemclass)

|  | Declaration |
| --- | --- |
| From | ``` case GenericPasswordItemClass ``` |
| To | ``` case genericPasswordItemClass ``` |

Modified [SecItemClass.internetPasswordItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecinternetpassworditemclass)

|  | Declaration |
| --- | --- |
| From | ``` case InternetPasswordItemClass ``` |
| To | ``` case internetPasswordItemClass ``` |

Modified [SecItemClass.privateKeyItemClass](https://developer.apple.com/documentation/security/secitemclass/privatekeyitemclass)

|  | Declaration |
| --- | --- |
| From | ``` case PrivateKeyItemClass ``` |
| To | ``` case privateKeyItemClass ``` |

Modified [SecItemClass.publicKeyItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecpublickeyitemclass)

|  | Declaration |
| --- | --- |
| From | ``` case PublicKeyItemClass ``` |
| To | ``` case publicKeyItemClass ``` |

Modified [SecItemClass.symmetricKeyItemClass](https://developer.apple.com/documentation/security/secitemclass/symmetrickeyitemclass)

|  | Declaration |
| --- | --- |
| From | ``` case SymmetricKeyItemClass ``` |
| To | ``` case symmetricKeyItemClass ``` |

Modified [SecItemImportExportFlags [struct]](https://developer.apple.com/documentation/security/secitemimportexportflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecItemImportExportFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var PemArmour: SecItemImportExportFlags { get } } ``` | OptionSetType |
| To | ``` struct SecItemImportExportFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var pemArmour: SecItemImportExportFlags { get }     func intersect(_ other: SecItemImportExportFlags) -> SecItemImportExportFlags     func exclusiveOr(_ other: SecItemImportExportFlags) -> SecItemImportExportFlags     mutating func unionInPlace(_ other: SecItemImportExportFlags)     mutating func intersectInPlace(_ other: SecItemImportExportFlags)     mutating func exclusiveOrInPlace(_ other: SecItemImportExportFlags)     func isSubsetOf(_ other: SecItemImportExportFlags) -> Bool     func isDisjointWith(_ other: SecItemImportExportFlags) -> Bool     func isSupersetOf(_ other: SecItemImportExportFlags) -> Bool     mutating func subtractInPlace(_ other: SecItemImportExportFlags)     func isStrictSupersetOf(_ other: SecItemImportExportFlags) -> Bool     func isStrictSubsetOf(_ other: SecItemImportExportFlags) -> Bool } extension SecItemImportExportFlags {     func union(_ other: SecItemImportExportFlags) -> SecItemImportExportFlags     func intersection(_ other: SecItemImportExportFlags) -> SecItemImportExportFlags     func symmetricDifference(_ other: SecItemImportExportFlags) -> SecItemImportExportFlags } extension SecItemImportExportFlags {     func contains(_ member: SecItemImportExportFlags) -> Bool     mutating func insert(_ newMember: SecItemImportExportFlags) -> (inserted: Bool, memberAfterInsert: SecItemImportExportFlags)     mutating func remove(_ member: SecItemImportExportFlags) -> SecItemImportExportFlags?     mutating func update(with newMember: SecItemImportExportFlags) -> SecItemImportExportFlags? } extension SecItemImportExportFlags {     convenience init()     mutating func formUnion(_ other: SecItemImportExportFlags)     mutating func formIntersection(_ other: SecItemImportExportFlags)     mutating func formSymmetricDifference(_ other: SecItemImportExportFlags) } extension SecItemImportExportFlags {     convenience init<S : Sequence where S.Iterator.Element == SecItemImportExportFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecItemImportExportFlags...)     mutating func subtract(_ other: SecItemImportExportFlags)     func isSubset(of other: SecItemImportExportFlags) -> Bool     func isSuperset(of other: SecItemImportExportFlags) -> Bool     func isDisjoint(with other: SecItemImportExportFlags) -> Bool     func subtracting(_ other: SecItemImportExportFlags) -> SecItemImportExportFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecItemImportExportFlags) -> Bool     func isStrictSubset(of other: SecItemImportExportFlags) -> Bool } ``` | OptionSet |

Modified [SecItemImportExportFlags.pemArmour](https://developer.apple.com/documentation/security/secitemimportexportflags/1399536-pemarmour)

|  | Declaration |
| --- | --- |
| From | ``` static var PemArmour: SecItemImportExportFlags { get } ``` |
| To | ``` static var pemArmour: SecItemImportExportFlags { get } ``` |

Modified [SecItemImportExportKeyParameters [struct]](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters)

|  | Declaration |
| --- | --- |
| From | ``` struct SecItemImportExportKeyParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>     var alertTitle: Unmanaged<CFString>     var alertPrompt: Unmanaged<CFString>     var accessRef: Unmanaged<SecAccess>?     var keyUsage: Unmanaged<CFArray>?     var keyAttributes: Unmanaged<CFArray>? } ``` |
| To | ``` struct SecItemImportExportKeyParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<CFTypeRef>     var alertTitle: Unmanaged<CFString>     var alertPrompt: Unmanaged<CFString>     var accessRef: Unmanaged<SecAccess>?     var keyUsage: Unmanaged<CFArray>?     var keyAttributes: Unmanaged<CFArray>? } ``` |

Modified [SecItemImportExportKeyParameters.passphrase](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/1395469-passphrase)

|  | Declaration |
| --- | --- |
| From | ``` var passphrase: Unmanaged<AnyObject> ``` |
| To | ``` var passphrase: Unmanaged<CFTypeRef> ``` |

Modified [SecKeychainAttribute [struct]](https://developer.apple.com/documentation/security/seckeychainattribute)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeychainAttribute {     var tag: SecKeychainAttrType     var length: UInt32     var data: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct SecKeychainAttribute {     var tag: SecKeychainAttrType     var length: UInt32     var data: UnsafeMutableRawPointer } ``` |

Modified [SecKeychainAttribute.data](https://developer.apple.com/documentation/security/seckeychainattribute/1397254-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<Void> ``` |
| To | ``` var data: UnsafeMutableRawPointer ``` |

Modified [SecKeychainEvent [enum]](https://developer.apple.com/documentation/security/seckeychainevent)

|  | Declaration |
| --- | --- |
| From | ``` enum SecKeychainEvent : UInt32 {     case LockEvent     case UnlockEvent     case AddEvent     case DeleteEvent     case UpdateEvent     case PasswordChangedEvent     case DefaultChangedEvent     case DataAccessEvent     case KeychainListChangedEvent     case TrustSettingsChangedEvent } ``` |
| To | ``` enum SecKeychainEvent : UInt32 {     case lockEvent     case unlockEvent     case addEvent     case deleteEvent     case updateEvent     case passwordChangedEvent     case defaultChangedEvent     case dataAccessEvent     case keychainListChangedEvent     case trustSettingsChangedEvent } ``` |

Modified [SecKeychainEvent.addEvent](https://developer.apple.com/documentation/security/seckeychainevent/addevent)

|  | Declaration |
| --- | --- |
| From | ``` case AddEvent ``` |
| To | ``` case addEvent ``` |

Modified [SecKeychainEvent.dataAccessEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecdataaccessevent)

|  | Declaration |
| --- | --- |
| From | ``` case DataAccessEvent ``` |
| To | ``` case dataAccessEvent ``` |

Modified [SecKeychainEvent.defaultChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecdefaultchangedevent)

|  | Declaration |
| --- | --- |
| From | ``` case DefaultChangedEvent ``` |
| To | ``` case defaultChangedEvent ``` |

Modified [SecKeychainEvent.deleteEvent](https://developer.apple.com/documentation/security/seckeychainevent/deleteevent)

|  | Declaration |
| --- | --- |
| From | ``` case DeleteEvent ``` |
| To | ``` case deleteEvent ``` |

Modified [SecKeychainEvent.keychainListChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/keychainlistchangedevent)

|  | Declaration |
| --- | --- |
| From | ``` case KeychainListChangedEvent ``` |
| To | ``` case keychainListChangedEvent ``` |

Modified [SecKeychainEvent.lockEvent](https://developer.apple.com/documentation/security/seckeychainevent/kseclockevent)

|  | Declaration |
| --- | --- |
| From | ``` case LockEvent ``` |
| To | ``` case lockEvent ``` |

Modified [SecKeychainEvent.passwordChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecpasswordchangedevent)

|  | Declaration |
| --- | --- |
| From | ``` case PasswordChangedEvent ``` |
| To | ``` case passwordChangedEvent ``` |

Modified [SecKeychainEvent.trustSettingsChangedEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksectrustsettingschangedevent)

|  | Declaration |
| --- | --- |
| From | ``` case TrustSettingsChangedEvent ``` |
| To | ``` case trustSettingsChangedEvent ``` |

Modified [SecKeychainEvent.unlockEvent](https://developer.apple.com/documentation/security/seckeychainevent/ksecunlockevent)

|  | Declaration |
| --- | --- |
| From | ``` case UnlockEvent ``` |
| To | ``` case unlockEvent ``` |

Modified [SecKeychainEvent.updateEvent](https://developer.apple.com/documentation/security/seckeychainevent/updateevent)

|  | Declaration |
| --- | --- |
| From | ``` case UpdateEvent ``` |
| To | ``` case updateEvent ``` |

Modified [SecKeychainEventMask [struct]](https://developer.apple.com/documentation/security/seckeychaineventmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecKeychainEventMask : OptionSetType {     init(rawValue rawValue: UInt32)     static var LockEventMask: SecKeychainEventMask { get }     static var UnlockEventMask: SecKeychainEventMask { get }     static var AddEventMask: SecKeychainEventMask { get }     static var DeleteEventMask: SecKeychainEventMask { get }     static var UpdateEventMask: SecKeychainEventMask { get }     static var PasswordChangedEventMask: SecKeychainEventMask { get }     static var DefaultChangedEventMask: SecKeychainEventMask { get }     static var DataAccessEventMask: SecKeychainEventMask { get }     static var KeychainListChangedMask: SecKeychainEventMask { get }     static var TrustSettingsChangedEventMask: SecKeychainEventMask { get }     static var EveryEventMask: SecKeychainEventMask { get } } ``` | OptionSetType |
| To | ``` struct SecKeychainEventMask : OptionSet {     init(rawValue rawValue: UInt32)     static var lockEventMask: SecKeychainEventMask { get }     static var unlockEventMask: SecKeychainEventMask { get }     static var addEventMask: SecKeychainEventMask { get }     static var deleteEventMask: SecKeychainEventMask { get }     static var updateEventMask: SecKeychainEventMask { get }     static var passwordChangedEventMask: SecKeychainEventMask { get }     static var defaultChangedEventMask: SecKeychainEventMask { get }     static var dataAccessEventMask: SecKeychainEventMask { get }     static var keychainListChangedMask: SecKeychainEventMask { get }     static var trustSettingsChangedEventMask: SecKeychainEventMask { get }     static var everyEventMask: SecKeychainEventMask { get }     func intersect(_ other: SecKeychainEventMask) -> SecKeychainEventMask     func exclusiveOr(_ other: SecKeychainEventMask) -> SecKeychainEventMask     mutating func unionInPlace(_ other: SecKeychainEventMask)     mutating func intersectInPlace(_ other: SecKeychainEventMask)     mutating func exclusiveOrInPlace(_ other: SecKeychainEventMask)     func isSubsetOf(_ other: SecKeychainEventMask) -> Bool     func isDisjointWith(_ other: SecKeychainEventMask) -> Bool     func isSupersetOf(_ other: SecKeychainEventMask) -> Bool     mutating func subtractInPlace(_ other: SecKeychainEventMask)     func isStrictSupersetOf(_ other: SecKeychainEventMask) -> Bool     func isStrictSubsetOf(_ other: SecKeychainEventMask) -> Bool } extension SecKeychainEventMask {     func union(_ other: SecKeychainEventMask) -> SecKeychainEventMask     func intersection(_ other: SecKeychainEventMask) -> SecKeychainEventMask     func symmetricDifference(_ other: SecKeychainEventMask) -> SecKeychainEventMask } extension SecKeychainEventMask {     func contains(_ member: SecKeychainEventMask) -> Bool     mutating func insert(_ newMember: SecKeychainEventMask) -> (inserted: Bool, memberAfterInsert: SecKeychainEventMask)     mutating func remove(_ member: SecKeychainEventMask) -> SecKeychainEventMask?     mutating func update(with newMember: SecKeychainEventMask) -> SecKeychainEventMask? } extension SecKeychainEventMask {     convenience init()     mutating func formUnion(_ other: SecKeychainEventMask)     mutating func formIntersection(_ other: SecKeychainEventMask)     mutating func formSymmetricDifference(_ other: SecKeychainEventMask) } extension SecKeychainEventMask {     convenience init<S : Sequence where S.Iterator.Element == SecKeychainEventMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecKeychainEventMask...)     mutating func subtract(_ other: SecKeychainEventMask)     func isSubset(of other: SecKeychainEventMask) -> Bool     func isSuperset(of other: SecKeychainEventMask) -> Bool     func isDisjoint(with other: SecKeychainEventMask) -> Bool     func subtracting(_ other: SecKeychainEventMask) -> SecKeychainEventMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecKeychainEventMask) -> Bool     func isStrictSubset(of other: SecKeychainEventMask) -> Bool } ``` | OptionSet |

Modified [SecKeychainEventMask.addEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1399566-addeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var AddEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var addEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.dataAccessEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecdataaccesseventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var DataAccessEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var dataAccessEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.defaultChangedEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecdefaultchangedeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var DefaultChangedEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var defaultChangedEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.deleteEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1392414-deleteeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var DeleteEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var deleteEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.everyEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/kseceveryeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var EveryEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var everyEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.keychainListChangedMask](https://developer.apple.com/documentation/security/seckeychaineventmask/kseckeychainlistchangedmask)

|  | Declaration |
| --- | --- |
| From | ``` static var KeychainListChangedMask: SecKeychainEventMask { get } ``` |
| To | ``` static var keychainListChangedMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.lockEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1398376-lockeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var LockEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var lockEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.passwordChangedEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecpasswordchangedeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var PasswordChangedEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var passwordChangedEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.trustSettingsChangedEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksectrustsettingschangedeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var TrustSettingsChangedEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var trustSettingsChangedEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.unlockEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/1392496-unlockeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var UnlockEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var unlockEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainEventMask.updateEventMask](https://developer.apple.com/documentation/security/seckeychaineventmask/ksecupdateeventmask)

|  | Declaration |
| --- | --- |
| From | ``` static var UpdateEventMask: SecKeychainEventMask { get } ``` |
| To | ``` static var updateEventMask: SecKeychainEventMask { get } ``` |

Modified [SecKeychainPromptSelector [struct]](https://developer.apple.com/documentation/security/seckeychainpromptselector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecKeychainPromptSelector : OptionSetType {     init(rawValue rawValue: uint16)     static var RequirePassphase: SecKeychainPromptSelector { get }     static var Unsigned: SecKeychainPromptSelector { get }     static var UnsignedAct: SecKeychainPromptSelector { get }     static var Invalid: SecKeychainPromptSelector { get }     static var InvalidAct: SecKeychainPromptSelector { get } } ``` | OptionSetType |
| To | ``` struct SecKeychainPromptSelector : OptionSet {     init(rawValue rawValue: uint16)     static var requirePassphase: SecKeychainPromptSelector { get }     static var unsigned: SecKeychainPromptSelector { get }     static var unsignedAct: SecKeychainPromptSelector { get }     static var invalid: SecKeychainPromptSelector { get }     static var invalidAct: SecKeychainPromptSelector { get }     func intersect(_ other: SecKeychainPromptSelector) -> SecKeychainPromptSelector     func exclusiveOr(_ other: SecKeychainPromptSelector) -> SecKeychainPromptSelector     mutating func unionInPlace(_ other: SecKeychainPromptSelector)     mutating func intersectInPlace(_ other: SecKeychainPromptSelector)     mutating func exclusiveOrInPlace(_ other: SecKeychainPromptSelector)     func isSubsetOf(_ other: SecKeychainPromptSelector) -> Bool     func isDisjointWith(_ other: SecKeychainPromptSelector) -> Bool     func isSupersetOf(_ other: SecKeychainPromptSelector) -> Bool     mutating func subtractInPlace(_ other: SecKeychainPromptSelector)     func isStrictSupersetOf(_ other: SecKeychainPromptSelector) -> Bool     func isStrictSubsetOf(_ other: SecKeychainPromptSelector) -> Bool } extension SecKeychainPromptSelector {     func union(_ other: SecKeychainPromptSelector) -> SecKeychainPromptSelector     func intersection(_ other: SecKeychainPromptSelector) -> SecKeychainPromptSelector     func symmetricDifference(_ other: SecKeychainPromptSelector) -> SecKeychainPromptSelector } extension SecKeychainPromptSelector {     func contains(_ member: SecKeychainPromptSelector) -> Bool     mutating func insert(_ newMember: SecKeychainPromptSelector) -> (inserted: Bool, memberAfterInsert: SecKeychainPromptSelector)     mutating func remove(_ member: SecKeychainPromptSelector) -> SecKeychainPromptSelector?     mutating func update(with newMember: SecKeychainPromptSelector) -> SecKeychainPromptSelector? } extension SecKeychainPromptSelector {     convenience init()     mutating func formUnion(_ other: SecKeychainPromptSelector)     mutating func formIntersection(_ other: SecKeychainPromptSelector)     mutating func formSymmetricDifference(_ other: SecKeychainPromptSelector) } extension SecKeychainPromptSelector {     convenience init<S : Sequence where S.Iterator.Element == SecKeychainPromptSelector>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecKeychainPromptSelector...)     mutating func subtract(_ other: SecKeychainPromptSelector)     func isSubset(of other: SecKeychainPromptSelector) -> Bool     func isSuperset(of other: SecKeychainPromptSelector) -> Bool     func isDisjoint(with other: SecKeychainPromptSelector) -> Bool     func subtracting(_ other: SecKeychainPromptSelector) -> SecKeychainPromptSelector     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecKeychainPromptSelector) -> Bool     func isStrictSubset(of other: SecKeychainPromptSelector) -> Bool } ``` | OptionSet |

Modified [SecKeychainPromptSelector.invalid](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptinvalid)

|  | Declaration |
| --- | --- |
| From | ``` static var Invalid: SecKeychainPromptSelector { get } ``` |
| To | ``` static var invalid: SecKeychainPromptSelector { get } ``` |

Modified [SecKeychainPromptSelector.invalidAct](https://developer.apple.com/documentation/security/seckeychainpromptselector/1395933-invalidact)

|  | Declaration |
| --- | --- |
| From | ``` static var InvalidAct: SecKeychainPromptSelector { get } ``` |
| To | ``` static var invalidAct: SecKeychainPromptSelector { get } ``` |

Modified [SecKeychainPromptSelector.requirePassphase](https://developer.apple.com/documentation/security/seckeychainpromptselector/1396844-requirepassphase)

|  | Declaration |
| --- | --- |
| From | ``` static var RequirePassphase: SecKeychainPromptSelector { get } ``` |
| To | ``` static var requirePassphase: SecKeychainPromptSelector { get } ``` |

Modified [SecKeychainPromptSelector.unsigned](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptunsigned)

|  | Declaration |
| --- | --- |
| From | ``` static var Unsigned: SecKeychainPromptSelector { get } ``` |
| To | ``` static var unsigned: SecKeychainPromptSelector { get } ``` |

Modified [SecKeychainPromptSelector.unsignedAct](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptunsignedact)

|  | Declaration |
| --- | --- |
| From | ``` static var UnsignedAct: SecKeychainPromptSelector { get } ``` |
| To | ``` static var unsignedAct: SecKeychainPromptSelector { get } ``` |

Modified [SecKeyImportExportFlags [struct]](https://developer.apple.com/documentation/security/seckeyimportexportflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecKeyImportExportFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var ImportOnlyOne: SecKeyImportExportFlags { get }     static var SecurePassphrase: SecKeyImportExportFlags { get }     static var NoAccessControl: SecKeyImportExportFlags { get } } ``` | OptionSetType |
| To | ``` struct SecKeyImportExportFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var importOnlyOne: SecKeyImportExportFlags { get }     static var securePassphrase: SecKeyImportExportFlags { get }     static var noAccessControl: SecKeyImportExportFlags { get }     func intersect(_ other: SecKeyImportExportFlags) -> SecKeyImportExportFlags     func exclusiveOr(_ other: SecKeyImportExportFlags) -> SecKeyImportExportFlags     mutating func unionInPlace(_ other: SecKeyImportExportFlags)     mutating func intersectInPlace(_ other: SecKeyImportExportFlags)     mutating func exclusiveOrInPlace(_ other: SecKeyImportExportFlags)     func isSubsetOf(_ other: SecKeyImportExportFlags) -> Bool     func isDisjointWith(_ other: SecKeyImportExportFlags) -> Bool     func isSupersetOf(_ other: SecKeyImportExportFlags) -> Bool     mutating func subtractInPlace(_ other: SecKeyImportExportFlags)     func isStrictSupersetOf(_ other: SecKeyImportExportFlags) -> Bool     func isStrictSubsetOf(_ other: SecKeyImportExportFlags) -> Bool } extension SecKeyImportExportFlags {     func union(_ other: SecKeyImportExportFlags) -> SecKeyImportExportFlags     func intersection(_ other: SecKeyImportExportFlags) -> SecKeyImportExportFlags     func symmetricDifference(_ other: SecKeyImportExportFlags) -> SecKeyImportExportFlags } extension SecKeyImportExportFlags {     func contains(_ member: SecKeyImportExportFlags) -> Bool     mutating func insert(_ newMember: SecKeyImportExportFlags) -> (inserted: Bool, memberAfterInsert: SecKeyImportExportFlags)     mutating func remove(_ member: SecKeyImportExportFlags) -> SecKeyImportExportFlags?     mutating func update(with newMember: SecKeyImportExportFlags) -> SecKeyImportExportFlags? } extension SecKeyImportExportFlags {     convenience init()     mutating func formUnion(_ other: SecKeyImportExportFlags)     mutating func formIntersection(_ other: SecKeyImportExportFlags)     mutating func formSymmetricDifference(_ other: SecKeyImportExportFlags) } extension SecKeyImportExportFlags {     convenience init<S : Sequence where S.Iterator.Element == SecKeyImportExportFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecKeyImportExportFlags...)     mutating func subtract(_ other: SecKeyImportExportFlags)     func isSubset(of other: SecKeyImportExportFlags) -> Bool     func isSuperset(of other: SecKeyImportExportFlags) -> Bool     func isDisjoint(with other: SecKeyImportExportFlags) -> Bool     func subtracting(_ other: SecKeyImportExportFlags) -> SecKeyImportExportFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecKeyImportExportFlags) -> Bool     func isStrictSubset(of other: SecKeyImportExportFlags) -> Bool } ``` | OptionSet |

Modified [SecKeyImportExportFlags.importOnlyOne](https://developer.apple.com/documentation/security/seckeyimportexportflags/1392169-importonlyone)

|  | Declaration |
| --- | --- |
| From | ``` static var ImportOnlyOne: SecKeyImportExportFlags { get } ``` |
| To | ``` static var importOnlyOne: SecKeyImportExportFlags { get } ``` |

Modified [SecKeyImportExportFlags.noAccessControl](https://developer.apple.com/documentation/security/seckeyimportexportflags/kseckeynoaccesscontrol)

|  | Declaration |
| --- | --- |
| From | ``` static var NoAccessControl: SecKeyImportExportFlags { get } ``` |
| To | ``` static var noAccessControl: SecKeyImportExportFlags { get } ``` |

Modified [SecKeyImportExportFlags.securePassphrase](https://developer.apple.com/documentation/security/seckeyimportexportflags/kseckeysecurepassphrase)

|  | Declaration |
| --- | --- |
| From | ``` static var SecurePassphrase: SecKeyImportExportFlags { get } ``` |
| To | ``` static var securePassphrase: SecKeyImportExportFlags { get } ``` |

Modified [SecKeyImportExportParameters [struct]](https://developer.apple.com/documentation/security/seckeyimportexportparameters)

|  | Declaration |
| --- | --- |
| From | ``` struct SecKeyImportExportParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<AnyObject>     var alertTitle: Unmanaged<CFString>     var alertPrompt: Unmanaged<CFString>     var accessRef: Unmanaged<SecAccess>?     var keyUsage: CSSM_KEYUSE     var keyAttributes: CSSM_KEYATTR_FLAGS } ``` |
| To | ``` struct SecKeyImportExportParameters {     var version: UInt32     var flags: SecKeyImportExportFlags     var passphrase: Unmanaged<CFTypeRef>     var alertTitle: Unmanaged<CFString>     var alertPrompt: Unmanaged<CFString>     var accessRef: Unmanaged<SecAccess>?     var keyUsage: CSSM_KEYUSE     var keyAttributes: CSSM_KEYATTR_FLAGS } ``` |

Modified [SecKeyImportExportParameters.passphrase](https://developer.apple.com/documentation/security/seckeyimportexportparameters/1399051-passphrase)

|  | Declaration |
| --- | --- |
| From | ``` var passphrase: Unmanaged<AnyObject> ``` |
| To | ``` var passphrase: Unmanaged<CFTypeRef> ``` |

Modified [SecKeySizes [enum]](https://developer.apple.com/documentation/security/seckeysizes)

|  | Declaration |
| --- | --- |
| From | ``` enum SecKeySizes : UInt32 {     case SecDefaultKeySize     case Sec3DES192     case SecAES128     static var SecAES192: SecKeySizes { get }     case SecAES256     static var Secp192r1: SecKeySizes { get }     static var Secp256r1: SecKeySizes { get }     case Secp384r1     case Secp521r1     case SecRSAMin     case SecRSAMax } ``` |
| To | ``` enum SecKeySizes : UInt32 {     case secDefaultKeySize     case sec3DES192     case secAES128     static var secAES192: SecKeySizes { get }     case secAES256     static var secp192r1: SecKeySizes { get }     static var secp256r1: SecKeySizes { get }     case secp384r1     case secp521r1     case secRSAMin     case secRSAMax } ``` |

Modified [SecKeySizes.sec3DES192](https://developer.apple.com/documentation/security/seckeysizes/sec3des192)

|  | Declaration |
| --- | --- |
| From | ``` case Sec3DES192 ``` |
| To | ``` case sec3DES192 ``` |

Modified [SecKeySizes.secAES128](https://developer.apple.com/documentation/security/seckeysizes/secaes128)

|  | Declaration |
| --- | --- |
| From | ``` case SecAES128 ``` |
| To | ``` case secAES128 ``` |

Modified [SecKeySizes.secAES192](https://developer.apple.com/documentation/security/seckeysizes/1400540-secaes192)

|  | Declaration |
| --- | --- |
| From | ``` static var SecAES192: SecKeySizes { get } ``` |
| To | ``` static var secAES192: SecKeySizes { get } ``` |

Modified [SecKeySizes.secAES256](https://developer.apple.com/documentation/security/seckeysizes/ksecaes256)

|  | Declaration |
| --- | --- |
| From | ``` case SecAES256 ``` |
| To | ``` case secAES256 ``` |

Modified [SecKeySizes.secDefaultKeySize](https://developer.apple.com/documentation/security/seckeysizes/ksecdefaultkeysize)

|  | Declaration |
| --- | --- |
| From | ``` case SecDefaultKeySize ``` |
| To | ``` case secDefaultKeySize ``` |

Modified [SecKeySizes.secp192r1](https://developer.apple.com/documentation/security/seckeysizes/1398550-secp192r1)

|  | Declaration |
| --- | --- |
| From | ``` static var Secp192r1: SecKeySizes { get } ``` |
| To | ``` static var secp192r1: SecKeySizes { get } ``` |

Modified [SecKeySizes.secp256r1](https://developer.apple.com/documentation/security/seckeysizes/1398756-secp256r1)

|  | Declaration |
| --- | --- |
| From | ``` static var Secp256r1: SecKeySizes { get } ``` |
| To | ``` static var secp256r1: SecKeySizes { get } ``` |

Modified [SecKeySizes.secp384r1](https://developer.apple.com/documentation/security/seckeysizes/ksecp384r1)

|  | Declaration |
| --- | --- |
| From | ``` case Secp384r1 ``` |
| To | ``` case secp384r1 ``` |

Modified [SecKeySizes.secp521r1](https://developer.apple.com/documentation/security/seckeysizes/ksecp521r1)

|  | Declaration |
| --- | --- |
| From | ``` case Secp521r1 ``` |
| To | ``` case secp521r1 ``` |

Modified [SecKeySizes.secRSAMax](https://developer.apple.com/documentation/security/seckeysizes/ksecrsamax)

|  | Declaration |
| --- | --- |
| From | ``` case SecRSAMax ``` |
| To | ``` case secRSAMax ``` |

Modified [SecKeySizes.secRSAMin](https://developer.apple.com/documentation/security/seckeysizes/secrsamin)

|  | Declaration |
| --- | --- |
| From | ``` case SecRSAMin ``` |
| To | ``` case secRSAMin ``` |

Modified [SecPadding [enum]](https://developer.apple.com/documentation/security/secpadding)

|  | Declaration |
| --- | --- |
| From | ``` enum SecPadding : UInt32 {     case None     case PKCS1     case SigRaw     case PKCS1MD2     case PKCS1MD5     case PKCS1SHA1 } ``` |
| To | ``` enum SecPadding : UInt32 {     case none     case PKCS1     case sigRaw     case PKCS1MD2     case PKCS1MD5     case PKCS1SHA1 } ``` |

Modified [SecPadding.none](https://developer.apple.com/documentation/security/secpadding/ksecpaddingnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [SecPadding.sigRaw](https://developer.apple.com/documentation/security/secpadding/1401132-sigraw)

|  | Declaration |
| --- | --- |
| From | ``` case SigRaw ``` |
| To | ``` case sigRaw ``` |

Modified [SecPreferencesDomain [enum]](https://developer.apple.com/documentation/security/secpreferencesdomain)

|  | Declaration |
| --- | --- |
| From | ``` enum SecPreferencesDomain : Int32 {     case User     case System     case Common     case Dynamic } ``` |
| To | ``` enum SecPreferencesDomain : Int32 {     case user     case system     case common     case dynamic } ``` |

Modified [SecPreferencesDomain.common](https://developer.apple.com/documentation/security/secpreferencesdomain/ksecpreferencesdomaincommon)

|  | Declaration |
| --- | --- |
| From | ``` case Common ``` |
| To | ``` case common ``` |

Modified [SecPreferencesDomain.dynamic](https://developer.apple.com/documentation/security/secpreferencesdomain/dynamic)

|  | Declaration |
| --- | --- |
| From | ``` case Dynamic ``` |
| To | ``` case dynamic ``` |

Modified [SecPreferencesDomain.system](https://developer.apple.com/documentation/security/secpreferencesdomain/ksecpreferencesdomainsystem)

|  | Declaration |
| --- | --- |
| From | ``` case System ``` |
| To | ``` case system ``` |

Modified [SecPreferencesDomain.user](https://developer.apple.com/documentation/security/secpreferencesdomain/ksecpreferencesdomainuser)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [SecProtocolType [enum]](https://developer.apple.com/documentation/security/secprotocoltype)

|  | Declaration |
| --- | --- |
| From | ``` enum SecProtocolType : FourCharCode {     case FTP     case FTPAccount     case HTTP     case IRC     case NNTP     case POP3     case SMTP     case SOCKS     case IMAP     case LDAP     case AppleTalk     case AFP     case Telnet     case SSH     case FTPS     case HTTPS     case HTTPProxy     case HTTPSProxy     case FTPProxy     case CIFS     case SMB     case RTSP     case RTSPProxy     case DAAP     case EPPC     case IPP     case NNTPS     case LDAPS     case TelnetS     case IMAPS     case IRCS     case POP3S     case CVSpserver     case SVN     case Any } ``` |
| To | ``` enum SecProtocolType : FourCharCode {     case FTP     case ftpAccount     case HTTP     case IRC     case NNTP     case POP3     case SMTP     case SOCKS     case IMAP     case LDAP     case appleTalk     case AFP     case telnet     case SSH     case FTPS     case HTTPS     case httpProxy     case httpsProxy     case ftpProxy     case CIFS     case SMB     case RTSP     case rtspProxy     case DAAP     case EPPC     case IPP     case NNTPS     case LDAPS     case telnetS     case IMAPS     case IRCS     case POP3S     case cvSpserver     case SVN     case any } ``` |

Modified [SecProtocolType.any](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeany)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [SecProtocolType.appleTalk](https://developer.apple.com/documentation/security/secprotocoltype/appletalk)

|  | Declaration |
| --- | --- |
| From | ``` case AppleTalk ``` |
| To | ``` case appleTalk ``` |

Modified [SecProtocolType.cvSpserver](https://developer.apple.com/documentation/security/secprotocoltype/cvspserver)

|  | Declaration |
| --- | --- |
| From | ``` case CVSpserver ``` |
| To | ``` case cvSpserver ``` |

Modified [SecProtocolType.ftpAccount](https://developer.apple.com/documentation/security/secprotocoltype/ftpaccount)

|  | Declaration |
| --- | --- |
| From | ``` case FTPAccount ``` |
| To | ``` case ftpAccount ``` |

Modified [SecProtocolType.ftpProxy](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypeftpproxy)

|  | Declaration |
| --- | --- |
| From | ``` case FTPProxy ``` |
| To | ``` case ftpProxy ``` |

Modified [SecProtocolType.httpProxy](https://developer.apple.com/documentation/security/secprotocoltype/httpproxy)

|  | Declaration |
| --- | --- |
| From | ``` case HTTPProxy ``` |
| To | ``` case httpProxy ``` |

Modified [SecProtocolType.httpsProxy](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypehttpsproxy)

|  | Declaration |
| --- | --- |
| From | ``` case HTTPSProxy ``` |
| To | ``` case httpsProxy ``` |

Modified [SecProtocolType.rtspProxy](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypertspproxy)

|  | Declaration |
| --- | --- |
| From | ``` case RTSPProxy ``` |
| To | ``` case rtspProxy ``` |

Modified [SecProtocolType.telnet](https://developer.apple.com/documentation/security/secprotocoltype/ksecprotocoltypetelnet)

|  | Declaration |
| --- | --- |
| From | ``` case Telnet ``` |
| To | ``` case telnet ``` |

Modified [SecProtocolType.telnetS](https://developer.apple.com/documentation/security/secprotocoltype/telnets)

|  | Declaration |
| --- | --- |
| From | ``` case TelnetS ``` |
| To | ``` case telnetS ``` |

Modified [SecRequirementType [enum]](https://developer.apple.com/documentation/security/secrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` enum SecRequirementType : UInt32 {     case HostRequirementType     case GuestRequirementType     case DesignatedRequirementType     case LibraryRequirementType     case PluginRequirementType     case InvalidRequirementType     static var RequirementTypeCount: SecRequirementType { get } } ``` |
| To | ``` enum SecRequirementType : UInt32 {     case hostRequirementType     case guestRequirementType     case designatedRequirementType     case libraryRequirementType     case pluginRequirementType     case invalidRequirementType     static var requirementTypeCount: SecRequirementType { get } } ``` |

Modified [SecRequirementType.designatedRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/ksecdesignatedrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` case DesignatedRequirementType ``` |
| To | ``` case designatedRequirementType ``` |

Modified [SecRequirementType.guestRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/guestrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` case GuestRequirementType ``` |
| To | ``` case guestRequirementType ``` |

Modified [SecRequirementType.hostRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/hostrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` case HostRequirementType ``` |
| To | ``` case hostRequirementType ``` |

Modified [SecRequirementType.invalidRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/invalidrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidRequirementType ``` |
| To | ``` case invalidRequirementType ``` |

Modified [SecRequirementType.libraryRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/kseclibraryrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` case LibraryRequirementType ``` |
| To | ``` case libraryRequirementType ``` |

Modified [SecRequirementType.pluginRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/ksecpluginrequirementtype)

|  | Declaration |
| --- | --- |
| From | ``` case PluginRequirementType ``` |
| To | ``` case pluginRequirementType ``` |

Modified [SecRequirementType.requirementTypeCount](https://developer.apple.com/documentation/security/secrequirementtype/1401052-requirementtypecount)

|  | Declaration |
| --- | --- |
| From | ``` static var RequirementTypeCount: SecRequirementType { get } ``` |
| To | ``` static var requirementTypeCount: SecRequirementType { get } ``` |

Modified [SecTransformMetaAttributeType [enum]](https://developer.apple.com/documentation/security/sectransformmetaattributetype)

|  | Declaration |
| --- | --- |
| From | ``` enum SecTransformMetaAttributeType : CFIndex {     case Value     case Name     case Ref     case Required     case RequiresOutboundConnection     case Deferred     case Stream     case CanCycle     case Externalize     case HasOutboundConnections     case HasInboundConnection } ``` |
| To | ``` enum SecTransformMetaAttributeType : CFIndex {     case value     case name     case ref     case required     case requiresOutboundConnection     case deferred     case stream     case canCycle     case externalize     case hasOutboundConnections     case hasInboundConnection } ``` |

Modified [SecTransformMetaAttributeType.canCycle](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributecancycle)

|  | Declaration |
| --- | --- |
| From | ``` case CanCycle ``` |
| To | ``` case canCycle ``` |

Modified [SecTransformMetaAttributeType.deferred](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributedeferred)

|  | Declaration |
| --- | --- |
| From | ``` case Deferred ``` |
| To | ``` case deferred ``` |

Modified [SecTransformMetaAttributeType.externalize](https://developer.apple.com/documentation/security/sectransformmetaattributetype/externalize)

|  | Declaration |
| --- | --- |
| From | ``` case Externalize ``` |
| To | ``` case externalize ``` |

Modified [SecTransformMetaAttributeType.hasInboundConnection](https://developer.apple.com/documentation/security/sectransformmetaattributetype/hasinboundconnection)

|  | Declaration |
| --- | --- |
| From | ``` case HasInboundConnection ``` |
| To | ``` case hasInboundConnection ``` |

Modified [SecTransformMetaAttributeType.hasOutboundConnections](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributehasoutboundconnections)

|  | Declaration |
| --- | --- |
| From | ``` case HasOutboundConnections ``` |
| To | ``` case hasOutboundConnections ``` |

Modified [SecTransformMetaAttributeType.name](https://developer.apple.com/documentation/security/sectransformmetaattributetype/name)

|  | Declaration |
| --- | --- |
| From | ``` case Name ``` |
| To | ``` case name ``` |

Modified [SecTransformMetaAttributeType.ref](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributeref)

|  | Declaration |
| --- | --- |
| From | ``` case Ref ``` |
| To | ``` case ref ``` |

Modified [SecTransformMetaAttributeType.required](https://developer.apple.com/documentation/security/sectransformmetaattributetype/required)

|  | Declaration |
| --- | --- |
| From | ``` case Required ``` |
| To | ``` case required ``` |

Modified [SecTransformMetaAttributeType.requiresOutboundConnection](https://developer.apple.com/documentation/security/sectransformmetaattributetype/requiresoutboundconnection)

|  | Declaration |
| --- | --- |
| From | ``` case RequiresOutboundConnection ``` |
| To | ``` case requiresOutboundConnection ``` |

Modified [SecTransformMetaAttributeType.stream](https://developer.apple.com/documentation/security/sectransformmetaattributetype/stream)

|  | Declaration |
| --- | --- |
| From | ``` case Stream ``` |
| To | ``` case stream ``` |

Modified [SecTransformMetaAttributeType.value](https://developer.apple.com/documentation/security/sectransformmetaattributetype/value)

|  | Declaration |
| --- | --- |
| From | ``` case Value ``` |
| To | ``` case value ``` |

Modified [SecTrustOptionFlags [struct]](https://developer.apple.com/documentation/security/sectrustoptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecTrustOptionFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var AllowExpired: SecTrustOptionFlags { get }     static var LeafIsCA: SecTrustOptionFlags { get }     static var FetchIssuerFromNet: SecTrustOptionFlags { get }     static var AllowExpiredRoot: SecTrustOptionFlags { get }     static var RequireRevPerCert: SecTrustOptionFlags { get }     static var UseTrustSettings: SecTrustOptionFlags { get }     static var ImplicitAnchors: SecTrustOptionFlags { get } } ``` | OptionSetType |
| To | ``` struct SecTrustOptionFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var allowExpired: SecTrustOptionFlags { get }     static var leafIsCA: SecTrustOptionFlags { get }     static var fetchIssuerFromNet: SecTrustOptionFlags { get }     static var allowExpiredRoot: SecTrustOptionFlags { get }     static var requireRevPerCert: SecTrustOptionFlags { get }     static var useTrustSettings: SecTrustOptionFlags { get }     static var implicitAnchors: SecTrustOptionFlags { get }     func intersect(_ other: SecTrustOptionFlags) -> SecTrustOptionFlags     func exclusiveOr(_ other: SecTrustOptionFlags) -> SecTrustOptionFlags     mutating func unionInPlace(_ other: SecTrustOptionFlags)     mutating func intersectInPlace(_ other: SecTrustOptionFlags)     mutating func exclusiveOrInPlace(_ other: SecTrustOptionFlags)     func isSubsetOf(_ other: SecTrustOptionFlags) -> Bool     func isDisjointWith(_ other: SecTrustOptionFlags) -> Bool     func isSupersetOf(_ other: SecTrustOptionFlags) -> Bool     mutating func subtractInPlace(_ other: SecTrustOptionFlags)     func isStrictSupersetOf(_ other: SecTrustOptionFlags) -> Bool     func isStrictSubsetOf(_ other: SecTrustOptionFlags) -> Bool } extension SecTrustOptionFlags {     func union(_ other: SecTrustOptionFlags) -> SecTrustOptionFlags     func intersection(_ other: SecTrustOptionFlags) -> SecTrustOptionFlags     func symmetricDifference(_ other: SecTrustOptionFlags) -> SecTrustOptionFlags } extension SecTrustOptionFlags {     func contains(_ member: SecTrustOptionFlags) -> Bool     mutating func insert(_ newMember: SecTrustOptionFlags) -> (inserted: Bool, memberAfterInsert: SecTrustOptionFlags)     mutating func remove(_ member: SecTrustOptionFlags) -> SecTrustOptionFlags?     mutating func update(with newMember: SecTrustOptionFlags) -> SecTrustOptionFlags? } extension SecTrustOptionFlags {     convenience init()     mutating func formUnion(_ other: SecTrustOptionFlags)     mutating func formIntersection(_ other: SecTrustOptionFlags)     mutating func formSymmetricDifference(_ other: SecTrustOptionFlags) } extension SecTrustOptionFlags {     convenience init<S : Sequence where S.Iterator.Element == SecTrustOptionFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecTrustOptionFlags...)     mutating func subtract(_ other: SecTrustOptionFlags)     func isSubset(of other: SecTrustOptionFlags) -> Bool     func isSuperset(of other: SecTrustOptionFlags) -> Bool     func isDisjoint(with other: SecTrustOptionFlags) -> Bool     func subtracting(_ other: SecTrustOptionFlags) -> SecTrustOptionFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecTrustOptionFlags) -> Bool     func isStrictSubset(of other: SecTrustOptionFlags) -> Bool } ``` | OptionSet |

Modified [SecTrustOptionFlags.allowExpired](https://developer.apple.com/documentation/security/sectrustoptionflags/1396581-allowexpired)

|  | Declaration |
| --- | --- |
| From | ``` static var AllowExpired: SecTrustOptionFlags { get } ``` |
| To | ``` static var allowExpired: SecTrustOptionFlags { get } ``` |

Modified [SecTrustOptionFlags.allowExpiredRoot](https://developer.apple.com/documentation/security/sectrustoptionflags/1401432-allowexpiredroot)

|  | Declaration |
| --- | --- |
| From | ``` static var AllowExpiredRoot: SecTrustOptionFlags { get } ``` |
| To | ``` static var allowExpiredRoot: SecTrustOptionFlags { get } ``` |

Modified [SecTrustOptionFlags.fetchIssuerFromNet](https://developer.apple.com/documentation/security/sectrustoptionflags/1395949-fetchissuerfromnet)

|  | Declaration |
| --- | --- |
| From | ``` static var FetchIssuerFromNet: SecTrustOptionFlags { get } ``` |
| To | ``` static var fetchIssuerFromNet: SecTrustOptionFlags { get } ``` |

Modified [SecTrustOptionFlags.implicitAnchors](https://developer.apple.com/documentation/security/sectrustoptionflags/1400933-implicitanchors)

|  | Declaration |
| --- | --- |
| From | ``` static var ImplicitAnchors: SecTrustOptionFlags { get } ``` |
| To | ``` static var implicitAnchors: SecTrustOptionFlags { get } ``` |

Modified [SecTrustOptionFlags.leafIsCA](https://developer.apple.com/documentation/security/sectrustoptionflags/1397419-leafisca)

|  | Declaration |
| --- | --- |
| From | ``` static var LeafIsCA: SecTrustOptionFlags { get } ``` |
| To | ``` static var leafIsCA: SecTrustOptionFlags { get } ``` |

Modified [SecTrustOptionFlags.requireRevPerCert](https://developer.apple.com/documentation/security/sectrustoptionflags/ksectrustoptionrequirerevpercert)

|  | Declaration |
| --- | --- |
| From | ``` static var RequireRevPerCert: SecTrustOptionFlags { get } ``` |
| To | ``` static var requireRevPerCert: SecTrustOptionFlags { get } ``` |

Modified [SecTrustOptionFlags.useTrustSettings](https://developer.apple.com/documentation/security/sectrustoptionflags/1398574-usetrustsettings)

|  | Declaration |
| --- | --- |
| From | ``` static var UseTrustSettings: SecTrustOptionFlags { get } ``` |
| To | ``` static var useTrustSettings: SecTrustOptionFlags { get } ``` |

Modified [SecTrustSettingsDomain [enum]](https://developer.apple.com/documentation/security/sectrustsettingsdomain)

|  | Declaration |
| --- | --- |
| From | ``` enum SecTrustSettingsDomain : uint32 {     case User     case Admin     case System } ``` |
| To | ``` enum SecTrustSettingsDomain : uint32 {     case user     case admin     case system } ``` |

Modified [SecTrustSettingsDomain.admin](https://developer.apple.com/documentation/security/sectrustsettingsdomain/ksectrustsettingsdomainadmin)

|  | Declaration |
| --- | --- |
| From | ``` case Admin ``` |
| To | ``` case admin ``` |

Modified [SecTrustSettingsDomain.system](https://developer.apple.com/documentation/security/sectrustsettingsdomain/system)

|  | Declaration |
| --- | --- |
| From | ``` case System ``` |
| To | ``` case system ``` |

Modified [SecTrustSettingsDomain.user](https://developer.apple.com/documentation/security/sectrustsettingsdomain/ksectrustsettingsdomainuser)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [SecTrustSettingsKeyUsage [struct]](https://developer.apple.com/documentation/security/sectrustsettingskeyusage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecTrustSettingsKeyUsage : OptionSetType {     init(rawValue rawValue: uint32)     static var UseSignature: SecTrustSettingsKeyUsage { get }     static var UseEnDecryptData: SecTrustSettingsKeyUsage { get }     static var UseEnDecryptKey: SecTrustSettingsKeyUsage { get }     static var UseSignCert: SecTrustSettingsKeyUsage { get }     static var UseSignRevocation: SecTrustSettingsKeyUsage { get }     static var UseKeyExchange: SecTrustSettingsKeyUsage { get }     static var UseAny: SecTrustSettingsKeyUsage { get } } ``` | OptionSetType |
| To | ``` struct SecTrustSettingsKeyUsage : OptionSet {     init(rawValue rawValue: uint32)     static var useSignature: SecTrustSettingsKeyUsage { get }     static var useEnDecryptData: SecTrustSettingsKeyUsage { get }     static var useEnDecryptKey: SecTrustSettingsKeyUsage { get }     static var useSignCert: SecTrustSettingsKeyUsage { get }     static var useSignRevocation: SecTrustSettingsKeyUsage { get }     static var useKeyExchange: SecTrustSettingsKeyUsage { get }     static var useAny: SecTrustSettingsKeyUsage { get }     func intersect(_ other: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage     func exclusiveOr(_ other: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage     mutating func unionInPlace(_ other: SecTrustSettingsKeyUsage)     mutating func intersectInPlace(_ other: SecTrustSettingsKeyUsage)     mutating func exclusiveOrInPlace(_ other: SecTrustSettingsKeyUsage)     func isSubsetOf(_ other: SecTrustSettingsKeyUsage) -> Bool     func isDisjointWith(_ other: SecTrustSettingsKeyUsage) -> Bool     func isSupersetOf(_ other: SecTrustSettingsKeyUsage) -> Bool     mutating func subtractInPlace(_ other: SecTrustSettingsKeyUsage)     func isStrictSupersetOf(_ other: SecTrustSettingsKeyUsage) -> Bool     func isStrictSubsetOf(_ other: SecTrustSettingsKeyUsage) -> Bool } extension SecTrustSettingsKeyUsage {     func union(_ other: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage     func intersection(_ other: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage     func symmetricDifference(_ other: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage } extension SecTrustSettingsKeyUsage {     func contains(_ member: SecTrustSettingsKeyUsage) -> Bool     mutating func insert(_ newMember: SecTrustSettingsKeyUsage) -> (inserted: Bool, memberAfterInsert: SecTrustSettingsKeyUsage)     mutating func remove(_ member: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage?     mutating func update(with newMember: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage? } extension SecTrustSettingsKeyUsage {     convenience init()     mutating func formUnion(_ other: SecTrustSettingsKeyUsage)     mutating func formIntersection(_ other: SecTrustSettingsKeyUsage)     mutating func formSymmetricDifference(_ other: SecTrustSettingsKeyUsage) } extension SecTrustSettingsKeyUsage {     convenience init<S : Sequence where S.Iterator.Element == SecTrustSettingsKeyUsage>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecTrustSettingsKeyUsage...)     mutating func subtract(_ other: SecTrustSettingsKeyUsage)     func isSubset(of other: SecTrustSettingsKeyUsage) -> Bool     func isSuperset(of other: SecTrustSettingsKeyUsage) -> Bool     func isDisjoint(with other: SecTrustSettingsKeyUsage) -> Bool     func subtracting(_ other: SecTrustSettingsKeyUsage) -> SecTrustSettingsKeyUsage     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecTrustSettingsKeyUsage) -> Bool     func isStrictSubset(of other: SecTrustSettingsKeyUsage) -> Bool } ``` | OptionSet |

Modified [SecTrustSettingsKeyUsage.useAny](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/ksectrustsettingskeyuseany)

|  | Declaration |
| --- | --- |
| From | ``` static var UseAny: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useAny: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsKeyUsage.useEnDecryptData](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1394291-useendecryptdata)

|  | Declaration |
| --- | --- |
| From | ``` static var UseEnDecryptData: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useEnDecryptData: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsKeyUsage.useEnDecryptKey](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/ksectrustsettingskeyuseendecryptkey)

|  | Declaration |
| --- | --- |
| From | ``` static var UseEnDecryptKey: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useEnDecryptKey: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsKeyUsage.useKeyExchange](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1392796-usekeyexchange)

|  | Declaration |
| --- | --- |
| From | ``` static var UseKeyExchange: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useKeyExchange: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsKeyUsage.useSignature](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1392354-usesignature)

|  | Declaration |
| --- | --- |
| From | ``` static var UseSignature: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useSignature: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsKeyUsage.useSignCert](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/ksectrustsettingskeyusesigncert)

|  | Declaration |
| --- | --- |
| From | ``` static var UseSignCert: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useSignCert: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsKeyUsage.useSignRevocation](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/1400014-usesignrevocation)

|  | Declaration |
| --- | --- |
| From | ``` static var UseSignRevocation: SecTrustSettingsKeyUsage { get } ``` |
| To | ``` static var useSignRevocation: SecTrustSettingsKeyUsage { get } ``` |

Modified [SecTrustSettingsResult [enum]](https://developer.apple.com/documentation/security/sectrustsettingsresult)

|  | Declaration |
| --- | --- |
| From | ``` enum SecTrustSettingsResult : uint32 {     case Invalid     case TrustRoot     case TrustAsRoot     case Deny     case Unspecified } ``` |
| To | ``` enum SecTrustSettingsResult : uint32 {     case invalid     case trustRoot     case trustAsRoot     case deny     case unspecified } ``` |

Modified [SecTrustSettingsResult.deny](https://developer.apple.com/documentation/security/sectrustsettingsresult/deny)

|  | Declaration |
| --- | --- |
| From | ``` case Deny ``` |
| To | ``` case deny ``` |

Modified [SecTrustSettingsResult.invalid](https://developer.apple.com/documentation/security/sectrustsettingsresult/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [SecTrustSettingsResult.trustAsRoot](https://developer.apple.com/documentation/security/sectrustsettingsresult/ksectrustsettingsresulttrustasroot)

|  | Declaration |
| --- | --- |
| From | ``` case TrustAsRoot ``` |
| To | ``` case trustAsRoot ``` |

Modified [SecTrustSettingsResult.trustRoot](https://developer.apple.com/documentation/security/sectrustsettingsresult/ksectrustsettingsresulttrustroot)

|  | Declaration |
| --- | --- |
| From | ``` case TrustRoot ``` |
| To | ``` case trustRoot ``` |

Modified [SecTrustSettingsResult.unspecified](https://developer.apple.com/documentation/security/sectrustsettingsresult/unspecified)

|  | Declaration |
| --- | --- |
| From | ``` case Unspecified ``` |
| To | ``` case unspecified ``` |

Modified [SSLAuthenticate [enum]](https://developer.apple.com/documentation/security/sslauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLAuthenticate : Int32 {     case NeverAuthenticate     case AlwaysAuthenticate     case TryAuthenticate } ``` |
| To | ``` enum SSLAuthenticate : Int32 {     case neverAuthenticate     case alwaysAuthenticate     case tryAuthenticate } ``` |

Modified [SSLAuthenticate.alwaysAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/alwaysauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` case AlwaysAuthenticate ``` |
| To | ``` case alwaysAuthenticate ``` |

Modified [SSLAuthenticate.neverAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/neverauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` case NeverAuthenticate ``` |
| To | ``` case neverAuthenticate ``` |

Modified [SSLAuthenticate.tryAuthenticate](https://developer.apple.com/documentation/security/sslauthenticate/ktryauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` case TryAuthenticate ``` |
| To | ``` case tryAuthenticate ``` |

Modified [SSLClientCertificateState [enum]](https://developer.apple.com/documentation/security/sslclientcertificatestate)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLClientCertificateState : Int32 {     case CertNone     case CertRequested     case CertSent     case CertRejected } ``` |
| To | ``` enum SSLClientCertificateState : Int32 {     case certNone     case certRequested     case certSent     case certRejected } ``` |

Modified [SSLClientCertificateState.certNone](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertnone)

|  | Declaration |
| --- | --- |
| From | ``` case CertNone ``` |
| To | ``` case certNone ``` |

Modified [SSLClientCertificateState.certRejected](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertrejected)

|  | Declaration |
| --- | --- |
| From | ``` case CertRejected ``` |
| To | ``` case certRejected ``` |

Modified [SSLClientCertificateState.certRequested](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertrequested)

|  | Declaration |
| --- | --- |
| From | ``` case CertRequested ``` |
| To | ``` case certRequested ``` |

Modified [SSLClientCertificateState.certSent](https://developer.apple.com/documentation/security/sslclientcertificatestate/ksslclientcertsent)

|  | Declaration |
| --- | --- |
| From | ``` case CertSent ``` |
| To | ``` case certSent ``` |

Modified [SSLConnectionType [enum]](https://developer.apple.com/documentation/security/sslconnectiontype)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLConnectionType : Int32 {     case StreamType     case DatagramType } ``` |
| To | ``` enum SSLConnectionType : Int32 {     case streamType     case datagramType } ``` |

Modified [SSLConnectionType.datagramType](https://developer.apple.com/documentation/security/sslconnectiontype/datagramtype)

|  | Declaration |
| --- | --- |
| From | ``` case DatagramType ``` |
| To | ``` case datagramType ``` |

Modified [SSLConnectionType.streamType](https://developer.apple.com/documentation/security/sslconnectiontype/ksslstreamtype)

|  | Declaration |
| --- | --- |
| From | ``` case StreamType ``` |
| To | ``` case streamType ``` |

Modified [SSLProtocol [enum]](https://developer.apple.com/documentation/security/sslprotocol)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLProtocol : Int32 {     case SSLProtocolUnknown     case SSLProtocol3     case TLSProtocol1     case TLSProtocol11     case TLSProtocol12     case DTLSProtocol1     case SSLProtocol2     case SSLProtocol3Only     case TLSProtocol1Only     case SSLProtocolAll } ``` |
| To | ``` enum SSLProtocol : Int32 {     case sslProtocolUnknown     case sslProtocol3     case tlsProtocol1     case tlsProtocol11     case tlsProtocol12     case dtlsProtocol1     case sslProtocol2     case sslProtocol3Only     case tlsProtocol1Only     case sslProtocolAll } ``` |

Modified [SSLProtocol.dtlsProtocol1](https://developer.apple.com/documentation/security/sslprotocol/dtlsprotocol1)

|  | Declaration |
| --- | --- |
| From | ``` case DTLSProtocol1 ``` |
| To | ``` case dtlsProtocol1 ``` |

Modified [SSLProtocol.sslProtocol2](https://developer.apple.com/documentation/security/sslprotocol/ksslprotocol2)

|  | Declaration |
| --- | --- |
| From | ``` case SSLProtocol2 ``` |
| To | ``` case sslProtocol2 ``` |

Modified [SSLProtocol.sslProtocol3](https://developer.apple.com/documentation/security/sslprotocol/sslprotocol3)

|  | Declaration |
| --- | --- |
| From | ``` case SSLProtocol3 ``` |
| To | ``` case sslProtocol3 ``` |

Modified [SSLProtocol.sslProtocol3Only](https://developer.apple.com/documentation/security/sslprotocol/sslprotocol3only)

|  | Declaration |
| --- | --- |
| From | ``` case SSLProtocol3Only ``` |
| To | ``` case sslProtocol3Only ``` |

Modified [SSLProtocol.sslProtocolAll](https://developer.apple.com/documentation/security/sslprotocol/sslprotocolall)

|  | Declaration |
| --- | --- |
| From | ``` case SSLProtocolAll ``` |
| To | ``` case sslProtocolAll ``` |

Modified [SSLProtocol.sslProtocolUnknown](https://developer.apple.com/documentation/security/sslprotocol/sslprotocolunknown)

|  | Declaration |
| --- | --- |
| From | ``` case SSLProtocolUnknown ``` |
| To | ``` case sslProtocolUnknown ``` |

Modified [SSLProtocol.tlsProtocol1](https://developer.apple.com/documentation/security/sslprotocol/ktlsprotocol1)

|  | Declaration |
| --- | --- |
| From | ``` case TLSProtocol1 ``` |
| To | ``` case tlsProtocol1 ``` |

Modified [SSLProtocol.tlsProtocol11](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol11)

|  | Declaration |
| --- | --- |
| From | ``` case TLSProtocol11 ``` |
| To | ``` case tlsProtocol11 ``` |

Modified [SSLProtocol.tlsProtocol12](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol12)

|  | Declaration |
| --- | --- |
| From | ``` case TLSProtocol12 ``` |
| To | ``` case tlsProtocol12 ``` |

Modified [SSLProtocol.tlsProtocol1Only](https://developer.apple.com/documentation/security/sslprotocol/ktlsprotocol1only)

|  | Declaration |
| --- | --- |
| From | ``` case TLSProtocol1Only ``` |
| To | ``` case tlsProtocol1Only ``` |

Modified [SSLProtocolSide [enum]](https://developer.apple.com/documentation/security/sslprotocolside)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLProtocolSide : Int32 {     case ServerSide     case ClientSide } ``` |
| To | ``` enum SSLProtocolSide : Int32 {     case serverSide     case clientSide } ``` |

Modified [SSLProtocolSide.clientSide](https://developer.apple.com/documentation/security/sslprotocolside/ksslclientside)

|  | Declaration |
| --- | --- |
| From | ``` case ClientSide ``` |
| To | ``` case clientSide ``` |

Modified [SSLProtocolSide.serverSide](https://developer.apple.com/documentation/security/sslprotocolside/serverside)

|  | Declaration |
| --- | --- |
| From | ``` case ServerSide ``` |
| To | ``` case serverSide ``` |

Modified [SSLSessionOption [enum]](https://developer.apple.com/documentation/security/sslsessionoption)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLSessionOption : Int32 {     case BreakOnServerAuth     case BreakOnCertRequested     case BreakOnClientAuth     case FalseStart     case SendOneByteRecord     case AllowServerIdentityChange     case Fallback     case BreakOnClientHello } ``` |
| To | ``` enum SSLSessionOption : Int32 {     case breakOnServerAuth     case breakOnCertRequested     case breakOnClientAuth     case falseStart     case sendOneByteRecord     case allowServerIdentityChange     case fallback     case breakOnClientHello     case allowRenegotiation } ``` |

Modified [SSLSessionOption.allowServerIdentityChange](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionallowserveridentitychange)

|  | Declaration |
| --- | --- |
| From | ``` case AllowServerIdentityChange ``` |
| To | ``` case allowServerIdentityChange ``` |

Modified [SSLSessionOption.breakOnCertRequested](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakoncertrequested)

|  | Declaration |
| --- | --- |
| From | ``` case BreakOnCertRequested ``` |
| To | ``` case breakOnCertRequested ``` |

Modified [SSLSessionOption.breakOnClientAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclientauth)

|  | Declaration |
| --- | --- |
| From | ``` case BreakOnClientAuth ``` |
| To | ``` case breakOnClientAuth ``` |

Modified [SSLSessionOption.breakOnClientHello](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclienthello)

|  | Declaration |
| --- | --- |
| From | ``` case BreakOnClientHello ``` |
| To | ``` case breakOnClientHello ``` |

Modified [SSLSessionOption.breakOnServerAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonserverauth)

|  | Declaration |
| --- | --- |
| From | ``` case BreakOnServerAuth ``` |
| To | ``` case breakOnServerAuth ``` |

Modified [SSLSessionOption.fallback](https://developer.apple.com/documentation/security/sslsessionoption/fallback)

|  | Declaration |
| --- | --- |
| From | ``` case Fallback ``` |
| To | ``` case fallback ``` |

Modified [SSLSessionOption.falseStart](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionfalsestart)

|  | Declaration |
| --- | --- |
| From | ``` case FalseStart ``` |
| To | ``` case falseStart ``` |

Modified [SSLSessionOption.sendOneByteRecord](https://developer.apple.com/documentation/security/sslsessionoption/sendonebyterecord)

|  | Declaration |
| --- | --- |
| From | ``` case SendOneByteRecord ``` |
| To | ``` case sendOneByteRecord ``` |

Modified [SSLSessionState [enum]](https://developer.apple.com/documentation/security/sslsessionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum SSLSessionState : Int32 {     case Idle     case Handshake     case Connected     case Closed     case Aborted } ``` |
| To | ``` enum SSLSessionState : Int32 {     case idle     case handshake     case connected     case closed     case aborted } ``` |

Modified [SSLSessionState.aborted](https://developer.apple.com/documentation/security/sslsessionstate/ksslaborted)

|  | Declaration |
| --- | --- |
| From | ``` case Aborted ``` |
| To | ``` case aborted ``` |

Modified [SSLSessionState.closed](https://developer.apple.com/documentation/security/sslsessionstate/ksslclosed)

|  | Declaration |
| --- | --- |
| From | ``` case Closed ``` |
| To | ``` case closed ``` |

Modified [SSLSessionState.connected](https://developer.apple.com/documentation/security/sslsessionstate/connected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [SSLSessionState.handshake](https://developer.apple.com/documentation/security/sslsessionstate/ksslhandshake)

|  | Declaration |
| --- | --- |
| From | ``` case Handshake ``` |
| To | ``` case handshake ``` |

Modified [SSLSessionState.idle](https://developer.apple.com/documentation/security/sslsessionstate/ksslidle)

|  | Declaration |
| --- | --- |
| From | ``` case Idle ``` |
| To | ``` case idle ``` |

Modified x509_validity [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x509_validity {     var notBefore: CSSM_X509_TIME     var notAfter: CSSM_X509_TIME     init()     init(notBefore notBefore: CSSM_X509_TIME, notAfter notAfter: CSSM_X509_TIME) } ``` |
| To | ``` struct x509_validity {     var notBefore: cssm_x509_time     var notAfter: cssm_x509_time     init()     init(notBefore notBefore: cssm_x509_time, notAfter notAfter: cssm_x509_time) } ``` |

Modified x509_validity.init(notBefore: cssm_x509_time, notAfter: cssm_x509_time)

|  | Declaration |
| --- | --- |
| From | ``` init(notBefore notBefore: CSSM_X509_TIME, notAfter notAfter: CSSM_X509_TIME) ``` |
| To | ``` init(notBefore notBefore: cssm_x509_time, notAfter notAfter: cssm_x509_time) ``` |

Modified x509_validity.notAfter

|  | Declaration |
| --- | --- |
| From | ``` var notAfter: CSSM_X509_TIME ``` |
| To | ``` var notAfter: cssm_x509_time ``` |

Modified x509_validity.notBefore

|  | Declaration |
| --- | --- |
| From | ``` var notBefore: CSSM_X509_TIME ``` |
| To | ``` var notBefore: cssm_x509_time ``` |

Modified [AuthorizationAsyncCallback](https://developer.apple.com/documentation/security/authorizationasynccallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AuthorizationAsyncCallback = (OSStatus, UnsafeMutablePointer<AuthorizationRights>) -> Void ``` |
| To | ``` typealias AuthorizationAsyncCallback = (OSStatus, UnsafeMutablePointer<AuthorizationRights>?) -> Swift.Void ``` |

Modified [AuthorizationCopyInfo(_: AuthorizationRef, _: AuthorizationString?, _: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>?>) -> OSStatus](https://developer.apple.com/documentation/security/1397734-authorizationcopyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyInfo(_ authorization: AuthorizationRef, _ tag: AuthorizationString, _ info: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>>) -> OSStatus ``` |
| To | ``` func AuthorizationCopyInfo(_ authorization: AuthorizationRef, _ tag: AuthorizationString?, _ info: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>?>) -> OSStatus ``` |

Modified [AuthorizationCopyRights(_: AuthorizationRef, _: UnsafePointer<AuthorizationRights>, _: UnsafePointer<AuthorizationEnvironment>?, _: AuthorizationFlags, _: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>?) -> OSStatus](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyRights(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) -> OSStatus ``` |
| To | ``` func AuthorizationCopyRights(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>?, _ flags: AuthorizationFlags, _ authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>?) -> OSStatus ``` |

Modified [AuthorizationCopyRightsAsync(_: AuthorizationRef, _: UnsafePointer<AuthorizationRights>, _: UnsafePointer<AuthorizationEnvironment>?, _: AuthorizationFlags, _: Security.AuthorizationAsyncCallback)](https://developer.apple.com/documentation/security/1394914-authorizationcopyrightsasync)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCopyRightsAsync(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ callbackBlock: AuthorizationAsyncCallback) ``` |
| To | ``` func AuthorizationCopyRightsAsync(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>?, _ flags: AuthorizationFlags, _ callbackBlock: Security.AuthorizationAsyncCallback) ``` |

Modified [AuthorizationCreate(_: UnsafePointer<AuthorizationRights>?, _: UnsafePointer<AuthorizationEnvironment>?, _: AuthorizationFlags, _: UnsafeMutablePointer<AuthorizationRef?>?) -> OSStatus](https://developer.apple.com/documentation/security/1397453-authorizationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCreate(_ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>, _ flags: AuthorizationFlags, _ authorization: UnsafeMutablePointer<AuthorizationRef>) -> OSStatus ``` |
| To | ``` func AuthorizationCreate(_ rights: UnsafePointer<AuthorizationRights>?, _ environment: UnsafePointer<AuthorizationEnvironment>?, _ flags: AuthorizationFlags, _ authorization: UnsafeMutablePointer<AuthorizationRef?>?) -> OSStatus ``` |

Modified [AuthorizationCreateFromExternalForm(_: UnsafePointer<AuthorizationExternalForm>, _: UnsafeMutablePointer<AuthorizationRef?>) -> OSStatus](https://developer.apple.com/documentation/security/1400640-authorizationcreatefromexternalf)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationCreateFromExternalForm(_ extForm: UnsafePointer<AuthorizationExternalForm>, _ authorization: UnsafeMutablePointer<AuthorizationRef>) -> OSStatus ``` |
| To | ``` func AuthorizationCreateFromExternalForm(_ extForm: UnsafePointer<AuthorizationExternalForm>, _ authorization: UnsafeMutablePointer<AuthorizationRef?>) -> OSStatus ``` |

Modified [AuthorizationRef](https://developer.apple.com/documentation/systemconfiguration/authorizationref)

|  | Declaration |
| --- | --- |
| From | ``` typealias AuthorizationRef = COpaquePointer ``` |
| To | ``` typealias AuthorizationRef = OpaquePointer ``` |

Modified [AuthorizationRightGet(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus](https://developer.apple.com/documentation/security/1397961-authorizationrightget)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightGet(_ rightName: UnsafePointer<Int8>, _ rightDefinition: UnsafeMutablePointer<CFDictionary?>) -> OSStatus ``` |
| To | ``` func AuthorizationRightGet(_ rightName: UnsafePointer<Int8>, _ rightDefinition: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus ``` |

Modified [AuthorizationRightSet(_: AuthorizationRef, _: UnsafePointer<Int8>, _: CFTypeRef, _: CFString?, _: CFBundle?, _: CFString?) -> OSStatus](https://developer.apple.com/documentation/security/1399311-authorizationrightset)

|  | Declaration |
| --- | --- |
| From | ``` func AuthorizationRightSet(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<Int8>, _ rightDefinition: AnyObject, _ descriptionKey: CFString?, _ bundle: CFBundle?, _ localeTableName: CFString?) -> OSStatus ``` |
| To | ``` func AuthorizationRightSet(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<Int8>, _ rightDefinition: CFTypeRef, _ descriptionKey: CFString?, _ bundle: CFBundle?, _ localeTableName: CFString?) -> OSStatus ``` |

Modified [CMSDecoderCopySignerStatus(_: CMSDecoder, _: Int, _: CFTypeRef, _: Bool, _: UnsafeMutablePointer<CMSSignerStatus>?, _: UnsafeMutablePointer<SecTrust?>?, _: UnsafeMutablePointer<OSStatus>?) -> OSStatus](https://developer.apple.com/documentation/security/1396762-cmsdecodercopysignerstatus)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ policyOrArray: AnyObject, _ evaluateSecTrust: Bool, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>, _ secTrustOut: UnsafeMutablePointer<SecTrust?>, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ policyOrArray: CFTypeRef, _ evaluateSecTrust: Bool, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>?, _ secTrustOut: UnsafeMutablePointer<SecTrust?>?, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>?) -> OSStatus ``` |

Modified [CMSDecoderCopySignerTimestampWithPolicy(_: CMSDecoder, _: CFTypeRef?, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1395908-cmsdecodercopysignertimestampwit)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderCopySignerTimestampWithPolicy(_ cmsDecoder: CMSDecoder, _ timeStampPolicy: AnyObject?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSDecoderCopySignerTimestampWithPolicy(_ cmsDecoder: CMSDecoder, _ timeStampPolicy: CFTypeRef?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSDecoderSetSearchKeychain(_: CMSDecoder, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/security/1392933-cmsdecodersetsearchkeychain)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder, _ keychainOrArray: AnyObject) -> OSStatus ``` |
| To | ``` func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder, _ keychainOrArray: CFTypeRef) -> OSStatus ``` |

Modified [CMSDecoderUpdateMessage(_: CMSDecoder, _: UnsafeRawPointer, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1393876-cmsdecoderupdatemessage)

|  | Declaration |
| --- | --- |
| From | ``` func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder, _ msgBytes: UnsafePointer<Void>, _ msgBytesLen: Int) -> OSStatus ``` |
| To | ``` func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder, _ msgBytes: UnsafeRawPointer, _ msgBytesLen: Int) -> OSStatus ``` |

Modified [CMSEncode(_: CFTypeRef?, _: CFTypeRef?, _: UnsafePointer<CSSM_OID>?, _: Bool, _: CMSSignedAttributes, _: UnsafeRawPointer, _: Int, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1387147-cmsencode)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncode(_ signers: AnyObject?, _ recipients: AnyObject?, _ eContentType: UnsafePointer<CSSM_OID>, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |
| To | ``` func CMSEncode(_ signers: CFTypeRef?, _ recipients: CFTypeRef?, _ eContentType: UnsafePointer<CSSM_OID>?, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafeRawPointer, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMSEncodeContent(_: CFTypeRef?, _: CFTypeRef?, _: CFTypeRef?, _: Bool, _: CMSSignedAttributes, _: UnsafeRawPointer, _: Int, _: UnsafeMutablePointer<CFData?>?) -> OSStatus](https://developer.apple.com/documentation/security/1387113-cmsencodecontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncodeContent(_ signers: AnyObject?, _ recipients: AnyObject?, _ eContentTypeOID: AnyObject?, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafePointer<Void>, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |
| To | ``` func CMSEncodeContent(_ signers: CFTypeRef?, _ recipients: CFTypeRef?, _ eContentTypeOID: CFTypeRef?, _ detachedContent: Bool, _ signedAttributes: CMSSignedAttributes, _ content: UnsafeRawPointer, _ contentLen: Int, _ encodedContentOut: UnsafeMutablePointer<CFData?>?) -> OSStatus ``` |

Modified [CMSEncoderAddRecipients(_: CMSEncoder, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/security/1387129-cmsencoderaddrecipients)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder, _ recipientOrArray: AnyObject) -> OSStatus ``` |
| To | ``` func CMSEncoderAddRecipients(_ cmsEncoder: CMSEncoder, _ recipientOrArray: CFTypeRef) -> OSStatus ``` |

Modified [CMSEncoderAddSigners(_: CMSEncoder, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/security/1387177-cmsencoderaddsigners)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder, _ signerOrArray: AnyObject) -> OSStatus ``` |
| To | ``` func CMSEncoderAddSigners(_ cmsEncoder: CMSEncoder, _ signerOrArray: CFTypeRef) -> OSStatus ``` |

Modified [CMSEncoderAddSupportingCerts(_: CMSEncoder, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/security/1387168-cmsencoderaddsupportingcerts)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderAddSupportingCerts(_ cmsEncoder: CMSEncoder, _ certOrArray: AnyObject) -> OSStatus ``` |
| To | ``` func CMSEncoderAddSupportingCerts(_ cmsEncoder: CMSEncoder, _ certOrArray: CFTypeRef) -> OSStatus ``` |

Modified [CMSEncoderCopySignerTimestampWithPolicy(_: CMSEncoder, _: CFTypeRef?, _: Int, _: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](https://developer.apple.com/documentation/security/1387162-cmsencodercopysignertimestampwit)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderCopySignerTimestampWithPolicy(_ cmsEncoder: CMSEncoder, _ timeStampPolicy: AnyObject?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |
| To | ``` func CMSEncoderCopySignerTimestampWithPolicy(_ cmsEncoder: CMSEncoder, _ timeStampPolicy: CFTypeRef?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus ``` |

Modified [CMSEncoderSetEncapsulatedContentTypeOID(_: CMSEncoder, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/security/1387115-cmsencodersetencapsulatedcontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderSetEncapsulatedContentTypeOID(_ cmsEncoder: CMSEncoder, _ eContentTypeOID: AnyObject) -> OSStatus ``` |
| To | ``` func CMSEncoderSetEncapsulatedContentTypeOID(_ cmsEncoder: CMSEncoder, _ eContentTypeOID: CFTypeRef) -> OSStatus ``` |

Modified [CMSEncoderUpdateContent(_: CMSEncoder, _: UnsafeRawPointer, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1387141-cmsencoderupdatecontent)

|  | Declaration |
| --- | --- |
| From | ``` func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder, _ content: UnsafePointer<Void>, _ contentLen: Int) -> OSStatus ``` |
| To | ``` func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder, _ content: UnsafeRawPointer, _ contentLen: Int) -> OSStatus ``` |

Modified CSSM_ACL_SUBJECT_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_ACL_SUBJECT_CALLBACK = (UnsafePointer<CSSM_LIST>, CSSM_LIST_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN ``` |
| To | ``` typealias CSSM_ACL_SUBJECT_CALLBACK = (UnsafePointer<cssm_list>?, UnsafeMutablePointer<cssm_list>?, UnsafeMutableRawPointer?, UnsafePointer<cssm_memory_funcs>?) -> CSSM_RETURN ``` |

Modified CSSM_API_MEMORY_FUNCS

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_API_MEMORY_FUNCS = CSSM_MEMORY_FUNCS ``` |
| To | ``` typealias CSSM_API_MEMORY_FUNCS = cssm_memory_funcs ``` |

Modified CSSM_API_ModuleEventHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_API_ModuleEventHandler = (UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN ``` |
| To | ``` typealias CSSM_API_ModuleEventHandler = (UnsafePointer<cssm_guid>?, UnsafeMutableRawPointer?, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN ``` |

Modified CSSM_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CALLBACK = (CSSM_DATA_PTR, UnsafeMutablePointer<Void>) -> CSSM_RETURN ``` |
| To | ``` typealias CSSM_CALLBACK = (UnsafeMutablePointer<cssm_data>?, UnsafeMutableRawPointer?) -> CSSM_RETURN ``` |

Modified CSSM_CALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CALLOC = (uint32, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_CALLOC = (uint32, CSSM_SIZE, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer? ``` |

Modified CSSM_CHALLENGE_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_CHALLENGE_CALLBACK = (UnsafePointer<CSSM_LIST>, CSSM_SAMPLEGROUP_PTR, UnsafeMutablePointer<Void>, UnsafePointer<CSSM_MEMORY_FUNCS>) -> CSSM_RETURN ``` |
| To | ``` typealias CSSM_CHALLENGE_CALLBACK = (UnsafePointer<cssm_list>?, UnsafeMutablePointer<cssm_samplegroup>?, UnsafeMutableRawPointer?, UnsafePointer<cssm_memory_funcs>?) -> CSSM_RETURN ``` |

Modified CSSM_DL_CUSTOM_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_CUSTOM_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_DL_CUSTOM_ATTRIBUTES = UnsafeMutableRawPointer ``` |

Modified CSSM_DL_FFS_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_FFS_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_DL_FFS_ATTRIBUTES = UnsafeMutableRawPointer ``` |

Modified CSSM_DL_LDAP_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_LDAP_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_DL_LDAP_ATTRIBUTES = UnsafeMutableRawPointer ``` |

Modified CSSM_DL_ODBC_ATTRIBUTES

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_DL_ODBC_ATTRIBUTES = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_DL_ODBC_ATTRIBUTES = UnsafeMutableRawPointer ``` |

Modified CSSM_FREE

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_FREE = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CSSM_FREE = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified CSSM_MALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_MALLOC = (CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_MALLOC = (CSSM_SIZE, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer? ``` |

Modified CSSM_OID

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_OID = CSSM_DATA ``` |
| To | ``` typealias CSSM_OID = cssm_data ``` |

Modified CSSM_OID_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_OID_PTR = UnsafeMutablePointer<CSSM_DATA> ``` |
| To | ``` typealias CSSM_OID_PTR = UnsafeMutablePointer<cssm_data> ``` |

Modified CSSM_PROC_ADDR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_PROC_ADDR = () -> Void ``` |
| To | ``` typealias CSSM_PROC_ADDR = () -> Swift.Void ``` |

Modified CSSM_PROC_ADDR_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_PROC_ADDR_PTR = UnsafeMutablePointer<CSSM_PROC_ADDR?> ``` |
| To | ``` typealias CSSM_PROC_ADDR_PTR = UnsafeMutablePointer<Security.CSSM_PROC_ADDR?> ``` |

Modified CSSM_REALLOC

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_REALLOC = (UnsafeMutablePointer<Void>, CSSM_SIZE, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` typealias CSSM_REALLOC = (UnsafeMutableRawPointer?, CSSM_SIZE, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer? ``` |

Modified CSSM_SPI_ModuleEventHandler

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_SPI_ModuleEventHandler = (UnsafePointer<CSSM_GUID>, UnsafeMutablePointer<Void>, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN ``` |
| To | ``` typealias CSSM_SPI_ModuleEventHandler = (UnsafePointer<cssm_guid>?, UnsafeMutableRawPointer?, uint32, CSSM_SERVICE_TYPE, CSSM_MODULE_EVENT) -> CSSM_RETURN ``` |

Modified CSSM_TP_VERIFICATION_RESULTS_CALLBACK

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_TP_VERIFICATION_RESULTS_CALLBACK = (CSSM_MODULE_HANDLE, UnsafeMutablePointer<Void>, CSSM_DATA_PTR) -> CSSM_RETURN ``` |
| To | ``` typealias CSSM_TP_VERIFICATION_RESULTS_CALLBACK = (CSSM_MODULE_HANDLE, UnsafeMutableRawPointer?, UnsafeMutablePointer<cssm_data>?) -> CSSM_RETURN ``` |

Modified CSSM_WRAP_KEY

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_WRAP_KEY = CSSM_KEY ``` |
| To | ``` typealias CSSM_WRAP_KEY = cssm_key ``` |

Modified CSSM_WRAP_KEY_PTR

|  | Declaration |
| --- | --- |
| From | ``` typealias CSSM_WRAP_KEY_PTR = UnsafeMutablePointer<CSSM_KEY> ``` |
| To | ``` typealias CSSM_WRAP_KEY_PTR = UnsafeMutablePointer<cssm_key> ``` |

Modified cssmAlgToOid(_: CSSM_ALGORITHMS) -> UnsafePointer<CSSM_OID>!

|  | Declaration |
| --- | --- |
| From | ``` func cssmAlgToOid(_ algId: CSSM_ALGORITHMS) -> UnsafePointer<CSSM_OID> ``` |
| To | ``` func cssmAlgToOid(_ algId: CSSM_ALGORITHMS) -> UnsafePointer<CSSM_OID>! ``` |

Modified cssmOidToAlg(_: UnsafePointer<CSSM_OID>!, _: UnsafeMutablePointer<CSSM_ALGORITHMS>!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func cssmOidToAlg(_ oid: UnsafePointer<CSSM_OID>, _ alg: UnsafeMutablePointer<CSSM_ALGORITHMS>) -> Bool ``` |
| To | ``` func cssmOidToAlg(_ oid: UnsafePointer<CSSM_OID>!, _ alg: UnsafeMutablePointer<CSSM_ALGORITHMS>!) -> Bool ``` |

Modified cssmPerror(_: UnsafePointer<Int8>!, _: CSSM_RETURN)

|  | Declaration |
| --- | --- |
| From | ``` func cssmPerror(_ how: UnsafePointer<Int8>, _ error: CSSM_RETURN) ``` |
| To | ``` func cssmPerror(_ how: UnsafePointer<Int8>!, _ error: CSSM_RETURN) ``` |

Modified gGuidAppleCSP

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleCSP: CSSM_GUID ``` |
| To | ``` let gGuidAppleCSP: cssm_guid ``` |

Modified gGuidAppleCSPDL

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleCSPDL: CSSM_GUID ``` |
| To | ``` let gGuidAppleCSPDL: cssm_guid ``` |

Modified gGuidAppleDotMacDL

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleDotMacDL: CSSM_GUID ``` |
| To | ``` let gGuidAppleDotMacDL: cssm_guid ``` |

Modified gGuidAppleDotMacTP

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleDotMacTP: CSSM_GUID ``` |
| To | ``` let gGuidAppleDotMacTP: cssm_guid ``` |

Modified gGuidAppleFileDL

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleFileDL: CSSM_GUID ``` |
| To | ``` let gGuidAppleFileDL: cssm_guid ``` |

Modified gGuidAppleLDAPDL

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleLDAPDL: CSSM_GUID ``` |
| To | ``` let gGuidAppleLDAPDL: cssm_guid ``` |

Modified gGuidAppleSdCSPDL

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleSdCSPDL: CSSM_GUID ``` |
| To | ``` let gGuidAppleSdCSPDL: cssm_guid ``` |

Modified gGuidAppleX509CL

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleX509CL: CSSM_GUID ``` |
| To | ``` let gGuidAppleX509CL: cssm_guid ``` |

Modified gGuidAppleX509TP

|  | Declaration |
| --- | --- |
| From | ``` let gGuidAppleX509TP: CSSM_GUID ``` |
| To | ``` let gGuidAppleX509TP: cssm_guid ``` |

Modified gGuidCssm

|  | Declaration |
| --- | --- |
| From | ``` let gGuidCssm: CSSM_GUID ``` |
| To | ``` let gGuidCssm: cssm_guid ``` |

Modified [kAuthorizationExternalFormLength](https://developer.apple.com/documentation/security/kauthorizationexternalformlength)

|  | Declaration |
| --- | --- |
| From | ``` var kAuthorizationExternalFormLength: Int { get } ``` |
| To | ``` let kAuthorizationExternalFormLength: Int ``` |

Modified [kSecRevocationCRLMethod](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationcrlmethod)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationCRLMethod: Int { get } ``` |
| To | ``` var kSecRevocationCRLMethod: CFOptionFlags { get } ``` |

Modified [kSecRevocationNetworkAccessDisabled](https://developer.apple.com/documentation/security/ksecrevocationnetworkaccessdisabled)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationNetworkAccessDisabled: Int { get } ``` |
| To | ``` var kSecRevocationNetworkAccessDisabled: CFOptionFlags { get } ``` |

Modified [kSecRevocationOCSPMethod](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationocspmethod)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationOCSPMethod: Int { get } ``` |
| To | ``` var kSecRevocationOCSPMethod: CFOptionFlags { get } ``` |

Modified [kSecRevocationPreferCRL](https://developer.apple.com/documentation/security/ksecrevocationprefercrl)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationPreferCRL: Int { get } ``` |
| To | ``` var kSecRevocationPreferCRL: CFOptionFlags { get } ``` |

Modified [kSecRevocationRequirePositiveResponse](https://developer.apple.com/documentation/security/ksecrevocationrequirepositiveresponse)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationRequirePositiveResponse: Int { get } ``` |
| To | ``` var kSecRevocationRequirePositiveResponse: CFOptionFlags { get } ``` |

Modified [kSecRevocationUseAnyAvailableMethod](https://developer.apple.com/documentation/security/ksecrevocationuseanyavailablemethod)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationUseAnyAvailableMethod: Int { get } ``` |
| To | ``` var kSecRevocationUseAnyAvailableMethod: CFOptionFlags { get } ``` |

Modified MDS_DB_HANDLE

|  | Declaration |
| --- | --- |
| From | ``` typealias MDS_DB_HANDLE = CSSM_DL_DB_HANDLE ``` |
| To | ``` typealias MDS_DB_HANDLE = cssm_dl_db_handle ``` |

Modified [SecAccessControlCreateWithFlags(_: CFAllocator?, _: CFTypeRef, _: SecAccessControlCreateFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl?](https://developer.apple.com/documentation/security/1394452-secaccesscontrolcreatewithflags)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: AnyObject, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccessControl? ``` |
| To | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: CFTypeRef, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl? ``` |

Modified [SecAccessCopyMatchingACLList(_: SecAccess, _: CFTypeRef) -> CFArray?](https://developer.apple.com/documentation/security/1400464-secaccesscopymatchingacllist)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCopyMatchingACLList(_ accessRef: SecAccess, _ authorizationTag: AnyObject) -> CFArray? ``` |
| To | ``` func SecAccessCopyMatchingACLList(_ accessRef: SecAccess, _ authorizationTag: CFTypeRef) -> CFArray? ``` |

Modified [SecAccessCopyOwnerAndACL(_: SecAccess, _: UnsafeMutablePointer<uid_t>?, _: UnsafeMutablePointer<gid_t>?, _: UnsafeMutablePointer<SecAccessOwnerType>?, _: UnsafeMutablePointer<CFArray?>?) -> OSStatus](https://developer.apple.com/documentation/security/1402089-secaccesscopyownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess, _ userId: UnsafeMutablePointer<uid_t>, _ groupId: UnsafeMutablePointer<gid_t>, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>, _ aclList: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |
| To | ``` func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess, _ userId: UnsafeMutablePointer<uid_t>?, _ groupId: UnsafeMutablePointer<gid_t>?, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>?, _ aclList: UnsafeMutablePointer<CFArray?>?) -> OSStatus ``` |

Modified [SecAccessCreateWithOwnerAndACL(_: uid_t, _: gid_t, _: SecAccessOwnerType, _: CFArray?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccess?](https://developer.apple.com/documentation/security/1395706-secaccesscreatewithownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccess? ``` |
| To | ``` func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccess? ``` |

Modified [SecAsn1AlgId](https://developer.apple.com/documentation/security/secasn1algid)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1AlgId = CSSM_X509_ALGORITHM_IDENTIFIER ``` |
| To | ``` typealias SecAsn1AlgId = cssm_x509_algorithm_identifier ``` |

Modified [SecAsn1Item](https://developer.apple.com/documentation/security/secasn1item)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1Item = CSSM_DATA ``` |
| To | ``` typealias SecAsn1Item = cssm_data ``` |

Modified [SecAsn1PubKeyInfo](https://developer.apple.com/documentation/security/secasn1pubkeyinfo)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1PubKeyInfo = CSSM_X509_SUBJECT_PUBLIC_KEY_INFO ``` |
| To | ``` typealias SecAsn1PubKeyInfo = cssm_x509_subject_public_key_info ``` |

Modified [SecAsn1TemplateChooser](https://developer.apple.com/documentation/security/secasn1templatechooser)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1TemplateChooser = (UnsafeMutablePointer<Void>, DarwinBoolean, UnsafePointer<Int8>, Int, UnsafeMutablePointer<Void>) -> UnsafePointer<SecAsn1Template> ``` |
| To | ``` typealias SecAsn1TemplateChooser = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<Int8>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>? ``` |

Modified [SecAsn1TemplateChooserPtr](https://developer.apple.com/documentation/security/secasn1templatechooserptr)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecAsn1TemplateChooserPtr = (UnsafeMutablePointer<Void>, DarwinBoolean, UnsafePointer<Int8>, Int, UnsafeMutablePointer<Void>) -> UnsafePointer<SecAsn1Template> ``` |
| To | ``` typealias SecAsn1TemplateChooserPtr = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<Int8>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>? ``` |

Modified [SecCertificateCopyLongDescription(_: CFAllocator?, _: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?](https://developer.apple.com/documentation/security/1396088-seccertificatecopylongdescriptio)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyLongDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFString? ``` |
| To | ``` func SecCertificateCopyLongDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString? ``` |

Modified [SecCertificateCopyNormalizedIssuerContent(_: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1392318-seccertificatecopynormalizedissu)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |
| To | ``` func SecCertificateCopyNormalizedIssuerContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData? ``` |

Modified [SecCertificateCopyNormalizedSubjectContent(_: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1396030-seccertificatecopynormalizedsubj)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |
| To | ``` func SecCertificateCopyNormalizedSubjectContent(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData? ``` |

Modified [SecCertificateCopySerialNumber(_: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1394241-seccertificatecopyserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopySerialNumber(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |
| To | ``` func SecCertificateCopySerialNumber(_ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData? ``` |

Modified [SecCertificateCopyShortDescription(_: CFAllocator?, _: SecCertificate, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?](https://developer.apple.com/documentation/security/1396036-seccertificatecopyshortdescripti)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyShortDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFString? ``` |
| To | ``` func SecCertificateCopyShortDescription(_ alloc: CFAllocator?, _ certificate: SecCertificate, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString? ``` |

Modified [SecCertificateCopyValues(_: SecCertificate, _: CFArray?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?](https://developer.apple.com/documentation/security/1396051-seccertificatecopyvalues)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyValues(_ certificate: SecCertificate, _ keys: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary? ``` |
| To | ``` func SecCertificateCopyValues(_ certificate: SecCertificate, _ keys: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary? ``` |

Modified [SecCodeCheckValidityWithErrors(_: SecCode, _: SecCSFlags, _: SecRequirement?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus](https://developer.apple.com/documentation/security/1395272-seccodecheckvaliditywitherrors)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCheckValidityWithErrors(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |
| To | ``` func SecCodeCheckValidityWithErrors(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus ``` |

Modified [SecCopyErrorMessageString(_: OSStatus, _: UnsafeMutableRawPointer?) -> CFString?](https://developer.apple.com/documentation/security/1394686-seccopyerrormessagestring)

|  | Declaration |
| --- | --- |
| From | ``` func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutablePointer<Void>) -> CFString? ``` |
| To | ``` func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutableRawPointer?) -> CFString? ``` |

Modified [SecDecodeTransformCreate(_: CFTypeRef, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](https://developer.apple.com/documentation/security/1395244-secdecodetransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecDecodeTransformCreate(_ DecodeType: AnyObject, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |
| To | ``` func SecDecodeTransformCreate(_ DecodeType: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform? ``` |

Modified [SecDecryptTransformCreate(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform](https://developer.apple.com/documentation/security/1399526-secdecrypttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecDecryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform ``` |
| To | ``` func SecDecryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform ``` |

Modified [SecDigestTransformCreate(_: CFTypeRef?, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform](https://developer.apple.com/documentation/security/1394846-secdigesttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecDigestTransformCreate(_ digestType: AnyObject?, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform ``` |
| To | ``` func SecDigestTransformCreate(_ digestType: CFTypeRef?, _ digestLength: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform ``` |

Modified [SecEncodeTransformCreate(_: CFTypeRef, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](https://developer.apple.com/documentation/security/1399382-secencodetransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecEncodeTransformCreate(_ encodeType: AnyObject, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |
| To | ``` func SecEncodeTransformCreate(_ encodeType: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform? ``` |

Modified [SecEncryptTransformCreate(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform](https://developer.apple.com/documentation/security/1399605-secencrypttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecEncryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform ``` |
| To | ``` func SecEncryptTransformCreate(_ keyRef: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform ``` |

Modified [SecIdentityCopySystemIdentity(_: CFString, _: UnsafeMutablePointer<SecIdentity?>, _: UnsafeMutablePointer<CFString?>?) -> OSStatus](https://developer.apple.com/documentation/security/1393646-secidentitycopysystemidentity)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopySystemIdentity(_ domain: CFString, _ idRef: UnsafeMutablePointer<SecIdentity?>, _ actualDomain: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |
| To | ``` func SecIdentityCopySystemIdentity(_ domain: CFString, _ idRef: UnsafeMutablePointer<SecIdentity?>, _ actualDomain: UnsafeMutablePointer<CFString?>?) -> OSStatus ``` |

Modified [SecIdentityCreateWithCertificate(_: CFTypeRef?, _: SecCertificate, _: UnsafeMutablePointer<SecIdentity?>) -> OSStatus](https://developer.apple.com/documentation/security/1401160-secidentitycreatewithcertificate)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCreateWithCertificate(_ keychainOrArray: AnyObject?, _ certificateRef: SecCertificate, _ identityRef: UnsafeMutablePointer<SecIdentity?>) -> OSStatus ``` |
| To | ``` func SecIdentityCreateWithCertificate(_ keychainOrArray: CFTypeRef?, _ certificateRef: SecCertificate, _ identityRef: UnsafeMutablePointer<SecIdentity?>) -> OSStatus ``` |

Modified [SecItemAdd(_: CFDictionary, _: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus](https://developer.apple.com/documentation/security/1401659-secitemadd)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemAdd(_ attributes: CFDictionary, _ result: UnsafeMutablePointer<AnyObject?>) -> OSStatus ``` |
| To | ``` func SecItemAdd(_ attributes: CFDictionary, _ result: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus ``` |

Modified [SecItemCopyMatching(_: CFDictionary, _: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus](https://developer.apple.com/documentation/security/1398306-secitemcopymatching)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemCopyMatching(_ query: CFDictionary, _ result: UnsafeMutablePointer<AnyObject?>) -> OSStatus ``` |
| To | ``` func SecItemCopyMatching(_ query: CFDictionary, _ result: UnsafeMutablePointer<CFTypeRef?>?) -> OSStatus ``` |

Modified [SecItemExport(_: CFTypeRef, _: SecExternalFormat, _: SecItemImportExportFlags, _: UnsafePointer<SecItemImportExportKeyParameters>?, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/security/1394828-secitemexport)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemExport(_ secItemOrArray: AnyObject, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ exportedData: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |
| To | ``` func SecItemExport(_ secItemOrArray: CFTypeRef, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>?, _ exportedData: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [SecItemImport(_: CFData, _: CFString?, _: UnsafeMutablePointer<SecExternalFormat>?, _: UnsafeMutablePointer<SecExternalItemType>?, _: SecItemImportExportFlags, _: UnsafePointer<SecItemImportExportKeyParameters>?, _: SecKeychain?, _: UnsafeMutablePointer<CFArray?>?) -> OSStatus](https://developer.apple.com/documentation/security/1395728-secitemimport)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemImport(_ importedData: CFData, _ fileNameOrExtension: CFString?, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>, _ itemType: UnsafeMutablePointer<SecExternalItemType>, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>, _ importKeychain: SecKeychain?, _ outItems: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |
| To | ``` func SecItemImport(_ importedData: CFData, _ fileNameOrExtension: CFString?, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>?, _ itemType: UnsafeMutablePointer<SecExternalItemType>?, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>?, _ importKeychain: SecKeychain?, _ outItems: UnsafeMutablePointer<CFArray?>?) -> OSStatus ``` |

Modified [SecKeychainAddCallback(_: Security.SecKeychainCallback, _: SecKeychainEventMask, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/security/1394998-seckeychainaddcallback)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddCallback(_ callbackFunction: SecKeychainCallback, _ eventMask: SecKeychainEventMask, _ userContext: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainAddCallback(_ callbackFunction: Security.SecKeychainCallback, _ eventMask: SecKeychainEventMask, _ userContext: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [SecKeychainAddGenericPassword(_: SecKeychain?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafeRawPointer, _: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](https://developer.apple.com/documentation/security/1398366-seckeychainaddgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddGenericPassword(_ keychain: SecKeychain?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddGenericPassword(_ keychain: SecKeychain?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>?, _ passwordLength: UInt32, _ passwordData: UnsafeRawPointer, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus ``` |

Modified [SecKeychainAddInternetPassword(_: SecKeychain?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt16, _: SecProtocolType, _: SecAuthenticationType, _: UInt32, _: UnsafeRawPointer, _: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](https://developer.apple.com/documentation/security/1393322-seckeychainaddinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>?, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>?, _ pathLength: UInt32, _ path: UnsafePointer<Int8>?, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafeRawPointer, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus ``` |

Modified [SecKeychainAttributeInfoForItemID(_: SecKeychain?, _: UInt32, _: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>?>) -> OSStatus](https://developer.apple.com/documentation/security/1392372-seckeychainattributeinfoforitemi)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain?, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>>) -> OSStatus ``` |
| To | ``` func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain?, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>?>) -> OSStatus ``` |

Modified [SecKeychainCallback](https://developer.apple.com/documentation/security/seckeychaincallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecKeychainCallback = (SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias SecKeychainCallback = (SecKeychainEvent, UnsafeMutablePointer<SecKeychainCallbackInfo>, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [SecKeychainCreate(_: UnsafePointer<Int8>, _: UInt32, _: UnsafeRawPointer?, _: Bool, _: SecAccess?, _: UnsafeMutablePointer<SecKeychain?>) -> OSStatus](https://developer.apple.com/documentation/security/1401214-seckeychaincreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainCreate(_ pathName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ promptUser: Bool, _ initialAccess: SecAccess?, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |
| To | ``` func SecKeychainCreate(_ pathName: UnsafePointer<Int8>, _ passwordLength: UInt32, _ password: UnsafeRawPointer?, _ promptUser: Bool, _ initialAccess: SecAccess?, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus ``` |

Modified [SecKeychainFindGenericPassword(_: CFTypeRef?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](https://developer.apple.com/documentation/security/1397301-seckeychainfindgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindGenericPassword(_ keychainOrArray: AnyObject?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindGenericPassword(_ keychainOrArray: CFTypeRef?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<Int8>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>?, _ passwordLength: UnsafeMutablePointer<UInt32>?, _ passwordData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus ``` |

Modified [SecKeychainFindInternetPassword(_: CFTypeRef?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt32, _: UnsafePointer<Int8>?, _: UInt16, _: SecProtocolType, _: SecAuthenticationType, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](https://developer.apple.com/documentation/security/1397763-seckeychainfindinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: CFTypeRef?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>?, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>?, _ pathLength: UInt32, _ path: UnsafePointer<Int8>?, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>?, _ passwordData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus ``` |

Modified [SecKeychainItemCopyAttributesAndData(_: SecKeychainItem, _: UnsafeMutablePointer<SecKeychainAttributeInfo>?, _: UnsafeMutablePointer<SecItemClass>?, _: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>?>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus](https://developer.apple.com/documentation/security/1400528-seckeychainitemcopyattributesand)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyAttributesAndData(_ itemRef: SecKeychainItem, _ info: UnsafeMutablePointer<SecKeychainAttributeInfo>?, _ itemClass: UnsafeMutablePointer<SecItemClass>?, _ attrList: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeList>?>?, _ length: UnsafeMutablePointer<UInt32>?, _ outData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus ``` |

Modified [SecKeychainItemCopyContent(_: SecKeychainItem, _: UnsafeMutablePointer<SecItemClass>?, _: UnsafeMutablePointer<SecKeychainAttributeList>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus](https://developer.apple.com/documentation/security/1401412-seckeychainitemcopycontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem, _ itemClass: UnsafeMutablePointer<SecItemClass>, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCopyContent(_ itemRef: SecKeychainItem, _ itemClass: UnsafeMutablePointer<SecItemClass>?, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ length: UnsafeMutablePointer<UInt32>?, _ outData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> OSStatus ``` |

Modified [SecKeychainItemCreateCopy(_: SecKeychainItem, _: SecKeychain?, _: SecAccess?, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1396024-seckeychainitemcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem, _ destKeychainRef: SecKeychain?, _ initialAccess: SecAccess, _ itemCopy: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreateCopy(_ itemRef: SecKeychainItem, _ destKeychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemCopy: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainItemCreateFromContent(_: SecItemClass, _: UnsafeMutablePointer<SecKeychainAttributeList>, _: UInt32, _: UnsafeRawPointer?, _: SecKeychain?, _: SecAccess?, _: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus](https://developer.apple.com/documentation/security/1393225-seckeychainitemcreatefromcontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>, _ keychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainItemCreateFromContent(_ itemClass: SecItemClass, _ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafeRawPointer?, _ keychainRef: SecKeychain?, _ initialAccess: SecAccess?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus ``` |

Modified [SecKeychainItemFreeAttributesAndData(_: UnsafeMutablePointer<SecKeychainAttributeList>?, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/security/1397736-seckeychainitemfreeattributesand)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemFreeAttributesAndData(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ data: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainItemFreeAttributesAndData(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ data: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [SecKeychainItemFreeContent(_: UnsafeMutablePointer<SecKeychainAttributeList>?, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/security/1402019-seckeychainitemfreecontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemFreeContent(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>, _ data: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainItemFreeContent(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ data: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [SecKeychainItemModifyAttributesAndData(_: SecKeychainItem, _: UnsafePointer<SecKeychainAttributeList>?, _: UInt32, _: UnsafeRawPointer?) -> OSStatus](https://developer.apple.com/documentation/security/1399963-seckeychainitemmodifyattributesa)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainItemModifyAttributesAndData(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>?, _ length: UInt32, _ data: UnsafeRawPointer?) -> OSStatus ``` |

Modified [SecKeychainItemModifyContent(_: SecKeychainItem, _: UnsafePointer<SecKeychainAttributeList>?, _: UInt32, _: UnsafeRawPointer?) -> OSStatus](https://developer.apple.com/documentation/security/1397154-seckeychainitemmodifycontent)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>, _ length: UInt32, _ data: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func SecKeychainItemModifyContent(_ itemRef: SecKeychainItem, _ attrList: UnsafePointer<SecKeychainAttributeList>?, _ length: UInt32, _ data: UnsafeRawPointer?) -> OSStatus ``` |

Modified [SecKeychainRemoveCallback(_: Security.SecKeychainCallback) -> OSStatus](https://developer.apple.com/documentation/security/1398240-seckeychainremovecallback)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainRemoveCallback(_ callbackFunction: SecKeychainCallback) -> OSStatus ``` |
| To | ``` func SecKeychainRemoveCallback(_ callbackFunction: Security.SecKeychainCallback) -> OSStatus ``` |

Modified [SecKeychainUnlock(_: SecKeychain?, _: UInt32, _: UnsafeRawPointer?, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1400341-seckeychainunlock)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainUnlock(_ keychain: SecKeychain?, _ passwordLength: UInt32, _ password: UnsafePointer<Void>, _ usePassword: Bool) -> OSStatus ``` |
| To | ``` func SecKeychainUnlock(_ keychain: SecKeychain?, _ passwordLength: UInt32, _ password: UnsafeRawPointer?, _ usePassword: Bool) -> OSStatus ``` |

Modified [SecKeyCreateFromData(_: CFDictionary, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1393853-seckeycreatefromdata)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyCreateFromData(_ parameters: CFDictionary, _ keyData: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |
| To | ``` func SecKeyCreateFromData(_ parameters: CFDictionary, _ keyData: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey? ``` |

Modified [SecKeyDeriveFromPassword(_: CFString, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1395028-seckeyderivefrompassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyDeriveFromPassword(_ password: CFString, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |
| To | ``` func SecKeyDeriveFromPassword(_ password: CFString, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey? ``` |

Modified [SecKeyGeneratePair(_: CFDictionary, _: UnsafeMutablePointer<SecKey?>?, _: UnsafeMutablePointer<SecKey?>?) -> OSStatus](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>, _ privateKey: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |
| To | ``` func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>?, _ privateKey: UnsafeMutablePointer<SecKey?>?) -> OSStatus ``` |

Modified [SecKeyGeneratePairAsync(_: CFDictionary, _: DispatchQueue, _: Security.SecKeyGeneratePairBlock)](https://developer.apple.com/documentation/security/1394698-seckeygeneratepairasync)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGeneratePairAsync(_ parameters: CFDictionary, _ deliveryQueue: dispatch_queue_t, _ result: SecKeyGeneratePairBlock) ``` |
| To | ``` func SecKeyGeneratePairAsync(_ parameters: CFDictionary, _ deliveryQueue: DispatchQueue, _ result: Security.SecKeyGeneratePairBlock) ``` |

Modified [SecKeyGeneratePairBlock](https://developer.apple.com/documentation/security/seckeygeneratepairblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecKeyGeneratePairBlock = (SecKey, SecKey, CFError) -> Void ``` |
| To | ``` typealias SecKeyGeneratePairBlock = (SecKey, SecKey, CFError) -> Swift.Void ``` |

Modified [SecKeyGenerateSymmetric(_: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1401861-seckeygeneratesymmetric)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGenerateSymmetric(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |
| To | ``` func SecKeyGenerateSymmetric(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey? ``` |

Modified [SecKeyUnwrapSymmetric(_: UnsafeMutablePointer<Unmanaged<CFData>?>, _: SecKey, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1394725-seckeyunwrapsymmetric)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecKey? ``` |
| To | ``` func SecKeyUnwrapSymmetric(_ keyToUnwrap: UnsafeMutablePointer<Unmanaged<CFData>?>, _ unwrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey? ``` |

Modified [SecKeyWrapSymmetric(_: SecKey, _: SecKey, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1396734-seckeywrapsymmetric)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyWrapSymmetric(_ keyToWrap: SecKey, _ wrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData? ``` |
| To | ``` func SecKeyWrapSymmetric(_ keyToWrap: SecKey, _ wrappingKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData? ``` |

Modified [SecMessageBlock](https://developer.apple.com/documentation/security/secmessageblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecMessageBlock = (AnyObject?, CFError?, Bool) -> Void ``` |
| To | ``` typealias SecMessageBlock = (CFTypeRef?, CFError?, Bool) -> Swift.Void ``` |

Modified [SecPolicyCopyProperties(_: SecPolicy) -> CFDictionary?](https://developer.apple.com/documentation/security/1401915-secpolicycopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCopyProperties(_ policyRef: SecPolicy) -> CFDictionary ``` |
| To | ``` func SecPolicyCopyProperties(_ policyRef: SecPolicy) -> CFDictionary? ``` |

Modified [SecPolicyCreateRevocation(_: CFOptionFlags) -> SecPolicy?](https://developer.apple.com/documentation/security/1400026-secpolicycreaterevocation)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateRevocation(_ revocationFlags: CFOptionFlags) -> SecPolicy ``` |
| To | ``` func SecPolicyCreateRevocation(_ revocationFlags: CFOptionFlags) -> SecPolicy? ``` |

Modified [SecPolicyCreateWithProperties(_: CFTypeRef, _: CFDictionary?) -> SecPolicy?](https://developer.apple.com/documentation/security/1394568-secpolicycreatewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: AnyObject, _ properties: CFDictionary?) -> SecPolicy? ``` |
| To | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: CFTypeRef, _ properties: CFDictionary?) -> SecPolicy? ``` |

Modified [SecRandomCopyBytes(_: SecRandomRef?, _: Int, _: UnsafeMutablePointer<UInt8>) -> Int32](https://developer.apple.com/documentation/security/1399291-secrandomcopybytes)

|  | Declaration |
| --- | --- |
| From | ``` func SecRandomCopyBytes(_ rnd: SecRandomRef, _ count: Int, _ bytes: UnsafeMutablePointer<UInt8>) -> Int32 ``` |
| To | ``` func SecRandomCopyBytes(_ rnd: SecRandomRef?, _ count: Int, _ bytes: UnsafeMutablePointer<UInt8>) -> Int32 ``` |

Modified [SecRandomRef](https://developer.apple.com/documentation/security/secrandomref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecRandomRef = COpaquePointer ``` |
| To | ``` typealias SecRandomRef = OpaquePointer ``` |

Modified [SecRequirementCreateWithStringAndErrors(_: CFString, _: SecCSFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>?, _: UnsafeMutablePointer<SecRequirement?>) -> OSStatus](https://developer.apple.com/documentation/security/1401166-secrequirementcreatewithstringan)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequirementCreateWithStringAndErrors(_ text: CFString, _ flags: SecCSFlags, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus ``` |
| To | ``` func SecRequirementCreateWithStringAndErrors(_ text: CFString, _ flags: SecCSFlags, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus ``` |

Modified [SecSignTransformCreate(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](https://developer.apple.com/documentation/security/1398780-secsigntransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecSignTransformCreate(_ key: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |
| To | ``` func SecSignTransformCreate(_ key: SecKey, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform? ``` |

Modified [SecStaticCodeCheckValidityWithErrors(_: SecStaticCode, _: SecCSFlags, _: SecRequirement?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus](https://developer.apple.com/documentation/security/1395252-secstaticcodecheckvaliditywither)

|  | Declaration |
| --- | --- |
| From | ``` func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OSStatus ``` |
| To | ``` func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus ``` |

Modified [SecTaskCopyValueForEntitlement(_: SecTask, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef?](https://developer.apple.com/documentation/security/1393461-sectaskcopyvalueforentitlement)

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCopyValueForEntitlement(_ task: SecTask, _ entitlement: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject? ``` |
| To | ``` func SecTaskCopyValueForEntitlement(_ task: SecTask, _ entitlement: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef? ``` |

Modified [SecTaskCopyValuesForEntitlements(_: SecTask, _: CFArray, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?](https://developer.apple.com/documentation/security/1397627-sectaskcopyvaluesforentitlements)

|  | Declaration |
| --- | --- |
| From | ``` func SecTaskCopyValuesForEntitlements(_ task: SecTask, _ entitlements: CFArray, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary? ``` |
| To | ``` func SecTaskCopyValuesForEntitlements(_ task: SecTask, _ entitlements: CFArray, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary? ``` |

Modified [SecTransformActionBlock](https://developer.apple.com/documentation/security/sectransformactionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformActionBlock = () -> Unmanaged<AnyObject>? ``` |
| To | ``` typealias SecTransformActionBlock = () -> Unmanaged<CFTypeRef>? ``` |

Modified [SecTransformAttribute](https://developer.apple.com/documentation/security/sectransformattributeref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformAttributeRef = SecTransformAttribute ``` |
| To | ``` typealias SecTransformAttribute = CFTypeRef ``` |

Modified [SecTransformAttributeActionBlock](https://developer.apple.com/documentation/security/sectransformattributeactionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformAttributeActionBlock = (SecTransformAttribute, AnyObject) -> Unmanaged<AnyObject>? ``` |
| To | ``` typealias SecTransformAttributeActionBlock = (SecTransformAttribute, CFTypeRef) -> Unmanaged<CFTypeRef>? ``` |

Modified [SecTransformConnectTransforms(_: SecTransform, _: CFString, _: SecTransform, _: CFString, _: SecGroupTransform, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecGroupTransform?](https://developer.apple.com/documentation/security/1401298-sectransformconnecttransforms)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformConnectTransforms(_ sourceTransformRef: SecTransform, _ sourceAttributeName: CFString, _ destinationTransformRef: SecTransform, _ destinationAttributeName: CFString, _ group: SecGroupTransform, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecGroupTransform? ``` |
| To | ``` func SecTransformConnectTransforms(_ sourceTransformRef: SecTransform, _ sourceAttributeName: CFString, _ destinationTransformRef: SecTransform, _ destinationAttributeName: CFString, _ group: SecGroupTransform, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecGroupTransform? ``` |

Modified [SecTransformCreate(_: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](https://developer.apple.com/documentation/security/1395256-sectransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreate(_ name: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |
| To | ``` func SecTransformCreate(_ name: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform? ``` |

Modified [SecTransformCreateFP](https://developer.apple.com/documentation/security/sectransformcreatefp)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformCreateFP = (CFString, SecTransform, SecTransformImplementationRef) -> SecTransformInstanceBlock ``` |
| To | ``` typealias SecTransformCreateFP = (CFString, SecTransform, SecTransformImplementationRef) -> Security.SecTransformInstanceBlock ``` |

Modified [SecTransformCreateFromExternalRepresentation(_: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](https://developer.apple.com/documentation/security/1397563-sectransformcreatefromexternalre)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |
| To | ``` func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform? ``` |

Modified [SecTransformCustomGetAttribute(_: SecTransformImplementationRef, _: SecTransformStringOrAttribute, _: SecTransformMetaAttributeType) -> CFTypeRef?](https://developer.apple.com/documentation/security/1397766-sectransformcustomgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType) -> AnyObject? ``` |
| To | ``` func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType) -> CFTypeRef? ``` |

Modified [SecTransformCustomSetAttribute(_: SecTransformImplementationRef, _: SecTransformStringOrAttribute, _: SecTransformMetaAttributeType, _: CFTypeRef?) -> CFTypeRef?](https://developer.apple.com/documentation/security/1392556-sectransformcustomsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType, _ value: AnyObject?) -> AnyObject? ``` |
| To | ``` func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType, _ value: CFTypeRef?) -> CFTypeRef? ``` |

Modified [SecTransformDataBlock](https://developer.apple.com/documentation/security/sectransformdatablock)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformDataBlock = (AnyObject) -> Unmanaged<AnyObject>? ``` |
| To | ``` typealias SecTransformDataBlock = (CFTypeRef) -> Unmanaged<CFTypeRef>? ``` |

Modified [SecTransformExecute(_: SecTransform, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef](https://developer.apple.com/documentation/security/1395776-sectransformexecute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformExecute(_ transformRef: SecTransform, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject ``` |
| To | ``` func SecTransformExecute(_ transformRef: SecTransform, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef ``` |

Modified [SecTransformExecuteAsync(_: SecTransform, _: DispatchQueue, _: Security.SecMessageBlock)](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformExecuteAsync(_ transformRef: SecTransform, _ deliveryQueue: dispatch_queue_t, _ deliveryBlock: SecMessageBlock) ``` |
| To | ``` func SecTransformExecuteAsync(_ transformRef: SecTransform, _ deliveryQueue: DispatchQueue, _ deliveryBlock: Security.SecMessageBlock) ``` |

Modified [SecTransformGetAttribute(_: SecTransform, _: CFString) -> CFTypeRef?](https://developer.apple.com/documentation/security/1398748-sectransformgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformGetAttribute(_ transformRef: SecTransform, _ key: CFString) -> AnyObject? ``` |
| To | ``` func SecTransformGetAttribute(_ transformRef: SecTransform, _ key: CFString) -> CFTypeRef? ``` |

Modified [SecTransformImplementationRef](https://developer.apple.com/documentation/security/sectransformimplementationref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformImplementationRef = COpaquePointer ``` |
| To | ``` typealias SecTransformImplementationRef = OpaquePointer ``` |

Modified [SecTransformNoData() -> CFTypeRef](https://developer.apple.com/documentation/security/1393788-sectransformnodata)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformNoData() -> AnyObject ``` |
| To | ``` func SecTransformNoData() -> CFTypeRef ``` |

Modified [SecTransformPushbackAttribute(_: SecTransformImplementationRef, _: SecTransformStringOrAttribute, _: CFTypeRef) -> CFTypeRef?](https://developer.apple.com/documentation/security/1400559-sectransformpushbackattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ value: AnyObject) -> AnyObject? ``` |
| To | ``` func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ value: CFTypeRef) -> CFTypeRef? ``` |

Modified [SecTransformRegister(_: CFString, _: Security.SecTransformCreateFP, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/security/1393997-sectransformregister)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformRegister(_ uniqueName: CFString, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func SecTransformRegister(_ uniqueName: CFString, _ createTransformFunction: Security.SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [SecTransformSetAttribute(_: SecTransform, _: CFString, _: CFTypeRef, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/security/1393861-sectransformsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetAttribute(_ transformRef: SecTransform, _ key: CFString, _ value: AnyObject, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func SecTransformSetAttribute(_ transformRef: SecTransform, _ key: CFString, _ value: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [SecTransformSetAttributeAction(_: SecTransformImplementationRef, _: CFString, _: SecTransformStringOrAttribute?, _: Security.SecTransformAttributeActionBlock) -> CFError?](https://developer.apple.com/documentation/security/1396035-sectransformsetattributeaction)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ attribute: SecTransformStringOrAttribute?, _ newAction: SecTransformAttributeActionBlock) -> CFError? ``` |
| To | ``` func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ attribute: SecTransformStringOrAttribute?, _ newAction: Security.SecTransformAttributeActionBlock) -> CFError? ``` |

Modified [SecTransformSetDataAction(_: SecTransformImplementationRef, _: CFString, _: Security.SecTransformDataBlock) -> CFError?](https://developer.apple.com/documentation/security/1399597-sectransformsetdataaction)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetDataAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: SecTransformDataBlock) -> CFError? ``` |
| To | ``` func SecTransformSetDataAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: Security.SecTransformDataBlock) -> CFError? ``` |

Modified [SecTransformSetTransformAction(_: SecTransformImplementationRef, _: CFString, _: Security.SecTransformActionBlock) -> CFError?](https://developer.apple.com/documentation/security/1402097-sectransformsettransformaction)

|  | Declaration |
| --- | --- |
| From | ``` func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: SecTransformActionBlock) -> CFError? ``` |
| To | ``` func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: Security.SecTransformActionBlock) -> CFError? ``` |

Modified [SecTrustCallback](https://developer.apple.com/documentation/security/sectrustcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTrustCallback = (SecTrust, SecTrustResultType) -> Void ``` |
| To | ``` typealias SecTrustCallback = (SecTrust, SecTrustResultType) -> Swift.Void ``` |

Modified [SecTrustCreateWithCertificates(_: CFTypeRef, _: CFTypeRef?, _: UnsafeMutablePointer<SecTrust?>) -> OSStatus](https://developer.apple.com/documentation/security/1401555-sectrustcreatewithcertificates)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustCreateWithCertificates(_ certificates: AnyObject, _ policies: AnyObject?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus ``` |
| To | ``` func SecTrustCreateWithCertificates(_ certificates: CFTypeRef, _ policies: CFTypeRef?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus ``` |

Modified [SecTrustedApplicationCreateFromPath(_: UnsafePointer<Int8>?, _: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus](https://developer.apple.com/documentation/security/1400622-sectrustedapplicationcreatefromp)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<Int8>, _ app: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus ``` |
| To | ``` func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<Int8>?, _ app: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus ``` |

Modified [SecTrustEvaluate(_: SecTrust, _: UnsafeMutablePointer<SecTrustResultType>?) -> OSStatus](https://developer.apple.com/documentation/security/1394363-sectrustevaluate)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustEvaluate(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus ``` |
| To | ``` func SecTrustEvaluate(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>?) -> OSStatus ``` |

Modified [SecTrustEvaluateAsync(_: SecTrust, _: DispatchQueue?, _: Security.SecTrustCallback) -> OSStatus](https://developer.apple.com/documentation/security/1400632-sectrustevaluateasync)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustEvaluateAsync(_ trust: SecTrust, _ queue: dispatch_queue_t?, _ result: SecTrustCallback) -> OSStatus ``` |
| To | ``` func SecTrustEvaluateAsync(_ trust: SecTrust, _ queue: DispatchQueue?, _ result: Security.SecTrustCallback) -> OSStatus ``` |

Modified [SecTrustSetExceptions(_: SecTrust, _: CFData?) -> Bool](https://developer.apple.com/documentation/security/1395676-sectrustsetexceptions)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetExceptions(_ trust: SecTrust, _ exceptions: CFData) -> Bool ``` |
| To | ``` func SecTrustSetExceptions(_ trust: SecTrust, _ exceptions: CFData?) -> Bool ``` |

Modified [SecTrustSetKeychains(_: SecTrust, _: CFTypeRef?) -> OSStatus](https://developer.apple.com/documentation/security/1395644-sectrustsetkeychains)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetKeychains(_ trust: SecTrust, _ keychainOrArray: AnyObject?) -> OSStatus ``` |
| To | ``` func SecTrustSetKeychains(_ trust: SecTrust, _ keychainOrArray: CFTypeRef?) -> OSStatus ``` |

Modified [SecTrustSetOCSPResponse(_: SecTrust, _: CFTypeRef?) -> OSStatus](https://developer.apple.com/documentation/security/1400880-sectrustsetocspresponse)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetOCSPResponse(_ trust: SecTrust, _ responseData: AnyObject?) -> OSStatus ``` |
| To | ``` func SecTrustSetOCSPResponse(_ trust: SecTrust, _ responseData: CFTypeRef?) -> OSStatus ``` |

Modified [SecTrustSetPolicies(_: SecTrust, _: CFTypeRef) -> OSStatus](https://developer.apple.com/documentation/security/1398399-sectrustsetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetPolicies(_ trust: SecTrust, _ policies: AnyObject) -> OSStatus ``` |
| To | ``` func SecTrustSetPolicies(_ trust: SecTrust, _ policies: CFTypeRef) -> OSStatus ``` |

Modified [SecTrustSettingsCopyCertificates(_: SecTrustSettingsDomain, _: UnsafeMutablePointer<CFArray?>?) -> OSStatus](https://developer.apple.com/documentation/security/1397413-sectrustsettingscopycertificates)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |
| To | ``` func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<CFArray?>?) -> OSStatus ``` |

Modified [SecTrustSettingsSetTrustSettings(_: SecCertificate, _: SecTrustSettingsDomain, _: CFTypeRef?) -> OSStatus](https://developer.apple.com/documentation/security/1399119-sectrustsettingssettrustsettings)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSettingsSetTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ trustSettingsDictOrArray: AnyObject?) -> OSStatus ``` |
| To | ``` func SecTrustSettingsSetTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ trustSettingsDictOrArray: CFTypeRef?) -> OSStatus ``` |

Modified [SecVerifyTransformCreate(_: SecKey, _: CFData?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?](https://developer.apple.com/documentation/security/1393414-secverifytransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SecVerifyTransformCreate(_ key: SecKey, _ signature: CFData?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecTransform? ``` |
| To | ``` func SecVerifyTransformCreate(_ key: SecKey, _ signature: CFData?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform? ``` |

Modified [SSLAddDistinguishedName(_: SSLContext, _: UnsafeRawPointer?, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1400906-ssladddistinguishedname)

|  | Declaration |
| --- | --- |
| From | ``` func SSLAddDistinguishedName(_ context: SSLContext, _ derDN: UnsafePointer<Void>, _ derDNLen: Int) -> OSStatus ``` |
| To | ``` func SSLAddDistinguishedName(_ context: SSLContext, _ derDN: UnsafeRawPointer?, _ derDNLen: Int) -> OSStatus ``` |

Modified [SSLConnectionRef](https://developer.apple.com/documentation/security/sslconnectionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLConnectionRef = UnsafePointer<Void> ``` |
| To | ``` typealias SSLConnectionRef = UnsafeRawPointer ``` |

Modified [SSLGetConnection(_: SSLContext, _: UnsafeMutablePointer<SSLConnectionRef?>) -> OSStatus](https://developer.apple.com/documentation/security/1397993-sslgetconnection)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetConnection(_ context: SSLContext, _ connection: UnsafeMutablePointer<SSLConnectionRef>) -> OSStatus ``` |
| To | ``` func SSLGetConnection(_ context: SSLContext, _ connection: UnsafeMutablePointer<SSLConnectionRef?>) -> OSStatus ``` |

Modified [SSLGetDiffieHellmanParams(_: SSLContext, _: UnsafeMutablePointer<UnsafeRawPointer?>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1399892-sslgetdiffiehellmanparams)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeMutablePointer<UnsafePointer<Void>>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeMutablePointer<UnsafeRawPointer?>, _ dhParamsLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLGetPeerID(_: SSLContext, _: UnsafeMutablePointer<UnsafeRawPointer?>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1395882-sslgetpeerid)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetPeerID(_ context: SSLContext, _ peerID: UnsafeMutablePointer<UnsafePointer<Void>>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLGetPeerID(_ context: SSLContext, _ peerID: UnsafeMutablePointer<UnsafeRawPointer?>, _ peerIDLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLRead(_: SSLContext, _: UnsafeMutableRawPointer, _: Int, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1394324-sslread)

|  | Declaration |
| --- | --- |
| From | ``` func SSLRead(_ context: SSLContext, _ data: UnsafeMutablePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLRead(_ context: SSLContext, _ data: UnsafeMutableRawPointer, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLReadFunc](https://developer.apple.com/documentation/security/sslreadfunc)

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLReadFunc = (SSLConnectionRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` typealias SSLReadFunc = (SSLConnectionRef, UnsafeMutableRawPointer, UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLSetCertificate(_: SSLContext, _: CFArray?) -> OSStatus](https://developer.apple.com/documentation/security/1392400-sslsetcertificate)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetCertificate(_ context: SSLContext, _ certRefs: CFArray) -> OSStatus ``` |
| To | ``` func SSLSetCertificate(_ context: SSLContext, _ certRefs: CFArray?) -> OSStatus ``` |

Modified [SSLSetCertificateAuthorities(_: SSLContext, _: CFTypeRef, _: Bool) -> OSStatus](https://developer.apple.com/documentation/security/1396770-sslsetcertificateauthorities)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetCertificateAuthorities(_ context: SSLContext, _ certificateOrArray: AnyObject, _ replaceExisting: Bool) -> OSStatus ``` |
| To | ``` func SSLSetCertificateAuthorities(_ context: SSLContext, _ certificateOrArray: CFTypeRef, _ replaceExisting: Bool) -> OSStatus ``` |

Modified [SSLSetConnection(_: SSLContext, _: SSLConnectionRef?) -> OSStatus](https://developer.apple.com/documentation/security/1398843-sslsetconnection)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetConnection(_ context: SSLContext, _ connection: SSLConnectionRef) -> OSStatus ``` |
| To | ``` func SSLSetConnection(_ context: SSLContext, _ connection: SSLConnectionRef?) -> OSStatus ``` |

Modified [SSLSetDatagramHelloCookie(_: SSLContext, _: UnsafeRawPointer?, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1398936-sslsetdatagramhellocookie)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext, _ cookie: UnsafePointer<Void>, _ cookieLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetDatagramHelloCookie(_ dtlsContext: SSLContext, _ cookie: UnsafeRawPointer?, _ cookieLen: Int) -> OSStatus ``` |

Modified [SSLSetDiffieHellmanParams(_: SSLContext, _: UnsafeRawPointer?, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1392524-sslsetdiffiehellmanparams)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafePointer<Void>, _ dhParamsLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetDiffieHellmanParams(_ context: SSLContext, _ dhParams: UnsafeRawPointer?, _ dhParamsLen: Int) -> OSStatus ``` |

Modified [SSLSetIOFuncs(_: SSLContext, _: Security.SSLReadFunc, _: Security.SSLWriteFunc) -> OSStatus](https://developer.apple.com/documentation/security/1396081-sslsetiofuncs)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetIOFuncs(_ context: SSLContext, _ readFunc: SSLReadFunc, _ writeFunc: SSLWriteFunc) -> OSStatus ``` |
| To | ``` func SSLSetIOFuncs(_ context: SSLContext, _ readFunc: Security.SSLReadFunc, _ writeFunc: Security.SSLWriteFunc) -> OSStatus ``` |

Modified [SSLSetPeerDomainName(_: SSLContext, _: UnsafePointer<Int8>?, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1393047-sslsetpeerdomainname)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetPeerDomainName(_ context: SSLContext, _ peerName: UnsafePointer<Int8>, _ peerNameLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetPeerDomainName(_ context: SSLContext, _ peerName: UnsafePointer<Int8>?, _ peerNameLen: Int) -> OSStatus ``` |

Modified [SSLSetPeerID(_: SSLContext, _: UnsafeRawPointer?, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1400006-sslsetpeerid)

|  | Declaration |
| --- | --- |
| From | ``` func SSLSetPeerID(_ context: SSLContext, _ peerID: UnsafePointer<Void>, _ peerIDLen: Int) -> OSStatus ``` |
| To | ``` func SSLSetPeerID(_ context: SSLContext, _ peerID: UnsafeRawPointer?, _ peerIDLen: Int) -> OSStatus ``` |

Modified [SSLWrite(_: SSLContext, _: UnsafeRawPointer?, _: Int, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1400864-sslwrite)

|  | Declaration |
| --- | --- |
| From | ``` func SSLWrite(_ context: SSLContext, _ data: UnsafePointer<Void>, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SSLWrite(_ context: SSLContext, _ data: UnsafeRawPointer?, _ dataLength: Int, _ processed: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SSLWriteFunc](https://developer.apple.com/documentation/security/sslwritefunc)

|  | Declaration |
| --- | --- |
| From | ``` typealias SSLWriteFunc = (SSLConnectionRef, UnsafePointer<Void>, UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` typealias SSLWriteFunc = (SSLConnectionRef, UnsafeRawPointer, UnsafeMutablePointer<Int>) -> OSStatus ``` |

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
