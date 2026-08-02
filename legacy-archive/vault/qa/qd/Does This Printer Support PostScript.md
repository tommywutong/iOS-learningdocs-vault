---
title: Does This Printer Support PostScript?
apple_id: DTS10001899
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-09'
source_url: https://developer.apple.com/library/archive/qa/qd/qd46.html
archived_at: '2026-07-18T02:38:37.911971Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD46Does This Printer Support PostScript? |

|  |  |
| --- | --- |
| ---   Q: I am trying to find a way for my application to determine if it is using a Postscript printer or not. For performance reasons, I'd like to send custom PostScript instead of a PICT to the printer if I can. Is there an API to find out if the currently selected printer uses PostScript?  A: There is no guaranteed way of doing this. For Apple's LaserWriters, you can determine this by looking at the wDev field in the print record of the currently selected printer. In order to determine whether the current printer is PostScript, here is a quote that is hidden in one of our older Technotes, [Technote QD10 "Picture Comments--The Real Deal"](https://developer.apple.com/library/archive/technotes/qd/qd_10.html):    |  | | --- | | "The high byte of the prStl.wDev field of the print record identifies a printer driver species; a value of $03 tells you that the printer driver belongs to the PostScript LaserWriter driver ancestry..." |    This Technote may be useful to you if you haven't already read it. You should also look at [Inside Macintosh: Imaging With QuickDraw](https://developer.apple.com/library/archive/documentation/mac/QuickDraw/QuickDraw-2.html) for more generic information on the print record.  However, although the Apple LaserWriter driver has a `wDev` of 3, third-party printer drivers for PostScript devices do not, so if your application determines whether or not to send PostScript based on `wDev` alone, your application may incorrectly print with QuickDraw on third-party PostScript devices. |

#### [Jan 09 1997]

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
