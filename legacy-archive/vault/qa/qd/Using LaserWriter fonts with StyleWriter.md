---
title: Using LaserWriter fonts with StyleWriter
apple_id: DTS10001792
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-22'
source_url: https://developer.apple.com/library/archive/qa/qd/qd33.html
archived_at: '2026-07-18T02:38:37.177004Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD33Using LaserWriter fonts with StyleWriter |

|  |
| --- |
| ---   Q: Can StyleWriter use all the LaserWriter Adobe fonts? Can StyleWriter print the encapsulated PostScript drawings I've developed? Does TrueType software come with the StyleWriter?  A: The LaserWriter has PostScript built-in; the StyleWriter does not. The StyleWriter, in fact, has nothing built-in, and only recognizes QuickDraw commands. Even sending it pure ASCII accomplishes nothing.  TrueType software is shipped with the StyleWriter because it can image fonts at any resolution with excellent quality, much like PostScript. The TrueType software is intended for users of System versions 6.0.7 up to, but not including, System 7. System 7 includes support for TrueType.  You can use PostScript images and fonts with the StyleWriter, but just as with the ImageWriter, you'll have to have something that images them in memory before sending them to the printer (in other words, a Macintosh-resident PostScript interpreter), or use ATM for Type 1 fonts on a StyleWriter. |

#### [Nov 22 1995]

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

---
