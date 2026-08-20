---
title: Selecting a PPD When no Printer is Available
apple_id: DTS10001771
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd12.html
archived_at: '2026-07-18T02:38:35.844948Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD12Selecting a PPD When no Printer is Available |

|  |
| --- |
| ---   Q: We are writing an application which has a somewhat unusual requirement: The user must be able to use the LaserWriter 8 driver to select a PPD, even when no printer is available on the network. We supply an option in our program to patch the user's Laserwriter driver, which allows LaserWriter 8.0 to perform the setup with no printer.  Do the LaserWriter 8 drivers provide any way to do this without patching the driver, and will this patch work on later LaserWriter 8 drivers, in particular 8.1.1, 8.2, and 8.2.2?  A: At present, there is no way to do this. Many customers have requested a feature that would allow them to either set up a printer or select a PPD file when there is no device visible in the chooser. This feature is particularly attractive to PowerBook users, and it is something we expect to add in a future version of the driver. |

#### [Jul 01 1995]

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
