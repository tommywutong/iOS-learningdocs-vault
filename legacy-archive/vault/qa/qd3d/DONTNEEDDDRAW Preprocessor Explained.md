---
title: DONT_NEED_DDRAW Preprocessor Explained
apple_id: DTS10001880
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d82.html
archived_at: '2026-07-18T02:38:44.613061Z'
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
| Technical Q&A QD3D82DONT_NEED_DDRAW Preprocessor Explained |

|  |
| --- |
| ---   Q: I'm trying to build the Win32 sample from the QuickDraw 3D SDK using the MSVC++ 4.0 build environment. However, I keep getting the error: "can't find interface file ddraw.h". What's going on?  A: You'll need to include the interface file "ddraw.h" in your build if you code makes use of the `Q3DDSurfaceDrawContext_XXX` routines. If you don't need `Q3DDSurfaceDrawContext_XXX` support in your application, define the preprocessor DONT_NEED_DDRAW in your application and the interface file "ddraw.h" won't be included in your build. An easy way to do this in MSVC++ 4.2 for a project is to go into the "Project Settings" window for the project (under the "Build" window, choose the "Settings" menu item), and in the "Preprocessor definitions" edit box add a definition for the preprocessor DONT_NEED_DDRAW.  However, if you do need `Q3DDSurfaceDrawContext` support in your application you'll need to actually get the "ddraw.h" interface file. This file can be found in MSVC++ 4.2, the Windows 32 SDK, or the Windows Game SDK. [Jul 11 1997] |

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
