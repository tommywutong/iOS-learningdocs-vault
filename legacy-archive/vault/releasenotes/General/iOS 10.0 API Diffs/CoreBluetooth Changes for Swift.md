---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/CoreBluetooth.html
archived_at: '2026-07-18T02:55:11.980764Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreBluetooth Changes for Swift

### CoreBluetooth

Removed CBCentralManager.stateRemoved CBPeripheralManager.stateAdded [CBATTError [struct]](https://developer.apple.com/documentation/corebluetooth/cbatterror)Added [CBATTError.attributeNotFound](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325728-attributenotfound)Added [CBATTError.attributeNotLong](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325742-attributenotlong)Added CBATTError.init(_nsError: NSError)Added [CBATTError.insufficientAuthentication](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325721-insufficientauthentication)Added [CBATTError.insufficientAuthorization](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325726-insufficientauthorization)Added [CBATTError.insufficientEncryption](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325743-insufficientencryption)Added [CBATTError.insufficientEncryptionKeySize](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325722-insufficientencryptionkeysize)Added [CBATTError.insufficientResources](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325734-insufficientresources)Added [CBATTError.invalidAttributeValueLength](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325723-invalidattributevaluelength)Added [CBATTError.invalidHandle](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325725-invalidhandle)Added [CBATTError.invalidOffset](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325744-invalidoffset)Added [CBATTError.invalidPdu](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325731-invalidpdu)Added [CBATTError.prepareQueueFull](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325740-preparequeuefull)Added [CBATTError.readNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325732-readnotpermitted)Added [CBATTError.requestNotSupported](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325737-requestnotsupported)Added [CBATTError.success](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325733-success)Added [CBATTError.unlikelyError](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325745-unlikelyerror)Added [CBATTError.unsupportedGroupType](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325741-unsupportedgrouptype)Added [CBATTError.writeNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/2325729-writenotpermitted)Added [CBCentralManager.init()](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1648596-init)Added [CBError [struct]](https://developer.apple.com/documentation/corebluetooth/cberror)Added [CBError.alreadyAdvertising](https://developer.apple.com/documentation/corebluetooth/cberror/2325748-alreadyadvertising)Added [CBError.connectionFailed](https://developer.apple.com/documentation/corebluetooth/cberror/2335069-connectionfailed)Added [CBError.connectionLimitReached](https://developer.apple.com/documentation/corebluetooth/cberror/2335070-connectionlimitreached)Added [CBError.connectionTimeout](https://developer.apple.com/documentation/corebluetooth/cberror/2325746-connectiontimeout)Added CBError.init(_nsError: NSError)Added [CBError.invalidHandle](https://developer.apple.com/documentation/corebluetooth/cberror/2325730-invalidhandle)Added [CBError.invalidParameters](https://developer.apple.com/documentation/corebluetooth/cberror/2325749-invalidparameters)Added [CBError.notConnected](https://developer.apple.com/documentation/corebluetooth/cberror/2325736-notconnected)Added [CBError.operationCancelled](https://developer.apple.com/documentation/corebluetooth/cberror/2325735-operationcancelled)Added [CBError.outOfSpace](https://developer.apple.com/documentation/corebluetooth/cberror/2325747-outofspace)Added [CBError.peripheralDisconnected](https://developer.apple.com/documentation/corebluetooth/cberror/2325738-peripheraldisconnected)Added [CBError.unknown](https://developer.apple.com/documentation/corebluetooth/cberror/2325724-unknown)Added [CBError.uuidNotAllowed](https://developer.apple.com/documentation/corebluetooth/cberror/2325727-uuidnotallowed)Added [CBManager](https://developer.apple.com/documentation/corebluetooth/cbmanager)Added [CBManager.state](https://developer.apple.com/documentation/corebluetooth/cbmanager/1648600-state)Added [CBManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate)Added [CBManagerState.poweredOff](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/poweredoff)Added [CBManagerState.poweredOn](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/cbmanagerstatepoweredon)Added [CBManagerState.resetting](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/resetting)Added [CBManagerState.unauthorized](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/unauthorized)Added [CBManagerState.unknown](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/unknown)Added [CBManagerState.unsupported](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/unsupported)Added [CBPeripheralManager.init()](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1648153-init)Added [CBUUIDCharacteristicValidRangeString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicvalidrangestring)Modified [CBATTError.Code [enum]](https://developer.apple.com/documentation/corebluetooth/cbatterror)

|  | Declaration |
| --- | --- |
| From | ``` enum CBATTError : Int {     case Success     case InvalidHandle     case ReadNotPermitted     case WriteNotPermitted     case InvalidPdu     case InsufficientAuthentication     case RequestNotSupported     case InvalidOffset     case InsufficientAuthorization     case PrepareQueueFull     case AttributeNotFound     case AttributeNotLong     case InsufficientEncryptionKeySize     case InvalidAttributeValueLength     case UnlikelyError     case InsufficientEncryption     case UnsupportedGroupType     case InsufficientResources } extension CBATTError : _BridgedNSError { } extension CBATTError : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = CBATTError         case success         case invalidHandle         case readNotPermitted         case writeNotPermitted         case invalidPdu         case insufficientAuthentication         case requestNotSupported         case invalidOffset         case insufficientAuthorization         case prepareQueueFull         case attributeNotFound         case attributeNotLong         case insufficientEncryptionKeySize         case invalidAttributeValueLength         case unlikelyError         case insufficientEncryption         case unsupportedGroupType         case insufficientResources     } ``` |

Modified [CBATTError.Code.attributeNotFound](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorattributenotfound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case AttributeNotFound ``` | iOS 8.0 |
| To | ``` case attributeNotFound ``` | iOS 10.0 |

Modified [CBATTError.Code.attributeNotLong](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorattributenotlong)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case AttributeNotLong ``` | iOS 8.0 |
| To | ``` case attributeNotLong ``` | iOS 10.0 |

Modified [CBATTError.Code.insufficientAuthentication](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinsufficientauthentication)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientAuthentication ``` |
| To | ``` case insufficientAuthentication ``` |

Modified [CBATTError.Code.insufficientAuthorization](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinsufficientauthorization)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InsufficientAuthorization ``` | iOS 8.0 |
| To | ``` case insufficientAuthorization ``` | iOS 10.0 |

Modified [CBATTError.Code.insufficientEncryption](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinsufficientencryption)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientEncryption ``` |
| To | ``` case insufficientEncryption ``` |

Modified [CBATTError.Code.insufficientEncryptionKeySize](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientencryptionkeysize)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InsufficientEncryptionKeySize ``` | iOS 8.0 |
| To | ``` case insufficientEncryptionKeySize ``` | iOS 10.0 |

Modified [CBATTError.Code.insufficientResources](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/insufficientresources)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientResources ``` |
| To | ``` case insufficientResources ``` |

Modified [CBATTError.Code.invalidAttributeValueLength](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidattributevaluelength)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidAttributeValueLength ``` |
| To | ``` case invalidAttributeValueLength ``` |

Modified [CBATTError.Code.invalidHandle](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidhandle)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidHandle ``` |
| To | ``` case invalidHandle ``` |

Modified [CBATTError.Code.invalidOffset](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidoffset)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidOffset ``` |
| To | ``` case invalidOffset ``` |

Modified [CBATTError.Code.invalidPdu](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorinvalidpdu)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidPdu ``` |
| To | ``` case invalidPdu ``` |

Modified [CBATTError.Code.prepareQueueFull](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorpreparequeuefull)

|  | Declaration |
| --- | --- |
| From | ``` case PrepareQueueFull ``` |
| To | ``` case prepareQueueFull ``` |

Modified [CBATTError.Code.readNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorreadnotpermitted)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case ReadNotPermitted ``` | iOS 8.0 |
| To | ``` case readNotPermitted ``` | iOS 10.0 |

Modified [CBATTError.Code.requestNotSupported](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/requestnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` case RequestNotSupported ``` |
| To | ``` case requestNotSupported ``` |

Modified [CBATTError.Code.success](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [CBATTError.Code.unlikelyError](https://developer.apple.com/documentation/corebluetooth/cbatterror/cbatterrorunlikelyerror)

|  | Declaration |
| --- | --- |
| From | ``` case UnlikelyError ``` |
| To | ``` case unlikelyError ``` |

Modified [CBATTError.Code.unsupportedGroupType](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/unsupportedgrouptype)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedGroupType ``` |
| To | ``` case unsupportedGroupType ``` |

Modified [CBATTError.Code.writeNotPermitted](https://developer.apple.com/documentation/corebluetooth/cbatterror/code/writenotpermitted)

|  | Declaration |
| --- | --- |
| From | ``` case WriteNotPermitted ``` |
| To | ``` case writeNotPermitted ``` |

Modified [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CBATTRequest : NSObject {     init()     var central: CBCentral { get }     var characteristic: CBCharacteristic { get }     var offset: Int { get }     @NSCopying var value: NSData? } ``` | -- |
| To | ``` class CBATTRequest : NSObject {     init()     var central: CBCentral { get }     var characteristic: CBCharacteristic { get }     var offset: Int { get }     var value: Data?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CBATTRequest : CVarArg { } extension CBATTRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CBATTRequest.value](https://developer.apple.com/documentation/corebluetooth/cbattrequest/1518795-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: NSData? ``` |
| To | ``` var value: Data? ``` |

Modified [CBAttribute](https://developer.apple.com/documentation/corebluetooth/cbattribute)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CBAttribute : NSObject {     init()     var UUID: CBUUID { get } } ``` | -- |
| To | ``` class CBAttribute : NSObject {     init()     var uuid: CBUUID { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CBAttribute : CVarArg { } extension CBAttribute : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CBAttribute.uuid](https://developer.apple.com/documentation/corebluetooth/cbattribute/1620638-uuid)

|  | Declaration |
| --- | --- |
| From | ``` var UUID: CBUUID { get } ``` |
| To | ``` var uuid: CBUUID { get } ``` |

Modified [CBAttributePermissions [struct]](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBAttributePermissions : OptionSetType {     init(rawValue rawValue: UInt)     static var Readable: CBAttributePermissions { get }     static var Writeable: CBAttributePermissions { get }     static var ReadEncryptionRequired: CBAttributePermissions { get }     static var WriteEncryptionRequired: CBAttributePermissions { get } } ``` | OptionSetType |
| To | ``` struct CBAttributePermissions : OptionSet {     init(rawValue rawValue: UInt)     static var readable: CBAttributePermissions { get }     static var writeable: CBAttributePermissions { get }     static var readEncryptionRequired: CBAttributePermissions { get }     static var writeEncryptionRequired: CBAttributePermissions { get }     func intersect(_ other: CBAttributePermissions) -> CBAttributePermissions     func exclusiveOr(_ other: CBAttributePermissions) -> CBAttributePermissions     mutating func unionInPlace(_ other: CBAttributePermissions)     mutating func intersectInPlace(_ other: CBAttributePermissions)     mutating func exclusiveOrInPlace(_ other: CBAttributePermissions)     func isSubsetOf(_ other: CBAttributePermissions) -> Bool     func isDisjointWith(_ other: CBAttributePermissions) -> Bool     func isSupersetOf(_ other: CBAttributePermissions) -> Bool     mutating func subtractInPlace(_ other: CBAttributePermissions)     func isStrictSupersetOf(_ other: CBAttributePermissions) -> Bool     func isStrictSubsetOf(_ other: CBAttributePermissions) -> Bool } extension CBAttributePermissions {     func union(_ other: CBAttributePermissions) -> CBAttributePermissions     func intersection(_ other: CBAttributePermissions) -> CBAttributePermissions     func symmetricDifference(_ other: CBAttributePermissions) -> CBAttributePermissions } extension CBAttributePermissions {     func contains(_ member: CBAttributePermissions) -> Bool     mutating func insert(_ newMember: CBAttributePermissions) -> (inserted: Bool, memberAfterInsert: CBAttributePermissions)     mutating func remove(_ member: CBAttributePermissions) -> CBAttributePermissions?     mutating func update(with newMember: CBAttributePermissions) -> CBAttributePermissions? } extension CBAttributePermissions {     convenience init()     mutating func formUnion(_ other: CBAttributePermissions)     mutating func formIntersection(_ other: CBAttributePermissions)     mutating func formSymmetricDifference(_ other: CBAttributePermissions) } extension CBAttributePermissions {     convenience init<S : Sequence where S.Iterator.Element == CBAttributePermissions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CBAttributePermissions...)     mutating func subtract(_ other: CBAttributePermissions)     func isSubset(of other: CBAttributePermissions) -> Bool     func isSuperset(of other: CBAttributePermissions) -> Bool     func isDisjoint(with other: CBAttributePermissions) -> Bool     func subtracting(_ other: CBAttributePermissions) -> CBAttributePermissions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CBAttributePermissions) -> Bool     func isStrictSubset(of other: CBAttributePermissions) -> Bool } ``` | OptionSet |

Modified [CBAttributePermissions.readable](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/cbattributepermissionsreadable)

|  | Declaration |
| --- | --- |
| From | ``` static var Readable: CBAttributePermissions { get } ``` |
| To | ``` static var readable: CBAttributePermissions { get } ``` |

Modified [CBAttributePermissions.readEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/1518779-readencryptionrequired)

|  | Declaration |
| --- | --- |
| From | ``` static var ReadEncryptionRequired: CBAttributePermissions { get } ``` |
| To | ``` static var readEncryptionRequired: CBAttributePermissions { get } ``` |

Modified [CBAttributePermissions.writeable](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/1519119-writeable)

|  | Declaration |
| --- | --- |
| From | ``` static var Writeable: CBAttributePermissions { get } ``` |
| To | ``` static var writeable: CBAttributePermissions { get } ``` |

Modified [CBAttributePermissions.writeEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions/cbattributepermissionswriteencryptionrequired)

|  | Declaration |
| --- | --- |
| From | ``` static var WriteEncryptionRequired: CBAttributePermissions { get } ``` |
| To | ``` static var writeEncryptionRequired: CBAttributePermissions { get } ``` |

Modified [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager)

|  | Declaration | Superclasses |
| --- | --- | --- |
| From | ``` class CBCentralManager : NSObject {     unowned(unsafe) var delegate: CBCentralManagerDelegate?     var state: CBCentralManagerState { get }     var isScanning: Bool { get }     convenience init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?)     init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?)     func retrievePeripheralsWithIdentifiers(_ identifiers: [NSUUID]) -> [CBPeripheral]     func retrieveConnectedPeripheralsWithServices(_ serviceUUIDs: [CBUUID]) -> [CBPeripheral]     func scanForPeripheralsWithServices(_ serviceUUIDs: [CBUUID]?, options options: [String : AnyObject]?)     func stopScan()     func connectPeripheral(_ peripheral: CBPeripheral, options options: [String : AnyObject]?)     func cancelPeripheralConnection(_ peripheral: CBPeripheral) } ``` | NSObject |
| To | ``` class CBCentralManager : CBManager {     weak var delegate: CBCentralManagerDelegate?     var isScanning: Bool { get }     convenience init()     convenience init(delegate delegate: CBCentralManagerDelegate?, queue queue: DispatchQueue?)     init(delegate delegate: CBCentralManagerDelegate?, queue queue: DispatchQueue?, options options: [String : Any]? = nil)     func retrievePeripherals(withIdentifiers identifiers: [UUID]) -> [CBPeripheral]     func retrieveConnectedPeripherals(withServices serviceUUIDs: [CBUUID]) -> [CBPeripheral]     func scanForPeripherals(withServices serviceUUIDs: [CBUUID]?, options options: [String : Any]? = nil)     func stopScan()     func connect(_ peripheral: CBPeripheral, options options: [String : Any]? = nil)     func cancelPeripheralConnection(_ peripheral: CBPeripheral) } ``` | CBManager |

Modified [CBCentralManager.connect(_: CBPeripheral, options: [String : Any]?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518766-connect)

|  | Declaration |
| --- | --- |
| From | ``` func connectPeripheral(_ peripheral: CBPeripheral, options options: [String : AnyObject]?) ``` |
| To | ``` func connect(_ peripheral: CBPeripheral, options options: [String : Any]? = nil) ``` |

Modified [CBCentralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518944-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: CBCentralManagerDelegate? ``` |
| To | ``` weak var delegate: CBCentralManagerDelegate? ``` |

Modified [CBCentralManager.init(delegate: CBCentralManagerDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518695-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?) ``` |
| To | ``` convenience init(delegate delegate: CBCentralManagerDelegate?, queue queue: DispatchQueue?) ``` |

Modified [CBCentralManager.init(delegate: CBCentralManagerDelegate?, queue: DispatchQueue?, options: [String : Any]?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519001-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: CBCentralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?) ``` |
| To | ``` init(delegate delegate: CBCentralManagerDelegate?, queue queue: DispatchQueue?, options options: [String : Any]? = nil) ``` |

Modified [CBCentralManager.retrieveConnectedPeripherals(withServices: [CBUUID]) -> [CBPeripheral]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518924-retrieveconnectedperipheralswith)

|  | Declaration |
| --- | --- |
| From | ``` func retrieveConnectedPeripheralsWithServices(_ serviceUUIDs: [CBUUID]) -> [CBPeripheral] ``` |
| To | ``` func retrieveConnectedPeripherals(withServices serviceUUIDs: [CBUUID]) -> [CBPeripheral] ``` |

Modified [CBCentralManager.retrievePeripherals(withIdentifiers: [UUID]) -> [CBPeripheral]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1519127-retrieveperipheralswithidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func retrievePeripheralsWithIdentifiers(_ identifiers: [NSUUID]) -> [CBPeripheral] ``` |
| To | ``` func retrievePeripherals(withIdentifiers identifiers: [UUID]) -> [CBPeripheral] ``` |

Modified [CBCentralManager.scanForPeripherals(withServices: [CBUUID]?, options: [String : Any]?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/1518986-scanforperipheralswithservices)

|  | Declaration |
| --- | --- |
| From | ``` func scanForPeripheralsWithServices(_ serviceUUIDs: [CBUUID]?, options options: [String : AnyObject]?) ``` |
| To | ``` func scanForPeripherals(withServices serviceUUIDs: [CBUUID]?, options options: [String : Any]? = nil) ``` |

Modified [CBCentralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CBCentralManagerDelegate : NSObjectProtocol {     func centralManagerDidUpdateState(_ central: CBCentralManager)     optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : AnyObject])     optional func centralManager(_ central: CBCentralManager, didDiscoverPeripheral peripheral: CBPeripheral, advertisementData advertisementData: [String : AnyObject], RSSI RSSI: NSNumber)     optional func centralManager(_ central: CBCentralManager, didConnectPeripheral peripheral: CBPeripheral)     optional func centralManager(_ central: CBCentralManager, didFailToConnectPeripheral peripheral: CBPeripheral, error error: NSError?)     optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error error: NSError?) } ``` |
| To | ``` protocol CBCentralManagerDelegate : NSObjectProtocol {     func centralManagerDidUpdateState(_ central: CBCentralManager)     optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : Any])     optional func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData advertisementData: [String : Any], rssi RSSI: NSNumber)     optional func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral)     optional func centralManager(_ central: CBCentralManager, didFailToConnect peripheral: CBPeripheral, error error: Error?)     optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error error: Error?) } ``` |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didConnect: CBPeripheral)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518969-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager, didConnectPeripheral peripheral: CBPeripheral) ``` |
| To | ``` optional func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) ``` |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didDisconnectPeripheral: CBPeripheral, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518791-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error error: NSError?) ``` |
| To | ``` optional func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error error: Error?) ``` |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didDiscover: CBPeripheral, advertisementData: [String : Any], rssi: NSNumber)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518937-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager, didDiscoverPeripheral peripheral: CBPeripheral, advertisementData advertisementData: [String : AnyObject], RSSI RSSI: NSNumber) ``` |
| To | ``` optional func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData advertisementData: [String : Any], rssi RSSI: NSNumber) ``` |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, didFailToConnect: CBPeripheral, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518988-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager, didFailToConnectPeripheral peripheral: CBPeripheral, error error: NSError?) ``` |
| To | ``` optional func centralManager(_ central: CBCentralManager, didFailToConnect peripheral: CBPeripheral, error error: Error?) ``` |

Modified [CBCentralManagerDelegate.centralManager(_: CBCentralManager, willRestoreState: [String : Any])](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/1518819-centralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : AnyObject]) ``` |
| To | ``` optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : Any]) ``` |

