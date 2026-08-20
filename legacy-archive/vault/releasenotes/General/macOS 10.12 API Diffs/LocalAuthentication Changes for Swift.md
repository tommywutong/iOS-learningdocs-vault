---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/LocalAuthentication.html
archived_at: '2026-07-18T02:51:28.034011Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


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
| To | ``` class LAContext : NSObject {     func canEvaluatePolicy(_ policy: LAPolicy, error error: NSErrorPointer) -> Bool     func evaluatePolicy(_ policy: LAPolicy, localizedReason localizedReason: String, reply reply: @escaping (Bool, Error?) -> Swift.Void)     func invalidate()     func setCredential(_ credential: Data?, type type: LACredentialType) -> Bool     func isCredentialSet(_ type: LACredentialType) -> Bool     func evaluateAccessControl(_ accessControl: SecAccessControl, operation operation: LAAccessControlOperation, localizedReason localizedReason: String, reply reply: @escaping (Bool, Error?) -> Swift.Void)     var localizedFallbackTitle: String?     var localizedCancelTitle: String?     var maxBiometryFailures: NSNumber?     var evaluatedPolicyDomainState: Data? { get }     var touchIDAuthenticationAllowableReuseDuration: TimeInterval     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension LAContext : CVarArg { } extension LAContext : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

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
| From | ``` case SystemCancel ``` | OS X 10.10 |
| To | ``` case systemCancel ``` | OS X 10.12 |

Modified [LAError.Code.touchIDLockout](https://developer.apple.com/documentation/localauthentication/laerror/laerrortouchidlockout)

|  | Declaration |
| --- | --- |
| From | ``` case TouchIDLockout ``` |
| To | ``` case touchIDLockout ``` |

Modified [LAError.Code.touchIDNotAvailable](https://developer.apple.com/documentation/localauthentication/laerror/laerrortouchidnotavailable)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TouchIDNotAvailable ``` | OS X 10.10 |
| To | ``` case touchIDNotAvailable ``` | OS X 10.12 |

Modified [LAError.Code.touchIDNotEnrolled](https://developer.apple.com/documentation/localauthentication/laerror/laerrortouchidnotenrolled)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TouchIDNotEnrolled ``` | OS X 10.10 |
| To | ``` case touchIDNotEnrolled ``` | OS X 10.12 |

Modified [LAError.Code.userCancel](https://developer.apple.com/documentation/localauthentication/laerror/code/usercancel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case UserCancel ``` | OS X 10.10 |
| To | ``` case userCancel ``` | OS X 10.12 |

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
