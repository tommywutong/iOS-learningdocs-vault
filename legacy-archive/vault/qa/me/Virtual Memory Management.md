---
title: Virtual Memory Management
apple_id: DTS10001406
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/me/me02.html
archived_at: '2026-07-18T02:29:43.613759Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A ME02Virtual Memory Management |

|  |
| --- |
|  Q: When I unlock memory with `UnlockMemory`, does it affect only the memory I locked with `LockMemory`, or does it affect the whole page (i.e., will `UnlockMemory` unlock other memory in the same page)?  A: It affects the whole page, not just a smaller part of it. The Virtual Memory lock and hold functions not only lock or hold a page (or pages) of memory, they also increment an internal counter associated with those VM pages. The counter for a page of memory has to return to its initial value (i.e., the value the counter was when the page was in the unlocked/unheld state) before a page is finally unlocked or unheld. So, even if you allocate a little piece of memory and lock it, and the rest of your page is locked by another program, the other program's LockMemory and UnlockMemory calls won't affect your locks. _Inside Macintosh:Memory_ Chapter 1, Introduction to Memory Management, page 20, Locking and Unlocking Relocatable Blocks. [May 01 1995] |

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
