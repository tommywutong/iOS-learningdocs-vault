---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/GameController.html
archived_at: '2026-07-18T02:56:50.656815Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GameController Changes for Swift

### GameController

Removed GCControllerPlayerIndexUnsetAdded [GCController.handlerQueue](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458869-handlerqueue)Added [GCControllerPlayerIndex [enum]](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex)Added [GCControllerPlayerIndex.Index1](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/gccontrollerplayerindex1)Added [GCControllerPlayerIndex.Index2](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index2)Added [GCControllerPlayerIndex.Index3](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index3)Added [GCControllerPlayerIndex.Index4](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/gccontrollerplayerindex4)Added [GCControllerPlayerIndex.IndexUnset](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/indexunset)Added [GCEulerAngles [struct]](https://developer.apple.com/documentation/gamecontroller/gceulerangles)Added GCEulerAngles.init()Added GCEulerAngles.init(pitch: Double, yaw: Double, roll: Double)Added [GCEulerAngles.pitch](https://developer.apple.com/documentation/gamecontroller/gceulerangles/1405150-pitch)Added [GCEulerAngles.roll](https://developer.apple.com/documentation/gamecontroller/gceulerangles/1405170-roll)Added [GCEulerAngles.yaw](https://developer.apple.com/documentation/gamecontroller/gceulerangles/1405142-yaw)Modified [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GCController : NSObject {     var controllerPausedHandler: ((GCController!) -> Void)!     var vendorName: String! { get }     var attachedToDevice: Bool { get }     var playerIndex: Int     var gamepad: GCGamepad! { get }     var extendedGamepad: GCExtendedGamepad! { get }     var motion: GCMotion! { get }     class func controllers() -> [AnyObject]!     class func startWirelessControllerDiscoveryWithCompletionHandler(_ completionHandler: (() -> Void)!)     class func stopWirelessControllerDiscovery() } ``` |
| To | ``` class GCController : NSObject {     var controllerPausedHandler: ((GCController) -> Void)?     var handlerQueue: dispatch_queue_t     var vendorName: String? { get }     var attachedToDevice: Bool { get }     var playerIndex: GCControllerPlayerIndex     var gamepad: GCGamepad? { get }     var extendedGamepad: GCExtendedGamepad? { get }     var motion: GCMotion? { get }     class func controllers() -> [GCController]     class func startWirelessControllerDiscoveryWithCompletionHandler(_ completionHandler: (() -> Void)?)     class func stopWirelessControllerDiscovery() } ``` |

Modified [GCController.controllerPausedHandler](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458852-controllerpausedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var controllerPausedHandler: ((GCController!) -> Void)! ``` |
| To | ``` var controllerPausedHandler: ((GCController) -> Void)? ``` |

Modified [GCController.controllers() -> [GCController] [class]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458871-controllers)

|  | Declaration |
| --- | --- |
| From | ``` class func controllers() -> [AnyObject]! ``` |
| To | ``` class func controllers() -> [GCController] ``` |

Modified [GCController.extendedGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458883-extendedgamepad)

|  | Declaration |
| --- | --- |
| From | ``` var extendedGamepad: GCExtendedGamepad! { get } ``` |
| To | ``` var extendedGamepad: GCExtendedGamepad? { get } ``` |

Modified [GCController.gamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458860-gamepad)

|  | Declaration |
| --- | --- |
| From | ``` var gamepad: GCGamepad! { get } ``` |
| To | ``` var gamepad: GCGamepad? { get } ``` |

Modified [GCController.motion](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458884-motion)

|  | Declaration |
| --- | --- |
| From | ``` var motion: GCMotion! { get } ``` |
| To | ``` var motion: GCMotion? { get } ``` |

Modified [GCController.playerIndex](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458885-playerindex)

|  | Declaration |
| --- | --- |
| From | ``` var playerIndex: Int ``` |
| To | ``` var playerIndex: GCControllerPlayerIndex ``` |

Modified [GCController.startWirelessControllerDiscoveryWithCompletionHandler(_: (() -> Void)?) [class]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458879-startwirelesscontrollerdiscovery)

|  | Declaration |
| --- | --- |
| From | ``` class func startWirelessControllerDiscoveryWithCompletionHandler(_ completionHandler: (() -> Void)!) ``` |
| To | ``` class func startWirelessControllerDiscoveryWithCompletionHandler(_ completionHandler: (() -> Void)?) ``` |

Modified [GCController.vendorName](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458877-vendorname)

|  | Declaration |
| --- | --- |
| From | ``` var vendorName: String! { get } ``` |
| To | ``` var vendorName: String? { get } ``` |

Modified [GCControllerAxisInput](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerAxisInput : GCControllerElement {     var valueChangedHandler: GCControllerAxisValueChangedHandler!     var value: Float { get } } ``` |
| To | ``` class GCControllerAxisInput : GCControllerElement {     var valueChangedHandler: GCControllerAxisValueChangedHandler?     var value: Float { get } } ``` |

Modified [GCControllerAxisInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500221-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCControllerAxisValueChangedHandler! ``` |
| To | ``` var valueChangedHandler: GCControllerAxisValueChangedHandler? ``` |

Modified [GCControllerButtonInput](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerButtonInput : GCControllerElement {     var valueChangedHandler: GCControllerButtonValueChangedHandler!     var pressedChangedHandler: GCControllerButtonValueChangedHandler!     var value: Float { get }     var pressed: Bool { get } } ``` |
| To | ``` class GCControllerButtonInput : GCControllerElement {     var valueChangedHandler: GCControllerButtonValueChangedHandler?     var pressedChangedHandler: GCControllerButtonValueChangedHandler?     var value: Float { get }     var pressed: Bool { get } } ``` |

Modified [GCControllerButtonInput.pressedChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522556-pressedchangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var pressedChangedHandler: GCControllerButtonValueChangedHandler! ``` |
| To | ``` var pressedChangedHandler: GCControllerButtonValueChangedHandler? ``` |

Modified [GCControllerButtonInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522491-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCControllerButtonValueChangedHandler! ``` |
| To | ``` var valueChangedHandler: GCControllerButtonValueChangedHandler? ``` |

Modified [GCControllerDirectionPad](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerDirectionPad : GCControllerElement {     var valueChangedHandler: GCControllerDirectionPadValueChangedHandler!     var xAxis: GCControllerAxisInput! { get }     var yAxis: GCControllerAxisInput! { get }     var up: GCControllerButtonInput! { get }     var down: GCControllerButtonInput! { get }     var left: GCControllerButtonInput! { get }     var right: GCControllerButtonInput! { get } } ``` |
| To | ``` class GCControllerDirectionPad : GCControllerElement {     var valueChangedHandler: GCControllerDirectionPadValueChangedHandler?     var xAxis: GCControllerAxisInput { get }     var yAxis: GCControllerAxisInput { get }     var up: GCControllerButtonInput { get }     var down: GCControllerButtonInput { get }     var left: GCControllerButtonInput { get }     var right: GCControllerButtonInput { get } } ``` |

Modified [GCControllerDirectionPad.down](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462920-down)

|  | Declaration |
| --- | --- |
| From | ``` var down: GCControllerButtonInput! { get } ``` |
| To | ``` var down: GCControllerButtonInput { get } ``` |

Modified [GCControllerDirectionPad.left](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462924-left)

|  | Declaration |
| --- | --- |
| From | ``` var left: GCControllerButtonInput! { get } ``` |
| To | ``` var left: GCControllerButtonInput { get } ``` |

Modified [GCControllerDirectionPad.right](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462922-right)

|  | Declaration |
| --- | --- |
| From | ``` var right: GCControllerButtonInput! { get } ``` |
| To | ``` var right: GCControllerButtonInput { get } ``` |

Modified [GCControllerDirectionPad.up](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462918-up)

|  | Declaration |
| --- | --- |
| From | ``` var up: GCControllerButtonInput! { get } ``` |
| To | ``` var up: GCControllerButtonInput { get } ``` |

Modified [GCControllerDirectionPad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462914-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCControllerDirectionPadValueChangedHandler! ``` |
| To | ``` var valueChangedHandler: GCControllerDirectionPadValueChangedHandler? ``` |

Modified [GCControllerDirectionPad.xAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462930-xaxis)

|  | Declaration |
| --- | --- |
| From | ``` var xAxis: GCControllerAxisInput! { get } ``` |
| To | ``` var xAxis: GCControllerAxisInput { get } ``` |

Modified [GCControllerDirectionPad.yAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462926-yaxis)

|  | Declaration |
| --- | --- |
| From | ``` var yAxis: GCControllerAxisInput! { get } ``` |
| To | ``` var yAxis: GCControllerAxisInput { get } ``` |

Modified [GCControllerElement](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement)

|  | Declaration |
| --- | --- |
| From | ``` class GCControllerElement : NSObject {     weak var collection: GCControllerElement! { get }     var analog: Bool { get } } ``` |
| To | ``` class GCControllerElement : NSObject {     weak var collection: GCControllerElement? { get }     var analog: Bool { get } } ``` |

Modified [GCControllerElement.collection](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522575-collection)

|  | Declaration |
| --- | --- |
| From | ``` weak var collection: GCControllerElement! { get } ``` |
| To | ``` weak var collection: GCControllerElement? { get } ``` |

Modified [GCExtendedGamepad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad)

|  | Declaration |
| --- | --- |
| From | ``` class GCExtendedGamepad : NSObject {     weak var controller: GCController! { get }     var valueChangedHandler: GCExtendedGamepadValueChangedHandler!     func saveSnapshot() -> GCExtendedGamepadSnapshot!     var dpad: GCControllerDirectionPad! { get }     var buttonA: GCControllerButtonInput! { get }     var buttonB: GCControllerButtonInput! { get }     var buttonX: GCControllerButtonInput! { get }     var buttonY: GCControllerButtonInput! { get }     var leftThumbstick: GCControllerDirectionPad! { get }     var rightThumbstick: GCControllerDirectionPad! { get }     var leftShoulder: GCControllerButtonInput! { get }     var rightShoulder: GCControllerButtonInput! { get }     var leftTrigger: GCControllerButtonInput! { get }     var rightTrigger: GCControllerButtonInput! { get } } ``` |
| To | ``` class GCExtendedGamepad : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GCExtendedGamepadValueChangedHandler?     func saveSnapshot() -> GCExtendedGamepadSnapshot     var dpad: GCControllerDirectionPad { get }     var buttonA: GCControllerButtonInput { get }     var buttonB: GCControllerButtonInput { get }     var buttonX: GCControllerButtonInput { get }     var buttonY: GCControllerButtonInput { get }     var leftThumbstick: GCControllerDirectionPad { get }     var rightThumbstick: GCControllerDirectionPad { get }     var leftShoulder: GCControllerButtonInput { get }     var rightShoulder: GCControllerButtonInput { get }     var leftTrigger: GCControllerButtonInput { get }     var rightTrigger: GCControllerButtonInput { get } } ``` |

Modified [GCExtendedGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522558-buttona)

|  | Declaration |
| --- | --- |
| From | ``` var buttonA: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonA: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522396-buttonb)

|  | Declaration |
| --- | --- |
| From | ``` var buttonB: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonB: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522567-buttonx)

|  | Declaration |
| --- | --- |
| From | ``` var buttonX: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonX: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522473-buttony)

|  | Declaration |
| --- | --- |
| From | ``` var buttonY: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonY: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522427-controller)

|  | Declaration |
| --- | --- |
| From | ``` weak var controller: GCController! { get } ``` |
| To | ``` weak var controller: GCController? { get } ``` |

Modified [GCExtendedGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522422-dpad)

|  | Declaration |
| --- | --- |
| From | ``` var dpad: GCControllerDirectionPad! { get } ``` |
| To | ``` var dpad: GCControllerDirectionPad { get } ``` |

Modified [GCExtendedGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522418-leftshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var leftShoulder: GCControllerButtonInput! { get } ``` |
| To | ``` var leftShoulder: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.leftThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522564-leftthumbstick)

|  | Declaration |
| --- | --- |
| From | ``` var leftThumbstick: GCControllerDirectionPad! { get } ``` |
| To | ``` var leftThumbstick: GCControllerDirectionPad { get } ``` |

Modified [GCExtendedGamepad.leftTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522569-lefttrigger)

|  | Declaration |
| --- | --- |
| From | ``` var leftTrigger: GCControllerButtonInput! { get } ``` |
| To | ``` var leftTrigger: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522484-rightshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var rightShoulder: GCControllerButtonInput! { get } ``` |
| To | ``` var rightShoulder: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.rightThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522437-rightthumbstick)

|  | Declaration |
| --- | --- |
| From | ``` var rightThumbstick: GCControllerDirectionPad! { get } ``` |
| To | ``` var rightThumbstick: GCControllerDirectionPad { get } ``` |

Modified [GCExtendedGamepad.rightTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522563-righttrigger)

|  | Declaration |
| --- | --- |
| From | ``` var rightTrigger: GCControllerButtonInput! { get } ``` |
| To | ``` var rightTrigger: GCControllerButtonInput { get } ``` |

Modified [GCExtendedGamepad.saveSnapshot() -> GCExtendedGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522447-savesnapshot)

|  | Declaration |
| --- | --- |
| From | ``` func saveSnapshot() -> GCExtendedGamepadSnapshot! ``` |
| To | ``` func saveSnapshot() -> GCExtendedGamepadSnapshot ``` |

Modified [GCExtendedGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522464-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCExtendedGamepadValueChangedHandler! ``` |
| To | ``` var valueChangedHandler: GCExtendedGamepadValueChangedHandler? ``` |

Modified [GCExtendedGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` class GCExtendedGamepadSnapshot : GCExtendedGamepad {     @NSCopying var snapshotData: NSData!     init!(snapshotData data: NSData!)     init!(controller controller: GCController!, snapshotData data: NSData!) } ``` |
| To | ``` class GCExtendedGamepadSnapshot : GCExtendedGamepad {     @NSCopying var snapshotData: NSData     init(snapshotData data: NSData)     init(controller controller: GCController, snapshotData data: NSData) } ``` |

Modified [GCExtendedGamepadSnapshot.init(controller: GCController, snapshotData: NSData)](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522527-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(controller controller: GCController!, snapshotData data: NSData!) ``` |
| To | ``` init(controller controller: GCController, snapshotData data: NSData) ``` |

Modified [GCExtendedGamepadSnapshot.init(snapshotData: NSData)](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522554-initwithsnapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(snapshotData data: NSData!) ``` |
| To | ``` init(snapshotData data: NSData) ``` |

Modified [GCExtendedGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522478-snapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var snapshotData: NSData! ``` |
| To | ``` @NSCopying var snapshotData: NSData ``` |

Modified [GCExtendedGamepadSnapShotDataV100 [struct]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100)

|  | Declaration |
| --- | --- |
| From | ``` struct GCExtendedGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: float_t     var dpadY: float_t     var buttonA: float_t     var buttonB: float_t     var buttonX: float_t     var buttonY: float_t     var leftShoulder: float_t     var rightShoulder: float_t     var leftThumbstickX: float_t     var leftThumbstickY: float_t     var rightThumbstickX: float_t     var rightThumbstickY: float_t     var leftTrigger: float_t     var rightTrigger: float_t     init()     init(version version: UInt16, size size: UInt16, dpadX dpadX: float_t, dpadY dpadY: float_t, buttonA buttonA: float_t, buttonB buttonB: float_t, buttonX buttonX: float_t, buttonY buttonY: float_t, leftShoulder leftShoulder: float_t, rightShoulder rightShoulder: float_t, leftThumbstickX leftThumbstickX: float_t, leftThumbstickY leftThumbstickY: float_t, rightThumbstickX rightThumbstickX: float_t, rightThumbstickY rightThumbstickY: float_t, leftTrigger leftTrigger: float_t, rightTrigger rightTrigger: float_t) } ``` |
| To | ``` struct GCExtendedGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: Float     var dpadY: Float     var buttonA: Float     var buttonB: Float     var buttonX: Float     var buttonY: Float     var leftShoulder: Float     var rightShoulder: Float     var leftThumbstickX: Float     var leftThumbstickY: Float     var rightThumbstickX: Float     var rightThumbstickY: Float     var leftTrigger: Float     var rightTrigger: Float     init()     init(version version: UInt16, size size: UInt16, dpadX dpadX: Float, dpadY dpadY: Float, buttonA buttonA: Float, buttonB buttonB: Float, buttonX buttonX: Float, buttonY buttonY: Float, leftShoulder leftShoulder: Float, rightShoulder rightShoulder: Float, leftThumbstickX leftThumbstickX: Float, leftThumbstickY leftThumbstickY: Float, rightThumbstickX rightThumbstickX: Float, rightThumbstickY rightThumbstickY: Float, leftTrigger leftTrigger: Float, rightTrigger rightTrigger: Float) } ``` |

Modified [GCExtendedGamepadSnapShotDataV100.buttonA](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522518-buttona)

|  | Declaration |
| --- | --- |
| From | ``` var buttonA: float_t ``` |
| To | ``` var buttonA: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.buttonB](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522534-buttonb)

|  | Declaration |
| --- | --- |
| From | ``` var buttonB: float_t ``` |
| To | ``` var buttonB: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.buttonX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522571-buttonx)

|  | Declaration |
| --- | --- |
| From | ``` var buttonX: float_t ``` |
| To | ``` var buttonX: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.buttonY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522482-buttony)

|  | Declaration |
| --- | --- |
| From | ``` var buttonY: float_t ``` |
| To | ``` var buttonY: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.dpadX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522468-dpadx)

|  | Declaration |
| --- | --- |
| From | ``` var dpadX: float_t ``` |
| To | ``` var dpadX: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.dpadY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522562-dpady)

|  | Declaration |
| --- | --- |
| From | ``` var dpadY: float_t ``` |
| To | ``` var dpadY: Float ``` |

Modified GCExtendedGamepadSnapShotDataV100.init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonB: Float, buttonX: Float, buttonY: Float, leftShoulder: Float, rightShoulder: Float, leftThumbstickX: Float, leftThumbstickY: Float, rightThumbstickX: Float, rightThumbstickY: Float, leftTrigger: Float, rightTrigger: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: UInt16, size size: UInt16, dpadX dpadX: float_t, dpadY dpadY: float_t, buttonA buttonA: float_t, buttonB buttonB: float_t, buttonX buttonX: float_t, buttonY buttonY: float_t, leftShoulder leftShoulder: float_t, rightShoulder rightShoulder: float_t, leftThumbstickX leftThumbstickX: float_t, leftThumbstickY leftThumbstickY: float_t, rightThumbstickX rightThumbstickX: float_t, rightThumbstickY rightThumbstickY: float_t, leftTrigger leftTrigger: float_t, rightTrigger rightTrigger: float_t) ``` |
| To | ``` init(version version: UInt16, size size: UInt16, dpadX dpadX: Float, dpadY dpadY: Float, buttonA buttonA: Float, buttonB buttonB: Float, buttonX buttonX: Float, buttonY buttonY: Float, leftShoulder leftShoulder: Float, rightShoulder rightShoulder: Float, leftThumbstickX leftThumbstickX: Float, leftThumbstickY leftThumbstickY: Float, rightThumbstickX rightThumbstickX: Float, rightThumbstickY rightThumbstickY: Float, leftTrigger leftTrigger: Float, rightTrigger rightTrigger: Float) ``` |

Modified [GCExtendedGamepadSnapShotDataV100.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522545-leftshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var leftShoulder: float_t ``` |
| To | ``` var leftShoulder: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.leftThumbstickX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522555-leftthumbstickx)

|  | Declaration |
| --- | --- |
| From | ``` var leftThumbstickX: float_t ``` |
| To | ``` var leftThumbstickX: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.leftThumbstickY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522559-leftthumbsticky)

