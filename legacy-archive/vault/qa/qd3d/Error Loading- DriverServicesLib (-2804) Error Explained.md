---
title: 'Error Loading: DriverServicesLib (-2804) Error Explained'
apple_id: DTS10001857
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d59.html
archived_at: '2026-07-18T02:38:42.917245Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD3D59Error Loading: DriverServicesLib (-2804) Error Explained |

|  |
| --- |
|  Q: I just installed QuickDraw 3D 1.5.1 on my Macintosh. However, when I boot my machine I drop into MacsBug with the error message: "Error Loading: `DriverServicesLib` (-2804)"  A: Sounds like you're using a non-PCI PowerMac (e.g., 6100/7100/8100) with the QD3D 1.5.1 \*debug\* extensions. The simple solution to your problem is to remove the "Apple QD3D HW Driver" and "Apple QD3D Plug-in" components from your Extensions folder. These are for running with the Apple QD3D accelarator card, available only on PCI PowerMacs (8500, 9500, etc.).  `DriverServicesLib` is a library used by drivers on PCI-based machines and is not found on non-PCI machines, so when QD3D RAVE tried to load the 'Apple QD3D HW Plug-in' shared library, the Code Fragment Manager reported back that the `DriverServicesLib` could not be found, hence the error message above. With the non-debug versions of all the libraries you'll never see any of these error messages. |

#### [Jul 11 1997]

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
