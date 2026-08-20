---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/NetworkExtension.html
archived_at: '2026-07-18T02:51:46.896783Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# NetworkExtension Changes for Swift

### NetworkExtension

Added [NEAppProxyFlowError [struct]](https://developer.apple.com/documentation/networkextension/neappproxyflowerror)Added [NEAppProxyFlowError.aborted](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630680-aborted)Added [NEAppProxyFlowError.datagramTooLarge](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630692-datagramtoolarge)Added [NEAppProxyFlowError.hostUnreachable](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630671-hostunreachable)Added NEAppProxyFlowError.init(_nsError: NSError)Added [NEAppProxyFlowError.internal](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630668-internal)Added [NEAppProxyFlowError.invalidArgument](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630688-invalidargument)Added [NEAppProxyFlowError.notConnected](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630683-notconnected)Added [NEAppProxyFlowError.peerReset](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630673-peerreset)Added [NEAppProxyFlowError.readAlreadyPending](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630687-readalreadypending)Added [NEAppProxyFlowError.refused](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630672-refused)Added [NEAppProxyFlowError.timedOut](https://developer.apple.com/documentation/networkextension/neappproxyflowerror/2630678-timedout)Added [NETunnelProviderError [struct]](https://developer.apple.com/documentation/networkextension/netunnelprovidererror)Added NETunnelProviderError.init(_nsError: NSError)Added [NETunnelProviderError.networkSettingsCanceled](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/2630686-networksettingscanceled)Added [NETunnelProviderError.networkSettingsFailed](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/2630669-networksettingsfailed)Added [NETunnelProviderError.networkSettingsInvalid](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/2630685-networksettingsinvalid)Added [NEVPNError [struct]](https://developer.apple.com/documentation/networkextension/nevpnerror)Added [NEVPNError.configurationDisabled](https://developer.apple.com/documentation/networkextension/nevpnerror/2630690-configurationdisabled)Added [NEVPNError.configurationInvalid](https://developer.apple.com/documentation/networkextension/nevpnerror/2630682-configurationinvalid)Added [NEVPNError.configurationReadWriteFailed](https://developer.apple.com/documentation/networkextension/nevpnerror/2630681-configurationreadwritefailed)Added [NEVPNError.configurationStale](https://developer.apple.com/documentation/networkextension/nevpnerror/2630670-configurationstale)Added [NEVPNError.configurationUnknown](https://developer.apple.com/documentation/networkextension/nevpnerror/2630674-configurationunknown)Added [NEVPNError.connectionFailed](https://developer.apple.com/documentation/networkextension/nevpnerror/2630676-connectionfailed)Added NEVPNError.init(_nsError: NSError)Modified [NEAppProxyFlowError.Code [enum]](https://developer.apple.com/documentation/networkextension/neappproxyflowerror)

|  | Declaration |
| --- | --- |
| From | ``` enum NEAppProxyErrorDomain : Int {     case notConnected     case peerReset     case hostUnreachable     case invalidArgument     case aborted     case refused     case timedOut     case `internal`     case datagramTooLarge     case readAlreadyPending } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = NEAppProxyFlowError         case notConnected         case peerReset         case hostUnreachable         case invalidArgument         case aborted         case refused         case timedOut         case `internal`         case datagramTooLarge         case readAlreadyPending     } ``` |

Modified [NETunnelProvider](https://developer.apple.com/documentation/networkextension/netunnelprovider)

|  | Declaration |
| --- | --- |
| From | ``` class NETunnelProvider : NEProvider {     func handleAppMessage(_ messageData: Data, completionHandler completionHandler: (@escaping (Data?) -> Swift.Void)? = nil)     func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     var protocolConfiguration: NEVPNProtocol { get }     var appRules: [NEAppRule]? { get }     var routingMethod: NETunnelProviderRoutingMethod { get }     var reasserting: Bool } ``` |
| To | ``` class NETunnelProvider : NEProvider {     func handleAppMessage(_ messageData: Data, completionHandler completionHandler: ((Data?) -> Swift.Void)? = nil)     func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     var protocolConfiguration: NEVPNProtocol { get }     var appRules: [NEAppRule]? { get }     var routingMethod: NETunnelProviderRoutingMethod { get }     var reasserting: Bool } ``` |

Modified [NETunnelProvider.handleAppMessage(_: Data, completionHandler: ((Data?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406545-handleappmessage)

|  | Declaration |
| --- | --- |
| From | ``` func handleAppMessage(_ messageData: Data, completionHandler completionHandler: (@escaping (Data?) -> Swift.Void)? = nil) ``` |
| To | ``` func handleAppMessage(_ messageData: Data, completionHandler completionHandler: ((Data?) -> Swift.Void)? = nil) ``` |

Modified [NETunnelProvider.setTunnelNetworkSettings(_: NETunnelNetworkSettings?, completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/netunnelprovider/1406539-settunnelnetworksettings)

|  | Declaration |
| --- | --- |
| From | ``` func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func setTunnelNetworkSettings(_ tunnelNetworkSettings: NETunnelNetworkSettings?, completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

Modified [NETunnelProviderError.Code [enum]](https://developer.apple.com/documentation/networkextension/netunnelprovidererror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum NETunnelProviderErrorDomain : Int {     case networkSettingsInvalid     case networkSettingsCanceled     case networkSettingsFailed } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = NETunnelProviderError         case networkSettingsInvalid         case networkSettingsCanceled         case networkSettingsFailed     } ``` |

Modified [NETunnelProviderSession](https://developer.apple.com/documentation/networkextension/netunnelprovidersession)

|  | Declaration |
| --- | --- |
| From | ``` class NETunnelProviderSession : NEVPNConnection {     func startTunnel(options options: [String : Any]? = nil) throws     func stopTunnel()     func sendProviderMessage(_ messageData: Data, responseHandler responseHandler: (@escaping (Data?) -> Swift.Void)? = nil) throws } ``` |
| To | ``` class NETunnelProviderSession : NEVPNConnection {     func startTunnel(options options: [String : Any]? = nil) throws     func stopTunnel()     func sendProviderMessage(_ messageData: Data, responseHandler responseHandler: ((Data?) -> Swift.Void)? = nil) throws } ``` |

Modified [NETunnelProviderSession.sendProviderMessage(_: Data, responseHandler: ((Data?) -> Swift.Void)?) throws](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/1406409-sendprovidermessage)

|  | Declaration |
| --- | --- |
| From | ``` func sendProviderMessage(_ messageData: Data, responseHandler responseHandler: (@escaping (Data?) -> Swift.Void)? = nil) throws ``` |
| To | ``` func sendProviderMessage(_ messageData: Data, responseHandler responseHandler: ((Data?) -> Swift.Void)? = nil) throws ``` |

Modified [NEVPNError.Code [enum]](https://developer.apple.com/documentation/networkextension/nevpnerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNErrorDomain : Int {     case configurationInvalid     case configurationDisabled     case connectionFailed     case configurationStale     case configurationReadWriteFailed     case configurationUnknown } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = NEVPNError         case configurationInvalid         case configurationDisabled         case connectionFailed         case configurationStale         case configurationReadWriteFailed         case configurationUnknown     } ``` |

Modified [NEVPNManager](https://developer.apple.com/documentation/networkextension/nevpnmanager)

|  | Declaration |
| --- | --- |
| From | ``` class NEVPNManager : NSObject {     class func shared() -> NEVPNManager     func loadFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func removeFromPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func saveToPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func setAuthorization(_ authorization: AuthorizationRef)     var onDemandRules: [NEOnDemandRule]?     var isOnDemandEnabled: Bool     var localizedDescription: String?     var `protocol`: NEVPNProtocol?     var protocolConfiguration: NEVPNProtocol?     var connection: NEVPNConnection { get }     var isEnabled: Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEVPNManager : CVarArg { } extension NEVPNManager : Equatable, Hashable {     var hashValue: Int { get } } ``` |
| To | ``` class NEVPNManager : NSObject {     class func shared() -> NEVPNManager     func loadFromPreferences(completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     func removeFromPreferences(completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func saveToPreferences(completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil)     func setAuthorization(_ authorization: AuthorizationRef)     var onDemandRules: [NEOnDemandRule]?     var isOnDemandEnabled: Bool     var localizedDescription: String?     var `protocol`: NEVPNProtocol?     var protocolConfiguration: NEVPNProtocol?     var connection: NEVPNConnection { get }     var isEnabled: Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NEVPNManager : CVarArg { } extension NEVPNManager : Equatable, Hashable {     var hashValue: Int { get } } ``` |

Modified [NEVPNManager.removeFromPreferences(completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1406202-removefrompreferenceswithcomplet)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func removeFromPreferences(completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

Modified [NEVPNManager.saveToPreferences(completionHandler: ((Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/networkextension/nevpnmanager/1405985-savetopreferenceswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` func saveToPreferences(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |
| To | ``` func saveToPreferences(completionHandler completionHandler: ((Error?) -> Swift.Void)? = nil) ``` |

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
