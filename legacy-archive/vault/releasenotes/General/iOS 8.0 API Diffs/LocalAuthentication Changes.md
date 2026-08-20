---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/LocalAuthentication.html
archived_at: '2026-07-18T02:55:58.813206Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# LocalAuthentication Changes

## LocalAuthentication (Added)

LAContext.h (Added)Added [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext)Added [-[LAContext canEvaluatePolicy:error:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514149-canevaluatepolicy)Added [-[LAContext evaluatePolicy:localizedReason:reply:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514176-evaluatepolicy)Added [LAContext.localizedFallbackTitle](https://developer.apple.com/documentation/localauthentication/lacontext/1514183-localizedfallbacktitle)Added [LAPolicy](https://developer.apple.com/documentation/localauthentication/lapolicy)Added [LAPolicyDeviceOwnerAuthenticationWithBiometrics](https://developer.apple.com/documentation/localauthentication/lapolicy/lapolicydeviceownerauthenticationwithbiometrics)LAError.h (Added)Added [LAError](https://developer.apple.com/documentation/localauthentication/laerror)Added [LAErrorAuthenticationFailed](https://developer.apple.com/documentation/localauthentication/laerror/code/authenticationfailed)Added [LAErrorDomain](https://developer.apple.com/documentation/localauthentication/laerrordomain)Added [LAErrorPasscodeNotSet](https://developer.apple.com/documentation/localauthentication/laerror/code/passcodenotset)Added [LAErrorSystemCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/systemcancel)Added [LAErrorTouchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/laerror/code/touchidnotavailable)Added [LAErrorTouchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/laerror/code/touchidnotenrolled)Added [LAErrorUserCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/usercancel)Added [LAErrorUserFallback](https://developer.apple.com/documentation/localauthentication/laerror/code/userfallback)LAPublicDefines.h (Added)Added #def LocalAuthentication_LAPublicDefines_hAdded [#def kLAErrorAuthenticationFailed](https://developer.apple.com/documentation/localauthentication/klaerrorauthenticationfailed)Added [#def kLAErrorDomain](https://developer.apple.com/documentation/localauthentication/klaerrordomain)Added [#def kLAErrorPasscodeNotSet](https://developer.apple.com/documentation/localauthentication/klaerrorpasscodenotset)Added [#def kLAErrorSystemCancel](https://developer.apple.com/documentation/localauthentication/klaerrorsystemcancel)Added [#def kLAErrorTouchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/klaerrortouchidnotavailable)Added [#def kLAErrorTouchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/klaerrortouchidnotenrolled)Added [#def kLAErrorUserCancel](https://developer.apple.com/documentation/localauthentication/klaerrorusercancel)Added [#def kLAErrorUserFallback](https://developer.apple.com/documentation/localauthentication/klaerroruserfallback)Added [#def kLAOptionAuthenticationReason](https://developer.apple.com/documentation/localauthentication/klaoptionauthenticationreason)Added [#def kLAOptionUserFallback](https://developer.apple.com/documentation/localauthentication/klaoptionuserfallback)Added [#def kLAPolicyDeviceOwnerAuthenticationWithBiometrics](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthenticationwithbiometrics)LocalAuthentication.h (Added)

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
