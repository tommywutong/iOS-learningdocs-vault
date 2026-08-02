---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/SecurityFoundation.html
archived_at: '2026-07-18T02:51:36.466210Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# SecurityFoundation Changes for Swift

### SecurityFoundation

Modified [SFAuthorization](https://developer.apple.com/documentation/securityfoundation/sfauthorization)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SFAuthorization : NSObject, NSCoding {     class func authorization() -> AnyObject!     func authorizationRef() -> AuthorizationRef     class func authorizationWithFlags(_ flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) -> AnyObject!     init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>)     init!()     func invalidateCredentials()     func obtainWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) throws     func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) throws } extension SFAuthorization {     func permitWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<AuthorizationRights>) -> OSStatus     func permitWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) -> OSStatus } ``` | NSCoding |
| To | ``` class SFAuthorization : NSObject, NSCoding {     class func authorization() -> Any!     func authorizationRef() -> AuthorizationRef!     class func authorization(with flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>!, environment environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!     init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>!, environment environment: UnsafePointer<AuthorizationEnvironment>!)     init!()     func invalidateCredentials()     func obtain(withRight rightName: AuthorizationString!, flags flags: AuthorizationFlags) throws     func obtain(withRights rights: UnsafePointer<AuthorizationRights>!, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws     func permit(withRights rights: UnsafePointer<AuthorizationRights>!, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights authorizedRights: UnsafeMutablePointer<AuthorizationRights>!) -> OSStatus     func permit(withRight rightName: AuthorizationString!, flags flags: AuthorizationFlags) -> OSStatus     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SFAuthorization : CVarArg { } extension SFAuthorization : Equatable, Hashable {     var hashValue: Int { get } } extension SFAuthorization {     func permit(withRights rights: UnsafePointer<AuthorizationRights>!, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights authorizedRights: UnsafeMutablePointer<AuthorizationRights>!) -> OSStatus     func permit(withRight rightName: AuthorizationString!, flags flags: AuthorizationFlags) -> OSStatus } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [SFAuthorization.authorization() -> Any! [class]](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417643-authorization)

|  | Declaration |
| --- | --- |
| From | ``` class func authorization() -> AnyObject! ``` |
| To | ``` class func authorization() -> Any! ``` |

Modified [SFAuthorization.authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any! [class]](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417650-authorizationwithflags)

|  | Declaration |
| --- | --- |
| From | ``` class func authorizationWithFlags(_ flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) -> AnyObject! ``` |
| To | ``` class func authorization(with flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>!, environment environment: UnsafePointer<AuthorizationEnvironment>!) -> Any! ``` |

Modified [SFAuthorization.authorizationRef() -> AuthorizationRef!](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417636-authorizationref)

|  | Declaration |
| --- | --- |
| From | ``` func authorizationRef() -> AuthorizationRef ``` |
| To | ``` func authorizationRef() -> AuthorizationRef! ``` |

Modified [SFAuthorization.init(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417632-initwithflags)

|  | Declaration |
| --- | --- |
| From | ``` init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>, environment environment: UnsafePointer<AuthorizationEnvironment>) ``` |
| To | ``` init!(flags flags: AuthorizationFlags, rights rights: UnsafePointer<AuthorizationRights>!, environment environment: UnsafePointer<AuthorizationEnvironment>!) ``` |

Modified [SFAuthorization.obtain(withRight: AuthorizationString!, flags: AuthorizationFlags) throws](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417652-obtainwithright)

|  | Declaration |
| --- | --- |
| From | ``` func obtainWithRight(_ rightName: AuthorizationString, flags flags: AuthorizationFlags) throws ``` |
| To | ``` func obtain(withRight rightName: AuthorizationString!, flags flags: AuthorizationFlags) throws ``` |

Modified [SFAuthorization.obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](https://developer.apple.com/documentation/securityfoundation/sfauthorization/1417648-obtainwithrights)

|  | Declaration |
| --- | --- |
| From | ``` func obtainWithRights(_ rights: UnsafePointer<AuthorizationRights>, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>>) throws ``` |
| To | ``` func obtain(withRights rights: UnsafePointer<AuthorizationRights>!, flags flags: AuthorizationFlags, environment environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws ``` |

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
