---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/Security.html
archived_at: '2026-07-18T02:57:55.646434Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# Security Changes for Swift

### Security

Removed [SecAccessControlCreateFlags.init(rawValue: CFIndex)](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1395038-init)Removed [SecPadding.None](https://developer.apple.com/documentation/security/secpadding/ksecpaddingnone)Removed [kSecSharedPassword](https://developer.apple.com/documentation/security/ksecsharedpassword)Removed [kSecTrustResultConfirm](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultconfirm)Removed [kSecTrustResultDeny](https://developer.apple.com/documentation/security/sectrustresulttype/deny)Removed [kSecTrustResultFatalTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultfataltrustfailure)Removed [kSecTrustResultInvalid](https://developer.apple.com/documentation/security/sectrustresulttype/invalid)Removed [kSecTrustResultOtherError](https://developer.apple.com/documentation/security/sectrustresulttype/othererror)Removed [kSecTrustResultProceed](https://developer.apple.com/documentation/security/sectrustresulttype/proceed)Removed [kSecTrustResultRecoverableTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultrecoverabletrustfailure)Removed [kSecTrustResultUnspecified](https://developer.apple.com/documentation/security/sectrustresulttype/unspecified)Removed [SecAddSharedWebCredential(_: CFString, _: CFString, _: CFString?, _: (CFError?) -> Void)](https://developer.apple.com/documentation/security/1617986-secaddsharedwebcredential)Removed [SecCreateSharedWebCredentialPassword() -> CFString?](https://developer.apple.com/documentation/security/1618050-seccreatesharedwebcredentialpass)Removed [SecRequestSharedWebCredential(_: CFString?, _: CFString?, _: (CFArray?, CFError?) -> Void)](https://developer.apple.com/documentation/security/1617896-secrequestsharedwebcredential)Removed [SecTrustResultType](https://developer.apple.com/documentation/security/sectrustresulttype)Added [SecAccessControlCreateFlags.init(rawValue: CFOptionFlags)](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1395038-init)Added [SecKeyAlgorithm [struct]](https://developer.apple.com/documentation/security/seckeyalgorithm)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactor](https://developer.apple.com/documentation/security/seckeyalgorithm/1643706-ecdhkeyexchangecofactor)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643700-ecdhkeyexchangecofactorx963sha1)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha224)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha256)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643670-ecdhkeyexchangecofactorx963sha38)Added [SecKeyAlgorithm.ecdhKeyExchangeCofactorX963SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha512)Added [SecKeyAlgorithm.ecdhKeyExchangeStandard](https://developer.apple.com/documentation/security/seckeyalgorithm/1644051-ecdhkeyexchangestandard)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643695-ecdhkeyexchangestandardx963sha1)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha224)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha256)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643783-ecdhkeyexchangestandardx963sha38)Added [SecKeyAlgorithm.ecdhKeyExchangeStandardX963SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha512)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643707-ecdsasignaturedigestx962sha1)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha224)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha256)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644044-ecdsasignaturedigestx962sha384)Added [SecKeyAlgorithm.ecdsaSignatureDigestX962SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha512)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha1)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643717-ecdsasignaturemessagex962sha224)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha256)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA384](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha384)Added [SecKeyAlgorithm.ecdsaSignatureMessageX962SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha512)Added [SecKeyAlgorithm.ecdsaSignatureRFC4754](https://developer.apple.com/documentation/security/seckeyalgorithm/1643720-ecdsasignaturerfc4754)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA1AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091904-eciesencryptioncofactorx963sha1a)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha224aesgcm)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA256AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091905-eciesencryptioncofactorx963sha25)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA384AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha384aesgcm)Added [SecKeyAlgorithm.eciesEncryptionCofactorX963SHA512AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091900-eciesencryptioncofactorx963sha51)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA1AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091894-eciesencryptionstandardx963sha1a)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA224AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091909-eciesencryptionstandardx963sha22)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA256AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha256aesgcm)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA384AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091903-eciesencryptionstandardx963sha38)Added [SecKeyAlgorithm.eciesEncryptionStandardX963SHA512AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha512aesgcm)Added [SecKeyAlgorithm.init(rawValue: CFString)](https://developer.apple.com/documentation/security/seckeyalgorithm/1779565-init)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha1)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA1AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha1aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643788-rsaencryptionoaepsha224)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha224aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA256](https://developer.apple.com/documentation/security/seckeyalgorithm/1643688-rsaencryptionoaepsha256)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA256AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha256aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644049-rsaencryptionoaepsha384)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA384AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091906-rsaencryptionoaepsha384aesgcm)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha512)Added [SecKeyAlgorithm.rsaEncryptionOAEPSHA512AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091902-rsaencryptionoaepsha512aesgcm)Added [SecKeyAlgorithm.rsaEncryptionPKCS1](https://developer.apple.com/documentation/security/seckeyalgorithm/1644055-rsaencryptionpkcs1)Added [SecKeyAlgorithm.rsaEncryptionRaw](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionraw)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15Raw](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15raw)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha1)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643784-rsasignaturedigestpkcs1v15sha224)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha256)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643724-rsasignaturedigestpkcs1v15sha384)Added [SecKeyAlgorithm.rsaSignatureDigestPKCS1v15SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha512)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha1)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643795-rsasignaturemessagepkcs1v15sha22)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA256](https://developer.apple.com/documentation/security/seckeyalgorithm/1644047-rsasignaturemessagepkcs1v15sha25)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA384](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha384)Added [SecKeyAlgorithm.rsaSignatureMessagePKCS1v15SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha512)Added [SecKeyAlgorithm.rsaSignatureRaw](https://developer.apple.com/documentation/security/seckeyalgorithm/1643780-rsasignatureraw)Added [SecKeyKeyExchangeParameter [struct]](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter)Added [SecKeyKeyExchangeParameter.init(rawValue: CFString)](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter/1779566-init)Added [SecKeyKeyExchangeParameter.requestedSize](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter/1643708-requestedsize)Added [SecKeyKeyExchangeParameter.sharedInfo](https://developer.apple.com/documentation/security/kseckeykeyexchangeparametersharedinfo)Added [SecKeyOperationType [enum]](https://developer.apple.com/documentation/security/seckeyoperationtype)Added [SecKeyOperationType.decrypt](https://developer.apple.com/documentation/security/seckeyoperationtype/decrypt)Added [SecKeyOperationType.encrypt](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypeencrypt)Added [SecKeyOperationType.keyExchange](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypekeyexchange)Added [SecKeyOperationType.sign](https://developer.apple.com/documentation/security/seckeyoperationtype/sign)Added [SecKeyOperationType.verify](https://developer.apple.com/documentation/security/seckeyoperationtype/verify)Added [SecTrustResultType [enum]](https://developer.apple.com/documentation/security/sectrustresulttype)Added [SecTrustResultType.deny](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultdeny)Added [SecTrustResultType.fatalTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultfataltrustfailure)Added [SecTrustResultType.invalid](https://developer.apple.com/documentation/security/sectrustresulttype/invalid)Added [SecTrustResultType.otherError](https://developer.apple.com/documentation/security/sectrustresulttype/othererror)Added [SecTrustResultType.proceed](https://developer.apple.com/documentation/security/sectrustresulttype/proceed)Added [SecTrustResultType.recoverableTrustFailure](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultrecoverabletrustfailure)Added [SecTrustResultType.unspecified](https://developer.apple.com/documentation/security/sectrustresulttype/unspecified)Added [errSecVerifyFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecverifyfailed)Added [kSecAttrAccessGroupToken](https://developer.apple.com/documentation/security/ksecattraccessgrouptoken)Added [kSecAttrKeyTypeECSECPrimeRandom](https://developer.apple.com/documentation/security/ksecattrkeytypeecsecprimerandom)Added [kSecPolicyApplePassbookSigning](https://developer.apple.com/documentation/security/ksecpolicyapplepassbooksigning)Added [kSecPolicyTeamIdentifier](https://developer.apple.com/documentation/security/ksecpolicyteamidentifier)Added [kSecTrustCertificateTransparencyWhiteList](https://developer.apple.com/documentation/security/ksectrustcertificatetransparencywhitelist)Added [SecKeyCopyAttributes(_: SecKey) -> CFDictionary?](https://developer.apple.com/documentation/security/1643699-seckeycopyattributes)Added [SecKeyCopyExternalRepresentation(_: SecKey, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1643698-seckeycopyexternalrepresentation)Added [SecKeyCopyKeyExchangeResult(_: SecKey, _: SecKeyAlgorithm, _: SecKey, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1644033-seckeycopykeyexchangeresult)Added [SecKeyCopyPublicKey(_: SecKey) -> SecKey?](https://developer.apple.com/documentation/security/1643774-seckeycopypublickey)Added [SecKeyCreateDecryptedData(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1644043-seckeycreatedecrypteddata)Added [SecKeyCreateEncryptedData(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1643957-seckeycreateencrypteddata)Added [SecKeyCreateRandomKey(_: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1823694-seckeycreaterandomkey)Added [SecKeyCreateSignature(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](https://developer.apple.com/documentation/security/1643916-seckeycreatesignature)Added [SecKeyCreateWithData(_: CFData, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](https://developer.apple.com/documentation/security/1643701-seckeycreatewithdata)Added [SecKeyIsAlgorithmSupported(_: SecKey, _: SecKeyOperationType, _: SecKeyAlgorithm) -> Bool](https://developer.apple.com/documentation/security/1644057-seckeyisalgorithmsupported)Added [SecKeyVerifySignature(_: SecKey, _: SecKeyAlgorithm, _: CFData, _: CFData, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/security/1643715-seckeyverifysignature)Modified [SecAccessControlCreateFlags [struct]](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecAccessControlCreateFlags : OptionSetType {     init(rawValue rawValue: CFIndex)     static var UserPresence: SecAccessControlCreateFlags { get }     static var TouchIDAny: SecAccessControlCreateFlags { get }     static var TouchIDCurrentSet: SecAccessControlCreateFlags { get }     static var DevicePasscode: SecAccessControlCreateFlags { get }     static var Or: SecAccessControlCreateFlags { get }     static var And: SecAccessControlCreateFlags { get }     static var PrivateKeyUsage: SecAccessControlCreateFlags { get }     static var ApplicationPassword: SecAccessControlCreateFlags { get } } ``` | OptionSetType |
| To | ``` struct SecAccessControlCreateFlags : OptionSet {     init(rawValue rawValue: CFOptionFlags)     static var userPresence: SecAccessControlCreateFlags { get }     static var touchIDAny: SecAccessControlCreateFlags { get }     static var touchIDCurrentSet: SecAccessControlCreateFlags { get }     static var devicePasscode: SecAccessControlCreateFlags { get }     static var or: SecAccessControlCreateFlags { get }     static var and: SecAccessControlCreateFlags { get }     static var privateKeyUsage: SecAccessControlCreateFlags { get }     static var applicationPassword: SecAccessControlCreateFlags { get }     func intersect(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     func exclusiveOr(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     mutating func unionInPlace(_ other: SecAccessControlCreateFlags)     mutating func intersectInPlace(_ other: SecAccessControlCreateFlags)     mutating func exclusiveOrInPlace(_ other: SecAccessControlCreateFlags)     func isSubsetOf(_ other: SecAccessControlCreateFlags) -> Bool     func isDisjointWith(_ other: SecAccessControlCreateFlags) -> Bool     func isSupersetOf(_ other: SecAccessControlCreateFlags) -> Bool     mutating func subtractInPlace(_ other: SecAccessControlCreateFlags)     func isStrictSupersetOf(_ other: SecAccessControlCreateFlags) -> Bool     func isStrictSubsetOf(_ other: SecAccessControlCreateFlags) -> Bool } extension SecAccessControlCreateFlags {     func union(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     func intersection(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     func symmetricDifference(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags } extension SecAccessControlCreateFlags {     func contains(_ member: SecAccessControlCreateFlags) -> Bool     mutating func insert(_ newMember: SecAccessControlCreateFlags) -> (inserted: Bool, memberAfterInsert: SecAccessControlCreateFlags)     mutating func remove(_ member: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags?     mutating func update(with newMember: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags? } extension SecAccessControlCreateFlags {     convenience init()     mutating func formUnion(_ other: SecAccessControlCreateFlags)     mutating func formIntersection(_ other: SecAccessControlCreateFlags)     mutating func formSymmetricDifference(_ other: SecAccessControlCreateFlags) } extension SecAccessControlCreateFlags {     convenience init<S : Sequence where S.Iterator.Element == SecAccessControlCreateFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecAccessControlCreateFlags...)     mutating func subtract(_ other: SecAccessControlCreateFlags)     func isSubset(of other: SecAccessControlCreateFlags) -> Bool     func isSuperset(of other: SecAccessControlCreateFlags) -> Bool     func isDisjoint(with other: SecAccessControlCreateFlags) -> Bool     func subtracting(_ other: SecAccessControlCreateFlags) -> SecAccessControlCreateFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecAccessControlCreateFlags) -> Bool     func isStrictSubset(of other: SecAccessControlCreateFlags) -> Bool } ``` | OptionSet |

Modified [SecAccessControlCreateFlags.and](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroland)

|  | Declaration |
| --- | --- |
| From | ``` static var And: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var and: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.applicationPassword](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontrolapplicationpassword)

|  | Declaration |
| --- | --- |
| From | ``` static var ApplicationPassword: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var applicationPassword: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.devicePasscode](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1394326-devicepasscode)

