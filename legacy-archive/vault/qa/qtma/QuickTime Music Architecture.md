---
title: QuickTime Music Architecture
apple_id: DTS10001938
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtma/qtma01.html
archived_at: '2026-07-18T02:38:46.185794Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Audio](https://developer.apple.com/referencelibrary/QuickTime/idxMusicAudio-date.html)

|  |
| --- |
| Technical Q&A QTMA01QuickTime Music Architecture |

|  |
| --- |
| Q Is it possible to have four simultaneous voices?   A Yes, you can have four simultaneous voices.   Q What load do four voices place on the CPU of a 25MHz 68030 Mac?   A Four voices are not a problem for a 25MHz 68030 Macintosh. On a Macintosh LC, we have measured approximately 30 percent CPU usage using 5 voices.   Q Does the load level depend on the number of instruments used simultaneously?   A Yes. The actual load depends on how many instruments are playing simultaneously.   Q Can we build our own instruments? If so, is there a tool available for this purpose?   A In QuickTime 2.0, there is no way to add user- instrument files. However, you can embed instruments into QuickTime movies. Future releases will add Musical Instrument Extensions to your system folder.   Q Are the answers to all the above questions the same for the Windows version of QuickTime as they are for the Mac version?   A On a Windows machine, the music in QuickTime movies plays through a sound card, with MIDI hardware support, using the MIDIMAPPER driver, with very minimal CPU load.   Q Are the instrument sounds the same on Windows?   A The sound of the instruments can vary with the sound card installed.   Q Are most PC sound cards supported?   A The music in your movies will play on any PC sound card that supports MIDI playback under Windows.   [May 01 1995] |

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
