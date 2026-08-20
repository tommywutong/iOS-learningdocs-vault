---
title: Process Manager
apple_id: DTS10001551
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ps/ps02.html
archived_at: '2026-07-18T02:29:54.571388Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Process Management](https://developer.apple.com/referencelibrary/Carbon/idxProcessManagement-date.html)

|  |
| --- |
| Technical Q&A PS02Process Manager |

|  |  |  |
| --- | --- | --- |
| ---   Q: Why does the Finder's Get Info window show Memory Requirements numbers for native applications that are different from the numbers in the `SIZE` resource? The Note at the bottom of the Get Info window also says that memory requirements will decrease by a certain amount if virtual memory is turned on. Please explain.  A: First, assume that virtual memory is turned off. When launching your application, the Process Manager creates a heap for you of the size:   |  | | --- | | ``` (amount from SIZE resource) + (size of native code) ``` |   or, if this is not possible, at least   |  | | --- | | ``` (minimum amount from SIZE resource) + (size of native code). ``` |   relocatable block in your application's heap, allocated low in the heap. Because there is no segmentation, the whole native code has to be loaded at once in this case, where virtual memory is turned off. And because the Process Manager can't know how much of the application heap space is needed for data blocks, it's safest to keep the full size of the application heap. In the Get Info window, the Finder displays the size as the sum of The Code Fragment Manager will then load your code into a non-the amount in the `SIZE` resource and the size of the native code. Note that when you change the numbers, the Finder will not add the size of the code when it updates the numbers in the `SIZE` resource.  In the second case, virtual memory is turned on. Now, the size of your heap will be determined the same way as on a 68K system, solely from the `SIZE` resource (and available memory constraints, of course). In this case, your code will be loaded in memory-mapped VM space, which is not in your heap. |

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
