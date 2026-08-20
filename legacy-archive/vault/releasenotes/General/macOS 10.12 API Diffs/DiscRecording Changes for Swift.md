---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/DiscRecording.html
archived_at: '2026-07-18T02:51:16.183145Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# DiscRecording Changes for Swift

### DiscRecording

Removed DRCDTextBlock.cdTextBlockWithLanguage(_: String!, encoding: UInt) -> DRCDTextBlock! [class]Removed DRFileProductionInfo.init(requestedAddress: UInt64, buffer: UnsafeMutablePointer<Void>, reqCount: UInt32, actCount: UInt32, blockSize: UInt32, fork: DRFileForkIndex)Removed DRMSF.msf() -> DRMSF! [class]Removed DRMSF.msfWithFrames(_: UInt32) -> DRMSF! [class]Removed DRMSF.msfWithString(_: String!) -> DRMSF! [class]Removed DRRefConCallbacks.init(version: UInt, retain: DRRefConRetainCallback!, release: DRRefConReleaseCallback!)Removed DRTrackProductionInfo.init(buffer: UnsafeMutablePointer<Void>, reqCount: UInt32, actCount: UInt32, flags: UInt32, blockSize: UInt32, requestedAddress: UInt64)Added DRFileProductionInfo.init(requestedAddress: UInt64, buffer: UnsafeMutableRawPointer!, reqCount: UInt32, actCount: UInt32, blockSize: UInt32, fork: DRFileForkIndex)Added DRRefConCallbacks.init(version: UInt, retain: DiscRecording.DRRefConRetainCallback!, release: DiscRecording.DRRefConReleaseCallback!)Added DRTrackProductionInfo.init(buffer: UnsafeMutableRawPointer!, reqCount: UInt32, actCount: UInt32, flags: UInt32, blockSize: UInt32, requestedAddress: UInt64)Modified DRBurn

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRBurn : NSObject {      init!(forDevice device: DRDevice!)     class func burnForDevice(_ device: DRDevice!) -> DRBurn!     init!(device device: DRDevice!)     func writeLayout(_ layout: AnyObject!)     func status() -> [NSObject : AnyObject]!     func abort()     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func device() -> DRDevice! } extension DRBurn {     func requestedBurnSpeed() -> Float     func setRequestedBurnSpeed(_ speed: Float)     func appendable() -> Bool     func setAppendable(_ appendable: Bool)     func verifyDisc() -> Bool     func setVerifyDisc(_ verify: Bool)     func completionAction() -> String!     func setCompletionAction(_ action: String!) } extension DRBurn {     class func layoutForImageFile(_ path: String!) -> AnyObject! } ``` | -- |
| To | ``` class DRBurn : NSObject {      init!(for device: DRDevice!)     class func forDevice(_ device: DRDevice!) -> DRBurn!     init!(device device: DRDevice!)     func writeLayout(_ layout: Any!)     func status() -> [AnyHashable : Any]!     func abort()     func properties() -> [AnyHashable : Any]!     func setProperties(_ properties: [AnyHashable : Any]!)     func device() -> DRDevice!     class func layout(forImageFile path: String!) -> Any!     func requestedBurnSpeed() -> Float     func setRequestedBurnSpeed(_ speed: Float)     func appendable() -> Bool     func setAppendable(_ appendable: Bool)     func verifyDisc() -> Bool     func setVerifyDisc(_ verify: Bool)     func completionAction() -> String!     func setCompletionAction(_ action: String!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRBurn : CVarArg { } extension DRBurn : Equatable, Hashable {     var hashValue: Int { get } } extension DRBurn {     func requestedBurnSpeed() -> Float     func setRequestedBurnSpeed(_ speed: Float)     func appendable() -> Bool     func setAppendable(_ appendable: Bool)     func verifyDisc() -> Bool     func setVerifyDisc(_ verify: Bool)     func completionAction() -> String!     func setCompletionAction(_ action: String!) } extension DRBurn {     class func layout(forImageFile path: String!) -> Any! } ``` | CVarArg, Equatable, Hashable |

Modified DRBurn.init(for: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forDevice device: DRDevice!) ``` |
| To | ``` init!(for device: DRDevice!) ``` |

Modified DRBurn.layout(forImageFile: String!) -> Any! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func layoutForImageFile(_ path: String!) -> AnyObject! ``` |
| To | ``` class func layout(forImageFile path: String!) -> Any! ``` |

Modified DRBurn.properties() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func properties() -> [NSObject : AnyObject]! ``` |
| To | ``` func properties() -> [AnyHashable : Any]! ``` |

Modified DRBurn.setProperties(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func setProperties(_ properties: [NSObject : AnyObject]!) ``` |
| To | ``` func setProperties(_ properties: [AnyHashable : Any]!) ``` |

Modified DRBurn.status() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func status() -> [NSObject : AnyObject]! ``` |
| To | ``` func status() -> [AnyHashable : Any]! ``` |

Modified DRBurn.writeLayout(_: Any!)

|  | Declaration |
| --- | --- |
| From | ``` func writeLayout(_ layout: AnyObject!) ``` |
| To | ``` func writeLayout(_ layout: Any!) ``` |

Modified DRCDTextBlock

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRCDTextBlock : NSObject {     class func arrayOfCDTextBlocksFromPacks(_ packs: NSData!) -> [AnyObject]!     class func cdTextBlockWithLanguage(_ lang: String!, encoding enc: UInt) -> DRCDTextBlock!     init!(language lang: String!, encoding enc: UInt)     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func trackDictionaries() -> [AnyObject]!     func setTrackDictionaries(_ tracks: [AnyObject]!)     func objectForKey(_ key: String!, ofTrack trackIndex: Int) -> AnyObject!     func setObject(_ value: AnyObject!, forKey key: String!, ofTrack trackIndex: Int)     func flatten() -> Int } extension DRCDTextBlock {     func language() -> String!     func encoding() -> UInt } ``` | -- |
| To | ``` class DRCDTextBlock : NSObject {     class func arrayOfCDTextBlocks(fromPacks packs: Data!) -> [Any]!      init!(language lang: String!, encoding enc: UInt)     class func withLanguage(_ lang: String!, encoding enc: UInt) -> DRCDTextBlock!     init!(language lang: String!, encoding enc: UInt)     func properties() -> [AnyHashable : Any]!     func setProperties(_ properties: [AnyHashable : Any]!)     func trackDictionaries() -> [Any]!     func setTrackDictionaries(_ tracks: [Any]!)     func object(forKey key: String!, ofTrack trackIndex: Int) -> Any!     func setObject(_ value: Any!, forKey key: String!, ofTrack trackIndex: Int)     func flatten() -> Int     func language() -> String!     func encoding() -> UInt     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRCDTextBlock : CVarArg { } extension DRCDTextBlock : Equatable, Hashable {     var hashValue: Int { get } } extension DRCDTextBlock {     func language() -> String!     func encoding() -> UInt } ``` | CVarArg, Equatable, Hashable |

Modified DRCDTextBlock.arrayOfCDTextBlocks(fromPacks: Data!) -> [Any]! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func arrayOfCDTextBlocksFromPacks(_ packs: NSData!) -> [AnyObject]! ``` |
| To | ``` class func arrayOfCDTextBlocks(fromPacks packs: Data!) -> [Any]! ``` |

Modified DRCDTextBlock.object(forKey: String!, ofTrack: Int) -> Any!

|  | Declaration |
| --- | --- |
| From | ``` func objectForKey(_ key: String!, ofTrack trackIndex: Int) -> AnyObject! ``` |
| To | ``` func object(forKey key: String!, ofTrack trackIndex: Int) -> Any! ``` |

Modified DRCDTextBlock.properties() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func properties() -> [NSObject : AnyObject]! ``` |
| To | ``` func properties() -> [AnyHashable : Any]! ``` |

Modified DRCDTextBlock.setObject(_: Any!, forKey: String!, ofTrack: Int)

|  | Declaration |
| --- | --- |
| From | ``` func setObject(_ value: AnyObject!, forKey key: String!, ofTrack trackIndex: Int) ``` |
| To | ``` func setObject(_ value: Any!, forKey key: String!, ofTrack trackIndex: Int) ``` |

Modified DRCDTextBlock.setProperties(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func setProperties(_ properties: [NSObject : AnyObject]!) ``` |
| To | ``` func setProperties(_ properties: [AnyHashable : Any]!) ``` |

Modified DRCDTextBlock.setTrackDictionaries(_: [Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func setTrackDictionaries(_ tracks: [AnyObject]!) ``` |
| To | ``` func setTrackDictionaries(_ tracks: [Any]!) ``` |

Modified DRCDTextBlock.trackDictionaries() -> [Any]!

|  | Declaration |
| --- | --- |
| From | ``` func trackDictionaries() -> [AnyObject]! ``` |
| To | ``` func trackDictionaries() -> [Any]! ``` |

Modified DRDevice

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRDevice : NSObject {     class func devices() -> [AnyObject]!      init!(forBSDName bsdName: String!)     class func deviceForBSDName(_ bsdName: String!) -> DRDevice!      init!(forIORegistryEntryPath path: String!)     class func deviceForIORegistryEntryPath(_ path: String!) -> DRDevice!     func isValid() -> Bool     func info() -> [NSObject : AnyObject]!     func status() -> [NSObject : AnyObject]!     func openTray() -> Bool     func closeTray() -> Bool     func ejectMedia() -> Bool     func acquireExclusiveAccess() -> Bool     func releaseExclusiveAccess()     func acquireMediaReservation()     func releaseMediaReservation()     func isEqualToDevice(_ otherDevice: DRDevice!) -> Bool } extension DRDevice {     func writesCD() -> Bool     func writesDVD() -> Bool     func displayName() -> String!     func ioRegistryEntryPath() -> String! } extension DRDevice {     func mediaIsPresent() -> Bool     func mediaIsTransitioning() -> Bool     func mediaIsBusy() -> Bool     func mediaType() -> String!     func mediaIsBlank() -> Bool     func mediaIsAppendable() -> Bool     func mediaIsOverwritable() -> Bool     func mediaIsErasable() -> Bool     func mediaIsReserved() -> Bool     func mediaSpaceOverwritable() -> DRMSF!     func mediaSpaceUsed() -> DRMSF!     func mediaSpaceFree() -> DRMSF!     func trayIsOpen() -> Bool     func bsdName() -> String! } ``` | -- |
| To | ``` class DRDevice : NSObject {     class func devices() -> [Any]!      init!(forBSDName bsdName: String!)     class func forBSDName(_ bsdName: String!) -> DRDevice!      init!(forIORegistryEntryPath path: String!)     class func forIORegistryEntryPath(_ path: String!) -> DRDevice!     func isValid() -> Bool     func info() -> [AnyHashable : Any]!     func status() -> [AnyHashable : Any]!     func openTray() -> Bool     func closeTray() -> Bool     func ejectMedia() -> Bool     func acquireExclusiveAccess() -> Bool     func releaseExclusiveAccess()     func acquireMediaReservation()     func releaseMediaReservation()     func isEqual(to otherDevice: DRDevice!) -> Bool     func mediaIsPresent() -> Bool     func mediaIsTransitioning() -> Bool     func mediaIsBusy() -> Bool     func mediaType() -> String!     func mediaIsBlank() -> Bool     func mediaIsAppendable() -> Bool     func mediaIsOverwritable() -> Bool     func mediaIsErasable() -> Bool     func mediaIsReserved() -> Bool     func mediaSpaceOverwritable() -> DRMSF!     func mediaSpaceUsed() -> DRMSF!     func mediaSpaceFree() -> DRMSF!     func trayIsOpen() -> Bool     func bsdName() -> String!     func writesCD() -> Bool     func writesDVD() -> Bool     func displayName() -> String!     func ioRegistryEntryPath() -> String!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRDevice : CVarArg { } extension DRDevice : Equatable, Hashable {     var hashValue: Int { get } } extension DRDevice {     func writesCD() -> Bool     func writesDVD() -> Bool     func displayName() -> String!     func ioRegistryEntryPath() -> String! } extension DRDevice {     func mediaIsPresent() -> Bool     func mediaIsTransitioning() -> Bool     func mediaIsBusy() -> Bool     func mediaType() -> String!     func mediaIsBlank() -> Bool     func mediaIsAppendable() -> Bool     func mediaIsOverwritable() -> Bool     func mediaIsErasable() -> Bool     func mediaIsReserved() -> Bool     func mediaSpaceOverwritable() -> DRMSF!     func mediaSpaceUsed() -> DRMSF!     func mediaSpaceFree() -> DRMSF!     func trayIsOpen() -> Bool     func bsdName() -> String! } ``` | CVarArg, Equatable, Hashable |

Modified DRDevice.devices() -> [Any]! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func devices() -> [AnyObject]! ``` |
| To | ``` class func devices() -> [Any]! ``` |

Modified DRDevice.info() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func info() -> [NSObject : AnyObject]! ``` |
| To | ``` func info() -> [AnyHashable : Any]! ``` |

Modified DRDevice.isEqual(to: DRDevice!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToDevice(_ otherDevice: DRDevice!) -> Bool ``` |
| To | ``` func isEqual(to otherDevice: DRDevice!) -> Bool ``` |

Modified DRDevice.status() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func status() -> [NSObject : AnyObject]! ``` |
| To | ``` func status() -> [AnyHashable : Any]! ``` |

Modified DRErase

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRErase : NSObject {      init!(forDevice device: DRDevice!)     class func eraseForDevice(_ device: DRDevice!) -> DRErase!     init!(device device: DRDevice!)     func start()     func status() -> [NSObject : AnyObject]!     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func device() -> DRDevice! } extension DRErase {     func eraseType() -> String!     func setEraseType(_ type: String!) } ``` | -- |
| To | ``` class DRErase : NSObject {      init!(for device: DRDevice!)     class func forDevice(_ device: DRDevice!) -> DRErase!     init!(device device: DRDevice!)     func start()     func status() -> [AnyHashable : Any]!     func properties() -> [AnyHashable : Any]!     func setProperties(_ properties: [AnyHashable : Any]!)     func device() -> DRDevice!     func eraseType() -> String!     func setEraseType(_ type: String!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRErase : CVarArg { } extension DRErase : Equatable, Hashable {     var hashValue: Int { get } } extension DRErase {     func eraseType() -> String!     func setEraseType(_ type: String!) } ``` | CVarArg, Equatable, Hashable |

Modified DRErase.init(for: DRDevice!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forDevice device: DRDevice!) ``` |
| To | ``` init!(for device: DRDevice!) ``` |

Modified DRErase.properties() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func properties() -> [NSObject : AnyObject]! ``` |
| To | ``` func properties() -> [AnyHashable : Any]! ``` |

Modified DRErase.setProperties(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func setProperties(_ properties: [NSObject : AnyObject]!) ``` |
| To | ``` func setProperties(_ properties: [AnyHashable : Any]!) ``` |

Modified DRErase.status() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func status() -> [NSObject : AnyObject]! ``` |
| To | ``` func status() -> [AnyHashable : Any]! ``` |

Modified DRFile

|  | Declaration |
| --- | --- |
| From | ``` class DRFile : DRFSObject {      init!(path path: String!)     class func fileWithPath(_ path: String!) -> DRFile!     init!(path path: String!) } extension DRFile {     class func virtualFileWithName(_ name: String!, data data: NSData!) -> DRFile!     class func virtualFileWithName(_ name: String!, dataProducer producer: AnyObject!) -> DRFile!     init!(name name: String!, data data: NSData!)     init!(name name: String!, dataProducer producer: AnyObject!) } extension DRFile {     class func hardLinkPointingTo(_ original: DRFile!, inFilesystem filesystem: String!) -> DRFile!     class func symLinkPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     class func finderAliasPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     init!(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!) } ``` |
| To | ``` class DRFile : DRFSObject {      init!(path path: String!)     class func withPath(_ path: String!) -> DRFile!     init!(path path: String!)     class func hardLinkPointing(to original: DRFile!, inFilesystem filesystem: String!) -> DRFile!     class func symLinkPointing(to original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     class func finderAliasPointing(to original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     init!(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!)     class func virtualFile(withName name: String!, data data: Data!) -> DRFile!     class func virtualFile(withName name: String!, dataProducer producer: Any!) -> DRFile!     init!(name name: String!, data data: Data!)     init!(name name: String!, dataProducer producer: Any!) } extension DRFile {     class func virtualFile(withName name: String!, data data: Data!) -> DRFile!     class func virtualFile(withName name: String!, dataProducer producer: Any!) -> DRFile!     init!(name name: String!, data data: Data!)     init!(name name: String!, dataProducer producer: Any!) } extension DRFile {     class func hardLinkPointing(to original: DRFile!, inFilesystem filesystem: String!) -> DRFile!     class func symLinkPointing(to original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     class func finderAliasPointing(to original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile!     init!(linkType linkType: String!, pointingTo original: DRFSObject!, inFilesystem filesystem: String!) } ``` |

Modified DRFile.finderAliasPointing(to: DRFSObject!, inFilesystem: String!) -> DRFile! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func finderAliasPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile! ``` |
| To | ``` class func finderAliasPointing(to original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile! ``` |

Modified DRFile.hardLinkPointing(to: DRFile!, inFilesystem: String!) -> DRFile! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func hardLinkPointingTo(_ original: DRFile!, inFilesystem filesystem: String!) -> DRFile! ``` |
| To | ``` class func hardLinkPointing(to original: DRFile!, inFilesystem filesystem: String!) -> DRFile! ``` |

Modified DRFile.init(name: String!, data: Data!)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, data data: NSData!) ``` |
| To | ``` init!(name name: String!, data data: Data!) ``` |

Modified DRFile.init(name: String!, dataProducer: Any!)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, dataProducer producer: AnyObject!) ``` |
| To | ``` init!(name name: String!, dataProducer producer: Any!) ``` |

Modified DRFile.symLinkPointing(to: DRFSObject!, inFilesystem: String!) -> DRFile! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func symLinkPointingTo(_ original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile! ``` |
| To | ``` class func symLinkPointing(to original: DRFSObject!, inFilesystem filesystem: String!) -> DRFile! ``` |

Modified DRFile.virtualFile(withName: String!, data: Data!) -> DRFile! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func virtualFileWithName(_ name: String!, data data: NSData!) -> DRFile! ``` |
| To | ``` class func virtualFile(withName name: String!, data data: Data!) -> DRFile! ``` |

Modified DRFile.virtualFile(withName: String!, dataProducer: Any!) -> DRFile! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func virtualFileWithName(_ name: String!, dataProducer producer: AnyObject!) -> DRFile! ``` |
| To | ``` class func virtualFile(withName name: String!, dataProducer producer: Any!) -> DRFile! ``` |

Modified DRFileDataProduction

|  | Declaration |
| --- | --- |
| From | ``` protocol DRFileDataProduction {     func calculateSizeOfFile(_ file: DRFile!, fork fork: DRFileFork, estimating estimate: Bool) -> UInt64     func prepareFileForBurn(_ file: DRFile!) -> Bool     func produceFile(_ file: DRFile!, fork fork: DRFileFork, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32) -> UInt32     func prepareFileForVerification(_ file: DRFile!) -> Bool     func cleanupFileAfterBurn(_ file: DRFile!) } ``` |
| To | ``` protocol DRFileDataProduction {     func calculateSize(of file: DRFile!, fork fork: DRFileFork, estimating estimate: Bool) -> UInt64     func prepareFile(forBurn file: DRFile!) -> Bool     func produce(_ file: DRFile!, fork fork: DRFileFork, intoBuffer buffer: UnsafeMutablePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32) -> UInt32     func prepareFile(forVerification file: DRFile!) -> Bool     func cleanupFile(afterBurn file: DRFile!) } ``` |

Modified DRFileDataProduction.calculateSize(of: DRFile!, fork: DRFileFork, estimating: Bool) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func calculateSizeOfFile(_ file: DRFile!, fork fork: DRFileFork, estimating estimate: Bool) -> UInt64 ``` |
| To | ``` func calculateSize(of file: DRFile!, fork fork: DRFileFork, estimating estimate: Bool) -> UInt64 ``` |

Modified DRFileDataProduction.cleanupFile(afterBurn: DRFile!)

|  | Declaration |
| --- | --- |
| From | ``` func cleanupFileAfterBurn(_ file: DRFile!) ``` |
| To | ``` func cleanupFile(afterBurn file: DRFile!) ``` |

Modified DRFileDataProduction.prepareFile(forBurn: DRFile!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func prepareFileForBurn(_ file: DRFile!) -> Bool ``` |
| To | ``` func prepareFile(forBurn file: DRFile!) -> Bool ``` |

Modified DRFileDataProduction.prepareFile(forVerification: DRFile!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func prepareFileForVerification(_ file: DRFile!) -> Bool ``` |
| To | ``` func prepareFile(forVerification file: DRFile!) -> Bool ``` |

Modified DRFileDataProduction.produce(_: DRFile!, fork: DRFileFork, intoBuffer: UnsafeMutablePointer<Int8>!, length: UInt32, atAddress: UInt64, blockSize: UInt32) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func produceFile(_ file: DRFile!, fork fork: DRFileFork, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32) -> UInt32 ``` |
| To | ``` func produce(_ file: DRFile!, fork fork: DRFileFork, intoBuffer buffer: UnsafeMutablePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32) -> UInt32 ``` |

Modified DRFileProductionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRFileProductionInfo {     var requestedAddress: UInt64     var buffer: UnsafeMutablePointer<Void>     var reqCount: UInt32     var actCount: UInt32     var blockSize: UInt32     var fork: DRFileForkIndex     init()     init(requestedAddress requestedAddress: UInt64, buffer buffer: UnsafeMutablePointer<Void>, reqCount reqCount: UInt32, actCount actCount: UInt32, blockSize blockSize: UInt32, fork fork: DRFileForkIndex) } ``` |
| To | ``` struct DRFileProductionInfo {     var requestedAddress: UInt64     var buffer: UnsafeMutableRawPointer!     var reqCount: UInt32     var actCount: UInt32     var blockSize: UInt32     var fork: DRFileForkIndex     init()     init(requestedAddress requestedAddress: UInt64, buffer buffer: UnsafeMutableRawPointer!, reqCount reqCount: UInt32, actCount actCount: UInt32, blockSize blockSize: UInt32, fork fork: DRFileForkIndex) } ``` |

Modified DRFileProductionInfo.buffer

|  | Declaration |
| --- | --- |
| From | ``` var buffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var buffer: UnsafeMutableRawPointer! ``` |

Modified DRFolder

|  | Declaration |
| --- | --- |
| From | ``` class DRFolder : DRFSObject {      init!(path path: String!)     class func folderWithPath(_ path: String!) -> DRFolder!     init!(path path: String!) } extension DRFolder {     class func virtualFolderWithName(_ name: String!) -> DRFolder!     init!(name name: String!)     func makeVirtual()     func addChild(_ child: DRFSObject!)     func removeChild(_ child: DRFSObject!)     func count() -> Int     func children() -> [AnyObject]! } ``` |
| To | ``` class DRFolder : DRFSObject {      init!(path path: String!)     class func withPath(_ path: String!) -> DRFolder!     init!(path path: String!)     class func virtualFolder(withName name: String!) -> DRFolder!     init!(name name: String!)     func makeVirtual()     func addChild(_ child: DRFSObject!)     func removeChild(_ child: DRFSObject!)     func count() -> Int     func children() -> [Any]! } extension DRFolder {     class func virtualFolder(withName name: String!) -> DRFolder!     init!(name name: String!)     func makeVirtual()     func addChild(_ child: DRFSObject!)     func removeChild(_ child: DRFSObject!)     func count() -> Int     func children() -> [Any]! } ``` |

Modified DRFolder.children() -> [Any]!

|  | Declaration |
| --- | --- |
| From | ``` func children() -> [AnyObject]! ``` |
| To | ``` func children() -> [Any]! ``` |

Modified DRFolder.virtualFolder(withName: String!) -> DRFolder! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func virtualFolderWithName(_ name: String!) -> DRFolder! ``` |
| To | ``` class func virtualFolder(withName name: String!) -> DRFolder! ``` |

Modified DRFSObject

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRFSObject : NSObject {     func isVirtual() -> Bool     func sourcePath() -> String!     func parent() -> DRFolder!     func baseName() -> String!     func setBaseName(_ baseName: String!)     func specificNameForFilesystem(_ filesystem: String!) -> String!     func specificNames() -> [NSObject : AnyObject]!     func setSpecificName(_ name: String!, forFilesystem filesystem: String!)     func setSpecificNames(_ specificNames: [NSObject : AnyObject]!)     func mangledNameForFilesystem(_ filesystem: String!) -> String!     func mangledNames() -> [NSObject : AnyObject]!     func propertyForKey(_ key: String!, inFilesystem filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> AnyObject!     func propertiesForFilesystem(_ filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> [NSObject : AnyObject]!     func setProperty(_ property: AnyObject!, forKey key: String!, inFilesystem filesystem: String!)     func setProperties(_ properties: [NSObject : AnyObject]!, inFilesystem filesystem: String!)     func explicitFilesystemMask() -> DRFilesystemInclusionMask     func setExplicitFilesystemMask(_ mask: DRFilesystemInclusionMask)     func effectiveFilesystemMask() -> DRFilesystemInclusionMask } ``` | -- |
| To | ``` class DRFSObject : NSObject {     func isVirtual() -> Bool     func sourcePath() -> String!     func parent() -> DRFolder!     func baseName() -> String!     func setBaseName(_ baseName: String!)     func specificName(forFilesystem filesystem: String!) -> String!     func specificNames() -> [AnyHashable : Any]!     func setSpecificName(_ name: String!, forFilesystem filesystem: String!)     func setSpecificNames(_ specificNames: [AnyHashable : Any]!)     func mangledName(forFilesystem filesystem: String!) -> String!     func mangledNames() -> [AnyHashable : Any]!     func property(forKey key: String!, inFilesystem filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> Any!     func properties(forFilesystem filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> [AnyHashable : Any]!     func setProperty(_ property: Any!, forKey key: String!, inFilesystem filesystem: String!)     func setProperties(_ properties: [AnyHashable : Any]!, inFilesystem filesystem: String!)     func explicitFilesystemMask() -> DRFilesystemInclusionMask     func setExplicitFilesystemMask(_ mask: DRFilesystemInclusionMask)     func effectiveFilesystemMask() -> DRFilesystemInclusionMask     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRFSObject : CVarArg { } extension DRFSObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified DRFSObject.mangledName(forFilesystem: String!) -> String!

|  | Declaration |
| --- | --- |
| From | ``` func mangledNameForFilesystem(_ filesystem: String!) -> String! ``` |
| To | ``` func mangledName(forFilesystem filesystem: String!) -> String! ``` |

Modified DRFSObject.mangledNames() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func mangledNames() -> [NSObject : AnyObject]! ``` |
| To | ``` func mangledNames() -> [AnyHashable : Any]! ``` |

Modified DRFSObject.properties(forFilesystem: String!, mergeWithOtherFilesystems: Bool) -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func propertiesForFilesystem(_ filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> [NSObject : AnyObject]! ``` |
| To | ``` func properties(forFilesystem filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> [AnyHashable : Any]! ``` |

Modified DRFSObject.property(forKey: String!, inFilesystem: String!, mergeWithOtherFilesystems: Bool) -> Any!

|  | Declaration |
| --- | --- |
| From | ``` func propertyForKey(_ key: String!, inFilesystem filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> AnyObject! ``` |
| To | ``` func property(forKey key: String!, inFilesystem filesystem: String!, mergeWithOtherFilesystems merge: Bool) -> Any! ``` |

Modified DRFSObject.setProperties(_: [AnyHashable : Any]!, inFilesystem: String!)

|  | Declaration |
| --- | --- |
| From | ``` func setProperties(_ properties: [NSObject : AnyObject]!, inFilesystem filesystem: String!) ``` |
| To | ``` func setProperties(_ properties: [AnyHashable : Any]!, inFilesystem filesystem: String!) ``` |

Modified DRFSObject.setProperty(_: Any!, forKey: String!, inFilesystem: String!)

|  | Declaration |
| --- | --- |
| From | ``` func setProperty(_ property: AnyObject!, forKey key: String!, inFilesystem filesystem: String!) ``` |
| To | ``` func setProperty(_ property: Any!, forKey key: String!, inFilesystem filesystem: String!) ``` |

Modified DRFSObject.setSpecificNames(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func setSpecificNames(_ specificNames: [NSObject : AnyObject]!) ``` |
| To | ``` func setSpecificNames(_ specificNames: [AnyHashable : Any]!) ``` |

Modified DRFSObject.specificName(forFilesystem: String!) -> String!

|  | Declaration |
| --- | --- |
| From | ``` func specificNameForFilesystem(_ filesystem: String!) -> String! ``` |
| To | ``` func specificName(forFilesystem filesystem: String!) -> String! ``` |

Modified DRFSObject.specificNames() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func specificNames() -> [NSObject : AnyObject]! ``` |
| To | ``` func specificNames() -> [AnyHashable : Any]! ``` |

Modified DRMSF

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRMSF : NSNumber {     class func msf() -> DRMSF!     class func msfWithFrames(_ frames: UInt32) -> DRMSF!     class func msfWithString(_ string: String!) -> DRMSF!     init!(frames frames: UInt32)     init!(string string: String!)     func minutes() -> UInt32     func seconds() -> UInt32     func frames() -> UInt32     func sectors() -> UInt32     func msfByAdding(_ msf: DRMSF!) -> DRMSF!     func msfBySubtracting(_ msf: DRMSF!) -> DRMSF!     func description() -> String!     func descriptionWithFormat(_ format: String!) -> String!     func isEqualToMSF(_ otherDRMSF: DRMSF!) -> Bool } ``` | -- |
| To | ``` class DRMSF : NSNumber {      init!()     class func msf() -> DRMSF!      init!(frames frames: UInt32)     class func withFrames(_ frames: UInt32) -> DRMSF!      init!(string string: String!)     class func withString(_ string: String!) -> DRMSF!     init!(frames frames: UInt32)     init!(string string: String!)     func minutes() -> UInt32     func seconds() -> UInt32     func frames() -> UInt32     func sectors() -> UInt32     func adding(_ msf: DRMSF!) -> DRMSF!     func subtracting(_ msf: DRMSF!) -> DRMSF!     func description() -> String!     func description(withFormat format: String!) -> String!     func isEqual(to otherDRMSF: DRMSF!) -> Bool     var decimalValue: Decimal { get }      init(char value: Int8)     class func withChar(_ value: Int8) -> NSNumber      init(unsignedChar value: UInt8)     class func withUnsignedChar(_ value: UInt8) -> NSNumber      init(short value: Int16)     class func withShort(_ value: Int16) -> NSNumber      init(unsignedShort value: UInt16)     class func withUnsignedShort(_ value: UInt16) -> NSNumber      init(int value: Int32)     class func withInt(_ value: Int32) -> NSNumber      init(unsignedInt value: UInt32)     class func withUnsignedInt(_ value: UInt32) -> NSNumber      init(long value: Int)     class func withLong(_ value: Int) -> NSNumber      init(unsignedLong value: UInt)     class func withUnsignedLong(_ value: UInt) -> NSNumber      init(longLong value: Int64)     class func withLongLong(_ value: Int64) -> NSNumber      init(unsignedLongLong value: UInt64)     class func withUnsignedLongLong(_ value: UInt64) -> NSNumber      init(float value: Float)     class func withFloat(_ value: Float) -> NSNumber      init(double value: Double)     class func withDouble(_ value: Double) -> NSNumber      init(bool value: Bool)     class func withBool(_ value: Bool) -> NSNumber      init(integer value: Int)     class func withInteger(_ value: Int) -> NSNumber      init(unsignedInteger value: UInt)     class func withUnsignedInteger(_ value: UInt) -> NSNumber      init(point point: NSPoint)     class func withPoint(_ point: NSPoint) -> NSValue      init(size size: NSSize)     class func withSize(_ size: NSSize) -> NSValue      init(rect rect: NSRect)     class func withRect(_ rect: NSRect) -> NSValue      init(edgeInsets insets: EdgeInsets)     class func withEdgeInsets(_ insets: EdgeInsets) -> NSValue     var pointValue: NSPoint { get }     var sizeValue: NSSize { get }     var rectValue: NSRect { get }     var edgeInsetsValue: EdgeInsets { get }      init(range range: NSRange)     class func withRange(_ range: NSRange) -> NSValue     var rangeValue: NSRange { get }      init(nonretainedObject anObject: Any?)     class func withNonretainedObject(_ anObject: Any?) -> NSValue     var nonretainedObjectValue: Any? { get }      init(pointer pointer: UnsafeRawPointer?)     class func withPointer(_ pointer: UnsafeRawPointer?) -> NSValue     var pointerValue: UnsafeMutableRawPointer? { get }     func isEqual(to value: NSValue) -> Bool     class func withBytes(_ value: UnsafeRawPointer, objCType type: UnsafePointer<Int8>) -> NSValue      init(_ value: UnsafeRawPointer, withObjCType type: UnsafePointer<Int8>)     class func value(_ value: UnsafeRawPointer, withObjCType type: UnsafePointer<Int8>) -> NSValue     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRMSF : CVarArg { } extension DRMSF : Equatable, Hashable {     var hashValue: Int { get } } extension DRMSF : ExpressibleByFloatLiteral, ExpressibleByIntegerLiteral, ExpressibleByBooleanLiteral {     required convenience init(integerLiteral value: Int)     required convenience init(floatLiteral value: Double)     required convenience init(booleanLiteral value: Bool) } ``` | CVarArg, Equatable, ExpressibleByBooleanLiteral, ExpressibleByFloatLiteral, ExpressibleByIntegerLiteral, Hashable |

Modified DRMSF.adding(_: DRMSF!) -> DRMSF!

|  | Declaration |
| --- | --- |
| From | ``` func msfByAdding(_ msf: DRMSF!) -> DRMSF! ``` |
| To | ``` func adding(_ msf: DRMSF!) -> DRMSF! ``` |

Modified DRMSF.description(withFormat: String!) -> String!

|  | Declaration |
| --- | --- |
| From | ``` func descriptionWithFormat(_ format: String!) -> String! ``` |
| To | ``` func description(withFormat format: String!) -> String! ``` |

Modified DRMSF.isEqual(to: DRMSF!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToMSF(_ otherDRMSF: DRMSF!) -> Bool ``` |
| To | ``` func isEqual(to otherDRMSF: DRMSF!) -> Bool ``` |

Modified DRMSF.subtracting(_: DRMSF!) -> DRMSF!

|  | Declaration |
| --- | --- |
| From | ``` func msfBySubtracting(_ msf: DRMSF!) -> DRMSF! ``` |
| To | ``` func subtracting(_ msf: DRMSF!) -> DRMSF! ``` |

Modified DRMSFFormatter

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRMSFFormatter : NSFormatter {     init!(format format: String!)     func format() -> String!     func setFormat(_ format: String!) } ``` | -- |
| To | ``` class DRMSFFormatter : Formatter {     init!(format format: String!)     func format() -> String!     func setFormat(_ format: String!)     enum Context : Int {         case unknown         case dynamic         case standalone         case listItem         case beginningOfSentence         case middleOfSentence     }     enum UnitStyle : Int {         case short         case medium         case long     }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRMSFFormatter : CVarArg { } extension DRMSFFormatter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified DRNotificationCenter

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRNotificationCenter : NSObject {     class func currentRunLoopCenter() -> DRNotificationCenter!     func addObserver(_ observer: AnyObject!, selector aSelector: Selector, name notificationName: String!, object anObject: AnyObject!)     func removeObserver(_ observer: AnyObject!, name aName: String!, object anObject: AnyObject!) } ``` | -- |
| To | ``` class DRNotificationCenter : NSObject {     class func currentRunLoop() -> DRNotificationCenter!     func addObserver(_ observer: Any!, selector aSelector: Selector!, name notificationName: String!, object anObject: Any!)     func removeObserver(_ observer: Any!, name aName: String!, object anObject: Any!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRNotificationCenter : CVarArg { } extension DRNotificationCenter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified DRNotificationCenter.addObserver(_: Any!, selector: Selector!, name: String!, object: Any!)

|  | Declaration |
| --- | --- |
| From | ``` func addObserver(_ observer: AnyObject!, selector aSelector: Selector, name notificationName: String!, object anObject: AnyObject!) ``` |
| To | ``` func addObserver(_ observer: Any!, selector aSelector: Selector!, name notificationName: String!, object anObject: Any!) ``` |

Modified DRNotificationCenter.currentRunLoop() -> DRNotificationCenter! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func currentRunLoopCenter() -> DRNotificationCenter! ``` |
| To | ``` class func currentRunLoop() -> DRNotificationCenter! ``` |

Modified DRNotificationCenter.removeObserver(_: Any!, name: String!, object: Any!)

|  | Declaration |
| --- | --- |
| From | ``` func removeObserver(_ observer: AnyObject!, name aName: String!, object anObject: AnyObject!) ``` |
| To | ``` func removeObserver(_ observer: Any!, name aName: String!, object anObject: Any!) ``` |

Modified DRRefConCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRRefConCallbacks {     var version: UInt     var retain: DRRefConRetainCallback!     var release: DRRefConReleaseCallback!     init()     init(version version: UInt, retain retain: DRRefConRetainCallback!, release release: DRRefConReleaseCallback!) } ``` |
| To | ``` struct DRRefConCallbacks {     var version: UInt     var retain: DiscRecording.DRRefConRetainCallback!     var release: DiscRecording.DRRefConReleaseCallback!     init()     init(version version: UInt, retain retain: DiscRecording.DRRefConRetainCallback!, release release: DiscRecording.DRRefConReleaseCallback!) } ``` |

Modified DRRefConCallbacks.release

|  | Declaration |
| --- | --- |
| From | ``` var release: DRRefConReleaseCallback! ``` |
| To | ``` var release: DiscRecording.DRRefConReleaseCallback! ``` |

Modified DRRefConCallbacks.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: DRRefConRetainCallback! ``` |
| To | ``` var retain: DiscRecording.DRRefConRetainCallback! ``` |

Modified DRTrack

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class DRTrack : NSObject {     init!(producer producer: AnyObject!)     func properties() -> [NSObject : AnyObject]!     func setProperties(_ properties: [NSObject : AnyObject]!)     func testProductionSpeedForInterval(_ interval: NSTimeInterval) -> Float     func testProductionSpeedForLength(_ length: UInt32) -> Float     func estimateLength() -> UInt64 } extension DRTrack {     func length() -> DRMSF!     func preGap() -> DRMSF!     func setPreGap(_ preGap: DRMSF!) } extension DRTrack {      init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!)     class func trackForAudioOfLength(_ length: DRMSF!, producer producer: AnyObject!) -> DRTrack!      init!(forAudioFile path: String!)     class func trackForAudioFile(_ path: String!) -> DRTrack! } extension DRTrack {      init!(forRootFolder rootFolder: DRFolder!)     class func trackForRootFolder(_ rootFolder: DRFolder!) -> DRTrack! } ``` | -- |
| To | ``` class DRTrack : NSObject {     init!(producer producer: Any!)     func properties() -> [AnyHashable : Any]!     func setProperties(_ properties: [AnyHashable : Any]!)     func testProductionSpeed(forInterval interval: TimeInterval) -> Float     func testProductionSpeed(forLength length: UInt32) -> Float     func estimateLength() -> UInt64      init!(forRootFolder rootFolder: DRFolder!)     class func forRootFolder(_ rootFolder: DRFolder!) -> DRTrack!      init!(forAudioOfLength length: DRMSF!, producer producer: Any!)     class func forAudioOfLength(_ length: DRMSF!, producer producer: Any!) -> DRTrack!      init!(forAudioFile path: String!)     class func forAudioFile(_ path: String!) -> DRTrack!     func length() -> DRMSF!     func preGap() -> DRMSF!     func setPreGap(_ preGap: DRMSF!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension DRTrack : CVarArg { } extension DRTrack : Equatable, Hashable {     var hashValue: Int { get } } extension DRTrack {     func length() -> DRMSF!     func preGap() -> DRMSF!     func setPreGap(_ preGap: DRMSF!) } extension DRTrack {      init!(forAudioOfLength length: DRMSF!, producer producer: Any!)     class func forAudioOfLength(_ length: DRMSF!, producer producer: Any!) -> DRTrack!      init!(forAudioFile path: String!)     class func forAudioFile(_ path: String!) -> DRTrack! } extension DRTrack {      init!(forRootFolder rootFolder: DRFolder!)     class func forRootFolder(_ rootFolder: DRFolder!) -> DRTrack! } ``` | CVarArg, Equatable, Hashable |

Modified DRTrack.init(forAudioOfLength: DRMSF!, producer: Any!)

|  | Declaration |
| --- | --- |
| From | ``` init!(forAudioOfLength length: DRMSF!, producer producer: AnyObject!) ``` |
| To | ``` init!(forAudioOfLength length: DRMSF!, producer producer: Any!) ``` |

Modified DRTrack.init(producer: Any!)

|  | Declaration |
| --- | --- |
| From | ``` init!(producer producer: AnyObject!) ``` |
| To | ``` init!(producer producer: Any!) ``` |

Modified DRTrack.properties() -> [AnyHashable : Any]!

|  | Declaration |
| --- | --- |
| From | ``` func properties() -> [NSObject : AnyObject]! ``` |
| To | ``` func properties() -> [AnyHashable : Any]! ``` |

Modified DRTrack.setProperties(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func setProperties(_ properties: [NSObject : AnyObject]!) ``` |
| To | ``` func setProperties(_ properties: [AnyHashable : Any]!) ``` |

Modified DRTrack.testProductionSpeed(forInterval: TimeInterval) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func testProductionSpeedForInterval(_ interval: NSTimeInterval) -> Float ``` |
| To | ``` func testProductionSpeed(forInterval interval: TimeInterval) -> Float ``` |

Modified DRTrack.testProductionSpeed(forLength: UInt32) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func testProductionSpeedForLength(_ length: UInt32) -> Float ``` |
| To | ``` func testProductionSpeed(forLength length: UInt32) -> Float ``` |

Modified DRTrackDataProduction

|  | Declaration |
| --- | --- |
| From | ``` protocol DRTrackDataProduction {     func estimateLengthOfTrack(_ track: DRTrack!) -> UInt64     func prepareTrack(_ track: DRTrack!, forBurn burn: DRBurn!, toMedia mediaInfo: [NSObject : AnyObject]!) -> Bool     func cleanupTrackAfterBurn(_ track: DRTrack!)     func producePreGapForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> UInt32     func produceDataForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> UInt32     func prepareTrackForVerification(_ track: DRTrack!) -> Bool     func verifyPreGapForTrack(_ track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> Bool     func verifyDataForTrack(_ track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> Bool     func cleanupTrackAfterVerification(_ track: DRTrack!) -> Bool } ``` |
| To | ``` protocol DRTrackDataProduction {     func estimateLength(of track: DRTrack!) -> UInt64     func prepare(_ track: DRTrack!, for burn: DRBurn!, toMedia mediaInfo: [AnyHashable : Any]!) -> Bool     func cleanupTrack(afterBurn track: DRTrack!)     func producePreGap(for track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> UInt32     func produceData(for track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> UInt32     func prepareTrack(forVerification track: DRTrack!) -> Bool     func verifyPreGap(for track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> Bool     func verifyData(for track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> Bool     func cleanupTrack(afterVerification track: DRTrack!) -> Bool } ``` |

Modified DRTrackDataProduction.cleanupTrack(afterBurn: DRTrack!)

|  | Declaration |
| --- | --- |
| From | ``` func cleanupTrackAfterBurn(_ track: DRTrack!) ``` |
| To | ``` func cleanupTrack(afterBurn track: DRTrack!) ``` |

Modified DRTrackDataProduction.cleanupTrack(afterVerification: DRTrack!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func cleanupTrackAfterVerification(_ track: DRTrack!) -> Bool ``` |
| To | ``` func cleanupTrack(afterVerification track: DRTrack!) -> Bool ``` |

Modified DRTrackDataProduction.estimateLength(of: DRTrack!) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func estimateLengthOfTrack(_ track: DRTrack!) -> UInt64 ``` |
| To | ``` func estimateLength(of track: DRTrack!) -> UInt64 ``` |

Modified DRTrackDataProduction.prepare(_: DRTrack!, for: DRBurn!, toMedia: [AnyHashable : Any]!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func prepareTrack(_ track: DRTrack!, forBurn burn: DRBurn!, toMedia mediaInfo: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` func prepare(_ track: DRTrack!, for burn: DRBurn!, toMedia mediaInfo: [AnyHashable : Any]!) -> Bool ``` |

Modified DRTrackDataProduction.prepareTrack(forVerification: DRTrack!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func prepareTrackForVerification(_ track: DRTrack!) -> Bool ``` |
| To | ``` func prepareTrack(forVerification track: DRTrack!) -> Bool ``` |

Modified DRTrackDataProduction.produceData(for: DRTrack!, intoBuffer: UnsafeMutablePointer<Int8>!, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>!) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func produceDataForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> UInt32 ``` |
| To | ``` func produceData(for track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> UInt32 ``` |

Modified DRTrackDataProduction.producePreGap(for: DRTrack!, intoBuffer: UnsafeMutablePointer<Int8>!, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>!) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func producePreGapForTrack(_ track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> UInt32 ``` |
| To | ``` func producePreGap(for track: DRTrack!, intoBuffer buffer: UnsafeMutablePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> UInt32 ``` |

Modified DRTrackDataProduction.verifyData(for: DRTrack!, inBuffer: UnsafePointer<Int8>!, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func verifyDataForTrack(_ track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> Bool ``` |
| To | ``` func verifyData(for track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> Bool ``` |

Modified DRTrackDataProduction.verifyPreGap(for: DRTrack!, inBuffer: UnsafePointer<Int8>!, length: UInt32, atAddress: UInt64, blockSize: UInt32, ioFlags: UnsafeMutablePointer<UInt32>!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func verifyPreGapForTrack(_ track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>) -> Bool ``` |
| To | ``` func verifyPreGap(for track: DRTrack!, inBuffer buffer: UnsafePointer<Int8>!, length bufferLength: UInt32, atAddress address: UInt64, blockSize blockSize: UInt32, ioFlags flags: UnsafeMutablePointer<UInt32>!) -> Bool ``` |

Modified DRTrackProductionInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DRTrackProductionInfo {     var buffer: UnsafeMutablePointer<Void>     var reqCount: UInt32     var actCount: UInt32     var flags: UInt32     var blockSize: UInt32     var requestedAddress: UInt64     init()     init(buffer buffer: UnsafeMutablePointer<Void>, reqCount reqCount: UInt32, actCount actCount: UInt32, flags flags: UInt32, blockSize blockSize: UInt32, requestedAddress requestedAddress: UInt64) } ``` |
| To | ``` struct DRTrackProductionInfo {     var buffer: UnsafeMutableRawPointer!     var reqCount: UInt32     var actCount: UInt32     var flags: UInt32     var blockSize: UInt32     var requestedAddress: UInt64     init()     init(buffer buffer: UnsafeMutableRawPointer!, reqCount reqCount: UInt32, actCount actCount: UInt32, flags flags: UInt32, blockSize blockSize: UInt32, requestedAddress requestedAddress: UInt64) } ``` |

Modified DRTrackProductionInfo.buffer

|  | Declaration |
| --- | --- |
| From | ``` var buffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var buffer: UnsafeMutableRawPointer! ``` |

Modified NSNotification.Name.DRBurnStatusChanged

|  | Name | Declaration |
| --- | --- | --- |
| From | DRBurnStatusChangedNotification | ``` let DRBurnStatusChangedNotification: String ``` |
| To | DRBurnStatusChanged | ``` static let DRBurnStatusChanged: NSNotification.Name ``` |

Modified NSNotification.Name.DRDeviceAppeared

|  | Name | Declaration |
| --- | --- | --- |
| From | DRDeviceAppearedNotification | ``` let DRDeviceAppearedNotification: String ``` |
| To | DRDeviceAppeared | ``` static let DRDeviceAppeared: NSNotification.Name ``` |

Modified NSNotification.Name.DRDeviceDisappeared

|  | Name | Declaration |
| --- | --- | --- |
| From | DRDeviceDisappearedNotification | ``` let DRDeviceDisappearedNotification: String ``` |
| To | DRDeviceDisappeared | ``` static let DRDeviceDisappeared: NSNotification.Name ``` |

Modified NSNotification.Name.DRDeviceStatusChanged

|  | Name | Declaration |
| --- | --- | --- |
| From | DRDeviceStatusChangedNotification | ``` let DRDeviceStatusChangedNotification: String ``` |
| To | DRDeviceStatusChanged | ``` static let DRDeviceStatusChanged: NSNotification.Name ``` |

Modified NSNotification.Name.DREraseStatusChanged

|  | Name | Declaration |
| --- | --- | --- |
| From | DREraseStatusChangedNotification | ``` let DREraseStatusChangedNotification: String ``` |
| To | DREraseStatusChanged | ``` static let DREraseStatusChanged: NSNotification.Name ``` |

Modified DRAudioTrack

|  | Declaration |
| --- | --- |
| From | ``` typealias DRAudioTrackRef = DRAudioTrack ``` |
| To | ``` typealias DRAudioTrack = DRTrackRef ``` |

Modified DRAudioTrackCreate(_: UnsafePointer<FSRef>!) -> Unmanaged<DRAudioTrack>!

|  | Declaration |
| --- | --- |
| From | ``` func DRAudioTrackCreate(_ audioFile: UnsafePointer<FSRef>) -> Unmanaged<DRAudioTrack>! ``` |
| To | ``` func DRAudioTrackCreate(_ audioFile: UnsafePointer<FSRef>!) -> Unmanaged<DRAudioTrack>! ``` |

Modified DRBurnWriteLayout(_: DRBurnRef!, _: CFTypeRef!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnWriteLayout(_ burn: DRBurnRef!, _ layout: AnyObject!) -> OSStatus ``` |
| To | ``` func DRBurnWriteLayout(_ burn: DRBurnRef!, _ layout: CFTypeRef!) -> OSStatus ``` |

Modified DRCDTextBlockGetValue(_: DRCDTextBlockRef!, _: CFIndex, _: CFString!) -> Unmanaged<CFTypeRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockGetValue(_ block: DRCDTextBlockRef!, _ trackIndex: CFIndex, _ key: CFString!) -> Unmanaged<AnyObject>! ``` |
| To | ``` func DRCDTextBlockGetValue(_ block: DRCDTextBlockRef!, _ trackIndex: CFIndex, _ key: CFString!) -> Unmanaged<CFTypeRef>! ``` |

Modified DRCDTextBlockSetValue(_: DRCDTextBlockRef!, _: CFIndex, _: CFString!, _: CFTypeRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRCDTextBlockSetValue(_ block: DRCDTextBlockRef!, _ trackIndex: CFIndex, _ key: CFString!, _ value: AnyObject!) ``` |
| To | ``` func DRCDTextBlockSetValue(_ block: DRCDTextBlockRef!, _ trackIndex: CFIndex, _ key: CFString!, _ value: CFTypeRef!) ``` |

Modified DRFileCreateReal(_: UnsafePointer<FSRef>!) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFileRef>! ``` |
| To | ``` func DRFileCreateReal(_ fsRef: UnsafePointer<FSRef>!) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileCreateVirtualWithCallback(_: CFString!, _: DiscRecording.DRFileProc!, _: UnsafeMutableRawPointer!) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DRFileProc!, _ fileProcRefCon: UnsafeMutablePointer<Void>) -> Unmanaged<DRFileRef>! ``` |
| To | ``` func DRFileCreateVirtualWithCallback(_ baseName: CFString!, _ fileProc: DiscRecording.DRFileProc!, _ fileProcRefCon: UnsafeMutableRawPointer!) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileCreateVirtualWithData(_: CFString!, _: UnsafeMutableRawPointer!, _: UInt32) -> Unmanaged<DRFileRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFileCreateVirtualWithData(_ baseName: CFString!, _ fileData: UnsafeMutablePointer<Void>, _ fileDataLength: UInt32) -> Unmanaged<DRFileRef>! ``` |
| To | ``` func DRFileCreateVirtualWithData(_ baseName: CFString!, _ fileData: UnsafeMutableRawPointer!, _ fileDataLength: UInt32) -> Unmanaged<DRFileRef>! ``` |

Modified DRFileProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRFileProc = (UnsafeMutablePointer<Void>, DRFileRef!, DRFileMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias DRFileProc = (UnsafeMutableRawPointer?, DRFileRef?, DRFileMessage, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified DRFolderCreateReal(_: UnsafePointer<FSRef>!) -> Unmanaged<DRFolderRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFolderCreateReal(_ fsRef: UnsafePointer<FSRef>) -> Unmanaged<DRFolderRef>! ``` |
| To | ``` func DRFolderCreateReal(_ fsRef: UnsafePointer<FSRef>!) -> Unmanaged<DRFolderRef>! ``` |

Modified DRFSObjectCopyFilesystemProperty(_: DRFSObjectRef!, _: CFString!, _: CFString!, _: Bool) -> Unmanaged<CFTypeRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Bool) -> Unmanaged<AnyObject>! ``` |
| To | ``` func DRFSObjectCopyFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ coalesce: Bool) -> Unmanaged<CFTypeRef>! ``` |

Modified DRFSObjectGetFilesystemMask(_: DRFSObjectRef!, _: UnsafeMutablePointer<DRFilesystemMask>!, _: UnsafeMutablePointer<DRFilesystemMask>!) -> DRFilesystemMask

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectGetFilesystemMask(_ object: DRFSObjectRef!, _ explicitMask: UnsafeMutablePointer<DRFilesystemMask>, _ effectiveMask: UnsafeMutablePointer<DRFilesystemMask>) -> DRFilesystemMask ``` |
| To | ``` func DRFSObjectGetFilesystemMask(_ object: DRFSObjectRef!, _ explicitMask: UnsafeMutablePointer<DRFilesystemMask>!, _ effectiveMask: UnsafeMutablePointer<DRFilesystemMask>!) -> DRFilesystemMask ``` |

Modified DRFSObjectGetRealFSRef(_: DRFSObjectRef!, _: UnsafeMutablePointer<FSRef>!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectGetRealFSRef(_ object: DRFSObjectRef!, _ fsRef: UnsafeMutablePointer<FSRef>) ``` |
| To | ``` func DRFSObjectGetRealFSRef(_ object: DRFSObjectRef!, _ fsRef: UnsafeMutablePointer<FSRef>!) ``` |

Modified DRFSObjectSetFilesystemProperty(_: DRFSObjectRef!, _: CFString!, _: CFString!, _: CFTypeRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRFSObjectSetFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ value: AnyObject!) ``` |
| To | ``` func DRFSObjectSetFilesystemProperty(_ object: DRFSObjectRef!, _ fsKey: CFString!, _ propertyKey: CFString!, _ value: CFTypeRef!) ``` |

Modified DRGetRefCon(_: DRType!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func DRGetRefCon(_ ref: DRType!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func DRGetRefCon(_ ref: DRType!) -> UnsafeMutableRawPointer! ``` |

Modified DRNotificationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRNotificationCallback = (DRNotificationCenterRef!, UnsafeMutablePointer<Void>, CFString!, DRType!, CFDictionary!) -> Void ``` |
| To | ``` typealias DRNotificationCallback = (DRNotificationCenterRef?, UnsafeMutableRawPointer?, CFString?, DRType?, CFDictionary?) -> Swift.Void ``` |

Modified DRNotificationCenterAddObserver(_: DRNotificationCenterRef!, _: UnsafeRawPointer!, _: DiscRecording.DRNotificationCallback!, _: CFString!, _: DRType!)

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenterRef!, _ observer: UnsafePointer<Void>, _ callback: DRNotificationCallback!, _ name: CFString!, _ object: DRType!) ``` |
| To | ``` func DRNotificationCenterAddObserver(_ center: DRNotificationCenterRef!, _ observer: UnsafeRawPointer!, _ callback: DiscRecording.DRNotificationCallback!, _ name: CFString!, _ object: DRType!) ``` |

Modified DRNotificationCenterRemoveObserver(_: DRNotificationCenterRef!, _: UnsafeRawPointer!, _: CFString!, _: DRType!)

|  | Declaration |
| --- | --- |
| From | ``` func DRNotificationCenterRemoveObserver(_ center: DRNotificationCenterRef!, _ observer: UnsafePointer<Void>, _ name: CFString!, _ object: DRType!) ``` |
| To | ``` func DRNotificationCenterRemoveObserver(_ center: DRNotificationCenterRef!, _ observer: UnsafeRawPointer!, _ name: CFString!, _ object: DRType!) ``` |

Modified DRRefConReleaseCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRRefConReleaseCallback = (UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias DRRefConReleaseCallback = (UnsafeRawPointer?) -> Swift.Void ``` |

Modified DRRefConRetainCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias DRRefConRetainCallback = (UnsafePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias DRRefConRetainCallback = (UnsafeRawPointer?) -> UnsafeRawPointer? ``` |

Modified DRSetRefCon(_: DRType!, _: UnsafeMutableRawPointer!, _: UnsafePointer<DRRefConCallbacks>!)

|  | Declaration |
| --- | --- |
| From | ``` func DRSetRefCon(_ ref: DRType!, _ refCon: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<DRRefConCallbacks>) ``` |
| To | ``` func DRSetRefCon(_ ref: DRType!, _ refCon: UnsafeMutableRawPointer!, _ callbacks: UnsafePointer<DRRefConCallbacks>!) ``` |

Modified DRTrackCallbackProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTrackCallbackProc = (DRTrackRef!, DRTrackMessage, UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` typealias DRTrackCallbackProc = (DRTrackRef?, DRTrackMessage, UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified DRTrackCreate(_: CFDictionary!, _: DiscRecording.DRTrackCallbackProc!) -> Unmanaged<DRTrackRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRTrackCreate(_ properties: CFDictionary!, _ callback: DRTrackCallbackProc!) -> Unmanaged<DRTrackRef>! ``` |
| To | ``` func DRTrackCreate(_ properties: CFDictionary!, _ callback: DiscRecording.DRTrackCallbackProc!) -> Unmanaged<DRTrackRef>! ``` |

Modified DRType

|  | Declaration |
| --- | --- |
| From | ``` typealias DRTypeRef = DRType ``` |
| To | ``` typealias DRType = CFTypeRef ``` |

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
