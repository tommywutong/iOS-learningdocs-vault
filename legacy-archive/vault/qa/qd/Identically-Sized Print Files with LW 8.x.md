---
title: Identically-Sized Print Files with LW 8.x
apple_id: DTS10001900
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-09'
source_url: https://developer.apple.com/library/archive/qa/qd/qd47.html
archived_at: '2026-07-18T02:38:37.974375Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD47Identically-Sized Print Files with LW 8.x |

|  |
| --- |
| ---   Q: For LaserWriter 8.4.1, I have saved files to the disk in foreground and background printing modes. The foreground and background file size is always the same. I would expect that the size of the background image to be smaller as a result of compression and the two pass optimizations. Why don't I get different size PostScript files stored on disk with foreground and background using the LaserWriter 8 driver?  A: LaserWriter 8.4 (and all other 8.x versions) always saves to disk using two passes, hence the foreground and background files you see are the same size. If we didn't do this, then we would generate non-DSC compliant PostScript jobs when saving to disk in the foreground. If you really want to check the PostScript being sent to the printer, then you should turn on the `papToDisk` bit in the driver's '`PRFS`' resource. This makes papToDisk files that capture the data to and from the printer. |

#### [Jan 09 1997]

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
