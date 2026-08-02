---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreWLAN.html
archived_at: '2026-07-18T02:53:01.503349Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreWLAN Changes for Objective-C

### CoreWLAN

#### CoreWLANUtil.h

Modified [CWKeychainCopyEAPIdentity()](https://developer.apple.com/documentation/corewlan/1569166-cwkeychaincopyeapidentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainCopyEAPIdentity (     CFDataRef ssidData,     SecIdentityRef *identity ); ``` |
| To | ``` OSStatus CWKeychainCopyEAPIdentity (     CFDataRef _Nonnull ssidData,     SecIdentityRef  _Nullable * _Nullable identity ); ``` |

Modified [CWKeychainCopyEAPIdentityList()](https://developer.apple.com/documentation/corewlan/1512258-cwkeychaincopyeapidentitylist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainCopyEAPIdentityList (     CFArrayRef *list ); ``` |
| To | ``` OSStatus CWKeychainCopyEAPIdentityList (     CFArrayRef  _Nullable * _Nullable list ); ``` |

Modified [CWKeychainCopyEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569173-cwkeychaincopyeapusernameandpass)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainCopyEAPUsernameAndPassword (     CFDataRef ssidData,     CFStringRef *username,     CFStringRef *password ); ``` |
| To | ``` OSStatus CWKeychainCopyEAPUsernameAndPassword (     CFDataRef _Nonnull ssidData,     CFStringRef  _Nullable * _Nullable username,     CFStringRef  _Nullable * _Nullable password ); ``` |

Modified [CWKeychainCopyPassword()](https://developer.apple.com/documentation/corewlan/1569169-cwkeychaincopypassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainCopyPassword (     CFDataRef ssidData,     CFStringRef *password ); ``` |
| To | ``` OSStatus CWKeychainCopyPassword (     CFDataRef _Nonnull ssidData,     CFStringRef  _Nullable * _Nullable password ); ``` |

Modified [CWKeychainCopyWiFiEAPIdentity()](https://developer.apple.com/documentation/corewlan/1512372-cwkeychaincopywifieapidentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainCopyWiFiEAPIdentity (     CWKeychainDomain domain,     NSData *ssid,     SecIdentityRef *identity ); ``` |
| To | ``` OSStatus CWKeychainCopyWiFiEAPIdentity (     CWKeychainDomain domain,     NSData * _Nonnull ssid,     SecIdentityRef  _Nullable * _Nullable identity ); ``` |

Modified [CWKeychainDeleteEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569171-cwkeychaindeleteeapusernameandpa)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainDeleteEAPUsernameAndPassword (     CFDataRef ssidData ); ``` |
| To | ``` OSStatus CWKeychainDeleteEAPUsernameAndPassword (     CFDataRef _Nonnull ssidData ); ``` |

Modified [CWKeychainDeletePassword()](https://developer.apple.com/documentation/corewlan/1569170-cwkeychaindeletepassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainDeletePassword (     CFDataRef ssidData ); ``` |
| To | ``` OSStatus CWKeychainDeletePassword (     CFDataRef _Nonnull ssidData ); ``` |

Modified [CWKeychainDeleteWiFiEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1512239-cwkeychaindeletewifieapusernamea)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainDeleteWiFiEAPUsernameAndPassword (     CWKeychainDomain domain,     NSData *ssid ); ``` |
| To | ``` OSStatus CWKeychainDeleteWiFiEAPUsernameAndPassword (     CWKeychainDomain domain,     NSData * _Nonnull ssid ); ``` |

Modified [CWKeychainDeleteWiFiPassword()](https://developer.apple.com/documentation/corewlan/1512242-cwkeychaindeletewifipassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainDeleteWiFiPassword (     CWKeychainDomain domain,     NSData *ssid ); ``` |
| To | ``` OSStatus CWKeychainDeleteWiFiPassword (     CWKeychainDomain domain,     NSData * _Nonnull ssid ); ``` |

Modified [CWKeychainFindWiFiEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1512198-cwkeychainfindwifieapusernameand)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainFindWiFiEAPUsernameAndPassword (     CWKeychainDomain domain,     NSData *ssid,     NSString **username,     NSString **password ); ``` |
| To | ``` OSStatus CWKeychainFindWiFiEAPUsernameAndPassword (     CWKeychainDomain domain,     NSData * _Nonnull ssid,     NSString * _Nullable * _Nullable username,     NSString * _Nullable * _Nullable password ); ``` |

Modified [CWKeychainFindWiFiPassword()](https://developer.apple.com/documentation/corewlan/1512359-cwkeychainfindwifipassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainFindWiFiPassword (     CWKeychainDomain domain,     NSData *ssid,     NSString **password ); ``` |
| To | ``` OSStatus CWKeychainFindWiFiPassword (     CWKeychainDomain domain,     NSData * _Nonnull ssid,     NSString * _Nullable * _Nullable password ); ``` |

Modified [CWKeychainSetEAPIdentity()](https://developer.apple.com/documentation/corewlan/1569167-cwkeychainseteapidentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainSetEAPIdentity (     CFDataRef ssidData,     SecIdentityRef identity ); ``` |
| To | ``` OSStatus CWKeychainSetEAPIdentity (     CFDataRef _Nonnull ssidData,     SecIdentityRef _Nullable identity ); ``` |

Modified [CWKeychainSetEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569172-cwkeychainseteapusernameandpassw)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainSetEAPUsernameAndPassword (     CFDataRef ssidData,     CFStringRef username,     CFStringRef password ); ``` |
| To | ``` OSStatus CWKeychainSetEAPUsernameAndPassword (     CFDataRef _Nonnull ssidData,     CFStringRef _Nullable username,     CFStringRef _Nullable password ); ``` |

Modified [CWKeychainSetPassword()](https://developer.apple.com/documentation/corewlan/1569168-cwkeychainsetpassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainSetPassword (     CFDataRef ssidData,     CFStringRef password ); ``` |
| To | ``` OSStatus CWKeychainSetPassword (     CFDataRef _Nonnull ssidData,     CFStringRef _Nonnull password ); ``` |

Modified [CWKeychainSetWiFiEAPIdentity()](https://developer.apple.com/documentation/corewlan/1512453-cwkeychainsetwifieapidentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainSetWiFiEAPIdentity (     CWKeychainDomain domain,     NSData *ssid,     SecIdentityRef identity ); ``` |
| To | ``` OSStatus CWKeychainSetWiFiEAPIdentity (     CWKeychainDomain domain,     NSData * _Nonnull ssid,     SecIdentityRef _Nullable identity ); ``` |

Modified [CWKeychainSetWiFiEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1512305-cwkeychainsetwifieapusernameandp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainSetWiFiEAPUsernameAndPassword (     CWKeychainDomain domain,     NSData *ssid,     NSString *username,     NSString *password ); ``` |
| To | ``` OSStatus CWKeychainSetWiFiEAPUsernameAndPassword (     CWKeychainDomain domain,     NSData * _Nonnull ssid,     NSString * _Nullable username,     NSString * _Nullable password ); ``` |

Modified [CWKeychainSetWiFiPassword()](https://developer.apple.com/documentation/corewlan/1512429-cwkeychainsetwifipassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CWKeychainSetWiFiPassword (     CWKeychainDomain domain,     NSData *ssid,     NSString *password ); ``` |
| To | ``` OSStatus CWKeychainSetWiFiPassword (     CWKeychainDomain domain,     NSData * _Nonnull ssid,     NSString * _Nonnull password ); ``` |

Modified [CWMergeNetworks()](https://developer.apple.com/documentation/corewlan/1512230-cwmergenetworks)

|  | Declaration |
| --- | --- |
| From | ``` NSSet * CWMergeNetworks (     NSSet *networks ); ``` |
| To | ``` NSSet<CWNetwork *> * _Nonnull CWMergeNetworks (     NSSet<CWNetwork *> * _Nonnull networks ); ``` |

#### CWChannel.h

Modified [-[CWChannel isEqualToChannel:]](https://developer.apple.com/documentation/corewlan/cwchannel/1512390-isequaltochannel)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToChannel:(CWChannel *)channel ``` |
| To | ``` - (BOOL)isEqualToChannel:(CWChannel * _Nonnull)channel ``` |

#### CWConfiguration.h

Modified [+[CWConfiguration configuration]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507059-configuration)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)configuration ``` |
| To | ``` + (instancetype _Nonnull)configuration ``` |

Modified [+[CWConfiguration configurationWithConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507051-configurationwithconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)configurationWithConfiguration:(CWConfiguration *)configuration ``` |
| To | ``` + (instancetype _Nonnull)configurationWithConfiguration:(CWConfiguration * _Nonnull)configuration ``` |

Modified [-[CWConfiguration init]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507049-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CWConfiguration initWithConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507057-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithConfiguration:(CWConfiguration *)configuration ``` |
| To | ``` - (instancetype _Nonnull)initWithConfiguration:(CWConfiguration * _Nonnull)configuration ``` |

Modified [-[CWConfiguration isEqualToConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507064-isequaltoconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToConfiguration:(CWConfiguration *)configuration ``` |
| To | ``` - (BOOL)isEqualToConfiguration:(CWConfiguration * _Nonnull)configuration ``` |

Modified [CWConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507055-networkprofiles)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSOrderedSet *networkProfiles ``` |
| To | ``` @property(readonly, copy, nonnull) NSOrderedSet<CWNetworkProfile *> *networkProfiles ``` |

Modified [CWMutableConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507065-networkprofiles)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSOrderedSet *networkProfiles ``` |
| To | ``` @property(copy, nonnull) NSOrderedSet<CWNetworkProfile *> *networkProfiles ``` |

#### CWInterface.h

Modified [-[CWInterface associateToEnterpriseNetwork:identity:username:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426468-associatetoenterprisenetwork)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)associateToEnterpriseNetwork:(CWNetwork *)network identity:(SecIdentityRef)identity username:(NSString *)username password:(NSString *)password error:(out NSError **)error ``` |
| To | ``` - (BOOL)associateToEnterpriseNetwork:(CWNetwork * _Nonnull)network identity:(SecIdentityRef _Nullable)identity username:(NSString * _Nullable)username password:(NSString * _Nullable)password error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface associateToNetwork:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426455-associatetonetwork)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)associateToNetwork:(CWNetwork *)network password:(NSString *)password error:(out NSError **)error ``` |
| To | ``` - (BOOL)associateToNetwork:(CWNetwork * _Nonnull)network password:(NSString * _Nullable)password error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface bssid]](https://developer.apple.com/documentation/corewlan/cwinterface/1426450-bssid)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)bssid ``` |
| To | ``` - (NSString * _Nullable)bssid ``` |

Modified [-[CWInterface cachedScanResults]](https://developer.apple.com/documentation/corewlan/cwinterface/1426424-cachedscanresults)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)cachedScanResults ``` |
| To | ``` - (NSSet<CWNetwork *> * _Nullable)cachedScanResults ``` |

Modified [-[CWInterface commitConfiguration:authorization:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426430-commitconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)commitConfiguration:(CWConfiguration *)configuration authorization:(SFAuthorization *)authorization error:(out NSError **)error ``` |
| To | ``` - (BOOL)commitConfiguration:(CWConfiguration * _Nonnull)configuration authorization:(SFAuthorization * _Nullable)authorization error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface configuration]](https://developer.apple.com/documentation/corewlan/cwinterface/1426446-configuration)

|  | Declaration |
| --- | --- |
| From | ``` - (CWConfiguration *)configuration ``` |
| To | ``` - (CWConfiguration * _Nullable)configuration ``` |

Modified [-[CWInterface countryCode]](https://developer.apple.com/documentation/corewlan/cwinterface/1426412-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)countryCode ``` |
| To | ``` - (NSString * _Nullable)countryCode ``` |

Modified [-[CWInterface hardwareAddress]](https://developer.apple.com/documentation/corewlan/cwinterface/1426466-hardwareaddress)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)hardwareAddress ``` |
| To | ``` - (NSString * _Nullable)hardwareAddress ``` |

Modified [-[CWInterface initWithInterfaceName:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426442-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithInterfaceName:(NSString *)name ``` |
| To | ``` - (instancetype _Nonnull)initWithInterfaceName:(NSString * _Nonnull)name ``` |

Modified [+[CWInterface interface]](https://developer.apple.com/documentation/corewlan/cwinterface/1426432-interface)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)interface ``` |
| To | ``` + (instancetype _Nonnull)interface ``` |

Modified [CWInterface.interfaceName](https://developer.apple.com/documentation/corewlan/cwinterface/1426462-interfacename)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *interfaceName ``` |
| To | ``` @property(readonly, nullable) NSString *interfaceName ``` |

Modified [+[CWInterface interfaceNames]](https://developer.apple.com/documentation/corewlan/cwinterface/1426457-interfacenames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSSet *)interfaceNames ``` |
| To | ``` + (NSSet<NSString *> * _Nullable)interfaceNames ``` |

Modified [+[CWInterface interfaceWithName:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426460-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)interfaceWithName:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)interfaceWithName:(NSString * _Nonnull)name ``` |

Modified [-[CWInterface scanForNetworksWithName:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426416-scanfornetworkswithname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)scanForNetworksWithName:(NSString *)networkName error:(out NSError **)error ``` |
| To | ``` - (NSSet<CWNetwork *> * _Nullable)scanForNetworksWithName:(NSString * _Nullable)networkName error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface scanForNetworksWithSSID:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426436-scanfornetworks)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)scanForNetworksWithSSID:(NSData *)ssid error:(out NSError **)error ``` |
| To | ``` - (NSSet<CWNetwork *> * _Nullable)scanForNetworksWithSSID:(NSData * _Nullable)ssid error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface setPairwiseMasterKey:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426458-setpairwisemasterkey)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setPairwiseMasterKey:(NSData *)key error:(out NSError **)error ``` |
| To | ``` - (BOOL)setPairwiseMasterKey:(NSData * _Nullable)key error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface setPower:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426451-setpower)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setPower:(BOOL)power error:(out NSError **)error ``` |
| To | ``` - (BOOL)setPower:(BOOL)power error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface setWEPKey:flags:index:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426440-setwepkey)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setWEPKey:(NSData *)key flags:(CWCipherKeyFlags)flags index:(NSInteger)index error:(out NSError **)error ``` |
| To | ``` - (BOOL)setWEPKey:(NSData * _Nullable)key flags:(CWCipherKeyFlags)flags index:(NSInteger)index error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface setWLANChannel:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426418-setwlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setWLANChannel:(CWChannel *)channel error:(out NSError **)error ``` |
| To | ``` - (BOOL)setWLANChannel:(CWChannel * _Nonnull)channel error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface ssid]](https://developer.apple.com/documentation/corewlan/cwinterface/1426441-ssid)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)ssid ``` |
| To | ``` - (NSString * _Nullable)ssid ``` |

Modified [-[CWInterface ssidData]](https://developer.apple.com/documentation/corewlan/cwinterface/1426434-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)ssidData ``` |
| To | ``` - (NSData * _Nullable)ssidData ``` |

Modified [-[CWInterface startIBSSModeWithSSID:security:channel:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426417-startibssmode)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)startIBSSModeWithSSID:(NSData *)ssidData security:(CWIBSSModeSecurity)security channel:(NSUInteger)channel password:(NSString *)password error:(out NSError **)error ``` |
| To | ``` - (BOOL)startIBSSModeWithSSID:(NSData * _Nonnull)ssidData security:(CWIBSSModeSecurity)security channel:(NSUInteger)channel password:(NSString * _Nullable)password error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWInterface supportedWLANChannels]](https://developer.apple.com/documentation/corewlan/cwinterface/1426420-supportedwlanchannels)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)supportedWLANChannels ``` |
| To | ``` - (NSSet<CWChannel *> * _Nullable)supportedWLANChannels ``` |

Modified [-[CWInterface wlanChannel]](https://developer.apple.com/documentation/corewlan/cwinterface/1426426-wlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` - (CWChannel *)wlanChannel ``` |
| To | ``` - (CWChannel * _Nullable)wlanChannel ``` |

#### CWNetwork.h

Modified [CWNetwork.bssid](https://developer.apple.com/documentation/corewlan/cwnetwork/1512224-bssid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *bssid ``` |
| To | ``` @property(readonly, nullable) NSString *bssid ``` |

Modified [CWNetwork.countryCode](https://developer.apple.com/documentation/corewlan/cwnetwork/1512435-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *countryCode ``` |
| To | ``` @property(readonly, nullable) NSString *countryCode ``` |

Modified [CWNetwork.informationElementData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512236-informationelementdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSData *informationElementData ``` |
| To | ``` @property(readonly, nullable) NSData *informationElementData ``` |

Modified [-[CWNetwork isEqualToNetwork:]](https://developer.apple.com/documentation/corewlan/cwnetwork/1512228-isequal)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToNetwork:(CWNetwork *)network ``` |
| To | ``` - (BOOL)isEqualToNetwork:(CWNetwork * _Nonnull)network ``` |

Modified [CWNetwork.ssid](https://developer.apple.com/documentation/corewlan/cwnetwork/1512318-ssid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *ssid ``` |
| To | ``` @property(readonly, nullable) NSString *ssid ``` |

Modified [CWNetwork.ssidData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512419-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSData *ssidData ``` |
| To | ``` @property(readonly, nullable) NSData *ssidData ``` |

Modified [CWNetwork.wlanChannel](https://developer.apple.com/documentation/corewlan/cwnetwork/1512212-wlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CWChannel *wlanChannel ``` |
| To | ``` @property(readonly, nonnull) CWChannel *wlanChannel ``` |

#### CWNetworkProfile.h

Modified [CWMutableNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512167-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *ssidData ``` |
| To | ``` @property(copy, nonnull) NSData *ssidData ``` |

Modified [-[CWNetworkProfile init]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512158-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CWNetworkProfile initWithNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512316-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithNetworkProfile:(CWNetworkProfile *)networkProfile ``` |
| To | ``` - (instancetype _Nonnull)initWithNetworkProfile:(CWNetworkProfile * _Nonnull)networkProfile ``` |

Modified [-[CWNetworkProfile isEqualToNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512221-isequal)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isEqualToNetworkProfile:(CWNetworkProfile *)networkProfile ``` |
| To | ``` - (BOOL)isEqualToNetworkProfile:(CWNetworkProfile * _Nonnull)networkProfile ``` |

Modified [+[CWNetworkProfile networkProfile]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1573754-networkprofile)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)networkProfile ``` |
| To | ``` + (instancetype _Nonnull)networkProfile ``` |

Modified [+[CWNetworkProfile networkProfileWithNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1573753-networkprofilewithnetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)networkProfileWithNetworkProfile:(CWNetworkProfile *)networkProfile ``` |
| To | ``` + (instancetype _Nonnull)networkProfileWithNetworkProfile:(CWNetworkProfile * _Nonnull)networkProfile ``` |

Modified [CWNetworkProfile.ssid](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512448-ssid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *ssid ``` |
| To | ``` @property(readonly, copy, nullable) NSString *ssid ``` |

Modified [CWNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512244-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSData *ssidData ``` |
| To | ``` @property(readonly, copy, nullable) NSData *ssidData ``` |

#### CWWiFiClient.h

Modified [-[CWEventDelegate bssidDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512367-bssiddidchangeforwifiinterfacewi)

|  | Declaration |
| --- | --- |
| From | ``` - (void)bssidDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)bssidDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [-[CWEventDelegate countryCodeDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512342-countrycodedidchangeforwifiinter)

|  | Declaration |
| --- | --- |
| From | ``` - (void)countryCodeDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)countryCodeDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [-[CWEventDelegate linkDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512395-linkdidchangeforwifiinterfacewit)

|  | Declaration |
| --- | --- |
| From | ``` - (void)linkDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)linkDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [-[CWEventDelegate linkQualityDidChangeForWiFiInterfaceWithName:rssi:transmitRate:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512300-linkqualitydidchangeforwifiinter)

|  | Declaration |
| --- | --- |
| From | ``` - (void)linkQualityDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName rssi:(NSInteger)rssi transmitRate:(double)transmitRate ``` |
| To | ``` - (void)linkQualityDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName rssi:(NSInteger)rssi transmitRate:(double)transmitRate ``` |

Modified [-[CWEventDelegate modeDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512226-modedidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` - (void)modeDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)modeDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [-[CWEventDelegate powerStateDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512253-powerstatedidchangeforwifiinterf)

|  | Declaration |
| --- | --- |
| From | ``` - (void)powerStateDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)powerStateDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [-[CWEventDelegate scanCacheUpdatedForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512322-scancacheupdatedforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` - (void)scanCacheUpdatedForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)scanCacheUpdatedForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [-[CWEventDelegate ssidDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512422-ssiddidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` - (void)ssidDidChangeForWiFiInterfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (void)ssidDidChangeForWiFiInterfaceWithName:(NSString * _Nonnull)interfaceName ``` |

Modified [CWWiFiClient.delegate](https://developer.apple.com/documentation/corewlan/cwwificlient/1512387-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak) id delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id delegate ``` |

Modified [-[CWWiFiClient init]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512206-init)

|  | Declaration |
| --- | --- |
| From | ``` - (CWWiFiClient *)init ``` |
| To | ``` - (CWWiFiClient * _Nullable)init ``` |

Modified [-[CWWiFiClient interface]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512352-interface)

|  | Declaration |
| --- | --- |
| From | ``` - (CWInterface *)interface ``` |
| To | ``` - (CWInterface * _Nullable)interface ``` |

Modified [+[CWWiFiClient interfaceNames]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512194-interfacenames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)interfaceNames ``` |
| To | ``` + (NSArray<NSString *> * _Nullable)interfaceNames ``` |

Modified [-[CWWiFiClient interfaces]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512313-interfaces)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)interfaces ``` |
| To | ``` - (NSArray<CWInterface *> * _Nullable)interfaces ``` |

Modified [-[CWWiFiClient interfaceWithName:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512328-interfacewithname)

|  | Declaration |
| --- | --- |
| From | ``` - (CWInterface *)interfaceWithName:(NSString *)interfaceName ``` |
| To | ``` - (CWInterface * _Nullable)interfaceWithName:(NSString * _Nullable)interfaceName ``` |

Modified [+[CWWiFiClient sharedWiFiClient]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512202-sharedwificlient)

|  | Declaration |
| --- | --- |
| From | ``` + (CWWiFiClient *)sharedWiFiClient ``` |
| To | ``` + (CWWiFiClient * _Nonnull)sharedWiFiClient ``` |

Modified [-[CWWiFiClient startMonitoringEventWithType:error:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512439-startmonitoringeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)startMonitoringEventWithType:(CWEventType)type error:(out NSError **)error ``` |
| To | ``` - (BOOL)startMonitoringEventWithType:(CWEventType)type error:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWWiFiClient stopMonitoringAllEventsAndReturnError:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512370-stopmonitoringallevents)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)stopMonitoringAllEventsAndReturnError:(out NSError **)error ``` |
| To | ``` - (BOOL)stopMonitoringAllEventsAndReturnError:(out NSError * _Nullable * _Nullable)error ``` |

Modified [-[CWWiFiClient stopMonitoringEventWithType:error:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512446-stopmonitoringeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)stopMonitoringEventWithType:(CWEventType)type error:(out NSError **)error ``` |
| To | ``` - (BOOL)stopMonitoringEventWithType:(CWEventType)type error:(out NSError * _Nullable * _Nullable)error ``` |

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
