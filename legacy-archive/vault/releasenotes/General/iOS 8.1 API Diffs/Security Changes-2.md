---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Security.html
archived_at: '2026-07-18T02:56:16.128385Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Security Changes

## Security

Removed SecAccessControlCreateFlags.valueAdded SecAccessControlCreateFlags.init(rawValue: CFIndex)Modified SecAccessControlCreateFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SecAccessControlCreateFlags : RawOptionSetType {     init(_ value: CFIndex)     var value: CFIndex     static var UserPresence: SecAccessControlCreateFlags { get } } ``` |
| To | ``` struct SecAccessControlCreateFlags : RawOptionSetType {     init(_ rawValue: CFIndex)     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get } } ``` |

Modified SecAccessControlCreateFlags.init(_: CFIndex)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFIndex) ``` |
| To | ``` init(_ rawValue: CFIndex) ``` |

Modified SecCertificateCopyData(SecCertificate!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecCertificateCopySubjectSummary(SecCertificate!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecCertificateCreateWithData(CFAllocator!, CFData!) -> Unmanaged<SecCertificate>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecCertificateGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecIdentityCopyCertificate(SecIdentity!, UnsafeMutablePointer<Unmanaged<SecCertificate>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecIdentityCopyPrivateKey(SecIdentity!, UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecIdentityGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecItemAdd(CFDictionary!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecItemCopyMatching(CFDictionary!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecItemDelete(CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecItemUpdate(CFDictionary!, CFDictionary!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyDecrypt(SecKey!, SecPadding, UnsafePointer<UInt8>, UInt, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyEncrypt(SecKey!, SecPadding, UnsafePointer<UInt8>, UInt, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyGeneratePair(CFDictionary!, UnsafeMutablePointer<Unmanaged<SecKey>?>, UnsafeMutablePointer<Unmanaged<SecKey>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyGetBlockSize(SecKey!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyRawSign(SecKey!, SecPadding, UnsafePointer<UInt8>, UInt, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<UInt>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecKeyRawVerify(SecKey!, SecPadding, UnsafePointer<UInt8>, UInt, UnsafePointer<UInt8>, UInt) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecPKCS12Import(CFData!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecPolicyCopyProperties(SecPolicy!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecPolicyCreateBasicX509() -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecPolicyCreateRevocation(CFOptionFlags) -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecPolicyCreateSSL(Boolean, CFString!) -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecPolicyCreateWithProperties(AnyObject!, CFDictionary!) -> Unmanaged<SecPolicy>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecPolicyGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecRandomCopyBytes(SecRandom!, UInt, UnsafeMutablePointer<UInt8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustCopyCustomAnchorCertificates(SecTrust!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustCopyExceptions(SecTrust!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified SecTrustCopyPolicies(SecTrust!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustCopyProperties(SecTrust!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustCopyPublicKey(SecTrust!) -> Unmanaged<SecKey>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustCopyResult(SecTrust!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustCreateWithCertificates(AnyObject!, AnyObject!, UnsafeMutablePointer<Unmanaged<SecTrust>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustEvaluate(SecTrust!, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustEvaluateAsync(SecTrust!, dispatch_queue_t!, SecTrustCallback!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustGetCertificateAtIndex(SecTrust!, CFIndex) -> Unmanaged<SecCertificate>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustGetCertificateCount(SecTrust!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustGetNetworkFetchAllowed(SecTrust!, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustGetTrustResult(SecTrust!, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustGetVerifyTime(SecTrust!) -> CFAbsoluteTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustSetAnchorCertificates(SecTrust!, CFArray!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustSetAnchorCertificatesOnly(SecTrust!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified SecTrustSetExceptions(SecTrust!, CFData!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified SecTrustSetNetworkFetchAllowed(SecTrust!, Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustSetOCSPResponse(SecTrust!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SecTrustSetPolicies(SecTrust!, AnyObject!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SecTrustSetVerifyDate(SecTrust!, CFDate!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

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

Modified kSecAttrAccessGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kSecAttrAccessible

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccessibleAfterFirstUnlock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccessibleAlways

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccessibleAlwaysThisDeviceOnly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccessibleWhenUnlocked

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccessibleWhenUnlockedThisDeviceOnly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrAccount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrApplicationLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrApplicationTag

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeDPA

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeHTMLForm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeHTTPBasic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeHTTPDigest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeMSN

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeNTLM

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrAuthenticationTypeRPA

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanDecrypt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanDerive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanEncrypt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanSign

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanUnwrap

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanVerify

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCanWrap

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCertificateEncoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCertificateType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrComment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCreationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrCreator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrEffectiveKeySize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrGeneric

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrIsInvisible

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrIsNegative

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrIsPermanent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrIssuer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeyClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeyClassPrivate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeyClassPublic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeyClassSymmetric

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeySizeInBits

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeyType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrKeyTypeEC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kSecAttrKeyTypeRSA

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrModificationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrPath

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocol

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolAFP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolAppleTalk

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolDAAP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolEPPC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolFTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolFTPAccount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolFTPProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolFTPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolHTTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolHTTPProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolHTTPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolHTTPSProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolIMAP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolIMAPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolIPP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolIRC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolIRCS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolLDAP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolLDAPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolNNTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolNNTPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolPOP3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolPOP3S

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolRTSP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolRTSPProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolSMB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolSMTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolSOCKS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolSSH

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolTelnet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrProtocolTelnetS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrPublicKeyHash

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrSecurityDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrServer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrService

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrSubject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrSubjectKeyID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecAttrSynchronizable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecAttrSynchronizableAny

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecAttrType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecClass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecClassCertificate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecClassGenericPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecClassIdentity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecClassInternetPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecClassKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecImportExportPassphrase

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecImportItemCertChain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecImportItemIdentity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecImportItemKeyID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecImportItemLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecImportItemTrust

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchCaseInsensitive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchEmailAddressIfPresent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchIssuers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchItemList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchLimit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchLimitAll

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchLimitOne

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchPolicy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchSearchList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchSubjectContains

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchTrustedOnly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecMatchValidOnDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecPolicyAppleCodeSigning

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleEAP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleIDValidation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleIPsec

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleRevocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleSMIME

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleSSL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleTimeStamping

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyAppleX509Basic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyClient

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyOid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPolicyRevocationFlags

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPrivateKeyAttrs

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecPropertyTypeError

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPropertyTypeTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecPublicKeyAttrs

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecRandomDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecReturnAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecReturnData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecReturnPersistentRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecReturnRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecTrustEvaluationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecTrustExtendedValidation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecTrustOrganizationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecTrustResultValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecTrustRevocationChecked

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecTrustRevocationValidUntilDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kSecUseItemList

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecValueData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecValuePersistentRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kSecValueRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

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
