---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreAudioKit.html
archived_at: '2026-07-18T02:52:09.920856Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreAudioKit Changes

## CoreAudioKit

Modified AUGenericView.init(audioUnit: AudioUnit)

|  | Declaration |
| --- | --- |
| From | ``` init(audioUnit au: AudioUnit) ``` |
| To | ``` init!(audioUnit au: AudioUnit) ``` |

Modified AUGenericView.init(audioUnit: AudioUnit, displayFlags: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: UInt32) ``` |
| To | ``` init!(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: UInt32) ``` |

Modified AUPannerView.init(audioUnit: AudioUnit)

|  | Declaration |
| --- | --- |
| From | ``` init(audioUnit au: AudioUnit) -> AUPannerView ``` |
| To | ``` init!(audioUnit au: AudioUnit) -> AUPannerView ``` |

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
