---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/IOBluetoothUI.html
archived_at: '2026-07-15T07:34:46.241194Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# IOBluetoothUI Changes

## IOBluetoothUI

objc/IOBluetoothPasskeyDisplay.hAdded [IOBluetoothPasskeyDisplay.isIncomingRequest](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516335-isincomingrequest)Modified [IOBluetoothPasskeyDisplay.backgroundImageConstraint](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516347-backgroundimageconstraint)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSLayoutConstraint *backgroundImageConstraint ``` |
| To | ``` @property(assign) IBOutlet NSLayoutConstraint *backgroundImageConstraint ``` |

Modified [IOBluetoothPasskeyDisplay.centeredView](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpasskeydisplay/1516526-centeredview)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) NSView *centeredView ``` |
| To | ``` @property(assign) IBOutlet NSView *centeredView ``` |

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
