---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/GameController.html
archived_at: '2026-07-18T02:54:13.511667Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# GameController Changes

## GameController

GCController.hAdded [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller)Added [GCController.attachedToDevice](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458868-attachedtodevice)Added [GCController.controllerPausedHandler](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458852-controllerpausedhandler)Added [+[GCController controllers]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458871-controllers)Added [GCController.extendedGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458883-extendedgamepad)Added [GCController.gamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458860-gamepad)Added [GCController.playerIndex](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458885-playerindex)Added [+[GCController startWirelessControllerDiscoveryWithCompletionHandler:]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458879-startwirelesscontrollerdiscovery)Added [+[GCController stopWirelessControllerDiscovery]](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458854-stopwirelesscontrollerdiscovery)Added [GCController.vendorName](https://developer.apple.com/documentation/gamecontroller/gccontroller/1458877-vendorname)Added [GCControllerDidConnectNotification](https://developer.apple.com/documentation/gamecontroller/gccontrollerdidconnectnotification)Added [GCControllerDidDisconnectNotification](https://developer.apple.com/documentation/gamecontroller/gccontrollerdiddisconnectnotification)Added [GCControllerPlayerIndexUnset](https://developer.apple.com/documentation/gamecontroller/gccontrollerplayerindex/indexunset)GCControllerAxisInput.hAdded [GCControllerAxisInput](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput)Added [GCControllerAxisInput.value](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500224-value)Added [GCControllerAxisInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisinput/1500221-valuechangedhandler)Added [GCControllerAxisValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisvaluechangedhandler)GCControllerButtonInput.hAdded [GCControllerButtonInput](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput)Added [GCControllerButtonInput.pressed](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522539-ispressed)Added [GCControllerButtonInput.value](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522580-value)Added [GCControllerButtonInput.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/1522491-valuechangedhandler)Added [GCControllerButtonValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttonvaluechangedhandler)GCControllerDirectionPad.hAdded [GCControllerDirectionPad](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad)Added [GCControllerDirectionPad.down](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462920-down)Added [GCControllerDirectionPad.left](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462924-left)Added [GCControllerDirectionPad.right](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462922-right)Added [GCControllerDirectionPad.up](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462918-up)Added [GCControllerDirectionPad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462914-valuechangedhandler)Added [GCControllerDirectionPad.xAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462930-xaxis)Added [GCControllerDirectionPad.yAxis](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/1462926-yaxis)Added [GCControllerDirectionPadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpadvaluechangedhandler)GCControllerElement.hAdded [GCControllerElement](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement)Added [GCControllerElement.analog](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522581-analog)Added [GCControllerElement.collection](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/1522575-collection)GCExtendedGamepad.hAdded [GCExtendedGamepad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad)Added [GCExtendedGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522558-buttona)Added [GCExtendedGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522396-buttonb)Added [GCExtendedGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522567-buttonx)Added [GCExtendedGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522473-buttony)Added [GCExtendedGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522427-controller)Added [GCExtendedGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522422-dpad)Added [GCExtendedGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522418-leftshoulder)Added [GCExtendedGamepad.leftThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522564-leftthumbstick)Added [GCExtendedGamepad.leftTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522569-lefttrigger)Added [GCExtendedGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522484-rightshoulder)Added [GCExtendedGamepad.rightThumbstick](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522437-rightthumbstick)Added [GCExtendedGamepad.rightTrigger](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522563-righttrigger)Added [-[GCExtendedGamepad saveSnapshot]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522447-savesnapshot)Added [GCExtendedGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/1522464-valuechangedhandler)Added [GCExtendedGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadvaluechangedhandler)GCExtendedGamepadSnapshot.hAdded [GCExtendedGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot)Added [-[GCExtendedGamepadSnapshot initWithController:snapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522527-init)Added [-[GCExtendedGamepadSnapshot initWithSnapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522554-initwithsnapshotdata)Added [GCExtendedGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/1522478-snapshotdata)Added [GCExtendedGamepadSnapShotDataV100](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100)Added [GCExtendedGamepadSnapShotDataV100FromNSData()](https://developer.apple.com/documentation/gamecontroller/1522439-gcextendedgamepadsnapshotdatav10)Added [NSDataFromGCExtendedGamepadSnapShotDataV100()](https://developer.apple.com/documentation/gamecontroller/1522471-nsdatafromgcextendedgamepadsnaps)GCGamepad.hAdded [GCGamepad](https://developer.apple.com/documentation/gamecontroller/gcgamepad)Added [GCGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497427-buttona)Added [GCGamepad.buttonB](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497418-buttonb)Added [GCGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497417-buttonx)Added [GCGamepad.buttonY](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497431-buttony)Added [GCGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497428-controller)Added [GCGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497425-dpad)Added [GCGamepad.leftShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497423-leftshoulder)Added [GCGamepad.rightShoulder](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497429-rightshoulder)Added [-[GCGamepad saveSnapshot]](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497415-savesnapshot)Added [GCGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepad/1497421-valuechangedhandler)Added [GCGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcgamepadvaluechangedhandler)GCGamepadSnapshot.hAdded [GCGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot)Added [-[GCGamepadSnapshot initWithController:snapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493915-init)Added [-[GCGamepadSnapshot initWithSnapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493933-init)Added [GCGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/1493928-snapshotdata)Added [GCGamepadSnapShotDataV100](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100)Added [GCGamepadSnapShotDataV100FromNSData()](https://developer.apple.com/documentation/gamecontroller/1493934-gcgamepadsnapshotdatav100fromnsd)Added [NSDataFromGCGamepadSnapShotDataV100()](https://developer.apple.com/documentation/gamecontroller/1493914-nsdatafromgcgamepadsnapshotdatav)GameController.h

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