|  | Declaration |
| --- | --- |
| From | ``` var leftThumbstickY: float_t ``` |
| To | ``` var leftThumbstickY: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.leftTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522531-lefttrigger)

|  | Declaration |
| --- | --- |
| From | ``` var leftTrigger: float_t ``` |
| To | ``` var leftTrigger: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522405-rightshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var rightShoulder: float_t ``` |
| To | ``` var rightShoulder: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.rightThumbstickX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522560-rightthumbstickx)

|  | Declaration |
| --- | --- |
| From | ``` var rightThumbstickX: float_t ``` |
| To | ``` var rightThumbstickX: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.rightThumbstickY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522561-rightthumbsticky)

|  | Declaration |
| --- | --- |
| From | ``` var rightThumbstickY: float_t ``` |
| To | ``` var rightThumbstickY: Float ``` |

Modified [GCExtendedGamepadSnapShotDataV100.rightTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100/1522442-righttrigger)

|  | Declaration |
| --- | --- |
| From | ``` var rightTrigger: float_t ``` |
| To | ``` var rightTrigger: Float ``` |

Modified [GCGamepad](https://developer.apple.com/documentation/gamecontroller/gcgamepad)

|  | Declaration |
| --- | --- |
| From | ``` class GCGamepad : NSObject {     weak var controller: GCController! { get }     var valueChangedHandler: GCGamepadValueChangedHandler!     func saveSnapshot() -> GCGamepadSnapshot!     var dpad: GCControllerDirectionPad! { get }     var buttonA: GCControllerButtonInput! { get }     var buttonB: GCControllerButtonInput! { get }     var buttonX: GCControllerButtonInput! { get }     var buttonY: GCControllerButtonInput! { get }     var leftShoulder: GCControllerButtonInput! { get }     var rightShoulder: GCControllerButtonInput! { get } } ``` |
| To | ``` class GCGamepad : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GCGamepadValueChangedHandler?     func saveSnapshot() -> GCGamepadSnapshot     var dpad: GCControllerDirectionPad { get }     var buttonA: GCControllerButtonInput { get }     var buttonB: GCControllerButtonInput { get }     var buttonX: GCControllerButtonInput { get }     var buttonY: GCControllerButtonInput { get }     var leftShoulder: GCControllerButtonInput { get }     var rightShoulder: GCControllerButtonInput { get } } ``` |

Modified [GCGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497427-buttona)

|  | Declaration |
| --- | --- |
| From | ``` var buttonA: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonA: GCControllerButtonInput { get } ``` |

Modified [GCGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497418-buttonb)

|  | Declaration |
| --- | --- |
| From | ``` var buttonB: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonB: GCControllerButtonInput { get } ``` |

Modified [GCGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497417-buttonx)

|  | Declaration |
| --- | --- |
| From | ``` var buttonX: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonX: GCControllerButtonInput { get } ``` |

Modified [GCGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497431-buttony)

|  | Declaration |
| --- | --- |
| From | ``` var buttonY: GCControllerButtonInput! { get } ``` |
| To | ``` var buttonY: GCControllerButtonInput { get } ``` |

Modified [GCGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497428-controller)

|  | Declaration |
| --- | --- |
| From | ``` weak var controller: GCController! { get } ``` |
| To | ``` weak var controller: GCController? { get } ``` |

Modified [GCGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497425-dpad)

|  | Declaration |
| --- | --- |
| From | ``` var dpad: GCControllerDirectionPad! { get } ``` |
| To | ``` var dpad: GCControllerDirectionPad { get } ``` |

Modified [GCGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497423-leftshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var leftShoulder: GCControllerButtonInput! { get } ``` |
| To | ``` var leftShoulder: GCControllerButtonInput { get } ``` |

