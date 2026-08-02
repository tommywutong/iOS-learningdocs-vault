---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/SystemConfiguration.html
archived_at: '2026-07-18T02:51:40.306347Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# SystemConfiguration Changes for Swift

### SystemConfiguration

Removed [SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1517217-init)Removed [SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1517275-init)Removed [SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1516770-init)Removed [SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516727-init)Added [SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ( (UnsafeRawPointer) -> UnsafeRawPointer)?, release: ( (UnsafeRawPointer) -> Swift.Void)?, copyDescription: ( (UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1517217-init)Added [SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ( (UnsafeRawPointer) -> UnsafeRawPointer)?, release: ( (UnsafeRawPointer) -> Swift.Void)?, copyDescription: ( (UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1517275-init)Added [SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ( (UnsafeRawPointer) -> UnsafeRawPointer)?, release: ( (UnsafeRawPointer) -> Swift.Void)?, copyDescription: ( (UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1516770-init)Added [SCPreferencesContext.init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ( (UnsafeRawPointer) -> UnsafeRawPointer)?, release: ( (UnsafeRawPointer) -> Swift.Void)?, copyDescription: ( (UnsafeRawPointer) -> Unmanaged<CFString>)?)](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516727-init)Modified [SCDynamicStoreContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCDynamicStoreContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437791-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)? ``` |

Modified [SCDynamicStoreContext.info](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437787-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [SCDynamicStoreContext.release](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437807-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |
| To | ``` var release: ((UnsafeRawPointer) -> Swift.Void)? ``` |

Modified [SCDynamicStoreContext.retain](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437803-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |
| To | ``` var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)? ``` |

Modified [SCNetworkConnectionContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCNetworkConnectionContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393177-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)? ``` |

Modified [SCNetworkConnectionContext.info](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393171-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [SCNetworkConnectionContext.release](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393098-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |
| To | ``` var release: ((UnsafeRawPointer) -> Swift.Void)? ``` |

Modified [SCNetworkConnectionContext.retain](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393118-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |
| To | ``` var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)? ``` |

Modified [SCNetworkConnectionPPPStatus [enum]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum SCNetworkConnectionPPPStatus : Int32 {     case Disconnected     case Initializing     case ConnectingLink     case DialOnTraffic     case NegotiatingLink     case Authenticating     case WaitingForCallBack     case NegotiatingNetwork     case Connected     case Terminating     case DisconnectingLink     case HoldingLinkOff     case Suspended     case WaitingForRedial } ``` |
| To | ``` enum SCNetworkConnectionPPPStatus : Int32 {     case disconnected     case initializing     case connectingLink     case dialOnTraffic     case negotiatingLink     case authenticating     case waitingForCallBack     case negotiatingNetwork     case connected     case terminating     case disconnectingLink     case holdingLinkOff     case suspended     case waitingForRedial } ``` |

Modified [SCNetworkConnectionPPPStatus.authenticating](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppauthenticating)

|  | Declaration |
| --- | --- |
| From | ``` case Authenticating ``` |
| To | ``` case authenticating ``` |

Modified [SCNetworkConnectionPPPStatus.connected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [SCNetworkConnectionPPPStatus.connectingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppconnectinglink)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectingLink ``` |
| To | ``` case connectingLink ``` |

Modified [SCNetworkConnectionPPPStatus.dialOnTraffic](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/dialontraffic)

|  | Declaration |
| --- | --- |
| From | ``` case DialOnTraffic ``` |
| To | ``` case dialOnTraffic ``` |

Modified [SCNetworkConnectionPPPStatus.disconnected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/disconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnected ``` |
| To | ``` case disconnected ``` |

Modified [SCNetworkConnectionPPPStatus.disconnectingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/disconnectinglink)

|  | Declaration |
| --- | --- |
| From | ``` case DisconnectingLink ``` |
| To | ``` case disconnectingLink ``` |

Modified [SCNetworkConnectionPPPStatus.holdingLinkOff](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppholdinglinkoff)

|  | Declaration |
| --- | --- |
| From | ``` case HoldingLinkOff ``` |
| To | ``` case holdingLinkOff ``` |

Modified [SCNetworkConnectionPPPStatus.initializing](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppinitializing)

|  | Declaration |
| --- | --- |
| From | ``` case Initializing ``` |
| To | ``` case initializing ``` |

Modified [SCNetworkConnectionPPPStatus.negotiatingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppnegotiatinglink)

|  | Declaration |
| --- | --- |
| From | ``` case NegotiatingLink ``` |
| To | ``` case negotiatingLink ``` |

Modified [SCNetworkConnectionPPPStatus.negotiatingNetwork](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppnegotiatingnetwork)

|  | Declaration |
| --- | --- |
| From | ``` case NegotiatingNetwork ``` |
| To | ``` case negotiatingNetwork ``` |

Modified [SCNetworkConnectionPPPStatus.suspended](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/suspended)

|  | Declaration |
| --- | --- |
| From | ``` case Suspended ``` |
| To | ``` case suspended ``` |

Modified [SCNetworkConnectionPPPStatus.terminating](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/terminating)

|  | Declaration |
| --- | --- |
| From | ``` case Terminating ``` |
| To | ``` case terminating ``` |

Modified [SCNetworkConnectionPPPStatus.waitingForCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/waitingforcallback)

|  | Declaration |
| --- | --- |
| From | ``` case WaitingForCallBack ``` |
| To | ``` case waitingForCallBack ``` |

Modified [SCNetworkConnectionPPPStatus.waitingForRedial](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppwaitingforredial)

|  | Declaration |
| --- | --- |
| From | ``` case WaitingForRedial ``` |
| To | ``` case waitingForRedial ``` |

Modified [SCNetworkConnectionStatus [enum]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum SCNetworkConnectionStatus : Int32 {     case Invalid     case Disconnected     case Connecting     case Connected     case Disconnecting } ``` |
| To | ``` enum SCNetworkConnectionStatus : Int32 {     case invalid     case disconnected     case connecting     case connected     case disconnecting } ``` |

Modified [SCNetworkConnectionStatus.connected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/connected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [SCNetworkConnectionStatus.connecting](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/kscnetworkconnectionconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Connecting ``` |
| To | ``` case connecting ``` |

Modified [SCNetworkConnectionStatus.disconnected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/disconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnected ``` |
| To | ``` case disconnected ``` |

Modified [SCNetworkConnectionStatus.disconnecting](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/kscnetworkconnectiondisconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnecting ``` |
| To | ``` case disconnecting ``` |

Modified [SCNetworkConnectionStatus.invalid](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [SCNetworkReachabilityContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCNetworkReachabilityContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514929-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)? ``` |

Modified [SCNetworkReachabilityContext.info](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514901-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [SCNetworkReachabilityContext.release](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514918-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |
| To | ``` var release: ((UnsafeRawPointer) -> Swift.Void)? ``` |

Modified [SCNetworkReachabilityContext.retain](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514910-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |
| To | ``` var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)? ``` |

Modified [SCNetworkReachabilityFlags [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SCNetworkReachabilityFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var TransientConnection: SCNetworkReachabilityFlags { get }     static var Reachable: SCNetworkReachabilityFlags { get }     static var ConnectionRequired: SCNetworkReachabilityFlags { get }     static var ConnectionOnTraffic: SCNetworkReachabilityFlags { get }     static var InterventionRequired: SCNetworkReachabilityFlags { get }     static var ConnectionOnDemand: SCNetworkReachabilityFlags { get }     static var IsLocalAddress: SCNetworkReachabilityFlags { get }     static var IsDirect: SCNetworkReachabilityFlags { get }     static var ConnectionAutomatic: SCNetworkReachabilityFlags { get } } ``` | OptionSetType |
| To | ``` struct SCNetworkReachabilityFlags : OptionSet {     init(rawValue rawValue: UInt32)     static var transientConnection: SCNetworkReachabilityFlags { get }     static var reachable: SCNetworkReachabilityFlags { get }     static var connectionRequired: SCNetworkReachabilityFlags { get }     static var connectionOnTraffic: SCNetworkReachabilityFlags { get }     static var interventionRequired: SCNetworkReachabilityFlags { get }     static var connectionOnDemand: SCNetworkReachabilityFlags { get }     static var isLocalAddress: SCNetworkReachabilityFlags { get }     static var isDirect: SCNetworkReachabilityFlags { get }     static var connectionAutomatic: SCNetworkReachabilityFlags { get }     func intersect(_ other: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags     func exclusiveOr(_ other: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags     mutating func unionInPlace(_ other: SCNetworkReachabilityFlags)     mutating func intersectInPlace(_ other: SCNetworkReachabilityFlags)     mutating func exclusiveOrInPlace(_ other: SCNetworkReachabilityFlags)     func isSubsetOf(_ other: SCNetworkReachabilityFlags) -> Bool     func isDisjointWith(_ other: SCNetworkReachabilityFlags) -> Bool     func isSupersetOf(_ other: SCNetworkReachabilityFlags) -> Bool     mutating func subtractInPlace(_ other: SCNetworkReachabilityFlags)     func isStrictSupersetOf(_ other: SCNetworkReachabilityFlags) -> Bool     func isStrictSubsetOf(_ other: SCNetworkReachabilityFlags) -> Bool } extension SCNetworkReachabilityFlags {     func union(_ other: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags     func intersection(_ other: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags     func symmetricDifference(_ other: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags } extension SCNetworkReachabilityFlags {     func contains(_ member: SCNetworkReachabilityFlags) -> Bool     mutating func insert(_ newMember: SCNetworkReachabilityFlags) -> (inserted: Bool, memberAfterInsert: SCNetworkReachabilityFlags)     mutating func remove(_ member: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags?     mutating func update(with newMember: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags? } extension SCNetworkReachabilityFlags {     convenience init()     mutating func formUnion(_ other: SCNetworkReachabilityFlags)     mutating func formIntersection(_ other: SCNetworkReachabilityFlags)     mutating func formSymmetricDifference(_ other: SCNetworkReachabilityFlags) } extension SCNetworkReachabilityFlags {     convenience init<S : Sequence where S.Iterator.Element == SCNetworkReachabilityFlags>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SCNetworkReachabilityFlags...)     mutating func subtract(_ other: SCNetworkReachabilityFlags)     func isSubset(of other: SCNetworkReachabilityFlags) -> Bool     func isSuperset(of other: SCNetworkReachabilityFlags) -> Bool     func isDisjoint(with other: SCNetworkReachabilityFlags) -> Bool     func subtracting(_ other: SCNetworkReachabilityFlags) -> SCNetworkReachabilityFlags     var isEmpty: Bool { get }     func isStrictSuperset(of other: SCNetworkReachabilityFlags) -> Bool     func isStrictSubset(of other: SCNetworkReachabilityFlags) -> Bool } ``` | OptionSet |

Modified [SCNetworkReachabilityFlags.connectionAutomatic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionautomatic)

|  | Declaration |
| --- | --- |
| From | ``` static var ConnectionAutomatic: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var connectionAutomatic: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.connectionOnDemand](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionondemand)

|  | Declaration |
| --- | --- |
| From | ``` static var ConnectionOnDemand: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var connectionOnDemand: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.connectionOnTraffic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514926-connectionontraffic)

|  | Declaration |
| --- | --- |
| From | ``` static var ConnectionOnTraffic: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var connectionOnTraffic: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.connectionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionrequired)

|  | Declaration |
| --- | --- |
| From | ``` static var ConnectionRequired: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var connectionRequired: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.interventionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsinterventionrequired)

|  | Declaration |
| --- | --- |
| From | ``` static var InterventionRequired: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var interventionRequired: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.isDirect](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514916-isdirect)

|  | Declaration |
| --- | --- |
| From | ``` static var IsDirect: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var isDirect: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.isLocalAddress](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514896-islocaladdress)

|  | Declaration |
| --- | --- |
| From | ``` static var IsLocalAddress: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var isLocalAddress: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.reachable](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514923-reachable)

|  | Declaration |
| --- | --- |
| From | ``` static var Reachable: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var reachable: SCNetworkReachabilityFlags { get } ``` |

Modified [SCNetworkReachabilityFlags.transientConnection](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514913-transientconnection)

|  | Declaration |
| --- | --- |
| From | ``` static var TransientConnection: SCNetworkReachabilityFlags { get } ``` |
| To | ``` static var transientConnection: SCNetworkReachabilityFlags { get } ``` |

Modified [SCPreferencesContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |
| To | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutableRawPointer?     var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?     var release: ((UnsafeRawPointer) -> Swift.Void)?     var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutableRawPointer?, retain retain: (@escaping (UnsafeRawPointer) -> UnsafeRawPointer)?, release release: (@escaping (UnsafeRawPointer) -> Swift.Void)?, copyDescription copyDescription: (@escaping (UnsafeRawPointer) -> Unmanaged<CFString>)?) } ``` |

Modified [SCPreferencesContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1517041-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |
| To | ``` var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)? ``` |

Modified [SCPreferencesContext.info](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516929-info)

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<Void> ``` |
| To | ``` var info: UnsafeMutableRawPointer? ``` |

Modified [SCPreferencesContext.release](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516916-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |
| To | ``` var release: ((UnsafeRawPointer) -> Swift.Void)? ``` |

Modified [SCPreferencesContext.retain](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516920-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |
| To | ``` var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)? ``` |

Modified [SCPreferencesNotification [struct]](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SCPreferencesNotification : OptionSetType {     init(rawValue rawValue: UInt32)     static var Commit: SCPreferencesNotification { get }     static var Apply: SCPreferencesNotification { get } } ``` | OptionSetType |
| To | ``` struct SCPreferencesNotification : OptionSet {     init(rawValue rawValue: UInt32)     static var commit: SCPreferencesNotification { get }     static var apply: SCPreferencesNotification { get }     func intersect(_ other: SCPreferencesNotification) -> SCPreferencesNotification     func exclusiveOr(_ other: SCPreferencesNotification) -> SCPreferencesNotification     mutating func unionInPlace(_ other: SCPreferencesNotification)     mutating func intersectInPlace(_ other: SCPreferencesNotification)     mutating func exclusiveOrInPlace(_ other: SCPreferencesNotification)     func isSubsetOf(_ other: SCPreferencesNotification) -> Bool     func isDisjointWith(_ other: SCPreferencesNotification) -> Bool     func isSupersetOf(_ other: SCPreferencesNotification) -> Bool     mutating func subtractInPlace(_ other: SCPreferencesNotification)     func isStrictSupersetOf(_ other: SCPreferencesNotification) -> Bool     func isStrictSubsetOf(_ other: SCPreferencesNotification) -> Bool } extension SCPreferencesNotification {     func union(_ other: SCPreferencesNotification) -> SCPreferencesNotification     func intersection(_ other: SCPreferencesNotification) -> SCPreferencesNotification     func symmetricDifference(_ other: SCPreferencesNotification) -> SCPreferencesNotification } extension SCPreferencesNotification {     func contains(_ member: SCPreferencesNotification) -> Bool     mutating func insert(_ newMember: SCPreferencesNotification) -> (inserted: Bool, memberAfterInsert: SCPreferencesNotification)     mutating func remove(_ member: SCPreferencesNotification) -> SCPreferencesNotification?     mutating func update(with newMember: SCPreferencesNotification) -> SCPreferencesNotification? } extension SCPreferencesNotification {     convenience init()     mutating func formUnion(_ other: SCPreferencesNotification)     mutating func formIntersection(_ other: SCPreferencesNotification)     mutating func formSymmetricDifference(_ other: SCPreferencesNotification) } extension SCPreferencesNotification {     convenience init<S : Sequence where S.Iterator.Element == SCPreferencesNotification>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SCPreferencesNotification...)     mutating func subtract(_ other: SCPreferencesNotification)     func isSubset(of other: SCPreferencesNotification) -> Bool     func isSuperset(of other: SCPreferencesNotification) -> Bool     func isDisjoint(with other: SCPreferencesNotification) -> Bool     func subtracting(_ other: SCPreferencesNotification) -> SCPreferencesNotification     var isEmpty: Bool { get }     func isStrictSuperset(of other: SCPreferencesNotification) -> Bool     func isStrictSubset(of other: SCPreferencesNotification) -> Bool } ``` | OptionSet |

Modified [SCPreferencesNotification.apply](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification/kscpreferencesnotificationapply)

|  | Declaration |
| --- | --- |
| From | ``` static var Apply: SCPreferencesNotification { get } ``` |
| To | ``` static var apply: SCPreferencesNotification { get } ``` |

Modified [SCPreferencesNotification.commit](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification/kscpreferencesnotificationcommit)

|  | Declaration |
| --- | --- |
| From | ``` static var Commit: SCPreferencesNotification { get } ``` |
| To | ``` static var commit: SCPreferencesNotification { get } ``` |

Modified [kSCEntNetPPTP](https://developer.apple.com/documentation/systemconfiguration/kscentnetpptp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [kSCNetworkInterfaceTypePPTP](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypepptp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [kSCValNetInterfaceSubTypePPTP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacesubtypepptp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [SCBondInterface](https://developer.apple.com/documentation/systemconfiguration/scbondinterfaceref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCBondInterface = SCNetworkInterfaceRef ``` |
| To | ``` typealias SCBondInterface = SCNetworkInterface ``` |

Modified [SCDynamicStoreCallBack](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCDynamicStoreCallBack = (SCDynamicStore, CFArray, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias SCDynamicStoreCallBack = (SCDynamicStore, CFArray, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [SCDynamicStoreCopyComputerName(_: SCDynamicStore?, _: UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517208-scdynamicstorecopycomputername)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore?, _ nameEncoding: UnsafeMutablePointer<CFStringEncoding>) -> CFString? ``` |
| To | ``` func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore?, _ nameEncoding: UnsafeMutablePointer<CFStringEncoding>?) -> CFString? ``` |

Modified [SCDynamicStoreCopyConsoleUser(_: SCDynamicStore?, _: UnsafeMutablePointer<uid_t>?, _: UnsafeMutablePointer<gid_t>?) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517123-scdynamicstorecopyconsoleuser)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore?, _ uid: UnsafeMutablePointer<uid_t>, _ gid: UnsafeMutablePointer<gid_t>) -> CFString? ``` |
| To | ``` func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore?, _ uid: UnsafeMutablePointer<uid_t>?, _ gid: UnsafeMutablePointer<gid_t>?) -> CFString? ``` |

Modified [SCDynamicStoreCreate(_: CFAllocator?, _: CFString, _: SystemConfiguration.SCDynamicStoreCallBack?, _: UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore?](https://developer.apple.com/documentation/systemconfiguration/1437828-scdynamicstorecreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCreate(_ allocator: CFAllocator?, _ name: CFString, _ callout: SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> SCDynamicStore? ``` |
| To | ``` func SCDynamicStoreCreate(_ allocator: CFAllocator?, _ name: CFString, _ callout: SystemConfiguration.SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore? ``` |

Modified [SCDynamicStoreCreateWithOptions(_: CFAllocator?, _: CFString, _: CFDictionary?, _: SystemConfiguration.SCDynamicStoreCallBack?, _: UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore?](https://developer.apple.com/documentation/systemconfiguration/1437818-scdynamicstorecreatewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCreateWithOptions(_ allocator: CFAllocator?, _ name: CFString, _ storeOptions: CFDictionary?, _ callout: SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> SCDynamicStore? ``` |
| To | ``` func SCDynamicStoreCreateWithOptions(_ allocator: CFAllocator?, _ name: CFString, _ storeOptions: CFDictionary?, _ callout: SystemConfiguration.SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore? ``` |

Modified [SCDynamicStoreSetDispatchQueue(_: SCDynamicStore, _: DispatchQueue?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437816-scdynamicstoresetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreSetDispatchQueue(_ store: SCDynamicStore, _ queue: dispatch_queue_t?) -> Bool ``` |
| To | ``` func SCDynamicStoreSetDispatchQueue(_ store: SCDynamicStore, _ queue: DispatchQueue?) -> Bool ``` |

Modified [SCNetworkConnectionCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkConnectionCallBack = (SCNetworkConnection, SCNetworkConnectionStatus, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias SCNetworkConnectionCallBack = (SCNetworkConnection, SCNetworkConnectionStatus, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [SCNetworkConnectionCopyUserPreferences(_: CFDictionary?, _: UnsafeMutablePointer<Unmanaged<CFString>>?, _: UnsafeMutablePointer<Unmanaged<CFDictionary>>?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393114-scnetworkconnectioncopyuserprefe)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary?, _ serviceID: UnsafeMutablePointer<Unmanaged<CFString>?>, _ userOptions: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool ``` |
| To | ``` func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary?, _ serviceID: UnsafeMutablePointer<Unmanaged<CFString>>?, _ userOptions: UnsafeMutablePointer<Unmanaged<CFDictionary>>?) -> Bool ``` |

Modified [SCNetworkConnectionCreateWithServiceID(_: CFAllocator?, _: CFString, _: SystemConfiguration.SCNetworkConnectionCallBack?, _: UnsafeMutablePointer<SCNetworkConnectionContext>?) -> SCNetworkConnection?](https://developer.apple.com/documentation/systemconfiguration/1393175-scnetworkconnectioncreatewithser)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator?, _ serviceID: CFString, _ callout: SCNetworkConnectionCallBack?, _ context: UnsafeMutablePointer<SCNetworkConnectionContext>) -> SCNetworkConnection? ``` |
| To | ``` func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator?, _ serviceID: CFString, _ callout: SystemConfiguration.SCNetworkConnectionCallBack?, _ context: UnsafeMutablePointer<SCNetworkConnectionContext>?) -> SCNetworkConnection? ``` |

Modified [SCNetworkConnectionSetDispatchQueue(_: SCNetworkConnection, _: DispatchQueue?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393138-scnetworkconnectionsetdispatchqu)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionSetDispatchQueue(_ connection: SCNetworkConnection, _ queue: dispatch_queue_t?) -> Bool ``` |
| To | ``` func SCNetworkConnectionSetDispatchQueue(_ connection: SCNetworkConnection, _ queue: DispatchQueue?) -> Bool ``` |

Modified [SCNetworkInterfaceCopyMediaOptions(_: SCNetworkInterface, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, _: UnsafeMutablePointer<Unmanaged<CFArray>?>?, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516738-scnetworkinterfacecopymediaoptio)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface, _ current: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ active: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ available: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ filter: Bool) -> Bool ``` |
| To | ``` func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface, _ current: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, _ active: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, _ available: UnsafeMutablePointer<Unmanaged<CFArray>?>?, _ filter: Bool) -> Bool ``` |

Modified [SCNetworkInterfaceCopyMTU(_: SCNetworkInterface, _: UnsafeMutablePointer<Int32>?, _: UnsafeMutablePointer<Int32>?, _: UnsafeMutablePointer<Int32>?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517279-scnetworkinterfacecopymtu)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface, _ mtu_cur: UnsafeMutablePointer<Int32>, _ mtu_min: UnsafeMutablePointer<Int32>, _ mtu_max: UnsafeMutablePointer<Int32>) -> Bool ``` |
| To | ``` func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface, _ mtu_cur: UnsafeMutablePointer<Int32>?, _ mtu_min: UnsafeMutablePointer<Int32>?, _ mtu_max: UnsafeMutablePointer<Int32>?) -> Bool ``` |

Modified [SCNetworkInterfaceSetConfiguration(_: SCNetworkInterface, _: CFDictionary?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517082-scnetworkinterfacesetconfigurati)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceSetConfiguration(_ interface: SCNetworkInterface, _ config: CFDictionary) -> Bool ``` |
| To | ``` func SCNetworkInterfaceSetConfiguration(_ interface: SCNetworkInterface, _ config: CFDictionary?) -> Bool ``` |

Modified [SCNetworkInterfaceSetExtendedConfiguration(_: SCNetworkInterface, _: CFString, _: CFDictionary?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517295-scnetworkinterfacesetextendedcon)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceSetExtendedConfiguration(_ interface: SCNetworkInterface, _ extendedType: CFString, _ config: CFDictionary) -> Bool ``` |
| To | ``` func SCNetworkInterfaceSetExtendedConfiguration(_ interface: SCNetworkInterface, _ extendedType: CFString, _ config: CFDictionary?) -> Bool ``` |

Modified [SCNetworkProtocolSetConfiguration(_: SCNetworkProtocol, _: CFDictionary?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517188-scnetworkprotocolsetconfiguratio)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkProtocolSetConfiguration(_ protocol: SCNetworkProtocol, _ config: CFDictionary) -> Bool ``` |
| To | ``` func SCNetworkProtocolSetConfiguration(_ protocol: SCNetworkProtocol, _ config: CFDictionary?) -> Bool ``` |

Modified [SCNetworkReachabilityCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkReachabilityCallBack = (SCNetworkReachability, SCNetworkReachabilityFlags, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias SCNetworkReachabilityCallBack = (SCNetworkReachability, SCNetworkReachabilityFlags, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [SCNetworkReachabilityCreateWithAddressPair(_: CFAllocator?, _: UnsafePointer<sockaddr>?, _: UnsafePointer<sockaddr>?) -> SCNetworkReachability?](https://developer.apple.com/documentation/systemconfiguration/1514908-scnetworkreachabilitycreatewitha)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator?, _ localAddress: UnsafePointer<sockaddr>, _ remoteAddress: UnsafePointer<sockaddr>) -> SCNetworkReachability? ``` |
| To | ``` func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator?, _ localAddress: UnsafePointer<sockaddr>?, _ remoteAddress: UnsafePointer<sockaddr>?) -> SCNetworkReachability? ``` |

Modified [SCNetworkReachabilitySetCallback(_: SCNetworkReachability, _: SystemConfiguration.SCNetworkReachabilityCallBack?, _: UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514903-scnetworkreachabilitysetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability, _ callout: SCNetworkReachabilityCallBack?, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Bool ``` |
| To | ``` func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability, _ callout: SystemConfiguration.SCNetworkReachabilityCallBack?, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool ``` |

Modified [SCNetworkReachabilitySetDispatchQueue(_: SCNetworkReachability, _: DispatchQueue?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514911-scnetworkreachabilitysetdispatch)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilitySetDispatchQueue(_ target: SCNetworkReachability, _ queue: dispatch_queue_t?) -> Bool ``` |
| To | ``` func SCNetworkReachabilitySetDispatchQueue(_ target: SCNetworkReachability, _ queue: DispatchQueue?) -> Bool ``` |

Modified [SCNetworkServiceSetName(_: SCNetworkService, _: CFString?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516988-scnetworkservicesetname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceSetName(_ service: SCNetworkService, _ name: CFString) -> Bool ``` |
| To | ``` func SCNetworkServiceSetName(_ service: SCNetworkService, _ name: CFString?) -> Bool ``` |

Modified [SCNetworkSetSetName(_: SCNetworkSet, _: CFString?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517309-scnetworksetsetname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetSetName(_ set: SCNetworkSet, _ name: CFString) -> Bool ``` |
| To | ``` func SCNetworkSetSetName(_ set: SCNetworkSet, _ name: CFString?) -> Bool ``` |

Modified [SCPreferencesCallBack](https://developer.apple.com/documentation/systemconfiguration/scpreferencescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCPreferencesCallBack = (SCPreferences, SCPreferencesNotification, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias SCPreferencesCallBack = (SCPreferences, SCPreferencesNotification, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [SCPreferencesCreateWithAuthorization(_: CFAllocator?, _: CFString, _: CFString?, _: AuthorizationRef?) -> SCPreferences?](https://developer.apple.com/documentation/systemconfiguration/1516686-scpreferencescreatewithauthoriza)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator?, _ name: CFString, _ prefsID: CFString?, _ authorization: AuthorizationRef) -> SCPreferences? ``` |
| To | ``` func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator?, _ name: CFString, _ prefsID: CFString?, _ authorization: AuthorizationRef?) -> SCPreferences? ``` |

Modified [SCPreferencesSetCallback(_: SCPreferences, _: SystemConfiguration.SCPreferencesCallBack?, _: UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517094-scpreferencessetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetCallback(_ prefs: SCPreferences, _ callout: SCPreferencesCallBack?, _ context: UnsafeMutablePointer<SCPreferencesContext>) -> Bool ``` |
| To | ``` func SCPreferencesSetCallback(_ prefs: SCPreferences, _ callout: SystemConfiguration.SCPreferencesCallBack?, _ context: UnsafeMutablePointer<SCPreferencesContext>?) -> Bool ``` |

Modified [SCPreferencesSetComputerName(_: SCPreferences, _: CFString?, _: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516772-scpreferencessetcomputername)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetComputerName(_ prefs: SCPreferences, _ name: CFString, _ nameEncoding: CFStringEncoding) -> Bool ``` |
| To | ``` func SCPreferencesSetComputerName(_ prefs: SCPreferences, _ name: CFString?, _ nameEncoding: CFStringEncoding) -> Bool ``` |

Modified [SCPreferencesSetDispatchQueue(_: SCPreferences, _: DispatchQueue?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517050-scpreferencessetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetDispatchQueue(_ prefs: SCPreferences, _ queue: dispatch_queue_t?) -> Bool ``` |
| To | ``` func SCPreferencesSetDispatchQueue(_ prefs: SCPreferences, _ queue: DispatchQueue?) -> Bool ``` |

Modified [SCPreferencesSetLocalHostName(_: SCPreferences, _: CFString?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516945-scpreferencessetlocalhostname)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetLocalHostName(_ prefs: SCPreferences, _ name: CFString) -> Bool ``` |
| To | ``` func SCPreferencesSetLocalHostName(_ prefs: SCPreferences, _ name: CFString?) -> Bool ``` |

Modified [SCVLANInterface](https://developer.apple.com/documentation/systemconfiguration/scvlaninterfaceref)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCVLANInterfaceRef = SCVLANInterface ``` |
| To | ``` typealias SCVLANInterface = SCNetworkInterface ``` |

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
