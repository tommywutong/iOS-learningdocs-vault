---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/MediaLibrary.html
archived_at: '2026-07-18T02:51:28.815378Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# MediaLibrary Changes for Swift

### MediaLibrary

Modified [MLMediaGroup](https://developer.apple.com/documentation/medialibrary/mlmediagroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MLMediaGroup : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     unowned(unsafe) var parent: MLMediaGroup? { get }     var mediaSourceIdentifier: String { get }     var name: String? { get }     var identifier: String { get }     var typeIdentifier: String { get }     var attributes: [String : AnyObject] { get }     var childGroups: [MLMediaGroup]? { get }     @NSCopying var URL: NSURL? { get }     @NSCopying var modificationDate: NSDate? { get }     @NSCopying var iconImage: NSImage? { get }     var mediaObjects: [MLMediaObject]? { get } } ``` | -- |
| To | ``` class MLMediaGroup : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     unowned(unsafe) var parent: MLMediaGroup? { get }     var mediaSourceIdentifier: String { get }     var name: String? { get }     var identifier: String { get }     var typeIdentifier: String { get }     var attributes: [String : Any] { get }     var childGroups: [MLMediaGroup]? { get }     var url: URL? { get }     var modificationDate: Date? { get }     @NSCopying var iconImage: NSImage? { get }     var mediaObjects: [MLMediaObject]? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MLMediaGroup : CVarArg { } extension MLMediaGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MLMediaGroup.attributes](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419125-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [String : AnyObject] { get } ``` |
| To | ``` var attributes: [String : Any] { get } ``` |

Modified [MLMediaGroup.modificationDate](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419335-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var modificationDate: NSDate? { get } ``` |
| To | ``` var modificationDate: Date? { get } ``` |

Modified [MLMediaGroup.url](https://developer.apple.com/documentation/medialibrary/mlmediagroup/1419079-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified [MLMediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmedialibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MLMediaLibrary : NSObject {     init(options options: [String : AnyObject])     var mediaSources: [String : MLMediaSource]? { get } } ``` | -- |
| To | ``` class MLMediaLibrary : NSObject {     init(options options: [String : Any] = [:])     var mediaSources: [String : MLMediaSource]? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MLMediaLibrary : CVarArg { } extension MLMediaLibrary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MLMediaLibrary.init(options: [String : Any])](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/1418988-init)

|  | Declaration |
| --- | --- |
| From | ``` init(options options: [String : AnyObject]) ``` |
| To | ``` init(options options: [String : Any] = [:]) ``` |

Modified [MLMediaObject](https://developer.apple.com/documentation/medialibrary/mlmediaobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MLMediaObject : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     var identifier: String { get }     var mediaSourceIdentifier: String { get }     var attributes: [String : AnyObject] { get }     var mediaType: MLMediaType { get }     var contentType: String? { get }     var name: String? { get }     @NSCopying var URL: NSURL? { get }     @NSCopying var originalURL: NSURL? { get }     var fileSize: Int { get }     @NSCopying var modificationDate: NSDate? { get }     @NSCopying var thumbnailURL: NSURL? { get }     @NSCopying var artworkImage: NSImage? { get } } ``` | -- |
| To | ``` class MLMediaObject : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     var identifier: String { get }     var mediaSourceIdentifier: String { get }     var attributes: [String : Any] { get }     var mediaType: MLMediaType { get }     var contentType: String? { get }     var name: String? { get }     var url: URL? { get }     var originalURL: URL? { get }     var fileSize: Int { get }     var modificationDate: Date? { get }     var thumbnailURL: URL? { get }     @NSCopying var artworkImage: NSImage? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MLMediaObject : CVarArg { } extension MLMediaObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MLMediaObject.attributes](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416715-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [String : AnyObject] { get } ``` |
| To | ``` var attributes: [String : Any] { get } ``` |

Modified [MLMediaObject.modificationDate](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416705-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var modificationDate: NSDate? { get } ``` |
| To | ``` var modificationDate: Date? { get } ``` |

Modified [MLMediaObject.originalURL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416703-originalurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var originalURL: NSURL? { get } ``` |
| To | ``` var originalURL: URL? { get } ``` |

Modified [MLMediaObject.thumbnailURL](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416708-thumbnailurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var thumbnailURL: NSURL? { get } ``` |
| To | ``` var thumbnailURL: URL? { get } ``` |

Modified [MLMediaObject.url](https://developer.apple.com/documentation/medialibrary/mlmediaobject/1416718-url)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var URL: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified [MLMediaSource](https://developer.apple.com/documentation/medialibrary/mlmediasource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MLMediaSource : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     var mediaSourceIdentifier: String { get }     var attributes: [String : AnyObject] { get }     var rootMediaGroup: MLMediaGroup? { get }     func mediaGroupForIdentifier(_ mediaGroupIdentifier: String) -> MLMediaGroup?     func mediaGroupsForIdentifiers(_ mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup]     func mediaObjectForIdentifier(_ mediaObjectIdentifier: String) -> MLMediaObject?     func mediaObjectsForIdentifiers(_ mediaObjectIdentifiers: [String]) -> [String : MLMediaObject] } ``` | -- |
| To | ``` class MLMediaSource : NSObject {     unowned(unsafe) var mediaLibrary: MLMediaLibrary? { get }     var mediaSourceIdentifier: String { get }     var attributes: [String : Any] { get }     var rootMediaGroup: MLMediaGroup? { get }     func mediaGroup(forIdentifier mediaGroupIdentifier: String) -> MLMediaGroup?     func mediaGroups(forIdentifiers mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup]     func mediaObject(forIdentifier mediaObjectIdentifier: String) -> MLMediaObject?     func mediaObjects(forIdentifiers mediaObjectIdentifiers: [String]) -> [String : MLMediaObject]     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MLMediaSource : CVarArg { } extension MLMediaSource : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MLMediaSource.attributes](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419157-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [String : AnyObject] { get } ``` |
| To | ``` var attributes: [String : Any] { get } ``` |

Modified [MLMediaSource.mediaGroup(forIdentifier: String) -> MLMediaGroup?](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419283-mediagroupforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func mediaGroupForIdentifier(_ mediaGroupIdentifier: String) -> MLMediaGroup? ``` |
| To | ``` func mediaGroup(forIdentifier mediaGroupIdentifier: String) -> MLMediaGroup? ``` |

Modified [MLMediaSource.mediaGroups(forIdentifiers: [String]) -> [String : MLMediaGroup]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419337-mediagroups)

|  | Declaration |
| --- | --- |
| From | ``` func mediaGroupsForIdentifiers(_ mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup] ``` |
| To | ``` func mediaGroups(forIdentifiers mediaGroupIdentifiers: [String]) -> [String : MLMediaGroup] ``` |

Modified [MLMediaSource.mediaObject(forIdentifier: String) -> MLMediaObject?](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419209-mediaobject)

|  | Declaration |
| --- | --- |
| From | ``` func mediaObjectForIdentifier(_ mediaObjectIdentifier: String) -> MLMediaObject? ``` |
| To | ``` func mediaObject(forIdentifier mediaObjectIdentifier: String) -> MLMediaObject? ``` |

Modified [MLMediaSource.mediaObjects(forIdentifiers: [String]) -> [String : MLMediaObject]](https://developer.apple.com/documentation/medialibrary/mlmediasource/1419123-mediaobjects)

|  | Declaration |
| --- | --- |
| From | ``` func mediaObjectsForIdentifiers(_ mediaObjectIdentifiers: [String]) -> [String : MLMediaObject] ``` |
| To | ``` func mediaObjects(forIdentifiers mediaObjectIdentifiers: [String]) -> [String : MLMediaObject] ``` |

Modified [MLMediaSourceType [struct]](https://developer.apple.com/documentation/medialibrary/mlmediasourcetype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MLMediaSourceType : OptionSetType {     init(rawValue rawValue: UInt)     static var Audio: MLMediaSourceType { get }     static var Image: MLMediaSourceType { get }     static var Movie: MLMediaSourceType { get } } ``` | OptionSetType |
| To | ``` struct MLMediaSourceType : OptionSet {     init(rawValue rawValue: UInt)     static var audio: MLMediaSourceType { get }     static var image: MLMediaSourceType { get }     static var movie: MLMediaSourceType { get }     func intersect(_ other: MLMediaSourceType) -> MLMediaSourceType     func exclusiveOr(_ other: MLMediaSourceType) -> MLMediaSourceType     mutating func unionInPlace(_ other: MLMediaSourceType)     mutating func intersectInPlace(_ other: MLMediaSourceType)     mutating func exclusiveOrInPlace(_ other: MLMediaSourceType)     func isSubsetOf(_ other: MLMediaSourceType) -> Bool     func isDisjointWith(_ other: MLMediaSourceType) -> Bool     func isSupersetOf(_ other: MLMediaSourceType) -> Bool     mutating func subtractInPlace(_ other: MLMediaSourceType)     func isStrictSupersetOf(_ other: MLMediaSourceType) -> Bool     func isStrictSubsetOf(_ other: MLMediaSourceType) -> Bool } extension MLMediaSourceType {     func union(_ other: MLMediaSourceType) -> MLMediaSourceType     func intersection(_ other: MLMediaSourceType) -> MLMediaSourceType     func symmetricDifference(_ other: MLMediaSourceType) -> MLMediaSourceType } extension MLMediaSourceType {     func contains(_ member: MLMediaSourceType) -> Bool     mutating func insert(_ newMember: MLMediaSourceType) -> (inserted: Bool, memberAfterInsert: MLMediaSourceType)     mutating func remove(_ member: MLMediaSourceType) -> MLMediaSourceType?     mutating func update(with newMember: MLMediaSourceType) -> MLMediaSourceType? } extension MLMediaSourceType {     convenience init()     mutating func formUnion(_ other: MLMediaSourceType)     mutating func formIntersection(_ other: MLMediaSourceType)     mutating func formSymmetricDifference(_ other: MLMediaSourceType) } extension MLMediaSourceType {     convenience init<S : Sequence where S.Iterator.Element == MLMediaSourceType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MLMediaSourceType...)     mutating func subtract(_ other: MLMediaSourceType)     func isSubset(of other: MLMediaSourceType) -> Bool     func isSuperset(of other: MLMediaSourceType) -> Bool     func isDisjoint(with other: MLMediaSourceType) -> Bool     func subtracting(_ other: MLMediaSourceType) -> MLMediaSourceType     var isEmpty: Bool { get }     func isStrictSuperset(of other: MLMediaSourceType) -> Bool     func isStrictSubset(of other: MLMediaSourceType) -> Bool } ``` | OptionSet |

Modified [MLMediaSourceType.audio](https://developer.apple.com/documentation/medialibrary/mlmediasourcetype/1419251-audio)

|  | Declaration |
| --- | --- |
| From | ``` static var Audio: MLMediaSourceType { get } ``` |
| To | ``` static var audio: MLMediaSourceType { get } ``` |

Modified [MLMediaSourceType.image](https://developer.apple.com/documentation/medialibrary/mlmediasourcetype/mlmediasourcetypeimage)

|  | Declaration |
| --- | --- |
| From | ``` static var Image: MLMediaSourceType { get } ``` |
| To | ``` static var image: MLMediaSourceType { get } ``` |

Modified [MLMediaSourceType.movie](https://developer.apple.com/documentation/medialibrary/mlmediasourcetype/mlmediasourcetypemovie)

|  | Declaration |
| --- | --- |
| From | ``` static var Movie: MLMediaSourceType { get } ``` |
| To | ``` static var movie: MLMediaSourceType { get } ``` |

Modified [MLMediaType [enum]](https://developer.apple.com/documentation/medialibrary/mlmediatype)

|  | Declaration |
| --- | --- |
| From | ``` enum MLMediaType : UInt {     case Audio     case Image     case Movie } ``` |
| To | ``` enum MLMediaType : UInt {     case audio     case image     case movie } ``` |

Modified [MLMediaType.audio](https://developer.apple.com/documentation/medialibrary/mlmediatype/audio)

|  | Declaration |
| --- | --- |
| From | ``` case Audio ``` |
| To | ``` case audio ``` |

Modified [MLMediaType.image](https://developer.apple.com/documentation/medialibrary/mlmediatype/mlmediatypeimage)

|  | Declaration |
| --- | --- |
| From | ``` case Image ``` |
| To | ``` case image ``` |

Modified [MLMediaType.movie](https://developer.apple.com/documentation/medialibrary/mlmediatype/movie)

|  | Declaration |
| --- | --- |
| From | ``` case Movie ``` |
| To | ``` case movie ``` |

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