Modified [CBCentralManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` enum CBCentralManagerState : Int {     case Unknown     case Resetting     case Unsupported     case Unauthorized     case PoweredOff     case PoweredOn } ``` | iOS 8.1 | -- |
| To | ``` enum CBCentralManagerState : Int {     case unknown     case resetting     case unsupported     case unauthorized     case poweredOff     case poweredOn } ``` | iOS 5.0 | iOS 10.0 |

Modified [CBCentralManagerState.poweredOff](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstatepoweredoff)

|  | Declaration |
| --- | --- |
| From | ``` case PoweredOff ``` |
| To | ``` case poweredOff ``` |

Modified [CBCentralManagerState.poweredOn](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/poweredon)

|  | Declaration |
| --- | --- |
| From | ``` case PoweredOn ``` |
| To | ``` case poweredOn ``` |

Modified [CBCentralManagerState.resetting](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/resetting)

|  | Declaration |
| --- | --- |
| From | ``` case Resetting ``` |
| To | ``` case resetting ``` |

Modified [CBCentralManagerState.unauthorized](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/cbcentralmanagerstateunauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case Unauthorized ``` |
| To | ``` case unauthorized ``` |

Modified [CBCentralManagerState.unknown](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CBCentralManagerState.unsupported](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unsupported)

|  | Declaration |
| --- | --- |
| From | ``` case Unsupported ``` |
| To | ``` case unsupported ``` |

Modified [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` class CBCharacteristic : CBAttribute {     unowned(unsafe) var service: CBService { get }     var properties: CBCharacteristicProperties { get }     var value: NSData? { get }     var descriptors: [CBDescriptor]? { get }     var isBroadcasted: Bool { get }     var isNotifying: Bool { get } } ``` |
| To | ``` class CBCharacteristic : CBAttribute {     unowned(unsafe) var service: CBService { get }     var properties: CBCharacteristicProperties { get }     var value: Data? { get }     var descriptors: [CBDescriptor]? { get }     var isBroadcasted: Bool { get }     var isNotifying: Bool { get } } ``` |

Modified [CBCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic/1518878-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: NSData? { get } ``` |
| To | ``` var value: Data? { get } ``` |

Modified [CBCharacteristicProperties [struct]](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBCharacteristicProperties : OptionSetType {     init(rawValue rawValue: UInt)     static var Broadcast: CBCharacteristicProperties { get }     static var Read: CBCharacteristicProperties { get }     static var WriteWithoutResponse: CBCharacteristicProperties { get }     static var Write: CBCharacteristicProperties { get }     static var Notify: CBCharacteristicProperties { get }     static var Indicate: CBCharacteristicProperties { get }     static var AuthenticatedSignedWrites: CBCharacteristicProperties { get }     static var ExtendedProperties: CBCharacteristicProperties { get }     static var NotifyEncryptionRequired: CBCharacteristicProperties { get }     static var IndicateEncryptionRequired: CBCharacteristicProperties { get } } ``` | OptionSetType |
| To | ``` struct CBCharacteristicProperties : OptionSet {     init(rawValue rawValue: UInt)     static var broadcast: CBCharacteristicProperties { get }     static var read: CBCharacteristicProperties { get }     static var writeWithoutResponse: CBCharacteristicProperties { get }     static var write: CBCharacteristicProperties { get }     static var notify: CBCharacteristicProperties { get }     static var indicate: CBCharacteristicProperties { get }     static var authenticatedSignedWrites: CBCharacteristicProperties { get }     static var extendedProperties: CBCharacteristicProperties { get }     static var notifyEncryptionRequired: CBCharacteristicProperties { get }     static var indicateEncryptionRequired: CBCharacteristicProperties { get }     func intersect(_ other: CBCharacteristicProperties) -> CBCharacteristicProperties     func exclusiveOr(_ other: CBCharacteristicProperties) -> CBCharacteristicProperties     mutating func unionInPlace(_ other: CBCharacteristicProperties)     mutating func intersectInPlace(_ other: CBCharacteristicProperties)     mutating func exclusiveOrInPlace(_ other: CBCharacteristicProperties)     func isSubsetOf(_ other: CBCharacteristicProperties) -> Bool     func isDisjointWith(_ other: CBCharacteristicProperties) -> Bool     func isSupersetOf(_ other: CBCharacteristicProperties) -> Bool     mutating func subtractInPlace(_ other: CBCharacteristicProperties)     func isStrictSupersetOf(_ other: CBCharacteristicProperties) -> Bool     func isStrictSubsetOf(_ other: CBCharacteristicProperties) -> Bool } extension CBCharacteristicProperties {     func union(_ other: CBCharacteristicProperties) -> CBCharacteristicProperties     func intersection(_ other: CBCharacteristicProperties) -> CBCharacteristicProperties     func symmetricDifference(_ other: CBCharacteristicProperties) -> CBCharacteristicProperties } extension CBCharacteristicProperties {     func contains(_ member: CBCharacteristicProperties) -> Bool     mutating func insert(_ newMember: CBCharacteristicProperties) -> (inserted: Bool, memberAfterInsert: CBCharacteristicProperties)     mutating func remove(_ member: CBCharacteristicProperties) -> CBCharacteristicProperties?     mutating func update(with newMember: CBCharacteristicProperties) -> CBCharacteristicProperties? } extension CBCharacteristicProperties {     convenience init()     mutating func formUnion(_ other: CBCharacteristicProperties)     mutating func formIntersection(_ other: CBCharacteristicProperties)     mutating func formSymmetricDifference(_ other: CBCharacteristicProperties) } extension CBCharacteristicProperties {     convenience init<S : Sequence where S.Iterator.Element == CBCharacteristicProperties>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CBCharacteristicProperties...)     mutating func subtract(_ other: CBCharacteristicProperties)     func isSubset(of other: CBCharacteristicProperties) -> Bool     func isSuperset(of other: CBCharacteristicProperties) -> Bool     func isDisjoint(with other: CBCharacteristicProperties) -> Bool     func subtracting(_ other: CBCharacteristicProperties) -> CBCharacteristicProperties     var isEmpty: Bool { get }     func isStrictSuperset(of other: CBCharacteristicProperties) -> Bool     func isStrictSubset(of other: CBCharacteristicProperties) -> Bool } ``` | OptionSet |

Modified [CBCharacteristicProperties.authenticatedSignedWrites](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyauthenticatedsignedwrites)

|  | Declaration |
| --- | --- |
| From | ``` static var AuthenticatedSignedWrites: CBCharacteristicProperties { get } ``` |
| To | ``` static var authenticatedSignedWrites: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.broadcast](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertybroadcast)

|  | Declaration |
| --- | --- |
| From | ``` static var Broadcast: CBCharacteristicProperties { get } ``` |
| To | ``` static var broadcast: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.extendedProperties](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyextendedproperties)

|  | Declaration |
| --- | --- |
| From | ``` static var ExtendedProperties: CBCharacteristicProperties { get } ``` |
| To | ``` static var extendedProperties: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.indicate](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1519085-indicate)

