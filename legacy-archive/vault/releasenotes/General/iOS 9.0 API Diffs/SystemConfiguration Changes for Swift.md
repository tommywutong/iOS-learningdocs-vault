---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/SystemConfiguration.html
archived_at: '2026-07-18T02:57:00.983053Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# SystemConfiguration Changes for Swift

### SystemConfiguration

Removed SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed kSCNetworkConnectionConnectedRemoved kSCNetworkConnectionConnectingRemoved kSCNetworkConnectionDisconnectedRemoved kSCNetworkConnectionDisconnectingRemoved kSCNetworkConnectionInvalidRemoved kSCNetworkConnectionPPPAuthenticatingRemoved kSCNetworkConnectionPPPConnectedRemoved kSCNetworkConnectionPPPConnectingLinkRemoved kSCNetworkConnectionPPPDialOnTrafficRemoved kSCNetworkConnectionPPPDisconnectedRemoved kSCNetworkConnectionPPPDisconnectingLinkRemoved kSCNetworkConnectionPPPHoldingLinkOffRemoved kSCNetworkConnectionPPPInitializingRemoved kSCNetworkConnectionPPPNegotiatingLinkRemoved kSCNetworkConnectionPPPNegotiatingNetworkRemoved kSCNetworkConnectionPPPSuspendedRemoved kSCNetworkConnectionPPPTerminatingRemoved kSCNetworkConnectionPPPWaitingForCallBackRemoved kSCNetworkConnectionPPPWaitingForRedialRemoved kSCNetworkReachabilityFlagsConnectionAutomaticRemoved kSCNetworkReachabilityFlagsConnectionOnDemandRemoved kSCNetworkReachabilityFlagsConnectionOnTrafficRemoved kSCNetworkReachabilityFlagsConnectionRequiredRemoved kSCNetworkReachabilityFlagsInterventionRequiredRemoved kSCNetworkReachabilityFlagsIsDirectRemoved kSCNetworkReachabilityFlagsIsLocalAddressRemoved kSCNetworkReachabilityFlagsIsWWANRemoved kSCNetworkReachabilityFlagsReachableRemoved kSCNetworkReachabilityFlagsTransientConnectionRemoved kSCPreferencesNotificationApplyRemoved kSCPreferencesNotificationCommitRemoved SCNetworkConnectionPPPStatusRemoved SCNetworkConnectionStatusRemoved SCNetworkReachabilityFlagsRemoved SCPreferencesNotificationAdded SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added [SCNetworkConnectionPPPStatus [enum]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus)Added [SCNetworkConnectionPPPStatus.Authenticating](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppauthenticating)Added [SCNetworkConnectionPPPStatus.Connected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppconnected)Added [SCNetworkConnectionPPPStatus.ConnectingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppconnectinglink)Added [SCNetworkConnectionPPPStatus.DialOnTraffic](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/dialontraffic)Added [SCNetworkConnectionPPPStatus.Disconnected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/disconnected)Added [SCNetworkConnectionPPPStatus.DisconnectingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/disconnectinglink)Added [SCNetworkConnectionPPPStatus.HoldingLinkOff](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppholdinglinkoff)Added [SCNetworkConnectionPPPStatus.Initializing](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppinitializing)Added [SCNetworkConnectionPPPStatus.NegotiatingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppnegotiatinglink)Added [SCNetworkConnectionPPPStatus.NegotiatingNetwork](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppnegotiatingnetwork)Added [SCNetworkConnectionPPPStatus.Suspended](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/suspended)Added [SCNetworkConnectionPPPStatus.Terminating](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/terminating)Added [SCNetworkConnectionPPPStatus.WaitingForCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/waitingforcallback)Added [SCNetworkConnectionPPPStatus.WaitingForRedial](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppwaitingforredial)Added [SCNetworkConnectionStatus [enum]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus)Added [SCNetworkConnectionStatus.Connected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/connected)Added [SCNetworkConnectionStatus.Connecting](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/kscnetworkconnectionconnecting)Added [SCNetworkConnectionStatus.Disconnected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/disconnected)Added [SCNetworkConnectionStatus.Disconnecting](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/kscnetworkconnectiondisconnecting)Added [SCNetworkConnectionStatus.Invalid](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/invalid)Added SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added [SCNetworkReachabilityFlags [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags)Added [SCNetworkReachabilityFlags.ConnectionAutomatic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionautomatic)Added [SCNetworkReachabilityFlags.ConnectionOnDemand](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionondemand)Added [SCNetworkReachabilityFlags.ConnectionOnTraffic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514926-connectionontraffic)Added [SCNetworkReachabilityFlags.ConnectionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionrequired)Added SCNetworkReachabilityFlags.init(rawValue: UInt32)Added [SCNetworkReachabilityFlags.InterventionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsinterventionrequired)Added [SCNetworkReachabilityFlags.IsDirect](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514916-isdirect)Added [SCNetworkReachabilityFlags.IsLocalAddress](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514896-islocaladdress)Added [SCNetworkReachabilityFlags.IsWWAN](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsiswwan)Added [SCNetworkReachabilityFlags.Reachable](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514923-reachable)Added [SCNetworkReachabilityFlags.TransientConnection](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514913-transientconnection)Added SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added [SCPreferencesNotification [struct]](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification)Added [SCPreferencesNotification.Apply](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification/kscpreferencesnotificationapply)Added [SCPreferencesNotification.Commit](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification/kscpreferencesnotificationcommit)Added SCPreferencesNotification.init(rawValue: UInt32)Modified [SCDynamicStoreContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |

Modified [SCDynamicStoreContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437791-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |

Modified [SCDynamicStoreContext.release](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437807-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |

Modified [SCDynamicStoreContext.retain](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/1437803-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |

Modified [SCNetworkConnectionContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |

Modified [SCNetworkConnectionContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393177-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |

Modified [SCNetworkConnectionContext.release](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393098-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |

Modified [SCNetworkConnectionContext.retain](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/1393118-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |

Modified [SCNetworkReachabilityContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |

Modified [SCNetworkReachabilityContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514929-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |

Modified [SCNetworkReachabilityContext.release](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514918-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |

Modified [SCNetworkReachabilityContext.retain](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext/1514910-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |

Modified [SCPreferencesContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext)

|  | Declaration |
| --- | --- |
| From | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |
| To | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?     var release: ((UnsafePointer<Void>) -> Void)?     var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release release: ((UnsafePointer<Void>) -> Void)?, copyDescription copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?) } ``` |

Modified [SCPreferencesContext.copyDescription](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1517041-copydescription)

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)? ``` |

Modified [SCPreferencesContext.release](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516916-release)

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |
| To | ``` var release: ((UnsafePointer<Void>) -> Void)? ``` |

Modified [SCPreferencesContext.retain](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/1516920-retain)

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |
| To | ``` var retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)? ``` |

Modified [kCFErrorDomainSystemConfiguration](https://developer.apple.com/documentation/systemconfiguration/kcferrordomainsystemconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainSystemConfiguration: CFString! ``` |
| To | ``` let kCFErrorDomainSystemConfiguration: CFString ``` |

Modified [SCCopyLastError() -> CFError](https://developer.apple.com/documentation/systemconfiguration/1517326-sccopylasterror)

|  | Declaration |
| --- | --- |
| From | ``` func SCCopyLastError() -> Unmanaged<CFError>! ``` |
| To | ``` func SCCopyLastError() -> CFError ``` |

Modified [SCDynamicStoreCallBack](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCDynamicStoreCallBack = CFunctionPointer<((SCDynamicStore!, CFArray!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCDynamicStoreCallBack = (SCDynamicStore, CFArray, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [SCNetworkConnectionCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkConnectionCallBack = CFunctionPointer<((SCNetworkConnection!, SCNetworkConnectionStatus, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCNetworkConnectionCallBack = (SCNetworkConnection, SCNetworkConnectionStatus, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [SCNetworkReachabilityCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkReachabilityCallBack = CFunctionPointer<((SCNetworkReachability!, SCNetworkReachabilityFlags, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCNetworkReachabilityCallBack = (SCNetworkReachability, SCNetworkReachabilityFlags, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [SCNetworkReachabilityCreateWithAddress(_: CFAllocator?, _: UnsafePointer<sockaddr>) -> SCNetworkReachability?](https://developer.apple.com/documentation/systemconfiguration/1514895-scnetworkreachabilitycreatewitha)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithAddress(_ allocator: CFAllocator!, _ address: UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>! ``` |
| To | ``` func SCNetworkReachabilityCreateWithAddress(_ allocator: CFAllocator?, _ address: UnsafePointer<sockaddr>) -> SCNetworkReachability? ``` |

Modified [SCNetworkReachabilityCreateWithAddressPair(_: CFAllocator?, _: UnsafePointer<sockaddr>, _: UnsafePointer<sockaddr>) -> SCNetworkReachability?](https://developer.apple.com/documentation/systemconfiguration/1514908-scnetworkreachabilitycreatewitha)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator!, _ localAddress: UnsafePointer<sockaddr>, _ remoteAddress: UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>! ``` |
| To | ``` func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator?, _ localAddress: UnsafePointer<sockaddr>, _ remoteAddress: UnsafePointer<sockaddr>) -> SCNetworkReachability? ``` |

Modified [SCNetworkReachabilityCreateWithName(_: CFAllocator?, _: UnsafePointer<Int8>) -> SCNetworkReachability?](https://developer.apple.com/documentation/systemconfiguration/1514904-scnetworkreachabilitycreatewithn)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithName(_ allocator: CFAllocator!, _ nodename: UnsafePointer<Int8>) -> Unmanaged<SCNetworkReachability>! ``` |
| To | ``` func SCNetworkReachabilityCreateWithName(_ allocator: CFAllocator?, _ nodename: UnsafePointer<Int8>) -> SCNetworkReachability? ``` |

Modified [SCNetworkReachabilityGetFlags(_: SCNetworkReachability, _: UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514924-scnetworkreachabilitygetflags)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityGetFlags(_ target: SCNetworkReachability!, _ flags: UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Boolean ``` |
| To | ``` func SCNetworkReachabilityGetFlags(_ target: SCNetworkReachability, _ flags: UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Bool ``` |

Modified [SCNetworkReachabilityScheduleWithRunLoop(_: SCNetworkReachability, _: CFRunLoop, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514894-scnetworkreachabilityschedulewit)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityScheduleWithRunLoop(_ target: SCNetworkReachability!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkReachabilityScheduleWithRunLoop(_ target: SCNetworkReachability, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool ``` |

Modified [SCNetworkReachabilitySetCallback(_: SCNetworkReachability, _: SCNetworkReachabilityCallBack?, _: UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514903-scnetworkreachabilitysetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability!, _ callout: SCNetworkReachabilityCallBack, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Boolean ``` |
| To | ``` func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability, _ callout: SCNetworkReachabilityCallBack?, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Bool ``` |

Modified [SCNetworkReachabilitySetDispatchQueue(_: SCNetworkReachability, _: dispatch_queue_t?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514911-scnetworkreachabilitysetdispatch)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilitySetDispatchQueue(_ target: SCNetworkReachability!, _ queue: dispatch_queue_t!) -> Boolean ``` |
| To | ``` func SCNetworkReachabilitySetDispatchQueue(_ target: SCNetworkReachability, _ queue: dispatch_queue_t?) -> Bool ``` |

Modified [SCNetworkReachabilityUnscheduleFromRunLoop(_: SCNetworkReachability, _: CFRunLoop, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1514899-scnetworkreachabilityunschedulef)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkReachabilityUnscheduleFromRunLoop(_ target: SCNetworkReachability!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkReachabilityUnscheduleFromRunLoop(_ target: SCNetworkReachability, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool ``` |

Modified [SCPreferencesCallBack](https://developer.apple.com/documentation/systemconfiguration/scpreferencescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCPreferencesCallBack = CFunctionPointer<((SCPreferences!, SCPreferencesNotification, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCPreferencesCallBack = (SCPreferences, SCPreferencesNotification, UnsafeMutablePointer<Void>) -> Void ``` |

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
