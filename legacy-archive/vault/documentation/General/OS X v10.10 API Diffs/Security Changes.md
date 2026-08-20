---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/Security.html
archived_at: '2026-07-15T07:34:47.337127Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Security Changes

## Security

CMSDecoder.hAdded [CMSDecoderCopySignerTimestampWithPolicy()](https://developer.apple.com/documentation/security/1395908-cmsdecodercopysignertimestampwit)CMSEncoder.hAdded [CMSEncoderCopySignerTimestampWithPolicy()](https://developer.apple.com/documentation/security/1387162-cmsencodercopysignertimestampwit)CSCommon.hAdded [errSecCSAmbiguousBundleFormat](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsambiguousbundleformat)Added [errSecCSBadFrameworkVersion](https://developer.apple.com/documentation/security/errseccsbadframeworkversion)Added [errSecCSBadLVArch](https://developer.apple.com/documentation/security/errseccsbadlvarch)Added [errSecCSBadMainExecutable](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbadmainexecutable)Added [errSecCSCancelled](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccscancelled)Added [errSecCSDSStoreSymlink](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsdsstoresymlink)Added [errSecCSRegularFile](https://developer.apple.com/documentation/security/errseccsregularfile)Added [errSecCSResourceNotSupported](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsresourcenotsupported)Added [errSecCSUnsealedAppRoot](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsunsealedapproot)Added [errSecCSUnsealedFrameworkRoot](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsunsealedframeworkroot)Added [errSecCSWeakResourceEnvelope](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsweakresourceenvelope)Added [errSecCSWeakResourceRules](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsweakresourcerules)Added [kSecCSNoNetworkAccess](https://developer.apple.com/documentation/security/seccsflags/1397911-nonetworkaccess)Added [kSecCSReportProgress](https://developer.apple.com/documentation/security/seccsflags/kseccsreportprogress)Added [kSecCodeSignatureLibraryValidation](https://developer.apple.com/documentation/security/seccodesignatureflags/kseccodesignaturelibraryvalidation)SecAccessControl.h (Added)Added [SecAccessControlCreateFlags](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags)Added [SecAccessControlCreateWithFlags()](https://developer.apple.com/documentation/security/1394452-secaccesscontrolcreatewithflags)Added [SecAccessControlGetTypeID()](https://developer.apple.com/documentation/security/1395487-secaccesscontrolgettypeid)Added [kSecAccessControlUserPresence](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroluserpresence)SecBase.hAdded [SecAccessControlRef](https://developer.apple.com/documentation/security/secaccesscontrol)Modified [SecCopyErrorMessageString()](https://developer.apple.com/documentation/security/1394686-seccopyerrormessagestring)

|  | Introduction |
| --- | --- |
| From | OS X 10.5 |
| To | OS X 10.3 |

SecCode.hAdded [kSecCodeInfoTeamIdentifier](https://developer.apple.com/documentation/security/kseccodeinfoteamidentifier)SecEncryptTransform.hModified [kSecOAEPEncodingParametersAttributeName](https://developer.apple.com/documentation/security/ksecoaepencodingparametersattributename)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.8 |

Modified [kSecOAEPMGF1DigestAlgorithmAttributeName](https://developer.apple.com/documentation/security/ksecoaepmgf1digestalgorithmattributename)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.8 |

Modified [kSecOAEPMessageLengthAttributeName](https://developer.apple.com/documentation/security/ksecoaepmessagelengthattributename)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.8 |

Modified [kSecPaddingOAEPKey](https://developer.apple.com/documentation/security/ksecpaddingoaepkey)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.8 |

SecItem.hAdded [kSecAttrAccessControl](https://developer.apple.com/documentation/security/ksecattraccesscontrol)Added [kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly](https://developer.apple.com/documentation/security/ksecattraccessiblewhenpasscodesetthisdeviceonly)SecKey.hAdded [kSecPrivateKeyAttrs](https://developer.apple.com/documentation/security/ksecprivatekeyattrs)Added [kSecPublicKeyAttrs](https://developer.apple.com/documentation/security/ksecpublickeyattrs)SecStaticCode.hAdded [kSecCSFullReport](https://developer.apple.com/documentation/security/kseccsfullreport)Added [kSecCSStrictValidate](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsstrictvalidate)SecureTransport.hAdded [kSSLSessionOptionFallback](https://developer.apple.com/documentation/security/sslsessionoption/fallback)cssmapple.hAdded [CSSMERR_APPLETP_CA_PIN_MISMATCH](https://developer.apple.com/documentation/security/cssmerr_appletp_ca_pin_mismatch)oidsalg.hAdded [CSSMOID_APPLE_TP_PCS_ESCROW_SERVICE](https://developer.apple.com/documentation/security/cssmoid_apple_tp_pcs_escrow_service)oidsbase.hAdded #def APPLE_EXTENSION_DEVELOPER_AUTHENTICATIONAdded [#def APPLE_EXTENSION_DEVELOPER_AUTHENTICATION_LENGTH](https://developer.apple.com/documentation/security/apple_extension_developer_authentication_length)Added #def APPLE_EXTENSION_SERVER_AUTHENTICATIONAdded [#def APPLE_EXTENSION_SERVER_AUTHENTICATION_LENGTH](https://developer.apple.com/documentation/security/apple_extension_server_authentication_length)oidscert.hAdded [CSSMOID_APPLE_EXTENSION_DEVELOPER_AUTHENTICATION](https://developer.apple.com/documentation/security/cssmoid_apple_extension_developer_authentication)Added [CSSMOID_APPLE_EXTENSION_SERVER_AUTHENTICATION](https://developer.apple.com/documentation/security/cssmoid_apple_extension_server_authentication)

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
