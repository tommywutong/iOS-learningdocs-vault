---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/NetworkExtension.html
archived_at: '2026-07-18T02:57:09.819664Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# NetworkExtension Changes for Swift

### NetworkExtension

Modified [NEAppProxyFlow](https://developer.apple.com/documentation/networkextension/neappproxyflow)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEAppProxyFlowError [enum]](https://developer.apple.com/documentation/networkextension/neappproxyflowerror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEAppProxyProvider](https://developer.apple.com/documentation/networkextension/neappproxyprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEAppProxyProviderManager](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEAppProxyTCPFlow](https://developer.apple.com/documentation/networkextension/neappproxytcpflow)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEAppProxyUDPFlow](https://developer.apple.com/documentation/networkextension/neappproxyudpflow)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEAppRule](https://developer.apple.com/documentation/networkextension/neapprule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEAppRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(signingIdentifier signingIdentifier: String)     init(signingIdentifier signingIdentifier: String, designatedRequirement designatedRequirement: String)     var matchSigningIdentifier: String { get }     var matchDesignatedRequirement: String { get }     var matchPath: String?     var matchDomains: [AnyObject]? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEAppRule : NSObject, NSSecureCoding, NSCopying {     init(signingIdentifier signingIdentifier: String)     init(signingIdentifier signingIdentifier: String, designatedRequirement designatedRequirement: String)     var matchSigningIdentifier: String { get }     var matchDesignatedRequirement: String { get }     var matchPath: String?     var matchDomains: [AnyObject]? } ``` | NSCopying, NSSecureCoding |

Modified [NEDNSSettings](https://developer.apple.com/documentation/networkextension/nednssettings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEDNSSettings : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(servers servers: [String])     var servers: [String] { get }     var searchDomains: [String]?     var domainName: String?     var matchDomains: [String]?     var matchDomainsNoSearch: Bool } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEDNSSettings : NSObject, NSSecureCoding, NSCopying {     init(servers servers: [String])     var servers: [String] { get }     var searchDomains: [String]?     var domainName: String?     var matchDomains: [String]?     var matchDomainsNoSearch: Bool } ``` | NSCopying, NSSecureCoding |

Modified [NEEvaluateConnectionRule](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEEvaluateConnectionRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction)     var action: NEEvaluateConnectionRuleAction { get }     var matchDomains: [String] { get }     var useDNSServers: [String]?     @NSCopying var probeURL: NSURL? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEEvaluateConnectionRule : NSObject, NSSecureCoding, NSCopying {     init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction)     var action: NEEvaluateConnectionRuleAction { get }     var matchDomains: [String] { get }     var useDNSServers: [String]?     @NSCopying var probeURL: NSURL? } ``` | NSCopying, NSSecureCoding |

Modified [NEEvaluateConnectionRuleAction [enum]](https://developer.apple.com/documentation/networkextension/neevaluateconnectionruleaction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEFilterBrowserFlow](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterBrowserFlow : NEFilterFlow {     var request: NSURLRequest { get }     var response: NSURLResponse? { get }     var parentURL: NSURL? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterBrowserFlow : NEFilterFlow, NSSecureCoding, NSCopying {     var request: NSURLRequest { get }     var response: NSURLResponse? { get }     var parentURL: NSURL? { get } } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterControlProvider](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEFilterControlVerdict](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterControlVerdict : NEFilterNewFlowVerdict {     class func allowVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict     class func dropVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict     class func updateRules() -> NEFilterControlVerdict } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterControlVerdict : NEFilterNewFlowVerdict, NSSecureCoding, NSCopying {     class func allowVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict     class func dropVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict     class func updateRules() -> NEFilterControlVerdict } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterDataProvider](https://developer.apple.com/documentation/networkextension/nefilterdataprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataverdict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterDataVerdict : NEFilterVerdict {     class func allowVerdict() -> NEFilterDataVerdict     class func dropVerdict() -> NEFilterDataVerdict     class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String?, remediationButtonTextMapKey remediationButtonTextMapKey: String?) -> NEFilterDataVerdict      init(passBytes passBytes: Int, peekBytes peekBytes: Int)     class func dataVerdictWithPassBytes(_ passBytes: Int, peekBytes peekBytes: Int) -> NEFilterDataVerdict     class func needRulesVerdict() -> NEFilterDataVerdict } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterDataVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func allowVerdict() -> NEFilterDataVerdict     class func dropVerdict() -> NEFilterDataVerdict     class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String?, remediationButtonTextMapKey remediationButtonTextMapKey: String?) -> NEFilterDataVerdict      init(passBytes passBytes: Int, peekBytes peekBytes: Int)     class func dataVerdictWithPassBytes(_ passBytes: Int, peekBytes peekBytes: Int) -> NEFilterDataVerdict     class func needRulesVerdict() -> NEFilterDataVerdict } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterFlow](https://developer.apple.com/documentation/networkextension/nefilterflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterFlow : NSObject, NSSecureCoding, NSCoding, NSCopying {     var URL: NSURL? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterFlow : NSObject, NSSecureCoding, NSCopying {     var URL: NSURL? { get } } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterManager](https://developer.apple.com/documentation/networkextension/nefiltermanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEFilterManagerError [enum]](https://developer.apple.com/documentation/networkextension/nefiltermanagererror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEFilterNewFlowVerdict](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterNewFlowVerdict : NEFilterVerdict {     class func needRulesVerdict() -> NEFilterNewFlowVerdict     class func allowVerdict() -> NEFilterNewFlowVerdict     class func dropVerdict() -> NEFilterNewFlowVerdict     class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String, remediationButtonTextMapKey remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict     class func URLAppendStringVerdictWithMapKey(_ urlAppendMapKey: String) -> NEFilterNewFlowVerdict     class func filterDataVerdictWithFilterInbound(_ filterInbound: Bool, peekInboundBytes peekInboundBytes: Int, filterOutbound filterOutbound: Bool, peekOutboundBytes peekOutboundBytes: Int) -> NEFilterNewFlowVerdict } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterNewFlowVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func needRulesVerdict() -> NEFilterNewFlowVerdict     class func allowVerdict() -> NEFilterNewFlowVerdict     class func dropVerdict() -> NEFilterNewFlowVerdict     class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String, remediationButtonTextMapKey remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict     class func URLAppendStringVerdictWithMapKey(_ urlAppendMapKey: String) -> NEFilterNewFlowVerdict     class func filterDataVerdictWithFilterInbound(_ filterInbound: Bool, peekInboundBytes peekInboundBytes: Int, filterOutbound filterOutbound: Bool, peekOutboundBytes peekOutboundBytes: Int) -> NEFilterNewFlowVerdict } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterProvider](https://developer.apple.com/documentation/networkextension/nefilterprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEFilterProviderConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterProviderConfiguration : NSObject, NSSecureCoding, NSCoding, NSCopying {     var filterBrowsers: Bool     var filterSockets: Bool     var vendorConfiguration: [String : AnyObject]?     var serverAddress: String?     var username: String?     var organization: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterProviderConfiguration : NSObject, NSSecureCoding, NSCopying {     var filterBrowsers: Bool     var filterSockets: Bool     var vendorConfiguration: [String : AnyObject]?     var serverAddress: String?     var username: String?     var organization: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData? } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterRemediationVerdict](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterRemediationVerdict : NEFilterVerdict {     class func allowVerdict() -> NEFilterRemediationVerdict     class func dropVerdict() -> NEFilterRemediationVerdict     class func needRulesVerdict() -> NEFilterRemediationVerdict } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterRemediationVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func allowVerdict() -> NEFilterRemediationVerdict     class func dropVerdict() -> NEFilterRemediationVerdict     class func needRulesVerdict() -> NEFilterRemediationVerdict } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterSocketFlow](https://developer.apple.com/documentation/networkextension/nefiltersocketflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterSocketFlow : NEFilterFlow {     var remoteEndpoint: NWEndpoint { get }     var localEndpoint: NWEndpoint { get }     var socketFamily: Int32     var socketType: Int32     var socketProtocol: Int32 } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterSocketFlow : NEFilterFlow, NSSecureCoding, NSCopying {     var remoteEndpoint: NWEndpoint { get }     var localEndpoint: NWEndpoint { get }     var socketFamily: Int32     var socketType: Int32     var socketProtocol: Int32 } ``` | NSCopying, NSSecureCoding |

Modified [NEFilterVerdict](https://developer.apple.com/documentation/networkextension/nefilterverdict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterVerdict : NSObject, NSSecureCoding, NSCoding, NSCopying { } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEFilterVerdict : NSObject, NSSecureCoding, NSCopying { } ``` | NSCopying, NSSecureCoding |

Modified [NEFlowMetaData](https://developer.apple.com/documentation/networkextension/neflowmetadata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEHotspotHelper](https://developer.apple.com/documentation/networkextension/nehotspothelper)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEHotspotHelperCommand](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEHotspotHelperCommandType [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEHotspotHelperConfidence [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEHotspotHelperResponse](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEHotspotHelperResult [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelperresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEHotspotNetwork](https://developer.apple.com/documentation/networkextension/nehotspotnetwork)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEIPv4Route](https://developer.apple.com/documentation/networkextension/neipv4route)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv4Route : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(destinationAddress address: String, subnetMask subnetMask: String)     var destinationAddress: String { get }     var destinationSubnetMask: String { get }     var gatewayAddress: String?     class func defaultRoute() -> NEIPv4Route } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEIPv4Route : NSObject, NSSecureCoding, NSCopying {     init(destinationAddress address: String, subnetMask subnetMask: String)     var destinationAddress: String { get }     var destinationSubnetMask: String { get }     var gatewayAddress: String?     class func defaultRoute() -> NEIPv4Route } ``` | NSCopying, NSSecureCoding |

Modified [NEIPv4Settings](https://developer.apple.com/documentation/networkextension/neipv4settings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv4Settings : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(addresses addresses: [String], subnetMasks subnetMasks: [String])     var addresses: [String] { get }     var subnetMasks: [String] { get }     var includedRoutes: [NEIPv4Route]?     var excludedRoutes: [NEIPv4Route]? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEIPv4Settings : NSObject, NSSecureCoding, NSCopying {     init(addresses addresses: [String], subnetMasks subnetMasks: [String])     var addresses: [String] { get }     var subnetMasks: [String] { get }     var includedRoutes: [NEIPv4Route]?     var excludedRoutes: [NEIPv4Route]? } ``` | NSCopying, NSSecureCoding |

Modified [NEIPv6Route](https://developer.apple.com/documentation/networkextension/neipv6route)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv6Route : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(destinationAddress address: String, networkPrefixLength networkPrefixLength: NSNumber)     var destinationAddress: String { get }     var destinationNetworkPrefixLength: NSNumber { get }     var gatewayAddress: String?     class func defaultRoute() -> NEIPv6Route } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEIPv6Route : NSObject, NSSecureCoding, NSCopying {     init(destinationAddress address: String, networkPrefixLength networkPrefixLength: NSNumber)     var destinationAddress: String { get }     var destinationNetworkPrefixLength: NSNumber { get }     var gatewayAddress: String?     class func defaultRoute() -> NEIPv6Route } ``` | NSCopying, NSSecureCoding |

Modified [NEIPv6Settings](https://developer.apple.com/documentation/networkextension/neipv6settings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv6Settings : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(addresses addresses: [String], networkPrefixLengths networkPrefixLengths: [NSNumber])     var addresses: [String] { get }     var networkPrefixLengths: [NSNumber] { get }     var includedRoutes: [NEIPv6Route]?     var excludedRoutes: [NEIPv6Route]? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEIPv6Settings : NSObject, NSSecureCoding, NSCopying {     init(addresses addresses: [String], networkPrefixLengths networkPrefixLengths: [NSNumber])     var addresses: [String] { get }     var networkPrefixLengths: [NSNumber] { get }     var includedRoutes: [NEIPv6Route]?     var excludedRoutes: [NEIPv6Route]? } ``` | NSCopying, NSSecureCoding |

Modified [NEOnDemandRule](https://developer.apple.com/documentation/networkextension/neondemandrule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEOnDemandRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     var action: NEOnDemandRuleAction { get }     var DNSSearchDomainMatch: [String]?     var DNSServerAddressMatch: [String]?     var interfaceTypeMatch: NEOnDemandRuleInterfaceType     var SSIDMatch: [String]?     @NSCopying var probeURL: NSURL? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEOnDemandRule : NSObject, NSSecureCoding, NSCopying {     var action: NEOnDemandRuleAction { get }     var DNSSearchDomainMatch: [String]?     var DNSServerAddressMatch: [String]?     var interfaceTypeMatch: NEOnDemandRuleInterfaceType     var SSIDMatch: [String]?     @NSCopying var probeURL: NSURL? } ``` | NSCopying, NSSecureCoding |

Modified [NEOnDemandRuleAction [enum]](https://developer.apple.com/documentation/networkextension/neondemandruleaction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEOnDemandRuleConnect](https://developer.apple.com/documentation/networkextension/neondemandruleconnect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEOnDemandRuleDisconnect](https://developer.apple.com/documentation/networkextension/neondemandruledisconnect)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEOnDemandRuleEvaluateConnection](https://developer.apple.com/documentation/networkextension/neondemandruleevaluateconnection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEOnDemandRuleIgnore](https://developer.apple.com/documentation/networkextension/neondemandruleignore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEOnDemandRuleInterfaceType [enum]](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEPacketTunnelFlow](https://developer.apple.com/documentation/networkextension/nepackettunnelflow)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEPacketTunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEPacketTunnelProvider](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEProvider](https://developer.apple.com/documentation/networkextension/neprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEProviderStopReason [enum]](https://developer.apple.com/documentation/networkextension/neproviderstopreason)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEProxyServer](https://developer.apple.com/documentation/networkextension/neproxyserver)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEProxyServer : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(address address: String, port port: Int)     var address: String { get }     var port: Int { get }     var authenticationRequired: Bool     var username: String?     var password: String? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEProxyServer : NSObject, NSSecureCoding, NSCopying {     init(address address: String, port port: Int)     var address: String { get }     var port: Int { get }     var authenticationRequired: Bool     var username: String?     var password: String? } ``` | NSCopying, NSSecureCoding |

Modified [NEProxySettings](https://developer.apple.com/documentation/networkextension/neproxysettings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEProxySettings : NSObject, NSSecureCoding, NSCoding, NSCopying {     var autoProxyConfigurationEnabled: Bool     @NSCopying var proxyAutoConfigurationURL: NSURL?     var proxyAutoConfigurationJavaScript: String?     var HTTPEnabled: Bool     @NSCopying var HTTPServer: NEProxyServer?     var HTTPSEnabled: Bool     @NSCopying var HTTPSServer: NEProxyServer?     var excludeSimpleHostnames: Bool     var exceptionList: [String]?     var matchDomains: [String]? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEProxySettings : NSObject, NSSecureCoding, NSCopying {     var autoProxyConfigurationEnabled: Bool     @NSCopying var proxyAutoConfigurationURL: NSURL?     var proxyAutoConfigurationJavaScript: String?     var HTTPEnabled: Bool     @NSCopying var HTTPServer: NEProxyServer?     var HTTPSEnabled: Bool     @NSCopying var HTTPSServer: NEProxyServer?     var excludeSimpleHostnames: Bool     var exceptionList: [String]?     var matchDomains: [String]? } ``` | NSCopying, NSSecureCoding |

Modified [NETunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NETunnelNetworkSettings : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(tunnelRemoteAddress address: String)     var tunnelRemoteAddress: String { get }     @NSCopying var DNSSettings: NEDNSSettings?     @NSCopying var proxySettings: NEProxySettings? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NETunnelNetworkSettings : NSObject, NSSecureCoding, NSCopying {     init(tunnelRemoteAddress address: String)     var tunnelRemoteAddress: String { get }     @NSCopying var DNSSettings: NEDNSSettings?     @NSCopying var proxySettings: NEProxySettings? } ``` | NSCopying, NSSecureCoding |

Modified [NETunnelProvider](https://developer.apple.com/documentation/networkextension/netunnelprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NETunnelProviderError [enum]](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NETunnelProviderManager](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NETunnelProviderProtocol](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NETunnelProviderRoutingMethod [enum]](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NETunnelProviderSession](https://developer.apple.com/documentation/networkextension/netunnelprovidersession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEVPNConnection](https://developer.apple.com/documentation/networkextension/nevpnconnection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEVPNError [enum]](https://developer.apple.com/documentation/networkextension/nevpnerror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEAuthenticationMethod [enum]](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEv2CertificateType [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEv2DeadPeerDetectionRate [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEv2DiffieHellmanGroup [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEv2EncryptionAlgorithm [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEv2IntegrityAlgorithm [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2integrityalgorithm)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NEVPNIKEv2SecurityAssociationParameters](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEVPNIKEv2SecurityAssociationParameters : NSObject, NSSecureCoding, NSCoding, NSCopying {     var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm     var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm     var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup     var lifetimeMinutes: Int32 } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEVPNIKEv2SecurityAssociationParameters : NSObject, NSSecureCoding, NSCopying {     var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm     var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm     var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup     var lifetimeMinutes: Int32 } ``` | NSCopying, NSSecureCoding |

Modified [NEVPNManager](https://developer.apple.com/documentation/networkextension/nevpnmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEVPNProtocol](https://developer.apple.com/documentation/networkextension/nevpnprotocol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEVPNProtocol : NSObject, NSCopying, NSSecureCoding, NSCoding {     var serverAddress: String?     var username: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData?     @NSCopying var identityData: NSData?     var identityDataPassword: String?     var disconnectOnSleep: Bool     @NSCopying var proxySettings: NEProxySettings? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class NEVPNProtocol : NSObject, NSCopying, NSSecureCoding {     var serverAddress: String?     var username: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData?     @NSCopying var identityData: NSData?     var identityDataPassword: String?     var disconnectOnSleep: Bool     @NSCopying var proxySettings: NEProxySettings? } ``` | NSCopying, NSSecureCoding |

Modified [NEVPNProtocolIKEv2](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEVPNProtocolIPSec](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NEVPNStatus [enum]](https://developer.apple.com/documentation/networkextension/nevpnstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NWBonjourServiceEndpoint](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWEndpoint](https://developer.apple.com/documentation/networkextension/nwendpoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWHostEndpoint](https://developer.apple.com/documentation/networkextension/nwhostendpoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWPath](https://developer.apple.com/documentation/networkextension/nwpath)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWPathStatus [enum]](https://developer.apple.com/documentation/networkextension/nwpathstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NWTCPConnection](https://developer.apple.com/documentation/networkextension/nwtcpconnection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWTCPConnectionState [enum]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NWTLSParameters](https://developer.apple.com/documentation/networkextension/nwtlsparameters)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWUDPSession](https://developer.apple.com/documentation/networkextension/nwudpsession)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NWUDPSessionState [enum]](https://developer.apple.com/documentation/networkextension/nwudpsessionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
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
