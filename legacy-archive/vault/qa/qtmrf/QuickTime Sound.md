---
title: QuickTime Sound
apple_id: DTS10001967
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmrf/qtmrf04.html
archived_at: '2026-07-18T02:38:47.510456Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTMRF04QuickTime Sound |

|  |
| --- |
| Q I am developing code which allows users to mix an additional sound into the sound track of a QuickTime movie playing under Windows. Since this cannot be accomplished when the CD- ROM is mastered -- the placement of the sound effect must be controlled by the user -- I am extracting the sound samples from the QuickTime movie and blending them with a WAV file which contains the sound effect. While testing this technique using one of the sample movies from the QuickTime for Windows beta CD- ROM, I discovered that the SoundDescription record returned by GetMediaSample contained the constant 'sowt' in the dataFormat field.  The only three formats documented in the QuickTime documentation are raw, MAC3, and MAC6. I need to know what the format of the 'sowt' samples is so I can mix them with the WAV samples. A You're reading the byte backwards. 'sowt' is actually 'twos', which means that the values of the samples go from a minimum point to a maximum point, unlike the raw format, which has a binary offset from zero. In all other aspects, 'twos' and 'raw' samples are the same.   [May 01 1995] |

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
