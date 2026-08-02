---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/NetworkExtension.html
archived_at: '2026-07-18T02:56:56.066074Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# NetworkExtension Changes for Swift

### NetworkExtension

Added [NEAppProxyFlow](https://developer.apple.com/documentation/networkextension/neappproxyflow)Added [NEAppProxyFlow.closeReadWithError(_: NSError?)](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406561-closereadwitherror)Added [NEAppProxyFlow.closeWriteWithError(_: NSError?)](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406664-closewritewitherror)Added [NEAppProxyFlow.metaData](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406171-metadata)Added [NEAppProxyFlow.openWithLocalEndpoint(_: NWHostEndpoint?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406476-openwithlocalendpoint)Added [NEAppProxyFlowError [enum]](https://developer.apple.com/documentation/networkextension/neappproxyflowerror)Added [NEAppProxyFlowError.Aborted](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerroraborted)Added [NEAppProxyFlowError.HostUnreachable](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrorhostunreachable)Added [NEAppProxyFlowError.Internal](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/internal)Added [NEAppProxyFlowError.InvalidArgument](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/invalidargument)Added [NEAppProxyFlowError.NotConnected](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrornotconnected)Added [NEAppProxyFlowError.PeerReset](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrorpeerreset)Added [NEAppProxyFlowError.Refused](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/refused)Added [NEAppProxyFlowError.TimedOut](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/timedout)Added [NEAppProxyProvider](https://developer.apple.com/documentation/networkextension/neappproxyprovider)Added [NEAppProxyProvider.cancelProxyWithError(_: NSError?)](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405081-cancelproxywitherror)Added [NEAppProxyProvider.handleNewFlow(_: NEAppProxyFlow) -> Bool](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405085-handlenewflow)Added [NEAppProxyProvider.startProxyWithOptions(_: [String : AnyObject]?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405083-startproxy)Added [NEAppProxyProvider.stopProxyWithReason(_: NEProviderStopReason, completionHandler: () -> Void)](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405077-stopproxywithreason)Added [NEAppProxyProviderManager](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager)Added [NEAppProxyProviderManager.loadAllFromPreferencesWithCompletionHandler(_: ([NEAppProxyProviderManager]?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager/1406790-loadallfrompreferenceswithcomple)Added [NEAppProxyTCPFlow](https://developer.apple.com/documentation/networkextension/neappproxytcpflow)Added [NEAppProxyTCPFlow.readDataWithCompletionHandler(_: (NSData?, NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406311-readdatawithcompletionhandler)Added [NEAppProxyTCPFlow.remoteEndpoint](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406233-remoteendpoint)Added [NEAppProxyTCPFlow.writeData(_: NSData, withCompletionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406776-write)Added [NEAppProxyUDPFlow](https://developer.apple.com/documentation/networkextension/neappproxyudpflow)Added [NEAppProxyUDPFlow.localEndpoint](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406699-localendpoint)Added [NEAppProxyUDPFlow.readDatagramsWithCompletionHandler(_: ([NSData]?, [NWEndpoint]?, NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406576-readdatagramswithcompletionhandl)Added [NEAppProxyUDPFlow.writeDatagrams(_: [NSData], sentByEndpoints: [NWEndpoint], completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406784-writedatagrams)Added [NEAppRule](https://developer.apple.com/documentation/networkextension/neapprule)Added [NEAppRule.init(signingIdentifier: String)](https://developer.apple.com/documentation/networkextension/neapprule/1617852-initwithsigningidentifier)Added [NEAppRule.matchDomains](https://developer.apple.com/documentation/networkextension/neapprule/1406488-matchdomains)Added [NEAppRule.matchSigningIdentifier](https://developer.apple.com/documentation/networkextension/neapprule/1406243-matchsigningidentifier)Added [NEDNSSettings](https://developer.apple.com/documentation/networkextension/nednssettings)Added [NEDNSSettings.domainName](https://developer.apple.com/documentation/networkextension/nednssettings/1406440-domainname)Added [NEDNSSettings.init(servers: [String])](https://developer.apple.com/documentation/networkextension/nednssettings/1406478-init)Added [NEDNSSettings.matchDomains](https://developer.apple.com/documentation/networkextension/nednssettings/1406537-matchdomains)Added [NEDNSSettings.matchDomainsNoSearch](https://developer.apple.com/documentation/networkextension/nednssettings/1406735-matchdomainsnosearch)Added [NEDNSSettings.searchDomains](https://developer.apple.com/documentation/networkextension/nednssettings/1406658-searchdomains)Added [NEDNSSettings.servers](https://developer.apple.com/documentation/networkextension/nednssettings/1406237-servers)Added [NEFilterBrowserFlow](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow)Added [NEFilterBrowserFlow.parentURL](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618932-parenturl)Added [NEFilterBrowserFlow.request](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618948-request)Added [NEFilterBrowserFlow.response](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618966-response)Added [NEFilterControlProvider](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider)Added [NEFilterControlProvider.handleNewFlow(_: NEFilterFlow, completionHandler: (NEFilterControlVerdict) -> Void)](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614120-handlenewflow)Added [NEFilterControlProvider.handleRemediationForFlow(_: NEFilterFlow, completionHandler: (NEFilterControlVerdict) -> Void)](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614122-handleremediationforflow)Added [NEFilterControlProvider.notifyRulesChanged()](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614125-notifyruleschanged)Added [NEFilterControlProvider.remediationMap](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614121-remediationmap)Added [NEFilterControlProvider.URLAppendStringMap](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614123-urlappendstringmap)Added [NEFilterControlVerdict](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict)Added [NEFilterControlVerdict.allowVerdictWithUpdateRules(_: Bool) -> NEFilterControlVerdict [class]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617040-allow)Added [NEFilterControlVerdict.dropVerdictWithUpdateRules(_: Bool) -> NEFilterControlVerdict [class]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617044-dropverdictwithupdaterules)Added [NEFilterControlVerdict.updateRules() -> NEFilterControlVerdict [class]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617037-updaterules)Added [NEFilterDataProvider](https://developer.apple.com/documentation/networkextension/nefilterdataprovider)Added [NEFilterDataProvider.handleInboundDataCompleteForFlow(_: NEFilterFlow) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618977-handleinbounddatacomplete)Added [NEFilterDataProvider.handleInboundDataFromFlow(_: NEFilterFlow, readBytesStartOffset: Int, readBytes: NSData) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618933-handleinbounddatafromflow)Added [NEFilterDataProvider.handleNewFlow(_: NEFilterFlow) -> NEFilterNewFlowVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618918-handlenewflow)Added [NEFilterDataProvider.handleOutboundDataCompleteForFlow(_: NEFilterFlow) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618961-handleoutbounddatacompleteforflo)Added [NEFilterDataProvider.handleOutboundDataFromFlow(_: NEFilterFlow, readBytesStartOffset: Int, readBytes: NSData) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618954-handleoutbounddata)Added [NEFilterDataProvider.handleRemediationForFlow(_: NEFilterFlow) -> NEFilterRemediationVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618928-handleremediationforflow)Added [NEFilterDataProvider.handleRulesChanged()](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618919-handleruleschanged)Added [NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataverdict)Added [NEFilterDataVerdict.allowVerdict() -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1619010-allowverdict)Added [NEFilterDataVerdict.dropVerdict() -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618952-dropverdict)Added [NEFilterDataVerdict.init(passBytes: Int, peekBytes: Int)](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1619005-init)Added [NEFilterDataVerdict.needRulesVerdict() -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618993-needrulesverdict)Added [NEFilterDataVerdict.remediateVerdictWithRemediationURLMapKey(_: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618964-remediateverdictwithremediationu)Added [NEFilterFlow](https://developer.apple.com/documentation/networkextension/nefilterflow)Added [NEFilterFlow.URL](https://developer.apple.com/documentation/networkextension/nefilterflow/1618935-url)Added [NEFilterManager](https://developer.apple.com/documentation/networkextension/nefiltermanager)Added [NEFilterManager.enabled](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406158-enabled)Added [NEFilterManager.loadFromPreferencesWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406359-loadfrompreferences)Added [NEFilterManager.localizedDescription](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406375-localizeddescription)Added [NEFilterManager.providerConfiguration](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406070-providerconfiguration)Added [NEFilterManager.removeFromPreferencesWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406876-removefrompreferenceswithcomplet)Added [NEFilterManager.saveToPreferencesWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406339-savetopreferences)Added [NEFilterManager.sharedManager() -> NEFilterManager [class]](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406438-shared)Added [NEFilterManagerError [enum]](https://developer.apple.com/documentation/networkextension/nefiltermanagererror)Added [NEFilterManagerError.ConfigurationCannotBeRemoved](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/nefiltermanagererrorconfigurationcannotberemoved)Added [NEFilterManagerError.ConfigurationDisabled](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationdisabled)Added [NEFilterManagerError.ConfigurationInvalid](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationinvalid)Added [NEFilterManagerError.ConfigurationStale](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationstale)Added [NEFilterNewFlowVerdict](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict)Added [NEFilterNewFlowVerdict.allowVerdict() -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617036-allow)Added [NEFilterNewFlowVerdict.dropVerdict() -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617035-dropverdict)Added [NEFilterNewFlowVerdict.filterDataVerdictWithFilterInbound(_: Bool, peekInboundBytes: Int, filterOutbound: Bool, peekOutboundBytes: Int) -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617038-filterdataverdictwithfilterinbou)Added [NEFilterNewFlowVerdict.needRulesVerdict() -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617034-needrules)Added [NEFilterNewFlowVerdict.remediateVerdictWithRemediationURLMapKey(_: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617042-remediateverdictwithremediationu)Added [NEFilterNewFlowVerdict.URLAppendStringVerdictWithMapKey(_: String) -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617046-urlappendstringverdictwithmapkey)Added [NEFilterProvider](https://developer.apple.com/documentation/networkextension/nefilterprovider)Added [NEFilterProvider.filterConfiguration](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617033-filterconfiguration)Added [NEFilterProvider.startFilterWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617043-startfilter)Added [NEFilterProvider.stopFilterWithReason(_: NEProviderStopReason, completionHandler: () -> Void)](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617032-stopfilter)Added [NEFilterProviderConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration)Added [NEFilterProviderConfiguration.filterBrowsers](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406864-filterbrowsers)Added [NEFilterProviderConfiguration.filterSockets](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406596-filtersockets)Added [NEFilterProviderConfiguration.identityReference](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406866-identityreference)Added [NEFilterProviderConfiguration.organization](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406012-organization)Added [NEFilterProviderConfiguration.passwordReference](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406146-passwordreference)Added [NEFilterProviderConfiguration.serverAddress](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406507-serveraddress)Added [NEFilterProviderConfiguration.username](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406482-username)Added [NEFilterProviderConfiguration.vendorConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406347-vendorconfiguration)Added [NEFilterRemediationVerdict](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict)Added [NEFilterRemediationVerdict.allowVerdict() -> NEFilterRemediationVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618962-allow)Added [NEFilterRemediationVerdict.dropVerdict() -> NEFilterRemediationVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618947-dropverdict)Added [NEFilterRemediationVerdict.needRulesVerdict() -> NEFilterRemediationVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618972-needrulesverdict)Added [NEFilterSocketFlow](https://developer.apple.com/documentation/networkextension/nefiltersocketflow)Added [NEFilterSocketFlow.localEndpoint](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1619004-localendpoint)Added [NEFilterSocketFlow.remoteEndpoint](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618940-remoteendpoint)Added [NEFilterSocketFlow.socketFamily](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618983-socketfamily)Added [NEFilterSocketFlow.socketProtocol](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618953-socketprotocol)Added [NEFilterSocketFlow.socketType](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618956-sockettype)Added [NEFilterVerdict](https://developer.apple.com/documentation/networkextension/nefilterverdict)Added [NEFlowMetaData](https://developer.apple.com/documentation/networkextension/neflowmetadata)Added [NEFlowMetaData.sourceAppSigningIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406840-sourceappsigningidentifier)Added [NEFlowMetaData.sourceAppUniqueIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406448-sourceappuniqueidentifier)Added [NEHotspotHelper](https://developer.apple.com/documentation/networkextension/nehotspothelper)Added [NEHotspotHelper.logoff(_: NEHotspotNetwork) -> Bool [class]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618944-logoff)Added [NEHotspotHelper.registerWithOptions(_: [String : NSObject]?, queue: dispatch_queue_t, handler: NEHotspotHelperHandler) -> Bool [class]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618965-registerwithoptions)Added [NEHotspotHelper.supportedNetworkInterfaces() -> [AnyObject] [class]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618921-supportednetworkinterfaces)Added [NEHotspotHelperCommand](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand)Added [NEHotspotHelperCommand.commandType](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618942-commandtype)Added [NEHotspotHelperCommand.createResponse(_: NEHotspotHelperResult) -> NEHotspotHelperResponse](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618931-createresponse)Added [NEHotspotHelperCommand.createTCPConnection(_: NWEndpoint) -> NWTCPConnection](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1619013-createtcpconnection)Added [NEHotspotHelperCommand.createUDPSession(_: NWEndpoint) -> NWUDPSession](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618934-createudpsession)Added [NEHotspotHelperCommand.network](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1619011-network)Added [NEHotspotHelperCommand.networkList](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618967-networklist)Added [NEHotspotHelperCommandType [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype)Added [NEHotspotHelperCommandType.Authenticate](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypeauthenticate)Added [NEHotspotHelperCommandType.Evaluate](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypeevaluate)Added [NEHotspotHelperCommandType.FilterScanList](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypefilterscanlist)Added [NEHotspotHelperCommandType.Logoff](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/logoff)Added [NEHotspotHelperCommandType.Maintain](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypemaintain)Added [NEHotspotHelperCommandType.None](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/none)Added [NEHotspotHelperCommandType.PresentUI](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypepresentui)Added [NEHotspotHelperConfidence [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence)Added [NEHotspotHelperConfidence.High](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/knehotspothelperconfidencehigh)Added [NEHotspotHelperConfidence.Low](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/low)Added [NEHotspotHelperConfidence.None](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/none)Added [NEHotspotHelperResponse](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse)Added [NEHotspotHelperResponse.deliver()](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/1618974-deliver)Added [NEHotspotHelperResponse.setNetwork(_: NEHotspotNetwork)](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/1618920-setnetwork)Added [NEHotspotHelperResponse.setNetworkList(_: [NEHotspotNetwork])](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/1618915-setnetworklist)Added [NEHotspotHelperResult [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelperresult)Added [NEHotspotHelperResult.AuthenticationRequired](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultauthenticationrequired)Added [NEHotspotHelperResult.CommandNotRecognized](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultcommandnotrecognized)Added [NEHotspotHelperResult.Failure](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/failure)Added [NEHotspotHelperResult.Success](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/success)Added [NEHotspotHelperResult.TemporaryFailure](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/temporaryfailure)Added [NEHotspotHelperResult.UIRequired](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/uirequired)Added [NEHotspotHelperResult.UnsupportedNetwork](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/unsupportednetwork)Added [NEHotspotNetwork](https://developer.apple.com/documentation/networkextension/nehotspotnetwork)Added [NEHotspotNetwork.autoJoined](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618976-autojoined)Added [NEHotspotNetwork.BSSID](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618936-bssid)Added [NEHotspotNetwork.chosenHelper](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618975-ischosenhelper)Added [NEHotspotNetwork.justJoined](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618955-justjoined)Added [NEHotspotNetwork.secure](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618930-issecure)Added [NEHotspotNetwork.setConfidence(_: NEHotspotHelperConfidence)](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618969-setconfidence)Added [NEHotspotNetwork.setPassword(_: String)](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1619009-setpassword)Added [NEHotspotNetwork.signalStrength](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618923-signalstrength)Added [NEHotspotNetwork.SSID](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618925-ssid)Added [NEIPv4Route](https://developer.apple.com/documentation/networkextension/neipv4route)Added [NEIPv4Route.defaultRoute() -> NEIPv4Route [class]](https://developer.apple.com/documentation/networkextension/neipv4route/1406474-defaultroute)Added [NEIPv4Route.destinationAddress](https://developer.apple.com/documentation/networkextension/neipv4route/1406578-destinationaddress)Added [NEIPv4Route.destinationSubnetMask](https://developer.apple.com/documentation/networkextension/neipv4route/1406411-destinationsubnetmask)Added [NEIPv4Route.gatewayAddress](https://developer.apple.com/documentation/networkextension/neipv4route/1406519-gatewayaddress)Added [NEIPv4Route.init(destinationAddress: String, subnetMask: String)](https://developer.apple.com/documentation/networkextension/neipv4route/1406643-initwithdestinationaddress)Added [NEIPv4Settings](https://developer.apple.com/documentation/networkextension/neipv4settings)Added [NEIPv4Settings.addresses](https://developer.apple.com/documentation/networkextension/neipv4settings/1406666-addresses)Added [NEIPv4Settings.excludedRoutes](https://developer.apple.com/documentation/networkextension/neipv4settings/1406267-excludedroutes)Added [NEIPv4Settings.includedRoutes](https://developer.apple.com/documentation/networkextension/neipv4settings/1406654-includedroutes)Added [NEIPv4Settings.init(addresses: [String], subnetMasks: [String])](https://developer.apple.com/documentation/networkextension/neipv4settings/1406709-initwithaddresses)Added [NEIPv4Settings.subnetMasks](https://developer.apple.com/documentation/networkextension/neipv4settings/1406160-subnetmasks)Added [NEIPv6Route](https://developer.apple.com/documentation/networkextension/neipv6route)Added [NEIPv6Route.defaultRoute() -> NEIPv6Route [class]](https://developer.apple.com/documentation/networkextension/neipv6route/1406847-default)Added [NEIPv6Route.destinationAddress](https://developer.apple.com/documentation/networkextension/neipv6route/1406269-destinationaddress)Added [NEIPv6Route.destinationNetworkPrefixLength](https://developer.apple.com/documentation/networkextension/neipv6route/1406897-destinationnetworkprefixlength)Added [NEIPv6Route.gatewayAddress](https://developer.apple.com/documentation/networkextension/neipv6route/1406691-gatewayaddress)Added [NEIPv6Route.init(destinationAddress: String, networkPrefixLength: NSNumber)](https://developer.apple.com/documentation/networkextension/neipv6route/1406245-initwithdestinationaddress)Added [NEIPv6Settings](https://developer.apple.com/documentation/networkextension/neipv6settings)Added [NEIPv6Settings.addresses](https://developer.apple.com/documentation/networkextension/neipv6settings/1406304-addresses)Added [NEIPv6Settings.excludedRoutes](https://developer.apple.com/documentation/networkextension/neipv6settings/1406294-excludedroutes)Added [NEIPv6Settings.includedRoutes](https://developer.apple.com/documentation/networkextension/neipv6settings/1406567-includedroutes)Added [NEIPv6Settings.init(addresses: [String], networkPrefixLengths: [NSNumber])](https://developer.apple.com/documentation/networkextension/neipv6settings/1406407-initwithaddresses)Added [NEIPv6Settings.networkPrefixLengths](https://developer.apple.com/documentation/networkextension/neipv6settings/1406167-networkprefixlengths)Added [NEOnDemandRuleInterfaceType.Any](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype/neondemandruleinterfacetypeany)Added [NEPacketTunnelFlow](https://developer.apple.com/documentation/networkextension/nepackettunnelflow)Added [NEPacketTunnelFlow.readPacketsWithCompletionHandler(_: ([NSData], [NSNumber]) -> Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/1406903-readpackets)Added [NEPacketTunnelFlow.writePackets(_: [NSData], withProtocols: [NSNumber]) -> Bool](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/1406484-writepackets)Added [NEPacketTunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings)Added [NEPacketTunnelNetworkSettings.IPv4Settings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406574-ipv4settings)Added [NEPacketTunnelNetworkSettings.IPv6Settings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406138-ipv6settings)Added [NEPacketTunnelNetworkSettings.MTU](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406094-mtu)Added [NEPacketTunnelNetworkSettings.tunnelOverheadBytes](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406675-tunneloverheadbytes)Added [NEPacketTunnelProvider](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider)Added [NEPacketTunnelProvider.cancelTunnelWithError(_: NSError?)](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406169-canceltunnelwitherror)Added [NEPacketTunnelProvider.createTCPConnectionThroughTunnelToEndpoint(_: NWEndpoint, enableTLS: Bool, TLSParameters: NWTLSParameters?, delegate: AnyObject?) -> NWTCPConnection](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406055-createtcpconnectionthroughtunnel)Added [NEPacketTunnelProvider.createUDPSessionThroughTunnelToEndpoint(_: NWEndpoint, fromEndpoint: NWHostEndpoint?) -> NWUDPSession](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406068-createudpsessionthroughtunneltoe)Added [NEPacketTunnelProvider.packetFlow](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406185-packetflow)Added [NEPacketTunnelProvider.startTunnelWithOptions(_: [String : NSObject]?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406118-starttunnelwithoptions)Added [NEPacketTunnelProvider.stopTunnelWithReason(_: NEProviderStopReason, completionHandler: () -> Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406192-stoptunnel)Added [NEProvider](https://developer.apple.com/documentation/networkextension/neprovider)Added [NEProvider.createTCPConnectionToEndpoint(_: NWEndpoint, enableTLS: Bool, TLSParameters: NWTLSParameters?, delegate: AnyObject?) -> NWTCPConnection](https://developer.apple.com/documentation/networkextension/neprovider/1406529-createtcpconnectiontoendpoint)Added [NEProvider.createUDPSessionToEndpoint(_: NWEndpoint, fromEndpoint: NWHostEndpoint?) -> NWUDPSession](https://developer.apple.com/documentation/networkextension/neprovider/1406004-createudpsessiontoendpoint)Added [NEProvider.defaultPath](https://developer.apple.com/documentation/networkextension/neprovider/1406740-defaultpath)Added [NEProvider.sleepWithCompletionHandler(_: () -> Void)](https://developer.apple.com/documentation/networkextension/neprovider/1406731-sleepwithcompletionhandler)Added [NEProvider.wake()](https://developer.apple.com/documentation/networkextension/neprovider/1406543-wake)Added [NEProviderStopReason [enum]](https://developer.apple.com/documentation/networkextension/neproviderstopreason)Added [NEProviderStopReason.AuthenticationCanceled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonauthenticationcanceled)Added [NEProviderStopReason.ConfigurationDisabled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationdisabled)Added [NEProviderStopReason.ConfigurationFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationfailed)Added [NEProviderStopReason.ConfigurationRemoved](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationremoved)Added [NEProviderStopReason.ConnectionFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/connectionfailed)Added [NEProviderStopReason.IdleTimeout](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonidletimeout)Added [NEProviderStopReason.None](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonnone)Added [NEProviderStopReason.NoNetworkAvailable](https://developer.apple.com/documentation/networkextension/neproviderstopreason/nonetworkavailable)Added [NEProviderStopReason.ProviderDisabled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/providerdisabled)Added [NEProviderStopReason.ProviderFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonproviderfailed)Added [NEProviderStopReason.Superceded](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonsuperceded)Added [NEProviderStopReason.UnrecoverableNetworkChange](https://developer.apple.com/documentation/networkextension/neproviderstopreason/unrecoverablenetworkchange)Added [NEProviderStopReason.UserInitiated](https://developer.apple.com/documentation/networkextension/neproviderstopreason/userinitiated)Added [NEProviderStopReason.UserLogout](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonuserlogout)Added [NEProviderStopReason.UserSwitch](https://developer.apple.com/documentation/networkextension/neproviderstopreason/userswitch)Added [NEProxyServer](https://developer.apple.com/documentation/networkextension/neproxyserver)Added [NEProxyServer.address](https://developer.apple.com/documentation/networkextension/neproxyserver/1406770-address)Added [NEProxyServer.authenticationRequired](https://developer.apple.com/documentation/networkextension/neproxyserver/1406429-authenticationrequired)Added [NEProxyServer.init(address: String, port: Int)](https://developer.apple.com/documentation/networkextension/neproxyserver/1406208-initwithaddress)Added [NEProxyServer.password](https://developer.apple.com/documentation/networkextension/neproxyserver/1406072-password)Added [NEProxyServer.port](https://developer.apple.com/documentation/networkextension/neproxyserver/1406018-port)Added [NEProxyServer.username](https://developer.apple.com/documentation/networkextension/neproxyserver/1406774-username)Added [NEProxySettings](https://developer.apple.com/documentation/networkextension/neproxysettings)Added [NEProxySettings.autoProxyConfigurationEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406034-autoproxyconfigurationenabled)Added [NEProxySettings.exceptionList](https://developer.apple.com/documentation/networkextension/neproxysettings/1406687-exceptionlist)Added [NEProxySettings.excludeSimpleHostnames](https://developer.apple.com/documentation/networkextension/neproxysettings/1406501-excludesimplehostnames)Added [NEProxySettings.HTTPEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406179-httpenabled)Added [NEProxySettings.HTTPSEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406309-httpsenabled)Added [NEProxySettings.HTTPServer](https://developer.apple.com/documentation/networkextension/neproxysettings/1406834-httpserver)Added [NEProxySettings.HTTPSServer](https://developer.apple.com/documentation/networkextension/neproxysettings/1406366-httpsserver)Added [NEProxySettings.matchDomains](https://developer.apple.com/documentation/networkextension/neproxysettings/1406016-matchdomains)Added [NEProxySettings.proxyAutoConfigurationJavaScript](https://developer.apple.com/documentation/networkextension/neproxysettings/1406766-proxyautoconfigurationjavascript)Added [NEProxySettings.proxyAutoConfigurationURL](https://developer.apple.com/documentation/networkextension/neproxysettings/1406225-proxyautoconfigurationurl)Added [NETunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings)Added [NETunnelNetworkSettings.DNSSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406331-dnssettings)Added [NETunnelNetworkSettings.init(tunnelRemoteAddress: String)](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406032-init)Added [NETunnelNetworkSettings.proxySettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406907-proxysettings)Added [NETunnelNetworkSettings.tunnelRemoteAddress](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406885-tunnelremoteaddress)Added [NETunnelProvider](https://developer.apple.com/documentation/networkextension/netunnelprovider)Added [NETunnelProvider.appRules](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406531-apprules)Added [NETunnelProvider.handleAppMessage(_: NSData, completionHandler: ((NSData?) -> Void)?)](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406545-handleappmessage)Added [NETunnelProvider.protocolConfiguration](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406737-protocolconfiguration)Added [NETunnelProvider.reasserting](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406276-reasserting)Added [NETunnelProvider.routingMethod](https://developer.apple.com/documentation/networkextension/netunnelprovider/1405979-routingmethod)Added [NETunnelProvider.setTunnelNetworkSettings(_: NETunnelNetworkSettings?, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406539-settunnelnetworksettings)Added [NETunnelProviderError [enum]](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code)Added [NETunnelProviderError.NetworkSettingsCanceled](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingscanceled)Added [NETunnelProviderError.NetworkSettingsFailed](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingsfailed)Added [NETunnelProviderError.NetworkSettingsInvalid](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingsinvalid)Added [NETunnelProviderManager](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager)Added [NETunnelProviderManager.copyAppRules() -> [NEAppRule]?](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1406386-copyapprules)Added [NETunnelProviderManager.loadAllFromPreferencesWithCompletionHandler(_: ([NETunnelProviderManager]?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1406271-loadallfrompreferences)Added [NETunnelProviderManager.routingMethod](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1405997-routingmethod)Added [NETunnelProviderProtocol](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol)Added [NETunnelProviderProtocol.providerBundleIdentifier](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/1406582-providerbundleidentifier)Added [NETunnelProviderProtocol.providerConfiguration](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/1406206-providerconfiguration)Added [NETunnelProviderRoutingMethod [enum]](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod)Added [NETunnelProviderRoutingMethod.DestinationIP](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod/destinationip)Added [NETunnelProviderRoutingMethod.SourceApplication](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod/sourceapplication)Added [NETunnelProviderSession](https://developer.apple.com/documentation/networkextension/netunnelprovidersession)Added [NETunnelProviderSession.sendProviderMessage(_: NSData, responseHandler: ((NSData?) -> Void)?) throws](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1406409-sendprovidermessage)Added [NETunnelProviderSession.startTunnelWithOptions(_: [String : AnyObject]?) throws](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1405991-starttunnelwithoptions)Added [NETunnelProviderSession.stopTunnel()](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1406662-stoptunnel)Added [NEVPNConnection.connectedDate](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406140-connecteddate)Added [NEVPNConnection.startVPNTunnelWithOptions(_: [String : NSObject]?) throws](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406061-startvpntunnelwithoptions)Added [NEVPNError.ConfigurationReadWriteFailed](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconfigurationreadwritefailed)Added [NEVPNError.ConfigurationUnknown](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconfigurationunknown)Added [NEVPNManager.protocolConfiguration](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406457-protocolconfiguration)Added [NEVPNProtocol.identityReference](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406609-identityreference)Added [NEVPNProtocol.proxySettings](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406635-proxysettings)Added [NEVPNProtocolIKEv2.disableMOBIKE](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406793-disablemobike)Added [NEVPNProtocolIKEv2.disableRedirect](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406591-disableredirect)Added [NEVPNProtocolIKEv2.enablePFS](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406173-enablepfs)Added [NEVPNProtocolIKEv2.enableRevocationCheck](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406490-enablerevocationcheck)Added [NEVPNProtocolIKEv2.strictRevocationCheck](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406417-strictrevocationcheck)Added [NEVPNProtocolIKEv2.useConfigurationAttributeInternalIPSubnet](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406181-useconfigurationattributeinterna)Added [NSMutableURLRequest.bindToHotspotHelperCommand(_: NEHotspotHelperCommand)](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1619006-bind)Added [NWBonjourServiceEndpoint](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint)Added [NWBonjourServiceEndpoint.domain](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406351-domain)Added [NWBonjourServiceEndpoint.init(name: String, type: String, domain: String)](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406261-endpointwithname)Added [NWBonjourServiceEndpoint.name](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406006-name)Added [NWBonjourServiceEndpoint.type](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406290-type)Added [NWEndpoint](https://developer.apple.com/documentation/networkextension/nwendpoint)Added [NWHostEndpoint](https://developer.apple.com/documentation/networkextension/nwhostendpoint)Added [NWHostEndpoint.hostname](https://developer.apple.com/documentation/networkextension/nwhostendpoint/1406580-hostname)Added [NWHostEndpoint.init(hostname: String, port: String)](https://developer.apple.com/documentation/networkextension/nwhostendpoint/1406263-init)Added [NWHostEndpoint.port](https://developer.apple.com/documentation/networkextension/nwhostendpoint/1406241-port)Added [NWPath](https://developer.apple.com/documentation/networkextension/nwpath)Added [NWPath.expensive](https://developer.apple.com/documentation/networkextension/nwpath/1406899-isexpensive)Added [NWPath.isEqualToPath(_: NWPath) -> Bool](https://developer.apple.com/documentation/networkextension/nwpath/1406152-isequal)Added [NWPath.status](https://developer.apple.com/documentation/networkextension/nwpath/1406329-status)Added [NWPathStatus [enum]](https://developer.apple.com/documentation/networkextension/nwpathstatus)Added [NWPathStatus.Invalid](https://developer.apple.com/documentation/networkextension/nwpathstatus/invalid)Added [NWPathStatus.Satisfiable](https://developer.apple.com/documentation/networkextension/nwpathstatus/nwpathstatussatisfiable)Added [NWPathStatus.Satisfied](https://developer.apple.com/documentation/networkextension/nwpathstatus/satisfied)Added [NWPathStatus.Unsatisfied](https://developer.apple.com/documentation/networkextension/nwpathstatus/nwpathstatusunsatisfied)Added [NWTCPConnection](https://developer.apple.com/documentation/networkextension/nwtcpconnection)Added [NWTCPConnection.cancel()](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406022-cancel)Added [NWTCPConnection.connectedPath](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406725-connectedpath)Added [NWTCPConnection.endpoint](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406838-endpoint)Added [NWTCPConnection.error](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406126-error)Added [NWTCPConnection.hasBetterPath](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406693-hasbetterpath)Added [NWTCPConnection.init(upgradeForConnection: NWTCPConnection)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406751-init)Added [NWTCPConnection.localAddress](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406265-localaddress)Added [NWTCPConnection.readLength(_: Int, completionHandler: (NSData?, NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406652-readlength)Added [NWTCPConnection.readMinimumLength(_: Int, maximumLength: Int, completionHandler: (NSData?, NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406156-readminimumlength)Added [NWTCPConnection.remoteAddress](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406014-remoteaddress)Added [NWTCPConnection.state](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406705-state)Added [NWTCPConnection.txtRecord](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406547-txtrecord)Added [NWTCPConnection.viable](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406292-isviable)Added [NWTCPConnection.write(_: NSData, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406631-write)Added [NWTCPConnection.writeClose()](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406695-writeclose)Added [NWTCPConnectionAuthenticationDelegate](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate)Added [NWTCPConnectionAuthenticationDelegate.evaluateTrustForConnection(_: NWTCPConnection, peerCertificateChain: [AnyObject], completionHandler: (SecTrust) -> Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406024-evaluatetrustforconnection)Added [NWTCPConnectionAuthenticationDelegate.provideIdentityForConnection(_: NWTCPConnection, completionHandler: (SecIdentity, [AnyObject]) -> Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406235-provideidentityforconnection)Added [NWTCPConnectionAuthenticationDelegate.shouldEvaluateTrustForConnection(_: NWTCPConnection) -> Bool](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406116-shouldevaluatetrust)Added [NWTCPConnectionAuthenticationDelegate.shouldProvideIdentityForConnection(_: NWTCPConnection) -> Bool](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406689-shouldprovideidentity)Added [NWTCPConnectionState [enum]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate)Added [NWTCPConnectionState.Cancelled](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/cancelled)Added [NWTCPConnectionState.Connected](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstateconnected)Added [NWTCPConnectionState.Connecting](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstateconnecting)Added [NWTCPConnectionState.Disconnected](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstatedisconnected)Added [NWTCPConnectionState.Invalid](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/invalid)Added [NWTCPConnectionState.Waiting](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/waiting)Added [NWTLSParameters](https://developer.apple.com/documentation/networkextension/nwtlsparameters)Added [NWTLSParameters.maximumSSLProtocolVersion](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406010-maximumsslprotocolversion)Added [NWTLSParameters.minimumSSLProtocolVersion](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406571-minimumsslprotocolversion)Added [NWTLSParameters.SSLCipherSuites](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406533-sslciphersuites)Added [NWTLSParameters.TLSSessionID](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406569-tlssessionid)Added [NWUDPSession](https://developer.apple.com/documentation/networkextension/nwudpsession)Added [NWUDPSession.cancel()](https://developer.apple.com/documentation/networkextension/nwudpsession/1406629-cancel)Added [NWUDPSession.currentPath](https://developer.apple.com/documentation/networkextension/nwudpsession/1406296-currentpath)Added [NWUDPSession.endpoint](https://developer.apple.com/documentation/networkextension/nwudpsession/1406388-endpoint)Added [NWUDPSession.hasBetterPath](https://developer.apple.com/documentation/networkextension/nwudpsession/1406231-hasbetterpath)Added [NWUDPSession.init(upgradeForSession: NWUDPSession)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406905-initwithupgradeforsession)Added [NWUDPSession.maximumDatagramLength](https://developer.apple.com/documentation/networkextension/nwudpsession/1406419-maximumdatagramlength)Added [NWUDPSession.resolvedEndpoint](https://developer.apple.com/documentation/networkextension/nwudpsession/1406190-resolvedendpoint)Added [NWUDPSession.setReadHandler(_: ([NSData]?, NSError?) -> Void, maxDatagrams: Int)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406772-setreadhandler)Added [NWUDPSession.state](https://developer.apple.com/documentation/networkextension/nwudpsession/1406901-state)Added [NWUDPSession.tryNextResolvedEndpoint()](https://developer.apple.com/documentation/networkextension/nwudpsession/1406223-trynextresolvedendpoint)Added [NWUDPSession.viable](https://developer.apple.com/documentation/networkextension/nwudpsession/1406357-viable)Added [NWUDPSession.writeDatagram(_: NSData, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406079-writedatagram)Added [NWUDPSession.writeMultipleDatagrams(_: [NSData], completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406390-writemultipledatagrams)Added [NWUDPSessionState [enum]](https://developer.apple.com/documentation/networkextension/nwudpsessionstate)Added [NWUDPSessionState.Cancelled](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/cancelled)Added [NWUDPSessionState.Failed](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/failed)Added [NWUDPSessionState.Invalid](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/invalid)Added [NWUDPSessionState.Preparing](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstatepreparing)Added [NWUDPSessionState.Ready](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstateready)Added [NWUDPSessionState.Waiting](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstatewaiting)Added [kNEHotspotHelperOptionDisplayName](https://developer.apple.com/documentation/networkextension/knehotspothelperoptiondisplayname)Added [NEAppProxyErrorDomain](https://developer.apple.com/documentation/networkextension/neappproxyerrordomain)Added [NEFilterConfigurationDidChangeNotification](https://developer.apple.com/documentation/networkextension/nefilterconfigurationdidchangenotification)Added [NEFilterErrorDomain](https://developer.apple.com/documentation/networkextension/nefiltererrordomain)Added [NEFilterFlowBytesMax](https://developer.apple.com/documentation/networkextension/nefilterflowbytesmax)Added [NEFilterProviderRemediationMapRemediationButtonTexts](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationmapremediationbuttontexts)Added [NEFilterProviderRemediationMapRemediationURLs](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationmapremediationurls)Added [NEFilterProviderRemediationURLFlowURL](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlflowurl)Added [NEFilterProviderRemediationURLFlowURLHostname](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlflowurlhostname)Added [NEFilterProviderRemediationURLOrganization](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlorganization)Added [NEFilterProviderRemediationURLUsername](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlusername)Added [NEHotspotHelperHandler](https://developer.apple.com/documentation/networkextension/nehotspothelperhandler)Added [NETunnelProviderErrorDomain](https://developer.apple.com/documentation/networkextension/netunnelprovidererrordomain)Added [NEVPNConnectionStartOptionPassword](https://developer.apple.com/documentation/networkextension/nevpnconnectionstartoptionpassword)Added [NEVPNConnectionStartOptionUsername](https://developer.apple.com/documentation/networkextension/nevpnconnectionstartoptionusername)Modified [NEEvaluateConnectionRule](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule)

|  | Declaration |
| --- | --- |
| From | ``` class NEEvaluateConnectionRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     init!(matchDomains domains: [AnyObject]!, andAction action: NEEvaluateConnectionRuleAction)     var action: NEEvaluateConnectionRuleAction { get }     var matchDomains: [AnyObject]! { get }     var useDNSServers: [AnyObject]!     @NSCopying var probeURL: NSURL! } ``` |
| To | ``` class NEEvaluateConnectionRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction)     var action: NEEvaluateConnectionRuleAction { get }     var matchDomains: [String] { get }     var useDNSServers: [String]?     @NSCopying var probeURL: NSURL? } ``` |

Modified [NEEvaluateConnectionRule.init(matchDomains: [String], andAction: NEEvaluateConnectionRuleAction)](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406315-initwithmatchdomains)

|  | Declaration |
| --- | --- |
| From | ``` init!(matchDomains domains: [AnyObject]!, andAction action: NEEvaluateConnectionRuleAction) ``` |
| To | ``` init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction) ``` |

Modified [NEEvaluateConnectionRule.matchDomains](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406096-matchdomains)

|  | Declaration |
| --- | --- |
| From | ``` var matchDomains: [AnyObject]! { get } ``` |
| To | ``` var matchDomains: [String] { get } ``` |

Modified [NEEvaluateConnectionRule.probeURL](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406082-probeurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var probeURL: NSURL! ``` |
| To | ``` @NSCopying var probeURL: NSURL? ``` |

Modified [NEEvaluateConnectionRule.useDNSServers](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406319-usednsservers)

|  | Declaration |
| --- | --- |
| From | ``` var useDNSServers: [AnyObject]! ``` |
| To | ``` var useDNSServers: [String]? ``` |

Modified [NEEvaluateConnectionRuleAction [enum]](https://developer.apple.com/documentation/networkextension/neevaluateconnectionruleaction)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 8.0 | Int |

Modified [NEOnDemandRule](https://developer.apple.com/documentation/networkextension/neondemandrule)

|  | Declaration |
| --- | --- |
| From | ``` class NEOnDemandRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     var action: NEOnDemandRuleAction { get }     var DNSSearchDomainMatch: [AnyObject]!     var DNSServerAddressMatch: [AnyObject]!     var interfaceTypeMatch: NEOnDemandRuleInterfaceType     var SSIDMatch: [AnyObject]!     @NSCopying var probeURL: NSURL! } ``` |
| To | ``` class NEOnDemandRule : NSObject, NSSecureCoding, NSCoding, NSCopying {     var action: NEOnDemandRuleAction { get }     var DNSSearchDomainMatch: [String]?     var DNSServerAddressMatch: [String]?     var interfaceTypeMatch: NEOnDemandRuleInterfaceType     var SSIDMatch: [String]?     @NSCopying var probeURL: NSURL? } ``` |

Modified [NEOnDemandRule.DNSSearchDomainMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406150-dnssearchdomainmatch)

|  | Declaration |
| --- | --- |
| From | ``` var DNSSearchDomainMatch: [AnyObject]! ``` |
| To | ``` var DNSSearchDomainMatch: [String]? ``` |

Modified [NEOnDemandRule.DNSServerAddressMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406551-dnsserveraddressmatch)

|  | Declaration |
| --- | --- |
| From | ``` var DNSServerAddressMatch: [AnyObject]! ``` |
| To | ``` var DNSServerAddressMatch: [String]? ``` |

Modified [NEOnDemandRule.probeURL](https://developer.apple.com/documentation/networkextension/neondemandrule/1405981-probeurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var probeURL: NSURL! ``` |
| To | ``` @NSCopying var probeURL: NSURL? ``` |

Modified [NEOnDemandRule.SSIDMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406503-ssidmatch)

|  | Declaration |
| --- | --- |
| From | ``` var SSIDMatch: [AnyObject]! ``` |
| To | ``` var SSIDMatch: [String]? ``` |

Modified [NEOnDemandRuleAction [enum]](https://developer.apple.com/documentation/networkextension/neondemandruleaction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NEOnDemandRuleEvaluateConnection](https://developer.apple.com/documentation/networkextension/neondemandruleevaluateconnection)

|  | Declaration |
| --- | --- |
| From | ``` class NEOnDemandRuleEvaluateConnection : NEOnDemandRule {     var connectionRules: [AnyObject]! } ``` |
| To | ``` class NEOnDemandRuleEvaluateConnection : NEOnDemandRule {     var connectionRules: [NEEvaluateConnectionRule]? } ``` |

Modified [NEOnDemandRuleEvaluateConnection.connectionRules](https://developer.apple.com/documentation/networkextension/neondemandruleevaluateconnection/1405987-connectionrules)

|  | Declaration |
| --- | --- |
| From | ``` var connectionRules: [AnyObject]! ``` |
| To | ``` var connectionRules: [NEEvaluateConnectionRule]? ``` |

Modified [NEOnDemandRuleInterfaceType [enum]](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NEOnDemandRuleInterfaceType : Int {     case Ethernet     case WiFi     case Cellular } ``` | -- |
| To | ``` enum NEOnDemandRuleInterfaceType : Int {     case Any     case Ethernet     case WiFi     case Cellular } ``` | Int |

Modified [NEVPNConnection](https://developer.apple.com/documentation/networkextension/nevpnconnection)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNConnection : NSObject {     func startVPNTunnelAndReturnError(_ error: NSErrorPointer) -> Bool     func stopVPNTunnel()     var status: NEVPNStatus { get } } ``` |
| To | ``` class NEVPNConnection : NSObject {     func startVPNTunnel() throws     func startVPNTunnelWithOptions(_ options: [String : NSObject]?) throws     func stopVPNTunnel()     var status: NEVPNStatus { get }     var connectedDate: NSDate? { get } } ``` |

Modified [NEVPNConnection.startVPNTunnel() throws](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406492-startvpntunnelandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func startVPNTunnelAndReturnError(_ error: NSErrorPointer) -> Bool ``` |
| To | ``` func startVPNTunnel() throws ``` |

Modified [NEVPNError [enum]](https://developer.apple.com/documentation/networkextension/nevpnerror/code)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum NEVPNError : Int {     case ConfigurationInvalid     case ConfigurationDisabled     case ConnectionFailed     case ConfigurationStale } ``` | -- |
| To | ``` enum NEVPNError : Int {     case ConfigurationInvalid     case ConfigurationDisabled     case ConnectionFailed     case ConfigurationStale     case ConfigurationReadWriteFailed     case ConfigurationUnknown } ``` | Int |

Modified [NEVPNIKEAuthenticationMethod [enum]](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NEVPNIKEv2CertificateType [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype)

|  | Introduction | Raw Value Type |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 8.3 | Int |

Modified [NEVPNIKEv2DeadPeerDetectionRate [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NEVPNIKEv2DiffieHellmanGroup [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NEVPNIKEv2EncryptionAlgorithm [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NEVPNIKEv2IntegrityAlgorithm [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2integrityalgorithm)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [NEVPNManager](https://developer.apple.com/documentation/networkextension/nevpnmanager)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNManager : NSObject {     class func sharedManager() -> NEVPNManager!     func loadFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     func removeFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     func saveToPreferencesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     var onDemandRules: [AnyObject]!     var onDemandEnabled: Bool     var localizedDescription: String!     var `protocol`: NEVPNProtocol!     var connection: NEVPNConnection! { get }     var enabled: Bool } ``` |
| To | ``` class NEVPNManager : NSObject {     class func sharedManager() -> NEVPNManager     func loadFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     func removeFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     func saveToPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     var onDemandRules: [NEOnDemandRule]?     var onDemandEnabled: Bool     var localizedDescription: String?     var `protocol`: NEVPNProtocol?     var protocolConfiguration: NEVPNProtocol?     var connection: NEVPNConnection { get }     var enabled: Bool } ``` |

Modified [NEVPNManager.connection](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406252-connection)

|  | Declaration |
| --- | --- |
| From | ``` var connection: NEVPNConnection! { get } ``` |
| To | ``` var connection: NEVPNConnection { get } ``` |

Modified [NEVPNManager.loadFromPreferencesWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406177-loadfrompreferenceswithcompletio)

|  | Declaration |
| --- | --- |
| From | ``` func loadFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func loadFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |

Modified [NEVPNManager.localizedDescription](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406280-localizeddescription)

|  | Declaration |
| --- | --- |
| From | ``` var localizedDescription: String! ``` |
| To | ``` var localizedDescription: String? ``` |

Modified [NEVPNManager.onDemandRules](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406862-ondemandrules)

|  | Declaration |
| --- | --- |
| From | ``` var onDemandRules: [AnyObject]! ``` |
| To | ``` var onDemandRules: [NEOnDemandRule]? ``` |

Modified [NEVPNManager.protocol](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406378-protocol)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var `protocol`: NEVPNProtocol! ``` | -- |
| To | ``` var `protocol`: NEVPNProtocol? ``` | iOS 9.0 |

Modified [NEVPNManager.removeFromPreferencesWithCompletionHandler(_: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406202-removefrompreferenceswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func removeFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |

Modified [NEVPNManager.saveToPreferencesWithCompletionHandler(_: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1405985-savetopreferenceswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` func saveToPreferencesWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func saveToPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |

Modified [NEVPNManager.sharedManager() -> NEVPNManager [class]](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406039-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedManager() -> NEVPNManager! ``` |
| To | ``` class func sharedManager() -> NEVPNManager ``` |

Modified [NEVPNProtocol](https://developer.apple.com/documentation/networkextension/nevpnprotocol)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNProtocol : NSObject, NSCopying, NSSecureCoding, NSCoding {     var serverAddress: String!     var username: String!     @NSCopying var passwordReference: NSData!     @NSCopying var identityReference: NSData!     @NSCopying var identityData: NSData!     var identityDataPassword: String!     var disconnectOnSleep: Bool } ``` |
| To | ``` class NEVPNProtocol : NSObject, NSCopying, NSSecureCoding, NSCoding {     var serverAddress: String?     var username: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData?     @NSCopying var identityData: NSData?     var identityDataPassword: String?     var disconnectOnSleep: Bool     @NSCopying var proxySettings: NEProxySettings? } ``` |

Modified [NEVPNProtocol.identityData](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406142-identitydata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var identityData: NSData! ``` |
| To | ``` @NSCopying var identityData: NSData? ``` |

Modified [NEVPNProtocol.identityDataPassword](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406353-identitydatapassword)

|  | Declaration |
| --- | --- |
| From | ``` var identityDataPassword: String! ``` |
| To | ``` var identityDataPassword: String? ``` |

Modified [NEVPNProtocol.passwordReference](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406650-passwordreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var passwordReference: NSData! ``` |
| To | ``` @NSCopying var passwordReference: NSData? ``` |

Modified [NEVPNProtocol.serverAddress](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406124-serveraddress)

|  | Declaration |
| --- | --- |
| From | ``` var serverAddress: String! ``` |
| To | ``` var serverAddress: String? ``` |

Modified [NEVPNProtocol.username](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406196-username)

|  | Declaration |
| --- | --- |
| From | ``` var username: String! ``` |
| To | ``` var username: String? ``` |

Modified [NEVPNProtocolIKEv2](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNProtocolIKEv2 : NEVPNProtocolIPSec {     var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate     var serverCertificateIssuerCommonName: String!     var serverCertificateCommonName: String!     var certificateType: NEVPNIKEv2CertificateType     var IKESecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters! { get }     var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters! { get } } ``` |
| To | ``` class NEVPNProtocolIKEv2 : NEVPNProtocolIPSec {     var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate     var serverCertificateIssuerCommonName: String?     var serverCertificateCommonName: String?     var certificateType: NEVPNIKEv2CertificateType     var useConfigurationAttributeInternalIPSubnet: Bool     var IKESecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }     var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }     var disableMOBIKE: Bool     var disableRedirect: Bool     var enablePFS: Bool     var enableRevocationCheck: Bool     var strictRevocationCheck: Bool } ``` |

Modified [NEVPNProtocolIKEv2.certificateType](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406860-certificatetype)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNProtocolIKEv2.childSecurityAssociationParameters](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406472-childsecurityassociationparamete)

|  | Declaration |
| --- | --- |
| From | ``` var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters! { get } ``` |
| To | ``` var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get } ``` |

Modified [NEVPNProtocolIKEv2.IKESecurityAssociationParameters](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406214-ikesecurityassociationparameters)

|  | Declaration |
| --- | --- |
| From | ``` var IKESecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters! { get } ``` |
| To | ``` var IKESecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get } ``` |

Modified [NEVPNProtocolIKEv2.serverCertificateCommonName](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406450-servercertificatecommonname)

|  | Declaration |
| --- | --- |
| From | ``` var serverCertificateCommonName: String! ``` |
| To | ``` var serverCertificateCommonName: String? ``` |

Modified [NEVPNProtocolIKEv2.serverCertificateIssuerCommonName](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406333-servercertificateissuercommonnam)

|  | Declaration |
| --- | --- |
| From | ``` var serverCertificateIssuerCommonName: String! ``` |
| To | ``` var serverCertificateIssuerCommonName: String? ``` |

Modified [NEVPNProtocolIPSec](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNProtocolIPSec : NEVPNProtocol {     var authenticationMethod: NEVPNIKEAuthenticationMethod     var useExtendedAuthentication: Bool     @NSCopying var sharedSecretReference: NSData!     var localIdentifier: String!     var remoteIdentifier: String! } ``` |
| To | ``` class NEVPNProtocolIPSec : NEVPNProtocol {     var authenticationMethod: NEVPNIKEAuthenticationMethod     var useExtendedAuthentication: Bool     @NSCopying var sharedSecretReference: NSData?     var localIdentifier: String?     var remoteIdentifier: String? } ``` |

Modified [NEVPNProtocolIPSec.localIdentifier](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec/1406431-localidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var localIdentifier: String! ``` |
| To | ``` var localIdentifier: String? ``` |

Modified [NEVPNProtocolIPSec.remoteIdentifier](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec/1406239-remoteidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var remoteIdentifier: String! ``` |
| To | ``` var remoteIdentifier: String? ``` |

Modified [NEVPNProtocolIPSec.sharedSecretReference](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec/1406112-sharedsecretreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sharedSecretReference: NSData! ``` |
| To | ``` @NSCopying var sharedSecretReference: NSData? ``` |

Modified [NEVPNStatus [enum]](https://developer.apple.com/documentation/networkextension/nevpnstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
