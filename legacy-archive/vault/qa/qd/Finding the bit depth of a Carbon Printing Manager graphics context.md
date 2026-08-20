---
title: Finding the bit depth of a Carbon Printing Manager graphics context
apple_id: DTS10001916
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-11-08'
source_url: https://developer.apple.com/library/archive/qa/qd/qd63.html
archived_at: '2026-07-18T02:38:38.912217Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Carbon](https://developer.apple.com/referencelibrary/Printing/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QD63Finding the bit depth of a Carbon Printing Manager graphics context |

|  |  |  |
| --- | --- | --- |
| ---     Q: My application calls `PMSessionGetGraphicsContext` to get a QuickDraw GrafPort to draw into. Once I have the GrafPort, I call  `SInt16 depth = GetPixDepth( GetPortPixMap( grafPtr ) );`  to determine the depth but the resulting depth is always zero. What am I doing wrong?  A: `GetPortPixMap` is designed to work with a `CGrafPtr`, not a `GrafPtr`, and so always returns `NULL` if you pass it a `GrafPtr`. `GetPixDepth` then returns zero because you passed in `NULL`. However, the graphics context from `PMSessionGetGraphicsContext` can be a `GrafPtr` if you are printing in black and white. If your application needs to find out the depth of the graphics context, you should use the code shown in listing 1.   |  |  | | --- | --- | | __Listing 1__. Calculating a GrafPort's bit depth.   |  | | --- | | ```     SInt16 depth;     PixMapHandle pmH = GetPortPixMap( grafPtr );     if ( pmH != NULL ) {                  /* process as a CGrafPtr */         depth = GetPixDepth( pmH );              } else {                  /* process as a GrafPtr */         depth = 1;              } ``` | | |

#### [Nov 08 2000]

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
