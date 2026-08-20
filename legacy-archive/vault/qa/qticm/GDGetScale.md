---
title: GDGetScale
apple_id: DTS10001923
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm04.html
archived_at: '2026-07-18T02:38:45.677540Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Compression & Decompression](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxCompressionDecompression-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM04GDGetScale |

|  |
| --- |
| GDGetScale returns the current scale of the given screen graphics device.  pascal OSErr GDGetScale(GDHandle gdh,Fixed \*scale,short \*flags)  gdh A handle to a screen graphics device.  scale Pointer to a fixed point field to hold the scale result.  flags Pointer to a short integer. It returns the status parameter flags for the video driver. For now, 0 is always returned in this field.  __Errors__:  cDevErr Not a screen device.  controlErr Video driver can not respond to this call.  See also: [QuickTime Technote QT4.](https://developer.apple.com/library/archive/technotes/qt/qt_04.html) [May 01 1995] |

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
