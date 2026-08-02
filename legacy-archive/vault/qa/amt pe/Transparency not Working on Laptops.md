---
title: Transparency not Working on Laptops
apple_id: DTS10001128
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/amt_pe/amt_pe26.html
archived_at: '2026-07-18T02:29:24.017475Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Apple Applications](https://developer.apple.com/referencelibrary/AppleApplications/index.html)

|  |
| --- |
| Technical Q&A AMTPE26Transparency not Working on Laptops |

|  |
| --- |
| ---   The Apple Media Tool and Apple Media Tool Programming Environment products have been discontinued. For more information check out: [AMT/PE Discontinued](https://developer.apple.com/library/archive/qa/amt_pe/whatsup.html).  Q: We have been seeing a problem on certain laptops where transparency for PICT images doesn't work. The symptoms are that the white areas of a graphic object are visible on the screen instead of being transparent. What would cause this and how can we work around it?  A: There is a system-level command that, if missing, could cause transparency to fail. This command is "transparency=bitmap", and it should be in the AMT.INI file in the Windows directory. If this command is not there, add it to the file (you may have to create the AMT.INI file if it doesn't presently exist).  If you are using Apple Media Tool 1.2, the default behavior (with no AMT.INI) is to compute the transparency in software. To force the hardware to compute the transparency, you must have an AMT.INI file that includes "transparency=bitmap" (not "transparency=driver").  Some Apple Media Tool applications create an .INI file that is named other than AMT.INI in the same directory as their executable file. If you use such a file, make sure it contains "transparency=bitmap", not "transparency=driver". |

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
