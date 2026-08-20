---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CoreWLAN.html
archived_at: '2026-07-18T02:51:12.705024Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreWLAN Changes for Swift

### CoreWLAN

Removed [CWCipherKeyFlags.None](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagsnone)Added CWEventDelegate.rangingReportEventForWiFiInterface(withName: String, data: [Any], error: Error)Added CWEventDelegate.virtualInterfaceStateChangedForWiFiInterface(withName: String)Added [CWEventType.rangingReportEvent](https://developer.apple.com/documentation/corewlan/cweventtype/rangingreportevent)Added [CWEventType.virtualInterfaceStateChanged](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypevirtualinterfacestatechanged)Modified [CWChannel](https://developer.apple.com/documentation/corewlan/cwchannel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CWChannel : NSObject, NSCopying, NSSecureCoding {     var channelNumber: Int { get }     var channelWidth: CWChannelWidth { get }     var channelBand: CWChannelBand { get }     func isEqualToChannel(_ channel: CWChannel) -> Bool } ``` | NSCopying, NSSecureCoding |
| To | ``` class CWChannel : NSObject, NSCopying, NSSecureCoding {     var channelNumber: Int { get }     var channelWidth: CWChannelWidth { get }     var channelBand: CWChannelBand { get }     func isEqual(to channel: CWChannel) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CWChannel : CVarArg { } extension CWChannel : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CWChannel.isEqual(to: CWChannel) -> Bool](https://developer.apple.com/documentation/corewlan/cwchannel/1512390-isequaltochannel)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToChannel(_ channel: CWChannel) -> Bool ``` |
| To | ``` func isEqual(to channel: CWChannel) -> Bool ``` |

Modified [CWChannelBand [enum]](https://developer.apple.com/documentation/corewlan/cwchannelband)

|  | Declaration |
| --- | --- |
| From | ``` enum CWChannelBand : Int {     case BandUnknown     case Band2GHz     case Band5GHz } ``` |
| To | ``` enum CWChannelBand : Int {     case bandUnknown     case band2GHz     case band5GHz } ``` |

Modified [CWChannelBand.band2GHz](https://developer.apple.com/documentation/corewlan/cwchannelband/band2ghz)

|  | Declaration |
| --- | --- |
| From | ``` case Band2GHz ``` |
| To | ``` case band2GHz ``` |

Modified [CWChannelBand.band5GHz](https://developer.apple.com/documentation/corewlan/cwchannelband/kcwchannelband5ghz)

|  | Declaration |
| --- | --- |
| From | ``` case Band5GHz ``` |
| To | ``` case band5GHz ``` |

Modified [CWChannelBand.bandUnknown](https://developer.apple.com/documentation/corewlan/cwchannelband/bandunknown)

|  | Declaration |
| --- | --- |
| From | ``` case BandUnknown ``` |
| To | ``` case bandUnknown ``` |

Modified [CWChannelWidth [enum]](https://developer.apple.com/documentation/corewlan/cwchannelwidth)

|  | Declaration |
| --- | --- |
| From | ``` enum CWChannelWidth : Int {     case WidthUnknown     case Width20MHz     case Width40MHz     case Width80MHz     case Width160MHz } ``` |
| To | ``` enum CWChannelWidth : Int {     case widthUnknown     case width20MHz     case width40MHz     case width80MHz     case width160MHz } ``` |

Modified [CWChannelWidth.width160MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth160mhz)

|  | Declaration |
| --- | --- |
| From | ``` case Width160MHz ``` |
| To | ``` case width160MHz ``` |

Modified [CWChannelWidth.width20MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth20mhz)

|  | Declaration |
| --- | --- |
| From | ``` case Width20MHz ``` |
| To | ``` case width20MHz ``` |

Modified [CWChannelWidth.width40MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth40mhz)

|  | Declaration |
| --- | --- |
| From | ``` case Width40MHz ``` |
| To | ``` case width40MHz ``` |

Modified [CWChannelWidth.width80MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth80mhz)

|  | Declaration |
| --- | --- |
| From | ``` case Width80MHz ``` |
| To | ``` case width80MHz ``` |

Modified [CWChannelWidth.widthUnknown](https://developer.apple.com/documentation/corewlan/cwchannelwidth/widthunknown)

|  | Declaration |
| --- | --- |
| From | ``` case WidthUnknown ``` |
| To | ``` case widthUnknown ``` |

Modified [CWCipherKeyFlags [struct]](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CWCipherKeyFlags : OptionSetType {     init(rawValue rawValue: UInt)     static var None: CWCipherKeyFlags { get }     static var Unicast: CWCipherKeyFlags { get }     static var Multicast: CWCipherKeyFlags { get }     static var Tx: CWCipherKeyFlags { get }     static var Rx: CWCipherKeyFlags { get } } ``` | OptionSetType |
| To | ``` struct CWCipherKeyFlags : OptionSet {     init(rawValue rawValue: UInt)     static var none: CWCipherKeyFlags { get }     static var unicast: CWCipherKeyFlags { get }     static var multicast: CWCipherKeyFlags { get }     static var tx: CWCipherKeyFlags { get }     static var rx: CWCipherKeyFlags { get }     func intersect(_ other: CWCipherKeyFlags) -> CWCipherKeyFlags     func exclusiveOr(_ other: CWCipherKeyFlags) -> CWCipherKeyFlags     mutating func unionInPlace(_ other: CWCipherKeyFlags)     mutating func intersectInPlace(_ other: CWCipherKeyFlags)     mutating func exclusiveOrInPlace(_ other: CWCipherKeyFlags)     func isSubsetOf(_ other: CWCipherKeyFlags) -> Bool     func isDisjointWith(_ other: CWCipherKeyFlags) -> Bool     func isSupersetOf(_ other: CWCipherKeyFlags) -> Bool     mutating func subtractInPlace(_ other: CWCipherKeyFlags)     func isStrictSupersetOf(_ other: CWCipherKeyFlags) -> Bool     func isStrictSubsetOf(_ other: CWCipherKeyFlags) -> Bool } extension CWCipherKeyFlags {     func union(_ other: CWCipherKeyFlags) -> CWCipherKeyFlags     func intersection(_ other: CWCipherKeyFlags) -> CWCipherKeyFlags     func symmetricDifference(_ other: CWCipherKeyFlags) -> CWCipherKeyFlags } extension CWCipherKeyFlags {     func contains(_ member: CWCipherKeyFlags) -> Bool     mutating func insert(_ newMember: CWCipherKeyFlags) -> (inserted: Bool, memberAfterInsert: CWCipherKeyFlags)     mutating func remove(_ member: CWCipherKeyFlags) -> CWCipherKeyFlags?     mutating func update(with newMember: CWCipherKeyFlags) -> CWCipherKeyFlags? } extension CWCipherKeyFlags {     convenience init()     mutating func formUnion(_ other: CWCipherKeyFlags)     mutating func formIntersection(_ other: CWCipherKeyFlags)     mutating func formSymmetricDifference(_ other: CWCipherKeyFlags) } extension CWCipherKeyFlags {     convenience init<S : Sequence where S.Iterator.Element == CWCipherKeyFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CWCipherKeyFlags...)     mutating func subtract(_ other: CWCipherKeyFlags)     func isSubset(of other: CWCipherKeyFlags) -> Bool     func isSuperset(of other: CWCipherKeyFlags) -> Bool     func isDisjoint(with other: CWCipherKeyFlags) -> Bool     func subtracting(_ other: CWCipherKeyFlags) -> CWCipherKeyFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: CWCipherKeyFlags) -> Bool     func isStrictSubset(of other: CWCipherKeyFlags) -> Bool } ``` | OptionSet |

Modified [CWCipherKeyFlags.multicast](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/1462695-multicast)

|  | Declaration |
| --- | --- |
| From | ``` static var Multicast: CWCipherKeyFlags { get } ``` |
| To | ``` static var multicast: CWCipherKeyFlags { get } ``` |

Modified [CWCipherKeyFlags.rx](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagsrx)

|  | Declaration |
| --- | --- |
| From | ``` static var Rx: CWCipherKeyFlags { get } ``` |
| To | ``` static var rx: CWCipherKeyFlags { get } ``` |

Modified [CWCipherKeyFlags.tx](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/1462723-tx)

|  | Declaration |
| --- | --- |
| From | ``` static var Tx: CWCipherKeyFlags { get } ``` |
| To | ``` static var tx: CWCipherKeyFlags { get } ``` |

Modified [CWCipherKeyFlags.unicast](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagsunicast)

|  | Declaration |
| --- | --- |
| From | ``` static var Unicast: CWCipherKeyFlags { get } ``` |
| To | ``` static var unicast: CWCipherKeyFlags { get } ``` |

Modified [CWConfiguration](https://developer.apple.com/documentation/corewlan/cwconfiguration)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CWConfiguration : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     @NSCopying var networkProfiles: NSOrderedSet { get }     var requireAdministratorForAssociation: Bool { get }     var requireAdministratorForPower: Bool { get }     var requireAdministratorForIBSSMode: Bool { get }     var rememberJoinedNetworks: Bool { get }     convenience init()     class func configuration() -> Self     init()     init(configuration configuration: CWConfiguration)     class func configurationWithConfiguration(_ configuration: CWConfiguration) -> Self     func isEqualToConfiguration(_ configuration: CWConfiguration) -> Bool } ``` | NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class CWConfiguration : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     @NSCopying var networkProfiles: NSOrderedSet { get }     var requireAdministratorForAssociation: Bool { get }     var requireAdministratorForPower: Bool { get }     var requireAdministratorForIBSSMode: Bool { get }     var rememberJoinedNetworks: Bool { get }     convenience init()     class func configuration() -> Self     init()     init(configuration configuration: CWConfiguration)     class func withConfiguration(_ configuration: CWConfiguration) -> Self     func isEqual(to configuration: CWConfiguration) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CWConfiguration : CVarArg { } extension CWConfiguration : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [CWConfiguration.isEqual(to: CWConfiguration) -> Bool](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507064-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToConfiguration(_ configuration: CWConfiguration) -> Bool ``` |
| To | ``` func isEqual(to configuration: CWConfiguration) -> Bool ``` |

Modified [CWErr [enum]](https://developer.apple.com/documentation/corewlan/cwerr)

|  | Declaration |
| --- | --- |
| From | ``` enum CWErr : Int {     case CWNoErr     case CWEAPOLErr     case CWInvalidParameterErr     case CWNoMemoryErr     case CWUnknownErr     case CWNotSupportedErr     case CWInvalidFormatErr     case CWTimeoutErr     case CWUnspecifiedFailureErr     case CWUnsupportedCapabilitiesErr     case CWReassociationDeniedErr     case CWAssociationDeniedErr     case CWAuthenticationAlgorithmUnsupportedErr     case CWInvalidAuthenticationSequenceNumberErr     case CWChallengeFailureErr     case CWAPFullErr     case CWUnsupportedRateSetErr     case CWShortSlotUnsupportedErr     case CWDSSSOFDMUnsupportedErr     case CWInvalidInformationElementErr     case CWInvalidGroupCipherErr     case CWInvalidPairwiseCipherErr     case CWInvalidAKMPErr     case CWUnsupportedRSNVersionErr     case CWInvalidRSNCapabilitiesErr     case CWCipherSuiteRejectedErr     case CWInvalidPMKErr     case CWSupplicantTimeoutErr     case CWHTFeaturesNotSupportedErr     case CWPCOTransitionTimeNotSupportedErr     case CWReferenceNotBoundErr     case CWIPCFailureErr     case CWOperationNotPermittedErr     case CWErr } ``` |
| To | ``` enum CWErr : Int {     case cwNoErr     case cweapolErr     case cwInvalidParameterErr     case cwNoMemoryErr     case cwUnknownErr     case cwNotSupportedErr     case cwInvalidFormatErr     case cwTimeoutErr     case cwUnspecifiedFailureErr     case cwUnsupportedCapabilitiesErr     case cwReassociationDeniedErr     case cwAssociationDeniedErr     case cwAuthenticationAlgorithmUnsupportedErr     case cwInvalidAuthenticationSequenceNumberErr     case cwChallengeFailureErr     case cwapFullErr     case cwUnsupportedRateSetErr     case cwShortSlotUnsupportedErr     case cwdsssofdmUnsupportedErr     case cwInvalidInformationElementErr     case cwInvalidGroupCipherErr     case cwInvalidPairwiseCipherErr     case cwInvalidAKMPErr     case cwUnsupportedRSNVersionErr     case cwInvalidRSNCapabilitiesErr     case cwCipherSuiteRejectedErr     case cwInvalidPMKErr     case cwSupplicantTimeoutErr     case cwhtFeaturesNotSupportedErr     case cwpcoTransitionTimeNotSupportedErr     case cwReferenceNotBoundErr     case cwipcFailureErr     case cwOperationNotPermittedErr     case cwErr } ``` |

Modified [CWErr.cwapFullErr](https://developer.apple.com/documentation/corewlan/cwerr/cwapfullerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWAPFullErr ``` |
| To | ``` case cwapFullErr ``` |

Modified [CWErr.cwAssociationDeniedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwassociationdeniederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWAssociationDeniedErr ``` |
| To | ``` case cwAssociationDeniedErr ``` |

Modified [CWErr.cwAuthenticationAlgorithmUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwauthenticationalgorithmunsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWAuthenticationAlgorithmUnsupportedErr ``` |
| To | ``` case cwAuthenticationAlgorithmUnsupportedErr ``` |

Modified [CWErr.cwChallengeFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwchallengefailureerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWChallengeFailureErr ``` |
| To | ``` case cwChallengeFailureErr ``` |

Modified [CWErr.cwCipherSuiteRejectedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwciphersuiterejectederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWCipherSuiteRejectedErr ``` |
| To | ``` case cwCipherSuiteRejectedErr ``` |

Modified [CWErr.cwdsssofdmUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwdsssofdmunsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWDSSSOFDMUnsupportedErr ``` |
| To | ``` case cwdsssofdmUnsupportedErr ``` |

Modified [CWErr.cweapolErr](https://developer.apple.com/documentation/corewlan/cwerr/cweapolerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWEAPOLErr ``` |
| To | ``` case cweapolErr ``` |

Modified [CWErr.cwErr](https://developer.apple.com/documentation/corewlan/cwerr/cwerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWErr ``` |
| To | ``` case cwErr ``` |

Modified [CWErr.cwhtFeaturesNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwhtfeaturesnotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWHTFeaturesNotSupportedErr ``` |
| To | ``` case cwhtFeaturesNotSupportedErr ``` |

Modified [CWErr.cwInvalidAKMPErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidakmperr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidAKMPErr ``` |
| To | ``` case cwInvalidAKMPErr ``` |

Modified [CWErr.cwInvalidAuthenticationSequenceNumberErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidauthenticationsequencenumbererr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidAuthenticationSequenceNumberErr ``` |
| To | ``` case cwInvalidAuthenticationSequenceNumberErr ``` |

Modified [CWErr.cwInvalidFormatErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidformaterr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidFormatErr ``` |
| To | ``` case cwInvalidFormatErr ``` |

Modified [CWErr.cwInvalidGroupCipherErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidgroupciphererr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidGroupCipherErr ``` |
| To | ``` case cwInvalidGroupCipherErr ``` |

Modified [CWErr.cwInvalidInformationElementErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidinformationelementerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidInformationElementErr ``` |
| To | ``` case cwInvalidInformationElementErr ``` |

Modified [CWErr.cwInvalidPairwiseCipherErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidpairwiseciphererr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidPairwiseCipherErr ``` |
| To | ``` case cwInvalidPairwiseCipherErr ``` |

Modified [CWErr.cwInvalidParameterErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidparametererr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidParameterErr ``` |
| To | ``` case cwInvalidParameterErr ``` |

Modified [CWErr.cwInvalidPMKErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidpmkerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidPMKErr ``` |
| To | ``` case cwInvalidPMKErr ``` |

Modified [CWErr.cwInvalidRSNCapabilitiesErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidrsncapabilitieserr)

|  | Declaration |
| --- | --- |
| From | ``` case CWInvalidRSNCapabilitiesErr ``` |
| To | ``` case cwInvalidRSNCapabilitiesErr ``` |

Modified [CWErr.cwipcFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwipcfailureerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWIPCFailureErr ``` |
| To | ``` case cwipcFailureErr ``` |

Modified [CWErr.cwNoErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwnoerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWNoErr ``` |
| To | ``` case cwNoErr ``` |

Modified [CWErr.cwNoMemoryErr](https://developer.apple.com/documentation/corewlan/cwerr/cwnomemoryerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWNoMemoryErr ``` |
| To | ``` case cwNoMemoryErr ``` |

Modified [CWErr.cwNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwnotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWNotSupportedErr ``` |
| To | ``` case cwNotSupportedErr ``` |

Modified [CWErr.cwOperationNotPermittedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwoperationnotpermittederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWOperationNotPermittedErr ``` |
| To | ``` case cwOperationNotPermittedErr ``` |

Modified [CWErr.cwpcoTransitionTimeNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwpcotransitiontimenotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWPCOTransitionTimeNotSupportedErr ``` |
| To | ``` case cwpcoTransitionTimeNotSupportedErr ``` |

Modified [CWErr.cwReassociationDeniedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwreassociationdeniederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWReassociationDeniedErr ``` |
| To | ``` case cwReassociationDeniedErr ``` |

Modified [CWErr.cwReferenceNotBoundErr](https://developer.apple.com/documentation/corewlan/cwerr/cwreferencenotbounderr)

|  | Declaration |
| --- | --- |
| From | ``` case CWReferenceNotBoundErr ``` |
| To | ``` case cwReferenceNotBoundErr ``` |

Modified [CWErr.cwShortSlotUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwshortslotunsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` case CWShortSlotUnsupportedErr ``` |
| To | ``` case cwShortSlotUnsupportedErr ``` |

Modified [CWErr.cwSupplicantTimeoutErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwsupplicanttimeouterr)

|  | Declaration |
| --- | --- |
| From | ``` case CWSupplicantTimeoutErr ``` |
| To | ``` case cwSupplicantTimeoutErr ``` |

Modified [CWErr.cwTimeoutErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwtimeouterr)

|  | Declaration |
| --- | --- |
| From | ``` case CWTimeoutErr ``` |
| To | ``` case cwTimeoutErr ``` |

Modified [CWErr.cwUnknownErr](https://developer.apple.com/documentation/corewlan/cwerr/cwunknownerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWUnknownErr ``` |
| To | ``` case cwUnknownErr ``` |

Modified [CWErr.cwUnspecifiedFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/cwunspecifiedfailureerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWUnspecifiedFailureErr ``` |
| To | ``` case cwUnspecifiedFailureErr ``` |

Modified [CWErr.cwUnsupportedCapabilitiesErr](https://developer.apple.com/documentation/corewlan/cwerr/cwunsupportedcapabilitieserr)

|  | Declaration |
| --- | --- |
| From | ``` case CWUnsupportedCapabilitiesErr ``` |
| To | ``` case cwUnsupportedCapabilitiesErr ``` |

Modified [CWErr.cwUnsupportedRateSetErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwunsupportedrateseterr)

|  | Declaration |
| --- | --- |
| From | ``` case CWUnsupportedRateSetErr ``` |
| To | ``` case cwUnsupportedRateSetErr ``` |

Modified [CWErr.cwUnsupportedRSNVersionErr](https://developer.apple.com/documentation/corewlan/cwerr/cwunsupportedrsnversionerr)

|  | Declaration |
| --- | --- |
| From | ``` case CWUnsupportedRSNVersionErr ``` |
| To | ``` case cwUnsupportedRSNVersionErr ``` |

Modified [CWEventDelegate](https://developer.apple.com/documentation/corewlan/cweventdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CWEventDelegate {     optional func clientConnectionInterrupted()     optional func clientConnectionInvalidated()     optional func powerStateDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func ssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func bssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func countryCodeDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func linkDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func linkQualityDidChangeForWiFiInterfaceWithName(_ interfaceName: String, rssi rssi: Int, transmitRate transmitRate: Double)     optional func modeDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func scanCacheUpdatedForWiFiInterfaceWithName(_ interfaceName: String) } ``` |
| To | ``` protocol CWEventDelegate {     optional func clientConnectionInterrupted()     optional func clientConnectionInvalidated()     optional func powerStateDidChangeForWiFiInterface(withName interfaceName: String)     optional func ssidDidChangeForWiFiInterface(withName interfaceName: String)     optional func bssidDidChangeForWiFiInterface(withName interfaceName: String)     optional func countryCodeDidChangeForWiFiInterface(withName interfaceName: String)     optional func virtualInterfaceStateChangedForWiFiInterface(withName interfaceName: String)     optional func rangingReportEventForWiFiInterface(withName interfaceName: String, data rangingData: [Any], error err: Error)     optional func linkDidChangeForWiFiInterface(withName interfaceName: String)     optional func linkQualityDidChangeForWiFiInterface(withName interfaceName: String, rssi rssi: Int, transmitRate transmitRate: Double)     optional func modeDidChangeForWiFiInterface(withName interfaceName: String)     optional func scanCacheUpdatedForWiFiInterface(withName interfaceName: String) } ``` |

Modified [CWEventDelegate.bssidDidChangeForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512367-bssiddidchangeforwifiinterfacewi)

|  | Declaration |
| --- | --- |
| From | ``` optional func bssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func bssidDidChangeForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventDelegate.countryCodeDidChangeForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512342-countrycodedidchangeforwifiinter)

|  | Declaration |
| --- | --- |
| From | ``` optional func countryCodeDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func countryCodeDidChangeForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventDelegate.linkDidChangeForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512395-linkdidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func linkDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func linkDidChangeForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventDelegate.linkQualityDidChangeForWiFiInterface(withName: String, rssi: Int, transmitRate: Double)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512300-linkqualitydidchangeforwifiinter)

|  | Declaration |
| --- | --- |
| From | ``` optional func linkQualityDidChangeForWiFiInterfaceWithName(_ interfaceName: String, rssi rssi: Int, transmitRate transmitRate: Double) ``` |
| To | ``` optional func linkQualityDidChangeForWiFiInterface(withName interfaceName: String, rssi rssi: Int, transmitRate transmitRate: Double) ``` |

Modified [CWEventDelegate.modeDidChangeForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512226-modedidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func modeDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func modeDidChangeForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventDelegate.powerStateDidChangeForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512253-powerstatedidchangeforwifiinterf)

|  | Declaration |
| --- | --- |
| From | ``` optional func powerStateDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func powerStateDidChangeForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventDelegate.scanCacheUpdatedForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512322-scancacheupdatedforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func scanCacheUpdatedForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func scanCacheUpdatedForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventDelegate.ssidDidChangeForWiFiInterface(withName: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512422-ssiddidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func ssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |
| To | ``` optional func ssidDidChangeForWiFiInterface(withName interfaceName: String) ``` |

Modified [CWEventType [enum]](https://developer.apple.com/documentation/corewlan/cweventtype)

|  | Declaration |
| --- | --- |
| From | ``` enum CWEventType : Int {     case None     case PowerDidChange     case SSIDDidChange     case BSSIDDidChange     case CountryCodeDidChange     case LinkDidChange     case LinkQualityDidChange     case ModeDidChange     case ScanCacheUpdated     case Unknown } ``` |
| To | ``` enum CWEventType : Int {     case none     case powerDidChange     case ssidDidChange     case bssidDidChange     case countryCodeDidChange     case linkDidChange     case linkQualityDidChange     case modeDidChange     case scanCacheUpdated     case virtualInterfaceStateChanged     case rangingReportEvent     case unknown } ``` |

Modified [CWEventType.bssidDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/bssiddidchange)

|  | Declaration |
| --- | --- |
| From | ``` case BSSIDDidChange ``` |
| To | ``` case bssidDidChange ``` |

Modified [CWEventType.countryCodeDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/countrycodedidchange)

|  | Declaration |
| --- | --- |
| From | ``` case CountryCodeDidChange ``` |
| To | ``` case countryCodeDidChange ``` |

Modified [CWEventType.linkDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/linkdidchange)

|  | Declaration |
| --- | --- |
| From | ``` case LinkDidChange ``` |
| To | ``` case linkDidChange ``` |

Modified [CWEventType.linkQualityDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/linkqualitydidchange)

|  | Declaration |
| --- | --- |
| From | ``` case LinkQualityDidChange ``` |
| To | ``` case linkQualityDidChange ``` |

Modified [CWEventType.modeDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypemodedidchange)

|  | Declaration |
| --- | --- |
| From | ``` case ModeDidChange ``` |
| To | ``` case modeDidChange ``` |

Modified [CWEventType.none](https://developer.apple.com/documentation/corewlan/cweventtype/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CWEventType.powerDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/powerdidchange)

|  | Declaration |
| --- | --- |
| From | ``` case PowerDidChange ``` |
| To | ``` case powerDidChange ``` |

Modified [CWEventType.scanCacheUpdated](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypescancacheupdated)

|  | Declaration |
| --- | --- |
| From | ``` case ScanCacheUpdated ``` |
| To | ``` case scanCacheUpdated ``` |

Modified [CWEventType.ssidDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/ssiddidchange)

|  | Declaration |
| --- | --- |
| From | ``` case SSIDDidChange ``` |
| To | ``` case ssidDidChange ``` |

Modified [CWEventType.unknown](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypeunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CWIBSSModeSecurity [enum]](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity)

|  | Declaration |
| --- | --- |
| From | ``` enum CWIBSSModeSecurity : Int {     case None     case WEP40     case WEP104 } ``` |
| To | ``` enum CWIBSSModeSecurity : Int {     case none     case WEP40     case WEP104 } ``` |

Modified [CWIBSSModeSecurity.none](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity/kcwibssmodesecuritynone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CWInterface](https://developer.apple.com/documentation/corewlan/cwinterface)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CWInterface : NSObject {     var interfaceName: String? { get }     func powerOn() -> Bool     func supportedWLANChannels() -> Set<CWChannel>?     func wlanChannel() -> CWChannel?     func activePHYMode() -> CWPHYMode     func ssid() -> String?     func ssidData() -> NSData?     func bssid() -> String?     func rssiValue() -> Int     func noiseMeasurement() -> Int     func security() -> CWSecurity     func transmitRate() -> Double     func countryCode() -> String?     func interfaceMode() -> CWInterfaceMode     func transmitPower() -> Int     func hardwareAddress() -> String?     func serviceActive() -> Bool     func cachedScanResults() -> Set<CWNetwork>?     func configuration() -> CWConfiguration?     class func interfaceNames() -> Set<String>?     convenience init()     class func interface() -> Self     convenience init(name name: String)     class func interfaceWithName(_ name: String) -> Self     init(interfaceName name: String)     func setPower(_ power: Bool) throws     func setWLANChannel(_ channel: CWChannel) throws     func setPairwiseMasterKey(_ key: NSData?) throws     func setWEPKey(_ key: NSData?, flags flags: CWCipherKeyFlags, index index: Int) throws     func scanForNetworksWithSSID(_ ssid: NSData?) throws -> Set<CWNetwork>     func scanForNetworksWithName(_ networkName: String?) throws -> Set<CWNetwork>     func associateToNetwork(_ network: CWNetwork, password password: String?) throws     func disassociate()     func associateToEnterpriseNetwork(_ network: CWNetwork, identity identity: SecIdentity?, username username: String?, password password: String?) throws     func startIBSSModeWithSSID(_ ssidData: NSData, security security: CWIBSSModeSecurity, channel channel: Int, password password: String?) throws     func commitConfiguration(_ configuration: CWConfiguration, authorization authorization: SFAuthorization?) throws } ``` | -- |
| To | ``` class CWInterface : NSObject {     var interfaceName: String? { get }     func powerOn() -> Bool     func supportedWLANChannels() -> Set<CWChannel>?     func wlanChannel() -> CWChannel?     func activePHYMode() -> CWPHYMode     func ssid() -> String?     func ssidData() -> Data?     func bssid() -> String?     func rssiValue() -> Int     func noiseMeasurement() -> Int     func security() -> CWSecurity     func transmitRate() -> Double     func countryCode() -> String?     func interfaceMode() -> CWInterfaceMode     func transmitPower() -> Int     func hardwareAddress() -> String?     func serviceActive() -> Bool     func cachedScanResults() -> Set<CWNetwork>?     func configuration() -> CWConfiguration?     class func interfaceNames() -> Set<String>?     convenience init()     class func interface() -> Self     convenience init(name name: String)     class func withName(_ name: String) -> Self     init(interfaceName name: String)     func setPower(_ power: Bool) throws     func setWLANChannel(_ channel: CWChannel) throws     func setPairwiseMasterKey(_ key: Data?) throws     func setWEPKey(_ key: Data?, flags flags: CWCipherKeyFlags, index index: Int) throws     func scanForNetworks(withSSID ssid: Data?) throws -> Set<CWNetwork>     func scanForNetworks(withName networkName: String?) throws -> Set<CWNetwork>     func associate(to network: CWNetwork, password password: String?) throws     func disassociate()     func associate(toEnterpriseNetwork network: CWNetwork, identity identity: SecIdentity?, username username: String?, password password: String?) throws     func startIBSSMode(withSSID ssidData: Data, security security: CWIBSSModeSecurity, channel channel: Int, password password: String?) throws     func commitConfiguration(_ configuration: CWConfiguration, authorization authorization: SFAuthorization?) throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CWInterface : CVarArg { } extension CWInterface : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CWInterface.associate(to: CWNetwork, password: String?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426455-associatetonetwork)

|  | Declaration |
| --- | --- |
| From | ``` func associateToNetwork(_ network: CWNetwork, password password: String?) throws ``` |
| To | ``` func associate(to network: CWNetwork, password password: String?) throws ``` |

Modified [CWInterface.associate(toEnterpriseNetwork: CWNetwork, identity: SecIdentity?, username: String?, password: String?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426468-associate)

|  | Declaration |
| --- | --- |
| From | ``` func associateToEnterpriseNetwork(_ network: CWNetwork, identity identity: SecIdentity?, username username: String?, password password: String?) throws ``` |
| To | ``` func associate(toEnterpriseNetwork network: CWNetwork, identity identity: SecIdentity?, username username: String?, password password: String?) throws ``` |

Modified [CWInterface.scanForNetworks(withName: String?) throws -> Set<CWNetwork>](https://developer.apple.com/documentation/corewlan/cwinterface/1426416-scanfornetworkswithname)

|  | Declaration |
| --- | --- |
| From | ``` func scanForNetworksWithName(_ networkName: String?) throws -> Set<CWNetwork> ``` |
| To | ``` func scanForNetworks(withName networkName: String?) throws -> Set<CWNetwork> ``` |

Modified [CWInterface.scanForNetworks(withSSID: Data?) throws -> Set<CWNetwork>](https://developer.apple.com/documentation/corewlan/cwinterface/1426436-scanfornetworkswithssid)

|  | Declaration |
| --- | --- |
| From | ``` func scanForNetworksWithSSID(_ ssid: NSData?) throws -> Set<CWNetwork> ``` |
| To | ``` func scanForNetworks(withSSID ssid: Data?) throws -> Set<CWNetwork> ``` |

Modified [CWInterface.setPairwiseMasterKey(_: Data?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426458-setpairwisemasterkey)

|  | Declaration |
| --- | --- |
| From | ``` func setPairwiseMasterKey(_ key: NSData?) throws ``` |
| To | ``` func setPairwiseMasterKey(_ key: Data?) throws ``` |

Modified [CWInterface.setWEPKey(_: Data?, flags: CWCipherKeyFlags, index: Int) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426440-setwepkey)

|  | Declaration |
| --- | --- |
| From | ``` func setWEPKey(_ key: NSData?, flags flags: CWCipherKeyFlags, index index: Int) throws ``` |
| To | ``` func setWEPKey(_ key: Data?, flags flags: CWCipherKeyFlags, index index: Int) throws ``` |

Modified [CWInterface.ssidData() -> Data?](https://developer.apple.com/documentation/corewlan/cwinterface/1426434-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` func ssidData() -> NSData? ``` |
| To | ``` func ssidData() -> Data? ``` |

Modified [CWInterface.startIBSSMode(withSSID: Data, security: CWIBSSModeSecurity, channel: Int, password: String?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426417-startibssmode)

|  | Declaration |
| --- | --- |
| From | ``` func startIBSSModeWithSSID(_ ssidData: NSData, security security: CWIBSSModeSecurity, channel channel: Int, password password: String?) throws ``` |
| To | ``` func startIBSSMode(withSSID ssidData: Data, security security: CWIBSSModeSecurity, channel channel: Int, password password: String?) throws ``` |

Modified [CWInterfaceMode [enum]](https://developer.apple.com/documentation/corewlan/cwinterfacemode)

|  | Declaration |
| --- | --- |
| From | ``` enum CWInterfaceMode : Int {     case None     case Station     case IBSS     case HostAP } ``` |
| To | ``` enum CWInterfaceMode : Int {     case none     case station     case IBSS     case hostAP } ``` |

Modified [CWInterfaceMode.hostAP](https://developer.apple.com/documentation/corewlan/cwinterfacemode/hostap)

|  | Declaration |
| --- | --- |
| From | ``` case HostAP ``` |
| To | ``` case hostAP ``` |

Modified [CWInterfaceMode.none](https://developer.apple.com/documentation/corewlan/cwinterfacemode/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CWInterfaceMode.station](https://developer.apple.com/documentation/corewlan/cwinterfacemode/kcwinterfacemodestation)

|  | Declaration |
| --- | --- |
| From | ``` case Station ``` |
| To | ``` case station ``` |

Modified [CWKeychainDomain [enum]](https://developer.apple.com/documentation/corewlan/cwkeychaindomain)

|  | Declaration |
| --- | --- |
| From | ``` enum CWKeychainDomain : Int {     case None     case User     case System } ``` |
| To | ``` enum CWKeychainDomain : Int {     case none     case user     case system } ``` |

Modified [CWKeychainDomain.none](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/kcwkeychaindomainnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CWKeychainDomain.system](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/kcwkeychaindomainsystem)

|  | Declaration |
| --- | --- |
| From | ``` case System ``` |
| To | ``` case system ``` |

Modified [CWKeychainDomain.user](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/user)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [CWMutableNetworkProfile](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` class CWMutableNetworkProfile : CWNetworkProfile {     @NSCopying var ssidData: NSData     var security: CWSecurity } ``` |
| To | ``` class CWMutableNetworkProfile : CWNetworkProfile {     var ssidData: Data     var security: CWSecurity } ``` |

Modified [CWMutableNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512167-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var ssidData: NSData ``` |
| To | ``` var ssidData: Data ``` |

Modified [CWNetwork](https://developer.apple.com/documentation/corewlan/cwnetwork)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CWNetwork : NSObject, NSCopying, NSSecureCoding {     var ssid: String? { get }     var ssidData: NSData? { get }     var bssid: String? { get }     var wlanChannel: CWChannel { get }     var rssiValue: Int { get }     var noiseMeasurement: Int { get }     var informationElementData: NSData? { get }     var countryCode: String? { get }     var beaconInterval: Int { get }     var ibss: Bool { get }     func isEqualToNetwork(_ network: CWNetwork) -> Bool     func supportsSecurity(_ security: CWSecurity) -> Bool     func supportsPHYMode(_ phyMode: CWPHYMode) -> Bool } ``` | NSCopying, NSSecureCoding |
| To | ``` class CWNetwork : NSObject, NSCopying, NSSecureCoding {     var ssid: String? { get }     var ssidData: Data? { get }     var bssid: String? { get }     var wlanChannel: CWChannel { get }     var rssiValue: Int { get }     var noiseMeasurement: Int { get }     var informationElementData: Data? { get }     var countryCode: String? { get }     var beaconInterval: Int { get }     var ibss: Bool { get }     func isEqual(to network: CWNetwork) -> Bool     func supportsSecurity(_ security: CWSecurity) -> Bool     func supportsPHYMode(_ phyMode: CWPHYMode) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CWNetwork : CVarArg { } extension CWNetwork : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CWNetwork.informationElementData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512236-informationelementdata)

|  | Declaration |
| --- | --- |
| From | ``` var informationElementData: NSData? { get } ``` |
| To | ``` var informationElementData: Data? { get } ``` |

Modified [CWNetwork.isEqual(to: CWNetwork) -> Bool](https://developer.apple.com/documentation/corewlan/cwnetwork/1512228-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToNetwork(_ network: CWNetwork) -> Bool ``` |
| To | ``` func isEqual(to network: CWNetwork) -> Bool ``` |

Modified [CWNetwork.ssidData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512419-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` var ssidData: NSData? { get } ``` |
| To | ``` var ssidData: Data? { get } ``` |

Modified [CWNetworkProfile](https://developer.apple.com/documentation/corewlan/cwnetworkprofile)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CWNetworkProfile : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var ssid: String? { get }     @NSCopying var ssidData: NSData? { get }     var security: CWSecurity { get }     convenience init()     class func networkProfile() -> Self     init()     init(networkProfile networkProfile: CWNetworkProfile)     class func networkProfileWithNetworkProfile(_ networkProfile: CWNetworkProfile) -> Self     func isEqualToNetworkProfile(_ networkProfile: CWNetworkProfile) -> Bool } ``` | NSCopying, NSMutableCopying, NSSecureCoding |
| To | ``` class CWNetworkProfile : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {     var ssid: String? { get }     var ssidData: Data? { get }     var security: CWSecurity { get }     convenience init()     class func networkProfile() -> Self     init()     init(networkProfile networkProfile: CWNetworkProfile)     class func withNetworkProfile(_ networkProfile: CWNetworkProfile) -> Self     func isEqual(to networkProfile: CWNetworkProfile) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CWNetworkProfile : CVarArg { } extension CWNetworkProfile : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying, NSSecureCoding |

Modified [CWNetworkProfile.isEqual(to: CWNetworkProfile) -> Bool](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512221-isequaltonetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToNetworkProfile(_ networkProfile: CWNetworkProfile) -> Bool ``` |
| To | ``` func isEqual(to networkProfile: CWNetworkProfile) -> Bool ``` |

Modified [CWNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512244-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var ssidData: NSData? { get } ``` |
| To | ``` var ssidData: Data? { get } ``` |

Modified [CWPHYMode [enum]](https://developer.apple.com/documentation/corewlan/cwphymode)

|  | Declaration |
| --- | --- |
| From | ``` enum CWPHYMode : Int {     case ModeNone     case Mode11a     case Mode11b     case Mode11g     case Mode11n     case Mode11ac } ``` |
| To | ``` enum CWPHYMode : Int {     case modeNone     case mode11a     case mode11b     case mode11g     case mode11n     case mode11ac } ``` |

Modified [CWPHYMode.mode11a](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11a)

|  | Declaration |
| --- | --- |
| From | ``` case Mode11a ``` |
| To | ``` case mode11a ``` |

Modified [CWPHYMode.mode11ac](https://developer.apple.com/documentation/corewlan/cwphymode/mode11ac)

|  | Declaration |
| --- | --- |
| From | ``` case Mode11ac ``` |
| To | ``` case mode11ac ``` |

Modified [CWPHYMode.mode11b](https://developer.apple.com/documentation/corewlan/cwphymode/mode11b)

|  | Declaration |
| --- | --- |
| From | ``` case Mode11b ``` |
| To | ``` case mode11b ``` |

Modified [CWPHYMode.mode11g](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11g)

|  | Declaration |
| --- | --- |
| From | ``` case Mode11g ``` |
| To | ``` case mode11g ``` |

Modified [CWPHYMode.mode11n](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11n)

|  | Declaration |
| --- | --- |
| From | ``` case Mode11n ``` |
| To | ``` case mode11n ``` |

Modified [CWPHYMode.modeNone](https://developer.apple.com/documentation/corewlan/cwphymode/modenone)

|  | Declaration |
| --- | --- |
| From | ``` case ModeNone ``` |
| To | ``` case modeNone ``` |

Modified [CWSecurity [enum]](https://developer.apple.com/documentation/corewlan/cwsecurity)

|  | Declaration |
| --- | --- |
| From | ``` enum CWSecurity : Int {     case None     case WEP     case WPAPersonal     case WPAPersonalMixed     case WPA2Personal     case Personal     case DynamicWEP     case WPAEnterprise     case WPAEnterpriseMixed     case WPA2Enterprise     case Enterprise     case Unknown } ``` |
| To | ``` enum CWSecurity : Int {     case none     case WEP     case wpaPersonal     case wpaPersonalMixed     case wpa2Personal     case personal     case dynamicWEP     case wpaEnterprise     case wpaEnterpriseMixed     case wpa2Enterprise     case enterprise     case unknown } ``` |

Modified [CWSecurity.dynamicWEP](https://developer.apple.com/documentation/corewlan/cwsecurity/dynamicwep)

|  | Declaration |
| --- | --- |
| From | ``` case DynamicWEP ``` |
| To | ``` case dynamicWEP ``` |

Modified [CWSecurity.enterprise](https://developer.apple.com/documentation/corewlan/cwsecurity/enterprise)

|  | Declaration |
| --- | --- |
| From | ``` case Enterprise ``` |
| To | ``` case enterprise ``` |

Modified [CWSecurity.none](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritynone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CWSecurity.personal](https://developer.apple.com/documentation/corewlan/cwsecurity/personal)

|  | Declaration |
| --- | --- |
| From | ``` case Personal ``` |
| To | ``` case personal ``` |

Modified [CWSecurity.unknown](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecurityunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CWSecurity.wpa2Enterprise](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywpa2enterprise)

|  | Declaration |
| --- | --- |
| From | ``` case WPA2Enterprise ``` |
| To | ``` case wpa2Enterprise ``` |

Modified [CWSecurity.wpa2Personal](https://developer.apple.com/documentation/corewlan/cwsecurity/wpa2personal)

|  | Declaration |
| --- | --- |
| From | ``` case WPA2Personal ``` |
| To | ``` case wpa2Personal ``` |

Modified [CWSecurity.wpaEnterprise](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywpaenterprise)

|  | Declaration |
| --- | --- |
| From | ``` case WPAEnterprise ``` |
| To | ``` case wpaEnterprise ``` |

Modified [CWSecurity.wpaEnterpriseMixed](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywpaenterprisemixed)

|  | Declaration |
| --- | --- |
| From | ``` case WPAEnterpriseMixed ``` |
| To | ``` case wpaEnterpriseMixed ``` |

Modified [CWSecurity.wpaPersonal](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywpapersonal)

|  | Declaration |
| --- | --- |
| From | ``` case WPAPersonal ``` |
| To | ``` case wpaPersonal ``` |

Modified [CWSecurity.wpaPersonalMixed](https://developer.apple.com/documentation/corewlan/cwsecurity/wpapersonalmixed)

|  | Declaration |
| --- | --- |
| From | ``` case WPAPersonalMixed ``` |
| To | ``` case wpaPersonalMixed ``` |

Modified [CWWiFiClient](https://developer.apple.com/documentation/corewlan/cwwificlient)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CWWiFiClient : NSObject {     weak var delegate: AnyObject?     class func sharedWiFiClient() -> CWWiFiClient     init?()     func interface() -> CWInterface?     class func interfaceNames() -> [String]?     func interfaceWithName(_ interfaceName: String?) -> CWInterface?     func interfaces() -> [CWInterface]?     func startMonitoringEventWithType(_ type: CWEventType) throws     func stopMonitoringEventWithType(_ type: CWEventType) throws     func stopMonitoringAllEvents() throws } ``` | -- |
| To | ``` class CWWiFiClient : NSObject {     weak var delegate: AnyObject?     class func shared() -> CWWiFiClient     init?()     func interface() -> CWInterface?     class func interfaceNames() -> [String]?     func interface(withName interfaceName: String?) -> CWInterface?     func interfaces() -> [CWInterface]?     func startMonitoringEvent(with type: CWEventType) throws     func stopMonitoringEvent(with type: CWEventType) throws     func stopMonitoringAllEvents() throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CWWiFiClient : CVarArg { } extension CWWiFiClient : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CWWiFiClient.interface(withName: String?) -> CWInterface?](https://developer.apple.com/documentation/corewlan/cwwificlient/1512328-interfacewithname)

|  | Declaration |
| --- | --- |
| From | ``` func interfaceWithName(_ interfaceName: String?) -> CWInterface? ``` |
| To | ``` func interface(withName interfaceName: String?) -> CWInterface? ``` |

Modified [CWWiFiClient.shared() -> CWWiFiClient [class]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512202-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedWiFiClient() -> CWWiFiClient ``` |
| To | ``` class func shared() -> CWWiFiClient ``` |

Modified [CWWiFiClient.startMonitoringEvent(with: CWEventType) throws](https://developer.apple.com/documentation/corewlan/cwwificlient/1512439-startmonitoringeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` func startMonitoringEventWithType(_ type: CWEventType) throws ``` |
| To | ``` func startMonitoringEvent(with type: CWEventType) throws ``` |

Modified [CWWiFiClient.stopMonitoringEvent(with: CWEventType) throws](https://developer.apple.com/documentation/corewlan/cwwificlient/1512446-stopmonitoringevent)

|  | Declaration |
| --- | --- |
| From | ``` func stopMonitoringEventWithType(_ type: CWEventType) throws ``` |
| To | ``` func stopMonitoringEvent(with type: CWEventType) throws ``` |

Modified [NSNotification.Name.CWBSSIDDidChange](https://developer.apple.com/documentation/corewlan/cwbssiddidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWBSSIDDidChangeNotification | ``` let CWBSSIDDidChangeNotification: String ``` |
| To | CWBSSIDDidChange | ``` static let CWBSSIDDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.CWCountryCodeDidChange](https://developer.apple.com/documentation/corewlan/cwcountrycodedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWCountryCodeDidChangeNotification | ``` let CWCountryCodeDidChangeNotification: String ``` |
| To | CWCountryCodeDidChange | ``` static let CWCountryCodeDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.CWLinkDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1512162-cwlinkdidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWLinkDidChangeNotification | ``` let CWLinkDidChangeNotification: String ``` |
| To | CWLinkDidChange | ``` static let CWLinkDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.CWLinkQualityDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1512189-cwlinkqualitydidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWLinkQualityDidChangeNotification | ``` let CWLinkQualityDidChangeNotification: String ``` |
| To | CWLinkQualityDidChange | ``` static let CWLinkQualityDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.CWModeDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1512192-cwmodedidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWModeDidChangeNotification | ``` let CWModeDidChangeNotification: String ``` |
| To | CWModeDidChange | ``` static let CWModeDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.CWPowerDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1512347-cwpowerdidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWPowerDidChangeNotification | ``` let CWPowerDidChangeNotification: String ``` |
| To | CWPowerDidChange | ``` static let CWPowerDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.CWScanCacheDidUpdate](https://developer.apple.com/documentation/corewlan/cwscancachedidupdatenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWScanCacheDidUpdateNotification | ``` let CWScanCacheDidUpdateNotification: String ``` |
| To | CWScanCacheDidUpdate | ``` static let CWScanCacheDidUpdate: NSNotification.Name ``` |

Modified [NSNotification.Name.CWSSIDDidChange](https://developer.apple.com/documentation/corewlan/cwssiddidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | CWSSIDDidChangeNotification | ``` let CWSSIDDidChangeNotification: String ``` |
| To | CWSSIDDidChange | ``` static let CWSSIDDidChange: NSNotification.Name ``` |

Modified [CWKeychainCopyEAPIdentityList(_: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512258-cwkeychaincopyeapidentitylist)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainCopyEAPIdentityList(_ list: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CWKeychainCopyEAPIdentityList(_ list: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> OSStatus ``` |

Modified [CWKeychainCopyWiFiEAPIdentity(_: CWKeychainDomain, _: Data, _: UnsafeMutablePointer<Unmanaged<SecIdentity>?>?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512372-cwkeychaincopywifieapidentity)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainCopyWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData, _ identity: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` |
| To | ``` func CWKeychainCopyWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: Data, _ identity: UnsafeMutablePointer<Unmanaged<SecIdentity>?>?) -> OSStatus ``` |

Modified [CWKeychainDeleteWiFiEAPUsernameAndPassword(_: CWKeychainDomain, _: Data) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512239-cwkeychaindeletewifieapusernamea)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainDeleteWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData) -> OSStatus ``` |
| To | ``` func CWKeychainDeleteWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: Data) -> OSStatus ``` |

Modified [CWKeychainDeleteWiFiPassword(_: CWKeychainDomain, _: Data) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512242-cwkeychaindeletewifipassword)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainDeleteWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData) -> OSStatus ``` |
| To | ``` func CWKeychainDeleteWiFiPassword(_ domain: CWKeychainDomain, _ ssid: Data) -> OSStatus ``` |

Modified [CWKeychainFindWiFiEAPUsernameAndPassword(_: CWKeychainDomain, _: Data, _: AutoreleasingUnsafeMutablePointer<NSString?>?, _: AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512198-cwkeychainfindwifieapusernameand)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainFindWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ username: AutoreleasingUnsafeMutablePointer<NSString?>, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` |
| To | ``` func CWKeychainFindWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: Data, _ username: AutoreleasingUnsafeMutablePointer<NSString?>?, _ password: AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus ``` |

Modified [CWKeychainFindWiFiPassword(_: CWKeychainDomain, _: Data, _: AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512359-cwkeychainfindwifipassword)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` |
| To | ``` func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: Data, _ password: AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus ``` |

Modified [CWKeychainSetWiFiEAPIdentity(_: CWKeychainDomain, _: Data, _: SecIdentity?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512453-cwkeychainsetwifieapidentity)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainSetWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData, _ identity: SecIdentity?) -> OSStatus ``` |
| To | ``` func CWKeychainSetWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: Data, _ identity: SecIdentity?) -> OSStatus ``` |

Modified [CWKeychainSetWiFiEAPUsernameAndPassword(_: CWKeychainDomain, _: Data, _: String?, _: String?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512305-cwkeychainsetwifieapusernameandp)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainSetWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ username: String?, _ password: String?) -> OSStatus ``` |
| To | ``` func CWKeychainSetWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: Data, _ username: String?, _ password: String?) -> OSStatus ``` |

Modified [CWKeychainSetWiFiPassword(_: CWKeychainDomain, _: Data, _: String) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512429-cwkeychainsetwifipassword)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainSetWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ password: String) -> OSStatus ``` |
| To | ``` func CWKeychainSetWiFiPassword(_ domain: CWKeychainDomain, _ ssid: Data, _ password: String) -> OSStatus ``` |

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
