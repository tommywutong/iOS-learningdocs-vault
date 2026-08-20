---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/AudioVideoBridging.html
archived_at: '2026-07-18T02:51:02.177448Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# AudioVideoBridging Changes for Swift

### AudioVideoBridging

Removed AVB17221ACMPFlags.NoneAdded AVB17221ACMPMessage.error(for: AVB17221ACMPStatusCode) -> Error? [class]Added AVB17221ACMPMessage.errorForStatusCode() -> Error?Added AVB17221AECPMessage.error(for: AVB17221AECPStatusCode) -> Error? [class]Added AVB17221AECPMessage.errorForStatusCode() -> Error?Modified AVB17221ACMPClient

|  | Declaration |
| --- | --- |
| From | ``` protocol AVB17221ACMPClient {     func ACMPDidReceiveCommand(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool     func ACMPDidReceiveResponse(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool } ``` |
| To | ``` protocol AVB17221ACMPClient {     func acmpDidReceiveCommand(_ message: AVB17221ACMPMessage, on anInterface: AVB17221ACMPInterface) -> Bool     func acmpDidReceiveResponse(_ message: AVB17221ACMPMessage, on anInterface: AVB17221ACMPInterface) -> Bool } ``` |

Modified AVB17221ACMPClient.acmpDidReceiveCommand(_: AVB17221ACMPMessage, on: AVB17221ACMPInterface) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ACMPDidReceiveCommand(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool ``` |
| To | ``` func acmpDidReceiveCommand(_ message: AVB17221ACMPMessage, on anInterface: AVB17221ACMPInterface) -> Bool ``` |

Modified AVB17221ACMPClient.acmpDidReceiveResponse(_: AVB17221ACMPMessage, on: AVB17221ACMPInterface) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ACMPDidReceiveResponse(_ message: AVB17221ACMPMessage, onInterface anInterface: AVB17221ACMPInterface) -> Bool ``` |
| To | ``` func acmpDidReceiveResponse(_ message: AVB17221ACMPMessage, on anInterface: AVB17221ACMPInterface) -> Bool ``` |

Modified AVB17221ACMPFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ACMPFlags : OptionSetType {     init(rawValue rawValue: UInt16)     static var None: AVB17221ACMPFlags { get }     static var ClassB: AVB17221ACMPFlags { get }     static var FastConnect: AVB17221ACMPFlags { get }     static var SavedState: AVB17221ACMPFlags { get }     static var StreamingWait: AVB17221ACMPFlags { get }     static var SupportsEncrypted: AVB17221ACMPFlags { get }     static var EncryptedPDU: AVB17221ACMPFlags { get }     static var StreamingTalkerFailed: AVB17221ACMPFlags { get } } ``` | OptionSetType |
| To | ``` struct AVB17221ACMPFlags : OptionSet {     init(rawValue rawValue: UInt16)     static var none: AVB17221ACMPFlags { get }     static var classB: AVB17221ACMPFlags { get }     static var fastConnect: AVB17221ACMPFlags { get }     static var savedState: AVB17221ACMPFlags { get }     static var streamingWait: AVB17221ACMPFlags { get }     static var supportsEncrypted: AVB17221ACMPFlags { get }     static var encryptedPDU: AVB17221ACMPFlags { get }     static var streamingTalkerFailed: AVB17221ACMPFlags { get }     func intersect(_ other: AVB17221ACMPFlags) -> AVB17221ACMPFlags     func exclusiveOr(_ other: AVB17221ACMPFlags) -> AVB17221ACMPFlags     mutating func unionInPlace(_ other: AVB17221ACMPFlags)     mutating func intersectInPlace(_ other: AVB17221ACMPFlags)     mutating func exclusiveOrInPlace(_ other: AVB17221ACMPFlags)     func isSubsetOf(_ other: AVB17221ACMPFlags) -> Bool     func isDisjointWith(_ other: AVB17221ACMPFlags) -> Bool     func isSupersetOf(_ other: AVB17221ACMPFlags) -> Bool     mutating func subtractInPlace(_ other: AVB17221ACMPFlags)     func isStrictSupersetOf(_ other: AVB17221ACMPFlags) -> Bool     func isStrictSubsetOf(_ other: AVB17221ACMPFlags) -> Bool } extension AVB17221ACMPFlags {     func union(_ other: AVB17221ACMPFlags) -> AVB17221ACMPFlags     func intersection(_ other: AVB17221ACMPFlags) -> AVB17221ACMPFlags     func symmetricDifference(_ other: AVB17221ACMPFlags) -> AVB17221ACMPFlags } extension AVB17221ACMPFlags {     func contains(_ member: AVB17221ACMPFlags) -> Bool     mutating func insert(_ newMember: AVB17221ACMPFlags) -> (inserted: Bool, memberAfterInsert: AVB17221ACMPFlags)     mutating func remove(_ member: AVB17221ACMPFlags) -> AVB17221ACMPFlags?     mutating func update(with newMember: AVB17221ACMPFlags) -> AVB17221ACMPFlags? } extension AVB17221ACMPFlags {     convenience init()     mutating func formUnion(_ other: AVB17221ACMPFlags)     mutating func formIntersection(_ other: AVB17221ACMPFlags)     mutating func formSymmetricDifference(_ other: AVB17221ACMPFlags) } extension AVB17221ACMPFlags {     convenience init<S : Sequence where S.Iterator.Element == AVB17221ACMPFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVB17221ACMPFlags...)     mutating func subtract(_ other: AVB17221ACMPFlags)     func isSubset(of other: AVB17221ACMPFlags) -> Bool     func isSuperset(of other: AVB17221ACMPFlags) -> Bool     func isDisjoint(with other: AVB17221ACMPFlags) -> Bool     func subtracting(_ other: AVB17221ACMPFlags) -> AVB17221ACMPFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVB17221ACMPFlags) -> Bool     func isStrictSubset(of other: AVB17221ACMPFlags) -> Bool } ``` | OptionSet |

Modified AVB17221ACMPFlags.classB

|  | Declaration |
| --- | --- |
| From | ``` static var ClassB: AVB17221ACMPFlags { get } ``` |
| To | ``` static var classB: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPFlags.encryptedPDU

|  | Declaration |
| --- | --- |
| From | ``` static var EncryptedPDU: AVB17221ACMPFlags { get } ``` |
| To | ``` static var encryptedPDU: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPFlags.fastConnect

|  | Declaration |
| --- | --- |
| From | ``` static var FastConnect: AVB17221ACMPFlags { get } ``` |
| To | ``` static var fastConnect: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPFlags.savedState

|  | Declaration |
| --- | --- |
| From | ``` static var SavedState: AVB17221ACMPFlags { get } ``` |
| To | ``` static var savedState: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPFlags.streamingTalkerFailed

|  | Declaration |
| --- | --- |
| From | ``` static var StreamingTalkerFailed: AVB17221ACMPFlags { get } ``` |
| To | ``` static var streamingTalkerFailed: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPFlags.streamingWait

|  | Declaration |
| --- | --- |
| From | ``` static var StreamingWait: AVB17221ACMPFlags { get } ``` |
| To | ``` static var streamingWait: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPFlags.supportsEncrypted

|  | Declaration |
| --- | --- |
| From | ``` static var SupportsEncrypted: AVB17221ACMPFlags { get } ``` |
| To | ``` static var supportsEncrypted: AVB17221ACMPFlags { get } ``` |

Modified AVB17221ACMPInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221ACMPInterface : AVB1722ControlInterface {     @NSCopying var multicastDestinationAddress: AVBMACAddress { get }      init(interface anInterface: AVBInterface)     class func ACMPInterfaceWithInterface(_ anInterface: AVBInterface) -> AVB17221ACMPInterface      init(interfaceNamed anInterfaceName: String)     class func ACMPInterfaceWithInterfaceNamed(_ anInterfaceName: String) -> AVB17221ACMPInterface     func setHandler(_ handler: AVB17221ACMPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221ACMPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandlerForGUID(_ targetGUID: UInt64)     func removeHandlerForEntityID(_ targetEntityID: UInt64)     func sendACMPResponseMessage(_ message: AVB17221ACMPMessage) throws     func sendACMPCommandMessage(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AVB17221ACMPInterfaceCompletion) -> Bool } ``` |
| To | ``` class AVB17221ACMPInterface : AVB1722ControlInterface {     @NSCopying var multicastDestinationAddress: AVBMACAddress { get }      init(interface anInterface: AVBInterface)     class func withInterface(_ anInterface: AVBInterface) -> AVB17221ACMPInterface      init(interfaceNamed anInterfaceName: String)     class func withInterfaceNamed(_ anInterfaceName: String) -> AVB17221ACMPInterface     func setHandler(_ handler: AVB17221ACMPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221ACMPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandler(forGUID targetGUID: UInt64)     func removeHandler(forEntityID targetEntityID: UInt64)     func sendACMPResponseMessage(_ message: AVB17221ACMPMessage) throws     func sendACMPCommand(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool } ``` |

