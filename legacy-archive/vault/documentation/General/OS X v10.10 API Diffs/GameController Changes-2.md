---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/GameController.html
archived_at: '2026-07-15T07:34:55.041751Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# GameController Changes

## GameController (Added)

Added GCAcceleration [struct]Added GCAcceleration.xAdded GCAcceleration.yAdded GCAcceleration.zAdded GCControllerAdded GCController.attachedToDeviceAdded GCController.controllerPausedHandlerAdded GCController.controllers() -> [AnyObject]! [class]Added GCController.extendedGamepadAdded GCController.gamepadAdded GCController.motionAdded GCController.playerIndexAdded GCController.startWirelessControllerDiscoveryWithCompletionHandler((() -> Void)!) [class]Added GCController.stopWirelessControllerDiscovery() [class]Added GCController.vendorNameAdded GCControllerAxisInputAdded GCControllerAxisInput.valueAdded GCControllerAxisInput.valueChangedHandlerAdded GCControllerButtonInputAdded GCControllerButtonInput.pressedAdded GCControllerButtonInput.pressedChangedHandlerAdded GCControllerButtonInput.valueAdded GCControllerButtonInput.valueChangedHandlerAdded GCControllerDirectionPadAdded GCControllerDirectionPad.downAdded GCControllerDirectionPad.leftAdded GCControllerDirectionPad.rightAdded GCControllerDirectionPad.upAdded GCControllerDirectionPad.valueChangedHandlerAdded GCControllerDirectionPad.xAxisAdded GCControllerDirectionPad.yAxisAdded GCControllerElementAdded GCControllerElement.analogAdded GCControllerElement.collectionAdded GCExtendedGamepadAdded GCExtendedGamepad.buttonAAdded GCExtendedGamepad.buttonBAdded GCExtendedGamepad.buttonXAdded GCExtendedGamepad.buttonYAdded GCExtendedGamepad.controllerAdded GCExtendedGamepad.dpadAdded GCExtendedGamepad.leftShoulderAdded GCExtendedGamepad.leftThumbstickAdded GCExtendedGamepad.leftTriggerAdded GCExtendedGamepad.rightShoulderAdded GCExtendedGamepad.rightThumbstickAdded GCExtendedGamepad.rightTriggerAdded GCExtendedGamepad.saveSnapshot() -> GCExtendedGamepadSnapshot!Added GCExtendedGamepad.valueChangedHandlerAdded GCExtendedGamepadSnapShotDataV100 [struct]Added GCExtendedGamepadSnapShotDataV100.buttonAAdded GCExtendedGamepadSnapShotDataV100.buttonBAdded GCExtendedGamepadSnapShotDataV100.buttonXAdded GCExtendedGamepadSnapShotDataV100.buttonYAdded GCExtendedGamepadSnapShotDataV100.dpadXAdded GCExtendedGamepadSnapShotDataV100.dpadYAdded GCExtendedGamepadSnapShotDataV100.leftShoulderAdded GCExtendedGamepadSnapShotDataV100.leftThumbstickXAdded GCExtendedGamepadSnapShotDataV100.leftThumbstickYAdded GCExtendedGamepadSnapShotDataV100.leftTriggerAdded GCExtendedGamepadSnapShotDataV100.rightShoulderAdded GCExtendedGamepadSnapShotDataV100.rightThumbstickXAdded GCExtendedGamepadSnapShotDataV100.rightThumbstickYAdded GCExtendedGamepadSnapShotDataV100.rightTriggerAdded GCExtendedGamepadSnapShotDataV100.sizeAdded GCExtendedGamepadSnapShotDataV100.versionAdded GCExtendedGamepadSnapshotAdded GCExtendedGamepadSnapshot.init(controller: GCController!, snapshotData: NSData!)Added GCExtendedGamepadSnapshot.snapshotDataAdded GCExtendedGamepadSnapshot.init(snapshotData: NSData!)Added GCGamepadAdded GCGamepad.buttonAAdded GCGamepad.buttonBAdded GCGamepad.buttonXAdded GCGamepad.buttonYAdded GCGamepad.controllerAdded GCGamepad.dpadAdded GCGamepad.leftShoulderAdded GCGamepad.rightShoulderAdded GCGamepad.saveSnapshot() -> GCGamepadSnapshot!Added GCGamepad.valueChangedHandlerAdded GCGamepadSnapShotDataV100 [struct]Added GCGamepadSnapShotDataV100.buttonAAdded GCGamepadSnapShotDataV100.buttonBAdded GCGamepadSnapShotDataV100.buttonXAdded GCGamepadSnapShotDataV100.buttonYAdded GCGamepadSnapShotDataV100.dpadXAdded GCGamepadSnapShotDataV100.dpadYAdded GCGamepadSnapShotDataV100.leftShoulderAdded GCGamepadSnapShotDataV100.rightShoulderAdded GCGamepadSnapShotDataV100.sizeAdded GCGamepadSnapShotDataV100.versionAdded GCGamepadSnapshotAdded GCGamepadSnapshot.init(controller: GCController!, snapshotData: NSData!)Added GCGamepadSnapshot.snapshotDataAdded GCGamepadSnapshot.init(snapshotData: NSData!)Added GCMotionAdded GCMotion.attitudeAdded GCMotion.controllerAdded GCMotion.gravityAdded GCMotion.rotationRateAdded GCMotion.userAccelerationAdded GCMotion.valueChangedHandlerAdded GCQuaternion [struct]Added GCQuaternion.wAdded GCQuaternion.xAdded GCQuaternion.yAdded GCQuaternion.zAdded GCRotationRate [struct]Added GCRotationRate.xAdded GCRotationRate.yAdded GCRotationRate.zAdded GCControllerAxisValueChangedHandlerAdded GCControllerButtonValueChangedHandlerAdded GCControllerDidConnectNotificationAdded GCControllerDidDisconnectNotificationAdded GCControllerDirectionPadValueChangedHandlerAdded GCControllerPlayerIndexUnsetAdded GCExtendedGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>, NSData!) -> BoolAdded GCExtendedGamepadValueChangedHandlerAdded GCGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCGamepadSnapShotDataV100>, NSData!) -> BoolAdded GCGamepadValueChangedHandlerAdded GCMotionValueChangedHandlerAdded NSDataFromGCExtendedGamepadSnapShotDataV100(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>) -> NSData!Added NSDataFromGCGamepadSnapShotDataV100(UnsafeMutablePointer<GCGamepadSnapShotDataV100>) -> NSData!

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
