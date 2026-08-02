---
title: siActive Channels Unsupported on Some Power Macs
apple_id: DTS10002170
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/snd/snd03.html
archived_at: '2026-07-18T02:38:53.712176Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND03siActive Channels Unsupported on Some Power Macs |

|  |
| --- |
| Q When I call SPBGetDeviceInfo or SPBSetDeviceInfo with the siActiveChannels selector on a 5200/5300/6200/6300 Power Macintosh, it returns siUnknownInfoType. What's wrong?   A The Power Macintosh 5200/5300/6200/6300 sound input drivers do not support the siActiveChannels selector. You will have to record in stereo and throw out the channel that you did not want. The best place to do this is in the interrupt routine: copy out the data only from the channel that you actually want to record from. In general, if a selector is not supported, SPBGetDeviceInfo and SPBSetDeviceInfo will return siUnknownInfoType. You will have to determine for yourself if this is a significant error as far as your project is concerned. [Jun 01 1996] |

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
