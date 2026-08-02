---
title: New Monitor Related Playback Calls
apple_id: DTS10001925
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm06.html
archived_at: '2026-07-18T02:38:45.779598Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM06New Monitor Related Playback Calls |

|  |
| --- |
| Three additional calls--GDHasScale, GDGetScale, GDSetScale--allow applications to zoom a monitor. They are considered low-level calls (comparable to SetEntries) that should be used only when playing back QuickTime movies in a controlled environment with no user interaction. Also, because this capability is not present on all machines, applications should not depend on its availability.  The new calls provide a standard way for developers to access the resizing abilities of a user's monitor for playback. Effectively, this allows you to have full screen Cinepak playback on low-end Macintosh computers.  Hardware 200 percent resize is currently available only on the Macintosh LC II, IIvx, IIvi, Performa 400, Performa 600, and Color Classic in 16-bit (thousands of colors) display mode on the 12-inch (512 x 384 pixels) monitors. In the future, other graphic devices may take advantage of it.  To implement this functionality, the Image Compression Manager actually makes calls to the video driver for the given device. Video card manufacturers interested in supporting this functionality in their cards should send an AppleLink to DEVSUPPORT (Internet: DEVSUPPORT@applelink.apple.com). See also: The QuickTime Technote (QT4). [May 01 1995] |

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
