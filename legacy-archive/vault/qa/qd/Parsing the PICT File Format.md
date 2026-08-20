---
title: Parsing the PICT File Format
apple_id: DTS10001909
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-10'
source_url: https://developer.apple.com/library/archive/qa/qd/qd56.html
archived_at: '2026-07-18T02:38:38.455158Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD56Parsing the PICT File Format |

|  |
| --- |
| ---   Q: I am looking for the PICT file format, but I can't find it anywhere. Can you help?  A: The PICT file format is documented in Appendix A of "_[Inside Macintosh: Imaging with QuickDraw](https://developer.apple.com/library/archive/documentation/mac/QuickDraw/QuickDraw-2.html)_," which is available on Apple's Developer World web site.  Apple does not recommend reading or writing PICTs directly -- instead, use the usual documented QuickDraw routines (e.g. `OpenCPicture`, `ClosePicture`, `DrawPicture`). For example, if you wanted to parse a PICT for `PicComments`, you could define a `commentProc` and patch out the QuickDraw bottlenecks. This is guaranteed to work, while parsing PICTs directly requires writing and testing a fair amount of code, and is likely to break in the future. |

#### [Feb 10 1998]

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
