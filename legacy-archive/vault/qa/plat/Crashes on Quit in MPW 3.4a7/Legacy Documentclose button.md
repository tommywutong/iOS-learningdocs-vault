---
title: Crashes on Quit in MPW 3.4a7
apple_id: DTS10001518
resource_type: QA
platform: Xcode Developer Tools
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat08.html
archived_at: '2026-07-18T02:29:51.488596Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Tools](https://developer.apple.com/referencelibrary/Java/idxTools-date.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT08Crashes on Quit in MPW 3.4a7 |

|  |
| --- |
| ---   Q: In MPW Shell 3.4a7, in a routine `disposeGlobals` called during Quit, a `disposePtr` call is made on a locked handle. This sometimes causes crashes on Quit.  A: This is fixed in MPW Shell 3.4b2. The crashes occurred because the memory for the environment globals was allocated using `NewHandleClear`, then `LockHHi`'d, and then the handle was de-referenced and stored as the pointer to the block. At termination time, this pointer was picked up by `disposeGlobals` and passed to `DisposePtr`. Since this particular address is already a de-referenced handle, it can cause the crash you experienced.  In MPW Shell 3.4b2, the pointer to the environment globals is the argument to a `RecoverHandle` call (to retrieve the real handle for the block of memory), which is then passed to `DisposeHandle`. |

#### [Jun 01 1995]

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
