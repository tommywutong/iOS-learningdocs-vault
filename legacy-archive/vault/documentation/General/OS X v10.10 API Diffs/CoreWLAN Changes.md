---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CoreWLAN.html
archived_at: '2026-07-15T07:34:45.410767Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreWLAN Changes

## CoreWLAN

CW8021XProfile.h (Removed)Removed [CW8021XProfile](https://developer.apple.com/documentation/corewlan/cw8021xprofile)Removed [+[CW8021XProfile allUser8021XProfiles]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804786-alluser8021xprofiles)Removed [CW8021XProfile.alwaysPromptForPassword](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804803-alwayspromptforpassword)Removed [-[CW8021XProfile init]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804780-init)Removed [-[CW8021XProfile isEqualToProfile:]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804789-isequaltoprofile)Removed [CW8021XProfile.password](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804801-password)Removed [+[CW8021XProfile profile]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804782-profile)Removed [CW8021XProfile.ssid](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804798-ssid)Removed [CW8021XProfile.userDefinedName](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804793-userdefinedname)Removed [CW8021XProfile.username](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804791-username)CWChannel.hModified [CWChannel.channelNumber](https://developer.apple.com/documentation/corewlan/cwchannel/1512176-channelnumber)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSUInteger channelNumber ``` |
| To | ``` @property(readonly) NSInteger channelNumber ``` |

CWConfiguration.hModified [+[CWConfiguration configuration]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507059-configuration)

|  | Declaration |
| --- | --- |
| From | ``` + (id)configuration ``` |
| To | ``` + (instancetype)configuration ``` |

Modified [+[CWConfiguration configurationWithConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507051-configurationwithconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` + (id)configurationWithConfiguration:(CWConfiguration *)configuration ``` |
| To | ``` + (instancetype)configurationWithConfiguration:(CWConfiguration *)configuration ``` |

Modified [-[CWConfiguration init]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507049-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[CWConfiguration initWithConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507057-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithConfiguration:(CWConfiguration *)configuration ``` |
| To | ``` - (instancetype)initWithConfiguration:(CWConfiguration *)configuration ``` |

Modified [CWConfiguration.rememberJoinedNetworks](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507047-rememberjoinednetworks)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) BOOL rememberJoinedNetworks ``` |
| To | ``` @property(readonly) BOOL rememberJoinedNetworks ``` |

Modified [CWConfiguration.requireAdministratorForAssociation](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507041-requireadministratorforassociati)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) BOOL requireAdministratorForAssociation ``` |
| To | ``` @property(readonly) BOOL requireAdministratorForAssociation ``` |

Modified [CWConfiguration.requireAdministratorForIBSSMode](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507066-requireadministratorforibssmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) BOOL requireAdministratorForIBSSMode ``` |
| To | ``` @property(readonly) BOOL requireAdministratorForIBSSMode ``` |

Modified [CWConfiguration.requireAdministratorForPower](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507061-requireadministratorforpower)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) BOOL requireAdministratorForPower ``` |
| To | ``` @property(readonly) BOOL requireAdministratorForPower ``` |

Modified [CWMutableConfiguration](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [CWMutableConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507065-networkprofiles)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSOrderedSet *networkProfiles ``` |
| To | ``` @property(copy) NSOrderedSet *networkProfiles ``` |

Modified [CWMutableConfiguration.rememberJoinedNetworks](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507045-rememberjoinednetworks)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign) BOOL rememberJoinedNetworks ``` |
| To | ``` @property BOOL rememberJoinedNetworks ``` |

Modified [CWMutableConfiguration.requireAdministratorForAssociation](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507069-requireadministratorforassociati)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign) BOOL requireAdministratorForAssociation ``` |
| To | ``` @property BOOL requireAdministratorForAssociation ``` |

Modified [CWMutableConfiguration.requireAdministratorForIBSSMode](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507067-requireadministratorforibssmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign) BOOL requireAdministratorForIBSSMode ``` |
| To | ``` @property BOOL requireAdministratorForIBSSMode ``` |

Modified [CWMutableConfiguration.requireAdministratorForPower](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507043-requireadministratorforpower)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign) BOOL requireAdministratorForPower ``` |
| To | ``` @property BOOL requireAdministratorForPower ``` |

CWInterface.hRemoved [CWInterface.activePHYMode](https://developer.apple.com/documentation/corewlan/cwinterface/1426471-activephymode)Removed [CWInterface.bssid](https://developer.apple.com/documentation/corewlan/cwinterface/1426450-bssid)Removed [CWInterface.cachedScanResults](https://developer.apple.com/documentation/corewlan/cwinterface/1426424-cachedscanresults)Removed [CWInterface.configuration](https://developer.apple.com/documentation/corewlan/cwinterface/1426446-configuration)Removed [CWInterface.countryCode](https://developer.apple.com/documentation/corewlan/cwinterface/1426412-countrycode)Removed [CWInterface.deviceAttached](https://developer.apple.com/documentation/corewlan/cwinterface/1804772-deviceattached)Removed [CWInterface.hardwareAddress](https://developer.apple.com/documentation/corewlan/cwinterface/1426466-hardwareaddress)Removed [CWInterface.interfaceMode](https://developer.apple.com/documentation/corewlan/cwinterface/1426448-interfacemode)Removed [CWInterface.noiseMeasurement](https://developer.apple.com/documentation/corewlan/cwinterface/1426445-noisemeasurement)Removed [CWInterface.powerOn](https://developer.apple.com/documentation/corewlan/cwinterface/1426453-poweron)Removed [CWInterface.rssiValue](https://developer.apple.com/documentation/corewlan/cwinterface/1426414-rssivalue)Removed [CWInterface.security](https://developer.apple.com/documentation/corewlan/cwinterface/1426464-security)Removed [CWInterface.serviceActive](https://developer.apple.com/documentation/corewlan/cwinterface/1426443-serviceactive)Removed [CWInterface.ssid](https://developer.apple.com/documentation/corewlan/cwinterface/1426441-ssid)Removed [CWInterface.ssidData](https://developer.apple.com/documentation/corewlan/cwinterface/1426434-ssiddata)Removed [CWInterface.supportedWLANChannels](https://developer.apple.com/documentation/corewlan/cwinterface/1426420-supportedwlanchannels)Removed [CWInterface.transmitPower](https://developer.apple.com/documentation/corewlan/cwinterface/1426428-transmitpower)Removed [CWInterface.transmitRate](https://developer.apple.com/documentation/corewlan/cwinterface/1426438-transmitrate)Removed [CWInterface.wlanChannel](https://developer.apple.com/documentation/corewlan/cwinterface/1426426-wlanchannel)Added [-[CWInterface activePHYMode]](https://developer.apple.com/documentation/corewlan/cwinterface/1426471-activephymode)Added [-[CWInterface bssid]](https://developer.apple.com/documentation/corewlan/cwinterface/1426450-bssid)Added [-[CWInterface cachedScanResults]](https://developer.apple.com/documentation/corewlan/cwinterface/1426424-cachedscanresults)Added [-[CWInterface configuration]](https://developer.apple.com/documentation/corewlan/cwinterface/1426446-configuration)Added [-[CWInterface countryCode]](https://developer.apple.com/documentation/corewlan/cwinterface/1426412-countrycode)Added [-[CWInterface hardwareAddress]](https://developer.apple.com/documentation/corewlan/cwinterface/1426466-hardwareaddress)Added [-[CWInterface interfaceMode]](https://developer.apple.com/documentation/corewlan/cwinterface/1426448-interfacemode)Added [-[CWInterface noiseMeasurement]](https://developer.apple.com/documentation/corewlan/cwinterface/1426445-noisemeasurement)Added [-[CWInterface powerOn]](https://developer.apple.com/documentation/corewlan/cwinterface/1426453-poweron)Added [-[CWInterface rssiValue]](https://developer.apple.com/documentation/corewlan/cwinterface/1426414-rssivalue)Added [-[CWInterface security]](https://developer.apple.com/documentation/corewlan/cwinterface/1426464-security)Added [-[CWInterface serviceActive]](https://developer.apple.com/documentation/corewlan/cwinterface/1426443-serviceactive)Added [-[CWInterface ssid]](https://developer.apple.com/documentation/corewlan/cwinterface/1426441-ssid)Added [-[CWInterface ssidData]](https://developer.apple.com/documentation/corewlan/cwinterface/1426434-ssiddata)Added [-[CWInterface supportedWLANChannels]](https://developer.apple.com/documentation/corewlan/cwinterface/1426420-supportedwlanchannels)Added [-[CWInterface transmitPower]](https://developer.apple.com/documentation/corewlan/cwinterface/1426428-transmitpower)Added [-[CWInterface transmitRate]](https://developer.apple.com/documentation/corewlan/cwinterface/1426438-transmitrate)Added [-[CWInterface wlanChannel]](https://developer.apple.com/documentation/corewlan/cwinterface/1426426-wlanchannel)Modified [-[CWInterface associateToEnterpriseNetwork:identity:username:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426468-associatetoenterprisenetwork)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)associateToEnterpriseNetwork:(CWNetwork *)network identity:(SecIdentityRef)identity username:(NSString *)username password:(NSString *)password error:(NSError **)error ``` |
| To | ``` - (BOOL)associateToEnterpriseNetwork:(CWNetwork *)network identity:(SecIdentityRef)identity username:(NSString *)username password:(NSString *)password error:(out NSError **)error ``` |

Modified [-[CWInterface associateToNetwork:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426455-associatetonetwork)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)associateToNetwork:(CWNetwork *)network password:(NSString *)password error:(NSError **)error ``` |
| To | ``` - (BOOL)associateToNetwork:(CWNetwork *)network password:(NSString *)password error:(out NSError **)error ``` |

Modified [-[CWInterface commitConfiguration:authorization:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426430-commitconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)commitConfiguration:(CWConfiguration *)configuration authorization:(SFAuthorization *)authorization error:(NSError **)error ``` |
| To | ``` - (BOOL)commitConfiguration:(CWConfiguration *)configuration authorization:(SFAuthorization *)authorization error:(out NSError **)error ``` |

Modified [-[CWInterface initWithInterfaceName:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426442-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithInterfaceName:(NSString *)name ``` | -- |
| To | ``` - (instancetype)initWithInterfaceName:(NSString *)name ``` | OS X 10.10 |

Modified [+[CWInterface interface]](https://developer.apple.com/documentation/corewlan/cwinterface/1426432-interface)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (CWInterface *)interface ``` | -- |
| To | ``` + (instancetype)interface ``` | OS X 10.10 |

Modified [CWInterface.interfaceName](https://developer.apple.com/documentation/corewlan/cwinterface/1426462-interfacename)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *interfaceName ``` |
| To | ``` @property(readonly) NSString *interfaceName ``` |

Modified [+[CWInterface interfaceNames]](https://developer.apple.com/documentation/corewlan/cwinterface/1426457-interfacenames)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified [+[CWInterface interfaceWithName:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426460-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (CWInterface *)interfaceWithName:(NSString *)name ``` | -- |
| To | ``` + (instancetype)interfaceWithName:(NSString *)name ``` | OS X 10.10 |

Modified [-[CWInterface scanForNetworksWithName:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426416-scanfornetworkswithname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)scanForNetworksWithName:(NSString *)networkName error:(NSError **)error ``` |
| To | ``` - (NSSet *)scanForNetworksWithName:(NSString *)networkName error:(out NSError **)error ``` |

Modified [-[CWInterface scanForNetworksWithSSID:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426436-scanfornetworks)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)scanForNetworksWithSSID:(NSData *)ssid error:(NSError **)error ``` |
| To | ``` - (NSSet *)scanForNetworksWithSSID:(NSData *)ssid error:(out NSError **)error ``` |

Modified [-[CWInterface setPairwiseMasterKey:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426458-setpairwisemasterkey)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setPairwiseMasterKey:(NSData *)key error:(NSError **)error ``` |
| To | ``` - (BOOL)setPairwiseMasterKey:(NSData *)key error:(out NSError **)error ``` |

Modified [-[CWInterface setPower:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426451-setpower)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setPower:(BOOL)power error:(NSError **)error ``` |
| To | ``` - (BOOL)setPower:(BOOL)power error:(out NSError **)error ``` |

Modified [-[CWInterface setWEPKey:flags:index:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426440-setwepkey)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setWEPKey:(NSData *)key flags:(CWCipherKeyFlags)flags index:(NSUInteger)index error:(NSError **)error ``` |
| To | ``` - (BOOL)setWEPKey:(NSData *)key flags:(CWCipherKeyFlags)flags index:(NSInteger)index error:(out NSError **)error ``` |

Modified [-[CWInterface setWLANChannel:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426418-setwlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setWLANChannel:(CWChannel *)channel error:(NSError **)error ``` |
| To | ``` - (BOOL)setWLANChannel:(CWChannel *)channel error:(out NSError **)error ``` |

Modified [-[CWInterface startIBSSModeWithSSID:security:channel:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426417-startibssmode)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)startIBSSModeWithSSID:(NSData *)ssidData security:(CWIBSSModeSecurity)security channel:(NSUInteger)channel password:(NSString *)password error:(NSError **)error ``` |
| To | ``` - (BOOL)startIBSSModeWithSSID:(NSData *)ssidData security:(CWIBSSModeSecurity)security channel:(NSUInteger)channel password:(NSString *)password error:(out NSError **)error ``` |

CWNetwork.hModified [CWNetwork.beaconInterval](https://developer.apple.com/documentation/corewlan/cwnetwork/1512398-beaconinterval)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSUInteger beaconInterval ``` |
| To | ``` @property(readonly) NSInteger beaconInterval ``` |

Modified [-[CWNetwork supportsPHYMode:]](https://developer.apple.com/documentation/corewlan/cwnetwork/1512292-supportsphymode)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.8 |

CWNetworkProfile.hModified [CWMutableNetworkProfile.security](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512361-security)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign) CWSecurity security ``` |
| To | ``` @property CWSecurity security ``` |

Modified [CWMutableNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512167-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSData *ssidData ``` |
| To | ``` @property(copy) NSData *ssidData ``` |

Modified [-[CWNetworkProfile init]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512158-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[CWNetworkProfile initWithNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512316-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithNetworkProfile:(CWNetworkProfile *)networkProfile ``` |
| To | ``` - (instancetype)initWithNetworkProfile:(CWNetworkProfile *)networkProfile ``` |

Modified [+[CWNetworkProfile networkProfile]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1573754-networkprofile)

|  | Declaration |
| --- | --- |
| From | ``` + (id)networkProfile ``` |
| To | ``` + (instancetype)networkProfile ``` |

Modified [+[CWNetworkProfile networkProfileWithNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1573753-networkprofilewithnetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` + (id)networkProfileWithNetworkProfile:(CWNetworkProfile *)networkProfile ``` |
| To | ``` + (instancetype)networkProfileWithNetworkProfile:(CWNetworkProfile *)networkProfile ``` |

Modified [CWNetworkProfile.security](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512364-security)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CWSecurity security ``` |
| To | ``` @property(readonly) CWSecurity security ``` |

CWWiFiClient.h (Added)Added [CWEventDelegate](https://developer.apple.com/documentation/corewlan/cweventdelegate)Added [-[CWEventDelegate bssidDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512367-bssiddidchangeforwifiinterfacewi)Added [-[CWEventDelegate clientConnectionInterrupted]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512337-clientconnectioninterrupted)Added [-[CWEventDelegate clientConnectionInvalidated]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512232-clientconnectioninvalidated)Added [-[CWEventDelegate countryCodeDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512342-countrycodedidchangeforwifiinter)Added [-[CWEventDelegate linkDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512395-linkdidchangeforwifiinterfacewit)Added [-[CWEventDelegate linkQualityDidChangeForWiFiInterfaceWithName:rssi:transmitRate:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512300-linkqualitydidchangeforwifiinter)Added [-[CWEventDelegate modeDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512226-modedidchangeforwifiinterface)Added [-[CWEventDelegate powerStateDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512253-powerstatedidchangeforwifiinterf)Added [-[CWEventDelegate scanCacheUpdatedForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512322-scancacheupdatedforwifiinterface)Added [-[CWEventDelegate ssidDidChangeForWiFiInterfaceWithName:]](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512422-ssiddidchangeforwifiinterface)Added [CWWiFiClient](https://developer.apple.com/documentation/corewlan/cwwificlient)Added [CWWiFiClient.delegate](https://developer.apple.com/documentation/corewlan/cwwificlient/1512387-delegate)Added [-[CWWiFiClient init]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512206-init)Added [-[CWWiFiClient interface]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512352-interface)Added [+[CWWiFiClient interfaceNames]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512194-interfacenames)Added [-[CWWiFiClient interfaceWithName:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512328-interfacewithname)Added [-[CWWiFiClient interfaces]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512313-interfaces)Added [+[CWWiFiClient sharedWiFiClient]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512202-sharedwificlient)Added [-[CWWiFiClient startMonitoringEventWithType:error:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512439-startmonitoringeventwithtype)Added [-[CWWiFiClient stopMonitoringAllEventsAndReturnError:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512370-stopmonitoringallevents)Added [-[CWWiFiClient stopMonitoringEventWithType:error:]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512446-stopmonitoringeventwithtype)CWWirelessProfile.h (Removed)Removed CWWirelessProfileRemoved -[CWWirelessProfile init]Removed -[CWWirelessProfile isEqualToProfile:]Removed CWWirelessProfile.passphraseRemoved +[CWWirelessProfile profile]Removed CWWirelessProfile.securityModeRemoved CWWirelessProfile.ssidRemoved CWWirelessProfile.user8021XProfileCoreWLAN.hRemoved CoreWLANFrameworkVersionNumberRemoved #def CoreWLANFrameworkVersionNumber2_0CoreWLANConstants.hRemoved [CWServiceDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/cwservicedidchangenotification)Modified [CWBSSIDDidChangeNotification](https://developer.apple.com/documentation/corewlan/cwbssiddidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWCountryCodeDidChangeNotification](https://developer.apple.com/documentation/corewlan/cwcountrycodedidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWLinkDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512162-cwlinkdidchange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWLinkQualityDidChangeNotification](https://developer.apple.com/documentation/corewlan/cwlinkqualitydidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWLinkQualityNotificationRSSIKey](https://developer.apple.com/documentation/corewlan/cwlinkqualitynotificationrssikey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified [CWLinkQualityNotificationTransmitRateKey](https://developer.apple.com/documentation/corewlan/cwlinkqualitynotificationtransmitratekey)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.7 | -- |
| To | OS X 10.6 | OS X 10.10 |

Modified [CWModeDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512192-cwmodedidchange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWPowerDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512347-cwpowerdidchange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWSSIDDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512200-cwssiddidchange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [CWScanCacheDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512155-cwscancachedidupdate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

CoreWLANTypes.hAdded [CWEventType](https://developer.apple.com/documentation/corewlan/cweventtype)Added [CWEventTypeBSSIDDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/bssiddidchange)Added [CWEventTypeCountryCodeDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypecountrycodedidchange)Added [CWEventTypeLinkDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypelinkdidchange)Added [CWEventTypeLinkQualityDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/linkqualitydidchange)Added [CWEventTypeModeDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/modedidchange)Added [CWEventTypeNone](https://developer.apple.com/documentation/corewlan/cweventtype/none)Added [CWEventTypePowerDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypepowerdidchange)Added [CWEventTypeSSIDDidChange](https://developer.apple.com/documentation/corewlan/cweventtype/cweventtypessiddidchange)Added [CWEventTypeScanCacheUpdated](https://developer.apple.com/documentation/corewlan/cweventtype/scancacheupdated)Added [CWEventTypeUnknown](https://developer.apple.com/documentation/corewlan/cweventtype/unknown)Modified [kCWAuthenticationAlgorithmUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwauthenticationalgorithmunsupportederr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWChannelWidth160MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth160mhz)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.7 |

Modified [kCWChannelWidth80MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth80mhz)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.7 |

Modified [kCWEAPOLErr](https://developer.apple.com/documentation/corewlan/cwerr/kcweapolerr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWErr](https://developer.apple.com/documentation/corewlan/cwerr/cwerr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWHTFeaturesNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwhtfeaturesnotsupportederr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWIPCFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/cwipcfailureerr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWInvalidAuthenticationSequenceNumberErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidauthenticationsequencenumbererr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWInvalidFormatErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidformaterr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWInvalidInformationElementErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidinformationelementerr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWInvalidParameterErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidparametererr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWKeychainDomainNone](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/none)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [kCWKeychainDomainSystem](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/kcwkeychaindomainsystem)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [kCWKeychainDomainUser](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/kcwkeychaindomainuser)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [kCWNoMemoryErr](https://developer.apple.com/documentation/corewlan/cwerr/cwnomemoryerr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWOperationNotPermittedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwoperationnotpermittederr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWPCOTransitionTimeNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwpcotransitiontimenotsupportederr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWPHYMode11ac](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11ac)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.7 |

Modified [kCWReferenceNotBoundErr](https://developer.apple.com/documentation/corewlan/cwerr/cwreferencenotbounderr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

Modified [kCWUnknownErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwunknownerr)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.6 |

CoreWLANUtil.hModified [CWKeychainCopyEAPIdentityList()](https://developer.apple.com/documentation/corewlan/1512258-cwkeychaincopyeapidentitylist)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | -- |

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
