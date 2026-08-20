---
title: Setting Audio Input Gain
apple_id: DTS10002178
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-10'
source_url: https://developer.apple.com/library/archive/qa/snd/snd11.html
archived_at: '2026-07-18T02:38:54.450646Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/MusicAudio/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/MusicAudio/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Carbon](https://developer.apple.com/referencelibrary/MusicAudio/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A SND11Setting Audio Input Gain |

|  |
| --- |
| Q My program used to set the gain to 1.5, which worked without any problems. With Mac OS 8.1, when I set the gain to 1.5, I get clipping. What happened?   A Mac OS 8.1 changed the gain so that all of the hardware's possible gain is usable. In the past, some Macs were not using the full gain that the hardware could provide (which isn't specified and varies from Mac to Mac). Now the 0.5 to 1.5 values will map to the minimum and maximum gain possible. On the AWAC sound chip, there are two gain amplifiers for input A: one that is on or off and provides 24 dB of gain, and another that has 16 steps of 1.5 dB each (22.5 dB total). Before Mac OS 8.1, the 24 dB gain circuit was never used, but now it is. This gives a 5-bit gain that can be adjusted in 32 steps of 1.5 dB each. These 32 steps are mapped into the 0.5 to 1.5 value that is passed to the sound input driver via `siInputGain`.  The Screamer chip has basically the same capabilities, but for both input A and input B.  The only problem with all of this is that you don't generally know which input you are connected to. In the general case (you can figure out what audio chip you are on without a problem), even the developer notes don't say which inputs are connected to which input ports on the sound chip.  The general solution to overdriving the input may be to provide a slider that adjusts the input gain so that the user can control it, or you can control the gain programmatically to reduce clipping if you detect that three or more continuous samples have the maximum input level value. [Feb 10 1998] |

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
