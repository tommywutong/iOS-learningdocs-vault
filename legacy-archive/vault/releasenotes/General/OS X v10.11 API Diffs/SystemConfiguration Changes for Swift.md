---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/SystemConfiguration.html
archived_at: '2026-07-18T02:53:45.871908Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# SystemConfiguration Changes for Swift

### SystemConfiguration

Removed SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Removed kSCNetworkConnectionConnectedRemoved kSCNetworkConnectionConnectingRemoved kSCNetworkConnectionDisconnectedRemoved kSCNetworkConnectionDisconnectingRemoved kSCNetworkConnectionInvalidRemoved kSCNetworkConnectionPPPAuthenticatingRemoved kSCNetworkConnectionPPPConnectedRemoved kSCNetworkConnectionPPPConnectingLinkRemoved kSCNetworkConnectionPPPDialOnTrafficRemoved kSCNetworkConnectionPPPDisconnectedRemoved kSCNetworkConnectionPPPDisconnectingLinkRemoved kSCNetworkConnectionPPPHoldingLinkOffRemoved kSCNetworkConnectionPPPInitializingRemoved kSCNetworkConnectionPPPNegotiatingLinkRemoved kSCNetworkConnectionPPPNegotiatingNetworkRemoved kSCNetworkConnectionPPPSuspendedRemoved kSCNetworkConnectionPPPTerminatingRemoved kSCNetworkConnectionPPPWaitingForCallBackRemoved kSCNetworkConnectionPPPWaitingForRedialRemoved kSCNetworkReachabilityFlagsConnectionAutomaticRemoved kSCNetworkReachabilityFlagsConnectionOnDemandRemoved kSCNetworkReachabilityFlagsConnectionOnTrafficRemoved kSCNetworkReachabilityFlagsConnectionRequiredRemoved kSCNetworkReachabilityFlagsInterventionRequiredRemoved kSCNetworkReachabilityFlagsIsDirectRemoved kSCNetworkReachabilityFlagsIsLocalAddressRemoved kSCNetworkReachabilityFlagsReachableRemoved kSCNetworkReachabilityFlagsTransientConnectionRemoved kSCPreferencesNotificationApplyRemoved kSCPreferencesNotificationCommitRemoved SCNetworkConnectionPPPStatusRemoved SCNetworkConnectionStatusRemoved SCNetworkReachabilityFlagsRemoved SCPreferencesNotificationAdded SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added [SCNetworkConnectionPPPStatus [enum]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus)Added [SCNetworkConnectionPPPStatus.Authenticating](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppauthenticating)Added [SCNetworkConnectionPPPStatus.Connected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppconnected)Added [SCNetworkConnectionPPPStatus.ConnectingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppconnectinglink)Added [SCNetworkConnectionPPPStatus.DialOnTraffic](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/dialontraffic)Added [SCNetworkConnectionPPPStatus.Disconnected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/disconnected)Added [SCNetworkConnectionPPPStatus.DisconnectingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/disconnectinglink)Added [SCNetworkConnectionPPPStatus.HoldingLinkOff](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppholdinglinkoff)Added [SCNetworkConnectionPPPStatus.Initializing](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppinitializing)Added [SCNetworkConnectionPPPStatus.NegotiatingLink](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppnegotiatinglink)Added [SCNetworkConnectionPPPStatus.NegotiatingNetwork](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppnegotiatingnetwork)Added [SCNetworkConnectionPPPStatus.Suspended](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/suspended)Added [SCNetworkConnectionPPPStatus.Terminating](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/terminating)Added [SCNetworkConnectionPPPStatus.WaitingForCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/waitingforcallback)Added [SCNetworkConnectionPPPStatus.WaitingForRedial](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionpppstatus/kscnetworkconnectionpppwaitingforredial)Added [SCNetworkConnectionStatus [enum]](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus)Added [SCNetworkConnectionStatus.Connected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/connected)Added [SCNetworkConnectionStatus.Connecting](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/kscnetworkconnectionconnecting)Added [SCNetworkConnectionStatus.Disconnected](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/disconnected)Added [SCNetworkConnectionStatus.Disconnecting](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/kscnetworkconnectiondisconnecting)Added [SCNetworkConnectionStatus.Invalid](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus/invalid)Added SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added [SCNetworkReachabilityFlags [struct]](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags)Added [SCNetworkReachabilityFlags.ConnectionAutomatic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionautomatic)Added [SCNetworkReachabilityFlags.ConnectionOnDemand](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionondemand)Added [SCNetworkReachabilityFlags.ConnectionOnTraffic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514926-connectionontraffic)Added [SCNetworkReachabilityFlags.ConnectionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionrequired)Added SCNetworkReachabilityFlags.init(rawValue: UInt32)Added [SCNetworkReachabilityFlags.InterventionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsinterventionrequired)Added [SCNetworkReachabilityFlags.IsDirect](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514916-isdirect)Added [SCNetworkReachabilityFlags.IsLocalAddress](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514896-islocaladdress)Added [SCNetworkReachabilityFlags.Reachable](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514923-reachable)Added [SCNetworkReachabilityFlags.TransientConnection](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514913-transientconnection)Added SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: ((UnsafePointer<Void>) -> UnsafePointer<Void>)?, release: ((UnsafePointer<Void>) -> Void)?, copyDescription: ((UnsafePointer<Void>) -> Unmanaged<CFString>)?)Added [SCPreferencesNotification [struct]](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification)Added [SCPreferencesNotification.Apply](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification/kscpreferencesnotificationapply)Added [SCPreferencesNotification.Commit](https://developer.apple.com/documentation/systemconfiguration/scpreferencesnotification/kscpreferencesnotificationcommit)Added SCPreferencesNotification.init(rawValue: UInt32)Modified [SCDynamicStoreContext [struct]](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext)

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

Modified [kSCBondStatusDeviceAggregationStatus](https://developer.apple.com/documentation/systemconfiguration/kscbondstatusdeviceaggregationstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kSCBondStatusDeviceAggregationStatus: CFString! ``` |
| To | ``` let kSCBondStatusDeviceAggregationStatus: CFString ``` |

Modified [kSCBondStatusDeviceCollecting](https://developer.apple.com/documentation/systemconfiguration/kscbondstatusdevicecollecting)

|  | Declaration |
| --- | --- |
| From | ``` let kSCBondStatusDeviceCollecting: CFString! ``` |
| To | ``` let kSCBondStatusDeviceCollecting: CFString ``` |

Modified [kSCBondStatusDeviceDistributing](https://developer.apple.com/documentation/systemconfiguration/kscbondstatusdevicedistributing)

|  | Declaration |
| --- | --- |
| From | ``` let kSCBondStatusDeviceDistributing: CFString! ``` |
| To | ``` let kSCBondStatusDeviceDistributing: CFString ``` |

Modified [kSCCompAnyRegex](https://developer.apple.com/documentation/systemconfiguration/ksccompanyregex)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompAnyRegex: CFString! ``` |
| To | ``` let kSCCompAnyRegex: CFString ``` |

Modified [kSCCompGlobal](https://developer.apple.com/documentation/systemconfiguration/ksccompglobal)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompGlobal: CFString! ``` |
| To | ``` let kSCCompGlobal: CFString ``` |

Modified [kSCCompHostNames](https://developer.apple.com/documentation/systemconfiguration/ksccomphostnames)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompHostNames: CFString! ``` |
| To | ``` let kSCCompHostNames: CFString ``` |

Modified [kSCCompInterface](https://developer.apple.com/documentation/systemconfiguration/ksccompinterface)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompInterface: CFString! ``` |
| To | ``` let kSCCompInterface: CFString ``` |

Modified [kSCCompNetwork](https://developer.apple.com/documentation/systemconfiguration/ksccompnetwork)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompNetwork: CFString! ``` |
| To | ``` let kSCCompNetwork: CFString ``` |

Modified [kSCCompService](https://developer.apple.com/documentation/systemconfiguration/ksccompservice)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompService: CFString! ``` |
| To | ``` let kSCCompService: CFString ``` |

Modified [kSCCompSystem](https://developer.apple.com/documentation/systemconfiguration/ksccompsystem)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompSystem: CFString! ``` |
| To | ``` let kSCCompSystem: CFString ``` |

Modified [kSCCompUsers](https://developer.apple.com/documentation/systemconfiguration/ksccompusers)

|  | Declaration |
| --- | --- |
| From | ``` let kSCCompUsers: CFString! ``` |
| To | ``` let kSCCompUsers: CFString ``` |

Modified [kSCDynamicStoreDomainFile](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstoredomainfile)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStoreDomainFile: CFString! ``` |
| To | ``` let kSCDynamicStoreDomainFile: CFString ``` |

Modified [kSCDynamicStoreDomainPlugin](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstoredomainplugin)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStoreDomainPlugin: CFString! ``` |
| To | ``` let kSCDynamicStoreDomainPlugin: CFString ``` |

Modified [kSCDynamicStoreDomainPrefs](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstoredomainprefs)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStoreDomainPrefs: CFString! ``` |
| To | ``` let kSCDynamicStoreDomainPrefs: CFString ``` |

Modified [kSCDynamicStoreDomainSetup](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstoredomainsetup)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStoreDomainSetup: CFString! ``` |
| To | ``` let kSCDynamicStoreDomainSetup: CFString ``` |

Modified [kSCDynamicStoreDomainState](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstoredomainstate)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStoreDomainState: CFString! ``` |
| To | ``` let kSCDynamicStoreDomainState: CFString ``` |

Modified [kSCDynamicStorePropNetInterfaces](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstorepropnetinterfaces)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStorePropNetInterfaces: CFString! ``` |
| To | ``` let kSCDynamicStorePropNetInterfaces: CFString ``` |

Modified [kSCDynamicStorePropNetPrimaryInterface](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstorepropnetprimaryinterface)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStorePropNetPrimaryInterface: CFString! ``` |
| To | ``` let kSCDynamicStorePropNetPrimaryInterface: CFString ``` |

Modified [kSCDynamicStorePropNetPrimaryService](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstorepropnetprimaryservice)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStorePropNetPrimaryService: CFString! ``` |
| To | ``` let kSCDynamicStorePropNetPrimaryService: CFString ``` |

Modified [kSCDynamicStorePropNetServiceIDs](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstorepropnetserviceids)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStorePropNetServiceIDs: CFString! ``` |
| To | ``` let kSCDynamicStorePropNetServiceIDs: CFString ``` |

Modified [kSCDynamicStorePropSetupCurrentSet](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstorepropsetupcurrentset)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStorePropSetupCurrentSet: CFString! ``` |
| To | ``` let kSCDynamicStorePropSetupCurrentSet: CFString ``` |

Modified [kSCDynamicStorePropSetupLastUpdated](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstorepropsetuplastupdated)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStorePropSetupLastUpdated: CFString! ``` |
| To | ``` let kSCDynamicStorePropSetupLastUpdated: CFString ``` |

Modified [kSCDynamicStoreUseSessionKeys](https://developer.apple.com/documentation/systemconfiguration/kscdynamicstoreusesessionkeys)

|  | Declaration |
| --- | --- |
| From | ``` let kSCDynamicStoreUseSessionKeys: CFString! ``` |
| To | ``` let kSCDynamicStoreUseSessionKeys: CFString ``` |

Modified [kSCEntNet6to4](https://developer.apple.com/documentation/systemconfiguration/kscentnet6to4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNet6to4: CFString! ``` |
| To | ``` let kSCEntNet6to4: CFString ``` |

Modified [kSCEntNetAirPort](https://developer.apple.com/documentation/systemconfiguration/kscentnetairport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetAirPort: CFString! ``` |
| To | ``` let kSCEntNetAirPort: CFString ``` |

Modified [kSCEntNetDHCP](https://developer.apple.com/documentation/systemconfiguration/kscentnetdhcp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetDHCP: CFString! ``` |
| To | ``` let kSCEntNetDHCP: CFString ``` |

Modified [kSCEntNetDNS](https://developer.apple.com/documentation/systemconfiguration/kscentnetdns)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetDNS: CFString! ``` |
| To | ``` let kSCEntNetDNS: CFString ``` |

Modified [kSCEntNetEthernet](https://developer.apple.com/documentation/systemconfiguration/kscentnetethernet)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetEthernet: CFString! ``` |
| To | ``` let kSCEntNetEthernet: CFString ``` |

Modified [kSCEntNetFireWire](https://developer.apple.com/documentation/systemconfiguration/kscentnetfirewire)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetFireWire: CFString! ``` |
| To | ``` let kSCEntNetFireWire: CFString ``` |

Modified [kSCEntNetInterface](https://developer.apple.com/documentation/systemconfiguration/kscentnetinterface)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetInterface: CFString! ``` |
| To | ``` let kSCEntNetInterface: CFString ``` |

Modified [kSCEntNetIPSec](https://developer.apple.com/documentation/systemconfiguration/kscentnetipsec)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetIPSec: CFString! ``` |
| To | ``` let kSCEntNetIPSec: CFString ``` |

Modified [kSCEntNetIPv4](https://developer.apple.com/documentation/systemconfiguration/kscentnetipv4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetIPv4: CFString! ``` |
| To | ``` let kSCEntNetIPv4: CFString ``` |

Modified [kSCEntNetIPv6](https://developer.apple.com/documentation/systemconfiguration/kscentnetipv6)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetIPv6: CFString! ``` |
| To | ``` let kSCEntNetIPv6: CFString ``` |

Modified [kSCEntNetL2TP](https://developer.apple.com/documentation/systemconfiguration/kscentnetl2tp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetL2TP: CFString! ``` |
| To | ``` let kSCEntNetL2TP: CFString ``` |

Modified [kSCEntNetLink](https://developer.apple.com/documentation/systemconfiguration/kscentnetlink)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetLink: CFString! ``` |
| To | ``` let kSCEntNetLink: CFString ``` |

Modified [kSCEntNetModem](https://developer.apple.com/documentation/systemconfiguration/kscentnetmodem)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetModem: CFString! ``` |
| To | ``` let kSCEntNetModem: CFString ``` |

Modified [kSCEntNetPPP](https://developer.apple.com/documentation/systemconfiguration/kscentnetppp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetPPP: CFString! ``` |
| To | ``` let kSCEntNetPPP: CFString ``` |

Modified [kSCEntNetPPPoE](https://developer.apple.com/documentation/systemconfiguration/kscentnetpppoe)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetPPPoE: CFString! ``` |
| To | ``` let kSCEntNetPPPoE: CFString ``` |

Modified [kSCEntNetPPPSerial](https://developer.apple.com/documentation/systemconfiguration/kscentnetpppserial)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetPPPSerial: CFString! ``` |
| To | ``` let kSCEntNetPPPSerial: CFString ``` |

Modified [kSCEntNetPPTP](https://developer.apple.com/documentation/systemconfiguration/kscentnetpptp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetPPTP: CFString! ``` |
| To | ``` let kSCEntNetPPTP: CFString ``` |

Modified [kSCEntNetProxies](https://developer.apple.com/documentation/systemconfiguration/kscentnetproxies)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetProxies: CFString! ``` |
| To | ``` let kSCEntNetProxies: CFString ``` |

Modified [kSCEntNetSMB](https://developer.apple.com/documentation/systemconfiguration/kscentnetsmb)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntNetSMB: CFString! ``` |
| To | ``` let kSCEntNetSMB: CFString ``` |

Modified [kSCEntUsersConsoleUser](https://developer.apple.com/documentation/systemconfiguration/kscentusersconsoleuser)

|  | Declaration |
| --- | --- |
| From | ``` let kSCEntUsersConsoleUser: CFString! ``` |
| To | ``` let kSCEntUsersConsoleUser: CFString ``` |

Modified [kSCNetworkInterfaceIPv4](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfaceipv4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceIPv4: SCNetworkInterface! ``` |
| To | ``` let kSCNetworkInterfaceIPv4: SCNetworkInterface ``` |

Modified [kSCNetworkInterfaceType6to4](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetype6to4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceType6to4: CFString! ``` |
| To | ``` let kSCNetworkInterfaceType6to4: CFString ``` |

Modified [kSCNetworkInterfaceTypeBluetooth](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypebluetooth)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeBluetooth: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeBluetooth: CFString ``` |

Modified [kSCNetworkInterfaceTypeBond](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypebond)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeBond: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeBond: CFString ``` |

Modified [kSCNetworkInterfaceTypeEthernet](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeethernet)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeEthernet: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeEthernet: CFString ``` |

Modified [kSCNetworkInterfaceTypeFireWire](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypefirewire)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeFireWire: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeFireWire: CFString ``` |

Modified [kSCNetworkInterfaceTypeIEEE80211](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeieee80211)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeIEEE80211: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeIEEE80211: CFString ``` |

Modified [kSCNetworkInterfaceTypeIPSec](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeipsec)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeIPSec: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeIPSec: CFString ``` |

Modified [kSCNetworkInterfaceTypeIPv4](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeipv4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeIPv4: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeIPv4: CFString ``` |

Modified [kSCNetworkInterfaceTypeIrDA](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeirda)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeIrDA: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeIrDA: CFString ``` |

Modified [kSCNetworkInterfaceTypeL2TP](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypel2tp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeL2TP: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeL2TP: CFString ``` |

Modified [kSCNetworkInterfaceTypeModem](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypemodem)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeModem: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeModem: CFString ``` |

Modified [kSCNetworkInterfaceTypePPP](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeppp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypePPP: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypePPP: CFString ``` |

Modified [kSCNetworkInterfaceTypePPTP](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypepptp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypePPTP: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypePPTP: CFString ``` |

Modified [kSCNetworkInterfaceTypeSerial](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeserial)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeSerial: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeSerial: CFString ``` |

Modified [kSCNetworkInterfaceTypeVLAN](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypevlan)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeVLAN: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeVLAN: CFString ``` |

Modified [kSCNetworkInterfaceTypeWWAN](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypewwan)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkInterfaceTypeWWAN: CFString! ``` |
| To | ``` let kSCNetworkInterfaceTypeWWAN: CFString ``` |

Modified [kSCNetworkProtocolTypeDNS](https://developer.apple.com/documentation/systemconfiguration/kscnetworkprotocoltypedns)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkProtocolTypeDNS: CFString! ``` |
| To | ``` let kSCNetworkProtocolTypeDNS: CFString ``` |

Modified [kSCNetworkProtocolTypeIPv4](https://developer.apple.com/documentation/systemconfiguration/kscnetworkprotocoltypeipv4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkProtocolTypeIPv4: CFString! ``` |
| To | ``` let kSCNetworkProtocolTypeIPv4: CFString ``` |

Modified [kSCNetworkProtocolTypeIPv6](https://developer.apple.com/documentation/systemconfiguration/kscnetworkprotocoltypeipv6)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkProtocolTypeIPv6: CFString! ``` |
| To | ``` let kSCNetworkProtocolTypeIPv6: CFString ``` |

Modified [kSCNetworkProtocolTypeProxies](https://developer.apple.com/documentation/systemconfiguration/kscnetworkprotocoltypeproxies)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkProtocolTypeProxies: CFString! ``` |
| To | ``` let kSCNetworkProtocolTypeProxies: CFString ``` |

Modified [kSCNetworkProtocolTypeSMB](https://developer.apple.com/documentation/systemconfiguration/kscnetworkprotocoltypesmb)

|  | Declaration |
| --- | --- |
| From | ``` let kSCNetworkProtocolTypeSMB: CFString! ``` |
| To | ``` let kSCNetworkProtocolTypeSMB: CFString ``` |

Modified [kSCPrefCurrentSet](https://developer.apple.com/documentation/systemconfiguration/kscprefcurrentset)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPrefCurrentSet: CFString! ``` |
| To | ``` let kSCPrefCurrentSet: CFString ``` |

Modified [kSCPrefNetworkServices](https://developer.apple.com/documentation/systemconfiguration/kscprefnetworkservices)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPrefNetworkServices: CFString! ``` |
| To | ``` let kSCPrefNetworkServices: CFString ``` |

Modified [kSCPrefSets](https://developer.apple.com/documentation/systemconfiguration/kscprefsets)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPrefSets: CFString! ``` |
| To | ``` let kSCPrefSets: CFString ``` |

Modified [kSCPrefSystem](https://developer.apple.com/documentation/systemconfiguration/kscprefsystem)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPrefSystem: CFString! ``` |
| To | ``` let kSCPrefSystem: CFString ``` |

Modified [kSCPropInterfaceName](https://developer.apple.com/documentation/systemconfiguration/kscpropinterfacename)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropInterfaceName: CFString! ``` |
| To | ``` let kSCPropInterfaceName: CFString ``` |

Modified [kSCPropMACAddress](https://developer.apple.com/documentation/systemconfiguration/kscpropmacaddress)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropMACAddress: CFString! ``` |
| To | ``` let kSCPropMACAddress: CFString ``` |

Modified [kSCPropNet6to4Relay](https://developer.apple.com/documentation/systemconfiguration/kscpropnet6to4relay)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNet6to4Relay: CFString! ``` |
| To | ``` let kSCPropNet6to4Relay: CFString ``` |

Modified [kSCPropNetDNSDomainName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnsdomainname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSDomainName: CFString! ``` |
| To | ``` let kSCPropNetDNSDomainName: CFString ``` |

Modified [kSCPropNetDNSOptions](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnsoptions)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSOptions: CFString! ``` |
| To | ``` let kSCPropNetDNSOptions: CFString ``` |

Modified [kSCPropNetDNSSearchDomains](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnssearchdomains)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSSearchDomains: CFString! ``` |
| To | ``` let kSCPropNetDNSSearchDomains: CFString ``` |

Modified [kSCPropNetDNSSearchOrder](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnssearchorder)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSSearchOrder: CFString! ``` |
| To | ``` let kSCPropNetDNSSearchOrder: CFString ``` |

Modified [kSCPropNetDNSServerAddresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnsserveraddresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSServerAddresses: CFString! ``` |
| To | ``` let kSCPropNetDNSServerAddresses: CFString ``` |

Modified [kSCPropNetDNSServerPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnsserverport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSServerPort: CFString! ``` |
| To | ``` let kSCPropNetDNSServerPort: CFString ``` |

Modified [kSCPropNetDNSServerTimeout](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnsservertimeout)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSServerTimeout: CFString! ``` |
| To | ``` let kSCPropNetDNSServerTimeout: CFString ``` |

Modified [kSCPropNetDNSSortList](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnssortlist)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSSortList: CFString! ``` |
| To | ``` let kSCPropNetDNSSortList: CFString ``` |

Modified [kSCPropNetDNSSupplementalMatchDomains](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnssupplementalmatchdomains)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSSupplementalMatchDomains: CFString! ``` |
| To | ``` let kSCPropNetDNSSupplementalMatchDomains: CFString ``` |

Modified [kSCPropNetDNSSupplementalMatchOrders](https://developer.apple.com/documentation/systemconfiguration/kscpropnetdnssupplementalmatchorders)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetDNSSupplementalMatchOrders: CFString! ``` |
| To | ``` let kSCPropNetDNSSupplementalMatchOrders: CFString ``` |

Modified [kSCPropNetEthernetMediaOptions](https://developer.apple.com/documentation/systemconfiguration/kscpropnetethernetmediaoptions)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetEthernetMediaOptions: CFString! ``` |
| To | ``` let kSCPropNetEthernetMediaOptions: CFString ``` |

Modified [kSCPropNetEthernetMediaSubType](https://developer.apple.com/documentation/systemconfiguration/kscpropnetethernetmediasubtype)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetEthernetMediaSubType: CFString! ``` |
| To | ``` let kSCPropNetEthernetMediaSubType: CFString ``` |

Modified [kSCPropNetEthernetMTU](https://developer.apple.com/documentation/systemconfiguration/kscpropnetethernetmtu)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetEthernetMTU: CFString! ``` |
| To | ``` let kSCPropNetEthernetMTU: CFString ``` |

Modified [kSCPropNetInterfaceDeviceName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfacedevicename)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetInterfaceDeviceName: CFString! ``` |
| To | ``` let kSCPropNetInterfaceDeviceName: CFString ``` |

Modified [kSCPropNetInterfaceHardware](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfacehardware)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetInterfaceHardware: CFString! ``` |
| To | ``` let kSCPropNetInterfaceHardware: CFString ``` |

Modified [kSCPropNetInterfaces](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfaces)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetInterfaces: CFString! ``` |
| To | ``` let kSCPropNetInterfaces: CFString ``` |

Modified [kSCPropNetInterfaceSubType](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfacesubtype)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetInterfaceSubType: CFString! ``` |
| To | ``` let kSCPropNetInterfaceSubType: CFString ``` |

Modified [kSCPropNetInterfaceSupportsModemOnHold](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfacesupportsmodemonhold)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetInterfaceSupportsModemOnHold: CFString! ``` |
| To | ``` let kSCPropNetInterfaceSupportsModemOnHold: CFString ``` |

Modified [kSCPropNetInterfaceType](https://developer.apple.com/documentation/systemconfiguration/kscpropnetinterfacetype)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetInterfaceType: CFString! ``` |
| To | ``` let kSCPropNetInterfaceType: CFString ``` |

Modified [kSCPropNetIPSecAuthenticationMethod](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecauthenticationmethod)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecAuthenticationMethod: CFString! ``` |
| To | ``` let kSCPropNetIPSecAuthenticationMethod: CFString ``` |

Modified [kSCPropNetIPSecConnectTime](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecconnecttime)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecConnectTime: CFString! ``` |
| To | ``` let kSCPropNetIPSecConnectTime: CFString ``` |

Modified [kSCPropNetIPSecLocalCertificate](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipseclocalcertificate)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecLocalCertificate: CFString! ``` |
| To | ``` let kSCPropNetIPSecLocalCertificate: CFString ``` |

Modified [kSCPropNetIPSecLocalIdentifier](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipseclocalidentifier)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecLocalIdentifier: CFString! ``` |
| To | ``` let kSCPropNetIPSecLocalIdentifier: CFString ``` |

Modified [kSCPropNetIPSecLocalIdentifierType](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipseclocalidentifiertype)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecLocalIdentifierType: CFString! ``` |
| To | ``` let kSCPropNetIPSecLocalIdentifierType: CFString ``` |

Modified [kSCPropNetIPSecRemoteAddress](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecremoteaddress)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecRemoteAddress: CFString! ``` |
| To | ``` let kSCPropNetIPSecRemoteAddress: CFString ``` |

Modified [kSCPropNetIPSecSharedSecret](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecsharedsecret)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecSharedSecret: CFString! ``` |
| To | ``` let kSCPropNetIPSecSharedSecret: CFString ``` |

Modified [kSCPropNetIPSecSharedSecretEncryption](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecsharedsecretencryption)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecSharedSecretEncryption: CFString! ``` |
| To | ``` let kSCPropNetIPSecSharedSecretEncryption: CFString ``` |

Modified [kSCPropNetIPSecStatus](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecStatus: CFString! ``` |
| To | ``` let kSCPropNetIPSecStatus: CFString ``` |

Modified [kSCPropNetIPSecXAuthEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthenabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecXAuthEnabled: CFString! ``` |
| To | ``` let kSCPropNetIPSecXAuthEnabled: CFString ``` |

Modified [kSCPropNetIPSecXAuthName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecXAuthName: CFString! ``` |
| To | ``` let kSCPropNetIPSecXAuthName: CFString ``` |

Modified [kSCPropNetIPSecXAuthPassword](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecXAuthPassword: CFString! ``` |
| To | ``` let kSCPropNetIPSecXAuthPassword: CFString ``` |

Modified [kSCPropNetIPSecXAuthPasswordEncryption](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthpasswordencryption)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPSecXAuthPasswordEncryption: CFString! ``` |
| To | ``` let kSCPropNetIPSecXAuthPasswordEncryption: CFString ``` |

Modified [kSCPropNetIPv4Addresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4addresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4Addresses: CFString! ``` |
| To | ``` let kSCPropNetIPv4Addresses: CFString ``` |

Modified [kSCPropNetIPv4BroadcastAddresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4broadcastaddresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4BroadcastAddresses: CFString! ``` |
| To | ``` let kSCPropNetIPv4BroadcastAddresses: CFString ``` |

Modified [kSCPropNetIPv4ConfigMethod](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4configmethod)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4ConfigMethod: CFString! ``` |
| To | ``` let kSCPropNetIPv4ConfigMethod: CFString ``` |

Modified [kSCPropNetIPv4DestAddresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4destaddresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4DestAddresses: CFString! ``` |
| To | ``` let kSCPropNetIPv4DestAddresses: CFString ``` |

Modified [kSCPropNetIPv4DHCPClientID](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4dhcpclientid)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4DHCPClientID: CFString! ``` |
| To | ``` let kSCPropNetIPv4DHCPClientID: CFString ``` |

Modified [kSCPropNetIPv4Router](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4router)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4Router: CFString! ``` |
| To | ``` let kSCPropNetIPv4Router: CFString ``` |

Modified [kSCPropNetIPv4SubnetMasks](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv4subnetmasks)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv4SubnetMasks: CFString! ``` |
| To | ``` let kSCPropNetIPv4SubnetMasks: CFString ``` |

Modified [kSCPropNetIPv6Addresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6addresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv6Addresses: CFString! ``` |
| To | ``` let kSCPropNetIPv6Addresses: CFString ``` |

Modified [kSCPropNetIPv6ConfigMethod](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6configmethod)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv6ConfigMethod: CFString! ``` |
| To | ``` let kSCPropNetIPv6ConfigMethod: CFString ``` |

Modified [kSCPropNetIPv6DestAddresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6destaddresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv6DestAddresses: CFString! ``` |
| To | ``` let kSCPropNetIPv6DestAddresses: CFString ``` |

Modified [kSCPropNetIPv6Flags](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6flags)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv6Flags: CFString! ``` |
| To | ``` let kSCPropNetIPv6Flags: CFString ``` |

Modified [kSCPropNetIPv6PrefixLength](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6prefixlength)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv6PrefixLength: CFString! ``` |
| To | ``` let kSCPropNetIPv6PrefixLength: CFString ``` |

Modified [kSCPropNetIPv6Router](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipv6router)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetIPv6Router: CFString! ``` |
| To | ``` let kSCPropNetIPv6Router: CFString ``` |

Modified [kSCPropNetL2TPIPSecSharedSecret](https://developer.apple.com/documentation/systemconfiguration/kscpropnetl2tpipsecsharedsecret)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetL2TPIPSecSharedSecret: CFString! ``` |
| To | ``` let kSCPropNetL2TPIPSecSharedSecret: CFString ``` |

Modified [kSCPropNetL2TPIPSecSharedSecretEncryption](https://developer.apple.com/documentation/systemconfiguration/kscpropnetl2tpipsecsharedsecretencryption)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetL2TPIPSecSharedSecretEncryption: CFString! ``` |
| To | ``` let kSCPropNetL2TPIPSecSharedSecretEncryption: CFString ``` |

Modified [kSCPropNetL2TPTransport](https://developer.apple.com/documentation/systemconfiguration/kscpropnetl2tptransport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetL2TPTransport: CFString! ``` |
| To | ``` let kSCPropNetL2TPTransport: CFString ``` |

Modified [kSCPropNetLinkActive](https://developer.apple.com/documentation/systemconfiguration/kscpropnetlinkactive)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetLinkActive: CFString! ``` |
| To | ``` let kSCPropNetLinkActive: CFString ``` |

Modified [kSCPropNetLinkDetaching](https://developer.apple.com/documentation/systemconfiguration/kscpropnetlinkdetaching)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetLinkDetaching: CFString! ``` |
| To | ``` let kSCPropNetLinkDetaching: CFString ``` |

Modified [kSCPropNetLocalHostName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetlocalhostname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetLocalHostName: CFString! ``` |
| To | ``` let kSCPropNetLocalHostName: CFString ``` |

Modified [kSCPropNetModemAccessPointName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemaccesspointname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemAccessPointName: CFString! ``` |
| To | ``` let kSCPropNetModemAccessPointName: CFString ``` |

Modified [kSCPropNetModemConnectionPersonality](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemconnectionpersonality)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemConnectionPersonality: CFString! ``` |
| To | ``` let kSCPropNetModemConnectionPersonality: CFString ``` |

Modified [kSCPropNetModemConnectionScript](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemconnectionscript)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemConnectionScript: CFString! ``` |
| To | ``` let kSCPropNetModemConnectionScript: CFString ``` |

Modified [kSCPropNetModemConnectSpeed](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemconnectspeed)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemConnectSpeed: CFString! ``` |
| To | ``` let kSCPropNetModemConnectSpeed: CFString ``` |

Modified [kSCPropNetModemDataCompression](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemdatacompression)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemDataCompression: CFString! ``` |
| To | ``` let kSCPropNetModemDataCompression: CFString ``` |

Modified [kSCPropNetModemDeviceContextID](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemdevicecontextid)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemDeviceContextID: CFString! ``` |
| To | ``` let kSCPropNetModemDeviceContextID: CFString ``` |

Modified [kSCPropNetModemDeviceModel](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemdevicemodel)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemDeviceModel: CFString! ``` |
| To | ``` let kSCPropNetModemDeviceModel: CFString ``` |

Modified [kSCPropNetModemDeviceVendor](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemdevicevendor)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemDeviceVendor: CFString! ``` |
| To | ``` let kSCPropNetModemDeviceVendor: CFString ``` |

Modified [kSCPropNetModemDialMode](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemdialmode)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemDialMode: CFString! ``` |
| To | ``` let kSCPropNetModemDialMode: CFString ``` |

Modified [kSCPropNetModemErrorCorrection](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemerrorcorrection)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemErrorCorrection: CFString! ``` |
| To | ``` let kSCPropNetModemErrorCorrection: CFString ``` |

Modified [kSCPropNetModemHoldCallWaitingAudibleAlert](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemholdcallwaitingaudiblealert)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemHoldCallWaitingAudibleAlert: CFString! ``` |
| To | ``` let kSCPropNetModemHoldCallWaitingAudibleAlert: CFString ``` |

Modified [kSCPropNetModemHoldDisconnectOnAnswer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemholddisconnectonanswer)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemHoldDisconnectOnAnswer: CFString! ``` |
| To | ``` let kSCPropNetModemHoldDisconnectOnAnswer: CFString ``` |

Modified [kSCPropNetModemHoldEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemholdenabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemHoldEnabled: CFString! ``` |
| To | ``` let kSCPropNetModemHoldEnabled: CFString ``` |

Modified [kSCPropNetModemHoldReminder](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemholdreminder)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemHoldReminder: CFString! ``` |
| To | ``` let kSCPropNetModemHoldReminder: CFString ``` |

Modified [kSCPropNetModemHoldReminderTime](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemholdremindertime)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemHoldReminderTime: CFString! ``` |
| To | ``` let kSCPropNetModemHoldReminderTime: CFString ``` |

Modified [kSCPropNetModemNote](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemnote)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemNote: CFString! ``` |
| To | ``` let kSCPropNetModemNote: CFString ``` |

Modified [kSCPropNetModemPulseDial](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodempulsedial)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemPulseDial: CFString! ``` |
| To | ``` let kSCPropNetModemPulseDial: CFString ``` |

Modified [kSCPropNetModemSpeaker](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemspeaker)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemSpeaker: CFString! ``` |
| To | ``` let kSCPropNetModemSpeaker: CFString ``` |

Modified [kSCPropNetModemSpeed](https://developer.apple.com/documentation/systemconfiguration/kscpropnetmodemspeed)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetModemSpeed: CFString! ``` |
| To | ``` let kSCPropNetModemSpeed: CFString ``` |

Modified [kSCPropNetOverridePrimary](https://developer.apple.com/documentation/systemconfiguration/kscpropnetoverrideprimary)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetOverridePrimary: CFString! ``` |
| To | ``` let kSCPropNetOverridePrimary: CFString ``` |

Modified [kSCPropNetPPPACSPEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppacspenabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPACSPEnabled: CFString! ``` |
| To | ``` let kSCPropNetPPPACSPEnabled: CFString ``` |

Modified [kSCPropNetPPPAuthEAPPlugins](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppautheapplugins)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPAuthEAPPlugins: CFString! ``` |
| To | ``` let kSCPropNetPPPAuthEAPPlugins: CFString ``` |

Modified [kSCPropNetPPPAuthName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppauthname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPAuthName: CFString! ``` |
| To | ``` let kSCPropNetPPPAuthName: CFString ``` |

Modified [kSCPropNetPPPAuthPassword](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppauthpassword)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPAuthPassword: CFString! ``` |
| To | ``` let kSCPropNetPPPAuthPassword: CFString ``` |

Modified [kSCPropNetPPPAuthPasswordEncryption](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppauthpasswordencryption)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPAuthPasswordEncryption: CFString! ``` |
| To | ``` let kSCPropNetPPPAuthPasswordEncryption: CFString ``` |

Modified [kSCPropNetPPPAuthPrompt](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppauthprompt)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPAuthPrompt: CFString! ``` |
| To | ``` let kSCPropNetPPPAuthPrompt: CFString ``` |

Modified [kSCPropNetPPPAuthProtocol](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppauthprotocol)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPAuthProtocol: CFString! ``` |
| To | ``` let kSCPropNetPPPAuthProtocol: CFString ``` |

Modified [kSCPropNetPPPCCPEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppccpenabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCCPEnabled: CFString! ``` |
| To | ``` let kSCPropNetPPPCCPEnabled: CFString ``` |

Modified [kSCPropNetPPPCCPMPPE128Enabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppccpmppe128enabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCCPMPPE128Enabled: CFString! ``` |
| To | ``` let kSCPropNetPPPCCPMPPE128Enabled: CFString ``` |

Modified [kSCPropNetPPPCCPMPPE40Enabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppccpmppe40enabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCCPMPPE40Enabled: CFString! ``` |
| To | ``` let kSCPropNetPPPCCPMPPE40Enabled: CFString ``` |

Modified [kSCPropNetPPPCommAlternateRemoteAddress](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommalternateremoteaddress)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommAlternateRemoteAddress: CFString! ``` |
| To | ``` let kSCPropNetPPPCommAlternateRemoteAddress: CFString ``` |

Modified [kSCPropNetPPPCommConnectDelay](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommconnectdelay)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommConnectDelay: CFString! ``` |
| To | ``` let kSCPropNetPPPCommConnectDelay: CFString ``` |

Modified [kSCPropNetPPPCommDisplayTerminalWindow](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommdisplayterminalwindow)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommDisplayTerminalWindow: CFString! ``` |
| To | ``` let kSCPropNetPPPCommDisplayTerminalWindow: CFString ``` |

Modified [kSCPropNetPPPCommRedialCount](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommredialcount)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommRedialCount: CFString! ``` |
| To | ``` let kSCPropNetPPPCommRedialCount: CFString ``` |

Modified [kSCPropNetPPPCommRedialEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommredialenabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommRedialEnabled: CFString! ``` |
| To | ``` let kSCPropNetPPPCommRedialEnabled: CFString ``` |

Modified [kSCPropNetPPPCommRedialInterval](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommredialinterval)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommRedialInterval: CFString! ``` |
| To | ``` let kSCPropNetPPPCommRedialInterval: CFString ``` |

Modified [kSCPropNetPPPCommRemoteAddress](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommremoteaddress)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommRemoteAddress: CFString! ``` |
| To | ``` let kSCPropNetPPPCommRemoteAddress: CFString ``` |

Modified [kSCPropNetPPPCommTerminalScript](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommterminalscript)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommTerminalScript: CFString! ``` |
| To | ``` let kSCPropNetPPPCommTerminalScript: CFString ``` |

Modified [kSCPropNetPPPCommUseTerminalScript](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppcommuseterminalscript)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPCommUseTerminalScript: CFString! ``` |
| To | ``` let kSCPropNetPPPCommUseTerminalScript: CFString ``` |

Modified [kSCPropNetPPPConnectTime](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppconnecttime)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPConnectTime: CFString! ``` |
| To | ``` let kSCPropNetPPPConnectTime: CFString ``` |

Modified [kSCPropNetPPPDeviceLastCause](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdevicelastcause)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDeviceLastCause: CFString! ``` |
| To | ``` let kSCPropNetPPPDeviceLastCause: CFString ``` |

Modified [kSCPropNetPPPDialOnDemand](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdialondemand)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDialOnDemand: CFString! ``` |
| To | ``` let kSCPropNetPPPDialOnDemand: CFString ``` |

Modified [kSCPropNetPPPDisconnectOnFastUserSwitch](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdisconnectonfastuserswitch)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDisconnectOnFastUserSwitch: CFString! ``` |
| To | ``` let kSCPropNetPPPDisconnectOnFastUserSwitch: CFString ``` |

Modified [kSCPropNetPPPDisconnectOnIdle](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdisconnectonidle)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDisconnectOnIdle: CFString! ``` |
| To | ``` let kSCPropNetPPPDisconnectOnIdle: CFString ``` |

Modified [kSCPropNetPPPDisconnectOnIdleTimer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdisconnectonidletimer)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDisconnectOnIdleTimer: CFString! ``` |
| To | ``` let kSCPropNetPPPDisconnectOnIdleTimer: CFString ``` |

Modified [kSCPropNetPPPDisconnectOnLogout](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdisconnectonlogout)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDisconnectOnLogout: CFString! ``` |
| To | ``` let kSCPropNetPPPDisconnectOnLogout: CFString ``` |

Modified [kSCPropNetPPPDisconnectOnSleep](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdisconnectonsleep)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDisconnectOnSleep: CFString! ``` |
| To | ``` let kSCPropNetPPPDisconnectOnSleep: CFString ``` |

Modified [kSCPropNetPPPDisconnectTime](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppdisconnecttime)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPDisconnectTime: CFString! ``` |
| To | ``` let kSCPropNetPPPDisconnectTime: CFString ``` |

Modified [kSCPropNetPPPIdleReminder](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppidlereminder)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPIdleReminder: CFString! ``` |
| To | ``` let kSCPropNetPPPIdleReminder: CFString ``` |

Modified [kSCPropNetPPPIdleReminderTimer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppidleremindertimer)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPIdleReminderTimer: CFString! ``` |
| To | ``` let kSCPropNetPPPIdleReminderTimer: CFString ``` |

Modified [kSCPropNetPPPIPCPCompressionVJ](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppipcpcompressionvj)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPIPCPCompressionVJ: CFString! ``` |
| To | ``` let kSCPropNetPPPIPCPCompressionVJ: CFString ``` |

Modified [kSCPropNetPPPIPCPUsePeerDNS](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppipcpusepeerdns)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPIPCPUsePeerDNS: CFString! ``` |
| To | ``` let kSCPropNetPPPIPCPUsePeerDNS: CFString ``` |

Modified [kSCPropNetPPPLastCause](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplastcause)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLastCause: CFString! ``` |
| To | ``` let kSCPropNetPPPLastCause: CFString ``` |

Modified [kSCPropNetPPPLCPCompressionACField](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpcompressionacfield)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPCompressionACField: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPCompressionACField: CFString ``` |

Modified [kSCPropNetPPPLCPCompressionPField](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpcompressionpfield)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPCompressionPField: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPCompressionPField: CFString ``` |

Modified [kSCPropNetPPPLCPEchoEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpechoenabled)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPEchoEnabled: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPEchoEnabled: CFString ``` |

Modified [kSCPropNetPPPLCPEchoFailure](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpechofailure)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPEchoFailure: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPEchoFailure: CFString ``` |

Modified [kSCPropNetPPPLCPEchoInterval](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpechointerval)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPEchoInterval: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPEchoInterval: CFString ``` |

Modified [kSCPropNetPPPLCPMRU](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpmru)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPMRU: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPMRU: CFString ``` |

Modified [kSCPropNetPPPLCPMTU](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpmtu)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPMTU: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPMTU: CFString ``` |

Modified [kSCPropNetPPPLCPReceiveACCM](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcpreceiveaccm)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPReceiveACCM: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPReceiveACCM: CFString ``` |

Modified [kSCPropNetPPPLCPTransmitACCM](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplcptransmitaccm)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLCPTransmitACCM: CFString! ``` |
| To | ``` let kSCPropNetPPPLCPTransmitACCM: CFString ``` |

Modified [kSCPropNetPPPLogfile](https://developer.apple.com/documentation/systemconfiguration/kscpropnetppplogfile)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPLogfile: CFString! ``` |
| To | ``` let kSCPropNetPPPLogfile: CFString ``` |

Modified [kSCPropNetPPPOverridePrimary](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppoverrideprimary)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPOverridePrimary: CFString! ``` |
| To | ``` let kSCPropNetPPPOverridePrimary: CFString ``` |

Modified [kSCPropNetPPPPlugins](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppplugins)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPPlugins: CFString! ``` |
| To | ``` let kSCPropNetPPPPlugins: CFString ``` |

Modified [kSCPropNetPPPRetryConnectTime](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppretryconnecttime)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPRetryConnectTime: CFString! ``` |
| To | ``` let kSCPropNetPPPRetryConnectTime: CFString ``` |

Modified [kSCPropNetPPPSessionTimer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppsessiontimer)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPSessionTimer: CFString! ``` |
| To | ``` let kSCPropNetPPPSessionTimer: CFString ``` |

Modified [kSCPropNetPPPStatus](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPStatus: CFString! ``` |
| To | ``` let kSCPropNetPPPStatus: CFString ``` |

Modified [kSCPropNetPPPUseSessionTimer](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppusesessiontimer)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPUseSessionTimer: CFString! ``` |
| To | ``` let kSCPropNetPPPUseSessionTimer: CFString ``` |

Modified [kSCPropNetPPPVerboseLogging](https://developer.apple.com/documentation/systemconfiguration/kscpropnetpppverboselogging)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetPPPVerboseLogging: CFString! ``` |
| To | ``` let kSCPropNetPPPVerboseLogging: CFString ``` |

Modified [kSCPropNetProxiesExceptionsList](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesexceptionslist)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesExceptionsList: CFString! ``` |
| To | ``` let kSCPropNetProxiesExceptionsList: CFString ``` |

Modified [kSCPropNetProxiesExcludeSimpleHostnames](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesexcludesimplehostnames)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesExcludeSimpleHostnames: CFString! ``` |
| To | ``` let kSCPropNetProxiesExcludeSimpleHostnames: CFString ``` |

Modified [kSCPropNetProxiesFTPEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesftpenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesFTPEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesFTPEnable: CFString ``` |

Modified [kSCPropNetProxiesFTPPassive](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesftppassive)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesFTPPassive: CFString! ``` |
| To | ``` let kSCPropNetProxiesFTPPassive: CFString ``` |

Modified [kSCPropNetProxiesFTPPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesftpport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesFTPPort: CFString! ``` |
| To | ``` let kSCPropNetProxiesFTPPort: CFString ``` |

Modified [kSCPropNetProxiesFTPProxy](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesftpproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesFTPProxy: CFString! ``` |
| To | ``` let kSCPropNetProxiesFTPProxy: CFString ``` |

Modified [kSCPropNetProxiesGopherEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesgopherenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesGopherEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesGopherEnable: CFString ``` |

Modified [kSCPropNetProxiesGopherPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesgopherport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesGopherPort: CFString! ``` |
| To | ``` let kSCPropNetProxiesGopherPort: CFString ``` |

Modified [kSCPropNetProxiesGopherProxy](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesgopherproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesGopherProxy: CFString! ``` |
| To | ``` let kSCPropNetProxiesGopherProxy: CFString ``` |

Modified [kSCPropNetProxiesHTTPEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxieshttpenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesHTTPEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesHTTPEnable: CFString ``` |

Modified [kSCPropNetProxiesHTTPPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxieshttpport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesHTTPPort: CFString! ``` |
| To | ``` let kSCPropNetProxiesHTTPPort: CFString ``` |

Modified [kSCPropNetProxiesHTTPProxy](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxieshttpproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesHTTPProxy: CFString! ``` |
| To | ``` let kSCPropNetProxiesHTTPProxy: CFString ``` |

Modified [kSCPropNetProxiesHTTPSEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxieshttpsenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesHTTPSEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesHTTPSEnable: CFString ``` |

Modified [kSCPropNetProxiesHTTPSPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxieshttpsport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesHTTPSPort: CFString! ``` |
| To | ``` let kSCPropNetProxiesHTTPSPort: CFString ``` |

Modified [kSCPropNetProxiesHTTPSProxy](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxieshttpsproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesHTTPSProxy: CFString! ``` |
| To | ``` let kSCPropNetProxiesHTTPSProxy: CFString ``` |

Modified [kSCPropNetProxiesProxyAutoConfigEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesproxyautoconfigenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesProxyAutoConfigEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesProxyAutoConfigEnable: CFString ``` |

Modified [kSCPropNetProxiesProxyAutoConfigJavaScript](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesproxyautoconfigjavascript)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesProxyAutoConfigJavaScript: CFString! ``` |
| To | ``` let kSCPropNetProxiesProxyAutoConfigJavaScript: CFString ``` |

Modified [kSCPropNetProxiesProxyAutoConfigURLString](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesproxyautoconfigurlstring)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesProxyAutoConfigURLString: CFString! ``` |
| To | ``` let kSCPropNetProxiesProxyAutoConfigURLString: CFString ``` |

Modified [kSCPropNetProxiesProxyAutoDiscoveryEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesproxyautodiscoveryenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesProxyAutoDiscoveryEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesProxyAutoDiscoveryEnable: CFString ``` |

Modified [kSCPropNetProxiesRTSPEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesrtspenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesRTSPEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesRTSPEnable: CFString ``` |

Modified [kSCPropNetProxiesRTSPPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesrtspport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesRTSPPort: CFString! ``` |
| To | ``` let kSCPropNetProxiesRTSPPort: CFString ``` |

Modified [kSCPropNetProxiesRTSPProxy](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiesrtspproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesRTSPProxy: CFString! ``` |
| To | ``` let kSCPropNetProxiesRTSPProxy: CFString ``` |

Modified [kSCPropNetProxiesSOCKSEnable](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiessocksenable)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesSOCKSEnable: CFString! ``` |
| To | ``` let kSCPropNetProxiesSOCKSEnable: CFString ``` |

Modified [kSCPropNetProxiesSOCKSPort](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiessocksport)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesSOCKSPort: CFString! ``` |
| To | ``` let kSCPropNetProxiesSOCKSPort: CFString ``` |

Modified [kSCPropNetProxiesSOCKSProxy](https://developer.apple.com/documentation/systemconfiguration/kscpropnetproxiessocksproxy)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetProxiesSOCKSProxy: CFString! ``` |
| To | ``` let kSCPropNetProxiesSOCKSProxy: CFString ``` |

Modified [kSCPropNetServiceOrder](https://developer.apple.com/documentation/systemconfiguration/kscpropnetserviceorder)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetServiceOrder: CFString! ``` |
| To | ``` let kSCPropNetServiceOrder: CFString ``` |

Modified [kSCPropNetSMBNetBIOSName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetsmbnetbiosname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetSMBNetBIOSName: CFString! ``` |
| To | ``` let kSCPropNetSMBNetBIOSName: CFString ``` |

Modified [kSCPropNetSMBNetBIOSNodeType](https://developer.apple.com/documentation/systemconfiguration/kscpropnetsmbnetbiosnodetype)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetSMBNetBIOSNodeType: CFString! ``` |
| To | ``` let kSCPropNetSMBNetBIOSNodeType: CFString ``` |

Modified [kSCPropNetSMBWINSAddresses](https://developer.apple.com/documentation/systemconfiguration/kscpropnetsmbwinsaddresses)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetSMBWINSAddresses: CFString! ``` |
| To | ``` let kSCPropNetSMBWINSAddresses: CFString ``` |

Modified [kSCPropNetSMBWorkgroup](https://developer.apple.com/documentation/systemconfiguration/kscpropnetsmbworkgroup)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropNetSMBWorkgroup: CFString! ``` |
| To | ``` let kSCPropNetSMBWorkgroup: CFString ``` |

Modified [kSCPropSystemComputerName](https://developer.apple.com/documentation/systemconfiguration/kscpropsystemcomputername)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropSystemComputerName: CFString! ``` |
| To | ``` let kSCPropSystemComputerName: CFString ``` |

Modified [kSCPropSystemComputerNameEncoding](https://developer.apple.com/documentation/systemconfiguration/kscpropsystemcomputernameencoding)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropSystemComputerNameEncoding: CFString! ``` |
| To | ``` let kSCPropSystemComputerNameEncoding: CFString ``` |

Modified [kSCPropUserDefinedName](https://developer.apple.com/documentation/systemconfiguration/kscpropuserdefinedname)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropUserDefinedName: CFString! ``` |
| To | ``` let kSCPropUserDefinedName: CFString ``` |

Modified [kSCPropVersion](https://developer.apple.com/documentation/systemconfiguration/kscpropversion)

|  | Declaration |
| --- | --- |
| From | ``` let kSCPropVersion: CFString! ``` |
| To | ``` let kSCPropVersion: CFString ``` |

Modified [kSCResvInactive](https://developer.apple.com/documentation/systemconfiguration/kscresvinactive)

|  | Declaration |
| --- | --- |
| From | ``` let kSCResvInactive: CFString! ``` |
| To | ``` let kSCResvInactive: CFString ``` |

Modified [kSCResvLink](https://developer.apple.com/documentation/systemconfiguration/kscresvlink)

|  | Declaration |
| --- | --- |
| From | ``` let kSCResvLink: CFString! ``` |
| To | ``` let kSCResvLink: CFString ``` |

Modified [kSCValNetInterfaceSubTypeL2TP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacesubtypel2tp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceSubTypeL2TP: CFString! ``` |
| To | ``` let kSCValNetInterfaceSubTypeL2TP: CFString ``` |

Modified [kSCValNetInterfaceSubTypePPPoE](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacesubtypepppoe)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceSubTypePPPoE: CFString! ``` |
| To | ``` let kSCValNetInterfaceSubTypePPPoE: CFString ``` |

Modified [kSCValNetInterfaceSubTypePPPSerial](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacesubtypepppserial)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceSubTypePPPSerial: CFString! ``` |
| To | ``` let kSCValNetInterfaceSubTypePPPSerial: CFString ``` |

Modified [kSCValNetInterfaceSubTypePPTP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacesubtypepptp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceSubTypePPTP: CFString! ``` |
| To | ``` let kSCValNetInterfaceSubTypePPTP: CFString ``` |

Modified [kSCValNetInterfaceType6to4](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacetype6to4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceType6to4: CFString! ``` |
| To | ``` let kSCValNetInterfaceType6to4: CFString ``` |

Modified [kSCValNetInterfaceTypeEthernet](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacetypeethernet)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceTypeEthernet: CFString! ``` |
| To | ``` let kSCValNetInterfaceTypeEthernet: CFString ``` |

Modified [kSCValNetInterfaceTypeFireWire](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacetypefirewire)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceTypeFireWire: CFString! ``` |
| To | ``` let kSCValNetInterfaceTypeFireWire: CFString ``` |

Modified [kSCValNetInterfaceTypeIPSec](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacetypeipsec)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceTypeIPSec: CFString! ``` |
| To | ``` let kSCValNetInterfaceTypeIPSec: CFString ``` |

Modified [kSCValNetInterfaceTypePPP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacetypeppp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetInterfaceTypePPP: CFString! ``` |
| To | ``` let kSCValNetInterfaceTypePPP: CFString ``` |

Modified [kSCValNetIPSecAuthenticationMethodCertificate](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecauthenticationmethodcertificate)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecAuthenticationMethodCertificate: CFString! ``` |
| To | ``` let kSCValNetIPSecAuthenticationMethodCertificate: CFString ``` |

Modified [kSCValNetIPSecAuthenticationMethodHybrid](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecauthenticationmethodhybrid)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecAuthenticationMethodHybrid: CFString! ``` |
| To | ``` let kSCValNetIPSecAuthenticationMethodHybrid: CFString ``` |

Modified [kSCValNetIPSecAuthenticationMethodSharedSecret](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecauthenticationmethodsharedsecret)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecAuthenticationMethodSharedSecret: CFString! ``` |
| To | ``` let kSCValNetIPSecAuthenticationMethodSharedSecret: CFString ``` |

Modified [kSCValNetIPSecLocalIdentifierTypeKeyID](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipseclocalidentifiertypekeyid)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecLocalIdentifierTypeKeyID: CFString! ``` |
| To | ``` let kSCValNetIPSecLocalIdentifierTypeKeyID: CFString ``` |

Modified [kSCValNetIPSecSharedSecretEncryptionKeychain](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecsharedsecretencryptionkeychain)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecSharedSecretEncryptionKeychain: CFString! ``` |
| To | ``` let kSCValNetIPSecSharedSecretEncryptionKeychain: CFString ``` |

Modified [kSCValNetIPSecXAuthPasswordEncryptionKeychain](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecxauthpasswordencryptionkeychain)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecXAuthPasswordEncryptionKeychain: CFString! ``` |
| To | ``` let kSCValNetIPSecXAuthPasswordEncryptionKeychain: CFString ``` |

Modified [kSCValNetIPSecXAuthPasswordEncryptionPrompt](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecxauthpasswordencryptionprompt)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPSecXAuthPasswordEncryptionPrompt: CFString! ``` |
| To | ``` let kSCValNetIPSecXAuthPasswordEncryptionPrompt: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodAutomatic](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethodautomatic)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodAutomatic: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodAutomatic: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodBOOTP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethodbootp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodBOOTP: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodBOOTP: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodDHCP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethoddhcp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodDHCP: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodDHCP: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodINFORM](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethodinform)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodINFORM: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodINFORM: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodLinkLocal](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethodlinklocal)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodLinkLocal: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodLinkLocal: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodManual](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethodmanual)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodManual: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodManual: CFString ``` |

Modified [kSCValNetIPv4ConfigMethodPPP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv4configmethodppp)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv4ConfigMethodPPP: CFString! ``` |
| To | ``` let kSCValNetIPv4ConfigMethodPPP: CFString ``` |

Modified [kSCValNetIPv6ConfigMethod6to4](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv6configmethod6to4)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv6ConfigMethod6to4: CFString! ``` |
| To | ``` let kSCValNetIPv6ConfigMethod6to4: CFString ``` |

Modified [kSCValNetIPv6ConfigMethodAutomatic](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv6configmethodautomatic)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv6ConfigMethodAutomatic: CFString! ``` |
| To | ``` let kSCValNetIPv6ConfigMethodAutomatic: CFString ``` |

Modified [kSCValNetIPv6ConfigMethodLinkLocal](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv6configmethodlinklocal)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv6ConfigMethodLinkLocal: CFString! ``` |
| To | ``` let kSCValNetIPv6ConfigMethodLinkLocal: CFString ``` |

Modified [kSCValNetIPv6ConfigMethodManual](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv6configmethodmanual)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv6ConfigMethodManual: CFString! ``` |
| To | ``` let kSCValNetIPv6ConfigMethodManual: CFString ``` |

Modified [kSCValNetIPv6ConfigMethodRouterAdvertisement](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipv6configmethodrouteradvertisement)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetIPv6ConfigMethodRouterAdvertisement: CFString! ``` |
| To | ``` let kSCValNetIPv6ConfigMethodRouterAdvertisement: CFString ``` |

Modified [kSCValNetL2TPIPSecSharedSecretEncryptionKeychain](https://developer.apple.com/documentation/systemconfiguration/kscvalnetl2tpipsecsharedsecretencryptionkeychain)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetL2TPIPSecSharedSecretEncryptionKeychain: CFString! ``` |
| To | ``` let kSCValNetL2TPIPSecSharedSecretEncryptionKeychain: CFString ``` |

Modified [kSCValNetL2TPTransportIP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetl2tptransportip)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetL2TPTransportIP: CFString! ``` |
| To | ``` let kSCValNetL2TPTransportIP: CFString ``` |

Modified [kSCValNetL2TPTransportIPSec](https://developer.apple.com/documentation/systemconfiguration/kscvalnetl2tptransportipsec)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetL2TPTransportIPSec: CFString! ``` |
| To | ``` let kSCValNetL2TPTransportIPSec: CFString ``` |

Modified [kSCValNetModemDialModeIgnoreDialTone](https://developer.apple.com/documentation/systemconfiguration/kscvalnetmodemdialmodeignoredialtone)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetModemDialModeIgnoreDialTone: CFString! ``` |
| To | ``` let kSCValNetModemDialModeIgnoreDialTone: CFString ``` |

Modified [kSCValNetModemDialModeManual](https://developer.apple.com/documentation/systemconfiguration/kscvalnetmodemdialmodemanual)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetModemDialModeManual: CFString! ``` |
| To | ``` let kSCValNetModemDialModeManual: CFString ``` |

Modified [kSCValNetModemDialModeWaitForDialTone](https://developer.apple.com/documentation/systemconfiguration/kscvalnetmodemdialmodewaitfordialtone)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetModemDialModeWaitForDialTone: CFString! ``` |
| To | ``` let kSCValNetModemDialModeWaitForDialTone: CFString ``` |

Modified [kSCValNetPPPAuthPasswordEncryptionKeychain](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthpasswordencryptionkeychain)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthPasswordEncryptionKeychain: CFString! ``` |
| To | ``` let kSCValNetPPPAuthPasswordEncryptionKeychain: CFString ``` |

Modified [kSCValNetPPPAuthPasswordEncryptionToken](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthpasswordencryptiontoken)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthPasswordEncryptionToken: CFString! ``` |
| To | ``` let kSCValNetPPPAuthPasswordEncryptionToken: CFString ``` |

Modified [kSCValNetPPPAuthPromptAfter](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthpromptafter)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthPromptAfter: CFString! ``` |
| To | ``` let kSCValNetPPPAuthPromptAfter: CFString ``` |

Modified [kSCValNetPPPAuthPromptBefore](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthpromptbefore)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthPromptBefore: CFString! ``` |
| To | ``` let kSCValNetPPPAuthPromptBefore: CFString ``` |

Modified [kSCValNetPPPAuthProtocolCHAP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthprotocolchap)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthProtocolCHAP: CFString! ``` |
| To | ``` let kSCValNetPPPAuthProtocolCHAP: CFString ``` |

Modified [kSCValNetPPPAuthProtocolEAP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthprotocoleap)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthProtocolEAP: CFString! ``` |
| To | ``` let kSCValNetPPPAuthProtocolEAP: CFString ``` |

Modified [kSCValNetPPPAuthProtocolMSCHAP1](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthprotocolmschap1)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthProtocolMSCHAP1: CFString! ``` |
| To | ``` let kSCValNetPPPAuthProtocolMSCHAP1: CFString ``` |

Modified [kSCValNetPPPAuthProtocolMSCHAP2](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthprotocolmschap2)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthProtocolMSCHAP2: CFString! ``` |
| To | ``` let kSCValNetPPPAuthProtocolMSCHAP2: CFString ``` |

Modified [kSCValNetPPPAuthProtocolPAP](https://developer.apple.com/documentation/systemconfiguration/kscvalnetpppauthprotocolpap)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetPPPAuthProtocolPAP: CFString! ``` |
| To | ``` let kSCValNetPPPAuthProtocolPAP: CFString ``` |

Modified [kSCValNetSMBNetBIOSNodeTypeBroadcast](https://developer.apple.com/documentation/systemconfiguration/kscvalnetsmbnetbiosnodetypebroadcast)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetSMBNetBIOSNodeTypeBroadcast: CFString! ``` |
| To | ``` let kSCValNetSMBNetBIOSNodeTypeBroadcast: CFString ``` |

Modified [kSCValNetSMBNetBIOSNodeTypeHybrid](https://developer.apple.com/documentation/systemconfiguration/kscvalnetsmbnetbiosnodetypehybrid)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetSMBNetBIOSNodeTypeHybrid: CFString! ``` |
| To | ``` let kSCValNetSMBNetBIOSNodeTypeHybrid: CFString ``` |

Modified [kSCValNetSMBNetBIOSNodeTypeMixed](https://developer.apple.com/documentation/systemconfiguration/kscvalnetsmbnetbiosnodetypemixed)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetSMBNetBIOSNodeTypeMixed: CFString! ``` |
| To | ``` let kSCValNetSMBNetBIOSNodeTypeMixed: CFString ``` |

Modified [kSCValNetSMBNetBIOSNodeTypePeer](https://developer.apple.com/documentation/systemconfiguration/kscvalnetsmbnetbiosnodetypepeer)

|  | Declaration |
| --- | --- |
| From | ``` let kSCValNetSMBNetBIOSNodeTypePeer: CFString! ``` |
| To | ``` let kSCValNetSMBNetBIOSNodeTypePeer: CFString ``` |

Modified [SCBondInterfaceCopyAll(_: SCPreferences) -> CFArray](https://developer.apple.com/documentation/systemconfiguration/1517283-scbondinterfacecopyall)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceCopyAll(_ prefs: SCPreferences!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCBondInterfaceCopyAll(_ prefs: SCPreferences) -> CFArray ``` |

Modified [SCBondInterfaceCopyAvailableMemberInterfaces(_: SCPreferences) -> CFArray](https://developer.apple.com/documentation/systemconfiguration/1516848-scbondinterfacecopyavailablememb)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceCopyAvailableMemberInterfaces(_ prefs: SCPreferences!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCBondInterfaceCopyAvailableMemberInterfaces(_ prefs: SCPreferences) -> CFArray ``` |

Modified [SCBondInterfaceCopyStatus(_: SCBondInterface) -> SCBondStatus?](https://developer.apple.com/documentation/systemconfiguration/1517046-scbondinterfacecopystatus)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceCopyStatus(_ bond: SCBondInterface!) -> Unmanaged<SCBondStatus>! ``` |
| To | ``` func SCBondInterfaceCopyStatus(_ bond: SCBondInterface) -> SCBondStatus? ``` |

Modified [SCBondInterfaceCreate(_: SCPreferences) -> SCBondInterface?](https://developer.apple.com/documentation/systemconfiguration/1517251-scbondinterfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceCreate(_ prefs: SCPreferences!) -> Unmanaged<SCBondInterface>! ``` |
| To | ``` func SCBondInterfaceCreate(_ prefs: SCPreferences) -> SCBondInterface? ``` |

Modified [SCBondInterfaceGetMemberInterfaces(_: SCBondInterface) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1516896-scbondinterfacegetmemberinterfac)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceGetMemberInterfaces(_ bond: SCBondInterface!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCBondInterfaceGetMemberInterfaces(_ bond: SCBondInterface) -> CFArray? ``` |

Modified [SCBondInterfaceGetOptions(_: SCBondInterface) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1517018-scbondinterfacegetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceGetOptions(_ bond: SCBondInterface!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCBondInterfaceGetOptions(_ bond: SCBondInterface) -> CFDictionary? ``` |

Modified [SCBondInterfaceRemove(_: SCBondInterface) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517223-scbondinterfaceremove)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceRemove(_ bond: SCBondInterface!) -> Boolean ``` |
| To | ``` func SCBondInterfaceRemove(_ bond: SCBondInterface) -> Bool ``` |

Modified [SCBondInterfaceSetLocalizedDisplayName(_: SCBondInterface, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516742-scbondinterfacesetlocalizeddispl)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceSetLocalizedDisplayName(_ bond: SCBondInterface!, _ newName: CFString!) -> Boolean ``` |
| To | ``` func SCBondInterfaceSetLocalizedDisplayName(_ bond: SCBondInterface, _ newName: CFString) -> Bool ``` |

Modified [SCBondInterfaceSetMemberInterfaces(_: SCBondInterface, _: CFArray) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517285-scbondinterfacesetmemberinterfac)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceSetMemberInterfaces(_ bond: SCBondInterface!, _ members: CFArray!) -> Boolean ``` |
| To | ``` func SCBondInterfaceSetMemberInterfaces(_ bond: SCBondInterface, _ members: CFArray) -> Bool ``` |

Modified [SCBondInterfaceSetOptions(_: SCBondInterface, _: CFDictionary) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516818-scbondinterfacesetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondInterfaceSetOptions(_ bond: SCBondInterface!, _ newOptions: CFDictionary!) -> Boolean ``` |
| To | ``` func SCBondInterfaceSetOptions(_ bond: SCBondInterface, _ newOptions: CFDictionary) -> Bool ``` |

Modified [SCBondStatusGetInterfaceStatus(_: SCBondStatus, _: SCNetworkInterface?) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1517119-scbondstatusgetinterfacestatus)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondStatusGetInterfaceStatus(_ bondStatus: SCBondStatus!, _ interface: SCNetworkInterface!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCBondStatusGetInterfaceStatus(_ bondStatus: SCBondStatus, _ interface: SCNetworkInterface?) -> CFDictionary? ``` |

Modified [SCBondStatusGetMemberInterfaces(_: SCBondStatus) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1517239-scbondstatusgetmemberinterfaces)

|  | Declaration |
| --- | --- |
| From | ``` func SCBondStatusGetMemberInterfaces(_ bondStatus: SCBondStatus!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCBondStatusGetMemberInterfaces(_ bondStatus: SCBondStatus) -> CFArray? ``` |

Modified [SCCopyLastError() -> CFError](https://developer.apple.com/documentation/systemconfiguration/1517326-sccopylasterror)

|  | Declaration |
| --- | --- |
| From | ``` func SCCopyLastError() -> Unmanaged<CFError>! ``` |
| To | ``` func SCCopyLastError() -> CFError ``` |

Modified [SCDynamicStoreAddTemporaryValue(_: SCDynamicStore, _: CFString, _: CFPropertyList) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437789-scdynamicstoreaddtemporaryvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreAddTemporaryValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` |
| To | ``` func SCDynamicStoreAddTemporaryValue(_ store: SCDynamicStore, _ key: CFString, _ value: CFPropertyList) -> Bool ``` |

Modified [SCDynamicStoreAddValue(_: SCDynamicStore?, _: CFString, _: CFPropertyList) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437785-scdynamicstoreaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreAddValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` |
| To | ``` func SCDynamicStoreAddValue(_ store: SCDynamicStore?, _ key: CFString, _ value: CFPropertyList) -> Bool ``` |

Modified [SCDynamicStoreCallBack](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCDynamicStoreCallBack = CFunctionPointer<((SCDynamicStore!, CFArray!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCDynamicStoreCallBack = (SCDynamicStore, CFArray, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [SCDynamicStoreCopyComputerName(_: SCDynamicStore?, _: UnsafeMutablePointer<CFStringEncoding>) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517208-scdynamicstorecopycomputername)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore!, _ nameEncoding: UnsafeMutablePointer<CFStringEncoding>) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore?, _ nameEncoding: UnsafeMutablePointer<CFStringEncoding>) -> CFString? ``` |

Modified [SCDynamicStoreCopyConsoleUser(_: SCDynamicStore?, _: UnsafeMutablePointer<uid_t>, _: UnsafeMutablePointer<gid_t>) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517123-scdynamicstorecopyconsoleuser)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore!, _ uid: UnsafeMutablePointer<uid_t>, _ gid: UnsafeMutablePointer<gid_t>) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore?, _ uid: UnsafeMutablePointer<uid_t>, _ gid: UnsafeMutablePointer<gid_t>) -> CFString? ``` |

Modified [SCDynamicStoreCopyKeyList(_: SCDynamicStore?, _: CFString) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1437799-scdynamicstorecopykeylist)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyKeyList(_ store: SCDynamicStore!, _ pattern: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCDynamicStoreCopyKeyList(_ store: SCDynamicStore?, _ pattern: CFString) -> CFArray? ``` |

Modified [SCDynamicStoreCopyLocalHostName(_: SCDynamicStore?) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517066-scdynamicstorecopylocalhostname)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyLocalHostName(_ store: SCDynamicStore!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreCopyLocalHostName(_ store: SCDynamicStore?) -> CFString? ``` |

Modified [SCDynamicStoreCopyLocation(_: SCDynamicStore?) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517216-scdynamicstorecopylocation)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyLocation(_ store: SCDynamicStore!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreCopyLocation(_ store: SCDynamicStore?) -> CFString? ``` |

Modified [SCDynamicStoreCopyMultiple(_: SCDynamicStore?, _: CFArray?, _: CFArray?) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1437809-scdynamicstorecopymultiple)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyMultiple(_ store: SCDynamicStore!, _ keys: CFArray!, _ patterns: CFArray!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCDynamicStoreCopyMultiple(_ store: SCDynamicStore?, _ keys: CFArray?, _ patterns: CFArray?) -> CFDictionary? ``` |

Modified [SCDynamicStoreCopyNotifiedKeys(_: SCDynamicStore) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1437805-scdynamicstorecopynotifiedkeys)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyNotifiedKeys(_ store: SCDynamicStore!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCDynamicStoreCopyNotifiedKeys(_ store: SCDynamicStore) -> CFArray? ``` |

Modified [SCDynamicStoreCopyProxies(_: SCDynamicStore?) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1517088-scdynamicstorecopyproxies)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyProxies(_ store: SCDynamicStore!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCDynamicStoreCopyProxies(_ store: SCDynamicStore?) -> CFDictionary? ``` |

Modified [SCDynamicStoreCopyValue(_: SCDynamicStore?, _: CFString) -> CFPropertyList?](https://developer.apple.com/documentation/systemconfiguration/1437812-scdynamicstorecopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCopyValue(_ store: SCDynamicStore!, _ key: CFString!) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func SCDynamicStoreCopyValue(_ store: SCDynamicStore?, _ key: CFString) -> CFPropertyList? ``` |

Modified [SCDynamicStoreCreate(_: CFAllocator?, _: CFString, _: SCDynamicStoreCallBack?, _: UnsafeMutablePointer<SCDynamicStoreContext>) -> SCDynamicStore?](https://developer.apple.com/documentation/systemconfiguration/1437828-scdynamicstorecreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCreate(_ allocator: CFAllocator!, _ name: CFString!, _ callout: SCDynamicStoreCallBack, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>! ``` |
| To | ``` func SCDynamicStoreCreate(_ allocator: CFAllocator?, _ name: CFString, _ callout: SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> SCDynamicStore? ``` |

Modified [SCDynamicStoreCreateRunLoopSource(_: CFAllocator?, _: SCDynamicStore, _: CFIndex) -> CFRunLoopSource?](https://developer.apple.com/documentation/systemconfiguration/1437797-scdynamicstorecreaterunloopsourc)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCreateRunLoopSource(_ allocator: CFAllocator!, _ store: SCDynamicStore!, _ order: CFIndex) -> Unmanaged<CFRunLoopSource>! ``` |
| To | ``` func SCDynamicStoreCreateRunLoopSource(_ allocator: CFAllocator?, _ store: SCDynamicStore, _ order: CFIndex) -> CFRunLoopSource? ``` |

Modified [SCDynamicStoreCreateWithOptions(_: CFAllocator?, _: CFString, _: CFDictionary?, _: SCDynamicStoreCallBack?, _: UnsafeMutablePointer<SCDynamicStoreContext>) -> SCDynamicStore?](https://developer.apple.com/documentation/systemconfiguration/1437818-scdynamicstorecreatewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreCreateWithOptions(_ allocator: CFAllocator!, _ name: CFString!, _ storeOptions: CFDictionary!, _ callout: SCDynamicStoreCallBack, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>! ``` |
| To | ``` func SCDynamicStoreCreateWithOptions(_ allocator: CFAllocator?, _ name: CFString, _ storeOptions: CFDictionary?, _ callout: SCDynamicStoreCallBack?, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> SCDynamicStore? ``` |

Modified [SCDynamicStoreKeyCreateComputerName(_: CFAllocator?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1517319-scdynamicstorekeycreatecomputern)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateComputerName(_ allocator: CFAllocator!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateComputerName(_ allocator: CFAllocator?) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateConsoleUser(_: CFAllocator?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1517286-scdynamicstorekeycreateconsoleus)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateConsoleUser(_ allocator: CFAllocator!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateConsoleUser(_ allocator: CFAllocator?) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateHostNames(_: CFAllocator?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1517184-scdynamicstorekeycreatehostnames)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateHostNames(_ allocator: CFAllocator!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateHostNames(_ allocator: CFAllocator?) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateLocation(_: CFAllocator?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1516900-scdynamicstorekeycreatelocation)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateLocation(_ allocator: CFAllocator!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateLocation(_ allocator: CFAllocator?) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateNetworkGlobalEntity(_: CFAllocator?, _: CFString, _: CFString) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1516684-scdynamicstorekeycreatenetworkgl)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateNetworkGlobalEntity(_ allocator: CFAllocator!, _ domain: CFString!, _ entity: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateNetworkGlobalEntity(_ allocator: CFAllocator?, _ domain: CFString, _ entity: CFString) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateNetworkInterface(_: CFAllocator?, _: CFString) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1517022-scdynamicstorekeycreatenetworkin)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateNetworkInterface(_ allocator: CFAllocator!, _ domain: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateNetworkInterface(_ allocator: CFAllocator?, _ domain: CFString) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateNetworkInterfaceEntity(_: CFAllocator?, _: CFString, _: CFString, _: CFString?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1517099-scdynamicstorekeycreatenetworkin)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateNetworkInterfaceEntity(_ allocator: CFAllocator!, _ domain: CFString!, _ ifname: CFString!, _ entity: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateNetworkInterfaceEntity(_ allocator: CFAllocator?, _ domain: CFString, _ ifname: CFString, _ entity: CFString?) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateNetworkServiceEntity(_: CFAllocator?, _: CFString, _: CFString, _: CFString?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1517288-scdynamicstorekeycreatenetworkse)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateNetworkServiceEntity(_ allocator: CFAllocator!, _ domain: CFString!, _ serviceID: CFString!, _ entity: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateNetworkServiceEntity(_ allocator: CFAllocator?, _ domain: CFString, _ serviceID: CFString, _ entity: CFString?) -> CFString ``` |

Modified [SCDynamicStoreKeyCreateProxies(_: CFAllocator?) -> CFString](https://developer.apple.com/documentation/systemconfiguration/1516870-scdynamicstorekeycreateproxies)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreKeyCreateProxies(_ allocator: CFAllocator!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCDynamicStoreKeyCreateProxies(_ allocator: CFAllocator?) -> CFString ``` |

Modified [SCDynamicStoreNotifyValue(_: SCDynamicStore?, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437793-scdynamicstorenotifyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreNotifyValue(_ store: SCDynamicStore!, _ key: CFString!) -> Boolean ``` |
| To | ``` func SCDynamicStoreNotifyValue(_ store: SCDynamicStore?, _ key: CFString) -> Bool ``` |

Modified [SCDynamicStoreRemoveValue(_: SCDynamicStore?, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437783-scdynamicstoreremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreRemoveValue(_ store: SCDynamicStore!, _ key: CFString!) -> Boolean ``` |
| To | ``` func SCDynamicStoreRemoveValue(_ store: SCDynamicStore?, _ key: CFString) -> Bool ``` |

Modified [SCDynamicStoreSetDispatchQueue(_: SCDynamicStore, _: dispatch_queue_t?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437816-scdynamicstoresetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreSetDispatchQueue(_ store: SCDynamicStore!, _ queue: dispatch_queue_t!) -> Boolean ``` |
| To | ``` func SCDynamicStoreSetDispatchQueue(_ store: SCDynamicStore, _ queue: dispatch_queue_t?) -> Bool ``` |

Modified [SCDynamicStoreSetMultiple(_: SCDynamicStore?, _: CFDictionary?, _: CFArray?, _: CFArray?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437824-scdynamicstoresetmultiple)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreSetMultiple(_ store: SCDynamicStore!, _ keysToSet: CFDictionary!, _ keysToRemove: CFArray!, _ keysToNotify: CFArray!) -> Boolean ``` |
| To | ``` func SCDynamicStoreSetMultiple(_ store: SCDynamicStore?, _ keysToSet: CFDictionary?, _ keysToRemove: CFArray?, _ keysToNotify: CFArray?) -> Bool ``` |

Modified [SCDynamicStoreSetNotificationKeys(_: SCDynamicStore, _: CFArray?, _: CFArray?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437820-scdynamicstoresetnotificationkey)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreSetNotificationKeys(_ store: SCDynamicStore!, _ keys: CFArray!, _ patterns: CFArray!) -> Boolean ``` |
| To | ``` func SCDynamicStoreSetNotificationKeys(_ store: SCDynamicStore, _ keys: CFArray?, _ patterns: CFArray?) -> Bool ``` |

Modified [SCDynamicStoreSetValue(_: SCDynamicStore?, _: CFString, _: CFPropertyList) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1437814-scdynamicstoresetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCDynamicStoreSetValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` |
| To | ``` func SCDynamicStoreSetValue(_ store: SCDynamicStore?, _ key: CFString, _ value: CFPropertyList) -> Bool ``` |

Modified [SCNetworkConnectionCallBack](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkConnectionCallBack = CFunctionPointer<((SCNetworkConnection!, SCNetworkConnectionStatus, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCNetworkConnectionCallBack = (SCNetworkConnection, SCNetworkConnectionStatus, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [SCNetworkConnectionCopyExtendedStatus(_: SCNetworkConnection) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1393134-scnetworkconnectioncopyextendeds)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCopyExtendedStatus(_ connection: SCNetworkConnection!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCNetworkConnectionCopyExtendedStatus(_ connection: SCNetworkConnection) -> CFDictionary? ``` |

Modified [SCNetworkConnectionCopyServiceID(_: SCNetworkConnection) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1393167-scnetworkconnectioncopyserviceid)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCopyServiceID(_ connection: SCNetworkConnection!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkConnectionCopyServiceID(_ connection: SCNetworkConnection) -> CFString? ``` |

Modified [SCNetworkConnectionCopyStatistics(_: SCNetworkConnection) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1393147-scnetworkconnectioncopystatistic)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCopyStatistics(_ connection: SCNetworkConnection!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCNetworkConnectionCopyStatistics(_ connection: SCNetworkConnection) -> CFDictionary? ``` |

Modified [SCNetworkConnectionCopyUserOptions(_: SCNetworkConnection) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1393128-scnetworkconnectioncopyuseroptio)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCopyUserOptions(_ connection: SCNetworkConnection!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCNetworkConnectionCopyUserOptions(_ connection: SCNetworkConnection) -> CFDictionary? ``` |

Modified [SCNetworkConnectionCopyUserPreferences(_: CFDictionary?, _: UnsafeMutablePointer<Unmanaged<CFString>?>, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393114-scnetworkconnectioncopyuserprefe)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary!, _ serviceID: UnsafeMutablePointer<Unmanaged<CFString>?>, _ userOptions: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Boolean ``` |
| To | ``` func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary?, _ serviceID: UnsafeMutablePointer<Unmanaged<CFString>?>, _ userOptions: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool ``` |

Modified [SCNetworkConnectionCreateWithServiceID(_: CFAllocator?, _: CFString, _: SCNetworkConnectionCallBack?, _: UnsafeMutablePointer<SCNetworkConnectionContext>) -> SCNetworkConnection?](https://developer.apple.com/documentation/systemconfiguration/1393175-scnetworkconnectioncreatewithser)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator!, _ serviceID: CFString!, _ callout: SCNetworkConnectionCallBack, _ context: UnsafeMutablePointer<SCNetworkConnectionContext>) -> Unmanaged<SCNetworkConnection>! ``` |
| To | ``` func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator?, _ serviceID: CFString, _ callout: SCNetworkConnectionCallBack?, _ context: UnsafeMutablePointer<SCNetworkConnectionContext>) -> SCNetworkConnection? ``` |

Modified [SCNetworkConnectionGetStatus(_: SCNetworkConnection) -> SCNetworkConnectionStatus](https://developer.apple.com/documentation/systemconfiguration/1393096-scnetworkconnectiongetstatus)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionGetStatus(_ connection: SCNetworkConnection!) -> SCNetworkConnectionStatus ``` |
| To | ``` func SCNetworkConnectionGetStatus(_ connection: SCNetworkConnection) -> SCNetworkConnectionStatus ``` |

Modified [SCNetworkConnectionScheduleWithRunLoop(_: SCNetworkConnection, _: CFRunLoop, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393120-scnetworkconnectionschedulewithr)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionScheduleWithRunLoop(_ connection: SCNetworkConnection!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkConnectionScheduleWithRunLoop(_ connection: SCNetworkConnection, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool ``` |

Modified [SCNetworkConnectionSetDispatchQueue(_: SCNetworkConnection, _: dispatch_queue_t?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393138-scnetworkconnectionsetdispatchqu)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionSetDispatchQueue(_ connection: SCNetworkConnection!, _ queue: dispatch_queue_t!) -> Boolean ``` |
| To | ``` func SCNetworkConnectionSetDispatchQueue(_ connection: SCNetworkConnection, _ queue: dispatch_queue_t?) -> Bool ``` |

Modified [SCNetworkConnectionStart(_: SCNetworkConnection, _: CFDictionary?, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393183-scnetworkconnectionstart)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionStart(_ connection: SCNetworkConnection!, _ userOptions: CFDictionary!, _ linger: Boolean) -> Boolean ``` |
| To | ``` func SCNetworkConnectionStart(_ connection: SCNetworkConnection, _ userOptions: CFDictionary?, _ linger: Bool) -> Bool ``` |

Modified [SCNetworkConnectionStop(_: SCNetworkConnection, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393169-scnetworkconnectionstop)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionStop(_ connection: SCNetworkConnection!, _ forceDisconnect: Boolean) -> Boolean ``` |
| To | ``` func SCNetworkConnectionStop(_ connection: SCNetworkConnection, _ forceDisconnect: Bool) -> Bool ``` |

Modified [SCNetworkConnectionUnscheduleFromRunLoop(_: SCNetworkConnection, _: CFRunLoop, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1393151-scnetworkconnectionunschedulefro)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkConnectionUnscheduleFromRunLoop(_ connection: SCNetworkConnection!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkConnectionUnscheduleFromRunLoop(_ connection: SCNetworkConnection, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool ``` |

Modified [SCNetworkInterfaceCopyAll() -> CFArray](https://developer.apple.com/documentation/systemconfiguration/1517090-scnetworkinterfacecopyall)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyAll() -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkInterfaceCopyAll() -> CFArray ``` |

Modified [SCNetworkInterfaceCopyMediaOptions(_: SCNetworkInterface, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _: UnsafeMutablePointer<Unmanaged<CFArray>?>, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516738-scnetworkinterfacecopymediaoptio)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface!, _ current: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ active: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ available: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ filter: Boolean) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface, _ current: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ active: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ available: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ filter: Bool) -> Bool ``` |

Modified [SCNetworkInterfaceCopyMediaSubTypeOptions(_: CFArray, _: CFString) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1516695-scnetworkinterfacecopymediasubty)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyMediaSubTypeOptions(_ available: CFArray!, _ subType: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkInterfaceCopyMediaSubTypeOptions(_ available: CFArray, _ subType: CFString) -> CFArray? ``` |

Modified [SCNetworkInterfaceCopyMediaSubTypes(_: CFArray) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1516927-scnetworkinterfacecopymediasubty)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyMediaSubTypes(_ available: CFArray!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkInterfaceCopyMediaSubTypes(_ available: CFArray) -> CFArray? ``` |

Modified [SCNetworkInterfaceCopyMTU(_: SCNetworkInterface, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<Int32>, _: UnsafeMutablePointer<Int32>) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517279-scnetworkinterfacecopymtu)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface!, _ mtu_cur: UnsafeMutablePointer<Int32>, _ mtu_min: UnsafeMutablePointer<Int32>, _ mtu_max: UnsafeMutablePointer<Int32>) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface, _ mtu_cur: UnsafeMutablePointer<Int32>, _ mtu_min: UnsafeMutablePointer<Int32>, _ mtu_max: UnsafeMutablePointer<Int32>) -> Bool ``` |

Modified [SCNetworkInterfaceCreateWithInterface(_: SCNetworkInterface, _: CFString) -> SCNetworkInterface?](https://developer.apple.com/documentation/systemconfiguration/1516824-scnetworkinterfacecreatewithinte)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceCreateWithInterface(_ interface: SCNetworkInterface!, _ interfaceType: CFString!) -> Unmanaged<SCNetworkInterface>! ``` |
| To | ``` func SCNetworkInterfaceCreateWithInterface(_ interface: SCNetworkInterface, _ interfaceType: CFString) -> SCNetworkInterface? ``` |

Modified [SCNetworkInterfaceForceConfigurationRefresh(_: SCNetworkInterface) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516815-scnetworkinterfaceforceconfigura)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceForceConfigurationRefresh(_ interface: SCNetworkInterface!) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceForceConfigurationRefresh(_ interface: SCNetworkInterface) -> Bool ``` |

Modified [SCNetworkInterfaceGetBSDName(_: SCNetworkInterface) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516854-scnetworkinterfacegetbsdname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetBSDName(_ interface: SCNetworkInterface!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkInterfaceGetBSDName(_ interface: SCNetworkInterface) -> CFString? ``` |

Modified [SCNetworkInterfaceGetConfiguration(_: SCNetworkInterface) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1516867-scnetworkinterfacegetconfigurati)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetConfiguration(_ interface: SCNetworkInterface!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCNetworkInterfaceGetConfiguration(_ interface: SCNetworkInterface) -> CFDictionary? ``` |

Modified [SCNetworkInterfaceGetExtendedConfiguration(_: SCNetworkInterface, _: CFString) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1517315-scnetworkinterfacegetextendedcon)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetExtendedConfiguration(_ interface: SCNetworkInterface!, _ extendedType: CFString!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCNetworkInterfaceGetExtendedConfiguration(_ interface: SCNetworkInterface, _ extendedType: CFString) -> CFDictionary? ``` |

Modified [SCNetworkInterfaceGetHardwareAddressString(_: SCNetworkInterface) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516925-scnetworkinterfacegethardwareadd)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetHardwareAddressString(_ interface: SCNetworkInterface!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkInterfaceGetHardwareAddressString(_ interface: SCNetworkInterface) -> CFString? ``` |

Modified [SCNetworkInterfaceGetInterface(_: SCNetworkInterface) -> SCNetworkInterface?](https://developer.apple.com/documentation/systemconfiguration/1517296-scnetworkinterfacegetinterface)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetInterface(_ interface: SCNetworkInterface!) -> Unmanaged<SCNetworkInterface>! ``` |
| To | ``` func SCNetworkInterfaceGetInterface(_ interface: SCNetworkInterface) -> SCNetworkInterface? ``` |

Modified [SCNetworkInterfaceGetInterfaceType(_: SCNetworkInterface) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517371-scnetworkinterfacegetinterfacety)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetInterfaceType(_ interface: SCNetworkInterface!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkInterfaceGetInterfaceType(_ interface: SCNetworkInterface) -> CFString? ``` |

Modified [SCNetworkInterfaceGetLocalizedDisplayName(_: SCNetworkInterface) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517060-scnetworkinterfacegetlocalizeddi)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetLocalizedDisplayName(_ interface: SCNetworkInterface!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkInterfaceGetLocalizedDisplayName(_ interface: SCNetworkInterface) -> CFString? ``` |

Modified [SCNetworkInterfaceGetSupportedInterfaceTypes(_: SCNetworkInterface) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1517339-scnetworkinterfacegetsupportedin)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetSupportedInterfaceTypes(_ interface: SCNetworkInterface!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkInterfaceGetSupportedInterfaceTypes(_ interface: SCNetworkInterface) -> CFArray? ``` |

Modified [SCNetworkInterfaceGetSupportedProtocolTypes(_: SCNetworkInterface) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1516844-scnetworkinterfacegetsupportedpr)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceGetSupportedProtocolTypes(_ interface: SCNetworkInterface!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkInterfaceGetSupportedProtocolTypes(_ interface: SCNetworkInterface) -> CFArray? ``` |

Modified [SCNetworkInterfaceSetConfiguration(_: SCNetworkInterface, _: CFDictionary) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517082-scnetworkinterfacesetconfigurati)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceSetConfiguration(_ interface: SCNetworkInterface!, _ config: CFDictionary!) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceSetConfiguration(_ interface: SCNetworkInterface, _ config: CFDictionary) -> Bool ``` |

Modified [SCNetworkInterfaceSetExtendedConfiguration(_: SCNetworkInterface, _: CFString, _: CFDictionary) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517295-scnetworkinterfacesetextendedcon)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceSetExtendedConfiguration(_ interface: SCNetworkInterface!, _ extendedType: CFString!, _ config: CFDictionary!) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceSetExtendedConfiguration(_ interface: SCNetworkInterface, _ extendedType: CFString, _ config: CFDictionary) -> Bool ``` |

Modified [SCNetworkInterfaceSetMediaOptions(_: SCNetworkInterface, _: CFString, _: CFArray) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516832-scnetworkinterfacesetmediaoption)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceSetMediaOptions(_ interface: SCNetworkInterface!, _ subtype: CFString!, _ options: CFArray!) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceSetMediaOptions(_ interface: SCNetworkInterface, _ subtype: CFString, _ options: CFArray) -> Bool ``` |

Modified [SCNetworkInterfaceSetMTU(_: SCNetworkInterface, _: Int32) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517131-scnetworkinterfacesetmtu)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkInterfaceSetMTU(_ interface: SCNetworkInterface!, _ mtu: Int32) -> Boolean ``` |
| To | ``` func SCNetworkInterfaceSetMTU(_ interface: SCNetworkInterface, _ mtu: Int32) -> Bool ``` |

Modified [SCNetworkProtocolGetConfiguration(_: SCNetworkProtocol) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1517352-scnetworkprotocolgetconfiguratio)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkProtocolGetConfiguration(_ `protocol`: SCNetworkProtocol!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCNetworkProtocolGetConfiguration(_ `protocol`: SCNetworkProtocol) -> CFDictionary? ``` |

Modified [SCNetworkProtocolGetEnabled(_: SCNetworkProtocol) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517299-scnetworkprotocolgetenabled)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkProtocolGetEnabled(_ `protocol`: SCNetworkProtocol!) -> Boolean ``` |
| To | ``` func SCNetworkProtocolGetEnabled(_ `protocol`: SCNetworkProtocol) -> Bool ``` |

Modified [SCNetworkProtocolGetProtocolType(_: SCNetworkProtocol) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1517302-scnetworkprotocolgetprotocoltype)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkProtocolGetProtocolType(_ `protocol`: SCNetworkProtocol!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkProtocolGetProtocolType(_ `protocol`: SCNetworkProtocol) -> CFString? ``` |

Modified [SCNetworkProtocolSetConfiguration(_: SCNetworkProtocol, _: CFDictionary) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517188-scnetworkprotocolsetconfiguratio)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkProtocolSetConfiguration(_ `protocol`: SCNetworkProtocol!, _ config: CFDictionary!) -> Boolean ``` |
| To | ``` func SCNetworkProtocolSetConfiguration(_ `protocol`: SCNetworkProtocol, _ config: CFDictionary) -> Bool ``` |

Modified [SCNetworkProtocolSetEnabled(_: SCNetworkProtocol, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517366-scnetworkprotocolsetenabled)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkProtocolSetEnabled(_ `protocol`: SCNetworkProtocol!, _ enabled: Boolean) -> Boolean ``` |
| To | ``` func SCNetworkProtocolSetEnabled(_ `protocol`: SCNetworkProtocol, _ enabled: Bool) -> Bool ``` |

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

Modified [SCNetworkServiceAddProtocolType(_: SCNetworkService, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516894-scnetworkserviceaddprotocoltype)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceAddProtocolType(_ service: SCNetworkService!, _ protocolType: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkServiceAddProtocolType(_ service: SCNetworkService, _ protocolType: CFString) -> Bool ``` |

Modified [SCNetworkServiceCopy(_: SCPreferences, _: CFString) -> SCNetworkService?](https://developer.apple.com/documentation/systemconfiguration/1516864-scnetworkservicecopy)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceCopy(_ prefs: SCPreferences!, _ serviceID: CFString!) -> Unmanaged<SCNetworkService>! ``` |
| To | ``` func SCNetworkServiceCopy(_ prefs: SCPreferences, _ serviceID: CFString) -> SCNetworkService? ``` |

Modified [SCNetworkServiceCopyAll(_: SCPreferences) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1516810-scnetworkservicecopyall)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceCopyAll(_ prefs: SCPreferences!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkServiceCopyAll(_ prefs: SCPreferences) -> CFArray? ``` |

Modified [SCNetworkServiceCopyProtocol(_: SCNetworkService, _: CFString) -> SCNetworkProtocol?](https://developer.apple.com/documentation/systemconfiguration/1517290-scnetworkservicecopyprotocol)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceCopyProtocol(_ service: SCNetworkService!, _ protocolType: CFString!) -> Unmanaged<SCNetworkProtocol>! ``` |
| To | ``` func SCNetworkServiceCopyProtocol(_ service: SCNetworkService, _ protocolType: CFString) -> SCNetworkProtocol? ``` |

Modified [SCNetworkServiceCopyProtocols(_: SCNetworkService) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1517200-scnetworkservicecopyprotocols)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceCopyProtocols(_ service: SCNetworkService!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkServiceCopyProtocols(_ service: SCNetworkService) -> CFArray? ``` |

Modified [SCNetworkServiceCreate(_: SCPreferences, _: SCNetworkInterface) -> SCNetworkService?](https://developer.apple.com/documentation/systemconfiguration/1517139-scnetworkservicecreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceCreate(_ prefs: SCPreferences!, _ interface: SCNetworkInterface!) -> Unmanaged<SCNetworkService>! ``` |
| To | ``` func SCNetworkServiceCreate(_ prefs: SCPreferences, _ interface: SCNetworkInterface) -> SCNetworkService? ``` |

Modified [SCNetworkServiceEstablishDefaultConfiguration(_: SCNetworkService) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517016-scnetworkserviceestablishdefault)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceEstablishDefaultConfiguration(_ service: SCNetworkService!) -> Boolean ``` |
| To | ``` func SCNetworkServiceEstablishDefaultConfiguration(_ service: SCNetworkService) -> Bool ``` |

Modified [SCNetworkServiceGetEnabled(_: SCNetworkService) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517075-scnetworkservicegetenabled)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceGetEnabled(_ service: SCNetworkService!) -> Boolean ``` |
| To | ``` func SCNetworkServiceGetEnabled(_ service: SCNetworkService) -> Bool ``` |

Modified [SCNetworkServiceGetInterface(_: SCNetworkService) -> SCNetworkInterface?](https://developer.apple.com/documentation/systemconfiguration/1516724-scnetworkservicegetinterface)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceGetInterface(_ service: SCNetworkService!) -> Unmanaged<SCNetworkInterface>! ``` |
| To | ``` func SCNetworkServiceGetInterface(_ service: SCNetworkService) -> SCNetworkInterface? ``` |

Modified [SCNetworkServiceGetName(_: SCNetworkService) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516819-scnetworkservicegetname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceGetName(_ service: SCNetworkService!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkServiceGetName(_ service: SCNetworkService) -> CFString? ``` |

Modified [SCNetworkServiceGetServiceID(_: SCNetworkService) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516965-scnetworkservicegetserviceid)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceGetServiceID(_ service: SCNetworkService!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkServiceGetServiceID(_ service: SCNetworkService) -> CFString? ``` |

Modified [SCNetworkServiceRemove(_: SCNetworkService) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517177-scnetworkserviceremove)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceRemove(_ service: SCNetworkService!) -> Boolean ``` |
| To | ``` func SCNetworkServiceRemove(_ service: SCNetworkService) -> Bool ``` |

Modified [SCNetworkServiceRemoveProtocolType(_: SCNetworkService, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517073-scnetworkserviceremoveprotocolty)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceRemoveProtocolType(_ service: SCNetworkService!, _ protocolType: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkServiceRemoveProtocolType(_ service: SCNetworkService, _ protocolType: CFString) -> Bool ``` |

Modified [SCNetworkServiceSetEnabled(_: SCNetworkService, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517240-scnetworkservicesetenabled)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceSetEnabled(_ service: SCNetworkService!, _ enabled: Boolean) -> Boolean ``` |
| To | ``` func SCNetworkServiceSetEnabled(_ service: SCNetworkService, _ enabled: Bool) -> Bool ``` |

Modified [SCNetworkServiceSetName(_: SCNetworkService, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516988-scnetworkservicesetname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkServiceSetName(_ service: SCNetworkService!, _ name: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkServiceSetName(_ service: SCNetworkService, _ name: CFString) -> Bool ``` |

Modified [SCNetworkSetAddService(_: SCNetworkSet, _: SCNetworkService) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516707-scnetworksetaddservice)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetAddService(_ set: SCNetworkSet!, _ service: SCNetworkService!) -> Boolean ``` |
| To | ``` func SCNetworkSetAddService(_ set: SCNetworkSet, _ service: SCNetworkService) -> Bool ``` |

Modified [SCNetworkSetContainsInterface(_: SCNetworkSet, _: SCNetworkInterface) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516672-scnetworksetcontainsinterface)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetContainsInterface(_ set: SCNetworkSet!, _ interface: SCNetworkInterface!) -> Boolean ``` |
| To | ``` func SCNetworkSetContainsInterface(_ set: SCNetworkSet, _ interface: SCNetworkInterface) -> Bool ``` |

Modified [SCNetworkSetCopy(_: SCPreferences, _: CFString) -> SCNetworkSet?](https://developer.apple.com/documentation/systemconfiguration/1517107-scnetworksetcopy)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetCopy(_ prefs: SCPreferences!, _ setID: CFString!) -> Unmanaged<SCNetworkSet>! ``` |
| To | ``` func SCNetworkSetCopy(_ prefs: SCPreferences, _ setID: CFString) -> SCNetworkSet? ``` |

Modified [SCNetworkSetCopyAll(_: SCPreferences) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1517220-scnetworksetcopyall)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetCopyAll(_ prefs: SCPreferences!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkSetCopyAll(_ prefs: SCPreferences) -> CFArray? ``` |

Modified [SCNetworkSetCopyCurrent(_: SCPreferences) -> SCNetworkSet?](https://developer.apple.com/documentation/systemconfiguration/1517183-scnetworksetcopycurrent)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetCopyCurrent(_ prefs: SCPreferences!) -> Unmanaged<SCNetworkSet>! ``` |
| To | ``` func SCNetworkSetCopyCurrent(_ prefs: SCPreferences) -> SCNetworkSet? ``` |

Modified [SCNetworkSetCopyServices(_: SCNetworkSet) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1517085-scnetworksetcopyservices)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetCopyServices(_ set: SCNetworkSet!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkSetCopyServices(_ set: SCNetworkSet) -> CFArray? ``` |

Modified [SCNetworkSetCreate(_: SCPreferences) -> SCNetworkSet?](https://developer.apple.com/documentation/systemconfiguration/1517084-scnetworksetcreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetCreate(_ prefs: SCPreferences!) -> Unmanaged<SCNetworkSet>! ``` |
| To | ``` func SCNetworkSetCreate(_ prefs: SCPreferences) -> SCNetworkSet? ``` |

Modified [SCNetworkSetGetName(_: SCNetworkSet) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516847-scnetworksetgetname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetGetName(_ set: SCNetworkSet!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkSetGetName(_ set: SCNetworkSet) -> CFString? ``` |

Modified [SCNetworkSetGetServiceOrder(_: SCNetworkSet) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1516892-scnetworksetgetserviceorder)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetGetServiceOrder(_ set: SCNetworkSet!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCNetworkSetGetServiceOrder(_ set: SCNetworkSet) -> CFArray? ``` |

Modified [SCNetworkSetGetSetID(_: SCNetworkSet) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516940-scnetworksetgetsetid)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetGetSetID(_ set: SCNetworkSet!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCNetworkSetGetSetID(_ set: SCNetworkSet) -> CFString? ``` |

Modified [SCNetworkSetRemove(_: SCNetworkSet) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517202-scnetworksetremove)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetRemove(_ set: SCNetworkSet!) -> Boolean ``` |
| To | ``` func SCNetworkSetRemove(_ set: SCNetworkSet) -> Bool ``` |

Modified [SCNetworkSetRemoveService(_: SCNetworkSet, _: SCNetworkService) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517325-scnetworksetremoveservice)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetRemoveService(_ set: SCNetworkSet!, _ service: SCNetworkService!) -> Boolean ``` |
| To | ``` func SCNetworkSetRemoveService(_ set: SCNetworkSet, _ service: SCNetworkService) -> Bool ``` |

Modified [SCNetworkSetSetCurrent(_: SCNetworkSet) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516959-scnetworksetsetcurrent)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetSetCurrent(_ set: SCNetworkSet!) -> Boolean ``` |
| To | ``` func SCNetworkSetSetCurrent(_ set: SCNetworkSet) -> Bool ``` |

Modified [SCNetworkSetSetName(_: SCNetworkSet, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517309-scnetworksetsetname)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetSetName(_ set: SCNetworkSet!, _ name: CFString!) -> Boolean ``` |
| To | ``` func SCNetworkSetSetName(_ set: SCNetworkSet, _ name: CFString) -> Bool ``` |

Modified [SCNetworkSetSetServiceOrder(_: SCNetworkSet, _: CFArray) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516839-scnetworksetsetserviceorder)

|  | Declaration |
| --- | --- |
| From | ``` func SCNetworkSetSetServiceOrder(_ set: SCNetworkSet!, _ newOrder: CFArray!) -> Boolean ``` |
| To | ``` func SCNetworkSetSetServiceOrder(_ set: SCNetworkSet, _ newOrder: CFArray) -> Bool ``` |

Modified [SCPreferencesAddValue(_: SCPreferences, _: CFString, _: CFPropertyList) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517178-scpreferencesaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesAddValue(_ prefs: SCPreferences!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` |
| To | ``` func SCPreferencesAddValue(_ prefs: SCPreferences, _ key: CFString, _ value: CFPropertyList) -> Bool ``` |

Modified [SCPreferencesApplyChanges(_: SCPreferences) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517125-scpreferencesapplychanges)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesApplyChanges(_ prefs: SCPreferences!) -> Boolean ``` |
| To | ``` func SCPreferencesApplyChanges(_ prefs: SCPreferences) -> Bool ``` |

Modified [SCPreferencesCallBack](https://developer.apple.com/documentation/systemconfiguration/scpreferencescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias SCPreferencesCallBack = CFunctionPointer<((SCPreferences!, SCPreferencesNotification, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias SCPreferencesCallBack = (SCPreferences, SCPreferencesNotification, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [SCPreferencesCommitChanges(_: SCPreferences) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517333-scpreferencescommitchanges)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesCommitChanges(_ prefs: SCPreferences!) -> Boolean ``` |
| To | ``` func SCPreferencesCommitChanges(_ prefs: SCPreferences) -> Bool ``` |

Modified [SCPreferencesCopyKeyList(_: SCPreferences) -> CFArray?](https://developer.apple.com/documentation/systemconfiguration/1517058-scpreferencescopykeylist)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesCopyKeyList(_ prefs: SCPreferences!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCPreferencesCopyKeyList(_ prefs: SCPreferences) -> CFArray? ``` |

Modified [SCPreferencesCreate(_: CFAllocator?, _: CFString, _: CFString?) -> SCPreferences?](https://developer.apple.com/documentation/systemconfiguration/1516807-scpreferencescreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesCreate(_ allocator: CFAllocator!, _ name: CFString!, _ prefsID: CFString!) -> Unmanaged<SCPreferences>! ``` |
| To | ``` func SCPreferencesCreate(_ allocator: CFAllocator?, _ name: CFString, _ prefsID: CFString?) -> SCPreferences? ``` |

Modified [SCPreferencesCreateWithAuthorization(_: CFAllocator?, _: CFString, _: CFString?, _: AuthorizationRef) -> SCPreferences?](https://developer.apple.com/documentation/systemconfiguration/1516686-scpreferencescreatewithauthoriza)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator!, _ name: CFString!, _ prefsID: CFString!, _ authorization: AuthorizationRef) -> Unmanaged<SCPreferences>! ``` |
| To | ``` func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator?, _ name: CFString, _ prefsID: CFString?, _ authorization: AuthorizationRef) -> SCPreferences? ``` |

Modified [SCPreferencesGetSignature(_: SCPreferences) -> CFData?](https://developer.apple.com/documentation/systemconfiguration/1517004-scpreferencesgetsignature)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesGetSignature(_ prefs: SCPreferences!) -> Unmanaged<CFData>! ``` |
| To | ``` func SCPreferencesGetSignature(_ prefs: SCPreferences) -> CFData? ``` |

Modified [SCPreferencesGetValue(_: SCPreferences, _: CFString) -> CFPropertyList?](https://developer.apple.com/documentation/systemconfiguration/1517189-scpreferencesgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesGetValue(_ prefs: SCPreferences!, _ key: CFString!) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func SCPreferencesGetValue(_ prefs: SCPreferences, _ key: CFString) -> CFPropertyList? ``` |

Modified [SCPreferencesLock(_: SCPreferences, _: Bool) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517297-scpreferenceslock)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesLock(_ prefs: SCPreferences!, _ wait: Boolean) -> Boolean ``` |
| To | ``` func SCPreferencesLock(_ prefs: SCPreferences, _ wait: Bool) -> Bool ``` |

Modified [SCPreferencesPathCreateUniqueChild(_: SCPreferences, _: CFString) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516713-scpreferencespathcreateuniquechi)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesPathCreateUniqueChild(_ prefs: SCPreferences!, _ prefix: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCPreferencesPathCreateUniqueChild(_ prefs: SCPreferences, _ prefix: CFString) -> CFString? ``` |

Modified [SCPreferencesPathGetLink(_: SCPreferences, _: CFString) -> CFString?](https://developer.apple.com/documentation/systemconfiguration/1516712-scpreferencespathgetlink)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesPathGetLink(_ prefs: SCPreferences!, _ path: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func SCPreferencesPathGetLink(_ prefs: SCPreferences, _ path: CFString) -> CFString? ``` |

Modified [SCPreferencesPathGetValue(_: SCPreferences, _: CFString) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1516904-scpreferencespathgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesPathGetValue(_ prefs: SCPreferences!, _ path: CFString!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCPreferencesPathGetValue(_ prefs: SCPreferences, _ path: CFString) -> CFDictionary? ``` |

Modified [SCPreferencesPathRemoveValue(_: SCPreferences, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517268-scpreferencespathremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesPathRemoveValue(_ prefs: SCPreferences!, _ path: CFString!) -> Boolean ``` |
| To | ``` func SCPreferencesPathRemoveValue(_ prefs: SCPreferences, _ path: CFString) -> Bool ``` |

Modified [SCPreferencesPathSetLink(_: SCPreferences, _: CFString, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517244-scpreferencespathsetlink)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesPathSetLink(_ prefs: SCPreferences!, _ path: CFString!, _ link: CFString!) -> Boolean ``` |
| To | ``` func SCPreferencesPathSetLink(_ prefs: SCPreferences, _ path: CFString, _ link: CFString) -> Bool ``` |

Modified [SCPreferencesPathSetValue(_: SCPreferences, _: CFString, _: CFDictionary) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517271-scpreferencespathsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesPathSetValue(_ prefs: SCPreferences!, _ path: CFString!, _ value: CFDictionary!) -> Boolean ``` |
| To | ``` func SCPreferencesPathSetValue(_ prefs: SCPreferences, _ path: CFString, _ value: CFDictionary) -> Bool ``` |

Modified [SCPreferencesRemoveValue(_: SCPreferences, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516723-scpreferencesremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesRemoveValue(_ prefs: SCPreferences!, _ key: CFString!) -> Boolean ``` |
| To | ``` func SCPreferencesRemoveValue(_ prefs: SCPreferences, _ key: CFString) -> Bool ``` |

Modified [SCPreferencesScheduleWithRunLoop(_: SCPreferences, _: CFRunLoop, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516901-scpreferencesschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesScheduleWithRunLoop(_ prefs: SCPreferences!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func SCPreferencesScheduleWithRunLoop(_ prefs: SCPreferences, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool ``` |

Modified [SCPreferencesSetCallback(_: SCPreferences, _: SCPreferencesCallBack?, _: UnsafeMutablePointer<SCPreferencesContext>) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517094-scpreferencessetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetCallback(_ prefs: SCPreferences!, _ callout: SCPreferencesCallBack, _ context: UnsafeMutablePointer<SCPreferencesContext>) -> Boolean ``` |
| To | ``` func SCPreferencesSetCallback(_ prefs: SCPreferences, _ callout: SCPreferencesCallBack?, _ context: UnsafeMutablePointer<SCPreferencesContext>) -> Bool ``` |

Modified [SCPreferencesSetComputerName(_: SCPreferences, _: CFString, _: CFStringEncoding) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516772-scpreferencessetcomputername)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetComputerName(_ prefs: SCPreferences!, _ name: CFString!, _ nameEncoding: CFStringEncoding) -> Boolean ``` |
| To | ``` func SCPreferencesSetComputerName(_ prefs: SCPreferences, _ name: CFString, _ nameEncoding: CFStringEncoding) -> Bool ``` |

Modified [SCPreferencesSetDispatchQueue(_: SCPreferences, _: dispatch_queue_t?) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517050-scpreferencessetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetDispatchQueue(_ prefs: SCPreferences!, _ queue: dispatch_queue_t!) -> Boolean ``` |
| To | ``` func SCPreferencesSetDispatchQueue(_ prefs: SCPreferences, _ queue: dispatch_queue_t?) -> Bool ``` |

Modified [SCPreferencesSetLocalHostName(_: SCPreferences, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516945-scpreferencessetlocalhostname)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetLocalHostName(_ prefs: SCPreferences!, _ name: CFString!) -> Boolean ``` |
| To | ``` func SCPreferencesSetLocalHostName(_ prefs: SCPreferences, _ name: CFString) -> Bool ``` |

Modified [SCPreferencesSetValue(_: SCPreferences, _: CFString, _: CFPropertyList) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517225-scpreferencessetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSetValue(_ prefs: SCPreferences!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` |
| To | ``` func SCPreferencesSetValue(_ prefs: SCPreferences, _ key: CFString, _ value: CFPropertyList) -> Bool ``` |

Modified [SCPreferencesSynchronize(_: SCPreferences)](https://developer.apple.com/documentation/systemconfiguration/1517260-scpreferencessynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesSynchronize(_ prefs: SCPreferences!) ``` |
| To | ``` func SCPreferencesSynchronize(_ prefs: SCPreferences) ``` |

Modified [SCPreferencesUnlock(_: SCPreferences) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1517230-scpreferencesunlock)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesUnlock(_ prefs: SCPreferences!) -> Boolean ``` |
| To | ``` func SCPreferencesUnlock(_ prefs: SCPreferences) -> Bool ``` |

Modified [SCPreferencesUnscheduleFromRunLoop(_: SCPreferences, _: CFRunLoop, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516711-scpreferencesunschedulefromrunlo)

|  | Declaration |
| --- | --- |
| From | ``` func SCPreferencesUnscheduleFromRunLoop(_ prefs: SCPreferences!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) -> Boolean ``` |
| To | ``` func SCPreferencesUnscheduleFromRunLoop(_ prefs: SCPreferences, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool ``` |

Modified [SCVLANInterfaceCopyAll(_: SCPreferences) -> CFArray](https://developer.apple.com/documentation/systemconfiguration/1517029-scvlaninterfacecopyall)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceCopyAll(_ prefs: SCPreferences!) -> Unmanaged<CFArray>! ``` |
| To | ``` func SCVLANInterfaceCopyAll(_ prefs: SCPreferences) -> CFArray ``` |

Modified [SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> CFArray](https://developer.apple.com/documentation/systemconfiguration/1517211-scvlaninterfacecopyavailablephys)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> Unmanaged<CFArray>! ``` |
| To | ``` func SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> CFArray ``` |

Modified [SCVLANInterfaceCreate(_: SCPreferences, _: SCNetworkInterface, _: CFNumber) -> SCVLANInterface?](https://developer.apple.com/documentation/systemconfiguration/1517209-scvlaninterfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceCreate(_ prefs: SCPreferences!, _ physical: SCNetworkInterface!, _ tag: CFNumber!) -> Unmanaged<SCVLANInterface>! ``` |
| To | ``` func SCVLANInterfaceCreate(_ prefs: SCPreferences, _ physical: SCNetworkInterface, _ tag: CFNumber) -> SCVLANInterface? ``` |

Modified [SCVLANInterfaceGetOptions(_: SCVLANInterface) -> CFDictionary?](https://developer.apple.com/documentation/systemconfiguration/1516719-scvlaninterfacegetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceGetOptions(_ vlan: SCVLANInterface!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func SCVLANInterfaceGetOptions(_ vlan: SCVLANInterface) -> CFDictionary? ``` |

Modified [SCVLANInterfaceGetPhysicalInterface(_: SCVLANInterface) -> SCNetworkInterface?](https://developer.apple.com/documentation/systemconfiguration/1517233-scvlaninterfacegetphysicalinterf)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceGetPhysicalInterface(_ vlan: SCVLANInterface!) -> Unmanaged<SCNetworkInterface>! ``` |
| To | ``` func SCVLANInterfaceGetPhysicalInterface(_ vlan: SCVLANInterface) -> SCNetworkInterface? ``` |

Modified [SCVLANInterfaceGetTag(_: SCVLANInterface) -> CFNumber?](https://developer.apple.com/documentation/systemconfiguration/1517151-scvlaninterfacegettag)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceGetTag(_ vlan: SCVLANInterface!) -> Unmanaged<CFNumber>! ``` |
| To | ``` func SCVLANInterfaceGetTag(_ vlan: SCVLANInterface) -> CFNumber? ``` |

Modified [SCVLANInterfaceRemove(_: SCVLANInterface) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516889-scvlaninterfaceremove)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceRemove(_ vlan: SCVLANInterface!) -> Boolean ``` |
| To | ``` func SCVLANInterfaceRemove(_ vlan: SCVLANInterface) -> Bool ``` |

Modified [SCVLANInterfaceSetLocalizedDisplayName(_: SCVLANInterface, _: CFString) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516732-scvlaninterfacesetlocalizeddispl)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceSetLocalizedDisplayName(_ vlan: SCVLANInterface!, _ newName: CFString!) -> Boolean ``` |
| To | ``` func SCVLANInterfaceSetLocalizedDisplayName(_ vlan: SCVLANInterface, _ newName: CFString) -> Bool ``` |

Modified [SCVLANInterfaceSetOptions(_: SCVLANInterface, _: CFDictionary) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516852-scvlaninterfacesetoptions)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceSetOptions(_ vlan: SCVLANInterface!, _ newOptions: CFDictionary!) -> Boolean ``` |
| To | ``` func SCVLANInterfaceSetOptions(_ vlan: SCVLANInterface, _ newOptions: CFDictionary) -> Bool ``` |

Modified [SCVLANInterfaceSetPhysicalInterfaceAndTag(_: SCVLANInterface, _: SCNetworkInterface, _: CFNumber) -> Bool](https://developer.apple.com/documentation/systemconfiguration/1516754-scvlaninterfacesetphysicalinterf)

|  | Declaration |
| --- | --- |
| From | ``` func SCVLANInterfaceSetPhysicalInterfaceAndTag(_ vlan: SCVLANInterface!, _ physical: SCNetworkInterface!, _ tag: CFNumber!) -> Boolean ``` |
| To | ``` func SCVLANInterfaceSetPhysicalInterfaceAndTag(_ vlan: SCVLANInterface, _ physical: SCNetworkInterface, _ tag: CFNumber) -> Bool ``` |

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
