---
title: Determining a PostScript Printer's Optimal Resolution
apple_id: DTS10001897
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-07-03'
source_url: https://developer.apple.com/library/archive/qa/qd/qd44.html
archived_at: '2026-07-18T02:38:37.794054Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Hardware & Drivers](https://developer.apple.com/referencelibrary/Printing/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A QD44Determining a PostScript Printer's Optimal Resolution |

|  |
| --- |
| ---   Q: I think I understand how to use the `getRslDataOp` `opCode` with `PrGeneral` to get the resolutions that a printer supports, but when I ask the LaserWriter driver about resolutions, it always tells me I'm talking to a 300 dpi printer. I want to print at the maximum resolution available, and this doesn't generate good results on a 600 (or higher) dpi printer. What gives?  A: The LaserWriter driver works with many different PostScript printers, which can have different output resolutions. Currently, the driver always returns a range of 25 to 1500 dpi for legal resolutions, and a fixed resolution of 300 dpi.  The range of 25 to 1500 means that the driver supports any resolution in that range. This is explained in Technical Note[PR 07 - PrGeneral](https://developer.apple.com/library/archive/technotes/pr/pr_07.html). What it means is that your application can ask for any resolution in that range, and the driver will support it. Given that LaserWriters and other PostScript printers can only support a limited number of resolutions, you may not get optimal results if you pick a resolution that is particularly bad for a printer, even if the driver supports it. You also will end up sending more data than is needed if you're generating bitmaps at a higher resolution than the printer can print. Some extremely high-resolution devices may be able to print at a resolution higher than 1500 dpi, and they are still supported by the LaserWriter driver. The range to return was chosen quite a while ago, and hasn't kept up with the times.  Currently, the only way to get the actual resolution(s) supported by a PostScript printer is to ask the LaserWriter driver for the PPD file, and parse the file yourself, looking for the valid resolutions. The call to get the PPD file is `PrGeneral` with the `PSPrimaryPPDOp`, which is 15. This call is documented in the Q &A, [QD 01 - PPDs](Legacy%20Documentclose%20button-2.md). When Apple makes the functions in LaserWriter 8.4's PPD Library available, you'll be able to use these functions to get the information from the PPD, but the API to that library has not yet been made available (July 1996).  For parsing the PPD file, you'll need to consult the [PPD specification](http://www.adobe.com/supportservice/devrelations/technotes.html) maintained by Adobe.  Rather than going to all that work, a better approach might be to change your code so you don't need to know the printer's resolution in order to generate high-quality data. There are various ways to solve this problem (none of which are perfect):   1. If your application is such that you require a PostScript printer, you could    generate your own PostScript to achieve high-quality results. 2. You could generate your own PostScript, but also use a QuickDraw    representation so images will print correctly to StyleWriters and other    QuickDraw printers. This solution is recommended if you're writing a program    which draws curves, such as a scientific graphing program. For the best    results, break down the curves you need to draw into small portions that can be    accurately represented by the primitives you have at your command. This is a    numerical analysis problem which is beyond the scope of this document. 3. You could use QuickDraw only, but draw in such a way that you'll get high    resolution results. To do this, use objects such as lines, ovals, arcs, etc.    The endpoints of the objects are limited by the resolution at which you draw,    but the objects will be drawn at device resolution.   The approach you take is up to you.  One last comment: if you decide to use PostScript, remember that it is a programming language. Depending on your needs, it may be possible to have the printer do the calculation, since the PostScript code that you generate must be run on the printer. |

#### [Jul 03 1996]

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
