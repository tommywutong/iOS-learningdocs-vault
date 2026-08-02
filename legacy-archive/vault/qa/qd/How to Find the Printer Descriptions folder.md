---
title: How to Find the Printer Descriptions folder
apple_id: DTS10001905
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-11-17'
source_url: https://developer.apple.com/library/archive/qa/qd/qd52.html
archived_at: '2026-07-18T02:38:38.239236Z'
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
| Technical Q&A QD52How to Find the Printer Descriptions folder |

|  |  |
| --- | --- |
| ---   Q: Most of the special system folders have documented ways to access them regardless of the localization of the operating system. We have been unable to find a way to access the "Printer Descriptions" folder on foreign systems without explicitly knowing the localized name of the folder. Can you point us to where this might be documented or how to access it?  A: Unfortunately, under System 7.x, there is no good way to do this. The only way that developers have been able to install their PPDs correctly is to use a 2-tiered approach:   1. Use `PrGeneral` with the `PSPrimaryPPDOp` opcode to    retrieve the `FSSpec` record locating the current PPD file chosen for the printer,    and the parent directory that you are interested in. (from "LaserWriter 8 for Fun and Profit"    in [_develop_issue 16](https://developer.apple.com/library/archive/dev/techsupport/develop/bysubject/printing.html)    (page 78)). Then place the PPD file there. 2. If your driver does not support `PrGeneral`, then you must look for a folder    called 'Printer Descriptions' and install the PPD there. This of course requires    a list of what that folder gets named for various localized systems.   Under System 8.0, Apple has added a Find Folder Selector for this folder, '`ppdf`', that makes installation of your PPD easier for Mac OS 8.0 and above. Please see _[Inside Macintosh: Macintosh Toolbox Essentials,](https://developer.apple.com/library/archive/documentation/mac/Toolbox/Toolbox-2.html)_page 7-54 for more information on `FindFolder`.    |  | | --- | | __Note:__  The LaserWriter driver (version 8.5.1 and before) does not take advantage of the '`ppdf`' FindFolder feature and still only looks in the Extensions:Printer Descriptions folder for PPDs (as opposed to System: Printer Descriptions). This will be fixed in a future release of the LaserWriter 8 driver. | |

#### [Nov 17 1997]

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