Modified AVB17221ACMPInterface.removeHandler(forEntityID: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func removeHandlerForEntityID(_ targetEntityID: UInt64) ``` |
| To | ``` func removeHandler(forEntityID targetEntityID: UInt64) ``` |

Modified AVB17221ACMPInterface.sendACMPCommand(_: AVB17221ACMPMessage, completionHandler: AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendACMPCommandMessage(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AVB17221ACMPInterfaceCompletion) -> Bool ``` |
| To | ``` func sendACMPCommand(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool ``` |

Modified AVB17221ACMPMessage

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVB17221ACMPMessage : NSObject, NSCopying {     var messageType: AVB17221ACMPMessageType     var status: AVB17221ACMPStatusCode     var streamID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var talkerGUID: UInt64     var talkerEntityID: UInt64     var listenerGUID: UInt64     var listenerEntityID: UInt64     var talkerUniqueID: UInt16     var listenerUniqueID: UInt16     @NSCopying var destinationMAC: AVBMACAddress?     var connectionCount: UInt16     var sequenceID: UInt16     var flags: AVB17221ACMPFlags     var vlanID: UInt16     @NSCopying var sourceMAC: AVBMACAddress? } ``` | NSCopying |
| To | ``` class AVB17221ACMPMessage : NSObject, NSCopying {     var messageType: AVB17221ACMPMessageType     var status: AVB17221ACMPStatusCode     var streamID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var talkerGUID: UInt64     var talkerEntityID: UInt64     var listenerGUID: UInt64     var listenerEntityID: UInt64     var talkerUniqueID: UInt16     var listenerUniqueID: UInt16     @NSCopying var destinationMAC: AVBMACAddress?     var connectionCount: UInt16     var sequenceID: UInt16     var flags: AVB17221ACMPFlags     var vlanID: UInt16     @NSCopying var sourceMAC: AVBMACAddress?     class func error(for statusCode: AVB17221ACMPStatusCode) -> Error?     func errorForStatusCode() -> Error?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVB17221ACMPMessage : CVarArg { } extension AVB17221ACMPMessage : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified AVB17221ACMPMessageType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221ACMPMessageType : UInt8 {     case ConnectTXCommand     case ConnectTXResponse     case DisconnectTXCommand     case DisconnectTXResponse     case GetTXStateCommand     case GetTXStateResponse     case ConnectRXCommand     case ConnectRXResponse     case DisconnectRXCommand     case DisconnectRXResponse     case GetRXStateCommand     case GetRXStateResponse     case GetTXConnectionCommand     case GetTXConnectionResponse } ``` |
| To | ``` enum AVB17221ACMPMessageType : UInt8 {     case connectTXCommand     case connectTXResponse     case disconnectTXCommand     case disconnectTXResponse     case getTXStateCommand     case getTXStateResponse     case connectRXCommand     case connectRXResponse     case disconnectRXCommand     case disconnectRXResponse     case getRXStateCommand     case getRXStateResponse     case getTXConnectionCommand     case getTXConnectionResponse } ``` |

Modified AVB17221ACMPMessageType.connectRXCommand

|  | Declaration |
| --- | --- |
| From | ``` case ConnectRXCommand ``` |
| To | ``` case connectRXCommand ``` |

Modified AVB17221ACMPMessageType.connectRXResponse

|  | Declaration |
| --- | --- |
| From | ``` case ConnectRXResponse ``` |
| To | ``` case connectRXResponse ``` |

Modified AVB17221ACMPMessageType.connectTXCommand

|  | Declaration |
| --- | --- |
| From | ``` case ConnectTXCommand ``` |
| To | ``` case connectTXCommand ``` |

Modified AVB17221ACMPMessageType.connectTXResponse

|  | Declaration |
| --- | --- |
| From | ``` case ConnectTXResponse ``` |
| To | ``` case connectTXResponse ``` |

Modified AVB17221ACMPMessageType.disconnectRXCommand

|  | Declaration |
| --- | --- |
| From | ``` case DisconnectRXCommand ``` |
| To | ``` case disconnectRXCommand ``` |

Modified AVB17221ACMPMessageType.disconnectRXResponse

|  | Declaration |
| --- | --- |
| From | ``` case DisconnectRXResponse ``` |
| To | ``` case disconnectRXResponse ``` |

Modified AVB17221ACMPMessageType.disconnectTXCommand

|  | Declaration |
| --- | --- |
| From | ``` case DisconnectTXCommand ``` |
| To | ``` case disconnectTXCommand ``` |

Modified AVB17221ACMPMessageType.disconnectTXResponse

|  | Declaration |
| --- | --- |
| From | ``` case DisconnectTXResponse ``` |
| To | ``` case disconnectTXResponse ``` |

Modified AVB17221ACMPMessageType.getRXStateCommand

|  | Declaration |
| --- | --- |
| From | ``` case GetRXStateCommand ``` |
| To | ``` case getRXStateCommand ``` |

Modified AVB17221ACMPMessageType.getRXStateResponse

|  | Declaration |
| --- | --- |
| From | ``` case GetRXStateResponse ``` |
| To | ``` case getRXStateResponse ``` |

Modified AVB17221ACMPMessageType.getTXConnectionCommand

|  | Declaration |
| --- | --- |
| From | ``` case GetTXConnectionCommand ``` |
| To | ``` case getTXConnectionCommand ``` |

Modified AVB17221ACMPMessageType.getTXConnectionResponse

|  | Declaration |
| --- | --- |
| From | ``` case GetTXConnectionResponse ``` |
| To | ``` case getTXConnectionResponse ``` |

Modified AVB17221ACMPMessageType.getTXStateCommand

|  | Declaration |
| --- | --- |
| From | ``` case GetTXStateCommand ``` |
| To | ``` case getTXStateCommand ``` |

Modified AVB17221ACMPMessageType.getTXStateResponse

|  | Declaration |
| --- | --- |
| From | ``` case GetTXStateResponse ``` |
| To | ``` case getTXStateResponse ``` |

Modified AVB17221ACMPStatusCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221ACMPStatusCode : UInt8 {     case Success     case ListenerUnknownID     case TalkerUnknownID     case TalkerDestMACFail     case TalkerNoStreamIndex     case TalkerNoBandwidth     case TalkerExclusive     case ListenerTalkerTimeout     case ListenerExclusive     case StateUnavailable     case NotConnected     case NoSuchConnection     case UnableToSendMessage     case TalkerMisbehaving     case ListenerMisbehaving     case SRPFace     case ControllerNotAuthorized     case IncompatibleRequest     case NotSupported } ``` |
| To | ``` enum AVB17221ACMPStatusCode : UInt8 {     case success     case listenerUnknownID     case talkerUnknownID     case talkerDestMACFail     case talkerNoStreamIndex     case talkerNoBandwidth     case talkerExclusive     case listenerTalkerTimeout     case listenerExclusive     case stateUnavailable     case notConnected     case noSuchConnection     case unableToSendMessage     case talkerMisbehaving     case listenerMisbehaving     case srpFace     case controllerNotAuthorized     case incompatibleRequest     case notSupported } ``` |

Modified AVB17221ACMPStatusCode.controllerNotAuthorized

|  | Declaration |
| --- | --- |
| From | ``` case ControllerNotAuthorized ``` |
| To | ``` case controllerNotAuthorized ``` |

Modified AVB17221ACMPStatusCode.incompatibleRequest

|  | Declaration |
| --- | --- |
| From | ``` case IncompatibleRequest ``` |
| To | ``` case incompatibleRequest ``` |

Modified AVB17221ACMPStatusCode.listenerExclusive

|  | Declaration |
| --- | --- |
| From | ``` case ListenerExclusive ``` |
| To | ``` case listenerExclusive ``` |

Modified AVB17221ACMPStatusCode.listenerMisbehaving

|  | Declaration |
| --- | --- |
| From | ``` case ListenerMisbehaving ``` |
| To | ``` case listenerMisbehaving ``` |

Modified AVB17221ACMPStatusCode.listenerTalkerTimeout

|  | Declaration |
| --- | --- |
| From | ``` case ListenerTalkerTimeout ``` |
| To | ``` case listenerTalkerTimeout ``` |

Modified AVB17221ACMPStatusCode.listenerUnknownID

|  | Declaration |
| --- | --- |
| From | ``` case ListenerUnknownID ``` |
| To | ``` case listenerUnknownID ``` |

Modified AVB17221ACMPStatusCode.noSuchConnection

|  | Declaration |
| --- | --- |
| From | ``` case NoSuchConnection ``` |
| To | ``` case noSuchConnection ``` |

Modified AVB17221ACMPStatusCode.notConnected

|  | Declaration |
| --- | --- |
| From | ``` case NotConnected ``` |
| To | ``` case notConnected ``` |

Modified AVB17221ACMPStatusCode.notSupported

|  | Declaration |
| --- | --- |
| From | ``` case NotSupported ``` |
| To | ``` case notSupported ``` |

Modified AVB17221ACMPStatusCode.srpFace

|  | Declaration |
| --- | --- |
| From | ``` case SRPFace ``` |
| To | ``` case srpFace ``` |

Modified AVB17221ACMPStatusCode.stateUnavailable

|  | Declaration |
| --- | --- |
| From | ``` case StateUnavailable ``` |
| To | ``` case stateUnavailable ``` |

Modified AVB17221ACMPStatusCode.success

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified AVB17221ACMPStatusCode.talkerDestMACFail

|  | Declaration |
| --- | --- |
| From | ``` case TalkerDestMACFail ``` |
| To | ``` case talkerDestMACFail ``` |

Modified AVB17221ACMPStatusCode.talkerExclusive

|  | Declaration |
| --- | --- |
| From | ``` case TalkerExclusive ``` |
| To | ``` case talkerExclusive ``` |

Modified AVB17221ACMPStatusCode.talkerMisbehaving

|  | Declaration |
| --- | --- |
| From | ``` case TalkerMisbehaving ``` |
| To | ``` case talkerMisbehaving ``` |

Modified AVB17221ACMPStatusCode.talkerNoBandwidth

|  | Declaration |
| --- | --- |
| From | ``` case TalkerNoBandwidth ``` |
| To | ``` case talkerNoBandwidth ``` |

Modified AVB17221ACMPStatusCode.talkerNoStreamIndex

|  | Declaration |
| --- | --- |
| From | ``` case TalkerNoStreamIndex ``` |
| To | ``` case talkerNoStreamIndex ``` |

Modified AVB17221ACMPStatusCode.talkerUnknownID

|  | Declaration |
| --- | --- |
| From | ``` case TalkerUnknownID ``` |
| To | ``` case talkerUnknownID ``` |

Modified AVB17221ACMPStatusCode.unableToSendMessage

|  | Declaration |
| --- | --- |
| From | ``` case UnableToSendMessage ``` |
| To | ``` case unableToSendMessage ``` |

Modified AVB17221ADPControllerCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ADPControllerCapabilities : OptionSetType {     init(rawValue rawValue: UInt32)     static var Implemented: AVB17221ADPControllerCapabilities { get }     static var HasLayer3Proxy: AVB17221ADPControllerCapabilities { get } } ``` | OptionSetType |
| To | ``` struct AVB17221ADPControllerCapabilities : OptionSet {     init(rawValue rawValue: UInt32)     static var implemented: AVB17221ADPControllerCapabilities { get }     static var hasLayer3Proxy: AVB17221ADPControllerCapabilities { get }     func intersect(_ other: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities     func exclusiveOr(_ other: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities     mutating func unionInPlace(_ other: AVB17221ADPControllerCapabilities)     mutating func intersectInPlace(_ other: AVB17221ADPControllerCapabilities)     mutating func exclusiveOrInPlace(_ other: AVB17221ADPControllerCapabilities)     func isSubsetOf(_ other: AVB17221ADPControllerCapabilities) -> Bool     func isDisjointWith(_ other: AVB17221ADPControllerCapabilities) -> Bool     func isSupersetOf(_ other: AVB17221ADPControllerCapabilities) -> Bool     mutating func subtractInPlace(_ other: AVB17221ADPControllerCapabilities)     func isStrictSupersetOf(_ other: AVB17221ADPControllerCapabilities) -> Bool     func isStrictSubsetOf(_ other: AVB17221ADPControllerCapabilities) -> Bool } extension AVB17221ADPControllerCapabilities {     func union(_ other: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities     func intersection(_ other: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities     func symmetricDifference(_ other: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities } extension AVB17221ADPControllerCapabilities {     func contains(_ member: AVB17221ADPControllerCapabilities) -> Bool     mutating func insert(_ newMember: AVB17221ADPControllerCapabilities) -> (inserted: Bool, memberAfterInsert: AVB17221ADPControllerCapabilities)     mutating func remove(_ member: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities?     mutating func update(with newMember: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities? } extension AVB17221ADPControllerCapabilities {     convenience init()     mutating func formUnion(_ other: AVB17221ADPControllerCapabilities)     mutating func formIntersection(_ other: AVB17221ADPControllerCapabilities)     mutating func formSymmetricDifference(_ other: AVB17221ADPControllerCapabilities) } extension AVB17221ADPControllerCapabilities {     convenience init<S : Sequence where S.Iterator.Element == AVB17221ADPControllerCapabilities>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVB17221ADPControllerCapabilities...)     mutating func subtract(_ other: AVB17221ADPControllerCapabilities)     func isSubset(of other: AVB17221ADPControllerCapabilities) -> Bool     func isSuperset(of other: AVB17221ADPControllerCapabilities) -> Bool     func isDisjoint(with other: AVB17221ADPControllerCapabilities) -> Bool     func subtracting(_ other: AVB17221ADPControllerCapabilities) -> AVB17221ADPControllerCapabilities     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVB17221ADPControllerCapabilities) -> Bool     func isStrictSubset(of other: AVB17221ADPControllerCapabilities) -> Bool } ``` | OptionSet |

Modified AVB17221ADPControllerCapabilities.hasLayer3Proxy

|  | Declaration |
| --- | --- |
| From | ``` static var HasLayer3Proxy: AVB17221ADPControllerCapabilities { get } ``` |
| To | ``` static var hasLayer3Proxy: AVB17221ADPControllerCapabilities { get } ``` |

Modified AVB17221ADPControllerCapabilities.implemented

|  | Declaration |
| --- | --- |
| From | ``` static var Implemented: AVB17221ADPControllerCapabilities { get } ``` |
| To | ``` static var implemented: AVB17221ADPControllerCapabilities { get } ``` |

Modified AVB17221ADPEntityCapabilities [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221ADPEntityCapabilities : UInt32 {     case DFUMode     static var EFUMode: AVB17221ADPEntityCapabilities { get }     case AddressAccessSupported     case GatewayEntity     case AEMSupported     case LegacyAVC     case AssociationIDSupported     case AssociationIDValid     case VendorUniqueSupported     case ClassASupported     case ClassBSupported     case ASSupported     static var GPTPSupported: AVB17221ADPEntityCapabilities { get }     case AEMAuthenticationSupported     case AEMAuthenticationRequired     case AEMPersistentAcquireSupported     case AEMIdenitifyControlIndexValid     case AEMInterfaceIndexValid     case GeneralControllerIgnore     case EntityNotReady } ``` |
| To | ``` enum AVB17221ADPEntityCapabilities : UInt32 {     case dfuMode     static var efuMode: AVB17221ADPEntityCapabilities { get }     case addressAccessSupported     case gatewayEntity     case aemSupported     case legacyAVC     case associationIDSupported     case associationIDValid     case vendorUniqueSupported     case classASupported     case classBSupported     case asSupported     static var gptpSupported: AVB17221ADPEntityCapabilities { get }     case aemAuthenticationSupported     case aemAuthenticationRequired     case aemPersistentAcquireSupported     case aemIdenitifyControlIndexValid     case aemInterfaceIndexValid     case generalControllerIgnore     case entityNotReady } ``` |

Modified AVB17221ADPEntityCapabilities.addressAccessSupported

|  | Declaration |
| --- | --- |
| From | ``` case AddressAccessSupported ``` |
| To | ``` case addressAccessSupported ``` |

Modified AVB17221ADPEntityCapabilities.aemAuthenticationRequired

|  | Declaration |
| --- | --- |
| From | ``` case AEMAuthenticationRequired ``` |
| To | ``` case aemAuthenticationRequired ``` |

Modified AVB17221ADPEntityCapabilities.aemAuthenticationSupported

|  | Declaration |
| --- | --- |
| From | ``` case AEMAuthenticationSupported ``` |
| To | ``` case aemAuthenticationSupported ``` |

Modified AVB17221ADPEntityCapabilities.aemIdenitifyControlIndexValid

|  | Declaration |
| --- | --- |
| From | ``` case AEMIdenitifyControlIndexValid ``` |
| To | ``` case aemIdenitifyControlIndexValid ``` |

Modified AVB17221ADPEntityCapabilities.aemInterfaceIndexValid

|  | Declaration |
| --- | --- |
| From | ``` case AEMInterfaceIndexValid ``` |
| To | ``` case aemInterfaceIndexValid ``` |

Modified AVB17221ADPEntityCapabilities.aemPersistentAcquireSupported

|  | Declaration |
| --- | --- |
| From | ``` case AEMPersistentAcquireSupported ``` |
| To | ``` case aemPersistentAcquireSupported ``` |

Modified AVB17221ADPEntityCapabilities.aemSupported

|  | Declaration |
| --- | --- |
| From | ``` case AEMSupported ``` |
| To | ``` case aemSupported ``` |

Modified AVB17221ADPEntityCapabilities.associationIDSupported

|  | Declaration |
| --- | --- |
| From | ``` case AssociationIDSupported ``` |
| To | ``` case associationIDSupported ``` |

Modified AVB17221ADPEntityCapabilities.associationIDValid

|  | Declaration |
| --- | --- |
| From | ``` case AssociationIDValid ``` |
| To | ``` case associationIDValid ``` |

Modified AVB17221ADPEntityCapabilities.classASupported

|  | Declaration |
| --- | --- |
| From | ``` case ClassASupported ``` |
| To | ``` case classASupported ``` |

Modified AVB17221ADPEntityCapabilities.classBSupported

|  | Declaration |
| --- | --- |
| From | ``` case ClassBSupported ``` |
| To | ``` case classBSupported ``` |

Modified AVB17221ADPEntityCapabilities.efuMode

|  | Declaration |
| --- | --- |
| From | ``` static var EFUMode: AVB17221ADPEntityCapabilities { get } ``` |
| To | ``` static var efuMode: AVB17221ADPEntityCapabilities { get } ``` |

Modified AVB17221ADPEntityCapabilities.entityNotReady

|  | Declaration |
| --- | --- |
| From | ``` case EntityNotReady ``` |
| To | ``` case entityNotReady ``` |

Modified AVB17221ADPEntityCapabilities.gatewayEntity

|  | Declaration |
| --- | --- |
| From | ``` case GatewayEntity ``` |
| To | ``` case gatewayEntity ``` |

Modified AVB17221ADPEntityCapabilities.generalControllerIgnore

|  | Declaration |
| --- | --- |
| From | ``` case GeneralControllerIgnore ``` |
| To | ``` case generalControllerIgnore ``` |

Modified AVB17221ADPEntityCapabilities.gptpSupported

|  | Declaration |
| --- | --- |
| From | ``` static var GPTPSupported: AVB17221ADPEntityCapabilities { get } ``` |
| To | ``` static var gptpSupported: AVB17221ADPEntityCapabilities { get } ``` |

Modified AVB17221ADPEntityCapabilities.legacyAVC

|  | Declaration |
| --- | --- |
| From | ``` case LegacyAVC ``` |
| To | ``` case legacyAVC ``` |

Modified AVB17221ADPEntityCapabilities.vendorUniqueSupported

|  | Declaration |
| --- | --- |
| From | ``` case VendorUniqueSupported ``` |
| To | ``` case vendorUniqueSupported ``` |

Modified AVB17221ADPListenerCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ADPListenerCapabilities : OptionSetType {     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPListenerCapabilities { get }     static var HasOtherSink: AVB17221ADPListenerCapabilities { get }     static var HasControlSink: AVB17221ADPListenerCapabilities { get }     static var HasMediaClockSink: AVB17221ADPListenerCapabilities { get }     static var HasSMPTESink: AVB17221ADPListenerCapabilities { get }     static var HasMIDISink: AVB17221ADPListenerCapabilities { get }     static var HasAudioSink: AVB17221ADPListenerCapabilities { get }     static var HasVideoSink: AVB17221ADPListenerCapabilities { get } } ``` | OptionSetType |
| To | ``` struct AVB17221ADPListenerCapabilities : OptionSet {     init(rawValue rawValue: UInt16)     static var implemented: AVB17221ADPListenerCapabilities { get }     static var hasOtherSink: AVB17221ADPListenerCapabilities { get }     static var hasControlSink: AVB17221ADPListenerCapabilities { get }     static var hasMediaClockSink: AVB17221ADPListenerCapabilities { get }     static var hasSMPTESink: AVB17221ADPListenerCapabilities { get }     static var hasMIDISink: AVB17221ADPListenerCapabilities { get }     static var hasAudioSink: AVB17221ADPListenerCapabilities { get }     static var hasVideoSink: AVB17221ADPListenerCapabilities { get }     func intersect(_ other: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities     func exclusiveOr(_ other: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities     mutating func unionInPlace(_ other: AVB17221ADPListenerCapabilities)     mutating func intersectInPlace(_ other: AVB17221ADPListenerCapabilities)     mutating func exclusiveOrInPlace(_ other: AVB17221ADPListenerCapabilities)     func isSubsetOf(_ other: AVB17221ADPListenerCapabilities) -> Bool     func isDisjointWith(_ other: AVB17221ADPListenerCapabilities) -> Bool     func isSupersetOf(_ other: AVB17221ADPListenerCapabilities) -> Bool     mutating func subtractInPlace(_ other: AVB17221ADPListenerCapabilities)     func isStrictSupersetOf(_ other: AVB17221ADPListenerCapabilities) -> Bool     func isStrictSubsetOf(_ other: AVB17221ADPListenerCapabilities) -> Bool } extension AVB17221ADPListenerCapabilities {     func union(_ other: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities     func intersection(_ other: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities     func symmetricDifference(_ other: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities } extension AVB17221ADPListenerCapabilities {     func contains(_ member: AVB17221ADPListenerCapabilities) -> Bool     mutating func insert(_ newMember: AVB17221ADPListenerCapabilities) -> (inserted: Bool, memberAfterInsert: AVB17221ADPListenerCapabilities)     mutating func remove(_ member: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities?     mutating func update(with newMember: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities? } extension AVB17221ADPListenerCapabilities {     convenience init()     mutating func formUnion(_ other: AVB17221ADPListenerCapabilities)     mutating func formIntersection(_ other: AVB17221ADPListenerCapabilities)     mutating func formSymmetricDifference(_ other: AVB17221ADPListenerCapabilities) } extension AVB17221ADPListenerCapabilities {     convenience init<S : Sequence where S.Iterator.Element == AVB17221ADPListenerCapabilities>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVB17221ADPListenerCapabilities...)     mutating func subtract(_ other: AVB17221ADPListenerCapabilities)     func isSubset(of other: AVB17221ADPListenerCapabilities) -> Bool     func isSuperset(of other: AVB17221ADPListenerCapabilities) -> Bool     func isDisjoint(with other: AVB17221ADPListenerCapabilities) -> Bool     func subtracting(_ other: AVB17221ADPListenerCapabilities) -> AVB17221ADPListenerCapabilities     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVB17221ADPListenerCapabilities) -> Bool     func isStrictSubset(of other: AVB17221ADPListenerCapabilities) -> Bool } ``` | OptionSet |

Modified AVB17221ADPListenerCapabilities.hasAudioSink

|  | Declaration |
| --- | --- |
| From | ``` static var HasAudioSink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasAudioSink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.hasControlSink

|  | Declaration |
| --- | --- |
| From | ``` static var HasControlSink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasControlSink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.hasMediaClockSink

|  | Declaration |
| --- | --- |
| From | ``` static var HasMediaClockSink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasMediaClockSink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.hasMIDISink

|  | Declaration |
| --- | --- |
| From | ``` static var HasMIDISink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasMIDISink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.hasOtherSink

|  | Declaration |
| --- | --- |
| From | ``` static var HasOtherSink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasOtherSink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.hasSMPTESink

|  | Declaration |
| --- | --- |
| From | ``` static var HasSMPTESink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasSMPTESink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.hasVideoSink

|  | Declaration |
| --- | --- |
| From | ``` static var HasVideoSink: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var hasVideoSink: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPListenerCapabilities.implemented

|  | Declaration |
| --- | --- |
| From | ``` static var Implemented: AVB17221ADPListenerCapabilities { get } ``` |
| To | ``` static var implemented: AVB17221ADPListenerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221ADPTalkerCapabilities : OptionSetType {     init(rawValue rawValue: UInt16)     static var Implemented: AVB17221ADPTalkerCapabilities { get }     static var HasOtherSource: AVB17221ADPTalkerCapabilities { get }     static var HasControlSource: AVB17221ADPTalkerCapabilities { get }     static var HasMediaClockSource: AVB17221ADPTalkerCapabilities { get }     static var HasSMPTESource: AVB17221ADPTalkerCapabilities { get }     static var HasMIDISource: AVB17221ADPTalkerCapabilities { get }     static var HasAudioSource: AVB17221ADPTalkerCapabilities { get }     static var HasVideoSource: AVB17221ADPTalkerCapabilities { get } } ``` | OptionSetType |
| To | ``` struct AVB17221ADPTalkerCapabilities : OptionSet {     init(rawValue rawValue: UInt16)     static var implemented: AVB17221ADPTalkerCapabilities { get }     static var hasOtherSource: AVB17221ADPTalkerCapabilities { get }     static var hasControlSource: AVB17221ADPTalkerCapabilities { get }     static var hasMediaClockSource: AVB17221ADPTalkerCapabilities { get }     static var hasSMPTESource: AVB17221ADPTalkerCapabilities { get }     static var hasMIDISource: AVB17221ADPTalkerCapabilities { get }     static var hasAudioSource: AVB17221ADPTalkerCapabilities { get }     static var hasVideoSource: AVB17221ADPTalkerCapabilities { get }     func intersect(_ other: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities     func exclusiveOr(_ other: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities     mutating func unionInPlace(_ other: AVB17221ADPTalkerCapabilities)     mutating func intersectInPlace(_ other: AVB17221ADPTalkerCapabilities)     mutating func exclusiveOrInPlace(_ other: AVB17221ADPTalkerCapabilities)     func isSubsetOf(_ other: AVB17221ADPTalkerCapabilities) -> Bool     func isDisjointWith(_ other: AVB17221ADPTalkerCapabilities) -> Bool     func isSupersetOf(_ other: AVB17221ADPTalkerCapabilities) -> Bool     mutating func subtractInPlace(_ other: AVB17221ADPTalkerCapabilities)     func isStrictSupersetOf(_ other: AVB17221ADPTalkerCapabilities) -> Bool     func isStrictSubsetOf(_ other: AVB17221ADPTalkerCapabilities) -> Bool } extension AVB17221ADPTalkerCapabilities {     func union(_ other: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities     func intersection(_ other: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities     func symmetricDifference(_ other: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities } extension AVB17221ADPTalkerCapabilities {     func contains(_ member: AVB17221ADPTalkerCapabilities) -> Bool     mutating func insert(_ newMember: AVB17221ADPTalkerCapabilities) -> (inserted: Bool, memberAfterInsert: AVB17221ADPTalkerCapabilities)     mutating func remove(_ member: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities?     mutating func update(with newMember: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities? } extension AVB17221ADPTalkerCapabilities {     convenience init()     mutating func formUnion(_ other: AVB17221ADPTalkerCapabilities)     mutating func formIntersection(_ other: AVB17221ADPTalkerCapabilities)     mutating func formSymmetricDifference(_ other: AVB17221ADPTalkerCapabilities) } extension AVB17221ADPTalkerCapabilities {     convenience init<S : Sequence where S.Iterator.Element == AVB17221ADPTalkerCapabilities>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVB17221ADPTalkerCapabilities...)     mutating func subtract(_ other: AVB17221ADPTalkerCapabilities)     func isSubset(of other: AVB17221ADPTalkerCapabilities) -> Bool     func isSuperset(of other: AVB17221ADPTalkerCapabilities) -> Bool     func isDisjoint(with other: AVB17221ADPTalkerCapabilities) -> Bool     func subtracting(_ other: AVB17221ADPTalkerCapabilities) -> AVB17221ADPTalkerCapabilities     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVB17221ADPTalkerCapabilities) -> Bool     func isStrictSubset(of other: AVB17221ADPTalkerCapabilities) -> Bool } ``` | OptionSet |

Modified AVB17221ADPTalkerCapabilities.hasAudioSource

|  | Declaration |
| --- | --- |
| From | ``` static var HasAudioSource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasAudioSource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.hasControlSource

|  | Declaration |
| --- | --- |
| From | ``` static var HasControlSource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasControlSource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.hasMediaClockSource

|  | Declaration |
| --- | --- |
| From | ``` static var HasMediaClockSource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasMediaClockSource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.hasMIDISource

|  | Declaration |
| --- | --- |
| From | ``` static var HasMIDISource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasMIDISource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.hasOtherSource

|  | Declaration |
| --- | --- |
| From | ``` static var HasOtherSource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasOtherSource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.hasSMPTESource

|  | Declaration |
| --- | --- |
| From | ``` static var HasSMPTESource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasSMPTESource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.hasVideoSource

|  | Declaration |
| --- | --- |
| From | ``` static var HasVideoSource: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var hasVideoSource: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221ADPTalkerCapabilities.implemented

|  | Declaration |
| --- | --- |
| From | ``` static var Implemented: AVB17221ADPTalkerCapabilities { get } ``` |
| To | ``` static var implemented: AVB17221ADPTalkerCapabilities { get } ``` |

Modified AVB17221AECPAddressAccessMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAddressAccessMessage : AVB17221AECPMessage {     var tlvs: [AVB17221AECPAddressAccessTLV]?     class func commandMessage() -> AVB17221AECPAddressAccessMessage     class func responseMessage() -> AVB17221AECPAddressAccessMessage } ``` |
| To | ``` class AVB17221AECPAddressAccessMessage : AVB17221AECPMessage {     var tlvs: [AVB17221AECPAddressAccessTLV]?     class func command() -> AVB17221AECPAddressAccessMessage     class func response() -> AVB17221AECPAddressAccessMessage } ``` |

Modified AVB17221AECPAddressAccessMessage.command() -> AVB17221AECPAddressAccessMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func commandMessage() -> AVB17221AECPAddressAccessMessage ``` |
| To | ``` class func command() -> AVB17221AECPAddressAccessMessage ``` |

Modified AVB17221AECPAddressAccessMessage.response() -> AVB17221AECPAddressAccessMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func responseMessage() -> AVB17221AECPAddressAccessMessage ``` |
| To | ``` class func response() -> AVB17221AECPAddressAccessMessage ``` |

Modified AVB17221AECPAddressAccessTLV

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVB17221AECPAddressAccessTLV : NSObject {     var mode: AVB17221AECPAddressAccessTLVMode     var address: UInt64     @NSCopying var memoryData: NSData? } ``` | -- |
| To | ``` class AVB17221AECPAddressAccessTLV : NSObject {     var mode: AVB17221AECPAddressAccessTLVMode     var address: UInt64     var memoryData: Data?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVB17221AECPAddressAccessTLV : CVarArg { } extension AVB17221AECPAddressAccessTLV : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified AVB17221AECPAddressAccessTLV.memoryData

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var memoryData: NSData? ``` |
| To | ``` var memoryData: Data? ``` |

Modified AVB17221AECPAddressAccessTLVMode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221AECPAddressAccessTLVMode : UInt8 {     case Read     case Write     case Execute } ``` |
| To | ``` enum AVB17221AECPAddressAccessTLVMode : UInt8 {     case read     case write     case execute } ``` |

Modified AVB17221AECPAddressAccessTLVMode.execute

|  | Declaration |
| --- | --- |
| From | ``` case Execute ``` |
| To | ``` case execute ``` |

Modified AVB17221AECPAddressAccessTLVMode.read

|  | Declaration |
| --- | --- |
| From | ``` case Read ``` |
| To | ``` case read ``` |

Modified AVB17221AECPAddressAccessTLVMode.write

|  | Declaration |
| --- | --- |
| From | ``` case Write ``` |
| To | ``` case write ``` |

Modified AVB17221AECPAEMMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAEMMessage : AVB17221AECPMessage {     var commandType: AVB17221AEMCommandType     var unsolicited: Bool     var controllerRequest: Bool     @NSCopying var commandSpecificData: NSData?     class func commandMessage() -> AVB17221AECPAEMMessage     class func responseMessage() -> AVB17221AECPAEMMessage } ``` |
| To | ``` class AVB17221AECPAEMMessage : AVB17221AECPMessage {     var commandType: AVB17221AEMCommandType     var isUnsolicited: Bool     var isControllerRequest: Bool     var commandSpecificData: Data?     class func command() -> AVB17221AECPAEMMessage     class func response() -> AVB17221AECPAEMMessage } ``` |

Modified AVB17221AECPAEMMessage.command() -> AVB17221AECPAEMMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func commandMessage() -> AVB17221AECPAEMMessage ``` |
| To | ``` class func command() -> AVB17221AECPAEMMessage ``` |

Modified AVB17221AECPAEMMessage.commandSpecificData

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var commandSpecificData: NSData? ``` |
| To | ``` var commandSpecificData: Data? ``` |

Modified AVB17221AECPAEMMessage.isControllerRequest

|  | Declaration |
| --- | --- |
| From | ``` var controllerRequest: Bool ``` |
| To | ``` var isControllerRequest: Bool ``` |

Modified AVB17221AECPAEMMessage.isUnsolicited

|  | Declaration |
| --- | --- |
| From | ``` var unsolicited: Bool ``` |
| To | ``` var isUnsolicited: Bool ``` |

Modified AVB17221AECPAEMMessage.response() -> AVB17221AECPAEMMessage [class]

|  | Declaration |
| --- | --- |
| From | ``` class func responseMessage() -> AVB17221AECPAEMMessage ``` |
| To | ``` class func response() -> AVB17221AECPAEMMessage ``` |

Modified AVB17221AECPAVCMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPAVCMessage : AVB17221AECPMessage {     @NSCopying var commandResponse: NSData? } ``` |
| To | ``` class AVB17221AECPAVCMessage : AVB17221AECPMessage {     var commandResponse: Data? } ``` |

Modified AVB17221AECPAVCMessage.commandResponse

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var commandResponse: NSData? ``` |
| To | ``` var commandResponse: Data? ``` |

Modified AVB17221AECPClient

|  | Declaration |
| --- | --- |
| From | ``` protocol AVB17221AECPClient {     func AECPDidReceiveCommand(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool     func AECPDidReceiveResponse(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool } ``` |
| To | ``` protocol AVB17221AECPClient {     func aecpDidReceiveCommand(_ message: AVB17221AECPMessage, on anInterface: AVB17221AECPInterface) -> Bool     func aecpDidReceiveResponse(_ message: AVB17221AECPMessage, on anInterface: AVB17221AECPInterface) -> Bool } ``` |

Modified AVB17221AECPClient.aecpDidReceiveCommand(_: AVB17221AECPMessage, on: AVB17221AECPInterface) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func AECPDidReceiveCommand(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool ``` |
| To | ``` func aecpDidReceiveCommand(_ message: AVB17221AECPMessage, on anInterface: AVB17221AECPInterface) -> Bool ``` |

Modified AVB17221AECPClient.aecpDidReceiveResponse(_: AVB17221AECPMessage, on: AVB17221AECPInterface) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func AECPDidReceiveResponse(_ message: AVB17221AECPMessage, onInterface anInterface: AVB17221AECPInterface) -> Bool ``` |
| To | ``` func aecpDidReceiveResponse(_ message: AVB17221AECPMessage, on anInterface: AVB17221AECPInterface) -> Bool ``` |

Modified AVB17221AECPInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPInterface : AVB1722ControlInterface {      init?(interface anInterface: AVBInterface)     class func AECPInterfaceWithInterface(_ anInterface: AVBInterface) -> AVB17221AECPInterface?      init?(interfaceNamed anInterfaceName: String)     class func AECPInterfaceWithInterfaceNamed(_ anInterfaceName: String) -> AVB17221AECPInterface?     func setHandler(_ handler: AVB17221AECPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandlerForGUID(_ targetGUID: UInt64)     func removeHandlerForEntityID(_ targetEntityID: UInt64)     func setCommandHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeCommandHandlerForEntityID(_ targetEntityID: UInt64)     func setResponseHandler(_ handler: AVB17221AECPClient, forControllerEntityID controllerEntityID: UInt64) -> Bool     func removeResponseHandlerForControllerEntityID(_ controllerEntityID: UInt64)     func sendCommand(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress, completionHandler completionHandler: AVB17221AECPInterfaceCompletion) -> Bool     func sendResponse(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress) throws } ``` |
| To | ``` class AVB17221AECPInterface : AVB1722ControlInterface {      init?(interface anInterface: AVBInterface)     class func withInterface(_ anInterface: AVBInterface) -> AVB17221AECPInterface?      init?(interfaceNamed anInterfaceName: String)     class func withInterfaceNamed(_ anInterfaceName: String) -> AVB17221AECPInterface?     func setHandler(_ handler: AVB17221AECPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandler(forGUID targetGUID: UInt64)     func removeHandler(forEntityID targetEntityID: UInt64)     func setCommandHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeCommandHandler(forEntityID targetEntityID: UInt64)     func setResponseHandler(_ handler: AVB17221AECPClient, forControllerEntityID controllerEntityID: UInt64) -> Bool     func removeResponseHandler(forControllerEntityID controllerEntityID: UInt64)     func sendCommand(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress, completionHandler completionHandler: AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool     func sendResponse(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress) throws } ``` |

Modified AVB17221AECPInterface.removeCommandHandler(forEntityID: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func removeCommandHandlerForEntityID(_ targetEntityID: UInt64) ``` |
| To | ``` func removeCommandHandler(forEntityID targetEntityID: UInt64) ``` |

Modified AVB17221AECPInterface.removeHandler(forEntityID: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func removeHandlerForEntityID(_ targetEntityID: UInt64) ``` |
| To | ``` func removeHandler(forEntityID targetEntityID: UInt64) ``` |

Modified AVB17221AECPInterface.removeResponseHandler(forControllerEntityID: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func removeResponseHandlerForControllerEntityID(_ controllerEntityID: UInt64) ``` |
| To | ``` func removeResponseHandler(forControllerEntityID controllerEntityID: UInt64) ``` |

Modified AVB17221AECPInterface.sendCommand(_: AVB17221AECPMessage, to: AVBMACAddress, completionHandler: AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendCommand(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress, completionHandler completionHandler: AVB17221AECPInterfaceCompletion) -> Bool ``` |
| To | ``` func sendCommand(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress, completionHandler completionHandler: AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool ``` |

Modified AVB17221AECPInterface.sendResponse(_: AVB17221AECPMessage, to: AVBMACAddress) throws

|  | Declaration |
| --- | --- |
| From | ``` func sendResponse(_ message: AVB17221AECPMessage, toMACAddress destMAC: AVBMACAddress) throws ``` |
| To | ``` func sendResponse(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress) throws ``` |

Modified AVB17221AECPMessage

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVB17221AECPMessage : NSObject, NSCopying {     var messageType: AVB17221AECPMessageType     var status: AVB17221AECPStatusCode     var targetGUID: UInt64     var targetEntityID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var sequenceID: UInt16     @NSCopying var sourceMAC: AVBMACAddress } ``` | NSCopying |
| To | ``` class AVB17221AECPMessage : NSObject, NSCopying {     var messageType: AVB17221AECPMessageType     var status: AVB17221AECPStatusCode     var targetGUID: UInt64     var targetEntityID: UInt64     var controllerGUID: UInt64     var controllerEntityID: UInt64     var sequenceID: UInt16     @NSCopying var sourceMAC: AVBMACAddress     class func error(for statusCode: AVB17221AECPStatusCode) -> Error?     func errorForStatusCode() -> Error?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVB17221AECPMessage : CVarArg { } extension AVB17221AECPMessage : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified AVB17221AECPMessageType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221AECPMessageType : UInt8 {     case AEMCommand     case AEMResponse     case AddressAccessCommand     case AddressAccessResponse     case LegacyAVCCommand     case LegacyAVCResponse     case VendorUniqueCommand     case VendorUniqueResponse } ``` |
| To | ``` enum AVB17221AECPMessageType : UInt8 {     case aemCommand     case aemResponse     case addressAccessCommand     case addressAccessResponse     case legacyAVCCommand     case legacyAVCResponse     case vendorUniqueCommand     case vendorUniqueResponse } ``` |

Modified AVB17221AECPMessageType.addressAccessCommand

|  | Declaration |
| --- | --- |
| From | ``` case AddressAccessCommand ``` |
| To | ``` case addressAccessCommand ``` |

Modified AVB17221AECPMessageType.addressAccessResponse

|  | Declaration |
| --- | --- |
| From | ``` case AddressAccessResponse ``` |
| To | ``` case addressAccessResponse ``` |

Modified AVB17221AECPMessageType.aemCommand

|  | Declaration |
| --- | --- |
| From | ``` case AEMCommand ``` |
| To | ``` case aemCommand ``` |

Modified AVB17221AECPMessageType.aemResponse

|  | Declaration |
| --- | --- |
| From | ``` case AEMResponse ``` |
| To | ``` case aemResponse ``` |

Modified AVB17221AECPMessageType.legacyAVCCommand

|  | Declaration |
| --- | --- |
| From | ``` case LegacyAVCCommand ``` |
| To | ``` case legacyAVCCommand ``` |

Modified AVB17221AECPMessageType.legacyAVCResponse

|  | Declaration |
| --- | --- |
| From | ``` case LegacyAVCResponse ``` |
| To | ``` case legacyAVCResponse ``` |

Modified AVB17221AECPMessageType.vendorUniqueCommand

|  | Declaration |
| --- | --- |
| From | ``` case VendorUniqueCommand ``` |
| To | ``` case vendorUniqueCommand ``` |

Modified AVB17221AECPMessageType.vendorUniqueResponse

|  | Declaration |
| --- | --- |
| From | ``` case VendorUniqueResponse ``` |
| To | ``` case vendorUniqueResponse ``` |

Modified AVB17221AECPStatusCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221AECPStatusCode : UInt8 {     case Success     case NotImplemented     case NoSuchDescriptor     case EntityLocked     case EntityAcquired     case NotAuthorized     case InsufficientPrivileges     case BadArguments     case NoResources     case InProgress     case EntityMisbehaving     case NotSupported     case StreamIsRunning     static var AddressAccessAddressTooLow: AVB17221AECPStatusCode { get }     static var AddressAccessAddressTooHigh: AVB17221AECPStatusCode { get }     static var AddressAccessAddressInvalid: AVB17221AECPStatusCode { get }     static var AddressAccessTLVInvalid: AVB17221AECPStatusCode { get }     static var AddressAccessDataInvalid: AVB17221AECPStatusCode { get }     static var AddressAccessUnsupported: AVB17221AECPStatusCode { get }     static var AVCFailure: AVB17221AECPStatusCode { get } } ``` |
| To | ``` enum AVB17221AECPStatusCode : UInt8 {     case success     case notImplemented     case noSuchDescriptor     case entityLocked     case entityAcquired     case notAuthorized     case insufficientPrivileges     case badArguments     case noResources     case inProgress     case entityMisbehaving     case notSupported     case streamIsRunning     static var addressAccessAddressTooLow: AVB17221AECPStatusCode { get }     static var addressAccessAddressTooHigh: AVB17221AECPStatusCode { get }     static var addressAccessAddressInvalid: AVB17221AECPStatusCode { get }     static var addressAccessTLVInvalid: AVB17221AECPStatusCode { get }     static var addressAccessDataInvalid: AVB17221AECPStatusCode { get }     static var addressAccessUnsupported: AVB17221AECPStatusCode { get }     static var avcFailure: AVB17221AECPStatusCode { get } } ``` |

Modified AVB17221AECPStatusCode.addressAccessAddressInvalid

|  | Declaration |
| --- | --- |
| From | ``` static var AddressAccessAddressInvalid: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var addressAccessAddressInvalid: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.addressAccessAddressTooHigh

|  | Declaration |
| --- | --- |
| From | ``` static var AddressAccessAddressTooHigh: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var addressAccessAddressTooHigh: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.addressAccessAddressTooLow

|  | Declaration |
| --- | --- |
| From | ``` static var AddressAccessAddressTooLow: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var addressAccessAddressTooLow: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.addressAccessDataInvalid

|  | Declaration |
| --- | --- |
| From | ``` static var AddressAccessDataInvalid: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var addressAccessDataInvalid: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.addressAccessTLVInvalid

|  | Declaration |
| --- | --- |
| From | ``` static var AddressAccessTLVInvalid: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var addressAccessTLVInvalid: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.addressAccessUnsupported

|  | Declaration |
| --- | --- |
| From | ``` static var AddressAccessUnsupported: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var addressAccessUnsupported: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.avcFailure

|  | Declaration |
| --- | --- |
| From | ``` static var AVCFailure: AVB17221AECPStatusCode { get } ``` |
| To | ``` static var avcFailure: AVB17221AECPStatusCode { get } ``` |

Modified AVB17221AECPStatusCode.badArguments

|  | Declaration |
| --- | --- |
| From | ``` case BadArguments ``` |
| To | ``` case badArguments ``` |

Modified AVB17221AECPStatusCode.entityAcquired

|  | Declaration |
| --- | --- |
| From | ``` case EntityAcquired ``` |
| To | ``` case entityAcquired ``` |

Modified AVB17221AECPStatusCode.entityLocked

|  | Declaration |
| --- | --- |
| From | ``` case EntityLocked ``` |
| To | ``` case entityLocked ``` |

Modified AVB17221AECPStatusCode.entityMisbehaving

|  | Declaration |
| --- | --- |
| From | ``` case EntityMisbehaving ``` |
| To | ``` case entityMisbehaving ``` |

Modified AVB17221AECPStatusCode.inProgress

|  | Declaration |
| --- | --- |
| From | ``` case InProgress ``` |
| To | ``` case inProgress ``` |

Modified AVB17221AECPStatusCode.insufficientPrivileges

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientPrivileges ``` |
| To | ``` case insufficientPrivileges ``` |

Modified AVB17221AECPStatusCode.noResources

|  | Declaration |
| --- | --- |
| From | ``` case NoResources ``` |
| To | ``` case noResources ``` |

Modified AVB17221AECPStatusCode.noSuchDescriptor

|  | Declaration |
| --- | --- |
| From | ``` case NoSuchDescriptor ``` |
| To | ``` case noSuchDescriptor ``` |

Modified AVB17221AECPStatusCode.notAuthorized

|  | Declaration |
| --- | --- |
| From | ``` case NotAuthorized ``` |
| To | ``` case notAuthorized ``` |

Modified AVB17221AECPStatusCode.notImplemented

|  | Declaration |
| --- | --- |
| From | ``` case NotImplemented ``` |
| To | ``` case notImplemented ``` |

Modified AVB17221AECPStatusCode.notSupported

|  | Declaration |
| --- | --- |
| From | ``` case NotSupported ``` |
| To | ``` case notSupported ``` |

Modified AVB17221AECPStatusCode.streamIsRunning

|  | Declaration |
| --- | --- |
| From | ``` case StreamIsRunning ``` |
| To | ``` case streamIsRunning ``` |

Modified AVB17221AECPStatusCode.success

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified AVB17221AECPVendorMessage

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPVendorMessage : AVB17221AECPMessage {     var protocolID: UInt64     @NSCopying var protocolSpecificData: NSData? } ``` |
| To | ``` class AVB17221AECPVendorMessage : AVB17221AECPMessage {     var protocolID: UInt64     var protocolSpecificData: Data? } ``` |

Modified AVB17221AECPVendorMessage.protocolSpecificData

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var protocolSpecificData: NSData? ``` |
| To | ``` var protocolSpecificData: Data? ``` |

Modified AVB17221AEMCommandType [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum AVB17221AEMCommandType : UInt16 {     case AcquireEntity     case LockEntity     case EntityAvailable     case ControllerAvailable     case ReadDescriptor     case WriteDescriptor     case SetConfiguration     case GetConfiguration     case SetStreamFormat     case GetStreamFormat     case SetVideoFormat     case GetVideoFormat     case SetSensorFormat     case GetSensorFormat     case SetStreamInfo     case GetStreamInfo     case SetName     case GetName     case SetAssociationID     case GetAssociationID     case SetSamplingRate     case GetSamplingRate     case SetClockSource     case GetClockSource     case SetControl     case GetControl     case IncrementControl     case DecrementControl     case SetSignalSelector     case GetSignalSelector     case SetMixer     case GetMixer     case SetMatrix     case GetMatrix     case StartStreaming     case StopStreaming     case RegisterUnsolicitedNotification     case DeregisterUnsolicitedNotification     case IdentifyNotification     case GetAVBInfo     case GetASPath     case GetCounters     case Reboot     case GetAudioMap     case AddAudioMapping     case RemoveAudioMapping     case GetVideoMap     case AddVideoMapping     case RemoveVideoMapping     case GetSensorMap     case AddSensorMapping     case RemoveSensorMapping     case StartOperation     case AbortOperation     case OperationStatus     case AuthenticateAddKey     case AuthenticateDeleteKey     case AuthenticateGetKeyList     case AuthenticateGetKey     case AuthenticateAddKeyToChain     case AuthenticateDeleteKeyFromChain     case AuthenticateGetKeychainList     case AuthenticateGetIdentity     case AuthenticateAddToken     case AuthenticateDeleteToken     case Authenticate     case Deauthenticate     case EnableTransportSecurity     case DisableTransportSecurity     case EnableStreamEncryption     case DisableStreamEncryption     case SetMemoryObjectLength     case GetMemoryObjectLength     case SetStreamBackup     case GetStreamBackup } ``` |
| To | ``` enum AVB17221AEMCommandType : UInt16 {     case acquireEntity     case lockEntity     case entityAvailable     case controllerAvailable     case readDescriptor     case writeDescriptor     case setConfiguration     case getConfiguration     case setStreamFormat     case getStreamFormat     case setVideoFormat     case getVideoFormat     case setSensorFormat     case getSensorFormat     case setStreamInfo     case getStreamInfo     case setName     case getName     case setAssociationID     case getAssociationID     case setSamplingRate     case getSamplingRate     case setClockSource     case getClockSource     case setControl     case getControl     case incrementControl     case decrementControl     case setSignalSelector     case getSignalSelector     case setMixer     case getMixer     case setMatrix     case getMatrix     case startStreaming     case stopStreaming     case registerUnsolicitedNotification     case deregisterUnsolicitedNotification     case identifyNotification     case getAVBInfo     case getASPath     case getCounters     case reboot     case getAudioMap     case addAudioMapping     case removeAudioMapping     case getVideoMap     case addVideoMapping     case removeVideoMapping     case getSensorMap     case addSensorMapping     case removeSensorMapping     case startOperation     case abortOperation     case operationStatus     case authenticateAddKey     case authenticateDeleteKey     case authenticateGetKeyList     case authenticateGetKey     case authenticateAddKeyToChain     case authenticateDeleteKeyFromChain     case authenticateGetKeychainList     case authenticateGetIdentity     case authenticateAddToken     case authenticateDeleteToken     case authenticate     case deauthenticate     case enableTransportSecurity     case disableTransportSecurity     case enableStreamEncryption     case disableStreamEncryption     case setMemoryObjectLength     case getMemoryObjectLength     case setStreamBackup     case getStreamBackup } ``` |

Modified AVB17221AEMCommandType.abortOperation

|  | Declaration |
| --- | --- |
| From | ``` case AbortOperation ``` |
| To | ``` case abortOperation ``` |

Modified AVB17221AEMCommandType.acquireEntity

|  | Declaration |
| --- | --- |
| From | ``` case AcquireEntity ``` |
| To | ``` case acquireEntity ``` |

Modified AVB17221AEMCommandType.addAudioMapping

|  | Declaration |
| --- | --- |
| From | ``` case AddAudioMapping ``` |
| To | ``` case addAudioMapping ``` |

Modified AVB17221AEMCommandType.addSensorMapping

|  | Declaration |
| --- | --- |
| From | ``` case AddSensorMapping ``` |
| To | ``` case addSensorMapping ``` |

Modified AVB17221AEMCommandType.addVideoMapping

|  | Declaration |
| --- | --- |
| From | ``` case AddVideoMapping ``` |
| To | ``` case addVideoMapping ``` |

Modified AVB17221AEMCommandType.authenticate

|  | Declaration |
| --- | --- |
| From | ``` case Authenticate ``` |
| To | ``` case authenticate ``` |

Modified AVB17221AEMCommandType.authenticateAddKey

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateAddKey ``` |
| To | ``` case authenticateAddKey ``` |

Modified AVB17221AEMCommandType.authenticateAddKeyToChain

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateAddKeyToChain ``` |
| To | ``` case authenticateAddKeyToChain ``` |

Modified AVB17221AEMCommandType.authenticateAddToken

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateAddToken ``` |
| To | ``` case authenticateAddToken ``` |

Modified AVB17221AEMCommandType.authenticateDeleteKey

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateDeleteKey ``` |
| To | ``` case authenticateDeleteKey ``` |

Modified AVB17221AEMCommandType.authenticateDeleteKeyFromChain

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateDeleteKeyFromChain ``` |
| To | ``` case authenticateDeleteKeyFromChain ``` |

Modified AVB17221AEMCommandType.authenticateDeleteToken

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateDeleteToken ``` |
| To | ``` case authenticateDeleteToken ``` |

Modified AVB17221AEMCommandType.authenticateGetIdentity

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateGetIdentity ``` |
| To | ``` case authenticateGetIdentity ``` |

Modified AVB17221AEMCommandType.authenticateGetKey

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateGetKey ``` |
| To | ``` case authenticateGetKey ``` |

Modified AVB17221AEMCommandType.authenticateGetKeychainList

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateGetKeychainList ``` |
| To | ``` case authenticateGetKeychainList ``` |

Modified AVB17221AEMCommandType.authenticateGetKeyList

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticateGetKeyList ``` |
| To | ``` case authenticateGetKeyList ``` |

Modified AVB17221AEMCommandType.controllerAvailable

|  | Declaration |
| --- | --- |
| From | ``` case ControllerAvailable ``` |
| To | ``` case controllerAvailable ``` |

Modified AVB17221AEMCommandType.deauthenticate

|  | Declaration |
| --- | --- |
| From | ``` case Deauthenticate ``` |
| To | ``` case deauthenticate ``` |

Modified AVB17221AEMCommandType.decrementControl

|  | Declaration |
| --- | --- |
| From | ``` case DecrementControl ``` |
| To | ``` case decrementControl ``` |

Modified AVB17221AEMCommandType.deregisterUnsolicitedNotification

|  | Declaration |
| --- | --- |
| From | ``` case DeregisterUnsolicitedNotification ``` |
| To | ``` case deregisterUnsolicitedNotification ``` |

Modified AVB17221AEMCommandType.disableStreamEncryption

|  | Declaration |
| --- | --- |
| From | ``` case DisableStreamEncryption ``` |
| To | ``` case disableStreamEncryption ``` |

Modified AVB17221AEMCommandType.disableTransportSecurity

|  | Declaration |
| --- | --- |
| From | ``` case DisableTransportSecurity ``` |
| To | ``` case disableTransportSecurity ``` |

Modified AVB17221AEMCommandType.enableStreamEncryption

|  | Declaration |
| --- | --- |
| From | ``` case EnableStreamEncryption ``` |
| To | ``` case enableStreamEncryption ``` |

Modified AVB17221AEMCommandType.enableTransportSecurity

|  | Declaration |
| --- | --- |
| From | ``` case EnableTransportSecurity ``` |
| To | ``` case enableTransportSecurity ``` |

Modified AVB17221AEMCommandType.entityAvailable

|  | Declaration |
| --- | --- |
| From | ``` case EntityAvailable ``` |
| To | ``` case entityAvailable ``` |

Modified AVB17221AEMCommandType.getASPath

|  | Declaration |
| --- | --- |
| From | ``` case GetASPath ``` |
| To | ``` case getASPath ``` |

Modified AVB17221AEMCommandType.getAssociationID

|  | Declaration |
| --- | --- |
| From | ``` case GetAssociationID ``` |
| To | ``` case getAssociationID ``` |

Modified AVB17221AEMCommandType.getAudioMap

|  | Declaration |
| --- | --- |
| From | ``` case GetAudioMap ``` |
| To | ``` case getAudioMap ``` |

Modified AVB17221AEMCommandType.getAVBInfo

|  | Declaration |
| --- | --- |
| From | ``` case GetAVBInfo ``` |
| To | ``` case getAVBInfo ``` |

Modified AVB17221AEMCommandType.getClockSource

|  | Declaration |
| --- | --- |
| From | ``` case GetClockSource ``` |
| To | ``` case getClockSource ``` |

Modified AVB17221AEMCommandType.getConfiguration

|  | Declaration |
| --- | --- |
| From | ``` case GetConfiguration ``` |
| To | ``` case getConfiguration ``` |

Modified AVB17221AEMCommandType.getControl

|  | Declaration |
| --- | --- |
| From | ``` case GetControl ``` |
| To | ``` case getControl ``` |

Modified AVB17221AEMCommandType.getCounters

|  | Declaration |
| --- | --- |
| From | ``` case GetCounters ``` |
| To | ``` case getCounters ``` |

Modified AVB17221AEMCommandType.getMatrix

|  | Declaration |
| --- | --- |
| From | ``` case GetMatrix ``` |
| To | ``` case getMatrix ``` |

Modified AVB17221AEMCommandType.getMemoryObjectLength

|  | Declaration |
| --- | --- |
| From | ``` case GetMemoryObjectLength ``` |
| To | ``` case getMemoryObjectLength ``` |

Modified AVB17221AEMCommandType.getMixer

|  | Declaration |
| --- | --- |
| From | ``` case GetMixer ``` |
| To | ``` case getMixer ``` |

Modified AVB17221AEMCommandType.getName

|  | Declaration |
| --- | --- |
| From | ``` case GetName ``` |
| To | ``` case getName ``` |

Modified AVB17221AEMCommandType.getSamplingRate

|  | Declaration |
| --- | --- |
| From | ``` case GetSamplingRate ``` |
| To | ``` case getSamplingRate ``` |

Modified AVB17221AEMCommandType.getSensorFormat

|  | Declaration |
| --- | --- |
| From | ``` case GetSensorFormat ``` |
| To | ``` case getSensorFormat ``` |

Modified AVB17221AEMCommandType.getSensorMap

|  | Declaration |
| --- | --- |
| From | ``` case GetSensorMap ``` |
| To | ``` case getSensorMap ``` |

Modified AVB17221AEMCommandType.getSignalSelector

|  | Declaration |
| --- | --- |
| From | ``` case GetSignalSelector ``` |
| To | ``` case getSignalSelector ``` |

Modified AVB17221AEMCommandType.getStreamBackup

|  | Declaration |
| --- | --- |
| From | ``` case GetStreamBackup ``` |
| To | ``` case getStreamBackup ``` |

Modified AVB17221AEMCommandType.getStreamFormat

|  | Declaration |
| --- | --- |
| From | ``` case GetStreamFormat ``` |
| To | ``` case getStreamFormat ``` |

Modified AVB17221AEMCommandType.getStreamInfo

|  | Declaration |
| --- | --- |
| From | ``` case GetStreamInfo ``` |
| To | ``` case getStreamInfo ``` |

Modified AVB17221AEMCommandType.getVideoFormat

|  | Declaration |
| --- | --- |
| From | ``` case GetVideoFormat ``` |
| To | ``` case getVideoFormat ``` |

Modified AVB17221AEMCommandType.getVideoMap

|  | Declaration |
| --- | --- |
| From | ``` case GetVideoMap ``` |
| To | ``` case getVideoMap ``` |

Modified AVB17221AEMCommandType.identifyNotification

|  | Declaration |
| --- | --- |
| From | ``` case IdentifyNotification ``` |
| To | ``` case identifyNotification ``` |

Modified AVB17221AEMCommandType.incrementControl

|  | Declaration |
| --- | --- |
| From | ``` case IncrementControl ``` |
| To | ``` case incrementControl ``` |

Modified AVB17221AEMCommandType.lockEntity

|  | Declaration |
| --- | --- |
| From | ``` case LockEntity ``` |
| To | ``` case lockEntity ``` |

Modified AVB17221AEMCommandType.operationStatus

|  | Declaration |
| --- | --- |
| From | ``` case OperationStatus ``` |
| To | ``` case operationStatus ``` |

Modified AVB17221AEMCommandType.readDescriptor

|  | Declaration |
| --- | --- |
| From | ``` case ReadDescriptor ``` |
| To | ``` case readDescriptor ``` |

Modified AVB17221AEMCommandType.reboot

|  | Declaration |
| --- | --- |
| From | ``` case Reboot ``` |
| To | ``` case reboot ``` |

Modified AVB17221AEMCommandType.registerUnsolicitedNotification

|  | Declaration |
| --- | --- |
| From | ``` case RegisterUnsolicitedNotification ``` |
| To | ``` case registerUnsolicitedNotification ``` |

Modified AVB17221AEMCommandType.removeAudioMapping

|  | Declaration |
| --- | --- |
| From | ``` case RemoveAudioMapping ``` |
| To | ``` case removeAudioMapping ``` |

Modified AVB17221AEMCommandType.removeSensorMapping

|  | Declaration |
| --- | --- |
| From | ``` case RemoveSensorMapping ``` |
| To | ``` case removeSensorMapping ``` |

Modified AVB17221AEMCommandType.removeVideoMapping

|  | Declaration |
| --- | --- |
| From | ``` case RemoveVideoMapping ``` |
| To | ``` case removeVideoMapping ``` |

Modified AVB17221AEMCommandType.setAssociationID

|  | Declaration |
| --- | --- |
| From | ``` case SetAssociationID ``` |
| To | ``` case setAssociationID ``` |

Modified AVB17221AEMCommandType.setClockSource

|  | Declaration |
| --- | --- |
| From | ``` case SetClockSource ``` |
| To | ``` case setClockSource ``` |

Modified AVB17221AEMCommandType.setConfiguration

|  | Declaration |
| --- | --- |
| From | ``` case SetConfiguration ``` |
| To | ``` case setConfiguration ``` |

Modified AVB17221AEMCommandType.setControl

|  | Declaration |
| --- | --- |
| From | ``` case SetControl ``` |
| To | ``` case setControl ``` |

Modified AVB17221AEMCommandType.setMatrix

|  | Declaration |
| --- | --- |
| From | ``` case SetMatrix ``` |
| To | ``` case setMatrix ``` |

Modified AVB17221AEMCommandType.setMemoryObjectLength

|  | Declaration |
| --- | --- |
| From | ``` case SetMemoryObjectLength ``` |
| To | ``` case setMemoryObjectLength ``` |

Modified AVB17221AEMCommandType.setMixer

|  | Declaration |
| --- | --- |
| From | ``` case SetMixer ``` |
| To | ``` case setMixer ``` |

Modified AVB17221AEMCommandType.setName

|  | Declaration |
| --- | --- |
| From | ``` case SetName ``` |
| To | ``` case setName ``` |

Modified AVB17221AEMCommandType.setSamplingRate

|  | Declaration |
| --- | --- |
| From | ``` case SetSamplingRate ``` |
| To | ``` case setSamplingRate ``` |

Modified AVB17221AEMCommandType.setSensorFormat

|  | Declaration |
| --- | --- |
| From | ``` case SetSensorFormat ``` |
| To | ``` case setSensorFormat ``` |

Modified AVB17221AEMCommandType.setSignalSelector

|  | Declaration |
| --- | --- |
| From | ``` case SetSignalSelector ``` |
| To | ``` case setSignalSelector ``` |

Modified AVB17221AEMCommandType.setStreamBackup

|  | Declaration |
| --- | --- |
| From | ``` case SetStreamBackup ``` |
| To | ``` case setStreamBackup ``` |

Modified AVB17221AEMCommandType.setStreamFormat

|  | Declaration |
| --- | --- |
| From | ``` case SetStreamFormat ``` |
| To | ``` case setStreamFormat ``` |

Modified AVB17221AEMCommandType.setStreamInfo

|  | Declaration |
| --- | --- |
| From | ``` case SetStreamInfo ``` |
| To | ``` case setStreamInfo ``` |

Modified AVB17221AEMCommandType.setVideoFormat

|  | Declaration |
| --- | --- |
| From | ``` case SetVideoFormat ``` |
| To | ``` case setVideoFormat ``` |

Modified AVB17221AEMCommandType.startOperation

|  | Declaration |
| --- | --- |
| From | ``` case StartOperation ``` |
| To | ``` case startOperation ``` |

Modified AVB17221AEMCommandType.startStreaming

|  | Declaration |
| --- | --- |
| From | ``` case StartStreaming ``` |
| To | ``` case startStreaming ``` |

Modified AVB17221AEMCommandType.stopStreaming

|  | Declaration |
| --- | --- |
| From | ``` case StopStreaming ``` |
| To | ``` case stopStreaming ``` |

Modified AVB17221AEMCommandType.writeDescriptor

|  | Declaration |
| --- | --- |
| From | ``` case WriteDescriptor ``` |
| To | ``` case writeDescriptor ``` |

Modified AVB17221Entity

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVB17221Entity : NSObject {     var localEntity: Bool     var timeToLive: UInt8     var guid: UInt64     var entityID: UInt64     var vendorID: UInt32     var modelID: UInt32     var entityModelID: UInt64     var entityCapabilities: AVB17221ADPEntityCapabilities     var talkerStreamSources: UInt16     var talkerCapabilities: AVB17221ADPTalkerCapabilities     var listenerStreamSinks: UInt16     var listenerCapabilities: AVB17221ADPListenerCapabilities     var controllerCapabilities: AVB17221ADPControllerCapabilities     var availableIndex: UInt32     var asGrandmasterID: UInt64     var gPTPGrandmasterID: UInt64     var gPTPDomainNumber: UInt8     var identifyControlIndex: UInt16     var interfaceIndex: UInt16     var associationID: UInt64     var macAddresses: [AVBMACAddress]     unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery? } ``` | -- |
| To | ``` class AVB17221Entity : NSObject {     var isLocalEntity: Bool     var timeToLive: UInt8     var guid: UInt64     var entityID: UInt64     var vendorID: UInt32     var modelID: UInt32     var entityModelID: UInt64     var entityCapabilities: AVB17221ADPEntityCapabilities     var talkerStreamSources: UInt16     var talkerCapabilities: AVB17221ADPTalkerCapabilities     var listenerStreamSinks: UInt16     var listenerCapabilities: AVB17221ADPListenerCapabilities     var controllerCapabilities: AVB17221ADPControllerCapabilities     var availableIndex: UInt32     var asGrandmasterID: UInt64     var gPTPGrandmasterID: UInt64     var gPTPDomainNumber: UInt8     var identifyControlIndex: UInt16     var interfaceIndex: UInt16     var associationID: UInt64     var macAddresses: [AVBMACAddress]     unowned(unsafe) var entityDiscovery: AVB17221EntityDiscovery?     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVB17221Entity : CVarArg { } extension AVB17221Entity : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified AVB17221Entity.isLocalEntity

|  | Declaration |
| --- | --- |
| From | ``` var localEntity: Bool ``` |
| To | ``` var isLocalEntity: Bool ``` |

Modified AVB17221EntityDiscovery

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVB17221EntityDiscovery : NSObject {     var interfaceName: String     unowned(unsafe) var interface: AVBInterface? { get }     unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate?     init(interfaceName anInterfaceName: String)     func primeIterators()     func discoverEntities() -> Bool     func discoverEntity(_ entityID: UInt64) -> Bool     func addLocalEntity(_ anEntity: AVB17221Entity) throws     func removeLocalEntity(_ guid: UInt64) throws     func changeEntityWithGUID(_ entityGUID: UInt64, toNewASGrandmasterID asGrandmasterID: UInt64) throws     func changeEntityWithEntityID(_ entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64) throws } ``` | -- |
| To | ``` class AVB17221EntityDiscovery : NSObject {     var interfaceName: String     unowned(unsafe) var interface: AVBInterface? { get }     unowned(unsafe) var discoveryDelegate: AVB17221EntityDiscoveryDelegate?     init(interfaceName anInterfaceName: String)     func primeIterators()     func discoverEntities() -> Bool     func discoverEntity(_ entityID: UInt64) -> Bool     func addLocalEntity(_ anEntity: AVB17221Entity) throws     func removeLocalEntity(_ guid: UInt64) throws     func changeEntity(withGUID entityGUID: UInt64, toNewASGrandmasterID asGrandmasterID: UInt64) throws     func changeEntity(withEntityID entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64) throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVB17221EntityDiscovery : CVarArg { } extension AVB17221EntityDiscovery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified AVB17221EntityDiscovery.changeEntity(withEntityID: UInt64, toNewGPTPGrandmasterID: UInt64) throws

|  | Declaration |
| --- | --- |
| From | ``` func changeEntityWithEntityID(_ entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64) throws ``` |
| To | ``` func changeEntity(withEntityID entityID: UInt64, toNewGPTPGrandmasterID gPTPGrandmasterID: UInt64) throws ``` |

Modified AVB17221EntityPropertyChanged [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AVB17221EntityPropertyChanged : OptionSetType {     init(rawValue rawValue: UInt)     static var TimeToLive: AVB17221EntityPropertyChanged { get }     static var GUID: AVB17221EntityPropertyChanged { get }     static var EntityID: AVB17221EntityPropertyChanged { get }     static var VendorID: AVB17221EntityPropertyChanged { get }     static var ModelID: AVB17221EntityPropertyChanged { get }     static var EntityCapabilities: AVB17221EntityPropertyChanged { get }     static var TalkerStreamSources: AVB17221EntityPropertyChanged { get }     static var TalkerCapabilities: AVB17221EntityPropertyChanged { get }     static var ListenerStreamSinks: AVB17221EntityPropertyChanged { get }     static var ListenerCapabilities: AVB17221EntityPropertyChanged { get }     static var ControllerCapabilities: AVB17221EntityPropertyChanged { get }     static var AvailableIndex: AVB17221EntityPropertyChanged { get }     static var ASGrandmasterID: AVB17221EntityPropertyChanged { get }     static var GPTPGrandmasterID: AVB17221EntityPropertyChanged { get }     static var MACAddress: AVB17221EntityPropertyChanged { get }     static var AssociationID: AVB17221EntityPropertyChanged { get }     static var EntityType: AVB17221EntityPropertyChanged { get }     static var IdentifyControlIndex: AVB17221EntityPropertyChanged { get }     static var InterfaceIndex: AVB17221EntityPropertyChanged { get }     static var GPTPDomainNumber: AVB17221EntityPropertyChanged { get } } ``` | OptionSetType |
| To | ``` struct AVB17221EntityPropertyChanged : OptionSet {     init(rawValue rawValue: UInt)     static var timeToLive: AVB17221EntityPropertyChanged { get }     static var GUID: AVB17221EntityPropertyChanged { get }     static var entityID: AVB17221EntityPropertyChanged { get }     static var vendorID: AVB17221EntityPropertyChanged { get }     static var modelID: AVB17221EntityPropertyChanged { get }     static var entityCapabilities: AVB17221EntityPropertyChanged { get }     static var talkerStreamSources: AVB17221EntityPropertyChanged { get }     static var talkerCapabilities: AVB17221EntityPropertyChanged { get }     static var listenerStreamSinks: AVB17221EntityPropertyChanged { get }     static var listenerCapabilities: AVB17221EntityPropertyChanged { get }     static var controllerCapabilities: AVB17221EntityPropertyChanged { get }     static var availableIndex: AVB17221EntityPropertyChanged { get }     static var asGrandmasterID: AVB17221EntityPropertyChanged { get }     static var gptpGrandmasterID: AVB17221EntityPropertyChanged { get }     static var macAddress: AVB17221EntityPropertyChanged { get }     static var associationID: AVB17221EntityPropertyChanged { get }     static var entityType: AVB17221EntityPropertyChanged { get }     static var identifyControlIndex: AVB17221EntityPropertyChanged { get }     static var interfaceIndex: AVB17221EntityPropertyChanged { get }     static var gptpDomainNumber: AVB17221EntityPropertyChanged { get }     func intersect(_ other: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged     func exclusiveOr(_ other: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged     mutating func unionInPlace(_ other: AVB17221EntityPropertyChanged)     mutating func intersectInPlace(_ other: AVB17221EntityPropertyChanged)     mutating func exclusiveOrInPlace(_ other: AVB17221EntityPropertyChanged)     func isSubsetOf(_ other: AVB17221EntityPropertyChanged) -> Bool     func isDisjointWith(_ other: AVB17221EntityPropertyChanged) -> Bool     func isSupersetOf(_ other: AVB17221EntityPropertyChanged) -> Bool     mutating func subtractInPlace(_ other: AVB17221EntityPropertyChanged)     func isStrictSupersetOf(_ other: AVB17221EntityPropertyChanged) -> Bool     func isStrictSubsetOf(_ other: AVB17221EntityPropertyChanged) -> Bool } extension AVB17221EntityPropertyChanged {     func union(_ other: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged     func intersection(_ other: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged     func symmetricDifference(_ other: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged } extension AVB17221EntityPropertyChanged {     func contains(_ member: AVB17221EntityPropertyChanged) -> Bool     mutating func insert(_ newMember: AVB17221EntityPropertyChanged) -> (inserted: Bool, memberAfterInsert: AVB17221EntityPropertyChanged)     mutating func remove(_ member: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged?     mutating func update(with newMember: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged? } extension AVB17221EntityPropertyChanged {     convenience init()     mutating func formUnion(_ other: AVB17221EntityPropertyChanged)     mutating func formIntersection(_ other: AVB17221EntityPropertyChanged)     mutating func formSymmetricDifference(_ other: AVB17221EntityPropertyChanged) } extension AVB17221EntityPropertyChanged {     convenience init<S : Sequence where S.Iterator.Element == AVB17221EntityPropertyChanged>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: AVB17221EntityPropertyChanged...)     mutating func subtract(_ other: AVB17221EntityPropertyChanged)     func isSubset(of other: AVB17221EntityPropertyChanged) -> Bool     func isSuperset(of other: AVB17221EntityPropertyChanged) -> Bool     func isDisjoint(with other: AVB17221EntityPropertyChanged) -> Bool     func subtracting(_ other: AVB17221EntityPropertyChanged) -> AVB17221EntityPropertyChanged     var isEmpty: Bool { get }     func isStrictSuperset(of other: AVB17221EntityPropertyChanged) -> Bool     func isStrictSubset(of other: AVB17221EntityPropertyChanged) -> Bool } ``` | OptionSet |

Modified AVB17221EntityPropertyChanged.associationID

|  | Declaration |
| --- | --- |
| From | ``` static var AssociationID: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var associationID: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.availableIndex

|  | Declaration |
| --- | --- |
| From | ``` static var AvailableIndex: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var availableIndex: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.controllerCapabilities

|  | Declaration |
| --- | --- |
| From | ``` static var ControllerCapabilities: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var controllerCapabilities: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.entityCapabilities

|  | Declaration |
| --- | --- |
| From | ``` static var EntityCapabilities: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var entityCapabilities: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.entityID

|  | Declaration |
| --- | --- |
| From | ``` static var EntityID: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var entityID: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.entityType

|  | Declaration |
| --- | --- |
| From | ``` static var EntityType: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var entityType: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.gptpDomainNumber

|  | Declaration |
| --- | --- |
| From | ``` static var GPTPDomainNumber: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var gptpDomainNumber: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.gptpGrandmasterID

|  | Declaration |
| --- | --- |
| From | ``` static var GPTPGrandmasterID: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var gptpGrandmasterID: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.identifyControlIndex

|  | Declaration |
| --- | --- |
| From | ``` static var IdentifyControlIndex: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var identifyControlIndex: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.interfaceIndex

|  | Declaration |
| --- | --- |
| From | ``` static var InterfaceIndex: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var interfaceIndex: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.listenerCapabilities

|  | Declaration |
| --- | --- |
| From | ``` static var ListenerCapabilities: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var listenerCapabilities: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.listenerStreamSinks

|  | Declaration |
| --- | --- |
| From | ``` static var ListenerStreamSinks: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var listenerStreamSinks: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.macAddress

|  | Declaration |
| --- | --- |
| From | ``` static var MACAddress: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var macAddress: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.modelID

|  | Declaration |
| --- | --- |
| From | ``` static var ModelID: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var modelID: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.talkerCapabilities

|  | Declaration |
| --- | --- |
| From | ``` static var TalkerCapabilities: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var talkerCapabilities: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.talkerStreamSources

|  | Declaration |
| --- | --- |
| From | ``` static var TalkerStreamSources: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var talkerStreamSources: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.timeToLive

|  | Declaration |
| --- | --- |
| From | ``` static var TimeToLive: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var timeToLive: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB17221EntityPropertyChanged.vendorID

|  | Declaration |
| --- | --- |
| From | ``` static var VendorID: AVB17221EntityPropertyChanged { get } ``` |
| To | ``` static var vendorID: AVB17221EntityPropertyChanged { get } ``` |

Modified AVB1722ControlInterface

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVB1722ControlInterface : NSObject {     var interfaceName: String { get }     unowned(unsafe) var interface: AVBInterface? { get }     init()     init?(interfaceName anInterfaceName: String)     init?(interface anInterface: AVBInterface) } ``` | -- |
| To | ``` class AVB1722ControlInterface : NSObject {     var interfaceName: String { get }     unowned(unsafe) var interface: AVBInterface? { get }     init()     init?(interfaceName anInterfaceName: String)     init?(interface anInterface: AVBInterface)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVB1722ControlInterface : CVarArg { } extension AVB1722ControlInterface : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified AVBCentralManager

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVBCentralManager : NSObject {     func startControllerMatching()     func didAddInterface(_ interface: AVBInterface)     func didRemoveInterface(_ interface: AVBInterface)     func streamingEnabledInterfacesOnly() -> Bool     class func nextAvailableDynamicEntityID() -> UInt64     class func releaseDynamicEntityID(_ entityID: UInt64)     class func nextAvailableDynamicEntityModelID() -> UInt64     class func releaseDynamicEntityModelID(_ entityModelID: UInt64) } ``` | -- |
| To | ``` class AVBCentralManager : NSObject {     func startControllerMatching()     func didAdd(_ interface: AVBInterface)     func didRemove(_ interface: AVBInterface)     func streamingEnabledInterfacesOnly() -> Bool     class func nextAvailableDynamicEntityID() -> UInt64     class func releaseDynamicEntityID(_ entityID: UInt64)     class func nextAvailableDynamicEntityModelID() -> UInt64     class func releaseDynamicEntityModelID(_ entityModelID: UInt64)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVBCentralManager : CVarArg { } extension AVBCentralManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified AVBCentralManager.didAdd(_: AVBInterface)

|  | Declaration |
| --- | --- |
| From | ``` func didAddInterface(_ interface: AVBInterface) ``` |
| To | ``` func didAdd(_ interface: AVBInterface) ``` |

Modified AVBCentralManager.didRemove(_: AVBInterface)

|  | Declaration |
| --- | --- |
| From | ``` func didRemoveInterface(_ interface: AVBInterface) ``` |
| To | ``` func didRemove(_ interface: AVBInterface) ``` |

Modified AVBInterface

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVBInterface : NSObject {     var interfaceName: String { get }     var entityDiscovery: AVB17221EntityDiscovery? { get }     var aecp: AVB17221AECPInterface? { get }     var acmp: AVB17221ACMPInterface? { get }     class func macAddressForInterfaceNamed(_ anInterfaceName: String) -> AVBMACAddress?     class func supportedInterfaces() -> [String]?     class func isAVBEnabledOnInterfaceNamed(_ anInterfaceName: String) -> Bool     class func isAVBCapableInterfaceNamed(_ anInterfaceName: String) -> Bool     init?(interfaceName anInterfaceName: String)     class func myGUID() -> UInt64     class func myEntityID() -> UInt64 } ``` | -- |
| To | ``` class AVBInterface : NSObject {     var interfaceName: String { get }     var entityDiscovery: AVB17221EntityDiscovery? { get }     var aecp: AVB17221AECPInterface? { get }     var acmp: AVB17221ACMPInterface? { get }     class func macAddress(forInterfaceNamed anInterfaceName: String) -> AVBMACAddress?     class func supportedInterfaces() -> [String]?     class func isAVBEnabled(onInterfaceNamed anInterfaceName: String) -> Bool     class func isAVBCapableInterfaceNamed(_ anInterfaceName: String) -> Bool     convenience init()     init?(interfaceName anInterfaceName: String)     class func myGUID() -> UInt64     class func myEntityID() -> UInt64     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVBInterface : CVarArg { } extension AVBInterface : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified AVBInterface.isAVBEnabled(onInterfaceNamed: String) -> Bool [class]

|  | Declaration |
| --- | --- |
| From | ``` class func isAVBEnabledOnInterfaceNamed(_ anInterfaceName: String) -> Bool ``` |
| To | ``` class func isAVBEnabled(onInterfaceNamed anInterfaceName: String) -> Bool ``` |

Modified AVBInterface.macAddress(forInterfaceNamed: String) -> AVBMACAddress? [class]

|  | Declaration |
| --- | --- |
| From | ``` class func macAddressForInterfaceNamed(_ anInterfaceName: String) -> AVBMACAddress? ``` |
| To | ``` class func macAddress(forInterfaceNamed anInterfaceName: String) -> AVBMACAddress? ``` |

Modified AVBMACAddress

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class AVBMACAddress : NSObject, NSCopying {     init(bytes bytes: UnsafePointer<UInt8>)     var bytes: UnsafePointer<UInt8> { get }     @NSCopying var dataRepresentation: NSData     var stringRepresentation: String     var multicast: Bool } ``` | NSCopying |
| To | ``` class AVBMACAddress : NSObject, NSCopying {     init(bytes bytes: UnsafePointer<UInt8>)     var bytes: UnsafePointer<UInt8> { get }     var dataRepresentation: Data     var stringRepresentation: String     var isMulticast: Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension AVBMACAddress : CVarArg { } extension AVBMACAddress : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified AVBMACAddress.dataRepresentation

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var dataRepresentation: NSData ``` |
| To | ``` var dataRepresentation: Data ``` |

Modified AVBMACAddress.isMulticast

|  | Declaration |
| --- | --- |
| From | ``` var multicast: Bool ``` |
| To | ``` var isMulticast: Bool ``` |

Modified AVB17221ACMPInterfaceCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias AVB17221ACMPInterfaceCompletion = (NSError?, AVB17221ACMPMessage) -> Void ``` |
| To | ``` typealias AVB17221ACMPInterfaceCompletion = (Error?, AVB17221ACMPMessage) -> Swift.Void ``` |

Modified AVB17221AECPInterfaceCompletion

|  | Declaration |
| --- | --- |
| From | ``` typealias AVB17221AECPInterfaceCompletion = (NSError?, AVB17221AECPMessage) -> Void ``` |
| To | ``` typealias AVB17221AECPInterfaceCompletion = (Error?, AVB17221AECPMessage) -> Swift.Void ``` |

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
