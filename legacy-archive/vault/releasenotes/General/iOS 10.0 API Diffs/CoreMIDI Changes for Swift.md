---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/CoreMIDI.html
archived_at: '2026-07-18T02:55:16.101670Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreMIDI Changes for Swift

### CoreMIDI

Removed MIDIDriverInterface.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Stop: ((MIDIDriverRef) -> OSStatus)!, Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)!, Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)!)Added MIDIDriverInterface.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, FindDevices: ( (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start: ( (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop: ( (MIDIDriverRef?) -> OSStatus)!, Configure: ( (MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send: ( (MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource: ( (MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush: ( (MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor: ( (MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!)Modified [MIDIDriverInterface [struct]](https://developer.apple.com/documentation/coremidi/mididriverinterface)

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!     var Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!     var Stop: ((MIDIDriverRef) -> OSStatus)!     var Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)!     var Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!     var EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!     var Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!     var Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, FindDevices FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Start Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: ((MIDIDriverRef) -> OSStatus)!, Configure Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)!, Send Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, EnableSource EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)!, Monitor Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)!) } ``` |
| To | ``` struct MIDIDriverInterface {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!     var Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!     var Stop: ((MIDIDriverRef?) -> OSStatus)!     var Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!     var Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!     var EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!     var Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!     var Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, FindDevices FindDevices: (@escaping (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Start Start: (@escaping (MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)!, Stop Stop: (@escaping (MIDIDriverRef?) -> OSStatus)!, Configure Configure: (@escaping (MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)!, Send Send: (@escaping (MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, EnableSource EnableSource: (@escaping (MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)!, Flush Flush: (@escaping (MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)!, Monitor Monitor: (@escaping (MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)!) } ``` |

Modified [MIDIDriverInterface.AddRef](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508512-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MIDIDriverInterface.Configure](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508254-configure)

|  | Declaration |
| --- | --- |
| From | ``` var Configure: ((MIDIDriverRef, MIDIDeviceRef) -> OSStatus)! ``` |
| To | ``` var Configure: ((MIDIDriverRef?, MIDIDeviceRef) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.EnableSource](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508318-enablesource)

|  | Declaration |
| --- | --- |
| From | ``` var EnableSource: ((MIDIDriverRef, MIDIEndpointRef, DarwinBoolean) -> OSStatus)! ``` |
| To | ``` var EnableSource: ((MIDIDriverRef?, MIDIEndpointRef, DarwinBoolean) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.FindDevices](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508437-finddevices)

|  | Declaration |
| --- | --- |
| From | ``` var FindDevices: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)! ``` |
| To | ``` var FindDevices: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Flush](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508514-flush)

|  | Declaration |
| --- | --- |
| From | ``` var Flush: ((MIDIDriverRef, MIDIEndpointRef, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)! ``` |
| To | ``` var Flush: ((MIDIDriverRef?, MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Monitor](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508375-monitor)

|  | Declaration |
| --- | --- |
| From | ``` var Monitor: ((MIDIDriverRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus)! ``` |
| To | ``` var Monitor: ((MIDIDriverRef?, MIDIEndpointRef, UnsafePointer<MIDIPacketList>?) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.QueryInterface](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508283-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [MIDIDriverInterface.Release](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508249-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [MIDIDriverInterface.Send](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508332-send)

|  | Declaration |
| --- | --- |
| From | ``` var Send: ((MIDIDriverRef, UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> OSStatus)! ``` |
| To | ``` var Send: ((MIDIDriverRef?, UnsafePointer<MIDIPacketList>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Start](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508269-start)

|  | Declaration |
| --- | --- |
| From | ``` var Start: ((MIDIDriverRef, MIDIDeviceListRef) -> OSStatus)! ``` |
| To | ``` var Start: ((MIDIDriverRef?, MIDIDeviceListRef) -> OSStatus)! ``` |

Modified [MIDIDriverInterface.Stop](https://developer.apple.com/documentation/coremidi/mididriverinterface/1508529-stop)

|  | Declaration |
| --- | --- |
| From | ``` var Stop: ((MIDIDriverRef) -> OSStatus)! ``` |
| To | ``` var Stop: ((MIDIDriverRef?) -> OSStatus)! ``` |

Modified [MIDINetworkConnection](https://developer.apple.com/documentation/coremidi/midinetworkconnection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MIDINetworkConnection : NSObject {     convenience init(host host: MIDINetworkHost)     class func connectionWithHost(_ host: MIDINetworkHost) -> Self     var host: MIDINetworkHost { get } } ``` | -- |
| To | ``` class MIDINetworkConnection : NSObject {     convenience init(host host: MIDINetworkHost)     class func withHost(_ host: MIDINetworkHost) -> Self     var host: MIDINetworkHost { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MIDINetworkConnection : CVarArg { } extension MIDINetworkConnection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MIDINetworkConnectionPolicy [enum]](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy)

|  | Declaration |
| --- | --- |
| From | ``` enum MIDINetworkConnectionPolicy : UInt {     case NoOne     case HostsInContactList     case Anyone } ``` |
| To | ``` enum MIDINetworkConnectionPolicy : UInt {     case noOne     case hostsInContactList     case anyone } ``` |

Modified [MIDINetworkConnectionPolicy.anyone](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/anyone)

|  | Declaration |
| --- | --- |
| From | ``` case Anyone ``` |
| To | ``` case anyone ``` |

Modified [MIDINetworkConnectionPolicy.hostsInContactList](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/hostsincontactlist)

|  | Declaration |
| --- | --- |
| From | ``` case HostsInContactList ``` |
| To | ``` case hostsInContactList ``` |

Modified [MIDINetworkConnectionPolicy.noOne](https://developer.apple.com/documentation/coremidi/midinetworkconnectionpolicy/noone)

|  | Declaration |
| --- | --- |
| From | ``` case NoOne ``` |
| To | ``` case noOne ``` |

Modified [MIDINetworkHost](https://developer.apple.com/documentation/coremidi/midinetworkhost)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MIDINetworkHost : NSObject {     convenience init(name name: String, address address: String, port port: Int)     class func hostWithName(_ name: String, address address: String, port port: Int) -> Self     convenience init(name name: String, netService netService: NSNetService)     class func hostWithName(_ name: String, netService netService: NSNetService) -> Self     convenience init(name name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String)     class func hostWithName(_ name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String) -> Self     func hasSameAddressAs(_ other: MIDINetworkHost) -> Bool     var name: String { get }     var address: String { get }     var port: Int { get }     var netServiceName: String? { get }     var netServiceDomain: String? { get } } ``` | -- |
| To | ``` class MIDINetworkHost : NSObject {     convenience init(name name: String, address address: String, port port: Int)     class func withName(_ name: String, address address: String, port port: Int) -> Self     convenience init(name name: String, netService netService: NetService)     class func withName(_ name: String, netService netService: NetService) -> Self     convenience init(name name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String)     class func withName(_ name: String, netServiceName netServiceName: String, netServiceDomain netServiceDomain: String) -> Self     func hasSameAddress(as other: MIDINetworkHost) -> Bool     var name: String { get }     var address: String { get }     var port: Int { get }     var netServiceName: String? { get }     var netServiceDomain: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MIDINetworkHost : CVarArg { } extension MIDINetworkHost : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MIDINetworkHost.hasSameAddress(as: MIDINetworkHost) -> Bool](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619372-hassameaddress)

|  | Declaration |
| --- | --- |
| From | ``` func hasSameAddressAs(_ other: MIDINetworkHost) -> Bool ``` |
| To | ``` func hasSameAddress(as other: MIDINetworkHost) -> Bool ``` |

Modified [MIDINetworkHost.init(name: String, netService: NetService)](https://developer.apple.com/documentation/coremidi/midinetworkhost/1619371-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String, netService netService: NSNetService) ``` |
| To | ``` convenience init(name name: String, netService netService: NetService) ``` |

Modified [MIDINetworkSession](https://developer.apple.com/documentation/coremidi/midinetworksession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MIDINetworkSession : NSObject {     class func defaultSession() -> MIDINetworkSession     var enabled: Bool     var networkPort: Int { get }     var networkName: String { get }     var localName: String { get }     var connectionPolicy: MIDINetworkConnectionPolicy     func contacts() -> Set<MIDINetworkHost>     func addContact(_ contact: MIDINetworkHost) -> Bool     func removeContact(_ contact: MIDINetworkHost) -> Bool     func connections() -> Set<MIDINetworkConnection>     func addConnection(_ connection: MIDINetworkConnection) -> Bool     func removeConnection(_ connection: MIDINetworkConnection) -> Bool     func sourceEndpoint() -> MIDIEndpointRef     func destinationEndpoint() -> MIDIEndpointRef } ``` | -- |
| To | ``` class MIDINetworkSession : NSObject {     class func `default`() -> MIDINetworkSession     var isEnabled: Bool     var networkPort: Int { get }     var networkName: String { get }     var localName: String { get }     var connectionPolicy: MIDINetworkConnectionPolicy     func contacts() -> Set<MIDINetworkHost>     func addContact(_ contact: MIDINetworkHost) -> Bool     func removeContact(_ contact: MIDINetworkHost) -> Bool     func connections() -> Set<MIDINetworkConnection>     func addConnection(_ connection: MIDINetworkConnection) -> Bool     func removeConnection(_ connection: MIDINetworkConnection) -> Bool     func sourceEndpoint() -> MIDIEndpointRef     func destinationEndpoint() -> MIDIEndpointRef     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MIDINetworkSession : CVarArg { } extension MIDINetworkSession : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MIDINetworkSession.default() [class]](https://developer.apple.com/documentation/coremidi/midinetworksession/1619363-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSession() -> MIDINetworkSession ``` |
| To | ``` class func `default`() -> MIDINetworkSession ``` |

Modified [MIDINetworkSession.isEnabled](https://developer.apple.com/documentation/coremidi/midinetworksession/1619368-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [MIDINotificationMessageID [enum]](https://developer.apple.com/documentation/coremidi/midinotificationmessageid)

|  | Declaration |
| --- | --- |
| From | ``` enum MIDINotificationMessageID : Int32 {     case MsgSetupChanged     case MsgObjectAdded     case MsgObjectRemoved     case MsgPropertyChanged     case MsgThruConnectionsChanged     case MsgSerialPortOwnerChanged     case MsgIOError } ``` |
| To | ``` enum MIDINotificationMessageID : Int32 {     case msgSetupChanged     case msgObjectAdded     case msgObjectRemoved     case msgPropertyChanged     case msgThruConnectionsChanged     case msgSerialPortOwnerChanged     case msgIOError } ``` |

Modified [MIDINotificationMessageID.msgIOError](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgioerror)

|  | Declaration |
| --- | --- |
| From | ``` case MsgIOError ``` |
| To | ``` case msgIOError ``` |

Modified [MIDINotificationMessageID.msgObjectAdded](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgobjectadded)

|  | Declaration |
| --- | --- |
| From | ``` case MsgObjectAdded ``` |
| To | ``` case msgObjectAdded ``` |

Modified [MIDINotificationMessageID.msgObjectRemoved](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgobjectremoved)

|  | Declaration |
| --- | --- |
| From | ``` case MsgObjectRemoved ``` |
| To | ``` case msgObjectRemoved ``` |

Modified [MIDINotificationMessageID.msgPropertyChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgpropertychanged)

|  | Declaration |
| --- | --- |
| From | ``` case MsgPropertyChanged ``` |
| To | ``` case msgPropertyChanged ``` |

Modified [MIDINotificationMessageID.msgSerialPortOwnerChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgserialportownerchanged)

|  | Declaration |
| --- | --- |
| From | ``` case MsgSerialPortOwnerChanged ``` |
| To | ``` case msgSerialPortOwnerChanged ``` |

Modified [MIDINotificationMessageID.msgSetupChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/kmidimsgsetupchanged)

|  | Declaration |
| --- | --- |
| From | ``` case MsgSetupChanged ``` |
| To | ``` case msgSetupChanged ``` |

Modified [MIDINotificationMessageID.msgThruConnectionsChanged](https://developer.apple.com/documentation/coremidi/midinotificationmessageid/msgthruconnectionschanged)

|  | Declaration |
| --- | --- |
| From | ``` case MsgThruConnectionsChanged ``` |
| To | ``` case msgThruConnectionsChanged ``` |

Modified [MIDIObjectType [enum]](https://developer.apple.com/documentation/coremidi/midiobjecttype)

|  | Declaration |
| --- | --- |
| From | ``` enum MIDIObjectType : Int32 {     case Other     case Device     case Entity     case Source     case Destination     case ExternalDevice     case ExternalEntity     case ExternalSource     case ExternalDestination } ``` |
| To | ``` enum MIDIObjectType : Int32 {     case other     case device     case entity     case source     case destination     case externalDevice     case externalEntity     case externalSource     case externalDestination } ``` |

Modified [MIDIObjectType.destination](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_destination)

|  | Declaration |
| --- | --- |
| From | ``` case Destination ``` |
| To | ``` case destination ``` |

Modified [MIDIObjectType.device](https://developer.apple.com/documentation/coremidi/midiobjecttype/device)

|  | Declaration |
| --- | --- |
| From | ``` case Device ``` |
| To | ``` case device ``` |

Modified [MIDIObjectType.entity](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_entity)

|  | Declaration |
| --- | --- |
| From | ``` case Entity ``` |
| To | ``` case entity ``` |

Modified [MIDIObjectType.externalDestination](https://developer.apple.com/documentation/coremidi/midiobjecttype/externaldestination)

|  | Declaration |
| --- | --- |
| From | ``` case ExternalDestination ``` |
| To | ``` case externalDestination ``` |

Modified [MIDIObjectType.externalDevice](https://developer.apple.com/documentation/coremidi/midiobjecttype/externaldevice)

|  | Declaration |
| --- | --- |
| From | ``` case ExternalDevice ``` |
| To | ``` case externalDevice ``` |

Modified [MIDIObjectType.externalEntity](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalentity)

|  | Declaration |
| --- | --- |
| From | ``` case ExternalEntity ``` |
| To | ``` case externalEntity ``` |

Modified [MIDIObjectType.externalSource](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_externalsource)

|  | Declaration |
| --- | --- |
| From | ``` case ExternalSource ``` |
| To | ``` case externalSource ``` |

Modified [MIDIObjectType.other](https://developer.apple.com/documentation/coremidi/midiobjecttype/other)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [MIDIObjectType.source](https://developer.apple.com/documentation/coremidi/midiobjecttype/kmidiobjecttype_source)

|  | Declaration |
| --- | --- |
| From | ``` case Source ``` |
| To | ``` case source ``` |

Modified [MIDISysexSendRequest [struct]](https://developer.apple.com/documentation/coremidi/midisysexsendrequest)

|  | Declaration |
| --- | --- |
| From | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: UnsafePointer<UInt8>     var bytesToSend: UInt32     var complete: DarwinBoolean     var reserved: (UInt8, UInt8, UInt8)     var completionProc: MIDICompletionProc     var completionRefCon: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct MIDISysexSendRequest {     var destination: MIDIEndpointRef     var data: UnsafePointer<UInt8>     var bytesToSend: UInt32     var complete: DarwinBoolean     var reserved: (UInt8, UInt8, UInt8)     var completionProc: CoreMIDI.MIDICompletionProc     var completionRefCon: UnsafeMutableRawPointer? } ``` |

Modified [MIDISysexSendRequest.completionProc](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/1495336-completionproc)

|  | Declaration |
| --- | --- |
| From | ``` var completionProc: MIDICompletionProc ``` |
| To | ``` var completionProc: CoreMIDI.MIDICompletionProc ``` |

Modified [MIDISysexSendRequest.completionRefCon](https://developer.apple.com/documentation/coremidi/midisysexsendrequest/1495195-completionrefcon)

|  | Declaration |
| --- | --- |
| From | ``` var completionRefCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var completionRefCon: UnsafeMutableRawPointer? ``` |

Modified [MIDITransformControlType [enum]](https://developer.apple.com/documentation/coremidi/miditransformcontroltype)

|  | Declaration |
| --- | --- |
| From | ``` enum MIDITransformControlType : UInt8 {     case ControlType_7Bit     case ControlType_14Bit     case ControlType_7BitRPN     case ControlType_14BitRPN     case ControlType_7BitNRPN     case ControlType_14BitNRPN } ``` |
| To | ``` enum MIDITransformControlType : UInt8 {     case controlType_7Bit     case controlType_14Bit     case controlType_7BitRPN     case controlType_14BitRPN     case controlType_7BitNRPN     case controlType_14BitNRPN } ``` |

Modified [MIDITransformControlType.controlType_14Bit](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_14bit)

|  | Declaration |
| --- | --- |
| From | ``` case ControlType_14Bit ``` |
| To | ``` case controlType_14Bit ``` |

Modified [MIDITransformControlType.controlType_14BitNRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_14bitnrpn)

|  | Declaration |
| --- | --- |
| From | ``` case ControlType_14BitNRPN ``` |
| To | ``` case controlType_14BitNRPN ``` |

Modified [MIDITransformControlType.controlType_14BitRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_14bitrpn)

|  | Declaration |
| --- | --- |
| From | ``` case ControlType_14BitRPN ``` |
| To | ``` case controlType_14BitRPN ``` |

Modified [MIDITransformControlType.controlType_7Bit](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bit)

|  | Declaration |
| --- | --- |
| From | ``` case ControlType_7Bit ``` |
| To | ``` case controlType_7Bit ``` |

Modified [MIDITransformControlType.controlType_7BitNRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/controltype_7bitnrpn)

|  | Declaration |
| --- | --- |
| From | ``` case ControlType_7BitNRPN ``` |
| To | ``` case controlType_7BitNRPN ``` |

Modified [MIDITransformControlType.controlType_7BitRPN](https://developer.apple.com/documentation/coremidi/miditransformcontroltype/kmidicontroltype_7bitrpn)

|  | Declaration |
| --- | --- |
| From | ``` case ControlType_7BitRPN ``` |
| To | ``` case controlType_7BitRPN ``` |

Modified [MIDITransformType [enum]](https://developer.apple.com/documentation/coremidi/miditransformtype)

|  | Declaration |
| --- | --- |
| From | ``` enum MIDITransformType : UInt16 {     case None     case FilterOut     case MapControl     case Add     case Scale     case MinValue     case MaxValue     case MapValue } ``` |
| To | ``` enum MIDITransformType : UInt16 {     case none     case filterOut     case mapControl     case add     case scale     case minValue     case maxValue     case mapValue } ``` |

Modified [MIDITransformType.add](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_add)

|  | Declaration |
| --- | --- |
| From | ``` case Add ``` |
| To | ``` case add ``` |

Modified [MIDITransformType.filterOut](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_filterout)

|  | Declaration |
| --- | --- |
| From | ``` case FilterOut ``` |
| To | ``` case filterOut ``` |

Modified [MIDITransformType.mapControl](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_mapcontrol)

|  | Declaration |
| --- | --- |
| From | ``` case MapControl ``` |
| To | ``` case mapControl ``` |

Modified [MIDITransformType.mapValue](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_mapvalue)

|  | Declaration |
| --- | --- |
| From | ``` case MapValue ``` |
| To | ``` case mapValue ``` |

Modified [MIDITransformType.maxValue](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_maxvalue)

|  | Declaration |
| --- | --- |
| From | ``` case MaxValue ``` |
| To | ``` case maxValue ``` |

Modified [MIDITransformType.minValue](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_minvalue)

|  | Declaration |
| --- | --- |
| From | ``` case MinValue ``` |
| To | ``` case minValue ``` |

Modified [MIDITransformType.none](https://developer.apple.com/documentation/coremidi/miditransformtype/kmiditransform_none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MIDITransformType.scale](https://developer.apple.com/documentation/coremidi/miditransformtype/scale)

|  | Declaration |
| --- | --- |
| From | ``` case Scale ``` |
| To | ``` case scale ``` |

Modified [MIDIClientCreate(_: CFString, _: CoreMIDI.MIDINotifyProc?, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495360-midiclientcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIClientCreate(_ name: CFString, _ notifyProc: MIDINotifyProc?, _ notifyRefCon: UnsafeMutablePointer<Void>, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus ``` |
| To | ``` func MIDIClientCreate(_ name: CFString, _ notifyProc: CoreMIDI.MIDINotifyProc?, _ notifyRefCon: UnsafeMutableRawPointer?, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus ``` |

Modified [MIDIClientCreateWithBlock(_: CFString, _: UnsafeMutablePointer<MIDIClientRef>, _: CoreMIDI.MIDINotifyBlock?) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495330-midiclientcreatewithblock)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIClientCreateWithBlock(_ name: CFString, _ outClient: UnsafeMutablePointer<MIDIClientRef>, _ notifyBlock: MIDINotifyBlock?) -> OSStatus ``` |
| To | ``` func MIDIClientCreateWithBlock(_ name: CFString, _ outClient: UnsafeMutablePointer<MIDIClientRef>, _ notifyBlock: CoreMIDI.MIDINotifyBlock?) -> OSStatus ``` |

Modified [MIDICompletionProc](https://developer.apple.com/documentation/coremidi/midicompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDICompletionProc = (UnsafeMutablePointer<MIDISysexSendRequest>) -> Void ``` |
| To | ``` typealias MIDICompletionProc = (UnsafeMutablePointer<MIDISysexSendRequest>) -> Swift.Void ``` |

Modified [MIDIDestinationCreate(_: MIDIClientRef, _: CFString, _: CoreMIDI.MIDIReadProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495347-mididestinationcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |
| To | ``` func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString, _ readProc: CoreMIDI.MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified [MIDIDestinationCreateWithBlock(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIEndpointRef>, _: CoreMIDI.MIDIReadBlock) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495247-mididestinationcreatewithblock)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDestinationCreateWithBlock(_ client: MIDIClientRef, _ name: CFString, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>, _ readBlock: MIDIReadBlock) -> OSStatus ``` |
| To | ``` func MIDIDestinationCreateWithBlock(_ client: MIDIClientRef, _ name: CFString, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>, _ readBlock: CoreMIDI.MIDIReadBlock) -> OSStatus ``` |

Modified [MIDIDeviceCreate(_: MIDIDriverRef!, _: CFString!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<MIDIDeviceRef>!) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508421-mididevicecreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIDeviceCreate(_ owner: MIDIDriverRef, _ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |
| To | ``` func MIDIDeviceCreate(_ owner: MIDIDriverRef!, _ name: CFString!, _ manufacturer: CFString!, _ model: CFString!, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>!) -> OSStatus ``` |

Modified [MIDIDriverRef](https://developer.apple.com/documentation/coremidi/mididriverref)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIDriverRef = UnsafeMutablePointer<UnsafeMutablePointer<MIDIDriverInterface>> ``` |
| To | ``` typealias MIDIDriverRef = UnsafeMutablePointer<UnsafeMutablePointer<MIDIDriverInterface>?> ``` |

Modified [MIDIEndpointGetEntity(_: MIDIEndpointRef, _: UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495196-midiendpointgetentity)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpointRef, _ outEntity: UnsafeMutablePointer<MIDIEntityRef>) -> OSStatus ``` |
| To | ``` func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpointRef, _ outEntity: UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus ``` |

Modified [MIDIEndpointGetRefCons(_: MIDIEndpointRef, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508417-midiendpointgetrefcons)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointGetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ ref2: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OSStatus ``` |
| To | ``` func MIDIEndpointGetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ ref2: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> OSStatus ``` |

Modified [MIDIEndpointSetRefCons(_: MIDIEndpointRef, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508268-midiendpointsetrefcons)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEndpointSetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<Void>, _ ref2: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func MIDIEndpointSetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutableRawPointer!, _ ref2: UnsafeMutableRawPointer!) -> OSStatus ``` |

Modified [MIDIEntityGetDevice(_: MIDIEntityRef, _: UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495210-midientitygetdevice)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIEntityGetDevice(_ inEntity: MIDIEntityRef, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus ``` |
| To | ``` func MIDIEntityGetDevice(_ inEntity: MIDIEntityRef, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>?) -> OSStatus ``` |

Modified [MIDIGetDriverDeviceList(_: MIDIDriverRef!) -> MIDIDeviceListRef](https://developer.apple.com/documentation/coremidi/1508306-midigetdriverdevicelist)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIGetDriverDeviceList(_ driver: MIDIDriverRef) -> MIDIDeviceListRef ``` |
| To | ``` func MIDIGetDriverDeviceList(_ driver: MIDIDriverRef!) -> MIDIDeviceListRef ``` |

Modified [MIDIInputPortCreate(_: MIDIClientRef, _: CFString, _: CoreMIDI.MIDIReadProc, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495225-midiinputportcreate)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ readProc: MIDIReadProc, _ refCon: UnsafeMutablePointer<Void>, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |
| To | ``` func MIDIInputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ readProc: CoreMIDI.MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus ``` |

Modified [MIDIInputPortCreateWithBlock(_: MIDIClientRef, _: CFString, _: UnsafeMutablePointer<MIDIPortRef>, _: CoreMIDI.MIDIReadBlock) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495333-midiinputportcreatewithblock)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIInputPortCreateWithBlock(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ readBlock: MIDIReadBlock) -> OSStatus ``` |
| To | ``` func MIDIInputPortCreateWithBlock(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ readBlock: CoreMIDI.MIDIReadBlock) -> OSStatus ``` |

Modified [MIDINotifyBlock](https://developer.apple.com/documentation/coremidi/midinotifyblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDINotifyBlock = (UnsafePointer<MIDINotification>) -> Void ``` |
| To | ``` typealias MIDINotifyBlock = (UnsafePointer<MIDINotification>) -> Swift.Void ``` |

Modified [MIDINotifyProc](https://developer.apple.com/documentation/coremidi/midinotifyproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDINotifyProc = (UnsafePointer<MIDINotification>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias MIDINotifyProc = (UnsafePointer<MIDINotification>, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [MIDIObjectFindByUniqueID(_: MIDIUniqueID, _: UnsafeMutablePointer<MIDIObjectRef>?, _: UnsafeMutablePointer<MIDIObjectType>?) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495191-midiobjectfindbyuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIObjectFindByUniqueID(_ inUniqueID: MIDIUniqueID, _ outObject: UnsafeMutablePointer<MIDIObjectRef>, _ outObjectType: UnsafeMutablePointer<MIDIObjectType>) -> OSStatus ``` |
| To | ``` func MIDIObjectFindByUniqueID(_ inUniqueID: MIDIUniqueID, _ outObject: UnsafeMutablePointer<MIDIObjectRef>?, _ outObjectType: UnsafeMutablePointer<MIDIObjectType>?) -> OSStatus ``` |

Modified [MIDIPortConnectSource(_: MIDIPortRef, _: MIDIEndpointRef, _: UnsafeMutableRawPointer?) -> OSStatus](https://developer.apple.com/documentation/coremidi/1495278-midiportconnectsource)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIPortConnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef, _ connRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func MIDIPortConnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef, _ connRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified [MIDIReadBlock](https://developer.apple.com/documentation/coremidi/midireadblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIReadBlock = (UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias MIDIReadBlock = (UnsafePointer<MIDIPacketList>, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [MIDIReadProc](https://developer.apple.com/documentation/coremidi/midireadproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias MIDIReadProc = (UnsafePointer<MIDIPacketList>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias MIDIReadProc = (UnsafePointer<MIDIPacketList>, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [MIDIThruConnectionFind(_: CFString, _: UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508377-midithruconnectionfind)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString, _ outConnectionList: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionFind(_ inPersistentOwnerID: CFString, _ outConnectionList: UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus ``` |

Modified [MIDIThruConnectionGetParams(_: MIDIThruConnectionRef, _: UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus](https://developer.apple.com/documentation/coremidi/1508390-midithruconnectiongetparams)

|  | Declaration |
| --- | --- |
| From | ``` func MIDIThruConnectionGetParams(_ connection: MIDIThruConnectionRef, _ outConnectionParams: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func MIDIThruConnectionGetParams(_ connection: MIDIThruConnectionRef, _ outConnectionParams: UnsafeMutablePointer<Unmanaged<CFData>>) -> OSStatus ``` |

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
