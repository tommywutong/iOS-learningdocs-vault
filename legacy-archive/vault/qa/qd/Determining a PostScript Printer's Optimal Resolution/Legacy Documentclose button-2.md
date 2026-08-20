---
title: PPDs
apple_id: DTS10001760
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd01.html
archived_at: '2026-07-18T02:38:35.136325Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Determining a PostScript Printer's Optimal Resolution](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD01PPDs |

|  |  |
| --- | --- |
| ---   Q: I know where the PPDs are located (System Folder:Extensions:Printer Descriptions), but how can I know what file reflects the current printer?  A: To find the PPD associated with the current printer, you should use the `PrGeneral` call with the `PSPrimaryPPDOp` opcode as documented in the LaserWriter 8 API. Full documentation can be found on the Toolchest CD in the Developer CD series.  The relevant portions of the header file follow:   |  | | --- | | ``` enum {		/* new PrGeneral selectors */ 	getPSInfoOp = 10, 	PSIntentionsOp = 11, 	PSAdobeOp = 14, 	PSPrimaryPPDOp = 15 }; struct TPSPrimaryPPD{ 	short	iOpCode; 	short	iError; 	long	lReserved; 	short	ppdIsRealFile; 	FFSpec	ppdFile; }; typedef struct TPSPrimaryPPD TPSPrimaryPPD; ``` | |

#### [May 01 1995]

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
