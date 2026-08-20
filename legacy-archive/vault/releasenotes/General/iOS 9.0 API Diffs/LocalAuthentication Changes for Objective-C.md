---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/LocalAuthentication.html
archived_at: '2026-07-18T02:56:34.619176Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# LocalAuthentication Changes for Objective-C

### LocalAuthentication

#### LAContext.h

Added [-[LAContext evaluateAccessControl:operation:localizedReason:reply:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514174-evaluateaccesscontrol)Added [LAContext.evaluatedPolicyDomainState](https://developer.apple.com/documentation/localauthentication/lacontext/1514150-evaluatedpolicydomainstate)Added [-[LAContext invalidate]](https://developer.apple.com/documentation/localauthentication/lacontext/1514192-invalidate)Added [-[LAContext isCredentialSet:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514153-iscredentialset)Added [-[LAContext setCredential:type:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514168-setcredential)Added [LAContext.touchIDAuthenticationAllowableReuseDuration](https://developer.apple.com/documentation/localauthentication/lacontext/1622329-touchidauthenticationallowablere)Added [LAAccessControlOperation](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation)Added [LAAccessControlOperationCreateItem](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/createitem)Added [LAAccessControlOperationCreateKey](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationcreatekey)Added [LAAccessControlOperationUseItem](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/useitem)Added [LAAccessControlOperationUseKeySign](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/usekeysign)Added [LACredentialType](https://developer.apple.com/documentation/localauthentication/lacredentialtype)Added [LACredentialTypeApplicationPassword](https://developer.apple.com/documentation/localauthentication/lacredentialtype/lacredentialtypeapplicationpassword)Added [LAPolicyDeviceOwnerAuthentication](https://developer.apple.com/documentation/localauthentication/lapolicy/lapolicydeviceownerauthentication)Added [LATouchIDAuthenticationMaximumAllowableReuseDuration](https://developer.apple.com/documentation/localauthentication/latouchidauthenticationmaximumallowablereuseduration)Modified [LAContext.maxBiometryFailures](https://developer.apple.com/documentation/localauthentication/lacontext/1622330-maxbiometryfailures)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.3 | iOS 9.0 |

#### LAError.h

Added [LAErrorAppCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/appcancel)Added [LAErrorInvalidContext](https://developer.apple.com/documentation/localauthentication/laerror/laerrorinvalidcontext)Added [LAErrorTouchIDLockout](https://developer.apple.com/documentation/localauthentication/laerror/code/touchidlockout)

#### LAPublicDefines.h

Added [#def kLAErrorAppCancel](https://developer.apple.com/documentation/localauthentication/klaerrorappcancel)Added [#def kLAErrorInvalidContext](https://developer.apple.com/documentation/localauthentication/klaerrorinvalidcontext)Added [#def kLAErrorTouchIDLockout](https://developer.apple.com/documentation/localauthentication/klaerrortouchidlockout)Added [#def kLAPolicyDeviceOwnerAuthentication](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthentication)

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
