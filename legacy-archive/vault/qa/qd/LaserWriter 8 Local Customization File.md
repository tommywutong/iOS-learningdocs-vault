---
title: LaserWriter 8 Local Customization File
apple_id: DTS10001770
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd11.html
archived_at: '2026-07-18T02:38:35.779584Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD11LaserWriter 8 Local Customization File |

|  |  |
| --- | --- |
| ---   Q: I have a PostScript Printer Description File (written to the Adobe PostScript Printer Description File Format Specification version 4.1 of 9 April, 1993), which works fine with the LaserWriter 8 driver (v 8.1.1) on a particular printer. I wrote a local customization file in the same format as the example on page 10 of the specification, which \*Include's my valid PPD. I named that file "cust.ppd" and put it in "System Folder: Extensions: Printer Descriptions". I then selected LaserWriter 8 in the Chooser, selected my printer, selected Setup, selected Select PPD, and clicked on cust.ppd in the dialog box. At the bottom of the dialog box, I got the message "Does not appear to be a valid PostScript Printer Description file." Should the LaserWriter 8 driver accept a local customization file?  A: The Adobe documentation appears to be incorrect, in that the \*Include example in the 4.1 specification incorrectly leaves out the following line:   |  | | --- | | ``` 	*PPD-Adobe: "4.1" ``` |   The LaserWriter 8 driver and the 4.1 PPD specification require that this line must always be the first line of a PPD file. Adding this line should solve the problem. In general, PPD developers should open the driver's '`PRFS`' resource with ResEdit and turn on full PPD error messages (the driver includes a ResEdit template to make editing this resource easy) to help with debugging. |

#### [Jul 01 1995]

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
