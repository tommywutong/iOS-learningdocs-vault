---
title: Page Setup/Format Dialog Extensions
apple_id: DTS10001247
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd32.html
archived_at: '2026-07-18T02:29:33.698276Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD32Page Setup/Format Dialog Extensions |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I want to create an extension for the Page Setup/Format dialog that performs "Flipping" functions. Is it feasible to create an extension for the Page Setup/Format Dialog?  A: There is nothing to prevent you from creating an extension that adds a panel to the Page Setup dialog. Most extensions add to the Print dialog because, in most cases, this is the proper place to add a panel so the functionality of the extension affects the entire output, and because what extensions typically do is best suited for the Print dialog. Print extensions typically add to the Print dialog; drivers and applications typically add to the Format dialog.  However, if you're trying to modify the Confidential extension so that it adds to the Page Setup dialog, you have a bit more work to do. In addition to changing the `'over'` resource, the `Forward_Job` call, and the name of the override function, you have to make changes to the code that adds the tag to the collection item.  The override calls a routine called `SetUpPrintPanel()` to add a new CollectionItem to the Job to store the confidential stamp information.  Since you want to change the extension so that it adds to the Page Setup dialog, you have to change this routine so that it adds the Collection to the Job's default Format object. Similarly, you have to change `theGetStamp()` routine so that it gets. Finally, you have to repeat all of these steps to add the panel to the Custom Page Setup dialog.  There is also another way that you can test your `PageSetup` panel. It is possible for an application to add a `PageSetup` or `CustomPageSetup` override. There are examples (Experiment no.9 and Banana Jr.) on the QuickDraw GX SDK that demonstrate the latter. You might try adding your flipping code to one of these. |

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
