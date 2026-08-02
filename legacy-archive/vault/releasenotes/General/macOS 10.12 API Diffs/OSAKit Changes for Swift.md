---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/OSAKit.html
archived_at: '2026-07-18T02:51:31.146832Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# OSAKit Changes for Swift

### OSAKit

Removed OSAStorageOptions.NullModified OSALanguage

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class OSALanguage : NSObject {     class func availableLanguages() -> [OSALanguage]      init?(forName name: String)     class func languageForName(_ name: String) -> OSALanguage?      init?(forScriptDataDescriptor descriptor: NSAppleEventDescriptor)     class func languageForScriptDataDescriptor(_ descriptor: NSAppleEventDescriptor) -> OSALanguage?     class func defaultLanguage() -> OSALanguage?     class func setDefaultLanguage(_ defaultLanguage: OSALanguage)     init(component component: Component)     func sharedLanguageInstance() -> OSALanguageInstance     var componentInstance: ComponentInstance { get }     var name: String? { get }     var info: String? { get }     var version: String? { get }     var type: OSType { get }     var subType: OSType { get }     var manufacturer: OSType { get }     var features: OSALanguageFeatures { get }     var threadSafe: Bool { get } } ``` | -- |
| To | ``` class OSALanguage : NSObject {     class func availableLanguages() -> [OSALanguage]      init?(forName name: String)     class func forName(_ name: String) -> OSALanguage?      init?(forScriptDataDescriptor descriptor: NSAppleEventDescriptor)     class func forScriptDataDescriptor(_ descriptor: NSAppleEventDescriptor) -> OSALanguage?     class func `default`() -> OSALanguage?     class func setDefault(_ defaultLanguage: OSALanguage)     init(component component: Component)     func sharedLanguageInstance() -> OSALanguageInstance     var componentInstance: ComponentInstance { get }     var name: String? { get }     var info: String? { get }     var version: String? { get }     var type: OSType { get }     var subType: OSType { get }     var manufacturer: OSType { get }     var features: OSALanguageFeatures { get }     var isThreadSafe: Bool { get }     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension OSALanguage : CVarArg { } extension OSALanguage : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified OSALanguage.default() [class]

|  | Declaration |
| --- | --- |
| From | ``` class func defaultLanguage() -> OSALanguage? ``` |
| To | ``` class func `default`() -> OSALanguage? ``` |

Modified OSALanguage.isThreadSafe

|  | Declaration |
| --- | --- |
| From | ``` var threadSafe: Bool { get } ``` |
| To | ``` var isThreadSafe: Bool { get } ``` |

Modified OSALanguage.setDefault(_: OSALanguage) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func setDefaultLanguage(_ defaultLanguage: OSALanguage) ``` |
| To | ``` class func setDefault(_ defaultLanguage: OSALanguage) ``` |

Modified OSALanguageFeatures [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OSALanguageFeatures : OptionSetType {     init(rawValue rawValue: UInt)     static var SupportsCompiling: OSALanguageFeatures { get }     static var SupportsGetSource: OSALanguageFeatures { get }     static var SupportsAECoercion: OSALanguageFeatures { get }     static var SupportsAESending: OSALanguageFeatures { get }     static var SupportsRecording: OSALanguageFeatures { get }     static var SupportsConvenience: OSALanguageFeatures { get }     static var SupportsDialects: OSALanguageFeatures { get }     static var SupportsEventHandling: OSALanguageFeatures { get } } ``` | OptionSetType |
| To | ``` struct OSALanguageFeatures : OptionSet {     init(rawValue rawValue: UInt)     static var supportsCompiling: OSALanguageFeatures { get }     static var supportsGetSource: OSALanguageFeatures { get }     static var supportsAECoercion: OSALanguageFeatures { get }     static var supportsAESending: OSALanguageFeatures { get }     static var supportsRecording: OSALanguageFeatures { get }     static var supportsConvenience: OSALanguageFeatures { get }     static var supportsDialects: OSALanguageFeatures { get }     static var supportsEventHandling: OSALanguageFeatures { get }     func intersect(_ other: OSALanguageFeatures) -> OSALanguageFeatures     func exclusiveOr(_ other: OSALanguageFeatures) -> OSALanguageFeatures     mutating func unionInPlace(_ other: OSALanguageFeatures)     mutating func intersectInPlace(_ other: OSALanguageFeatures)     mutating func exclusiveOrInPlace(_ other: OSALanguageFeatures)     func isSubsetOf(_ other: OSALanguageFeatures) -> Bool     func isDisjointWith(_ other: OSALanguageFeatures) -> Bool     func isSupersetOf(_ other: OSALanguageFeatures) -> Bool     mutating func subtractInPlace(_ other: OSALanguageFeatures)     func isStrictSupersetOf(_ other: OSALanguageFeatures) -> Bool     func isStrictSubsetOf(_ other: OSALanguageFeatures) -> Bool } extension OSALanguageFeatures {     func union(_ other: OSALanguageFeatures) -> OSALanguageFeatures     func intersection(_ other: OSALanguageFeatures) -> OSALanguageFeatures     func symmetricDifference(_ other: OSALanguageFeatures) -> OSALanguageFeatures } extension OSALanguageFeatures {     func contains(_ member: OSALanguageFeatures) -> Bool     mutating func insert(_ newMember: OSALanguageFeatures) -> (inserted: Bool, memberAfterInsert: OSALanguageFeatures)     mutating func remove(_ member: OSALanguageFeatures) -> OSALanguageFeatures?     mutating func update(with newMember: OSALanguageFeatures) -> OSALanguageFeatures? } extension OSALanguageFeatures {     convenience init()     mutating func formUnion(_ other: OSALanguageFeatures)     mutating func formIntersection(_ other: OSALanguageFeatures)     mutating func formSymmetricDifference(_ other: OSALanguageFeatures) } extension OSALanguageFeatures {     convenience init<S : Sequence where S.Iterator.Element == OSALanguageFeatures>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: OSALanguageFeatures...)     mutating func subtract(_ other: OSALanguageFeatures)     func isSubset(of other: OSALanguageFeatures) -> Bool     func isSuperset(of other: OSALanguageFeatures) -> Bool     func isDisjoint(with other: OSALanguageFeatures) -> Bool     func subtracting(_ other: OSALanguageFeatures) -> OSALanguageFeatures     var isEmpty: Bool { get }     func isStrictSuperset(of other: OSALanguageFeatures) -> Bool     func isStrictSubset(of other: OSALanguageFeatures) -> Bool } ``` | OptionSet |

Modified OSALanguageFeatures.supportsAECoercion

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsAECoercion: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsAECoercion: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsAESending

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsAESending: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsAESending: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsCompiling

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsCompiling: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsCompiling: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsConvenience

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsConvenience: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsConvenience: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsDialects

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsDialects: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsDialects: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsEventHandling

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsEventHandling: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsEventHandling: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsGetSource

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsGetSource: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsGetSource: OSALanguageFeatures { get } ``` |

Modified OSALanguageFeatures.supportsRecording

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsRecording: OSALanguageFeatures { get } ``` |
| To | ``` static var supportsRecording: OSALanguageFeatures { get } ``` |

Modified OSALanguageInstance

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class OSALanguageInstance : NSObject {     convenience init(language language: OSALanguage)     class func languageInstanceWithLanguage(_ language: OSALanguage) -> Self     init(language language: OSALanguage)     var language: OSALanguage { get }     var componentInstance: ComponentInstance { get }     var defaultTarget: NSAppleEventDescriptor?     func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString? } ``` | -- |
| To | ``` class OSALanguageInstance : NSObject {     convenience init(language language: OSALanguage)     class func withLanguage(_ language: OSALanguage) -> Self     init(language language: OSALanguage)     var language: OSALanguage { get }     var componentInstance: ComponentInstance { get }     var defaultTarget: NSAppleEventDescriptor?     func richText(from descriptor: NSAppleEventDescriptor) -> NSAttributedString?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension OSALanguageInstance : CVarArg { } extension OSALanguageInstance : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified OSALanguageInstance.richText(from: NSAppleEventDescriptor) -> NSAttributedString?

|  | Declaration |
| --- | --- |
| From | ``` func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString? ``` |
| To | ``` func richText(from descriptor: NSAppleEventDescriptor) -> NSAttributedString? ``` |

Modified OSAScript

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class OSAScript : NSObject, NSCopying {     class func scriptDataDescriptorWithContentsOfURL(_ url: NSURL) -> NSAppleEventDescriptor?     init(source source: String)     init(source source: String, language language: OSALanguage?)     init(source source: String, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions)     init?(contentsOfURL url: NSURL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init(contentsOfURL url: NSURL, language language: OSALanguage, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init(contentsOfURL url: NSURL, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws     init(compiledData data: NSData, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>)     init(compiledData data: NSData, fromURL url: NSURL?, usingStorageOptions storageOptions: OSAStorageOptions) throws     init(scriptDataDescriptor data: NSAppleEventDescriptor, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws     var source: String { get }     @NSCopying var url: NSURL? { get }     var language: OSALanguage     var languageInstance: OSALanguageInstance     var compiled: Bool { get }     func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     func executeHandlerWithName(_ name: String, arguments arguments: [AnyObject], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor?     @NSCopying var richTextSource: NSAttributedString? { get }     func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString?     func writeToURL(_ url: NSURL, ofType type: String, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func writeToURL(_ url: NSURL, ofType type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool     func compiledDataForType(_ type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData? } ``` | NSCopying |
| To | ``` class OSAScript : NSObject, NSCopying {     class func scriptDataDescriptor(withContentsOf url: URL) -> NSAppleEventDescriptor?     init(source source: String)     init(source source: String, language language: OSALanguage?)     init(source source: String, from url: URL?, languageInstance instance: OSALanguageInstance?, using storageOptions: OSAStorageOptions = [])     init?(contentsOf url: URL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)     init(contentsOf url: URL, language language: OSALanguage, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)     init(contentsOf url: URL, languageInstance instance: OSALanguageInstance?, using storageOptions: OSAStorageOptions = []) throws     init(compiledData data: Data, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)     init(compiledData data: Data, from url: URL?, using storageOptions: OSAStorageOptions = []) throws     init(scriptDataDescriptor data: NSAppleEventDescriptor, from url: URL?, languageInstance instance: OSALanguageInstance?, using storageOptions: OSAStorageOptions = []) throws     var source: String { get }     var url: URL? { get }     var language: OSALanguage     var languageInstance: OSALanguageInstance     var isCompiled: Bool { get }     func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool     func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?     func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?     func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?     func executeHandler(withName name: String, arguments arguments: [Any], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?     @NSCopying var richTextSource: NSAttributedString? { get }     func richText(from descriptor: NSAppleEventDescriptor) -> NSAttributedString?     func write(to url: URL, ofType type: String, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool     func write(to url: URL, ofType type: String, using storageOptions: OSAStorageOptions = [], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool     func compiledData(forType type: String, using storageOptions: OSAStorageOptions = [], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Data?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension OSAScript : CVarArg { } extension OSAScript : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified OSAScript.compileAndReturnError(_: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool ``` |

Modified OSAScript.compiledData(forType: String, using: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Data?

|  | Declaration |
| --- | --- |
| From | ``` func compiledDataForType(_ type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSData? ``` |
| To | ``` func compiledData(forType type: String, using storageOptions: OSAStorageOptions = [], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Data? ``` |

Modified OSAScript.executeAndReturnDisplayValue(_: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |
| To | ``` func executeAndReturnDisplayValue(_ displayValue: AutoreleasingUnsafeMutablePointer<NSAttributedString?>, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.executeAndReturnError(_: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |
| To | ``` func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.executeAppleEvent(_: NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |
| To | ``` func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.executeHandler(withName: String, arguments: [Any], error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor?

|  | Declaration |
| --- | --- |
| From | ``` func executeHandlerWithName(_ name: String, arguments arguments: [AnyObject], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> NSAppleEventDescriptor? ``` |
| To | ``` func executeHandler(withName name: String, arguments arguments: [Any], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.init(compiledData: Data, from: URL?, using: OSAStorageOptions) throws

|  | Declaration |
| --- | --- |
| From | ``` init(compiledData data: NSData, fromURL url: NSURL?, usingStorageOptions storageOptions: OSAStorageOptions) throws ``` |
| To | ``` init(compiledData data: Data, from url: URL?, using storageOptions: OSAStorageOptions = []) throws ``` |

Modified OSAScript.init(contentsOf: URL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)

|  | Declaration |
| --- | --- |
| From | ``` init?(contentsOfURL url: NSURL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) ``` |
| To | ``` init?(contentsOf url: URL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) ``` |

Modified OSAScript.init(contentsOf: URL, languageInstance: OSALanguageInstance?, using: OSAStorageOptions) throws

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws ``` |
| To | ``` init(contentsOf url: URL, languageInstance instance: OSALanguageInstance?, using storageOptions: OSAStorageOptions = []) throws ``` |

Modified OSAScript.init(scriptDataDescriptor: NSAppleEventDescriptor, from: URL?, languageInstance: OSALanguageInstance?, using: OSAStorageOptions) throws

|  | Declaration |
| --- | --- |
| From | ``` init(scriptDataDescriptor data: NSAppleEventDescriptor, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) throws ``` |
| To | ``` init(scriptDataDescriptor data: NSAppleEventDescriptor, from url: URL?, languageInstance instance: OSALanguageInstance?, using storageOptions: OSAStorageOptions = []) throws ``` |

Modified OSAScript.init(source: String, from: URL?, languageInstance: OSALanguageInstance?, using: OSAStorageOptions)

|  | Declaration |
| --- | --- |
| From | ``` init(source source: String, fromURL url: NSURL?, languageInstance instance: OSALanguageInstance?, usingStorageOptions storageOptions: OSAStorageOptions) ``` |
| To | ``` init(source source: String, from url: URL?, languageInstance instance: OSALanguageInstance?, using storageOptions: OSAStorageOptions = []) ``` |

Modified OSAScript.isCompiled

|  | Declaration |
| --- | --- |
| From | ``` var compiled: Bool { get } ``` |
| To | ``` var isCompiled: Bool { get } ``` |

Modified OSAScript.richText(from: NSAppleEventDescriptor) -> NSAttributedString?

|  | Declaration |
| --- | --- |
| From | ``` func richTextFromDescriptor(_ descriptor: NSAppleEventDescriptor) -> NSAttributedString? ``` |
| To | ``` func richText(from descriptor: NSAppleEventDescriptor) -> NSAttributedString? ``` |

Modified OSAScript.scriptDataDescriptor(withContentsOf: URL) -> NSAppleEventDescriptor? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func scriptDataDescriptorWithContentsOfURL(_ url: NSURL) -> NSAppleEventDescriptor? ``` |
| To | ``` class func scriptDataDescriptor(withContentsOf url: URL) -> NSAppleEventDescriptor? ``` |

Modified OSAScript.url

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var url: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified OSAScript.write(to: URL, ofType: String, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL, ofType type: String, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func write(to url: URL, ofType type: String, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool ``` |

Modified OSAScript.write(to: URL, ofType: String, using: OSAStorageOptions, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ url: NSURL, ofType type: String, usingStorageOptions storageOptions: OSAStorageOptions, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> Bool ``` |
| To | ``` func write(to url: URL, ofType type: String, using storageOptions: OSAStorageOptions = [], error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool ``` |

Modified OSAScriptController

|  | Declaration |
| --- | --- |
| From | ``` class OSAScriptController : NSController {     var scriptView: OSAScriptView?     var resultView: NSTextView?     @NSCopying var script: OSAScript?     var language: OSALanguage?     var scriptState: OSAScriptState { get }     var compiling: Bool { get }     @IBAction func compileScript(_ sender: AnyObject?)     @IBAction func recordScript(_ sender: AnyObject?)     @IBAction func runScript(_ sender: AnyObject?)     @IBAction func stopScript(_ sender: AnyObject?) } ``` |
| To | ``` class OSAScriptController : NSController {     var scriptView: OSAScriptView?     var resultView: NSTextView?     @NSCopying var script: OSAScript?     var language: OSALanguage?     var scriptState: OSAScriptState { get }     var isCompiling: Bool { get }     @IBAction func compileScript(_ sender: Any?)     @IBAction func recordScript(_ sender: Any?)     @IBAction func runScript(_ sender: Any?)     @IBAction func stopScript(_ sender: Any?) } ``` |

Modified OSAScriptController.compileScript(_: Any?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func compileScript(_ sender: AnyObject?) ``` |
| To | ``` @IBAction func compileScript(_ sender: Any?) ``` |

Modified OSAScriptController.isCompiling

|  | Declaration |
| --- | --- |
| From | ``` var compiling: Bool { get } ``` |
| To | ``` var isCompiling: Bool { get } ``` |

Modified OSAScriptController.recordScript(_: Any?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func recordScript(_ sender: AnyObject?) ``` |
| To | ``` @IBAction func recordScript(_ sender: Any?) ``` |

Modified OSAScriptController.runScript(_: Any?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func runScript(_ sender: AnyObject?) ``` |
| To | ``` @IBAction func runScript(_ sender: Any?) ``` |

Modified OSAScriptController.stopScript(_: Any?)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stopScript(_ sender: AnyObject?) ``` |
| To | ``` @IBAction func stopScript(_ sender: Any?) ``` |

Modified OSAScriptState [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum OSAScriptState : Int {     case Stopped     case Running     case Recording } ``` |
| To | ``` enum OSAScriptState : Int {     case stopped     case running     case recording } ``` |

Modified OSAScriptState.recording

|  | Declaration |
| --- | --- |
| From | ``` case Recording ``` |
| To | ``` case recording ``` |

Modified OSAScriptState.running

|  | Declaration |
| --- | --- |
| From | ``` case Running ``` |
| To | ``` case running ``` |

Modified OSAScriptState.stopped

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified OSAScriptView

|  | Declaration |
| --- | --- |
| From | ``` class OSAScriptView : NSTextView {     var source: String?     var usesScriptAssistant: Bool     var usesTabs: Bool     var tabWidth: Int     var wrapsLines: Bool     var indentsWrappedLines: Bool     var indentWidth: Int } ``` |
| To | ``` class OSAScriptView : NSTextView {     var source: String?     var usesScriptAssistant: Bool     var usesTabs: Bool     var tabWidth: Int     var wrapsLines: Bool     var indentsWrappedLines: Bool     var indentWidth: Int     func toggleBaseWritingDirection(_ sender: Any?)     @IBAction func orderFrontSharingServicePicker(_ sender: Any?)     @IBAction func toggleQuickLookPreviewPanel(_ sender: Any?)     func updateQuickLookPreviewPanel()     var smartInsertDeleteEnabled: Bool     func smartDeleteRange(forProposedRange proposedCharRange: NSRange) -> NSRange     func toggleSmartInsertDelete(_ sender: Any?)     func smartInsert(for pasteString: String, replacing charRangeToReplace: NSRange, before beforeString: AutoreleasingUnsafeMutablePointer<NSString?>?, after afterString: AutoreleasingUnsafeMutablePointer<NSString?>?)     func smartInsert(beforeStringFor pasteString: String, replacing charRangeToReplace: NSRange) -> String?     func smartInsert(afterStringFor pasteString: String, replacing charRangeToReplace: NSRange) -> String?     var isAutomaticQuoteSubstitutionEnabled: Bool     func toggleAutomaticQuoteSubstitution(_ sender: Any?)     var isAutomaticLinkDetectionEnabled: Bool     func toggleAutomaticLinkDetection(_ sender: Any?)     var isAutomaticDataDetectionEnabled: Bool     func toggleAutomaticDataDetection(_ sender: Any?)     var isAutomaticDashSubstitutionEnabled: Bool     func toggleAutomaticDashSubstitution(_ sender: Any?)     var isAutomaticTextReplacementEnabled: Bool     func toggleAutomaticTextReplacement(_ sender: Any?)     var isAutomaticSpellingCorrectionEnabled: Bool     func toggleAutomaticSpellingCorrection(_ sender: Any?)     var enabledTextCheckingTypes: NSTextCheckingTypes     func checkText(in range: NSRange, types checkingTypes: NSTextCheckingTypes, options options: [String : Any] = [:])     func handleTextCheckingResults(_ results: [NSTextCheckingResult], forRange range: NSRange, types checkingTypes: NSTextCheckingTypes, options options: [String : Any] = [:], orthography orthography: NSOrthography, wordCount wordCount: Int)     func orderFrontSubstitutionsPanel(_ sender: Any?)     func checkTextInSelection(_ sender: Any?)     func checkTextInDocument(_ sender: Any?)     var usesFindPanel: Bool     var usesFindBar: Bool     var isIncrementalSearchingEnabled: Bool     var selectedRanges: [NSValue]     func setSelectedRanges(_ ranges: [NSValue], affinity affinity: NSSelectionAffinity, stillSelecting stillSelectingFlag: Bool)     func setSelectedRange(_ charRange: NSRange, affinity affinity: NSSelectionAffinity, stillSelecting stillSelectingFlag: Bool)     var selectionAffinity: NSSelectionAffinity { get }     var selectionGranularity: NSSelectionGranularity     var selectedTextAttributes: [String : Any]     @NSCopying var insertionPointColor: NSColor     func updateInsertionPointStateAndRestartTimer(_ restartFlag: Bool)     var markedTextAttributes: [String : Any]?     var linkTextAttributes: [String : Any]?     var displaysLinkToolTips: Bool     var acceptsGlyphInfo: Bool     var usesRuler: Bool     var usesInspectorBar: Bool     var isContinuousSpellCheckingEnabled: Bool     func toggleContinuousSpellChecking(_ sender: Any?)     var spellCheckerDocumentTag: Int { get }     var isGrammarCheckingEnabled: Bool     func toggleGrammarChecking(_ sender: Any?)     func setSpellingState(_ value: Int, range charRange: NSRange)     var typingAttributes: [String : Any]     func shouldChangeText(inRanges affectedRanges: [NSValue], replacementStrings replacementStrings: [String]?) -> Bool     var rangesForUserTextChange: [NSValue]? { get }     var rangesForUserCharacterAttributeChange: [NSValue]? { get }     var rangesForUserParagraphAttributeChange: [NSValue]? { get }     func shouldChangeText(in affectedCharRange: NSRange, replacementString replacementString: String?) -> Bool     func didChangeText()     var rangeForUserTextChange: NSRange { get }     var rangeForUserCharacterAttributeChange: NSRange { get }     var rangeForUserParagraphAttributeChange: NSRange { get }     var allowsDocumentBackgroundColorChange: Bool     @NSCopying var defaultParagraphStyle: NSParagraphStyle?     var allowsUndo: Bool     func breakUndoCoalescing()     var isCoalescingUndo: Bool { get }     var allowsImageEditing: Bool     func showFindIndicator(for charRange: NSRange)     var usesRolloverButtonForSelection: Bool     unowned(unsafe) var delegate: NSTextViewDelegate?     var isEditable: Bool     var isSelectable: Bool     var isRichText: Bool     var importsGraphics: Bool     var drawsBackground: Bool     @NSCopying var backgroundColor: NSColor     var isFieldEditor: Bool     var usesFontPanel: Bool     var isRulerVisible: Bool     func setSelectedRange(_ charRange: NSRange)     var allowedInputSourceLocales: [String]?     func dragSelection(with event: NSEvent, offset mouseOffset: NSSize, slideBack slideBack: Bool) -> Bool     func dragImageForSelection(with event: NSEvent, origin origin: NSPointPointer?) -> NSImage?     var acceptableDragTypes: [String] { get }     func dragOperation(for dragInfo: NSDraggingInfo, type type: String) -> NSDragOperation     func cleanUpAfterDragOperation()     var writablePasteboardTypes: [String] { get }     func writeSelection(to pboard: NSPasteboard, type type: String) -> Bool     func writeSelection(to pboard: NSPasteboard, types types: [String]) -> Bool     var readablePasteboardTypes: [String] { get }     func preferredPasteboardType(from availableTypes: [String], restrictedToTypesFrom allowedTypes: [String]?) -> String?     func readSelection(from pboard: NSPasteboard, type type: String) -> Bool     func readSelection(from pboard: NSPasteboard) -> Bool     class func registerForServices()     func validRequestor(forSendType sendType: String, returnType returnType: String) -> Any?     func pasteAsPlainText(_ sender: Any?)     func pasteAsRichText(_ sender: Any?)     func complete(_ sender: Any?)     var rangeForUserCompletion: NSRange { get }     func completions(forPartialWordRange charRange: NSRange, indexOfSelectedItem index: UnsafeMutablePointer<Int>) -> [String]?     func insertCompletion(_ word: String, forPartialWordRange charRange: NSRange, movement movement: Int, isFinal flag: Bool) } ``` |

Modified OSAStorageOptions [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct OSAStorageOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var Null: OSAStorageOptions { get }     static var PreventGetSource: OSAStorageOptions { get }     static var CompileIntoContext: OSAStorageOptions { get }     static var DontSetScriptLocation: OSAStorageOptions { get }     static var StayOpenApplet: OSAStorageOptions { get }     static var ShowStartupScreen: OSAStorageOptions { get } } ``` | OptionSetType |
| To | ``` struct OSAStorageOptions : OptionSet {     init(rawValue rawValue: UInt)     static var null: OSAStorageOptions { get }     static var preventGetSource: OSAStorageOptions { get }     static var compileIntoContext: OSAStorageOptions { get }     static var dontSetScriptLocation: OSAStorageOptions { get }     static var stayOpenApplet: OSAStorageOptions { get }     static var showStartupScreen: OSAStorageOptions { get }     func intersect(_ other: OSAStorageOptions) -> OSAStorageOptions     func exclusiveOr(_ other: OSAStorageOptions) -> OSAStorageOptions     mutating func unionInPlace(_ other: OSAStorageOptions)     mutating func intersectInPlace(_ other: OSAStorageOptions)     mutating func exclusiveOrInPlace(_ other: OSAStorageOptions)     func isSubsetOf(_ other: OSAStorageOptions) -> Bool     func isDisjointWith(_ other: OSAStorageOptions) -> Bool     func isSupersetOf(_ other: OSAStorageOptions) -> Bool     mutating func subtractInPlace(_ other: OSAStorageOptions)     func isStrictSupersetOf(_ other: OSAStorageOptions) -> Bool     func isStrictSubsetOf(_ other: OSAStorageOptions) -> Bool } extension OSAStorageOptions {     func union(_ other: OSAStorageOptions) -> OSAStorageOptions     func intersection(_ other: OSAStorageOptions) -> OSAStorageOptions     func symmetricDifference(_ other: OSAStorageOptions) -> OSAStorageOptions } extension OSAStorageOptions {     func contains(_ member: OSAStorageOptions) -> Bool     mutating func insert(_ newMember: OSAStorageOptions) -> (inserted: Bool, memberAfterInsert: OSAStorageOptions)     mutating func remove(_ member: OSAStorageOptions) -> OSAStorageOptions?     mutating func update(with newMember: OSAStorageOptions) -> OSAStorageOptions? } extension OSAStorageOptions {     convenience init()     mutating func formUnion(_ other: OSAStorageOptions)     mutating func formIntersection(_ other: OSAStorageOptions)     mutating func formSymmetricDifference(_ other: OSAStorageOptions) } extension OSAStorageOptions {     convenience init<S : Sequence where S.Iterator.Element == OSAStorageOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: OSAStorageOptions...)     mutating func subtract(_ other: OSAStorageOptions)     func isSubset(of other: OSAStorageOptions) -> Bool     func isSuperset(of other: OSAStorageOptions) -> Bool     func isDisjoint(with other: OSAStorageOptions) -> Bool     func subtracting(_ other: OSAStorageOptions) -> OSAStorageOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: OSAStorageOptions) -> Bool     func isStrictSubset(of other: OSAStorageOptions) -> Bool } ``` | OptionSet |

Modified OSAStorageOptions.compileIntoContext

|  | Declaration |
| --- | --- |
| From | ``` static var CompileIntoContext: OSAStorageOptions { get } ``` |
| To | ``` static var compileIntoContext: OSAStorageOptions { get } ``` |

Modified OSAStorageOptions.dontSetScriptLocation

|  | Declaration |
| --- | --- |
| From | ``` static var DontSetScriptLocation: OSAStorageOptions { get } ``` |
| To | ``` static var dontSetScriptLocation: OSAStorageOptions { get } ``` |

Modified OSAStorageOptions.preventGetSource

|  | Declaration |
| --- | --- |
| From | ``` static var PreventGetSource: OSAStorageOptions { get } ``` |
| To | ``` static var preventGetSource: OSAStorageOptions { get } ``` |

Modified OSAStorageOptions.showStartupScreen

|  | Declaration |
| --- | --- |
| From | ``` static var ShowStartupScreen: OSAStorageOptions { get } ``` |
| To | ``` static var showStartupScreen: OSAStorageOptions { get } ``` |

Modified OSAStorageOptions.stayOpenApplet

|  | Declaration |
| --- | --- |
| From | ``` static var StayOpenApplet: OSAStorageOptions { get } ``` |
| To | ``` static var stayOpenApplet: OSAStorageOptions { get } ``` |

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
