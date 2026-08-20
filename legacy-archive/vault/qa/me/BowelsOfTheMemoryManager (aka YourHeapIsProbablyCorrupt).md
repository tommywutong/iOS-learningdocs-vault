---
title: BowelsOfTheMemoryManager (aka YourHeapIsProbablyCorrupt)
apple_id: DTS10001409
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-02-01'
source_url: https://developer.apple.com/library/archive/qa/me/me05.html
archived_at: '2026-07-18T02:29:43.778678Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Data Management](https://developer.apple.com/library/archive/technicalqas/Carbon/idxDataManagement-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Data Management](https://developer.apple.com/referencelibrary/Carbon/idxDataManagement-date.html)

|  |
| --- |
| Technical Q&A ME05BowelsOfTheMemoryManager (aka YourHeapIsProbablyCorrupt) |

|  |  |
| --- | --- |
|  Q: Sometimes, MacsBug generates a PowerPC unmapped memory exception with an address that starts with the symbol `BowelsOfTheMemoryMgr`. What does this mean?  A: When you are displaying addresses in Macsbug, MacsBug shows offsets from the last symbol it can find. In the Modern Memory Manager on Power Macintosh computers up to Mac OS version 7.6, the last symbol was `__HSetStateQ`. The code after `__HSetStateQ` consists of various internal Memory Manager subroutines. So, if there's a hang or crash in an internal Memory Manager subroutine, it shows up in MacsBug as `__HSetStateQ+xxxxxxxx`.  Various system software engineers were tired of seeing bug reports that said `__HSetStateQ` was crashing, so beginning with Mac OS 7.6, we decided to add a new last symbol to the Memory Manager. As a consequence, bug reports would be somewhat more informative. We thought of naming the new symbol `YourHeapIsCorrupt` (since that's usually the case when a program crashes the Memory Manager) but decided on `BowelsOfTheMemoryMgr` instead because that's where you are.  So, if you're crashing or hanging at `BowelsOfTheMemoryMgr+xxxxxxxx`, type `HC` to see if your heap is corrupted (it probably will be) and then start debugging your code to find out how it got corrupted.     |  | | --- | | __Note:__  Starting with Mac OS 9.1, this symbol was changed fromt `BowelsOfTheMemoryMgr` to the more descriptive name `YourHeapIsProbablyCorrupt` (r. 2529682). |     [Feb 01 2001] |

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
