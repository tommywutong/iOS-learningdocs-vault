---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/LocalAuthentication.html
archived_at: '2026-07-18T02:56:53.921454Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# LocalAuthentication Changes for Swift

### LocalAuthentication

Added [LAAccessControlOperation [enum]](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation)Added [LAAccessControlOperation.CreateItem](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/createitem)Added [LAAccessControlOperation.CreateKey](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationcreatekey)Added [LAAccessControlOperation.UseItem](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/useitem)Added [LAAccessControlOperation.UseKeySign](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationusekeysign)Added [LAContext.evaluateAccessControl(_: SecAccessControl, operation: LAAccessControlOperation, localizedReason: String, reply: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/localauthentication/lacontext/1514174-evaluateaccesscontrol)Added [LAContext.evaluatedPolicyDomainState](https://developer.apple.com/documentation/localauthentication/lacontext/1514150-evaluatedpolicydomainstate)Added [LAContext.invalidate()](https://developer.apple.com/documentation/localauthentication/lacontext/1514192-invalidate)Added [LAContext.isCredentialSet(_: LACredentialType) -> Bool](https://developer.apple.com/documentation/localauthentication/lacontext/1514153-iscredentialset)Added [LAContext.setCredential(_: NSData?, type: LACredentialType) -> Bool](https://developer.apple.com/documentation/localauthentication/lacontext/1514168-setcredential)Added [LAContext.touchIDAuthenticationAllowableReuseDuration](https://developer.apple.com/documentation/localauthentication/lacontext/1622329-touchidauthenticationallowablere)Added [LACredentialType [enum]](https://developer.apple.com/documentation/localauthentication/lacredentialtype)Added [LACredentialType.ApplicationPassword](https://developer.apple.com/documentation/localauthentication/lacredentialtype/lacredentialtypeapplicationpassword)Added [LAError.AppCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/appcancel)Added [LAError.InvalidContext](https://developer.apple.com/documentation/localauthentication/laerror/code/invalidcontext)Added [LAError.TouchIDLockout](https://developer.apple.com/documentation/localauthentication/laerror/code/touchidlockout)Added [LAPolicy.DeviceOwnerAuthentication](https://developer.apple.com/documentation/localauthentication/lapolicy/lapolicydeviceownerauthentication)Added [kLAErrorAppCancel](https://developer.apple.com/documentation/localauthentication/klaerrorappcancel)Added [kLAErrorInvalidContext](https://developer.apple.com/documentation/localauthentication/klaerrorinvalidcontext)Added [kLAErrorTouchIDLockout](https://developer.apple.com/documentation/localauthentication/klaerrortouchidlockout)Added [kLAPolicyDeviceOwnerAuthentication](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthentication)Added [LATouchIDAuthenticationMaximumAllowableReuseDuration](https://developer.apple.com/documentation/localauthentication/latouchidauthenticationmaximumallowablereuseduration)Modified [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext)

|  | Declaration |
| --- | --- |
| From | ``` class LAContext : NSObject {     func canEvaluatePolicy(_ policy: LAPolicy, error error: NSErrorPointer) -> Bool     func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String!, reply reply: ((Bool, NSError!) -> Void)!)     var localizedFallbackTitle: String!     var maxBiometryFailures: NSNumber! } ``` |
| To | ``` class LAContext : NSObject {     func canEvaluatePolicy(_ policy: LAPolicy, error error: NSErrorPointer) -> Bool     func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void)     func invalidate()     func setCredential(_ credential: NSData?, type type: LACredentialType) -> Bool     func isCredentialSet(_ type: LACredentialType) -> Bool     func evaluateAccessControl(_ accessControl: SecAccessControl, operation operation: LAAccessControlOperation, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void)     var localizedFallbackTitle: String?     var maxBiometryFailures: NSNumber?     var evaluatedPolicyDomainState: NSData? { get }     var touchIDAuthenticationAllowableReuseDuration: NSTimeInterval } ``` |

Modified [LAContext.evaluatePolicy(_: LAPolicy, localizedReason: String, reply: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/localauthentication/lacontext/1514176-evaluatepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String!, reply reply: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void) ``` |

Modified [LAContext.localizedFallbackTitle](https://developer.apple.com/documentation/localauthentication/lacontext/1514183-localizedfallbacktitle)

|  | Declaration |
| --- | --- |
| From | ``` var localizedFallbackTitle: String! ``` |
| To | ``` var localizedFallbackTitle: String? ``` |

Modified [LAContext.maxBiometryFailures](https://developer.apple.com/documentation/localauthentication/lacontext/1622330-maxbiometryfailures)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` var maxBiometryFailures: NSNumber! ``` | iOS 8.1 | -- |
| To | ``` var maxBiometryFailures: NSNumber? ``` | iOS 8.3 | iOS 9.0 |

Modified [LAError [enum]](https://developer.apple.com/documentation/localauthentication/laerror/code)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum LAError : Int {     case AuthenticationFailed     case UserCancel     case UserFallback     case SystemCancel     case PasscodeNotSet     case TouchIDNotAvailable     case TouchIDNotEnrolled } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum LAError : Int {     case AuthenticationFailed     case UserCancel     case UserFallback     case SystemCancel     case PasscodeNotSet     case TouchIDNotAvailable     case TouchIDNotEnrolled     case TouchIDLockout     case AppCancel     case InvalidContext } extension LAError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension LAError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [LAPolicy [enum]](https://developer.apple.com/documentation/localauthentication/lapolicy)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum LAPolicy : Int {     case DeviceOwnerAuthenticationWithBiometrics } ``` | -- |
| To | ``` enum LAPolicy : Int {     case DeviceOwnerAuthenticationWithBiometrics     case DeviceOwnerAuthentication } ``` | Int |

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
