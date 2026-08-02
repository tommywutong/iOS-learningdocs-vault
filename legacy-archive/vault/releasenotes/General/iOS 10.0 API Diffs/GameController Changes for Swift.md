---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/GameController.html
archived_at: '2026-07-18T02:55:27.100926Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# GameController Changes for Swift

### GameController

Added [GCController.microGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1627772-microgamepad)Added [GCEventViewController](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller)Added [GCEventViewController.controllerUserInteractionEnabled](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller/1627773-controlleruserinteractionenabled)Added [GCMicroGamepad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad)Added [GCMicroGamepad.allowsRotation](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627755-allowsrotation)Added [GCMicroGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627762-buttona)Added [GCMicroGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627759-buttonx)Added [GCMicroGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627756-controller)Added [GCMicroGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627763-dpad)Added [GCMicroGamepad.reportsAbsoluteDpadValues](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627757-reportsabsolutedpadvalues)Added [GCMicroGamepad.saveSnapshot() -> GCMicroGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627754-savesnapshot)Added [GCMicroGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627758-valuechangedhandler)Added [GCMicroGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot)Added [GCMicroGamepadSnapshot.init(controller: GCController, snapshotData: Data)](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/1627534-init)Added [GCMicroGamepadSnapshot.init(snapshotData: Data)](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/1627540-init)Added [GCMicroGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/1627537-snapshotdata)Added [GCMicroGamepadSnapShotDataV100 [struct]](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100)Added [GCMicroGamepadSnapShotDataV100.buttonA](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627533-buttona)Added [GCMicroGamepadSnapShotDataV100.buttonX](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627543-buttonx)Added [GCMicroGamepadSnapShotDataV100.dpadX](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627544-dpadx)Added [GCMicroGamepadSnapShotDataV100.dpadY](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627535-dpady)Added [GCMicroGamepadSnapShotDataV100.init()](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627776-init)Added [GCMicroGamepadSnapShotDataV100.init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonX: Float)](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627775-init)Added [GCMicroGamepadSnapShotDataV100.size](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627538-size)Added [GCMicroGamepadSnapShotDataV100.version](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100/1627536-version)Added [GCMicroGamepadSnapShotDataV100FromNSData(_: UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, _: Data?) -> Bool](https://developer.apple.com/documentation/gamecontroller/1627542-gcmicrogamepadsnapshotdatav100fr)Added [GCMicroGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadvaluechangedhandler)Added [NSDataFromGCMicroGamepadSnapShotDataV100(_: UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?](https://developer.apple.com/documentation/gamecontroller/1627541-nsdatafromgcmicrogamepadsnapshot)Modified [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GCController : NSObject {     var controllerPausedHandler: ((GCController) -> Void)?     var handlerQueue: dispatch_queue_t     var vendorName: String? { get }     var attachedToDevice: Bool { get }     var playerIndex: GCControllerPlayerIndex     var gamepad: GCGamepad? { get }     var extendedGamepad: GCExtendedGamepad? { get }     var motion: GCMotion? { get }     class func controllers() -> [GCController]     class func startWirelessControllerDiscoveryWithCompletionHandler(_ completionHandler: (() -> Void)?)     class func stopWirelessControllerDiscovery() } ``` | -- |
| To | ``` class GCController : NSObject {     var controllerPausedHandler: ((GCController) -> Swift.Void)?     var handlerQueue: DispatchQueue     var vendorName: String? { get }     var isAttachedToDevice: Bool { get }     var playerIndex: GCControllerPlayerIndex     var gamepad: GCGamepad? { get }     var microGamepad: GCMicroGamepad? { get }     var extendedGamepad: GCExtendedGamepad? { get }     var motion: GCMotion? { get }     class func controllers() -> [GCController]     class func startWirelessControllerDiscovery(completionHandler completionHandler: (@escaping () -> Swift.Void)? = nil)     class func stopWirelessControllerDiscovery()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GCController : CVarArg { } extension GCController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GCController.controllerPausedHandler](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458852-controllerpausedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var controllerPausedHandler: ((GCController) -> Void)? ``` |
| To | ``` var controllerPausedHandler: ((GCController) -> Swift.Void)? ``` |

Modified [GCController.handlerQueue](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458869-handlerqueue)

|  | Declaration |
| --- | --- |
| From | ``` var handlerQueue: dispatch_queue_t ``` |
| To | ``` var handlerQueue: DispatchQueue ``` |

Modified [GCController.isAttachedToDevice](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458868-attachedtodevice)

|  | Declaration |
| --- | --- |
| From | ``` var attachedToDevice: Bool { get } ``` |
| To | ``` var isAttachedToDevice: Bool { get } ``` |

Modified [GCController.startWirelessControllerDiscovery(completionHandler: ( () -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458879-startwirelesscontrollerdiscovery)

|  | Declaration |
| --- | --- |
| From | ``` class func startWirelessControllerDiscoveryWithCompletionHandler(_ completionHandler: (() -> Void)?) ``` |
| To | ``` class func startWirelessControllerDiscovery(completionHandler completionHandler: (@escaping () -> Swift.Void)? = nil) ``` |

Modified [GCControllerAxisInput](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerAxisInput : GCControllerElement {     var valueChangedHandler: GCControllerAxisValueChangedHandler?     var value: Float { get } } ``` |
| To | ``` class GCControllerAxisInput : GCControllerElement {     var valueChangedHandler: GameController.GCControllerAxisValueChangedHandler?     var value: Float { get } } ``` |

Modified [GCControllerAxisInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500221-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCControllerAxisValueChangedHandler? ``` |
| To | ``` var valueChangedHandler: GameController.GCControllerAxisValueChangedHandler? ``` |

Modified [GCControllerButtonInput](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerButtonInput : GCControllerElement {     var valueChangedHandler: GCControllerButtonValueChangedHandler?     var pressedChangedHandler: GCControllerButtonValueChangedHandler?     var value: Float { get }     var pressed: Bool { get } } ``` |
| To | ``` class GCControllerButtonInput : GCControllerElement {     var valueChangedHandler: GameController.GCControllerButtonValueChangedHandler?     var pressedChangedHandler: GameController.GCControllerButtonValueChangedHandler?     var value: Float { get }     var isPressed: Bool { get } } ``` |

Modified [GCControllerButtonInput.isPressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed)

|  | Declaration |
| --- | --- |
| From | ``` var pressed: Bool { get } ``` |
| To | ``` var isPressed: Bool { get } ``` |

Modified [GCControllerButtonInput.pressedChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522556-pressedchangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var pressedChangedHandler: GCControllerButtonValueChangedHandler? ``` |
| To | ``` var pressedChangedHandler: GameController.GCControllerButtonValueChangedHandler? ``` |

Modified [GCControllerButtonInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522491-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCControllerButtonValueChangedHandler? ``` |
| To | ``` var valueChangedHandler: GameController.GCControllerButtonValueChangedHandler? ``` |

Modified [GCControllerDirectionPad](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerDirectionPad : GCControllerElement {     var valueChangedHandler: GCControllerDirectionPadValueChangedHandler?     var xAxis: GCControllerAxisInput { get }     var yAxis: GCControllerAxisInput { get }     var up: GCControllerButtonInput { get }     var down: GCControllerButtonInput { get }     var left: GCControllerButtonInput { get }     var right: GCControllerButtonInput { get } } ``` |
| To | ``` class GCControllerDirectionPad : GCControllerElement {     var valueChangedHandler: GameController.GCControllerDirectionPadValueChangedHandler?     var xAxis: GCControllerAxisInput { get }     var yAxis: GCControllerAxisInput { get }     var up: GCControllerButtonInput { get }     var down: GCControllerButtonInput { get }     var left: GCControllerButtonInput { get }     var right: GCControllerButtonInput { get } } ``` |

Modified [GCControllerDirectionPad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462914-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCControllerDirectionPadValueChangedHandler? ``` |
| To | ``` var valueChangedHandler: GameController.GCControllerDirectionPadValueChangedHandler? ``` |

Modified [GCControllerElement](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GCControllerElement : NSObject {     weak var collection: GCControllerElement? { get }     var analog: Bool { get } } ``` | -- |
| To | ``` class GCControllerElement : NSObject {     weak var collection: GCControllerElement? { get }     var isAnalog: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GCControllerElement : CVarArg { } extension GCControllerElement : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GCControllerElement.isAnalog](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522581-analog)

|  | Declaration |
| --- | --- |
| From | ``` var analog: Bool { get } ``` |
| To | ``` var isAnalog: Bool { get } ``` |

Modified [GCControllerPlayerIndex [enum]](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex)

|  | Declaration |
| --- | --- |
| From | ``` enum GCControllerPlayerIndex : Int {     case IndexUnset     case Index1     case Index2     case Index3     case Index4 } ``` |
| To | ``` enum GCControllerPlayerIndex : Int {     case indexUnset     case index1     case index2     case index3     case index4 } ``` |

Modified [GCControllerPlayerIndex.index1](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/gccontrollerplayerindex1)

|  | Declaration |
| --- | --- |
| From | ``` case Index1 ``` |
| To | ``` case index1 ``` |

Modified [GCControllerPlayerIndex.index2](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index2)

|  | Declaration |
| --- | --- |
| From | ``` case Index2 ``` |
| To | ``` case index2 ``` |

Modified [GCControllerPlayerIndex.index3](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index3)

|  | Declaration |
| --- | --- |
| From | ``` case Index3 ``` |
| To | ``` case index3 ``` |

Modified [GCControllerPlayerIndex.index4](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/gccontrollerplayerindex4)

|  | Declaration |
| --- | --- |
| From | ``` case Index4 ``` |
| To | ``` case index4 ``` |

Modified [GCControllerPlayerIndex.indexUnset](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/indexunset)

|  | Declaration |
| --- | --- |
| From | ``` case IndexUnset ``` |
| To | ``` case indexUnset ``` |

Modified [GCExtendedGamepad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GCExtendedGamepad : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GCExtendedGamepadValueChangedHandler?     func saveSnapshot() -> GCExtendedGamepadSnapshot     var dpad: GCControllerDirectionPad { get }     var buttonA: GCControllerButtonInput { get }     var buttonB: GCControllerButtonInput { get }     var buttonX: GCControllerButtonInput { get }     var buttonY: GCControllerButtonInput { get }     var leftThumbstick: GCControllerDirectionPad { get }     var rightThumbstick: GCControllerDirectionPad { get }     var leftShoulder: GCControllerButtonInput { get }     var rightShoulder: GCControllerButtonInput { get }     var leftTrigger: GCControllerButtonInput { get }     var rightTrigger: GCControllerButtonInput { get } } ``` | -- |
| To | ``` class GCExtendedGamepad : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GameController.GCExtendedGamepadValueChangedHandler?     func saveSnapshot() -> GCExtendedGamepadSnapshot     var dpad: GCControllerDirectionPad { get }     var buttonA: GCControllerButtonInput { get }     var buttonB: GCControllerButtonInput { get }     var buttonX: GCControllerButtonInput { get }     var buttonY: GCControllerButtonInput { get }     var leftThumbstick: GCControllerDirectionPad { get }     var rightThumbstick: GCControllerDirectionPad { get }     var leftShoulder: GCControllerButtonInput { get }     var rightShoulder: GCControllerButtonInput { get }     var leftTrigger: GCControllerButtonInput { get }     var rightTrigger: GCControllerButtonInput { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GCExtendedGamepad : CVarArg { } extension GCExtendedGamepad : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GCExtendedGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522464-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCExtendedGamepadValueChangedHandler? ``` |
| To | ``` var valueChangedHandler: GameController.GCExtendedGamepadValueChangedHandler? ``` |

Modified [GCExtendedGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` class GCExtendedGamepadSnapshot : GCExtendedGamepad {     @NSCopying var snapshotData: NSData     init(snapshotData data: NSData)     init(controller controller: GCController, snapshotData data: NSData) } ``` |
| To | ``` class GCExtendedGamepadSnapshot : GCExtendedGamepad {     var snapshotData: Data     init(snapshotData data: Data)     init(controller controller: GCController, snapshotData data: Data) } ``` |

Modified [GCExtendedGamepadSnapshot.init(controller: GCController, snapshotData: Data)](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522527-init)

|  | Declaration |
| --- | --- |
| From | ``` init(controller controller: GCController, snapshotData data: NSData) ``` |
| To | ``` init(controller controller: GCController, snapshotData data: Data) ``` |

Modified [GCExtendedGamepadSnapshot.init(snapshotData: Data)](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522554-initwithsnapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` init(snapshotData data: NSData) ``` |
| To | ``` init(snapshotData data: Data) ``` |

Modified [GCExtendedGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522478-snapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var snapshotData: NSData ``` |
| To | ``` var snapshotData: Data ``` |

Modified [GCGamepad](https://developer.apple.com/documentation/gamecontroller/gcgamepad)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GCGamepad : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GCGamepadValueChangedHandler?     func saveSnapshot() -> GCGamepadSnapshot     var dpad: GCControllerDirectionPad { get }     var buttonA: GCControllerButtonInput { get }     var buttonB: GCControllerButtonInput { get }     var buttonX: GCControllerButtonInput { get }     var buttonY: GCControllerButtonInput { get }     var leftShoulder: GCControllerButtonInput { get }     var rightShoulder: GCControllerButtonInput { get } } ``` | -- |
| To | ``` class GCGamepad : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GameController.GCGamepadValueChangedHandler?     func saveSnapshot() -> GCGamepadSnapshot     var dpad: GCControllerDirectionPad { get }     var buttonA: GCControllerButtonInput { get }     var buttonB: GCControllerButtonInput { get }     var buttonX: GCControllerButtonInput { get }     var buttonY: GCControllerButtonInput { get }     var leftShoulder: GCControllerButtonInput { get }     var rightShoulder: GCControllerButtonInput { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GCGamepad : CVarArg { } extension GCGamepad : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GCGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497421-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCGamepadValueChangedHandler? ``` |
| To | ``` var valueChangedHandler: GameController.GCGamepadValueChangedHandler? ``` |

Modified [GCGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` class GCGamepadSnapshot : GCGamepad {     @NSCopying var snapshotData: NSData     init(snapshotData data: NSData)     init(controller controller: GCController, snapshotData data: NSData) } ``` |
| To | ``` class GCGamepadSnapshot : GCGamepad {     var snapshotData: Data     init(snapshotData data: Data)     init(controller controller: GCController, snapshotData data: Data) } ``` |

Modified [GCGamepadSnapshot.init(controller: GCController, snapshotData: Data)](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493915-initwithcontroller)

|  | Declaration |
| --- | --- |
| From | ``` init(controller controller: GCController, snapshotData data: NSData) ``` |
| To | ``` init(controller controller: GCController, snapshotData data: Data) ``` |

Modified [GCGamepadSnapshot.init(snapshotData: Data)](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493933-initwithsnapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` init(snapshotData data: NSData) ``` |
| To | ``` init(snapshotData data: Data) ``` |

Modified [GCGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493928-snapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var snapshotData: NSData ``` |
| To | ``` var snapshotData: Data ``` |

Modified [GCMotion](https://developer.apple.com/documentation/gamecontroller/gcmotion)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GCMotion : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GCMotionValueChangedHandler?     var gravity: GCAcceleration { get }     var userAcceleration: GCAcceleration { get }     var attitude: GCQuaternion { get }     var rotationRate: GCRotationRate { get } } ``` | -- |
| To | ``` class GCMotion : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GameController.GCMotionValueChangedHandler?     var gravity: GCAcceleration { get }     var userAcceleration: GCAcceleration { get }     var attitude: GCQuaternion { get }     var rotationRate: GCRotationRate { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GCMotion : CVarArg { } extension GCMotion : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GCMotion.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405166-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCMotionValueChangedHandler? ``` |
| To | ``` var valueChangedHandler: GameController.GCMotionValueChangedHandler? ``` |

Modified [NSNotification.Name.GCControllerDidConnect](https://developer.apple.com/documentation/gamecontroller/gccontrollerdidconnectnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | GCControllerDidConnectNotification | ``` let GCControllerDidConnectNotification: String ``` |
| To | GCControllerDidConnect | ``` static let GCControllerDidConnect: NSNotification.Name ``` |

Modified [NSNotification.Name.GCControllerDidDisconnect](https://developer.apple.com/documentation/gamecontroller/gccontrollerdiddisconnectnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | GCControllerDidDisconnectNotification | ``` let GCControllerDidDisconnectNotification: String ``` |
| To | GCControllerDidDisconnect | ``` static let GCControllerDidDisconnect: NSNotification.Name ``` |

Modified [GCControllerAxisValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCControllerAxisValueChangedHandler = (GCControllerAxisInput, Float) -> Void ``` |
| To | ``` typealias GCControllerAxisValueChangedHandler = (GCControllerAxisInput, Float) -> Swift.Void ``` |

Modified [GCControllerButtonValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttonvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCControllerButtonValueChangedHandler = (GCControllerButtonInput, Float, Bool) -> Void ``` |
| To | ``` typealias GCControllerButtonValueChangedHandler = (GCControllerButtonInput, Float, Bool) -> Swift.Void ``` |

Modified [GCControllerDirectionPadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpadvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCControllerDirectionPadValueChangedHandler = (GCControllerDirectionPad, Float, Float) -> Void ``` |
| To | ``` typealias GCControllerDirectionPadValueChangedHandler = (GCControllerDirectionPad, Float, Float) -> Swift.Void ``` |

Modified [GCExtendedGamepadSnapShotDataV100FromNSData(_: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, _: Data?) -> Bool](https://developer.apple.com/documentation/gamecontroller/1522439-gcextendedgamepadsnapshotdatav10)

|  | Declaration |
| --- | --- |
| From | ``` func GCExtendedGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>, _ data: NSData?) -> Bool ``` |
| To | ``` func GCExtendedGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, _ data: Data?) -> Bool ``` |

Modified [GCExtendedGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCExtendedGamepadValueChangedHandler = (GCExtendedGamepad, GCControllerElement) -> Void ``` |
| To | ``` typealias GCExtendedGamepadValueChangedHandler = (GCExtendedGamepad, GCControllerElement) -> Swift.Void ``` |

Modified [GCGamepadSnapShotDataV100FromNSData(_: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, _: Data?) -> Bool](https://developer.apple.com/documentation/gamecontroller/1493934-gcgamepadsnapshotdatav100fromnsd)

|  | Declaration |
| --- | --- |
| From | ``` func GCGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>, _ data: NSData?) -> Bool ``` |
| To | ``` func GCGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, _ data: Data?) -> Bool ``` |

Modified [GCGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepadvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCGamepadValueChangedHandler = (GCGamepad, GCControllerElement) -> Void ``` |
| To | ``` typealias GCGamepadValueChangedHandler = (GCGamepad, GCControllerElement) -> Swift.Void ``` |

Modified [GCMotionValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmotionvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCMotionValueChangedHandler = (GCMotion) -> Void ``` |
| To | ``` typealias GCMotionValueChangedHandler = (GCMotion) -> Swift.Void ``` |

Modified [NSDataFromGCExtendedGamepadSnapShotDataV100(_: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?](https://developer.apple.com/documentation/gamecontroller/1522471-nsdatafromgcextendedgamepadsnaps)

|  | Declaration |
| --- | --- |
| From | ``` func NSDataFromGCExtendedGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>) -> NSData? ``` |
| To | ``` func NSDataFromGCExtendedGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data? ``` |

Modified [NSDataFromGCGamepadSnapShotDataV100(_: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?](https://developer.apple.com/documentation/gamecontroller/1493914-nsdatafromgcgamepadsnapshotdatav)

|  | Declaration |
| --- | --- |
| From | ``` func NSDataFromGCGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>) -> NSData? ``` |
| To | ``` func NSDataFromGCGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data? ``` |

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
