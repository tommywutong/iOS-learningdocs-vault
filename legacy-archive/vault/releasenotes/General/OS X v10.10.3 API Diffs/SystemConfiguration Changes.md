---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/SystemConfiguration.html
archived_at: '2026-07-18T02:52:42.273997Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# SystemConfiguration Changes

## SystemConfiguration

Added SCDynamicStoreContext.init()Added SCDynamicStoreContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added SCNetworkConnectionContext.init()Added SCNetworkConnectionContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added SCNetworkReachabilityContext.init()Added SCNetworkReachabilityContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added SCPreferencesContext.init()Added SCPreferencesContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>)Added kSCNetworkConnectionBytesInAdded kSCNetworkConnectionBytesOutAdded kSCNetworkConnectionErrorsInAdded kSCNetworkConnectionErrorsOutAdded kSCNetworkConnectionPacketsInAdded kSCNetworkConnectionPacketsOutAdded kSCNetworkConnectionSelectionOptionOnDemandHostNameAdded kSCNetworkConnectionSelectionOptionOnDemandRetryModified SCDynamicStoreContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCDynamicStoreContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCDynamicStoreContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified SCDynamicStoreContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified SCDynamicStoreContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified SCDynamicStoreContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified SCNetworkConnectionContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCNetworkConnectionContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCNetworkConnectionContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified SCNetworkConnectionContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified SCNetworkConnectionContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified SCNetworkConnectionContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified SCNetworkReachabilityContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCNetworkReachabilityContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCNetworkReachabilityContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified SCNetworkReachabilityContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified SCNetworkReachabilityContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified SCNetworkReachabilityContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified SCPreferencesContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)>     var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)>     var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> } ``` |
| To | ``` struct SCPreferencesContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>     var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>     var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)>, release release: CFunctionPointer<((UnsafePointer<Void>) -> Void)>, copyDescription copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)>) } ``` |

Modified SCPreferencesContext.copyDescription

|  | Declaration |
| --- | --- |
| From | ``` var copyDescription: CFunctionPointer<((ConstUnsafePointer<()>) -> Unmanaged<CFString>!)> ``` |
| To | ``` var copyDescription: CFunctionPointer<((UnsafePointer<Void>) -> Unmanaged<CFString>!)> ``` |

Modified SCPreferencesContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified SCPreferencesContext.release

|  | Declaration |
| --- | --- |
| From | ``` var release: CFunctionPointer<((ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` var release: CFunctionPointer<((UnsafePointer<Void>) -> Void)> ``` |

Modified SCPreferencesContext.retain

|  | Declaration |
| --- | --- |
| From | ``` var retain: CFunctionPointer<((ConstUnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` var retain: CFunctionPointer<((UnsafePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified SCBondInterfaceCopyAll(SCPreferences!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceCopyAvailableMemberInterfaces(SCPreferences!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceCopyStatus(SCBondInterface!) -> Unmanaged<SCBondStatus>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceCreate(SCPreferences!) -> Unmanaged<SCBondInterface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceGetMemberInterfaces(SCBondInterface!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceGetOptions(SCBondInterface!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceRemove(SCBondInterface!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceSetLocalizedDisplayName(SCBondInterface!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceSetMemberInterfaces(SCBondInterface!, CFArray!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondInterfaceSetOptions(SCBondInterface!, CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondStatusGetInterfaceStatus(SCBondStatus!, SCNetworkInterface!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondStatusGetMemberInterfaces(SCBondStatus!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCBondStatusGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCCopyLastError() -> Unmanaged<CFError>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCDynamicStoreAddTemporaryValue(SCDynamicStore!, CFString!, CFPropertyList!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreAddTemporaryValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyListRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreAddTemporaryValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` | OS X 10.1 |

Modified SCDynamicStoreAddValue(SCDynamicStore!, CFString!, CFPropertyList!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreAddValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyListRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreAddValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` | OS X 10.1 |

Modified SCDynamicStoreCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias SCDynamicStoreCallBack = CFunctionPointer<((SCDynamicStore!, CFArray!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias SCDynamicStoreCallBack = CFunctionPointer<((SCDynamicStore!, CFArray!, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified SCDynamicStoreCopyComputerName(SCDynamicStore!, UnsafeMutablePointer<CFStringEncoding>) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore!, _ nameEncoding: UnsafePointer<CFStringEncoding>) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreCopyComputerName(_ store: SCDynamicStore!, _ nameEncoding: UnsafeMutablePointer<CFStringEncoding>) -> Unmanaged<CFString>! ``` | OS X 10.1 |

Modified SCDynamicStoreCopyConsoleUser(SCDynamicStore!, UnsafeMutablePointer<uid_t>, UnsafeMutablePointer<gid_t>) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore!, _ uid: UnsafePointer<uid_t>, _ gid: UnsafePointer<gid_t>) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreCopyConsoleUser(_ store: SCDynamicStore!, _ uid: UnsafeMutablePointer<uid_t>, _ gid: UnsafeMutablePointer<gid_t>) -> Unmanaged<CFString>! ``` | OS X 10.1 |

Modified SCDynamicStoreCopyKeyList(SCDynamicStore!, CFString!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCopyLocalHostName(SCDynamicStore!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCopyLocation(SCDynamicStore!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCopyMultiple(SCDynamicStore!, CFArray!, CFArray!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCopyNotifiedKeys(SCDynamicStore!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCopyProxies(SCDynamicStore!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCopyValue(SCDynamicStore!, CFString!) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreCopyValue(_ store: SCDynamicStore!, _ key: CFString!) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreCopyValue(_ store: SCDynamicStore!, _ key: CFString!) -> Unmanaged<CFPropertyList>! ``` | OS X 10.1 |

Modified SCDynamicStoreCreate(CFAllocator!, CFString!, SCDynamicStoreCallBack, UnsafeMutablePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreCreate(_ allocator: CFAllocator!, _ name: CFString!, _ callout: SCDynamicStoreCallBack, _ context: UnsafePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>! ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreCreate(_ allocator: CFAllocator!, _ name: CFString!, _ callout: SCDynamicStoreCallBack, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>! ``` | OS X 10.1 |

Modified SCDynamicStoreCreateRunLoopSource(CFAllocator!, SCDynamicStore!, CFIndex) -> Unmanaged<CFRunLoopSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreCreateWithOptions(CFAllocator!, CFString!, CFDictionary!, SCDynamicStoreCallBack, UnsafeMutablePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreCreateWithOptions(_ allocator: CFAllocator!, _ name: CFString!, _ storeOptions: CFDictionary!, _ callout: SCDynamicStoreCallBack, _ context: UnsafePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>! ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreCreateWithOptions(_ allocator: CFAllocator!, _ name: CFString!, _ storeOptions: CFDictionary!, _ callout: SCDynamicStoreCallBack, _ context: UnsafeMutablePointer<SCDynamicStoreContext>) -> Unmanaged<SCDynamicStore>! ``` | OS X 10.4 |

Modified SCDynamicStoreGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateComputerName(CFAllocator!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateConsoleUser(CFAllocator!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateHostNames(CFAllocator!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SCDynamicStoreKeyCreateLocation(CFAllocator!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SCDynamicStoreKeyCreateNetworkGlobalEntity(CFAllocator!, CFString!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateNetworkInterface(CFAllocator!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateNetworkInterfaceEntity(CFAllocator!, CFString!, CFString!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateNetworkServiceEntity(CFAllocator!, CFString!, CFString!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreKeyCreateProxies(CFAllocator!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreNotifyValue(SCDynamicStore!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreRemoveValue(SCDynamicStore!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreSetDispatchQueue(SCDynamicStore!, dispatch_queue_t!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SCDynamicStoreSetMultiple(SCDynamicStore!, CFDictionary!, CFArray!, CFArray!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreSetNotificationKeys(SCDynamicStore!, CFArray!, CFArray!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCDynamicStoreSetValue(SCDynamicStore!, CFString!, CFPropertyList!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCDynamicStoreSetValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyListRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCDynamicStoreSetValue(_ store: SCDynamicStore!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` | OS X 10.1 |

Modified SCError() -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCErrorString(Int32) -> UnsafePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCErrorString(_ status: Int32) -> ConstUnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func SCErrorString(_ status: Int32) -> UnsafePointer<Int8> ``` | OS X 10.1 |

Modified SCNetworkConnectionCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkConnectionCallBack = CFunctionPointer<((SCNetworkConnection!, SCNetworkConnectionStatus, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias SCNetworkConnectionCallBack = CFunctionPointer<((SCNetworkConnection!, SCNetworkConnectionStatus, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified SCNetworkConnectionCopyExtendedStatus(SCNetworkConnection!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionCopyServiceID(SCNetworkConnection!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionCopyStatistics(SCNetworkConnection!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionCopyUserOptions(SCNetworkConnection!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionCopyUserPreferences(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary!, _ serviceID: UnsafePointer<Unmanaged<CFString>?>, _ userOptions: UnsafePointer<Unmanaged<CFDictionary>?>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary!, _ serviceID: UnsafeMutablePointer<Unmanaged<CFString>?>, _ userOptions: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Boolean ``` | OS X 10.3 |

Modified SCNetworkConnectionCreateWithServiceID(CFAllocator!, CFString!, SCNetworkConnectionCallBack, UnsafeMutablePointer<SCNetworkConnectionContext>) -> Unmanaged<SCNetworkConnection>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator!, _ serviceID: CFString!, _ callout: SCNetworkConnectionCallBack, _ context: UnsafePointer<SCNetworkConnectionContext>) -> Unmanaged<SCNetworkConnection>! ``` | OS X 10.10 |
| To | ``` func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator!, _ serviceID: CFString!, _ callout: SCNetworkConnectionCallBack, _ context: UnsafeMutablePointer<SCNetworkConnectionContext>) -> Unmanaged<SCNetworkConnection>! ``` | OS X 10.3 |

Modified SCNetworkConnectionGetStatus(SCNetworkConnection!) -> SCNetworkConnectionStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionScheduleWithRunLoop(SCNetworkConnection!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionSetDispatchQueue(SCNetworkConnection!, dispatch_queue_t!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SCNetworkConnectionStart(SCNetworkConnection!, CFDictionary!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionStop(SCNetworkConnection!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkConnectionUnscheduleFromRunLoop(SCNetworkConnection!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkInterfaceCopyAll() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceCopyMTU(SCNetworkInterface!, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface!, _ mtu_cur: UnsafePointer<Int32>, _ mtu_min: UnsafePointer<Int32>, _ mtu_max: UnsafePointer<Int32>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface!, _ mtu_cur: UnsafeMutablePointer<Int32>, _ mtu_min: UnsafeMutablePointer<Int32>, _ mtu_max: UnsafeMutablePointer<Int32>) -> Boolean ``` | OS X 10.5 |

Modified SCNetworkInterfaceCopyMediaOptions(SCNetworkInterface!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>, UnsafeMutablePointer<Unmanaged<CFArray>?>, Boolean) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface!, _ current: UnsafePointer<Unmanaged<CFDictionary>?>, _ active: UnsafePointer<Unmanaged<CFDictionary>?>, _ available: UnsafePointer<Unmanaged<CFArray>?>, _ filter: Boolean) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface!, _ current: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ active: UnsafeMutablePointer<Unmanaged<CFDictionary>?>, _ available: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ filter: Boolean) -> Boolean ``` | OS X 10.5 |

Modified SCNetworkInterfaceCopyMediaSubTypeOptions(CFArray!, CFString!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkInterfaceCopyMediaSubTypes(CFArray!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkInterfaceCreateWithInterface(SCNetworkInterface!, CFString!) -> Unmanaged<SCNetworkInterface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceForceConfigurationRefresh(SCNetworkInterface!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkInterfaceGetBSDName(SCNetworkInterface!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetConfiguration(SCNetworkInterface!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetExtendedConfiguration(SCNetworkInterface!, CFString!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkInterfaceGetHardwareAddressString(SCNetworkInterface!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetInterface(SCNetworkInterface!) -> Unmanaged<SCNetworkInterface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetInterfaceType(SCNetworkInterface!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetLocalizedDisplayName(SCNetworkInterface!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetSupportedInterfaceTypes(SCNetworkInterface!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetSupportedProtocolTypes(SCNetworkInterface!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceSetConfiguration(SCNetworkInterface!, CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkInterfaceSetExtendedConfiguration(SCNetworkInterface!, CFString!, CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkInterfaceSetMTU(SCNetworkInterface!, Int32) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkInterfaceSetMediaOptions(SCNetworkInterface!, CFString!, CFArray!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkProtocolGetConfiguration(SCNetworkProtocol!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkProtocolGetEnabled(SCNetworkProtocol!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkProtocolGetProtocolType(SCNetworkProtocol!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkProtocolGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkProtocolSetConfiguration(SCNetworkProtocol!, CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkProtocolSetEnabled(SCNetworkProtocol!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkReachabilityCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias SCNetworkReachabilityCallBack = CFunctionPointer<((SCNetworkReachability!, SCNetworkReachabilityFlags, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias SCNetworkReachabilityCallBack = CFunctionPointer<((SCNetworkReachability!, SCNetworkReachabilityFlags, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified SCNetworkReachabilityCreateWithAddress(CFAllocator!, UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithAddress(_ allocator: CFAllocator!, _ address: ConstUnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>! ``` | OS X 10.10 |
| To | ``` func SCNetworkReachabilityCreateWithAddress(_ allocator: CFAllocator!, _ address: UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>! ``` | OS X 10.3 |

Modified SCNetworkReachabilityCreateWithAddressPair(CFAllocator!, UnsafePointer<sockaddr>, UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator!, _ localAddress: ConstUnsafePointer<sockaddr>, _ remoteAddress: ConstUnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>! ``` | OS X 10.10 |
| To | ``` func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator!, _ localAddress: UnsafePointer<sockaddr>, _ remoteAddress: UnsafePointer<sockaddr>) -> Unmanaged<SCNetworkReachability>! ``` | OS X 10.3 |

Modified SCNetworkReachabilityCreateWithName(CFAllocator!, UnsafePointer<Int8>) -> Unmanaged<SCNetworkReachability>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkReachabilityCreateWithName(_ allocator: CFAllocator!, _ nodename: ConstUnsafePointer<Int8>) -> Unmanaged<SCNetworkReachability>! ``` | OS X 10.10 |
| To | ``` func SCNetworkReachabilityCreateWithName(_ allocator: CFAllocator!, _ nodename: UnsafePointer<Int8>) -> Unmanaged<SCNetworkReachability>! ``` | OS X 10.3 |

Modified SCNetworkReachabilityGetFlags(SCNetworkReachability!, UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkReachabilityGetFlags(_ target: SCNetworkReachability!, _ flags: UnsafePointer<SCNetworkReachabilityFlags>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCNetworkReachabilityGetFlags(_ target: SCNetworkReachability!, _ flags: UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Boolean ``` | OS X 10.3 |

Modified SCNetworkReachabilityGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkReachabilitySetCallback(SCNetworkReachability!, SCNetworkReachabilityCallBack, UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability!, _ callout: SCNetworkReachabilityCallBack, _ context: UnsafePointer<SCNetworkReachabilityContext>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability!, _ callout: SCNetworkReachabilityCallBack, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>) -> Boolean ``` | OS X 10.3 |

Modified SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability!, dispatch_queue_t!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified SCNetworkServiceAddProtocolType(SCNetworkService!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceCopy(SCPreferences!, CFString!) -> Unmanaged<SCNetworkService>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceCopyAll(SCPreferences!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceCopyProtocol(SCNetworkService!, CFString!) -> Unmanaged<SCNetworkProtocol>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceCopyProtocols(SCNetworkService!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceCreate(SCPreferences!, SCNetworkInterface!) -> Unmanaged<SCNetworkService>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceEstablishDefaultConfiguration(SCNetworkService!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkServiceGetEnabled(SCNetworkService!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceGetInterface(SCNetworkService!) -> Unmanaged<SCNetworkInterface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceGetName(SCNetworkService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceGetServiceID(SCNetworkService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceRemove(SCNetworkService!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceRemoveProtocolType(SCNetworkService!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceSetEnabled(SCNetworkService!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkServiceSetName(SCNetworkService!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetAddService(SCNetworkSet!, SCNetworkService!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetContainsInterface(SCNetworkSet!, SCNetworkInterface!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCNetworkSetCopy(SCPreferences!, CFString!) -> Unmanaged<SCNetworkSet>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetCopyAll(SCPreferences!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetCopyCurrent(SCPreferences!) -> Unmanaged<SCNetworkSet>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetCopyServices(SCNetworkSet!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetCreate(SCPreferences!) -> Unmanaged<SCNetworkSet>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetGetName(SCNetworkSet!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetGetServiceOrder(SCNetworkSet!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetGetSetID(SCNetworkSet!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetRemove(SCNetworkSet!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetRemoveService(SCNetworkSet!, SCNetworkService!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetSetCurrent(SCNetworkSet!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetSetName(SCNetworkSet!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCNetworkSetSetServiceOrder(SCNetworkSet!, CFArray!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCPreferencesAddValue(SCPreferences!, CFString!, CFPropertyList!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCPreferencesAddValue(_ prefs: SCPreferences!, _ key: CFString!, _ value: CFPropertyListRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCPreferencesAddValue(_ prefs: SCPreferences!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` | OS X 10.1 |

Modified SCPreferencesApplyChanges(SCPreferences!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias SCPreferencesCallBack = CFunctionPointer<((SCPreferences!, SCPreferencesNotification, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias SCPreferencesCallBack = CFunctionPointer<((SCPreferences!, SCPreferencesNotification, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified SCPreferencesCommitChanges(SCPreferences!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesCopyKeyList(SCPreferences!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesCreate(CFAllocator!, CFString!, CFString!) -> Unmanaged<SCPreferences>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesCreateWithAuthorization(CFAllocator!, CFString!, CFString!, AuthorizationRef) -> Unmanaged<SCPreferences>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator!, _ name: CFString!, _ prefsID: CFString!, _ authorization: Authorization!) -> Unmanaged<SCPreferences>! ``` | OS X 10.10 |
| To | ``` func SCPreferencesCreateWithAuthorization(_ allocator: CFAllocator!, _ name: CFString!, _ prefsID: CFString!, _ authorization: AuthorizationRef) -> Unmanaged<SCPreferences>! ``` | OS X 10.5 |

Modified SCPreferencesGetSignature(SCPreferences!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesGetValue(SCPreferences!, CFString!) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCPreferencesGetValue(_ prefs: SCPreferences!, _ key: CFString!) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 |
| To | ``` func SCPreferencesGetValue(_ prefs: SCPreferences!, _ key: CFString!) -> Unmanaged<CFPropertyList>! ``` | OS X 10.1 |

Modified SCPreferencesLock(SCPreferences!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesPathCreateUniqueChild(SCPreferences!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesPathGetLink(SCPreferences!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesPathGetValue(SCPreferences!, CFString!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesPathRemoveValue(SCPreferences!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesPathSetLink(SCPreferences!, CFString!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesPathSetValue(SCPreferences!, CFString!, CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesRemoveValue(SCPreferences!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesScheduleWithRunLoop(SCPreferences!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCPreferencesSetCallback(SCPreferences!, SCPreferencesCallBack, UnsafeMutablePointer<SCPreferencesContext>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCPreferencesSetCallback(_ prefs: SCPreferences!, _ callout: SCPreferencesCallBack, _ context: UnsafePointer<SCPreferencesContext>) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCPreferencesSetCallback(_ prefs: SCPreferences!, _ callout: SCPreferencesCallBack, _ context: UnsafeMutablePointer<SCPreferencesContext>) -> Boolean ``` | OS X 10.4 |

Modified SCPreferencesSetComputerName(SCPreferences!, CFString!, CFStringEncoding) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesSetDispatchQueue(SCPreferences!, dispatch_queue_t!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SCPreferencesSetLocalHostName(SCPreferences!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified SCPreferencesSetValue(SCPreferences!, CFString!, CFPropertyList!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func SCPreferencesSetValue(_ prefs: SCPreferences!, _ key: CFString!, _ value: CFPropertyListRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func SCPreferencesSetValue(_ prefs: SCPreferences!, _ key: CFString!, _ value: CFPropertyList!) -> Boolean ``` | OS X 10.1 |

Modified SCPreferencesSynchronize(SCPreferences!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCPreferencesUnlock(SCPreferences!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified SCPreferencesUnscheduleFromRunLoop(SCPreferences!, CFRunLoop!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified SCVLANInterfaceCopyAll(SCPreferences!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceCreate(SCPreferences!, SCNetworkInterface!, CFNumber!) -> Unmanaged<SCVLANInterface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceGetOptions(SCVLANInterface!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceGetPhysicalInterface(SCVLANInterface!) -> Unmanaged<SCNetworkInterface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceGetTag(SCVLANInterface!) -> Unmanaged<CFNumber>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceRemove(SCVLANInterface!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceSetLocalizedDisplayName(SCVLANInterface!, CFString!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceSetOptions(SCVLANInterface!, CFDictionary!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SCVLANInterfaceSetPhysicalInterfaceAndTag(SCVLANInterface!, SCNetworkInterface!, CFNumber!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainSystemConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCBondStatusDeviceAggregationStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCBondStatusDeviceCollecting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCBondStatusDeviceDistributing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCCompAnyRegex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCCompGlobal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCCompHostNames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCCompInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCCompNetwork

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCCompService

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCCompSystem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCCompUsers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStoreDomainFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStoreDomainPlugin

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStoreDomainPrefs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStoreDomainSetup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStoreDomainState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStorePropNetInterfaces

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStorePropNetPrimaryInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStorePropNetPrimaryService

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStorePropNetServiceIDs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStorePropSetupCurrentSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStorePropSetupLastUpdated

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCDynamicStoreUseSessionKeys

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCEntNet6to4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCEntNetAirPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetDHCP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetDNS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetEthernet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetFireWire

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCEntNetIPSec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCEntNetIPv4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetIPv6

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetL2TP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCEntNetLink

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetModem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetPPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetPPPSerial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCEntNetPPPoE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetPPTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCEntNetProxies

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCEntNetSMB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCEntUsersConsoleUser

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCNetworkInterfaceIPv4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceType6to4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeBluetooth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeBond

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeEthernet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeFireWire

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeIEEE80211

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeIPSec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCNetworkInterfaceTypeIPv4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeIrDA

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeL2TP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeModem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypePPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypePPTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeSerial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeVLAN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkInterfaceTypeWWAN

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCNetworkProtocolTypeDNS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkProtocolTypeIPv4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkProtocolTypeIPv6

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkProtocolTypeProxies

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCNetworkProtocolTypeSMB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPrefCurrentSet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPrefNetworkServices

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPrefSets

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPrefSystem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropInterfaceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropMACAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNet6to4Relay

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetDNSDomainName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetDNSOptions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetDNSSearchDomains

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetDNSSearchOrder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetDNSServerAddresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetDNSServerPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetDNSServerTimeout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetDNSSortList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetDNSSupplementalMatchDomains

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetDNSSupplementalMatchOrders

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetEthernetMTU

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetEthernetMediaOptions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetEthernetMediaSubType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetIPSecAuthenticationMethod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetIPSecConnectTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPSecLocalCertificate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetIPSecLocalIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetIPSecLocalIdentifierType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetIPSecRemoteAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPSecSharedSecret

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetIPSecSharedSecretEncryption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetIPSecStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPSecXAuthEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPSecXAuthName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPSecXAuthPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPSecXAuthPasswordEncryption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCPropNetIPv4Addresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv4BroadcastAddresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv4ConfigMethod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv4DHCPClientID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv4DestAddresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv4Router

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv4SubnetMasks

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv6Addresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv6ConfigMethod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetIPv6DestAddresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetIPv6Flags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetIPv6PrefixLength

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetIPv6Router

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetInterfaceDeviceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetInterfaceHardware

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetInterfaceSubType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetInterfaceSupportsModemOnHold

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetInterfaceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetInterfaces

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetL2TPIPSecSharedSecret

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetL2TPIPSecSharedSecretEncryption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetL2TPTransport

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetLinkActive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetLinkDetaching

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetLocalHostName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemAccessPointName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetModemConnectSpeed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemConnectionPersonality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetModemConnectionScript

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetModemDataCompression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetModemDeviceContextID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetModemDeviceModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetModemDeviceVendor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetModemDialMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetModemErrorCorrection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetModemHoldCallWaitingAudibleAlert

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemHoldDisconnectOnAnswer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemHoldEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemHoldReminder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemHoldReminderTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemNote

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetModemPulseDial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetModemSpeaker

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetModemSpeed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetOverridePrimary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPACSPEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetPPPAuthEAPPlugins

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetPPPAuthName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPAuthPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPAuthPasswordEncryption

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPAuthPrompt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetPPPAuthProtocol

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCCPEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPCCPMPPE128Enabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetPPPCCPMPPE40Enabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetPPPCommAlternateRemoteAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommConnectDelay

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommDisplayTerminalWindow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommRedialCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommRedialEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommRedialInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommRemoteAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommTerminalScript

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPCommUseTerminalScript

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPConnectTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPDeviceLastCause

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPDialOnDemand

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPDisconnectOnFastUserSwitch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetPPPDisconnectOnIdle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPDisconnectOnIdleTimer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPDisconnectOnLogout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPDisconnectOnSleep

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPDisconnectTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetPPPIPCPCompressionVJ

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPIPCPUsePeerDNS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetPPPIdleReminder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPIdleReminderTimer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPCompressionACField

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPCompressionPField

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPEchoEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPEchoFailure

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPEchoInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPMRU

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPMTU

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPReceiveACCM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLCPTransmitACCM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPLastCause

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPLogfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPOverridePrimary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPPlugins

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPRetryConnectTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCPropNetPPPSessionTimer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetPPPStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPUseSessionTimer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCPropNetPPPVerboseLogging

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesExceptionsList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesExcludeSimpleHostnames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetProxiesFTPEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesFTPPassive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesFTPPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesFTPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesGopherEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesGopherPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesGopherProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesHTTPEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesHTTPPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesHTTPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesHTTPSEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesHTTPSPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesHTTPSProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesProxyAutoConfigEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetProxiesProxyAutoConfigJavaScript

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSCPropNetProxiesProxyAutoConfigURLString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetProxiesProxyAutoDiscoveryEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kSCPropNetProxiesRTSPEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesRTSPPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesRTSPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesSOCKSEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesSOCKSPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetProxiesSOCKSProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropNetSMBNetBIOSName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetSMBNetBIOSNodeType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetSMBWINSAddresses

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetSMBWorkgroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCPropNetServiceOrder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropSystemComputerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropSystemComputerNameEncoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropUserDefinedName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCPropVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCResvInactive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCResvLink

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetIPSecAuthenticationMethodCertificate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetIPSecAuthenticationMethodHybrid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetIPSecAuthenticationMethodSharedSecret

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetIPSecLocalIdentifierTypeKeyID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetIPSecSharedSecretEncryptionKeychain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetIPSecXAuthPasswordEncryptionKeychain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCValNetIPSecXAuthPasswordEncryptionPrompt

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCValNetIPv4ConfigMethodAutomatic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCValNetIPv4ConfigMethodBOOTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetIPv4ConfigMethodDHCP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetIPv4ConfigMethodINFORM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetIPv4ConfigMethodLinkLocal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCValNetIPv4ConfigMethodManual

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetIPv4ConfigMethodPPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetIPv6ConfigMethod6to4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetIPv6ConfigMethodAutomatic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetIPv6ConfigMethodLinkLocal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kSCValNetIPv6ConfigMethodManual

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetIPv6ConfigMethodRouterAdvertisement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetInterfaceSubTypeL2TP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetInterfaceSubTypePPPSerial

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetInterfaceSubTypePPPoE

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetInterfaceSubTypePPTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kSCValNetInterfaceType6to4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetInterfaceTypeEthernet

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetInterfaceTypeFireWire

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetInterfaceTypeIPSec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kSCValNetInterfaceTypePPP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetL2TPIPSecSharedSecretEncryptionKeychain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetL2TPTransportIP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetL2TPTransportIPSec

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetModemDialModeIgnoreDialTone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetModemDialModeManual

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetModemDialModeWaitForDialTone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetPPPAuthPasswordEncryptionKeychain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetPPPAuthPasswordEncryptionToken

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetPPPAuthPromptAfter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetPPPAuthPromptBefore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetPPPAuthProtocolCHAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetPPPAuthProtocolEAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetPPPAuthProtocolMSCHAP1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetPPPAuthProtocolMSCHAP2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kSCValNetPPPAuthProtocolPAP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kSCValNetSMBNetBIOSNodeTypeBroadcast

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetSMBNetBIOSNodeTypeHybrid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetSMBNetBIOSNodeTypeMixed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kSCValNetSMBNetBIOSNodeTypePeer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

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
