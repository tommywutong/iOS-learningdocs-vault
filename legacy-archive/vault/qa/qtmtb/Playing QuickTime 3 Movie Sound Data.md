---
title: Playing QuickTime 3 Movie Sound Data
apple_id: DTS10002020
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-11-09'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb50.html
archived_at: '2026-07-18T02:38:49.264051Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMusicAudio-date.html) >

|  |
| --- |
| Technical Q&A QTMTB50Playing QuickTime 3 Movie Sound Data |

|  |
| --- |
| Q I’d like to play a movie using the QuickTime 3 function `MCDoAction` for a very short period of time, say, 0.10 seconds, and then stop. I can successfully play movie video data for 0.10 seconds, but movie sound data continues to play for about 0.30 ~ 0.50 seconds. Is it possible to play movie sound data using `MCDoAction` for such a short time period?   A The delay you are seeing when stopping your movie after 0.10 seconds is attributable to the fact that QuickTime 3 will play out the contents of the "audio `fifo` queue" when stopping a sound. If we didn't do that, you would never hear the last bit of audio in every movie that you play (this is particularly irritating when your movie is a very short sound, like a button-click).   Let me explain: On the Macintosh, there is a hardware `fifo` (`fifo` = "First In/First Out Queue") which contains the actual sound samples ready to be played out the speaker by the sound hardware. It is generally very small, so you won't notice the "stop delay" on the Mac. On Windows, QuickTime 3 emulates this hardware `fifo` with a software buffer. When `DirectSound` support is available from the audio driver, the default size of this buffer is about 60 milliseconds. When driver-level `DirectSound` support is not available, QuickTime falls back to using Windows' `waveOut` APIs. These APIs are pretty poor, and latency is a big problem. For that reason, the default `fifo` size in that case is about 0.25 seconds (and the "stop delay" is very obvious, as you have found).   The good news is that on Windows you can change the `fifo` size. Go to the QuickTime control panel and select the "Sound Out" pop-up. You will then see whether you are using `waveOut` or `DirectSound`. If `waveOut` is selected, select `DirectSound` instead (if it is in the list). Then (whichever device you have selected) hit the "Options" button. The `DirectSound` Options dialog allows you to enter the `fifo` size in milliseconds. The `waveOut` Options dialog allows you to enter the number of `waveOut` buffers in the `fifo`, as well as their individual size in milliseconds. Shrink the `fifo` as far as you can without getting audio break-up (note that you will need to restart MoviePlayer every time you change the `fifo` size, before you can actually try it out by playing some audio). Remember, you are making a trade-off between audio breakup and latency, and depending on the capability of your sound hardware/drivers, you may have to strike a compromise between the two.   [Nov 09 1998] |

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
