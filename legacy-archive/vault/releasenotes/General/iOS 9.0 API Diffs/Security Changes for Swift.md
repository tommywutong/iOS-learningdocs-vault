---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Security.html
archived_at: '2026-07-18T02:56:58.283360Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Security Changes for Swift

### Security

Removed SecAccessControlCreateFlags.init(_: CFIndex)Removed errSecAllocateRemoved errSecAuthFailedRemoved errSecDecodeRemoved errSecDuplicateItemRemoved errSecInteractionNotAllowedRemoved errSecItemNotFoundRemoved errSecNotAvailableRemoved errSecParamRemoved errSecSuccessRemoved errSecUnimplementedRemoved kSecPaddingNoneRemoved kSecPaddingOAEPRemoved kSecPaddingPKCS1Removed kSecPaddingPKCS1MD2Removed kSecPaddingPKCS1MD5Removed kSecPaddingPKCS1SHA1Removed kSecPaddingPKCS1SHA224Removed kSecPaddingPKCS1SHA256Removed kSecPaddingPKCS1SHA384Removed kSecPaddingPKCS1SHA512Removed kSecPaddingSigRawRemoved SecPaddingAdded [SecAccessControlCreateFlags.And](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroland)Added [SecAccessControlCreateFlags.ApplicationPassword](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontrolapplicationpassword)Added [SecAccessControlCreateFlags.DevicePasscode](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1394326-devicepasscode)Added [SecAccessControlCreateFlags.Or](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1618071-or)Added [SecAccessControlCreateFlags.PrivateKeyUsage](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1617983-privatekeyusage)Added [SecAccessControlCreateFlags.TouchIDAny](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroltouchidany)Added [SecAccessControlCreateFlags.TouchIDCurrentSet](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1618004-touchidcurrentset)Added [SecPadding [struct]](https://developer.apple.com/documentation/security/secpadding)Added SecPadding.init(rawValue: UInt32)Added [SecPadding.None](https://developer.apple.com/documentation/security/secpadding/ksecpaddingnone)Added [SecPadding.OAEP](https://developer.apple.com/documentation/security/secpadding/ksecpaddingoaep)Added [SecPadding.PKCS1](https://developer.apple.com/documentation/security/secpadding/1401893-pkcs1)Added [SecPadding.PKCS1MD2](https://developer.apple.com/documentation/security/secpadding/1398958-pkcs1md2)Added [SecPadding.PKCS1MD5](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1md5)Added [SecPadding.PKCS1SHA1](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1sha1)Added [SecPadding.PKCS1SHA224](https://developer.apple.com/documentation/security/secpadding/1617939-pkcs1sha224)Added [SecPadding.PKCS1SHA256](https://developer.apple.com/documentation/security/secpadding/ksecpaddingpkcs1sha256)Added [SecPadding.PKCS1SHA384](https://developer.apple.com/documentation/security/secpadding/1617890-pkcs1sha384)Added [SecPadding.PKCS1SHA512](https://developer.apple.com/documentation/security/secpadding/1618005-pkcs1sha512)Added [SecPadding.SigRaw](https://developer.apple.com/documentation/security/secpadding/ksecpaddingsigraw)Added [kSecAttrSyncViewHint](https://developer.apple.com/documentation/security/ksecattrsyncviewhint)Added [kSecAttrTokenID](https://developer.apple.com/documentation/security/ksecattrtokenid)Added [kSecAttrTokenIDSecureEnclave](https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave)Added [kSecPolicyApplePayIssuerEncryption](https://developer.apple.com/documentation/security/ksecpolicyapplepayissuerencryption)Added [kSecPolicyMacAppStoreReceipt](https://developer.apple.com/documentation/security/ksecpolicymacappstorereceipt)Added [kSecTrustCertificateTransparency](https://developer.apple.com/documentation/security/ksectrustcertificatetransparency)Added [kSecTrustResultConfirm](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultconfirm)Added [kSecUseAuthenticationContext](https://developer.apple.com/documentation/security/ksecuseauthenticationcontext)Added [kSecUseAuthenticationUI](https://developer.apple.com/documentation/security/ksecuseauthenticationui)Added [kSecUseAuthenticationUIAllow](https://developer.apple.com/documentation/security/ksecuseauthenticationuiallow)Added [kSecUseAuthenticationUIFail](https://developer.apple.com/documentation/security/ksecuseauthenticationuifail)Added [kSecUseAuthenticationUISkip](https://developer.apple.com/documentation/security/ksecuseauthenticationuiskip)Modified [SecAccessControlCreateFlags [struct]](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecAccessControlCreateFlags : RawOptionSetType {     init(_ rawValue: CFIndex)     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get } } ``` | RawOptionSetType |
| To | ``` struct SecAccessControlCreateFlags : OptionSetType {     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get }     static var TouchIDAny: SecAccessControlCreateFlags { get }     static var TouchIDCurrentSet: SecAccessControlCreateFlags { get }     static var DevicePasscode: SecAccessControlCreateFlags { get }     static var Or: SecAccessControlCreateFlags { get }     static var And: SecAccessControlCreateFlags { get }     static var PrivateKeyUsage: SecAccessControlCreateFlags { get }     static var ApplicationPassword: SecAccessControlCreateFlags { get } } ``` | OptionSetType |

Modified [errSecAllocate](https://developer.apple.com/documentation/security/errsecallocate)

|  | Declaration |
| --- | --- |
| From | ``` var errSecAllocate: Int { get } ``` |
| To | ``` var errSecAllocate: OSStatus { get } ``` |

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

Modified [errSecDecode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdecode)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDecode: Int { get } ``` |
| To | ``` var errSecDecode: OSStatus { get } ``` |

Modified [errSecDuplicateItem](https://developer.apple.com/documentation/security/errsecduplicateitem)

|  | Declaration |
| --- | --- |
| From | ``` var errSecDuplicateItem: Int { get } ``` |
| To | ``` var errSecDuplicateItem: OSStatus { get } ``` |

Modified [errSecInteractionNotAllowed](https://developer.apple.com/documentation/security/errsecinteractionnotallowed)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInteractionNotAllowed: Int { get } ``` |
| To | ``` var errSecInteractionNotAllowed: OSStatus { get } ``` |

Modified [errSecInternalComponent](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinternalcomponent)

|  | Declaration |
| --- | --- |
| From | ``` var errSecInternalComponent: Int { get } ``` |
| To | ``` var errSecInternalComponent: OSStatus { get } ``` |

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

Modified [errSecNotAvailable](https://developer.apple.com/documentation/security/errsecnotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var errSecNotAvailable: Int { get } ``` |
| To | ``` var errSecNotAvailable: OSStatus { get } ``` |

Modified [errSecOpWr](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecopwr)

|  | Declaration |
| --- | --- |
| From | ``` var errSecOpWr: Int { get } ``` |
| To | ``` var errSecOpWr: OSStatus { get } ``` |

Modified [errSecParam](https://developer.apple.com/documentation/security/errsecparam)

|  | Declaration |
| --- | --- |
| From | ``` var errSecParam: Int { get } ``` |
| To | ``` var errSecParam: OSStatus { get } ``` |

Modified [errSecSuccess](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsuccess)

|  | Declaration |
| --- | --- |
| From | ``` var errSecSuccess: Int { get } ``` |
| To | ``` var errSecSuccess: OSStatus { get } ``` |

Modified [errSecUnimplemented](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunimplemented)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUnimplemented: Int { get } ``` |
| To | ``` var errSecUnimplemented: OSStatus { get } ``` |

Modified [errSecUserCanceled](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecusercanceled)

|  | Declaration |
| --- | --- |
| From | ``` var errSecUserCanceled: Int { get } ``` |
| To | ``` var errSecUserCanceled: OSStatus { get } ``` |

Modified [kSecAttrAccessControl](https://developer.apple.com/documentation/security/ksecattraccesscontrol)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessControl: CFStringRef ``` |
| To | ``` let kSecAttrAccessControl: CFString ``` |

Modified [kSecAttrAccessGroup](https://developer.apple.com/documentation/security/ksecattraccessgroup)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessGroup: CFStringRef ``` |
| To | ``` let kSecAttrAccessGroup: CFString ``` |

Modified [kSecAttrAccessible](https://developer.apple.com/documentation/security/ksecattraccessible)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessible: CFStringRef ``` |
| To | ``` let kSecAttrAccessible: CFString ``` |

Modified [kSecAttrAccessibleAfterFirstUnlock](https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlock)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleAfterFirstUnlock: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAfterFirstUnlock: CFString ``` |

Modified [kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccessibleAlways](https://developer.apple.com/documentation/security/ksecattraccessiblealways)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleAlways: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAlways: CFString ``` |

Modified [kSecAttrAccessibleAlwaysThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblealwaysthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleAlwaysThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleAlwaysThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccessibleWhenUnlocked](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlocked)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleWhenUnlocked: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleWhenUnlocked: CFString ``` |

Modified [kSecAttrAccessibleWhenUnlockedThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFStringRef ``` |
| To | ``` let kSecAttrAccessibleWhenUnlockedThisDeviceOnly: CFString ``` |

Modified [kSecAttrAccount](https://developer.apple.com/documentation/security/ksecattraccount)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAccount: CFStringRef ``` |
| To | ``` let kSecAttrAccount: CFString ``` |

Modified [kSecAttrApplicationLabel](https://developer.apple.com/documentation/security/ksecattrapplicationlabel)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrApplicationLabel: CFStringRef ``` |
| To | ``` let kSecAttrApplicationLabel: CFString ``` |

Modified [kSecAttrApplicationTag](https://developer.apple.com/documentation/security/ksecattrapplicationtag)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrApplicationTag: CFStringRef ``` |
| To | ``` let kSecAttrApplicationTag: CFString ``` |

Modified [kSecAttrAuthenticationType](https://developer.apple.com/documentation/security/ksecattrauthenticationtype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationType: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationType: CFString ``` |

Modified [kSecAttrAuthenticationTypeDefault](https://developer.apple.com/documentation/security/ksecattrauthenticationtypedefault)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeDefault: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeDefault: CFString ``` |

Modified [kSecAttrAuthenticationTypeDPA](https://developer.apple.com/documentation/security/ksecattrauthenticationtypedpa)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeDPA: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeDPA: CFString ``` |

Modified [kSecAttrAuthenticationTypeHTMLForm](https://developer.apple.com/documentation/security/ksecattrauthenticationtypehtmlform)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeHTMLForm: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeHTMLForm: CFString ``` |

Modified [kSecAttrAuthenticationTypeHTTPBasic](https://developer.apple.com/documentation/security/ksecattrauthenticationtypehttpbasic)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeHTTPBasic: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeHTTPBasic: CFString ``` |

Modified [kSecAttrAuthenticationTypeHTTPDigest](https://developer.apple.com/documentation/security/ksecattrauthenticationtypehttpdigest)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeHTTPDigest: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeHTTPDigest: CFString ``` |

Modified [kSecAttrAuthenticationTypeMSN](https://developer.apple.com/documentation/security/ksecattrauthenticationtypemsn)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeMSN: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeMSN: CFString ``` |

Modified [kSecAttrAuthenticationTypeNTLM](https://developer.apple.com/documentation/security/ksecattrauthenticationtypentlm)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeNTLM: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeNTLM: CFString ``` |

Modified [kSecAttrAuthenticationTypeRPA](https://developer.apple.com/documentation/security/ksecattrauthenticationtyperpa)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrAuthenticationTypeRPA: CFStringRef ``` |
| To | ``` let kSecAttrAuthenticationTypeRPA: CFString ``` |

Modified [kSecAttrCanDecrypt](https://developer.apple.com/documentation/security/ksecattrcandecrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanDecrypt: CFStringRef ``` |
| To | ``` let kSecAttrCanDecrypt: CFString ``` |

Modified [kSecAttrCanDerive](https://developer.apple.com/documentation/security/ksecattrcanderive)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanDerive: CFStringRef ``` |
| To | ``` let kSecAttrCanDerive: CFString ``` |

Modified [kSecAttrCanEncrypt](https://developer.apple.com/documentation/security/ksecattrcanencrypt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanEncrypt: CFStringRef ``` |
| To | ``` let kSecAttrCanEncrypt: CFString ``` |

Modified [kSecAttrCanSign](https://developer.apple.com/documentation/security/ksecattrcansign)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanSign: CFStringRef ``` |
| To | ``` let kSecAttrCanSign: CFString ``` |

Modified [kSecAttrCanUnwrap](https://developer.apple.com/documentation/security/ksecattrcanunwrap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanUnwrap: CFStringRef ``` |
| To | ``` let kSecAttrCanUnwrap: CFString ``` |

Modified [kSecAttrCanVerify](https://developer.apple.com/documentation/security/ksecattrcanverify)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanVerify: CFStringRef ``` |
| To | ``` let kSecAttrCanVerify: CFString ``` |

Modified [kSecAttrCanWrap](https://developer.apple.com/documentation/security/ksecattrcanwrap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCanWrap: CFStringRef ``` |
| To | ``` let kSecAttrCanWrap: CFString ``` |

Modified [kSecAttrCertificateEncoding](https://developer.apple.com/documentation/security/ksecattrcertificateencoding)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCertificateEncoding: CFStringRef ``` |
| To | ``` let kSecAttrCertificateEncoding: CFString ``` |

Modified [kSecAttrCertificateType](https://developer.apple.com/documentation/security/ksecattrcertificatetype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCertificateType: CFStringRef ``` |
| To | ``` let kSecAttrCertificateType: CFString ``` |

Modified [kSecAttrComment](https://developer.apple.com/documentation/security/ksecattrcomment)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrComment: CFStringRef ``` |
| To | ``` let kSecAttrComment: CFString ``` |

Modified [kSecAttrCreationDate](https://developer.apple.com/documentation/security/ksecattrcreationdate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCreationDate: CFStringRef ``` |
| To | ``` let kSecAttrCreationDate: CFString ``` |

Modified [kSecAttrCreator](https://developer.apple.com/documentation/security/ksecattrcreator)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrCreator: CFStringRef ``` |
| To | ``` let kSecAttrCreator: CFString ``` |

Modified [kSecAttrDescription](https://developer.apple.com/documentation/security/ksecattrdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrDescription: CFStringRef ``` |
| To | ``` let kSecAttrDescription: CFString ``` |

Modified [kSecAttrEffectiveKeySize](https://developer.apple.com/documentation/security/ksecattreffectivekeysize)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrEffectiveKeySize: CFStringRef ``` |
| To | ``` let kSecAttrEffectiveKeySize: CFString ``` |

Modified [kSecAttrGeneric](https://developer.apple.com/documentation/security/ksecattrgeneric)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrGeneric: CFStringRef ``` |
| To | ``` let kSecAttrGeneric: CFString ``` |

Modified [kSecAttrIsInvisible](https://developer.apple.com/documentation/security/ksecattrisinvisible)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrIsInvisible: CFStringRef ``` |
| To | ``` let kSecAttrIsInvisible: CFString ``` |

Modified [kSecAttrIsNegative](https://developer.apple.com/documentation/security/ksecattrisnegative)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrIsNegative: CFStringRef ``` |
| To | ``` let kSecAttrIsNegative: CFString ``` |

Modified [kSecAttrIsPermanent](https://developer.apple.com/documentation/security/ksecattrispermanent)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrIsPermanent: CFStringRef ``` |
| To | ``` let kSecAttrIsPermanent: CFString ``` |

Modified [kSecAttrIssuer](https://developer.apple.com/documentation/security/ksecattrissuer)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrIssuer: CFStringRef ``` |
| To | ``` let kSecAttrIssuer: CFString ``` |

Modified [kSecAttrKeyClass](https://developer.apple.com/documentation/security/ksecattrkeyclass)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyClass: CFStringRef ``` |
| To | ``` let kSecAttrKeyClass: CFString ``` |

Modified [kSecAttrKeyClassPrivate](https://developer.apple.com/documentation/security/ksecattrkeyclassprivate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyClassPrivate: CFStringRef ``` |
| To | ``` let kSecAttrKeyClassPrivate: CFString ``` |

Modified [kSecAttrKeyClassPublic](https://developer.apple.com/documentation/security/ksecattrkeyclasspublic)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyClassPublic: CFStringRef ``` |
| To | ``` let kSecAttrKeyClassPublic: CFString ``` |

Modified [kSecAttrKeyClassSymmetric](https://developer.apple.com/documentation/security/ksecattrkeyclasssymmetric)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyClassSymmetric: CFStringRef ``` |
| To | ``` let kSecAttrKeyClassSymmetric: CFString ``` |

Modified [kSecAttrKeySizeInBits](https://developer.apple.com/documentation/security/ksecattrkeysizeinbits)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeySizeInBits: CFStringRef ``` |
| To | ``` let kSecAttrKeySizeInBits: CFString ``` |

Modified [kSecAttrKeyType](https://developer.apple.com/documentation/security/ksecattrkeytype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyType: CFStringRef ``` |
| To | ``` let kSecAttrKeyType: CFString ``` |

Modified [kSecAttrKeyTypeEC](https://developer.apple.com/documentation/security/ksecattrkeytypeec)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyTypeEC: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeEC: CFString ``` |

Modified [kSecAttrKeyTypeRSA](https://developer.apple.com/documentation/security/ksecattrkeytypersa)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrKeyTypeRSA: CFStringRef ``` |
| To | ``` let kSecAttrKeyTypeRSA: CFString ``` |

Modified [kSecAttrLabel](https://developer.apple.com/documentation/security/ksecattrlabel)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrLabel: CFStringRef ``` |
| To | ``` let kSecAttrLabel: CFString ``` |

Modified [kSecAttrModificationDate](https://developer.apple.com/documentation/security/ksecattrmodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrModificationDate: CFStringRef ``` |
| To | ``` let kSecAttrModificationDate: CFString ``` |

Modified [kSecAttrPath](https://developer.apple.com/documentation/security/ksecattrpath)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrPath: CFStringRef ``` |
| To | ``` let kSecAttrPath: CFString ``` |

Modified [kSecAttrPort](https://developer.apple.com/documentation/security/ksecattrport)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrPort: CFStringRef ``` |
| To | ``` let kSecAttrPort: CFString ``` |

Modified [kSecAttrProtocol](https://developer.apple.com/documentation/security/ksecattrprotocol)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocol: CFStringRef ``` |
| To | ``` let kSecAttrProtocol: CFString ``` |

Modified [kSecAttrProtocolAFP](https://developer.apple.com/documentation/security/ksecattrprotocolafp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolAFP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolAFP: CFString ``` |

Modified [kSecAttrProtocolAppleTalk](https://developer.apple.com/documentation/security/ksecattrprotocolappletalk)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolAppleTalk: CFStringRef ``` |
| To | ``` let kSecAttrProtocolAppleTalk: CFString ``` |

Modified [kSecAttrProtocolDAAP](https://developer.apple.com/documentation/security/ksecattrprotocoldaap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolDAAP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolDAAP: CFString ``` |

Modified [kSecAttrProtocolEPPC](https://developer.apple.com/documentation/security/ksecattrprotocoleppc)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolEPPC: CFStringRef ``` |
| To | ``` let kSecAttrProtocolEPPC: CFString ``` |

Modified [kSecAttrProtocolFTP](https://developer.apple.com/documentation/security/ksecattrprotocolftp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolFTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTP: CFString ``` |

Modified [kSecAttrProtocolFTPAccount](https://developer.apple.com/documentation/security/ksecattrprotocolftpaccount)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolFTPAccount: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTPAccount: CFString ``` |

Modified [kSecAttrProtocolFTPProxy](https://developer.apple.com/documentation/security/ksecattrprotocolftpproxy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolFTPProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTPProxy: CFString ``` |

Modified [kSecAttrProtocolFTPS](https://developer.apple.com/documentation/security/ksecattrprotocolftps)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolFTPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolFTPS: CFString ``` |

Modified [kSecAttrProtocolHTTP](https://developer.apple.com/documentation/security/ksecattrprotocolhttp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolHTTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTP: CFString ``` |

Modified [kSecAttrProtocolHTTPProxy](https://developer.apple.com/documentation/security/ksecattrprotocolhttpproxy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolHTTPProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTPProxy: CFString ``` |

Modified [kSecAttrProtocolHTTPS](https://developer.apple.com/documentation/security/ksecattrprotocolhttps)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolHTTPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTPS: CFString ``` |

Modified [kSecAttrProtocolHTTPSProxy](https://developer.apple.com/documentation/security/ksecattrprotocolhttpsproxy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolHTTPSProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolHTTPSProxy: CFString ``` |

Modified [kSecAttrProtocolIMAP](https://developer.apple.com/documentation/security/ksecattrprotocolimap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolIMAP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIMAP: CFString ``` |

Modified [kSecAttrProtocolIMAPS](https://developer.apple.com/documentation/security/ksecattrprotocolimaps)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolIMAPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIMAPS: CFString ``` |

Modified [kSecAttrProtocolIPP](https://developer.apple.com/documentation/security/ksecattrprotocolipp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolIPP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIPP: CFString ``` |

Modified [kSecAttrProtocolIRC](https://developer.apple.com/documentation/security/ksecattrprotocolirc)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolIRC: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIRC: CFString ``` |

Modified [kSecAttrProtocolIRCS](https://developer.apple.com/documentation/security/ksecattrprotocolircs)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolIRCS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolIRCS: CFString ``` |

Modified [kSecAttrProtocolLDAP](https://developer.apple.com/documentation/security/ksecattrprotocolldap)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolLDAP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolLDAP: CFString ``` |

Modified [kSecAttrProtocolLDAPS](https://developer.apple.com/documentation/security/ksecattrprotocolldaps)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolLDAPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolLDAPS: CFString ``` |

Modified [kSecAttrProtocolNNTP](https://developer.apple.com/documentation/security/ksecattrprotocolnntp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolNNTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolNNTP: CFString ``` |

Modified [kSecAttrProtocolNNTPS](https://developer.apple.com/documentation/security/ksecattrprotocolnntps)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolNNTPS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolNNTPS: CFString ``` |

Modified [kSecAttrProtocolPOP3](https://developer.apple.com/documentation/security/ksecattrprotocolpop3)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolPOP3: CFStringRef ``` |
| To | ``` let kSecAttrProtocolPOP3: CFString ``` |

Modified [kSecAttrProtocolPOP3S](https://developer.apple.com/documentation/security/ksecattrprotocolpop3s)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolPOP3S: CFStringRef ``` |
| To | ``` let kSecAttrProtocolPOP3S: CFString ``` |

Modified [kSecAttrProtocolRTSP](https://developer.apple.com/documentation/security/ksecattrprotocolrtsp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolRTSP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolRTSP: CFString ``` |

Modified [kSecAttrProtocolRTSPProxy](https://developer.apple.com/documentation/security/ksecattrprotocolrtspproxy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolRTSPProxy: CFStringRef ``` |
| To | ``` let kSecAttrProtocolRTSPProxy: CFString ``` |

Modified [kSecAttrProtocolSMB](https://developer.apple.com/documentation/security/ksecattrprotocolsmb)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolSMB: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSMB: CFString ``` |

Modified [kSecAttrProtocolSMTP](https://developer.apple.com/documentation/security/ksecattrprotocolsmtp)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolSMTP: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSMTP: CFString ``` |

Modified [kSecAttrProtocolSOCKS](https://developer.apple.com/documentation/security/ksecattrprotocolsocks)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolSOCKS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSOCKS: CFString ``` |

Modified [kSecAttrProtocolSSH](https://developer.apple.com/documentation/security/ksecattrprotocolssh)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolSSH: CFStringRef ``` |
| To | ``` let kSecAttrProtocolSSH: CFString ``` |

Modified [kSecAttrProtocolTelnet](https://developer.apple.com/documentation/security/ksecattrprotocoltelnet)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolTelnet: CFStringRef ``` |
| To | ``` let kSecAttrProtocolTelnet: CFString ``` |

Modified [kSecAttrProtocolTelnetS](https://developer.apple.com/documentation/security/ksecattrprotocoltelnets)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrProtocolTelnetS: CFStringRef ``` |
| To | ``` let kSecAttrProtocolTelnetS: CFString ``` |

Modified [kSecAttrPublicKeyHash](https://developer.apple.com/documentation/security/ksecattrpublickeyhash)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrPublicKeyHash: CFStringRef ``` |
| To | ``` let kSecAttrPublicKeyHash: CFString ``` |

Modified [kSecAttrSecurityDomain](https://developer.apple.com/documentation/security/ksecattrsecuritydomain)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrSecurityDomain: CFStringRef ``` |
| To | ``` let kSecAttrSecurityDomain: CFString ``` |

Modified [kSecAttrSerialNumber](https://developer.apple.com/documentation/security/ksecattrserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrSerialNumber: CFStringRef ``` |
| To | ``` let kSecAttrSerialNumber: CFString ``` |

Modified [kSecAttrServer](https://developer.apple.com/documentation/security/ksecattrserver)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrServer: CFStringRef ``` |
| To | ``` let kSecAttrServer: CFString ``` |

Modified [kSecAttrService](https://developer.apple.com/documentation/security/ksecattrservice)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrService: CFStringRef ``` |
| To | ``` let kSecAttrService: CFString ``` |

Modified [kSecAttrSubject](https://developer.apple.com/documentation/security/ksecattrsubject)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrSubject: CFStringRef ``` |
| To | ``` let kSecAttrSubject: CFString ``` |

Modified [kSecAttrSubjectKeyID](https://developer.apple.com/documentation/security/ksecattrsubjectkeyid)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrSubjectKeyID: CFStringRef ``` |
| To | ``` let kSecAttrSubjectKeyID: CFString ``` |

Modified [kSecAttrSynchronizable](https://developer.apple.com/documentation/security/ksecattrsynchronizable)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrSynchronizable: CFStringRef ``` |
| To | ``` let kSecAttrSynchronizable: CFString ``` |

Modified [kSecAttrSynchronizableAny](https://developer.apple.com/documentation/security/ksecattrsynchronizableany)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrSynchronizableAny: CFStringRef ``` |
| To | ``` let kSecAttrSynchronizableAny: CFString ``` |

Modified [kSecAttrType](https://developer.apple.com/documentation/security/ksecattrtype)

|  | Declaration |
| --- | --- |
| From | ``` var kSecAttrType: CFStringRef ``` |
| To | ``` let kSecAttrType: CFString ``` |

Modified [kSecClass](https://developer.apple.com/documentation/security/ksecclass)

|  | Declaration |
| --- | --- |
| From | ``` var kSecClass: CFStringRef ``` |
| To | ``` let kSecClass: CFString ``` |

Modified [kSecClassCertificate](https://developer.apple.com/documentation/security/ksecclasscertificate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecClassCertificate: CFStringRef ``` |
| To | ``` let kSecClassCertificate: CFString ``` |

Modified [kSecClassGenericPassword](https://developer.apple.com/documentation/security/ksecclassgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` var kSecClassGenericPassword: CFStringRef ``` |
| To | ``` let kSecClassGenericPassword: CFString ``` |

Modified [kSecClassIdentity](https://developer.apple.com/documentation/security/ksecclassidentity)

|  | Declaration |
| --- | --- |
| From | ``` var kSecClassIdentity: CFStringRef ``` |
| To | ``` let kSecClassIdentity: CFString ``` |

Modified [kSecClassInternetPassword](https://developer.apple.com/documentation/security/ksecclassinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` var kSecClassInternetPassword: CFStringRef ``` |
| To | ``` let kSecClassInternetPassword: CFString ``` |

Modified [kSecClassKey](https://developer.apple.com/documentation/security/ksecclasskey)

|  | Declaration |
| --- | --- |
| From | ``` var kSecClassKey: CFStringRef ``` |
| To | ``` let kSecClassKey: CFString ``` |

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

Modified [kSecMatchCaseInsensitive](https://developer.apple.com/documentation/security/ksecmatchcaseinsensitive)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchCaseInsensitive: CFStringRef ``` |
| To | ``` let kSecMatchCaseInsensitive: CFString ``` |

Modified [kSecMatchEmailAddressIfPresent](https://developer.apple.com/documentation/security/ksecmatchemailaddressifpresent)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchEmailAddressIfPresent: CFStringRef ``` |
| To | ``` let kSecMatchEmailAddressIfPresent: CFString ``` |

Modified [kSecMatchIssuers](https://developer.apple.com/documentation/security/ksecmatchissuers)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchIssuers: CFStringRef ``` |
| To | ``` let kSecMatchIssuers: CFString ``` |

Modified [kSecMatchItemList](https://developer.apple.com/documentation/security/ksecmatchitemlist)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchItemList: CFStringRef ``` |
| To | ``` let kSecMatchItemList: CFString ``` |

Modified [kSecMatchLimit](https://developer.apple.com/documentation/security/ksecmatchlimit)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchLimit: CFStringRef ``` |
| To | ``` let kSecMatchLimit: CFString ``` |

Modified [kSecMatchLimitAll](https://developer.apple.com/documentation/security/ksecmatchlimitall)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchLimitAll: CFStringRef ``` |
| To | ``` let kSecMatchLimitAll: CFString ``` |

Modified [kSecMatchLimitOne](https://developer.apple.com/documentation/security/ksecmatchlimitone)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchLimitOne: CFStringRef ``` |
| To | ``` let kSecMatchLimitOne: CFString ``` |

Modified [kSecMatchPolicy](https://developer.apple.com/documentation/security/ksecmatchpolicy)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchPolicy: CFStringRef ``` |
| To | ``` let kSecMatchPolicy: CFString ``` |

Modified [kSecMatchSearchList](https://developer.apple.com/documentation/security/ksecmatchsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchSearchList: CFStringRef ``` |
| To | ``` let kSecMatchSearchList: CFString ``` |

Modified [kSecMatchSubjectContains](https://developer.apple.com/documentation/security/ksecmatchsubjectcontains)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchSubjectContains: CFStringRef ``` |
| To | ``` let kSecMatchSubjectContains: CFString ``` |

Modified [kSecMatchTrustedOnly](https://developer.apple.com/documentation/security/ksecmatchtrustedonly)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchTrustedOnly: CFStringRef ``` |
| To | ``` let kSecMatchTrustedOnly: CFString ``` |

Modified [kSecMatchValidOnDate](https://developer.apple.com/documentation/security/ksecmatchvalidondate)

|  | Declaration |
| --- | --- |
| From | ``` var kSecMatchValidOnDate: CFStringRef ``` |
| To | ``` let kSecMatchValidOnDate: CFString ``` |

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

Modified [kSecPrivateKeyAttrs](https://developer.apple.com/documentation/security/ksecprivatekeyattrs)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPrivateKeyAttrs: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPrivateKeyAttrs: CFString ``` |

Modified [kSecPropertyTypeError](https://developer.apple.com/documentation/security/ksecpropertytypeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeError: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPropertyTypeError: CFString ``` |

Modified [kSecPropertyTypeTitle](https://developer.apple.com/documentation/security/ksecpropertytypetitle)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPropertyTypeTitle: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPropertyTypeTitle: CFString ``` |

Modified [kSecPublicKeyAttrs](https://developer.apple.com/documentation/security/ksecpublickeyattrs)

|  | Declaration |
| --- | --- |
| From | ``` var kSecPublicKeyAttrs: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecPublicKeyAttrs: CFString ``` |

Modified [kSecReturnAttributes](https://developer.apple.com/documentation/security/ksecreturnattributes)

|  | Declaration |
| --- | --- |
| From | ``` var kSecReturnAttributes: CFStringRef ``` |
| To | ``` let kSecReturnAttributes: CFString ``` |

Modified [kSecReturnData](https://developer.apple.com/documentation/security/ksecreturndata)

|  | Declaration |
| --- | --- |
| From | ``` var kSecReturnData: CFStringRef ``` |
| To | ``` let kSecReturnData: CFString ``` |

Modified [kSecReturnPersistentRef](https://developer.apple.com/documentation/security/ksecreturnpersistentref)

|  | Declaration |
| --- | --- |
| From | ``` var kSecReturnPersistentRef: CFStringRef ``` |
| To | ``` let kSecReturnPersistentRef: CFString ``` |

Modified [kSecReturnRef](https://developer.apple.com/documentation/security/ksecreturnref)

|  | Declaration |
| --- | --- |
| From | ``` var kSecReturnRef: CFStringRef ``` |
| To | ``` let kSecReturnRef: CFString ``` |

Modified [kSecRevocationCRLMethod](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationcrlmethod)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationCRLMethod: Int { get } ``` |
| To | ``` var kSecRevocationCRLMethod: CFOptionFlags { get } ``` |

Modified [kSecRevocationNetworkAccessDisabled](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationnetworkaccessdisabled)

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

Modified [kSecRevocationUseAnyAvailableMethod](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationuseanyavailablemethod)

|  | Declaration |
| --- | --- |
| From | ``` var kSecRevocationUseAnyAvailableMethod: Int { get } ``` |
| To | ``` var kSecRevocationUseAnyAvailableMethod: CFOptionFlags { get } ``` |

Modified [kSecSharedPassword](https://developer.apple.com/documentation/security/ksecsharedpassword)

|  | Declaration |
| --- | --- |
| From | ``` var kSecSharedPassword: Unmanaged<AnyObject>! ``` |
| To | ``` let kSecSharedPassword: CFString ``` |

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

Modified [kSecUseItemList](https://developer.apple.com/documentation/security/ksecuseitemlist)

|  | Declaration |
| --- | --- |
| From | ``` var kSecUseItemList: CFStringRef ``` |
| To | ``` let kSecUseItemList: CFString ``` |

Modified [kSecUseNoAuthenticationUI](https://developer.apple.com/documentation/security/ksecusenoauthenticationui)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var kSecUseNoAuthenticationUI: CFStringRef ``` | -- |
| To | ``` let kSecUseNoAuthenticationUI: CFString ``` | iOS 9.0 |

Modified [kSecUseOperationPrompt](https://developer.apple.com/documentation/security/ksecuseoperationprompt)

|  | Declaration |
| --- | --- |
| From | ``` var kSecUseOperationPrompt: CFStringRef ``` |
| To | ``` let kSecUseOperationPrompt: CFString ``` |

Modified [kSecValueData](https://developer.apple.com/documentation/security/ksecvaluedata)

|  | Declaration |
| --- | --- |
| From | ``` var kSecValueData: CFStringRef ``` |
| To | ``` let kSecValueData: CFString ``` |

Modified [kSecValuePersistentRef](https://developer.apple.com/documentation/security/ksecvaluepersistentref)

|  | Declaration |
| --- | --- |
| From | ``` var kSecValuePersistentRef: CFStringRef ``` |
| To | ``` let kSecValuePersistentRef: CFString ``` |

Modified [kSecValueRef](https://developer.apple.com/documentation/security/ksecvalueref)

|  | Declaration |
| --- | --- |
| From | ``` var kSecValueRef: CFStringRef ``` |
| To | ``` let kSecValueRef: CFString ``` |

Modified [SecAccessControlCreateWithFlags(_: CFAllocator?, _: AnyObject, _: SecAccessControlCreateFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccessControl?](https://developer.apple.com/documentation/security/1394452-secaccesscontrolcreatewithflags)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator!, _ protection: AnyObject!, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<SecAccessControl>! ``` |
| To | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: AnyObject, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccessControl? ``` |

Modified [SecAddSharedWebCredential(_: CFString, _: CFString, _: CFString?, _: (CFError?) -> Void)](https://developer.apple.com/documentation/security/1617986-secaddsharedwebcredential)

|  | Declaration |
| --- | --- |
| From | ``` func SecAddSharedWebCredential(_ fqdn: CFString!, _ account: CFString!, _ password: CFString!, _ completionHandler: ((CFError!) -> Void)!) ``` |
| To | ``` func SecAddSharedWebCredential(_ fqdn: CFString, _ account: CFString, _ password: CFString?, _ completionHandler: (CFError?) -> Void) ``` |

Modified [SecCertificateCopyData(_: SecCertificate) -> CFData](https://developer.apple.com/documentation/security/1396080-seccertificatecopydata)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopyData(_ certificate: SecCertificate!) -> Unmanaged<CFData>! ``` |
| To | ``` func SecCertificateCopyData(_ certificate: SecCertificate) -> CFData ``` |

Modified [SecCertificateCopySubjectSummary(_: SecCertificate) -> CFString](https://developer.apple.com/documentation/security/1396041-seccertificatecopysubjectsummary)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopySubjectSummary(_ certificate: SecCertificate!) -> Unmanaged<CFString>! ``` |
| To | ``` func SecCertificateCopySubjectSummary(_ certificate: SecCertificate) -> CFString ``` |

Modified [SecCertificateCreateWithData(_: CFAllocator?, _: CFData) -> SecCertificate?](https://developer.apple.com/documentation/security/1396073-seccertificatecreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCreateWithData(_ allocator: CFAllocator!, _ data: CFData!) -> Unmanaged<SecCertificate>! ``` |
| To | ``` func SecCertificateCreateWithData(_ allocator: CFAllocator?, _ data: CFData) -> SecCertificate? ``` |

Modified [SecCreateSharedWebCredentialPassword() -> CFString?](https://developer.apple.com/documentation/security/1618050-seccreatesharedwebcredentialpass)

|  | Declaration |
| --- | --- |
| From | ``` func SecCreateSharedWebCredentialPassword() -> Unmanaged<CFString>! ``` |
| To | ``` func SecCreateSharedWebCredentialPassword() -> CFString? ``` |

Modified [SecIdentityCopyCertificate(_: SecIdentity, _: UnsafeMutablePointer<SecCertificate?>) -> OSStatus](https://developer.apple.com/documentation/security/1401305-secidentitycopycertificate)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopyCertificate(_ identityRef: SecIdentity!, _ certificateRef: UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus ``` |
| To | ``` func SecIdentityCopyCertificate(_ identityRef: SecIdentity, _ certificateRef: UnsafeMutablePointer<SecCertificate?>) -> OSStatus ``` |

Modified [SecIdentityCopyPrivateKey(_: SecIdentity, _: UnsafeMutablePointer<SecKey?>) -> OSStatus](https://developer.apple.com/documentation/security/1392978-secidentitycopyprivatekey)

|  | Declaration |
| --- | --- |
| From | ``` func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity!, _ privateKeyRef: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` |
| To | ``` func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity, _ privateKeyRef: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |

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

Modified [SecItemUpdate(_: CFDictionary, _: CFDictionary) -> OSStatus](https://developer.apple.com/documentation/security/1393617-secitemupdate)

|  | Declaration |
| --- | --- |
| From | ``` func SecItemUpdate(_ query: CFDictionary!, _ attributesToUpdate: CFDictionary!) -> OSStatus ``` |
| To | ``` func SecItemUpdate(_ query: CFDictionary, _ attributesToUpdate: CFDictionary) -> OSStatus ``` |

Modified [SecKeyDecrypt(_: SecKey, _: SecPadding, _: UnsafePointer<UInt8>, _: Int, _: UnsafeMutablePointer<UInt8>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1617894-seckeydecrypt)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyDecrypt(_ key: SecKey!, _ padding: SecPadding, _ cipherText: UnsafePointer<UInt8>, _ cipherTextLen: Int, _ plainText: UnsafeMutablePointer<UInt8>, _ plainTextLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SecKeyDecrypt(_ key: SecKey, _ padding: SecPadding, _ cipherText: UnsafePointer<UInt8>, _ cipherTextLen: Int, _ plainText: UnsafeMutablePointer<UInt8>, _ plainTextLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SecKeyEncrypt(_: SecKey, _: SecPadding, _: UnsafePointer<UInt8>, _: Int, _: UnsafeMutablePointer<UInt8>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1617956-seckeyencrypt)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyEncrypt(_ key: SecKey!, _ padding: SecPadding, _ plainText: UnsafePointer<UInt8>, _ plainTextLen: Int, _ cipherText: UnsafeMutablePointer<UInt8>, _ cipherTextLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SecKeyEncrypt(_ key: SecKey, _ padding: SecPadding, _ plainText: UnsafePointer<UInt8>, _ plainTextLen: Int, _ cipherText: UnsafeMutablePointer<UInt8>, _ cipherTextLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SecKeyGeneratePair(_: CFDictionary, _: UnsafeMutablePointer<SecKey?>, _: UnsafeMutablePointer<SecKey?>) -> OSStatus](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGeneratePair(_ parameters: CFDictionary!, _ publicKey: UnsafeMutablePointer<Unmanaged<SecKey>?>, _ privateKey: UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus ``` |
| To | ``` func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>, _ privateKey: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |

Modified [SecKeyGetBlockSize(_: SecKey) -> Int](https://developer.apple.com/documentation/security/1394222-seckeygetblocksize)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGetBlockSize(_ key: SecKey!) -> Int ``` |
| To | ``` func SecKeyGetBlockSize(_ key: SecKey) -> Int ``` |

Modified [SecKeyRawSign(_: SecKey, _: SecPadding, _: UnsafePointer<UInt8>, _: Int, _: UnsafeMutablePointer<UInt8>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/security/1618025-seckeyrawsign)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyRawSign(_ key: SecKey!, _ padding: SecPadding, _ dataToSign: UnsafePointer<UInt8>, _ dataToSignLen: Int, _ sig: UnsafeMutablePointer<UInt8>, _ sigLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func SecKeyRawSign(_ key: SecKey, _ padding: SecPadding, _ dataToSign: UnsafePointer<UInt8>, _ dataToSignLen: Int, _ sig: UnsafeMutablePointer<UInt8>, _ sigLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [SecKeyRawVerify(_: SecKey, _: SecPadding, _: UnsafePointer<UInt8>, _: Int, _: UnsafePointer<UInt8>, _: Int) -> OSStatus](https://developer.apple.com/documentation/security/1617884-seckeyrawverify)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyRawVerify(_ key: SecKey!, _ padding: SecPadding, _ signedData: UnsafePointer<UInt8>, _ signedDataLen: Int, _ sig: UnsafePointer<UInt8>, _ sigLen: Int) -> OSStatus ``` |
| To | ``` func SecKeyRawVerify(_ key: SecKey, _ padding: SecPadding, _ signedData: UnsafePointer<UInt8>, _ signedDataLen: Int, _ sig: UnsafePointer<UInt8>, _ sigLen: Int) -> OSStatus ``` |

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

Modified [SecPolicyCreateWithProperties(_: AnyObject, _: CFDictionary?) -> SecPolicy](https://developer.apple.com/documentation/security/1394568-secpolicycreatewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: AnyObject!, _ properties: CFDictionary!) -> Unmanaged<SecPolicy>! ``` |
| To | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: AnyObject, _ properties: CFDictionary?) -> SecPolicy ``` |

Modified [SecRequestSharedWebCredential(_: CFString?, _: CFString?, _: (CFArray?, CFError?) -> Void)](https://developer.apple.com/documentation/security/1617896-secrequestsharedwebcredential)

|  | Declaration |
| --- | --- |
| From | ``` func SecRequestSharedWebCredential(_ fqdn: CFString!, _ account: CFString!, _ completionHandler: ((CFArray!, CFError!) -> Void)!) ``` |
| To | ``` func SecRequestSharedWebCredential(_ fqdn: CFString?, _ account: CFString?, _ completionHandler: (CFArray?, CFError?) -> Void) ``` |

Modified [SecTrustCallback](https://developer.apple.com/documentation/security/sectrustcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SecTrustCallback = (SecTrust!, SecTrustResultType) -> Void ``` |
| To | ``` typealias SecTrustCallback = (SecTrust, SecTrustResultType) -> Void ``` |

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

Modified [SecTrustSetPolicies(_: SecTrust, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/security/1398399-sectrustsetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetPolicies(_ trust: SecTrust!, _ policies: AnyObject!) -> OSStatus ``` |
| To | ``` func SecTrustSetPolicies(_ trust: SecTrust, _ policies: AnyObject) -> OSStatus ``` |

Modified [SecTrustSetVerifyDate(_: SecTrust, _: CFDate) -> OSStatus](https://developer.apple.com/documentation/security/1397216-sectrustsetverifydate)

|  | Declaration |
| --- | --- |
| From | ``` func SecTrustSetVerifyDate(_ trust: SecTrust!, _ verifyDate: CFDate!) -> OSStatus ``` |
| To | ``` func SecTrustSetVerifyDate(_ trust: SecTrust, _ verifyDate: CFDate) -> OSStatus ``` |

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
