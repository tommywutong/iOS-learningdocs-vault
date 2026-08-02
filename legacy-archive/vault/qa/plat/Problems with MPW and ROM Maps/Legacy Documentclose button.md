---
title: Problems with MPW and ROM Maps
apple_id: DTS10001513
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat03.html
archived_at: '2026-07-18T02:29:50.906116Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| Technical Q&A PLAT03Problems with MPW and ROM Maps |

|  |
| --- |
| ---   Q: How do we build or get a ROM map for a Power Macintosh? Can we use MPW's profiling tools?  A: Power Macintosh computers don't have ROM maps -- they use a different data structure called a ROMInfo file. There is a single ROMInfo file (in the folder on ETO containing the Macintosh Debugger for PowerPC) for the three Power Mac models.  Please note that the MPW-based 68K profiling tools do not work for the Power Macintosh. For profiling, the Adaptive Sampling Profiler from the Macintosh Debugger for PowerPC is the preferred tool. ETO #16 has a new version that can read ROMInfo maps. To show the Macintosh Debugger for PowerPC where to look for ROM symbols, just put the ROMInfo file in the same folder as Power Mac Debugger. |

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
