---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/StoreKit.html
archived_at: '2026-07-18T02:51:37.128918Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# StoreKit Changes for Swift

### StoreKit

Removed [SKDownloadState [struct]](https://developer.apple.com/documentation/storekit/skdownloadstate)Removed SKDownloadState.init(_: Int)Removed SKDownloadState.init(rawValue: Int)Removed SKDownloadState.rawValueRemoved [SKDownloadStateActive](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstateactive)Removed [SKDownloadStateCancelled](https://developer.apple.com/documentation/storekit/skdownloadstate/cancelled)Removed [SKDownloadStateFailed](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefailed)Removed [SKDownloadStateFinished](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefinished)Removed [SKDownloadStatePaused](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatepaused)Removed [SKDownloadStateWaiting](https://developer.apple.com/documentation/storekit/skdownloadstate/waiting)Removed [SKErrorClientInvalid](https://developer.apple.com/documentation/storekit/skerror/code/clientinvalid)Removed [SKErrorPaymentCancelled](https://developer.apple.com/documentation/storekit/skerror/code/paymentcancelled)Removed [SKErrorPaymentInvalid](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorpaymentinvalid)Removed [SKErrorPaymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/code/paymentnotallowed)Removed [SKErrorUnknown](https://developer.apple.com/documentation/storekit/skerror/code/unknown)Removed [SKPaymentTransactionState](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate)Removed [SKPaymentTransactionStateDeferred](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred)Removed [SKPaymentTransactionStateFailed](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/failed)Removed [SKPaymentTransactionStatePurchased](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstatepurchased)Removed [SKPaymentTransactionStatePurchasing](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchasing)Removed [SKPaymentTransactionStateRestored](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstaterestored)Added [SKDownloadState [enum]](https://developer.apple.com/documentation/storekit/skdownloadstate)Added [SKDownloadState.active](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstateactive)Added [SKDownloadState.cancelled](https://developer.apple.com/documentation/storekit/skdownloadstate/cancelled)Added [SKDownloadState.failed](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefailed)Added [SKDownloadState.finished](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefinished)Added [SKDownloadState.paused](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatepaused)Added [SKDownloadState.waiting](https://developer.apple.com/documentation/storekit/skdownloadstate/waiting)Added [SKError [struct]](https://developer.apple.com/documentation/storekit/skerror)Added [SKError.clientInvalid](https://developer.apple.com/documentation/storekit/skerror/2330533-clientinvalid)Added SKError.init(_nsError: NSError)Added [SKError.paymentCancelled](https://developer.apple.com/documentation/storekit/skerror/2330537-paymentcancelled)Added [SKError.paymentInvalid](https://developer.apple.com/documentation/storekit/skerror/2330536-paymentinvalid)Added [SKError.paymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/2330535-paymentnotallowed)Added [SKError.unknown](https://developer.apple.com/documentation/storekit/skerror/2330534-unknown)Added [SKError.Code [enum]](https://developer.apple.com/documentation/storekit/skerrorcode)Added [SKError.Code.clientInvalid](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorclientinvalid)Added [SKError.Code.paymentCancelled](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorpaymentcancelled)Added [SKError.Code.paymentInvalid](https://developer.apple.com/documentation/storekit/skerror/code/paymentinvalid)Added [SKError.Code.paymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/code/paymentnotallowed)Added [SKError.Code.unknown](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorunknown)Added [SKPaymentTransactionState [enum]](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate)Added [SKPaymentTransactionState.deferred](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred)Added [SKPaymentTransactionState.failed](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstatefailed)Added [SKPaymentTransactionState.purchased](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstatepurchased)Added [SKPaymentTransactionState.purchasing](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchasing)Added [SKPaymentTransactionState.restored](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstaterestored)Modified [SKDownload](https://developer.apple.com/documentation/storekit/skdownload)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKDownload : NSObject {     var contentIdentifier: String { get }     var state: SKDownloadState { get }     @NSCopying var contentURL: NSURL? { get }     var progress: Float { get }     @NSCopying var error: NSError? { get }     var timeRemaining: NSTimeInterval { get }     @NSCopying var contentLength: NSNumber { get }     var contentVersion: String? { get }     var transaction: SKPaymentTransaction? { get }     class func contentURLForProductID(_ productID: String) -> NSURL?     class func deleteContentForProductID(_ productID: String) } ``` | -- |
| To | ``` class SKDownload : NSObject {     var contentIdentifier: String { get }     var state: SKDownloadState { get }     var contentURL: URL? { get }     var progress: Float { get }     var error: Error? { get }     var timeRemaining: TimeInterval { get }     @NSCopying var contentLength: NSNumber { get }     var contentVersion: String { get }     var transaction: SKPaymentTransaction { get }     class func contentURL(forProductID productID: String) -> URL?     class func deleteContent(forProductID productID: String)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKDownload : CVarArg { } extension SKDownload : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKDownload.contentIdentifier](https://developer.apple.com/documentation/storekit/skdownload/1458941-contentidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified [SKDownload.contentLength](https://developer.apple.com/documentation/storekit/skdownload/1458932-contentlength)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @NSCopying var contentURL: NSURL? { get } ``` | OS X 10.10 |
| To | ``` var contentURL: URL? { get } ``` | OS X 10.8 |

Modified [SKDownload.contentURL(forProductID: String) -> URL? [class]](https://developer.apple.com/documentation/storekit/skdownload/1458924-contenturlforproductid)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func contentURLForProductID(_ productID: String) -> NSURL? ``` | OS X 10.10 |
| To | ``` class func contentURL(forProductID productID: String) -> URL? ``` | OS X 10.8 |

Modified [SKDownload.contentVersion](https://developer.apple.com/documentation/storekit/skdownload/1458916-contentversion)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var contentVersion: String? { get } ``` | OS X 10.10 |
| To | ``` var contentVersion: String { get } ``` | OS X 10.8 |

Modified [SKDownload.deleteContent(forProductID: String) [class]](https://developer.apple.com/documentation/storekit/skdownload/1458926-deletecontentforproductid)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func deleteContentForProductID(_ productID: String) ``` | OS X 10.10 |
| To | ``` class func deleteContent(forProductID productID: String) ``` | OS X 10.8 |

Modified [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @NSCopying var error: NSError? { get } ``` | OS X 10.10 |
| To | ``` var error: Error? { get } ``` | OS X 10.8 |

Modified [SKDownload.progress](https://developer.apple.com/documentation/storekit/skdownload/1458945-progress)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified [SKDownload.state](https://developer.apple.com/documentation/storekit/skdownload/1458937-state)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified [SKDownload.timeRemaining](https://developer.apple.com/documentation/storekit/skdownload/1458943-timeremaining)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var timeRemaining: NSTimeInterval { get } ``` | OS X 10.10 |
| To | ``` var timeRemaining: TimeInterval { get } ``` | OS X 10.8 |

Modified [SKDownload.transaction](https://developer.apple.com/documentation/storekit/skdownload/1458949-transaction)

|  | Declaration |
| --- | --- |
| From | ``` var transaction: SKPaymentTransaction? { get } ``` |
| To | ``` var transaction: SKPaymentTransaction { get } ``` |

Modified [SKMutablePayment](https://developer.apple.com/documentation/storekit/skmutablepayment)

|  | Declaration |
| --- | --- |
| From | ``` class SKMutablePayment : SKPayment {     var productIdentifier: String     var quantity: Int     @NSCopying var requestData: NSData?     var applicationUsername: String? } ``` |
| To | ``` class SKMutablePayment : SKPayment {     var productIdentifier: String     var quantity: Int     var requestData: Data?     var applicationUsername: String? } ``` |

Modified [SKMutablePayment.applicationUsername](https://developer.apple.com/documentation/storekit/skmutablepayment/1506088-applicationusername)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified [SKMutablePayment.productIdentifier](https://developer.apple.com/documentation/storekit/skmutablepayment/1505983-productidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKMutablePayment.quantity](https://developer.apple.com/documentation/storekit/skmutablepayment/1506170-quantity)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKMutablePayment.requestData](https://developer.apple.com/documentation/storekit/skmutablepayment/1505974-requestdata)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @NSCopying var requestData: NSData? ``` | OS X 10.10 |
| To | ``` var requestData: Data? ``` | OS X 10.7 |

Modified [SKPayment](https://developer.apple.com/documentation/storekit/skpayment)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPayment : NSObject, NSCopying, NSMutableCopying {     class func paymentWithProduct(_ product: SKProduct) -> AnyObject     var productIdentifier: String { get }     @NSCopying var requestData: NSData? { get }     var quantity: Int { get }     var applicationUsername: String? { get } } ``` | NSCopying, NSMutableCopying |
| To | ``` class SKPayment : NSObject, NSCopying, NSMutableCopying {     convenience init(product product: SKProduct)     class func withProduct(_ product: SKProduct) -> Self     var productIdentifier: String { get }     var requestData: Data? { get }     var quantity: Int { get }     var applicationUsername: String? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKPayment : CVarArg { } extension SKPayment : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [SKPayment.applicationUsername](https://developer.apple.com/documentation/storekit/skpayment/1506116-applicationusername)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified [SKPayment.init(product: SKProduct)](https://developer.apple.com/documentation/storekit/skpayment/1506008-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | paymentWithProduct(_:) | ``` class func paymentWithProduct(_ product: SKProduct) -> AnyObject ``` | OS X 10.10 |
| To | init(product:) | ``` convenience init(product product: SKProduct) ``` | OS X 10.7 |

Modified [SKPayment.productIdentifier](https://developer.apple.com/documentation/storekit/skpayment/1506155-productidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPayment.quantity](https://developer.apple.com/documentation/storekit/skpayment/1506077-quantity)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPayment.requestData](https://developer.apple.com/documentation/storekit/skpayment/1506159-requestdata)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @NSCopying var requestData: NSData? { get } ``` | OS X 10.10 |
| To | ``` var requestData: Data? { get } ``` | OS X 10.7 |

Modified [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPaymentQueue : NSObject {     class func defaultQueue() -> SKPaymentQueue     class func canMakePayments() -> Bool     func addPayment(_ payment: SKPayment)     func restoreCompletedTransactions()     func restoreCompletedTransactionsWithApplicationUsername(_ username: String?)     func finishTransaction(_ transaction: SKPaymentTransaction)     func addTransactionObserver(_ observer: SKPaymentTransactionObserver)     func removeTransactionObserver(_ observer: SKPaymentTransactionObserver)     var transactions: [SKPaymentTransaction]? { get }     func startDownloads(_ downloads: [SKDownload])     func pauseDownloads(_ downloads: [SKDownload])     func resumeDownloads(_ downloads: [SKDownload])     func cancelDownloads(_ downloads: [SKDownload]) } ``` | -- |
| To | ``` class SKPaymentQueue : NSObject {     class func `default`() -> Self     class func canMakePayments() -> Bool     func add(_ payment: SKPayment)     func restoreCompletedTransactions()     func restoreCompletedTransactions(withApplicationUsername username: String?)     func finishTransaction(_ transaction: SKPaymentTransaction)     func add(_ observer: SKPaymentTransactionObserver)     func remove(_ observer: SKPaymentTransactionObserver)     var transactions: [SKPaymentTransaction] { get }     func start(_ downloads: [SKDownload])     func pause(_ downloads: [SKDownload])     func resume(_ downloads: [SKDownload])     func cancel(_ downloads: [SKDownload])     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKPaymentQueue : CVarArg { } extension SKPaymentQueue : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKPaymentQueue.add(_: SKPayment)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506036-addpayment)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addPayment(_ payment: SKPayment) ``` | OS X 10.10 |
| To | ``` func add(_ payment: SKPayment) ``` | OS X 10.7 |

Modified [SKPaymentQueue.add(_: SKPaymentTransactionObserver)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506042-addtransactionobserver)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func addTransactionObserver(_ observer: SKPaymentTransactionObserver) ``` | OS X 10.10 |
| To | ``` func add(_ observer: SKPaymentTransactionObserver) ``` | OS X 10.7 |

Modified [SKPaymentQueue.cancel(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-canceldownloads)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func cancelDownloads(_ downloads: [SKDownload]) ``` | OS X 10.10 |
| To | ``` func cancel(_ downloads: [SKDownload]) ``` | OS X 10.8 |

Modified [SKPaymentQueue.canMakePayments() -> Bool [class]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506139-canmakepayments)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPaymentQueue.default() [class]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505990-default)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func defaultQueue() -> SKPaymentQueue ``` | OS X 10.10 |
| To | ``` class func `default`() -> Self ``` | OS X 10.7 |

Modified [SKPaymentQueue.finishTransaction(_: SKPaymentTransaction)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506003-finishtransaction)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPaymentQueue.pause(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pausedownloads)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func pauseDownloads(_ downloads: [SKDownload]) ``` | OS X 10.10 |
| To | ``` func pause(_ downloads: [SKDownload]) ``` | OS X 10.8 |

Modified [SKPaymentQueue.remove(_: SKPaymentTransactionObserver)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506165-remove)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func removeTransactionObserver(_ observer: SKPaymentTransactionObserver) ``` | OS X 10.10 |
| To | ``` func remove(_ observer: SKPaymentTransactionObserver) ``` | OS X 10.7 |

Modified [SKPaymentQueue.restoreCompletedTransactions()](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506123-restorecompletedtransactions)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPaymentQueue.restoreCompletedTransactions(withApplicationUsername: String?)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func restoreCompletedTransactionsWithApplicationUsername(_ username: String?) ``` | OS X 10.10 |
| To | ``` func restoreCompletedTransactions(withApplicationUsername username: String?) ``` | OS X 10.9 |

Modified [SKPaymentQueue.resume(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func resumeDownloads(_ downloads: [SKDownload]) ``` | OS X 10.10 |
| To | ``` func resume(_ downloads: [SKDownload]) ``` | OS X 10.8 |

Modified [SKPaymentQueue.start(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-startdownloads)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func startDownloads(_ downloads: [SKDownload]) ``` | OS X 10.10 |
| To | ``` func start(_ downloads: [SKDownload]) ``` | OS X 10.8 |

Modified [SKPaymentQueue.transactions](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506026-transactions)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var transactions: [SKPaymentTransaction]? { get } ``` | OS X 10.10 |
| To | ``` var transactions: [SKPaymentTransaction] { get } ``` | OS X 10.7 |

Modified [SKPaymentTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPaymentTransaction : NSObject {     var error: NSError? { get }     var originalTransaction: SKPaymentTransaction? { get }     var payment: SKPayment { get }     var transactionDate: NSDate? { get }     var transactionIdentifier: String? { get }     var downloads: [AnyObject]? { get }     var transactionState: SKPaymentTransactionState { get } } ``` | -- |
| To | ``` class SKPaymentTransaction : NSObject {     var error: Error? { get }     var original: SKPaymentTransaction? { get }     var payment: SKPayment { get }     var transactionDate: Date? { get }     var transactionIdentifier: String? { get }     var downloads: [SKDownload] { get }     var transactionState: SKPaymentTransactionState { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKPaymentTransaction : CVarArg { } extension SKPaymentTransaction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var downloads: [AnyObject]? { get } ``` | OS X 10.10 |
| To | ``` var downloads: [SKDownload] { get } ``` | OS X 10.8 |

Modified [SKPaymentTransaction.error](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411269-error)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var error: NSError? { get } ``` | OS X 10.10 |
| To | ``` var error: Error? { get } ``` | OS X 10.7 |

Modified [SKPaymentTransaction.original](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411284-originaltransaction)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var originalTransaction: SKPaymentTransaction? { get } ``` | OS X 10.10 |
| To | ``` var original: SKPaymentTransaction? { get } ``` | OS X 10.7 |

Modified [SKPaymentTransaction.payment](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411286-payment)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPaymentTransaction.transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var transactionDate: NSDate? { get } ``` | OS X 10.10 |
| To | ``` var transactionDate: Date? { get } ``` | OS X 10.7 |

Modified [SKPaymentTransaction.transactionIdentifier](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411288-transactionidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPaymentTransaction.transactionState](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411275-transactionstate)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKPaymentTransactionObserver : NSObjectProtocol {     func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])     optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction])     optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: NSError)     optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)     optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload]) } ``` |
| To | ``` protocol SKPaymentTransactionObserver : NSObjectProtocol {     func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])     optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction])     optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: Error)     optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)     optional func paymentQueue(_ queue: SKPaymentQueue, updatedDownloads downloads: [SKDownload]) } ``` |

Modified [SKPaymentTransactionObserver.paymentQueue(_: SKPaymentQueue, restoreCompletedTransactionsFailedWithError: Error)](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506063-paymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: NSError) ``` |
| To | ``` optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: Error) ``` |

Modified [SKProduct](https://developer.apple.com/documentation/storekit/skproduct)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKProduct : NSObject {     var localizedDescription: String? { get }     var localizedTitle: String? { get }     var price: NSDecimalNumber? { get }     var priceLocale: NSLocale? { get }     var productIdentifier: String? { get }     var downloadable: Bool { get }     var contentVersion: String? { get }     var contentLengths: [NSNumber]? { get } } ``` | -- |
| To | ``` class SKProduct : NSObject {     var localizedDescription: String { get }     var localizedTitle: String { get }     var price: NSDecimalNumber { get }     var priceLocale: Locale { get }     var productIdentifier: String { get }     var downloadable: Bool { get }     var contentVersion: String { get }     var contentLengths: [NSNumber] { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKProduct : CVarArg { } extension SKProduct : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKProduct.contentLengths](https://developer.apple.com/documentation/storekit/skproduct/1506157-contentlengths)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var contentLengths: [NSNumber]? { get } ``` | OS X 10.10 |
| To | ``` var contentLengths: [NSNumber] { get } ``` | OS X 10.8 |

Modified [SKProduct.contentVersion](https://developer.apple.com/documentation/storekit/skproduct/1505996-contentversion)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var contentVersion: String? { get } ``` | OS X 10.10 |
| To | ``` var contentVersion: String { get } ``` | OS X 10.8 |

Modified [SKProduct.downloadable](https://developer.apple.com/documentation/storekit/skproduct/1506161-isdownloadable)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified [SKProduct.localizedDescription](https://developer.apple.com/documentation/storekit/skproduct/1506040-localizeddescription)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var localizedDescription: String? { get } ``` | OS X 10.10 |
| To | ``` var localizedDescription: String { get } ``` | OS X 10.7 |

Modified [SKProduct.localizedTitle](https://developer.apple.com/documentation/storekit/skproduct/1506001-localizedtitle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var localizedTitle: String? { get } ``` | OS X 10.10 |
| To | ``` var localizedTitle: String { get } ``` | OS X 10.7 |

Modified [SKProduct.price](https://developer.apple.com/documentation/storekit/skproduct/1506094-price)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var price: NSDecimalNumber? { get } ``` | OS X 10.10 |
| To | ``` var price: NSDecimalNumber { get } ``` | OS X 10.7 |

Modified [SKProduct.priceLocale](https://developer.apple.com/documentation/storekit/skproduct/1506145-pricelocale)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var priceLocale: NSLocale? { get } ``` | OS X 10.10 |
| To | ``` var priceLocale: Locale { get } ``` | OS X 10.7 |

Modified [SKProduct.productIdentifier](https://developer.apple.com/documentation/storekit/skproduct/1506080-productidentifier)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var productIdentifier: String? { get } ``` | OS X 10.10 |
| To | ``` var productIdentifier: String { get } ``` | OS X 10.7 |

Modified [SKProductsRequest](https://developer.apple.com/documentation/storekit/skproductsrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SKProductsRequest : SKRequest {     init(productIdentifiers productIdentifiers: Set<NSObject>)     unowned(unsafe) var delegate: SKProductsRequestDelegate? } ``` |
| To | ``` class SKProductsRequest : SKRequest {     init(productIdentifiers productIdentifiers: Set<String>)     weak var delegate: SKProductsRequestDelegate? } ``` |

Modified [SKProductsRequest.delegate](https://developer.apple.com/documentation/storekit/skproductsrequest/1506142-delegate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` unowned(unsafe) var delegate: SKProductsRequestDelegate? ``` | OS X 10.10 |
| To | ``` weak var delegate: SKProductsRequestDelegate? ``` | OS X 10.7 |

Modified [SKProductsRequest.init(productIdentifiers: Set<String>)](https://developer.apple.com/documentation/storekit/skproductsrequest/1506172-init)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(productIdentifiers productIdentifiers: Set<NSObject>) ``` | OS X 10.10 |
| To | ``` init(productIdentifiers productIdentifiers: Set<String>) ``` | OS X 10.7 |

Modified [SKProductsRequestDelegate](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKProductsRequestDelegate : SKRequestDelegate {     func productsRequest(_ request: SKProductsRequest, didReceiveResponse response: SKProductsResponse) } ``` |
| To | ``` protocol SKProductsRequestDelegate : SKRequestDelegate {     func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) } ``` |

Modified [SKProductsRequestDelegate.productsRequest(_: SKProductsRequest, didReceive: SKProductsResponse)](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate/1506070-productsrequest)

|  | Declaration |
| --- | --- |
| From | ``` func productsRequest(_ request: SKProductsRequest, didReceiveResponse response: SKProductsResponse) ``` |
| To | ``` func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) ``` |

Modified [SKProductsResponse](https://developer.apple.com/documentation/storekit/skproductsresponse)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKProductsResponse : NSObject {     var products: [SKProduct]? { get }     var invalidProductIdentifiers: [String]? { get } } ``` | -- |
| To | ``` class SKProductsResponse : NSObject {     var products: [SKProduct] { get }     var invalidProductIdentifiers: [String] { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKProductsResponse : CVarArg { } extension SKProductsResponse : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKProductsResponse.invalidProductIdentifiers](https://developer.apple.com/documentation/storekit/skproductsresponse/1505985-invalidproductidentifiers)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var invalidProductIdentifiers: [String]? { get } ``` | OS X 10.10 |
| To | ``` var invalidProductIdentifiers: [String] { get } ``` | OS X 10.7 |

Modified [SKProductsResponse.products](https://developer.apple.com/documentation/storekit/skproductsresponse/1506047-products)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var products: [SKProduct]? { get } ``` | OS X 10.10 |
| To | ``` var products: [SKProduct] { get } ``` | OS X 10.7 |

Modified [SKReceiptRefreshRequest](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SKReceiptRefreshRequest : SKRequest {     init?(receiptProperties properties: [String : AnyObject])     var receiptProperties: [String : AnyObject]? { get } } ``` |
| To | ``` class SKReceiptRefreshRequest : SKRequest {     init(receiptProperties properties: [String : Any]?)     var receiptProperties: [String : Any]? { get } } ``` |

Modified [SKReceiptRefreshRequest.init(receiptProperties: [String : Any]?)](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-initwithreceiptproperties)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init?(receiptProperties properties: [String : AnyObject]) ``` | OS X 10.10 |
| To | ``` init(receiptProperties properties: [String : Any]?) ``` | OS X 10.9 |

Modified [SKReceiptRefreshRequest.receiptProperties](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506029-receiptproperties)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var receiptProperties: [String : AnyObject]? { get } ``` | OS X 10.10 |
| To | ``` var receiptProperties: [String : Any]? { get } ``` | OS X 10.9 |

Modified [SKRequest](https://developer.apple.com/documentation/storekit/skrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKRequest : NSObject {     unowned(unsafe) var delegate: SKRequestDelegate?     func cancel()     func start() } ``` | -- |
| To | ``` class SKRequest : NSObject {     weak var delegate: SKRequestDelegate?     func cancel()     func start()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension SKRequest : CVarArg { } extension SKRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKRequest.cancel()](https://developer.apple.com/documentation/storekit/skrequest/1385526-cancel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKRequest.delegate](https://developer.apple.com/documentation/storekit/skrequest/1385530-delegate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` unowned(unsafe) var delegate: SKRequestDelegate? ``` | OS X 10.10 |
| To | ``` weak var delegate: SKRequestDelegate? ``` | OS X 10.7 |

Modified [SKRequest.start()](https://developer.apple.com/documentation/storekit/skrequest/1385534-start)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [SKRequestDelegate](https://developer.apple.com/documentation/storekit/skrequestdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKRequestDelegate : NSObjectProtocol {     optional func requestDidFinish(_ request: SKRequest)     optional func request(_ request: SKRequest, didFailWithError error: NSError?) } ``` |
| To | ``` protocol SKRequestDelegate : NSObjectProtocol {     optional func requestDidFinish(_ request: SKRequest)     optional func request(_ request: SKRequest, didFailWithError error: Error) } ``` |

Modified [SKRequestDelegate.request(_: SKRequest, didFailWithError: Error)](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385536-request)

|  | Declaration |
| --- | --- |
| From | ``` optional func request(_ request: SKRequest, didFailWithError error: NSError?) ``` |
| To | ``` optional func request(_ request: SKRequest, didFailWithError error: Error) ``` |

Modified [SKReceiptPropertyIsExpired](https://developer.apple.com/documentation/storekit/skreceiptpropertyisexpired)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.9 |

Modified [SKReceiptPropertyIsRevoked](https://developer.apple.com/documentation/storekit/skreceiptpropertyisrevoked)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.9 |

Modified [SKReceiptPropertyIsVolumePurchase](https://developer.apple.com/documentation/storekit/skreceiptpropertyisvolumepurchase)

|  | Introduction |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.9 |

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
