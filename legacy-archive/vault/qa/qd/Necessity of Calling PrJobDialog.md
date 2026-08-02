---
title: Necessity of Calling PrJobDialog
apple_id: DTS10001790
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd31.html
archived_at: '2026-07-18T02:38:37.078890Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Carbon](https://developer.apple.com/referencelibrary/Printing/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QD31Necessity of Calling PrJobDialog |

|  |
| --- |
| ---   Q: Do I need to call `PrJobDialog` to print a document? Why?  A: Yes. In _Inside Macintosh:Imaging with QuickDraw_, [pages 9-18 and 9-19,](https://developer.apple.com/library/archive/documentation/mac/QuickDraw/QuickDraw-408.html#HEADING408-28) it states:  "When writing an application, the code you provide that handles printing is referred to as the _printing loop_. A printing loop calls all the Printing Manager routines necessary to print a document. In general, a printing loop must do the following tasks:  [...]  \* It must display the job dialog box as appropriate by using the `PrJobDialog` function or, for a customized job dialog box, the `PrDlgMain` function. (When the user is printing from the Finder, display the job dialog box only once, and then use the `PrJobMerge` procedure to apply the information from this dialog box to any other documents selected by the user.)  [...]"  The reason for this is that many drivers (most notably LaserWriter 8) don't initialize the job-specific settings until `PrJobInit` is called. Without this call, they fall back on the default, which is usually stored in the driver in the PREC 0 resource. This default may not have the settings that your user desires.  The normal definition of the PREC (which maps to a `TPrint` structure) doesn't have as much space as LaserWriter 8 needs. Because of this, LaserWriter 8 stores some settings in this PREC 0 resource, and stores others in the "LaserWriter 8 Prefs" file. This separation of LaserWriter settings can wreak havoc on a job run without the `PrJobDialog` call.  If you absolutely MUST not display the `PrJob` dialog, there are two ways to work around it. These are not supported methods, and by using either of them you've just made your application hostile to QuickDraw GX and your application may break with future releases of the LaserWriter 8 driver.  That said, you can either:   1. Call `PrJobDialog` either when you make your final build, or have users    do it as part of their preferences (or both), and save the resulting print record. Every time    you print, merge that print record in with a call to `PrJobMerge`. This way each    document can have its own page setup, accomodating things like printing on A4 paper instead of letter. OR 2. "Display" the dialog, but never let the user see it. You can accomplish this by    calling `PrJobInit`, moving the resulting dialog offscreen, dismissing the    dialog yourself, and calling `PrDlgMain`. Please see this [sample file](https://developer.apple.com/library/archive/qa/qd/downloads/InhibitPrJob.hqx)    for an idea of how to accomplish this.   See _Inside Macintosh: Imaging with QuickDraw_, [Chapter 9](https://developer.apple.com/library/archive/documentation/mac/QuickDraw/QuickDraw-406.html) for further information on the Macintosh Print Manager. |

#### [Nov 01 1995]

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
