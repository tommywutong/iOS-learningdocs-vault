---
title: watchOS 2.2 API Diffs
apple_id: TP40016663
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS22APIDiffs/Swift/ObjectiveC.html
archived_at: '2026-07-18T02:58:11.968847Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.2 API Diffs](watchOS%202.1%20to%20watchOS%202.2%20API%20Differences.md)


# ObjectiveC Changes for Swift

### ObjectiveC

Modified [NSObject](https://developer.apple.com/documentation/objectivec/nsobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSObject : NSObjectProtocol {     class func load()     class func initialize()     init()     class func new() -> Self     class func allocWithZone(_ zone: NSZone) -> Self     class func alloc() -> Self     func finalize()     func copy() -> AnyObject     func mutableCopy() -> AnyObject     class func copyWithZone(_ zone: NSZone) -> AnyObject!     class func mutableCopyWithZone(_ zone: NSZone) -> AnyObject!     class func instancesRespondToSelector(_ aSelector: Selector) -> Bool     class func conformsToProtocol(_ `protocol`: Protocol) -> Bool     func methodForSelector(_ aSelector: Selector) -> IMP     class func instanceMethodForSelector(_ aSelector: Selector) -> IMP     func doesNotRecognizeSelector(_ aSelector: Selector)     func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject?     func forwardInvocation(_ anInvocation: NSInvocation!)     func methodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     class func instanceMethodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool     class func isSubclassOfClass(_ aClass: AnyClass) -> Bool     class func resolveClassMethod(_ sel: Selector) -> Bool     class func resolveInstanceMethod(_ sel: Selector) -> Bool     class func hash() -> Int     class func superclass() -> AnyClass?     class func `class`() -> AnyClass!     class func description() -> String     class func debugDescription() -> String } extension NSObject {     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject?, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int) -> Bool } extension NSObject {     func fileManager(_ fm: NSFileManager, shouldProceedAfterError errorInfo: [NSObject : AnyObject]) -> Bool     func fileManager(_ fm: NSFileManager, willProcessPath path: String) } extension NSObject {     class func accessInstanceVariablesDirectly() -> Bool     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValueForKey(_ key: String) -> NSMutableArray     func mutableOrderedSetValueForKey(_ key: String) -> NSMutableOrderedSet     func mutableSetValueForKey(_ key: String) -> NSMutableSet     func valueForKeyPath(_ keyPath: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValueForKeyPath(_ keyPath: String) -> NSMutableArray     func mutableOrderedSetValueForKeyPath(_ keyPath: String) -> NSMutableOrderedSet     func mutableSetValueForKeyPath(_ keyPath: String) -> NSMutableSet     func valueForUndefinedKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValuesForKeys(_ keys: [String]) -> [String : AnyObject]     func setValuesForKeysWithDictionary(_ keyedValues: [String : AnyObject]) } extension NSObject {     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) } extension NSObject {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSObject {     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>)     func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) } extension NSObject {     class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<String>     class func automaticallyNotifiesObserversForKey(_ key: String) -> Bool     var observationInfo: UnsafeMutablePointer<Void> } extension NSObject {     var classForKeyedArchiver: AnyClass? { get }     func replacementObjectForKeyedArchiver(_ archiver: NSKeyedArchiver) -> AnyObject?     class func classFallbacksForKeyedArchiver() -> [String] } extension NSObject {     class func classForKeyedUnarchiver() -> AnyClass } extension NSObject {     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObjectForCoder(_ aCoder: NSCoder) -> AnyObject?     func awakeAfterUsingCoder(_ aDecoder: NSCoder) -> AnyObject? } extension NSObject {     var autoContentAccessingProxy: AnyObject { get } } extension NSObject {     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval, inModes modes: [String])     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject, selector aSelector: Selector, object anArgument: AnyObject?)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject) } extension NSObject {     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelectorInBackground(_ aSelector: Selector, withObject arg: AnyObject?) } extension NSObject : CustomStringConvertible { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } ``` | CVarArgType, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |
| To | ``` class NSObject : NSObjectProtocol {     class func load()     class func initialize()     init()     class func new() -> Self     class func allocWithZone(_ zone: NSZone) -> Self     class func alloc() -> Self     func finalize()     func copy() -> AnyObject     func mutableCopy() -> AnyObject     class func copyWithZone(_ zone: NSZone) -> AnyObject!     class func mutableCopyWithZone(_ zone: NSZone) -> AnyObject!     class func instancesRespondToSelector(_ aSelector: Selector) -> Bool     class func conformsToProtocol(_ protocol: Protocol) -> Bool     func methodForSelector(_ aSelector: Selector) -> IMP     class func instanceMethodForSelector(_ aSelector: Selector) -> IMP     func doesNotRecognizeSelector(_ aSelector: Selector)     func forwardingTargetForSelector(_ aSelector: Selector) -> AnyObject?     func forwardInvocation(_ anInvocation: NSInvocation!)     func methodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     class func instanceMethodSignatureForSelector(_ aSelector: Selector) -> NSMethodSignature!     func allowsWeakReference() -> Bool     func retainWeakReference() -> Bool     class func isSubclassOfClass(_ aClass: AnyClass) -> Bool     class func resolveClassMethod(_ sel: Selector) -> Bool     class func resolveInstanceMethod(_ sel: Selector) -> Bool     class func hash() -> Int     class func superclass() -> AnyClass?     class func `class`() -> AnyClass!     class func description() -> String     class func debugDescription() -> String } extension NSObject {     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int, delegate delegate: AnyObject?, didRecoverSelector didRecoverSelector: Selector, contextInfo contextInfo: UnsafeMutablePointer<Void>)     func attemptRecoveryFromError(_ error: NSError, optionIndex recoveryOptionIndex: Int) -> Bool } extension NSObject {     func fileManager(_ fm: NSFileManager, shouldProceedAfterError errorInfo: [NSObject : AnyObject]) -> Bool     func fileManager(_ fm: NSFileManager, willProcessPath path: String) } extension NSObject {     class func accessInstanceVariablesDirectly() -> Bool     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValueForKey(_ key: String) -> NSMutableArray     func mutableOrderedSetValueForKey(_ key: String) -> NSMutableOrderedSet     func mutableSetValueForKey(_ key: String) -> NSMutableSet     func valueForKeyPath(_ keyPath: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValueForKeyPath(_ keyPath: String) -> NSMutableArray     func mutableOrderedSetValueForKeyPath(_ keyPath: String) -> NSMutableOrderedSet     func mutableSetValueForKeyPath(_ keyPath: String) -> NSMutableSet     func valueForUndefinedKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValuesForKeys(_ keys: [String]) -> [String : AnyObject]     func setValuesForKeysWithDictionary(_ keyedValues: [String : AnyObject]) } extension NSObject {     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) } extension NSObject {     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutablePointer<Void>)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String) } extension NSObject {     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAtIndexes indexes: NSIndexSet, forKey key: String)     func willChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>)     func didChangeValueForKey(_ key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, usingObjects objects: Set<NSObject>) } extension NSObject {     class func keyPathsForValuesAffectingValueForKey(_ key: String) -> Set<String>     class func automaticallyNotifiesObserversForKey(_ key: String) -> Bool     var observationInfo: UnsafeMutablePointer<Void> } extension NSObject {     var classForKeyedArchiver: AnyClass? { get }     func replacementObjectForKeyedArchiver(_ archiver: NSKeyedArchiver) -> AnyObject?     class func classFallbacksForKeyedArchiver() -> [String] } extension NSObject {     class func classForKeyedUnarchiver() -> AnyClass } extension NSObject {     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObjectForCoder(_ aCoder: NSCoder) -> AnyObject?     func awakeAfterUsingCoder(_ aDecoder: NSCoder) -> AnyObject? } extension NSObject {     var autoContentAccessingProxy: AnyObject { get } } extension NSObject {     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval, inModes modes: [String])     func performSelector(_ aSelector: Selector, withObject anArgument: AnyObject?, afterDelay delay: NSTimeInterval)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject, selector aSelector: Selector, object anArgument: AnyObject?)     class func cancelPreviousPerformRequestsWithTarget(_ aTarget: AnyObject) } extension NSObject {     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelectorOnMainThread(_ aSelector: Selector, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(_ aSelector: Selector, onThread thr: NSThread, withObject arg: AnyObject?, waitUntilDone wait: Bool)     func performSelectorInBackground(_ aSelector: Selector, withObject arg: AnyObject?) } extension NSObject : CustomDebugStringConvertible { } extension NSObject : CustomStringConvertible { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } extension NSObject : Equatable, Hashable {     var hashValue: Int { get } } extension NSObject : CVarArgType { } ``` | CVarArgType, CustomDebugStringConvertible, CustomStringConvertible, Equatable, Hashable, NSObjectProtocol |

Modified [NSObject.conformsToProtocol(_: Protocol) -> Bool [class]](https://developer.apple.com/documentation/objectivec/nsobject/1418893-conforms)

|  | Declaration |
| --- | --- |
| From | ``` class func conformsToProtocol(_ `protocol`: Protocol) -> Bool ``` |
| To | ``` class func conformsToProtocol(_ protocol: Protocol) -> Bool ``` |

Modified autoreleasepool(_: () -> Void)

|  | Declaration |
| --- | --- |
| From | ``` func autoreleasepool(@noescape _ code: () -> ()) ``` |
| To | ``` func autoreleasepool(@noescape _ code: () -> Void) ``` |

Modified [class_addProtocol(_: AnyClass!, _: Protocol!) -> Bool](https://developer.apple.com/documentation/objectivec/1418773-class_addprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func class_addProtocol(_ cls: AnyClass!, _ `protocol`: Protocol!) -> Bool ``` |
| To | ``` func class_addProtocol(_ cls: AnyClass!, _ protocol: Protocol!) -> Bool ``` |

Modified [class_conformsToProtocol(_: AnyClass!, _: Protocol!) -> Bool](https://developer.apple.com/documentation/objectivec/1418685-class_conformstoprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func class_conformsToProtocol(_ cls: AnyClass!, _ `protocol`: Protocol!) -> Bool ``` |
| To | ``` func class_conformsToProtocol(_ cls: AnyClass!, _ protocol: Protocol!) -> Bool ``` |

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
