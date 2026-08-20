---
title: Extensions vs. Libraries
apple_id: DTS10001835
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d37.html
archived_at: '2026-07-18T02:38:41.148925Z'
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
| Technical Q&A QD3D37Extensions vs. Libraries |

|  |  |
| --- | --- |
|  Q: What's the difference between the QuickDraw 3D extensions and the xxxLib files in the folder Development:Libraries on the QuickDraw 3D SDK CD-ROM?  A: The xxxLib files in the Libraries folder are stub libraries. The stubs are much smaller than the Extensions installed in the System Extensions folder, and, therefore, can be included in your project file without bloating it unnecessarily.  The files in the Extensions folder are the real libraries. When your application runs, it will dynamically link to libraries found in either your application folder or (more commonly) the Extensions folder. Since the system will use the library in your application's folder first (if it's there), you can experiment with new libraries without disturbing other applications that use QuickDraw 3D.  The QuickDraw 3D extensions installed by the installer are the normal extensions; those found in the Development:Debug folder are the extensions with extra debugging code. They will be slower, but during development of your application, they will be much more helpful in tracking down bugs.   |  | | --- | | ``` Extensions			Stubs QuickDraw 3D			  QuickDraw3DLib QuickDraw 3D Viewer		  QuickDraw3DViewerLib QuickDraw3D Accelerator		  QuickDraw3DAcceleratorLib ``` | |

#### [Apr 08 1996]

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
