---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/NewsstandKit.html
archived_at: '2026-07-18T02:55:34.687667Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# NewsstandKit Changes for Swift

### NewsstandKit

Modified [NKAssetDownload](https://developer.apple.com/documentation/newsstandkit/nkassetdownload)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NKAssetDownload : NSObject {     weak var issue: NKIssue? { get }     var identifier: String { get }     var userInfo: [NSObject : AnyObject]?     @NSCopying var URLRequest: NSURLRequest { get }     func downloadWithDelegate(_ delegate: NSURLConnectionDownloadDelegate) -> NSURLConnection } ``` | -- |
| To | ``` class NKAssetDownload : NSObject {     weak var issue: NKIssue? { get }     var identifier: String { get }     var userInfo: [AnyHashable : Any]?     var urlRequest: URLRequest { get }     func download(with delegate: NSURLConnectionDownloadDelegate) -> NSURLConnection     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NKAssetDownload : CVarArg { } extension NKAssetDownload : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NKAssetDownload.download(with: NSURLConnectionDownloadDelegate) -> NSURLConnection](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615792-download)

|  | Declaration |
| --- | --- |
| From | ``` func downloadWithDelegate(_ delegate: NSURLConnectionDownloadDelegate) -> NSURLConnection ``` |
| To | ``` func download(with delegate: NSURLConnectionDownloadDelegate) -> NSURLConnection ``` |

Modified [NKAssetDownload.urlRequest](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615802-urlrequest)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URLRequest: NSURLRequest { get } ``` |
| To | ``` var urlRequest: URLRequest { get } ``` |

Modified [NKAssetDownload.userInfo](https://developer.apple.com/documentation/newsstandkit/nkassetdownload/1615811-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` |
| To | ``` var userInfo: [AnyHashable : Any]? ``` |

Modified [NKIssue](https://developer.apple.com/documentation/newsstandkit/nkissue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NKIssue : NSObject {     var downloadingAssets: [NKAssetDownload] { get }     @NSCopying var contentURL: NSURL { get }     var status: NKIssueContentStatus { get }     var name: String { get }     @NSCopying var date: NSDate { get }     func addAssetWithRequest(_ request: NSURLRequest) -> NKAssetDownload } ``` | -- |
| To | ``` class NKIssue : NSObject {     var downloadingAssets: [NKAssetDownload] { get }     var contentURL: URL { get }     var status: NKIssueContentStatus { get }     var name: String { get }     var date: Date { get }     func addAsset(with request: URLRequest) -> NKAssetDownload     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NKIssue : CVarArg { } extension NKIssue : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NKIssue.addAsset(with: URLRequest) -> NKAssetDownload](https://developer.apple.com/documentation/newsstandkit/nkissue/1615794-addasset)

|  | Declaration |
| --- | --- |
| From | ``` func addAssetWithRequest(_ request: NSURLRequest) -> NKAssetDownload ``` |
| To | ``` func addAsset(with request: URLRequest) -> NKAssetDownload ``` |

Modified [NKIssue.contentURL](https://developer.apple.com/documentation/newsstandkit/nkissue/1615813-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var contentURL: NSURL { get } ``` |
| To | ``` var contentURL: URL { get } ``` |

Modified [NKIssue.date](https://developer.apple.com/documentation/newsstandkit/nkissue/1615809-date)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var date: NSDate { get } ``` |
| To | ``` var date: Date { get } ``` |

Modified [NKIssueContentStatus [enum]](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum NKIssueContentStatus : Int {     case None     case Downloading     case Available } ``` |
| To | ``` enum NKIssueContentStatus : Int {     case none     case downloading     case available } ``` |

Modified [NKIssueContentStatus.available](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus/nkissuecontentstatusavailable)

|  | Declaration |
| --- | --- |
| From | ``` case Available ``` |
| To | ``` case available ``` |

Modified [NKIssueContentStatus.downloading](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus/nkissuecontentstatusdownloading)

|  | Declaration |
| --- | --- |
| From | ``` case Downloading ``` |
| To | ``` case downloading ``` |

Modified [NKIssueContentStatus.none](https://developer.apple.com/documentation/newsstandkit/nkissuecontentstatus/nkissuecontentstatusnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [NKLibrary](https://developer.apple.com/documentation/newsstandkit/nklibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NKLibrary : NSObject {     var issues: [NKIssue] { get }     var downloadingAssets: [NKAssetDownload] { get }     var currentlyReadingIssue: NKIssue?     class func sharedLibrary() -> NKLibrary?     func issueWithName(_ name: String) -> NKIssue?     func addIssueWithName(_ name: String, date date: NSDate) -> NKIssue     func removeIssue(_ issue: NKIssue) } ``` | -- |
| To | ``` class NKLibrary : NSObject {     var issues: [NKIssue] { get }     var downloadingAssets: [NKAssetDownload] { get }     var currentlyReadingIssue: NKIssue?     class func shared() -> NKLibrary?     func issue(withName name: String) -> NKIssue?     func addIssue(withName name: String, date date: Date) -> NKIssue     func removeIssue(_ issue: NKIssue)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NKLibrary : CVarArg { } extension NKLibrary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NKLibrary.addIssue(withName: String, date: Date) -> NKIssue](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615804-addissuewithname)

|  | Declaration |
| --- | --- |
| From | ``` func addIssueWithName(_ name: String, date date: NSDate) -> NKIssue ``` |
| To | ``` func addIssue(withName name: String, date date: Date) -> NKIssue ``` |

Modified [NKLibrary.issue(withName: String) -> NKIssue?](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615796-issue)

|  | Declaration |
| --- | --- |
| From | ``` func issueWithName(_ name: String) -> NKIssue? ``` |
| To | ``` func issue(withName name: String) -> NKIssue? ``` |

Modified [NKLibrary.shared() -> NKLibrary? [class]](https://developer.apple.com/documentation/newsstandkit/nklibrary/1615801-sharedlibrary)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedLibrary() -> NKLibrary? ``` |
| To | ``` class func shared() -> NKLibrary? ``` |

Modified [NSNotification.Name.NKIssueDownloadCompleted](https://developer.apple.com/documentation/newsstandkit/nkissuedownloadcompletednotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | NKIssueDownloadCompletedNotification | ``` let NKIssueDownloadCompletedNotification: String ``` |
| To | NKIssueDownloadCompleted | ``` static let NKIssueDownloadCompleted: NSNotification.Name ``` |

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
