---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/TVServices.html
archived_at: '2026-07-18T02:57:59.461075Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# TVServices Changes for Swift

### TVServices

Modified [NSNotification.Name.TVTopShelfItemsDidChange](https://developer.apple.com/documentation/tvservices/tvtopshelfitemsdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | TVTopShelfItemsDidChangeNotification | ``` let TVTopShelfItemsDidChangeNotification: String ``` |
| To | TVTopShelfItemsDidChange | ``` static let TVTopShelfItemsDidChange: NSNotification.Name ``` |

Modified [TVContentIdentifier](https://developer.apple.com/documentation/tvservices/tvcontentidentifier)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVContentIdentifier : NSObject, NSCopying, NSSecureCoding {     var identifier: String { get }     @NSCopying var container: TVContentIdentifier? { get }     convenience init?()     init?(identifier identifier: String, container container: TVContentIdentifier?)     init?(coder coder: NSCoder) } ``` | NSCopying, NSSecureCoding |
| To | ``` class TVContentIdentifier : NSObject, NSCopying, NSSecureCoding {     var identifier: String { get }     @NSCopying var container: TVContentIdentifier? { get }     convenience init?()     init?(identifier identifier: String, container container: TVContentIdentifier?)     init?(coder coder: NSCoder)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TVContentIdentifier : CVarArg { } extension TVContentIdentifier : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [TVContentItem](https://developer.apple.com/documentation/tvservices/tvcontentitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVContentItem : NSObject, NSCopying, NSSecureCoding {     @NSCopying var contentIdentifier: TVContentIdentifier { get }     @NSCopying var imageURL: NSURL?     var imageShape: TVContentItemImageShape     var title: String?     @NSCopying var lastAccessedDate: NSDate?     @NSCopying var expirationDate: NSDate?     @NSCopying var creationDate: NSDate?     @NSCopying var badgeCount: NSNumber?     @NSCopying var duration: NSNumber?     @NSCopying var currentPosition: NSNumber?     @NSCopying var hasPlayedToEnd: NSNumber?     @NSCopying var playURL: NSURL?     @NSCopying var displayURL: NSURL?     var topShelfItems: [TVContentItem]?     convenience init?()     init?(contentIdentifier ident: TVContentIdentifier)     init?(coder coder: NSCoder) } ``` | NSCopying, NSSecureCoding |
| To | ``` class TVContentItem : NSObject, NSCopying, NSSecureCoding {     @NSCopying var contentIdentifier: TVContentIdentifier { get }     var imageURL: URL?     var imageShape: TVContentItemImageShape     var title: String?     var lastAccessedDate: Date?     var expirationDate: Date?     var creationDate: Date?     @NSCopying var badgeCount: NSNumber?     @NSCopying var duration: NSNumber?     @NSCopying var currentPosition: NSNumber?     @NSCopying var hasPlayedToEnd: NSNumber?     var playURL: URL?     var displayURL: URL?     var topShelfItems: [TVContentItem]?     convenience init?()     init?(contentIdentifier ident: TVContentIdentifier)     init?(coder coder: NSCoder)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TVContentItem : CVarArg { } extension TVContentItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [TVContentItem.creationDate](https://developer.apple.com/documentation/tvservices/tvcontentitem/1627606-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var creationDate: NSDate? ``` |
| To | ``` var creationDate: Date? ``` |

Modified [TVContentItem.displayURL](https://developer.apple.com/documentation/tvservices/tvcontentitem/1627579-displayurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var displayURL: NSURL? ``` |
| To | ``` var displayURL: URL? ``` |

Modified [TVContentItem.expirationDate](https://developer.apple.com/documentation/tvservices/tvcontentitem/1627590-expirationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var expirationDate: NSDate? ``` |
| To | ``` var expirationDate: Date? ``` |

Modified [TVContentItem.imageURL](https://developer.apple.com/documentation/tvservices/tvcontentitem/1627608-imageurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var imageURL: NSURL? ``` |
| To | ``` var imageURL: URL? ``` |

Modified [TVContentItem.lastAccessedDate](https://developer.apple.com/documentation/tvservices/tvcontentitem/1627599-lastaccesseddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastAccessedDate: NSDate? ``` |
| To | ``` var lastAccessedDate: Date? ``` |

Modified [TVContentItem.playURL](https://developer.apple.com/documentation/tvservices/tvcontentitem/1627601-playurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var playURL: NSURL? ``` |
| To | ``` var playURL: URL? ``` |

Modified [TVContentItemImageShape [enum]](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape)

|  | Declaration |
| --- | --- |
| From | ``` enum TVContentItemImageShape : Int {     case None     case Poster     case Square     case SDTV     case HDTV     case Wide     case ExtraWide } ``` |
| To | ``` enum TVContentItemImageShape : Int {     case none     case poster     case square     case SDTV     case HDTV     case wide     case extraWide } ``` |

Modified [TVContentItemImageShape.extraWide](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape/tvcontentitemimageshapeextrawide)

|  | Declaration |
| --- | --- |
| From | ``` case ExtraWide ``` |
| To | ``` case extraWide ``` |

Modified [TVContentItemImageShape.none](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape/tvcontentitemimageshapenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [TVContentItemImageShape.poster](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape/poster)

|  | Declaration |
| --- | --- |
| From | ``` case Poster ``` |
| To | ``` case poster ``` |

Modified [TVContentItemImageShape.square](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape/square)

|  | Declaration |
| --- | --- |
| From | ``` case Square ``` |
| To | ``` case square ``` |

Modified [TVContentItemImageShape.wide](https://developer.apple.com/documentation/tvservices/tvcontentitemimageshape/tvcontentitemimageshapewide)

|  | Declaration |
| --- | --- |
| From | ``` case Wide ``` |
| To | ``` case wide ``` |

Modified [TVTopShelfContentStyle [enum]](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum TVTopShelfContentStyle : Int {     case Inset     case Sectioned } ``` |
| To | ``` enum TVTopShelfContentStyle : Int {     case inset     case sectioned } ``` |

Modified [TVTopShelfContentStyle.inset](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentstyle/inset)

|  | Declaration |
| --- | --- |
| From | ``` case Inset ``` |
| To | ``` case inset ``` |

Modified [TVTopShelfContentStyle.sectioned](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentstyle/sectioned)

|  | Declaration |
| --- | --- |
| From | ``` case Sectioned ``` |
| To | ``` case sectioned ``` |

Modified [TVTopShelfImageSize(shape: TVContentItemImageShape, style: TVTopShelfContentStyle) -> CGSize](https://developer.apple.com/documentation/tvservices/1627587-tvtopshelfimagesizeforshape)

|  | Declaration |
| --- | --- |
| From | ``` func TVTopShelfImageSizeForShape(_ shape: TVContentItemImageShape, _ style: TVTopShelfContentStyle) -> CGSize ``` |
| To | ``` func TVTopShelfImageSize(shape shape: TVContentItemImageShape, style style: TVTopShelfContentStyle) -> CGSize ``` |

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
