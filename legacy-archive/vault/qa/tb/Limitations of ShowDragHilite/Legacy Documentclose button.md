---
title: Limitations of ShowDragHilite
apple_id: DTS10002207
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/tb/tb21.html
archived_at: '2026-07-18T02:38:56.383614Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB21Limitations of ShowDragHilite |

|  |
| --- |
| Q When I use ShowDragHilite with a picture filling my window, it only highlights the areas that are the same as the background of my window. Is there anyway around this, or do I have to do everything manually?   A You're right in observing that ShowDragHilite is not very savvy when overlaying image data other than the background color. The problem lies within QuickDraw's hilite mode. The operation of hilite mode is based rather coarsely on the background color. Engineering is currently working on a fix for this problem, and upon its completion hilite mode will start working significantly better in all cases, including that of selecting cells in lists drawn by the standard LDEF. Until then, your only alternative is to implement your own version of ShowDragHilite. The question then becomes, 'what color to use?' Depending on your circumstances, you may want to use black, white, or perhaps even inversion, although against complex images you should try to avoid inversion if at all possible, since it can be ugly and confusing. Once you discover hilite mode to be insufficient, it's up to you to decide how best to serve your users. [Aug 21 1996] |

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
