---
title: Sound Track Hiccups under Windows 95
apple_id: DTS10002173
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/snd/snd06.html
archived_at: '2026-07-18T02:38:53.976803Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMusicAudio-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Audio](https://developer.apple.com/referencelibrary/MusicAudio/index.html)

|  |
| --- |
| Technical Q&A SND06Sound Track Hiccups under Windows 95 |

|  |
| --- |
| Q A new client of mine has problems with Sound-track-only QuickTime for Windows playback under Windows 95. During Movie Player and/or Director playback from CD-ROM, the audio breaks up or hiccups regularly. On Windows 3.1, (as well as on the Mac) the same files play with no problems. Also, other QuickTime movies containing video tracks play back their audio just fine under Win95, Win3.1 and MacOS. Is it possible that the interleave ratio is a source of the problem?   A There is only an interleave if the movie contains multiple tracks. If this is a one-sound-track movie, then there is no interleave. I believe your client's problem is a case of the data rate being too low for the CD-ROM cache/buffer size. The CD-ROM drive goes to sleep between physical accesses and can't wake up in time to provide the next data to QTW without an audio dropout. In the System Control Panel, select Performance|File system|CD-ROM. Set the "Supplemental cache size" slider to "Small" and the "Optimize access pattern for:" value to "No read-ahead". Then click "Okay", "Close", and "Yes" to restart the computer.  As an alternative, you can increase the data rate by increasing the quality of the sound. [Sep 27 1996] |

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
