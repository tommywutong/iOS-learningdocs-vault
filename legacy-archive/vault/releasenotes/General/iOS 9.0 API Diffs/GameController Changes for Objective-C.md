---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/GameController.html
archived_at: '2026-07-18T02:56:33.840565Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GameController Changes for Objective-C

### GameController

#### GCController.h

Added [GCController.handlerQueue](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458869-handlerqueue)Added [GCControllerPlayerIndex](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex)Added [GCControllerPlayerIndex1](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index1)Added [GCControllerPlayerIndex2](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/gccontrollerplayerindex2)Added [GCControllerPlayerIndex3](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index3)Added [GCControllerPlayerIndex4](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/index4)Modified [GCController.attachedToDevice](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458868-attachedtodevice)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, getter=isAttachedToDevice) BOOL attachedToDevice ``` |
| To | ``` @property(nonatomic, readonly, getter=isAttachedToDevice) BOOL attachedToDevice ``` |

Modified [GCController.controllerPausedHandler](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458852-controllerpausedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) void (^controllerPausedHandler)(GCController *controller) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^controllerPausedHandler)(GCController * _Nonnull controller) ``` |

Modified [+[GCController controllers]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458871-controllers)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)controllers ``` |
| To | ``` + (NSArray<GCController *> * _Nonnull)controllers ``` |

Modified [GCController.extendedGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458883-extendedgamepad)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) GCExtendedGamepad *extendedGamepad ``` |
| To | ``` @property(nonatomic, retain, readonly, nullable) GCExtendedGamepad *extendedGamepad ``` |

Modified [GCController.gamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458860-gamepad)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) GCGamepad *gamepad ``` |
| To | ``` @property(nonatomic, retain, readonly, nullable) GCGamepad *gamepad ``` |

Modified [GCController.motion](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458884-motion)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) GCMotion *motion ``` |
| To | ``` @property(nonatomic, retain, readonly, nullable) GCMotion *motion ``` |

Modified [GCController.playerIndex](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458885-playerindex)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSInteger playerIndex ``` |
| To | ``` @property(nonatomic) GCControllerPlayerIndex playerIndex ``` |

Modified [GCController.vendorName](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458877-vendorname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *vendorName ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *vendorName ``` |

#### GCControllerAxisInput.h

Modified [GCControllerAxisInput.value](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500224-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) float value ``` |
| To | ``` @property(nonatomic, readonly) float value ``` |

Modified [GCControllerAxisInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500221-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCControllerAxisValueChangedHandler valueChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCControllerAxisValueChangedHandler valueChangedHandler ``` |

#### GCControllerButtonInput.h

Modified [GCControllerButtonInput.pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, getter=isPressed) BOOL pressed ``` |
| To | ``` @property(nonatomic, readonly, getter=isPressed) BOOL pressed ``` |

Modified [GCControllerButtonInput.pressedChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522556-pressedchangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCControllerButtonValueChangedHandler pressedChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCControllerButtonValueChangedHandler pressedChangedHandler ``` |

Modified [GCControllerButtonInput.value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) float value ``` |
| To | ``` @property(nonatomic, readonly) float value ``` |

Modified [GCControllerButtonInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522491-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCControllerButtonValueChangedHandler valueChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCControllerButtonValueChangedHandler valueChangedHandler ``` |

#### GCControllerDirectionPad.h

Modified [GCControllerDirectionPad.down](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462920-down)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *down ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *down ``` |

Modified [GCControllerDirectionPad.left](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462924-left)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *left ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *left ``` |

Modified [GCControllerDirectionPad.right](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462922-right)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *right ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *right ``` |

Modified [GCControllerDirectionPad.up](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462918-up)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *up ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *up ``` |

Modified [GCControllerDirectionPad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462914-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCControllerDirectionPadValueChangedHandler valueChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCControllerDirectionPadValueChangedHandler valueChangedHandler ``` |

Modified [GCControllerDirectionPad.xAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462930-xaxis)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerAxisInput *xAxis ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerAxisInput *xAxis ``` |

Modified [GCControllerDirectionPad.yAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462926-yaxis)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerAxisInput *yAxis ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerAxisInput *yAxis ``` |

#### GCControllerElement.h

Modified [GCControllerElement.analog](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522581-analog)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, getter=isAnalog) BOOL analog ``` |
| To | ``` @property(nonatomic, readonly, getter=isAnalog) BOOL analog ``` |

Modified [GCControllerElement.collection](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522575-collection)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, readonly) GCControllerElement *collection ``` |
| To | ``` @property(nonatomic, assign, readonly, nonnull) GCControllerElement *collection ``` |

#### GCExtendedGamepad.h

Modified [GCExtendedGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522558-buttona)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonA ``` |

