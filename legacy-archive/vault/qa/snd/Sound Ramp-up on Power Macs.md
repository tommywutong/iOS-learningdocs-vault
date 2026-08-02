---
title: Sound Ramp-up on Power Macs
apple_id: DTS10002169
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/snd/snd02.html
archived_at: '2026-07-18T02:38:53.654303Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMusicAudio-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Audio](https://developer.apple.com/referencelibrary/MusicAudio/index.html)

|  |
| --- |
| Technical Q&A SND02Sound Ramp-up on Power Macs |

|  |
| --- |
| Q When I turn on recording on a Power Macintosh 5200/5300/6200/6300, the first quarter of a second of the sound ramps up from silence to full volume. How can I prevent this?   A This is a factor of the sound input hardware "getting ready" to record data. The workaround is to use SPBSetDeviceInfo with the siLevelMeterOnOff selector to turn the level metering on (which will open the recording device) before you go to record. Since the device is already open, when you start your actual recording the sound input level should be stable and you should not notice the ramp-up effect.   [Jun 01 1996] |

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
