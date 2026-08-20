---
title: siOSTypeInputAvailable Format
apple_id: DTS10002176
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-01-16'
source_url: https://developer.apple.com/library/archive/qa/snd/snd09.html
archived_at: '2026-07-18T02:38:54.331869Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND09siOSTypeInputAvailable Format |

|  |
| --- |
| Q What is the format of the data returned by the `siOSTypeInputAvailable` selector?   A The format is `SoundInfoList`. You pass a pointer to a `SoundInfoList` in the `SPBGetDeviceInfo` call with the `siOSTypeInputAvailable` selector, and it returns in that pointer a `SoundInfoList` structure which contains a short (`count`) and a Handle (`infoHandle`) to the `OSType` list. [Jan 16 1998] |

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
