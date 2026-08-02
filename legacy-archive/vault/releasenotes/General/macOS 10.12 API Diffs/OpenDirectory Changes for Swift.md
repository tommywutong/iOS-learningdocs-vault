---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/OpenDirectory.html
archived_at: '2026-07-18T02:51:31.875804Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# OpenDirectory Changes for Swift

### OpenDirectory

Modified [ODAttributeMap](https://developer.apple.com/documentation/opendirectory/odattributemap)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODAttributeMap : NSObject {     var customQueryFunction: String!     var customTranslationFunction: String!     var customAttributes: [AnyObject]!     var value: String!     convenience init!(value value: String!)     class func attributeMapWithValue(_ value: String!) -> Self!     convenience init!(staticValue staticValue: String!)     class func attributeMapWithStaticValue(_ staticValue: String!) -> Self!     func setStaticValue(_ staticValue: String!)     func setVariableSubstitution(_ variableSubstitution: String!) } ``` | -- |
| To | ``` class ODAttributeMap : NSObject {     var customQueryFunction: String!     var customTranslationFunction: String!     var customAttributes: [Any]!     var value: String!     convenience init!(value value: String!)     class func withValue(_ value: String!) -> Self!     convenience init!(staticValue staticValue: String!)     class func withStaticValue(_ staticValue: String!) -> Self!     func setStaticValue(_ staticValue: String!)     func setVariableSubstitution(_ variableSubstitution: String!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODAttributeMap : CVarArg { } extension ODAttributeMap : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODAttributeMap.customAttributes](https://developer.apple.com/documentation/opendirectory/odattributemap/1427255-customattributes)

|  | Declaration |
| --- | --- |
| From | ``` var customAttributes: [AnyObject]! ``` |
| To | ``` var customAttributes: [Any]! ``` |

Modified [ODConfiguration](https://developer.apple.com/documentation/opendirectory/odconfiguration)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODConfiguration : NSObject {     var nodeName: String!     var comment: String!     var defaultMappings: ODMappings!     var templateName: String!     var virtualSubnodes: [AnyObject]!     var hideRegistration: Bool     var preferredDestinationHostName: String!     var preferredDestinationHostPort: UInt16     var trustAccount: String! { get }     var trustMetaAccount: String! { get }     var trustKerberosPrincipal: String! { get }     var trustType: String! { get }     var trustUsesMutualAuthentication: Bool { get }     var trustUsesKerberosKeytab: Bool { get }     var trustUsesSystemKeychain: Bool { get }     var packetSigning: Int     var packetEncryption: Int     var manInTheMiddleProtection: Bool     var queryTimeoutInSeconds: Int     var connectionSetupTimeoutInSeconds: Int     var connectionIdleTimeoutInSeconds: Int     var defaultModuleEntries: [AnyObject]!     var authenticationModuleEntries: [AnyObject]!     var discoveryModuleEntries: [AnyObject]!     var generalModuleEntries: [AnyObject]!     convenience init!()     class func configuration() -> Self!     class func suggestedTrustAccount(_ hostname: String!) -> String!     class func suggestedTrustPassword(_ length: Int) -> String!     func saveUsingAuthorization(_ authorization: SFAuthorization!) throws     func addTrustType(_ trustType: String!, trustAccount account: String!, trustPassword accountPassword: String!, username username: String!, password password: String!, joinExisting join: Bool) throws     func removeTrustUsingUsername(_ username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool) throws } ``` | -- |
| To | ``` class ODConfiguration : NSObject {     var nodeName: String!     var comment: String!     var defaultMappings: ODMappings!     var templateName: String!     var virtualSubnodes: [Any]!     var hideRegistration: Bool     var preferredDestinationHostName: String!     var preferredDestinationHostPort: UInt16     var trustAccount: String! { get }     var trustMetaAccount: String! { get }     var trustKerberosPrincipal: String! { get }     var trustType: String! { get }     var trustUsesMutualAuthentication: Bool { get }     var trustUsesKerberosKeytab: Bool { get }     var trustUsesSystemKeychain: Bool { get }     var packetSigning: Int     var packetEncryption: Int     var manInTheMiddleProtection: Bool     var queryTimeoutInSeconds: Int     var connectionSetupTimeoutInSeconds: Int     var connectionIdleTimeoutInSeconds: Int     var defaultModuleEntries: [Any]!     var authenticationModuleEntries: [Any]!     var discoveryModuleEntries: [Any]!     var generalModuleEntries: [Any]!     convenience init!()     class func configuration() -> Self!     class func suggestedTrustAccount(_ hostname: String!) -> String!     class func suggestedTrustPassword(_ length: Int) -> String!     func save(using authorization: SFAuthorization!) throws     func addTrustType(_ trustType: String!, trustAccount account: String!, trustPassword accountPassword: String!, username username: String!, password password: String!, joinExisting join: Bool) throws     func removeTrust(usingUsername username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool) throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODConfiguration : CVarArg { } extension ODConfiguration : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODConfiguration.authenticationModuleEntries](https://developer.apple.com/documentation/opendirectory/odconfiguration/1428041-authenticationmoduleentries)

|  | Declaration |
| --- | --- |
| From | ``` var authenticationModuleEntries: [AnyObject]! ``` |
| To | ``` var authenticationModuleEntries: [Any]! ``` |

Modified [ODConfiguration.defaultModuleEntries](https://developer.apple.com/documentation/opendirectory/odconfiguration/1427619-defaultmoduleentries)

|  | Declaration |
| --- | --- |
| From | ``` var defaultModuleEntries: [AnyObject]! ``` |
| To | ``` var defaultModuleEntries: [Any]! ``` |

Modified [ODConfiguration.discoveryModuleEntries](https://developer.apple.com/documentation/opendirectory/odconfiguration/1427330-discoverymoduleentries)

|  | Declaration |
| --- | --- |
| From | ``` var discoveryModuleEntries: [AnyObject]! ``` |
| To | ``` var discoveryModuleEntries: [Any]! ``` |

Modified [ODConfiguration.generalModuleEntries](https://developer.apple.com/documentation/opendirectory/odconfiguration/1428200-generalmoduleentries)

|  | Declaration |
| --- | --- |
| From | ``` var generalModuleEntries: [AnyObject]! ``` |
| To | ``` var generalModuleEntries: [Any]! ``` |

Modified [ODConfiguration.removeTrust(usingUsername: String!, password: String!, deleteTrustAccount: Bool) throws](https://developer.apple.com/documentation/opendirectory/odconfiguration/1426928-removetrust)

|  | Declaration |
| --- | --- |
| From | ``` func removeTrustUsingUsername(_ username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool) throws ``` |
| To | ``` func removeTrust(usingUsername username: String!, password password: String!, deleteTrustAccount deleteAccount: Bool) throws ``` |

Modified [ODConfiguration.save(using: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odconfiguration/1427633-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveUsingAuthorization(_ authorization: SFAuthorization!) throws ``` |
| To | ``` func save(using authorization: SFAuthorization!) throws ``` |

Modified [ODConfiguration.virtualSubnodes](https://developer.apple.com/documentation/opendirectory/odconfiguration/1427275-virtualsubnodes)

|  | Declaration |
| --- | --- |
| From | ``` var virtualSubnodes: [AnyObject]! ``` |
| To | ``` var virtualSubnodes: [Any]! ``` |

Modified [ODMappings](https://developer.apple.com/documentation/opendirectory/odmappings)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODMappings : NSObject {     var comment: String!     var templateName: String!     var identifier: String!     var recordTypes: [AnyObject]! { get }     var function: String!     var functionAttributes: [AnyObject]!     convenience init!()     class func mappings() -> Self!     func recordMapForStandardRecordType(_ stdType: String!) -> ODRecordMap!     func setRecordMap(_ map: ODRecordMap!, forStandardRecordType stdType: String!) } ``` | -- |
| To | ``` class ODMappings : NSObject {     var comment: String!     var templateName: String!     var identifier: String!     var recordTypes: [Any]! { get }     var function: String!     var functionAttributes: [Any]!     convenience init!()     class func mappings() -> Self!     func recordMap(forStandardRecordType stdType: String!) -> ODRecordMap!     func setRecordMap(_ map: ODRecordMap!, forStandardRecordType stdType: String!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODMappings : CVarArg { } extension ODMappings : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODMappings.functionAttributes](https://developer.apple.com/documentation/opendirectory/odmappings/1427859-functionattributes)

|  | Declaration |
| --- | --- |
| From | ``` var functionAttributes: [AnyObject]! ``` |
| To | ``` var functionAttributes: [Any]! ``` |

Modified [ODMappings.recordMap(forStandardRecordType: String!) -> ODRecordMap!](https://developer.apple.com/documentation/opendirectory/odmappings/1428100-recordmap)

|  | Declaration |
| --- | --- |
| From | ``` func recordMapForStandardRecordType(_ stdType: String!) -> ODRecordMap! ``` |
| To | ``` func recordMap(forStandardRecordType stdType: String!) -> ODRecordMap! ``` |

Modified [ODMappings.recordTypes](https://developer.apple.com/documentation/opendirectory/odmappings/1427905-recordtypes)

|  | Declaration |
| --- | --- |
| From | ``` var recordTypes: [AnyObject]! { get } ``` |
| To | ``` var recordTypes: [Any]! { get } ``` |

Modified [ODModuleEntry](https://developer.apple.com/documentation/opendirectory/odmoduleentry)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODModuleEntry : NSObject {     var mappings: ODMappings!     var supportedOptions: [AnyObject]! { get }     var name: String!     var xpcServiceName: String!     var uuidString: String!     convenience init!(name name: String!, xpcServiceName xpcServiceName: String!)     class func moduleEntryWithName(_ name: String!, xpcServiceName xpcServiceName: String!) -> Self!     func setOption(_ optionName: String!, value value: AnyObject!)     func option(_ optionName: String!) -> AnyObject! } ``` | -- |
| To | ``` class ODModuleEntry : NSObject {     var mappings: ODMappings!     var supportedOptions: [Any]! { get }     var name: String!     var xpcServiceName: String!     var uuidString: String!     convenience init!(name name: String!, xpcServiceName xpcServiceName: String!)     class func withName(_ name: String!, xpcServiceName xpcServiceName: String!) -> Self!     func setOption(_ optionName: String!, value value: Any!)     func option(_ optionName: String!) -> Any!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODModuleEntry : CVarArg { } extension ODModuleEntry : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODModuleEntry.option(_: String!) -> Any!](https://developer.apple.com/documentation/opendirectory/odmoduleentry/1428094-option)

|  | Declaration |
| --- | --- |
| From | ``` func option(_ optionName: String!) -> AnyObject! ``` |
| To | ``` func option(_ optionName: String!) -> Any! ``` |

Modified [ODModuleEntry.setOption(_: String!, value: Any!)](https://developer.apple.com/documentation/opendirectory/odmoduleentry/1427280-setoption)

|  | Declaration |
| --- | --- |
| From | ``` func setOption(_ optionName: String!, value value: AnyObject!) ``` |
| To | ``` func setOption(_ optionName: String!, value value: Any!) ``` |

Modified [ODModuleEntry.supportedOptions](https://developer.apple.com/documentation/opendirectory/odmoduleentry/1426926-supportedoptions)

|  | Declaration |
| --- | --- |
| From | ``` var supportedOptions: [AnyObject]! { get } ``` |
| To | ``` var supportedOptions: [Any]! { get } ``` |

Modified [ODNode](https://developer.apple.com/documentation/opendirectory/odnode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODNode : NSObject {     convenience init(session inSession: ODSession!, type inType: ODNodeType) throws     class func nodeWithSession(_ inSession: ODSession!, type inType: ODNodeType) throws -> Self     convenience init(session inSession: ODSession!, name inName: String!) throws     class func nodeWithSession(_ inSession: ODSession!, name inName: String!) throws -> Self     init(session inSession: ODSession!, type inType: ODNodeType) throws     init(session inSession: ODSession!, name inName: String!) throws     func subnodeNames() throws -> [AnyObject]     func unreachableSubnodeNames() throws -> [AnyObject]     var nodeName: String! { get }     func nodeDetailsForKeys(_ inKeys: [AnyObject]!) throws -> [NSObject : AnyObject]     func supportedRecordTypes() throws -> [AnyObject]     func supportedAttributesForRecordType(_ inRecordType: String!) throws -> [AnyObject]     func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!) throws     func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws     func setCredentialsUsingKerberosCache(_ inCacheName: String!) throws     func createRecordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: [NSObject : AnyObject]!) throws -> ODRecord     func recordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: AnyObject!) throws -> ODRecord     func customCall(_ inCustomCode: Int, sendData inSendData: NSData!) throws -> NSData     func customFunction(_ function: String!, payload payload: AnyObject!) throws -> AnyObject     var configuration: ODConfiguration! { get }     func policies() throws -> [NSObject : AnyObject]     func supportedPolicies() throws -> [NSObject : AnyObject]     func setPolicies(_ policies: [NSObject : AnyObject]!) throws     func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws     func removePolicy(_ policy: ODPolicyType!) throws     func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws     func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws     func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws     func accountPolicies() throws -> [NSObject : AnyObject]     func passwordContentCheck(_ password: String!, forRecordName recordName: String!) throws } ``` | -- |
| To | ``` class ODNode : NSObject {     convenience init(session inSession: ODSession!, type inType: ODNodeType) throws     class func withSession(_ inSession: ODSession!, type inType: ODNodeType) throws -> Self     convenience init(session inSession: ODSession!, name inName: String!) throws     class func withSession(_ inSession: ODSession!, name inName: String!) throws -> Self     init(session inSession: ODSession!, type inType: ODNodeType) throws     init(session inSession: ODSession!, name inName: String!) throws     func subnodeNames() throws -> [Any]     func unreachableSubnodeNames() throws -> [Any]     var nodeName: String! { get }     func nodeDetails(forKeys inKeys: [Any]!) throws -> [AnyHashable : Any]     func supportedRecordTypes() throws -> [Any]     func supportedAttributes(forRecordType inRecordType: String!) throws -> [Any]     func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!) throws     func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws     func setCredentialsUsingKerberosCache(_ inCacheName: String!) throws     func createRecord(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: [AnyHashable : Any]! = [:]) throws -> ODRecord     func record(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: Any!) throws -> ODRecord     func customCall(_ inCustomCode: Int, send inSendData: Data!) throws -> Data     func customFunction(_ function: String!, payload payload: Any!) throws -> Any     var configuration: ODConfiguration! { get }     func policies() throws -> [AnyHashable : Any]     func supportedPolicies() throws -> [AnyHashable : Any]     func setPolicies(_ policies: [AnyHashable : Any]!) throws     func setPolicy(_ policy: String!, value value: Any!) throws     func removePolicy(_ policy: String!) throws     func addAccountPolicy(_ policy: [AnyHashable : Any]!, toCategory category: String!) throws     func removeAccountPolicy(_ policy: [AnyHashable : Any]!, fromCategory category: String!) throws     func setAccountPolicies(_ policies: [AnyHashable : Any]!) throws     func accountPolicies() throws -> [AnyHashable : Any]     func passwordContentCheck(_ password: String!, forRecordName recordName: String!) throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODNode : CVarArg { } extension ODNode : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODNode.accountPolicies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odnode/1428081-accountpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func accountPolicies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func accountPolicies() throws -> [AnyHashable : Any] ``` |

Modified [ODNode.addAccountPolicy(_: [AnyHashable : Any]!, toCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427951-addaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws ``` |
| To | ``` func addAccountPolicy(_ policy: [AnyHashable : Any]!, toCategory category: String!) throws ``` |

Modified [ODNode.createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](https://developer.apple.com/documentation/opendirectory/odnode/1427031-createrecordwithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func createRecordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: [NSObject : AnyObject]!) throws -> ODRecord ``` |
| To | ``` func createRecord(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: [AnyHashable : Any]! = [:]) throws -> ODRecord ``` |

Modified [ODNode.customCall(_: Int, send: Data!) throws -> Data](https://developer.apple.com/documentation/opendirectory/odnode/1427478-customcall)

|  | Declaration |
| --- | --- |
| From | ``` func customCall(_ inCustomCode: Int, sendData inSendData: NSData!) throws -> NSData ``` |
| To | ``` func customCall(_ inCustomCode: Int, send inSendData: Data!) throws -> Data ``` |

Modified [ODNode.customFunction(_: String!, payload: Any!) throws -> Any](https://developer.apple.com/documentation/opendirectory/odnode/1427071-customfunction)

|  | Declaration |
| --- | --- |
| From | ``` func customFunction(_ function: String!, payload payload: AnyObject!) throws -> AnyObject ``` |
| To | ``` func customFunction(_ function: String!, payload payload: Any!) throws -> Any ``` |

Modified [ODNode.nodeDetails(forKeys: [Any]!) throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odnode/1427177-nodedetailsforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func nodeDetailsForKeys(_ inKeys: [AnyObject]!) throws -> [NSObject : AnyObject] ``` |
| To | ``` func nodeDetails(forKeys inKeys: [Any]!) throws -> [AnyHashable : Any] ``` |

Modified [ODNode.policies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odnode/1428217-policies)

|  | Declaration |
| --- | --- |
| From | ``` func policies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func policies() throws -> [AnyHashable : Any] ``` |

Modified [ODNode.record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](https://developer.apple.com/documentation/opendirectory/odnode/1428065-record)

|  | Declaration |
| --- | --- |
| From | ``` func recordWithRecordType(_ inRecordType: String!, name inRecordName: String!, attributes inAttributes: AnyObject!) throws -> ODRecord ``` |
| To | ``` func record(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: Any!) throws -> ODRecord ``` |

Modified [ODNode.removeAccountPolicy(_: [AnyHashable : Any]!, fromCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427267-removeaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws ``` |
| To | ``` func removeAccountPolicy(_ policy: [AnyHashable : Any]!, fromCategory category: String!) throws ``` |

Modified [ODNode.removePolicy(_: String!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1427245-removepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removePolicy(_ policy: ODPolicyType!) throws ``` |
| To | ``` func removePolicy(_ policy: String!) throws ``` |

Modified [ODNode.setAccountPolicies(_: [AnyHashable : Any]!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1426999-setaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |
| To | ``` func setAccountPolicies(_ policies: [AnyHashable : Any]!) throws ``` |

Modified [ODNode.setCredentialsWithRecordType(_: String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1426987-setcredentialswithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws ``` |
| To | ``` func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws ``` |

Modified [ODNode.setPolicies(_: [AnyHashable : Any]!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1426946-setpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |
| To | ``` func setPolicies(_ policies: [AnyHashable : Any]!) throws ``` |

Modified [ODNode.setPolicy(_: String!, value: Any!) throws](https://developer.apple.com/documentation/opendirectory/odnode/1428225-setpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws ``` |
| To | ``` func setPolicy(_ policy: String!, value value: Any!) throws ``` |

Modified [ODNode.subnodeNames() throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odnode/1428155-subnodenamesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func subnodeNames() throws -> [AnyObject] ``` |
| To | ``` func subnodeNames() throws -> [Any] ``` |

Modified [ODNode.supportedAttributes(forRecordType: String!) throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odnode/1428017-supportedattributes)

|  | Declaration |
| --- | --- |
| From | ``` func supportedAttributesForRecordType(_ inRecordType: String!) throws -> [AnyObject] ``` |
| To | ``` func supportedAttributes(forRecordType inRecordType: String!) throws -> [Any] ``` |

Modified [ODNode.supportedPolicies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odnode/1428033-supportedpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func supportedPolicies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func supportedPolicies() throws -> [AnyHashable : Any] ``` |

Modified [ODNode.supportedRecordTypes() throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odnode/1427314-supportedrecordtypes)

|  | Declaration |
| --- | --- |
| From | ``` func supportedRecordTypes() throws -> [AnyObject] ``` |
| To | ``` func supportedRecordTypes() throws -> [Any] ``` |

Modified [ODNode.unreachableSubnodeNames() throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odnode/1427251-unreachablesubnodenamesandreturn)

|  | Declaration |
| --- | --- |
| From | ``` func unreachableSubnodeNames() throws -> [AnyObject] ``` |
| To | ``` func unreachableSubnodeNames() throws -> [Any] ``` |

Modified [ODQuery](https://developer.apple.com/documentation/opendirectory/odquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODQuery : NSObject, NSCopying {      init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws     class func queryWithNode(_ inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws -> ODQuery     init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws     func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [AnyObject]     unowned(unsafe) var delegate: ODQueryDelegate!     func scheduleInRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!)     func removeFromRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!)     func synchronize()     var operationQueue: NSOperationQueue! } ``` | NSCopying |
| To | ``` class ODQuery : NSObject, NSCopying {      init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: Any!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: Any!, returnAttributes inReturnAttributeOrList: Any!, maximumResults inMaximumResults: Int) throws     class func withNode(_ inNode: ODNode!, forRecordTypes inRecordTypeOrList: Any!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: Any!, returnAttributes inReturnAttributeOrList: Any!, maximumResults inMaximumResults: Int) throws -> ODQuery     init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: Any!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: Any!, returnAttributes inReturnAttributeOrList: Any!, maximumResults inMaximumResults: Int) throws     func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [Any]     unowned(unsafe) var delegate: ODQueryDelegate!     func schedule(in inRunLoop: RunLoop!, forMode inMode: String!)     func remove(from inRunLoop: RunLoop!, forMode inMode: String!)     func synchronize()     var operationQueue: OperationQueue!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODQuery : CVarArg { } extension ODQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [ODQuery.init(node: ODNode!, forRecordTypes: Any!, attribute: String!, matchType: ODMatchType, queryValues: Any!, returnAttributes: Any!, maximumResults: Int) throws](https://developer.apple.com/documentation/opendirectory/odquery/1391711-init)

|  | Declaration |
| --- | --- |
| From | ``` init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: AnyObject!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: AnyObject!, returnAttributes inReturnAttributeOrList: AnyObject!, maximumResults inMaximumResults: Int) throws ``` |
| To | ``` init(node inNode: ODNode!, forRecordTypes inRecordTypeOrList: Any!, attribute inAttribute: String!, matchType inMatchType: ODMatchType, queryValues inQueryValueOrList: Any!, returnAttributes inReturnAttributeOrList: Any!, maximumResults inMaximumResults: Int) throws ``` |

Modified [ODQuery.operationQueue](https://developer.apple.com/documentation/opendirectory/odquery/1391696-operationqueue)

|  | Declaration |
| --- | --- |
| From | ``` var operationQueue: NSOperationQueue! ``` |
| To | ``` var operationQueue: OperationQueue! ``` |

Modified [ODQuery.remove(from: RunLoop!, forMode: String!)](https://developer.apple.com/documentation/opendirectory/odquery/1391695-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!) ``` |
| To | ``` func remove(from inRunLoop: RunLoop!, forMode inMode: String!) ``` |

Modified [ODQuery.resultsAllowingPartial(_: Bool) throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odquery/1391702-resultsallowingpartial)

|  | Declaration |
| --- | --- |
| From | ``` func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [AnyObject] ``` |
| To | ``` func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [Any] ``` |

Modified [ODQuery.schedule(in: RunLoop!, forMode: String!)](https://developer.apple.com/documentation/opendirectory/odquery/1391698-schedule)

|  | Declaration |
| --- | --- |
| From | ``` func scheduleInRunLoop(_ inRunLoop: NSRunLoop!, forMode inMode: String!) ``` |
| To | ``` func schedule(in inRunLoop: RunLoop!, forMode inMode: String!) ``` |

Modified [ODQueryDelegate](https://developer.apple.com/documentation/opendirectory/odquerydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol ODQueryDelegate : NSObjectProtocol {     func query(_ inQuery: ODQuery!, foundResults inResults: [AnyObject]!, error inError: NSError!) } ``` |
| To | ``` protocol ODQueryDelegate : NSObjectProtocol {     func query(_ inQuery: ODQuery!, foundResults inResults: [Any]!, error inError: Error!) } ``` |

Modified [ODQueryDelegate.query(_: ODQuery!, foundResults: [Any]!, error: Error!)](https://developer.apple.com/documentation/opendirectory/odquerydelegate/1391704-query)

|  | Declaration |
| --- | --- |
| From | ``` func query(_ inQuery: ODQuery!, foundResults inResults: [AnyObject]!, error inError: NSError!) ``` |
| To | ``` func query(_ inQuery: ODQuery!, foundResults inResults: [Any]!, error inError: Error!) ``` |

Modified [ODRecord](https://developer.apple.com/documentation/opendirectory/odrecord)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODRecord : NSObject {     func setNodeCredentials(_ inUsername: String!, password inPassword: String!) throws     func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws     func setNodeCredentialsUsingKerberosCache(_ inCacheName: String!) throws     func passwordPolicy() throws -> [NSObject : AnyObject]     func verifyPassword(_ inPassword: String!) throws     func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws     func changePassword(_ oldPassword: String!, toPassword newPassword: String!) throws     func synchronize() throws     var recordType: String! { get }     var recordName: String! { get }     func recordDetailsForAttributes(_ inAttributes: [AnyObject]!) throws -> [NSObject : AnyObject]     func valuesForAttribute(_ inAttribute: String!) throws -> [AnyObject]     func setValue(_ inValueOrValues: AnyObject!, forAttribute inAttribute: String!) throws     func removeValuesForAttribute(_ inAttribute: String!) throws     func addValue(_ inValue: AnyObject!, toAttribute inAttribute: String!) throws     func removeValue(_ inValue: AnyObject!, fromAttribute inAttribute: String!) throws     func deleteRecord() throws     func policies() throws -> [NSObject : AnyObject]     func effectivePolicies() throws -> [NSObject : AnyObject]     func supportedPolicies() throws -> [NSObject : AnyObject]     func setPolicies(_ policies: [NSObject : AnyObject]!) throws     func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws     func removePolicy(_ policy: ODPolicyType!) throws     func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws     func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws     func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws     func accountPolicies() throws -> [NSObject : AnyObject]     func authenticationAllowed() throws     func passwordChangeAllowed(_ newPassword: String!) throws     func willPasswordExpire(_ willExpireIn: UInt64) -> Bool     func willAuthenticationsExpire(_ willExpireIn: UInt64) -> Bool     var secondsUntilPasswordExpires: Int64 { get }     var secondsUntilAuthenticationsExpire: Int64 { get } } extension ODRecord {     func addMemberRecord(_ inRecord: ODRecord!) throws     func removeMemberRecord(_ inRecord: ODRecord!) throws     func isMemberRecord(_ inRecord: ODRecord!) throws } ``` | -- |
| To | ``` class ODRecord : NSObject {     func setNodeCredentials(_ inUsername: String!, password inPassword: String!) throws     func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws     func setNodeCredentialsUsingKerberosCache(_ inCacheName: String!) throws     func passwordPolicy() throws -> [AnyHashable : Any]     func verifyPassword(_ inPassword: String!) throws     func verifyExtended(withAuthenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws     func changePassword(_ oldPassword: String!, toPassword newPassword: String!) throws     func synchronize() throws     var recordType: String! { get }     var recordName: String! { get }     func recordDetails(forAttributes inAttributes: [Any]!) throws -> [AnyHashable : Any]     func values(forAttribute inAttribute: String!) throws -> [Any]     func setValue(_ inValueOrValues: Any!, forAttribute inAttribute: String!) throws     func removeValues(forAttribute inAttribute: String!) throws     func addValue(_ inValue: Any!, toAttribute inAttribute: String!) throws     func removeValue(_ inValue: Any!, fromAttribute inAttribute: String!) throws     func delete() throws     func policies() throws -> [AnyHashable : Any]     func effectivePolicies() throws -> [AnyHashable : Any]     func supportedPolicies() throws -> [AnyHashable : Any]     func setPolicies(_ policies: [AnyHashable : Any]!) throws     func setPolicy(_ policy: String!, value value: Any!) throws     func removePolicy(_ policy: String!) throws     func addAccountPolicy(_ policy: [AnyHashable : Any]!, toCategory category: String!) throws     func removeAccountPolicy(_ policy: [AnyHashable : Any]!, fromCategory category: String!) throws     func setAccountPolicies(_ policies: [AnyHashable : Any]!) throws     func accountPolicies() throws -> [AnyHashable : Any]     func authenticationAllowed() throws     func passwordChangeAllowed(_ newPassword: String!) throws     func willPasswordExpire(_ willExpireIn: UInt64) -> Bool     func willAuthenticationsExpire(_ willExpireIn: UInt64) -> Bool     var secondsUntilPasswordExpires: Int64 { get }     var secondsUntilAuthenticationsExpire: Int64 { get }     func addMemberRecord(_ inRecord: ODRecord!) throws     func removeMemberRecord(_ inRecord: ODRecord!) throws     func isMemberRecord(_ inRecord: ODRecord!) throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODRecord : CVarArg { } extension ODRecord : Equatable, Hashable {     var hashValue: Int { get } } extension ODRecord {     func addMemberRecord(_ inRecord: ODRecord!) throws     func removeMemberRecord(_ inRecord: ODRecord!) throws     func isMemberRecord(_ inRecord: ODRecord!) throws } ``` | CVarArg, Equatable, Hashable |

Modified [ODRecord.accountPolicies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odrecord/1428124-accountpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func accountPolicies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func accountPolicies() throws -> [AnyHashable : Any] ``` |

Modified [ODRecord.addAccountPolicy(_: [AnyHashable : Any]!, toCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427406-addaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func addAccountPolicy(_ policy: [NSObject : AnyObject]!, toCategory category: String!) throws ``` |
| To | ``` func addAccountPolicy(_ policy: [AnyHashable : Any]!, toCategory category: String!) throws ``` |

Modified [ODRecord.addValue(_: Any!, toAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427729-addvalue)

|  | Declaration |
| --- | --- |
| From | ``` func addValue(_ inValue: AnyObject!, toAttribute inAttribute: String!) throws ``` |
| To | ``` func addValue(_ inValue: Any!, toAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.delete() throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427488-deleterecordandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func deleteRecord() throws ``` |
| To | ``` func delete() throws ``` |

Modified [ODRecord.effectivePolicies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odrecord/1427296-effectivepoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func effectivePolicies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func effectivePolicies() throws -> [AnyHashable : Any] ``` |

Modified [ODRecord.policies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odrecord/1427995-policiesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func policies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func policies() throws -> [AnyHashable : Any] ``` |

Modified [ODRecord.recordDetails(forAttributes: [Any]!) throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odrecord/1427081-recorddetails)

|  | Declaration |
| --- | --- |
| From | ``` func recordDetailsForAttributes(_ inAttributes: [AnyObject]!) throws -> [NSObject : AnyObject] ``` |
| To | ``` func recordDetails(forAttributes inAttributes: [Any]!) throws -> [AnyHashable : Any] ``` |

Modified [ODRecord.removeAccountPolicy(_: [AnyHashable : Any]!, fromCategory: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427577-removeaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removeAccountPolicy(_ policy: [NSObject : AnyObject]!, fromCategory category: String!) throws ``` |
| To | ``` func removeAccountPolicy(_ policy: [AnyHashable : Any]!, fromCategory category: String!) throws ``` |

Modified [ODRecord.removePolicy(_: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427589-removepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func removePolicy(_ policy: ODPolicyType!) throws ``` |
| To | ``` func removePolicy(_ policy: String!) throws ``` |

Modified [ODRecord.removeValue(_: Any!, fromAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1428290-removevalue)

|  | Declaration |
| --- | --- |
| From | ``` func removeValue(_ inValue: AnyObject!, fromAttribute inAttribute: String!) throws ``` |
| To | ``` func removeValue(_ inValue: Any!, fromAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.removeValues(forAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427273-removevalues)

|  | Declaration |
| --- | --- |
| From | ``` func removeValuesForAttribute(_ inAttribute: String!) throws ``` |
| To | ``` func removeValues(forAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.setAccountPolicies(_: [AnyHashable : Any]!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427241-setaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setAccountPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |
| To | ``` func setAccountPolicies(_ policies: [AnyHashable : Any]!) throws ``` |

Modified [ODRecord.setNodeCredentialsWithRecordType(_: String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427282-setnodecredentialswithrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws ``` |
| To | ``` func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws ``` |

Modified [ODRecord.setPolicies(_: [AnyHashable : Any]!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427266-setpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicies(_ policies: [NSObject : AnyObject]!) throws ``` |
| To | ``` func setPolicies(_ policies: [AnyHashable : Any]!) throws ``` |

Modified [ODRecord.setPolicy(_: String!, value: Any!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427191-setpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func setPolicy(_ policy: ODPolicyType!, value value: AnyObject!) throws ``` |
| To | ``` func setPolicy(_ policy: String!, value value: Any!) throws ``` |

Modified [ODRecord.setValue(_: Any!, forAttribute: String!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427911-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ inValueOrValues: AnyObject!, forAttribute inAttribute: String!) throws ``` |
| To | ``` func setValue(_ inValueOrValues: Any!, forAttribute inAttribute: String!) throws ``` |

Modified [ODRecord.supportedPolicies() throws -> [AnyHashable : Any]](https://developer.apple.com/documentation/opendirectory/odrecord/1428172-supportedpoliciesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func supportedPolicies() throws -> [NSObject : AnyObject] ``` |
| To | ``` func supportedPolicies() throws -> [AnyHashable : Any] ``` |

Modified [ODRecord.values(forAttribute: String!) throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odrecord/1427803-values)

|  | Declaration |
| --- | --- |
| From | ``` func valuesForAttribute(_ inAttribute: String!) throws -> [AnyObject] ``` |
| To | ``` func values(forAttribute inAttribute: String!) throws -> [Any] ``` |

Modified [ODRecord.verifyExtended(withAuthenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](https://developer.apple.com/documentation/opendirectory/odrecord/1427575-verifyextendedwithauthentication)

|  | Declaration |
| --- | --- |
| From | ``` func verifyExtendedWithAuthenticationType(_ inType: String!, authenticationItems inItems: [AnyObject]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws ``` |
| To | ``` func verifyExtended(withAuthenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws ``` |

Modified [ODRecordMap](https://developer.apple.com/documentation/opendirectory/odrecordmap)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODRecordMap : NSObject {     var native: String!     var odPredicate: [NSObject : AnyObject]!     var attributes: [NSObject : AnyObject]! { get }     var standardAttributeTypes: [AnyObject]! { get }     convenience init!()     class func recordMap() -> Self!     func attributeMapForStandardAttribute(_ standardAttribute: String!) -> ODAttributeMap!     func setAttributeMap(_ attributeMap: ODAttributeMap!, forStandardAttribute standardAttribute: String!) } ``` | -- |
| To | ``` class ODRecordMap : NSObject {     var native: String!     var odPredicate: [AnyHashable : Any]!     var attributes: [AnyHashable : Any]! { get }     var standardAttributeTypes: [Any]! { get }     convenience init!()     class func recordMap() -> Self!     func attributeMap(forStandardAttribute standardAttribute: String!) -> ODAttributeMap!     func setAttribute(_ attributeMap: ODAttributeMap!, forStandardAttribute standardAttribute: String!)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODRecordMap : CVarArg { } extension ODRecordMap : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODRecordMap.attributeMap(forStandardAttribute: String!) -> ODAttributeMap!](https://developer.apple.com/documentation/opendirectory/odrecordmap/1426918-attributemapforstandardattribute)

|  | Declaration |
| --- | --- |
| From | ``` func attributeMapForStandardAttribute(_ standardAttribute: String!) -> ODAttributeMap! ``` |
| To | ``` func attributeMap(forStandardAttribute standardAttribute: String!) -> ODAttributeMap! ``` |

Modified [ODRecordMap.attributes](https://developer.apple.com/documentation/opendirectory/odrecordmap/1428179-attributes)

|  | Declaration |
| --- | --- |
| From | ``` var attributes: [NSObject : AnyObject]! { get } ``` |
| To | ``` var attributes: [AnyHashable : Any]! { get } ``` |

Modified [ODRecordMap.odPredicate](https://developer.apple.com/documentation/opendirectory/odrecordmap/1427256-odpredicate)

|  | Declaration |
| --- | --- |
| From | ``` var odPredicate: [NSObject : AnyObject]! ``` |
| To | ``` var odPredicate: [AnyHashable : Any]! ``` |

Modified [ODRecordMap.setAttribute(_: ODAttributeMap!, forStandardAttribute: String!)](https://developer.apple.com/documentation/opendirectory/odrecordmap/1427114-setattribute)

|  | Declaration |
| --- | --- |
| From | ``` func setAttributeMap(_ attributeMap: ODAttributeMap!, forStandardAttribute standardAttribute: String!) ``` |
| To | ``` func setAttribute(_ attributeMap: ODAttributeMap!, forStandardAttribute standardAttribute: String!) ``` |

Modified [ODRecordMap.standardAttributeTypes](https://developer.apple.com/documentation/opendirectory/odrecordmap/1427183-standardattributetypes)

|  | Declaration |
| --- | --- |
| From | ``` var standardAttributeTypes: [AnyObject]! { get } ``` |
| To | ``` var standardAttributeTypes: [Any]! { get } ``` |

Modified [ODSession](https://developer.apple.com/documentation/opendirectory/odsession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class ODSession : NSObject {     class func defaultSession() -> ODSession!     convenience init(options inOptions: [NSObject : AnyObject]!) throws     class func sessionWithOptions(_ inOptions: [NSObject : AnyObject]!) throws -> Self     init(options inOptions: [NSObject : AnyObject]!) throws     func nodeNames() throws -> [AnyObject]     var configurationTemplateNames: [AnyObject]! { get }     var mappingTemplateNames: [AnyObject]! { get }     func configurationAuthorizationAllowingUserInteraction(_ allowInteraction: Bool) throws -> SFAuthorization     func configurationForNodename(_ nodename: String!) -> ODConfiguration!     func addConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws     func deleteConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws     func deleteConfigurationWithNodename(_ nodename: String!, authorization authorization: SFAuthorization!) throws } ``` | -- |
| To | ``` class ODSession : NSObject {     class func `default`() -> ODSession!     convenience init(options inOptions: [AnyHashable : Any]! = [:]) throws     class func withOptions(_ inOptions: [AnyHashable : Any]! = [:]) throws -> Self     init(options inOptions: [AnyHashable : Any]! = [:]) throws     func nodeNames() throws -> [Any]     var configurationTemplateNames: [Any]! { get }     var mappingTemplateNames: [Any]! { get }     func configurationAuthorizationAllowingUserInteraction(_ allowInteraction: Bool) throws -> SFAuthorization     func configuration(forNodename nodename: String!) -> ODConfiguration!     func add(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws     func delete(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws     func deleteConfiguration(withNodename nodename: String!, authorization authorization: SFAuthorization!) throws     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension ODSession : CVarArg { } extension ODSession : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [ODSession.add(_: ODConfiguration!, authorization: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1427913-addconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func addConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws ``` |
| To | ``` func add(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws ``` |

Modified [ODSession.configuration(forNodename: String!) -> ODConfiguration!](https://developer.apple.com/documentation/opendirectory/odsession/1427364-configurationfornodename)

|  | Declaration |
| --- | --- |
| From | ``` func configurationForNodename(_ nodename: String!) -> ODConfiguration! ``` |
| To | ``` func configuration(forNodename nodename: String!) -> ODConfiguration! ``` |

Modified [ODSession.configurationTemplateNames](https://developer.apple.com/documentation/opendirectory/odsession/1427783-configurationtemplatenames)

|  | Declaration |
| --- | --- |
| From | ``` var configurationTemplateNames: [AnyObject]! { get } ``` |
| To | ``` var configurationTemplateNames: [Any]! { get } ``` |

Modified [ODSession.default() [class]](https://developer.apple.com/documentation/opendirectory/odsession/1428153-defaultsession)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSession() -> ODSession! ``` |
| To | ``` class func `default`() -> ODSession! ``` |

Modified [ODSession.delete(_: ODConfiguration!, authorization: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1428166-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteConfiguration(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws ``` |
| To | ``` func delete(_ configuration: ODConfiguration!, authorization authorization: SFAuthorization!) throws ``` |

Modified [ODSession.deleteConfiguration(withNodename: String!, authorization: SFAuthorization!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1427476-deleteconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func deleteConfigurationWithNodename(_ nodename: String!, authorization authorization: SFAuthorization!) throws ``` |
| To | ``` func deleteConfiguration(withNodename nodename: String!, authorization authorization: SFAuthorization!) throws ``` |

Modified [ODSession.init(options: [AnyHashable : Any]!) throws](https://developer.apple.com/documentation/opendirectory/odsession/1427223-init)

|  | Declaration |
| --- | --- |
| From | ``` init(options inOptions: [NSObject : AnyObject]!) throws ``` |
| To | ``` init(options inOptions: [AnyHashable : Any]! = [:]) throws ``` |

Modified [ODSession.mappingTemplateNames](https://developer.apple.com/documentation/opendirectory/odsession/1427663-mappingtemplatenames)

|  | Declaration |
| --- | --- |
| From | ``` var mappingTemplateNames: [AnyObject]! { get } ``` |
| To | ``` var mappingTemplateNames: [Any]! { get } ``` |

Modified [ODSession.nodeNames() throws -> [Any]](https://developer.apple.com/documentation/opendirectory/odsession/1427490-nodenamesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` func nodeNames() throws -> [AnyObject] ``` |
| To | ``` func nodeNames() throws -> [Any] ``` |

Modified [kODPolicyTypeAccountExpiresOnDate](https://developer.apple.com/documentation/opendirectory/kodpolicytypeaccountexpiresondate)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypeAccountExpiresOnDate: ODPolicyType! ``` |
| To | ``` let kODPolicyTypeAccountExpiresOnDate: String ``` |

Modified [kODPolicyTypeAccountMaximumFailedLogins](https://developer.apple.com/documentation/opendirectory/kodpolicytypeaccountmaximumfailedlogins)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypeAccountMaximumFailedLogins: ODPolicyType! ``` |
| To | ``` let kODPolicyTypeAccountMaximumFailedLogins: String ``` |

Modified [kODPolicyTypeAccountMaximumMinutesOfNonUse](https://developer.apple.com/documentation/opendirectory/kodpolicytypeaccountmaximumminutesofnonuse)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypeAccountMaximumMinutesOfNonUse: ODPolicyType! ``` |
| To | ``` let kODPolicyTypeAccountMaximumMinutesOfNonUse: String ``` |

Modified [kODPolicyTypeAccountMaximumMinutesUntilDisabled](https://developer.apple.com/documentation/opendirectory/kodpolicytypeaccountmaximumminutesuntildisabled)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypeAccountMaximumMinutesUntilDisabled: ODPolicyType! ``` |
| To | ``` let kODPolicyTypeAccountMaximumMinutesUntilDisabled: String ``` |

Modified [kODPolicyTypeAccountMinutesUntilFailedLoginReset](https://developer.apple.com/documentation/opendirectory/kodpolicytypeaccountminutesuntilfailedloginreset)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypeAccountMinutesUntilFailedLoginReset: ODPolicyType! ``` |
| To | ``` let kODPolicyTypeAccountMinutesUntilFailedLoginReset: String ``` |

Modified [kODPolicyTypePasswordCannotBeAccountName](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordcannotbeaccountname)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordCannotBeAccountName: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordCannotBeAccountName: String ``` |

Modified [kODPolicyTypePasswordChangeRequired](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordchangerequired)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordChangeRequired: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordChangeRequired: String ``` |

Modified [kODPolicyTypePasswordHistory](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordhistory)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordHistory: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordHistory: String ``` |

Modified [kODPolicyTypePasswordMaximumAgeInMinutes](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordmaximumageinminutes)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordMaximumAgeInMinutes: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordMaximumAgeInMinutes: String ``` |

Modified [kODPolicyTypePasswordMaximumNumberOfCharacters](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordmaximumnumberofcharacters)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordMaximumNumberOfCharacters: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordMaximumNumberOfCharacters: String ``` |

Modified [kODPolicyTypePasswordMinimumNumberOfCharacters](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordminimumnumberofcharacters)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordMinimumNumberOfCharacters: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordMinimumNumberOfCharacters: String ``` |

Modified [kODPolicyTypePasswordRequiresAlpha](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordrequiresalpha)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordRequiresAlpha: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordRequiresAlpha: String ``` |

Modified [kODPolicyTypePasswordRequiresMixedCase](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordrequiresmixedcase)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordRequiresMixedCase: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordRequiresMixedCase: String ``` |

Modified [kODPolicyTypePasswordRequiresNumeric](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordrequiresnumeric)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordRequiresNumeric: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordRequiresNumeric: String ``` |

Modified [kODPolicyTypePasswordRequiresSymbol](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordrequiressymbol)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordRequiresSymbol: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordRequiresSymbol: String ``` |

Modified [kODPolicyTypePasswordSelfModification](https://developer.apple.com/documentation/opendirectory/kodpolicytypepasswordselfmodification)

|  | Declaration |
| --- | --- |
| From | ``` let kODPolicyTypePasswordSelfModification: ODPolicyType! ``` |
| To | ``` let kODPolicyTypePasswordSelfModification: String ``` |

Modified [ODNodeAddAccountPolicy(_: ODNodeRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427169-odnodeaddaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeAddAccountPolicy(_ node: ODNodeRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeAddAccountPolicy(_ node: ODNodeRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeCopyAccountPolicies(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](https://developer.apple.com/documentation/opendirectory/1427963-odnodecopyaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyAccountPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |
| To | ``` func ODNodeCopyAccountPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary! ``` |

Modified [ODNodeCopyDetails(_: ODNodeRef!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427681-odnodecopydetails)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyDetails(_ node: ODNodeRef!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODNodeCopyDetails(_ node: ODNodeRef!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODNodeCopyPolicies(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1426916-odnodecopypolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODNodeCopyPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODNodeCopyRecord(_: ODNodeRef!, _: String!, _: CFString!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](https://developer.apple.com/documentation/opendirectory/1427368-odnodecopyrecord)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributes: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecordRef>! ``` |
| To | ``` func ODNodeCopyRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributes: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>! ``` |

Modified [ODNodeCopySubnodeNames(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427388-odnodecopysubnodenames)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySubnodeNames(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopySubnodeNames(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCopySupportedAttributes(_: ODNodeRef!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427263-odnodecopysupportedattributes)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySupportedAttributes(_ node: ODNodeRef!, _ recordType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopySupportedAttributes(_ node: ODNodeRef!, _ recordType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCopySupportedPolicies(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427601-odnodecopysupportedpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySupportedPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODNodeCopySupportedPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODNodeCopySupportedRecordTypes(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427209-odnodecopysupportedrecordtypes)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySupportedRecordTypes(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopySupportedRecordTypes(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCopyUnreachableSubnodeNames(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1428190-odnodecopyunreachablesubnodename)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyUnreachableSubnodeNames(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopyUnreachableSubnodeNames(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCreateCopy(_: CFAllocator!, _: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](https://developer.apple.com/documentation/opendirectory/1427771-odnodecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateCopy(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>! ``` |
| To | ``` func ODNodeCreateCopy(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>! ``` |

Modified [ODNodeCreateRecord(_: ODNodeRef!, _: String!, _: CFString!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](https://developer.apple.com/documentation/opendirectory/1427989-odnodecreaterecord)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecordRef>! ``` |
| To | ``` func ODNodeCreateRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>! ``` |

Modified [ODNodeCreateWithName(_: CFAllocator!, _: ODSessionRef!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](https://developer.apple.com/documentation/opendirectory/1427133-odnodecreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>! ``` |
| To | ``` func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>! ``` |

Modified [ODNodeCreateWithNodeType(_: CFAllocator!, _: ODSessionRef!, _: ODNodeType, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](https://developer.apple.com/documentation/opendirectory/1428021-odnodecreatewithnodetype)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeType: ODNodeType, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>! ``` |
| To | ``` func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeType: ODNodeType, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>! ``` |

Modified [ODNodeCustomCall(_: ODNodeRef!, _: CFIndex, _: CFData!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFData!](https://developer.apple.com/documentation/opendirectory/1427838-odnodecustomcall)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCustomCall(_ node: ODNodeRef!, _ customCode: CFIndex, _ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData! ``` |
| To | ``` func ODNodeCustomCall(_ node: ODNodeRef!, _ customCode: CFIndex, _ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFData! ``` |

Modified [ODNodeCustomFunction(_: ODNodeRef!, _: CFString!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFTypeRef!](https://developer.apple.com/documentation/opendirectory/1427565-odnodecustomfunction)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCustomFunction(_ node: ODNodeRef!, _ function: CFString!, _ payload: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject! ``` |
| To | ``` func ODNodeCustomFunction(_ node: ODNodeRef!, _ function: CFString!, _ payload: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFTypeRef! ``` |

Modified [ODNodePasswordContentCheck(_: ODNodeRef!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1426938-odnodepasswordcontentcheck)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodePasswordContentCheck(_ node: ODNodeRef!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodePasswordContentCheck(_ node: ODNodeRef!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeRemoveAccountPolicy(_: ODNodeRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427805-odnoderemoveaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeRemoveAccountPolicy(_ node: ODNodeRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeRemoveAccountPolicy(_ node: ODNodeRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeRemovePolicy(_: ODNodeRef!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427219-odnoderemovepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeRemovePolicy(_ node: ODNodeRef!, _ policyType: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeRemovePolicy(_ node: ODNodeRef!, _ policyType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeSetAccountPolicies(_: ODNodeRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427971-odnodesetaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetAccountPolicies(_ node: ODNodeRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetAccountPolicies(_ node: ODNodeRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeSetCredentials(_: ODNodeRef!, _: String!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427179-odnodesetcredentials)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetCredentials(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetCredentials(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeSetCredentialsExtended(_: ODNodeRef!, _: String!, _: String!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1428069-odnodesetcredentialsextended)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetCredentialsExtended(_ node: ODNodeRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetCredentialsExtended(_ node: ODNodeRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeSetPolicies(_: ODNodeRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427235-odnodesetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetPolicies(_ node: ODNodeRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetPolicies(_ node: ODNodeRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODNodeSetPolicy(_: ODNodeRef!, _: String!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427861-odnodesetpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetPolicy(_ node: ODNodeRef!, _ policyType: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetPolicy(_ node: ODNodeRef!, _ policyType: String!, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODPolicyType](https://developer.apple.com/documentation/opendirectory/odpolicytype)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODPolicyType = CFStringRef ``` |
| To | ``` typealias ODPolicyType = NSString ``` |

Modified [ODQueryCallback](https://developer.apple.com/documentation/opendirectory/odquerycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODQueryCallback = (ODQueryRef!, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias ODQueryCallback = (ODQueryRef?, CFArray?, CFError?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [ODQueryCopyResults(_: ODQueryRef!, _: Bool, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1426942-odquerycopyresults)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryCopyResults(_ query: ODQueryRef!, _ allowPartialResults: Bool, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODQueryCopyResults(_ query: ODQueryRef!, _ allowPartialResults: Bool, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODQueryCreateWithNode(_: CFAllocator!, _: ODNodeRef!, _: CFTypeRef!, _: String!, _: ODMatchType, _: CFTypeRef!, _: CFTypeRef!, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](https://developer.apple.com/documentation/opendirectory/1427159-odquerycreatewithnode)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQueryRef>! ``` |
| To | ``` func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ recordTypeOrList: CFTypeRef!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: CFTypeRef!, _ returnAttributeOrList: CFTypeRef!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>! ``` |

Modified [ODQueryCreateWithNodeType(_: CFAllocator!, _: ODNodeType, _: CFTypeRef!, _: String!, _: ODMatchType, _: CFTypeRef!, _: CFTypeRef!, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](https://developer.apple.com/documentation/opendirectory/1428246-odquerycreatewithnodetype)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryCreateWithNodeType(_ allocator: CFAllocator!, _ nodeType: ODNodeType, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQueryRef>! ``` |
| To | ``` func ODQueryCreateWithNodeType(_ allocator: CFAllocator!, _ nodeType: ODNodeType, _ recordTypeOrList: CFTypeRef!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: CFTypeRef!, _ returnAttributeOrList: CFTypeRef!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>! ``` |

Modified [ODQuerySetCallback(_: ODQueryRef!, _: OpenDirectory.ODQueryCallback!, _: UnsafeMutableRawPointer!)](https://developer.apple.com/documentation/opendirectory/1427306-odquerysetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func ODQuerySetCallback(_ query: ODQueryRef!, _ callback: ODQueryCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ODQuerySetCallback(_ query: ODQueryRef!, _ callback: OpenDirectory.ODQueryCallback!, _ userInfo: UnsafeMutableRawPointer!) ``` |

Modified [ODQuerySetDispatchQueue(_: ODQueryRef!, _: DispatchQueue!)](https://developer.apple.com/documentation/opendirectory/1427637-odquerysetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func ODQuerySetDispatchQueue(_ query: ODQueryRef!, _ queue: dispatch_queue_t!) ``` |
| To | ``` func ODQuerySetDispatchQueue(_ query: ODQueryRef!, _ queue: DispatchQueue!) ``` |

Modified [ODRecordAddAccountPolicy(_: ODRecordRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427181-odrecordaddaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddAccountPolicy(_ record: ODRecordRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddAccountPolicy(_ record: ODRecordRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordAddMember(_: ODRecordRef!, _: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427898-odrecordaddmember)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordAddValue(_: ODRecordRef!, _: String!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427832-odrecordaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddValue(_ record: ODRecordRef!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddValue(_ record: ODRecordRef!, _ attribute: String!, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordAuthenticationAllowed(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427977-odrecordauthenticationallowed)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAuthenticationAllowed(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAuthenticationAllowed(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordChangePassword(_: ODRecordRef!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1428272-odrecordchangepassword)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordChangePassword(_ record: ODRecordRef!, _ oldPassword: CFString!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordChangePassword(_ record: ODRecordRef!, _ oldPassword: CFString!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordContainsMember(_: ODRecordRef!, _: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427923-odrecordcontainsmember)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordContainsMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordContainsMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordCopyAccountPolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](https://developer.apple.com/documentation/opendirectory/1427023-odrecordcopyaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyAccountPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |
| To | ``` func ODRecordCopyAccountPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary! ``` |

Modified [ODRecordCopyDetails(_: ODRecordRef!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427472-odrecordcopydetails)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyDetails(_ record: ODRecordRef!, _ attributes: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopyDetails(_ record: ODRecordRef!, _ attributes: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopyEffectivePolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427362-odrecordcopyeffectivepolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyEffectivePolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopyEffectivePolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopyPolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427298-odrecordcopypolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopyPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopySupportedPolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427055-odrecordcopysupportedpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopySupportedPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopySupportedPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopyValues(_: ODRecordRef!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1428186-odrecordcopyvalues)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyValues(_ record: ODRecordRef!, _ attribute: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODRecordCopyValues(_ record: ODRecordRef!, _ attribute: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODRecordDelete(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427118-odrecorddelete)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordDelete(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordDelete(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordPasswordChangeAllowed(_: ODRecordRef!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427135-odrecordpasswordchangeallowed)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordPasswordChangeAllowed(_ record: ODRecordRef!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordPasswordChangeAllowed(_ record: ODRecordRef!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordRemoveAccountPolicy(_: ODRecordRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427675-odrecordremoveaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveAccountPolicy(_ record: ODRecordRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveAccountPolicy(_ record: ODRecordRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordRemoveMember(_: ODRecordRef!, _: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427621-odrecordremovemember)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordRemovePolicy(_: ODRecordRef!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427063-odrecordremovepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemovePolicy(_ record: ODRecordRef!, _ policy: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemovePolicy(_ record: ODRecordRef!, _ policy: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordRemoveValue(_: ODRecordRef!, _: String!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427332-odrecordremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveValue(_ record: ODRecordRef!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveValue(_ record: ODRecordRef!, _ attribute: String!, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSetAccountPolicies(_: ODRecordRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427703-odrecordsetaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetAccountPolicies(_ record: ODRecordRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetAccountPolicies(_ record: ODRecordRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSetNodeCredentials(_: ODRecordRef!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427646-odrecordsetnodecredentials)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetNodeCredentials(_ record: ODRecordRef!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetNodeCredentials(_ record: ODRecordRef!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSetNodeCredentialsExtended(_: ODRecordRef!, _: String!, _: String!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427347-odrecordsetnodecredentialsextend)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetNodeCredentialsExtended(_ record: ODRecordRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetNodeCredentialsExtended(_ record: ODRecordRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSetPolicies(_: ODRecordRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427387-odrecordsetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetPolicies(_ record: ODRecordRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetPolicies(_ record: ODRecordRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSetPolicy(_: ODRecordRef!, _: String!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1428137-odrecordsetpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetPolicy(_ record: ODRecordRef!, _ policy: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetPolicy(_ record: ODRecordRef!, _ policy: String!, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSetValue(_: ODRecordRef!, _: String!, _: CFTypeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427997-odrecordsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetValue(_ record: ODRecordRef!, _ attribute: String!, _ valueOrValues: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetValue(_ record: ODRecordRef!, _ attribute: String!, _ valueOrValues: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordSynchronize(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1428125-odrecordsynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSynchronize(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSynchronize(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordVerifyPassword(_: ODRecordRef!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427277-odrecordverifypassword)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordVerifyPassword(_ record: ODRecordRef!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordVerifyPassword(_ record: ODRecordRef!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODRecordVerifyPasswordExtended(_: ODRecordRef!, _: String!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](https://developer.apple.com/documentation/opendirectory/1427104-odrecordverifypasswordextended)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordVerifyPasswordExtended(_ record: ODRecordRef!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordVerifyPasswordExtended(_ record: ODRecordRef!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool ``` |

Modified [ODSessionCopyNodeNames(_: CFAllocator!, _: ODSessionRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427427-odsessioncopynodenames)

|  | Declaration |
| --- | --- |
| From | ``` func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>! ``` |

Modified [ODSessionCreate(_: CFAllocator!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](https://developer.apple.com/documentation/opendirectory/1427961-odsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSessionRef>! ``` |
| To | ``` func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>! ``` |

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
