---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/Security.html
archived_at: '2026-07-18T02:53:53.787357Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Security Changes for Swift

### Security

Added [CMSSignedAttributes.AttrAppleCodesigningHashAgility](https://developer.apple.com/documentation/security/cmssignedattributes/1387155-attrapplecodesigninghashagility)Added cssm_certgroup.GroupListAdded cssm_certgroup.init(CertType: CSSM_CERT_TYPE, CertEncoding: CSSM_CERT_ENCODING, NumCerts: uint32, GroupList: cssm_certgroup.__Unnamed_union_GroupList, CertGroupType: CSSM_CERTGROUP_TYPE, Reserved: UnsafeMutablePointer<Void>)Added cssm_context_attribute_value [struct]Added cssm_context_attribute_value.AccessCredentialsAdded cssm_context_attribute_value.CryptoDataAdded cssm_context_attribute_value.DataAdded cssm_context_attribute_value.DateAdded cssm_context_attribute_value.DLDBHandleAdded cssm_context_attribute_value.init()Added cssm_context_attribute_value.init(AccessCredentials: CSSM_ACCESS_CREDENTIALS_PTR)Added cssm_context_attribute_value.init(CryptoData: CSSM_CRYPTO_DATA_PTR)Added cssm_context_attribute_value.init(Data: CSSM_DATA_PTR)Added cssm_context_attribute_value.init(Date: CSSM_DATE_PTR)Added cssm_context_attribute_value.init(DLDBHandle: CSSM_DL_DB_HANDLE_PTR)Added cssm_context_attribute_value.init(Key: CSSM_KEY_PTR)Added cssm_context_attribute_value.init(KRProfile: UnsafeMutablePointer<cssm_kr_profile>)Added cssm_context_attribute_value.init(Padding: CSSM_PADDING)Added cssm_context_attribute_value.init(Range: CSSM_RANGE_PTR)Added cssm_context_attribute_value.init(String: UnsafeMutablePointer<Int8>)Added cssm_context_attribute_value.init(Uint32: uint32)Added cssm_context_attribute_value.init(Version: CSSM_VERSION_PTR)Added cssm_context_attribute_value.KeyAdded cssm_context_attribute_value.KRProfileAdded cssm_context_attribute_value.PaddingAdded cssm_context_attribute_value.RangeAdded cssm_context_attribute_value.StringAdded cssm_context_attribute_value.Uint32Added cssm_context_attribute_value.VersionAdded cssm_crlgroup.GroupCrlListAdded cssm_crlgroup.init(CrlType: CSSM_CRL_TYPE, CrlEncoding: CSSM_CRL_ENCODING, NumberOfCrls: uint32, GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList, CrlGroupType: CSSM_CRLGROUP_TYPE)Added cssm_db_attribute_label [struct]Added cssm_db_attribute_label.AttributeIDAdded cssm_db_attribute_label.AttributeNameAdded cssm_db_attribute_label.AttributeOIDAdded cssm_db_attribute_label.init()Added cssm_db_attribute_label.init(AttributeID: uint32)Added cssm_db_attribute_label.init(AttributeName: UnsafeMutablePointer<Int8>)Added cssm_db_attribute_label.init(AttributeOID: CSSM_OID)Added cssm_list_element.ElementAdded cssm_list_element.init(NextElement: UnsafeMutablePointer<cssm_list_element>, WordID: CSSM_WORDID_TYPE, ElementType: CSSM_LIST_ELEMENT_TYPE, Element: cssm_list_element.__Unnamed_union_Element)Added cssm_x509ext_value [struct]Added cssm_x509ext_value.init()Added cssm_x509ext_value.init(parsedValue: UnsafeMutablePointer<Void>)Added cssm_x509ext_value.init(tagAndValue: UnsafeMutablePointer<CSSM_X509EXT_TAGandVALUE>)Added cssm_x509ext_value.init(valuePair: UnsafeMutablePointer<CSSM_X509EXT_PAIR>)Added cssm_x509ext_value.parsedValueAdded cssm_x509ext_value.tagAndValueAdded cssm_x509ext_value.valuePairAdded [SecCSDigestAlgorithm [enum]](https://developer.apple.com/documentation/security/seccsdigestalgorithm)Added [SecCSDigestAlgorithm.CodeSignatureHashSHA1](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha1)Added [SecCSDigestAlgorithm.CodeSignatureHashSHA256](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha256)Added [SecCSDigestAlgorithm.CodeSignatureHashSHA256Truncated](https://developer.apple.com/documentation/security/seccsdigestalgorithm/codesignaturehashsha256truncated)Added [SecCSDigestAlgorithm.CodeSignatureHashSHA384](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha384)Added [SecCSDigestAlgorithm.CodeSignatureNoHash](https://developer.apple.com/documentation/security/seccsdigestalgorithm/codesignaturenohash)Added [CSSM_ACL_AUTHORIZATION_INTEGRITY](https://developer.apple.com/documentation/security/1434848-anonymous/cssm_acl_authorization_integrity)Added [CSSM_ACL_AUTHORIZATION_PARTITION_ID](https://developer.apple.com/documentation/security/cssm_acl_authorization_partition_id)Added [CSSM_ACL_SUBJECT_TYPE_PARTITION](https://developer.apple.com/documentation/security/1434858-anonymous/cssm_acl_subject_type_partition)Added [CSSM_APPLE_ACL_TAG_INTEGRITY](https://developer.apple.com/documentation/security/cssm_apple_acl_tag_integrity)Added [CSSM_APPLE_ACL_TAG_PARTITION_ID](https://developer.apple.com/documentation/security/cssm_apple_acl_tag_partition_id)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_19](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_19)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_20](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_20)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_21](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_21)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_22](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_22)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_23](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_23)Added [CSSM_APPLEFILEDL_MAKE_BACKUP](https://developer.apple.com/documentation/security/1434707-anonymous/cssm_applefiledl_make_backup)Added [CSSM_APPLEFILEDL_TAKE_FILE_LOCK](https://developer.apple.com/documentation/security/1434707-anonymous/cssm_applefiledl_take_file_lock)Added [CSSM_WORDID_PARTITION](https://developer.apple.com/documentation/security/1434818-anonymous/cssm_wordid_partition)Added [errSecCSBadDiskImageFormat](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbaddiskimageformat)Added [errSecCSNotAppLike](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsnotapplike)Added [errSecCSUnsupportedDigestAlgorithm](https://developer.apple.com/documentation/security/errseccsunsupporteddigestalgorithm)Added [kSecACLAuthorizationIntegrity](https://developer.apple.com/documentation/security/ksecaclauthorizationintegrity)Added [kSecACLAuthorizationPartitionID](https://developer.apple.com/documentation/security/ksecaclauthorizationpartitionid)Added [kSecCodeInfoCdHashes](https://developer.apple.com/documentation/security/kseccodeinfocdhashes)Added [kSecCodeInfoDigestAlgorithms](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithms)Added [kSecCSRestrictToAppLike](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsrestricttoapplike)Modified [CMSDecoder](https://developer.apple.com/documentation/security/cmsdecoder)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMSDecoderRef | ``` typealias CMSDecoderRef = CMSDecoder ``` |
| To | CMSDecoder | ``` class CMSDecoder { } ``` |

Modified [CMSEncoder](https://developer.apple.com/documentation/security/cmsencoderref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CMSEncoderRef | ``` typealias CMSEncoderRef = CMSEncoder ``` |
| To | CMSEncoder | ``` class CMSEncoder { } ``` |

Modified [CMSSignedAttributes [enum]](https://developer.apple.com/documentation/security/cmssignedattributes)

|  | Declaration |
| --- | --- |
| From | ``` enum CMSSignedAttributes : UInt32 {     case AttrNone     case AttrSmimeCapabilities     case AttrSmimeEncryptionKeyPrefs     case AttrSmimeMSEncryptionKeyPrefs     case AttrSigningTime } ``` |
| To | ``` enum CMSSignedAttributes : UInt32 {     case AttrNone     case AttrSmimeCapabilities     case AttrSmimeEncryptionKeyPrefs     case AttrSmimeMSEncryptionKeyPrefs     case AttrSigningTime     case AttrAppleCodesigningHashAgility } ``` |

Modified cssm_certgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_certgroup {     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var NumCerts: uint32     var CertGroupType: CSSM_CERTGROUP_TYPE     var Reserved: UnsafeMutablePointer<Void>     init() } ``` |
| To | ``` struct cssm_certgroup {     struct __Unnamed_union_GroupList {         var CertList: CSSM_DATA_PTR         var EncodedCertList: CSSM_ENCODED_CERT_PTR         var ParsedCertList: CSSM_PARSED_CERT_PTR         var PairCertList: CSSM_CERT_PAIR_PTR         init(CertList CertList: CSSM_DATA_PTR)         init(EncodedCertList EncodedCertList: CSSM_ENCODED_CERT_PTR)         init(ParsedCertList ParsedCertList: CSSM_PARSED_CERT_PTR)         init(PairCertList PairCertList: CSSM_CERT_PAIR_PTR)         init()     }     var CertType: CSSM_CERT_TYPE     var CertEncoding: CSSM_CERT_ENCODING     var NumCerts: uint32     var GroupList: cssm_certgroup.__Unnamed_union_GroupList     var CertGroupType: CSSM_CERTGROUP_TYPE     var Reserved: UnsafeMutablePointer<Void>     init()     init(CertType CertType: CSSM_CERT_TYPE, CertEncoding CertEncoding: CSSM_CERT_ENCODING, NumCerts NumCerts: uint32, GroupList GroupList: cssm_certgroup.__Unnamed_union_GroupList, CertGroupType CertGroupType: CSSM_CERTGROUP_TYPE, Reserved Reserved: UnsafeMutablePointer<Void>) } ``` |

Modified cssm_crlgroup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_crlgroup {     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var NumberOfCrls: uint32     var CrlGroupType: CSSM_CRLGROUP_TYPE     init() } ``` |
| To | ``` struct cssm_crlgroup {     struct __Unnamed_union_GroupCrlList {         var CrlList: CSSM_DATA_PTR         var EncodedCrlList: CSSM_ENCODED_CRL_PTR         var ParsedCrlList: CSSM_PARSED_CRL_PTR         var PairCrlList: CSSM_CRL_PAIR_PTR         init(CrlList CrlList: CSSM_DATA_PTR)         init(EncodedCrlList EncodedCrlList: CSSM_ENCODED_CRL_PTR)         init(ParsedCrlList ParsedCrlList: CSSM_PARSED_CRL_PTR)         init(PairCrlList PairCrlList: CSSM_CRL_PAIR_PTR)         init()     }     var CrlType: CSSM_CRL_TYPE     var CrlEncoding: CSSM_CRL_ENCODING     var NumberOfCrls: uint32     var GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList     var CrlGroupType: CSSM_CRLGROUP_TYPE     init()     init(CrlType CrlType: CSSM_CRL_TYPE, CrlEncoding CrlEncoding: CSSM_CRL_ENCODING, NumberOfCrls NumberOfCrls: uint32, GroupCrlList GroupCrlList: cssm_crlgroup.__Unnamed_union_GroupCrlList, CrlGroupType CrlGroupType: CSSM_CRLGROUP_TYPE) } ``` |

Modified cssm_list_element [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cssm_list_element {     var NextElement: UnsafeMutablePointer<cssm_list_element>     var WordID: CSSM_WORDID_TYPE     var ElementType: CSSM_LIST_ELEMENT_TYPE     init() } ``` |
| To | ``` struct cssm_list_element {     struct __Unnamed_union_Element {         var Sublist: CSSM_LIST         var Word: CSSM_DATA         init(Sublist Sublist: CSSM_LIST)         init(Word Word: CSSM_DATA)         init()     }     var NextElement: UnsafeMutablePointer<cssm_list_element>     var WordID: CSSM_WORDID_TYPE     var ElementType: CSSM_LIST_ELEMENT_TYPE     var Element: cssm_list_element.__Unnamed_union_Element     init()     init(NextElement NextElement: UnsafeMutablePointer<cssm_list_element>, WordID WordID: CSSM_WORDID_TYPE, ElementType ElementType: CSSM_LIST_ELEMENT_TYPE, Element Element: cssm_list_element.__Unnamed_union_Element) } ``` |

Modified [SecAccess](https://developer.apple.com/documentation/security/secaccess)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecAccessRef | ``` typealias SecAccessRef = SecAccess ``` |
| To | SecAccess | ``` class SecAccess { } ``` |

Modified [SecAccessControl](https://developer.apple.com/documentation/security/secaccesscontrolref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecAccessControlRef | ``` typealias SecAccessControlRef = SecAccessControl ``` |
| To | SecAccessControl | ``` class SecAccessControl { } ``` |

Modified [SecACL](https://developer.apple.com/documentation/security/secaclref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecACLRef | ``` typealias SecACLRef = SecACL ``` |
| To | SecACL | ``` class SecACL { } ``` |

Modified [SecCertificate](https://developer.apple.com/documentation/security/seccertificate)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecCertificateRef | ``` typealias SecCertificateRef = SecCertificate ``` |
| To | SecCertificate | ``` class SecCertificate { } ``` |

Modified [SecCode](https://developer.apple.com/documentation/security/seccoderef)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecCodeRef | ``` typealias SecCodeRef = SecCode ``` |
| To | SecCode | ``` class SecCode { } ``` |

Modified [SecIdentity](https://developer.apple.com/documentation/security/secidentityref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecIdentityRef | ``` typealias SecIdentityRef = SecIdentity ``` |
| To | SecIdentity | ``` class SecIdentity { } ``` |

Modified [SecIdentitySearch](https://developer.apple.com/documentation/security/secidentitysearchref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecIdentitySearchRef | ``` typealias SecIdentitySearchRef = SecIdentitySearch ``` |
| To | SecIdentitySearch | ``` class SecIdentitySearch { } ``` |

Modified [SecKey](https://developer.apple.com/documentation/security/seckeyref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecKeyRef | ``` typealias SecKeyRef = SecKey ``` |
| To | SecKey | ``` class SecKey { } ``` |

Modified [SecKeychain](https://developer.apple.com/documentation/security/seckeychain)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecKeychainRef | ``` typealias SecKeychainRef = SecKeychain ``` |
| To | SecKeychain | ``` class SecKeychain { } ``` |

Modified [SecKeychainItem](https://developer.apple.com/documentation/security/seckeychainitem)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecKeychainItemRef | ``` typealias SecKeychainItemRef = SecKeychainItem ``` |
| To | SecKeychainItem | ``` class SecKeychainItem { } ``` |

Modified [SecKeychainSearch](https://developer.apple.com/documentation/security/seckeychainsearchref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecKeychainSearchRef | ``` typealias SecKeychainSearchRef = SecKeychainSearch ``` |
| To | SecKeychainSearch | ``` class SecKeychainSearch { } ``` |

Modified [SecPassword](https://developer.apple.com/documentation/security/secpasswordref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecPasswordRef | ``` typealias SecPasswordRef = SecPassword ``` |
| To | SecPassword | ``` class SecPassword { } ``` |

Modified [SecPolicy](https://developer.apple.com/documentation/security/secpolicyref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecPolicyRef | ``` typealias SecPolicyRef = SecPolicy ``` |
| To | SecPolicy | ``` class SecPolicy { } ``` |

Modified [SecPolicySearch](https://developer.apple.com/documentation/security/secpolicysearchref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecPolicySearchRef | ``` typealias SecPolicySearchRef = SecPolicySearch ``` |
| To | SecPolicySearch | ``` class SecPolicySearch { } ``` |

Modified [SecRequirement](https://developer.apple.com/documentation/security/secrequirement)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecRequirementRef | ``` typealias SecRequirementRef = SecRequirement ``` |
| To | SecRequirement | ``` class SecRequirement { } ``` |

Modified [SecStaticCode](https://developer.apple.com/documentation/security/secstaticcode)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecStaticCodeRef | ``` typealias SecStaticCodeRef = SecStaticCode ``` |
| To | SecStaticCode | ``` class SecStaticCode { } ``` |

Modified [SecTask](https://developer.apple.com/documentation/security/sectask)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecTaskRef | ``` typealias SecTaskRef = SecTask ``` |
| To | SecTask | ``` class SecTask { } ``` |

Modified [SecTrust](https://developer.apple.com/documentation/security/sectrustref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecTrustRef | ``` typealias SecTrustRef = SecTrust ``` |
| To | SecTrust | ``` class SecTrust { } ``` |

Modified [SecTrustedApplication](https://developer.apple.com/documentation/security/sectrustedapplicationref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecTrustedApplicationRef | ``` typealias SecTrustedApplicationRef = SecTrustedApplication ``` |
| To | SecTrustedApplication | ``` class SecTrustedApplication { } ``` |

Modified [SSLContext](https://developer.apple.com/documentation/security/sslcontext)

|  | Name | Declaration |
| --- | --- | --- |
| From | SSLContextRef | ``` typealias SSLContextRef = SSLContext ``` |
| To | SSLContext | ``` class SSLContext { } ``` |

Modified [SecCodeCopySelf(_: SecCSFlags, _: UnsafeMutablePointer<SecCode?>) -> OSStatus](https://developer.apple.com/documentation/security/1402140-seccodecopyself)

|  | Declaration |
| --- | --- |
| From | ``` func SecCodeCopySelf(_ flags: SecCSFlags, _ `self`: UnsafeMutablePointer<SecCode?>) -> OSStatus ``` |
| To | ``` func SecCodeCopySelf(_ flags: SecCSFlags, _ self: UnsafeMutablePointer<SecCode?>) -> OSStatus ``` |

Modified [SecGroupTransform](https://developer.apple.com/documentation/security/secgrouptransform)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecGroupTransformRef = SecGroupTransform ``` |
| To | ``` typealias SecGroupTransform = CFTypeRef ``` |

Modified [SecKeychainAddInternetPassword(_: SecKeychain?, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt16, _: SecProtocolType, _: SecAuthenticationType, _: UInt32, _: UnsafePointer<Void>, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1393322-seckeychainaddinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainAddInternetPassword(_ keychain: SecKeychain?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafePointer<Void>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecKeychainFindInternetPassword(_: AnyObject?, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt32, _: UnsafePointer<Int8>, _: UInt16, _: SecProtocolType, _: SecAuthenticationType, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus](https://developer.apple.com/documentation/security/1397763-seckeychainfindinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ `protocol`: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |
| To | ``` func SecKeychainFindInternetPassword(_ keychainOrArray: AnyObject?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<Int8>, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<Int8>, _ accountNameLength: UInt32, _ accountName: UnsafePointer<Int8>, _ pathLength: UInt32, _ path: UnsafePointer<Int8>, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>, _ passwordData: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>) -> OSStatus ``` |

Modified [SecTransform](https://developer.apple.com/documentation/security/sectransform)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformRef = SecTransform ``` |
| To | ``` typealias SecTransform = CFTypeRef ``` |

Modified [SecTransformStringOrAttribute](https://developer.apple.com/documentation/security/sectransformstringorattribute)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTransformStringOrAttributeRef = SecTransformStringOrAttribute ``` |
| To | ``` typealias SecTransformStringOrAttribute = CFTypeRef ``` |

Modified [SSLGetNegotiatedProtocolVersion(_: SSLContext, _: UnsafeMutablePointer<SSLProtocol>) -> OSStatus](https://developer.apple.com/documentation/security/1397382-sslgetnegotiatedprotocolversion)

|  | Declaration |
| --- | --- |
| From | ``` func SSLGetNegotiatedProtocolVersion(_ context: SSLContext, _ `protocol`: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |
| To | ``` func SSLGetNegotiatedProtocolVersion(_ context: SSLContext, _ protocol: UnsafeMutablePointer<SSLProtocol>) -> OSStatus ``` |

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
