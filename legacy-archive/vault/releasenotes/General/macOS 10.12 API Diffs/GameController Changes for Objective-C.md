---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/GameController.html
archived_at: '2026-07-18T02:50:39.242360Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# GameController Changes for Objective-C

### GameController

#### GCController.h

Added [GCController.microGamepad](https://developer.apple.com/documentation/gamecontroller/gccontroller/1627772-microgamepad)Added [GCEventViewController](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller)Added [GCEventViewController.controllerUserInteractionEnabled](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller/1627773-controlleruserinteractionenabled)

#### GCMicroGamepad.h (Added)

Added [GCMicroGamepad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad)Added [GCMicroGamepad.allowsRotation](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627755-allowsrotation)Added [GCMicroGamepad.buttonA](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627762-buttona)Added [GCMicroGamepad.buttonX](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627759-buttonx)Added [GCMicroGamepad.controller](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627756-controller)Added [GCMicroGamepad.dpad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627763-dpad)Added [GCMicroGamepad.reportsAbsoluteDpadValues](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627757-reportsabsolutedpadvalues)Added [-[GCMicroGamepad saveSnapshot]](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627754-savesnapshot)Added [GCMicroGamepad.valueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/1627758-valuechangedhandler)Added [GCMicroGamepadValueChangedHandler](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadvaluechangedhandler)

#### GCMicroGamepadSnapshot.h (Added)

Added [GCMicroGamepadSnapshot](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot)Added [-[GCMicroGamepadSnapshot initWithController:snapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/1627534-initwithcontroller)Added [-[GCMicroGamepadSnapshot initWithSnapshotData:]](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/1627540-initwithsnapshotdata)Added [GCMicroGamepadSnapshot.snapshotData](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/1627537-snapshotdata)Added [GCMicroGamepadSnapShotDataV100](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100)Added [GCMicroGamepadSnapShotDataV100FromNSData()](https://developer.apple.com/documentation/gamecontroller/1627542-gcmicrogamepadsnapshotdatav100fr)Added [NSDataFromGCMicroGamepadSnapShotDataV100()](https://developer.apple.com/documentation/gamecontroller/1627541-nsdatafromgcmicrogamepadsnapshot)

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
