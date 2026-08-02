---
title: Playing Compressed WAVE files via the Sound Manager
apple_id: DTS10002175
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/snd/snd08.html
archived_at: '2026-07-18T02:38:54.239625Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A SND08Playing Compressed WAVE files via the Sound Manager |

|  |
| --- |
| Q Can I play a compressed WAVE file on the Mac?   A Yes, but probably not with the default functionality of the Sound Manager. You have to do all of the sound header parsing yourself, just as you do for an uncompressed sound, and then you have data which you may or may not be able to directly pass to the Sound Manager.  If the WAVE is formatted using µlaw then your program doesn't have to do anything special. Since the µlaw file is processed on a byte by byte, and there is no endian difference between the same data as an AIFF or WAVE file, the standard Mac µlaw decompressor can deal with this data without a problem.  On the other hand, you cannot play IMA-ADPCM compressed WAVE files as simply as you could play a µlaw WAVE files because of the difference in the actual data stream of a sound compressed with the Mac's IMA compressor versus the same sound compressed with the Windows' IMA-ADPCM compressor.  You have to deal with Windows' IMA-ADPCM compressed WAVE sounds just as you would any sound which required a custom decompressor. Your program does all the decompression. This can be done either by writing a decompression component for the Mac (in which case any program can use it), or by having a decompression function in your program.  If you write your own 'sdec' then you can use any Sound Manager routine that will play an arbitrarily compressed sound, just make sure to say that the sound header says the sound is compressed with your compressor so that the Sound Manager will call your 'sdec'.  If you choose not to write a decompression component and you can decompress the sound completely, then you can use any Sound Manager call that takes a buffer of uncompressed sound. If you can't decompress the sound completely then you will have to decompress it in chunks and use SndPlayDoubleBuffer or bufferCmd's to play each chunk. [Sep 27 1996] |

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
