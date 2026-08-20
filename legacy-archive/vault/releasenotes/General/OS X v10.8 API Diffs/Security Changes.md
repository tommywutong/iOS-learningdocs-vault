---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Security.html
archived_at: '2026-07-18T02:54:06.492757Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Security Changes

## Security

CMSDecoder.hAdded [CMSDecoderCopySignerSigningTime()](https://developer.apple.com/documentation/security/1401770-cmsdecodercopysignersigningtime)Added [CMSDecoderCopySignerTimestamp()](https://developer.apple.com/documentation/security/1399271-cmsdecodercopysignertimestamp)Added [CMSDecoderCopySignerTimestampCertificates()](https://developer.apple.com/documentation/security/1392952-cmsdecodercopysignertimestampcer)CMSEncoder.hAdded [CMSEncoderCopySignerTimestamp()](https://developer.apple.com/documentation/security/1387179-cmsencodercopysignertimestamp)CSCommon.hAdded [errSecCSBadBundleFormat](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadbundleformat)Added [errSecCSDBAccess](https://developer.apple.com/documentation/security/errseccsdbaccess)Added [errSecCSDBDenied](https://developer.apple.com/documentation/security/errseccsdbdenied)Added [errSecCSDbCorrupt](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsdbcorrupt)Added [errSecCSFileHardQuarantined](https://developer.apple.com/documentation/security/errseccsfilehardquarantined)Added [errSecCSNoMatches](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsnomatches)Added [errSecCSOutdated](https://developer.apple.com/documentation/security/errseccsoutdated)Added [kSecCFErrorPath](https://developer.apple.com/documentation/security/kseccferrorpath)Added [kSecCSEnforceRevocationChecks](https://developer.apple.com/documentation/security/seccsflags/1394974-enforcerevocationchecks)CipherSuite.hAdded [TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_dss_with_3des_ede_cbc_sha)Added [TLS_DHE_DSS_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_128_cbc_sha256)Added [TLS_DHE_DSS_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dhe_dss_with_aes_128_gcm_sha256)Added [TLS_DHE_DSS_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_cbc_sha256)Added [TLS_DHE_DSS_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_dss_with_aes_256_gcm_sha384)Added [TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_3des_ede_cbc_sha)Added [TLS_DHE_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dhe_rsa_with_aes_128_cbc_sha256)Added [TLS_DHE_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_128_gcm_sha256)Added [TLS_DHE_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_256_cbc_sha256)Added [TLS_DHE_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dhe_rsa_with_aes_256_gcm_sha384)Added [TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_dss_with_3des_ede_cbc_sha)Added [TLS_DH_DSS_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_cbc_sha256)Added [TLS_DH_DSS_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_dss_with_aes_128_gcm_sha256)Added [TLS_DH_DSS_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_256_cbc_sha256)Added [TLS_DH_DSS_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_dh_dss_with_aes_256_gcm_sha384)Added [TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_3des_ede_cbc_sha)Added [TLS_DH_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_128_cbc_sha256)Added [TLS_DH_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_128_gcm_sha256)Added [TLS_DH_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_rsa_with_aes_256_cbc_sha256)Added [TLS_DH_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_rsa_with_aes_256_gcm_sha384)Added [TLS_DH_anon_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/tls_dh_anon_with_3des_ede_cbc_sha)Added [TLS_DH_anon_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_128_cbc_sha256)Added [TLS_DH_anon_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_dh_anon_with_aes_128_gcm_sha256)Added [TLS_DH_anon_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_256_cbc_sha256)Added [TLS_DH_anon_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_dh_anon_with_aes_256_gcm_sha384)Added [TLS_DH_anon_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/tls_dh_anon_with_rc4_128_md5)Added [TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_128_cbc_sha256)Added [TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_128_gcm_sha256)Added [TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdhe_ecdsa_with_aes_256_cbc_sha384)Added [TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_ecdsa_with_aes_256_gcm_sha384)Added [TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_128_cbc_sha256)Added [TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_128_gcm_sha256)Added [TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_256_cbc_sha384)Added [TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/tls_ecdhe_rsa_with_aes_256_gcm_sha384)Added [TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_128_cbc_sha256)Added [TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_128_gcm_sha256)Added [TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/tls_ecdh_ecdsa_with_aes_256_cbc_sha384)Added [TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_ecdsa_with_aes_256_gcm_sha384)Added [TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_128_cbc_sha256)Added [TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_ecdh_rsa_with_aes_128_gcm_sha256)Added [TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_256_cbc_sha384)Added [TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_ecdh_rsa_with_aes_256_gcm_sha384)Added [TLS_EMPTY_RENEGOTIATION_INFO_SCSV](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_empty_renegotiation_info_scsv)Added [TLS_NULL_WITH_NULL_NULL](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_null_with_null_null)Added [TLS_RSA_WITH_3DES_EDE_CBC_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_3des_ede_cbc_sha)Added [TLS_RSA_WITH_AES_128_CBC_SHA256](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_aes_128_cbc_sha256)Added [TLS_RSA_WITH_AES_128_GCM_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_128_gcm_sha256)Added [TLS_RSA_WITH_AES_256_CBC_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_aes_256_cbc_sha256)Added [TLS_RSA_WITH_AES_256_GCM_SHA384](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_aes_256_gcm_sha384)Added [TLS_RSA_WITH_NULL_MD5](https://developer.apple.com/documentation/security/tls_rsa_with_null_md5)Added [TLS_RSA_WITH_NULL_SHA](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_null_sha)Added [TLS_RSA_WITH_NULL_SHA256](https://developer.apple.com/documentation/security/tls_rsa_with_null_sha256)Added [TLS_RSA_WITH_RC4_128_MD5](https://developer.apple.com/documentation/security/1550981-ssl_cipher_suite_values/tls_rsa_with_rc4_128_md5)Added [TLS_RSA_WITH_RC4_128_SHA](https://developer.apple.com/documentation/security/tls_rsa_with_rc4_128_sha)SecAsn1Coder.hAdded [SecAsn1OidCompare()](https://developer.apple.com/documentation/security/1428201-secasn1oidcompare)Modified [SecAsn1EncodeItem()](https://developer.apple.com/documentation/security/1428195-secasn1encodeitem)

|  | Declaration |
| --- | --- |
| From | OSStatus SecAsn1EncodeItem ( SecAsn1CoderRef coder, const void \*src, const SecAsn1Template \*templates, CSSM_DATA \*dest); |
| To | OSStatus SecAsn1EncodeItem ( SecAsn1CoderRef coder, const void \*src, const SecAsn1Template \*templates, SecAsn1Item \*dest); |

Modified [SecAsn1AllocItem()](https://developer.apple.com/documentation/security/1428206-secasn1allocitem)

|  | Declaration |
| --- | --- |
| From | OSStatus SecAsn1AllocItem ( SecAsn1CoderRef coder, CSSM_DATA \*item, size_t len); |
| To | OSStatus SecAsn1AllocItem ( SecAsn1CoderRef coder, SecAsn1Item \*item, size_t len); |

Modified [SecAsn1AllocCopyItem()](https://developer.apple.com/documentation/security/1428197-secasn1alloccopyitem)

|  | Declaration |
| --- | --- |
| From | OSStatus SecAsn1AllocCopyItem ( SecAsn1CoderRef coder, const CSSM_DATA \*src, CSSM_DATA \*dest); |
| To | OSStatus SecAsn1AllocCopyItem ( SecAsn1CoderRef coder, const SecAsn1Item \*src, SecAsn1Item \*dest); |

Modified [SecAsn1DecodeData()](https://developer.apple.com/documentation/security/1428204-secasn1decodedata)

|  | Declaration |
| --- | --- |
| From | OSStatus SecAsn1DecodeData ( SecAsn1CoderRef coder, const CSSM_DATA \*src, const SecAsn1Template \*templ, void \*dest); |
| To | OSStatus SecAsn1DecodeData ( SecAsn1CoderRef coder, const SecAsn1Item \*src, const SecAsn1Template \*templ, void \*dest); |

Modified [SecAsn1AllocCopy()](https://developer.apple.com/documentation/security/1428212-secasn1alloccopy)

|  | Declaration |
| --- | --- |
| From | OSStatus SecAsn1AllocCopy ( SecAsn1CoderRef coder, const void \*src, size_t len, CSSM_DATA \*dest); |
| To | OSStatus SecAsn1AllocCopy ( SecAsn1CoderRef coder, const void \*src, size_t len, SecAsn1Item \*dest); |

SecAsn1Types.hAdded [SecAsn1AlgId](https://developer.apple.com/documentation/security/secasn1algid)Added [SecAsn1Item](https://developer.apple.com/documentation/security/secasn1item)Added [SecAsn1Oid](https://developer.apple.com/documentation/security/secasn1oid)Added [SecAsn1PubKeyInfo](https://developer.apple.com/documentation/security/secasn1pubkeyinfo)SecBase.hAdded [errSecExtendedKeyUsageNotCritical](https://developer.apple.com/documentation/security/errsecextendedkeyusagenotcritical)Added [errSecInDarkWake](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecindarkwake)Added [errSecMissingRequiredExtension](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingrequiredextension)Added [errSecSigningTimeMissing](https://developer.apple.com/documentation/security/errsecsigningtimemissing)Added [errSecTimestampAddInfoNotAvailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampaddinfonotavailable)Added [errSecTimestampBadAlg](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampbadalg)Added [errSecTimestampBadDataFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampbaddataformat)Added [errSecTimestampBadRequest](https://developer.apple.com/documentation/security/errsectimestampbadrequest)Added [errSecTimestampInvalid](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampinvalid)Added [errSecTimestampMissing](https://developer.apple.com/documentation/security/errsectimestampmissing)Added [errSecTimestampNotTrusted](https://developer.apple.com/documentation/security/errsectimestampnottrusted)Added [errSecTimestampRejection](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestamprejection)Added [errSecTimestampRevocationNotification](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestamprevocationnotification)Added [errSecTimestampRevocationWarning](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestamprevocationwarning)Added [errSecTimestampServiceNotAvailable](https://developer.apple.com/documentation/security/errsectimestampservicenotavailable)Added [errSecTimestampSystemFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampsystemfailure)Added [errSecTimestampTimeNotAvailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestamptimenotavailable)Added [errSecTimestampUnacceptedExtension](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampunacceptedextension)Added [errSecTimestampUnacceptedPolicy](https://developer.apple.com/documentation/security/errsectimestampunacceptedpolicy)Added [errSecTimestampWaiting](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectimestampwaiting)SecCertificateOIDs.hAdded [kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_appleid_intermediate)Added [kSecOIDSRVName](https://developer.apple.com/documentation/security/ksecoidsrvname)SecCode.hAdded [kSecCodeInfoEntitlementsDict](https://developer.apple.com/documentation/security/kseccodeinfoentitlementsdict)Added [kSecCodeInfoTimestamp](https://developer.apple.com/documentation/security/kseccodeinfotimestamp)Added kSecCodeSignerFlagsSecCustomTransform.hAdded [SecTransformCustomGetAttribute()](https://developer.apple.com/documentation/security/1397766-sectransformcustomgetattribute)Modified [SecTranformCustomGetAttribute()](https://developer.apple.com/documentation/security/1552632-sectranformcustomgetattribute)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

SecEncodeTransform.hAdded [kSecLineLength64](https://developer.apple.com/documentation/security/kseclinelength64)Added [kSecLineLength76](https://developer.apple.com/documentation/security/kseclinelength76)SecEncryptTransform.hAdded [kSecOAEPEncodingParametersAttributeName](https://developer.apple.com/documentation/security/ksecoaepencodingparametersattributename)Added [kSecOAEPMGF1DigestAlgorithmAttributeName](https://developer.apple.com/documentation/security/ksecoaepmgf1digestalgorithmattributename)Added [kSecOAEPMessageLengthAttributeName](https://developer.apple.com/documentation/security/ksecoaepmessagelengthattributename)Added [kSecPaddingOAEPKey](https://developer.apple.com/documentation/security/ksecpaddingoaepkey)SecPolicy.hAdded [kSecPolicyAppleTimeStamping](https://developer.apple.com/documentation/security/ksecpolicyappletimestamping)SecStaticCode.hAdded [kSecCSCheckNestedCode](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccschecknestedcode)SecTask.hAdded [SecTaskCreateFromSelf()](https://developer.apple.com/documentation/security/1400321-sectaskcreatefromself)SecureTransport.hRemoved SSLGetPeerCertificates()Removed SSLGetTrustedRoots()Removed [errSSLServerAuthCompleted](https://developer.apple.com/documentation/security/secure_transport/1503828-secure_transport_result_codes/errsslserverauthcompleted)Added [SSLConnectionType](https://developer.apple.com/documentation/security/sslconnectiontype)Added [SSLContextGetTypeID()](https://developer.apple.com/documentation/security/1398165-sslcontextgettypeid)Added [SSLCreateContext()](https://developer.apple.com/documentation/security/1393063-sslcreatecontext)Added [SSLGetDatagramWriteSize()](https://developer.apple.com/documentation/security/1401259-sslgetdatagramwritesize)Added [SSLGetMaxDatagramRecordSize()](https://developer.apple.com/documentation/security/1399678-sslgetmaxdatagramrecordsize)Added [SSLGetProtocolVersionMax()](https://developer.apple.com/documentation/security/1396167-sslgetprotocolversionmax)Added [SSLGetProtocolVersionMin()](https://developer.apple.com/documentation/security/1395690-sslgetprotocolversionmin)Added [SSLProtocolSide](https://developer.apple.com/documentation/security/sslprotocolside)Added [SSLSetDatagramHelloCookie()](https://developer.apple.com/documentation/security/1398936-sslsetdatagramhellocookie)Added [SSLSetMaxDatagramRecordSize()](https://developer.apple.com/documentation/security/1394978-sslsetmaxdatagramrecordsize)Added [SSLSetProtocolVersionMax()](https://developer.apple.com/documentation/security/1393798-sslsetprotocolversionmax)Added [SSLSetProtocolVersionMin()](https://developer.apple.com/documentation/security/1398139-sslsetprotocolversionmin)Added #def errSSLClientAuthCompletedAdded [errSSLPeerAuthCompleted](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslpeerauthcompleted)Added #def errSSLServerAuthCompletedAdded [kDTLSProtocol1](https://developer.apple.com/documentation/security/sslprotocol/dtlsprotocol1)Added [kSSLClientSide](https://developer.apple.com/documentation/security/sslprotocolside/ksslclientside)Added [kSSLDatagramType](https://developer.apple.com/documentation/security/sslconnectiontype/kssldatagramtype)Added [kSSLServerSide](https://developer.apple.com/documentation/security/sslprotocolside/ksslserverside)Added [kSSLSessionOptionBreakOnClientAuth](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclientauth)Added [kSSLStreamType](https://developer.apple.com/documentation/security/sslconnectiontype/ksslstreamtype)Added [kTLSProtocol11](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol11)Added [kTLSProtocol12](https://developer.apple.com/documentation/security/sslprotocol/tlsprotocol12)Modified [SSLSetIOFuncs()](https://developer.apple.com/documentation/security/1396081-sslsetiofuncs)

|  | Declaration |
| --- | --- |
| From | OSStatus SSLSetIOFuncs ( SSLContextRef context, SSLReadFunc read, SSLWriteFunc write); |
| To | OSStatus SSLSetIOFuncs ( SSLContextRef context, SSLReadFunc readFunc, SSLWriteFunc writeFunc); |

Modified [SSLSetProtocolVersion()](https://developer.apple.com/documentation/security/1503760-sslsetprotocolversion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [SSLGetProtocolVersion()](https://developer.apple.com/documentation/security/1503847-sslgetprotocolversion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

cssmapple.hAdded CSSMERR_AC_IN_DARK_WAKEAdded CSSMERR_APPLETP_EXT_KEYUSAGE_NOT_CRITICALAdded CSSMERR_CL_IN_DARK_WAKEAdded CSSMERR_CSP_IN_DARK_WAKEAdded CSSMERR_CSSM_IN_DARK_WAKEAdded CSSMERR_DL_IN_DARK_WAKEAdded CSSMERR_TP_IN_DARK_WAKEAdded CSSM_ERRCODE_IN_DARK_WAKEoidsalg.hAdded CSSMOID_APPLE_TP_TIMESTAMPINGoidsattr.hAdded CSSMOID_PKCS9_Id_Ct_TSTInfoAdded CSSMOID_PKCS9_TimeStampTokenoidsbase.hAdded #def APPLE_EXTENSION_APPLEID_INTERMEDIATEAdded #def APPLE_EXTENSION_APPLEID_INTERMEDIATE_LENGTHoidscert.hAdded CSSMOID_APPLE_EXTENSION_APPLEID_INTERMEDIATE

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
