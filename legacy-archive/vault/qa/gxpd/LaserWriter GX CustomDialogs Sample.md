---
title: LaserWriter GX CustomDialogs Sample
apple_id: DTS10001245
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd30.html
archived_at: '2026-07-18T02:29:33.613074Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A GXPD30LaserWriter GX CustomDialogs Sample |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I used the SDK Custom Dialogs sample driver as the basis for the compatibility part of our GX PostScript driver, and I added an Options dialog to it for our printer-specific features. I have two problems with it when using applications that aren't GX-aware:   1. For non-GX-aware applications, the page size always is defaults to the fifth paper size. As a result, whichever paper type is the fifth one listed in the resource file that has the `'ptyp'`s in it becomes the default paper size in the GX compatibility driver. This is, of course, reflected in the Page Setup dialog. 2. The driver always defaults to having the "Print To File" checkbox on.   What can I do about these problems?  A: Both of these quirks in the sample driver that you describe (improper default paper type and the "Print to File" check box defaulting to on) can be fixed by modifying the `'PREC'` 0 resource in the driver.  When an old-style-printing application calls `PrintDefault()` to request the default old-style print record from the current printer driver, the driver gives it the contents of the `'PREC'` 0 resource. Then, when the application calls `PrJobDialog` or `PrStlDialog()`, it passes in that print record. In its overrides, the GX printer driver interprets the contents of the old-style-printrecord in order to set up the states of the button, checkboxes, etc. in the old-style dialogs.  To determine which paper type radio button to select in the old-style page-setup dialog, QuickDraw GX compares the page rect of the old-style-printrecord to the rects of all the paper types in the driver (or paper-type extensions, such as "3-Hole Punch"), and tries to find the best match. Because of the way that the old-style-printrecord in the `CustomDialogs` sample is defined, that best match turns out to be the fifth paper type in your list. So, to fix this quirk, all you have to do is change the bounds setting in the `'PREC'` 0 resource so that it matches the bounds of the US Letter paper type in the driver.  To determine the state of the "Print to disk" checkbox, the driver looks at the `UIOffset` bit of the old-style-printrecord. (One might not think to look at this bit, but old-style-printrecords are limited to 120 bytes, and there was no better place for this driver to store this information.) Because the `'PREC'` 0 resource in this driver has this bit set, the checkbox defaults to on. So, to fix this quirk, all you have to do is set this bit off. |

#### [Aug 01 1995]

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
