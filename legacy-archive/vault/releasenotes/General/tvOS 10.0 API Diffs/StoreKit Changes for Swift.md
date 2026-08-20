---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/StoreKit.html
archived_at: '2026-07-18T02:57:56.497816Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# StoreKit Changes for Swift

### StoreKit

Removed [SKCloudServiceCapability.None](https://developer.apple.com/documentation/storekit/skcloudservicecapability/skcloudservicecapabilitynone)Added [SKError [struct]](https://developer.apple.com/documentation/storekit/skerror)Added [SKError.clientInvalid](https://developer.apple.com/documentation/storekit/skerror/2330533-clientinvalid)Added [SKError.cloudServiceNetworkConnectionFailed](https://developer.apple.com/documentation/storekit/skerror/2335082-cloudservicenetworkconnectionfai)Added [SKError.cloudServicePermissionDenied](https://developer.apple.com/documentation/storekit/skerror/2335083-cloudservicepermissiondenied)Added SKError.init(_nsError: NSError)Added [SKError.paymentCancelled](https://developer.apple.com/documentation/storekit/skerror/2330537-paymentcancelled)Added [SKError.paymentInvalid](https://developer.apple.com/documentation/storekit/skerror/2330536-paymentinvalid)Added [SKError.paymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/2330535-paymentnotallowed)Added [SKError.storeProductNotAvailable](https://developer.apple.com/documentation/storekit/skerror/2335084-storeproductnotavailable)Added [SKError.unknown](https://developer.apple.com/documentation/storekit/skerror/2330534-unknown)Modified [NSNotification.Name.SKCloudServiceCapabilitiesDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620626-skcloudservicecapabilitiesdidcha)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKCloudServiceCapabilitiesDidChangeNotification | ``` let SKCloudServiceCapabilitiesDidChangeNotification: String ``` |
| To | SKCloudServiceCapabilitiesDidChange | ``` static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.SKStorefrontIdentifierDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620636-skstorefrontidentifierdidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKStorefrontIdentifierDidChangeNotification | ``` let SKStorefrontIdentifierDidChangeNotification: String ``` |
| To | SKStorefrontIdentifierDidChange | ``` static let SKStorefrontIdentifierDidChange: NSNotification.Name ``` |

Modified [SKCloudServiceAuthorizationStatus [enum]](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum SKCloudServiceAuthorizationStatus : Int {     case NotDetermined     case Denied     case Restricted     case Authorized } ``` |
| To | ``` enum SKCloudServiceAuthorizationStatus : Int {     case notDetermined     case denied     case restricted     case authorized } ``` |

Modified [SKCloudServiceAuthorizationStatus.authorized](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/authorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [SKCloudServiceAuthorizationStatus.denied](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/skcloudserviceauthorizationstatusdenied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [SKCloudServiceAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/notdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [SKCloudServiceAuthorizationStatus.restricted](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/restricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [SKCloudServiceCapability [struct]](https://developer.apple.com/documentation/storekit/skcloudservicecapability)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SKCloudServiceCapability : OptionSetType {     init(rawValue rawValue: UInt)     static var None: SKCloudServiceCapability { get }     static var MusicCatalogPlayback: SKCloudServiceCapability { get }     static var AddToCloudMusicLibrary: SKCloudServiceCapability { get } } ``` | OptionSetType |
| To | ``` struct SKCloudServiceCapability : OptionSet {     init(rawValue rawValue: UInt)     static var none: SKCloudServiceCapability { get }     static var musicCatalogPlayback: SKCloudServiceCapability { get }     static var addToCloudMusicLibrary: SKCloudServiceCapability { get }     func intersect(_ other: SKCloudServiceCapability) -> SKCloudServiceCapability     func exclusiveOr(_ other: SKCloudServiceCapability) -> SKCloudServiceCapability     mutating func unionInPlace(_ other: SKCloudServiceCapability)     mutating func intersectInPlace(_ other: SKCloudServiceCapability)     mutating func exclusiveOrInPlace(_ other: SKCloudServiceCapability)     func isSubsetOf(_ other: SKCloudServiceCapability) -> Bool     func isDisjointWith(_ other: SKCloudServiceCapability) -> Bool     func isSupersetOf(_ other: SKCloudServiceCapability) -> Bool     mutating func subtractInPlace(_ other: SKCloudServiceCapability)     func isStrictSupersetOf(_ other: SKCloudServiceCapability) -> Bool     func isStrictSubsetOf(_ other: SKCloudServiceCapability) -> Bool } extension SKCloudServiceCapability {     func union(_ other: SKCloudServiceCapability) -> SKCloudServiceCapability     func intersection(_ other: SKCloudServiceCapability) -> SKCloudServiceCapability     func symmetricDifference(_ other: SKCloudServiceCapability) -> SKCloudServiceCapability } extension SKCloudServiceCapability {     func contains(_ member: SKCloudServiceCapability) -> Bool     mutating func insert(_ newMember: SKCloudServiceCapability) -> (inserted: Bool, memberAfterInsert: SKCloudServiceCapability)     mutating func remove(_ member: SKCloudServiceCapability) -> SKCloudServiceCapability?     mutating func update(with newMember: SKCloudServiceCapability) -> SKCloudServiceCapability? } extension SKCloudServiceCapability {     convenience init()     mutating func formUnion(_ other: SKCloudServiceCapability)     mutating func formIntersection(_ other: SKCloudServiceCapability)     mutating func formSymmetricDifference(_ other: SKCloudServiceCapability) } extension SKCloudServiceCapability {     convenience init<S : Sequence where S.Iterator.Element == SKCloudServiceCapability>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: SKCloudServiceCapability...)     mutating func subtract(_ other: SKCloudServiceCapability)     func isSubset(of other: SKCloudServiceCapability) -> Bool     func isSuperset(of other: SKCloudServiceCapability) -> Bool     func isDisjoint(with other: SKCloudServiceCapability) -> Bool     func subtracting(_ other: SKCloudServiceCapability) -> SKCloudServiceCapability     var isEmpty: Bool { get }     func isStrictSuperset(of other: SKCloudServiceCapability) -> Bool     func isStrictSubset(of other: SKCloudServiceCapability) -> Bool } ``` | OptionSet |

Modified [SKCloudServiceCapability.addToCloudMusicLibrary](https://developer.apple.com/documentation/storekit/skcloudservicecapability/1620629-addtocloudmusiclibrary)

|  | Declaration |
| --- | --- |
| From | ``` static var AddToCloudMusicLibrary: SKCloudServiceCapability { get } ``` |
| To | ``` static var addToCloudMusicLibrary: SKCloudServiceCapability { get } ``` |

Modified [SKCloudServiceCapability.musicCatalogPlayback](https://developer.apple.com/documentation/storekit/skcloudservicecapability/skcloudservicecapabilitymusiccatalogplayback)

|  | Declaration |
| --- | --- |
| From | ``` static var MusicCatalogPlayback: SKCloudServiceCapability { get } ``` |
| To | ``` static var musicCatalogPlayback: SKCloudServiceCapability { get } ``` |

Modified [SKCloudServiceController](https://developer.apple.com/documentation/storekit/skcloudservicecontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKCloudServiceController : NSObject {     class func authorizationStatus() -> SKCloudServiceAuthorizationStatus     class func requestAuthorization(_ handler: (SKCloudServiceAuthorizationStatus) -> Void)     func requestStorefrontIdentifierWithCompletionHandler(_ completionHandler: (String?, NSError?) -> Void)     func requestCapabilitiesWithCompletionHandler(_ completionHandler: (SKCloudServiceCapability, NSError?) -> Void) } ``` | -- |
| To | ``` class SKCloudServiceController : NSObject {     class func authorizationStatus() -> SKCloudServiceAuthorizationStatus     class func requestAuthorization(_ handler: @escaping (SKCloudServiceAuthorizationStatus) -> Swift.Void)     func requestStorefrontIdentifier(completionHandler completionHandler: @escaping (String?, Error?) -> Swift.Void)     func requestCapabilities(completionHandler completionHandler: @escaping (SKCloudServiceCapability, Error?) -> Swift.Void)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKCloudServiceController : CVarArg { } extension SKCloudServiceController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKCloudServiceController.requestAuthorization(_: (SKCloudServiceAuthorizationStatus) -> Swift.Void) [class]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620609-requestauthorization)

|  | Declaration |
| --- | --- |
| From | ``` class func requestAuthorization(_ handler: (SKCloudServiceAuthorizationStatus) -> Void) ``` |
| To | ``` class func requestAuthorization(_ handler: @escaping (SKCloudServiceAuthorizationStatus) -> Swift.Void) ``` |

Modified [SKCloudServiceController.requestCapabilities(completionHandler: (SKCloudServiceCapability, Error?) -> Swift.Void)](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620610-requestcapabilities)

|  | Declaration |
| --- | --- |
| From | ``` func requestCapabilitiesWithCompletionHandler(_ completionHandler: (SKCloudServiceCapability, NSError?) -> Void) ``` |
| To | ``` func requestCapabilities(completionHandler completionHandler: @escaping (SKCloudServiceCapability, Error?) -> Swift.Void) ``` |

Modified [SKCloudServiceController.requestStorefrontIdentifier(completionHandler: (String?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620618-requeststorefrontidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func requestStorefrontIdentifierWithCompletionHandler(_ completionHandler: (String?, NSError?) -> Void) ``` |
| To | ``` func requestStorefrontIdentifier(completionHandler completionHandler: @escaping (String?, Error?) -> Swift.Void) ``` |

Modified [SKDownload](https://developer.apple.com/documentation/storekit/skdownload)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKDownload : NSObject {     var downloadState: SKDownloadState { get }     var contentLength: Int64 { get }     var contentIdentifier: String { get }     var contentURL: NSURL? { get }     var contentVersion: String { get }     var error: NSError? { get }     var progress: Float { get }     var timeRemaining: NSTimeInterval { get }     var transaction: SKPaymentTransaction { get } } ``` | -- |
| To | ``` class SKDownload : NSObject {     var downloadState: SKDownloadState { get }     var contentLength: Int64 { get }     var contentIdentifier: String { get }     var contentURL: URL? { get }     var contentVersion: String { get }     var error: Error? { get }     var progress: Float { get }     var timeRemaining: TimeInterval { get }     var transaction: SKPaymentTransaction { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKDownload : CVarArg { } extension SKDownload : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` var contentURL: NSURL? { get } ``` |
| To | ``` var contentURL: URL? { get } ``` |

Modified [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [SKDownload.timeRemaining](https://developer.apple.com/documentation/storekit/skdownload/1458943-timeremaining)

|  | Declaration |
| --- | --- |
| From | ``` var timeRemaining: NSTimeInterval { get } ``` |
| To | ``` var timeRemaining: TimeInterval { get } ``` |

Modified [SKDownloadState [enum]](https://developer.apple.com/documentation/storekit/skdownloadstate)

|  | Declaration |
| --- | --- |
| From | ``` enum SKDownloadState : Int {     case Waiting     case Active     case Paused     case Finished     case Failed     case Cancelled } ``` |
| To | ``` enum SKDownloadState : Int {     case waiting     case active     case paused     case finished     case failed     case cancelled } ``` |

Modified [SKDownloadState.active](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstateactive)

|  | Declaration |
| --- | --- |
| From | ``` case Active ``` |
| To | ``` case active ``` |

Modified [SKDownloadState.cancelled](https://developer.apple.com/documentation/storekit/skdownloadstate/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [SKDownloadState.failed](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [SKDownloadState.finished](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefinished)

|  | Declaration |
| --- | --- |
| From | ``` case Finished ``` |
| To | ``` case finished ``` |

Modified [SKDownloadState.paused](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatepaused)

|  | Declaration |
| --- | --- |
| From | ``` case Paused ``` |
| To | ``` case paused ``` |

Modified [SKDownloadState.waiting](https://developer.apple.com/documentation/storekit/skdownloadstate/waiting)

|  | Declaration |
| --- | --- |
| From | ``` case Waiting ``` |
| To | ``` case waiting ``` |

Modified [SKError.Code [enum]](https://developer.apple.com/documentation/storekit/skerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKErrorCode : Int {     case Unknown     case ClientInvalid     case PaymentCancelled     case PaymentInvalid     case PaymentNotAllowed     case StoreProductNotAvailable     case CloudServicePermissionDenied     case CloudServiceNetworkConnectionFailed } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = SKError         case unknown         case clientInvalid         case paymentCancelled         case paymentInvalid         case paymentNotAllowed         case storeProductNotAvailable         case cloudServicePermissionDenied         case cloudServiceNetworkConnectionFailed     } ``` |

Modified [SKError.Code.clientInvalid](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorclientinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case ClientInvalid ``` |
| To | ``` case clientInvalid ``` |

Modified [SKError.Code.cloudServiceNetworkConnectionFailed](https://developer.apple.com/documentation/storekit/skerror/code/cloudservicenetworkconnectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CloudServiceNetworkConnectionFailed ``` |
| To | ``` case cloudServiceNetworkConnectionFailed ``` |

Modified [SKError.Code.cloudServicePermissionDenied](https://developer.apple.com/documentation/storekit/skerror/code/cloudservicepermissiondenied)

|  | Declaration |
| --- | --- |
| From | ``` case CloudServicePermissionDenied ``` |
| To | ``` case cloudServicePermissionDenied ``` |

Modified [SKError.Code.paymentCancelled](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorpaymentcancelled)

|  | Declaration |
| --- | --- |
| From | ``` case PaymentCancelled ``` |
| To | ``` case paymentCancelled ``` |

Modified [SKError.Code.paymentInvalid](https://developer.apple.com/documentation/storekit/skerror/code/paymentinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case PaymentInvalid ``` |
| To | ``` case paymentInvalid ``` |

Modified [SKError.Code.paymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/code/paymentnotallowed)

|  | Declaration |
| --- | --- |
| From | ``` case PaymentNotAllowed ``` |
| To | ``` case paymentNotAllowed ``` |

Modified [SKError.Code.storeProductNotAvailable](https://developer.apple.com/documentation/storekit/skerror/code/storeproductnotavailable)

|  | Declaration |
| --- | --- |
| From | ``` case StoreProductNotAvailable ``` |
| To | ``` case storeProductNotAvailable ``` |

Modified [SKError.Code.unknown](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorunknown)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Unknown ``` | tvOS 9.2 |
| To | ``` case unknown ``` | tvOS 10.0 |

Modified [SKMutablePayment](https://developer.apple.com/documentation/storekit/skmutablepayment)

|  | Declaration |
| --- | --- |
| From | ``` class SKMutablePayment : SKPayment {     var applicationUsername: String     var productIdentifier: String     var quantity: Int     @NSCopying var requestData: NSData?     var simulatesAskToBuyInSandbox: Bool } ``` |
| To | ``` class SKMutablePayment : SKPayment {     var applicationUsername: String     var productIdentifier: String     var quantity: Int     var requestData: Data?     var simulatesAskToBuyInSandbox: Bool } ``` |

Modified [SKMutablePayment.requestData](https://developer.apple.com/documentation/storekit/skmutablepayment/1505974-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var requestData: NSData? ``` |
| To | ``` var requestData: Data? ``` |

Modified [SKPayment](https://developer.apple.com/documentation/storekit/skpayment)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPayment : NSObject, NSCopying, NSMutableCopying {     convenience init(product product: SKProduct)     class func paymentWithProduct(_ product: SKProduct) -> Self     class func paymentWithProductIdentifier(_ identifier: String) -> AnyObject     var productIdentifier: String { get }     @NSCopying var requestData: NSData? { get }     var quantity: Int { get }     var applicationUsername: String? { get }     var simulatesAskToBuyInSandbox: Bool { get } } ``` | NSCopying, NSMutableCopying |
| To | ``` class SKPayment : NSObject, NSCopying, NSMutableCopying {     convenience init(product product: SKProduct)     class func withProduct(_ product: SKProduct) -> Self     class func payment(withProductIdentifier identifier: String) -> Any     var productIdentifier: String { get }     var requestData: Data? { get }     var quantity: Int { get }     var applicationUsername: String? { get }     var simulatesAskToBuyInSandbox: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPayment : CVarArg { } extension SKPayment : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSMutableCopying |

Modified [SKPayment.requestData](https://developer.apple.com/documentation/storekit/skpayment/1506159-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var requestData: NSData? { get } ``` |
| To | ``` var requestData: Data? { get } ``` |

Modified [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPaymentQueue : NSObject {     class func defaultQueue() -> Self     class func canMakePayments() -> Bool     func addPayment(_ payment: SKPayment)     func restoreCompletedTransactions()     func restoreCompletedTransactionsWithApplicationUsername(_ username: String?)     func finishTransaction(_ transaction: SKPaymentTransaction)     func startDownloads(_ downloads: [SKDownload])     func pauseDownloads(_ downloads: [SKDownload])     func resumeDownloads(_ downloads: [SKDownload])     func cancelDownloads(_ downloads: [SKDownload])     func addTransactionObserver(_ observer: SKPaymentTransactionObserver)     func removeTransactionObserver(_ observer: SKPaymentTransactionObserver)     var transactions: [SKPaymentTransaction] { get } } ``` | -- |
| To | ``` class SKPaymentQueue : NSObject {     class func `default`() -> Self     class func canMakePayments() -> Bool     func add(_ payment: SKPayment)     func restoreCompletedTransactions()     func restoreCompletedTransactions(withApplicationUsername username: String?)     func finishTransaction(_ transaction: SKPaymentTransaction)     func start(_ downloads: [SKDownload])     func pause(_ downloads: [SKDownload])     func resume(_ downloads: [SKDownload])     func cancel(_ downloads: [SKDownload])     func add(_ observer: SKPaymentTransactionObserver)     func remove(_ observer: SKPaymentTransactionObserver)     var transactions: [SKPaymentTransaction] { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPaymentQueue : CVarArg { } extension SKPaymentQueue : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKPaymentQueue.add(_: SKPayment)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506036-addpayment)

|  | Declaration |
| --- | --- |
| From | ``` func addPayment(_ payment: SKPayment) ``` |
| To | ``` func add(_ payment: SKPayment) ``` |

Modified [SKPaymentQueue.add(_: SKPaymentTransactionObserver)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506042-addtransactionobserver)

|  | Declaration |
| --- | --- |
| From | ``` func addTransactionObserver(_ observer: SKPaymentTransactionObserver) ``` |
| To | ``` func add(_ observer: SKPaymentTransactionObserver) ``` |

Modified [SKPaymentQueue.cancel(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-canceldownloads)

|  | Declaration |
| --- | --- |
| From | ``` func cancelDownloads(_ downloads: [SKDownload]) ``` |
| To | ``` func cancel(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.default() [class]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505990-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultQueue() -> Self ``` |
| To | ``` class func `default`() -> Self ``` |

Modified [SKPaymentQueue.pause(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pausedownloads)

|  | Declaration |
| --- | --- |
| From | ``` func pauseDownloads(_ downloads: [SKDownload]) ``` |
| To | ``` func pause(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.remove(_: SKPaymentTransactionObserver)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506165-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeTransactionObserver(_ observer: SKPaymentTransactionObserver) ``` |
| To | ``` func remove(_ observer: SKPaymentTransactionObserver) ``` |

Modified [SKPaymentQueue.restoreCompletedTransactions(withApplicationUsername: String?)](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions)

|  | Declaration |
| --- | --- |
| From | ``` func restoreCompletedTransactionsWithApplicationUsername(_ username: String?) ``` |
| To | ``` func restoreCompletedTransactions(withApplicationUsername username: String?) ``` |

Modified [SKPaymentQueue.resume(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume)

|  | Declaration |
| --- | --- |
| From | ``` func resumeDownloads(_ downloads: [SKDownload]) ``` |
| To | ``` func resume(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentQueue.start(_: [SKDownload])](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-startdownloads)

|  | Declaration |
| --- | --- |
| From | ``` func startDownloads(_ downloads: [SKDownload]) ``` |
| To | ``` func start(_ downloads: [SKDownload]) ``` |

Modified [SKPaymentTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPaymentTransaction : NSObject {     var error: NSError? { get }     var originalTransaction: SKPaymentTransaction? { get }     var payment: SKPayment { get }     var downloads: [SKDownload] { get }     var transactionDate: NSDate? { get }     var transactionIdentifier: String? { get }     var transactionReceipt: NSData? { get }     var transactionState: SKPaymentTransactionState { get } } ``` | -- |
| To | ``` class SKPaymentTransaction : NSObject {     var error: Error? { get }     var original: SKPaymentTransaction? { get }     var payment: SKPayment { get }     var downloads: [SKDownload] { get }     var transactionDate: Date? { get }     var transactionIdentifier: String? { get }     var transactionReceipt: Data? { get }     var transactionState: SKPaymentTransactionState { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPaymentTransaction : CVarArg { } extension SKPaymentTransaction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKPaymentTransaction.error](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411269-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [SKPaymentTransaction.original](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411284-originaltransaction)

|  | Declaration |
| --- | --- |
| From | ``` var originalTransaction: SKPaymentTransaction? { get } ``` |
| To | ``` var original: SKPaymentTransaction? { get } ``` |

Modified [SKPaymentTransaction.transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate)

|  | Declaration |
| --- | --- |
| From | ``` var transactionDate: NSDate? { get } ``` |
| To | ``` var transactionDate: Date? { get } ``` |

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

Modified [SKPaymentTransactionState [enum]](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum SKPaymentTransactionState : Int {     case Purchasing     case Purchased     case Failed     case Restored     case Deferred } ``` |
| To | ``` enum SKPaymentTransactionState : Int {     case purchasing     case purchased     case failed     case restored     case deferred } ``` |

Modified [SKPaymentTransactionState.deferred](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred)

|  | Declaration |
| --- | --- |
| From | ``` case Deferred ``` |
| To | ``` case deferred ``` |

Modified [SKPaymentTransactionState.failed](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstatefailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [SKPaymentTransactionState.purchased](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstatepurchased)

|  | Declaration |
| --- | --- |
| From | ``` case Purchased ``` |
| To | ``` case purchased ``` |

Modified [SKPaymentTransactionState.purchasing](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchasing)

|  | Declaration |
| --- | --- |
| From | ``` case Purchasing ``` |
| To | ``` case purchasing ``` |

Modified [SKPaymentTransactionState.restored](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstaterestored)

|  | Declaration |
| --- | --- |
| From | ``` case Restored ``` |
| To | ``` case restored ``` |

Modified [SKProduct](https://developer.apple.com/documentation/storekit/skproduct)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKProduct : NSObject {     var localizedDescription: String { get }     var localizedTitle: String { get }     var price: NSDecimalNumber { get }     var priceLocale: NSLocale { get }     var productIdentifier: String { get }     var downloadable: Bool { get }     var downloadContentLengths: [NSNumber] { get }     var downloadContentVersion: String { get } } ``` | -- |
| To | ``` class SKProduct : NSObject {     var localizedDescription: String { get }     var localizedTitle: String { get }     var price: NSDecimalNumber { get }     var priceLocale: Locale { get }     var productIdentifier: String { get }     var isDownloadable: Bool { get }     var downloadContentLengths: [NSNumber] { get }     var downloadContentVersion: String { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKProduct : CVarArg { } extension SKProduct : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKProduct.isDownloadable](https://developer.apple.com/documentation/storekit/skproduct/1506161-isdownloadable)

|  | Declaration |
| --- | --- |
| From | ``` var downloadable: Bool { get } ``` |
| To | ``` var isDownloadable: Bool { get } ``` |

Modified [SKProduct.priceLocale](https://developer.apple.com/documentation/storekit/skproduct/1506145-pricelocale)

|  | Declaration |
| --- | --- |
| From | ``` var priceLocale: NSLocale { get } ``` |
| To | ``` var priceLocale: Locale { get } ``` |

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
| From | ``` class SKProductsResponse : NSObject {     var products: [SKProduct] { get }     var invalidProductIdentifiers: [String] { get } } ``` | -- |
| To | ``` class SKProductsResponse : NSObject {     var products: [SKProduct] { get }     var invalidProductIdentifiers: [String] { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKProductsResponse : CVarArg { } extension SKProductsResponse : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKReceiptRefreshRequest](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SKReceiptRefreshRequest : SKRequest {     init(receiptProperties properties: [String : AnyObject]?)     var receiptProperties: [String : AnyObject]? { get } } ``` |
| To | ``` class SKReceiptRefreshRequest : SKRequest {     init(receiptProperties properties: [String : Any]?)     var receiptProperties: [String : Any]? { get } } ``` |

Modified [SKReceiptRefreshRequest.init(receiptProperties: [String : Any]?)](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-initwithreceiptproperties)

|  | Declaration |
| --- | --- |
| From | ``` init(receiptProperties properties: [String : AnyObject]?) ``` |
| To | ``` init(receiptProperties properties: [String : Any]?) ``` |

Modified [SKReceiptRefreshRequest.receiptProperties](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506029-receiptproperties)

|  | Declaration |
| --- | --- |
| From | ``` var receiptProperties: [String : AnyObject]? { get } ``` |
| To | ``` var receiptProperties: [String : Any]? { get } ``` |

Modified [SKRequest](https://developer.apple.com/documentation/storekit/skrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKRequest : NSObject {     unowned(unsafe) var delegate: SKRequestDelegate?     func cancel()     func start() } ``` | -- |
| To | ``` class SKRequest : NSObject {     unowned(unsafe) var delegate: SKRequestDelegate?     func cancel()     func start()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKRequest : CVarArg { } extension SKRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKRequestDelegate](https://developer.apple.com/documentation/storekit/skrequestdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKRequestDelegate : NSObjectProtocol {     optional func requestDidFinish(_ request: SKRequest)     optional func request(_ request: SKRequest, didFailWithError error: NSError) } ``` |
| To | ``` protocol SKRequestDelegate : NSObjectProtocol {     optional func requestDidFinish(_ request: SKRequest)     optional func request(_ request: SKRequest, didFailWithError error: Error) } ``` |

Modified [SKRequestDelegate.request(_: SKRequest, didFailWithError: Error)](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385536-request)

|  | Declaration |
| --- | --- |
| From | ``` optional func request(_ request: SKRequest, didFailWithError error: NSError) ``` |
| To | ``` optional func request(_ request: SKRequest, didFailWithError error: Error) ``` |

Modified [SKDownloadTimeRemainingUnknown](https://developer.apple.com/documentation/storekit/skdownloadtimeremainingunknown)

|  | Declaration |
| --- | --- |
| From | ``` var SKDownloadTimeRemainingUnknown: NSTimeInterval ``` |
| To | ``` var SKDownloadTimeRemainingUnknown: TimeInterval ``` |

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
