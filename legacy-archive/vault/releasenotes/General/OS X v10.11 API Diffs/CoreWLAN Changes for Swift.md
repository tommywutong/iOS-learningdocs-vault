---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreWLAN.html
archived_at: '2026-07-18T02:53:30.389201Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreWLAN Changes for Swift

### CoreWLAN

Removed CWCipherKeyFlags.init(_: UInt)Modified [CWChannel](https://developer.apple.com/documentation/corewlan/cwchannel)

|  | Declaration |
| --- | --- |
| From | ``` class CWChannel : NSObject, NSCopying, NSSecureCoding, NSCoding {     var channelNumber: Int { get }     var channelWidth: CWChannelWidth { get }     var channelBand: CWChannelBand { get }     func isEqualToChannel(_ channel: CWChannel!) -> Bool } ``` |
| To | ``` class CWChannel : NSObject, NSCopying, NSSecureCoding, NSCoding {     var channelNumber: Int { get }     var channelWidth: CWChannelWidth { get }     var channelBand: CWChannelBand { get }     func isEqualToChannel(_ channel: CWChannel) -> Bool } ``` |

Modified [CWChannel.isEqualToChannel(_: CWChannel) -> Bool](https://developer.apple.com/documentation/corewlan/cwchannel/1512390-isequaltochannel)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToChannel(_ channel: CWChannel!) -> Bool ``` |
| To | ``` func isEqualToChannel(_ channel: CWChannel) -> Bool ``` |

Modified [CWChannelBand [enum]](https://developer.apple.com/documentation/corewlan/cwchannelband)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWChannelWidth [enum]](https://developer.apple.com/documentation/corewlan/cwchannelwidth)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWCipherKeyFlags [struct]](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CWCipherKeyFlags : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: CWCipherKeyFlags { get }     static var Unicast: CWCipherKeyFlags { get }     static var Multicast: CWCipherKeyFlags { get }     static var Tx: CWCipherKeyFlags { get }     static var Rx: CWCipherKeyFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CWCipherKeyFlags : OptionSetType {     init(rawValue rawValue: UInt)     static var None: CWCipherKeyFlags { get }     static var Unicast: CWCipherKeyFlags { get }     static var Multicast: CWCipherKeyFlags { get }     static var Tx: CWCipherKeyFlags { get }     static var Rx: CWCipherKeyFlags { get } } ``` | OptionSetType |

Modified [CWConfiguration](https://developer.apple.com/documentation/corewlan/cwconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` class CWConfiguration : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     @NSCopying var networkProfiles: NSOrderedSet! { get }     var requireAdministratorForAssociation: Bool { get }     var requireAdministratorForPower: Bool { get }     var requireAdministratorForIBSSMode: Bool { get }     var rememberJoinedNetworks: Bool { get }     convenience init!()     class func configuration() -> Self!     init!()     init!(configuration configuration: CWConfiguration!)     class func configurationWithConfiguration(_ configuration: CWConfiguration!) -> Self!     func isEqualToConfiguration(_ configuration: CWConfiguration!) -> Bool } ``` |
| To | ``` class CWConfiguration : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     @NSCopying var networkProfiles: NSOrderedSet { get }     var requireAdministratorForAssociation: Bool { get }     var requireAdministratorForPower: Bool { get }     var requireAdministratorForIBSSMode: Bool { get }     var rememberJoinedNetworks: Bool { get }     convenience init()     class func configuration() -> Self     init()     init(configuration configuration: CWConfiguration)     class func configurationWithConfiguration(_ configuration: CWConfiguration) -> Self     func isEqualToConfiguration(_ configuration: CWConfiguration) -> Bool } ``` |

Modified [CWConfiguration.init()](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507049-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CWConfiguration.init(configuration: CWConfiguration)](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507057-initwithconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` init!(configuration configuration: CWConfiguration!) ``` |
| To | ``` init(configuration configuration: CWConfiguration) ``` |

Modified [CWConfiguration.isEqualToConfiguration(_: CWConfiguration) -> Bool](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507064-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToConfiguration(_ configuration: CWConfiguration!) -> Bool ``` |
| To | ``` func isEqualToConfiguration(_ configuration: CWConfiguration) -> Bool ``` |

Modified [CWConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwconfiguration/1507055-networkprofiles)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var networkProfiles: NSOrderedSet! { get } ``` |
| To | ``` @NSCopying var networkProfiles: NSOrderedSet { get } ``` |

Modified [CWErr [enum]](https://developer.apple.com/documentation/corewlan/cwerr)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWEventDelegate](https://developer.apple.com/documentation/corewlan/cweventdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CWEventDelegate {     optional func clientConnectionInterrupted()     optional func clientConnectionInvalidated()     optional func powerStateDidChangeForWiFiInterfaceWithName(_ interfaceName: String!)     optional func ssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String!)     optional func bssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String!)     optional func countryCodeDidChangeForWiFiInterfaceWithName(_ interfaceName: String!)     optional func linkDidChangeForWiFiInterfaceWithName(_ interfaceName: String!)     optional func linkQualityDidChangeForWiFiInterfaceWithName(_ interfaceName: String!, rssi rssi: Int, transmitRate transmitRate: Double)     optional func modeDidChangeForWiFiInterfaceWithName(_ interfaceName: String!)     optional func scanCacheUpdatedForWiFiInterfaceWithName(_ interfaceName: String!) } ``` |
| To | ``` protocol CWEventDelegate {     optional func clientConnectionInterrupted()     optional func clientConnectionInvalidated()     optional func powerStateDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func ssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func bssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func countryCodeDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func linkDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func linkQualityDidChangeForWiFiInterfaceWithName(_ interfaceName: String, rssi rssi: Int, transmitRate transmitRate: Double)     optional func modeDidChangeForWiFiInterfaceWithName(_ interfaceName: String)     optional func scanCacheUpdatedForWiFiInterfaceWithName(_ interfaceName: String) } ``` |

Modified [CWEventDelegate.bssidDidChangeForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512367-bssiddidchangeforwifiinterfacewi)

|  | Declaration |
| --- | --- |
| From | ``` optional func bssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func bssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventDelegate.countryCodeDidChangeForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512342-countrycodedidchangeforwifiinter)

|  | Declaration |
| --- | --- |
| From | ``` optional func countryCodeDidChangeForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func countryCodeDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventDelegate.linkDidChangeForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512395-linkdidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func linkDidChangeForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func linkDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventDelegate.linkQualityDidChangeForWiFiInterfaceWithName(_: String, rssi: Int, transmitRate: Double)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512300-linkqualitydidchangeforwifiinter)

|  | Declaration |
| --- | --- |
| From | ``` optional func linkQualityDidChangeForWiFiInterfaceWithName(_ interfaceName: String!, rssi rssi: Int, transmitRate transmitRate: Double) ``` |
| To | ``` optional func linkQualityDidChangeForWiFiInterfaceWithName(_ interfaceName: String, rssi rssi: Int, transmitRate transmitRate: Double) ``` |

Modified [CWEventDelegate.modeDidChangeForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512226-modedidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func modeDidChangeForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func modeDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventDelegate.powerStateDidChangeForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512253-powerstatedidchangeforwifiinterf)

|  | Declaration |
| --- | --- |
| From | ``` optional func powerStateDidChangeForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func powerStateDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventDelegate.scanCacheUpdatedForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512322-scancacheupdatedforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func scanCacheUpdatedForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func scanCacheUpdatedForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventDelegate.ssidDidChangeForWiFiInterfaceWithName(_: String)](https://developer.apple.com/documentation/corewlan/cweventdelegate/1512422-ssiddidchangeforwifiinterface)

|  | Declaration |
| --- | --- |
| From | ``` optional func ssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String!) ``` |
| To | ``` optional func ssidDidChangeForWiFiInterfaceWithName(_ interfaceName: String) ``` |

Modified [CWEventType [enum]](https://developer.apple.com/documentation/corewlan/cweventtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWIBSSModeSecurity [enum]](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWInterface](https://developer.apple.com/documentation/corewlan/cwinterface)

|  | Declaration |
| --- | --- |
| From | ``` class CWInterface : NSObject {     var interfaceName: String! { get }     func powerOn() -> Bool     func supportedWLANChannels() -> Set<NSObject>!     func wlanChannel() -> CWChannel!     func activePHYMode() -> CWPHYMode     func ssid() -> String!     func ssidData() -> NSData!     func bssid() -> String!     func rssiValue() -> Int     func noiseMeasurement() -> Int     func security() -> CWSecurity     func transmitRate() -> Double     func countryCode() -> String!     func interfaceMode() -> CWInterfaceMode     func transmitPower() -> Int     func hardwareAddress() -> String!     func serviceActive() -> Bool     func cachedScanResults() -> Set<NSObject>!     func configuration() -> CWConfiguration!     class func interfaceNames() -> Set<NSObject>!     convenience init!()     class func interface() -> Self!     convenience init!(name name: String!)     class func interfaceWithName(_ name: String!) -> Self!     init!(interfaceName name: String!)     func setPower(_ power: Bool, error error: NSErrorPointer) -> Bool     func setWLANChannel(_ channel: CWChannel!, error error: NSErrorPointer) -> Bool     func setPairwiseMasterKey(_ key: NSData!, error error: NSErrorPointer) -> Bool     func setWEPKey(_ key: NSData!, flags flags: CWCipherKeyFlags, index index: Int, error error: NSErrorPointer) -> Bool     func scanForNetworksWithSSID(_ ssid: NSData!, error error: NSErrorPointer) -> Set<NSObject>!     func scanForNetworksWithName(_ networkName: String!, error error: NSErrorPointer) -> Set<NSObject>!     func associateToNetwork(_ network: CWNetwork!, password password: String!, error error: NSErrorPointer) -> Bool     func disassociate()     func associateToEnterpriseNetwork(_ network: CWNetwork!, identity identity: SecIdentity!, username username: String!, password password: String!, error error: NSErrorPointer) -> Bool     func startIBSSModeWithSSID(_ ssidData: NSData!, security security: CWIBSSModeSecurity, channel channel: Int, password password: String!, error error: NSErrorPointer) -> Bool     func commitConfiguration(_ configuration: CWConfiguration!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool } ``` |
| To | ``` class CWInterface : NSObject {     var interfaceName: String? { get }     func powerOn() -> Bool     func supportedWLANChannels() -> Set<CWChannel>?     func wlanChannel() -> CWChannel?     func activePHYMode() -> CWPHYMode     func ssid() -> String?     func ssidData() -> NSData?     func bssid() -> String?     func rssiValue() -> Int     func noiseMeasurement() -> Int     func security() -> CWSecurity     func transmitRate() -> Double     func countryCode() -> String?     func interfaceMode() -> CWInterfaceMode     func transmitPower() -> Int     func hardwareAddress() -> String?     func serviceActive() -> Bool     func cachedScanResults() -> Set<CWNetwork>?     func configuration() -> CWConfiguration?     class func interfaceNames() -> Set<String>?     convenience init()     class func interface() -> Self     convenience init(name name: String)     class func interfaceWithName(_ name: String) -> Self     init(interfaceName name: String)     func setPower(_ power: Bool) throws     func setWLANChannel(_ channel: CWChannel) throws     func setPairwiseMasterKey(_ key: NSData?) throws     func setWEPKey(_ key: NSData?, flags flags: CWCipherKeyFlags, index index: Int) throws     func scanForNetworksWithSSID(_ ssid: NSData?) throws -> Set<CWNetwork>     func scanForNetworksWithName(_ networkName: String?) throws -> Set<CWNetwork>     func associateToNetwork(_ network: CWNetwork, password password: String?) throws     func disassociate()     func associateToEnterpriseNetwork(_ network: CWNetwork, identity identity: SecIdentity?, username username: String?, password password: String?) throws     func startIBSSModeWithSSID(_ ssidData: NSData, security security: CWIBSSModeSecurity, channel channel: Int, password password: String?) throws     func commitConfiguration(_ configuration: CWConfiguration, authorization authorization: SFAuthorization?) throws } ``` |

Modified [CWInterface.associateToEnterpriseNetwork(_: CWNetwork, identity: SecIdentity?, username: String?, password: String?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426468-associate)

|  | Declaration |
| --- | --- |
| From | ``` func associateToEnterpriseNetwork(_ network: CWNetwork!, identity identity: SecIdentity!, username username: String!, password password: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func associateToEnterpriseNetwork(_ network: CWNetwork, identity identity: SecIdentity?, username username: String?, password password: String?) throws ``` |

Modified [CWInterface.associateToNetwork(_: CWNetwork, password: String?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426455-associatetonetwork)

|  | Declaration |
| --- | --- |
| From | ``` func associateToNetwork(_ network: CWNetwork!, password password: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func associateToNetwork(_ network: CWNetwork, password password: String?) throws ``` |

Modified [CWInterface.bssid() -> String?](https://developer.apple.com/documentation/corewlan/cwinterface/1426450-bssid)

|  | Declaration |
| --- | --- |
| From | ``` func bssid() -> String! ``` |
| To | ``` func bssid() -> String? ``` |

Modified [CWInterface.cachedScanResults() -> Set<CWNetwork>?](https://developer.apple.com/documentation/corewlan/cwinterface/1426424-cachedscanresults)

|  | Declaration |
| --- | --- |
| From | ``` func cachedScanResults() -> Set<NSObject>! ``` |
| To | ``` func cachedScanResults() -> Set<CWNetwork>? ``` |

Modified [CWInterface.commitConfiguration(_: CWConfiguration, authorization: SFAuthorization?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426430-commitconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func commitConfiguration(_ configuration: CWConfiguration!, authorization authorization: SFAuthorization!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func commitConfiguration(_ configuration: CWConfiguration, authorization authorization: SFAuthorization?) throws ``` |

Modified [CWInterface.configuration() -> CWConfiguration?](https://developer.apple.com/documentation/corewlan/cwinterface/1426446-configuration)

|  | Declaration |
| --- | --- |
| From | ``` func configuration() -> CWConfiguration! ``` |
| To | ``` func configuration() -> CWConfiguration? ``` |

Modified [CWInterface.countryCode() -> String?](https://developer.apple.com/documentation/corewlan/cwinterface/1426412-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` func countryCode() -> String! ``` |
| To | ``` func countryCode() -> String? ``` |

Modified [CWInterface.hardwareAddress() -> String?](https://developer.apple.com/documentation/corewlan/cwinterface/1426466-hardwareaddress)

|  | Declaration |
| --- | --- |
| From | ``` func hardwareAddress() -> String! ``` |
| To | ``` func hardwareAddress() -> String? ``` |

Modified [CWInterface.init(interfaceName: String)](https://developer.apple.com/documentation/corewlan/cwinterface/1426442-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(interfaceName name: String!) ``` |
| To | ``` init(interfaceName name: String) ``` |

Modified [CWInterface.init(name: String)](https://developer.apple.com/documentation/corewlan/cwinterface/1426460-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(name name: String!) ``` |
| To | ``` convenience init(name name: String) ``` |

Modified [CWInterface.interfaceName](https://developer.apple.com/documentation/corewlan/cwinterface/1426462-interfacename)

|  | Declaration |
| --- | --- |
| From | ``` var interfaceName: String! { get } ``` |
| To | ``` var interfaceName: String? { get } ``` |

Modified [CWInterface.interfaceNames() -> Set<String>? [class]](https://developer.apple.com/documentation/corewlan/cwinterface/1426457-interfacenames)

|  | Declaration |
| --- | --- |
| From | ``` class func interfaceNames() -> Set<NSObject>! ``` |
| To | ``` class func interfaceNames() -> Set<String>? ``` |

Modified [CWInterface.scanForNetworksWithName(_: String?) throws -> Set<CWNetwork>](https://developer.apple.com/documentation/corewlan/cwinterface/1426416-scanfornetworkswithname)

|  | Declaration |
| --- | --- |
| From | ``` func scanForNetworksWithName(_ networkName: String!, error error: NSErrorPointer) -> Set<NSObject>! ``` |
| To | ``` func scanForNetworksWithName(_ networkName: String?) throws -> Set<CWNetwork> ``` |

Modified [CWInterface.scanForNetworksWithSSID(_: NSData?) throws -> Set<CWNetwork>](https://developer.apple.com/documentation/corewlan/cwinterface/1426436-scanfornetworkswithssid)

|  | Declaration |
| --- | --- |
| From | ``` func scanForNetworksWithSSID(_ ssid: NSData!, error error: NSErrorPointer) -> Set<NSObject>! ``` |
| To | ``` func scanForNetworksWithSSID(_ ssid: NSData?) throws -> Set<CWNetwork> ``` |

Modified [CWInterface.setPairwiseMasterKey(_: NSData?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426458-setpairwisemasterkey)

|  | Declaration |
| --- | --- |
| From | ``` func setPairwiseMasterKey(_ key: NSData!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setPairwiseMasterKey(_ key: NSData?) throws ``` |

Modified [CWInterface.setPower(_: Bool) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426451-setpower)

|  | Declaration |
| --- | --- |
| From | ``` func setPower(_ power: Bool, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setPower(_ power: Bool) throws ``` |

Modified [CWInterface.setWEPKey(_: NSData?, flags: CWCipherKeyFlags, index: Int) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426440-setwepkey)

|  | Declaration |
| --- | --- |
| From | ``` func setWEPKey(_ key: NSData!, flags flags: CWCipherKeyFlags, index index: Int, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setWEPKey(_ key: NSData?, flags flags: CWCipherKeyFlags, index index: Int) throws ``` |

Modified [CWInterface.setWLANChannel(_: CWChannel) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426418-setwlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` func setWLANChannel(_ channel: CWChannel!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func setWLANChannel(_ channel: CWChannel) throws ``` |

Modified [CWInterface.ssid() -> String?](https://developer.apple.com/documentation/corewlan/cwinterface/1426441-ssid)

|  | Declaration |
| --- | --- |
| From | ``` func ssid() -> String! ``` |
| To | ``` func ssid() -> String? ``` |

Modified [CWInterface.ssidData() -> NSData?](https://developer.apple.com/documentation/corewlan/cwinterface/1426434-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` func ssidData() -> NSData! ``` |
| To | ``` func ssidData() -> NSData? ``` |

Modified [CWInterface.startIBSSModeWithSSID(_: NSData, security: CWIBSSModeSecurity, channel: Int, password: String?) throws](https://developer.apple.com/documentation/corewlan/cwinterface/1426417-startibssmode)

|  | Declaration |
| --- | --- |
| From | ``` func startIBSSModeWithSSID(_ ssidData: NSData!, security security: CWIBSSModeSecurity, channel channel: Int, password password: String!, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func startIBSSModeWithSSID(_ ssidData: NSData, security security: CWIBSSModeSecurity, channel channel: Int, password password: String?) throws ``` |

Modified [CWInterface.supportedWLANChannels() -> Set<CWChannel>?](https://developer.apple.com/documentation/corewlan/cwinterface/1426420-supportedwlanchannels)

|  | Declaration |
| --- | --- |
| From | ``` func supportedWLANChannels() -> Set<NSObject>! ``` |
| To | ``` func supportedWLANChannels() -> Set<CWChannel>? ``` |

Modified [CWInterface.wlanChannel() -> CWChannel?](https://developer.apple.com/documentation/corewlan/cwinterface/1426426-wlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` func wlanChannel() -> CWChannel! ``` |
| To | ``` func wlanChannel() -> CWChannel? ``` |

Modified [CWInterfaceMode [enum]](https://developer.apple.com/documentation/corewlan/cwinterfacemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWKeychainDomain [enum]](https://developer.apple.com/documentation/corewlan/cwkeychaindomain)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWMutableConfiguration](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` class CWMutableConfiguration : CWConfiguration {     @NSCopying var networkProfiles: NSOrderedSet!     var requireAdministratorForAssociation: Bool     var requireAdministratorForPower: Bool     var requireAdministratorForIBSSMode: Bool     var rememberJoinedNetworks: Bool } ``` |
| To | ``` class CWMutableConfiguration : CWConfiguration {     @NSCopying var networkProfiles: NSOrderedSet     var requireAdministratorForAssociation: Bool     var requireAdministratorForPower: Bool     var requireAdministratorForIBSSMode: Bool     var rememberJoinedNetworks: Bool } ``` |

Modified [CWMutableConfiguration.networkProfiles](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration/1507065-networkprofiles)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var networkProfiles: NSOrderedSet! ``` |
| To | ``` @NSCopying var networkProfiles: NSOrderedSet ``` |

Modified [CWMutableNetworkProfile](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` class CWMutableNetworkProfile : CWNetworkProfile {     @NSCopying var ssidData: NSData!     var security: CWSecurity } ``` |
| To | ``` class CWMutableNetworkProfile : CWNetworkProfile {     @NSCopying var ssidData: NSData     var security: CWSecurity } ``` |

Modified [CWMutableNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile/1512167-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var ssidData: NSData! ``` |
| To | ``` @NSCopying var ssidData: NSData ``` |

Modified [CWNetwork](https://developer.apple.com/documentation/corewlan/cwnetwork)

|  | Declaration |
| --- | --- |
| From | ``` class CWNetwork : NSObject, NSCopying, NSSecureCoding, NSCoding {     var ssid: String! { get }     var ssidData: NSData! { get }     var bssid: String! { get }     var wlanChannel: CWChannel! { get }     var rssiValue: Int { get }     var noiseMeasurement: Int { get }     var informationElementData: NSData! { get }     var countryCode: String! { get }     var beaconInterval: Int { get }     var ibss: Bool { get }     func isEqualToNetwork(_ network: CWNetwork!) -> Bool     func supportsSecurity(_ security: CWSecurity) -> Bool     func supportsPHYMode(_ phyMode: CWPHYMode) -> Bool } ``` |
| To | ``` class CWNetwork : NSObject, NSCopying, NSSecureCoding, NSCoding {     var ssid: String? { get }     var ssidData: NSData? { get }     var bssid: String? { get }     var wlanChannel: CWChannel { get }     var rssiValue: Int { get }     var noiseMeasurement: Int { get }     var informationElementData: NSData? { get }     var countryCode: String? { get }     var beaconInterval: Int { get }     var ibss: Bool { get }     func isEqualToNetwork(_ network: CWNetwork) -> Bool     func supportsSecurity(_ security: CWSecurity) -> Bool     func supportsPHYMode(_ phyMode: CWPHYMode) -> Bool } ``` |

Modified [CWNetwork.bssid](https://developer.apple.com/documentation/corewlan/cwnetwork/1512224-bssid)

|  | Declaration |
| --- | --- |
| From | ``` var bssid: String! { get } ``` |
| To | ``` var bssid: String? { get } ``` |

Modified [CWNetwork.countryCode](https://developer.apple.com/documentation/corewlan/cwnetwork/1512435-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` var countryCode: String! { get } ``` |
| To | ``` var countryCode: String? { get } ``` |

Modified [CWNetwork.informationElementData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512236-informationelementdata)

|  | Declaration |
| --- | --- |
| From | ``` var informationElementData: NSData! { get } ``` |
| To | ``` var informationElementData: NSData? { get } ``` |

Modified [CWNetwork.isEqualToNetwork(_: CWNetwork) -> Bool](https://developer.apple.com/documentation/corewlan/cwnetwork/1512228-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToNetwork(_ network: CWNetwork!) -> Bool ``` |
| To | ``` func isEqualToNetwork(_ network: CWNetwork) -> Bool ``` |

Modified [CWNetwork.ssid](https://developer.apple.com/documentation/corewlan/cwnetwork/1512318-ssid)

|  | Declaration |
| --- | --- |
| From | ``` var ssid: String! { get } ``` |
| To | ``` var ssid: String? { get } ``` |

Modified [CWNetwork.ssidData](https://developer.apple.com/documentation/corewlan/cwnetwork/1512419-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` var ssidData: NSData! { get } ``` |
| To | ``` var ssidData: NSData? { get } ``` |

Modified [CWNetwork.wlanChannel](https://developer.apple.com/documentation/corewlan/cwnetwork/1512212-wlanchannel)

|  | Declaration |
| --- | --- |
| From | ``` var wlanChannel: CWChannel! { get } ``` |
| To | ``` var wlanChannel: CWChannel { get } ``` |

Modified [CWNetworkProfile](https://developer.apple.com/documentation/corewlan/cwnetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` class CWNetworkProfile : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var ssid: String! { get }     @NSCopying var ssidData: NSData! { get }     var security: CWSecurity { get }     convenience init!()     class func networkProfile() -> Self!     init!()     init!(networkProfile networkProfile: CWNetworkProfile!)     class func networkProfileWithNetworkProfile(_ networkProfile: CWNetworkProfile!) -> Self!     func isEqualToNetworkProfile(_ networkProfile: CWNetworkProfile!) -> Bool } ``` |
| To | ``` class CWNetworkProfile : NSObject, NSCopying, NSMutableCopying, NSSecureCoding, NSCoding {     var ssid: String? { get }     @NSCopying var ssidData: NSData? { get }     var security: CWSecurity { get }     convenience init()     class func networkProfile() -> Self     init()     init(networkProfile networkProfile: CWNetworkProfile)     class func networkProfileWithNetworkProfile(_ networkProfile: CWNetworkProfile) -> Self     func isEqualToNetworkProfile(_ networkProfile: CWNetworkProfile) -> Bool } ``` |

Modified [CWNetworkProfile.init()](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512158-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CWNetworkProfile.init(networkProfile: CWNetworkProfile)](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512316-initwithnetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` init!(networkProfile networkProfile: CWNetworkProfile!) ``` |
| To | ``` init(networkProfile networkProfile: CWNetworkProfile) ``` |

Modified [CWNetworkProfile.isEqualToNetworkProfile(_: CWNetworkProfile) -> Bool](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512221-isequaltonetworkprofile)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToNetworkProfile(_ networkProfile: CWNetworkProfile!) -> Bool ``` |
| To | ``` func isEqualToNetworkProfile(_ networkProfile: CWNetworkProfile) -> Bool ``` |

Modified [CWNetworkProfile.ssid](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512448-ssid)

|  | Declaration |
| --- | --- |
| From | ``` var ssid: String! { get } ``` |
| To | ``` var ssid: String? { get } ``` |

Modified [CWNetworkProfile.ssidData](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/1512244-ssiddata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var ssidData: NSData! { get } ``` |
| To | ``` @NSCopying var ssidData: NSData? { get } ``` |

Modified [CWPHYMode [enum]](https://developer.apple.com/documentation/corewlan/cwphymode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWSecurity [enum]](https://developer.apple.com/documentation/corewlan/cwsecurity)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CWWiFiClient](https://developer.apple.com/documentation/corewlan/cwwificlient)

|  | Declaration |
| --- | --- |
| From | ``` class CWWiFiClient : NSObject {     weak var delegate: AnyObject!     class func sharedWiFiClient() -> CWWiFiClient!     init!()     func interface() -> CWInterface!     class func interfaceNames() -> [AnyObject]!     func interfaceWithName(_ interfaceName: String!) -> CWInterface!     func interfaces() -> [AnyObject]!     func startMonitoringEventWithType(_ type: CWEventType, error error: NSErrorPointer) -> Bool     func stopMonitoringEventWithType(_ type: CWEventType, error error: NSErrorPointer) -> Bool     func stopMonitoringAllEventsAndReturnError(_ error: NSErrorPointer) -> Bool } ``` |
| To | ``` class CWWiFiClient : NSObject {     weak var delegate: AnyObject?     class func sharedWiFiClient() -> CWWiFiClient     init?()     func interface() -> CWInterface?     class func interfaceNames() -> [String]?     func interfaceWithName(_ interfaceName: String?) -> CWInterface?     func interfaces() -> [CWInterface]?     func startMonitoringEventWithType(_ type: CWEventType) throws     func stopMonitoringEventWithType(_ type: CWEventType) throws     func stopMonitoringAllEvents() throws } ``` |

Modified [CWWiFiClient.delegate](https://developer.apple.com/documentation/corewlan/cwwificlient/1512387-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: AnyObject! ``` |
| To | ``` weak var delegate: AnyObject? ``` |

Modified [CWWiFiClient.init()](https://developer.apple.com/documentation/corewlan/cwwificlient/1512206-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init?() ``` |

Modified [CWWiFiClient.interface() -> CWInterface?](https://developer.apple.com/documentation/corewlan/cwwificlient/1512352-interface)

|  | Declaration |
| --- | --- |
| From | ``` func interface() -> CWInterface! ``` |
| To | ``` func interface() -> CWInterface? ``` |

Modified [CWWiFiClient.interfaceNames() -> [String]? [class]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512194-interfacenames)

|  | Declaration |
| --- | --- |
| From | ``` class func interfaceNames() -> [AnyObject]! ``` |
| To | ``` class func interfaceNames() -> [String]? ``` |

Modified [CWWiFiClient.interfaces() -> [CWInterface]?](https://developer.apple.com/documentation/corewlan/cwwificlient/1512313-interfaces)

|  | Declaration |
| --- | --- |
| From | ``` func interfaces() -> [AnyObject]! ``` |
| To | ``` func interfaces() -> [CWInterface]? ``` |

Modified [CWWiFiClient.interfaceWithName(_: String?) -> CWInterface?](https://developer.apple.com/documentation/corewlan/cwwificlient/1512328-interfacewithname)

|  | Declaration |
| --- | --- |
| From | ``` func interfaceWithName(_ interfaceName: String!) -> CWInterface! ``` |
| To | ``` func interfaceWithName(_ interfaceName: String?) -> CWInterface? ``` |

Modified [CWWiFiClient.sharedWiFiClient() -> CWWiFiClient [class]](https://developer.apple.com/documentation/corewlan/cwwificlient/1512202-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedWiFiClient() -> CWWiFiClient! ``` |
| To | ``` class func sharedWiFiClient() -> CWWiFiClient ``` |

Modified [CWWiFiClient.startMonitoringEventWithType(_: CWEventType) throws](https://developer.apple.com/documentation/corewlan/cwwificlient/1512439-startmonitoringeventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` func startMonitoringEventWithType(_ type: CWEventType, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func startMonitoringEventWithType(_ type: CWEventType) throws ``` |

Modified [CWWiFiClient.stopMonitoringAllEvents() throws](https://developer.apple.com/documentation/corewlan/cwwificlient/1512370-stopmonitoringallevents)

|  | Declaration |
| --- | --- |
| From | ``` func stopMonitoringAllEventsAndReturnError(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func stopMonitoringAllEvents() throws ``` |

Modified [CWWiFiClient.stopMonitoringEventWithType(_: CWEventType) throws](https://developer.apple.com/documentation/corewlan/cwwificlient/1512446-stopmonitoringevent)

|  | Declaration |
| --- | --- |
| From | ``` func stopMonitoringEventWithType(_ type: CWEventType, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func stopMonitoringEventWithType(_ type: CWEventType) throws ``` |

Modified [CWKeychainCopyWiFiEAPIdentity(_: CWKeychainDomain, _: NSData, _: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512372-cwkeychaincopywifieapidentity)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainCopyWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData!, _ identity: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` |
| To | ``` func CWKeychainCopyWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData, _ identity: UnsafeMutablePointer<Unmanaged<SecIdentity>?>) -> OSStatus ``` |

Modified [CWKeychainDeleteWiFiEAPUsernameAndPassword(_: CWKeychainDomain, _: NSData) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512239-cwkeychaindeletewifieapusernamea)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainDeleteWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData!) -> OSStatus ``` |
| To | ``` func CWKeychainDeleteWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData) -> OSStatus ``` |

Modified [CWKeychainDeleteWiFiPassword(_: CWKeychainDomain, _: NSData) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512242-cwkeychaindeletewifipassword)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainDeleteWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData!) -> OSStatus ``` |
| To | ``` func CWKeychainDeleteWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData) -> OSStatus ``` |

Modified [CWKeychainFindWiFiEAPUsernameAndPassword(_: CWKeychainDomain, _: NSData, _: AutoreleasingUnsafeMutablePointer<NSString?>, _: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512198-cwkeychainfindwifieapusernameand)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainFindWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ username: AutoreleasingUnsafeMutablePointer<NSString?>, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` |
| To | ``` func CWKeychainFindWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ username: AutoreleasingUnsafeMutablePointer<NSString?>, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` |

Modified [CWKeychainFindWiFiPassword(_: CWKeychainDomain, _: NSData, _: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512359-cwkeychainfindwifipassword)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` |
| To | ``` func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ password: AutoreleasingUnsafeMutablePointer<NSString?>) -> OSStatus ``` |

Modified [CWKeychainSetWiFiEAPIdentity(_: CWKeychainDomain, _: NSData, _: SecIdentity?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512453-cwkeychainsetwifieapidentity)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainSetWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData!, _ identity: SecIdentity!) -> OSStatus ``` |
| To | ``` func CWKeychainSetWiFiEAPIdentity(_ domain: CWKeychainDomain, _ ssid: NSData, _ identity: SecIdentity?) -> OSStatus ``` |

Modified [CWKeychainSetWiFiEAPUsernameAndPassword(_: CWKeychainDomain, _: NSData, _: String?, _: String?) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512305-cwkeychainsetwifieapusernameandp)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainSetWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ username: String!, _ password: String!) -> OSStatus ``` |
| To | ``` func CWKeychainSetWiFiEAPUsernameAndPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ username: String?, _ password: String?) -> OSStatus ``` |

Modified [CWKeychainSetWiFiPassword(_: CWKeychainDomain, _: NSData, _: String) -> OSStatus](https://developer.apple.com/documentation/corewlan/1512429-cwkeychainsetwifipassword)

|  | Declaration |
| --- | --- |
| From | ``` func CWKeychainSetWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData!, _ password: String!) -> OSStatus ``` |
| To | ``` func CWKeychainSetWiFiPassword(_ domain: CWKeychainDomain, _ ssid: NSData, _ password: String) -> OSStatus ``` |

Modified [CWMergeNetworks(_: Set<CWNetwork>) -> Set<CWNetwork>](https://developer.apple.com/documentation/corewlan/1512230-cwmergenetworks)

|  | Declaration |
| --- | --- |
| From | ``` func CWMergeNetworks(_ networks: Set<NSObject>!) -> Set<NSObject>! ``` |
| To | ``` func CWMergeNetworks(_ networks: Set<CWNetwork>) -> Set<CWNetwork> ``` |

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
