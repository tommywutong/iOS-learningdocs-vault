---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ScriptingBridge.html
archived_at: '2026-07-18T02:51:34.911601Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ScriptingBridge Changes for Swift

### ScriptingBridge

Modified [SBApplication](https://developer.apple.com/documentation/scriptingbridge/sbapplication)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SBApplication : SBObject, NSCoding {     init?(bundleIdentifier ident: String)     init?(URL url: NSURL)     init?(processIdentifier pid: pid_t)     class func applicationWithBundleIdentifier(_ ident: String) -> SBApplication?     class func applicationWithURL(_ url: NSURL) -> SBApplication?     class func applicationWithProcessIdentifier(_ pid: pid_t) -> SBApplication?     func classForScriptingClass(_ className: String) -> AnyClass?     var running: Bool { get }     func activate()     var delegate: SBApplicationDelegate?     var launchFlags: LSLaunchFlags     var sendMode: AESendMode     var timeout: Int } ``` | NSCoding |
| To | ``` class SBApplication : SBObject, NSCoding {     init?(bundleIdentifier ident: String)     init?(url url: URL)     init?(processIdentifier pid: pid_t)     class func withBundleIdentifier(_ ident: String) -> SBApplication?     class func withURL(_ url: URL) -> SBApplication?     class func withProcessIdentifier(_ pid: pid_t) -> SBApplication?     func `class`(forScriptingClass className: String) -> Swift.AnyClass?     var isRunning: Bool { get }     func activate()     var delegate: SBApplicationDelegate?     var launchFlags: LSLaunchFlags     var sendMode: AESendMode     var timeout: Int     init(elementCode code: DescType, properties properties: [String : Any]?, data data: Any?)     func property(withCode code: AEKeyword) -> SBObject     func property(with cls: AnyClass, code code: AEKeyword) -> SBObject     func elementArray(withCode code: DescType) -> SBElementArray     func setTo(_ value: Any?)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SBApplication : CVarArg { } extension SBApplication : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [SBApplication.class(forScriptingClass: String) -> Swift.AnyClass?](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423987-classforscriptingclass)

|  | Declaration |
| --- | --- |
| From | ``` func classForScriptingClass(_ className: String) -> AnyClass? ``` |
| To | ``` func `class`(forScriptingClass className: String) -> Swift.AnyClass? ``` |

Modified [SBApplication.init(url: URL)](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423947-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init?(URL url: NSURL) ``` |
| To | ``` init?(url url: URL) ``` |

Modified [SBApplication.isRunning](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423981-isrunning)

|  | Declaration |
| --- | --- |
| From | ``` var running: Bool { get } ``` |
| To | ``` var isRunning: Bool { get } ``` |

Modified [SBApplicationDelegate](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SBApplicationDelegate {     func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError) -> AnyObject } ``` |
| To | ``` protocol SBApplicationDelegate {     func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: Error) -> Any? } ``` |

Modified [SBApplicationDelegate.eventDidFail(_: UnsafePointer<AppleEvent>, withError: Error) -> Any?](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate/1424011-eventdidfail)

|  | Declaration |
| --- | --- |
| From | ``` func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError) -> AnyObject ``` |
| To | ``` func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: Error) -> Any? ``` |

Modified [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SBElementArray : NSMutableArray {     func objectWithName(_ name: String) -> AnyObject     func objectWithID(_ identifier: AnyObject) -> AnyObject     func objectAtLocation(_ location: AnyObject) -> AnyObject     func arrayByApplyingSelector(_ selector: Selector) -> [AnyObject]     func arrayByApplyingSelector(_ aSelector: Selector, withObject argument: AnyObject) -> [AnyObject]     func get() -> [AnyObject]? } ``` | -- |
| To | ``` class SBElementArray : NSMutableArray {     func object(withName name: String) -> Any     func object(withID identifier: Any) -> Any     func object(atLocation location: Any) -> Any     func array(byApplying selector: Selector) -> [Any]     func array(byApplying aSelector: Selector, with argument: Any) -> [Any]     func get() -> [Any]?     func filter(using predicate: NSPredicate)     func sort(using sortDescriptors: [NSSortDescriptor])     class func withCapacity(_ numItems: Int) -> Self     class func withContentsOfFile(_ path: String) -> NSMutableArray?     class func withContentsOf(_ url: URL) -> NSMutableArray?     func addObjects(from otherArray: [Any])     func exchangeObject(at idx1: Int, withObjectAt idx2: Int)     func removeAllObjects()     func remove(_ anObject: Any, in range: NSRange)     func remove(_ anObject: Any)     func removeObject(identicalTo anObject: Any, in range: NSRange)     func removeObject(identicalTo anObject: Any)     func removeObjects(fromIndices indices: UnsafeMutablePointer<Int>, numIndices cnt: Int)     func removeObjects(in otherArray: [Any])     func removeObjects(in range: NSRange)     func replaceObjects(in range: NSRange, withObjectsFrom otherArray: [Any], range otherRange: NSRange)     func replaceObjects(in range: NSRange, withObjectsFrom otherArray: [Any])     func setArray(_ otherArray: [Any])     func sort(_ compare: @convention(c) (Any, Any, UnsafeMutableRawPointer?) -> Int, context context: UnsafeMutableRawPointer?)     func sort(using comparator: Selector)     func insert(_ objects: [Any], at indexes: IndexSet)     func removeObjects(at indexes: IndexSet)     func replaceObjects(at indexes: IndexSet, with objects: [Any])     subscript(_ idx: Int) -> Any     func setObject(_ obj: Any, atIndexedSubscript idx: Int)     func sort(comparator cmptr: (Any, Any) -> ComparisonResult)     func sort(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult)     convenience init(objects elements: Any...)     @nonobjc convenience init(array anArray: NSArray)     func filtered(using predicate: NSPredicate) -> [Any]     func sortedArray(using sortDescriptors: [NSSortDescriptor]) -> [Any]     func addObserver(_ observer: NSObject, toObjectsAt indexes: IndexSet, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, fromObjectsAt indexes: IndexSet, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, fromObjectsAt indexes: IndexSet, forKeyPath keyPath: String)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func value(forKey key: String) -> Any     func setValue(_ value: Any?, forKey key: String)     func pathsMatchingExtensions(_ filterTypes: [String]) -> [String]     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject>!)     class func array() -> Self     convenience init(object anObject: Any)     class func withObject(_ anObject: Any) -> Self     class func withObjects(_ objects: UnsafePointer<AnyObject>!, count cnt: Int) -> Self     convenience init(array array: [Any])     class func withArray(_ array: [Any]) -> Self     convenience init(array array: [Any])     convenience init(array array: [Any], copyItems flag: Bool)      init?(contentsOfFile path: String)     class func withContentsOfFile(_ path: String) -> [Any]?      init?(contentsOf url: URL)     class func withContentsOf(_ url: URL) -> [Any]?     convenience init?(contentsOfFile path: String)     convenience init?(contentsOf url: URL)     func adding(_ anObject: Any) -> [Any]     func addingObjects(from otherArray: [Any]) -> [Any]     func componentsJoined(by separator: String) -> String     func contains(_ anObject: Any) -> Bool     var description: String { get }     func description(withLocale locale: Any?) -> String     func description(withLocale locale: Any?, indent level: Int) -> String     func firstObjectCommon(with otherArray: [Any]) -> Any?     func getObjects(_ objects: AutoreleasingUnsafeMutablePointer<AnyObject>!, range range: NSRange)     func index(of anObject: Any) -> Int     func index(of anObject: Any, in range: NSRange) -> Int     func indexOfObjectIdentical(to anObject: Any) -> Int     func indexOfObjectIdentical(to anObject: Any, in range: NSRange) -> Int     func isEqual(to otherArray: [Any]) -> Bool     var firstObject: Any? { get }     var lastObject: Any? { get }     func objectEnumerator() -> NSEnumerator     func reverseObjectEnumerator() -> NSEnumerator     var sortedArrayHint: Data { get }     func sortedArray(_ comparator: @convention(c) (Any, Any, UnsafeMutableRawPointer?) -> Int, context context: UnsafeMutableRawPointer?) -> [Any]     func sortedArray(_ comparator: @convention(c) (Any, Any, UnsafeMutableRawPointer?) -> Int, context context: UnsafeMutableRawPointer?, hint hint: Data?) -> [Any]     func sortedArray(using comparator: Selector) -> [Any]     func subarray(with range: NSRange) -> [Any]     func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool     func write(to url: URL, atomically atomically: Bool) -> Bool     func makeObjectsPerform(_ aSelector: Selector)     func makeObjectsPerform(_ aSelector: Selector, with argument: Any?)     func objects(at indexes: IndexSet) -> [Any]     subscript(_ idx: Int) -> Any { get }     func objectAtIndexedSubscript(_ idx: Int) -> Any     func enumerateObjects(_ block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjects(options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateObjects(at s: IndexSet, options opts: NSEnumerationOptions = [], using block: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)     func indexOfObject(passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObject(options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexOfObject(at s: IndexSet, options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int     func indexesOfObjects(passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet     func indexesOfObjects(options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet     func indexesOfObjects(at s: IndexSet, options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet     func sortedArray(comparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]     func sortedArray(options opts: NSSortOptions = [], usingComparator cmptr: (Any, Any) -> ComparisonResult) -> [Any]     func index(of obj: Any, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions = [], usingComparator cmp: (Any, Any) -> ComparisonResult) -> Int     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SBElementArray : ExpressibleByArrayLiteral {     required convenience init(arrayLiteral elements: Any...) } extension SBElementArray : Sequence {     final func makeIterator() -> NSFastEnumerationIterator } extension SBElementArray : CustomReflectable {     var customMirror: Mirror { get } } extension SBElementArray : CVarArg { } extension SBElementArray : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, CustomReflectable, Equatable, ExpressibleByArrayLiteral, Hashable, Sequence |

Modified [SBElementArray.array(byApplying: Selector) -> [Any]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423951-arraybyapplyingselector)

|  | Declaration |
| --- | --- |
| From | ``` func arrayByApplyingSelector(_ selector: Selector) -> [AnyObject] ``` |
| To | ``` func array(byApplying selector: Selector) -> [Any] ``` |

Modified [SBElementArray.array(byApplying: Selector, with: Any) -> [Any]](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1424007-arraybyapplyingselector)

|  | Declaration |
| --- | --- |
| From | ``` func arrayByApplyingSelector(_ aSelector: Selector, withObject argument: AnyObject) -> [AnyObject] ``` |
| To | ``` func array(byApplying aSelector: Selector, with argument: Any) -> [Any] ``` |

Modified [SBElementArray.get() -> [Any]?](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423997-get)

|  | Declaration |
| --- | --- |
| From | ``` func get() -> [AnyObject]? ``` |
| To | ``` func get() -> [Any]? ``` |

Modified [SBElementArray.object(atLocation: Any) -> Any](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423963-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectAtLocation(_ location: AnyObject) -> AnyObject ``` |
| To | ``` func object(atLocation location: Any) -> Any ``` |

