---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/PushKit.html
archived_at: '2026-07-18T02:55:36.702635Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# PushKit Changes for Swift

### PushKit

Added [PKPushType [struct]](https://developer.apple.com/documentation/pushkit/pkpushtype)Added [PKPushType.init(rawValue: String)](https://developer.apple.com/documentation/pushkit/pkpushtype/1845292-init)Modified [PKPushCredentials](https://developer.apple.com/documentation/pushkit/pkpushcredentials)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPushCredentials : NSObject {     var type: String! { get }     @NSCopying var token: NSData! { get } } ``` | -- |
| To | ``` class PKPushCredentials : NSObject {     var type: PKPushType { get }     var token: Data { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension PKPushCredentials : CVarArg { } extension PKPushCredentials : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPushCredentials.token](https://developer.apple.com/documentation/pushkit/pkpushcredentials/1614477-token)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var token: NSData! { get } ``` |
| To | ``` var token: Data { get } ``` |

Modified [PKPushCredentials.type](https://developer.apple.com/documentation/pushkit/pkpushcredentials/1614484-type)

|  | Declaration |
| --- | --- |
| From | ``` var type: String! { get } ``` |
| To | ``` var type: PKPushType { get } ``` |

Modified [PKPushPayload](https://developer.apple.com/documentation/pushkit/pkpushpayload)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPushPayload : NSObject {     var type: String! { get }     var dictionaryPayload: [NSObject : AnyObject]! { get } } ``` | -- |
| To | ``` class PKPushPayload : NSObject {     var type: PKPushType { get }     var dictionaryPayload: [AnyHashable : Any] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension PKPushPayload : CVarArg { } extension PKPushPayload : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPushPayload.dictionaryPayload](https://developer.apple.com/documentation/pushkit/pkpushpayload/1614474-dictionarypayload)

|  | Declaration |
| --- | --- |
| From | ``` var dictionaryPayload: [NSObject : AnyObject]! { get } ``` |
| To | ``` var dictionaryPayload: [AnyHashable : Any] { get } ``` |

Modified [PKPushPayload.type](https://developer.apple.com/documentation/pushkit/pkpushpayload/1614476-type)

|  | Declaration |
| --- | --- |
| From | ``` var type: String! { get } ``` |
| To | ``` var type: PKPushType { get } ``` |

Modified [PKPushRegistry](https://developer.apple.com/documentation/pushkit/pkpushregistry)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class PKPushRegistry : NSObject {     weak var delegate: PKPushRegistryDelegate!     var desiredPushTypes: Set<NSObject>!     func pushTokenForType(_ type: String!) -> NSData!     init!(queue queue: dispatch_queue_t!) } ``` | -- |
| To | ``` class PKPushRegistry : NSObject {     weak var delegate: PKPushRegistryDelegate?     var desiredPushTypes: Set<PKPushType>?     func pushToken(forType type: PKPushType) -> Data?     init(queue queue: DispatchQueue?)     convenience init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension PKPushRegistry : CVarArg { } extension PKPushRegistry : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [PKPushRegistry.delegate](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614468-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: PKPushRegistryDelegate! ``` |
| To | ``` weak var delegate: PKPushRegistryDelegate? ``` |

Modified [PKPushRegistry.desiredPushTypes](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614479-desiredpushtypes)

|  | Declaration |
| --- | --- |
| From | ``` var desiredPushTypes: Set<NSObject>! ``` |
| To | ``` var desiredPushTypes: Set<PKPushType>? ``` |

Modified [PKPushRegistry.init(queue: DispatchQueue?)](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614494-initwithqueue)

|  | Declaration |
| --- | --- |
| From | ``` init!(queue queue: dispatch_queue_t!) ``` |
| To | ``` init(queue queue: DispatchQueue?) ``` |

Modified [PKPushRegistry.pushToken(forType: PKPushType) -> Data?](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614472-pushtokenfortype)

|  | Declaration |
| --- | --- |
| From | ``` func pushTokenForType(_ type: String!) -> NSData! ``` |
| To | ``` func pushToken(forType type: PKPushType) -> Data? ``` |

Modified [PKPushRegistryDelegate](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol PKPushRegistryDelegate : NSObjectProtocol {     func pushRegistry(_ registry: PKPushRegistry!, didUpdatePushCredentials credentials: PKPushCredentials!, forType type: String!)     func pushRegistry(_ registry: PKPushRegistry!, didReceiveIncomingPushWithPayload payload: PKPushPayload!, forType type: String!)     optional func pushRegistry(_ registry: PKPushRegistry!, didInvalidatePushTokenForType type: String!) } ``` |
| To | ``` protocol PKPushRegistryDelegate : NSObjectProtocol {     func pushRegistry(_ registry: PKPushRegistry, didUpdate credentials: PKPushCredentials, forType type: PKPushType)     func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, forType type: PKPushType)     optional func pushRegistry(_ registry: PKPushRegistry, didInvalidatePushTokenForType type: PKPushType) } ``` |

Modified [PKPushRegistryDelegate.pushRegistry(_: PKPushRegistry, didInvalidatePushTokenForType: PKPushType)](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/1614490-pushregistry)

|  | Declaration |
| --- | --- |
| From | ``` optional func pushRegistry(_ registry: PKPushRegistry!, didInvalidatePushTokenForType type: String!) ``` |
| To | ``` optional func pushRegistry(_ registry: PKPushRegistry, didInvalidatePushTokenForType type: PKPushType) ``` |

Modified [PKPushRegistryDelegate.pushRegistry(_: PKPushRegistry, didReceiveIncomingPushWith: PKPushPayload, forType: PKPushType)](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/1614492-pushregistry)

|  | Declaration |
| --- | --- |
| From | ``` func pushRegistry(_ registry: PKPushRegistry!, didReceiveIncomingPushWithPayload payload: PKPushPayload!, forType type: String!) ``` |
| To | ``` func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, forType type: PKPushType) ``` |

Modified [PKPushRegistryDelegate.pushRegistry(_: PKPushRegistry, didUpdate: PKPushCredentials, forType: PKPushType)](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/1614470-pushregistry)

|  | Declaration |
| --- | --- |
| From | ``` func pushRegistry(_ registry: PKPushRegistry!, didUpdatePushCredentials credentials: PKPushCredentials!, forType type: String!) ``` |
| To | ``` func pushRegistry(_ registry: PKPushRegistry, didUpdate credentials: PKPushCredentials, forType type: PKPushType) ``` |

Modified [PKPushType.complication](https://developer.apple.com/documentation/pushkit/pkpushtypecomplication)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPushTypeComplication | ``` let PKPushTypeComplication: String ``` |
| To | complication | ``` static let complication: PKPushType ``` |

Modified [PKPushType.voIP](https://developer.apple.com/documentation/pushkit/pkpushtype/1614481-voip)

|  | Name | Declaration |
| --- | --- | --- |
| From | PKPushTypeVoIP | ``` let PKPushTypeVoIP: String ``` |
| To | voIP | ``` static let voIP: PKPushType ``` |

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
