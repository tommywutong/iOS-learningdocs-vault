---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Security.html
archived_at: '2026-07-18T02:54:21.633172Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Security Changes

## Security

CSCommon.hAdded [errSecCSBadCallbackValue](https://developer.apple.com/documentation/security/errseccsbadcallbackvalue)Added [errSecCSBadNestedCode](https://developer.apple.com/documentation/security/errseccsbadnestedcode)Added [errSecCSHelperFailed](https://developer.apple.com/documentation/security/errseccshelperfailed)Added [errSecCSResourceDirectoryFailed](https://developer.apple.com/documentation/security/errseccsresourcedirectoryfailed)Added [errSecCSUnsignedNestedCode](https://developer.apple.com/documentation/security/errseccsunsignednestedcode)Added [errSecCSVetoed](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsvetoed)Added [kSecCodeSignatureEnforcement](https://developer.apple.com/documentation/security/seccodesignatureflags/1395087-enforcement)Added [kSecCodeSignatureRestrict](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignaturerestrict)CipherSuite.hAdded [TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_3des_ede_cbc_sha)Added [TLS_DHE_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_128_cbc_sha)Added [TLS_DHE_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_128_cbc_sha256)Added [TLS_DHE_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_128_gcm_sha256)Added [TLS_DHE_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_256_cbc_sha)Added [TLS_DHE_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_dhe_psk_with_aes_256_cbc_sha384)Added [TLS_DHE_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_aes_256_gcm_sha384)Added [TLS_DHE_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_null_sha)Added [TLS_DHE_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_null_sha256)Added [TLS_DHE_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_psk_with_null_sha384)Added [TLS_DHE_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_dhe_psk_with_rc4_128_sha)Added [TLS_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_3des_ede_cbc_sha)Added [TLS_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_cbc_sha)Added [TLS_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_cbc_sha256)Added [TLS_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_128_gcm_sha256)Added [TLS_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_cbc_sha)Added [TLS_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_aes_256_cbc_sha384)Added [TLS_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_psk_with_aes_256_gcm_sha384)Added [TLS_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_null_sha)Added [TLS_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_psk_with_null_sha256)Added [TLS_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_null_sha384)Added [TLS_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_psk_with_rc4_128_sha)Added [TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_3des_ede_cbc_sha)Added [TLS_RSA_PSK_WITH_AES_128_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_128_cbc_sha)Added [TLS_RSA_PSK_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_128_cbc_sha256)Added [TLS_RSA_PSK_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_128_gcm_sha256)Added [TLS_RSA_PSK_WITH_AES_256_CBC_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_aes_256_cbc_sha)Added [TLS_RSA_PSK_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_256_cbc_sha384)Added [TLS_RSA_PSK_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_aes_256_gcm_sha384)Added [TLS_RSA_PSK_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_null_sha)Added [TLS_RSA_PSK_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_psk_with_null_sha256)Added [TLS_RSA_PSK_WITH_NULL_SHA384](https://developer.apple.com/documentation/security/tls_rsa_psk_with_null_sha384)Added [TLS_RSA_PSK_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_rsa_psk_with_rc4_128_sha)SecBase.hAdded [errSecBadReq](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecbadreq)Added [errSecCoreFoundationUnknown](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccorefoundationunknown)Added [errSecDskFull](https://developer.apple.com/documentation/security/errsecdskfull)Added [errSecIO](https://developer.apple.com/documentation/security/errsecio)Added [errSecInternalComponent](https://developer.apple.com/documentation/security/errsecinternalcomponent)Added [errSecUserCanceled](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecusercanceled)Added [errSecWrPerm](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecwrperm)SecCode.hRemoved kSecCodeSignerFlagsAdded [kSecCSUseAllArchitectures](https://developer.apple.com/documentation/security/1569510-code_signing_architecture_flags/kseccsuseallarchitectures)Added [kSecCodeInfoFlags](https://developer.apple.com/documentation/security/kseccodeinfoflags)Added [kSecGuestAttributeDynamicCode](https://developer.apple.com/documentation/security/ksecguestattributedynamiccode)Added [kSecGuestAttributeDynamicCodeInfoPlist](https://developer.apple.com/documentation/security/ksecguestattributedynamiccodeinfoplist)SecItem.hAdded [kSecAttrAccessGroup](https://developer.apple.com/documentation/security/ksecattraccessgroup)Added [kSecAttrAccessible](https://developer.apple.com/documentation/security/ksecattraccessible)Added [kSecAttrAccessibleAfterFirstUnlock](https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlock)Added [kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly)Added [kSecAttrAccessibleAlways](https://developer.apple.com/documentation/security/ksecattraccessiblealways)Added [kSecAttrAccessibleAlwaysThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblealwaysthisdeviceonly)Added [kSecAttrAccessibleWhenUnlocked](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlocked)Added [kSecAttrAccessibleWhenUnlockedThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly)Added [kSecAttrIsExtractable](https://developer.apple.com/documentation/security/ksecattrisextractable)Added [kSecAttrIsSensitive](https://developer.apple.com/documentation/security/ksecattrissensitive)Added [kSecAttrKeyTypeEC](https://developer.apple.com/documentation/security/ksecattrkeytypeec)Added [kSecAttrSynchronizable](https://developer.apple.com/documentation/security/ksecattrsynchronizable)Added [kSecAttrSynchronizableAny](https://developer.apple.com/documentation/security/ksecattrsynchronizableany)SecKeychainItem.hModified [kSecAppleSharePasswordItemClass](https://developer.apple.com/documentation/security/secitemclass/ksecapplesharepassworditemclass)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

SecPolicy.hAdded [SecPolicyCreateRevocation()](https://developer.apple.com/documentation/security/1400026-secpolicycreaterevocation)Added [SecPolicyCreateWithProperties()](https://developer.apple.com/documentation/security/1394568-secpolicycreatewithproperties)Added [kSecPolicyApplePassbookSigning](https://developer.apple.com/documentation/security/ksecpolicyapplepassbooksigning)Added [kSecPolicyAppleRevocation](https://developer.apple.com/documentation/security/ksecpolicyapplerevocation)Added [kSecPolicyRevocationFlags](https://developer.apple.com/documentation/security/ksecpolicyrevocationflags)Added [kSecPolicyTeamIdentifier](https://developer.apple.com/documentation/security/ksecpolicyteamidentifier)Added [kSecRevocationCRLMethod](https://developer.apple.com/documentation/security/ksecrevocationcrlmethod)Added [kSecRevocationNetworkAccessDisabled](https://developer.apple.com/documentation/security/ksecrevocationnetworkaccessdisabled)Added [kSecRevocationOCSPMethod](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationocspmethod)Added [kSecRevocationPreferCRL](https://developer.apple.com/documentation/security/ksecrevocationprefercrl)Added [kSecRevocationRequirePositiveResponse](https://developer.apple.com/documentation/security/1563600-revocation_policy_constants/ksecrevocationrequirepositiveresponse)Added [kSecRevocationUseAnyAvailableMethod](https://developer.apple.com/documentation/security/ksecrevocationuseanyavailablemethod)Modified [SecPolicyCreateWithOID()](https://developer.apple.com/documentation/security/1563598-secpolicycreatewithoid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SecPolicyGetOID()](https://developer.apple.com/documentation/security/1563594-secpolicygetoid)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecPolicyGetTPHandle()](https://developer.apple.com/documentation/security/1563593-secpolicygettphandle)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecPolicyGetValue()](https://developer.apple.com/documentation/security/1563595-secpolicygetvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecPolicySetProperties()](https://developer.apple.com/documentation/security/1563596-secpolicysetproperties)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SecPolicySetValue()](https://developer.apple.com/documentation/security/1563597-secpolicysetvalue)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [kSecPolicyAppleiChat](https://developer.apple.com/documentation/security/ksecpolicyappleichat)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

SecStaticCode.hAdded [kSecCodeAttributeUniversalFileOffset](https://developer.apple.com/documentation/security/kseccodeattributeuniversalfileoffset)SecTrust.hAdded [SecTrustCopyExceptions()](https://developer.apple.com/documentation/security/1400106-sectrustcopyexceptions)Added [SecTrustCopyResult()](https://developer.apple.com/documentation/security/1398612-sectrustcopyresult)Added [SecTrustGetNetworkFetchAllowed()](https://developer.apple.com/documentation/security/1400259-sectrustgetnetworkfetchallowed)Added [SecTrustSetExceptions()](https://developer.apple.com/documentation/security/1395676-sectrustsetexceptions)Added [SecTrustSetNetworkFetchAllowed()](https://developer.apple.com/documentation/security/1395083-sectrustsetnetworkfetchallowed)Added [SecTrustSetOCSPResponse()](https://developer.apple.com/documentation/security/1400880-sectrustsetocspresponse)Added [kSecTrustEvaluationDate](https://developer.apple.com/documentation/security/ksectrustevaluationdate)Added [kSecTrustExtendedValidation](https://developer.apple.com/documentation/security/ksectrustextendedvalidation)Added [kSecTrustOrganizationName](https://developer.apple.com/documentation/security/ksectrustorganizationname)Added [kSecTrustResultValue](https://developer.apple.com/documentation/security/ksectrustresultvalue)Added [kSecTrustRevocationChecked](https://developer.apple.com/documentation/security/ksectrustrevocationchecked)Added [kSecTrustRevocationValidUntilDate](https://developer.apple.com/documentation/security/ksectrustrevocationvaliduntildate)Modified [SecTrustCreateWithCertificates()](https://developer.apple.com/documentation/security/1401555-sectrustcreatewithcertificates)

|  | Declaration |
| --- | --- |
| From | OSStatus SecTrustCreateWithCertificates ( CFArrayRef certificates, CFTypeRef policies, SecTrustRef \*trustRef); |
| To | OSStatus SecTrustCreateWithCertificates ( CFTypeRef certificates, CFTypeRef policies, SecTrustRef \*trust); |

Modified [SecTrustGetCssmResult()](https://developer.apple.com/documentation/security/1524311-sectrustgetcssmresult)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecTrustGetCssmResultCode()](https://developer.apple.com/documentation/security/1524327-sectrustgetcssmresultcode)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecTrustGetResult()](https://developer.apple.com/documentation/security/1524331-sectrustgetresult)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecTrustGetTPHandle()](https://developer.apple.com/documentation/security/1524309-sectrustgettphandle)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecTrustGetTrustResult()](https://developer.apple.com/documentation/security/1396077-sectrustgettrustresult)

|  | Declaration |
| --- | --- |
| From | OSStatus SecTrustGetTrustResult ( SecTrustRef trustRef, SecTrustResultType \*result); |
| To | OSStatus SecTrustGetTrustResult ( SecTrustRef trust, SecTrustResultType \*result); |

Modified [SecTrustSetParameters()](https://developer.apple.com/documentation/security/1524326-sectrustsetparameters)

|  | Introduction |
| --- | --- |
| From | OS X 10.0 |
| To | OS X 10.2 |

Modified [SecTrustUserSetting](https://developer.apple.com/documentation/security/sectrustusersetting)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [kSecTrustResultConfirm](https://developer.apple.com/documentation/security/sectrustresulttype/ksectrustresultconfirm)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

SecureTransport.hRemoved errSSLLastAdded #def errSSLLastAdded [errSSLUnexpectedRecord](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslunexpectedrecord)Added [kSSLSessionOptionFalseStart](https://developer.apple.com/documentation/security/sslsessionoption/falsestart)Added [kSSLSessionOptionSendOneByteRecord](https://developer.apple.com/documentation/security/sslsessionoption/sendonebyterecord)Modified [SSLCopyPeerCertificates()](https://developer.apple.com/documentation/security/1503748-sslcopypeercertificates)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLCopyTrustedRoots()](https://developer.apple.com/documentation/security/1503838-sslcopytrustedroots)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLDisposeContext()](https://developer.apple.com/documentation/security/1503799-ssldisposecontext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLGetAllowsAnyRoot()](https://developer.apple.com/documentation/security/1503841-sslgetallowsanyroot)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLGetAllowsExpiredCerts()](https://developer.apple.com/documentation/security/1503806-sslgetallowsexpiredcerts)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLGetAllowsExpiredRoots()](https://developer.apple.com/documentation/security/1503740-sslgetallowsexpiredroots)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLGetEnableCertVerify()](https://developer.apple.com/documentation/security/1503774-sslgetenablecertverify)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLGetProtocolVersionEnabled()](https://developer.apple.com/documentation/security/1503767-sslgetprotocolversionenabled)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLGetRsaBlinding()](https://developer.apple.com/documentation/security/1503742-sslgetrsablinding)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLNewContext()](https://developer.apple.com/documentation/security/1503793-sslnewcontext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetAllowsAnyRoot()](https://developer.apple.com/documentation/security/1503848-sslsetallowsanyroot)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetAllowsExpiredCerts()](https://developer.apple.com/documentation/security/1503738-sslsetallowsexpiredcerts)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetAllowsExpiredRoots()](https://developer.apple.com/documentation/security/1503782-sslsetallowsexpiredroots)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetEnableCertVerify()](https://developer.apple.com/documentation/security/1503735-sslsetenablecertverify)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetProtocolVersionEnabled()](https://developer.apple.com/documentation/security/1503754-sslsetprotocolversionenabled)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetRsaBlinding()](https://developer.apple.com/documentation/security/1503756-sslsetrsablinding)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SSLSetTrustedRoots()](https://developer.apple.com/documentation/security/1503776-sslsettrustedroots)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

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
