---
title: Print Scaling
apple_id: DTS10001764
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd05.html
archived_at: '2026-07-18T02:38:35.416306Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD05Print Scaling |

|  |
| --- |
| ---   Q: I want my application to do its own scaling during printing, so the information that I put around the outside of the page is at a 1:1 ratio. I also need to retrieve the scaling factor from the `TPrint` record for my application, and then set the scaling to 100 percent. How do I retrieve this information, and how do I set the scaling in a print record?  A: When using classic QuickDraw (not QuickDraw GX), the process you describe is not supported. Since the original API was developed when there were only two printers available for the Macintosh, driver developers needed to find a way to store the settings they needed in the print record. Since Apple did not provide an API for this, a multitude of unapproved techniques were used to insert various settings into the print record. As a result, each driver stores information in the print record in a different place.  You can't get the information you need from the edit-text item of the driver - in fact, you should never assume an edit-text item in a dialog is the scaling field, since you have no way of knowing what the field contains. Don't assume anything about the items or the order of the dialog boxes, because printer-driver developers are free to do whatever they want, and many of them have. The ImageWriter, for example, only allows a 50-percent reduction, so it has a checkbox instead of a numerical field. In some drivers, options like this may even be in the job dialog for "user convenience."  Drivers can and do store scaling values, if they support them, anywhere at all in the print record. You can't compare the page rectangle to that returned by `PrintDefault`, because the user may pick a paper size other than the default (for example, it wouldn't work to choose legal paper and get an 8.5 x 11-inch image scaled 100 percent horizontally and 122 percent vertically). This process was designed to be transparent so applications don't have to intervene, but it turned out to be too transparent, in that applications can't determine what the scaling is, even if they need to.  There is no API in classic QuickDraw printing to allow you to set the scaling, although QuickDraw GX does support this. For more information about the way you can do this in QuickDraw GX, see Inside Macintosh: QuickDraw GX Printing.  There is one way you can circumvent this shortcoming in classic QuickDraw, at least partially: You can store a print record in your application resource fork and use it when you print, but bear in mind that this may not work for other versions of the same driver (if the driver's developer chooses to store the scaling information elsewhere in the print record). Thus, you can store a print record in your application that you can validate by calling `PrValidate` (you must do this on any print record you store to ensure that its settings are appropriate for the currently selected driver).  Of course, you need to find the place in the print record where the scaling is stored (one way to do this is with an application called `PrintRecordSpy` that is on the Developer CD: Toolchest edition). Since drivers store this information in various places, this isn't fully compatible with all drivers. However, you can save print handles for all of Apple's drivers in the resource fork. To learn how to save print handles, see page 58 of the January 1990 issue of develop magazine. The code for saving print handles is also on the Developer CD in the periodicals folder (search for develop, issue 1).  You need to save the resources in such a way that you can find them based on the high byte of the print record's `wDev` field. The high byte of the `wDev` field identifies the printer, so adding a number such as 1000 to it augments the meaning of the field (allowing you to specify the type of print-record sub-type for that printer) without destroying the printer identity number. For example, you can add 1000 to the high byte of `wDev`, and use that for the resource id. If you use this approach, be sure to do this for all of Apple's printers.  You now have a print record stored with the scaling set to 100 percent for every driver. You cannot change the print handle between `PrOpenDoc`/`PrCloseDoc` calls, so each page has to be a separate document. For pages that you want to print at 100 percent scaling, load that print handle, and then do the `PrOpenDoc` call.  There are some drawbacks to this approach that you need to be aware of. First, this method doesn't work if a driver is released that has a `wDev` that you haven't included. This could happen if a new and radically different Apple printer were introduced, or it could happen with third-party printers. If it does happen, you can notify the user that they need to set the scaling. This shouldn't be a significant problem unless a third-party printer and driver are used. For example, most of our LaserWriters use the same driver, so if another one is introduced, it will probably follow suit. Eventually, there will be printers that you won't have included, so you should plan for that.  Another drawback is that the user won't be able to choose settings such as landscape-mode printing. Only the settings that are active when you save your print handles can be used, and this may frustrate users.  If you decide to use this method, don't save your print handles as '`PREC`' resources. Instead, make up your own resource type, such as '`PHDL`'. Also, if you need to determine which orientation a user has selected in a print dialog, you can do this by passing the print handle to `PRGeneral` with the `GetRotn` opCode.  When you encounter a new device, you can force the print-style dialog to come up, ask the user to select landscape, and save a print record for the device. This is a bit clumsy, but it works, and you're able to use `PrGeneral` (if supported) to determine if the user actually set the mode. |

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
