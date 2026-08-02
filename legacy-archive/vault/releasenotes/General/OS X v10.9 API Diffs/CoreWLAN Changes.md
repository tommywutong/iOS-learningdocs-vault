---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/CoreWLAN.html
archived_at: '2026-07-18T02:54:12.106471Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# CoreWLAN Changes

## CoreWLAN

CW8021XProfile.hModified [CW8021XProfile](https://developer.apple.com/documentation/corewlan/cw8021xprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

CWChannel.hModified [CWChannel](https://developer.apple.com/documentation/corewlan/cwchannel)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CWConfiguration.hRemoved CWConfiguration.alwaysRememberNetworksRemoved CWConfiguration.disconnectOnLogoutRemoved CWConfiguration.preferredNetworksRemoved CWConfiguration.rememberedNetworksRemoved CWConfiguration.requireAdminForIBSSCreationRemoved CWConfiguration.requireAdminForNetworkChangeRemoved CWConfiguration.requireAdminForPowerChangeRemoved CWConfiguration(Deprecated)Modified [CWConfiguration](https://developer.apple.com/documentation/corewlan/cwconfiguration)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

CWGlobals.hCWInterface.hRemoved -[CWInterface associateToNetwork:parameters:error:]Removed CWInterface.authorizationRemoved CWInterface.bssidDataRemoved CWInterface.channelRemoved -[CWInterface commitConfiguration:error:]Removed -[CWInterface enableIBSSWithParameters:error:]Removed CWInterface.interfaceStateRemoved -[CWInterface isEqualToInterface:]Removed CWInterface.nameRemoved CWInterface.noiseRemoved CWInterface.opModeRemoved CWInterface.phyModeRemoved CWInterface.powerRemoved CWInterface.powerSaveRemoved CWInterface.rssiRemoved -[CWInterface scanForNetworksWithParameters:error:]Removed CWInterface.securityModeRemoved -[CWInterface setChannel:error:]Removed CWInterface.supportedChannelsRemoved +[CWInterface supportedInterfaces]Removed CWInterface.supportedPHYModesRemoved CWInterface.supportsAES_CCMRemoved CWInterface.supportsHostAPRemoved CWInterface.supportsIBSSRemoved CWInterface.supportsMonitorModeRemoved CWInterface.supportsPMGTRemoved CWInterface.supportsShortGI20MHzRemoved CWInterface.supportsShortGI40MHzRemoved CWInterface.supportsTKIPRemoved CWInterface.supportsTSNRemoved CWInterface.supportsWEPRemoved CWInterface.supportsWMERemoved CWInterface.supportsWPARemoved CWInterface.supportsWPA2Removed CWInterface.supportsWoWRemoved CWInterface.txPowerRemoved CWInterface.txRateRemoved CWInterface(Deprecated)CWNetwork.hRemoved CWNetwork.bssidDataRemoved CWNetwork.channelRemoved CWNetwork.ieDataRemoved CWNetwork.isIBSSRemoved CWNetwork.noiseRemoved CWNetwork.phyModeRemoved CWNetwork.rssiRemoved CWNetwork.securityModeRemoved CWNetwork.wirelessProfileRemoved CWNetwork(Deprecated)Modified [CWNetwork](https://developer.apple.com/documentation/corewlan/cwnetwork)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

CWNetworkProfile.hModified [CWNetworkProfile](https://developer.apple.com/documentation/corewlan/cwnetworkprofile)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying, NSSecureCoding |

CWWirelessProfile.hModified CWWirelessProfile

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.7 |

CoreWLANConstants.hRemoved [kCWAssocKey8021XProfile](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwassockey8021xprofile)Removed [kCWAssocKeyPassphrase](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwassockeypassphrase)Removed [kCWBSSIDDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwbssiddidchangenotification)Removed [kCWCountryCodeDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwcountrycodedidchangenotification)Removed [kCWErrorDomain](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwerrordomain)Removed [kCWIBSSKeyChannel](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwibsskeychannel)Removed [kCWIBSSKeyPassphrase](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwibsskeypassphrase)Removed [kCWIBSSKeySSID](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwibsskeyssid)Removed [kCWLinkDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwlinkdidchangenotification)Removed [kCWModeDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwmodedidchangenotification)Removed [kCWPowerDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwpowerdidchangenotification)Removed [kCWSSIDDidChangeNotification](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwssiddidchangenotification)Removed [kCWScanKeyBSSID](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeybssid)Removed [kCWScanKeyDwellTime](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeydwelltime)Removed [kCWScanKeyMerge](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeymerge)Removed [kCWScanKeyRestTime](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeyresttime)Removed [kCWScanKeySSID](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeyssid)Removed [kCWScanKeyScanType](https://developer.apple.com/documentation/corewlan/corewlanconstants.h/global_constants/kcwscankeyscantype)CoreWLANTypes.hRemoved CWInterfaceStateRemoved CWOpModeRemoved CWScanTypeRemoved CWSecurityModeRemoved kCWAuthAlgUnsupportedErrRemoved [kCWError](https://developer.apple.com/documentation/corewlan/corewlantypes.h/kcwparamerr/kcwerror)Removed kCWFormatErrRemoved kCWHTFeaturesNotSupportedRemoved kCWIPCErrorRemoved [kCWInterfaceStateAssociating](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestateassociating)Removed [kCWInterfaceStateAuthenticating](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestateauthenticating)Removed [kCWInterfaceStateInactive](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestateinactive)Removed [kCWInterfaceStateRunning](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestaterunning)Removed [kCWInterfaceStateScanning](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwinterfacestate/kcwinterfacestatescanning)Removed kCWInvalidAuthSeqNumErrRemoved kCWInvalidInfoElementErrRemoved kCWNoMemErrRemoved [kCWOpModeHostAP](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodehostap)Removed [kCWOpModeIBSS](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodeibss)Removed [kCWOpModeMonitorMode](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodemonitormode)Removed [kCWOpModeStation](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwopmode/kcwopmodestation)Removed kCWOpNotPermittedRemoved kCWPCOTransitionTimeNotSupportedRemoved kCWPHYMode11ARemoved kCWPHYMode11BRemoved kCWPHYMode11GRemoved kCWPHYMode11NRemoved kCWParamErrRemoved kCWRefNotBoundErrRemoved [kCWScanTypeActive](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwscantype/kcwscantypeactive)Removed [kCWScanTypeFast](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwscantype/kcwscantypefast)Removed [kCWScanTypePassive](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwscantype/kcwscantypepassive)Removed [kCWSecurityModeDynamicWEP](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodedynamicwep)Removed [kCWSecurityModeOpen](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodeopen)Removed [kCWSecurityModeWEP](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewep)Removed [kCWSecurityModeWPA2_Enterprise](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa2_enterprise)Removed [kCWSecurityModeWPA2_PSK](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa2_psk)Removed [kCWSecurityModeWPA_Enterprise](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa_enterprise)Removed [kCWSecurityModeWPA_PSK](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewpa_psk)Removed [kCWSecurityModeWPS](https://developer.apple.com/documentation/corewlan/corewlantypes.h/cwsecuritymode/kcwsecuritymodewps)Removed kCWUknownErrAdded [CWKeychainDomain](https://developer.apple.com/documentation/corewlan/cwkeychaindomain)Added [kCWChannelWidth160MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth160mhz)Added [kCWChannelWidth80MHz](https://developer.apple.com/documentation/corewlan/cwchannelwidth/kcwchannelwidth80mhz)Added [kCWKeychainDomainNone](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/none)Added [kCWKeychainDomainSystem](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/kcwkeychaindomainsystem)Added [kCWKeychainDomainUser](https://developer.apple.com/documentation/corewlan/cwkeychaindomain/kcwkeychaindomainuser)Added [kCWPHYMode11ac](https://developer.apple.com/documentation/corewlan/cwphymode/kcwphymode11ac)CoreWLANUtil.hAdded [CWKeychainCopyWiFiEAPIdentity()](https://developer.apple.com/documentation/corewlan/1512372-cwkeychaincopywifieapidentity)Added [CWKeychainDeleteWiFiEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1512239-cwkeychaindeletewifieapusernamea)Added [CWKeychainDeleteWiFiPassword()](https://developer.apple.com/documentation/corewlan/1512242-cwkeychaindeletewifipassword)Added [CWKeychainFindWiFiEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1512198-cwkeychainfindwifieapusernameand)Added [CWKeychainFindWiFiPassword()](https://developer.apple.com/documentation/corewlan/1512359-cwkeychainfindwifipassword)Added [CWKeychainSetWiFiEAPIdentity()](https://developer.apple.com/documentation/corewlan/1512453-cwkeychainsetwifieapidentity)Added [CWKeychainSetWiFiEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1512305-cwkeychainsetwifieapusernameandp)Added [CWKeychainSetWiFiPassword()](https://developer.apple.com/documentation/corewlan/1512429-cwkeychainsetwifipassword)Modified [CWKeychainCopyEAPIdentity()](https://developer.apple.com/documentation/corewlan/1569166-cwkeychaincopyeapidentity)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainCopyEAPIdentityList()](https://developer.apple.com/documentation/corewlan/1512258-cwkeychaincopyeapidentitylist)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainCopyEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569173-cwkeychaincopyeapusernameandpass)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainCopyPassword()](https://developer.apple.com/documentation/corewlan/1569169-cwkeychaincopypassword)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainDeleteEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569171-cwkeychaindeleteeapusernameandpa)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainDeletePassword()](https://developer.apple.com/documentation/corewlan/1569170-cwkeychaindeletepassword)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainSetEAPIdentity()](https://developer.apple.com/documentation/corewlan/1569167-cwkeychainseteapidentity)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainSetEAPUsernameAndPassword()](https://developer.apple.com/documentation/corewlan/1569172-cwkeychainseteapusernameandpassw)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [CWKeychainSetPassword()](https://developer.apple.com/documentation/corewlan/1569168-cwkeychainsetpassword)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

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
