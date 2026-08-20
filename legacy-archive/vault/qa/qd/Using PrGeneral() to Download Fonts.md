---
title: Using PrGeneral() to Download Fonts
apple_id: DTS10001765
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd06.html
archived_at: '2026-07-18T02:38:35.463174Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD06Using PrGeneral() to Download Fonts |

|  |
| --- |
| ---   Q: I'm having a problem using a `PrGeneral` call for the LaserWriter 8 to download fonts to my Encapsulated Postscript (EPS) files. Sometimes, while writing the font info to my EPS file, my program crashes or I get a bus error. It may happen with the second or with some later font -- not always at the same place. And it doesn't seem make a any difference which font is being written. I'm compiling with Symantec Think C++ 6.0. Is it a bug?  A: Yes, it's a bug, and a fix is forthcoming in the LaserWriter 8 driver, version 8.3 release.  One word of caution: The `PrGeneral` call you're using in LaserWriter 8 will continue to be supported, but you need to check that the opcode continues to be supported by checking if it returns an `opNotImpl` (opcode not implemented) error. |

#### [May 01 1995]

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
