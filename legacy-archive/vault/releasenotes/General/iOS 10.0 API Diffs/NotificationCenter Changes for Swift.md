---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/NotificationCenter.html
archived_at: '2026-07-18T02:55:34.738113Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# NotificationCenter Changes for Swift

### NotificationCenter

Added [NCWidgetDisplayMode [enum]](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode)Added [NCWidgetDisplayMode.compact](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode/compact)Added [NCWidgetDisplayMode.expanded](https://developer.apple.com/documentation/notificationcenter/ncwidgetdisplaymode/ncwidgetdisplaymodeexpanded)Added [NCWidgetProviding.widgetActiveDisplayModeDidChange(_: NCWidgetDisplayMode, withMaximumSize: CGSize)](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1649132-widgetactivedisplaymodedidchange)Added [NSExtensionContext.widgetActiveDisplayMode](https://developer.apple.com/documentation/foundation/nsextensioncontext/1649134-widgetactivedisplaymode)Added [NSExtensionContext.widgetLargestAvailableDisplayMode](https://developer.apple.com/documentation/foundation/nsextensioncontext/1649133-widgetlargestavailabledisplaymod)Added [NSExtensionContext.widgetMaximumSize(for: NCWidgetDisplayMode) -> CGSize](https://developer.apple.com/documentation/foundation/nsextensioncontext/1649135-widgetmaximumsizefordisplaymode)Added [UIVibrancyEffect.widgetPrimary() -> UIVibrancyEffect [class]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1771278-widgetprimaryvibrancyeffect)Added [UIVibrancyEffect.widgetSecondary() -> UIVibrancyEffect [class]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1771277-widgetsecondary)Modified [NCUpdateResult [enum]](https://developer.apple.com/documentation/notificationcenter/ncupdateresult)

|  | Declaration |
| --- | --- |
| From | ``` enum NCUpdateResult : UInt {     case NewData     case NoData     case Failed } ``` |
| To | ``` enum NCUpdateResult : UInt {     case newData     case noData     case failed } ``` |

Modified [NCUpdateResult.failed](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/failed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [NCUpdateResult.newData](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/newdata)

|  | Declaration |
| --- | --- |
| From | ``` case NewData ``` |
| To | ``` case newData ``` |

Modified [NCUpdateResult.noData](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/nodata)

|  | Declaration |
| --- | --- |
| From | ``` case NoData ``` |
| To | ``` case noData ``` |

Modified [NCWidgetController](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NCWidgetController : NSObject {     class func widgetController() -> Self     func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String) } ``` | -- |
| To | ``` class NCWidgetController : NSObject {     class func widgetController() -> Self     func setHasContent(_ flag: Bool, forWidgetWithBundleIdentifier bundleID: String)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension NCWidgetController : CVarArg { } extension NCWidgetController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding)

|  | Declaration |
| --- | --- |
| From | ``` protocol NCWidgetProviding : NSObjectProtocol {     optional func widgetPerformUpdateWithCompletionHandler(_ completionHandler: (NCUpdateResult) -> Void)     optional func widgetMarginInsetsForProposedMarginInsets(_ defaultMarginInsets: UIEdgeInsets) -> UIEdgeInsets } ``` |
| To | ``` protocol NCWidgetProviding : NSObjectProtocol {     optional func widgetPerformUpdate(completionHandler completionHandler: @escaping (NCUpdateResult) -> Swift.Void)     optional func widgetActiveDisplayModeDidChange(_ activeDisplayMode: NCWidgetDisplayMode, withMaximumSize maxSize: CGSize)     optional func widgetMarginInsets(forProposedMarginInsets defaultMarginInsets: UIEdgeInsets) -> UIEdgeInsets } ``` |

Modified [NCWidgetProviding.widgetMarginInsets(forProposedMarginInsets: UIEdgeInsets) -> UIEdgeInsets](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490248-widgetmargininsetsforproposedmar)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` optional func widgetMarginInsetsForProposedMarginInsets(_ defaultMarginInsets: UIEdgeInsets) -> UIEdgeInsets ``` | -- |
| To | ``` optional func widgetMarginInsets(forProposedMarginInsets defaultMarginInsets: UIEdgeInsets) -> UIEdgeInsets ``` | iOS 10.0 |

Modified [NCWidgetProviding.widgetPerformUpdate(completionHandler: (NCUpdateResult) -> Swift.Void)](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490262-widgetperformupdatewithcompletio)

|  | Declaration |
| --- | --- |
| From | ``` optional func widgetPerformUpdateWithCompletionHandler(_ completionHandler: (NCUpdateResult) -> Void) ``` |
| To | ``` optional func widgetPerformUpdate(completionHandler completionHandler: @escaping (NCUpdateResult) -> Swift.Void) ``` |

Modified [UIVibrancyEffect.notificationCenter() -> UIVibrancyEffect [class]](https://developer.apple.com/documentation/uikit/uivibrancyeffect/1613917-notificationcentervibrancyeffect)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func notificationCenterVibrancyEffect() -> UIVibrancyEffect ``` | iOS 8.1 | -- |
| To | ``` class func notificationCenter() -> UIVibrancyEffect ``` | iOS 8.0 | iOS 10.0 |

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