Modified [SBElementArray.object(withID: Any) -> Any](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423985-objectwithid)

|  | Declaration |
| --- | --- |
| From | ``` func objectWithID(_ identifier: AnyObject) -> AnyObject ``` |
| To | ``` func object(withID identifier: Any) -> Any ``` |

Modified [SBElementArray.object(withName: String) -> Any](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423971-objectwithname)

|  | Declaration |
| --- | --- |
| From | ``` func objectWithName(_ name: String) -> AnyObject ``` |
| To | ``` func object(withName name: String) -> Any ``` |

Modified [SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SBObject : NSObject, NSCoding {     init()     init(properties properties: [NSObject : AnyObject])     init(data data: AnyObject)     func get() -> AnyObject?     func lastError() -> NSError? } extension SBObject {     init(elementCode code: DescType, properties properties: [String : AnyObject]?, data data: AnyObject?)     func propertyWithCode(_ code: AEKeyword) -> SBObject     func propertyWithClass(_ cls: AnyClass, code code: AEKeyword) -> SBObject     func elementArrayWithCode(_ code: DescType) -> SBElementArray     func setTo(_ value: AnyObject?) } ``` | NSCoding |
| To | ``` class SBObject : NSObject, NSCoding {     init()     init(properties properties: [AnyHashable : Any])     init(data data: Any)     func get() -> Any?     func lastError() -> Error?     init(elementCode code: DescType, properties properties: [String : Any]?, data data: Any?)     func property(withCode code: AEKeyword) -> SBObject     func property(with cls: Swift.AnyClass, code code: AEKeyword) -> SBObject     func elementArray(withCode code: DescType) -> SBElementArray     func setTo(_ value: Any?)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SBObject : CVarArg { } extension SBObject : Equatable, Hashable {     var hashValue: Int { get } } extension SBObject {     init(elementCode code: DescType, properties properties: [String : Any]?, data data: Any?)     func property(withCode code: AEKeyword) -> SBObject     func property(with cls: Swift.AnyClass, code code: AEKeyword) -> SBObject     func elementArray(withCode code: DescType) -> SBElementArray     func setTo(_ value: Any?) } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [SBObject.elementArray(withCode: DescType) -> SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423995-elementarray)

|  | Declaration |
| --- | --- |
| From | ``` func elementArrayWithCode(_ code: DescType) -> SBElementArray ``` |
| To | ``` func elementArray(withCode code: DescType) -> SBElementArray ``` |

Modified [SBObject.get() -> Any?](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get)

|  | Declaration |
| --- | --- |
| From | ``` func get() -> AnyObject? ``` |
| To | ``` func get() -> Any? ``` |

Modified [SBObject.init(data: Any)](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423961-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: AnyObject) ``` |
| To | ``` init(data data: Any) ``` |

Modified [SBObject.init(elementCode: DescType, properties: [String : Any]?, data: Any?)](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423999-init)

|  | Declaration |
| --- | --- |
| From | ``` init(elementCode code: DescType, properties properties: [String : AnyObject]?, data data: AnyObject?) ``` |
| To | ``` init(elementCode code: DescType, properties properties: [String : Any]?, data data: Any?) ``` |

Modified [SBObject.init(properties: [AnyHashable : Any])](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423973-init)

|  | Declaration |
| --- | --- |
| From | ``` init(properties properties: [NSObject : AnyObject]) ``` |
| To | ``` init(properties properties: [AnyHashable : Any]) ``` |

Modified [SBObject.lastError() -> Error?](https://developer.apple.com/documentation/scriptingbridge/sbobject/1424005-lasterror)

|  | Declaration |
| --- | --- |
| From | ``` func lastError() -> NSError? ``` |
| To | ``` func lastError() -> Error? ``` |

Modified [SBObject.property(with: Swift.AnyClass, code: AEKeyword) -> SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423977-propertywithclass)

|  | Declaration |
| --- | --- |
| From | ``` func propertyWithClass(_ cls: AnyClass, code code: AEKeyword) -> SBObject ``` |
| To | ``` func property(with cls: Swift.AnyClass, code code: AEKeyword) -> SBObject ``` |

Modified [SBObject.property(withCode: AEKeyword) -> SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423975-propertywithcode)

|  | Declaration |
| --- | --- |
| From | ``` func propertyWithCode(_ code: AEKeyword) -> SBObject ``` |
| To | ``` func property(withCode code: AEKeyword) -> SBObject ``` |

Modified [SBObject.setTo(_: Any?)](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423967-setto)

|  | Declaration |
| --- | --- |
| From | ``` func setTo(_ value: AnyObject?) ``` |
| To | ``` func setTo(_ value: Any?) ``` |

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
