---
title: Incorrect Inside Macintosh Volume V documentation
apple_id: DTS10001774
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd15.html
archived_at: '2026-07-18T02:38:36.062948Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD15Incorrect Inside Macintosh Volume V documentation |

|  |
| --- |
| ---   Q: _Inside Macintosh_ Volume V, page 103, says that when a PICT pattern opcode (for instance, `0x0012`) comes along, and the pattern isn't a dither pattern, the full pixMap data follows the old-style 8-byte pattern. The `pixMap` data structure shown on page 104 starts with an unused long (`baseAddr` placeholder), followed by the `rowBytes`, bounds, and so on. However, looking at the Pict.r file on the October 1992 Developer CD, at the same opcode (`BkPixPat` == `0x0012`), the first data field after the old-style pattern (hex string[8]) is the `rowBytes` field (broken down into three bitstrings). The `baseAddr` placeholder field isn't there. Which is correct?  A: The _Inside Macintosh_ Volume V documentation on pages 103-104 is wrong. The Pict.r file correctly describes the format of the `PnPixPat` and `BkPixPat` opcodes. So there shouldn't be a `baseAddr` field in the `pixMap` record of a pattern as stored in the `PnPixPat` of a PICT. However, the `baseAddr` does occur in a '`ppat`' resource as described on page 79. Thanks for pointing out this discrepancy. |

#### [Sep 15 1995]

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
