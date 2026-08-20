---
title: Spooling a pixMap into a Window
apple_id: DTS10001773
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd14.html
archived_at: '2026-07-18T02:38:36.000358Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD14Spooling a pixMap into a Window |

|  |
| --- |
| ---   Q: When a picture that contains a `pixMap` is spooled into a window, how and when is the depth of the `pixMap` in the picture converted to the depth of the screens the window is on?  A: When a picture is spooled in, if QuickDraw encounters any bitmap `opcode`, it allocates a `pixMap` of the same depth as the data associated with the bitmap `opcode`, expands the data into the temporary `pixMap`, and then calls `StdBits`. `StdBits` is what triggers the depth and color conversions as demanded by the color environment (depth, color table, B & W settings) of the devices the target port may span (as when a window crosses two or more screens).  If there's not enough memory in the application heap or in the temporary memory pool, QuickDraw bands the image down to one scan line and calls `StdBits` for each of these bands. Note that if you're providing your own `bitsProc`, QuickDraw will call it instead of `StdBits`.  This process is the same when the picture is in memory, with the obvious exception that all the picture data is present; the color mapping occurs when `StdBits` does its stuff. |

#### [Sep 15 1995]

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
