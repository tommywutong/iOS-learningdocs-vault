---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/NetworkExtension.html
archived_at: '2026-07-18T02:56:35.713696Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# NetworkExtension Changes for Objective-C

### NetworkExtension

#### NEAppProxyFlow.h (Added)

Added [NEAppProxyFlow](https://developer.apple.com/documentation/networkextension/neappproxyflow)Added [-[NEAppProxyFlow closeReadWithError:]](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406561-closereadwitherror)Added [-[NEAppProxyFlow closeWriteWithError:]](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406664-closewritewitherror)Added [NEAppProxyFlow.metaData](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406171-metadata)Added [-[NEAppProxyFlow openWithLocalEndpoint:completionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406476-open)Added [NEFlowMetaData](https://developer.apple.com/documentation/networkextension/neflowmetadata)Added [NEFlowMetaData.sourceAppSigningIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406840-sourceappsigningidentifier)Added [NEFlowMetaData.sourceAppUniqueIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406448-sourceappuniqueidentifier)Added [NEAppProxyErrorDomain](https://developer.apple.com/documentation/networkextension/neappproxyerrordomain)Added #def NEAPPPROXYFLOW_EXPORTAdded [NEAppProxyFlowError](https://developer.apple.com/documentation/networkextension/neappproxyflowerror)Added [NEAppProxyFlowErrorAborted](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/aborted)Added [NEAppProxyFlowErrorHostUnreachable](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/hostunreachable)Added [NEAppProxyFlowErrorInternal](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrorinternal)Added [NEAppProxyFlowErrorInvalidArgument](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/invalidargument)Added [NEAppProxyFlowErrorNotConnected](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrornotconnected)Added [NEAppProxyFlowErrorPeerReset](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrorpeerreset)Added [NEAppProxyFlowErrorRefused](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/refused)Added [NEAppProxyFlowErrorTimedOut](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/timedout)

#### NEAppProxyProvider.h (Added)

Added [NEAppProxyProvider](https://developer.apple.com/documentation/networkextension/neappproxyprovider)Added [-[NEAppProxyProvider cancelProxyWithError:]](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405081-cancelproxywitherror)Added [-[NEAppProxyProvider handleNewFlow:]](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405085-handlenewflow)Added [-[NEAppProxyProvider startProxyWithOptions:completionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405083-startproxywithoptions)Added [-[NEAppProxyProvider stopProxyWithReason:completionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405077-stopproxy)

#### NEAppProxyProviderManager.h (Added)

Added [NEAppProxyProviderManager](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager)Added [+[NEAppProxyProviderManager loadAllFromPreferencesWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager/1406790-loadallfrompreferenceswithcomple)

#### NEAppProxyTCPFlow.h (Added)

Added [NEAppProxyTCPFlow](https://developer.apple.com/documentation/networkextension/neappproxytcpflow)Added [-[NEAppProxyTCPFlow readDataWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406311-readdata)Added [NEAppProxyTCPFlow.remoteEndpoint](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406233-remoteendpoint)Added [-[NEAppProxyTCPFlow writeData:withCompletionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406776-writedata)

#### NEAppProxyUDPFlow.h (Added)

Added [NEAppProxyUDPFlow](https://developer.apple.com/documentation/networkextension/neappproxyudpflow)Added [NEAppProxyUDPFlow.localEndpoint](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406699-localendpoint)Added [-[NEAppProxyUDPFlow readDatagramsWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406576-readdatagramswithcompletionhandl)Added [-[NEAppProxyUDPFlow writeDatagrams:sentByEndpoints:completionHandler:]](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406784-writedatagrams)

#### NEAppRule.h (Added)

Added [NEAppRule](https://developer.apple.com/documentation/networkextension/neapprule)Added [-[NEAppRule initWithSigningIdentifier:]](https://developer.apple.com/documentation/networkextension/neapprule/1617852-init)Added [NEAppRule.matchDomains](https://developer.apple.com/documentation/networkextension/neapprule/1406488-matchdomains)Added [NEAppRule.matchSigningIdentifier](https://developer.apple.com/documentation/networkextension/neapprule/1406243-matchsigningidentifier)

#### NEDNSSettings.h (Added)

Added [NEDNSSettings](https://developer.apple.com/documentation/networkextension/nednssettings)Added [NEDNSSettings.domainName](https://developer.apple.com/documentation/networkextension/nednssettings/1406440-domainname)Added [-[NEDNSSettings initWithServers:]](https://developer.apple.com/documentation/networkextension/nednssettings/1406478-initwithservers)Added [NEDNSSettings.matchDomains](https://developer.apple.com/documentation/networkextension/nednssettings/1406537-matchdomains)Added [NEDNSSettings.matchDomainsNoSearch](https://developer.apple.com/documentation/networkextension/nednssettings/1406735-matchdomainsnosearch)Added [NEDNSSettings.searchDomains](https://developer.apple.com/documentation/networkextension/nednssettings/1406658-searchdomains)Added [NEDNSSettings.servers](https://developer.apple.com/documentation/networkextension/nednssettings/1406237-servers)

#### NEFilterControlProvider.h (Added)

Added [NEFilterControlProvider](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider)Added [-[NEFilterControlProvider handleNewFlow:completionHandler:]](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614120-handlenewflow)Added [-[NEFilterControlProvider handleRemediationForFlow:completionHandler:]](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614122-handleremediation)Added [-[NEFilterControlProvider notifyRulesChanged]](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614125-notifyruleschanged)Added [NEFilterControlProvider.remediationMap](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614121-remediationmap)Added [NEFilterControlProvider.URLAppendStringMap](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614123-urlappendstringmap)

#### NEFilterDataProvider.h (Added)

Added [NEFilterDataProvider](https://developer.apple.com/documentation/networkextension/nefilterdataprovider)Added [-[NEFilterDataProvider handleInboundDataCompleteForFlow:]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618977-handleinbounddatacomplete)Added [-[NEFilterDataProvider handleInboundDataFromFlow:readBytesStartOffset:readBytes:]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618933-handleinbounddatafromflow)Added [-[NEFilterDataProvider handleNewFlow:]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618918-handlenewflow)Added [-[NEFilterDataProvider handleOutboundDataCompleteForFlow:]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618961-handleoutbounddatacomplete)Added [-[NEFilterDataProvider handleOutboundDataFromFlow:readBytesStartOffset:readBytes:]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618954-handleoutbounddata)Added [-[NEFilterDataProvider handleRemediationForFlow:]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618928-handleremediation)Added [-[NEFilterDataProvider handleRulesChanged]](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618919-handleruleschanged)Added [NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataverdict)Added [+[NEFilterDataVerdict allowVerdict]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1619010-allowverdict)Added [+[NEFilterDataVerdict dataVerdictWithPassBytes:peekBytes:]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1619005-init)Added [+[NEFilterDataVerdict dropVerdict]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618952-drop)Added [+[NEFilterDataVerdict needRulesVerdict]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618993-needrulesverdict)Added [+[NEFilterDataVerdict remediateVerdictWithRemediationURLMapKey:remediationButtonTextMapKey:]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618964-remediateverdictwithremediationu)Added [NEFilterRemediationVerdict](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict)Added [+[NEFilterRemediationVerdict allowVerdict]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618962-allow)Added [+[NEFilterRemediationVerdict dropVerdict]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618947-dropverdict)Added [+[NEFilterRemediationVerdict needRulesVerdict]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618972-needrules)Added #def NEFILTER_DATA_PROVIDER_EXTERN

#### NEFilterFlow.h (Added)

Added [NEFilterBrowserFlow](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow)Added [NEFilterBrowserFlow.parentURL](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618932-parenturl)Added [NEFilterBrowserFlow.request](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618948-request)Added [NEFilterBrowserFlow.response](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618966-response)Added [NEFilterFlow](https://developer.apple.com/documentation/networkextension/nefilterflow)Added [NEFilterFlow.URL](https://developer.apple.com/documentation/networkextension/nefilterflow/1618935-url)Added [NEFilterSocketFlow](https://developer.apple.com/documentation/networkextension/nefiltersocketflow)Added [NEFilterSocketFlow.localEndpoint](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1619004-localendpoint)Added [NEFilterSocketFlow.remoteEndpoint](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618940-remoteendpoint)Added [NEFilterSocketFlow.socketFamily](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618983-socketfamily)Added [NEFilterSocketFlow.socketProtocol](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618953-socketprotocol)Added [NEFilterSocketFlow.socketType](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618956-sockettype)Added [#def NEFilterFlowBytesMax](https://developer.apple.com/documentation/networkextension/nefilterflowbytesmax)

#### NEFilterManager.h (Added)

Added [NEFilterManager](https://developer.apple.com/documentation/networkextension/nefiltermanager)Added [NEFilterManager.enabled](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406158-isenabled)Added [-[NEFilterManager loadFromPreferencesWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406359-loadfrompreferenceswithcompletio)Added [NEFilterManager.localizedDescription](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406375-localizeddescription)Added [NEFilterManager.providerConfiguration](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406070-providerconfiguration)Added [-[NEFilterManager removeFromPreferencesWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406876-removefrompreferenceswithcomplet)Added [-[NEFilterManager saveToPreferencesWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406339-savetopreferenceswithcompletionh)Added [+[NEFilterManager sharedManager]](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406438-sharedmanager)Added #def NEFILTER_EXPORTAdded [NEFilterConfigurationDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1406656-nefilterconfigurationdidchange)Added [NEFilterErrorDomain](https://developer.apple.com/documentation/networkextension/nefiltererrordomain)Added [NEFilterManagerError](https://developer.apple.com/documentation/networkextension/nefiltermanagererror)Added [NEFilterManagerErrorConfigurationCannotBeRemoved](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/nefiltermanagererrorconfigurationcannotberemoved)Added [NEFilterManagerErrorConfigurationDisabled](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationdisabled)Added [NEFilterManagerErrorConfigurationInvalid](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/nefiltermanagererrorconfigurationinvalid)Added [NEFilterManagerErrorConfigurationStale](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationstale)

#### NEFilterProvider.h (Added)

Added [NEFilterControlVerdict](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict)Added [+[NEFilterControlVerdict allowVerdictWithUpdateRules:]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617040-allow)Added [+[NEFilterControlVerdict dropVerdictWithUpdateRules:]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617044-drop)Added [+[NEFilterControlVerdict updateRules]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617037-updaterules)Added [NEFilterNewFlowVerdict](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict)Added [+[NEFilterNewFlowVerdict allowVerdict]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617036-allow)Added [+[NEFilterNewFlowVerdict dropVerdict]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617035-dropverdict)Added [+[NEFilterNewFlowVerdict filterDataVerdictWithFilterInbound:peekInboundBytes:filterOutbound:peekOutboundBytes:]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617038-filterdataverdict)Added [+[NEFilterNewFlowVerdict needRulesVerdict]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617034-needrules)Added [+[NEFilterNewFlowVerdict remediateVerdictWithRemediationURLMapKey:remediationButtonTextMapKey:]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617042-remediateverdictwithremediationu)Added [+[NEFilterNewFlowVerdict URLAppendStringVerdictWithMapKey:]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617046-urlappendstringverdictwithmapkey)Added [NEFilterProvider](https://developer.apple.com/documentation/networkextension/nefilterprovider)Added [NEFilterProvider.filterConfiguration](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617033-filterconfiguration)Added [-[NEFilterProvider startFilterWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617043-startfilterwithcompletionhandler)Added [-[NEFilterProvider stopFilterWithReason:completionHandler:]](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617032-stopfilterwithreason)Added [NEFilterVerdict](https://developer.apple.com/documentation/networkextension/nefilterverdict)Added #def NEFILTER_EXPORTAdded [NEFilterProviderRemediationMapRemediationButtonTexts](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationmapremediationbuttontexts)Added [NEFilterProviderRemediationMapRemediationURLs](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationmapremediationurls)Added [#def NEFilterProviderRemediationURLFlowURL](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlflowurl)Added [#def NEFilterProviderRemediationURLFlowURLHostname](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlflowurlhostname)Added [#def NEFilterProviderRemediationURLOrganization](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlorganization)Added [#def NEFilterProviderRemediationURLUsername](https://developer.apple.com/documentation/networkextension/nefilterproviderremediationurlusername)

#### NEFilterProviderConfiguration.h (Added)

Added [NEFilterProviderConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration)Added [NEFilterProviderConfiguration.filterBrowsers](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406864-filterbrowsers)Added [NEFilterProviderConfiguration.filterSockets](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406596-filtersockets)Added [NEFilterProviderConfiguration.identityReference](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406866-identityreference)Added [NEFilterProviderConfiguration.organization](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406012-organization)Added [NEFilterProviderConfiguration.passwordReference](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406146-passwordreference)Added [NEFilterProviderConfiguration.serverAddress](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406507-serveraddress)Added [NEFilterProviderConfiguration.username](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406482-username)Added [NEFilterProviderConfiguration.vendorConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406347-vendorconfiguration)

#### NEHotspotHelper.h (Added)

Added [NEHotspotHelper](https://developer.apple.com/documentation/networkextension/nehotspothelper)Added [+[NEHotspotHelper logoff:]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618944-logoff)Added [+[NEHotspotHelper registerWithOptions:queue:handler:]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618965-register)Added [+[NEHotspotHelper supportedNetworkInterfaces]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618921-supportednetworkinterfaces)Added [NEHotspotHelperCommand](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand)Added [NEHotspotHelperCommand.commandType](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618942-commandtype)Added [-[NEHotspotHelperCommand createResponse:]](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618931-createresponse)Added [-[NEHotspotHelperCommand createTCPConnection:]](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1619013-createtcpconnection)Added [-[NEHotspotHelperCommand createUDPSession:]](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618934-createudpsession)Added [NEHotspotHelperCommand.network](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1619011-network)Added [NEHotspotHelperCommand.networkList](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/1618967-networklist)Added [NEHotspotHelperResponse](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse)Added [-[NEHotspotHelperResponse deliver]](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/1618974-deliver)Added [-[NEHotspotHelperResponse setNetwork:]](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/1618920-setnetwork)Added [-[NEHotspotHelperResponse setNetworkList:]](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse/1618915-setnetworklist)Added [NEHotspotNetwork](https://developer.apple.com/documentation/networkextension/nehotspotnetwork)Added [NEHotspotNetwork.autoJoined](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618976-autojoined)Added [NEHotspotNetwork.BSSID](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618936-bssid)Added [NEHotspotNetwork.chosenHelper](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618975-chosenhelper)Added [NEHotspotNetwork.justJoined](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618955-justjoined)Added [NEHotspotNetwork.secure](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618930-issecure)Added [-[NEHotspotNetwork setConfidence:]](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618969-setconfidence)Added [-[NEHotspotNetwork setPassword:]](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1619009-setpassword)Added [NEHotspotNetwork.signalStrength](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618923-signalstrength)Added [NEHotspotNetwork.SSID](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618925-ssid)Added [-[NSMutableURLRequest bindToHotspotHelperCommand:]](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1619006-bind)Added [kNEHotspotHelperCommandTypeAuthenticate](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/authenticate)Added [kNEHotspotHelperCommandTypeEvaluate](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/evaluate)Added [kNEHotspotHelperCommandTypeFilterScanList](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypefilterscanlist)Added [kNEHotspotHelperCommandTypeLogoff](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/logoff)Added [kNEHotspotHelperCommandTypeMaintain](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/maintain)Added [kNEHotspotHelperCommandTypeNone](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/none)Added [kNEHotspotHelperCommandTypePresentUI](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypepresentui)Added [kNEHotspotHelperConfidenceHigh](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/knehotspothelperconfidencehigh)Added [kNEHotspotHelperConfidenceLow](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/knehotspothelperconfidencelow)Added [kNEHotspotHelperConfidenceNone](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/none)Added [kNEHotspotHelperOptionDisplayName](https://developer.apple.com/documentation/networkextension/knehotspothelperoptiondisplayname)Added [kNEHotspotHelperResultAuthenticationRequired](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/authenticationrequired)Added [kNEHotspotHelperResultCommandNotRecognized](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultcommandnotrecognized)Added [kNEHotspotHelperResultFailure](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/failure)Added [kNEHotspotHelperResultSuccess](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultsuccess)Added [kNEHotspotHelperResultTemporaryFailure](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresulttemporaryfailure)Added [kNEHotspotHelperResultUIRequired](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultuirequired)Added [kNEHotspotHelperResultUnsupportedNetwork](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/unsupportednetwork)Added [NEHotspotHelperCommandType](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype)Added [NEHotspotHelperConfidence](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence)Added [NEHotspotHelperHandler](https://developer.apple.com/documentation/networkextension/nehotspothelperhandler)Added [NEHotspotHelperResult](https://developer.apple.com/documentation/networkextension/nehotspothelperresult)Added #def NEHS_EXPORTAdded NSMutableURLRequest(NEHotspotHelper)

#### NEIPv4Settings.h (Added)

Added [NEIPv4Route](https://developer.apple.com/documentation/networkextension/neipv4route)Added [+[NEIPv4Route defaultRoute]](https://developer.apple.com/documentation/networkextension/neipv4route/1406474-default)Added [NEIPv4Route.destinationAddress](https://developer.apple.com/documentation/networkextension/neipv4route/1406578-destinationaddress)Added [NEIPv4Route.destinationSubnetMask](https://developer.apple.com/documentation/networkextension/neipv4route/1406411-destinationsubnetmask)Added [NEIPv4Route.gatewayAddress](https://developer.apple.com/documentation/networkextension/neipv4route/1406519-gatewayaddress)Added [-[NEIPv4Route initWithDestinationAddress:subnetMask:]](https://developer.apple.com/documentation/networkextension/neipv4route/1406643-initwithdestinationaddress)Added [NEIPv4Settings](https://developer.apple.com/documentation/networkextension/neipv4settings)Added [NEIPv4Settings.addresses](https://developer.apple.com/documentation/networkextension/neipv4settings/1406666-addresses)Added [NEIPv4Settings.excludedRoutes](https://developer.apple.com/documentation/networkextension/neipv4settings/1406267-excludedroutes)Added [NEIPv4Settings.includedRoutes](https://developer.apple.com/documentation/networkextension/neipv4settings/1406654-includedroutes)Added [-[NEIPv4Settings initWithAddresses:subnetMasks:]](https://developer.apple.com/documentation/networkextension/neipv4settings/1406709-initwithaddresses)Added [NEIPv4Settings.subnetMasks](https://developer.apple.com/documentation/networkextension/neipv4settings/1406160-subnetmasks)

#### NEIPv6Settings.h (Added)

Added [NEIPv6Route](https://developer.apple.com/documentation/networkextension/neipv6route)Added [+[NEIPv6Route defaultRoute]](https://developer.apple.com/documentation/networkextension/neipv6route/1406847-defaultroute)Added [NEIPv6Route.destinationAddress](https://developer.apple.com/documentation/networkextension/neipv6route/1406269-destinationaddress)Added [NEIPv6Route.destinationNetworkPrefixLength](https://developer.apple.com/documentation/networkextension/neipv6route/1406897-destinationnetworkprefixlength)Added [NEIPv6Route.gatewayAddress](https://developer.apple.com/documentation/networkextension/neipv6route/1406691-gatewayaddress)Added [-[NEIPv6Route initWithDestinationAddress:networkPrefixLength:]](https://developer.apple.com/documentation/networkextension/neipv6route/1406245-initwithdestinationaddress)Added [NEIPv6Settings](https://developer.apple.com/documentation/networkextension/neipv6settings)Added [NEIPv6Settings.addresses](https://developer.apple.com/documentation/networkextension/neipv6settings/1406304-addresses)Added [NEIPv6Settings.excludedRoutes](https://developer.apple.com/documentation/networkextension/neipv6settings/1406294-excludedroutes)Added [NEIPv6Settings.includedRoutes](https://developer.apple.com/documentation/networkextension/neipv6settings/1406567-includedroutes)Added [-[NEIPv6Settings initWithAddresses:networkPrefixLengths:]](https://developer.apple.com/documentation/networkextension/neipv6settings/1406407-init)Added [NEIPv6Settings.networkPrefixLengths](https://developer.apple.com/documentation/networkextension/neipv6settings/1406167-networkprefixlengths)

#### NEOnDemandRule.h

Added [NEOnDemandRuleInterfaceTypeAny](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype/any)Modified [-[NEEvaluateConnectionRule initWithMatchDomains:andAction:]](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406315-initwithmatchdomains)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMatchDomains:(NSArray *)domains andAction:(NEEvaluateConnectionRuleAction)action ``` |
| To | ``` - (instancetype _Nonnull)initWithMatchDomains:(NSArray<NSString *> * _Nonnull)domains andAction:(NEEvaluateConnectionRuleAction)action ``` |

Modified [NEEvaluateConnectionRule.matchDomains](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406096-matchdomains)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *matchDomains ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSString *> *matchDomains ``` |

Modified [NEEvaluateConnectionRule.useDNSServers](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406319-usednsservers)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *useDNSServers ``` |
| To | ``` @property(copy, nullable) NSArray<NSString *> *useDNSServers ``` |

Modified [NEOnDemandRule.DNSSearchDomainMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406150-dnssearchdomainmatch)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *DNSSearchDomainMatch ``` |
| To | ``` @property(copy, nullable) NSArray<NSString *> *DNSSearchDomainMatch ``` |

Modified [NEOnDemandRule.DNSServerAddressMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406551-dnsserveraddressmatch)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *DNSServerAddressMatch ``` |
| To | ``` @property(copy, nullable) NSArray<NSString *> *DNSServerAddressMatch ``` |

Modified [NEOnDemandRule.SSIDMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406503-ssidmatch)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *SSIDMatch ``` |
| To | ``` @property(copy, nullable) NSArray<NSString *> *SSIDMatch ``` |

Modified [NEOnDemandRuleEvaluateConnection.connectionRules](https://developer.apple.com/documentation/networkextension/neondemandruleevaluateconnection/1405987-connectionrules)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *connectionRules ``` |
| To | ``` @property(copy, nullable) NSArray<NEEvaluateConnectionRule *> *connectionRules ``` |

#### NEPacketTunnelFlow.h (Added)

Added [NEPacketTunnelFlow](https://developer.apple.com/documentation/networkextension/nepackettunnelflow)Added [-[NEPacketTunnelFlow readPacketsWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/1406903-readpackets)Added [-[NEPacketTunnelFlow writePackets:withProtocols:]](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/1406484-writepackets)

#### NEPacketTunnelNetworkSettings.h (Added)

Added [NEPacketTunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings)Added [NEPacketTunnelNetworkSettings.IPv4Settings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406574-ipv4settings)Added [NEPacketTunnelNetworkSettings.IPv6Settings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406138-ipv6settings)Added [NEPacketTunnelNetworkSettings.MTU](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406094-mtu)Added [NEPacketTunnelNetworkSettings.tunnelOverheadBytes](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406675-tunneloverheadbytes)

#### NEPacketTunnelProvider.h (Added)

Added [NEPacketTunnelProvider](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider)Added [-[NEPacketTunnelProvider cancelTunnelWithError:]](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406169-canceltunnelwitherror)Added [-[NEPacketTunnelProvider createTCPConnectionThroughTunnelToEndpoint:enableTLS:TLSParameters:delegate:]](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406055-createtcpconnectionthroughtunnel)Added [-[NEPacketTunnelProvider createUDPSessionThroughTunnelToEndpoint:fromEndpoint:]](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406068-createudpsessionthroughtunneltoe)Added [NEPacketTunnelProvider.packetFlow](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406185-packetflow)Added [-[NEPacketTunnelProvider startTunnelWithOptions:completionHandler:]](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406118-starttunnelwithoptions)Added [-[NEPacketTunnelProvider stopTunnelWithReason:completionHandler:]](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406192-stoptunnel)

#### NEProvider.h (Added)

Added [NEProvider](https://developer.apple.com/documentation/networkextension/neprovider)Added [-[NEProvider createTCPConnectionToEndpoint:enableTLS:TLSParameters:delegate:]](https://developer.apple.com/documentation/networkextension/neprovider/1406529-createtcpconnection)Added [-[NEProvider createUDPSessionToEndpoint:fromEndpoint:]](https://developer.apple.com/documentation/networkextension/neprovider/1406004-createudpsessiontoendpoint)Added [NEProvider.defaultPath](https://developer.apple.com/documentation/networkextension/neprovider/1406740-defaultpath)Added [-[NEProvider sleepWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/neprovider/1406731-sleepwithcompletionhandler)Added [-[NEProvider wake]](https://developer.apple.com/documentation/networkextension/neprovider/1406543-wake)Added [NEProviderStopReason](https://developer.apple.com/documentation/networkextension/neproviderstopreason)Added [NEProviderStopReasonAuthenticationCanceled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonauthenticationcanceled)Added [NEProviderStopReasonConfigurationDisabled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationdisabled)Added [NEProviderStopReasonConfigurationFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationfailed)Added [NEProviderStopReasonConfigurationRemoved](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationremoved)Added [NEProviderStopReasonConnectionFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconnectionfailed)Added [NEProviderStopReasonIdleTimeout](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonidletimeout)Added [NEProviderStopReasonNone](https://developer.apple.com/documentation/networkextension/neproviderstopreason/none)Added [NEProviderStopReasonNoNetworkAvailable](https://developer.apple.com/documentation/networkextension/neproviderstopreason/nonetworkavailable)Added [NEProviderStopReasonProviderDisabled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonproviderdisabled)Added [NEProviderStopReasonProviderFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonproviderfailed)Added [NEProviderStopReasonSuperceded](https://developer.apple.com/documentation/networkextension/neproviderstopreason/superceded)Added [NEProviderStopReasonUnrecoverableNetworkChange](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonunrecoverablenetworkchange)Added [NEProviderStopReasonUserInitiated](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonuserinitiated)Added [NEProviderStopReasonUserLogout](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonuserlogout)Added [NEProviderStopReasonUserSwitch](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonuserswitch)

#### NEProxySettings.h (Added)

Added [NEProxyServer](https://developer.apple.com/documentation/networkextension/neproxyserver)Added [NEProxyServer.address](https://developer.apple.com/documentation/networkextension/neproxyserver/1406770-address)Added [NEProxyServer.authenticationRequired](https://developer.apple.com/documentation/networkextension/neproxyserver/1406429-authenticationrequired)Added [-[NEProxyServer initWithAddress:port:]](https://developer.apple.com/documentation/networkextension/neproxyserver/1406208-initwithaddress)Added [NEProxyServer.password](https://developer.apple.com/documentation/networkextension/neproxyserver/1406072-password)Added [NEProxyServer.port](https://developer.apple.com/documentation/networkextension/neproxyserver/1406018-port)Added [NEProxyServer.username](https://developer.apple.com/documentation/networkextension/neproxyserver/1406774-username)Added [NEProxySettings](https://developer.apple.com/documentation/networkextension/neproxysettings)Added [NEProxySettings.autoProxyConfigurationEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406034-autoproxyconfigurationenabled)Added [NEProxySettings.exceptionList](https://developer.apple.com/documentation/networkextension/neproxysettings/1406687-exceptionlist)Added [NEProxySettings.excludeSimpleHostnames](https://developer.apple.com/documentation/networkextension/neproxysettings/1406501-excludesimplehostnames)Added [NEProxySettings.HTTPEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406179-httpenabled)Added [NEProxySettings.HTTPSEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406309-httpsenabled)Added [NEProxySettings.HTTPServer](https://developer.apple.com/documentation/networkextension/neproxysettings/1406834-httpserver)Added [NEProxySettings.HTTPSServer](https://developer.apple.com/documentation/networkextension/neproxysettings/1406366-httpsserver)Added [NEProxySettings.matchDomains](https://developer.apple.com/documentation/networkextension/neproxysettings/1406016-matchdomains)Added [NEProxySettings.proxyAutoConfigurationJavaScript](https://developer.apple.com/documentation/networkextension/neproxysettings/1406766-proxyautoconfigurationjavascript)Added [NEProxySettings.proxyAutoConfigurationURL](https://developer.apple.com/documentation/networkextension/neproxysettings/1406225-proxyautoconfigurationurl)

#### NETunnelNetworkSettings.h (Added)

Added [NETunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings)Added [NETunnelNetworkSettings.DNSSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406331-dnssettings)Added [-[NETunnelNetworkSettings initWithTunnelRemoteAddress:]](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406032-init)Added [NETunnelNetworkSettings.proxySettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406907-proxysettings)Added [NETunnelNetworkSettings.tunnelRemoteAddress](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406885-tunnelremoteaddress)

#### NETunnelProvider.h (Added)

Added [NETunnelProvider](https://developer.apple.com/documentation/networkextension/netunnelprovider)Added [NETunnelProvider.appRules](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406531-apprules)Added [-[NETunnelProvider handleAppMessage:completionHandler:]](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406545-handleappmessage)Added [NETunnelProvider.protocolConfiguration](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406737-protocolconfiguration)Added [NETunnelProvider.reasserting](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406276-reasserting)Added [NETunnelProvider.routingMethod](https://developer.apple.com/documentation/networkextension/netunnelprovider/1405979-routingmethod)Added [-[NETunnelProvider setTunnelNetworkSettings:completionHandler:]](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406539-settunnelnetworksettings)Added #def NETUNNELPROVIDER_EXPORTAdded [NETunnelProviderError](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code)Added [NETunnelProviderErrorDomain](https://developer.apple.com/documentation/networkextension/netunnelprovidererrordomain)Added [NETunnelProviderErrorNetworkSettingsCanceled](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingscanceled)Added [NETunnelProviderErrorNetworkSettingsFailed](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code/networksettingsfailed)Added [NETunnelProviderErrorNetworkSettingsInvalid](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code/networksettingsinvalid)Added [NETunnelProviderRoutingMethod](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod)Added [NETunnelProviderRoutingMethodDestinationIP](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod/destinationip)Added [NETunnelProviderRoutingMethodSourceApplication](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod/sourceapplication)

#### NETunnelProviderManager.h (Added)

Added [NETunnelProviderManager](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager)Added [-[NETunnelProviderManager copyAppRules]](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1406386-copyapprules)Added [+[NETunnelProviderManager loadAllFromPreferencesWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1406271-loadallfrompreferenceswithcomple)Added [NETunnelProviderManager.routingMethod](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1405997-routingmethod)

#### NETunnelProviderProtocol.h (Added)

Added [NETunnelProviderProtocol](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol)Added [NETunnelProviderProtocol.providerBundleIdentifier](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/1406582-providerbundleidentifier)Added [NETunnelProviderProtocol.providerConfiguration](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/1406206-providerconfiguration)

#### NETunnelProviderSession.h (Added)

Added [NETunnelProviderSession](https://developer.apple.com/documentation/networkextension/netunnelprovidersession)Added [-[NETunnelProviderSession sendProviderMessage:returnError:responseHandler:]](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1406409-sendprovidermessage)Added [-[NETunnelProviderSession startTunnelWithOptions:andReturnError:]](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1405991-starttunnelwithoptions)Added [-[NETunnelProviderSession stopTunnel]](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1406662-stoptunnel)

#### NEVPNConnection.h

Added [NEVPNConnection.connectedDate](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406140-connecteddate)Added [-[NEVPNConnection startVPNTunnelWithOptions:andReturnError:]](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406061-startvpntunnel)Added [NEVPNConnectionStartOptionPassword](https://developer.apple.com/documentation/networkextension/nevpnconnectionstartoptionpassword)Added [NEVPNConnectionStartOptionUsername](https://developer.apple.com/documentation/networkextension/nevpnconnectionstartoptionusername)

#### NEVPNManager.h

Added [NEVPNManager.protocolConfiguration](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406457-protocolconfiguration)Added [NEVPNErrorConfigurationReadWriteFailed](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconfigurationreadwritefailed)Added [NEVPNErrorConfigurationUnknown](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconfigurationunknown)Modified [NEVPNManager.onDemandRules](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406862-ondemandrules)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *onDemandRules ``` |
| To | ``` @property(copy, nullable) NSArray<NEOnDemandRule *> *onDemandRules ``` |

Modified [NEVPNManager.protocol](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406378-protocol)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### NEVPNProtocol.h

Added [NEVPNProtocol.identityReference](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406609-identityreference)Added [NEVPNProtocol.proxySettings](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406635-proxysettings)

#### NEVPNProtocolIKEv2.h

Added [NEVPNProtocolIKEv2.disableMOBIKE](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406793-disablemobike)Added [NEVPNProtocolIKEv2.disableRedirect](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406591-disableredirect)Added [NEVPNProtocolIKEv2.enablePFS](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406173-enablepfs)Added [NEVPNProtocolIKEv2.enableRevocationCheck](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406490-enablerevocationcheck)Added [NEVPNProtocolIKEv2.strictRevocationCheck](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406417-strictrevocationcheck)Added [NEVPNProtocolIKEv2.useConfigurationAttributeInternalIPSubnet](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406181-useconfigurationattributeinterna)Modified [NEVPNProtocolIKEv2.certificateType](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406860-certificatetype)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNIKEv2CertificateTypeECDSA256](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype/nevpnikev2certificatetypeecdsa256)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNIKEv2CertificateTypeECDSA384](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype/ecdsa384)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNIKEv2CertificateTypeECDSA521](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype/ecdsa521)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNIKEv2CertificateTypeRSA](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype/rsa)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNIKEv2EncryptionAlgorithmAES128GCM](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/algorithmaes128gcm)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified [NEVPNIKEv2EncryptionAlgorithmAES256GCM](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/nevpnikev2encryptionalgorithmaes256gcm)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

#### NWBonjourServiceEndpoint.h (Added)

Added [NWBonjourServiceEndpoint](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint)Added [NWBonjourServiceEndpoint.domain](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406351-domain)Added [+[NWBonjourServiceEndpoint endpointWithName:type:domain:]](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406261-init)Added [NWBonjourServiceEndpoint.name](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406006-name)Added [NWBonjourServiceEndpoint.type](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint/1406290-type)

#### NWEndpoint.h (Added)

Added [NWEndpoint](https://developer.apple.com/documentation/networkextension/nwendpoint)

#### NWHostEndpoint.h (Added)

Added [NWHostEndpoint](https://developer.apple.com/documentation/networkextension/nwhostendpoint)Added [+[NWHostEndpoint endpointWithHostname:port:]](https://developer.apple.com/documentation/networkextension/nwhostendpoint/1406263-init)Added [NWHostEndpoint.hostname](https://developer.apple.com/documentation/networkextension/nwhostendpoint/1406580-hostname)Added [NWHostEndpoint.port](https://developer.apple.com/documentation/networkextension/nwhostendpoint/1406241-port)

#### NWPath.h (Added)

Added [NWPath](https://developer.apple.com/documentation/networkextension/nwpath)Added [NWPath.expensive](https://developer.apple.com/documentation/networkextension/nwpath/1406899-expensive)Added [-[NWPath isEqualToPath:]](https://developer.apple.com/documentation/networkextension/nwpath/1406152-isequaltopath)Added [NWPath.status](https://developer.apple.com/documentation/networkextension/nwpath/1406329-status)Added [NWPathStatus](https://developer.apple.com/documentation/networkextension/nwpathstatus)Added [NWPathStatusInvalid](https://developer.apple.com/documentation/networkextension/nwpathstatus/invalid)Added [NWPathStatusSatisfiable](https://developer.apple.com/documentation/networkextension/nwpathstatus/satisfiable)Added [NWPathStatusSatisfied](https://developer.apple.com/documentation/networkextension/nwpathstatus/nwpathstatussatisfied)Added [NWPathStatusUnsatisfied](https://developer.apple.com/documentation/networkextension/nwpathstatus/nwpathstatusunsatisfied)

#### NWTCPConnection.h (Added)

Added [NWTCPConnection](https://developer.apple.com/documentation/networkextension/nwtcpconnection)Added [-[NWTCPConnection cancel]](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406022-cancel)Added [NWTCPConnection.connectedPath](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406725-connectedpath)Added [NWTCPConnection.endpoint](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406838-endpoint)Added [NWTCPConnection.error](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406126-error)Added [NWTCPConnection.hasBetterPath](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406693-hasbetterpath)Added [-[NWTCPConnection initWithUpgradeForConnection:]](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406751-initwithupgradeforconnection)Added [NWTCPConnection.localAddress](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406265-localaddress)Added [-[NWTCPConnection readLength:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406652-readlength)Added [-[NWTCPConnection readMinimumLength:maximumLength:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406156-readminimumlength)Added [NWTCPConnection.remoteAddress](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406014-remoteaddress)Added [NWTCPConnection.state](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406705-state)Added [NWTCPConnection.txtRecord](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406547-txtrecord)Added [NWTCPConnection.viable](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406292-isviable)Added [-[NWTCPConnection write:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406631-write)Added [-[NWTCPConnection writeClose]](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406695-writeclose)Added [NWTCPConnectionAuthenticationDelegate](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate)Added [-[NWTCPConnectionAuthenticationDelegate evaluateTrustForConnection:peerCertificateChain:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406024-evaluatetrust)Added [-[NWTCPConnectionAuthenticationDelegate provideIdentityForConnection:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406235-provideidentity)Added [-[NWTCPConnectionAuthenticationDelegate shouldEvaluateTrustForConnection:]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406116-shouldevaluatetrustforconnection)Added [-[NWTCPConnectionAuthenticationDelegate shouldProvideIdentityForConnection:]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406689-shouldprovideidentity)Added [NWTCPConnectionState](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate)Added [NWTCPConnectionStateCancelled](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstatecancelled)Added [NWTCPConnectionStateConnected](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/connected)Added [NWTCPConnectionStateConnecting](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstateconnecting)Added [NWTCPConnectionStateDisconnected](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/disconnected)Added [NWTCPConnectionStateInvalid](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/invalid)Added [NWTCPConnectionStateWaiting](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/waiting)

#### NWTLSParameters.h (Added)

Added [NWTLSParameters](https://developer.apple.com/documentation/networkextension/nwtlsparameters)Added [NWTLSParameters.maximumSSLProtocolVersion](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406010-maximumsslprotocolversion)Added [NWTLSParameters.minimumSSLProtocolVersion](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406571-minimumsslprotocolversion)Added [NWTLSParameters.SSLCipherSuites](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406533-sslciphersuites)Added [NWTLSParameters.TLSSessionID](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406569-tlssessionid)

#### NWUDPSession.h (Added)

Added [NWUDPSession](https://developer.apple.com/documentation/networkextension/nwudpsession)Added [-[NWUDPSession cancel]](https://developer.apple.com/documentation/networkextension/nwudpsession/1406629-cancel)Added [NWUDPSession.currentPath](https://developer.apple.com/documentation/networkextension/nwudpsession/1406296-currentpath)Added [NWUDPSession.endpoint](https://developer.apple.com/documentation/networkextension/nwudpsession/1406388-endpoint)Added [NWUDPSession.hasBetterPath](https://developer.apple.com/documentation/networkextension/nwudpsession/1406231-hasbetterpath)Added [-[NWUDPSession initWithUpgradeForSession:]](https://developer.apple.com/documentation/networkextension/nwudpsession/1406905-initwithupgradeforsession)Added [NWUDPSession.maximumDatagramLength](https://developer.apple.com/documentation/networkextension/nwudpsession/1406419-maximumdatagramlength)Added [NWUDPSession.resolvedEndpoint](https://developer.apple.com/documentation/networkextension/nwudpsession/1406190-resolvedendpoint)Added [-[NWUDPSession setReadHandler:maxDatagrams:]](https://developer.apple.com/documentation/networkextension/nwudpsession/1406772-setreadhandler)Added [NWUDPSession.state](https://developer.apple.com/documentation/networkextension/nwudpsession/1406901-state)Added [-[NWUDPSession tryNextResolvedEndpoint]](https://developer.apple.com/documentation/networkextension/nwudpsession/1406223-trynextresolvedendpoint)Added [NWUDPSession.viable](https://developer.apple.com/documentation/networkextension/nwudpsession/1406357-isviable)Added [-[NWUDPSession writeDatagram:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwudpsession/1406079-writedatagram)Added [-[NWUDPSession writeMultipleDatagrams:completionHandler:]](https://developer.apple.com/documentation/networkextension/nwudpsession/1406390-writemultipledatagrams)Added [NWUDPSessionState](https://developer.apple.com/documentation/networkextension/nwudpsessionstate)Added [NWUDPSessionStateCancelled](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstatecancelled)Added [NWUDPSessionStateFailed](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstatefailed)Added [NWUDPSessionStateInvalid](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstateinvalid)Added [NWUDPSessionStatePreparing](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/preparing)Added [NWUDPSessionStateReady](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstateready)Added [NWUDPSessionStateWaiting](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/waiting)

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
