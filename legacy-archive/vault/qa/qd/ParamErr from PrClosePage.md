---
title: ParamErr from PrClosePage
apple_id: DTS10001796
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-12-07'
source_url: https://developer.apple.com/library/archive/qa/qd/qd37.html
archived_at: '2026-07-18T02:38:37.403399Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Hardware & Drivers](https://developer.apple.com/referencelibrary/Printing/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A QD37ParamErr from PrClosePage |

|  |  |
| --- | --- |
| ---   Q: When I'm printing and I call `PrClosePage` after the end of the page, I get a `paramErr` (-50) error. What's that mean?  A: There are two ways to get this error. The most common is to pass a bad `GrafPort` to `PrClosePage`. If you don't pass back the port you got from `PrOpenPage`, then you will (rightfully) get an error.  The second way to get a `paramErr` from `PrClosePage` is more esoteric. If you've hidded the menu bar before printing, and leave it hidden, some drivers will report a `paramErr` when `PrClosePage` is called. What's happening is that somewhere deep in the Print Manager, one of the Print Manager routines is calling a QD function with the Menu Bar's rectangle as the parameter. This QuickDraw function sees the empty rectangle (because you've hidden the menu bar), and sets `QDError` to `paramErr`. The driver checks `QDError` when it's done printing, sees the error, and sets `PrError` to the error.    |  | | --- | | __Note:__  this only happens on 68K machines, not on PPCs, although 68k QuickDraw in general does less error checking, and seldom sets `QDError`. | |

#### [Dec 07 1995]

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