|  | Declaration |
| --- | --- |
| From | ``` static var Indicate: CBCharacteristicProperties { get } ``` |
| To | ``` static var indicate: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.indicateEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518893-indicateencryptionrequired)

|  | Declaration |
| --- | --- |
| From | ``` static var IndicateEncryptionRequired: CBCharacteristicProperties { get } ``` |
| To | ``` static var indicateEncryptionRequired: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.notify](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertynotify)

|  | Declaration |
| --- | --- |
| From | ``` static var Notify: CBCharacteristicProperties { get } ``` |
| To | ``` static var notify: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.notifyEncryptionRequired](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertynotifyencryptionrequired)

|  | Declaration |
| --- | --- |
| From | ``` static var NotifyEncryptionRequired: CBCharacteristicProperties { get } ``` |
| To | ``` static var notifyEncryptionRequired: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.read](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/cbcharacteristicpropertyread)

|  | Declaration |
| --- | --- |
| From | ``` static var Read: CBCharacteristicProperties { get } ``` |
| To | ``` static var read: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.write](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1519089-write)

|  | Declaration |
| --- | --- |
| From | ``` static var Write: CBCharacteristicProperties { get } ``` |
| To | ``` static var write: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicProperties.writeWithoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicproperties/1518734-writewithoutresponse)

