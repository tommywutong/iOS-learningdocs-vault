---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Security.html
archived_at: '2026-07-18T02:50:45.298165Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Security Changes for Objective-C

### Security

#### Authorization.h

Removed [kAuthorizationExternalFormLength](https://developer.apple.com/documentation/security/kauthorizationexternalformlength)Added [kAuthorizationExternalFormLength](https://developer.apple.com/documentation/security/kauthorizationexternalformlength)

#### CSCommon.h

Added [errSecCSBadTeamIdentifier](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadteamidentifier)Added [errSecCSInvalidAssociatedFileData](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidassociatedfiledata)Added [errSecCSInvalidTeamIdentifier](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidteamidentifier)Added [kSecCFErrorResourceSideband](https://developer.apple.com/documentation/security/kseccferrorresourcesideband)Added [kSecCSQuickCheck](https://developer.apple.com/documentation/security/seccsflags/kseccsquickcheck)

#### cssmapple.h

Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_24](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_24)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_25](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_25)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_26](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_26)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_27](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_27)Added [CSSM_APPLEFILEDL_DELETE_FILE](https://developer.apple.com/documentation/security/1434707-anonymous/cssm_applefiledl_delete_file)Added [CSSM_APPLEFILEDL_MAKE_COPY](https://developer.apple.com/documentation/security/cssm_applefiledl_make_copy)Added [#def kKeychainDbSuffix](https://developer.apple.com/documentation/security/kkeychaindbsuffix)

#### oids.h

Added [oidAnsip384r1](https://developer.apple.com/documentation/security/oidansip384r1)Added [oidAnsip521r1](https://developer.apple.com/documentation/security/oidansip521r1)Added [oidEcPrime192v1](https://developer.apple.com/documentation/security/oidecprime192v1)Added [oidEcPrime256v1](https://developer.apple.com/documentation/security/oidecprime256v1)

#### SecCertificate.h

Added [kSecKeyUsageAll](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusageall)Added [kSecKeyUsageContentCommitment](https://developer.apple.com/documentation/security/seckeyusage/1643244-contentcommitment)Added [kSecKeyUsageCritical](https://developer.apple.com/documentation/security/seckeyusage/1643252-critical)Added [kSecKeyUsageCRLSign](https://developer.apple.com/documentation/security/seckeyusage/1643245-crlsign)Added [kSecKeyUsageDataEncipherment](https://developer.apple.com/documentation/security/seckeyusage/1643243-dataencipherment)Added [kSecKeyUsageDecipherOnly](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagedecipheronly)Added [kSecKeyUsageDigitalSignature](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagedigitalsignature)Added [kSecKeyUsageEncipherOnly](https://developer.apple.com/documentation/security/seckeyusage/1643248-encipheronly)Added [kSecKeyUsageKeyAgreement](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagekeyagreement)Added [kSecKeyUsageKeyCertSign](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagekeycertsign)Added [kSecKeyUsageKeyEncipherment](https://developer.apple.com/documentation/security/seckeyusage/1643253-keyencipherment)Added [kSecKeyUsageNonRepudiation](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusagenonrepudiation)Added [kSecKeyUsageUnspecified](https://developer.apple.com/documentation/security/seckeyusage/kseckeyusageunspecified)Added [SecKeyUsage](https://developer.apple.com/documentation/security/seckeyusage)

#### SecCode.h

Added [kSecGuestAttributeAudit](https://developer.apple.com/documentation/security/ksecguestattributeaudit)

#### SecItem.h

Added [kSecAttrAccessGroupToken](https://developer.apple.com/documentation/security/ksecattraccessgrouptoken)Added [kSecAttrKeyTypeECSECPrimeRandom](https://developer.apple.com/documentation/security/ksecattrkeytypeecsecprimerandom)Added [kSecAttrTokenID](https://developer.apple.com/documentation/security/ksecattrtokenid)

#### SecKey.h

Added [kSecKeyAlgorithmECDHKeyExchangeCofactor](https://developer.apple.com/documentation/security/seckeyalgorithm/1643706-ecdhkeyexchangecofactor)Added [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha1)Added [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643981-ecdhkeyexchangecofactorx963sha22)Added [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangecofactorx963sha256)Added [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643670-ecdhkeyexchangecofactorx963sha38)Added [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA512](https://developer.apple.com/documentation/security/seckeyalgorithm/1643703-ecdhkeyexchangecofactorx963sha51)Added [kSecKeyAlgorithmECDHKeyExchangeStandard](https://developer.apple.com/documentation/security/seckeyalgorithm/1644051-ecdhkeyexchangestandard)Added [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha1)Added [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha224)Added [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha256)Added [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA384](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha384)Added [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdhkeyexchangestandardx963sha512)Added [kSecKeyAlgorithmECDSASignatureDigestX962](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962)Added [kSecKeyAlgorithmECDSASignatureDigestX962SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha1)Added [kSecKeyAlgorithmECDSASignatureDigestX962SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha224)Added [kSecKeyAlgorithmECDSASignatureDigestX962SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha256)Added [kSecKeyAlgorithmECDSASignatureDigestX962SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644044-ecdsasignaturedigestx962sha384)Added [kSecKeyAlgorithmECDSASignatureDigestX962SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturedigestx962sha512)Added [kSecKeyAlgorithmECDSASignatureMessageX962SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha1)Added [kSecKeyAlgorithmECDSASignatureMessageX962SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643717-ecdsasignaturemessagex962sha224)Added [kSecKeyAlgorithmECDSASignatureMessageX962SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmecdsasignaturemessagex962sha256)Added [kSecKeyAlgorithmECDSASignatureMessageX962SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1643714-ecdsasignaturemessagex962sha384)Added [kSecKeyAlgorithmECDSASignatureMessageX962SHA512](https://developer.apple.com/documentation/security/seckeyalgorithm/1643668-ecdsasignaturemessagex962sha512)Added [kSecKeyAlgorithmECDSASignatureRFC4754](https://developer.apple.com/documentation/security/seckeyalgorithm/1643720-ecdsasignaturerfc4754)Added [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA1AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha1aesgcm)Added [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha224aesgcm)Added [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA256AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091905-eciesencryptioncofactorx963sha25)Added [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA384AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptioncofactorx963sha384aesgcm)Added [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA512AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091900-eciesencryptioncofactorx963sha51)Added [kSecKeyAlgorithmECIESEncryptionStandardX963SHA1AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha1aesgcm)Added [kSecKeyAlgorithmECIESEncryptionStandardX963SHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha224aesgcm)Added [kSecKeyAlgorithmECIESEncryptionStandardX963SHA256AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091899-eciesencryptionstandardx963sha25)Added [kSecKeyAlgorithmECIESEncryptionStandardX963SHA384AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091903-eciesencryptionstandardx963sha38)Added [kSecKeyAlgorithmECIESEncryptionStandardX963SHA512AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmeciesencryptionstandardx963sha512aesgcm)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA1](https://developer.apple.com/documentation/security/seckeyalgorithm/1643711-rsaencryptionoaepsha1)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA1AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091901-rsaencryptionoaepsha1aesgcm)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643788-rsaencryptionoaepsha224)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA224AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha224aesgcm)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha256)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA256AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091907-rsaencryptionoaepsha256aesgcm)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644049-rsaencryptionoaepsha384)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA384AESGCM](https://developer.apple.com/documentation/security/seckeyalgorithm/2091906-rsaencryptionoaepsha384aesgcm)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha512)Added [kSecKeyAlgorithmRSAEncryptionOAEPSHA512AESGCM](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionoaepsha512aesgcm)Added [kSecKeyAlgorithmRSAEncryptionPKCS1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsaencryptionpkcs1)Added [kSecKeyAlgorithmRSAEncryptionRaw](https://developer.apple.com/documentation/security/seckeyalgorithm/1643716-rsaencryptionraw)Added [kSecKeyAlgorithmRSASignatureDigestPKCS1v15Raw](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15raw)Added [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha1)Added [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA224](https://developer.apple.com/documentation/security/seckeyalgorithm/1643784-rsasignaturedigestpkcs1v15sha224)Added [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA256](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha256)Added [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA384](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturedigestpkcs1v15sha384)Added [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA512](https://developer.apple.com/documentation/security/seckeyalgorithm/1644050-rsasignaturedigestpkcs1v15sha512)Added [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA1](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha1)Added [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA224](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha224)Added [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA256](https://developer.apple.com/documentation/security/seckeyalgorithm/1644047-rsasignaturemessagepkcs1v15sha25)Added [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA384](https://developer.apple.com/documentation/security/seckeyalgorithm/1644054-rsasignaturemessagepkcs1v15sha38)Added [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA512](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignaturemessagepkcs1v15sha512)Added [kSecKeyAlgorithmRSASignatureRaw](https://developer.apple.com/documentation/security/kseckeyalgorithmrsasignatureraw)Added [kSecKeyKeyExchangeParameterRequestedSize](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter/1643708-requestedsize)Added [kSecKeyKeyExchangeParameterSharedInfo](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter/1644059-sharedinfo)Added [kSecKeyOperationTypeDecrypt](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypedecrypt)Added [kSecKeyOperationTypeEncrypt](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypeencrypt)Added [kSecKeyOperationTypeKeyExchange](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypekeyexchange)Added [kSecKeyOperationTypeSign](https://developer.apple.com/documentation/security/seckeyoperationtype/kseckeyoperationtypesign)Added [kSecKeyOperationTypeVerify](https://developer.apple.com/documentation/security/seckeyoperationtype/verify)Added [SecKeyAlgorithm](https://developer.apple.com/documentation/security/seckeyalgorithm)Added [SecKeyCopyAttributes()](https://developer.apple.com/documentation/security/1643699-seckeycopyattributes)Added [SecKeyCopyExternalRepresentation()](https://developer.apple.com/documentation/security/1643698-seckeycopyexternalrepresentation)Added [SecKeyCopyKeyExchangeResult()](https://developer.apple.com/documentation/security/1644033-seckeycopykeyexchangeresult)Added [SecKeyCopyPublicKey()](https://developer.apple.com/documentation/security/1643774-seckeycopypublickey)Added [SecKeyCreateDecryptedData()](https://developer.apple.com/documentation/security/1644043-seckeycreatedecrypteddata)Added [SecKeyCreateEncryptedData()](https://developer.apple.com/documentation/security/1643957-seckeycreateencrypteddata)Added [SecKeyCreateRandomKey()](https://developer.apple.com/documentation/security/1823694-seckeycreaterandomkey)Added [SecKeyCreateSignature()](https://developer.apple.com/documentation/security/1643916-seckeycreatesignature)Added [SecKeyCreateWithData()](https://developer.apple.com/documentation/security/1643701-seckeycreatewithdata)Added [SecKeyIsAlgorithmSupported()](https://developer.apple.com/documentation/security/1644057-seckeyisalgorithmsupported)Added [SecKeyKeyExchangeParameter](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter)Added [SecKeyOperationType](https://developer.apple.com/documentation/security/seckeyoperationtype)Added [SecKeyVerifySignature()](https://developer.apple.com/documentation/security/1643715-seckeyverifysignature)

#### SecStaticCode.h

Added [kSecCSRestrictSidebandData](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsrestrictsidebanddata)

#### SecTask.h

Added [SecTaskCopySigningIdentifier()](https://developer.apple.com/documentation/security/1643737-sectaskcopysigningidentifier)

#### SecTrust.h

Added [kSecTrustCertificateTransparency](https://developer.apple.com/documentation/security/ksectrustcertificatetransparency)Added [kSecTrustCertificateTransparencyWhiteList](https://developer.apple.com/documentation/security/ksectrustcertificatetransparencywhitelist)

#### SecureTransport.h

Removed kSSLSessionStrengthPolicyATSv1Removed kSSLSessionStrengthPolicyATSv1_noPFSRemoved kSSLSessionStrengthPolicyDefaultRemoved SSLSessionStrengthPolicyRemoved SSLSetSessionStrengthPolicy()Added [kSSLSessionConfig_anonymous](https://developer.apple.com/documentation/security/ksslsessionconfig_anonymous)Added [kSSLSessionConfig_ATSv1](https://developer.apple.com/documentation/security/ksslsessionconfig_atsv1)Added [kSSLSessionConfig_ATSv1_noPFS](https://developer.apple.com/documentation/security/ksslsessionconfig_atsv1_nopfs)Added [kSSLSessionConfig_default](https://developer.apple.com/documentation/security/ksslsessionconfig_default)Added [kSSLSessionConfig_legacy](https://developer.apple.com/documentation/security/ksslsessionconfig_legacy)Added [kSSLSessionConfig_legacy_DHE](https://developer.apple.com/documentation/security/ksslsessionconfig_legacy_dhe)Added [kSSLSessionConfig_RC4_fallback](https://developer.apple.com/documentation/security/ksslsessionconfig_rc4_fallback)Added [kSSLSessionConfig_standard](https://developer.apple.com/documentation/security/ksslsessionconfig_standard)Added [kSSLSessionConfig_TLSv1_fallback](https://developer.apple.com/documentation/security/ksslsessionconfig_tlsv1_fallback)Added [kSSLSessionConfig_TLSv1_RC4_fallback](https://developer.apple.com/documentation/security/ksslsessionconfig_tlsv1_rc4_fallback)Added [kSSLSessionOptionAllowRenegotiation](https://developer.apple.com/documentation/security/sslsessionoption/allowrenegotiation)Added [SSLCopyRequestedPeerName()](https://developer.apple.com/documentation/security/1845288-sslcopyrequestedpeername)Added [SSLCopyRequestedPeerNameLength()](https://developer.apple.com/documentation/security/1845290-sslcopyrequestedpeernamelength)Added [SSLReHandshake()](https://developer.apple.com/documentation/security/1638073-sslrehandshake)Added [SSLSetSessionConfig()](https://developer.apple.com/documentation/security/1638095-sslsetsessionconfig)

#### SecurityFeatures.h (Added)

Added #def SECURITY_LEGACY_CSSMAdded #def SECURITY_LEGACY_SECURE_TRANSPORTAdded #def SECURITY_SECURITY_FEATURES_H

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
