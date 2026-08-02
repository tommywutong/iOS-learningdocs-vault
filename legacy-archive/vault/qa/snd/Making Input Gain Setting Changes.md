---
title: Making Input Gain Setting Changes
apple_id: DTS10002168
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/snd/snd01.html
archived_at: '2026-07-18T02:38:53.604885Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND01Making Input Gain Setting Changes |

|  |
| --- |
| Q When I make changes to the input gain setting on a Power Macintosh 5200/5300/6200/6300 and then record, the gain is not where I set it. What's wrong?   A The gain settings do not take effect until you open the sound input device for recording. The name SPBOpenDevice is a misnomer -- it does not actually open the device, it merely returns which device to open when you begin recording. The recording calls actually open the device, allowing changes in the gain settings to be made.  The one other call that will open the device is the SPBSetDeviceInfo call with the siLevelMeterOnOff selector set to on. Making this call will open the device and begin recording (but not saving data), so that the gain settings will take effect. You can now begin the real recording, with the gain set to the desired level. [Jun 01 1996] |

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
