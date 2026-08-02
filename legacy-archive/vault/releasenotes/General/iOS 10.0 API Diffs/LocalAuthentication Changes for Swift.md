---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/LocalAuthentication.html
archived_at: '2026-07-18T02:55:30.902115Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# LocalAuthentication Changes for Swift

### LocalAuthentication

Added [LAAccessControlOperation.useKeyDecrypt](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationusekeydecrypt)Added [LAAccessControlOperation.useKeyKeyExchange](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationusekeykeyexchange)Added [LAContext.localizedCancelTitle](https://developer.apple.com/documentation/localauthentication/lacontext/1643658-localizedcanceltitle)Added [LAError [struct]](https://developer.apple.com/documentation/localauthentication/laerror)Added [LAError.appCancel](https://developer.apple.com/documentation/localauthentication/laerror/2325750-appcancel)Added [LAError.authenticationFailed](https://developer.apple.com/documentation/localauthentication/laerror/2325757-authenticationfailed)Added LAError.init(_nsError: NSError)Added [LAError.invalidContext](https://developer.apple.com/documentation/localauthentication/laerror/2325751-invalidcontext)Added [LAError.passcodeNotSet](https://developer.apple.com/documentation/localauthentication/laerror/2325754-passcodenotset)Added [LAError.systemCancel](https://developer.apple.com/documentation/localauthentication/laerror/2325753-systemcancel)Added [LAError.touchIDLockout](https://developer.apple.com/documentation/localauthentication/laerror/2325758-touchidlockout)Added [LAError.touchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/laerror/2325752-touchidnotavailable)Added [LAError.touchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/laerror/2325756-touchidnotenrolled)Added [LAError.userCancel](https://developer.apple.com/documentation/localauthentication/laerror/2325755-usercancel)Added [LAError.userFallback](https://developer.apple.com/documentation/localauthentication/laerror/2325759-userfallback)Added kLACredentialCTKPINAdded kLACredentialTypePasscodeAdded kLACredentialTypePassphraseModified [LAAccessControlOperation [enum]](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation)

|  | Declaration |
| --- | --- |
| From | ``` enum LAAccessControlOperation : Int {     case CreateItem     case UseItem     case CreateKey     case UseKeySign } ``` |
| To | ``` enum LAAccessControlOperation : Int {     case createItem     case useItem     case createKey     case useKeySign     case useKeyDecrypt     case useKeyKeyExchange } ``` |

Modified [LAAccessControlOperation.createItem](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/createitem)

|  | Declaration |
| --- | --- |
| From | ``` case CreateItem ``` |
| To | ``` case createItem ``` |

Modified [LAAccessControlOperation.createKey](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationcreatekey)

|  | Declaration |
| --- | --- |
| From | ``` case CreateKey ``` |
| To | ``` case createKey ``` |

Modified [LAAccessControlOperation.useItem](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/useitem)

|  | Declaration |
| --- | --- |
| From | ``` case UseItem ``` |
| To | ``` case useItem ``` |

Modified [LAAccessControlOperation.useKeySign](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation/laaccesscontroloperationusekeysign)

|  | Declaration |
| --- | --- |
| From | ``` case UseKeySign ``` |
| To | ``` case useKeySign ``` |

Modified [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class LAContext : NSObject {     func canEvaluatePolicy(_ policy: LAPolicy, error error: NSErrorPointer) -> Bool     func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void)     func invalidate()     func setCredential(_ credential: NSData?, type type: LACredentialType) -> Bool     func isCredentialSet(_ type: LACredentialType) -> Bool     func evaluateAccessControl(_ accessControl: SecAccessControl, operation operation: LAAccessControlOperation, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void)     var localizedFallbackTitle: String?     var maxBiometryFailures: NSNumber?     var evaluatedPolicyDomainState: NSData? { get }     var touchIDAuthenticationAllowableReuseDuration: NSTimeInterval } ``` | -- |
| To | ``` class LAContext : NSObject {     func canEvaluatePolicy(_ policy: LAPolicy, error error: NSErrorPointer) -> Bool     func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: @escaping (Bool, Error?) -> Swift.Void)     func invalidate()     func setCredential(_ credential: Data?, type type: LACredentialType) -> Bool     func isCredentialSet(_ type: LACredentialType) -> Bool     func evaluateAccessControl(_ accessControl: SecAccessControl, operation operation: LAAccessControlOperation, localizedReason localizedReason: String, reply reply: @escaping (Bool, Error?) -> Swift.Void)     var localizedFallbackTitle: String?     var localizedCancelTitle: String?     var maxBiometryFailures: NSNumber?     var evaluatedPolicyDomainState: Data? { get }     var touchIDAuthenticationAllowableReuseDuration: TimeInterval     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension LAContext : CVarArg { } extension LAContext : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [LAContext.evaluateAccessControl(_: SecAccessControl, operation: LAAccessControlOperation, localizedReason: String, reply: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/localauthentication/lacontext/1514174-evaluateaccesscontrol)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateAccessControl(_ accessControl: SecAccessControl, operation operation: LAAccessControlOperation, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void) ``` |
| To | ``` func evaluateAccessControl(_ accessControl: SecAccessControl, operation operation: LAAccessControlOperation, localizedReason localizedReason: String, reply reply: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [LAContext.evaluatedPolicyDomainState](https://developer.apple.com/documentation/localauthentication/lacontext/1514150-evaluatedpolicydomainstate)

|  | Declaration |
| --- | --- |
| From | ``` var evaluatedPolicyDomainState: NSData? { get } ``` |
| To | ``` var evaluatedPolicyDomainState: Data? { get } ``` |

Modified [LAContext.evaluatePolicy(_: LAPolicy, localizedReason: String, reply: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/localauthentication/lacontext/1514176-evaluatepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: (Bool, NSError?) -> Void) ``` |
| To | ``` func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [LAContext.setCredential(_: Data?, type: LACredentialType) -> Bool](https://developer.apple.com/documentation/localauthentication/lacontext/1514168-setcredential)

|  | Declaration |
| --- | --- |
| From | ``` func setCredential(_ credential: NSData?, type type: LACredentialType) -> Bool ``` |
| To | ``` func setCredential(_ credential: Data?, type type: LACredentialType) -> Bool ``` |

Modified [LAContext.touchIDAuthenticationAllowableReuseDuration](https://developer.apple.com/documentation/localauthentication/lacontext/1622329-touchidauthenticationallowablere)

|  | Declaration |
| --- | --- |
| From | ``` var touchIDAuthenticationAllowableReuseDuration: NSTimeInterval ``` |
| To | ``` var touchIDAuthenticationAllowableReuseDuration: TimeInterval ``` |

Modified [LACredentialType [enum]](https://developer.apple.com/documentation/localauthentication/lacredentialtype)

|  | Declaration |
| --- | --- |
| From | ``` enum LACredentialType : Int {     case ApplicationPassword } ``` |
| To | ``` enum LACredentialType : Int {     case applicationPassword } ``` |

Modified [LACredentialType.applicationPassword](https://developer.apple.com/documentation/localauthentication/lacredentialtype/lacredentialtypeapplicationpassword)

|  | Declaration |
| --- | --- |
| From | ``` case ApplicationPassword ``` |
| To | ``` case applicationPassword ``` |

Modified [LAError.Code [enum]](https://developer.apple.com/documentation/localauthentication/laerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum LAError : Int {     case AuthenticationFailed     case UserCancel     case UserFallback     case SystemCancel     case PasscodeNotSet     case TouchIDNotAvailable     case TouchIDNotEnrolled     case TouchIDLockout     case AppCancel     case InvalidContext } extension LAError : _BridgedNSError { } extension LAError : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = LAError         case authenticationFailed         case userCancel         case userFallback         case systemCancel         case passcodeNotSet         case touchIDNotAvailable         case touchIDNotEnrolled         case touchIDLockout         case appCancel         case invalidContext     } ``` |

Modified [LAError.Code.appCancel](https://developer.apple.com/documentation/localauthentication/laerror/laerrorappcancel)

|  | Declaration |
| --- | --- |
| From | ``` case AppCancel ``` |
| To | ``` case appCancel ``` |

Modified [LAError.Code.authenticationFailed](https://developer.apple.com/documentation/localauthentication/laerror/laerrorauthenticationfailed)

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticationFailed ``` |
| To | ``` case authenticationFailed ``` |

Modified [LAError.Code.invalidContext](https://developer.apple.com/documentation/localauthentication/laerror/code/invalidcontext)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidContext ``` |
| To | ``` case invalidContext ``` |

Modified [LAError.Code.passcodeNotSet](https://developer.apple.com/documentation/localauthentication/laerror/laerrorpasscodenotset)

|  | Declaration |
| --- | --- |
| From | ``` case PasscodeNotSet ``` |
| To | ``` case passcodeNotSet ``` |

Modified [LAError.Code.systemCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/systemcancel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case SystemCancel ``` | iOS 8.0 |
| To | ``` case systemCancel ``` | iOS 10.0 |

Modified [LAError.Code.touchIDLockout](https://developer.apple.com/documentation/localauthentication/laerror/laerrortouchidlockout)

|  | Declaration |
| --- | --- |
| From | ``` case TouchIDLockout ``` |
| To | ``` case touchIDLockout ``` |

Modified [LAError.Code.touchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/laerror/laerrortouchidnotavailable)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TouchIDNotAvailable ``` | iOS 8.0 |
| To | ``` case touchIDNotAvailable ``` | iOS 10.0 |

Modified [LAError.Code.touchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/laerror/laerrortouchidnotenrolled)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TouchIDNotEnrolled ``` | iOS 8.0 |
| To | ``` case touchIDNotEnrolled ``` | iOS 10.0 |

Modified [LAError.Code.userCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/usercancel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UserCancel ``` | iOS 8.0 |
| To | ``` case userCancel ``` | iOS 10.0 |

Modified [LAError.Code.userFallback](https://developer.apple.com/documentation/localauthentication/laerror/code/userfallback)

|  | Declaration |
| --- | --- |
| From | ``` case UserFallback ``` |
| To | ``` case userFallback ``` |

Modified [LAPolicy [enum]](https://developer.apple.com/documentation/localauthentication/lapolicy)

|  | Declaration |
| --- | --- |
| From | ``` enum LAPolicy : Int {     case DeviceOwnerAuthenticationWithBiometrics     case DeviceOwnerAuthentication } ``` |
| To | ``` enum LAPolicy : Int {     case deviceOwnerAuthenticationWithBiometrics     case deviceOwnerAuthentication } ``` |

Modified [LAPolicy.deviceOwnerAuthentication](https://developer.apple.com/documentation/localauthentication/lapolicy/lapolicydeviceownerauthentication)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceOwnerAuthentication ``` |
| To | ``` case deviceOwnerAuthentication ``` |

Modified [LAPolicy.deviceOwnerAuthenticationWithBiometrics](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometrics)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceOwnerAuthenticationWithBiometrics ``` |
| To | ``` case deviceOwnerAuthenticationWithBiometrics ``` |

Modified [LATouchIDAuthenticationMaximumAllowableReuseDuration](https://developer.apple.com/documentation/localauthentication/latouchidauthenticationmaximumallowablereuseduration)

|  | Declaration |
| --- | --- |
| From | ``` let LATouchIDAuthenticationMaximumAllowableReuseDuration: NSTimeInterval ``` |
| To | ``` let LATouchIDAuthenticationMaximumAllowableReuseDuration: TimeInterval ``` |

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
