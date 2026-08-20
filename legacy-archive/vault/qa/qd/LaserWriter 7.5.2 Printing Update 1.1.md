---
title: LaserWriter 7.5.2 Printing Update 1.1
apple_id: DTS10001795
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-22'
source_url: https://developer.apple.com/library/archive/qa/qd/qd36.html
archived_at: '2026-07-18T02:38:37.349144Z'
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
| Technical Q&A QD36LaserWriter 7.5.2 Printing Update 1.1 |

|  |
| --- |
| ---   Q: What does the 7.5.2 Printing Update 1.1 update? Why do I need it?  A: This extension fixes a printing problem that may occur on Power Macintosh 7200, 7500, 8500, and 9500 computers using System 7.5.2. Without this fix, your computer may freeze if you attempt to print on a network-based printer that is already busy, and it may be necessary to restart your computer.  The update contains a new version of the LaserWriter driver (8.3.2) and also a fix to serial DMA. The changes fix the ATP and PAP networking protocol layers.  The updates you will need are:  [7.5.2 Printing Update 1.1](http://swupdates.info.apple.com/cgi-bin/lister.pl%3FApple_Support_Area/Apple_Software_Updates/US/Macintosh/Printing/Other_Printing) and [Open Transport 1.0.8](http://swupdates.info.apple.com/cgi-bin/lister.pl%3FApple_Support_Area/Apple_Software_Updates/US/Macintosh/Networking-Communications/Open_Transport).  An updated version of the PAP.WrkStation.o library will be distributed on a future version of the Mac OS SDK and developers who have licensed the library will be notified via email when the new library is available. |

#### [Nov 22 1995]

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
