---
title: Image Compression Dialog Options
apple_id: DTS10001933
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm14.html
archived_at: '2026-07-18T02:38:46.066062Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM14Image Compression Dialog Options |

|  |
| --- |
| Q Our codec needs to provide more options to the user than the normal Image Compression dialog contains. _Inside Macintosh_ suggests that it's possible to provide an extra Options button in the dialog, but this seems to be a function of the application, not the codec. However, I have seen some applications that do provide an Options button for some codecs. How does the application know to do this?   A If your codec component has an exported function named CDRequestSettings, the Standard Compression dialog is smart enough to provide the specific button. In other words, the QuickTime code checks the codec component, adds the button (provided it is available), tests the button status, and calls CDRequestSettings. You get the rect of the displayed Rect with the coordinates if you want to display your dialog inside the other one. In many cases, it makes sense to provide a filterProc as well to process update events (with the exception of a totally modal dialog box). To test if this works for your codec, put a DebugStr inside your CDRequestSettings, and check the Standard Dialog to see if it displays the button and to see if your function is called.  If you need additional information, CDRequestSettings is documented in the [QuickTime Technote QT4](https://developer.apple.com/library/archive/technotes/qt/qt_04.html)and_QuickTime 1.6.1 Features_, which is on the Developer CDs. [Aug 01 1995] |

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
