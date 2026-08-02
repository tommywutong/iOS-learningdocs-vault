---
title: Determining Which Features Are Supported by Specific Renderers
apple_id: DTS10001829
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d31.html
archived_at: '2026-07-18T02:38:40.839054Z'
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
| Technical Q&A QD3D31Determining Which Features Are Supported by Specific Renderers |

|  |  |
| --- | --- |
|  Q: Using the QuickDraw 3D API, how can I ascertain whether transparency (or csg or shadows) is supported by any particular renderer?  A: As of version 1.0.4, the QuickDraw API has no support for determining which features are supported by specific renderers. This capability is planned for a future release. You can, however, use the QAEngineGestalt() call to get much of the information you need.    |  | | --- | | __Note:__  `QAEngineGestalt` is found in the Rendering Acceleration Virtual Engine (RAVE) API, not the QD3D API. |    Search the RAVE3D.h file for `QAEngineGestalt`, and look for the associated comments regarding what kind of selectors you can use in you queries. You'll also need to call `QADeviceGetFirstEngine` to get a reference to the first 3D accelerator card. Then you must call `QADeviceGetNextEngine` to get references to any other 3D accelerator cards in the system. `QADeviceGetNextEngine` will return NULL if there are no more cards.  Remember that, as of version 1.0.4, transparency is not supported if there is no 3D acceleration card. CSG (Constructive Solid Geometry) and shadows are unimplemented features that are scheduled for a future version of QuickDraw 3D, and will also most probably require hardware assist. What is RAVE RAVE stands for Rendering Acceleration Virtual Engine (RAVE) API. It is a standard API specification for applications which make use of any 3D acceleration provided by 3D accelerator hardware. It also specifies the API for drivers (aka "drawing engines") of 3D accelerator hardware. Because RAVE describes both an application API and a driver API, RAVE is often referred to as a "thin veneer" between the two layers. Application authors who use the RAVE layer are guaranteed the fastest possible access to hardware acceleration; hardware vendors who supply RAVE-compliant drivers for their cards are guaranteed a large base of applications compatible with their hardware. |

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
