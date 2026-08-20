---
title: ATSUI and MLTE Printing
apple_id: DTS10001917
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-11-08'
source_url: https://developer.apple.com/library/archive/qa/qd/qd64.html
archived_at: '2026-07-18T02:38:38.971161Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/Printing/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Printing/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Carbon](https://developer.apple.com/referencelibrary/Printing/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QD64ATSUI and MLTE Printing |

|  |  |  |  |
| --- | --- | --- | --- |
| ---     Q: I'm writing a printer driver. Why doesn't text drawn using ATSUI (`ATSUDrawText`, for example) or MLTE (`TXNDrawUnicodeTextBox`, for example) show up using my driver when it does show up using other printer drivers? I've replaced all of the QuickDraw bottlenecks with my own code but none of my bottlenecks are getting called to draw the text.  A: ATSUI and MLTE rely on a low level flag to indicate whether or not to use the `StdPix` QuickDraw bottleneck. If you are currently printing then they use the bottleneck. To indicate to MLTE and ATSUI that you are printing, use the macros shown in listing 1.   |  |  |  | | --- | --- | --- | | __Listing 1__. Macros for turning on and off the printing flag used by ATSUI and MLTE.   |  |  | | --- | --- | | |  | | --- | | ```     #define setPrinting() {*((short *)0x948) = 0;}     #define clearPrinting() {*((short *)0x948) = -1;} ``` | | | |

#### [Nov 08 2000]

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
