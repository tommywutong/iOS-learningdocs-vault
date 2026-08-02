---
title: iOS 10.1 API Diffs
apple_id: TP40017545
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS101APIDiffs/Swift/QuartzCore.html
archived_at: '2026-07-18T02:54:47.696262Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.1 API Diffs](iOS%2010.0%20to%20iOS%2010.1%20API%20Differences.md)


# QuartzCore Changes for Swift

### QuartzCore

Modified [CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction)

|  | Declaration |
| --- | --- |
| From | ``` class CATransaction : NSObject {     class func begin()     class func commit()     class func flush()     class func lock()     class func unlock()     class func animationDuration() -> CFTimeInterval     class func setAnimationDuration(_ dur: CFTimeInterval)     class func animationTimingFunction() -> CAMediaTimingFunction?     class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)     class func disableActions() -> Bool     class func setDisableActions(_ flag: Bool)     class func completionBlock() -> (() -> Swift.Void)?     class func setCompletionBlock(_ block: (@escaping () -> Swift.Void)?)     class func value(forKey key: String) -> Any?     class func setValue(_ anObject: Any?, forKey key: String)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CATransaction : CVarArg { } extension CATransaction : Equatable, Hashable {     var hashValue: Int { get } } ``` |
| To | ``` class CATransaction : NSObject {     class func begin()     class func commit()     class func flush()     class func lock()     class func unlock()     class func animationDuration() -> CFTimeInterval     class func setAnimationDuration(_ dur: CFTimeInterval)     class func animationTimingFunction() -> CAMediaTimingFunction?     class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)     class func disableActions() -> Bool     class func setDisableActions(_ flag: Bool)     class func completionBlock() -> (() -> Swift.Void)?     class func setCompletionBlock(_ block: (() -> Swift.Void)?)     class func value(forKey key: String) -> Any?     class func setValue(_ anObject: Any?, forKey key: String)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CATransaction : CVarArg { } extension CATransaction : Equatable, Hashable {     var hashValue: Int { get } } ``` |

Modified [CATransaction.setCompletionBlock(_: (() -> Swift.Void)?) [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448281-setcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` class func setCompletionBlock(_ block: (@escaping () -> Swift.Void)?) ``` |
| To | ``` class func setCompletionBlock(_ block: (() -> Swift.Void)?) ``` |

Modified [CATransform3D [struct]](https://developer.apple.com/documentation/quartzcore/catransform3d)

|  | Declaration |
| --- | --- |
| From | ``` struct CATransform3D {     var m11: CGFloat     var m12: CGFloat     var m13: CGFloat     var m14: CGFloat     var m21: CGFloat     var m22: CGFloat     var m23: CGFloat     var m24: CGFloat     var m31: CGFloat     var m32: CGFloat     var m33: CGFloat     var m34: CGFloat     var m41: CGFloat     var m42: CGFloat     var m43: CGFloat     var m44: CGFloat     init()     init(m11 m11: CGFloat, m12 m12: CGFloat, m13 m13: CGFloat, m14 m14: CGFloat, m21 m21: CGFloat, m22 m22: CGFloat, m23 m23: CGFloat, m24 m24: CGFloat, m31 m31: CGFloat, m32 m32: CGFloat, m33 m33: CGFloat, m34 m34: CGFloat, m41 m41: CGFloat, m42 m42: CGFloat, m43 m43: CGFloat, m44 m44: CGFloat) } ``` |
| To | ``` struct CATransform3D {     var m11: CGFloat     var m12: CGFloat     var m13: CGFloat     var m14: CGFloat     var m21: CGFloat     var m22: CGFloat     var m23: CGFloat     var m24: CGFloat     var m31: CGFloat     var m32: CGFloat     var m33: CGFloat     var m34: CGFloat     var m41: CGFloat     var m42: CGFloat     var m43: CGFloat     var m44: CGFloat     init()     init(m11 m11: CGFloat, m12 m12: CGFloat, m13 m13: CGFloat, m14 m14: CGFloat, m21 m21: CGFloat, m22 m22: CGFloat, m23 m23: CGFloat, m24 m24: CGFloat, m31 m31: CGFloat, m32 m32: CGFloat, m33 m33: CGFloat, m34 m34: CGFloat, m41 m41: CGFloat, m42 m42: CGFloat, m43 m43: CGFloat, m44 m44: CGFloat) } extension CATransform3D { } ``` |

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
