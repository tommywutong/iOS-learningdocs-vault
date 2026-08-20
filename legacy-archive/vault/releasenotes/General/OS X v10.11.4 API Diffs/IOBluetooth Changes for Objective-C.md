---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Objective-C/IOBluetooth.html
archived_at: '2026-07-18T02:53:48.937714Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# IOBluetooth Changes for Objective-C

### IOBluetooth

#### BluetoothAssignedNumbers.h

Added [kBluetoothHCIVersionCoreSpecification4_2](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciversioncorespecification4_2)Added [kBluetoothLMPVersionCoreSpecification4_2](https://developer.apple.com/documentation/iobluetooth/kbluetoothlmpversioncorespecification4_2)

#### objc/IOBluetoothHandsFree.h

Added [IOBluetoothHandsFreeAudioGatewayFeatureCodecNegotiation](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewayfeatures/codecnegotiation)Added [IOBluetoothHandsFreeCodecID](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid)Added [IOBluetoothHandsFreeCodecIDAACELD](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid/idaaceld)Added [IOBluetoothHandsFreeCodecIDCVSD](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid/iobluetoothhandsfreecodecidcvsd)Added [IOBluetoothHandsFreeCodecIDmSBC](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreecodecid/idmsbc)Added [IOBluetoothHandsFreeDeviceFeatureCodecNegotiation](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicefeatures/codecnegotiation)Modified [IOBluetoothHandsFree.connected](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/1427760-connected)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | isConnected | ``` - (BOOL)isConnected ``` | -- |
| To | connected | ``` @property(readonly, getter=isConnected) BOOL connected ``` | yes |

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
