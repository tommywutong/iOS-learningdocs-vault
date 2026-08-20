---
title: A5 World
apple_id: DTS10001543
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ppcsys/ppcsys02.html
archived_at: '2026-07-18T02:29:54.087251Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A PPCSYS02A5 World |

|  |
| --- |
| ---   Q: Will `rememberA5`, `setupA5`, and `setCurrentA5` still work as designed in MPW/ThinkC for the PowerPC? Some documentation I've read clearly states that these routines need to work (for example, in the MyGrowZone example of IM:Memory).  A: Regarding calls such as `SetA5` and `SetCurrentA5`, these work as documented when called from PowerPC, which is not to say that they are actually useful in the situation you describe.  A5 worlds serve several different functions for a 68K application, most notably, access to QuickDraw globals and access to application globals.  For a PowerPC application, the system maintains a notion of an A5 world for the purposes of accessing QuickDraw globals because much of the system code depends on locating the QuickDraw globals this way. But there is no concept of an A5 world for accessing application globals, because such globals are accessed by a different mechanism. The way that mechanism works means that a code fragment always has access to its globals. So code that previously had to jump through hoops to get to global data no longer has to do so.  Therefore, the calls to `SetCurrentA5` and `SetA5` in the GrowZone proc example in IM:Memory are unnecessary for PowerPC code. [They still are required, however, for 68K code, even if running on a PowerPC machine under the emulator.] |

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
