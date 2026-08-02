---
title: URL Access and the Missing Progress Dialog
apple_id: DTS10001685
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-09-23'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1140.html
archived_at: '2026-07-18T02:38:15.261702Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QA1140URL Access and the Missing Progress Dialog |

|  |
| --- |
| ---   Q: When I call `URLDownload` or `URLUpload` in Mac OS X and specify the `kURLDisplayProgressFlag` as an option, why don't I see a progress dialog?  A: The progress dialog isn't being shown because of a bug in URL Access (r. 2719169). If you'd like to display a progress dialog on Mac OS X 10.1.x, you can use `URLOpen` and create your own custom progress dialog by following the example shown in the [URLAccessSample](https://developer.apple.com/samplecode/Sample_Code/Networking/URLAccessSample.htm) code. Alternatively, starting with Mac OS X 10.2, you can use the `kURLDisplayProgressFlag` when calling `URLOpen` in order to display a progress dialog.   ---  [Sep 23 2002] |

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
