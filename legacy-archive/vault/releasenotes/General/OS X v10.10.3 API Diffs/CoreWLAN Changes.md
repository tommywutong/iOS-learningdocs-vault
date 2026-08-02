---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreWLAN.html
archived_at: '2026-07-18T02:52:17.814476Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreWLAN Changes

## CoreWLAN

Removed CWCipherKeyFlags.valueRemoved CWConfiguration.configurationWithConfiguration(CWConfiguration!) -> Self! [class]Removed CWNetworkProfile.networkProfileWithNetworkProfile(CWNetworkProfile!) -> Self! [class]Added CWCipherKeyFlags.init(rawValue: UInt)Added CWInterface.commitConfiguration(CWConfiguration!, authorization: SFAuthorization!, error: NSErrorPointer) -> BoolModified CWChannel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWChannel.channelBand

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWChannel.channelNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWChannel.channelWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWChannel.isEqualToChannel(CWChannel!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWChannelBand [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWChannelWidth [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWCipherKeyFlags [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct CWCipherKeyFlags : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var None: CWCipherKeyFlags { get }     static var Unicast: CWCipherKeyFlags { get }     static var Multicast: CWCipherKeyFlags { get }     static var Tx: CWCipherKeyFlags { get }     static var Rx: CWCipherKeyFlags { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct CWCipherKeyFlags : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: CWCipherKeyFlags { get }     static var Unicast: CWCipherKeyFlags { get }     static var Multicast: CWCipherKeyFlags { get }     static var Tx: CWCipherKeyFlags { get }     static var Rx: CWCipherKeyFlags { get } } ``` | RawOptionSetType | OS X 10.7 |

Modified CWCipherKeyFlags.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified CWConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWConfiguration.init()

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init() ``` | OS X 10.10 |
| To | ``` init!() ``` | OS X 10.6 |

Modified CWConfiguration.init(configuration: CWConfiguration!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(configuration configuration: CWConfiguration!) ``` | OS X 10.10 |
| To | ``` init!(configuration configuration: CWConfiguration!) ``` | OS X 10.7 |

Modified CWConfiguration.isEqualToConfiguration(CWConfiguration!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWConfiguration.networkProfiles

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var networkProfiles: NSOrderedSet! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var networkProfiles: NSOrderedSet! { get } ``` | OS X 10.7 |

Modified CWConfiguration.rememberJoinedNetworks

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWConfiguration.requireAdministratorForAssociation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWConfiguration.requireAdministratorForIBSSMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWConfiguration.requireAdministratorForPower

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWErr [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWEventDelegate.bssidDidChangeForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.clientConnectionInterrupted()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.clientConnectionInvalidated()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.countryCodeDidChangeForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.linkDidChangeForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.linkQualityDidChangeForWiFiInterfaceWithName(String!, rssi: Int, transmitRate: Double)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.modeDidChangeForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.powerStateDidChangeForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.scanCacheUpdatedForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWEventDelegate.ssidDidChangeForWiFiInterfaceWithName(String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified CWIBSSModeSecurity [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.activePHYMode() -> CWPHYMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.associateToEnterpriseNetwork(CWNetwork!, identity: SecIdentity!, username: String!, password: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.associateToNetwork(CWNetwork!, password: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.bssid() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.cachedScanResults() -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func cachedScanResults() -> NSSet! ``` | OS X 10.10 |
| To | ``` func cachedScanResults() -> Set<NSObject>! ``` | OS X 10.7 |

Modified CWInterface.configuration() -> CWConfiguration!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.countryCode() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.disassociate()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.hardwareAddress() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.interfaceMode() -> CWInterfaceMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.interfaceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.init(interfaceName: String!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(interfaceName name: String!) ``` | OS X 10.10 | -- |
| To | ``` init!(interfaceName name: String!) ``` | OS X 10.6 | OS X 10.10 |

Modified CWInterface.interfaceNames() -> Set<NSObject>! [class]

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func interfaceNames() -> NSSet! ``` | OS X 10.10 | -- |
| To | ``` class func interfaceNames() -> Set<NSObject>! ``` | OS X 10.6 | OS X 10.10 |

Modified CWInterface.init(name: String!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` convenience init(name name: String!) ``` | OS X 10.10 | -- |
| To | ``` convenience init!(name name: String!) ``` | OS X 10.6 | OS X 10.10 |

Modified CWInterface.noiseMeasurement() -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.powerOn() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.rssiValue() -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.scanForNetworksWithName(String!, error: NSErrorPointer) -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanForNetworksWithName(_ networkName: String!, error error: NSErrorPointer) -> NSSet! ``` | OS X 10.10 |
| To | ``` func scanForNetworksWithName(_ networkName: String!, error error: NSErrorPointer) -> Set<NSObject>! ``` | OS X 10.7 |

Modified CWInterface.scanForNetworksWithSSID(NSData!, error: NSErrorPointer) -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func scanForNetworksWithSSID(_ ssid: NSData!, error error: NSErrorPointer) -> NSSet! ``` | OS X 10.10 |
| To | ``` func scanForNetworksWithSSID(_ ssid: NSData!, error error: NSErrorPointer) -> Set<NSObject>! ``` | OS X 10.7 |

Modified CWInterface.security() -> CWSecurity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.serviceActive() -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.setPairwiseMasterKey(NSData!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.setPower(Bool, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.setWEPKey(NSData!, flags: CWCipherKeyFlags, index: Int, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.setWLANChannel(CWChannel!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.ssid() -> String!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWInterface.ssidData() -> NSData!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.startIBSSModeWithSSID(NSData!, security: CWIBSSModeSecurity, channel: Int, password: String!, error: NSErrorPointer) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.supportedWLANChannels() -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func supportedWLANChannels() -> NSSet! ``` | OS X 10.10 |
| To | ``` func supportedWLANChannels() -> Set<NSObject>! ``` | OS X 10.7 |

Modified CWInterface.transmitPower() -> Int

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.transmitRate() -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterface.wlanChannel() -> CWChannel!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWInterfaceMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWMutableConfiguration.networkProfiles

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var networkProfiles: NSOrderedSet! ``` | OS X 10.10 |
| To | ``` @NSCopying var networkProfiles: NSOrderedSet! ``` | OS X 10.7 |

Modified CWMutableConfiguration.rememberJoinedNetworks

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableConfiguration.requireAdministratorForAssociation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableConfiguration.requireAdministratorForIBSSMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableConfiguration.requireAdministratorForPower

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableNetworkProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableNetworkProfile.security

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWMutableNetworkProfile.ssidData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var ssidData: NSData! ``` | OS X 10.10 |
| To | ``` @NSCopying var ssidData: NSData! ``` | OS X 10.7 |

Modified CWNetwork

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWNetwork.beaconInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.bssid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWNetwork.countryCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.ibss

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.informationElementData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.isEqualToNetwork(CWNetwork!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWNetwork.noiseMeasurement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.rssiValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.ssid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CWNetwork.ssidData

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.supportsPHYMode(CWPHYMode) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CWNetwork.supportsSecurity(CWSecurity) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetwork.wlanChannel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetworkProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetworkProfile.init()

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init() ``` | OS X 10.10 |
| To | ``` init!() ``` | OS X 10.7 |

Modified CWNetworkProfile.isEqualToNetworkProfile(CWNetworkProfile!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetworkProfile.init(networkProfile: CWNetworkProfile!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(networkProfile networkProfile: CWNetworkProfile!) ``` | OS X 10.10 |
| To | ``` init!(networkProfile networkProfile: CWNetworkProfile!) ``` | OS X 10.7 |

Modified CWNetworkProfile.security

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetworkProfile.ssid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWNetworkProfile.ssidData

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var ssidData: NSData! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var ssidData: NSData! { get } ``` | OS X 10.7 |

Modified CWPHYMode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWSecurity [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CWWiFiClient.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CWWiFiClient.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` weak var delegate: AnyObject! ``` |

Modified CWBSSIDDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWBSSIDDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWBSSIDDidChangeNotification: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWCountryCodeDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWCountryCodeDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWCountryCodeDidChangeNotification: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CWErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let CWErrorDomain: String ``` | OS X 10.7 |

Modified CWKeychainCopyEAPIdentityList(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CWKeychainCopyEAPIdentityList(_ list: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CWKeychainCopyEAPIdentityList(_ list: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.7 |

Modified CWKeychainCopyWiFiEAPIdentity(CWKeychainDomain, NSData!, UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CWKeychainCopyWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData!, _ identity: UnsafePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CWKeychainCopyWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData!, _ identity: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` | OS X 10.9 |

Modified CWKeychainDeleteWiFiEAPUsernameAndPassword(CWKeychainDomain, NSData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CWKeychainDeleteWiFiPassword(CWKeychainDomain, NSData!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CWKeychainFindWiFiEAPUsernameAndPassword(CWKeychainDomain, NSData!, AutoreleasingUnsafeMutablePointer<NSString?>, AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CWKeychainFindWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ username: AutoreleasingUnsafePointer<NSString?>, _ password: AutoreleasingUnsafePointer<NSString?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CWKeychainFindWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ username: AutoreleasingUnsafeMutablePointer<NSString?>, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` | OS X 10.9 |

Modified CWKeychainFindWiFiPassword(CWKeychainDomain, NSData!, AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ password: AutoreleasingUnsafePointer<NSString?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` | OS X 10.9 |

Modified CWKeychainSetWiFiEAPIdentity(CWKeychainDomain, NSData!, SecIdentity!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CWKeychainSetWiFiEAPUsernameAndPassword(CWKeychainDomain, NSData!, String!, String!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CWKeychainSetWiFiPassword(CWKeychainDomain, NSData!, String!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CWLinkDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWLinkDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWLinkDidChangeNotification: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWLinkQualityDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWLinkQualityDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWLinkQualityDidChangeNotification: String ``` | OS X 10.7 | OS X 10.10 |

Modified CWLinkQualityNotificationRSSIKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWLinkQualityNotificationRSSIKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWLinkQualityNotificationRSSIKey: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWLinkQualityNotificationTransmitRateKey

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWLinkQualityNotificationTransmitRateKey: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWLinkQualityNotificationTransmitRateKey: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWMergeNetworks(Set<NSObject>!) -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CWMergeNetworks(_ networks: NSSet!) -> NSSet! ``` | OS X 10.10 |
| To | ``` func CWMergeNetworks(_ networks: Set<NSObject>!) -> Set<NSObject>! ``` | OS X 10.7 |

Modified CWModeDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWModeDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWModeDidChangeNotification: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWPowerDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWPowerDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWPowerDidChangeNotification: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWSSIDDidChangeNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWSSIDDidChangeNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWSSIDDidChangeNotification: String ``` | OS X 10.6 | OS X 10.10 |

Modified CWScanCacheDidUpdateNotification

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` let CWScanCacheDidUpdateNotification: NSString! ``` | OS X 10.10 | -- |
| To | ``` let CWScanCacheDidUpdateNotification: String ``` | OS X 10.7 | OS X 10.10 |

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
