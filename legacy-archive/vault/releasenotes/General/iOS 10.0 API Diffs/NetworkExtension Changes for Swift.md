---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/NetworkExtension.html
archived_at: '2026-07-18T02:55:34.056673Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# NetworkExtension Changes for Swift

### NetworkExtension

Removed NEVPNIKEv2DiffieHellmanGroup.Group0Added [NEPacket](https://developer.apple.com/documentation/networkextension/nepacket)Added [NEPacket.data](https://developer.apple.com/documentation/networkextension/nepacket/2118333-data)Added [NEPacket.init(data: Data, protocolFamily: sa_family_t)](https://developer.apple.com/documentation/networkextension/nepacket/2118334-init)Added [NEPacket.metadata](https://developer.apple.com/documentation/networkextension/nepacket/2118332-metadata)Added [NEPacket.protocolFamily](https://developer.apple.com/documentation/networkextension/nepacket/2118335-protocolfamily)Added [NEPacketTunnelFlow.readPacketObjects(completionHandler: ([NEPacket]) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/2118343-readpacketobjectswithcompletionh)Added [NEPacketTunnelFlow.writePacketObjects(_: [NEPacket]) -> Bool](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/2118344-writepacketobjects)Added [NEProvider.displayMessage(_: String, completionHandler: (Bool) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neprovider/1690502-displaymessage)Added [NEVPNConnection.manager](https://developer.apple.com/documentation/networkextension/nevpnconnection/1639571-manager)Added [NEVPNIKEv2DiffieHellmanGroup.groupInvalid](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/groupinvalid)Modified [NEAppProxyErrorDomain [enum]](https://developer.apple.com/documentation/networkextension/neappproxyflowerror)

|  | Declaration |
| --- | --- |
| From | ``` enum NEAppProxyFlowError : Int {     case NotConnected     case PeerReset     case HostUnreachable     case InvalidArgument     case Aborted     case Refused     case TimedOut     case Internal     case DatagramTooLarge     case ReadAlreadyPending } ``` |
| To | ``` enum NEAppProxyErrorDomain : Int {     case notConnected     case peerReset     case hostUnreachable     case invalidArgument     case aborted     case refused     case timedOut     case `internal`     case datagramTooLarge     case readAlreadyPending } ``` |

Modified [NEAppProxyErrorDomain.aborted](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/aborted)

|  | Declaration |
| --- | --- |
| From | ``` case Aborted ``` |
| To | ``` case aborted ``` |

Modified [NEAppProxyErrorDomain.datagramTooLarge](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/datagramtoolarge)

|  | Declaration |
| --- | --- |
| From | ``` case DatagramTooLarge ``` |
| To | ``` case datagramTooLarge ``` |

Modified [NEAppProxyErrorDomain.hostUnreachable](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/hostunreachable)

|  | Declaration |
| --- | --- |
| From | ``` case HostUnreachable ``` |
| To | ``` case hostUnreachable ``` |

Modified [NEAppProxyErrorDomain.internal](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/internal)

|  | Declaration |
| --- | --- |
| From | ``` case Internal ``` |
| To | ``` case `internal` ``` |

Modified [NEAppProxyErrorDomain.invalidArgument](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrorinvalidargument)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidArgument ``` |
| To | ``` case invalidArgument ``` |

Modified [NEAppProxyErrorDomain.notConnected](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/notconnected)

|  | Declaration |
| --- | --- |
| From | ``` case NotConnected ``` |
| To | ``` case notConnected ``` |

Modified [NEAppProxyErrorDomain.peerReset](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrorpeerreset)

|  | Declaration |
| --- | --- |
| From | ``` case PeerReset ``` |
| To | ``` case peerReset ``` |

Modified [NEAppProxyErrorDomain.readAlreadyPending](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/readalreadypending)

|  | Declaration |
| --- | --- |
| From | ``` case ReadAlreadyPending ``` |
| To | ``` case readAlreadyPending ``` |

Modified [NEAppProxyErrorDomain.refused](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/code/refused)

|  | Declaration |
| --- | --- |
| From | ``` case Refused ``` |
| To | ``` case refused ``` |

Modified [NEAppProxyErrorDomain.timedOut](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/neappproxyflowerrortimedout)

|  | Declaration |
| --- | --- |
| From | ``` case TimedOut ``` |
| To | ``` case timedOut ``` |

Modified [NEAppProxyFlow](https://developer.apple.com/documentation/networkextension/neappproxyflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEAppProxyFlow : NSObject {     func openWithLocalEndpoint(_ localEndpoint: NWHostEndpoint?, completionHandler completionHandler: (NSError?) -> Void)     func closeReadWithError(_ error: NSError?)     func closeWriteWithError(_ error: NSError?)     var metaData: NEFlowMetaData { get } } ``` | -- |
| To | ``` class NEAppProxyFlow : NSObject {     func open(withLocalEndpoint localEndpoint: NWHostEndpoint?, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func closeReadWithError(_ error: Error?)     func closeWriteWithError(_ error: Error?)     var metaData: NEFlowMetaData { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEAppProxyFlow : CVarArg { } extension NEAppProxyFlow : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEAppProxyFlow.closeReadWithError(_: Error?)](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406561-closereadwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func closeReadWithError(_ error: NSError?) ``` |
| To | ``` func closeReadWithError(_ error: Error?) ``` |

Modified [NEAppProxyFlow.closeWriteWithError(_: Error?)](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406664-closewritewitherror)

|  | Declaration |
| --- | --- |
| From | ``` func closeWriteWithError(_ error: NSError?) ``` |
| To | ``` func closeWriteWithError(_ error: Error?) ``` |

Modified [NEAppProxyFlow.open(withLocalEndpoint: NWHostEndpoint?, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxyflow/1406476-openwithlocalendpoint)

|  | Declaration |
| --- | --- |
| From | ``` func openWithLocalEndpoint(_ localEndpoint: NWHostEndpoint?, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func open(withLocalEndpoint localEndpoint: NWHostEndpoint?, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEAppProxyProvider](https://developer.apple.com/documentation/networkextension/neappproxyprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NEAppProxyProvider : NETunnelProvider {     func startProxyWithOptions(_ options: [String : AnyObject]?, completionHandler completionHandler: (NSError?) -> Void)     func stopProxyWithReason(_ reason: NEProviderStopReason, completionHandler completionHandler: () -> Void)     func cancelProxyWithError(_ error: NSError?)     func handleNewFlow(_ flow: NEAppProxyFlow) -> Bool } ``` |
| To | ``` class NEAppProxyProvider : NETunnelProvider {     func startProxy(options options: [String : Any]? = nil, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func stopProxy(with reason: NEProviderStopReason, completionHandler completionHandler: @escaping () -> Swift.Void)     func cancelProxyWithError(_ error: Error?)     func handleNewFlow(_ flow: NEAppProxyFlow) -> Bool } ``` |

Modified [NEAppProxyProvider.cancelProxyWithError(_: Error?)](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405081-cancelproxywitherror)

|  | Declaration |
| --- | --- |
| From | ``` func cancelProxyWithError(_ error: NSError?) ``` |
| To | ``` func cancelProxyWithError(_ error: Error?) ``` |

Modified [NEAppProxyProvider.startProxy(options: [String : Any]?, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405083-startproxy)

|  | Declaration |
| --- | --- |
| From | ``` func startProxyWithOptions(_ options: [String : AnyObject]?, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func startProxy(options options: [String : Any]? = nil, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEAppProxyProvider.stopProxy(with: NEProviderStopReason, completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxyprovider/1405077-stopproxywithreason)

|  | Declaration |
| --- | --- |
| From | ``` func stopProxyWithReason(_ reason: NEProviderStopReason, completionHandler completionHandler: () -> Void) ``` |
| To | ``` func stopProxy(with reason: NEProviderStopReason, completionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [NEAppProxyProviderManager](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager)

|  | Declaration |
| --- | --- |
| From | ``` class NEAppProxyProviderManager : NETunnelProviderManager {     class func loadAllFromPreferencesWithCompletionHandler(_ completionHandler: ([NEAppProxyProviderManager]?, NSError?) -> Void) } ``` |
| To | ``` class NEAppProxyProviderManager : NETunnelProviderManager {     class func loadAllFromPreferences(completionHandler completionHandler: @escaping ([NEAppProxyProviderManager]?, Error?) -> Swift.Void) } ``` |

Modified [NEAppProxyProviderManager.loadAllFromPreferences(completionHandler: ([NEAppProxyProviderManager]?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager/1406790-loadallfrompreferenceswithcomple)

|  | Declaration |
| --- | --- |
| From | ``` class func loadAllFromPreferencesWithCompletionHandler(_ completionHandler: ([NEAppProxyProviderManager]?, NSError?) -> Void) ``` |
| To | ``` class func loadAllFromPreferences(completionHandler completionHandler: @escaping ([NEAppProxyProviderManager]?, Error?) -> Swift.Void) ``` |

Modified [NEAppProxyTCPFlow](https://developer.apple.com/documentation/networkextension/neappproxytcpflow)

|  | Declaration |
| --- | --- |
| From | ``` class NEAppProxyTCPFlow : NEAppProxyFlow {     func readDataWithCompletionHandler(_ completionHandler: (NSData?, NSError?) -> Void)     func writeData(_ data: NSData, withCompletionHandler completionHandler: (NSError?) -> Void)     var remoteEndpoint: NWEndpoint { get } } ``` |
| To | ``` class NEAppProxyTCPFlow : NEAppProxyFlow {     func readData(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void)     func write(_ data: Data, withCompletionHandler completionHandler: @escaping (Error?) -> Swift.Void)     var remoteEndpoint: NWEndpoint { get } } ``` |

Modified [NEAppProxyTCPFlow.readData(completionHandler: (Data?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406311-readdatawithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func readDataWithCompletionHandler(_ completionHandler: (NSData?, NSError?) -> Void) ``` |
| To | ``` func readData(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void) ``` |

Modified [NEAppProxyTCPFlow.write(_: Data, withCompletionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/1406776-write)

|  | Declaration |
| --- | --- |
| From | ``` func writeData(_ data: NSData, withCompletionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func write(_ data: Data, withCompletionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEAppProxyUDPFlow](https://developer.apple.com/documentation/networkextension/neappproxyudpflow)

|  | Declaration |
| --- | --- |
| From | ``` class NEAppProxyUDPFlow : NEAppProxyFlow {     func readDatagramsWithCompletionHandler(_ completionHandler: ([NSData]?, [NWEndpoint]?, NSError?) -> Void)     func writeDatagrams(_ datagrams: [NSData], sentByEndpoints remoteEndpoints: [NWEndpoint], completionHandler completionHandler: (NSError?) -> Void)     var localEndpoint: NWEndpoint? { get } } ``` |
| To | ``` class NEAppProxyUDPFlow : NEAppProxyFlow {     func readDatagrams(completionHandler completionHandler: @escaping ([Data]?, [NWEndpoint]?, Error?) -> Swift.Void)     func writeDatagrams(_ datagrams: [Data], sentBy remoteEndpoints: [NWEndpoint], completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     var localEndpoint: NWEndpoint? { get } } ``` |

Modified [NEAppProxyUDPFlow.readDatagrams(completionHandler: ([Data]?, [NWEndpoint]?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406576-readdatagramswithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func readDatagramsWithCompletionHandler(_ completionHandler: ([NSData]?, [NWEndpoint]?, NSError?) -> Void) ``` |
| To | ``` func readDatagrams(completionHandler completionHandler: @escaping ([Data]?, [NWEndpoint]?, Error?) -> Swift.Void) ``` |

Modified [NEAppProxyUDPFlow.writeDatagrams(_: [Data], sentBy: [NWEndpoint], completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/1406784-writedatagrams)

|  | Declaration |
| --- | --- |
| From | ``` func writeDatagrams(_ datagrams: [NSData], sentByEndpoints remoteEndpoints: [NWEndpoint], completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func writeDatagrams(_ datagrams: [Data], sentBy remoteEndpoints: [NWEndpoint], completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEAppRule](https://developer.apple.com/documentation/networkextension/neapprule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEAppRule : NSObject, NSSecureCoding, NSCopying {     init(signingIdentifier signingIdentifier: String)     init(signingIdentifier signingIdentifier: String, designatedRequirement designatedRequirement: String)     var matchSigningIdentifier: String { get }     var matchDesignatedRequirement: String { get }     var matchPath: String?     var matchDomains: [AnyObject]? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEAppRule : NSObject, NSSecureCoding, NSCopying {     init(signingIdentifier signingIdentifier: String)     init(signingIdentifier signingIdentifier: String, designatedRequirement designatedRequirement: String)     var matchSigningIdentifier: String { get }     var matchDesignatedRequirement: String { get }     var matchPath: String?     var matchDomains: [Any]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEAppRule : CVarArg { } extension NEAppRule : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEAppRule.matchDomains](https://developer.apple.com/documentation/networkextension/neapprule/1406488-matchdomains)

|  | Declaration |
| --- | --- |
| From | ``` var matchDomains: [AnyObject]? ``` |
| To | ``` var matchDomains: [Any]? ``` |

Modified [NEDNSSettings](https://developer.apple.com/documentation/networkextension/nednssettings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEDNSSettings : NSObject, NSSecureCoding, NSCopying {     init(servers servers: [String])     var servers: [String] { get }     var searchDomains: [String]?     var domainName: String?     var matchDomains: [String]?     var matchDomainsNoSearch: Bool } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEDNSSettings : NSObject, NSSecureCoding, NSCopying {     init(servers servers: [String])     var servers: [String] { get }     var searchDomains: [String]?     var domainName: String?     var matchDomains: [String]?     var matchDomainsNoSearch: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEDNSSettings : CVarArg { } extension NEDNSSettings : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEEvaluateConnectionRule](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEEvaluateConnectionRule : NSObject, NSSecureCoding, NSCopying {     init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction)     var action: NEEvaluateConnectionRuleAction { get }     var matchDomains: [String] { get }     var useDNSServers: [String]?     @NSCopying var probeURL: NSURL? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEEvaluateConnectionRule : NSObject, NSSecureCoding, NSCopying {     init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction)     var action: NEEvaluateConnectionRuleAction { get }     var matchDomains: [String] { get }     var useDNSServers: [String]?     var probeURL: URL?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEEvaluateConnectionRule : CVarArg { } extension NEEvaluateConnectionRule : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEEvaluateConnectionRule.probeURL](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/1406082-probeurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var probeURL: NSURL? ``` |
| To | ``` var probeURL: URL? ``` |

Modified [NEEvaluateConnectionRuleAction [enum]](https://developer.apple.com/documentation/networkextension/neevaluateconnectionruleaction)

|  | Declaration |
| --- | --- |
| From | ``` enum NEEvaluateConnectionRuleAction : Int {     case ConnectIfNeeded     case NeverConnect } ``` |
| To | ``` enum NEEvaluateConnectionRuleAction : Int {     case connectIfNeeded     case neverConnect } ``` |

Modified [NEEvaluateConnectionRuleAction.connectIfNeeded](https://developer.apple.com/documentation/networkextension/neevaluateconnectionruleaction/neevaluateconnectionruleactionconnectifneeded)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectIfNeeded ``` |
| To | ``` case connectIfNeeded ``` |

Modified [NEEvaluateConnectionRuleAction.neverConnect](https://developer.apple.com/documentation/networkextension/neevaluateconnectionruleaction/neevaluateconnectionruleactionneverconnect)

|  | Declaration |
| --- | --- |
| From | ``` case NeverConnect ``` |
| To | ``` case neverConnect ``` |

Modified [NEFilterBrowserFlow](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterBrowserFlow : NEFilterFlow, NSSecureCoding, NSCopying {     var request: NSURLRequest { get }     var response: NSURLResponse? { get }     var parentURL: NSURL? { get } } ``` |
| To | ``` class NEFilterBrowserFlow : NEFilterFlow, NSSecureCoding, NSCopying {     var request: URLRequest { get }     var response: URLResponse? { get }     var parentURL: URL? { get } } ``` |

Modified [NEFilterBrowserFlow.parentURL](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618932-parenturl)

|  | Declaration |
| --- | --- |
| From | ``` var parentURL: NSURL? { get } ``` |
| To | ``` var parentURL: URL? { get } ``` |

Modified [NEFilterBrowserFlow.request](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618948-request)

|  | Declaration |
| --- | --- |
| From | ``` var request: NSURLRequest { get } ``` |
| To | ``` var request: URLRequest { get } ``` |

Modified [NEFilterBrowserFlow.response](https://developer.apple.com/documentation/networkextension/nefilterbrowserflow/1618966-response)

|  | Declaration |
| --- | --- |
| From | ``` var response: NSURLResponse? { get } ``` |
| To | ``` var response: URLResponse? { get } ``` |

Modified [NEFilterControlProvider](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterControlProvider : NEFilterProvider {     var remediationMap: [String : [String : NSObject]]?     var URLAppendStringMap: [String : String]?     func handleRemediationForFlow(_ flow: NEFilterFlow, completionHandler completionHandler: (NEFilterControlVerdict) -> Void)     func handleNewFlow(_ flow: NEFilterFlow, completionHandler completionHandler: (NEFilterControlVerdict) -> Void)     func notifyRulesChanged() } ``` |
| To | ``` class NEFilterControlProvider : NEFilterProvider {     var remediationMap: [String : [String : NSObject]]?     var urlAppendStringMap: [String : String]?     func handleRemediation(for flow: NEFilterFlow, completionHandler completionHandler: @escaping (NEFilterControlVerdict) -> Swift.Void)     func handleNewFlow(_ flow: NEFilterFlow, completionHandler completionHandler: @escaping (NEFilterControlVerdict) -> Swift.Void)     func notifyRulesChanged() } ``` |

Modified [NEFilterControlProvider.handleNewFlow(_: NEFilterFlow, completionHandler: (NEFilterControlVerdict) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614120-handlenewflow)

|  | Declaration |
| --- | --- |
| From | ``` func handleNewFlow(_ flow: NEFilterFlow, completionHandler completionHandler: (NEFilterControlVerdict) -> Void) ``` |
| To | ``` func handleNewFlow(_ flow: NEFilterFlow, completionHandler completionHandler: @escaping (NEFilterControlVerdict) -> Swift.Void) ``` |

Modified [NEFilterControlProvider.handleRemediation(for: NEFilterFlow, completionHandler: (NEFilterControlVerdict) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614122-handleremediationforflow)

|  | Declaration |
| --- | --- |
| From | ``` func handleRemediationForFlow(_ flow: NEFilterFlow, completionHandler completionHandler: (NEFilterControlVerdict) -> Void) ``` |
| To | ``` func handleRemediation(for flow: NEFilterFlow, completionHandler completionHandler: @escaping (NEFilterControlVerdict) -> Swift.Void) ``` |

Modified [NEFilterControlProvider.urlAppendStringMap](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/1614123-urlappendstringmap)

|  | Declaration |
| --- | --- |
| From | ``` var URLAppendStringMap: [String : String]? ``` |
| To | ``` var urlAppendStringMap: [String : String]? ``` |

Modified [NEFilterControlVerdict](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterControlVerdict : NEFilterNewFlowVerdict, NSSecureCoding, NSCopying {     class func allowVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict     class func dropVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict     class func updateRules() -> NEFilterControlVerdict } ``` |
| To | ``` class NEFilterControlVerdict : NEFilterNewFlowVerdict, NSSecureCoding, NSCopying {     class func allow(withUpdateRules updateRules: Bool) -> NEFilterControlVerdict     class func drop(withUpdateRules updateRules: Bool) -> NEFilterControlVerdict     class func updateRules() -> NEFilterControlVerdict } ``` |

Modified [NEFilterControlVerdict.allow(withUpdateRules: Bool) -> NEFilterControlVerdict [class]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617040-allow)

|  | Declaration |
| --- | --- |
| From | ``` class func allowVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict ``` |
| To | ``` class func allow(withUpdateRules updateRules: Bool) -> NEFilterControlVerdict ``` |

Modified [NEFilterControlVerdict.drop(withUpdateRules: Bool) -> NEFilterControlVerdict [class]](https://developer.apple.com/documentation/networkextension/nefiltercontrolverdict/1617044-dropverdictwithupdaterules)

|  | Declaration |
| --- | --- |
| From | ``` class func dropVerdictWithUpdateRules(_ updateRules: Bool) -> NEFilterControlVerdict ``` |
| To | ``` class func drop(withUpdateRules updateRules: Bool) -> NEFilterControlVerdict ``` |

Modified [NEFilterDataProvider](https://developer.apple.com/documentation/networkextension/nefilterdataprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterDataProvider : NEFilterProvider {     func handleNewFlow(_ flow: NEFilterFlow) -> NEFilterNewFlowVerdict     func handleInboundDataFromFlow(_ flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: NSData) -> NEFilterDataVerdict     func handleOutboundDataFromFlow(_ flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: NSData) -> NEFilterDataVerdict     func handleInboundDataCompleteForFlow(_ flow: NEFilterFlow) -> NEFilterDataVerdict     func handleOutboundDataCompleteForFlow(_ flow: NEFilterFlow) -> NEFilterDataVerdict     func handleRemediationForFlow(_ flow: NEFilterFlow) -> NEFilterRemediationVerdict     func handleRulesChanged() } ``` |
| To | ``` class NEFilterDataProvider : NEFilterProvider {     func handleNewFlow(_ flow: NEFilterFlow) -> NEFilterNewFlowVerdict     func handleInboundData(from flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: Data) -> NEFilterDataVerdict     func handleOutboundData(from flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: Data) -> NEFilterDataVerdict     func handleInboundDataComplete(for flow: NEFilterFlow) -> NEFilterDataVerdict     func handleOutboundDataComplete(for flow: NEFilterFlow) -> NEFilterDataVerdict     func handleRemediation(for flow: NEFilterFlow) -> NEFilterRemediationVerdict     func handleRulesChanged() } ``` |

Modified [NEFilterDataProvider.handleInboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618933-handleinbounddatafromflow)

|  | Declaration |
| --- | --- |
| From | ``` func handleInboundDataFromFlow(_ flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: NSData) -> NEFilterDataVerdict ``` |
| To | ``` func handleInboundData(from flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: Data) -> NEFilterDataVerdict ``` |

Modified [NEFilterDataProvider.handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618977-handleinbounddatacomplete)

|  | Declaration |
| --- | --- |
| From | ``` func handleInboundDataCompleteForFlow(_ flow: NEFilterFlow) -> NEFilterDataVerdict ``` |
| To | ``` func handleInboundDataComplete(for flow: NEFilterFlow) -> NEFilterDataVerdict ``` |

Modified [NEFilterDataProvider.handleOutboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618954-handleoutbounddata)

|  | Declaration |
| --- | --- |
| From | ``` func handleOutboundDataFromFlow(_ flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: NSData) -> NEFilterDataVerdict ``` |
| To | ``` func handleOutboundData(from flow: NEFilterFlow, readBytesStartOffset offset: Int, readBytes readBytes: Data) -> NEFilterDataVerdict ``` |

Modified [NEFilterDataProvider.handleOutboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618961-handleoutbounddatacompleteforflo)

|  | Declaration |
| --- | --- |
| From | ``` func handleOutboundDataCompleteForFlow(_ flow: NEFilterFlow) -> NEFilterDataVerdict ``` |
| To | ``` func handleOutboundDataComplete(for flow: NEFilterFlow) -> NEFilterDataVerdict ``` |

Modified [NEFilterDataProvider.handleRemediation(for: NEFilterFlow) -> NEFilterRemediationVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/1618928-handleremediationforflow)

|  | Declaration |
| --- | --- |
| From | ``` func handleRemediationForFlow(_ flow: NEFilterFlow) -> NEFilterRemediationVerdict ``` |
| To | ``` func handleRemediation(for flow: NEFilterFlow) -> NEFilterRemediationVerdict ``` |

Modified [NEFilterDataVerdict](https://developer.apple.com/documentation/networkextension/nefilterdataverdict)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterDataVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func allowVerdict() -> NEFilterDataVerdict     class func dropVerdict() -> NEFilterDataVerdict     class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String?, remediationButtonTextMapKey remediationButtonTextMapKey: String?) -> NEFilterDataVerdict      init(passBytes passBytes: Int, peekBytes peekBytes: Int)     class func dataVerdictWithPassBytes(_ passBytes: Int, peekBytes peekBytes: Int) -> NEFilterDataVerdict     class func needRulesVerdict() -> NEFilterDataVerdict } ``` |
| To | ``` class NEFilterDataVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func allow() -> NEFilterDataVerdict     class func drop() -> NEFilterDataVerdict     class func remediateVerdict(withRemediationURLMapKey remediationURLMapKey: String?, remediationButtonTextMapKey remediationButtonTextMapKey: String?) -> NEFilterDataVerdict      init(passBytes passBytes: Int, peekBytes peekBytes: Int)     class func withPassBytes(_ passBytes: Int, peekBytes peekBytes: Int) -> NEFilterDataVerdict     class func needRules() -> NEFilterDataVerdict } ``` |

Modified [NEFilterDataVerdict.allow() -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1619010-allowverdict)

|  | Declaration |
| --- | --- |
| From | ``` class func allowVerdict() -> NEFilterDataVerdict ``` |
| To | ``` class func allow() -> NEFilterDataVerdict ``` |

Modified [NEFilterDataVerdict.drop() -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618952-dropverdict)

|  | Declaration |
| --- | --- |
| From | ``` class func dropVerdict() -> NEFilterDataVerdict ``` |
| To | ``` class func drop() -> NEFilterDataVerdict ``` |

Modified [NEFilterDataVerdict.needRules() -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618993-needrulesverdict)

|  | Declaration |
| --- | --- |
| From | ``` class func needRulesVerdict() -> NEFilterDataVerdict ``` |
| To | ``` class func needRules() -> NEFilterDataVerdict ``` |

Modified [NEFilterDataVerdict.remediateVerdict(withRemediationURLMapKey: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/1618964-remediateverdictwithremediationu)

|  | Declaration |
| --- | --- |
| From | ``` class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String?, remediationButtonTextMapKey remediationButtonTextMapKey: String?) -> NEFilterDataVerdict ``` |
| To | ``` class func remediateVerdict(withRemediationURLMapKey remediationURLMapKey: String?, remediationButtonTextMapKey remediationButtonTextMapKey: String?) -> NEFilterDataVerdict ``` |

Modified [NEFilterFlow](https://developer.apple.com/documentation/networkextension/nefilterflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterFlow : NSObject, NSSecureCoding, NSCopying {     var URL: NSURL? { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEFilterFlow : NSObject, NSSecureCoding, NSCopying {     var url: URL? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEFilterFlow : CVarArg { } extension NEFilterFlow : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEFilterFlow.url](https://developer.apple.com/documentation/networkextension/nefilterflow/1618935-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified [NEFilterManager](https://developer.apple.com/documentation/networkextension/nefiltermanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterManager : NSObject {     class func sharedManager() -> NEFilterManager     func loadFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     func removeFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     func saveToPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     var localizedDescription: String?     var providerConfiguration: NEFilterProviderConfiguration?     var enabled: Bool } ``` | -- |
| To | ``` class NEFilterManager : NSObject {     class func shared() -> NEFilterManager     func loadFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func removeFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func saveToPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     var localizedDescription: String?     var providerConfiguration: NEFilterProviderConfiguration?     var isEnabled: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEFilterManager : CVarArg { } extension NEFilterManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEFilterManager.isEnabled](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406158-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [NEFilterManager.loadFromPreferences(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406359-loadfrompreferences)

|  | Declaration |
| --- | --- |
| From | ``` func loadFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |
| To | ``` func loadFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEFilterManager.removeFromPreferences(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406876-removefrompreferenceswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |
| To | ``` func removeFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEFilterManager.saveToPreferences(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406339-savetopreferences)

|  | Declaration |
| --- | --- |
| From | ``` func saveToPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |
| To | ``` func saveToPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEFilterManager.shared() -> NEFilterManager [class]](https://developer.apple.com/documentation/networkextension/nefiltermanager/1406438-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedManager() -> NEFilterManager ``` |
| To | ``` class func shared() -> NEFilterManager ``` |

Modified [NEFilterManagerError [enum]](https://developer.apple.com/documentation/networkextension/nefiltermanagererror)

|  | Declaration |
| --- | --- |
| From | ``` enum NEFilterManagerError : Int {     case ConfigurationInvalid     case ConfigurationDisabled     case ConfigurationStale     case ConfigurationCannotBeRemoved } ``` |
| To | ``` enum NEFilterManagerError : Int {     case configurationInvalid     case configurationDisabled     case configurationStale     case configurationCannotBeRemoved } ``` |

Modified [NEFilterManagerError.configurationCannotBeRemoved](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/nefiltermanagererrorconfigurationcannotberemoved)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationCannotBeRemoved ``` |
| To | ``` case configurationCannotBeRemoved ``` |

Modified [NEFilterManagerError.configurationDisabled](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationdisabled)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationDisabled ``` |
| To | ``` case configurationDisabled ``` |

Modified [NEFilterManagerError.configurationInvalid](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationInvalid ``` |
| To | ``` case configurationInvalid ``` |

Modified [NEFilterManagerError.configurationStale](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationstale)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationStale ``` |
| To | ``` case configurationStale ``` |

Modified [NEFilterNewFlowVerdict](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterNewFlowVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func needRulesVerdict() -> NEFilterNewFlowVerdict     class func allowVerdict() -> NEFilterNewFlowVerdict     class func dropVerdict() -> NEFilterNewFlowVerdict     class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String, remediationButtonTextMapKey remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict     class func URLAppendStringVerdictWithMapKey(_ urlAppendMapKey: String) -> NEFilterNewFlowVerdict     class func filterDataVerdictWithFilterInbound(_ filterInbound: Bool, peekInboundBytes peekInboundBytes: Int, filterOutbound filterOutbound: Bool, peekOutboundBytes peekOutboundBytes: Int) -> NEFilterNewFlowVerdict } ``` |
| To | ``` class NEFilterNewFlowVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func needRules() -> NEFilterNewFlowVerdict     class func allow() -> NEFilterNewFlowVerdict     class func drop() -> NEFilterNewFlowVerdict     class func remediateVerdict(withRemediationURLMapKey remediationURLMapKey: String, remediationButtonTextMapKey remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict     class func urlAppendStringVerdict(withMapKey urlAppendMapKey: String) -> NEFilterNewFlowVerdict     class func filterDataVerdict(withFilterInbound filterInbound: Bool, peekInboundBytes peekInboundBytes: Int, filterOutbound filterOutbound: Bool, peekOutboundBytes peekOutboundBytes: Int) -> NEFilterNewFlowVerdict } ``` |

Modified [NEFilterNewFlowVerdict.allow() -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617036-allow)

|  | Declaration |
| --- | --- |
| From | ``` class func allowVerdict() -> NEFilterNewFlowVerdict ``` |
| To | ``` class func allow() -> NEFilterNewFlowVerdict ``` |

Modified [NEFilterNewFlowVerdict.drop() -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617035-dropverdict)

|  | Declaration |
| --- | --- |
| From | ``` class func dropVerdict() -> NEFilterNewFlowVerdict ``` |
| To | ``` class func drop() -> NEFilterNewFlowVerdict ``` |

Modified [NEFilterNewFlowVerdict.filterDataVerdict(withFilterInbound: Bool, peekInboundBytes: Int, filterOutbound: Bool, peekOutboundBytes: Int) -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617038-filterdataverdictwithfilterinbou)

|  | Declaration |
| --- | --- |
| From | ``` class func filterDataVerdictWithFilterInbound(_ filterInbound: Bool, peekInboundBytes peekInboundBytes: Int, filterOutbound filterOutbound: Bool, peekOutboundBytes peekOutboundBytes: Int) -> NEFilterNewFlowVerdict ``` |
| To | ``` class func filterDataVerdict(withFilterInbound filterInbound: Bool, peekInboundBytes peekInboundBytes: Int, filterOutbound filterOutbound: Bool, peekOutboundBytes peekOutboundBytes: Int) -> NEFilterNewFlowVerdict ``` |

Modified [NEFilterNewFlowVerdict.needRules() -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617034-needrules)

|  | Declaration |
| --- | --- |
| From | ``` class func needRulesVerdict() -> NEFilterNewFlowVerdict ``` |
| To | ``` class func needRules() -> NEFilterNewFlowVerdict ``` |

Modified [NEFilterNewFlowVerdict.remediateVerdict(withRemediationURLMapKey: String, remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617042-remediateverdictwithremediationu)

|  | Declaration |
| --- | --- |
| From | ``` class func remediateVerdictWithRemediationURLMapKey(_ remediationURLMapKey: String, remediationButtonTextMapKey remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict ``` |
| To | ``` class func remediateVerdict(withRemediationURLMapKey remediationURLMapKey: String, remediationButtonTextMapKey remediationButtonTextMapKey: String) -> NEFilterNewFlowVerdict ``` |

Modified [NEFilterNewFlowVerdict.urlAppendStringVerdict(withMapKey: String) -> NEFilterNewFlowVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilternewflowverdict/1617046-urlappendstringverdictwithmapkey)

|  | Declaration |
| --- | --- |
| From | ``` class func URLAppendStringVerdictWithMapKey(_ urlAppendMapKey: String) -> NEFilterNewFlowVerdict ``` |
| To | ``` class func urlAppendStringVerdict(withMapKey urlAppendMapKey: String) -> NEFilterNewFlowVerdict ``` |

Modified [NEFilterProvider](https://developer.apple.com/documentation/networkextension/nefilterprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterProvider : NEProvider {     func startFilterWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     func stopFilterWithReason(_ reason: NEProviderStopReason, completionHandler completionHandler: () -> Void)     var filterConfiguration: NEFilterProviderConfiguration { get } } ``` |
| To | ``` class NEFilterProvider : NEProvider {     func startFilter(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func stopFilter(with reason: NEProviderStopReason, completionHandler completionHandler: @escaping () -> Swift.Void)     var filterConfiguration: NEFilterProviderConfiguration { get } } ``` |

Modified [NEFilterProvider.startFilter(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617043-startfilter)

|  | Declaration |
| --- | --- |
| From | ``` func startFilterWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |
| To | ``` func startFilter(completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEFilterProvider.stopFilter(with: NEProviderStopReason, completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nefilterprovider/1617032-stopfilter)

|  | Declaration |
| --- | --- |
| From | ``` func stopFilterWithReason(_ reason: NEProviderStopReason, completionHandler completionHandler: () -> Void) ``` |
| To | ``` func stopFilter(with reason: NEProviderStopReason, completionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [NEFilterProviderConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterProviderConfiguration : NSObject, NSSecureCoding, NSCopying {     var filterBrowsers: Bool     var filterSockets: Bool     var vendorConfiguration: [String : AnyObject]?     var serverAddress: String?     var username: String?     var organization: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEFilterProviderConfiguration : NSObject, NSSecureCoding, NSCopying {     var filterBrowsers: Bool     var filterSockets: Bool     var vendorConfiguration: [String : Any]?     var serverAddress: String?     var username: String?     var organization: String?     var passwordReference: Data?     var identityReference: Data?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEFilterProviderConfiguration : CVarArg { } extension NEFilterProviderConfiguration : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEFilterProviderConfiguration.identityReference](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406866-identityreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var identityReference: NSData? ``` |
| To | ``` var identityReference: Data? ``` |

Modified [NEFilterProviderConfiguration.passwordReference](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406146-passwordreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var passwordReference: NSData? ``` |
| To | ``` var passwordReference: Data? ``` |

Modified [NEFilterProviderConfiguration.vendorConfiguration](https://developer.apple.com/documentation/networkextension/nefilterproviderconfiguration/1406347-vendorconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` var vendorConfiguration: [String : AnyObject]? ``` |
| To | ``` var vendorConfiguration: [String : Any]? ``` |

Modified [NEFilterRemediationVerdict](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterRemediationVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func allowVerdict() -> NEFilterRemediationVerdict     class func dropVerdict() -> NEFilterRemediationVerdict     class func needRulesVerdict() -> NEFilterRemediationVerdict } ``` |
| To | ``` class NEFilterRemediationVerdict : NEFilterVerdict, NSSecureCoding, NSCopying {     class func allow() -> NEFilterRemediationVerdict     class func drop() -> NEFilterRemediationVerdict     class func needRules() -> NEFilterRemediationVerdict } ``` |

Modified [NEFilterRemediationVerdict.allow() -> NEFilterRemediationVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618962-allow)

|  | Declaration |
| --- | --- |
| From | ``` class func allowVerdict() -> NEFilterRemediationVerdict ``` |
| To | ``` class func allow() -> NEFilterRemediationVerdict ``` |

Modified [NEFilterRemediationVerdict.drop() -> NEFilterRemediationVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618947-dropverdict)

|  | Declaration |
| --- | --- |
| From | ``` class func dropVerdict() -> NEFilterRemediationVerdict ``` |
| To | ``` class func drop() -> NEFilterRemediationVerdict ``` |

Modified [NEFilterRemediationVerdict.needRules() -> NEFilterRemediationVerdict [class]](https://developer.apple.com/documentation/networkextension/nefilterremediationverdict/1618972-needrulesverdict)

|  | Declaration |
| --- | --- |
| From | ``` class func needRulesVerdict() -> NEFilterRemediationVerdict ``` |
| To | ``` class func needRules() -> NEFilterRemediationVerdict ``` |

Modified [NEFilterSocketFlow](https://developer.apple.com/documentation/networkextension/nefiltersocketflow)

|  | Declaration |
| --- | --- |
| From | ``` class NEFilterSocketFlow : NEFilterFlow, NSSecureCoding, NSCopying {     var remoteEndpoint: NWEndpoint { get }     var localEndpoint: NWEndpoint { get }     var socketFamily: Int32     var socketType: Int32     var socketProtocol: Int32 } ``` |
| To | ``` class NEFilterSocketFlow : NEFilterFlow, NSSecureCoding, NSCopying {     var remoteEndpoint: NWEndpoint? { get }     var localEndpoint: NWEndpoint? { get }     var socketFamily: Int32     var socketType: Int32     var socketProtocol: Int32 } ``` |

Modified [NEFilterSocketFlow.localEndpoint](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1619004-localendpoint)

|  | Declaration |
| --- | --- |
| From | ``` var localEndpoint: NWEndpoint { get } ``` |
| To | ``` var localEndpoint: NWEndpoint? { get } ``` |

Modified [NEFilterSocketFlow.remoteEndpoint](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/1618940-remoteendpoint)

|  | Declaration |
| --- | --- |
| From | ``` var remoteEndpoint: NWEndpoint { get } ``` |
| To | ``` var remoteEndpoint: NWEndpoint? { get } ``` |

Modified [NEFilterVerdict](https://developer.apple.com/documentation/networkextension/nefilterverdict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFilterVerdict : NSObject, NSSecureCoding, NSCopying { } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEFilterVerdict : NSObject, NSSecureCoding, NSCopying {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEFilterVerdict : CVarArg { } extension NEFilterVerdict : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEFlowMetaData](https://developer.apple.com/documentation/networkextension/neflowmetadata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEFlowMetaData : NSObject {     var sourceAppUniqueIdentifier: NSData { get }     var sourceAppSigningIdentifier: String { get } } ``` | -- |
| To | ``` class NEFlowMetaData : NSObject, NSCopying, NSSecureCoding {     var sourceAppUniqueIdentifier: Data { get }     var sourceAppSigningIdentifier: String { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEFlowMetaData : CVarArg { } extension NEFlowMetaData : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEFlowMetaData.sourceAppUniqueIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406448-sourceappuniqueidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var sourceAppUniqueIdentifier: NSData { get } ``` |
| To | ``` var sourceAppUniqueIdentifier: Data { get } ``` |

Modified [NEHotspotHelper](https://developer.apple.com/documentation/networkextension/nehotspothelper)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEHotspotHelper : NSObject {     class func registerWithOptions(_ options: [String : NSObject]?, queue queue: dispatch_queue_t, handler handler: NEHotspotHelperHandler) -> Bool     class func logoff(_ network: NEHotspotNetwork) -> Bool     class func supportedNetworkInterfaces() -> [AnyObject] } ``` | -- |
| To | ``` class NEHotspotHelper : NSObject {     class func register(options options: [String : NSObject]? = nil, queue queue: DispatchQueue, handler handler: NetworkExtension.NEHotspotHelperHandler) -> Bool     class func logoff(_ network: NEHotspotNetwork) -> Bool     class func supportedNetworkInterfaces() -> [Any]     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEHotspotHelper : CVarArg { } extension NEHotspotHelper : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEHotspotHelper.register(options: [String : NSObject]?, queue: DispatchQueue, handler: NetworkExtension.NEHotspotHelperHandler) -> Bool [class]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618965-registerwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` class func registerWithOptions(_ options: [String : NSObject]?, queue queue: dispatch_queue_t, handler handler: NEHotspotHelperHandler) -> Bool ``` |
| To | ``` class func register(options options: [String : NSObject]? = nil, queue queue: DispatchQueue, handler handler: NetworkExtension.NEHotspotHelperHandler) -> Bool ``` |

Modified [NEHotspotHelper.supportedNetworkInterfaces() -> [Any] [class]](https://developer.apple.com/documentation/networkextension/nehotspothelper/1618921-supportednetworkinterfaces)

|  | Declaration |
| --- | --- |
| From | ``` class func supportedNetworkInterfaces() -> [AnyObject] ``` |
| To | ``` class func supportedNetworkInterfaces() -> [Any] ``` |

Modified [NEHotspotHelperCommand](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEHotspotHelperCommand : NSObject {     var commandType: NEHotspotHelperCommandType { get }     var network: NEHotspotNetwork? { get }     var networkList: [NEHotspotNetwork]? { get }     func createResponse(_ result: NEHotspotHelperResult) -> NEHotspotHelperResponse     func createTCPConnection(_ endpoint: NWEndpoint) -> NWTCPConnection     func createUDPSession(_ endpoint: NWEndpoint) -> NWUDPSession } ``` | -- |
| To | ``` class NEHotspotHelperCommand : NSObject {     var commandType: NEHotspotHelperCommandType { get }     var network: NEHotspotNetwork? { get }     var networkList: [NEHotspotNetwork]? { get }     func createResponse(_ result: NEHotspotHelperResult) -> NEHotspotHelperResponse     func createTCPConnection(_ endpoint: NWEndpoint) -> NWTCPConnection     func createUDPSession(_ endpoint: NWEndpoint) -> NWUDPSession     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEHotspotHelperCommand : CVarArg { } extension NEHotspotHelperCommand : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEHotspotHelperCommandType [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype)

|  | Declaration |
| --- | --- |
| From | ``` enum NEHotspotHelperCommandType : Int {     case None     case FilterScanList     case Evaluate     case Authenticate     case PresentUI     case Maintain     case Logoff } ``` |
| To | ``` enum NEHotspotHelperCommandType : Int {     case none     case filterScanList     case evaluate     case authenticate     case presentUI     case maintain     case logoff } ``` |

Modified [NEHotspotHelperCommandType.authenticate](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypeauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` case Authenticate ``` |
| To | ``` case authenticate ``` |

Modified [NEHotspotHelperCommandType.evaluate](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypeevaluate)

|  | Declaration |
| --- | --- |
| From | ``` case Evaluate ``` |
| To | ``` case evaluate ``` |

Modified [NEHotspotHelperCommandType.filterScanList](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypefilterscanlist)

|  | Declaration |
| --- | --- |
| From | ``` case FilterScanList ``` |
| To | ``` case filterScanList ``` |

Modified [NEHotspotHelperCommandType.logoff](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/logoff)

|  | Declaration |
| --- | --- |
| From | ``` case Logoff ``` |
| To | ``` case logoff ``` |

Modified [NEHotspotHelperCommandType.maintain](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypemaintain)

|  | Declaration |
| --- | --- |
| From | ``` case Maintain ``` |
| To | ``` case maintain ``` |

Modified [NEHotspotHelperCommandType.none](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [NEHotspotHelperCommandType.presentUI](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype/knehotspothelpercommandtypepresentui)

|  | Declaration |
| --- | --- |
| From | ``` case PresentUI ``` |
| To | ``` case presentUI ``` |

Modified [NEHotspotHelperConfidence [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence)

|  | Declaration |
| --- | --- |
| From | ``` enum NEHotspotHelperConfidence : Int {     case None     case Low     case High } ``` |
| To | ``` enum NEHotspotHelperConfidence : Int {     case none     case low     case high } ``` |

Modified [NEHotspotHelperConfidence.high](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/knehotspothelperconfidencehigh)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [NEHotspotHelperConfidence.low](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/low)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [NEHotspotHelperConfidence.none](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [NEHotspotHelperResponse](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEHotspotHelperResponse : NSObject {     func setNetwork(_ network: NEHotspotNetwork)     func setNetworkList(_ networkList: [NEHotspotNetwork])     func deliver() } ``` | -- |
| To | ``` class NEHotspotHelperResponse : NSObject {     func setNetwork(_ network: NEHotspotNetwork)     func setNetworkList(_ networkList: [NEHotspotNetwork])     func deliver()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEHotspotHelperResponse : CVarArg { } extension NEHotspotHelperResponse : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEHotspotHelperResult [enum]](https://developer.apple.com/documentation/networkextension/nehotspothelperresult)

|  | Declaration |
| --- | --- |
| From | ``` enum NEHotspotHelperResult : Int {     case Success     case Failure     case UIRequired     case CommandNotRecognized     case AuthenticationRequired     case UnsupportedNetwork     case TemporaryFailure } ``` |
| To | ``` enum NEHotspotHelperResult : Int {     case success     case failure     case uiRequired     case commandNotRecognized     case authenticationRequired     case unsupportedNetwork     case temporaryFailure } ``` |

Modified [NEHotspotHelperResult.authenticationRequired](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultauthenticationrequired)

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticationRequired ``` |
| To | ``` case authenticationRequired ``` |

Modified [NEHotspotHelperResult.commandNotRecognized](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/knehotspothelperresultcommandnotrecognized)

|  | Declaration |
| --- | --- |
| From | ``` case CommandNotRecognized ``` |
| To | ``` case commandNotRecognized ``` |

Modified [NEHotspotHelperResult.failure](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/failure)

|  | Declaration |
| --- | --- |
| From | ``` case Failure ``` |
| To | ``` case failure ``` |

Modified [NEHotspotHelperResult.success](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [NEHotspotHelperResult.temporaryFailure](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/temporaryfailure)

|  | Declaration |
| --- | --- |
| From | ``` case TemporaryFailure ``` |
| To | ``` case temporaryFailure ``` |

Modified [NEHotspotHelperResult.uiRequired](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/uirequired)

|  | Declaration |
| --- | --- |
| From | ``` case UIRequired ``` |
| To | ``` case uiRequired ``` |

Modified [NEHotspotHelperResult.unsupportedNetwork](https://developer.apple.com/documentation/networkextension/nehotspothelperresult/unsupportednetwork)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedNetwork ``` |
| To | ``` case unsupportedNetwork ``` |

Modified [NEHotspotNetwork](https://developer.apple.com/documentation/networkextension/nehotspotnetwork)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEHotspotNetwork : NSObject {     var SSID: String { get }     var BSSID: String { get }     var signalStrength: Double { get }     var secure: Bool { get }     var autoJoined: Bool { get }     var justJoined: Bool { get }     var chosenHelper: Bool { get }     func setConfidence(_ confidence: NEHotspotHelperConfidence)     func setPassword(_ password: String) } ``` | -- |
| To | ``` class NEHotspotNetwork : NSObject {     var ssid: String { get }     var bssid: String { get }     var signalStrength: Double { get }     var isSecure: Bool { get }     var didAutoJoin: Bool { get }     var didJustJoin: Bool { get }     var isChosenHelper: Bool { get }     func setConfidence(_ confidence: NEHotspotHelperConfidence)     func setPassword(_ password: String)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEHotspotNetwork : CVarArg { } extension NEHotspotNetwork : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEHotspotNetwork.bssid](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618936-bssid)

|  | Declaration |
| --- | --- |
| From | ``` var BSSID: String { get } ``` |
| To | ``` var bssid: String { get } ``` |

Modified [NEHotspotNetwork.didAutoJoin](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618976-autojoined)

|  | Declaration |
| --- | --- |
| From | ``` var autoJoined: Bool { get } ``` |
| To | ``` var didAutoJoin: Bool { get } ``` |

Modified [NEHotspotNetwork.didJustJoin](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618955-justjoined)

|  | Declaration |
| --- | --- |
| From | ``` var justJoined: Bool { get } ``` |
| To | ``` var didJustJoin: Bool { get } ``` |

Modified [NEHotspotNetwork.isChosenHelper](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618975-ischosenhelper)

|  | Declaration |
| --- | --- |
| From | ``` var chosenHelper: Bool { get } ``` |
| To | ``` var isChosenHelper: Bool { get } ``` |

Modified [NEHotspotNetwork.isSecure](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618930-issecure)

|  | Declaration |
| --- | --- |
| From | ``` var secure: Bool { get } ``` |
| To | ``` var isSecure: Bool { get } ``` |

Modified [NEHotspotNetwork.ssid](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/1618925-ssid)

|  | Declaration |
| --- | --- |
| From | ``` var SSID: String { get } ``` |
| To | ``` var ssid: String { get } ``` |

Modified [NEIPv4Route](https://developer.apple.com/documentation/networkextension/neipv4route)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv4Route : NSObject, NSSecureCoding, NSCopying {     init(destinationAddress address: String, subnetMask subnetMask: String)     var destinationAddress: String { get }     var destinationSubnetMask: String { get }     var gatewayAddress: String?     class func defaultRoute() -> NEIPv4Route } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEIPv4Route : NSObject, NSSecureCoding, NSCopying {     init(destinationAddress address: String, subnetMask subnetMask: String)     var destinationAddress: String { get }     var destinationSubnetMask: String { get }     var gatewayAddress: String?     class func `default`() -> NEIPv4Route     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEIPv4Route : CVarArg { } extension NEIPv4Route : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEIPv4Route.default() [class]](https://developer.apple.com/documentation/networkextension/neipv4route/1406474-defaultroute)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultRoute() -> NEIPv4Route ``` |
| To | ``` class func `default`() -> NEIPv4Route ``` |

Modified [NEIPv4Settings](https://developer.apple.com/documentation/networkextension/neipv4settings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv4Settings : NSObject, NSSecureCoding, NSCopying {     init(addresses addresses: [String], subnetMasks subnetMasks: [String])     var addresses: [String] { get }     var subnetMasks: [String] { get }     var includedRoutes: [NEIPv4Route]?     var excludedRoutes: [NEIPv4Route]? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEIPv4Settings : NSObject, NSSecureCoding, NSCopying {     init(addresses addresses: [String], subnetMasks subnetMasks: [String])     var addresses: [String] { get }     var subnetMasks: [String] { get }     var includedRoutes: [NEIPv4Route]?     var excludedRoutes: [NEIPv4Route]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEIPv4Settings : CVarArg { } extension NEIPv4Settings : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEIPv6Route](https://developer.apple.com/documentation/networkextension/neipv6route)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv6Route : NSObject, NSSecureCoding, NSCopying {     init(destinationAddress address: String, networkPrefixLength networkPrefixLength: NSNumber)     var destinationAddress: String { get }     var destinationNetworkPrefixLength: NSNumber { get }     var gatewayAddress: String?     class func defaultRoute() -> NEIPv6Route } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEIPv6Route : NSObject, NSSecureCoding, NSCopying {     init(destinationAddress address: String, networkPrefixLength networkPrefixLength: NSNumber)     var destinationAddress: String { get }     var destinationNetworkPrefixLength: NSNumber { get }     var gatewayAddress: String?     class func `default`() -> NEIPv6Route     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEIPv6Route : CVarArg { } extension NEIPv6Route : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEIPv6Route.default() [class]](https://developer.apple.com/documentation/networkextension/neipv6route/1406847-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultRoute() -> NEIPv6Route ``` |
| To | ``` class func `default`() -> NEIPv6Route ``` |

Modified [NEIPv6Settings](https://developer.apple.com/documentation/networkextension/neipv6settings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEIPv6Settings : NSObject, NSSecureCoding, NSCopying {     init(addresses addresses: [String], networkPrefixLengths networkPrefixLengths: [NSNumber])     var addresses: [String] { get }     var networkPrefixLengths: [NSNumber] { get }     var includedRoutes: [NEIPv6Route]?     var excludedRoutes: [NEIPv6Route]? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEIPv6Settings : NSObject, NSSecureCoding, NSCopying {     init(addresses addresses: [String], networkPrefixLengths networkPrefixLengths: [NSNumber])     var addresses: [String] { get }     var networkPrefixLengths: [NSNumber] { get }     var includedRoutes: [NEIPv6Route]?     var excludedRoutes: [NEIPv6Route]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEIPv6Settings : CVarArg { } extension NEIPv6Settings : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEOnDemandRule](https://developer.apple.com/documentation/networkextension/neondemandrule)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEOnDemandRule : NSObject, NSSecureCoding, NSCopying {     var action: NEOnDemandRuleAction { get }     var DNSSearchDomainMatch: [String]?     var DNSServerAddressMatch: [String]?     var interfaceTypeMatch: NEOnDemandRuleInterfaceType     var SSIDMatch: [String]?     @NSCopying var probeURL: NSURL? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEOnDemandRule : NSObject, NSSecureCoding, NSCopying {     var action: NEOnDemandRuleAction { get }     var dnsSearchDomainMatch: [String]?     var dnsServerAddressMatch: [String]?     var interfaceTypeMatch: NEOnDemandRuleInterfaceType     var ssidMatch: [String]?     var probeURL: URL?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEOnDemandRule : CVarArg { } extension NEOnDemandRule : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEOnDemandRule.dnsSearchDomainMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406150-dnssearchdomainmatch)

|  | Declaration |
| --- | --- |
| From | ``` var DNSSearchDomainMatch: [String]? ``` |
| To | ``` var dnsSearchDomainMatch: [String]? ``` |

Modified [NEOnDemandRule.dnsServerAddressMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406551-dnsserveraddressmatch)

|  | Declaration |
| --- | --- |
| From | ``` var DNSServerAddressMatch: [String]? ``` |
| To | ``` var dnsServerAddressMatch: [String]? ``` |

Modified [NEOnDemandRule.probeURL](https://developer.apple.com/documentation/networkextension/neondemandrule/1405981-probeurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var probeURL: NSURL? ``` |
| To | ``` var probeURL: URL? ``` |

Modified [NEOnDemandRule.ssidMatch](https://developer.apple.com/documentation/networkextension/neondemandrule/1406503-ssidmatch)

|  | Declaration |
| --- | --- |
| From | ``` var SSIDMatch: [String]? ``` |
| To | ``` var ssidMatch: [String]? ``` |

Modified [NEOnDemandRuleAction [enum]](https://developer.apple.com/documentation/networkextension/neondemandruleaction)

|  | Declaration |
| --- | --- |
| From | ``` enum NEOnDemandRuleAction : Int {     case Connect     case Disconnect     case EvaluateConnection     case Ignore } ``` |
| To | ``` enum NEOnDemandRuleAction : Int {     case connect     case disconnect     case evaluateConnection     case ignore } ``` |

Modified [NEOnDemandRuleAction.connect](https://developer.apple.com/documentation/networkextension/neondemandruleaction/connect)

|  | Declaration |
| --- | --- |
| From | ``` case Connect ``` |
| To | ``` case connect ``` |

Modified [NEOnDemandRuleAction.disconnect](https://developer.apple.com/documentation/networkextension/neondemandruleaction/neondemandruleactiondisconnect)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnect ``` |
| To | ``` case disconnect ``` |

Modified [NEOnDemandRuleAction.evaluateConnection](https://developer.apple.com/documentation/networkextension/neondemandruleaction/neondemandruleactionevaluateconnection)

|  | Declaration |
| --- | --- |
| From | ``` case EvaluateConnection ``` |
| To | ``` case evaluateConnection ``` |

Modified [NEOnDemandRuleAction.ignore](https://developer.apple.com/documentation/networkextension/neondemandruleaction/neondemandruleactionignore)

|  | Declaration |
| --- | --- |
| From | ``` case Ignore ``` |
| To | ``` case ignore ``` |

Modified [NEOnDemandRuleInterfaceType [enum]](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype)

|  | Declaration |
| --- | --- |
| From | ``` enum NEOnDemandRuleInterfaceType : Int {     case Any     case Ethernet     case WiFi     case Cellular } ``` |
| To | ``` enum NEOnDemandRuleInterfaceType : Int {     case any     case ethernet     case wiFi     case cellular } ``` |

Modified [NEOnDemandRuleInterfaceType.any](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype/neondemandruleinterfacetypeany)

|  | Declaration |
| --- | --- |
| From | ``` case Any ``` |
| To | ``` case any ``` |

Modified [NEOnDemandRuleInterfaceType.cellular](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype/neondemandruleinterfacetypecellular)

|  | Declaration |
| --- | --- |
| From | ``` case Cellular ``` |
| To | ``` case cellular ``` |

Modified [NEOnDemandRuleInterfaceType.wiFi](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype/wifi)

|  | Declaration |
| --- | --- |
| From | ``` case WiFi ``` |
| To | ``` case wiFi ``` |

Modified [NEPacketTunnelFlow](https://developer.apple.com/documentation/networkextension/nepackettunnelflow)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEPacketTunnelFlow : NSObject {     func readPacketsWithCompletionHandler(_ completionHandler: ([NSData], [NSNumber]) -> Void)     func writePackets(_ packets: [NSData], withProtocols protocols: [NSNumber]) -> Bool } ``` | -- |
| To | ``` class NEPacketTunnelFlow : NSObject {     func readPackets(completionHandler completionHandler: @escaping ([Data], [NSNumber]) -> Swift.Void)     func writePackets(_ packets: [Data], withProtocols protocols: [NSNumber]) -> Bool     func readPacketObjects(completionHandler completionHandler: @escaping ([NEPacket]) -> Swift.Void)     func writePacketObjects(_ packets: [NEPacket]) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEPacketTunnelFlow : CVarArg { } extension NEPacketTunnelFlow : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEPacketTunnelFlow.readPackets(completionHandler: ([Data], [NSNumber]) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/1406903-readpackets)

|  | Declaration |
| --- | --- |
| From | ``` func readPacketsWithCompletionHandler(_ completionHandler: ([NSData], [NSNumber]) -> Void) ``` |
| To | ``` func readPackets(completionHandler completionHandler: @escaping ([Data], [NSNumber]) -> Swift.Void) ``` |

Modified [NEPacketTunnelFlow.writePackets(_: [Data], withProtocols: [NSNumber]) -> Bool](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/1406484-writepackets)

|  | Declaration |
| --- | --- |
| From | ``` func writePackets(_ packets: [NSData], withProtocols protocols: [NSNumber]) -> Bool ``` |
| To | ``` func writePackets(_ packets: [Data], withProtocols protocols: [NSNumber]) -> Bool ``` |

Modified [NEPacketTunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings)

|  | Declaration |
| --- | --- |
| From | ``` class NEPacketTunnelNetworkSettings : NETunnelNetworkSettings {     @NSCopying var IPv4Settings: NEIPv4Settings?     @NSCopying var IPv6Settings: NEIPv6Settings?     @NSCopying var tunnelOverheadBytes: NSNumber?     @NSCopying var MTU: NSNumber? } ``` |
| To | ``` class NEPacketTunnelNetworkSettings : NETunnelNetworkSettings {     @NSCopying var iPv4Settings: NEIPv4Settings?     @NSCopying var iPv6Settings: NEIPv6Settings?     @NSCopying var tunnelOverheadBytes: NSNumber?     @NSCopying var mtu: NSNumber? } ``` |

Modified [NEPacketTunnelNetworkSettings.iPv4Settings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406574-ipv4settings)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var IPv4Settings: NEIPv4Settings? ``` |
| To | ``` @NSCopying var iPv4Settings: NEIPv4Settings? ``` |

Modified [NEPacketTunnelNetworkSettings.iPv6Settings](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406138-ipv6settings)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var IPv6Settings: NEIPv6Settings? ``` |
| To | ``` @NSCopying var iPv6Settings: NEIPv6Settings? ``` |

Modified [NEPacketTunnelNetworkSettings.mtu](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/1406094-mtu)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var MTU: NSNumber? ``` |
| To | ``` @NSCopying var mtu: NSNumber? ``` |

Modified [NEPacketTunnelProvider](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NEPacketTunnelProvider : NETunnelProvider {     func startTunnelWithOptions(_ options: [String : NSObject]?, completionHandler completionHandler: (NSError?) -> Void)     func stopTunnelWithReason(_ reason: NEProviderStopReason, completionHandler completionHandler: () -> Void)     func cancelTunnelWithError(_ error: NSError?)     var packetFlow: NEPacketTunnelFlow { get }     func createTCPConnectionThroughTunnelToEndpoint(_ remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, TLSParameters TLSParameters: NWTLSParameters?, delegate delegate: AnyObject?) -> NWTCPConnection     func createUDPSessionThroughTunnelToEndpoint(_ remoteEndpoint: NWEndpoint, fromEndpoint localEndpoint: NWHostEndpoint?) -> NWUDPSession } ``` |
| To | ``` class NEPacketTunnelProvider : NETunnelProvider {     func startTunnel(options options: [String : NSObject]? = nil, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func stopTunnel(with reason: NEProviderStopReason, completionHandler completionHandler: @escaping () -> Swift.Void)     func cancelTunnelWithError(_ error: Error?)     var packetFlow: NEPacketTunnelFlow { get }     func createTCPConnectionThroughTunnel(to remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate delegate: Any?) -> NWTCPConnection     func createUDPSessionThroughTunnel(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession } ``` |

Modified [NEPacketTunnelProvider.cancelTunnelWithError(_: Error?)](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406169-canceltunnelwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func cancelTunnelWithError(_ error: NSError?) ``` |
| To | ``` func cancelTunnelWithError(_ error: Error?) ``` |

Modified [NEPacketTunnelProvider.createTCPConnectionThroughTunnel(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406055-createtcpconnectionthroughtunnel)

|  | Declaration |
| --- | --- |
| From | ``` func createTCPConnectionThroughTunnelToEndpoint(_ remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, TLSParameters TLSParameters: NWTLSParameters?, delegate delegate: AnyObject?) -> NWTCPConnection ``` |
| To | ``` func createTCPConnectionThroughTunnel(to remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate delegate: Any?) -> NWTCPConnection ``` |

Modified [NEPacketTunnelProvider.createUDPSessionThroughTunnel(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406068-createudpsessionthroughtunneltoe)

|  | Declaration |
| --- | --- |
| From | ``` func createUDPSessionThroughTunnelToEndpoint(_ remoteEndpoint: NWEndpoint, fromEndpoint localEndpoint: NWHostEndpoint?) -> NWUDPSession ``` |
| To | ``` func createUDPSessionThroughTunnel(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession ``` |

Modified [NEPacketTunnelProvider.startTunnel(options: [String : NSObject]?, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406118-starttunnelwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func startTunnelWithOptions(_ options: [String : NSObject]?, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func startTunnel(options options: [String : NSObject]? = nil, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEPacketTunnelProvider.stopTunnel(with: NEProviderStopReason, completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/1406192-stoptunnel)

|  | Declaration |
| --- | --- |
| From | ``` func stopTunnelWithReason(_ reason: NEProviderStopReason, completionHandler completionHandler: () -> Void) ``` |
| To | ``` func stopTunnel(with reason: NEProviderStopReason, completionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [NEProvider](https://developer.apple.com/documentation/networkextension/neprovider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEProvider : NSObject {     func sleepWithCompletionHandler(_ completionHandler: () -> Void)     func wake()     func createTCPConnectionToEndpoint(_ remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, TLSParameters TLSParameters: NWTLSParameters?, delegate delegate: AnyObject?) -> NWTCPConnection     func createUDPSessionToEndpoint(_ remoteEndpoint: NWEndpoint, fromEndpoint localEndpoint: NWHostEndpoint?) -> NWUDPSession     var defaultPath: NWPath? { get } } ``` | -- |
| To | ``` class NEProvider : NSObject {     func sleep(completionHandler completionHandler: @escaping () -> Swift.Void)     func wake()     func createTCPConnection(to remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate delegate: Any?) -> NWTCPConnection     func createUDPSession(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession     func displayMessage(_ message: String, completionHandler completionHandler: @escaping (Bool) -> Swift.Void)     var defaultPath: NWPath? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEProvider : CVarArg { } extension NEProvider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEProvider.createTCPConnection(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](https://developer.apple.com/documentation/networkextension/neprovider/1406529-createtcpconnectiontoendpoint)

|  | Declaration |
| --- | --- |
| From | ``` func createTCPConnectionToEndpoint(_ remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, TLSParameters TLSParameters: NWTLSParameters?, delegate delegate: AnyObject?) -> NWTCPConnection ``` |
| To | ``` func createTCPConnection(to remoteEndpoint: NWEndpoint, enableTLS enableTLS: Bool, tlsParameters TLSParameters: NWTLSParameters?, delegate delegate: Any?) -> NWTCPConnection ``` |

Modified [NEProvider.createUDPSession(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](https://developer.apple.com/documentation/networkextension/neprovider/1406004-createudpsessiontoendpoint)

|  | Declaration |
| --- | --- |
| From | ``` func createUDPSessionToEndpoint(_ remoteEndpoint: NWEndpoint, fromEndpoint localEndpoint: NWHostEndpoint?) -> NWUDPSession ``` |
| To | ``` func createUDPSession(to remoteEndpoint: NWEndpoint, from localEndpoint: NWHostEndpoint?) -> NWUDPSession ``` |

Modified [NEProvider.sleep(completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/networkextension/neprovider/1406731-sleepwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func sleepWithCompletionHandler(_ completionHandler: () -> Void) ``` |
| To | ``` func sleep(completionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [NEProviderStopReason [enum]](https://developer.apple.com/documentation/networkextension/neproviderstopreason)

|  | Declaration |
| --- | --- |
| From | ``` enum NEProviderStopReason : Int {     case None     case UserInitiated     case ProviderFailed     case NoNetworkAvailable     case UnrecoverableNetworkChange     case ProviderDisabled     case AuthenticationCanceled     case ConfigurationFailed     case IdleTimeout     case ConfigurationDisabled     case ConfigurationRemoved     case Superceded     case UserLogout     case UserSwitch     case ConnectionFailed } ``` |
| To | ``` enum NEProviderStopReason : Int {     case none     case userInitiated     case providerFailed     case noNetworkAvailable     case unrecoverableNetworkChange     case providerDisabled     case authenticationCanceled     case configurationFailed     case idleTimeout     case configurationDisabled     case configurationRemoved     case superceded     case userLogout     case userSwitch     case connectionFailed } ``` |

Modified [NEProviderStopReason.authenticationCanceled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonauthenticationcanceled)

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticationCanceled ``` |
| To | ``` case authenticationCanceled ``` |

Modified [NEProviderStopReason.configurationDisabled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationdisabled)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationDisabled ``` |
| To | ``` case configurationDisabled ``` |

Modified [NEProviderStopReason.configurationFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationFailed ``` |
| To | ``` case configurationFailed ``` |

Modified [NEProviderStopReason.configurationRemoved](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonconfigurationremoved)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationRemoved ``` |
| To | ``` case configurationRemoved ``` |

Modified [NEProviderStopReason.connectionFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/connectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionFailed ``` |
| To | ``` case connectionFailed ``` |

Modified [NEProviderStopReason.idleTimeout](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonidletimeout)

|  | Declaration |
| --- | --- |
| From | ``` case IdleTimeout ``` |
| To | ``` case idleTimeout ``` |

Modified [NEProviderStopReason.none](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [NEProviderStopReason.noNetworkAvailable](https://developer.apple.com/documentation/networkextension/neproviderstopreason/nonetworkavailable)

|  | Declaration |
| --- | --- |
| From | ``` case NoNetworkAvailable ``` |
| To | ``` case noNetworkAvailable ``` |

Modified [NEProviderStopReason.providerDisabled](https://developer.apple.com/documentation/networkextension/neproviderstopreason/providerdisabled)

|  | Declaration |
| --- | --- |
| From | ``` case ProviderDisabled ``` |
| To | ``` case providerDisabled ``` |

Modified [NEProviderStopReason.providerFailed](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonproviderfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ProviderFailed ``` |
| To | ``` case providerFailed ``` |

Modified [NEProviderStopReason.superceded](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonsuperceded)

|  | Declaration |
| --- | --- |
| From | ``` case Superceded ``` |
| To | ``` case superceded ``` |

Modified [NEProviderStopReason.unrecoverableNetworkChange](https://developer.apple.com/documentation/networkextension/neproviderstopreason/unrecoverablenetworkchange)

|  | Declaration |
| --- | --- |
| From | ``` case UnrecoverableNetworkChange ``` |
| To | ``` case unrecoverableNetworkChange ``` |

Modified [NEProviderStopReason.userInitiated](https://developer.apple.com/documentation/networkextension/neproviderstopreason/userinitiated)

|  | Declaration |
| --- | --- |
| From | ``` case UserInitiated ``` |
| To | ``` case userInitiated ``` |

Modified [NEProviderStopReason.userLogout](https://developer.apple.com/documentation/networkextension/neproviderstopreason/neproviderstopreasonuserlogout)

|  | Declaration |
| --- | --- |
| From | ``` case UserLogout ``` |
| To | ``` case userLogout ``` |

Modified [NEProviderStopReason.userSwitch](https://developer.apple.com/documentation/networkextension/neproviderstopreason/userswitch)

|  | Declaration |
| --- | --- |
| From | ``` case UserSwitch ``` |
| To | ``` case userSwitch ``` |

Modified [NEProxyServer](https://developer.apple.com/documentation/networkextension/neproxyserver)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEProxyServer : NSObject, NSSecureCoding, NSCopying {     init(address address: String, port port: Int)     var address: String { get }     var port: Int { get }     var authenticationRequired: Bool     var username: String?     var password: String? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEProxyServer : NSObject, NSSecureCoding, NSCopying {     init(address address: String, port port: Int)     var address: String { get }     var port: Int { get }     var authenticationRequired: Bool     var username: String?     var password: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEProxyServer : CVarArg { } extension NEProxyServer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEProxySettings](https://developer.apple.com/documentation/networkextension/neproxysettings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEProxySettings : NSObject, NSSecureCoding, NSCopying {     var autoProxyConfigurationEnabled: Bool     @NSCopying var proxyAutoConfigurationURL: NSURL?     var proxyAutoConfigurationJavaScript: String?     var HTTPEnabled: Bool     @NSCopying var HTTPServer: NEProxyServer?     var HTTPSEnabled: Bool     @NSCopying var HTTPSServer: NEProxyServer?     var excludeSimpleHostnames: Bool     var exceptionList: [String]?     var matchDomains: [String]? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEProxySettings : NSObject, NSSecureCoding, NSCopying {     var autoProxyConfigurationEnabled: Bool     var proxyAutoConfigurationURL: URL?     var proxyAutoConfigurationJavaScript: String?     var httpEnabled: Bool     @NSCopying var httpServer: NEProxyServer?     var httpsEnabled: Bool     @NSCopying var httpsServer: NEProxyServer?     var excludeSimpleHostnames: Bool     var exceptionList: [String]?     var matchDomains: [String]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEProxySettings : CVarArg { } extension NEProxySettings : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEProxySettings.httpEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406179-httpenabled)

|  | Declaration |
| --- | --- |
| From | ``` var HTTPEnabled: Bool ``` |
| To | ``` var httpEnabled: Bool ``` |

Modified [NEProxySettings.httpsEnabled](https://developer.apple.com/documentation/networkextension/neproxysettings/1406309-httpsenabled)

|  | Declaration |
| --- | --- |
| From | ``` var HTTPSEnabled: Bool ``` |
| To | ``` var httpsEnabled: Bool ``` |

Modified [NEProxySettings.httpServer](https://developer.apple.com/documentation/networkextension/neproxysettings/1406834-httpserver)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var HTTPServer: NEProxyServer? ``` |
| To | ``` @NSCopying var httpServer: NEProxyServer? ``` |

Modified [NEProxySettings.httpsServer](https://developer.apple.com/documentation/networkextension/neproxysettings/1406366-httpsserver)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var HTTPSServer: NEProxyServer? ``` |
| To | ``` @NSCopying var httpsServer: NEProxyServer? ``` |

Modified [NEProxySettings.proxyAutoConfigurationURL](https://developer.apple.com/documentation/networkextension/neproxysettings/1406225-proxyautoconfigurationurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var proxyAutoConfigurationURL: NSURL? ``` |
| To | ``` var proxyAutoConfigurationURL: URL? ``` |

Modified [NETunnelNetworkSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NETunnelNetworkSettings : NSObject, NSSecureCoding, NSCopying {     init(tunnelRemoteAddress address: String)     var tunnelRemoteAddress: String { get }     @NSCopying var DNSSettings: NEDNSSettings?     @NSCopying var proxySettings: NEProxySettings? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NETunnelNetworkSettings : NSObject, NSSecureCoding, NSCopying {     init(tunnelRemoteAddress address: String)     var tunnelRemoteAddress: String { get }     @NSCopying var dnsSettings: NEDNSSettings?     @NSCopying var proxySettings: NEProxySettings?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NETunnelNetworkSettings : CVarArg { } extension NETunnelNetworkSettings : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NETunnelNetworkSettings.dnsSettings](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/1406331-dnssettings)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var DNSSettings: NEDNSSettings? ``` |
| To | ``` @NSCopying var dnsSettings: NEDNSSettings? ``` |

Modified [NETunnelProvider](https://developer.apple.com/documentation/networkextension/netunnelprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NETunnelProvider : NEProvider {     func handleAppMessage(_ messageData: NSData, completionHandler completionHandler: ((NSData?) -> Void)?)     func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: ((NSError?) -> Void)?)     var protocolConfiguration: NEVPNProtocol { get }     var appRules: [NEAppRule]? { get }     var routingMethod: NETunnelProviderRoutingMethod { get }     var reasserting: Bool } ``` |
| To | ``` class NETunnelProvider : NEProvider {     func handleAppMessage(_ messageData: Data, completionHandler completionHandler: (@escaping (Data?) -> Swift.Void)? = nil)     func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     var protocolConfiguration: NEVPNProtocol { get }     var appRules: [NEAppRule]? { get }     var routingMethod: NETunnelProviderRoutingMethod { get }     var reasserting: Bool } ``` |

Modified [NETunnelProvider.handleAppMessage(_: Data, completionHandler: ( (Data?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406545-handleappmessage)

|  | Declaration |
| --- | --- |
| From | ``` func handleAppMessage(_ messageData: NSData, completionHandler completionHandler: ((NSData?) -> Void)?) ``` |
| To | ``` func handleAppMessage(_ messageData: Data, completionHandler completionHandler: (@escaping (Data?) -> Swift.Void)? = nil) ``` |

Modified [NETunnelProvider.setTunnelNetworkSettings(_: NETunnelNetworkSettings?, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406539-settunnelnetworksettings)

|  | Declaration |
| --- | --- |
| From | ``` func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [NETunnelProviderErrorDomain [enum]](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum NETunnelProviderError : Int {     case NetworkSettingsInvalid     case NetworkSettingsCanceled     case NetworkSettingsFailed } ``` |
| To | ``` enum NETunnelProviderErrorDomain : Int {     case networkSettingsInvalid     case networkSettingsCanceled     case networkSettingsFailed } ``` |

Modified [NETunnelProviderErrorDomain.networkSettingsCanceled](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingscanceled)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkSettingsCanceled ``` |
| To | ``` case networkSettingsCanceled ``` |

Modified [NETunnelProviderErrorDomain.networkSettingsFailed](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingsfailed)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkSettingsFailed ``` |
| To | ``` case networkSettingsFailed ``` |

Modified [NETunnelProviderErrorDomain.networkSettingsInvalid](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/netunnelprovidererrornetworksettingsinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkSettingsInvalid ``` |
| To | ``` case networkSettingsInvalid ``` |

Modified [NETunnelProviderManager](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager)

|  | Declaration |
| --- | --- |
| From | ``` class NETunnelProviderManager : NEVPNManager {     class func loadAllFromPreferencesWithCompletionHandler(_ completionHandler: ([NETunnelProviderManager]?, NSError?) -> Void)     func copyAppRules() -> [NEAppRule]?     var routingMethod: NETunnelProviderRoutingMethod { get } } ``` |
| To | ``` class NETunnelProviderManager : NEVPNManager {     class func loadAllFromPreferences(completionHandler completionHandler: @escaping ([NETunnelProviderManager]?, Error?) -> Swift.Void)     func copyAppRules() -> [NEAppRule]?     var routingMethod: NETunnelProviderRoutingMethod { get } } ``` |

Modified [NETunnelProviderManager.loadAllFromPreferences(completionHandler: ([NETunnelProviderManager]?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/1406271-loadallfrompreferences)

|  | Declaration |
| --- | --- |
| From | ``` class func loadAllFromPreferencesWithCompletionHandler(_ completionHandler: ([NETunnelProviderManager]?, NSError?) -> Void) ``` |
| To | ``` class func loadAllFromPreferences(completionHandler completionHandler: @escaping ([NETunnelProviderManager]?, Error?) -> Swift.Void) ``` |

Modified [NETunnelProviderProtocol](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol)

|  | Declaration |
| --- | --- |
| From | ``` class NETunnelProviderProtocol : NEVPNProtocol {     var providerConfiguration: [String : AnyObject]?     var providerBundleIdentifier: String? } ``` |
| To | ``` class NETunnelProviderProtocol : NEVPNProtocol {     var providerConfiguration: [String : Any]?     var providerBundleIdentifier: String? } ``` |

Modified [NETunnelProviderProtocol.providerConfiguration](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol/1406206-providerconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` var providerConfiguration: [String : AnyObject]? ``` |
| To | ``` var providerConfiguration: [String : Any]? ``` |

Modified [NETunnelProviderRoutingMethod [enum]](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod)

|  | Declaration |
| --- | --- |
| From | ``` enum NETunnelProviderRoutingMethod : Int {     case DestinationIP     case SourceApplication } ``` |
| To | ``` enum NETunnelProviderRoutingMethod : Int {     case destinationIP     case sourceApplication } ``` |

Modified [NETunnelProviderRoutingMethod.destinationIP](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod/destinationip)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationIP ``` |
| To | ``` case destinationIP ``` |

Modified [NETunnelProviderRoutingMethod.sourceApplication](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod/sourceapplication)

|  | Declaration |
| --- | --- |
| From | ``` case SourceApplication ``` |
| To | ``` case sourceApplication ``` |

Modified [NETunnelProviderSession](https://developer.apple.com/documentation/networkextension/netunnelprovidersession)

|  | Declaration |
| --- | --- |
| From | ``` class NETunnelProviderSession : NEVPNConnection {     func startTunnelWithOptions(_ options: [String : AnyObject]?) throws     func stopTunnel()     func sendProviderMessage(_ messageData: NSData, responseHandler responseHandler: ((NSData?) -> Void)?) throws } ``` |
| To | ``` class NETunnelProviderSession : NEVPNConnection {     func startTunnel(options options: [String : Any]? = nil) throws     func stopTunnel()     func sendProviderMessage(_ messageData: Data, responseHandler responseHandler: (@escaping (Data?) -> Swift.Void)? = nil) throws } ``` |

Modified [NETunnelProviderSession.sendProviderMessage(_: Data, responseHandler: ( (Data?) -> Swift.Void)?) throws](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1406409-sendprovidermessage)

|  | Declaration |
| --- | --- |
| From | ``` func sendProviderMessage(_ messageData: NSData, responseHandler responseHandler: ((NSData?) -> Void)?) throws ``` |
| To | ``` func sendProviderMessage(_ messageData: Data, responseHandler responseHandler: (@escaping (Data?) -> Swift.Void)? = nil) throws ``` |

Modified [NETunnelProviderSession.startTunnel(options: [String : Any]?) throws](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1405991-starttunnelwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func startTunnelWithOptions(_ options: [String : AnyObject]?) throws ``` |
| To | ``` func startTunnel(options options: [String : Any]? = nil) throws ``` |

Modified [NEVPNConnection](https://developer.apple.com/documentation/networkextension/nevpnconnection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEVPNConnection : NSObject {     func startVPNTunnel() throws     func startVPNTunnelWithOptions(_ options: [String : NSObject]?) throws     func stopVPNTunnel()     var status: NEVPNStatus { get }     var connectedDate: NSDate? { get } } ``` | -- |
| To | ``` class NEVPNConnection : NSObject {     func startVPNTunnel() throws     func startVPNTunnel(options options: [String : NSObject]? = nil) throws     func stopVPNTunnel()     var status: NEVPNStatus { get }     var connectedDate: Date? { get }     var manager: NEVPNManager { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEVPNConnection : CVarArg { } extension NEVPNConnection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEVPNConnection.connectedDate](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406140-connecteddate)

|  | Declaration |
| --- | --- |
| From | ``` var connectedDate: NSDate? { get } ``` |
| To | ``` var connectedDate: Date? { get } ``` |

Modified [NEVPNConnection.startVPNTunnel(options: [String : NSObject]?) throws](https://developer.apple.com/documentation/networkextension/nevpnconnection/1406061-startvpntunnelwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func startVPNTunnelWithOptions(_ options: [String : NSObject]?) throws ``` |
| To | ``` func startVPNTunnel(options options: [String : NSObject]? = nil) throws ``` |

Modified [NEVPNErrorDomain [enum]](https://developer.apple.com/documentation/networkextension/nevpnerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNError : Int {     case ConfigurationInvalid     case ConfigurationDisabled     case ConnectionFailed     case ConfigurationStale     case ConfigurationReadWriteFailed     case ConfigurationUnknown } ``` |
| To | ``` enum NEVPNErrorDomain : Int {     case configurationInvalid     case configurationDisabled     case connectionFailed     case configurationStale     case configurationReadWriteFailed     case configurationUnknown } ``` |

Modified [NEVPNErrorDomain.configurationDisabled](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconfigurationdisabled)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationDisabled ``` |
| To | ``` case configurationDisabled ``` |

Modified [NEVPNErrorDomain.configurationInvalid](https://developer.apple.com/documentation/networkextension/nevpnerror/code/configurationinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationInvalid ``` |
| To | ``` case configurationInvalid ``` |

Modified [NEVPNErrorDomain.configurationReadWriteFailed](https://developer.apple.com/documentation/networkextension/nevpnerror/code/configurationreadwritefailed)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationReadWriteFailed ``` |
| To | ``` case configurationReadWriteFailed ``` |

Modified [NEVPNErrorDomain.configurationStale](https://developer.apple.com/documentation/networkextension/nevpnerror/code/configurationstale)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationStale ``` |
| To | ``` case configurationStale ``` |

Modified [NEVPNErrorDomain.configurationUnknown](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconfigurationunknown)

|  | Declaration |
| --- | --- |
| From | ``` case ConfigurationUnknown ``` |
| To | ``` case configurationUnknown ``` |

Modified [NEVPNErrorDomain.connectionFailed](https://developer.apple.com/documentation/networkextension/nevpnerror/nevpnerrorconnectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case ConnectionFailed ``` |
| To | ``` case connectionFailed ``` |

Modified [NEVPNIKEAuthenticationMethod [enum]](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNIKEAuthenticationMethod : Int {     case None     case Certificate     case SharedSecret } ``` |
| To | ``` enum NEVPNIKEAuthenticationMethod : Int {     case none     case certificate     case sharedSecret } ``` |

Modified [NEVPNIKEAuthenticationMethod.certificate](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod/nevpnikeauthenticationmethodcertificate)

|  | Declaration |
| --- | --- |
| From | ``` case Certificate ``` |
| To | ``` case certificate ``` |

Modified [NEVPNIKEAuthenticationMethod.none](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod/nevpnikeauthenticationmethodnone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [NEVPNIKEAuthenticationMethod.sharedSecret](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod/nevpnikeauthenticationmethodsharedsecret)

|  | Declaration |
| --- | --- |
| From | ``` case SharedSecret ``` |
| To | ``` case sharedSecret ``` |

Modified [NEVPNIKEv2DeadPeerDetectionRate [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNIKEv2DeadPeerDetectionRate : Int {     case None     case Low     case Medium     case High } ``` |
| To | ``` enum NEVPNIKEv2DeadPeerDetectionRate : Int {     case none     case low     case medium     case high } ``` |

Modified [NEVPNIKEv2DeadPeerDetectionRate.high](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate/high)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [NEVPNIKEv2DeadPeerDetectionRate.low](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate/low)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [NEVPNIKEv2DeadPeerDetectionRate.medium](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate/medium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [NEVPNIKEv2DeadPeerDetectionRate.none](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNIKEv2DiffieHellmanGroup : Int {     case Group0     case Group1     case Group2     case Group5     case Group14     case Group15     case Group16     case Group17     case Group18     case Group19     case Group20     case Group21 } ``` |
| To | ``` enum NEVPNIKEv2DiffieHellmanGroup : Int {     case groupInvalid     case group1     case group2     case group5     case group14     case group15     case group16     case group17     case group18     case group19     case group20     case group21 } ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group1](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group1)

|  | Declaration |
| --- | --- |
| From | ``` case Group1 ``` |
| To | ``` case group1 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group14](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group14)

|  | Declaration |
| --- | --- |
| From | ``` case Group14 ``` |
| To | ``` case group14 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group15](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group15)

|  | Declaration |
| --- | --- |
| From | ``` case Group15 ``` |
| To | ``` case group15 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group16](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group16)

|  | Declaration |
| --- | --- |
| From | ``` case Group16 ``` |
| To | ``` case group16 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group17](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group17)

|  | Declaration |
| --- | --- |
| From | ``` case Group17 ``` |
| To | ``` case group17 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group18](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group18)

|  | Declaration |
| --- | --- |
| From | ``` case Group18 ``` |
| To | ``` case group18 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group19](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group19)

|  | Declaration |
| --- | --- |
| From | ``` case Group19 ``` |
| To | ``` case group19 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group2](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/nevpnikev2diffiehellmangroup2)

|  | Declaration |
| --- | --- |
| From | ``` case Group2 ``` |
| To | ``` case group2 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group20](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/nevpnikev2diffiehellmangroup20)

|  | Declaration |
| --- | --- |
| From | ``` case Group20 ``` |
| To | ``` case group20 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group21](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/nevpnikev2diffiehellmangroup21)

|  | Declaration |
| --- | --- |
| From | ``` case Group21 ``` |
| To | ``` case group21 ``` |

Modified [NEVPNIKEv2DiffieHellmanGroup.group5](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/group5)

|  | Declaration |
| --- | --- |
| From | ``` case Group5 ``` |
| To | ``` case group5 ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm [enum]](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNIKEv2EncryptionAlgorithm : Int {     case AlgorithmDES     case Algorithm3DES     case AlgorithmAES128     case AlgorithmAES256     case AlgorithmAES128GCM     case AlgorithmAES256GCM } ``` |
| To | ``` enum NEVPNIKEv2EncryptionAlgorithm : Int {     case algorithmDES     case algorithm3DES     case algorithmAES128     case algorithmAES256     case algorithmAES128GCM     case algorithmAES256GCM } ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm.algorithm3DES](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/algorithm3des)

|  | Declaration |
| --- | --- |
| From | ``` case Algorithm3DES ``` |
| To | ``` case algorithm3DES ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm.algorithmAES128](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/nevpnikev2encryptionalgorithmaes128)

|  | Declaration |
| --- | --- |
| From | ``` case AlgorithmAES128 ``` |
| To | ``` case algorithmAES128 ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm.algorithmAES128GCM](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/nevpnikev2encryptionalgorithmaes128gcm)

|  | Declaration |
| --- | --- |
| From | ``` case AlgorithmAES128GCM ``` |
| To | ``` case algorithmAES128GCM ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm.algorithmAES256](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/algorithmaes256)

|  | Declaration |
| --- | --- |
| From | ``` case AlgorithmAES256 ``` |
| To | ``` case algorithmAES256 ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm.algorithmAES256GCM](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/algorithmaes256gcm)

|  | Declaration |
| --- | --- |
| From | ``` case AlgorithmAES256GCM ``` |
| To | ``` case algorithmAES256GCM ``` |

Modified [NEVPNIKEv2EncryptionAlgorithm.algorithmDES](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm/algorithmdes)

|  | Declaration |
| --- | --- |
| From | ``` case AlgorithmDES ``` |
| To | ``` case algorithmDES ``` |

Modified [NEVPNIKEv2SecurityAssociationParameters](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEVPNIKEv2SecurityAssociationParameters : NSObject, NSSecureCoding, NSCopying {     var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm     var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm     var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup     var lifetimeMinutes: Int32 } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEVPNIKEv2SecurityAssociationParameters : NSObject, NSSecureCoding, NSCopying {     var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm     var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm     var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup     var lifetimeMinutes: Int32     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEVPNIKEv2SecurityAssociationParameters : CVarArg { } extension NEVPNIKEv2SecurityAssociationParameters : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEVPNManager](https://developer.apple.com/documentation/networkextension/nevpnmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEVPNManager : NSObject {     class func sharedManager() -> NEVPNManager     func loadFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void)     func removeFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     func saveToPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     var onDemandRules: [NEOnDemandRule]?     var onDemandEnabled: Bool     var localizedDescription: String?     var `protocol`: NEVPNProtocol?     var protocolConfiguration: NEVPNProtocol?     var connection: NEVPNConnection { get }     var enabled: Bool } ``` | -- |
| To | ``` class NEVPNManager : NSObject {     class func shared() -> NEVPNManager     func loadFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func removeFromPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func saveToPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     var onDemandRules: [NEOnDemandRule]?     var isOnDemandEnabled: Bool     var localizedDescription: String?     var `protocol`: NEVPNProtocol?     var protocolConfiguration: NEVPNProtocol?     var connection: NEVPNConnection { get }     var isEnabled: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEVPNManager : CVarArg { } extension NEVPNManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NEVPNManager.isEnabled](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406382-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [NEVPNManager.isOnDemandEnabled](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406200-isondemandenabled)

|  | Declaration |
| --- | --- |
| From | ``` var onDemandEnabled: Bool ``` |
| To | ``` var isOnDemandEnabled: Bool ``` |

Modified [NEVPNManager.loadFromPreferences(completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406177-loadfrompreferenceswithcompletio)

|  | Declaration |
| --- | --- |
| From | ``` func loadFromPreferencesWithCompletionHandler(_ completionHandler: (NSError?) -> Void) ``` |
| To | ``` func loadFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NEVPNManager.removeFromPreferences(completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406202-removefrompreferenceswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func removeFromPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [NEVPNManager.saveToPreferences(completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1405985-savetopreferenceswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` func saveToPreferencesWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func saveToPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [NEVPNManager.shared() -> NEVPNManager [class]](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406039-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedManager() -> NEVPNManager ``` |
| To | ``` class func shared() -> NEVPNManager ``` |

Modified [NEVPNProtocol](https://developer.apple.com/documentation/networkextension/nevpnprotocol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NEVPNProtocol : NSObject, NSCopying, NSSecureCoding {     var serverAddress: String?     var username: String?     @NSCopying var passwordReference: NSData?     @NSCopying var identityReference: NSData?     @NSCopying var identityData: NSData?     var identityDataPassword: String?     var disconnectOnSleep: Bool     @NSCopying var proxySettings: NEProxySettings? } ``` | NSCopying, NSSecureCoding |
| To | ``` class NEVPNProtocol : NSObject, NSCopying, NSSecureCoding {     var serverAddress: String?     var username: String?     var passwordReference: Data?     var identityReference: Data?     var identityData: Data?     var identityDataPassword: String?     var disconnectOnSleep: Bool     @NSCopying var proxySettings: NEProxySettings?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEVPNProtocol : CVarArg { } extension NEVPNProtocol : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NEVPNProtocol.identityData](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406142-identitydata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var identityData: NSData? ``` |
| To | ``` var identityData: Data? ``` |

Modified [NEVPNProtocol.identityReference](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406609-identityreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var identityReference: NSData? ``` |
| To | ``` var identityReference: Data? ``` |

Modified [NEVPNProtocol.passwordReference](https://developer.apple.com/documentation/networkextension/nevpnprotocol/1406650-passwordreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var passwordReference: NSData? ``` |
| To | ``` var passwordReference: Data? ``` |

Modified [NEVPNProtocolIKEv2](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNProtocolIKEv2 : NEVPNProtocolIPSec {     var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate     var serverCertificateIssuerCommonName: String?     var serverCertificateCommonName: String?     var certificateType: NEVPNIKEv2CertificateType     var useConfigurationAttributeInternalIPSubnet: Bool     var IKESecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }     var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }     var disableMOBIKE: Bool     var disableRedirect: Bool     var enablePFS: Bool     var enableRevocationCheck: Bool     var strictRevocationCheck: Bool } ``` |
| To | ``` class NEVPNProtocolIKEv2 : NEVPNProtocolIPSec {     var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate     var serverCertificateIssuerCommonName: String?     var serverCertificateCommonName: String?     var certificateType: NEVPNIKEv2CertificateType     var useConfigurationAttributeInternalIPSubnet: Bool     var ikeSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }     var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }     var disableMOBIKE: Bool     var disableRedirect: Bool     var enablePFS: Bool     var enableRevocationCheck: Bool     var strictRevocationCheck: Bool } ``` |

Modified [NEVPNProtocolIKEv2.ikeSecurityAssociationParameters](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/1406214-ikesecurityassociationparameters)

|  | Declaration |
| --- | --- |
| From | ``` var IKESecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get } ``` |
| To | ``` var ikeSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get } ``` |

Modified [NEVPNProtocolIPSec](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNProtocolIPSec : NEVPNProtocol {     var authenticationMethod: NEVPNIKEAuthenticationMethod     var useExtendedAuthentication: Bool     @NSCopying var sharedSecretReference: NSData?     var localIdentifier: String?     var remoteIdentifier: String? } ``` |
| To | ``` class NEVPNProtocolIPSec : NEVPNProtocol {     var authenticationMethod: NEVPNIKEAuthenticationMethod     var useExtendedAuthentication: Bool     var sharedSecretReference: Data?     var localIdentifier: String?     var remoteIdentifier: String? } ``` |

Modified [NEVPNProtocolIPSec.sharedSecretReference](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec/1406112-sharedsecretreference)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sharedSecretReference: NSData? ``` |
| To | ``` var sharedSecretReference: Data? ``` |

Modified [NEVPNStatus [enum]](https://developer.apple.com/documentation/networkextension/nevpnstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNStatus : Int {     case Invalid     case Disconnected     case Connecting     case Connected     case Reasserting     case Disconnecting } ``` |
| To | ``` enum NEVPNStatus : Int {     case invalid     case disconnected     case connecting     case connected     case reasserting     case disconnecting } ``` |

Modified [NEVPNStatus.connected](https://developer.apple.com/documentation/networkextension/nevpnstatus/connected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [NEVPNStatus.connecting](https://developer.apple.com/documentation/networkextension/nevpnstatus/nevpnstatusconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Connecting ``` |
| To | ``` case connecting ``` |

Modified [NEVPNStatus.disconnected](https://developer.apple.com/documentation/networkextension/nevpnstatus/disconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnected ``` |
| To | ``` case disconnected ``` |

Modified [NEVPNStatus.disconnecting](https://developer.apple.com/documentation/networkextension/nevpnstatus/nevpnstatusdisconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnecting ``` |
| To | ``` case disconnecting ``` |

Modified [NEVPNStatus.invalid](https://developer.apple.com/documentation/networkextension/nevpnstatus/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [NEVPNStatus.reasserting](https://developer.apple.com/documentation/networkextension/nevpnstatus/reasserting)

|  | Declaration |
| --- | --- |
| From | ``` case Reasserting ``` |
| To | ``` case reasserting ``` |

Modified [NSMutableURLRequest.bind(to: NEHotspotHelperCommand)](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/1619006-bind)

|  | Declaration |
| --- | --- |
| From | ``` func bindToHotspotHelperCommand(_ command: NEHotspotHelperCommand) ``` |
| To | ``` func bind(to command: NEHotspotHelperCommand) ``` |

Modified [NSNotification.Name.NEFilterConfigurationDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1406656-nefilterconfigurationdidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | NEFilterConfigurationDidChangeNotification | ``` let NEFilterConfigurationDidChangeNotification: String ``` |
| To | NEFilterConfigurationDidChange | ``` static let NEFilterConfigurationDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.NEVPNConfigurationChange](https://developer.apple.com/documentation/networkextension/nevpnconfigurationchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | NEVPNConfigurationChangeNotification | ``` let NEVPNConfigurationChangeNotification: String ``` |
| To | NEVPNConfigurationChange | ``` static let NEVPNConfigurationChange: NSNotification.Name ``` |

Modified [NSNotification.Name.NEVPNStatusDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1406683-nevpnstatusdidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | NEVPNStatusDidChangeNotification | ``` let NEVPNStatusDidChangeNotification: String ``` |
| To | NEVPNStatusDidChange | ``` static let NEVPNStatusDidChange: NSNotification.Name ``` |

Modified [NWBonjourServiceEndpoint](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint)

|  | Declaration |
| --- | --- |
| From | ``` class NWBonjourServiceEndpoint : NWEndpoint {     convenience init(name name: String, type type: String, domain domain: String)     class func endpointWithName(_ name: String, type type: String, domain domain: String) -> Self     var name: String { get }     var type: String { get }     var domain: String { get } } ``` |
| To | ``` class NWBonjourServiceEndpoint : NWEndpoint {     convenience init(name name: String, type type: String, domain domain: String)     class func withName(_ name: String, type type: String, domain domain: String) -> Self     var name: String { get }     var type: String { get }     var domain: String { get } } ``` |

Modified [NWEndpoint](https://developer.apple.com/documentation/networkextension/nwendpoint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NWEndpoint : NSObject { } ``` | -- |
| To | ``` class NWEndpoint : NSObject, NSSecureCoding, NSCopying {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NWEndpoint : CVarArg { } extension NWEndpoint : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [NWHostEndpoint](https://developer.apple.com/documentation/networkextension/nwhostendpoint)

|  | Declaration |
| --- | --- |
| From | ``` class NWHostEndpoint : NWEndpoint {     convenience init(hostname hostname: String, port port: String)     class func endpointWithHostname(_ hostname: String, port port: String) -> Self     var hostname: String { get }     var port: String { get } } ``` |
| To | ``` class NWHostEndpoint : NWEndpoint {     convenience init(hostname hostname: String, port port: String)     class func withHostname(_ hostname: String, port port: String) -> Self     var hostname: String { get }     var port: String { get } } ``` |

Modified [NWPath](https://developer.apple.com/documentation/networkextension/nwpath)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NWPath : NSObject {     var status: NWPathStatus { get }     var expensive: Bool { get }     func isEqualToPath(_ path: NWPath) -> Bool } ``` | -- |
| To | ``` class NWPath : NSObject {     var status: NWPathStatus { get }     var isExpensive: Bool { get }     func isEqual(to path: NWPath) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NWPath : CVarArg { } extension NWPath : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NWPath.isEqual(to: NWPath) -> Bool](https://developer.apple.com/documentation/networkextension/nwpath/1406152-isequal)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToPath(_ path: NWPath) -> Bool ``` |
| To | ``` func isEqual(to path: NWPath) -> Bool ``` |

Modified [NWPath.isExpensive](https://developer.apple.com/documentation/networkextension/nwpath/1406899-isexpensive)

|  | Declaration |
| --- | --- |
| From | ``` var expensive: Bool { get } ``` |
| To | ``` var isExpensive: Bool { get } ``` |

Modified [NWPathStatus [enum]](https://developer.apple.com/documentation/networkextension/nwpathstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum NWPathStatus : Int {     case Invalid     case Satisfied     case Unsatisfied     case Satisfiable } ``` |
| To | ``` enum NWPathStatus : Int {     case invalid     case satisfied     case unsatisfied     case satisfiable } ``` |

Modified [NWPathStatus.invalid](https://developer.apple.com/documentation/networkextension/nwpathstatus/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [NWPathStatus.satisfiable](https://developer.apple.com/documentation/networkextension/nwpathstatus/nwpathstatussatisfiable)

|  | Declaration |
| --- | --- |
| From | ``` case Satisfiable ``` |
| To | ``` case satisfiable ``` |

Modified [NWPathStatus.satisfied](https://developer.apple.com/documentation/networkextension/nwpathstatus/satisfied)

|  | Declaration |
| --- | --- |
| From | ``` case Satisfied ``` |
| To | ``` case satisfied ``` |

Modified [NWPathStatus.unsatisfied](https://developer.apple.com/documentation/networkextension/nwpathstatus/nwpathstatusunsatisfied)

|  | Declaration |
| --- | --- |
| From | ``` case Unsatisfied ``` |
| To | ``` case unsatisfied ``` |

Modified [NWTCPConnection](https://developer.apple.com/documentation/networkextension/nwtcpconnection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NWTCPConnection : NSObject {     init(upgradeForConnection connection: NWTCPConnection)     var state: NWTCPConnectionState { get }     var viable: Bool { get }     var hasBetterPath: Bool { get }     var endpoint: NWEndpoint { get }     var connectedPath: NWPath? { get }     var localAddress: NWEndpoint? { get }     var remoteAddress: NWEndpoint? { get }     var txtRecord: NSData? { get }     var error: NSError? { get }     func cancel()     func readLength(_ length: Int, completionHandler completion: (NSData?, NSError?) -> Void)     func readMinimumLength(_ minimum: Int, maximumLength maximum: Int, completionHandler completion: (NSData?, NSError?) -> Void)     func write(_ data: NSData, completionHandler completion: (NSError?) -> Void)     func writeClose() } ``` | -- |
| To | ``` class NWTCPConnection : NSObject {     init(upgradeFor connection: NWTCPConnection)     var state: NWTCPConnectionState { get }     var isViable: Bool { get }     var hasBetterPath: Bool { get }     var endpoint: NWEndpoint { get }     var connectedPath: NWPath? { get }     var localAddress: NWEndpoint? { get }     var remoteAddress: NWEndpoint? { get }     var txtRecord: Data? { get }     var error: Error? { get }     func cancel()     func readLength(_ length: Int, completionHandler completion: @escaping (Data, Error?) -> Swift.Void)     func readMinimumLength(_ minimum: Int, maximumLength maximum: Int, completionHandler completion: @escaping (Data, Error?) -> Swift.Void)     func write(_ data: Data, completionHandler completion: @escaping (Error?) -> Swift.Void)     func writeClose()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NWTCPConnection : CVarArg { } extension NWTCPConnection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NWTCPConnection.error](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406126-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [NWTCPConnection.init(upgradeFor: NWTCPConnection)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406751-init)

|  | Declaration |
| --- | --- |
| From | ``` init(upgradeForConnection connection: NWTCPConnection) ``` |
| To | ``` init(upgradeFor connection: NWTCPConnection) ``` |

Modified [NWTCPConnection.isViable](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406292-isviable)

|  | Declaration |
| --- | --- |
| From | ``` var viable: Bool { get } ``` |
| To | ``` var isViable: Bool { get } ``` |

Modified [NWTCPConnection.readLength(_: Int, completionHandler: (Data, Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406652-readlength)

|  | Declaration |
| --- | --- |
| From | ``` func readLength(_ length: Int, completionHandler completion: (NSData?, NSError?) -> Void) ``` |
| To | ``` func readLength(_ length: Int, completionHandler completion: @escaping (Data, Error?) -> Swift.Void) ``` |

Modified [NWTCPConnection.readMinimumLength(_: Int, maximumLength: Int, completionHandler: (Data, Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406156-readminimumlength)

|  | Declaration |
| --- | --- |
| From | ``` func readMinimumLength(_ minimum: Int, maximumLength maximum: Int, completionHandler completion: (NSData?, NSError?) -> Void) ``` |
| To | ``` func readMinimumLength(_ minimum: Int, maximumLength maximum: Int, completionHandler completion: @escaping (Data, Error?) -> Swift.Void) ``` |

Modified [NWTCPConnection.txtRecord](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406547-txtrecord)

|  | Declaration |
| --- | --- |
| From | ``` var txtRecord: NSData? { get } ``` |
| To | ``` var txtRecord: Data? { get } ``` |

Modified [NWTCPConnection.write(_: Data, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnection/1406631-write)

|  | Declaration |
| --- | --- |
| From | ``` func write(_ data: NSData, completionHandler completion: (NSError?) -> Void) ``` |
| To | ``` func write(_ data: Data, completionHandler completion: @escaping (Error?) -> Swift.Void) ``` |

Modified [NWTCPConnectionAuthenticationDelegate](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NWTCPConnectionAuthenticationDelegate : NSObjectProtocol {     optional func shouldProvideIdentityForConnection(_ connection: NWTCPConnection) -> Bool     optional func provideIdentityForConnection(_ connection: NWTCPConnection, completionHandler completion: (SecIdentity, [AnyObject]) -> Void)     optional func shouldEvaluateTrustForConnection(_ connection: NWTCPConnection) -> Bool     optional func evaluateTrustForConnection(_ connection: NWTCPConnection, peerCertificateChain peerCertificateChain: [AnyObject], completionHandler completion: (SecTrust) -> Void) } ``` |
| To | ``` protocol NWTCPConnectionAuthenticationDelegate : NSObjectProtocol {     optional func shouldProvideIdentity(for connection: NWTCPConnection) -> Bool     optional func provideIdentity(for connection: NWTCPConnection, completionHandler completion: @escaping (SecIdentity, [Any]) -> Swift.Void)     optional func shouldEvaluateTrust(for connection: NWTCPConnection) -> Bool     optional func evaluateTrust(for connection: NWTCPConnection, peerCertificateChain peerCertificateChain: [Any], completionHandler completion: @escaping (SecTrust) -> Swift.Void) } ``` |

Modified [NWTCPConnectionAuthenticationDelegate.evaluateTrust(for: NWTCPConnection, peerCertificateChain: [Any], completionHandler: (SecTrust) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406024-evaluatetrustforconnection)

|  | Declaration |
| --- | --- |
| From | ``` optional func evaluateTrustForConnection(_ connection: NWTCPConnection, peerCertificateChain peerCertificateChain: [AnyObject], completionHandler completion: (SecTrust) -> Void) ``` |
| To | ``` optional func evaluateTrust(for connection: NWTCPConnection, peerCertificateChain peerCertificateChain: [Any], completionHandler completion: @escaping (SecTrust) -> Swift.Void) ``` |

Modified [NWTCPConnectionAuthenticationDelegate.provideIdentity(for: NWTCPConnection, completionHandler: (SecIdentity, [Any]) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406235-provideidentityforconnection)

|  | Declaration |
| --- | --- |
| From | ``` optional func provideIdentityForConnection(_ connection: NWTCPConnection, completionHandler completion: (SecIdentity, [AnyObject]) -> Void) ``` |
| To | ``` optional func provideIdentity(for connection: NWTCPConnection, completionHandler completion: @escaping (SecIdentity, [Any]) -> Swift.Void) ``` |

Modified [NWTCPConnectionAuthenticationDelegate.shouldEvaluateTrust(for: NWTCPConnection) -> Bool](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406116-shouldevaluatetrust)

|  | Declaration |
| --- | --- |
| From | ``` optional func shouldEvaluateTrustForConnection(_ connection: NWTCPConnection) -> Bool ``` |
| To | ``` optional func shouldEvaluateTrust(for connection: NWTCPConnection) -> Bool ``` |

Modified [NWTCPConnectionAuthenticationDelegate.shouldProvideIdentity(for: NWTCPConnection) -> Bool](https://developer.apple.com/documentation/networkextension/nwtcpconnectionauthenticationdelegate/1406689-shouldprovideidentity)

|  | Declaration |
| --- | --- |
| From | ``` optional func shouldProvideIdentityForConnection(_ connection: NWTCPConnection) -> Bool ``` |
| To | ``` optional func shouldProvideIdentity(for connection: NWTCPConnection) -> Bool ``` |

Modified [NWTCPConnectionState [enum]](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum NWTCPConnectionState : Int {     case Invalid     case Connecting     case Waiting     case Connected     case Disconnected     case Cancelled } ``` |
| To | ``` enum NWTCPConnectionState : Int {     case invalid     case connecting     case waiting     case connected     case disconnected     case cancelled } ``` |

Modified [NWTCPConnectionState.cancelled](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [NWTCPConnectionState.connected](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstateconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [NWTCPConnectionState.connecting](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstateconnecting)

|  | Declaration |
| --- | --- |
| From | ``` case Connecting ``` |
| To | ``` case connecting ``` |

Modified [NWTCPConnectionState.disconnected](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/nwtcpconnectionstatedisconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnected ``` |
| To | ``` case disconnected ``` |

Modified [NWTCPConnectionState.invalid](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [NWTCPConnectionState.waiting](https://developer.apple.com/documentation/networkextension/nwtcpconnectionstate/waiting)

|  | Declaration |
| --- | --- |
| From | ``` case Waiting ``` |
| To | ``` case waiting ``` |

Modified [NWTLSParameters](https://developer.apple.com/documentation/networkextension/nwtlsparameters)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NWTLSParameters : NSObject {     @NSCopying var TLSSessionID: NSData?     var SSLCipherSuites: Set<NSNumber>?     var minimumSSLProtocolVersion: Int     var maximumSSLProtocolVersion: Int } ``` | -- |
| To | ``` class NWTLSParameters : NSObject {     var tlsSessionID: Data?     var sslCipherSuites: Set<NSNumber>?     var minimumSSLProtocolVersion: Int     var maximumSSLProtocolVersion: Int     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NWTLSParameters : CVarArg { } extension NWTLSParameters : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NWTLSParameters.sslCipherSuites](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406533-sslciphersuites)

|  | Declaration |
| --- | --- |
| From | ``` var SSLCipherSuites: Set<NSNumber>? ``` |
| To | ``` var sslCipherSuites: Set<NSNumber>? ``` |

Modified [NWTLSParameters.tlsSessionID](https://developer.apple.com/documentation/networkextension/nwtlsparameters/1406569-tlssessionid)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var TLSSessionID: NSData? ``` |
| To | ``` var tlsSessionID: Data? ``` |

Modified [NWUDPSession](https://developer.apple.com/documentation/networkextension/nwudpsession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NWUDPSession : NSObject {     init(upgradeForSession session: NWUDPSession)     var state: NWUDPSessionState { get }     var endpoint: NWEndpoint { get }     var resolvedEndpoint: NWEndpoint? { get }     var viable: Bool { get }     var hasBetterPath: Bool { get }     var currentPath: NWPath? { get }     func tryNextResolvedEndpoint()     var maximumDatagramLength: Int { get }     func setReadHandler(_ handler: ([NSData]?, NSError?) -> Void, maxDatagrams maxDatagrams: Int)     func writeMultipleDatagrams(_ datagramArray: [NSData], completionHandler completionHandler: (NSError?) -> Void)     func writeDatagram(_ datagram: NSData, completionHandler completionHandler: (NSError?) -> Void)     func cancel() } ``` | -- |
| To | ``` class NWUDPSession : NSObject {     init(upgradeFor session: NWUDPSession)     var state: NWUDPSessionState { get }     var endpoint: NWEndpoint { get }     var resolvedEndpoint: NWEndpoint? { get }     var isViable: Bool { get }     var hasBetterPath: Bool { get }     var currentPath: NWPath? { get }     func tryNextResolvedEndpoint()     var maximumDatagramLength: Int { get }     func setReadHandler(_ handler: @escaping ([Data], Error?) -> Swift.Void, maxDatagrams maxDatagrams: Int)     func writeMultipleDatagrams(_ datagramArray: [Data], completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func writeDatagram(_ datagram: Data, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func cancel()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NWUDPSession : CVarArg { } extension NWUDPSession : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NWUDPSession.init(upgradeFor: NWUDPSession)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406905-initwithupgradeforsession)

|  | Declaration |
| --- | --- |
| From | ``` init(upgradeForSession session: NWUDPSession) ``` |
| To | ``` init(upgradeFor session: NWUDPSession) ``` |

Modified [NWUDPSession.isViable](https://developer.apple.com/documentation/networkextension/nwudpsession/1406357-viable)

|  | Declaration |
| --- | --- |
| From | ``` var viable: Bool { get } ``` |
| To | ``` var isViable: Bool { get } ``` |

Modified [NWUDPSession.setReadHandler(_: ([Data], Error?) -> Swift.Void, maxDatagrams: Int)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406772-setreadhandler)

|  | Declaration |
| --- | --- |
| From | ``` func setReadHandler(_ handler: ([NSData]?, NSError?) -> Void, maxDatagrams maxDatagrams: Int) ``` |
| To | ``` func setReadHandler(_ handler: @escaping ([Data], Error?) -> Swift.Void, maxDatagrams maxDatagrams: Int) ``` |

Modified [NWUDPSession.writeDatagram(_: Data, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406079-writedatagram)

|  | Declaration |
| --- | --- |
| From | ``` func writeDatagram(_ datagram: NSData, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func writeDatagram(_ datagram: Data, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NWUDPSession.writeMultipleDatagrams(_: [Data], completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/networkextension/nwudpsession/1406390-writemultipledatagrams)

|  | Declaration |
| --- | --- |
| From | ``` func writeMultipleDatagrams(_ datagramArray: [NSData], completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` func writeMultipleDatagrams(_ datagramArray: [Data], completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [NWUDPSessionState [enum]](https://developer.apple.com/documentation/networkextension/nwudpsessionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum NWUDPSessionState : Int {     case Invalid     case Waiting     case Preparing     case Ready     case Failed     case Cancelled } ``` |
| To | ``` enum NWUDPSessionState : Int {     case invalid     case waiting     case preparing     case ready     case failed     case cancelled } ``` |

Modified [NWUDPSessionState.cancelled](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [NWUDPSessionState.failed](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/failed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [NWUDPSessionState.invalid](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [NWUDPSessionState.preparing](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstatepreparing)

|  | Declaration |
| --- | --- |
| From | ``` case Preparing ``` |
| To | ``` case preparing ``` |

Modified [NWUDPSessionState.ready](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstateready)

|  | Declaration |
| --- | --- |
| From | ``` case Ready ``` |
| To | ``` case ready ``` |

Modified [NWUDPSessionState.waiting](https://developer.apple.com/documentation/networkextension/nwudpsessionstate/nwudpsessionstatewaiting)

|  | Declaration |
| --- | --- |
| From | ``` case Waiting ``` |
| To | ``` case waiting ``` |

Modified [NEHotspotHelperHandler](https://developer.apple.com/documentation/networkextension/nehotspothelperhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias NEHotspotHelperHandler = (NEHotspotHelperCommand) -> Void ``` |
| To | ``` typealias NEHotspotHelperHandler = (NEHotspotHelperCommand) -> Swift.Void ``` |

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
