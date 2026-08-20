---
title: Use QuickDraw 3D B1C3 Library to Eliminate User Breaks
apple_id: DTS10001817
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d19.html
archived_at: '2026-07-18T02:38:40.201162Z'
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
| Technical Q&A QD3D19Use QuickDraw 3D B1C3 Library to Eliminate User Breaks |

|  |
| --- |
|  Q: I built a very simple file in 3DMF binary format. Tumbler can read it, but Metafile Read cannot (a user break appears). Typing "g" in MacsBug allows Metafile Read to recover and show the cube. I also get a user break with this file in my application, which uses the code from the Tumbler example. The user break in MacsBug is crashing the Metrowerks Debugger, so I am forced to debug with `DebugStr`. Is there a workaround?  A: You should be able to eliminate the user break problem by replacing your current library with the QuickDraw 3D B1C3 library, which is posted on AppleLink and on the Apple FTP site. The updated source for the metafile-read snippet is also available at these sites. Earlier versions of the library had a number of problems reading metafile data, but these problems have been eliminated in the B1C3 build.  The problem of `DebugStr` crashing the Metrowerks Debugger can be caused by an odd combination of CodeWarrior, the System 7.5 update, and PowerMac debug services. If you are using CodeWarrior 5.5, you should upgrade your copy of DebugServices to the most recent version. If you are using CodeWarrior 5.0, try removing the system update (unfortunately, the only way to do this is to re-install System 7.5).  Also, if you are using the Metrowerks Debugger and you find yourself in MacsBug, you can propagate the exception (in the case of PowerPC exceptions) to the high-level debugger by typing GP in MacsBug. |

#### [Jun 01 1995]

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
