---
title: Preventing Memory Leaks
apple_id: DTS10001405
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/me/me01.html
archived_at: '2026-07-18T02:29:43.540386Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A ME01Preventing Memory Leaks |

|  |
| --- |
|  Q: When `NewPtr` is used to allocate a block of memory in the application heap, is it necessary to use `DisposePtr` to release this block when the program terminates?  A: No. All memory allocated by an application in the application heap (with `NewPtr`, `NewHandle`, `NewPtrClear`, or `NewHandleClear`) is released by the Process Manager when the application terminates, and the application's heap zone is destroyed. This means that you do not explicitly have to call `DisposePtr` to release blocks of memory you allocate with a `NewPtr` call before the application exits.  If your application allocates memory in the system heap, then it must deallocate it. Otherwise, leaks occur. Calls that allocate memory in the system heap include `NewHandleSys`, `NewHandleSysClear`, `NewPtrSys`, and `NewPtrSysClear`. [May 01 1995] |

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
