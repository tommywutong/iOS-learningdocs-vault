---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/GameController.html
archived_at: '2026-07-18T02:56:25.653652Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# GameController Changes

## GameController

Added GCAcceleration.init()Added GCAcceleration.init(x: Double, y: Double, z: Double)Added GCExtendedGamepadSnapShotDataV100.init()Added GCExtendedGamepadSnapShotDataV100.init(version: UInt16, size: UInt16, dpadX: float_t, dpadY: float_t, buttonA: float_t, buttonB: float_t, buttonX: float_t, buttonY: float_t, leftShoulder: float_t, rightShoulder: float_t, leftThumbstickX: float_t, leftThumbstickY: float_t, rightThumbstickX: float_t, rightThumbstickY: float_t, leftTrigger: float_t, rightTrigger: float_t)Added GCGamepadSnapShotDataV100.init()Added GCGamepadSnapShotDataV100.init(version: UInt16, size: UInt16, dpadX: float_t, dpadY: float_t, buttonA: float_t, buttonB: float_t, buttonX: float_t, buttonY: float_t, leftShoulder: float_t, rightShoulder: float_t)Added GCQuaternion.init()Added GCQuaternion.init(x: Double, y: Double, z: Double, w: Double)Added GCRotationRate.init()Added GCRotationRate.init(x: Double, y: Double, z: Double)Modified GCAcceleration [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GCAcceleration {     var x: Double     var y: Double     var z: Double } ``` |
| To | ``` struct GCAcceleration {     var x: Double     var y: Double     var z: Double     init()     init(x x: Double, y y: Double, z z: Double) } ``` |

Modified GCExtendedGamepadSnapShotDataV100 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GCExtendedGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: float_t     var dpadY: float_t     var buttonA: float_t     var buttonB: float_t     var buttonX: float_t     var buttonY: float_t     var leftShoulder: float_t     var rightShoulder: float_t     var leftThumbstickX: float_t     var leftThumbstickY: float_t     var rightThumbstickX: float_t     var rightThumbstickY: float_t     var leftTrigger: float_t     var rightTrigger: float_t } ``` |
| To | ``` struct GCExtendedGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: float_t     var dpadY: float_t     var buttonA: float_t     var buttonB: float_t     var buttonX: float_t     var buttonY: float_t     var leftShoulder: float_t     var rightShoulder: float_t     var leftThumbstickX: float_t     var leftThumbstickY: float_t     var rightThumbstickX: float_t     var rightThumbstickY: float_t     var leftTrigger: float_t     var rightTrigger: float_t     init()     init(version version: UInt16, size size: UInt16, dpadX dpadX: float_t, dpadY dpadY: float_t, buttonA buttonA: float_t, buttonB buttonB: float_t, buttonX buttonX: float_t, buttonY buttonY: float_t, leftShoulder leftShoulder: float_t, rightShoulder rightShoulder: float_t, leftThumbstickX leftThumbstickX: float_t, leftThumbstickY leftThumbstickY: float_t, rightThumbstickX rightThumbstickX: float_t, rightThumbstickY rightThumbstickY: float_t, leftTrigger leftTrigger: float_t, rightTrigger rightTrigger: float_t) } ``` |

Modified GCGamepadSnapShotDataV100 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GCGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: float_t     var dpadY: float_t     var buttonA: float_t     var buttonB: float_t     var buttonX: float_t     var buttonY: float_t     var leftShoulder: float_t     var rightShoulder: float_t } ``` |
| To | ``` struct GCGamepadSnapShotDataV100 {     var version: UInt16     var size: UInt16     var dpadX: float_t     var dpadY: float_t     var buttonA: float_t     var buttonB: float_t     var buttonX: float_t     var buttonY: float_t     var leftShoulder: float_t     var rightShoulder: float_t     init()     init(version version: UInt16, size size: UInt16, dpadX dpadX: float_t, dpadY dpadY: float_t, buttonA buttonA: float_t, buttonB buttonB: float_t, buttonX buttonX: float_t, buttonY buttonY: float_t, leftShoulder leftShoulder: float_t, rightShoulder rightShoulder: float_t) } ``` |

Modified GCQuaternion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GCQuaternion {     var x: Double     var y: Double     var z: Double     var w: Double } ``` |
| To | ``` struct GCQuaternion {     var x: Double     var y: Double     var z: Double     var w: Double     init()     init(x x: Double, y y: Double, z z: Double, w w: Double) } ``` |

Modified GCRotationRate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GCRotationRate {     var x: Double     var y: Double     var z: Double } ``` |
| To | ``` struct GCRotationRate {     var x: Double     var y: Double     var z: Double     init()     init(x x: Double, y y: Double, z z: Double) } ``` |

Modified GCControllerDidConnectNotification

|  | Declaration |
| --- | --- |
| From | ``` let GCControllerDidConnectNotification: NSString! ``` |
| To | ``` let GCControllerDidConnectNotification: String ``` |

Modified GCControllerDidDisconnectNotification

|  | Declaration |
| --- | --- |
| From | ``` let GCControllerDidDisconnectNotification: NSString! ``` |
| To | ``` let GCControllerDidDisconnectNotification: String ``` |

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
