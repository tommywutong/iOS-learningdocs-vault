---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/FinderSync.html
archived_at: '2026-07-18T02:51:17.581732Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# FinderSync Changes for Swift

### FinderSync

Modified [FIFinderSync](https://developer.apple.com/documentation/findersync/fifindersync)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class FIFinderSync : NSObject, FIFinderSyncProtocol, NSExtensionRequestHandling { } ``` | FIFinderSyncProtocol, NSExtensionRequestHandling |
| To | ``` class FIFinderSync : NSObject, FIFinderSyncProtocol, NSExtensionRequestHandling {     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension FIFinderSync : CVarArg { } extension FIFinderSync : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, FIFinderSyncProtocol, Hashable, NSExtensionRequestHandling |

Modified [FIFinderSyncController](https://developer.apple.com/documentation/findersync/fifindersynccontroller)

|  | Declaration |
| --- | --- |
| From | ``` class FIFinderSyncController : NSExtensionContext {     class func defaultController() -> Self     var directoryURLs: Set<NSURL>!     func setBadgeImage(_ image: NSImage, label label: String?, forBadgeIdentifier badgeID: String)     func setBadgeIdentifier(_ badgeID: String, forURL url: NSURL)     func targetedURL() -> NSURL?     func selectedItemURLs() -> [NSURL]? } ``` |
| To | ``` class FIFinderSyncController : NSExtensionContext {     class func `default`() -> Self     var directoryURLs: Set<URL>!     func setBadgeImage(_ image: NSImage, label label: String?, forBadgeIdentifier badgeID: String)     func setBadgeIdentifier(_ badgeID: String, for url: URL)     func targetedURL() -> URL?     func selectedItemURLs() -> [URL]? } ``` |

Modified [FIFinderSyncController.default() [class]](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501588-defaultcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultController() -> Self ``` |
| To | ``` class func `default`() -> Self ``` |

Modified [FIFinderSyncController.directoryURLs](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501579-directoryurls)

|  | Declaration |
| --- | --- |
| From | ``` var directoryURLs: Set<NSURL>! ``` |
| To | ``` var directoryURLs: Set<URL>! ``` |

Modified [FIFinderSyncController.selectedItemURLs() -> [URL]?](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501575-selecteditemurls)

|  | Declaration |
| --- | --- |
| From | ``` func selectedItemURLs() -> [NSURL]? ``` |
| To | ``` func selectedItemURLs() -> [URL]? ``` |

Modified [FIFinderSyncController.setBadgeIdentifier(_: String, for: URL)](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501577-setbadgeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func setBadgeIdentifier(_ badgeID: String, forURL url: NSURL) ``` |
| To | ``` func setBadgeIdentifier(_ badgeID: String, for url: URL) ``` |

Modified [FIFinderSyncController.targetedURL() -> URL?](https://developer.apple.com/documentation/findersync/fifindersynccontroller/1501595-targetedurl)

|  | Declaration |
| --- | --- |
| From | ``` func targetedURL() -> NSURL? ``` |
| To | ``` func targetedURL() -> URL? ``` |

Modified [FIFinderSyncProtocol](https://developer.apple.com/documentation/findersync/fifindersyncprotocol)

|  | Declaration |
| --- | --- |
| From | ``` protocol FIFinderSyncProtocol {     optional func menuForMenuKind(_ menu: FIMenuKind) -> NSMenu?     optional func beginObservingDirectoryAtURL(_ url: NSURL)     optional func endObservingDirectoryAtURL(_ url: NSURL)     optional func requestBadgeIdentifierForURL(_ url: NSURL)     optional var toolbarItemName: String { get }     @NSCopying optional var toolbarItemImage: NSImage { get }     optional var toolbarItemToolTip: String { get } } ``` |
| To | ``` protocol FIFinderSyncProtocol {     optional func menu(for menu: FIMenuKind) -> NSMenu?     optional func beginObservingDirectory(at url: URL)     optional func endObservingDirectory(at url: URL)     optional func requestBadgeIdentifier(for url: URL)     optional var toolbarItemName: String { get }     @NSCopying optional var toolbarItemImage: NSImage { get }     optional var toolbarItemToolTip: String { get } } ``` |

Modified [FIFinderSyncProtocol.beginObservingDirectory(at: URL)](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501578-beginobservingdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` optional func beginObservingDirectoryAtURL(_ url: NSURL) ``` |
| To | ``` optional func beginObservingDirectory(at url: URL) ``` |

Modified [FIFinderSyncProtocol.endObservingDirectory(at: URL)](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501582-endobservingdirectoryaturl)

|  | Declaration |
| --- | --- |
| From | ``` optional func endObservingDirectoryAtURL(_ url: NSURL) ``` |
| To | ``` optional func endObservingDirectory(at url: URL) ``` |

Modified [FIFinderSyncProtocol.menu(for: FIMenuKind) -> NSMenu?](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/1501585-menu)

|  | Declaration |
| --- | --- |
| From | ``` optional func menuForMenuKind(_ menu: FIMenuKind) -> NSMenu? ``` |
| To | ``` optional func menu(for menu: FIMenuKind) -> NSMenu? ``` |

Modified [FIFinderSyncProtocol.requestBadgeIdentifier(for: URL)](https://developer.apple.com/documentation/findersync/1501586-fifindersync/1501589-requestbadgeidentifierforurl)

|  | Declaration |
| --- | --- |
| From | ``` optional func requestBadgeIdentifierForURL(_ url: NSURL) ``` |
| To | ``` optional func requestBadgeIdentifier(for url: URL) ``` |

Modified [FIMenuKind [enum]](https://developer.apple.com/documentation/findersync/fimenukind)

|  | Declaration |
| --- | --- |
| From | ``` enum FIMenuKind : UInt {     case ContextualMenuForItems     case ContextualMenuForContainer     case ContextualMenuForSidebar     case ToolbarItemMenu } ``` |
| To | ``` enum FIMenuKind : UInt {     case contextualMenuForItems     case contextualMenuForContainer     case contextualMenuForSidebar     case toolbarItemMenu } ``` |

Modified [FIMenuKind.contextualMenuForContainer](https://developer.apple.com/documentation/findersync/fimenukind/contextualmenuforcontainer)

|  | Declaration |
| --- | --- |
| From | ``` case ContextualMenuForContainer ``` |
| To | ``` case contextualMenuForContainer ``` |

Modified [FIMenuKind.contextualMenuForItems](https://developer.apple.com/documentation/findersync/fimenukind/contextualmenuforitems)

|  | Declaration |
| --- | --- |
| From | ``` case ContextualMenuForItems ``` |
| To | ``` case contextualMenuForItems ``` |

Modified [FIMenuKind.contextualMenuForSidebar](https://developer.apple.com/documentation/findersync/fimenukind/contextualmenuforsidebar)

|  | Declaration |
| --- | --- |
| From | ``` case ContextualMenuForSidebar ``` |
| To | ``` case contextualMenuForSidebar ``` |

Modified [FIMenuKind.toolbarItemMenu](https://developer.apple.com/documentation/findersync/fimenukind/fimenukindtoolbaritemmenu)

|  | Declaration |
| --- | --- |
| From | ``` case ToolbarItemMenu ``` |
| To | ``` case toolbarItemMenu ``` |

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
