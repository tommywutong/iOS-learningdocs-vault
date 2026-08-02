---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/CoreWLAN.html
archived_at: '2026-07-15T07:34:53.017013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreWLAN Changes

## CoreWLAN (Added)

Added CWChannelAdded CWChannel.channelBandAdded CWChannel.channelNumberAdded CWChannel.channelWidthAdded CWChannel.isEqualToChannel(CWChannel!) -> BoolAdded CWChannelBand [enum]Added CWChannelBand.Band2GHzAdded CWChannelBand.Band5GHzAdded CWChannelBand.BandUnknownAdded CWChannelWidth [enum]Added CWChannelWidth.Width160MHzAdded CWChannelWidth.Width20MHzAdded CWChannelWidth.Width40MHzAdded CWChannelWidth.Width80MHzAdded CWChannelWidth.WidthUnknownAdded CWCipherKeyFlags [struct]Added CWCipherKeyFlags.MulticastAdded CWCipherKeyFlags.NoneAdded CWCipherKeyFlags.RxAdded CWCipherKeyFlags.TxAdded CWCipherKeyFlags.UnicastAdded CWCipherKeyFlags.init(_: UInt)Added CWCipherKeyFlags.init(rawValue: UInt)Added CWConfigurationAdded CWConfiguration.init()Added CWConfiguration.init(configuration: CWConfiguration!)Added CWConfiguration.isEqualToConfiguration(CWConfiguration!) -> BoolAdded CWConfiguration.networkProfilesAdded CWConfiguration.rememberJoinedNetworksAdded CWConfiguration.requireAdministratorForAssociationAdded CWConfiguration.requireAdministratorForIBSSModeAdded CWConfiguration.requireAdministratorForPowerAdded CWErr [enum]Added CWErr.CWAPFullErrAdded CWErr.CWAssociationDeniedErrAdded CWErr.CWAuthenticationAlgorithmUnsupportedErrAdded CWErr.CWChallengeFailureErrAdded CWErr.CWCipherSuiteRejectedErrAdded CWErr.CWDSSSOFDMUnsupportedErrAdded CWErr.CWEAPOLErrAdded CWErr.CWErrAdded CWErr.CWHTFeaturesNotSupportedErrAdded CWErr.CWIPCFailureErrAdded CWErr.CWInvalidAKMPErrAdded CWErr.CWInvalidAuthenticationSequenceNumberErrAdded CWErr.CWInvalidFormatErrAdded CWErr.CWInvalidGroupCipherErrAdded CWErr.CWInvalidInformationElementErrAdded CWErr.CWInvalidPMKErrAdded CWErr.CWInvalidPairwiseCipherErrAdded CWErr.CWInvalidParameterErrAdded CWErr.CWInvalidRSNCapabilitiesErrAdded CWErr.CWNoErrAdded CWErr.CWNoMemoryErrAdded CWErr.CWNotSupportedErrAdded CWErr.CWOperationNotPermittedErrAdded CWErr.CWPCOTransitionTimeNotSupportedErrAdded CWErr.CWReassociationDeniedErrAdded CWErr.CWReferenceNotBoundErrAdded CWErr.CWShortSlotUnsupportedErrAdded CWErr.CWSupplicantTimeoutErrAdded CWErr.CWTimeoutErrAdded CWErr.CWUnknownErrAdded CWErr.CWUnspecifiedFailureErrAdded CWErr.CWUnsupportedCapabilitiesErrAdded CWErr.CWUnsupportedRSNVersionErrAdded CWErr.CWUnsupportedRateSetErrAdded CWEventDelegateAdded CWEventDelegate.bssidDidChangeForWiFiInterfaceWithName(String!)Added CWEventDelegate.clientConnectionInterrupted()Added CWEventDelegate.clientConnectionInvalidated()Added CWEventDelegate.countryCodeDidChangeForWiFiInterfaceWithName(String!)Added CWEventDelegate.linkDidChangeForWiFiInterfaceWithName(String!)Added CWEventDelegate.linkQualityDidChangeForWiFiInterfaceWithName(String!, rssi: Int, transmitRate: Double)Added CWEventDelegate.modeDidChangeForWiFiInterfaceWithName(String!)Added CWEventDelegate.powerStateDidChangeForWiFiInterfaceWithName(String!)Added CWEventDelegate.scanCacheUpdatedForWiFiInterfaceWithName(String!)Added CWEventDelegate.ssidDidChangeForWiFiInterfaceWithName(String!)Added CWEventType [enum]Added CWEventType.BSSIDDidChangeAdded CWEventType.CountryCodeDidChangeAdded CWEventType.LinkDidChangeAdded CWEventType.LinkQualityDidChangeAdded CWEventType.ModeDidChangeAdded CWEventType.NoneAdded CWEventType.PowerDidChangeAdded CWEventType.SSIDDidChangeAdded CWEventType.ScanCacheUpdatedAdded CWEventType.UnknownAdded CWIBSSModeSecurity [enum]Added CWIBSSModeSecurity.NoneAdded CWIBSSModeSecurity.WEP104Added CWIBSSModeSecurity.WEP40Added CWInterfaceAdded CWInterface.activePHYMode() -> CWPHYModeAdded CWInterface.associateToEnterpriseNetwork(CWNetwork!, identity: SecIdentity!, username: String!, password: String!, error: NSErrorPointer) -> BoolAdded CWInterface.associateToNetwork(CWNetwork!, password: String!, error: NSErrorPointer) -> BoolAdded CWInterface.bssid() -> String!Added CWInterface.cachedScanResults() -> NSSet!Added CWInterface.commitConfiguration(CWConfiguration!, authorization: SFAuthorization!, error: NSErrorPointer) -> BoolAdded CWInterface.configuration() -> CWConfiguration!Added CWInterface.countryCode() -> String!Added CWInterface.disassociate()Added CWInterface.hardwareAddress() -> String!Added CWInterface.interfaceMode() -> CWInterfaceModeAdded CWInterface.interfaceNameAdded CWInterface.init(interfaceName: String!)Added CWInterface.interfaceNames() -> NSSet! [class]Added CWInterface.init(name: String!)Added CWInterface.noiseMeasurement() -> IntAdded CWInterface.powerOn() -> BoolAdded CWInterface.rssiValue() -> IntAdded CWInterface.scanForNetworksWithName(String!, error: NSErrorPointer) -> NSSet!Added CWInterface.scanForNetworksWithSSID(NSData!, error: NSErrorPointer) -> NSSet!Added CWInterface.security() -> CWSecurityAdded CWInterface.serviceActive() -> BoolAdded CWInterface.setPairwiseMasterKey(NSData!, error: NSErrorPointer) -> BoolAdded CWInterface.setPower(Bool, error: NSErrorPointer) -> BoolAdded CWInterface.setWEPKey(NSData!, flags: CWCipherKeyFlags, index: Int, error: NSErrorPointer) -> BoolAdded CWInterface.setWLANChannel(CWChannel!, error: NSErrorPointer) -> BoolAdded CWInterface.ssid() -> String!Added CWInterface.ssidData() -> NSData!Added CWInterface.startIBSSModeWithSSID(NSData!, security: CWIBSSModeSecurity, channel: Int, password: String!, error: NSErrorPointer) -> BoolAdded CWInterface.supportedWLANChannels() -> NSSet!Added CWInterface.transmitPower() -> IntAdded CWInterface.transmitRate() -> DoubleAdded CWInterface.wlanChannel() -> CWChannel!Added CWInterfaceMode [enum]Added CWInterfaceMode.HostAPAdded CWInterfaceMode.IBSSAdded CWInterfaceMode.NoneAdded CWInterfaceMode.StationAdded CWKeychainDomain [enum]Added CWKeychainDomain.NoneAdded CWKeychainDomain.SystemAdded CWKeychainDomain.UserAdded CWMutableConfigurationAdded CWMutableConfiguration.networkProfilesAdded CWMutableConfiguration.rememberJoinedNetworksAdded CWMutableConfiguration.requireAdministratorForAssociationAdded CWMutableConfiguration.requireAdministratorForIBSSModeAdded CWMutableConfiguration.requireAdministratorForPowerAdded CWMutableNetworkProfileAdded CWMutableNetworkProfile.securityAdded CWMutableNetworkProfile.ssidDataAdded CWNetworkAdded CWNetwork.beaconIntervalAdded CWNetwork.bssidAdded CWNetwork.countryCodeAdded CWNetwork.ibssAdded CWNetwork.informationElementDataAdded CWNetwork.isEqualToNetwork(CWNetwork!) -> BoolAdded CWNetwork.noiseMeasurementAdded CWNetwork.rssiValueAdded CWNetwork.ssidAdded CWNetwork.ssidDataAdded CWNetwork.supportsPHYMode(CWPHYMode) -> BoolAdded CWNetwork.supportsSecurity(CWSecurity) -> BoolAdded CWNetwork.wlanChannelAdded CWNetworkProfileAdded CWNetworkProfile.init()Added CWNetworkProfile.isEqualToNetworkProfile(CWNetworkProfile!) -> BoolAdded CWNetworkProfile.init(networkProfile: CWNetworkProfile!)Added CWNetworkProfile.securityAdded CWNetworkProfile.ssidAdded CWNetworkProfile.ssidDataAdded CWPHYMode [enum]Added CWPHYMode.Mode11aAdded CWPHYMode.Mode11acAdded CWPHYMode.Mode11bAdded CWPHYMode.Mode11gAdded CWPHYMode.Mode11nAdded CWPHYMode.ModeNoneAdded CWSecurity [enum]Added CWSecurity.DynamicWEPAdded CWSecurity.EnterpriseAdded CWSecurity.NoneAdded CWSecurity.PersonalAdded CWSecurity.UnknownAdded CWSecurity.WEPAdded CWSecurity.WPA2EnterpriseAdded CWSecurity.WPA2PersonalAdded CWSecurity.WPAEnterpriseAdded CWSecurity.WPAEnterpriseMixedAdded CWSecurity.WPAPersonalAdded CWSecurity.WPAPersonalMixedAdded CWWiFiClientAdded CWWiFiClient.init()Added CWWiFiClient.delegateAdded CWWiFiClient.interface() -> CWInterface!Added CWWiFiClient.interfaceNames() -> [AnyObject]! [class]Added CWWiFiClient.interfaceWithName(String!) -> CWInterface!Added CWWiFiClient.interfaces() -> [AnyObject]!Added CWWiFiClient.sharedWiFiClient() -> CWWiFiClient! [class]Added CWWiFiClient.startMonitoringEventWithType(CWEventType, error: NSErrorPointer) -> BoolAdded CWWiFiClient.stopMonitoringAllEventsAndReturnError(NSErrorPointer) -> BoolAdded CWWiFiClient.stopMonitoringEventWithType(CWEventType, error: NSErrorPointer) -> BoolAdded CWBSSIDDidChangeNotificationAdded CWCountryCodeDidChangeNotificationAdded CWErrorDomainAdded CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatusAdded CWKeychainCopyWiFiEAPIdentity(CWKeychainDomain, NSData!, UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatusAdded CWKeychainDeleteWiFiEAPUsernameAndPassword(CWKeychainDomain, NSData!) -> OSStatusAdded CWKeychainDeleteWiFiPassword(CWKeychainDomain, NSData!) -> OSStatusAdded CWKeychainFindWiFiEAPUsernameAndPassword(CWKeychainDomain, NSData!, AutoreleasingUnsafeMutablePointer<NSString?>, AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatusAdded CWKeychainFindWiFiPassword(CWKeychainDomain, NSData!, AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatusAdded CWKeychainSetWiFiEAPIdentity(CWKeychainDomain, NSData!, SecIdentity!) -> OSStatusAdded CWKeychainSetWiFiEAPUsernameAndPassword(CWKeychainDomain, NSData!, String!, String!) -> OSStatusAdded CWKeychainSetWiFiPassword(CWKeychainDomain, NSData!, String!) -> OSStatusAdded CWLinkDidChangeNotificationAdded CWLinkQualityDidChangeNotificationAdded CWLinkQualityNotificationRSSIKeyAdded CWLinkQualityNotificationTransmitRateKeyAdded CWMergeNetworks(NSSet!) -> NSSet!Added CWModeDidChangeNotificationAdded CWPowerDidChangeNotificationAdded CWSSIDDidChangeNotificationAdded CWScanCacheDidUpdateNotification

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