|  | Declaration |
| --- | --- |
| From | ``` static var DevicePasscode: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var devicePasscode: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.or](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1618071-or)

|  | Declaration |
| --- | --- |
| From | ``` static var Or: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var or: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.privateKeyUsage](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1617983-privatekeyusage)

|  | Declaration |
| --- | --- |
| From | ``` static var PrivateKeyUsage: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var privateKeyUsage: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.touchIDAny](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroltouchidany)

|  | Declaration |
| --- | --- |
| From | ``` static var TouchIDAny: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var touchIDAny: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.touchIDCurrentSet](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1618004-touchidcurrentset)

|  | Declaration |
| --- | --- |
| From | ``` static var TouchIDCurrentSet: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var touchIDCurrentSet: SecAccessControlCreateFlags { get } ``` |

Modified [SecAccessControlCreateFlags.userPresence](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroluserpresence)

|  | Declaration |
| --- | --- |
| From | ``` static var UserPresence: SecAccessControlCreateFlags { get } ``` |
| To | ``` static var userPresence: SecAccessControlCreateFlags { get } ``` |

Modified [SecPadding [struct]](https://developer.apple.com/documentation/security/secpadding)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SecPadding : OptionSetType {     init(rawValue rawValue: UInt32)     static var None: SecPadding { get }     static var PKCS1: SecPadding { get }     static var OAEP: SecPadding { get }     static var SigRaw: SecPadding { get }     static var PKCS1MD2: SecPadding { get }     static var PKCS1MD5: SecPadding { get }     static var PKCS1SHA1: SecPadding { get }     static var PKCS1SHA224: SecPadding { get }     static var PKCS1SHA256: SecPadding { get }     static var PKCS1SHA384: SecPadding { get }     static var PKCS1SHA512: SecPadding { get } } ``` | OptionSetType |
| To | ``` struct SecPadding : OptionSet {     init(rawValue rawValue: UInt32)     static var none: SecPadding { get }     static var PKCS1: SecPadding { get }     static var OAEP: SecPadding { get }     static var sigRaw: SecPadding { get }     static var PKCS1MD2: SecPadding { get }     static var PKCS1MD5: SecPadding { get }     static var PKCS1SHA1: SecPadding { get }     static var PKCS1SHA224: SecPadding { get }     static var PKCS1SHA256: SecPadding { get }     static var PKCS1SHA384: SecPadding { get }     static var PKCS1SHA512: SecPadding { get }     func intersect(_ other: SecPadding) -> SecPadding     func exclusiveOr(_ other: SecPadding) -> SecPadding     mutating func unionInPlace(_ other: SecPadding)     mutating func intersectInPlace(_ other: SecPadding)     mutating func exclusiveOrInPlace(_ other: SecPadding)     func isSubsetOf(_ other: SecPadding) -> Bool     func isDisjointWith(_ other: SecPadding) -> Bool     func isSupersetOf(_ other: SecPadding) -> Bool     mutating func subtractInPlace(_ other: SecPadding)     func isStrictSupersetOf(_ other: SecPadding) -> Bool     func isStrictSubsetOf(_ other: SecPadding) -> Bool } extension SecPadding {     func union(_ other: SecPadding) -> SecPadding     func intersection(_ other: SecPadding) -> SecPadding     func symmetricDifference(_ other: SecPadding) -> SecPadding } extension SecPadding {     func contains(_ member: SecPadding) -> Bool     mutating func insert(_ newMember: SecPadding) -> (inserted: Bool, memberAfterInsert: SecPadding)     mutating func remove(_ member: SecPadding) -> SecPadding?     mutating func update(with newMember: SecPadding) -> SecPadding? } extension SecPadding {     convenience init()     mutating func formUnion(_ other: SecPadding)     mutating func formIntersection(_ other: SecPadding)     mutating func formSymmetricDifference(_ other: SecPadding) } extension SecPadding {     convenience init<S : Sequence where S.Iterator.Element == SecPadding>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SecPadding...)     mutating func subtract(_ other: SecPadding)     func isSubset(of other: SecPadding) -> Bool     func isSuperset(of other: SecPadding) -> Bool     func isDisjoint(with other: SecPadding) -> Bool     func subtracting(_ other: SecPadding) -> SecPadding     var isEmpty: Bool { get }     func isStrictSuperset(of other: SecPadding) -> Bool     func isStrictSubset(of other: SecPadding) -> Bool } ``` | OptionSet |

Modified [SecPadding.sigRaw](https://developer.apple.com/documentation/security/secpadding/ksecpaddingsigraw)

|  | Declaration |
| --- | --- |
| From | ``` static var SigRaw: SecPadding { get } ``` |
| To | ``` static var sigRaw: SecPadding { get } ``` |

Modified [SecAccessControlCreateWithFlags(_: CFAllocator?, _: CFTypeRef, _: SecAccessControlCreateFlags, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl?](https://developer.apple.com/documentation/security/1394452-secaccesscontrolcreatewithflags)

|  | Declaration |
| --- | --- |
| From | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: AnyObject, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> SecAccessControl? ``` |
| To | ``` func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: CFTypeRef, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl? ``` |

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

Modified [SecKeyGeneratePair(_: CFDictionary, _: UnsafeMutablePointer<SecKey?>?, _: UnsafeMutablePointer<SecKey?>?) -> OSStatus](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair)

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>, _ privateKey: UnsafeMutablePointer<SecKey?>) -> OSStatus ``` |
| To | ``` func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>?, _ privateKey: UnsafeMutablePointer<SecKey?>?) -> OSStatus ``` |

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
| From | ``` func SecPolicyCreateWithProperties(_ policyIdentifier: AnyObject, _ properties: CFDictionary?) -> SecPolicy ``` |
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
