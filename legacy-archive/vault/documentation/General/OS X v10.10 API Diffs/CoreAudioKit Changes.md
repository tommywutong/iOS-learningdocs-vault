---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CoreAudioKit.html
archived_at: '2026-07-15T07:34:45.016018Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CoreAudioKit Changes

## CoreAudioKit

AUGenericView.hRemoved [-[AUGenericView audioUnit]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516592-audiounit)Removed [-[AUGenericView setShowsExpertParameters:]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516611-showsexpertparameters)Removed [-[AUGenericView showsExpertParameters]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516611-showsexpertparameters)Added [AUGenericView.audioUnit](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516592-audiounit)Added [AUGenericView.showsExpertParameters](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516611-showsexpertparameters)Modified [-[AUGenericView initWithAudioUnit:]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516586-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAudioUnit:(AudioUnit)au ``` |
| To | ``` - (AUGenericView *)initWithAudioUnit:(AudioUnit)au ``` |

Modified [-[AUGenericView initWithAudioUnit:displayFlags:]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516569-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAudioUnit:(AudioUnit)inAudioUnit displayFlags:(UInt32)inFlags ``` |
| To | ``` - (AUGenericView *)initWithAudioUnit:(AudioUnit)inAudioUnit displayFlags:(UInt32)inFlags ``` |

AUPannerView.hRemoved [-[AUPannerView audioUnit]](https://developer.apple.com/documentation/coreaudiokit/aupannerview/1516584-audiounit)Added [AUPannerView.audioUnit](https://developer.apple.com/documentation/coreaudiokit/aupannerview/1516584-audiounit)Modified [+[AUPannerView AUPannerViewWithAudioUnit:]](https://developer.apple.com/documentation/coreaudiokit/aupannerview/1516567-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)AUPannerViewWithAudioUnit:(AudioUnit)au ``` |
| To | ``` + (AUPannerView *)AUPannerViewWithAudioUnit:(AudioUnit)au ``` |

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
