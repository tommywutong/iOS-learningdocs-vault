---
title: Order for using the Scene Editor
apple_id: DTS10002065
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr21.html
archived_at: '2026-07-18T02:38:51.438653Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR21Order for using the Scene Editor |

|  |
| --- |
| Technical Q&AQTVR 21 - Order for using the Scene Editor (1-Sept-95)  Q Is there a particular order in which I should use the Scene Editor?  A Here's a recommended order:   1) Stitch all panoramas.    2) Name PICTs: <some name>.01.srcPict,<some name>.02.srcPict,...    3) Duplicate the Scene Editor folder and place panos in the Source Picts folder.    4) Make miniPicts in Photoshop for each pano and place in Link Backdrop Picts folder.    5) Fill out pages 1 & 2 of Scene Editor.    Note that if you don't have object hot spots, change the Composited Hotspot Directory on page 1 to be the Link Hot Spot Picts directory and the file extension to be .linkPict.    6) In node mode, place nodes on page 3 of the Scene Editor in their appropriate places. Do not attempt to link yet.    7) Export Worksheets and Resources.    8) Quit Scene Editor and execute the Worksheet that you just exported.    9) Reload Scene Editor and create all of your links and hotspots.    10) Export Worksheets, Resources, and Picts.    11) Composite your link and object hot spots in Photoshop.    12) Execute your new Worksheet. |

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
