---
title: QuickTime .qtx/.qtr/.qt/.mov files defined
apple_id: DTS10002167
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw99.html
archived_at: '2026-07-18T02:38:53.472327Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [QuickTime for Windows](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxQuickTimeforWindows-date.html) >

|  |
| --- |
| Technical Q&A QTW99QuickTime .qtx/.qtr/.qt/.mov files defined |

|  |
| --- |
| ---   Q: What are the differences between QuickTime files with the .qt, .qtx, .qtr and .mov extensions?  A: A .mov file is, of course, a movie file. A .qt file is (for historical reasons) an alternate extension for movie files (.qt's and .mov's are identical).  The .qtx and .qtr files are pieces of QuickTime extensions (e.g., codecs and file importers). A .qtx file contains the data fork (it's a Windows DLL, actually), while a .qtr file contains the resource fork (for Macintosh-style resources). Note that you may embed a .qtr resource file into a .qtx file so you don't have to actually ship two files for your product. To accomplish this, use the QuickTime Rezwack tool to combine a .qtx file and a .qtr file into a stand-alone .qtx file. [Sep 05 2000] |

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
