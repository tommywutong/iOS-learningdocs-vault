---
title: Printing, Forward and Reverse Line Feeds
apple_id: DTS10001762
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-12-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd03.html
archived_at: '2026-07-18T02:38:35.312505Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD03Printing, Forward and Reverse Line Feeds |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: What are the possible number-type values for the forward and reverse line feeds?  A: These are the values:  Name Value   |  | | --- | | ``` rasterNumNone		0 ``` |   Only the prefix and postfix strings are sent to the device, not the number itself.   |  | | --- | | ``` rasterNumDirect		1 ``` |   This pads the number to `minwidth` (minwidth is a field in the `ropt` struct) bytes by appending 0s to the front of the number, and then puts the hex data into the stream.   |  | | --- | | ``` rasterNumToAscii	2 ``` |   This is similar to `rasterNumDirect` (above), except the number is converted to ASCII and then front-padded with the pad character specified to make it `minwidth` characters long. For example, the ImageWriter requires four-digit numbers, so `minwidth` would be set to four, the `padchar` would be 0, and this attribute would be set. |

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
