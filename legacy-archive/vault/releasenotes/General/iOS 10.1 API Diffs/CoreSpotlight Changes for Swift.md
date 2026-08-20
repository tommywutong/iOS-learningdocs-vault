---
title: iOS 10.1 API Diffs
apple_id: TP40017545
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS101APIDiffs/Swift/CoreSpotlight.html
archived_at: '2026-07-18T02:54:46.342450Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.1 API Diffs](iOS%2010.0%20to%20iOS%2010.1%20API%20Differences.md)


# CoreSpotlight Changes for Swift

### CoreSpotlight

Modified [CSSearchableIndex](https://developer.apple.com/documentation/corespotlight/cssearchableindex)

|  | Declaration |
| --- | --- |
| From | ``` class CSSearchableIndex : NSObject {     weak var indexDelegate: CSSearchableIndexDelegate?     class func isIndexingAvailable() -> Bool     class func `default`() -> Self     init(name name: String)     init(name name: String, protectionClass protectionClass: String?)     func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func deleteSearchableItems(withIdentifiers identifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func deleteAllSearchableItems(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func beginBatch()     func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSSearchableIndex : CVarArg { } extension CSSearchableIndex : Equatable, Hashable {     var hashValue: Int { get } } extension CSSearchableIndex {     func beginBatch()     func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void) } ``` |
| To | ``` class CSSearchableIndex : NSObject {     weak var indexDelegate: CSSearchableIndexDelegate?     class func isIndexingAvailable() -> Bool     class func `default`() -> Self     init(name name: String)     init(name name: String, protectionClass protectionClass: String?)     func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func deleteSearchableItems(withIdentifiers identifiers: [String], completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String], completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func deleteAllSearchableItems(completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func beginBatch()     func endBatch(withClientState clientState: Data, completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CSSearchableIndex : CVarArg { } extension CSSearchableIndex : Equatable, Hashable {     var hashValue: Int { get } } extension CSSearchableIndex {     func beginBatch()     func endBatch(withClientState clientState: Data, completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void) } ``` |

Modified [CSSearchableIndex.deleteAllSearchableItems(completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620342-deleteallsearchableitems)

|  | Declaration |
| --- | --- |
| From | ``` func deleteAllSearchableItems(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func deleteAllSearchableItems(completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.deleteSearchableItems(withDomainIdentifiers: [String], completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620351-deletesearchableitemswithdomaini)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String], completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.deleteSearchableItems(withIdentifiers: [String], completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620337-deletesearchableitemswithidentif)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSearchableItems(withIdentifiers identifiers: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func deleteSearchableItems(withIdentifiers identifiers: [String], completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.endBatch(withClientState: Data, completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620344-endindexbatchwithclientstate)

|  | Declaration |
| --- | --- |
| From | ``` func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func endBatch(withClientState clientState: Data, completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.indexSearchableItems(_: [CSSearchableItem], completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620333-indexsearchableitems)

|  | Declaration |
| --- | --- |
| From | ``` func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func indexSearchableItems(_ items: [CSSearchableItem], completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

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