|  | Declaration |
| --- | --- |
| From | ``` static var WriteWithoutResponse: CBCharacteristicProperties { get } ``` |
| To | ``` static var writeWithoutResponse: CBCharacteristicProperties { get } ``` |

Modified [CBCharacteristicWriteType [enum]](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype)

|  | Declaration |
| --- | --- |
| From | ``` enum CBCharacteristicWriteType : Int {     case WithResponse     case WithoutResponse } ``` |
| To | ``` enum CBCharacteristicWriteType : Int {     case withResponse     case withoutResponse } ``` |

Modified [CBCharacteristicWriteType.withoutResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/withoutresponse)

|  | Declaration |
| --- | --- |
| From | ``` case WithoutResponse ``` |
| To | ``` case withoutResponse ``` |

Modified [CBCharacteristicWriteType.withResponse](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype/withresponse)

|  | Declaration |
| --- | --- |
| From | ``` case WithResponse ``` |
| To | ``` case withResponse ``` |

Modified [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class CBDescriptor : CBAttribute {     unowned(unsafe) var characteristic: CBCharacteristic { get }     var value: AnyObject? { get } } ``` |
| To | ``` class CBDescriptor : CBAttribute {     unowned(unsafe) var characteristic: CBCharacteristic { get }     var value: Any? { get } } ``` |

Modified [CBDescriptor.value](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/1518778-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: AnyObject? { get } ``` |
| To | ``` var value: Any? { get } ``` |

Modified [CBError.Code [enum]](https://developer.apple.com/documentation/corebluetooth/cberror)

|  | Declaration |
| --- | --- |
| From | ``` enum CBError : Int {     case Unknown     case InvalidParameters     case InvalidHandle     case NotConnected     case OutOfSpace     case OperationCancelled     case ConnectionTimeout     case PeripheralDisconnected     case UUIDNotAllowed     case AlreadyAdvertising     case ConnectionFailed     case ConnectionLimitReached } extension CBError : _BridgedNSError { } extension CBError : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = CBError         case unknown         case invalidParameters         case invalidHandle         case notConnected         case outOfSpace         case operationCancelled         case connectionTimeout         case peripheralDisconnected         case uuidNotAllowed         case alreadyAdvertising         case connectionFailed         case connectionLimitReached     } ``` |

Modified [CBError.Code.alreadyAdvertising](https://developer.apple.com/documentation/corebluetooth/cberror/cberroralreadyadvertising)

|  | Declaration |
| --- | --- |
| From | ``` case AlreadyAdvertising ``` |
| To | ``` case alreadyAdvertising ``` |

Modified [CBError.Code.connectionFailed](https://developer.apple.com/documentation/corebluetooth/cberror/code/connectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionFailed ``` |
| To | ``` case connectionFailed ``` |

Modified [CBError.Code.connectionLimitReached](https://developer.apple.com/documentation/corebluetooth/cberror/code/connectionlimitreached)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionLimitReached ``` |
| To | ``` case connectionLimitReached ``` |

Modified [CBError.Code.connectionTimeout](https://developer.apple.com/documentation/corebluetooth/cberror/cberrorconnectiontimeout)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionTimeout ``` |
| To | ``` case connectionTimeout ``` |

Modified [CBError.Code.invalidHandle](https://developer.apple.com/documentation/corebluetooth/cberror/code/invalidhandle)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidHandle ``` |
| To | ``` case invalidHandle ``` |

Modified [CBError.Code.invalidParameters](https://developer.apple.com/documentation/corebluetooth/cberror/code/invalidparameters)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidParameters ``` |
| To | ``` case invalidParameters ``` |

Modified [CBError.Code.notConnected](https://developer.apple.com/documentation/corebluetooth/cberror/code/notconnected)

|  | Declaration |
| --- | --- |
| From | ``` case NotConnected ``` |
| To | ``` case notConnected ``` |

Modified [CBError.Code.operationCancelled](https://developer.apple.com/documentation/corebluetooth/cberror/cberroroperationcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case OperationCancelled ``` |
| To | ``` case operationCancelled ``` |

Modified [CBError.Code.outOfSpace](https://developer.apple.com/documentation/corebluetooth/cberror/cberroroutofspace)

|  | Declaration |
| --- | --- |
| From | ``` case OutOfSpace ``` |
| To | ``` case outOfSpace ``` |

Modified [CBError.Code.peripheralDisconnected](https://developer.apple.com/documentation/corebluetooth/cberror/cberrorperipheraldisconnected)

|  | Declaration |
| --- | --- |
| From | ``` case PeripheralDisconnected ``` |
| To | ``` case peripheralDisconnected ``` |

Modified [CBError.Code.unknown](https://developer.apple.com/documentation/corebluetooth/cberror/code/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CBError.Code.uuidNotAllowed](https://developer.apple.com/documentation/corebluetooth/cberror/cberroruuidnotallowed)

|  | Declaration |
| --- | --- |
| From | ``` case UUIDNotAllowed ``` |
| To | ``` case uuidNotAllowed ``` |

Modified [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` class CBMutableCharacteristic : CBCharacteristic {     var permissions: CBAttributePermissions     var subscribedCentrals: [CBCentral]? { get }     var properties: CBCharacteristicProperties     var value: NSData?     var descriptors: [CBDescriptor]?     init(type UUID: CBUUID, properties properties: CBCharacteristicProperties, value value: NSData?, permissions permissions: CBAttributePermissions) } ``` |
| To | ``` class CBMutableCharacteristic : CBCharacteristic {     var permissions: CBAttributePermissions     var subscribedCentrals: [CBCentral]? { get }     var properties: CBCharacteristicProperties     var value: Data?     var descriptors: [CBDescriptor]?     init(type UUID: CBUUID, properties properties: CBCharacteristicProperties, value value: Data?, permissions permissions: CBAttributePermissions) } ``` |

Modified [CBMutableCharacteristic.init(type: CBUUID, properties: CBCharacteristicProperties, value: Data?, permissions: CBAttributePermissions)](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519073-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID, properties properties: CBCharacteristicProperties, value value: NSData?, permissions permissions: CBAttributePermissions) ``` |
| To | ``` init(type UUID: CBUUID, properties properties: CBCharacteristicProperties, value value: Data?, permissions permissions: CBAttributePermissions) ``` |

Modified [CBMutableCharacteristic.value](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/1519121-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: NSData? ``` |
| To | ``` var value: Data? ``` |

Modified [CBMutableDescriptor](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class CBMutableDescriptor : CBDescriptor {     init(type UUID: CBUUID, value value: AnyObject?) } ``` |
| To | ``` class CBMutableDescriptor : CBDescriptor {     init(type UUID: CBUUID, value value: Any?) } ``` |

Modified [CBMutableDescriptor.init(type: CBUUID, value: Any?)](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor/1518999-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init(type UUID: CBUUID, value value: AnyObject?) ``` |
| To | ``` init(type UUID: CBUUID, value value: Any?) ``` |

Modified [CBPeer](https://developer.apple.com/documentation/corebluetooth/cbpeer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CBPeer : NSObject, NSCopying {     init()     var identifier: NSUUID { get } } ``` | NSCopying |
| To | ``` class CBPeer : NSObject, NSCopying {     init()     var identifier: UUID { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CBPeer : CVarArg { } extension CBPeer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [CBPeer.identifier](https://developer.apple.com/documentation/corebluetooth/cbpeer/1620687-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: NSUUID { get } ``` |
| To | ``` var identifier: UUID { get } ``` |

Modified [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral)

|  | Declaration |
| --- | --- |
| From | ``` class CBPeripheral : CBPeer {     unowned(unsafe) var delegate: CBPeripheralDelegate?     var name: String? { get }     var RSSI: NSNumber? { get }     var state: CBPeripheralState { get }     var services: [CBService]? { get }     func readRSSI()     func discoverServices(_ serviceUUIDs: [CBUUID]?)     func discoverIncludedServices(_ includedServiceUUIDs: [CBUUID]?, forService service: CBService)     func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, forService service: CBService)     func readValueForCharacteristic(_ characteristic: CBCharacteristic)     func maximumWriteValueLengthForType(_ type: CBCharacteristicWriteType) -> Int     func writeValue(_ data: NSData, forCharacteristic characteristic: CBCharacteristic, type type: CBCharacteristicWriteType)     func setNotifyValue(_ enabled: Bool, forCharacteristic characteristic: CBCharacteristic)     func discoverDescriptorsForCharacteristic(_ characteristic: CBCharacteristic)     func readValueForDescriptor(_ descriptor: CBDescriptor)     func writeValue(_ data: NSData, forDescriptor descriptor: CBDescriptor) } ``` |
| To | ``` class CBPeripheral : CBPeer {     weak var delegate: CBPeripheralDelegate?     var name: String? { get }     var rssi: NSNumber? { get }     var state: CBPeripheralState { get }     var services: [CBService]? { get }     func readRSSI()     func discoverServices(_ serviceUUIDs: [CBUUID]?)     func discoverIncludedServices(_ includedServiceUUIDs: [CBUUID]?, for service: CBService)     func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, for service: CBService)     func readValue(for characteristic: CBCharacteristic)     func maximumWriteValueLength(for type: CBCharacteristicWriteType) -> Int     func writeValue(_ data: Data, for characteristic: CBCharacteristic, type type: CBCharacteristicWriteType)     func setNotifyValue(_ enabled: Bool, for characteristic: CBCharacteristic)     func discoverDescriptors(for characteristic: CBCharacteristic)     func readValue(for descriptor: CBDescriptor)     func writeValue(_ data: Data, for descriptor: CBDescriptor) } ``` |

Modified [CBPeripheral.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518730-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: CBPeripheralDelegate? ``` |
| To | ``` weak var delegate: CBPeripheralDelegate? ``` |

Modified [CBPeripheral.discoverCharacteristics(_: [CBUUID]?, for: CBService)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518797-discovercharacteristics)

|  | Declaration |
| --- | --- |
| From | ``` func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, forService service: CBService) ``` |
| To | ``` func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, for service: CBService) ``` |

Modified [CBPeripheral.discoverDescriptors(for: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519070-discoverdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` func discoverDescriptorsForCharacteristic(_ characteristic: CBCharacteristic) ``` |
| To | ``` func discoverDescriptors(for characteristic: CBCharacteristic) ``` |

Modified [CBPeripheral.discoverIncludedServices(_: [CBUUID]?, for: CBService)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519014-discoverincludedservices)

|  | Declaration |
| --- | --- |
| From | ``` func discoverIncludedServices(_ includedServiceUUIDs: [CBUUID]?, forService service: CBService) ``` |
| To | ``` func discoverIncludedServices(_ includedServiceUUIDs: [CBUUID]?, for service: CBService) ``` |

Modified [CBPeripheral.maximumWriteValueLength(for: CBCharacteristicWriteType) -> Int](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1620312-maximumwritevaluelengthfortype)

|  | Declaration |
| --- | --- |
| From | ``` func maximumWriteValueLengthForType(_ type: CBCharacteristicWriteType) -> Int ``` |
| To | ``` func maximumWriteValueLength(for type: CBCharacteristicWriteType) -> Int ``` |

Modified [CBPeripheral.readValue(for: CBDescriptor)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518789-readvaluefordescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func readValueForDescriptor(_ descriptor: CBDescriptor) ``` |
| To | ``` func readValue(for descriptor: CBDescriptor) ``` |

Modified [CBPeripheral.readValue(for: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518759-readvalueforcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` func readValueForCharacteristic(_ characteristic: CBCharacteristic) ``` |
| To | ``` func readValue(for characteristic: CBCharacteristic) ``` |

Modified [CBPeripheral.rssi](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518869-rssi)

|  | Declaration |
| --- | --- |
| From | ``` var RSSI: NSNumber? { get } ``` |
| To | ``` var rssi: NSNumber? { get } ``` |

Modified [CBPeripheral.setNotifyValue(_: Bool, for: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518949-setnotifyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setNotifyValue(_ enabled: Bool, forCharacteristic characteristic: CBCharacteristic) ``` |
| To | ``` func setNotifyValue(_ enabled: Bool, for characteristic: CBCharacteristic) ``` |

Modified [CBPeripheral.writeValue(_: Data, for: CBDescriptor)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1519107-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` func writeValue(_ data: NSData, forDescriptor descriptor: CBDescriptor) ``` |
| To | ``` func writeValue(_ data: Data, for descriptor: CBDescriptor) ``` |

Modified [CBPeripheral.writeValue(_: Data, for: CBCharacteristic, type: CBCharacteristicWriteType)](https://developer.apple.com/documentation/corebluetooth/cbperipheral/1518747-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` func writeValue(_ data: NSData, forCharacteristic characteristic: CBCharacteristic, type type: CBCharacteristicWriteType) ``` |
| To | ``` func writeValue(_ data: Data, for characteristic: CBCharacteristic, type type: CBCharacteristicWriteType) ``` |

Modified [CBPeripheralDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CBPeripheralDelegate : NSObjectProtocol {     optional func peripheralDidUpdateName(_ peripheral: CBPeripheral)     optional func peripheral(_ peripheral: CBPeripheral, didModifyServices invalidatedServices: [CBService])     optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesForService service: CBService, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsForService service: CBService, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsForCharacteristic characteristic: CBCharacteristic, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForDescriptor descriptor: CBDescriptor, error error: NSError?)     optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForDescriptor descriptor: CBDescriptor, error error: NSError?) } ``` |
| To | ``` protocol CBPeripheralDelegate : NSObjectProtocol {     optional func peripheralDidUpdateName(_ peripheral: CBPeripheral)     optional func peripheral(_ peripheral: CBPeripheral, didModifyServices invalidatedServices: [CBService])     optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesFor service: CBService, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didWriteValueFor characteristic: CBCharacteristic, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateFor characteristic: CBCharacteristic, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsFor characteristic: CBCharacteristic, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor descriptor: CBDescriptor, error error: Error?)     optional func peripheral(_ peripheral: CBPeripheral, didWriteValueFor descriptor: CBDescriptor, error error: Error?) } ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverCharacteristicsFor: CBService, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518821-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsForService service: CBService, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverDescriptorsFor: CBCharacteristic, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518785-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsFor characteristic: CBCharacteristic, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverIncludedServicesFor: CBService, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519124-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesForService service: CBService, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesFor service: CBService, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didDiscoverServices: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518744-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didReadRSSI: NSNumber, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1620304-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didUpdateNotificationStateFor: CBCharacteristic, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518768-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateFor characteristic: CBCharacteristic, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didUpdateValueFor: CBDescriptor, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518929-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForDescriptor descriptor: CBDescriptor, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor descriptor: CBDescriptor, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didUpdateValueFor: CBCharacteristic, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518708-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didWriteValueFor: CBDescriptor, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519062-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForDescriptor descriptor: CBDescriptor, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didWriteValueFor descriptor: CBDescriptor, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheral(_: CBPeripheral, didWriteValueFor: CBCharacteristic, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1518823-peripheral)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheral(_ peripheral: CBPeripheral, didWriteValueForCharacteristic characteristic: CBCharacteristic, error error: NSError?) ``` |
| To | ``` optional func peripheral(_ peripheral: CBPeripheral, didWriteValueFor characteristic: CBCharacteristic, error error: Error?) ``` |

Modified [CBPeripheralDelegate.peripheralDidUpdateRSSI(_: CBPeripheral, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/1519083-peripheraldidupdaterssi)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error error: NSError?) ``` |
| To | ``` optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error error: Error?) ``` |

Modified [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager)

|  | Declaration | Superclasses |
| --- | --- | --- |
| From | ``` class CBPeripheralManager : NSObject {     unowned(unsafe) var delegate: CBPeripheralManagerDelegate?     var state: CBPeripheralManagerState { get }     var isAdvertising: Bool { get }     class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus     convenience init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?)     init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?)     func startAdvertising(_ advertisementData: [String : AnyObject]?)     func stopAdvertising()     func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, forCentral central: CBCentral)     func addService(_ service: CBMutableService)     func removeService(_ service: CBMutableService)     func removeAllServices()     func respondToRequest(_ request: CBATTRequest, withResult result: CBATTError)     func updateValue(_ value: NSData, forCharacteristic characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool } ``` | NSObject |
| To | ``` class CBPeripheralManager : CBManager {     weak var delegate: CBPeripheralManagerDelegate?     var isAdvertising: Bool { get }     class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus     convenience init()     convenience init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: DispatchQueue?)     init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: DispatchQueue?, options options: [String : Any]? = nil)     func startAdvertising(_ advertisementData: [String : Any]?)     func stopAdvertising()     func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, for central: CBCentral)     func add(_ service: CBMutableService)     func remove(_ service: CBMutableService)     func removeAllServices()     func respond(to request: CBATTRequest, withResult result: CBATTError.Code)     func updateValue(_ value: Data, for characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool } ``` | CBManager |

Modified [CBPeripheralManager.add(_: CBMutableService)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393255-addservice)

|  | Declaration |
| --- | --- |
| From | ``` func addService(_ service: CBMutableService) ``` |
| To | ``` func add(_ service: CBMutableService) ``` |

Modified [CBPeripheralManager.delegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393313-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: CBPeripheralManagerDelegate? ``` |
| To | ``` weak var delegate: CBPeripheralManagerDelegate? ``` |

Modified [CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate?, queue: DispatchQueue?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393299-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?) ``` |
| To | ``` convenience init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: DispatchQueue?) ``` |

Modified [CBPeripheralManager.init(delegate: CBPeripheralManagerDelegate?, queue: DispatchQueue?, options: [String : Any]?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393295-init)

|  | Declaration |
| --- | --- |
| From | ``` init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: dispatch_queue_t?, options options: [String : AnyObject]?) ``` |
| To | ``` init(delegate delegate: CBPeripheralManagerDelegate?, queue queue: DispatchQueue?, options options: [String : Any]? = nil) ``` |

Modified [CBPeripheralManager.remove(_: CBMutableService)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393287-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeService(_ service: CBMutableService) ``` |
| To | ``` func remove(_ service: CBMutableService) ``` |

Modified [CBPeripheralManager.respond(to: CBATTRequest, withResult: CBATTError.Code)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393293-respond)

|  | Declaration |
| --- | --- |
| From | ``` func respondToRequest(_ request: CBATTRequest, withResult result: CBATTError) ``` |
| To | ``` func respond(to request: CBATTRequest, withResult result: CBATTError.Code) ``` |

Modified [CBPeripheralManager.setDesiredConnectionLatency(_: CBPeripheralManagerConnectionLatency, for: CBCentral)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393277-setdesiredconnectionlatency)

|  | Declaration |
| --- | --- |
| From | ``` func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, forCentral central: CBCentral) ``` |
| To | ``` func setDesiredConnectionLatency(_ latency: CBPeripheralManagerConnectionLatency, for central: CBCentral) ``` |

Modified [CBPeripheralManager.startAdvertising(_: [String : Any]?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393252-startadvertising)

|  | Declaration |
| --- | --- |
| From | ``` func startAdvertising(_ advertisementData: [String : AnyObject]?) ``` |
| To | ``` func startAdvertising(_ advertisementData: [String : Any]?) ``` |

Modified [CBPeripheralManager.updateValue(_: Data, for: CBMutableCharacteristic, onSubscribedCentrals: [CBCentral]?) -> Bool](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/1393281-updatevalue)

|  | Declaration |
| --- | --- |
| From | ``` func updateValue(_ value: NSData, forCharacteristic characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool ``` |
| To | ``` func updateValue(_ value: Data, for characteristic: CBMutableCharacteristic, onSubscribedCentrals centrals: [CBCentral]?) -> Bool ``` |

Modified [CBPeripheralManagerAuthorizationStatus [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CBPeripheralManagerAuthorizationStatus : Int {     case NotDetermined     case Restricted     case Denied     case Authorized } ``` |
| To | ``` enum CBPeripheralManagerAuthorizationStatus : Int {     case notDetermined     case restricted     case denied     case authorized } ``` |

Modified [CBPeripheralManagerAuthorizationStatus.authorized](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/authorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [CBPeripheralManagerAuthorizationStatus.denied](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [CBPeripheralManagerAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/cbperipheralmanagerauthorizationstatusnotdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [CBPeripheralManagerAuthorizationStatus.restricted](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerauthorizationstatus/cbperipheralmanagerauthorizationstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [CBPeripheralManagerConnectionLatency [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency)

|  | Declaration |
| --- | --- |
| From | ``` enum CBPeripheralManagerConnectionLatency : Int {     case Low     case Medium     case High } ``` |
| To | ``` enum CBPeripheralManagerConnectionLatency : Int {     case low     case medium     case high } ``` |

Modified [CBPeripheralManagerConnectionLatency.high](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency/cbperipheralmanagerconnectionlatencyhigh)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [CBPeripheralManagerConnectionLatency.low](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency/cbperipheralmanagerconnectionlatencylow)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [CBPeripheralManagerConnectionLatency.medium](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerconnectionlatency/cbperipheralmanagerconnectionlatencymedium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [CBPeripheralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CBPeripheralManagerDelegate : NSObjectProtocol {     func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager)     optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : AnyObject])     optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error error: NSError?)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didAddService service: CBService, error error: NSError?)     optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didSubscribeToCharacteristic characteristic: CBCharacteristic)     optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didUnsubscribeFromCharacteristic characteristic: CBCharacteristic)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveReadRequest request: CBATTRequest)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWriteRequests requests: [CBATTRequest])     optional func peripheralManagerIsReadyToUpdateSubscribers(_ peripheral: CBPeripheralManager) } ``` |
| To | ``` protocol CBPeripheralManagerDelegate : NSObjectProtocol {     func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager)     optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : Any])     optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error error: Error?)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didAdd service: CBService, error error: Error?)     optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didSubscribeTo characteristic: CBCharacteristic)     optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didUnsubscribeFrom characteristic: CBCharacteristic)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveRead request: CBATTRequest)     optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWrite requests: [CBATTRequest])     optional func peripheralManagerIsReady(toUpdateSubscribers peripheral: CBPeripheralManager) } ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, central: CBCentral, didSubscribeTo: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393261-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didSubscribeToCharacteristic characteristic: CBCharacteristic) ``` |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didSubscribeTo characteristic: CBCharacteristic) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, central: CBCentral, didUnsubscribeFrom: CBCharacteristic)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393289-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didUnsubscribeFromCharacteristic characteristic: CBCharacteristic) ``` |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, central central: CBCentral, didUnsubscribeFrom characteristic: CBCharacteristic) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, didAdd: CBService, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393279-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didAddService service: CBService, error error: NSError?) ``` |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didAdd service: CBService, error error: Error?) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, didReceiveRead: CBATTRequest)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393257-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveReadRequest request: CBATTRequest) ``` |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveRead request: CBATTRequest) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, didReceiveWrite: [CBATTRequest])](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393315-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWriteRequests requests: [CBATTRequest]) ``` |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWrite requests: [CBATTRequest]) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManager(_: CBPeripheralManager, willRestoreState: [String : Any])](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393317-peripheralmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : AnyObject]) ``` |
| To | ``` optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : Any]) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManagerDidStartAdvertising(_: CBPeripheralManager, error: Error?)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393321-peripheralmanagerdidstartadverti)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error error: NSError?) ``` |
| To | ``` optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error error: Error?) ``` |

Modified [CBPeripheralManagerDelegate.peripheralManagerIsReady(toUpdateSubscribers: CBPeripheralManager)](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/1393248-peripheralmanagerisreadytoupdate)

|  | Declaration |
| --- | --- |
| From | ``` optional func peripheralManagerIsReadyToUpdateSubscribers(_ peripheral: CBPeripheralManager) ``` |
| To | ``` optional func peripheralManagerIsReady(toUpdateSubscribers peripheral: CBPeripheralManager) ``` |

Modified [CBPeripheralManagerState [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` enum CBPeripheralManagerState : Int {     case Unknown     case Resetting     case Unsupported     case Unauthorized     case PoweredOff     case PoweredOn } ``` | -- |
| To | ``` enum CBPeripheralManagerState : Int {     case unknown     case resetting     case unsupported     case unauthorized     case poweredOff     case poweredOn } ``` | iOS 10.0 |

Modified [CBPeripheralManagerState.poweredOff](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstatepoweredoff)

|  | Declaration |
| --- | --- |
| From | ``` case PoweredOff ``` |
| To | ``` case poweredOff ``` |

Modified [CBPeripheralManagerState.poweredOn](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/poweredon)

|  | Declaration |
| --- | --- |
| From | ``` case PoweredOn ``` |
| To | ``` case poweredOn ``` |

Modified [CBPeripheralManagerState.resetting](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/resetting)

|  | Declaration |
| --- | --- |
| From | ``` case Resetting ``` |
| To | ``` case resetting ``` |

Modified [CBPeripheralManagerState.unauthorized](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/unauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case Unauthorized ``` |
| To | ``` case unauthorized ``` |

Modified [CBPeripheralManagerState.unknown](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CBPeripheralManagerState.unsupported](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/cbperipheralmanagerstateunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case Unsupported ``` |
| To | ``` case unsupported ``` |

Modified [CBPeripheralState [enum]](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate)

|  | Declaration |
| --- | --- |
| From | ``` enum CBPeripheralState : Int {     case Disconnected     case Connecting     case Connected     case Disconnecting } ``` |
| To | ``` enum CBPeripheralState : Int {     case disconnected     case connecting     case connected     case disconnecting } ``` |

Modified [CBPeripheralState.connected](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/connected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [CBPeripheralState.connecting](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/cbperipheralstateconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Connecting ``` |
| To | ``` case connecting ``` |

Modified [CBPeripheralState.disconnected](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/disconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnected ``` |
| To | ``` case disconnected ``` |

Modified [CBPeripheralState.disconnecting](https://developer.apple.com/documentation/corebluetooth/cbperipheralstate/cbperipheralstatedisconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnecting ``` |
| To | ``` case disconnecting ``` |

Modified [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CBUUID : NSObject, NSCopying {     var data: NSData { get }     var UUIDString: String { get }      init(string theString: String)     class func UUIDWithString(_ theString: String) -> CBUUID      init(data theData: NSData)     class func UUIDWithData(_ theData: NSData) -> CBUUID      init(CFUUID theUUID: CFUUID)     class func UUIDWithCFUUID(_ theUUID: CFUUID) -> CBUUID      init(NSUUID theUUID: NSUUID)     class func UUIDWithNSUUID(_ theUUID: NSUUID) -> CBUUID } ``` | NSCopying |
| To | ``` class CBUUID : NSObject, NSCopying {     var data: Data { get }     var uuidString: String { get }      init(string theString: String)     class func withString(_ theString: String) -> CBUUID      init(data theData: Data)     class func withData(_ theData: Data) -> CBUUID      init(cfuuid theUUID: CFUUID)     class func withCFUUID(_ theUUID: CFUUID) -> CBUUID      init(nsuuid theUUID: UUID)     class func withNSUUID(_ theUUID: UUID) -> CBUUID     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CBUUID : CVarArg { } extension CBUUID : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [CBUUID.data](https://developer.apple.com/documentation/corebluetooth/cbuuid/1519007-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData { get } ``` |
| To | ``` var data: Data { get } ``` |

Modified [CBUUID.init(cfuuid: CFUUID)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518861-uuidwithcfuuid)

|  | Declaration |
| --- | --- |
| From | ``` init(CFUUID theUUID: CFUUID) ``` |
| To | ``` init(cfuuid theUUID: CFUUID) ``` |

Modified [CBUUID.init(data: Data)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518799-uuidwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init(data theData: NSData) ``` |
| To | ``` init(data theData: Data) ``` |

Modified [CBUUID.init(nsuuid: UUID)](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518783-init)

|  | Declaration |
| --- | --- |
| From | ``` init(NSUUID theUUID: NSUUID) ``` |
| To | ``` init(nsuuid theUUID: UUID) ``` |

Modified [CBUUID.uuidString](https://developer.apple.com/documentation/corebluetooth/cbuuid/1518742-uuidstring)

|  | Declaration |
| --- | --- |
| From | ``` var UUIDString: String { get } ``` |
| To | ``` var uuidString: String { get } ``` |

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
