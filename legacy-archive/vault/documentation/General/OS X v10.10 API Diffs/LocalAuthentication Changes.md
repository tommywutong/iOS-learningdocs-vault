---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/LocalAuthentication.html
archived_at: '2026-07-15T07:34:46.778113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# LocalAuthentication Changes

## LocalAuthentication (Added)

LAContext.h (Added)Added [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext)Added [-[LAContext canEvaluatePolicy:error:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514149-canevaluatepolicy)Added [-[LAContext evaluatePolicy:localizedReason:reply:]](https://developer.apple.com/documentation/localauthentication/lacontext/1514176-evaluatepolicy)Added [LAContext.localizedFallbackTitle](https://developer.apple.com/documentation/localauthentication/lacontext/1514183-localizedfallbacktitle)Added [LAPolicy](https://developer.apple.com/documentation/localauthentication/lapolicy)LAError.h (Added)Added [LAError](https://developer.apple.com/documentation/localauthentication/laerror)Added [LAErrorAuthenticationFailed](https://developer.apple.com/documentation/localauthentication/laerror/code/authenticationfailed)Added [LAErrorDomain](https://developer.apple.com/documentation/localauthentication/laerrordomain)Added [LAErrorPasscodeNotSet](https://developer.apple.com/documentation/localauthentication/laerror/code/passcodenotset)Added [LAErrorSystemCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/systemcancel)Added [LAErrorTouchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/laerror/code/touchidnotavailable)Added [LAErrorTouchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/laerror/code/touchidnotenrolled)Added [LAErrorUserCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/usercancel)Added [LAErrorUserFallback](https://developer.apple.com/documentation/localauthentication/laerror/code/userfallback)LAPublicDefines.h (Added)Added #def LocalAuthentication_LAPublicDefines_hAdded [#def kLAErrorAuthenticationFailed](https://developer.apple.com/documentation/localauthentication/klaerrorauthenticationfailed)Added [#def kLAErrorDomain](https://developer.apple.com/documentation/localauthentication/klaerrordomain)Added [#def kLAErrorPasscodeNotSet](https://developer.apple.com/documentation/localauthentication/klaerrorpasscodenotset)Added [#def kLAErrorSystemCancel](https://developer.apple.com/documentation/localauthentication/klaerrorsystemcancel)Added [#def kLAErrorTouchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/klaerrortouchidnotavailable)Added [#def kLAErrorTouchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/klaerrortouchidnotenrolled)Added [#def kLAErrorUserCancel](https://developer.apple.com/documentation/localauthentication/klaerrorusercancel)Added [#def kLAErrorUserFallback](https://developer.apple.com/documentation/localauthentication/klaerroruserfallback)Added [#def kLAOptionAuthenticationReason](https://developer.apple.com/documentation/localauthentication/klaoptionauthenticationreason)Added [#def kLAOptionUserFallback](https://developer.apple.com/documentation/localauthentication/klaoptionuserfallback)Added [#def kLAPolicyDeviceOwnerAuthenticationWithBiometrics](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthenticationwithbiometrics)LocalAuthentication.h (Added)

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
