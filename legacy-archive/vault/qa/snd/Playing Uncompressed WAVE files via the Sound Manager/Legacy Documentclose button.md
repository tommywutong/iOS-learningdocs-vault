---
title: Playing Uncompressed WAVE files via the Sound Manager
apple_id: DTS10002174
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/snd/snd07.html
archived_at: '2026-07-18T02:38:54.174373Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Audio](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMusicAudio-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Audio](https://developer.apple.com/referencelibrary/MusicAudio/index.html)

|  |
| --- |
| Technical Q&A SND07Playing Uncompressed WAVE files via the Sound Manager |

|  |
| --- |
| Q Can I play an uncompressed WAVE file via the Sound Manager?   A Yes, this is easy, you only need to parse the sound's header and then give the Sound Manager buffers of properly formatted data to play. The AIFF and WAVE file formats are very similar and the data is stored in very much the same way in both files. Parsing a WAVE header is no more difficult than parsing an AIFF header. Microsoft documents the format in _Multimedia Programming Interface and Data Specification v1.0_ and in the SndPlayDoubleBuffer sample code (on the Developer ToolChest CDs) there is quick and dirty code that shows how to parse a WAVE header.  Once you have parsed the WAVE header you can play the data in much the same way you would play AIFF data. However, the WAVE file's data is stored little-endian, but if you have 8 bit (mono or stereo) sounds that means nothing, a byte in little-endian is the same as a byte in big-endian. If, however, you use 16 bit (mono or stereo) sound then an endian conversion will have to take place before before you play the sound. Sound Manager 3.1 and later offer the 'sowt' ("twos" spelled backwards) decompressor which doesn't decompress the sound but instead does the required endian conversion. Simply say that the data from the WAVE file is compressed using this compressor and the Sound Manager willl use this decompressor to play the data without a problem.  See [Q&A SND-08](../Playing%20Compressed%20WAVE%20files%20via%20the%20Sound%20Manager.md) for information about playing compressed WAVE files. [Sep 27 1996] |

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
