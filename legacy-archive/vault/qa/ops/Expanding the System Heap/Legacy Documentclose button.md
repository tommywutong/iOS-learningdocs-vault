---
title: Expanding the System Heap
apple_id: DTS10001483
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-03-26'
source_url: https://developer.apple.com/library/archive/qa/ops/ops02.html
archived_at: '2026-07-18T02:29:48.339814Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS02Expanding the System Heap |

|  |
| --- |
| Q I am writing a driver and need more system heap space. How can I expand the System heap?   A The System heap, since System 7, shrinks and grows dynamically. Whenever possible, it grows when it needs to, and it is sometimes purged and then shrunk when applications launch. When applications are running, the System heap can still grow to meet demands made on it by expanding into any available Process Manager memory space, (i.e., if an application isn't in the way). At accRun time, you might be able to allocate more memory for your driver if the System heap can grow, but there is no guarantee that this technique will work. To guarantee that your driver has enough memory, you can limit how much the System Heap shrinks by allocating memory for your driver at INIT time and never releasing that memory.  To expand the System heap, install your driver at INIT time and use a 'sysz' resource to allocate space for the driver. The 'sysz' resource contains a long word which specifies the amount of additional space your driver requires (in bytes). When your INIT is loaded, the loader checks your driver's resource file for a 'sysz' resource of ID 0 and ensures that there is at least that much free space in the system heap, expanding the system heap if necessary. This technique works fine but there are three things to bear in mind when using it:  \* The loader checks for free memory -- not contiguous free memory.  \* The maximum amount the system heap may grow at INIT time is half the total amount of RAM.  \* _Inside Macintosh: Memory_ indicates on page 2-13 that you don't need to use a 'sysz' resource under System 7. This is incorrect.  Once the System heap has grown to accommodate your sysz resource, you can allocate any reasonable amount of memory (with a NewHandleSys() call) for your driver at INIT time, but you must lock and retain this memory (that's why you have to allocate a reasonable amount). Your code should be able to recover if the allocation fails, since the sysz resource can guarantee only free memory, not contiguous memory. If you don't lock down the memory when you allocate it at INIT time, you can lose it, because the free memory obtained by the sysz resource is guaranteed only while your INIT runs. The next INIT can take this memory away if it isn't locked.  The sysz resource works this way because it is designed to be useful at INIT time only. It does not provide for an INIT's memory requirements when INIT time is passed and normal system operations are occurring. [Mar 26 2001] |

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
