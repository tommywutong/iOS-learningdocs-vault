---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/TVMLKit.html
archived_at: '2026-07-18T02:57:59.333456Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# TVMLKit Changes for Swift

### TVMLKit

Added [TVElementUpdateType.styles](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/tvelementupdatetypestyles)Added [TVInterfaceCreating.collectionViewCellClass(for: TVViewElement) -> Swift.AnyClass?](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/1651061-collectionviewcellclassforelemen)Added [TVViewElementStyle.focusMargin](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle/1650988-focusmargin)Modified [TVApplicationController](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVApplicationController : NSObject {     init(context context: TVApplicationControllerContext, window window: UIWindow?, delegate delegate: TVApplicationControllerDelegate?)     convenience init()     var window: UIWindow? { get }     var context: TVApplicationControllerContext { get }     weak var delegate: TVApplicationControllerDelegate? { get }     var navigationController: UINavigationController { get }     func evaluateInJavaScriptContext(_ evaluation: (JSContext) -> Void, completion completion: ((Bool) -> Void)?)     func stop() } ``` | -- |
| To | ``` class TVApplicationController : NSObject {     init(context context: TVApplicationControllerContext, window window: UIWindow?, delegate delegate: TVApplicationControllerDelegate?)     convenience init()     var window: UIWindow? { get }     var context: TVApplicationControllerContext { get }     weak var delegate: TVApplicationControllerDelegate? { get }     var navigationController: UINavigationController { get }     func evaluate(inJavaScriptContext evaluation: @escaping (JSContext) -> Swift.Void, completion completion: (@escaping (Bool) -> Swift.Void)? = nil)     func stop()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVApplicationController : CVarArg { } extension TVApplicationController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TVApplicationController.evaluate(inJavaScriptContext: (JSContext) -> Swift.Void, completion: ( (Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/1627498-evaluateinjavascriptcontext)

|  | Declaration |
| --- | --- |
| From | ``` func evaluateInJavaScriptContext(_ evaluation: (JSContext) -> Void, completion completion: ((Bool) -> Void)?) ``` |
| To | ``` func evaluate(inJavaScriptContext evaluation: @escaping (JSContext) -> Swift.Void, completion completion: (@escaping (Bool) -> Swift.Void)? = nil) ``` |

Modified [TVApplicationControllerContext](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVApplicationControllerContext : NSObject, NSCopying {     @NSCopying var javaScriptApplicationURL: NSURL     var storageIdentifier: String?     var launchOptions: [String : AnyObject] } ``` | NSCopying |
| To | ``` class TVApplicationControllerContext : NSObject, NSCopying {     var javaScriptApplicationURL: URL     var storageIdentifier: String?     var launchOptions: [String : Any]     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVApplicationControllerContext : CVarArg { } extension TVApplicationControllerContext : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [TVApplicationControllerContext.javaScriptApplicationURL](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/1627494-javascriptapplicationurl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var javaScriptApplicationURL: NSURL ``` |
| To | ``` var javaScriptApplicationURL: URL ``` |

Modified [TVApplicationControllerContext.launchOptions](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext/1627492-launchoptions)

|  | Declaration |
| --- | --- |
| From | ``` var launchOptions: [String : AnyObject] ``` |
| To | ``` var launchOptions: [String : Any] ``` |

Modified [TVApplicationControllerDelegate](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol TVApplicationControllerDelegate : NSObjectProtocol {     optional func appController(_ appController: TVApplicationController, evaluateAppJavaScriptInContext jsContext: JSContext)     optional func appController(_ appController: TVApplicationController, didFinishLaunchingWithOptions options: [String : AnyObject]?)     optional func appController(_ appController: TVApplicationController, didFailWithError error: NSError)     optional func appController(_ appController: TVApplicationController, didStopWithOptions options: [String : AnyObject]?) } ``` |
| To | ``` protocol TVApplicationControllerDelegate : NSObjectProtocol {     optional func appController(_ appController: TVApplicationController, evaluateAppJavaScriptIn jsContext: JSContext)     optional func appController(_ appController: TVApplicationController, didFinishLaunching options: [String : Any]?)     optional func appController(_ appController: TVApplicationController, didFail error: Error)     optional func appController(_ appController: TVApplicationController, didStop options: [String : Any]?) } ``` |

Modified [TVApplicationControllerDelegate.appController(_: TVApplicationController, didFail: Error)](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/1627500-appcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func appController(_ appController: TVApplicationController, didFailWithError error: NSError) ``` |
| To | ``` optional func appController(_ appController: TVApplicationController, didFail error: Error) ``` |

Modified [TVApplicationControllerDelegate.appController(_: TVApplicationController, didFinishLaunching: [String : Any]?)](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/1627503-appcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func appController(_ appController: TVApplicationController, didFinishLaunchingWithOptions options: [String : AnyObject]?) ``` |
| To | ``` optional func appController(_ appController: TVApplicationController, didFinishLaunching options: [String : Any]?) ``` |

Modified [TVApplicationControllerDelegate.appController(_: TVApplicationController, didStop: [String : Any]?)](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/1627508-appcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func appController(_ appController: TVApplicationController, didStopWithOptions options: [String : AnyObject]?) ``` |
| To | ``` optional func appController(_ appController: TVApplicationController, didStop options: [String : Any]?) ``` |

Modified [TVApplicationControllerDelegate.appController(_: TVApplicationController, evaluateAppJavaScriptIn: JSContext)](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollerdelegate/1627506-appcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func appController(_ appController: TVApplicationController, evaluateAppJavaScriptInContext jsContext: JSContext) ``` |
| To | ``` optional func appController(_ appController: TVApplicationController, evaluateAppJavaScriptIn jsContext: JSContext) ``` |

Modified [TVColor](https://developer.apple.com/documentation/tvmlkit/tvcolor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVColor : NSObject, NSCopying {     var colorType: TVColorType { get }     var color: UIColor? { get }     var gradientColors: [UIColor]? { get }     var gradientPoints: [NSNumber]? { get } } ``` | NSCopying |
| To | ``` class TVColor : NSObject, NSCopying {     var colorType: TVColorType { get }     var color: UIColor? { get }     var gradientColors: [UIColor]? { get }     var gradientPoints: [NSNumber]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVColor : CVarArg { } extension TVColor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [TVColorType [enum]](https://developer.apple.com/documentation/tvmlkit/tvcolortype)

|  | Declaration |
| --- | --- |
| From | ``` enum TVColorType : Int {     case None     case Plain     case LinearGradientTopToBottom     case LinearGradientLeftToRight } ``` |
| To | ``` enum TVColorType : Int {     case none     case plain     case linearGradientTopToBottom     case linearGradientLeftToRight } ``` |

Modified [TVColorType.linearGradientLeftToRight](https://developer.apple.com/documentation/tvmlkit/tvcolortype/lineargradientlefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case LinearGradientLeftToRight ``` |
| To | ``` case linearGradientLeftToRight ``` |

Modified [TVColorType.linearGradientTopToBottom](https://developer.apple.com/documentation/tvmlkit/tvcolortype/tvcolortypelineargradienttoptobottom)

|  | Declaration |
| --- | --- |
| From | ``` case LinearGradientTopToBottom ``` |
| To | ``` case linearGradientTopToBottom ``` |

Modified [TVColorType.none](https://developer.apple.com/documentation/tvmlkit/tvcolortype/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [TVColorType.plain](https://developer.apple.com/documentation/tvmlkit/tvcolortype/tvcolortypeplain)

|  | Declaration |
| --- | --- |
| From | ``` case Plain ``` |
| To | ``` case plain ``` |

Modified [TVElementAlignment [enum]](https://developer.apple.com/documentation/tvmlkit/tvelementalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum TVElementAlignment : Int {     case Undefined     case Left     case Center     case Right } ``` |
| To | ``` enum TVElementAlignment : Int {     case undefined     case left     case center     case right } ``` |

Modified [TVElementAlignment.center](https://developer.apple.com/documentation/tvmlkit/tvelementalignment/tvelementalignmentcenter)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [TVElementAlignment.left](https://developer.apple.com/documentation/tvmlkit/tvelementalignment/tvelementalignmentleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [TVElementAlignment.right](https://developer.apple.com/documentation/tvmlkit/tvelementalignment/right)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [TVElementAlignment.undefined](https://developer.apple.com/documentation/tvmlkit/tvelementalignment/tvelementalignmentundefined)

|  | Declaration |
| --- | --- |
| From | ``` case Undefined ``` |
| To | ``` case undefined ``` |

Modified [TVElementContentAlignment [enum]](https://developer.apple.com/documentation/tvmlkit/tvelementcontentalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum TVElementContentAlignment : Int {     case Undefined     case Top     case Center     case Bottom } ``` |
| To | ``` enum TVElementContentAlignment : Int {     case undefined     case top     case center     case bottom } ``` |

Modified [TVElementContentAlignment.bottom](https://developer.apple.com/documentation/tvmlkit/tvelementcontentalignment/bottom)

|  | Declaration |
| --- | --- |
| From | ``` case Bottom ``` |
| To | ``` case bottom ``` |

Modified [TVElementContentAlignment.center](https://developer.apple.com/documentation/tvmlkit/tvelementcontentalignment/tvelementcontentalignmentcenter)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [TVElementContentAlignment.top](https://developer.apple.com/documentation/tvmlkit/tvelementcontentalignment/tvelementcontentalignmenttop)

|  | Declaration |
| --- | --- |
| From | ``` case Top ``` |
| To | ``` case top ``` |

Modified [TVElementContentAlignment.undefined](https://developer.apple.com/documentation/tvmlkit/tvelementcontentalignment/undefined)

|  | Declaration |
| --- | --- |
| From | ``` case Undefined ``` |
| To | ``` case undefined ``` |

Modified [TVElementEventType [enum]](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype)

|  | Declaration |
| --- | --- |
| From | ``` enum TVElementEventType : Int {     case Play     case Select     case HoldSelect     case Highlight     case Change } ``` |
| To | ``` enum TVElementEventType : Int {     case play     case select     case holdSelect     case highlight     case change } ``` |

Modified [TVElementEventType.change](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype/tvelementeventtypechange)

|  | Declaration |
| --- | --- |
| From | ``` case Change ``` |
| To | ``` case change ``` |

Modified [TVElementEventType.highlight](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype/highlight)

|  | Declaration |
| --- | --- |
| From | ``` case Highlight ``` |
| To | ``` case highlight ``` |

Modified [TVElementEventType.holdSelect](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype/holdselect)

|  | Declaration |
| --- | --- |
| From | ``` case HoldSelect ``` |
| To | ``` case holdSelect ``` |

Modified [TVElementEventType.play](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype/play)

|  | Declaration |
| --- | --- |
| From | ``` case Play ``` |
| To | ``` case play ``` |

Modified [TVElementEventType.select](https://developer.apple.com/documentation/tvmlkit/tvelementeventtype/tvelementeventtypeselect)

|  | Declaration |
| --- | --- |
| From | ``` case Select ``` |
| To | ``` case select ``` |

Modified [TVElementFactory](https://developer.apple.com/documentation/tvmlkit/tvelementfactory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVElementFactory : NSObject {     class func registerViewElementClass(_ elementClass: AnyClass, forElementName elementName: String) } ``` | -- |
| To | ``` class TVElementFactory : NSObject {     class func registerViewElementClass(_ elementClass: Swift.AnyClass, elementName elementName: String)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVElementFactory : CVarArg { } extension TVElementFactory : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TVElementFactory.registerViewElementClass(_: Swift.AnyClass, elementName: String) [class]](https://developer.apple.com/documentation/tvmlkit/tvelementfactory/1627637-registerviewelementclass)

|  | Declaration |
| --- | --- |
| From | ``` class func registerViewElementClass(_ elementClass: AnyClass, forElementName elementName: String) ``` |
| To | ``` class func registerViewElementClass(_ elementClass: Swift.AnyClass, elementName elementName: String) ``` |

Modified [TVElementPosition [enum]](https://developer.apple.com/documentation/tvmlkit/tvelementposition)

|  | Declaration |
| --- | --- |
| From | ``` enum TVElementPosition : Int {     case Undefined     case Center     case Top     case Bottom     case Left     case Right     case TopLeft     case TopRight     case BottomLeft     case BottomRight     case Header     case Footer } ``` |
| To | ``` enum TVElementPosition : Int {     case undefined     case center     case top     case bottom     case left     case right     case topLeft     case topRight     case bottomLeft     case bottomRight     case header     case footer } ``` |

Modified [TVElementPosition.bottom](https://developer.apple.com/documentation/tvmlkit/tvelementposition/tvelementpositionbottom)

|  | Declaration |
| --- | --- |
| From | ``` case Bottom ``` |
| To | ``` case bottom ``` |

Modified [TVElementPosition.bottomLeft](https://developer.apple.com/documentation/tvmlkit/tvelementposition/tvelementpositionbottomleft)

|  | Declaration |
| --- | --- |
| From | ``` case BottomLeft ``` |
| To | ``` case bottomLeft ``` |

Modified [TVElementPosition.bottomRight](https://developer.apple.com/documentation/tvmlkit/tvelementposition/tvelementpositionbottomright)

|  | Declaration |
| --- | --- |
| From | ``` case BottomRight ``` |
| To | ``` case bottomRight ``` |

Modified [TVElementPosition.center](https://developer.apple.com/documentation/tvmlkit/tvelementposition/center)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [TVElementPosition.footer](https://developer.apple.com/documentation/tvmlkit/tvelementposition/footer)

|  | Declaration |
| --- | --- |
| From | ``` case Footer ``` |
| To | ``` case footer ``` |

Modified [TVElementPosition.header](https://developer.apple.com/documentation/tvmlkit/tvelementposition/header)

|  | Declaration |
| --- | --- |
| From | ``` case Header ``` |
| To | ``` case header ``` |

Modified [TVElementPosition.left](https://developer.apple.com/documentation/tvmlkit/tvelementposition/left)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [TVElementPosition.right](https://developer.apple.com/documentation/tvmlkit/tvelementposition/right)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [TVElementPosition.top](https://developer.apple.com/documentation/tvmlkit/tvelementposition/top)

|  | Declaration |
| --- | --- |
| From | ``` case Top ``` |
| To | ``` case top ``` |

Modified [TVElementPosition.topLeft](https://developer.apple.com/documentation/tvmlkit/tvelementposition/tvelementpositiontopleft)

|  | Declaration |
| --- | --- |
| From | ``` case TopLeft ``` |
| To | ``` case topLeft ``` |

Modified [TVElementPosition.topRight](https://developer.apple.com/documentation/tvmlkit/tvelementposition/topright)

|  | Declaration |
| --- | --- |
| From | ``` case TopRight ``` |
| To | ``` case topRight ``` |

Modified [TVElementPosition.undefined](https://developer.apple.com/documentation/tvmlkit/tvelementposition/undefined)

|  | Declaration |
| --- | --- |
| From | ``` case Undefined ``` |
| To | ``` case undefined ``` |

Modified [TVElementResettableProperty [enum]](https://developer.apple.com/documentation/tvmlkit/tvelementresettableproperty)

|  | Declaration |
| --- | --- |
| From | ``` enum TVElementResettableProperty : Int {     case UpdateType     case AutoHighlightIdentifier } ``` |
| To | ``` enum TVElementResettableProperty : Int {     case updateType     case autoHighlightIdentifier } ``` |

Modified [TVElementResettableProperty.autoHighlightIdentifier](https://developer.apple.com/documentation/tvmlkit/tvelementresettableproperty/tvelementresettablepropertyautohighlightidentifier)

|  | Declaration |
| --- | --- |
| From | ``` case AutoHighlightIdentifier ``` |
| To | ``` case autoHighlightIdentifier ``` |

Modified [TVElementResettableProperty.updateType](https://developer.apple.com/documentation/tvmlkit/tvelementresettableproperty/tvelementresettablepropertyupdatetype)

|  | Declaration |
| --- | --- |
| From | ``` case UpdateType ``` |
| To | ``` case updateType ``` |

Modified [TVElementUpdateType [enum]](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype)

|  | Declaration |
| --- | --- |
| From | ``` enum TVElementUpdateType : Int {     case None     case Subtree     case Children     case `Self` } ``` |
| To | ``` enum TVElementUpdateType : Int {     case none     case subtree     case children     case node     case styles } ``` |

Modified [TVElementUpdateType.children](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/tvelementupdatetypechildren)

|  | Declaration |
| --- | --- |
| From | ``` case Children ``` |
| To | ``` case children ``` |

Modified [TVElementUpdateType.node](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/node)

|  | Declaration |
| --- | --- |
| From | ``` case `Self` ``` |
| To | ``` case node ``` |

Modified [TVElementUpdateType.none](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/tvelementupdatetypenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [TVElementUpdateType.subtree](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/tvelementupdatetypesubtree)

|  | Declaration |
| --- | --- |
| From | ``` case Subtree ``` |
| To | ``` case subtree ``` |

Modified [TVImageElement](https://developer.apple.com/documentation/tvmlkit/tvimageelement)

|  | Declaration |
| --- | --- |
| From | ``` class TVImageElement : TVViewElement {     var URL: NSURL? { get }     var srcset: [String : NSURL]? { get }     var imageType: TVImageType { get } } ``` |
| To | ``` class TVImageElement : TVViewElement {     var url: URL? { get }     var srcset: [String : URL]? { get }     var imageType: TVImageType { get } } ``` |

Modified [TVImageElement.srcset](https://developer.apple.com/documentation/tvmlkit/tvimageelement/1627694-srcset)

|  | Declaration |
| --- | --- |
| From | ``` var srcset: [String : NSURL]? { get } ``` |
| To | ``` var srcset: [String : URL]? { get } ``` |

Modified [TVImageElement.url](https://developer.apple.com/documentation/tvmlkit/tvimageelement/1627699-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL? { get } ``` |
| To | ``` var url: URL? { get } ``` |

Modified [TVImageType [enum]](https://developer.apple.com/documentation/tvmlkit/tvimagetype)

|  | Declaration |
| --- | --- |
| From | ``` enum TVImageType : Int {     case Image     case Fullscreen     case Decoration     case Hero } ``` |
| To | ``` enum TVImageType : Int {     case image     case fullscreen     case decoration     case hero } ``` |

Modified [TVImageType.decoration](https://developer.apple.com/documentation/tvmlkit/tvimagetype/decoration)

|  | Declaration |
| --- | --- |
| From | ``` case Decoration ``` |
| To | ``` case decoration ``` |

Modified [TVImageType.fullscreen](https://developer.apple.com/documentation/tvmlkit/tvimagetype/fullscreen)

|  | Declaration |
| --- | --- |
| From | ``` case Fullscreen ``` |
| To | ``` case fullscreen ``` |

Modified [TVImageType.hero](https://developer.apple.com/documentation/tvmlkit/tvimagetype/hero)

|  | Declaration |
| --- | --- |
| From | ``` case Hero ``` |
| To | ``` case hero ``` |

Modified [TVImageType.image](https://developer.apple.com/documentation/tvmlkit/tvimagetype/image)

|  | Declaration |
| --- | --- |
| From | ``` case Image ``` |
| To | ``` case image ``` |

Modified [TVInterfaceCreating](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating)

|  | Declaration |
| --- | --- |
| From | ``` protocol TVInterfaceCreating : NSObjectProtocol {     optional func viewForElement(_ element: TVViewElement, existingView existingView: UIView?) -> UIView?     optional func viewControllerForElement(_ element: TVViewElement, existingViewController existingViewController: UIViewController?) -> UIViewController?     optional func URLForResource(_ resourceName: String) -> NSURL?     optional func imageForResource(_ resourceName: String) -> UIImage? } ``` |
| To | ``` protocol TVInterfaceCreating : NSObjectProtocol {     optional func makeView(element element: TVViewElement, existingView existingView: UIView?) -> UIView?     optional func makeViewController(element element: TVViewElement, existingViewController existingViewController: UIViewController?) -> UIViewController?     optional func resourceURL(name resourceName: String) -> URL?     optional func resourceImage(name resourceName: String) -> UIImage?     optional func collectionViewCellClass(for element: TVViewElement) -> Swift.AnyClass? } ``` |

Modified [TVInterfaceCreating.makeView(element: TVViewElement, existingView: UIView?) -> UIView?](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/1627683-viewforelement)

|  | Declaration |
| --- | --- |
| From | ``` optional func viewForElement(_ element: TVViewElement, existingView existingView: UIView?) -> UIView? ``` |
| To | ``` optional func makeView(element element: TVViewElement, existingView existingView: UIView?) -> UIView? ``` |

Modified [TVInterfaceCreating.makeViewController(element: TVViewElement, existingViewController: UIViewController?) -> UIViewController?](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/1627678-viewcontrollerforelement)

|  | Declaration |
| --- | --- |
| From | ``` optional func viewControllerForElement(_ element: TVViewElement, existingViewController existingViewController: UIViewController?) -> UIViewController? ``` |
| To | ``` optional func makeViewController(element element: TVViewElement, existingViewController existingViewController: UIViewController?) -> UIViewController? ``` |

Modified [TVInterfaceCreating.resourceImage(name: String) -> UIImage?](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/1627677-resourceimage)

|  | Declaration |
| --- | --- |
| From | ``` optional func imageForResource(_ resourceName: String) -> UIImage? ``` |
| To | ``` optional func resourceImage(name resourceName: String) -> UIImage? ``` |

Modified [TVInterfaceCreating.resourceURL(name: String) -> URL?](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/1627676-resourceurl)

|  | Declaration |
| --- | --- |
| From | ``` optional func URLForResource(_ resourceName: String) -> NSURL? ``` |
| To | ``` optional func resourceURL(name resourceName: String) -> URL? ``` |

Modified [TVInterfaceFactory](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVInterfaceFactory : NSObject, TVInterfaceCreating {     class func sharedInterfaceFactory() -> Self     var extendedInterfaceCreator: TVInterfaceCreating? } ``` | TVInterfaceCreating |
| To | ``` class TVInterfaceFactory : NSObject, TVInterfaceCreating {     class func shared() -> Self     var extendedInterfaceCreator: TVInterfaceCreating?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVInterfaceFactory : CVarArg { } extension TVInterfaceFactory : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, TVInterfaceCreating |

Modified [TVInterfaceFactory.shared() -> Self [class]](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory/1627679-sharedinterfacefactory)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedInterfaceFactory() -> Self ``` |
| To | ``` class func shared() -> Self ``` |

Modified [TVMLKitError [enum]](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror)

|  | Declaration |
| --- | --- |
| From | ``` enum TVMLKitError : Int {     case Unknown     case InternetUnavailable     case FailedToLaunch     case Last } ``` |
| To | ``` enum TVMLKitError : Int {     case unknown     case internetUnavailable     case failedToLaunch     case last } ``` |

Modified [TVMLKitError.failedToLaunch](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror/failedtolaunch)

|  | Declaration |
| --- | --- |
| From | ``` case FailedToLaunch ``` |
| To | ``` case failedToLaunch ``` |

Modified [TVMLKitError.internetUnavailable](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror/tvmlkiterrorinternetunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case InternetUnavailable ``` |
| To | ``` case internetUnavailable ``` |

Modified [TVMLKitError.last](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror/tvmlkiterrorlast)

|  | Declaration |
| --- | --- |
| From | ``` case Last ``` |
| To | ``` case last ``` |

Modified [TVMLKitError.unknown](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror/tvmlkiterrorunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [TVStyleFactory](https://developer.apple.com/documentation/tvmlkit/tvstylefactory)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVStyleFactory : NSObject {     class func registerStyle(_ styleName: String, withType type: TVViewElementStyleType, inherited inherited: Bool) } ``` | -- |
| To | ``` class TVStyleFactory : NSObject {     class func registerStyleName(_ styleName: String, type type: TVViewElementStyleType, inherited inherited: Bool)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVStyleFactory : CVarArg { } extension TVStyleFactory : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TVStyleFactory.registerStyleName(_: String, type: TVViewElementStyleType, inherited: Bool) [class]](https://developer.apple.com/documentation/tvmlkit/tvstylefactory/1627567-registerstyle)

|  | Declaration |
| --- | --- |
| From | ``` class func registerStyle(_ styleName: String, withType type: TVViewElementStyleType, inherited inherited: Bool) ``` |
| To | ``` class func registerStyleName(_ styleName: String, type type: TVViewElementStyleType, inherited inherited: Bool) ``` |

Modified [TVTextElement](https://developer.apple.com/documentation/tvmlkit/tvtextelement)

|  | Declaration |
| --- | --- |
| From | ``` class TVTextElement : TVViewElement {     var attributedText: NSAttributedString? { get }     var textStyle: TVTextElementStyle { get }     func attributedStringWithFont(_ font: UIFont) -> NSAttributedString     func attributedStringWithFont(_ font: UIFont, foregroundColor foregroundColor: UIColor?, textAlignment alignment: NSTextAlignment) -> NSAttributedString } ``` |
| To | ``` class TVTextElement : TVViewElement {     var attributedString: NSAttributedString? { get }     var textStyle: TVTextElementStyle { get }     func makeAttributedString(font font: UIFont) -> NSAttributedString     func makeAttributedString(font font: UIFont, foregroundColor foregroundColor: UIColor?, textAlignment alignment: NSTextAlignment) -> NSAttributedString } ``` |

Modified [TVTextElement.attributedString](https://developer.apple.com/documentation/tvmlkit/tvtextelement/1627620-attributedstring)

|  | Declaration |
| --- | --- |
| From | ``` var attributedText: NSAttributedString? { get } ``` |
| To | ``` var attributedString: NSAttributedString? { get } ``` |

Modified [TVTextElement.makeAttributedString(font: UIFont) -> NSAttributedString](https://developer.apple.com/documentation/tvmlkit/tvtextelement/1627616-makeattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` func attributedStringWithFont(_ font: UIFont) -> NSAttributedString ``` |
| To | ``` func makeAttributedString(font font: UIFont) -> NSAttributedString ``` |

Modified [TVTextElement.makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment: NSTextAlignment) -> NSAttributedString](https://developer.apple.com/documentation/tvmlkit/tvtextelement/1627622-makeattributedstring)

|  | Declaration |
| --- | --- |
| From | ``` func attributedStringWithFont(_ font: UIFont, foregroundColor foregroundColor: UIColor?, textAlignment alignment: NSTextAlignment) -> NSAttributedString ``` |
| To | ``` func makeAttributedString(font font: UIFont, foregroundColor foregroundColor: UIColor?, textAlignment alignment: NSTextAlignment) -> NSAttributedString ``` |

Modified [TVTextElementStyle [enum]](https://developer.apple.com/documentation/tvmlkit/tvtextelementstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum TVTextElementStyle : Int {     case None     case Title     case Subtitle     case Description     case Decoration } ``` |
| To | ``` enum TVTextElementStyle : Int {     case none     case title     case subtitle     case description     case decoration } ``` |

Modified [TVTextElementStyle.decoration](https://developer.apple.com/documentation/tvmlkit/tvtextelementstyle/tvtextelementstyledecoration)

|  | Declaration |
| --- | --- |
| From | ``` case Decoration ``` |
| To | ``` case decoration ``` |

Modified [TVTextElementStyle.description](https://developer.apple.com/documentation/tvmlkit/tvtextelementstyle/tvtextelementstyledescription)

|  | Declaration |
| --- | --- |
| From | ``` case Description ``` |
| To | ``` case description ``` |

Modified [TVTextElementStyle.none](https://developer.apple.com/documentation/tvmlkit/tvtextelementstyle/tvtextelementstylenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [TVTextElementStyle.subtitle](https://developer.apple.com/documentation/tvmlkit/tvtextelementstyle/subtitle)

|  | Declaration |
| --- | --- |
| From | ``` case Subtitle ``` |
| To | ``` case subtitle ``` |

Modified [TVTextElementStyle.title](https://developer.apple.com/documentation/tvmlkit/tvtextelementstyle/title)

|  | Declaration |
| --- | --- |
| From | ``` case Title ``` |
| To | ``` case title ``` |

Modified [TVViewElement](https://developer.apple.com/documentation/tvmlkit/tvviewelement)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVViewElement : NSObject, NSCopying {     var elementIdentifier: String { get }     var elementName: String { get }     weak var parentViewElement: TVViewElement? { get }     var childViewElements: [TVViewElement]? { get }     var attributes: [String : String]? { get }     var style: TVViewElementStyle? { get }     var autoHighlightIdentifier: String? { get }     var disabled: Bool     var updateType: TVElementUpdateType { get }     func resetProperty(_ resettableProperty: TVElementResettableProperty)     func dispatchEventOfType(_ type: TVElementEventType, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : AnyObject]?, completion completion: ((Bool, Bool) -> Void)?)     func dispatchEventWithName(_ eventName: String, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : AnyObject]?, completion completion: ((Bool, Bool) -> Void)?) } ``` | NSCopying |
| To | ``` class TVViewElement : NSObject, NSCopying {     var identifier: String { get }     var name: String { get }     weak var parent: TVViewElement? { get }     var children: [TVViewElement]? { get }     var attributes: [String : String]? { get }     var style: TVViewElementStyle? { get }     var autoHighlightIdentifier: String? { get }     var isDisabled: Bool     var updateType: TVElementUpdateType { get }     func resetProperty(_ resettableProperty: TVElementResettableProperty)     func dispatchEvent(type type: TVElementEventType, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : Any]?, completion completion: (@escaping (Bool, Bool) -> Swift.Void)? = nil)     func dispatchEvent(name eventName: String, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : Any]?, completion completion: (@escaping (Bool, Bool) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVViewElement : CVarArg { } extension TVViewElement : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [TVViewElement.children](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627656-childviewelements)

|  | Declaration |
| --- | --- |
| From | ``` var childViewElements: [TVViewElement]? { get } ``` |
| To | ``` var children: [TVViewElement]? { get } ``` |

Modified [TVViewElement.dispatchEvent(name: String, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ( (Bool, Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627672-dispatchevent)

|  | Declaration |
| --- | --- |
| From | ``` func dispatchEventWithName(_ eventName: String, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : AnyObject]?, completion completion: ((Bool, Bool) -> Void)?) ``` |
| To | ``` func dispatchEvent(name eventName: String, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : Any]?, completion completion: (@escaping (Bool, Bool) -> Swift.Void)? = nil) ``` |

Modified [TVViewElement.dispatchEvent(type: TVElementEventType, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ( (Bool, Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627670-dispatchevent)

|  | Declaration |
| --- | --- |
| From | ``` func dispatchEventOfType(_ type: TVElementEventType, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : AnyObject]?, completion completion: ((Bool, Bool) -> Void)?) ``` |
| To | ``` func dispatchEvent(type type: TVElementEventType, canBubble canBubble: Bool, cancellable isCancellable: Bool, extraInfo extraInfo: [String : Any]?, completion completion: (@escaping (Bool, Bool) -> Swift.Void)? = nil) ``` |

Modified [TVViewElement.identifier](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627667-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var elementIdentifier: String { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [TVViewElement.isDisabled](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627650-isdisabled)

|  | Declaration |
| --- | --- |
| From | ``` var disabled: Bool ``` |
| To | ``` var isDisabled: Bool ``` |

Modified [TVViewElement.name](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627655-elementname)

|  | Declaration |
| --- | --- |
| From | ``` var elementName: String { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [TVViewElement.parent](https://developer.apple.com/documentation/tvmlkit/tvviewelement/1627657-parent)

|  | Declaration |
| --- | --- |
| From | ``` weak var parentViewElement: TVViewElement? { get } ``` |
| To | ``` weak var parent: TVViewElement? { get } ``` |

Modified [TVViewElementStyle](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TVViewElementStyle : NSObject, NSCopying {     func valueForStyleProperty(_ name: String) -> AnyObject?     var backgroundColor: TVColor? { get }     var color: TVColor? { get }     var fontSize: CGFloat { get }     var fontWeight: String? { get }     var height: CGFloat { get }     var margin: UIEdgeInsets { get }     var maxHeight: CGFloat { get }     var maxWidth: CGFloat { get }     var minHeight: CGFloat { get }     var minWidth: CGFloat { get }     var padding: UIEdgeInsets { get }     var textAlignment: NSTextAlignment { get }     var width: CGFloat { get }     var alignment: TVElementAlignment { get }     var contentAlignment: TVElementContentAlignment { get }     var highlightColor: TVColor? { get }     var imageTreatmentName: String? { get }     var interitemSpacing: CGFloat { get }     var textHighlightStyle: String? { get }     var textMinimumScaleFactor: CGFloat { get }     var position: TVElementPosition { get }     var ratingStyle: String? { get }     var maxTextLines: Int { get }     var textStyle: String? { get }     var tintColor: TVColor? { get } } ``` | NSCopying |
| To | ``` class TVViewElementStyle : NSObject, NSCopying {     func value(propertyName name: String) -> Any?     var backgroundColor: TVColor? { get }     var color: TVColor? { get }     var fontSize: CGFloat { get }     var fontWeight: String? { get }     var height: CGFloat { get }     var margin: UIEdgeInsets { get }     var focusMargin: UIEdgeInsets { get }     var maxHeight: CGFloat { get }     var maxWidth: CGFloat { get }     var minHeight: CGFloat { get }     var minWidth: CGFloat { get }     var padding: UIEdgeInsets { get }     var textAlignment: NSTextAlignment { get }     var width: CGFloat { get }     var alignment: TVElementAlignment { get }     var contentAlignment: TVElementContentAlignment { get }     var highlightColor: TVColor? { get }     var imageTreatmentName: String? { get }     var interitemSpacing: CGFloat { get }     var textHighlightStyle: String? { get }     var textMinimumScaleFactor: CGFloat { get }     var position: TVElementPosition { get }     var ratingStyle: String? { get }     var maxTextLines: Int { get }     var textStyle: String? { get }     var tintColor: TVColor? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension TVViewElementStyle : CVarArg { } extension TVViewElementStyle : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [TVViewElementStyle.value(propertyName: String) -> Any?](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle/1627709-valueforstyleproperty)

|  | Declaration |
| --- | --- |
| From | ``` func valueForStyleProperty(_ name: String) -> AnyObject? ``` |
| To | ``` func value(propertyName name: String) -> Any? ``` |

Modified [TVViewElementStyleType [enum]](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype)

|  | Declaration |
| --- | --- |
| From | ``` enum TVViewElementStyleType : Int {     case Integer     case Double     case Point     case String     case Color     case URL     case Transform     case EdgeInsets } ``` |
| To | ``` enum TVViewElementStyleType : Int {     case integer     case double     case point     case string     case color     case URL     case transform     case edgeInsets } ``` |

Modified [TVViewElementStyleType.color](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/color)

|  | Declaration |
| --- | --- |
| From | ``` case Color ``` |
| To | ``` case color ``` |

Modified [TVViewElementStyleType.double](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/double)

|  | Declaration |
| --- | --- |
| From | ``` case Double ``` |
| To | ``` case double ``` |

Modified [TVViewElementStyleType.edgeInsets](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/tvviewelementstyletypeedgeinsets)

|  | Declaration |
| --- | --- |
| From | ``` case EdgeInsets ``` |
| To | ``` case edgeInsets ``` |

Modified [TVViewElementStyleType.integer](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/tvviewelementstyletypeinteger)

|  | Declaration |
| --- | --- |
| From | ``` case Integer ``` |
| To | ``` case integer ``` |

Modified [TVViewElementStyleType.point](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/point)

|  | Declaration |
| --- | --- |
| From | ``` case Point ``` |
| To | ``` case point ``` |

Modified [TVViewElementStyleType.string](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/tvviewelementstyletypestring)

|  | Declaration |
| --- | --- |
| From | ``` case String ``` |
| To | ``` case string ``` |

Modified [TVViewElementStyleType.transform](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype/tvviewelementstyletypetransform)

|  | Declaration |
| --- | --- |
| From | ``` case Transform ``` |
| To | ``` case transform ``` |

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
