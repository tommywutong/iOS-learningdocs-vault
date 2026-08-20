---
title: Setting Landscape Printing from an Application
apple_id: DTS10001907
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-01-16'
source_url: https://developer.apple.com/library/archive/qa/qd/qd54.html
archived_at: '2026-07-18T02:38:38.362891Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Hardware & Drivers](https://developer.apple.com/referencelibrary/Printing/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A QD54Setting Landscape Printing from an Application |

|  |  |
| --- | --- |
| ---   Q: How can I set landscape mode printing from within my application?  A: Apple has always cautioned applications against trying to force landscape printing on the user; however, there are certain apps in the marketplace that have good reason to do this. Therefore, even though there is no API in "classic" printing to set landscape mode, here is an overview of a method that you may want to consider implementing if you need to force the orientation of your print job:   1. Call `PrValidate` on your print record to ensure that the contents of    your print record are compatible with the current active printer driver. 2. Look at the values of the paper rectangle in the print record. If it    is wider than it is tall, your user has already selected landscape mode. If it    is taller than it is wide, then you need to put up an alert asking your user to    choose landscape printing, followed by a call to `PrStlDialog` so they can    set the orientation. 3. Call `PrValidate` again to ensure that the user did change to    landscape mode. If the paper rectangle is still taller than wide, go    back to step 2 and ask the user to set the orientation again because they    did not follow or did not understand the instructions in step 2. 4. Save the print record with the correct orientation in the resource    fork of the preferences file, and read it back in each time the user    needs to print. For information on how to save print records, refer to    the Premier Issue of _develop_ 1990, page 58. By saving and    using the saved print record, the user is only bothered by the    `PrStlDialog` \*once\*. Thereafter, the print record is restored from    preferences when printing needs to occur. 5. If the user changes printer drivers in the Chooser, the call to    `PrValidate` will fail, and `PrDefault` must be called.    This will make a new print record for the new printer driver, and it will default to portrait mode    (not landscape mode), so, go back to step 2.     |  | | --- | | __Note:__  Every printer driver implements its orientation settings differently, so this method may not work across all printer drivers. Also, if your customer frequently changes printers, this method may not be an acceptable solution. | |

#### [Jan 16 1998]

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
