---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/Security.html
archived_at: '2026-07-18T02:56:36.634204Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Security Changes for Objective-C

### Security

#### SecAccessControl.h

Added [kSecAccessControlAnd](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroland)Added [kSecAccessControlApplicationPassword](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontrolapplicationpassword)Added [kSecAccessControlDevicePasscode](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1394326-devicepasscode)Added [kSecAccessControlOr](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontrolor)Added [kSecAccessControlPrivateKeyUsage](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1617983-privatekeyusage)Added [kSecAccessControlTouchIDAny](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroltouchidany)Added [kSecAccessControlTouchIDCurrentSet](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/ksecaccesscontroltouchidcurrentset)

#### SecItem.h

Added [kSecAttrSyncViewHint](https://developer.apple.com/documentation/security/ksecattrsyncviewhint)Added [kSecAttrTokenID](https://developer.apple.com/documentation/security/ksecattrtokenid)Added [kSecAttrTokenIDSecureEnclave](https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave)Added [kSecUseAuthenticationContext](https://developer.apple.com/documentation/security/ksecuseauthenticationcontext)Added [kSecUseAuthenticationUI](https://developer.apple.com/documentation/security/ksecuseauthenticationui)Added [kSecUseAuthenticationUIAllow](https://developer.apple.com/documentation/security/ksecuseauthenticationuiallow)Added [kSecUseAuthenticationUIFail](https://developer.apple.com/documentation/security/ksecuseauthenticationuifail)Added [kSecUseAuthenticationUISkip](https://developer.apple.com/documentation/security/ksecuseauthenticationuiskip)Modified [kSecUseNoAuthenticationUI](https://developer.apple.com/documentation/security/ksecusenoauthenticationui)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### SecPolicy.h

Added [kSecPolicyApplePayIssuerEncryption](https://developer.apple.com/documentation/security/ksecpolicyapplepayissuerencryption)Added [kSecPolicyMacAppStoreReceipt](https://developer.apple.com/documentation/security/ksecpolicymacappstorereceipt)

#### SecTrust.h

Added [kSecTrustCertificateTransparency](https://developer.apple.com/documentation/security/ksectrustcertificatetransparency)

#### SecureTransport.h

Added [errSSLClientHelloReceived](https://developer.apple.com/documentation/security/errsslclienthelloreceived)Added [errSSLWeakPeerEphemeralDHKey](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslweakpeerephemeraldhkey)Added [kSSLSessionOptionAllowServerIdentityChange](https://developer.apple.com/documentation/security/sslsessionoption/allowserveridentitychange)Added [kSSLSessionOptionBreakOnClientHello](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclienthello)Added kSSLSessionStrengthPolicyATSv1Added kSSLSessionStrengthPolicyDefaultAdded SSLSessionStrengthPolicyAdded SSLSetSessionStrengthPolicy()Modified [SSLSetEncryptionCertificate()](https://developer.apple.com/documentation/security/1398098-sslsetencryptioncertificate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
