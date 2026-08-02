---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/Automator.html
archived_at: '2026-07-18T02:51:02.616348Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Automator Changes for Swift

### Automator

Modified [AMAction](https://developer.apple.com/documentation/automator/amaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AMAction : NSObject {     init?(definition dict: [String : AnyObject], fromArchive archived: Bool)     init(contentsOfURL fileURL: NSURL) throws     var name: String { get }     var ignoresInput: Bool { get }     var selectedInputType: String?     var selectedOutputType: String?     var progressValue: CGFloat     func runWithInput(_ input: AnyObject?, fromAction anAction: AMAction?, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>) -> AnyObject?     func runWithInput(_ input: AnyObject?) throws -> AnyObject     func runAsynchronouslyWithInput(_ input: AnyObject?)     func willFinishRunning()     func didFinishRunningWithError(_ errorInfo: [String : AnyObject]?)     func finishRunningWithError(_ error: NSError?)     var output: AnyObject?     func stop()     func reset()     func writeToDictionary(_ dictionary: NSMutableDictionary)     func opened()     func activated()     func closed()     func updateParameters()     func parametersUpdated()     var stopped: Bool { get } } ``` | -- |
| To | ``` class AMAction : NSObject {     init?(definition dict: [String : Any], fromArchive archived: Bool)     init(contentsOf fileURL: URL) throws     var name: String { get }     var ignoresInput: Bool { get }     var selectedInputType: String?     var selectedOutputType: String?     var progressValue: CGFloat     func run(withInput input: Any?, from anAction: AMAction?, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Any?     func run(withInput input: Any?) throws -> Any     func runAsynchronously(withInput input: Any?)     func willFinishRunning()     func didFinishRunningWithError(_ errorInfo: [String : Any]?)     func finishRunningWithError(_ error: Error?)     var output: Any?     func stop()     func reset()     func write(to dictionary: NSMutableDictionary)     func opened()     func activated()     func closed()     func updateParameters()     func parametersUpdated()     var isStopped: Bool { get }     func workflowControllerWillRun(_ controller: AMWorkflowController)     func workflowControllerWillStop(_ controller: AMWorkflowController)     func workflowControllerDidRun(_ controller: AMWorkflowController)     func workflowControllerDidStop(_ controller: AMWorkflowController)     func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didError error: Error)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension AMAction : CVarArg { } extension AMAction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AMAction.finishRunningWithError(_: Error?)](https://developer.apple.com/documentation/automator/amaction/1419677-finishrunningwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func finishRunningWithError(_ error: NSError?) ``` |
| To | ``` func finishRunningWithError(_ error: Error?) ``` |

Modified [AMAction.init(contentsOf: URL) throws](https://developer.apple.com/documentation/automator/amaction/1419742-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL fileURL: NSURL) throws ``` |
| To | ``` init(contentsOf fileURL: URL) throws ``` |

Modified [AMAction.init(definition: [String : Any], fromArchive: Bool)](https://developer.apple.com/documentation/automator/amaction/1419574-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(definition dict: [String : AnyObject], fromArchive archived: Bool) ``` |
| To | ``` init?(definition dict: [String : Any], fromArchive archived: Bool) ``` |

Modified [AMAction.isStopped](https://developer.apple.com/documentation/automator/amaction/1419600-isstopped)

|  | Declaration |
| --- | --- |
| From | ``` var stopped: Bool { get } ``` |
| To | ``` var isStopped: Bool { get } ``` |

Modified [AMAction.output](https://developer.apple.com/documentation/automator/amaction/1419786-output)

|  | Declaration |
| --- | --- |
| From | ``` var output: AnyObject? ``` |
| To | ``` var output: Any? ``` |

Modified [AMAction.run(withInput: Any?) throws -> Any](https://developer.apple.com/documentation/automator/amaction/1419624-run)

|  | Declaration |
| --- | --- |
| From | ``` func runWithInput(_ input: AnyObject?) throws -> AnyObject ``` |
| To | ``` func run(withInput input: Any?) throws -> Any ``` |

Modified [AMAction.runAsynchronously(withInput: Any?)](https://developer.apple.com/documentation/automator/amaction/1419691-runasynchronously)

|  | Declaration |
| --- | --- |
| From | ``` func runAsynchronouslyWithInput(_ input: AnyObject?) ``` |
| To | ``` func runAsynchronously(withInput input: Any?) ``` |

Modified [AMAction.write(to: NSMutableDictionary)](https://developer.apple.com/documentation/automator/amaction/1419736-writetodictionary)

|  | Declaration |
| --- | --- |
| From | ``` func writeToDictionary(_ dictionary: NSMutableDictionary) ``` |
| To | ``` func write(to dictionary: NSMutableDictionary) ``` |

Modified [AMBundleAction](https://developer.apple.com/documentation/automator/ambundleaction)

|  | Declaration |
| --- | --- |
| From | ``` class AMBundleAction : AMAction, NSCoding, NSCopying {     func awakeFromBundle()     var hasView: Bool { get }     var view: NSView? { get }     var bundle: NSBundle { get }     var parameters: NSMutableDictionary? } ``` |
| To | ``` class AMBundleAction : AMAction, NSCoding, NSCopying {     func awakeFromBundle()     var hasView: Bool { get }     var view: NSView? { get }     var bundle: Bundle { get }     var parameters: NSMutableDictionary? } ``` |

Modified [AMBundleAction.bundle](https://developer.apple.com/documentation/automator/ambundleaction/1419572-bundle)

|  | Declaration |
| --- | --- |
| From | ``` var bundle: NSBundle { get } ``` |
| To | ``` var bundle: Bundle { get } ``` |

Modified [AMLogLevel [enum]](https://developer.apple.com/documentation/automator/amloglevel)

|  | Declaration |
| --- | --- |
| From | ``` enum AMLogLevel : UInt {     case Debug     case Info     case Warn     case Error } ``` |
| To | ``` enum AMLogLevel : UInt {     case debug     case info     case warn     case error } ``` |

Modified [AMLogLevel.debug](https://developer.apple.com/documentation/automator/amloglevel/amlogleveldebug)

|  | Declaration |
| --- | --- |
| From | ``` case Debug ``` |
| To | ``` case debug ``` |

Modified [AMLogLevel.error](https://developer.apple.com/documentation/automator/amloglevel/error)

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified [AMLogLevel.info](https://developer.apple.com/documentation/automator/amloglevel/info)

|  | Declaration |
| --- | --- |
| From | ``` case Info ``` |
| To | ``` case info ``` |

Modified [AMLogLevel.warn](https://developer.apple.com/documentation/automator/amloglevel/amloglevelwarn)

|  | Declaration |
| --- | --- |
| From | ``` case Warn ``` |
| To | ``` case warn ``` |

Modified [AMWorkflow](https://developer.apple.com/documentation/automator/amworkflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AMWorkflow : NSObject, NSCopying {     class func runWorkflowAtURL(_ fileURL: NSURL, withInput input: AnyObject?) throws -> AnyObject     init()     convenience init(contentsOfURL fileURL: NSURL) throws     func writeToURL(_ fileURL: NSURL) throws     func setValue(_ value: AnyObject?, forVariableWithName variableName: String) -> Bool     func valueForVariableWithName(_ variableName: String) -> AnyObject     func addAction(_ action: AMAction)     func removeAction(_ action: AMAction)     func insertAction(_ action: AMAction, atIndex index: Int)     func moveActionAtIndex(_ startIndex: Int, toIndex endIndex: Int)     @NSCopying var fileURL: NSURL? { get }     var actions: [AMAction] { get }     var input: AnyObject?     var output: AnyObject? { get } } ``` | NSCopying |
| To | ``` class AMWorkflow : NSObject, NSCopying {     class func run(at fileURL: URL, withInput input: Any?) throws -> Any     init()     convenience init(contentsOf fileURL: URL) throws     func write(to fileURL: URL) throws     func setValue(_ value: Any?, forVariableWithName variableName: String) -> Bool     func valueForVariable(withName variableName: String) -> Any     func addAction(_ action: AMAction)     func removeAction(_ action: AMAction)     func insertAction(_ action: AMAction, at index: Int)     func moveAction(at startIndex: Int, to endIndex: Int)     var fileURL: URL? { get }     var actions: [AMAction] { get }     var input: Any?     var output: Any? { get }     func workflowControllerWillRun(_ controller: AMWorkflowController)     func workflowControllerWillStop(_ controller: AMWorkflowController)     func workflowControllerDidRun(_ controller: AMWorkflowController)     func workflowControllerDidStop(_ controller: AMWorkflowController)     func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didError error: Error)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension AMWorkflow : CVarArg { } extension AMWorkflow : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [AMWorkflow.fileURL](https://developer.apple.com/documentation/automator/amworkflow/1419726-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fileURL: NSURL? { get } ``` |
| To | ``` var fileURL: URL? { get } ``` |

Modified [AMWorkflow.init(contentsOf: URL) throws](https://developer.apple.com/documentation/automator/amworkflow/1419774-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(contentsOfURL fileURL: NSURL) throws ``` |
| To | ``` convenience init(contentsOf fileURL: URL) throws ``` |

Modified [AMWorkflow.input](https://developer.apple.com/documentation/automator/amworkflow/1419587-input)

|  | Declaration |
| --- | --- |
| From | ``` var input: AnyObject? ``` |
| To | ``` var input: Any? ``` |

Modified [AMWorkflow.insertAction(_: AMAction, at: Int)](https://developer.apple.com/documentation/automator/amworkflow/1419714-insertaction)

|  | Declaration |
| --- | --- |
| From | ``` func insertAction(_ action: AMAction, atIndex index: Int) ``` |
| To | ``` func insertAction(_ action: AMAction, at index: Int) ``` |

Modified [AMWorkflow.moveAction(at: Int, to: Int)](https://developer.apple.com/documentation/automator/amworkflow/1419734-moveaction)

|  | Declaration |
| --- | --- |
| From | ``` func moveActionAtIndex(_ startIndex: Int, toIndex endIndex: Int) ``` |
| To | ``` func moveAction(at startIndex: Int, to endIndex: Int) ``` |

Modified [AMWorkflow.output](https://developer.apple.com/documentation/automator/amworkflow/1419626-output)

|  | Declaration |
| --- | --- |
| From | ``` var output: AnyObject? { get } ``` |
| To | ``` var output: Any? { get } ``` |

Modified [AMWorkflow.run(at: URL, withInput: Any?) throws -> Any [class]](https://developer.apple.com/documentation/automator/amworkflow/1419750-run)

|  | Declaration |
| --- | --- |
| From | ``` class func runWorkflowAtURL(_ fileURL: NSURL, withInput input: AnyObject?) throws -> AnyObject ``` |
| To | ``` class func run(at fileURL: URL, withInput input: Any?) throws -> Any ``` |

Modified [AMWorkflow.setValue(_: Any?, forVariableWithName: String) -> Bool](https://developer.apple.com/documentation/automator/amworkflow/1419768-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject?, forVariableWithName variableName: String) -> Bool ``` |
| To | ``` func setValue(_ value: Any?, forVariableWithName variableName: String) -> Bool ``` |

Modified [AMWorkflow.valueForVariable(withName: String) -> Any](https://developer.apple.com/documentation/automator/amworkflow/1419622-valueforvariablewithname)

|  | Declaration |
| --- | --- |
| From | ``` func valueForVariableWithName(_ variableName: String) -> AnyObject ``` |
| To | ``` func valueForVariable(withName variableName: String) -> Any ``` |

Modified [AMWorkflow.write(to: URL) throws](https://developer.apple.com/documentation/automator/amworkflow/1419685-writetourl)

|  | Declaration |
| --- | --- |
| From | ``` func writeToURL(_ fileURL: NSURL) throws ``` |
| To | ``` func write(to fileURL: URL) throws ``` |

Modified [AMWorkflowController](https://developer.apple.com/documentation/automator/amworkflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class AMWorkflowController : NSController {     var workflow: AMWorkflow?     var workflowView: AMWorkflowView?     unowned(unsafe) var delegate: AnyObject?     var canRun: Bool { get }     var running: Bool { get }     @IBAction func run(_ sender: AnyObject)     @IBAction func stop(_ sender: AnyObject)     var paused: Bool { get }     @IBAction func pause(_ sender: AnyObject)     @IBAction func step(_ sender: AnyObject)     @IBAction func reset(_ sender: AnyObject) } ``` |
| To | ``` class AMWorkflowController : NSController {     var workflow: AMWorkflow?     var workflowView: AMWorkflowView?     unowned(unsafe) var delegate: AnyObject?     var canRun: Bool { get }     var isRunning: Bool { get }     @IBAction func run(_ sender: Any)     @IBAction func stop(_ sender: Any)     var isPaused: Bool { get }     @IBAction func pause(_ sender: Any)     @IBAction func step(_ sender: Any)     @IBAction func reset(_ sender: Any) } ``` |

Modified [AMWorkflowController.isPaused](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419746-paused)

|  | Declaration |
| --- | --- |
| From | ``` var paused: Bool { get } ``` |
| To | ``` var isPaused: Bool { get } ``` |

Modified [AMWorkflowController.isRunning](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419694-running)

|  | Declaration |
| --- | --- |
| From | ``` var running: Bool { get } ``` |
| To | ``` var isRunning: Bool { get } ``` |

Modified [AMWorkflowController.pause(_: Any)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419659-pause)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func pause(_ sender: AnyObject) ``` |
| To | ``` @IBAction func pause(_ sender: Any) ``` |

Modified [AMWorkflowController.reset(_: Any)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419748-reset)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func reset(_ sender: AnyObject) ``` |
| To | ``` @IBAction func reset(_ sender: Any) ``` |

Modified [AMWorkflowController.run(_: Any)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419780-run)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func run(_ sender: AnyObject) ``` |
| To | ``` @IBAction func run(_ sender: Any) ``` |

Modified [AMWorkflowController.step(_: Any)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419740-step)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func step(_ sender: AnyObject) ``` |
| To | ``` @IBAction func step(_ sender: Any) ``` |

Modified [AMWorkflowController.stop(_: Any)](https://developer.apple.com/documentation/automator/amworkflowcontroller/1419712-stop)

|  | Declaration |
| --- | --- |
| From | ``` @IBAction func stop(_ sender: AnyObject) ``` |
| To | ``` @IBAction func stop(_ sender: Any) ``` |

Modified [AMWorkflowView](https://developer.apple.com/documentation/automator/amworkflowview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AMWorkflowView : NSView {     var editable: Bool     var workflowController: AMWorkflowController? } ``` | -- |
| To | ``` class AMWorkflowView : NSView {     var isEditable: Bool     var workflowController: AMWorkflowController?     var pressureConfiguration: NSPressureConfiguration?     var wantsExtendedDynamicRangeOpenGLSurface: Bool     var wantsBestResolutionOpenGLSurface: Bool     func rulerView(_ ruler: NSRulerView, shouldMove marker: NSRulerMarker) -> Bool     func rulerView(_ ruler: NSRulerView, willMove marker: NSRulerMarker, toLocation location: CGFloat) -> CGFloat     func rulerView(_ ruler: NSRulerView, didMove marker: NSRulerMarker)     func rulerView(_ ruler: NSRulerView, shouldRemove marker: NSRulerMarker) -> Bool     func rulerView(_ ruler: NSRulerView, didRemove marker: NSRulerMarker)     func rulerView(_ ruler: NSRulerView, shouldAdd marker: NSRulerMarker) -> Bool     func rulerView(_ ruler: NSRulerView, willAdd marker: NSRulerMarker, atLocation location: CGFloat) -> CGFloat     func rulerView(_ ruler: NSRulerView, didAdd marker: NSRulerMarker)     func rulerView(_ ruler: NSRulerView, handleMouseDownWith event: NSEvent)     func rulerView(_ ruler: NSRulerView, willSetClientView newClient: NSView)     func rulerView(_ ruler: NSRulerView, locationFor point: NSPoint) -> CGFloat     func rulerView(_ ruler: NSRulerView, pointForLocation point: CGFloat) -> NSPoint     func addLayoutGuide(_ guide: NSLayoutGuide)     func removeLayoutGuide(_ guide: NSLayoutGuide)     var layoutGuides: [NSLayoutGuide] { get }     func constraintsAffectingLayout(for orientation: NSLayoutConstraintOrientation) -> [NSLayoutConstraint]     var hasAmbiguousLayout: Bool { get }     func exerciseAmbiguityInLayout()     var fittingSize: NSSize { get }     func alignmentRect(forFrame frame: NSRect) -> NSRect     func frame(forAlignmentRect alignmentRect: NSRect) -> NSRect     var alignmentRectInsets: EdgeInsets { get }     var firstBaselineOffsetFromTop: CGFloat { get }     var lastBaselineOffsetFromBottom: CGFloat { get }     var baselineOffsetFromBottom: CGFloat { get }     var intrinsicContentSize: NSSize { get }     func invalidateIntrinsicContentSize()     func contentHuggingPriority(for orientation: NSLayoutConstraintOrientation) -> NSLayoutPriority     func setContentHuggingPriority(_ priority: NSLayoutPriority, for orientation: NSLayoutConstraintOrientation)     func contentCompressionResistancePriority(for orientation: NSLayoutConstraintOrientation) -> NSLayoutPriority     func setContentCompressionResistancePriority(_ priority: NSLayoutPriority, for orientation: NSLayoutConstraintOrientation)     var translatesAutoresizingMaskIntoConstraints: Bool     class func requiresConstraintBasedLayout() -> Bool     func updateConstraintsForSubtreeIfNeeded()     func updateConstraints()     var needsUpdateConstraints: Bool     func layoutSubtreeIfNeeded()     func layout()     var needsLayout: Bool     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get }     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint])     var enclosingMenuItem: NSMenuItem? { get }     func reflectScrolledClipView(_ clipView: NSClipView)     func scroll(_ clipView: NSClipView, to point: NSPoint)     func drag(_ image: NSImage, at viewLocation: NSPoint, offset initialOffset: NSSize, event event: NSEvent, pasteboard pboard: NSPasteboard, source sourceObj: Any, slideBack slideFlag: Bool)     func convertPoint(toBase point: NSPoint) -> NSPoint     func convertPoint(fromBase point: NSPoint) -> NSPoint     func convertSize(toBase size: NSSize) -> NSSize     func convertSize(fromBase size: NSSize) -> NSSize     func convertRect(toBase rect: NSRect) -> NSRect     func convertRect(fromBase rect: NSRect) -> NSRect     func performMnemonic(_ string: String) -> Bool     func shouldDrawColor() -> Bool     func gState() -> Int     func allocateGState()     func releaseGState()     func setUpGState()     func renewGState()     var gestureRecognizers: [NSGestureRecognizer]     func addGestureRecognizer(_ gestureRecognizer: NSGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: NSGestureRecognizer)     var isDrawingFindIndicator: Bool { get }     func showDefinition(for attrString: NSAttributedString?, at textBaselineOrigin: NSPoint)     func showDefinition(for attrString: NSAttributedString?, range targetRange: NSRange, options options: [String : Any]? = nil, baselineOriginProvider originProvider: (@escaping (NSRange) -> NSPoint)? = nil)     func enterFullScreenMode(_ screen: NSScreen, withOptions options: [String : Any]? = nil) -> Bool     func exitFullScreenMode(options options: [String : Any]? = nil)     var isInFullScreenMode: Bool { get }     func beginDraggingSession(with items: [NSDraggingItem], event event: NSEvent, source source: NSDraggingSource) -> NSDraggingSession     var registeredDraggedTypes: [String] { get }     func register(forDraggedTypes newTypes: [String])     func unregisterDraggedTypes()     func dragFile(_ filename: String, from rect: NSRect, slideBack flag: Bool, event event: NSEvent) -> Bool     func dragPromisedFiles(ofTypes typeArray: [String], from rect: NSRect, source sourceObject: Any, slideBack flag: Bool, event event: NSEvent) -> Bool     func writeEPS(inside rect: NSRect, to pasteboard: NSPasteboard)     func dataWithEPS(inside rect: NSRect) -> Data     func writePDF(inside rect: NSRect, to pasteboard: NSPasteboard)     func dataWithPDF(inside rect: NSRect) -> Data     @warn_unqualified_access     func print(_ sender: Any?)     func knowsPageRange(_ range: NSRangePointer) -> Bool     var heightAdjustLimit: CGFloat { get }     var widthAdjustLimit: CGFloat { get }     func adjustPageWidthNew(_ newRight: UnsafeMutablePointer<CGFloat>, left oldLeft: CGFloat, right oldRight: CGFloat, limit rightLimit: CGFloat)     func adjustPageHeightNew(_ newBottom: UnsafeMutablePointer<CGFloat>, top oldTop: CGFloat, bottom oldBottom: CGFloat, limit bottomLimit: CGFloat)     func rectForPage(_ page: Int) -> NSRect     func locationOfPrintRect(_ rect: NSRect) -> NSPoint     func drawPageBorder(with borderSize: NSSize)     @NSCopying var pageHeader: NSAttributedString { get }     @NSCopying var pageFooter: NSAttributedString { get }     func drawSheetBorder(with borderSize: NSSize)     var printJobTitle: String { get }     func beginDocument()     func endDocument()     func beginPage(in rect: NSRect, atPlacement location: NSPoint)     func endPage()     unowned(unsafe) var nextKeyView: NSView?     unowned(unsafe) var previousKeyView: NSView? { get }     unowned(unsafe) var nextValidKeyView: NSView? { get }     unowned(unsafe) var previousValidKeyView: NSView? { get }     var canBecomeKeyView: Bool { get }     func setKeyboardFocusRingNeedsDisplay(_ rect: NSRect)     var focusRingType: NSFocusRingType     class func defaultFocusRingType() -> NSFocusRingType     func drawFocusRingMask()     var focusRingMaskBounds: NSRect { get }     func noteFocusRingMaskChanged()     func encodeRestorableState(with coder: NSCoder)     func restoreState(with coder: NSCoder)     func invalidateRestorableState()     class func restorableStateKeyPaths() -> [String]     func interfaceStyle() -> Int     func setInterfaceStyle(_ interfaceStyle: Int)     var userActivity: NSUserActivity?     func updateUserActivityState(_ userActivity: NSUserActivity)     func restoreUserActivityState(_ userActivity: NSUserActivity)     @IBAction func newWindowForTab(_ sender: Any?)     func performTextFinderAction(_ sender: Any?)     func presentError(_ error: Error, modalFor window: NSWindow, delegate delegate: Any?, didPresent didPresentSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func presentError(_ error: Error) -> Bool     func willPresentError(_ error: Error) -> Error     func validateProposedFirstResponder(_ responder: NSResponder, for event: NSEvent?) -> Bool     var undoManager: UndoManager? { get }     func insertText(_ insertString: Any)     func doCommand(by selector: Selector)     func moveForward(_ sender: Any?)     func moveRight(_ sender: Any?)     func moveBackward(_ sender: Any?)     func moveLeft(_ sender: Any?)     func moveUp(_ sender: Any?)     func moveDown(_ sender: Any?)     func moveWordForward(_ sender: Any?)     func moveWordBackward(_ sender: Any?)     func moveToBeginningOfLine(_ sender: Any?)     func moveToEndOfLine(_ sender: Any?)     func moveToBeginningOfParagraph(_ sender: Any?)     func moveToEndOfParagraph(_ sender: Any?)     func moveToEndOfDocument(_ sender: Any?)     func moveToBeginningOfDocument(_ sender: Any?)     func pageDown(_ sender: Any?)     func pageUp(_ sender: Any?)     func centerSelectionInVisibleArea(_ sender: Any?)     func moveBackwardAndModifySelection(_ sender: Any?)     func moveForwardAndModifySelection(_ sender: Any?)     func moveWordForwardAndModifySelection(_ sender: Any?)     func moveWordBackwardAndModifySelection(_ sender: Any?)     func moveUpAndModifySelection(_ sender: Any?)     func moveDownAndModifySelection(_ sender: Any?)     func moveToBeginningOfLineAndModifySelection(_ sender: Any?)     func moveToEndOfLineAndModifySelection(_ sender: Any?)     func moveToBeginningOfParagraphAndModifySelection(_ sender: Any?)     func moveToEndOfParagraphAndModifySelection(_ sender: Any?)     func moveToEndOfDocumentAndModifySelection(_ sender: Any?)     func moveToBeginningOfDocumentAndModifySelection(_ sender: Any?)     func pageDownAndModifySelection(_ sender: Any?)     func pageUpAndModifySelection(_ sender: Any?)     func moveParagraphForwardAndModifySelection(_ sender: Any?)     func moveParagraphBackwardAndModifySelection(_ sender: Any?)     func moveWordRight(_ sender: Any?)     func moveWordLeft(_ sender: Any?)     func moveRightAndModifySelection(_ sender: Any?)     func moveLeftAndModifySelection(_ sender: Any?)     func moveWordRightAndModifySelection(_ sender: Any?)     func moveWordLeftAndModifySelection(_ sender: Any?)     func moveToLeftEndOfLine(_ sender: Any?)     func moveToRightEndOfLine(_ sender: Any?)     func moveToLeftEndOfLineAndModifySelection(_ sender: Any?)     func moveToRightEndOfLineAndModifySelection(_ sender: Any?)     func scrollPageUp(_ sender: Any?)     func scrollPageDown(_ sender: Any?)     func scrollLineUp(_ sender: Any?)     func scrollLineDown(_ sender: Any?)     func scrollToBeginningOfDocument(_ sender: Any?)     func scrollToEndOfDocument(_ sender: Any?)     func transpose(_ sender: Any?)     func transposeWords(_ sender: Any?)     func selectAll(_ sender: Any?)     func selectParagraph(_ sender: Any?)     func selectLine(_ sender: Any?)     func selectWord(_ sender: Any?)     func indent(_ sender: Any?)     func insertTab(_ sender: Any?)     func insertBacktab(_ sender: Any?)     func insertNewline(_ sender: Any?)     func insertParagraphSeparator(_ sender: Any?)     func insertNewlineIgnoringFieldEditor(_ sender: Any?)     func insertTabIgnoringFieldEditor(_ sender: Any?)     func insertLineBreak(_ sender: Any?)     func insertContainerBreak(_ sender: Any?)     func insertSingleQuoteIgnoringSubstitution(_ sender: Any?)     func insertDoubleQuoteIgnoringSubstitution(_ sender: Any?)     func changeCaseOfLetter(_ sender: Any?)     func uppercaseWord(_ sender: Any?)     func lowercaseWord(_ sender: Any?)     func capitalizeWord(_ sender: Any?)     func deleteForward(_ sender: Any?)     func deleteBackward(_ sender: Any?)     func deleteBackwardByDecomposingPreviousCharacter(_ sender: Any?)     func deleteWordForward(_ sender: Any?)     func deleteWordBackward(_ sender: Any?)     func deleteToBeginningOfLine(_ sender: Any?)     func deleteToEndOfLine(_ sender: Any?)     func deleteToBeginningOfParagraph(_ sender: Any?)     func deleteToEndOfParagraph(_ sender: Any?)     func yank(_ sender: Any?)     func complete(_ sender: Any?)     func setMark(_ sender: Any?)     func deleteToMark(_ sender: Any?)     func selectToMark(_ sender: Any?)     func swapWithMark(_ sender: Any?)     func cancelOperation(_ sender: Any?)     func makeBaseWritingDirectionNatural(_ sender: Any?)     func makeBaseWritingDirectionLeftToRight(_ sender: Any?)     func makeBaseWritingDirectionRightToLeft(_ sender: Any?)     func makeTextWritingDirectionNatural(_ sender: Any?)     func makeTextWritingDirectionLeftToRight(_ sender: Any?)     func makeTextWritingDirectionRightToLeft(_ sender: Any?)     func quickLookPreviewItems(_ sender: Any?)     func workflowControllerWillRun(_ controller: AMWorkflowController)     func workflowControllerWillStop(_ controller: AMWorkflowController)     func workflowControllerDidRun(_ controller: AMWorkflowController)     func workflowControllerDidStop(_ controller: AMWorkflowController)     func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)     func workflowController(_ controller: AMWorkflowController, didError error: Error)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any?     func discardEditing()     func commitEditing() -> Bool     func commitEditing(withDelegate delegate: Any?, didCommit didCommitSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func commitEditingAndReturnError() throws     func objectDidBeginEditing(_ editor: Any)     func objectDidEndEditing(_ editor: Any)     class func setDefaultPlaceholder(_ placeholder: Any?, forMarker marker: Any?, withBinding binding: String)     class func defaultPlaceholder(forMarker marker: Any?, withBinding binding: String) -> Any?     class func exposeBinding(_ binding: String)     var exposedBindings: [String] { get }     func valueClassForBinding(_ binding: String) -> AnyClass?     func bind(_ binding: String, to observable: Any, withKeyPath keyPath: String, options options: [String : Any]? = nil)     func unbind(_ binding: String)     func infoForBinding(_ binding: String) -> [String : Any]?     func optionDescriptionsForBinding(_ binding: String) -> [NSAttributeDescription]     func validateToolbarItem(_ item: NSToolbarItem) -> Bool     func application(_ sender: NSApplication, delegateHandlesKey key: String) -> Bool     func tableView(_ tableView: NSTableView, writeRows rows: [Any], to pboard: NSPasteboard) -> Bool     func textStorageWillProcessEditing(_ notification: Notification)     func textStorageDidProcessEditing(_ notification: Notification)     func panel(_ sender: Any, isValidFilename filename: String) -> Bool     func panel(_ sender: Any, directoryDidChange path: String)     func panel(_ sender: Any, compareFilename name1: String, with name2: String, caseSensitive caseSensitive: Bool) -> ComparisonResult     func panel(_ sender: Any, shouldShowFilename filename: String) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func changeColor(_ sender: Any?)     func pasteboard(_ sender: NSPasteboard, provideDataForType type: String)     func pasteboardChangedOwner(_ sender: NSPasteboard)     func validateMenuItem(_ menuItem: NSMenuItem) -> Bool     func validModesForFontPanel(_ fontPanel: NSFontPanel) -> Int     func changeFont(_ sender: Any?)     func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool     func controlTextDidBeginEditing(_ obj: Notification)     func controlTextDidEndEditing(_ obj: Notification)     func controlTextDidChange(_ obj: Notification)     func view(_ view: NSView, stringForToolTip tag: NSToolTipTag, point point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String     func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool     func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?     func draggingSourceOperationMask(forLocal flag: Bool) -> NSDragOperation     func draggedImage(_ image: NSImage!, beganAt screenPoint: NSPoint)     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, operation operation: NSDragOperation)     func draggedImage(_ image: NSImage!, movedTo screenPoint: NSPoint)     func ignoreModifierKeysWhileDragging() -> Bool     func draggedImage(_ image: NSImage!, endedAt screenPoint: NSPoint, deposited flag: Bool)     func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: String) -> Bool     func accessibilityAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String) -> Any?     func accessibilityIsAttributeSettable(_ attribute: String) -> Bool     func accessibilitySetValue(_ value: Any?, forAttribute attribute: String)     func accessibilityParameterizedAttributeNames() -> [Any]     func accessibilityAttributeValue(_ attribute: String, forParameter parameter: Any?) -> Any?     func accessibilityActionNames() -> [Any]     func accessibilityActionDescription(_ action: String) -> String?     func accessibilityPerformAction(_ action: String)     func accessibilityIsIgnored() -> Bool     func accessibilityHitTest(_ point: NSPoint) -> Any?     var accessibilityFocusedUIElement: Any? { get }     func accessibilityIndex(ofChild child: Any) -> Int     func accessibilityArrayAttributeCount(_ attribute: String) -> Int     func accessibilityArrayAttributeValues(_ attribute: String, index index: Int, maxCount maxCount: Int) -> [Any]     var accessibilityNotifiesWhenDestroyed: Bool { get }     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension AMWorkflowView : CVarArg { } extension AMWorkflowView : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [AMWorkflowView.isEditable](https://developer.apple.com/documentation/automator/amworkflowview/1419702-iseditable)

|  | Declaration |
| --- | --- |
| From | ``` var editable: Bool ``` |
| To | ``` var isEditable: Bool ``` |

Modified [NSObject.workflowController(_: AMWorkflowController, didError: Error)](https://developer.apple.com/documentation/objectivec/nsobject/1419652-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func workflowController(_ controller: AMWorkflowController, didError error: NSError) ``` |
| To | ``` func workflowController(_ controller: AMWorkflowController, didError error: Error) ``` |

Modified [NSObject.workflowController(_: AMWorkflowController, didRun: AMAction)](https://developer.apple.com/documentation/objectivec/nsobject/1419675-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func workflowController(_ controller: AMWorkflowController, didRunAction action: AMAction) ``` |
| To | ``` func workflowController(_ controller: AMWorkflowController, didRun action: AMAction) ``` |

Modified [NSObject.workflowController(_: AMWorkflowController, willRun: AMAction)](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/1419720-workflowcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func workflowController(_ controller: AMWorkflowController, willRunAction action: AMAction) ``` |
| To | ``` func workflowController(_ controller: AMWorkflowController, willRun action: AMAction) ``` |

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