Modified [GCGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497429-rightshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var rightShoulder: GCControllerButtonInput! { get } ``` |
| To | ``` var rightShoulder: GCControllerButtonInput { get } ``` |

Modified [GCGamepad.saveSnapshot() -> GCGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497415-savesnapshot)

|  | Declaration |
| --- | --- |
| From | ``` func saveSnapshot() -> GCGamepadSnapshot! ``` |
| To | ``` func saveSnapshot() -> GCGamepadSnapshot ``` |

Modified [GCGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497421-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCGamepadValueChangedHandler! ``` |
| To | ``` var valueChangedHandler: GCGamepadValueChangedHandler? ``` |

Modified [GCGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` class GCGamepadSnapshot : GCGamepad {     @NSCopying var snapshotData: NSData!     init!(snapshotData data: NSData!)     init!(controller controller: GCController!, snapshotData data: NSData!) } ``` |
| To | ``` class GCGamepadSnapshot : GCGamepad {     @NSCopying var snapshotData: NSData     init(snapshotData data: NSData)     init(controller controller: GCController, snapshotData data: NSData) } ``` |

Modified [GCGamepadSnapshot.init(controller: GCController, snapshotData: NSData)](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493915-initwithcontroller)

|  | Declaration |
| --- | --- |
| From | ``` init!(controller controller: GCController!, snapshotData data: NSData!) ``` |
| To | ``` init(controller controller: GCController, snapshotData data: NSData) ``` |

Modified [GCGamepadSnapshot.init(snapshotData: NSData)](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493933-initwithsnapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(snapshotData data: NSData!) ``` |
| To | ``` init(snapshotData data: NSData) ``` |

Modified [GCGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493928-snapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var snapshotData: NSData! ``` |
| To | ``` @NSCopying var snapshotData: NSData ``` |

Modified [GCGamepadSnapShotDataV100 [struct]](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100)

|  | Declaration |
| --- | --- |
| From | ``` struct GCGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: float_t     var dpadY: float_t     var buttonA: float_t     var buttonB: float_t     var buttonX: float_t     var buttonY: float_t     var leftShoulder: float_t     var rightShoulder: float_t     init()     init(version version: UInt16, size size: UInt16, dpadX dpadX: float_t, dpadY dpadY: float_t, buttonA buttonA: float_t, buttonB buttonB: float_t, buttonX buttonX: float_t, buttonY buttonY: float_t, leftShoulder leftShoulder: float_t, rightShoulder rightShoulder: float_t) } ``` |
| To | ``` struct GCGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: Float     var dpadY: Float     var buttonA: Float     var buttonB: Float     var buttonX: Float     var buttonY: Float     var leftShoulder: Float     var rightShoulder: Float     init()     init(version version: UInt16, size size: UInt16, dpadX dpadX: Float, dpadY dpadY: Float, buttonA buttonA: Float, buttonB buttonB: Float, buttonX buttonX: Float, buttonY buttonY: Float, leftShoulder leftShoulder: Float, rightShoulder rightShoulder: Float) } ``` |

Modified [GCGamepadSnapShotDataV100.buttonA](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493919-buttona)

|  | Declaration |
| --- | --- |
| From | ``` var buttonA: float_t ``` |
| To | ``` var buttonA: Float ``` |

Modified [GCGamepadSnapShotDataV100.buttonB](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493910-buttonb)

|  | Declaration |
| --- | --- |
| From | ``` var buttonB: float_t ``` |
| To | ``` var buttonB: Float ``` |

Modified [GCGamepadSnapShotDataV100.buttonX](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493924-buttonx)

|  | Declaration |
| --- | --- |
| From | ``` var buttonX: float_t ``` |
| To | ``` var buttonX: Float ``` |

Modified [GCGamepadSnapShotDataV100.buttonY](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493913-buttony)

|  | Declaration |
| --- | --- |
| From | ``` var buttonY: float_t ``` |
| To | ``` var buttonY: Float ``` |

Modified [GCGamepadSnapShotDataV100.dpadX](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493921-dpadx)

|  | Declaration |
| --- | --- |
| From | ``` var dpadX: float_t ``` |
| To | ``` var dpadX: Float ``` |

Modified [GCGamepadSnapShotDataV100.dpadY](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493912-dpady)

|  | Declaration |
| --- | --- |
| From | ``` var dpadY: float_t ``` |
| To | ``` var dpadY: Float ``` |

Modified GCGamepadSnapShotDataV100.init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonB: Float, buttonX: Float, buttonY: Float, leftShoulder: Float, rightShoulder: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(version version: UInt16, size size: UInt16, dpadX dpadX: float_t, dpadY dpadY: float_t, buttonA buttonA: float_t, buttonB buttonB: float_t, buttonX buttonX: float_t, buttonY buttonY: float_t, leftShoulder leftShoulder: float_t, rightShoulder rightShoulder: float_t) ``` |
| To | ``` init(version version: UInt16, size size: UInt16, dpadX dpadX: Float, dpadY dpadY: Float, buttonA buttonA: Float, buttonB buttonB: Float, buttonX buttonX: Float, buttonY buttonY: Float, leftShoulder leftShoulder: Float, rightShoulder rightShoulder: Float) ``` |

Modified [GCGamepadSnapShotDataV100.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493930-leftshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var leftShoulder: float_t ``` |
| To | ``` var leftShoulder: Float ``` |

Modified [GCGamepadSnapShotDataV100.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100/1493922-rightshoulder)

|  | Declaration |
| --- | --- |
| From | ``` var rightShoulder: float_t ``` |
| To | ``` var rightShoulder: Float ``` |

Modified [GCMotion](https://developer.apple.com/documentation/gamecontroller/gcmotion)

|  | Declaration |
| --- | --- |
| From | ``` class GCMotion : NSObject {     weak var controller: GCController! { get }     var valueChangedHandler: GCMotionValueChangedHandler!     var gravity: GCAcceleration { get }     var userAcceleration: GCAcceleration { get }     var attitude: GCQuaternion { get }     var rotationRate: GCRotationRate { get } } ``` |
| To | ``` class GCMotion : NSObject {     weak var controller: GCController? { get }     var valueChangedHandler: GCMotionValueChangedHandler?     var gravity: GCAcceleration { get }     var userAcceleration: GCAcceleration { get }     var attitude: GCQuaternion { get }     var rotationRate: GCRotationRate { get } } ``` |

Modified [GCMotion.controller](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405174-controller)

|  | Declaration |
| --- | --- |
| From | ``` weak var controller: GCController! { get } ``` |
| To | ``` weak var controller: GCController? { get } ``` |

Modified [GCMotion.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405166-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` var valueChangedHandler: GCMotionValueChangedHandler! ``` |
| To | ``` var valueChangedHandler: GCMotionValueChangedHandler? ``` |

Modified [GCControllerAxisValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCControllerAxisValueChangedHandler = (GCControllerAxisInput!, Float) -> Void ``` |
| To | ``` typealias GCControllerAxisValueChangedHandler = (GCControllerAxisInput, Float) -> Void ``` |

Modified [GCControllerButtonValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttonvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCControllerButtonValueChangedHandler = (GCControllerButtonInput!, Float, Bool) -> Void ``` |
| To | ``` typealias GCControllerButtonValueChangedHandler = (GCControllerButtonInput, Float, Bool) -> Void ``` |

Modified [GCControllerDirectionPadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpadvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCControllerDirectionPadValueChangedHandler = (GCControllerDirectionPad!, Float, Float) -> Void ``` |
| To | ``` typealias GCControllerDirectionPadValueChangedHandler = (GCControllerDirectionPad, Float, Float) -> Void ``` |

Modified [GCExtendedGamepadSnapShotDataV100FromNSData(_: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>, _: NSData?) -> Bool](https://developer.apple.com/documentation/gamecontroller/1522439-gcextendedgamepadsnapshotdatav10)

|  | Declaration |
| --- | --- |
| From | ``` func GCExtendedGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>, _ data: NSData!) -> Bool ``` |
| To | ``` func GCExtendedGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>, _ data: NSData?) -> Bool ``` |

Modified [GCExtendedGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCExtendedGamepadValueChangedHandler = (GCExtendedGamepad!, GCControllerElement!) -> Void ``` |
| To | ``` typealias GCExtendedGamepadValueChangedHandler = (GCExtendedGamepad, GCControllerElement) -> Void ``` |

Modified [GCGamepadSnapShotDataV100FromNSData(_: UnsafeMutablePointer<GCGamepadSnapShotDataV100>, _: NSData?) -> Bool](https://developer.apple.com/documentation/gamecontroller/1493934-gcgamepadsnapshotdatav100fromnsd)

|  | Declaration |
| --- | --- |
| From | ``` func GCGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>, _ data: NSData!) -> Bool ``` |
| To | ``` func GCGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>, _ data: NSData?) -> Bool ``` |

Modified [GCGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepadvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCGamepadValueChangedHandler = (GCGamepad!, GCControllerElement!) -> Void ``` |
| To | ``` typealias GCGamepadValueChangedHandler = (GCGamepad, GCControllerElement) -> Void ``` |

Modified [GCMotionValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmotionvaluechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias GCMotionValueChangedHandler = (GCMotion!) -> Void ``` |
| To | ``` typealias GCMotionValueChangedHandler = (GCMotion) -> Void ``` |

Modified [NSDataFromGCExtendedGamepadSnapShotDataV100(_: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>) -> NSData?](https://developer.apple.com/documentation/gamecontroller/1522471-nsdatafromgcextendedgamepadsnaps)

|  | Declaration |
| --- | --- |
| From | ``` func NSDataFromGCExtendedGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>) -> NSData! ``` |
| To | ``` func NSDataFromGCExtendedGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>) -> NSData? ``` |

Modified [NSDataFromGCGamepadSnapShotDataV100(_: UnsafeMutablePointer<GCGamepadSnapShotDataV100>) -> NSData?](https://developer.apple.com/documentation/gamecontroller/1493914-nsdatafromgcgamepadsnapshotdatav)

|  | Declaration |
| --- | --- |
| From | ``` func NSDataFromGCGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>) -> NSData! ``` |
| To | ``` func NSDataFromGCGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>) -> NSData? ``` |

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
