---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/SystemConfiguration.html
archived_at: '2026-07-18T02:53:14.391619Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# SystemConfiguration Changes for Objective-C

### SystemConfiguration

#### CaptiveNetwork.h

Added #def CN_DEPRECATION_NOTICEModified [CNCopySupportedInterfaces()](https://developer.apple.com/documentation/systemconfiguration/1494829-cncopysupportedinterfaces)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CNCopySupportedInterfaces (     void ); ``` |
| To | ``` CFArrayRef _Nullable CNCopySupportedInterfaces (     void ); ``` |

Modified [CNMarkPortalOffline()](https://developer.apple.com/documentation/systemconfiguration/1494825-cnmarkportaloffline)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CNMarkPortalOffline (     CFStringRef interfaceName ); ``` |
| To | ``` Boolean CNMarkPortalOffline (     CFStringRef _Nonnull interfaceName ); ``` |

Modified [CNMarkPortalOnline()](https://developer.apple.com/documentation/systemconfiguration/1494833-cnmarkportalonline)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CNMarkPortalOnline (     CFStringRef interfaceName ); ``` |
| To | ``` Boolean CNMarkPortalOnline (     CFStringRef _Nonnull interfaceName ); ``` |

Modified [CNSetSupportedSSIDs()](https://developer.apple.com/documentation/systemconfiguration/1494831-cnsetsupportedssids)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CNSetSupportedSSIDs (     CFArrayRef ssidArray ); ``` |
| To | ``` Boolean CNSetSupportedSSIDs (     CFArrayRef _Nonnull ssidArray ); ``` |

#### DHCPClientPreferences.h

Modified [DHCPClientPreferencesCopyApplicationOptions()](https://developer.apple.com/documentation/systemconfiguration/1386993-dhcpclientpreferencescopyapplica)

|  | Declaration |
| --- | --- |
| From | ``` UInt8 * DHCPClientPreferencesCopyApplicationOptions (     CFStringRef applicationID,     CFIndex *count ); ``` |
| To | ``` UInt8 * _Nullable DHCPClientPreferencesCopyApplicationOptions (     CFStringRef _Nonnull applicationID,     CFIndex * _Nonnull count ); ``` |

Modified [DHCPClientPreferencesSetApplicationOptions()](https://developer.apple.com/documentation/systemconfiguration/1386995-dhcpclientpreferencessetapplicat)

|  | Declaration |
| --- | --- |
| From | ``` Boolean DHCPClientPreferencesSetApplicationOptions (     CFStringRef applicationID,     UInt8 *options,     CFIndex count ); ``` |
| To | ``` Boolean DHCPClientPreferencesSetApplicationOptions (     CFStringRef _Nonnull applicationID,     UInt8 * _Nullable options,     CFIndex count ); ``` |

#### SCDynamicStore.h

Modified [SCDynamicStoreAddTemporaryValue()](https://developer.apple.com/documentation/systemconfiguration/1437789-scdynamicstoreaddtemporaryvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreAddTemporaryValue (     SCDynamicStoreRef store,     CFStringRef key,     CFPropertyListRef value ); ``` |
| To | ``` Boolean SCDynamicStoreAddTemporaryValue (     SCDynamicStoreRef _Nonnull store,     CFStringRef _Nonnull key,     CFPropertyListRef _Nonnull value ); ``` |

Modified [SCDynamicStoreAddValue()](https://developer.apple.com/documentation/systemconfiguration/1437785-scdynamicstoreaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreAddValue (     SCDynamicStoreRef store,     CFStringRef key,     CFPropertyListRef value ); ``` |
| To | ``` Boolean SCDynamicStoreAddValue (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nonnull key,     CFPropertyListRef _Nonnull value ); ``` |

Modified [SCDynamicStoreCopyKeyList()](https://developer.apple.com/documentation/systemconfiguration/1437799-scdynamicstorecopykeylist)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCDynamicStoreCopyKeyList (     SCDynamicStoreRef store,     CFStringRef pattern ); ``` |
| To | ``` CFArrayRef _Nullable SCDynamicStoreCopyKeyList (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nonnull pattern ); ``` |

Modified [SCDynamicStoreCopyMultiple()](https://developer.apple.com/documentation/systemconfiguration/1437809-scdynamicstorecopymultiple)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCDynamicStoreCopyMultiple (     SCDynamicStoreRef store,     CFArrayRef keys,     CFArrayRef patterns ); ``` |
| To | ``` CFDictionaryRef _Nullable SCDynamicStoreCopyMultiple (     SCDynamicStoreRef _Nullable store,     CFArrayRef _Nullable keys,     CFArrayRef _Nullable patterns ); ``` |

Modified [SCDynamicStoreCopyNotifiedKeys()](https://developer.apple.com/documentation/systemconfiguration/1437805-scdynamicstorecopynotifiedkeys)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCDynamicStoreCopyNotifiedKeys (     SCDynamicStoreRef store ); ``` |
| To | ``` CFArrayRef _Nullable SCDynamicStoreCopyNotifiedKeys (     SCDynamicStoreRef _Nonnull store ); ``` |

Modified [SCDynamicStoreCopyValue()](https://developer.apple.com/documentation/systemconfiguration/1437812-scdynamicstorecopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` CFPropertyListRef SCDynamicStoreCopyValue (     SCDynamicStoreRef store,     CFStringRef key ); ``` |
| To | ``` CFPropertyListRef _Nullable SCDynamicStoreCopyValue (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nonnull key ); ``` |

Modified [SCDynamicStoreCreate()](https://developer.apple.com/documentation/systemconfiguration/1437828-scdynamicstorecreate)

|  | Declaration |
| --- | --- |
| From | ``` SCDynamicStoreRef SCDynamicStoreCreate (     CFAllocatorRef allocator,     CFStringRef name,     SCDynamicStoreCallBack callout,     SCDynamicStoreContext *context ); ``` |
| To | ``` SCDynamicStoreRef _Nullable SCDynamicStoreCreate (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull name,     SCDynamicStoreCallBack _Nullable callout,     SCDynamicStoreContext * _Nullable context ); ``` |

Modified [SCDynamicStoreCreateRunLoopSource()](https://developer.apple.com/documentation/systemconfiguration/1437797-scdynamicstorecreaterunloopsourc)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopSourceRef SCDynamicStoreCreateRunLoopSource (     CFAllocatorRef allocator,     SCDynamicStoreRef store,     CFIndex order ); ``` |
| To | ``` CFRunLoopSourceRef _Nullable SCDynamicStoreCreateRunLoopSource (     CFAllocatorRef _Nullable allocator,     SCDynamicStoreRef _Nonnull store,     CFIndex order ); ``` |

Modified [SCDynamicStoreCreateWithOptions()](https://developer.apple.com/documentation/systemconfiguration/1437818-scdynamicstorecreatewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` SCDynamicStoreRef SCDynamicStoreCreateWithOptions (     CFAllocatorRef allocator,     CFStringRef name,     CFDictionaryRef storeOptions,     SCDynamicStoreCallBack callout,     SCDynamicStoreContext *context ); ``` |
| To | ``` SCDynamicStoreRef _Nullable SCDynamicStoreCreateWithOptions (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull name,     CFDictionaryRef _Nullable storeOptions,     SCDynamicStoreCallBack _Nullable callout,     SCDynamicStoreContext * _Nullable context ); ``` |

Modified [SCDynamicStoreNotifyValue()](https://developer.apple.com/documentation/systemconfiguration/1437793-scdynamicstorenotifyvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreNotifyValue (     SCDynamicStoreRef store,     CFStringRef key ); ``` |
| To | ``` Boolean SCDynamicStoreNotifyValue (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nonnull key ); ``` |

Modified [SCDynamicStoreRemoveValue()](https://developer.apple.com/documentation/systemconfiguration/1437783-scdynamicstoreremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreRemoveValue (     SCDynamicStoreRef store,     CFStringRef key ); ``` |
| To | ``` Boolean SCDynamicStoreRemoveValue (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nonnull key ); ``` |

Modified [SCDynamicStoreSetDispatchQueue()](https://developer.apple.com/documentation/systemconfiguration/1437816-scdynamicstoresetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreSetDispatchQueue (     SCDynamicStoreRef store,     dispatch_queue_t queue ); ``` |
| To | ``` Boolean SCDynamicStoreSetDispatchQueue (     SCDynamicStoreRef _Nonnull store,     dispatch_queue_t _Nullable queue ); ``` |

Modified [SCDynamicStoreSetMultiple()](https://developer.apple.com/documentation/systemconfiguration/1437824-scdynamicstoresetmultiple)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreSetMultiple (     SCDynamicStoreRef store,     CFDictionaryRef keysToSet,     CFArrayRef keysToRemove,     CFArrayRef keysToNotify ); ``` |
| To | ``` Boolean SCDynamicStoreSetMultiple (     SCDynamicStoreRef _Nullable store,     CFDictionaryRef _Nullable keysToSet,     CFArrayRef _Nullable keysToRemove,     CFArrayRef _Nullable keysToNotify ); ``` |

Modified [SCDynamicStoreSetNotificationKeys()](https://developer.apple.com/documentation/systemconfiguration/1437820-scdynamicstoresetnotificationkey)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreSetNotificationKeys (     SCDynamicStoreRef store,     CFArrayRef keys,     CFArrayRef patterns ); ``` |
| To | ``` Boolean SCDynamicStoreSetNotificationKeys (     SCDynamicStoreRef _Nonnull store,     CFArrayRef _Nullable keys,     CFArrayRef _Nullable patterns ); ``` |

Modified [SCDynamicStoreSetValue()](https://developer.apple.com/documentation/systemconfiguration/1437814-scdynamicstoresetvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCDynamicStoreSetValue (     SCDynamicStoreRef store,     CFStringRef key,     CFPropertyListRef value ); ``` |
| To | ``` Boolean SCDynamicStoreSetValue (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nonnull key,     CFPropertyListRef _Nonnull value ); ``` |

#### SCDynamicStoreCopyDHCPInfo.h

Modified [DHCPInfoGetLeaseExpirationTime()](https://developer.apple.com/documentation/systemconfiguration/1500230-dhcpinfogetleaseexpirationtime)

|  | Declaration |
| --- | --- |
| From | ``` CFDateRef DHCPInfoGetLeaseExpirationTime (     CFDictionaryRef info ); ``` |
| To | ``` CFDateRef _Nullable DHCPInfoGetLeaseExpirationTime (     CFDictionaryRef _Nonnull info ); ``` |

Modified [DHCPInfoGetLeaseStartTime()](https://developer.apple.com/documentation/systemconfiguration/1500232-dhcpinfogetleasestarttime)

|  | Declaration |
| --- | --- |
| From | ``` CFDateRef DHCPInfoGetLeaseStartTime (     CFDictionaryRef info ); ``` |
| To | ``` CFDateRef _Nullable DHCPInfoGetLeaseStartTime (     CFDictionaryRef _Nonnull info ); ``` |

Modified [DHCPInfoGetOptionData()](https://developer.apple.com/documentation/systemconfiguration/1500228-dhcpinfogetoptiondata)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef DHCPInfoGetOptionData (     CFDictionaryRef info,     UInt8 code ); ``` |
| To | ``` CFDataRef _Nullable DHCPInfoGetOptionData (     CFDictionaryRef _Nonnull info,     UInt8 code ); ``` |

Modified [SCDynamicStoreCopyDHCPInfo()](https://developer.apple.com/documentation/systemconfiguration/1500231-scdynamicstorecopydhcpinfo)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCDynamicStoreCopyDHCPInfo (     SCDynamicStoreRef store,     CFStringRef serviceID ); ``` |
| To | ``` CFDictionaryRef _Nullable SCDynamicStoreCopyDHCPInfo (     SCDynamicStoreRef _Nullable store,     CFStringRef _Nullable serviceID ); ``` |

#### SCDynamicStoreCopySpecific.h

Modified [SCDynamicStoreCopyComputerName()](https://developer.apple.com/documentation/systemconfiguration/1517208-scdynamicstorecopycomputername)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreCopyComputerName (     SCDynamicStoreRef store,     CFStringEncoding *nameEncoding ); ``` |
| To | ``` CFStringRef _Nullable SCDynamicStoreCopyComputerName (     SCDynamicStoreRef _Nullable store,     CFStringEncoding * _Nullable nameEncoding ); ``` |

Modified [SCDynamicStoreCopyConsoleUser()](https://developer.apple.com/documentation/systemconfiguration/1517123-scdynamicstorecopyconsoleuser)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreCopyConsoleUser (     SCDynamicStoreRef store,     uid_t *uid,     gid_t *gid ); ``` |
| To | ``` CFStringRef _Nullable SCDynamicStoreCopyConsoleUser (     SCDynamicStoreRef _Nullable store,     uid_t * _Nullable uid,     gid_t * _Nullable gid ); ``` |

Modified [SCDynamicStoreCopyLocalHostName()](https://developer.apple.com/documentation/systemconfiguration/1517066-scdynamicstorecopylocalhostname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreCopyLocalHostName (     SCDynamicStoreRef store ); ``` |
| To | ``` CFStringRef _Nullable SCDynamicStoreCopyLocalHostName (     SCDynamicStoreRef _Nullable store ); ``` |

Modified [SCDynamicStoreCopyLocation()](https://developer.apple.com/documentation/systemconfiguration/1517216-scdynamicstorecopylocation)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreCopyLocation (     SCDynamicStoreRef store ); ``` |
| To | ``` CFStringRef _Nullable SCDynamicStoreCopyLocation (     SCDynamicStoreRef _Nullable store ); ``` |

Modified [SCDynamicStoreCopyProxies()](https://developer.apple.com/documentation/systemconfiguration/1517088-scdynamicstorecopyproxies)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCDynamicStoreCopyProxies (     SCDynamicStoreRef store ); ``` |
| To | ``` CFDictionaryRef _Nullable SCDynamicStoreCopyProxies (     SCDynamicStoreRef _Nullable store ); ``` |

#### SCDynamicStoreKey.h

Modified [SCDynamicStoreKeyCreate()](https://developer.apple.com/documentation/systemconfiguration/1578297-scdynamicstorekeycreate)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreate (     CFAllocatorRef allocator,     CFStringRef fmt,     ... ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreate (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull fmt,     ... ); ``` |

Modified [SCDynamicStoreKeyCreateComputerName()](https://developer.apple.com/documentation/systemconfiguration/1517319-scdynamicstorekeycreatecomputern)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateComputerName (     CFAllocatorRef allocator ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateComputerName (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [SCDynamicStoreKeyCreateConsoleUser()](https://developer.apple.com/documentation/systemconfiguration/1517286-scdynamicstorekeycreateconsoleus)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateConsoleUser (     CFAllocatorRef allocator ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateConsoleUser (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [SCDynamicStoreKeyCreateHostNames()](https://developer.apple.com/documentation/systemconfiguration/1517184-scdynamicstorekeycreatehostnames)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateHostNames (     CFAllocatorRef allocator ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateHostNames (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [SCDynamicStoreKeyCreateLocation()](https://developer.apple.com/documentation/systemconfiguration/1516900-scdynamicstorekeycreatelocation)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateLocation (     CFAllocatorRef allocator ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateLocation (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [SCDynamicStoreKeyCreateNetworkGlobalEntity()](https://developer.apple.com/documentation/systemconfiguration/1516684-scdynamicstorekeycreatenetworkgl)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateNetworkGlobalEntity (     CFAllocatorRef allocator,     CFStringRef domain,     CFStringRef entity ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateNetworkGlobalEntity (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull domain,     CFStringRef _Nonnull entity ); ``` |

Modified [SCDynamicStoreKeyCreateNetworkInterface()](https://developer.apple.com/documentation/systemconfiguration/1517022-scdynamicstorekeycreatenetworkin)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateNetworkInterface (     CFAllocatorRef allocator,     CFStringRef domain ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateNetworkInterface (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull domain ); ``` |

Modified [SCDynamicStoreKeyCreateNetworkInterfaceEntity()](https://developer.apple.com/documentation/systemconfiguration/1517099-scdynamicstorekeycreatenetworkin)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateNetworkInterfaceEntity (     CFAllocatorRef allocator,     CFStringRef domain,     CFStringRef ifname,     CFStringRef entity ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateNetworkInterfaceEntity (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull domain,     CFStringRef _Nonnull ifname,     CFStringRef _Nullable entity ); ``` |

Modified [SCDynamicStoreKeyCreateNetworkServiceEntity()](https://developer.apple.com/documentation/systemconfiguration/1517288-scdynamicstorekeycreatenetworkse)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateNetworkServiceEntity (     CFAllocatorRef allocator,     CFStringRef domain,     CFStringRef serviceID,     CFStringRef entity ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateNetworkServiceEntity (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull domain,     CFStringRef _Nonnull serviceID,     CFStringRef _Nullable entity ); ``` |

Modified [SCDynamicStoreKeyCreateProxies()](https://developer.apple.com/documentation/systemconfiguration/1516870-scdynamicstorekeycreateproxies)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCDynamicStoreKeyCreateProxies (     CFAllocatorRef allocator ); ``` |
| To | ``` CFStringRef _Nonnull SCDynamicStoreKeyCreateProxies (     CFAllocatorRef _Nullable allocator ); ``` |

#### SCNetwork.h

Modified [SCNetworkCheckReachabilityByAddress()](https://developer.apple.com/documentation/systemconfiguration/1420208-scnetworkcheckreachabilitybyaddr)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkCheckReachabilityByAddress (     const struct sockaddr *address,     socklen_t addrlen,     SCNetworkConnectionFlags *flags ); ``` |
| To | ``` Boolean SCNetworkCheckReachabilityByAddress (     const struct sockaddr * _Nonnull address,     socklen_t addrlen,     SCNetworkConnectionFlags * _Nonnull flags ); ``` |

Modified [SCNetworkCheckReachabilityByName()](https://developer.apple.com/documentation/systemconfiguration/1420196-scnetworkcheckreachabilitybyname)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkCheckReachabilityByName (     const char *nodename,     SCNetworkConnectionFlags *flags ); ``` |
| To | ``` Boolean SCNetworkCheckReachabilityByName (     const char * _Nonnull nodename,     SCNetworkConnectionFlags * _Nonnull flags ); ``` |

Modified [SCNetworkInterfaceRefreshConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1420192-scnetworkinterfacerefreshconfigu)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceRefreshConfiguration (     CFStringRef ifName ); ``` |
| To | ``` Boolean SCNetworkInterfaceRefreshConfiguration (     CFStringRef _Nonnull ifName ); ``` |

#### SCNetworkConfiguration.h

Modified [SCBondInterfaceCopyAll()](https://developer.apple.com/documentation/systemconfiguration/1517283-scbondinterfacecopyall)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCBondInterfaceCopyAll (     SCPreferencesRef prefs ); ``` |
| To | ``` CFArrayRef _Nonnull SCBondInterfaceCopyAll (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCBondInterfaceCopyAvailableMemberInterfaces()](https://developer.apple.com/documentation/systemconfiguration/1516848-scbondinterfacecopyavailablememb)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCBondInterfaceCopyAvailableMemberInterfaces (     SCPreferencesRef prefs ); ``` |
| To | ``` CFArrayRef _Nonnull SCBondInterfaceCopyAvailableMemberInterfaces (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCBondInterfaceCopyStatus()](https://developer.apple.com/documentation/systemconfiguration/1517046-scbondinterfacecopystatus)

|  | Declaration |
| --- | --- |
| From | ``` SCBondStatusRef SCBondInterfaceCopyStatus (     SCBondInterfaceRef bond ); ``` |
| To | ``` SCBondStatusRef _Nullable SCBondInterfaceCopyStatus (     SCBondInterfaceRef _Nonnull bond ); ``` |

Modified [SCBondInterfaceCreate()](https://developer.apple.com/documentation/systemconfiguration/1517251-scbondinterfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` SCBondInterfaceRef SCBondInterfaceCreate (     SCPreferencesRef prefs ); ``` |
| To | ``` SCBondInterfaceRef _Nullable SCBondInterfaceCreate (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCBondInterfaceGetMemberInterfaces()](https://developer.apple.com/documentation/systemconfiguration/1516896-scbondinterfacegetmemberinterfac)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCBondInterfaceGetMemberInterfaces (     SCBondInterfaceRef bond ); ``` |
| To | ``` CFArrayRef _Nullable SCBondInterfaceGetMemberInterfaces (     SCBondInterfaceRef _Nonnull bond ); ``` |

Modified [SCBondInterfaceGetOptions()](https://developer.apple.com/documentation/systemconfiguration/1517018-scbondinterfacegetoptions)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCBondInterfaceGetOptions (     SCBondInterfaceRef bond ); ``` |
| To | ``` CFDictionaryRef _Nullable SCBondInterfaceGetOptions (     SCBondInterfaceRef _Nonnull bond ); ``` |

Modified [SCBondInterfaceRemove()](https://developer.apple.com/documentation/systemconfiguration/1517223-scbondinterfaceremove)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCBondInterfaceRemove (     SCBondInterfaceRef bond ); ``` |
| To | ``` Boolean SCBondInterfaceRemove (     SCBondInterfaceRef _Nonnull bond ); ``` |

Modified [SCBondInterfaceSetLocalizedDisplayName()](https://developer.apple.com/documentation/systemconfiguration/1516742-scbondinterfacesetlocalizeddispl)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCBondInterfaceSetLocalizedDisplayName (     SCBondInterfaceRef bond,     CFStringRef newName ); ``` |
| To | ``` Boolean SCBondInterfaceSetLocalizedDisplayName (     SCBondInterfaceRef _Nonnull bond,     CFStringRef _Nonnull newName ); ``` |

Modified [SCBondInterfaceSetMemberInterfaces()](https://developer.apple.com/documentation/systemconfiguration/1517285-scbondinterfacesetmemberinterfac)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCBondInterfaceSetMemberInterfaces (     SCBondInterfaceRef bond,     CFArrayRef members ); ``` |
| To | ``` Boolean SCBondInterfaceSetMemberInterfaces (     SCBondInterfaceRef _Nonnull bond,     CFArrayRef _Nonnull members ); ``` |

Modified [SCBondInterfaceSetOptions()](https://developer.apple.com/documentation/systemconfiguration/1516818-scbondinterfacesetoptions)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCBondInterfaceSetOptions (     SCBondInterfaceRef bond,     CFDictionaryRef newOptions ); ``` |
| To | ``` Boolean SCBondInterfaceSetOptions (     SCBondInterfaceRef _Nonnull bond,     CFDictionaryRef _Nonnull newOptions ); ``` |

Modified [SCBondStatusGetInterfaceStatus()](https://developer.apple.com/documentation/systemconfiguration/1517119-scbondstatusgetinterfacestatus)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCBondStatusGetInterfaceStatus (     SCBondStatusRef bondStatus,     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFDictionaryRef _Nullable SCBondStatusGetInterfaceStatus (     SCBondStatusRef _Nonnull bondStatus,     SCNetworkInterfaceRef _Nullable interface ); ``` |

Modified [SCBondStatusGetMemberInterfaces()](https://developer.apple.com/documentation/systemconfiguration/1517239-scbondstatusgetmemberinterfaces)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCBondStatusGetMemberInterfaces (     SCBondStatusRef bondStatus ); ``` |
| To | ``` CFArrayRef _Nullable SCBondStatusGetMemberInterfaces (     SCBondStatusRef _Nonnull bondStatus ); ``` |

Modified [SCNetworkInterfaceCopyAll()](https://developer.apple.com/documentation/systemconfiguration/1517090-scnetworkinterfacecopyall)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkInterfaceCopyAll (     void ); ``` |
| To | ``` CFArrayRef _Nonnull SCNetworkInterfaceCopyAll (     void ); ``` |

Modified [SCNetworkInterfaceCopyMediaOptions()](https://developer.apple.com/documentation/systemconfiguration/1516738-scnetworkinterfacecopymediaoptio)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceCopyMediaOptions (     SCNetworkInterfaceRef interface,     CFDictionaryRef *current,     CFDictionaryRef *active,     CFArrayRef *available,     Boolean filter ); ``` |
| To | ``` Boolean SCNetworkInterfaceCopyMediaOptions (     SCNetworkInterfaceRef _Nonnull interface,     CFDictionaryRef  _Nullable * _Nullable current,     CFDictionaryRef  _Nullable * _Nullable active,     CFArrayRef  _Nullable * _Nullable available,     Boolean filter ); ``` |

Modified [SCNetworkInterfaceCopyMediaSubTypeOptions()](https://developer.apple.com/documentation/systemconfiguration/1516695-scnetworkinterfacecopymediasubty)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkInterfaceCopyMediaSubTypeOptions (     CFArrayRef available,     CFStringRef subType ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkInterfaceCopyMediaSubTypeOptions (     CFArrayRef _Nonnull available,     CFStringRef _Nonnull subType ); ``` |

Modified [SCNetworkInterfaceCopyMediaSubTypes()](https://developer.apple.com/documentation/systemconfiguration/1516927-scnetworkinterfacecopymediasubty)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkInterfaceCopyMediaSubTypes (     CFArrayRef available ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkInterfaceCopyMediaSubTypes (     CFArrayRef _Nonnull available ); ``` |

Modified [SCNetworkInterfaceCopyMTU()](https://developer.apple.com/documentation/systemconfiguration/1517279-scnetworkinterfacecopymtu)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceCopyMTU (     SCNetworkInterfaceRef interface,     int *mtu_cur,     int *mtu_min,     int *mtu_max ); ``` |
| To | ``` Boolean SCNetworkInterfaceCopyMTU (     SCNetworkInterfaceRef _Nonnull interface,     int * _Nullable mtu_cur,     int * _Nullable mtu_min,     int * _Nullable mtu_max ); ``` |

Modified [SCNetworkInterfaceCreateWithInterface()](https://developer.apple.com/documentation/systemconfiguration/1516824-scnetworkinterfacecreatewithinte)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkInterfaceRef SCNetworkInterfaceCreateWithInterface (     SCNetworkInterfaceRef interface,     CFStringRef interfaceType ); ``` |
| To | ``` SCNetworkInterfaceRef _Nullable SCNetworkInterfaceCreateWithInterface (     SCNetworkInterfaceRef _Nonnull interface,     CFStringRef _Nonnull interfaceType ); ``` |

Modified [SCNetworkInterfaceForceConfigurationRefresh()](https://developer.apple.com/documentation/systemconfiguration/1516815-scnetworkinterfaceforceconfigura)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceForceConfigurationRefresh (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` Boolean SCNetworkInterfaceForceConfigurationRefresh (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetBSDName()](https://developer.apple.com/documentation/systemconfiguration/1516854-scnetworkinterfacegetbsdname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkInterfaceGetBSDName (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkInterfaceGetBSDName (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1516867-scnetworkinterfacegetconfigurati)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCNetworkInterfaceGetConfiguration (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFDictionaryRef _Nullable SCNetworkInterfaceGetConfiguration (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetExtendedConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1517315-scnetworkinterfacegetextendedcon)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCNetworkInterfaceGetExtendedConfiguration (     SCNetworkInterfaceRef interface,     CFStringRef extendedType ); ``` |
| To | ``` CFDictionaryRef _Nullable SCNetworkInterfaceGetExtendedConfiguration (     SCNetworkInterfaceRef _Nonnull interface,     CFStringRef _Nonnull extendedType ); ``` |

Modified [SCNetworkInterfaceGetHardwareAddressString()](https://developer.apple.com/documentation/systemconfiguration/1516925-scnetworkinterfacegethardwareadd)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkInterfaceGetHardwareAddressString (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkInterfaceGetHardwareAddressString (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetInterface()](https://developer.apple.com/documentation/systemconfiguration/1517296-scnetworkinterfacegetinterface)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkInterfaceRef SCNetworkInterfaceGetInterface (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` SCNetworkInterfaceRef _Nullable SCNetworkInterfaceGetInterface (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetInterfaceType()](https://developer.apple.com/documentation/systemconfiguration/1517371-scnetworkinterfacegetinterfacety)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkInterfaceGetInterfaceType (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkInterfaceGetInterfaceType (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetLocalizedDisplayName()](https://developer.apple.com/documentation/systemconfiguration/1517060-scnetworkinterfacegetlocalizeddi)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkInterfaceGetLocalizedDisplayName (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkInterfaceGetLocalizedDisplayName (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetSupportedInterfaceTypes()](https://developer.apple.com/documentation/systemconfiguration/1517339-scnetworkinterfacegetsupportedin)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkInterfaceGetSupportedInterfaceTypes (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkInterfaceGetSupportedInterfaceTypes (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceGetSupportedProtocolTypes()](https://developer.apple.com/documentation/systemconfiguration/1516844-scnetworkinterfacegetsupportedpr)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkInterfaceGetSupportedProtocolTypes (     SCNetworkInterfaceRef interface ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkInterfaceGetSupportedProtocolTypes (     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkInterfaceSetConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1517082-scnetworkinterfacesetconfigurati)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceSetConfiguration (     SCNetworkInterfaceRef interface,     CFDictionaryRef config ); ``` |
| To | ``` Boolean SCNetworkInterfaceSetConfiguration (     SCNetworkInterfaceRef _Nonnull interface,     CFDictionaryRef _Nonnull config ); ``` |

Modified [SCNetworkInterfaceSetExtendedConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1517295-scnetworkinterfacesetextendedcon)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceSetExtendedConfiguration (     SCNetworkInterfaceRef interface,     CFStringRef extendedType,     CFDictionaryRef config ); ``` |
| To | ``` Boolean SCNetworkInterfaceSetExtendedConfiguration (     SCNetworkInterfaceRef _Nonnull interface,     CFStringRef _Nonnull extendedType,     CFDictionaryRef _Nonnull config ); ``` |

Modified [SCNetworkInterfaceSetMediaOptions()](https://developer.apple.com/documentation/systemconfiguration/1516832-scnetworkinterfacesetmediaoption)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceSetMediaOptions (     SCNetworkInterfaceRef interface,     CFStringRef subtype,     CFArrayRef options ); ``` |
| To | ``` Boolean SCNetworkInterfaceSetMediaOptions (     SCNetworkInterfaceRef _Nonnull interface,     CFStringRef _Nonnull subtype,     CFArrayRef _Nonnull options ); ``` |

Modified [SCNetworkInterfaceSetMTU()](https://developer.apple.com/documentation/systemconfiguration/1517131-scnetworkinterfacesetmtu)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkInterfaceSetMTU (     SCNetworkInterfaceRef interface,     int mtu ); ``` |
| To | ``` Boolean SCNetworkInterfaceSetMTU (     SCNetworkInterfaceRef _Nonnull interface,     int mtu ); ``` |

Modified [SCNetworkProtocolGetConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1517352-scnetworkprotocolgetconfiguratio)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCNetworkProtocolGetConfiguration (     SCNetworkProtocolRef protocol ); ``` |
| To | ``` CFDictionaryRef _Nullable SCNetworkProtocolGetConfiguration (     SCNetworkProtocolRef _Nonnull protocol ); ``` |

Modified [SCNetworkProtocolGetEnabled()](https://developer.apple.com/documentation/systemconfiguration/1517299-scnetworkprotocolgetenabled)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkProtocolGetEnabled (     SCNetworkProtocolRef protocol ); ``` |
| To | ``` Boolean SCNetworkProtocolGetEnabled (     SCNetworkProtocolRef _Nonnull protocol ); ``` |

Modified [SCNetworkProtocolGetProtocolType()](https://developer.apple.com/documentation/systemconfiguration/1517302-scnetworkprotocolgetprotocoltype)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkProtocolGetProtocolType (     SCNetworkProtocolRef protocol ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkProtocolGetProtocolType (     SCNetworkProtocolRef _Nonnull protocol ); ``` |

Modified [SCNetworkProtocolSetConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1517188-scnetworkprotocolsetconfiguratio)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkProtocolSetConfiguration (     SCNetworkProtocolRef protocol,     CFDictionaryRef config ); ``` |
| To | ``` Boolean SCNetworkProtocolSetConfiguration (     SCNetworkProtocolRef _Nonnull protocol,     CFDictionaryRef _Nonnull config ); ``` |

Modified [SCNetworkProtocolSetEnabled()](https://developer.apple.com/documentation/systemconfiguration/1517366-scnetworkprotocolsetenabled)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkProtocolSetEnabled (     SCNetworkProtocolRef protocol,     Boolean enabled ); ``` |
| To | ``` Boolean SCNetworkProtocolSetEnabled (     SCNetworkProtocolRef _Nonnull protocol,     Boolean enabled ); ``` |

Modified [SCNetworkServiceAddProtocolType()](https://developer.apple.com/documentation/systemconfiguration/1516894-scnetworkserviceaddprotocoltype)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceAddProtocolType (     SCNetworkServiceRef service,     CFStringRef protocolType ); ``` |
| To | ``` Boolean SCNetworkServiceAddProtocolType (     SCNetworkServiceRef _Nonnull service,     CFStringRef _Nonnull protocolType ); ``` |

Modified [SCNetworkServiceCopy()](https://developer.apple.com/documentation/systemconfiguration/1516864-scnetworkservicecopy)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkServiceRef SCNetworkServiceCopy (     SCPreferencesRef prefs,     CFStringRef serviceID ); ``` |
| To | ``` SCNetworkServiceRef _Nullable SCNetworkServiceCopy (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull serviceID ); ``` |

Modified [SCNetworkServiceCopyAll()](https://developer.apple.com/documentation/systemconfiguration/1516810-scnetworkservicecopyall)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkServiceCopyAll (     SCPreferencesRef prefs ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkServiceCopyAll (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCNetworkServiceCopyProtocol()](https://developer.apple.com/documentation/systemconfiguration/1517290-scnetworkservicecopyprotocol)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkProtocolRef SCNetworkServiceCopyProtocol (     SCNetworkServiceRef service,     CFStringRef protocolType ); ``` |
| To | ``` SCNetworkProtocolRef _Nullable SCNetworkServiceCopyProtocol (     SCNetworkServiceRef _Nonnull service,     CFStringRef _Nonnull protocolType ); ``` |

Modified [SCNetworkServiceCopyProtocols()](https://developer.apple.com/documentation/systemconfiguration/1517200-scnetworkservicecopyprotocols)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkServiceCopyProtocols (     SCNetworkServiceRef service ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkServiceCopyProtocols (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceCreate()](https://developer.apple.com/documentation/systemconfiguration/1517139-scnetworkservicecreate)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkServiceRef SCNetworkServiceCreate (     SCPreferencesRef prefs,     SCNetworkInterfaceRef interface ); ``` |
| To | ``` SCNetworkServiceRef _Nullable SCNetworkServiceCreate (     SCPreferencesRef _Nonnull prefs,     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkServiceEstablishDefaultConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1517016-scnetworkserviceestablishdefault)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceEstablishDefaultConfiguration (     SCNetworkServiceRef service ); ``` |
| To | ``` Boolean SCNetworkServiceEstablishDefaultConfiguration (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceGetEnabled()](https://developer.apple.com/documentation/systemconfiguration/1517075-scnetworkservicegetenabled)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceGetEnabled (     SCNetworkServiceRef service ); ``` |
| To | ``` Boolean SCNetworkServiceGetEnabled (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceGetInterface()](https://developer.apple.com/documentation/systemconfiguration/1516724-scnetworkservicegetinterface)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkInterfaceRef SCNetworkServiceGetInterface (     SCNetworkServiceRef service ); ``` |
| To | ``` SCNetworkInterfaceRef _Nullable SCNetworkServiceGetInterface (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceGetName()](https://developer.apple.com/documentation/systemconfiguration/1516819-scnetworkservicegetname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkServiceGetName (     SCNetworkServiceRef service ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkServiceGetName (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceGetServiceID()](https://developer.apple.com/documentation/systemconfiguration/1516965-scnetworkservicegetserviceid)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkServiceGetServiceID (     SCNetworkServiceRef service ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkServiceGetServiceID (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceRemove()](https://developer.apple.com/documentation/systemconfiguration/1517177-scnetworkserviceremove)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceRemove (     SCNetworkServiceRef service ); ``` |
| To | ``` Boolean SCNetworkServiceRemove (     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkServiceRemoveProtocolType()](https://developer.apple.com/documentation/systemconfiguration/1517073-scnetworkserviceremoveprotocolty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceRemoveProtocolType (     SCNetworkServiceRef service,     CFStringRef protocolType ); ``` |
| To | ``` Boolean SCNetworkServiceRemoveProtocolType (     SCNetworkServiceRef _Nonnull service,     CFStringRef _Nonnull protocolType ); ``` |

Modified [SCNetworkServiceSetEnabled()](https://developer.apple.com/documentation/systemconfiguration/1517240-scnetworkservicesetenabled)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceSetEnabled (     SCNetworkServiceRef service,     Boolean enabled ); ``` |
| To | ``` Boolean SCNetworkServiceSetEnabled (     SCNetworkServiceRef _Nonnull service,     Boolean enabled ); ``` |

Modified [SCNetworkServiceSetName()](https://developer.apple.com/documentation/systemconfiguration/1516988-scnetworkservicesetname)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkServiceSetName (     SCNetworkServiceRef service,     CFStringRef name ); ``` |
| To | ``` Boolean SCNetworkServiceSetName (     SCNetworkServiceRef _Nonnull service,     CFStringRef _Nonnull name ); ``` |

Modified [SCNetworkSetAddService()](https://developer.apple.com/documentation/systemconfiguration/1516707-scnetworksetaddservice)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetAddService (     SCNetworkSetRef set,     SCNetworkServiceRef service ); ``` |
| To | ``` Boolean SCNetworkSetAddService (     SCNetworkSetRef _Nonnull set,     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkSetContainsInterface()](https://developer.apple.com/documentation/systemconfiguration/1516672-scnetworksetcontainsinterface)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetContainsInterface (     SCNetworkSetRef set,     SCNetworkInterfaceRef interface ); ``` |
| To | ``` Boolean SCNetworkSetContainsInterface (     SCNetworkSetRef _Nonnull set,     SCNetworkInterfaceRef _Nonnull interface ); ``` |

Modified [SCNetworkSetCopy()](https://developer.apple.com/documentation/systemconfiguration/1517107-scnetworksetcopy)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkSetRef SCNetworkSetCopy (     SCPreferencesRef prefs,     CFStringRef setID ); ``` |
| To | ``` SCNetworkSetRef _Nullable SCNetworkSetCopy (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull setID ); ``` |

Modified [SCNetworkSetCopyAll()](https://developer.apple.com/documentation/systemconfiguration/1517220-scnetworksetcopyall)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkSetCopyAll (     SCPreferencesRef prefs ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkSetCopyAll (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCNetworkSetCopyCurrent()](https://developer.apple.com/documentation/systemconfiguration/1517183-scnetworksetcopycurrent)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkSetRef SCNetworkSetCopyCurrent (     SCPreferencesRef prefs ); ``` |
| To | ``` SCNetworkSetRef _Nullable SCNetworkSetCopyCurrent (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCNetworkSetCopyServices()](https://developer.apple.com/documentation/systemconfiguration/1517085-scnetworksetcopyservices)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkSetCopyServices (     SCNetworkSetRef set ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkSetCopyServices (     SCNetworkSetRef _Nonnull set ); ``` |

Modified [SCNetworkSetCreate()](https://developer.apple.com/documentation/systemconfiguration/1517084-scnetworksetcreate)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkSetRef SCNetworkSetCreate (     SCPreferencesRef prefs ); ``` |
| To | ``` SCNetworkSetRef _Nullable SCNetworkSetCreate (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCNetworkSetGetName()](https://developer.apple.com/documentation/systemconfiguration/1516847-scnetworksetgetname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkSetGetName (     SCNetworkSetRef set ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkSetGetName (     SCNetworkSetRef _Nonnull set ); ``` |

Modified [SCNetworkSetGetServiceOrder()](https://developer.apple.com/documentation/systemconfiguration/1516892-scnetworksetgetserviceorder)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCNetworkSetGetServiceOrder (     SCNetworkSetRef set ); ``` |
| To | ``` CFArrayRef _Nullable SCNetworkSetGetServiceOrder (     SCNetworkSetRef _Nonnull set ); ``` |

Modified [SCNetworkSetGetSetID()](https://developer.apple.com/documentation/systemconfiguration/1516940-scnetworksetgetsetid)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkSetGetSetID (     SCNetworkSetRef set ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkSetGetSetID (     SCNetworkSetRef _Nonnull set ); ``` |

Modified [SCNetworkSetRemove()](https://developer.apple.com/documentation/systemconfiguration/1517202-scnetworksetremove)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetRemove (     SCNetworkSetRef set ); ``` |
| To | ``` Boolean SCNetworkSetRemove (     SCNetworkSetRef _Nonnull set ); ``` |

Modified [SCNetworkSetRemoveService()](https://developer.apple.com/documentation/systemconfiguration/1517325-scnetworksetremoveservice)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetRemoveService (     SCNetworkSetRef set,     SCNetworkServiceRef service ); ``` |
| To | ``` Boolean SCNetworkSetRemoveService (     SCNetworkSetRef _Nonnull set,     SCNetworkServiceRef _Nonnull service ); ``` |

Modified [SCNetworkSetSetCurrent()](https://developer.apple.com/documentation/systemconfiguration/1516959-scnetworksetsetcurrent)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetSetCurrent (     SCNetworkSetRef set ); ``` |
| To | ``` Boolean SCNetworkSetSetCurrent (     SCNetworkSetRef _Nonnull set ); ``` |

Modified [SCNetworkSetSetName()](https://developer.apple.com/documentation/systemconfiguration/1517309-scnetworksetsetname)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetSetName (     SCNetworkSetRef set,     CFStringRef name ); ``` |
| To | ``` Boolean SCNetworkSetSetName (     SCNetworkSetRef _Nonnull set,     CFStringRef _Nonnull name ); ``` |

Modified [SCNetworkSetSetServiceOrder()](https://developer.apple.com/documentation/systemconfiguration/1516839-scnetworksetsetserviceorder)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkSetSetServiceOrder (     SCNetworkSetRef set,     CFArrayRef newOrder ); ``` |
| To | ``` Boolean SCNetworkSetSetServiceOrder (     SCNetworkSetRef _Nonnull set,     CFArrayRef _Nonnull newOrder ); ``` |

Modified [SCVLANInterfaceCopyAll()](https://developer.apple.com/documentation/systemconfiguration/1517029-scvlaninterfacecopyall)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCVLANInterfaceCopyAll (     SCPreferencesRef prefs ); ``` |
| To | ``` CFArrayRef _Nonnull SCVLANInterfaceCopyAll (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCVLANInterfaceCopyAvailablePhysicalInterfaces()](https://developer.apple.com/documentation/systemconfiguration/1517211-scvlaninterfacecopyavailablephys)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCVLANInterfaceCopyAvailablePhysicalInterfaces (     void ); ``` |
| To | ``` CFArrayRef _Nonnull SCVLANInterfaceCopyAvailablePhysicalInterfaces (     void ); ``` |

Modified [SCVLANInterfaceCreate()](https://developer.apple.com/documentation/systemconfiguration/1517209-scvlaninterfacecreate)

|  | Declaration |
| --- | --- |
| From | ``` SCVLANInterfaceRef SCVLANInterfaceCreate (     SCPreferencesRef prefs,     SCNetworkInterfaceRef physical,     CFNumberRef tag ); ``` |
| To | ``` SCVLANInterfaceRef _Nullable SCVLANInterfaceCreate (     SCPreferencesRef _Nonnull prefs,     SCNetworkInterfaceRef _Nonnull physical,     CFNumberRef _Nonnull tag ); ``` |

Modified [SCVLANInterfaceGetOptions()](https://developer.apple.com/documentation/systemconfiguration/1516719-scvlaninterfacegetoptions)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCVLANInterfaceGetOptions (     SCVLANInterfaceRef vlan ); ``` |
| To | ``` CFDictionaryRef _Nullable SCVLANInterfaceGetOptions (     SCVLANInterfaceRef _Nonnull vlan ); ``` |

Modified [SCVLANInterfaceGetPhysicalInterface()](https://developer.apple.com/documentation/systemconfiguration/1517233-scvlaninterfacegetphysicalinterf)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkInterfaceRef SCVLANInterfaceGetPhysicalInterface (     SCVLANInterfaceRef vlan ); ``` |
| To | ``` SCNetworkInterfaceRef _Nullable SCVLANInterfaceGetPhysicalInterface (     SCVLANInterfaceRef _Nonnull vlan ); ``` |

Modified [SCVLANInterfaceGetTag()](https://developer.apple.com/documentation/systemconfiguration/1517151-scvlaninterfacegettag)

|  | Declaration |
| --- | --- |
| From | ``` CFNumberRef SCVLANInterfaceGetTag (     SCVLANInterfaceRef vlan ); ``` |
| To | ``` CFNumberRef _Nullable SCVLANInterfaceGetTag (     SCVLANInterfaceRef _Nonnull vlan ); ``` |

Modified [SCVLANInterfaceRemove()](https://developer.apple.com/documentation/systemconfiguration/1516889-scvlaninterfaceremove)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCVLANInterfaceRemove (     SCVLANInterfaceRef vlan ); ``` |
| To | ``` Boolean SCVLANInterfaceRemove (     SCVLANInterfaceRef _Nonnull vlan ); ``` |

Modified [SCVLANInterfaceSetLocalizedDisplayName()](https://developer.apple.com/documentation/systemconfiguration/1516732-scvlaninterfacesetlocalizeddispl)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCVLANInterfaceSetLocalizedDisplayName (     SCVLANInterfaceRef vlan,     CFStringRef newName ); ``` |
| To | ``` Boolean SCVLANInterfaceSetLocalizedDisplayName (     SCVLANInterfaceRef _Nonnull vlan,     CFStringRef _Nonnull newName ); ``` |

Modified [SCVLANInterfaceSetOptions()](https://developer.apple.com/documentation/systemconfiguration/1516852-scvlaninterfacesetoptions)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCVLANInterfaceSetOptions (     SCVLANInterfaceRef vlan,     CFDictionaryRef newOptions ); ``` |
| To | ``` Boolean SCVLANInterfaceSetOptions (     SCVLANInterfaceRef _Nonnull vlan,     CFDictionaryRef _Nonnull newOptions ); ``` |

Modified [SCVLANInterfaceSetPhysicalInterfaceAndTag()](https://developer.apple.com/documentation/systemconfiguration/1516754-scvlaninterfacesetphysicalinterf)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCVLANInterfaceSetPhysicalInterfaceAndTag (     SCVLANInterfaceRef vlan,     SCNetworkInterfaceRef physical,     CFNumberRef tag ); ``` |
| To | ``` Boolean SCVLANInterfaceSetPhysicalInterfaceAndTag (     SCVLANInterfaceRef _Nonnull vlan,     SCNetworkInterfaceRef _Nonnull physical,     CFNumberRef _Nonnull tag ); ``` |

#### SCNetworkConnection.h

Modified [SCNetworkConnectionCopyExtendedStatus()](https://developer.apple.com/documentation/systemconfiguration/1393134-scnetworkconnectioncopyextendeds)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCNetworkConnectionCopyExtendedStatus (     SCNetworkConnectionRef connection ); ``` |
| To | ``` CFDictionaryRef _Nullable SCNetworkConnectionCopyExtendedStatus (     SCNetworkConnectionRef _Nonnull connection ); ``` |

Modified [SCNetworkConnectionCopyServiceID()](https://developer.apple.com/documentation/systemconfiguration/1393167-scnetworkconnectioncopyserviceid)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCNetworkConnectionCopyServiceID (     SCNetworkConnectionRef connection ); ``` |
| To | ``` CFStringRef _Nullable SCNetworkConnectionCopyServiceID (     SCNetworkConnectionRef _Nonnull connection ); ``` |

Modified [SCNetworkConnectionCopyStatistics()](https://developer.apple.com/documentation/systemconfiguration/1393147-scnetworkconnectioncopystatistic)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCNetworkConnectionCopyStatistics (     SCNetworkConnectionRef connection ); ``` |
| To | ``` CFDictionaryRef _Nullable SCNetworkConnectionCopyStatistics (     SCNetworkConnectionRef _Nonnull connection ); ``` |

Modified [SCNetworkConnectionCopyUserOptions()](https://developer.apple.com/documentation/systemconfiguration/1393128-scnetworkconnectioncopyuseroptio)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCNetworkConnectionCopyUserOptions (     SCNetworkConnectionRef connection ); ``` |
| To | ``` CFDictionaryRef _Nullable SCNetworkConnectionCopyUserOptions (     SCNetworkConnectionRef _Nonnull connection ); ``` |

Modified [SCNetworkConnectionCopyUserPreferences()](https://developer.apple.com/documentation/systemconfiguration/1393114-scnetworkconnectioncopyuserprefe)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkConnectionCopyUserPreferences (     CFDictionaryRef selectionOptions,     CFStringRef *serviceID,     CFDictionaryRef *userOptions ); ``` |
| To | ``` Boolean SCNetworkConnectionCopyUserPreferences (     CFDictionaryRef _Nullable selectionOptions,     CFStringRef  _Nonnull * _Nullable serviceID,     CFDictionaryRef  _Nonnull * _Nullable userOptions ); ``` |

Modified [SCNetworkConnectionCreateWithServiceID()](https://developer.apple.com/documentation/systemconfiguration/1393175-scnetworkconnectioncreatewithser)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkConnectionRef SCNetworkConnectionCreateWithServiceID (     CFAllocatorRef allocator,     CFStringRef serviceID,     SCNetworkConnectionCallBack callout,     SCNetworkConnectionContext *context ); ``` |
| To | ``` SCNetworkConnectionRef _Nullable SCNetworkConnectionCreateWithServiceID (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull serviceID,     SCNetworkConnectionCallBack _Nullable callout,     SCNetworkConnectionContext * _Nullable context ); ``` |

Modified [SCNetworkConnectionGetStatus()](https://developer.apple.com/documentation/systemconfiguration/1393096-scnetworkconnectiongetstatus)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkConnectionStatus SCNetworkConnectionGetStatus (     SCNetworkConnectionRef connection ); ``` |
| To | ``` SCNetworkConnectionStatus SCNetworkConnectionGetStatus (     SCNetworkConnectionRef _Nonnull connection ); ``` |

Modified [SCNetworkConnectionScheduleWithRunLoop()](https://developer.apple.com/documentation/systemconfiguration/1393120-scnetworkconnectionschedulewithr)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkConnectionScheduleWithRunLoop (     SCNetworkConnectionRef connection,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` Boolean SCNetworkConnectionScheduleWithRunLoop (     SCNetworkConnectionRef _Nonnull connection,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [SCNetworkConnectionSetDispatchQueue()](https://developer.apple.com/documentation/systemconfiguration/1393138-scnetworkconnectionsetdispatchqu)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkConnectionSetDispatchQueue (     SCNetworkConnectionRef connection,     dispatch_queue_t queue ); ``` |
| To | ``` Boolean SCNetworkConnectionSetDispatchQueue (     SCNetworkConnectionRef _Nonnull connection,     dispatch_queue_t _Nullable queue ); ``` |

Modified [SCNetworkConnectionStart()](https://developer.apple.com/documentation/systemconfiguration/1393183-scnetworkconnectionstart)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkConnectionStart (     SCNetworkConnectionRef connection,     CFDictionaryRef userOptions,     Boolean linger ); ``` |
| To | ``` Boolean SCNetworkConnectionStart (     SCNetworkConnectionRef _Nonnull connection,     CFDictionaryRef _Nullable userOptions,     Boolean linger ); ``` |

Modified [SCNetworkConnectionStop()](https://developer.apple.com/documentation/systemconfiguration/1393169-scnetworkconnectionstop)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkConnectionStop (     SCNetworkConnectionRef connection,     Boolean forceDisconnect ); ``` |
| To | ``` Boolean SCNetworkConnectionStop (     SCNetworkConnectionRef _Nonnull connection,     Boolean forceDisconnect ); ``` |

Modified [SCNetworkConnectionUnscheduleFromRunLoop()](https://developer.apple.com/documentation/systemconfiguration/1393151-scnetworkconnectionunschedulefro)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkConnectionUnscheduleFromRunLoop (     SCNetworkConnectionRef connection,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` Boolean SCNetworkConnectionUnscheduleFromRunLoop (     SCNetworkConnectionRef _Nonnull connection,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### SCNetworkReachability.h

Modified [SCNetworkReachabilityCreateWithAddress()](https://developer.apple.com/documentation/systemconfiguration/1514895-scnetworkreachabilitycreatewitha)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkReachabilityRef SCNetworkReachabilityCreateWithAddress (     CFAllocatorRef allocator,     const struct sockaddr *address ); ``` |
| To | ``` SCNetworkReachabilityRef _Nullable SCNetworkReachabilityCreateWithAddress (     CFAllocatorRef _Nullable allocator,     const struct sockaddr * _Nonnull address ); ``` |

Modified [SCNetworkReachabilityCreateWithAddressPair()](https://developer.apple.com/documentation/systemconfiguration/1514908-scnetworkreachabilitycreatewitha)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkReachabilityRef SCNetworkReachabilityCreateWithAddressPair (     CFAllocatorRef allocator,     const struct sockaddr *localAddress,     const struct sockaddr *remoteAddress ); ``` |
| To | ``` SCNetworkReachabilityRef _Nullable SCNetworkReachabilityCreateWithAddressPair (     CFAllocatorRef _Nullable allocator,     const struct sockaddr * _Nullable localAddress,     const struct sockaddr * _Nullable remoteAddress ); ``` |

Modified [SCNetworkReachabilityCreateWithName()](https://developer.apple.com/documentation/systemconfiguration/1514904-scnetworkreachabilitycreatewithn)

|  | Declaration |
| --- | --- |
| From | ``` SCNetworkReachabilityRef SCNetworkReachabilityCreateWithName (     CFAllocatorRef allocator,     const char *nodename ); ``` |
| To | ``` SCNetworkReachabilityRef _Nullable SCNetworkReachabilityCreateWithName (     CFAllocatorRef _Nullable allocator,     const char * _Nonnull nodename ); ``` |

Modified [SCNetworkReachabilityGetFlags()](https://developer.apple.com/documentation/systemconfiguration/1514924-scnetworkreachabilitygetflags)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkReachabilityGetFlags (     SCNetworkReachabilityRef target,     SCNetworkReachabilityFlags *flags ); ``` |
| To | ``` Boolean SCNetworkReachabilityGetFlags (     SCNetworkReachabilityRef _Nonnull target,     SCNetworkReachabilityFlags * _Nonnull flags ); ``` |

Modified [SCNetworkReachabilityScheduleWithRunLoop()](https://developer.apple.com/documentation/systemconfiguration/1514894-scnetworkreachabilityschedulewit)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkReachabilityScheduleWithRunLoop (     SCNetworkReachabilityRef target,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` Boolean SCNetworkReachabilityScheduleWithRunLoop (     SCNetworkReachabilityRef _Nonnull target,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [SCNetworkReachabilitySetCallback()](https://developer.apple.com/documentation/systemconfiguration/1514903-scnetworkreachabilitysetcallback)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkReachabilitySetCallback (     SCNetworkReachabilityRef target,     SCNetworkReachabilityCallBack callout,     SCNetworkReachabilityContext *context ); ``` |
| To | ``` Boolean SCNetworkReachabilitySetCallback (     SCNetworkReachabilityRef _Nonnull target,     SCNetworkReachabilityCallBack _Nullable callout,     SCNetworkReachabilityContext * _Nullable context ); ``` |

Modified [SCNetworkReachabilitySetDispatchQueue()](https://developer.apple.com/documentation/systemconfiguration/1514911-scnetworkreachabilitysetdispatch)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkReachabilitySetDispatchQueue (     SCNetworkReachabilityRef target,     dispatch_queue_t queue ); ``` |
| To | ``` Boolean SCNetworkReachabilitySetDispatchQueue (     SCNetworkReachabilityRef _Nonnull target,     dispatch_queue_t _Nullable queue ); ``` |

Modified [SCNetworkReachabilityUnscheduleFromRunLoop()](https://developer.apple.com/documentation/systemconfiguration/1514899-scnetworkreachabilityunschedulef)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCNetworkReachabilityUnscheduleFromRunLoop (     SCNetworkReachabilityRef target,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` Boolean SCNetworkReachabilityUnscheduleFromRunLoop (     SCNetworkReachabilityRef _Nonnull target,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### SCPreferences.h

Modified [SCPreferencesAddValue()](https://developer.apple.com/documentation/systemconfiguration/1517178-scpreferencesaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesAddValue (     SCPreferencesRef prefs,     CFStringRef key,     CFPropertyListRef value ); ``` |
| To | ``` Boolean SCPreferencesAddValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull key,     CFPropertyListRef _Nonnull value ); ``` |

Modified [SCPreferencesApplyChanges()](https://developer.apple.com/documentation/systemconfiguration/1517125-scpreferencesapplychanges)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesApplyChanges (     SCPreferencesRef prefs ); ``` |
| To | ``` Boolean SCPreferencesApplyChanges (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCPreferencesCommitChanges()](https://developer.apple.com/documentation/systemconfiguration/1517333-scpreferencescommitchanges)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesCommitChanges (     SCPreferencesRef prefs ); ``` |
| To | ``` Boolean SCPreferencesCommitChanges (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCPreferencesCopyKeyList()](https://developer.apple.com/documentation/systemconfiguration/1517058-scpreferencescopykeylist)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SCPreferencesCopyKeyList (     SCPreferencesRef prefs ); ``` |
| To | ``` CFArrayRef _Nullable SCPreferencesCopyKeyList (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCPreferencesCreate()](https://developer.apple.com/documentation/systemconfiguration/1516807-scpreferencescreate)

|  | Declaration |
| --- | --- |
| From | ``` SCPreferencesRef SCPreferencesCreate (     CFAllocatorRef allocator,     CFStringRef name,     CFStringRef prefsID ); ``` |
| To | ``` SCPreferencesRef _Nullable SCPreferencesCreate (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull name,     CFStringRef _Nullable prefsID ); ``` |

Modified [SCPreferencesCreateWithAuthorization()](https://developer.apple.com/documentation/systemconfiguration/1516686-scpreferencescreatewithauthoriza)

|  | Declaration |
| --- | --- |
| From | ``` SCPreferencesRef SCPreferencesCreateWithAuthorization (     CFAllocatorRef allocator,     CFStringRef name,     CFStringRef prefsID,     AuthorizationRef authorization ); ``` |
| To | ``` SCPreferencesRef _Nullable SCPreferencesCreateWithAuthorization (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull name,     CFStringRef _Nullable prefsID,     AuthorizationRef _Nullable authorization ); ``` |

Modified [SCPreferencesGetSignature()](https://developer.apple.com/documentation/systemconfiguration/1517004-scpreferencesgetsignature)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SCPreferencesGetSignature (     SCPreferencesRef prefs ); ``` |
| To | ``` CFDataRef _Nullable SCPreferencesGetSignature (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCPreferencesGetValue()](https://developer.apple.com/documentation/systemconfiguration/1517189-scpreferencesgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` CFPropertyListRef SCPreferencesGetValue (     SCPreferencesRef prefs,     CFStringRef key ); ``` |
| To | ``` CFPropertyListRef _Nullable SCPreferencesGetValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull key ); ``` |

Modified [SCPreferencesLock()](https://developer.apple.com/documentation/systemconfiguration/1517297-scpreferenceslock)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesLock (     SCPreferencesRef prefs,     Boolean wait ); ``` |
| To | ``` Boolean SCPreferencesLock (     SCPreferencesRef _Nonnull prefs,     Boolean wait ); ``` |

Modified [SCPreferencesRemoveValue()](https://developer.apple.com/documentation/systemconfiguration/1516723-scpreferencesremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesRemoveValue (     SCPreferencesRef prefs,     CFStringRef key ); ``` |
| To | ``` Boolean SCPreferencesRemoveValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull key ); ``` |

Modified [SCPreferencesScheduleWithRunLoop()](https://developer.apple.com/documentation/systemconfiguration/1516901-scpreferencesschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesScheduleWithRunLoop (     SCPreferencesRef prefs,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` Boolean SCPreferencesScheduleWithRunLoop (     SCPreferencesRef _Nonnull prefs,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [SCPreferencesSetCallback()](https://developer.apple.com/documentation/systemconfiguration/1517094-scpreferencessetcallback)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesSetCallback (     SCPreferencesRef prefs,     SCPreferencesCallBack callout,     SCPreferencesContext *context ); ``` |
| To | ``` Boolean SCPreferencesSetCallback (     SCPreferencesRef _Nonnull prefs,     SCPreferencesCallBack _Nullable callout,     SCPreferencesContext * _Nullable context ); ``` |

Modified [SCPreferencesSetDispatchQueue()](https://developer.apple.com/documentation/systemconfiguration/1517050-scpreferencessetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesSetDispatchQueue (     SCPreferencesRef prefs,     dispatch_queue_t queue ); ``` |
| To | ``` Boolean SCPreferencesSetDispatchQueue (     SCPreferencesRef _Nonnull prefs,     dispatch_queue_t _Nullable queue ); ``` |

Modified [SCPreferencesSetValue()](https://developer.apple.com/documentation/systemconfiguration/1517225-scpreferencessetvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesSetValue (     SCPreferencesRef prefs,     CFStringRef key,     CFPropertyListRef value ); ``` |
| To | ``` Boolean SCPreferencesSetValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull key,     CFPropertyListRef _Nonnull value ); ``` |

Modified [SCPreferencesSynchronize()](https://developer.apple.com/documentation/systemconfiguration/1517260-scpreferencessynchronize)

|  | Declaration |
| --- | --- |
| From | ``` void SCPreferencesSynchronize (     SCPreferencesRef prefs ); ``` |
| To | ``` void SCPreferencesSynchronize (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCPreferencesUnlock()](https://developer.apple.com/documentation/systemconfiguration/1517230-scpreferencesunlock)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesUnlock (     SCPreferencesRef prefs ); ``` |
| To | ``` Boolean SCPreferencesUnlock (     SCPreferencesRef _Nonnull prefs ); ``` |

Modified [SCPreferencesUnscheduleFromRunLoop()](https://developer.apple.com/documentation/systemconfiguration/1516711-scpreferencesunschedulefromrunlo)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesUnscheduleFromRunLoop (     SCPreferencesRef prefs,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` Boolean SCPreferencesUnscheduleFromRunLoop (     SCPreferencesRef _Nonnull prefs,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### SCPreferencesPath.h

Modified [SCPreferencesPathCreateUniqueChild()](https://developer.apple.com/documentation/systemconfiguration/1516713-scpreferencespathcreateuniquechi)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCPreferencesPathCreateUniqueChild (     SCPreferencesRef prefs,     CFStringRef prefix ); ``` |
| To | ``` CFStringRef _Nullable SCPreferencesPathCreateUniqueChild (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull prefix ); ``` |

Modified [SCPreferencesPathGetLink()](https://developer.apple.com/documentation/systemconfiguration/1516712-scpreferencespathgetlink)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SCPreferencesPathGetLink (     SCPreferencesRef prefs,     CFStringRef path ); ``` |
| To | ``` CFStringRef _Nullable SCPreferencesPathGetLink (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull path ); ``` |

Modified [SCPreferencesPathGetValue()](https://developer.apple.com/documentation/systemconfiguration/1516904-scpreferencespathgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SCPreferencesPathGetValue (     SCPreferencesRef prefs,     CFStringRef path ); ``` |
| To | ``` CFDictionaryRef _Nullable SCPreferencesPathGetValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull path ); ``` |

Modified [SCPreferencesPathRemoveValue()](https://developer.apple.com/documentation/systemconfiguration/1517268-scpreferencespathremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesPathRemoveValue (     SCPreferencesRef prefs,     CFStringRef path ); ``` |
| To | ``` Boolean SCPreferencesPathRemoveValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull path ); ``` |

Modified [SCPreferencesPathSetLink()](https://developer.apple.com/documentation/systemconfiguration/1517244-scpreferencespathsetlink)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesPathSetLink (     SCPreferencesRef prefs,     CFStringRef path,     CFStringRef link ); ``` |
| To | ``` Boolean SCPreferencesPathSetLink (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull path,     CFStringRef _Nonnull link ); ``` |

Modified [SCPreferencesPathSetValue()](https://developer.apple.com/documentation/systemconfiguration/1517271-scpreferencespathsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesPathSetValue (     SCPreferencesRef prefs,     CFStringRef path,     CFDictionaryRef value ); ``` |
| To | ``` Boolean SCPreferencesPathSetValue (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull path,     CFDictionaryRef _Nonnull value ); ``` |

#### SCPreferencesSetSpecific.h

Modified [SCPreferencesSetComputerName()](https://developer.apple.com/documentation/systemconfiguration/1516772-scpreferencessetcomputername)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesSetComputerName (     SCPreferencesRef prefs,     CFStringRef name,     CFStringEncoding nameEncoding ); ``` |
| To | ``` Boolean SCPreferencesSetComputerName (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull name,     CFStringEncoding nameEncoding ); ``` |

Modified [SCPreferencesSetLocalHostName()](https://developer.apple.com/documentation/systemconfiguration/1516945-scpreferencessetlocalhostname)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SCPreferencesSetLocalHostName (     SCPreferencesRef prefs,     CFStringRef name ); ``` |
| To | ``` Boolean SCPreferencesSetLocalHostName (     SCPreferencesRef _Nonnull prefs,     CFStringRef _Nonnull name ); ``` |

#### SystemConfiguration.h

Modified [SCCopyLastError()](https://developer.apple.com/documentation/systemconfiguration/1517326-sccopylasterror)

|  | Declaration |
| --- | --- |
| From | ``` CFErrorRef SCCopyLastError (     void ); ``` |
| To | ``` CFErrorRef _Nonnull SCCopyLastError (     void ); ``` |

Modified [SCErrorString()](https://developer.apple.com/documentation/systemconfiguration/1516776-scerrorstring)

|  | Declaration |
| --- | --- |
| From | ``` const char * SCErrorString (     int status ); ``` |
| To | ``` const char * _Nonnull SCErrorString (     int status ); ``` |

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