Modified [GCExtendedGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522396-buttonb)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonB ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonB ``` |

Modified [GCExtendedGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522567-buttonx)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonX ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonX ``` |

Modified [GCExtendedGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522473-buttony)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonY ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonY ``` |

Modified [GCExtendedGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522427-controller)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) GCController *controller ``` |
| To | ``` @property(nonatomic, readonly, assign, nonnull) GCController *controller ``` |

Modified [GCExtendedGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522422-dpad)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerDirectionPad *dpad ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerDirectionPad *dpad ``` |

Modified [GCExtendedGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522418-leftshoulder)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *leftShoulder ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *leftShoulder ``` |

Modified [GCExtendedGamepad.leftThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522564-leftthumbstick)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerDirectionPad *leftThumbstick ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerDirectionPad *leftThumbstick ``` |

Modified [GCExtendedGamepad.leftTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522569-lefttrigger)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *leftTrigger ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *leftTrigger ``` |

Modified [GCExtendedGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522484-rightshoulder)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *rightShoulder ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *rightShoulder ``` |

Modified [GCExtendedGamepad.rightThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522437-rightthumbstick)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerDirectionPad *rightThumbstick ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerDirectionPad *rightThumbstick ``` |

Modified [GCExtendedGamepad.rightTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522563-righttrigger)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *rightTrigger ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *rightTrigger ``` |

Modified [GCExtendedGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522464-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCExtendedGamepadValueChangedHandler valueChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCExtendedGamepadValueChangedHandler valueChangedHandler ``` |

#### GCExtendedGamepadSnapshot.h

Modified [GCExtendedGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522478-snapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *snapshotData ``` |
| To | ``` @property(atomic, copy, nonnull) NSData *snapshotData ``` |

#### GCGamepad.h

Modified [GCGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497427-buttona)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonA ``` |

Modified [GCGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497418-buttonb)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonB ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonB ``` |

Modified [GCGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497417-buttonx)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonX ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonX ``` |

Modified [GCGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497431-buttony)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *buttonY ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *buttonY ``` |

Modified [GCGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497428-controller)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) GCController *controller ``` |
| To | ``` @property(nonatomic, readonly, assign, nonnull) GCController *controller ``` |

Modified [GCGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497425-dpad)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerDirectionPad *dpad ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerDirectionPad *dpad ``` |

Modified [GCGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497423-leftshoulder)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *leftShoulder ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *leftShoulder ``` |

Modified [GCGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497429-rightshoulder)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) GCControllerButtonInput *rightShoulder ``` |
| To | ``` @property(nonatomic, readonly, nonnull) GCControllerButtonInput *rightShoulder ``` |

Modified [GCGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497421-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCGamepadValueChangedHandler valueChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCGamepadValueChangedHandler valueChangedHandler ``` |

#### GCGamepadSnapshot.h

Modified [GCGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493928-snapshotdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *snapshotData ``` |
| To | ``` @property(atomic, copy, nonnull) NSData *snapshotData ``` |

#### GCMotion.h

Added [GCEulerAngles](https://developer.apple.com/documentation/gamecontroller/gceulerangles)Modified [GCMotion.attitude](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405146-attitude)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, readonly) GCQuaternion attitude ``` |
| To | ``` @property(nonatomic, assign, readonly) GCQuaternion attitude ``` |

Modified [GCMotion.controller](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405174-controller)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) GCController *controller ``` |
| To | ``` @property(nonatomic, readonly, assign, nonnull) GCController *controller ``` |

Modified [GCMotion.gravity](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405176-gravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, readonly) GCAcceleration gravity ``` |
| To | ``` @property(nonatomic, assign, readonly) GCAcceleration gravity ``` |

Modified [GCMotion.rotationRate](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405172-rotationrate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, readonly) GCRotationRate rotationRate ``` |
| To | ``` @property(nonatomic, assign, readonly) GCRotationRate rotationRate ``` |

Modified [GCMotion.userAcceleration](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405182-useracceleration)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, readonly) GCAcceleration userAcceleration ``` |
| To | ``` @property(nonatomic, assign, readonly) GCAcceleration userAcceleration ``` |

Modified [GCMotion.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmotion/1405166-valuechangedhandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) GCMotionValueChangedHandler valueChangedHandler ``` |
| To | ``` @property(nonatomic, copy, nullable) GCMotionValueChangedHandler valueChangedHandler ``` |

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
