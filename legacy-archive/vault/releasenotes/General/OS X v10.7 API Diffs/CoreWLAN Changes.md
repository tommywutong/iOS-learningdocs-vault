---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreWLAN.html
archived_at: '2026-07-18T02:54:27.617358Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreWLAN Changes

## CoreWLAN

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CW8021XProfile.hModified [-[CW8021XProfile init]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804780-init)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[CW8021XProfile isEqualToProfile:]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804789-isequaltoprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CW8021XProfile.password](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804801-password)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CW8021XProfile.userDefinedName](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804793-userdefinedname)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CW8021XProfile.alwaysPromptForPassword](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804803-alwayspromptforpassword)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CW8021XProfile.username](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804791-username)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [+[CW8021XProfile allUser8021XProfiles]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804786-alluser8021xprofiles)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CW8021XProfile.ssid](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804798-ssid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [+[CW8021XProfile profile]](https://developer.apple.com/documentation/corewlan/cw8021xprofile/1804782-profile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CWChannel.hAdded [CWChannel](https://developer.apple.com/documentation/corewlan/cwchannel)Added [CWChannel.channelBand](https://developer.apple.com/documentation/corewlan/cwchannel/1512165-channelband)Added [CWChannel.channelNumber](https://developer.apple.com/documentation/corewlan/cwchannel/1512176-channelnumber)Added [CWChannel.channelWidth](https://developer.apple.com/documentation/corewlan/cwchannel/1512185-channelwidth)Added [-[CWChannel isEqualToChannel:]](https://developer.apple.com/documentation/corewlan/cwchannel/1512390-isequaltochannel)CWConfiguration.hAdded [+[CWConfiguration configurationWithConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507051-configurationwithconfiguration)Added [-[CWConfiguration initWithConfiguration:]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507057-init)Added [CWConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507055-networkprofiles)Added [CWConfiguration.rememberJoinedNetworks](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507047-rememberjoinednetworks)Added [CWConfiguration.requireAdministratorForAssociation](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507041-requireadministratorforassociati)Added [CWConfiguration.requireAdministratorForIBSSMode](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507066-requireadministratorforibssmode)Added [CWConfiguration.requireAdministratorForPower](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507061-requireadministratorforpower)Added [CWMutableConfiguration](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration)Added [CWMutableConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507065-networkprofiles)Added [CWMutableConfiguration.rememberJoinedNetworks](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507045-rememberjoinednetworks)Added [CWMutableConfiguration.requireAdministratorForAssociation](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507069-requireadministratorforassociati)Added [CWMutableConfiguration.requireAdministratorForIBSSMode](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507067-requireadministratorforibssmode)Added [CWMutableConfiguration.requireAdministratorForPower](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507043-requireadministratorforpower)Added CWConfiguration(Deprecated)Modified [CWConfiguration](https://developer.apple.com/documentation/corewlan/cwconfiguration)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCoding, NSCopying, NSMutableCopying |

Modified CWConfiguration.disconnectOnLogout

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property BOOL disconnectOnLogout |
| To | OS X v10.7 | @property(readwrite, assign) BOOL disconnectOnLogout |

Modified CWConfiguration.alwaysRememberNetworks

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property BOOL alwaysRememberNetworks |
| To | OS X v10.7 | @property(readwrite, assign) BOOL alwaysRememberNetworks |

Modified CWConfiguration.requireAdminForIBSSCreation

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property BOOL requireAdminForIBSSCreation |
| To | OS X v10.7 | @property(readwrite, assign) BOOL requireAdminForIBSSCreation |

Modified CWConfiguration.requireAdminForPowerChange

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property BOOL requireAdminForPowerChange |
| To | OS X v10.7 | @property(readwrite, assign) BOOL requireAdminForPowerChange |

Modified CWConfiguration.preferredNetworks

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWConfiguration.rememberedNetworks

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [+[CWConfiguration configuration]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507059-configuration)

|  | Declaration |
| --- | --- |
| From | + (CWConfiguration \*)configuration |
| To | + (id)configuration |

Modified CWConfiguration.requireAdminForNetworkChange

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property BOOL requireAdminForNetworkChange |
| To | OS X v10.7 | @property(readwrite, assign) BOOL requireAdminForNetworkChange |

Modified [-[CWConfiguration init]](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507049-init)

|  | Declaration |
| --- | --- |
| From | - (CWConfiguration \*)init |
| To | - (id)init |

CWInterface.hRemoved -[CWInterface init]Added [CWInterface.activePHYMode](https://developer.apple.com/documentation/corewlan/cwinterface/1426471-activephymode)Added [-[CWInterface associateToEnterpriseNetwork:identity:username:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426468-associatetoenterprisenetwork)Added [-[CWInterface associateToNetwork:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426455-associatetonetwork)Added [CWInterface.cachedScanResults](https://developer.apple.com/documentation/corewlan/cwinterface/1426424-cachedscanresults)Added [-[CWInterface commitConfiguration:authorization:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426430-commitconfiguration)Added [CWInterface.deviceAttached](https://developer.apple.com/documentation/corewlan/cwinterface/1804772-deviceattached)Added [CWInterface.hardwareAddress](https://developer.apple.com/documentation/corewlan/cwinterface/1426466-hardwareaddress)Added [CWInterface.interfaceMode](https://developer.apple.com/documentation/corewlan/cwinterface/1426448-interfacemode)Added [CWInterface.interfaceName](https://developer.apple.com/documentation/corewlan/cwinterface/1426462-interfacename)Added [+[CWInterface interfaceNames]](https://developer.apple.com/documentation/corewlan/cwinterface/1426457-interfacenames)Added [CWInterface.noiseMeasurement](https://developer.apple.com/documentation/corewlan/cwinterface/1426445-noisemeasurement)Added [CWInterface.powerOn](https://developer.apple.com/documentation/corewlan/cwinterface/1426453-poweron)Added [CWInterface.rssiValue](https://developer.apple.com/documentation/corewlan/cwinterface/1426414-rssivalue)Added [-[CWInterface scanForNetworksWithName:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426416-scanfornetworkswithname)Added [-[CWInterface scanForNetworksWithSSID:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426436-scanfornetworks)Added [CWInterface.security](https://developer.apple.com/documentation/corewlan/cwinterface/1426464-security)Added [CWInterface.serviceActive](https://developer.apple.com/documentation/corewlan/cwinterface/1426443-serviceactive)Added [-[CWInterface setPairwiseMasterKey:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426458-setpairwisemasterkey)Added [-[CWInterface setWEPKey:flags:index:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426440-setwepkey)Added [-[CWInterface setWLANChannel:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426418-setwlanchannel)Added [CWInterface.ssidData](https://developer.apple.com/documentation/corewlan/cwinterface/1426434-ssiddata)Added [-[CWInterface startIBSSModeWithSSID:security:channel:password:error:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426417-startibssmode)Added [CWInterface.supportedWLANChannels](https://developer.apple.com/documentation/corewlan/cwinterface/1426420-supportedwlanchannels)Added [CWInterface.transmitPower](https://developer.apple.com/documentation/corewlan/cwinterface/1426428-transmitpower)Added [CWInterface.transmitRate](https://developer.apple.com/documentation/corewlan/cwinterface/1426438-transmitrate)Added [CWInterface.wlanChannel](https://developer.apple.com/documentation/corewlan/cwinterface/1426426-wlanchannel)Added CWInterface(Deprecated)Modified CWInterface.powerSave

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsMonitorMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.opMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.noise

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.interfaceState

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.securityMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsTKIP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsShortGI40MHz

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsWEP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsWoW

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.phyMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportedPHYModes

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsWME

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsAES_CCM

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.power

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.txPower

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.authorization

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWInterface setChannel:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.channel

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWInterface isEqualToInterface:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.txRate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[CWInterface supportedInterfaces]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.bssidData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsWPA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsPMGT

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsTSN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.rssi

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportedChannels

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWInterface commitConfiguration:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsIBSS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsWPA2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWInterface scanForNetworksWithParameters:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsHostAP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.supportsShortGI20MHz

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWInterface.name

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWInterface associateToNetwork:parameters:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWInterface enableIBSSWithParameters:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [-[CWInterface initWithInterfaceName:]](https://developer.apple.com/documentation/corewlan/cwinterface/1426442-init)

|  | Declaration |
| --- | --- |
| From | - (CWInterface \*)initWithInterfaceName:(NSString \*)name |
| To | - (id)initWithInterfaceName:(NSString \*)name |

CWNetwork.hAdded [CWNetwork.beaconInterval](https://developer.apple.com/documentation/corewlan/cwnetwork/1512398-beaconinterval)Added [CWNetwork.countryCode](https://developer.apple.com/documentation/corewlan/cwnetwork/1512435-countrycode)Added [CWNetwork.ibss](https://developer.apple.com/documentation/corewlan/cwnetwork/1512251-ibss)Added [CWNetwork.informationElementData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512236-informationelementdata)Added [CWNetwork.noiseMeasurement](https://developer.apple.com/documentation/corewlan/cwnetwork/1512455-noisemeasurement)Added [CWNetwork.rssiValue](https://developer.apple.com/documentation/corewlan/cwnetwork/1512249-rssivalue)Added [CWNetwork.ssidData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512419-ssiddata)Added [-[CWNetwork supportsPHYMode:]](https://developer.apple.com/documentation/corewlan/cwnetwork/1512292-supportsphymode)Added [-[CWNetwork supportsSecurity:]](https://developer.apple.com/documentation/corewlan/cwnetwork/1512450-supportssecurity)Added [CWNetwork.wlanChannel](https://developer.apple.com/documentation/corewlan/cwnetwork/1512212-wlanchannel)Added CWNetwork(Deprecated)Modified CWNetwork.channel

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.noise

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.phyMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.rssi

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.securityMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.bssidData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.isIBSS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.wirelessProfile

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWNetwork.ieData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CWNetworkProfile.hAdded [CWMutableNetworkProfile](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile)Added [CWMutableNetworkProfile.security](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512361-security)Added [CWMutableNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512167-ssiddata)Added [CWNetworkProfile](https://developer.apple.com/documentation/corewlan/cwnetworkprofile)Added [-[CWNetworkProfile init]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512158-init)Added [-[CWNetworkProfile initWithNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512316-init)Added [-[CWNetworkProfile isEqualToNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512221-isequal)Added [+[CWNetworkProfile networkProfile]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1573754-networkprofile)Added [+[CWNetworkProfile networkProfileWithNetworkProfile:]](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1573753-networkprofilewithnetworkprofile)Added [CWNetworkProfile.security](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512364-security)Added [CWNetworkProfile.ssid](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512448-ssid)Added [CWNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512244-ssiddata)CWWirelessProfile.hModified CWWirelessProfile.ssid

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWWirelessProfile.securityMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified +[CWWirelessProfile profile]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWWirelessProfile init]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWWirelessProfile.passphrase

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CWWirelessProfile.user8021XProfile

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified -[CWWirelessProfile isEqualToProfile:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CoreWLAN.hRemoved #def COREWLAN_VERSION_1_0Added CoreWLANFrameworkVersionNumberAdded #def CoreWLANFrameworkVersionNumber2_0CoreWLANConstants.hAdded [CWBSSIDDidChangeNotification](https://developer.apple.com/documentation/corewlan/cwbssiddidchangenotification)Added [CWCountryCodeDidChangeNotification](https://developer.apple.com/documentation/corewlan/cwcountrycodedidchangenotification)Added [CWErrorDomain](https://developer.apple.com/documentation/corewlan/cwerrordomain)Added [CWLinkDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512162-cwlinkdidchange)Added [CWLinkQualityDidChangeNotification](https://developer.apple.com/documentation/corewlan/cwlinkqualitydidchangenotification)Added [CWLinkQualityNotificationRSSIKey](https://developer.apple.com/documentation/corewlan/cwlinkqualitynotificationrssikey)Added [CWLinkQualityNotificationTransmitRateKey](https://developer.apple.com/documentation/corewlan/cwlinkqualitynotificationtransmitratekey)Added [CWModeDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512192-cwmodedidchange)Added [CWPowerDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512347-cwpowerdidchange)Added [CWSSIDDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512200-cwssiddidchange)Added [CWScanCacheDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1512155-cwscancachedidupdate)Added [CWServiceDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/cwservicedidchangenotification)Modified [kCWScanKeyMerge](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeymerge)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWSSIDDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwssiddidchangenotification)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWIBSSKeyPassphrase](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwibsskeypassphrase)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWScanKeyDwellTime](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeydwelltime)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWBSSIDDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwbssiddidchangenotification)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWScanKeyRestTime](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeyresttime)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWCountryCodeDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwcountrycodedidchangenotification)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWIBSSKeyChannel](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwibsskeychannel)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWErrorDomain](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwerrordomain)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWLinkDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwlinkdidchangenotification)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWPowerDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwpowerdidchangenotification)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWIBSSKeySSID](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwibsskeyssid)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWScanKeySSID](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeyssid)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWScanKeyScanType](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeyscantype)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWAssocKey8021XProfile](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwassockey8021xprofile)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWAssocKeyPassphrase](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwassockeypassphrase)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWScanKeyBSSID](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeybssid)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

Modified [kCWModeDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwmodedidchangenotification)

|  | Header | Deprecation |
| --- | --- | --- |
| From | CWGlobals.h | _none_ |
| To | CoreWLANConstants.h | OS X v10.7 |

CoreWLANTypes.hAdded [CWChannelBand](https://developer.apple.com/documentation/corewlan/cwchannelband)Added [CWChannelWidth](https://developer.apple.com/documentation/corewlan/cwchannelwidth)Added [CWCipherKeyFlags](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags)Added [CWIBSSModeSecurity](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity)Added [CWInterfaceMode](https://developer.apple.com/documentation/corewlan/cwinterfacemode)Added [CWSecurity](https://developer.apple.com/documentation/corewlan/cwsecurity)Added [kCWAuthenticationAlgorithmUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwauthenticationalgorithmunsupportederr)Added [kCWChannelBand2GHz](https://developer.apple.com/documentation/corewlan/cwchannelband/band2ghz)Added [kCWChannelBand5GHz](https://developer.apple.com/documentation/corewlan/cwchannelband/band5ghz)Added [kCWChannelBandUnknown](https://developer.apple.com/documentation/corewlan/cwchannelband/bandunknown)Added [kCWChannelWidth20MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth20mhz)Added [kCWChannelWidth40MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth40mhz)Added [kCWChannelWidthUnknown](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidthunknown)Added [kCWCipherKeyFlagsMulticast](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagsmulticast)Added [kCWCipherKeyFlagsNone](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagsnone)Added [kCWCipherKeyFlagsRx](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/1462705-rx)Added [kCWCipherKeyFlagsTx](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagstx)Added [kCWCipherKeyFlagsUnicast](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/kcwcipherkeyflagsunicast)Added [kCWEAPOLErr](https://developer.apple.com/documentation/corewlan/cwerr/kcweapolerr)Added [kCWErr](https://developer.apple.com/documentation/corewlan/cwerr/cwerr)Added [kCWHTFeaturesNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwhtfeaturesnotsupportederr)Added [kCWIBSSModeSecurityNone](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity/none)Added [kCWIBSSModeSecurityWEP104](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity/wep104)Added [kCWIBSSModeSecurityWEP40](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity/wep40)Added [kCWIPCFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/cwipcfailureerr)Added [kCWInterfaceModeHostAP](https://developer.apple.com/documentation/corewlan/cwinterfacemode/kcwinterfacemodehostap)Added [kCWInterfaceModeIBSS](https://developer.apple.com/documentation/corewlan/cwinterfacemode/ibss)Added [kCWInterfaceModeNone](https://developer.apple.com/documentation/corewlan/cwinterfacemode/none)Added [kCWInterfaceModeStation](https://developer.apple.com/documentation/corewlan/cwinterfacemode/station)Added [kCWInvalidAuthenticationSequenceNumberErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidauthenticationsequencenumbererr)Added [kCWInvalidFormatErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidformaterr)Added [kCWInvalidInformationElementErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidinformationelementerr)Added [kCWInvalidParameterErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidparametererr)Added [kCWNoMemoryErr](https://developer.apple.com/documentation/corewlan/cwerr/cwnomemoryerr)Added [kCWOperationNotPermittedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwoperationnotpermittederr)Added [kCWPCOTransitionTimeNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwpcotransitiontimenotsupportederr)Added [kCWPHYMode11a](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11a)Added [kCWPHYMode11b](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11b)Added [kCWPHYMode11g](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11g)Added [kCWPHYMode11n](https://developer.apple.com/documentation/corewlan/cwphymode/mode11n)Added [kCWPHYModeNone](https://developer.apple.com/documentation/corewlan/cwphymode/modenone)Added [kCWReferenceNotBoundErr](https://developer.apple.com/documentation/corewlan/cwerr/cwreferencenotbounderr)Added [kCWSecurityDynamicWEP](https://developer.apple.com/documentation/corewlan/cwsecurity/dynamicwep)Added [kCWSecurityEnterprise](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecurityenterprise)Added [kCWSecurityNone](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritynone)Added [kCWSecurityPersonal](https://developer.apple.com/documentation/corewlan/cwsecurity/personal)Added [kCWSecurityUnknown](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecurityunknown)Added [kCWSecurityWEP](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywep)Added [kCWSecurityWPA2Enterprise](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywpa2enterprise)Added [kCWSecurityWPA2Personal](https://developer.apple.com/documentation/corewlan/cwsecurity/wpa2personal)Added [kCWSecurityWPAEnterprise](https://developer.apple.com/documentation/corewlan/cwsecurity/wpaenterprise)Added [kCWSecurityWPAEnterpriseMixed](https://developer.apple.com/documentation/corewlan/cwsecurity/wpaenterprisemixed)Added [kCWSecurityWPAPersonal](https://developer.apple.com/documentation/corewlan/cwsecurity/wpapersonal)Added [kCWSecurityWPAPersonalMixed](https://developer.apple.com/documentation/corewlan/cwsecurity/kcwsecuritywpapersonalmixed)Added [kCWUnknownErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwunknownerr)Modified [kCWInvalidPairwiseCipherErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidpairwiseciphererr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWError](https://developer.apple.com/documentation/corewlan/corewlantypes.h/kcwparamerr/kcwerror)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified CWInterfaceState

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWOpModeMonitorMode](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodemonitormode)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [CWPHYMode](https://developer.apple.com/documentation/corewlan/cwphymode)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInvalidGroupCipherErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidgroupciphererr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWUnsupportedRSNVersionErr](https://developer.apple.com/documentation/corewlan/cwerr/cwunsupportedrsnversionerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWPHYMode11A

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWScanTypeFast](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwscantype/kcwscantypefast)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWChallengeFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/cwchallengefailureerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWAssociationDeniedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwassociationdeniederr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified CWOpMode

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWRefNotBoundErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeWPA2_PSK](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa2_psk)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInvalidRSNCapabilitiesErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwinvalidrsncapabilitieserr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWScanTypePassive](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwscantype/kcwscantypepassive)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWScanTypeActive](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwscantype/kcwscantypeactive)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWFormatErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInterfaceStateInactive](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestateinactive)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWDSSSOFDMUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwdsssofdmunsupportederr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified CWSecurityMode

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWHTFeaturesNotSupported

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInvalidPMKErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidpmkerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWNoMemErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSupplicantTimeoutErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwsupplicanttimeouterr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWPCOTransitionTimeNotSupported

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWOpNotPermitted

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWUnsupportedCapabilitiesErr](https://developer.apple.com/documentation/corewlan/cwerr/cwunsupportedcapabilitieserr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWOpModeStation](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodestation)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWOpModeHostAP](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodehostap)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWInvalidInfoElementErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeWPA2_Enterprise](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa2_enterprise)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWNoErr](https://developer.apple.com/documentation/corewlan/cwerr/cwnoerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [CWErr](https://developer.apple.com/documentation/corewlan/cwerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWInvalidAuthSeqNumErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWReassociationDeniedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwreassociationdeniederr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInterfaceStateRunning](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestaterunning)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWCipherSuiteRejectedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwciphersuiterejectederr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInterfaceStateAuthenticating](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestateauthenticating)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeWPA_Enterprise](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa_enterprise)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWParamErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWAPFullErr](https://developer.apple.com/documentation/corewlan/cwerr/cwapfullerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWUknownErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeWPS](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewps)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInterfaceStateScanning](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestatescanning)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWUnspecifiedFailureErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwunspecifiedfailureerr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWPHYMode11B

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWIPCError

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWNotSupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/cwnotsupportederr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWAuthAlgUnsupportedErr

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWUnsupportedRateSetErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwunsupportedrateseterr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeOpen](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodeopen)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInvalidAKMPErr](https://developer.apple.com/documentation/corewlan/cwerr/cwinvalidakmperr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWPHYMode11N

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeDynamicWEP](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodedynamicwep)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWInterfaceStateAssociating](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestateassociating)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified CWScanType

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified kCWPHYMode11G

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWShortSlotUnsupportedErr](https://developer.apple.com/documentation/corewlan/cwerr/kcwshortslotunsupportederr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWOpModeIBSS](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodeibss)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWTimeoutErr](https://developer.apple.com/documentation/corewlan/cwerr/cwtimeouterr)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeWEP](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewep)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

Modified [kCWSecurityModeWPA_PSK](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa_psk)

|  | Header |
| --- | --- |
| From | CWGlobals.h |
| To | CoreWLANTypes.h |

CoreWLANUtil.hAdded [CWKeychainCopyEAPIdentity()](https://developer.apple.com/documentation/corewlan/1569166-cwkeychaincopyeapidentity)Added [CWKeychainCopyEAPIdentityList()](https://developer.apple.com/documentation/corewlan/1512258-cwkeychaincopyeapidentitylist)Added [CWKeychainCopyEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569173-cwkeychaincopyeapusernameandpass)Added [CWKeychainCopyPassword()](https://developer.apple.com/documentation/corewlan/1569169-cwkeychaincopypassword)Added [CWKeychainDeleteEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569171-cwkeychaindeleteeapusernameandpa)Added [CWKeychainDeletePassword()](https://developer.apple.com/documentation/corewlan/1569170-cwkeychaindeletepassword)Added [CWKeychainSetEAPIdentity()](https://developer.apple.com/documentation/corewlan/1569167-cwkeychainseteapidentity)Added [CWKeychainSetEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569172-cwkeychainseteapusernameandpassw)Added [CWKeychainSetPassword()](https://developer.apple.com/documentation/corewlan/1569168-cwkeychainsetpassword)Added [CWMergeNetworks()](https://developer.apple.com/documentation/corewlan/1512230-cwmergenetworks)

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
