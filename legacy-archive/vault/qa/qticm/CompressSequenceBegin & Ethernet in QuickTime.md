---
title: CompressSequenceBegin & Ethernet in QuickTime
apple_id: DTS10001932
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm13.html
archived_at: '2026-07-18T02:38:46.009296Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM13CompressSequenceBegin & Ethernet in QuickTime |

|  |
| --- |
| Q When I send compressed images over Ethernet, CompressSequenceBegin doesn't fill in the ImageDescription, which is needed at the other end of the conference link to DecompressSequenceBegin. Is this a bug?   A CompressSequenceBegin doesn't actually modify the handle that you pass. Instead, QuickTime makes note of the handle that's passed, but it doesn't actually modify the contents until the first call that actually compresses data, such as CompressSequenceFrame. At that point, the handle is changed. If you can postpone dealing with the image descriptor until after the first call that compresses data, your code should work.   [May 01 1995] |

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
