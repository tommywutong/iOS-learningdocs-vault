---
title: RAVE and DrawSprocket Integration
apple_id: DTS10001883
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-04-20'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d85.html
archived_at: '2026-07-18T02:38:44.845918Z'
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
| Technical Q&A QD3D85RAVE and DrawSprocket Integration |

|  |
| --- |
| ---   Q: How can I integrate RAVE and `DrawSprocket` in my application?  A: RAVE and `DrawSprocket` both perform single and double buffering, so it would be really nice to integrate them together. Unfortunately, there won't be any resources to do this in the near future.  The easiest way to do this is to only use `DrawSprocket` to choose and configure the display, and allow RAVE to handle all of the buffering issues. This also makes sense since the RAVE engine may be able to do the buffering and blitting entirely in hardware.  First, you should walk the list of all RAVE engines, and create a list of engines that your application will successfully run under. Once you've got the list of engines, the next step is to eliminate any `GDevices` from the list that won't support one of those engines. This can be done by iterating over the device list, and checking each device against all of the engines using `QAEngineCheckDevice`. If no engines support that device, you can remove it from the list by reserving a DrawSprocket context on that monitor. You'll never actually activate that context, so you can just call `DSpGetFirstContext` to get the first valid mode, and reserve the context using that information.  When you've finished walking the list of `GDevices`, call `DrawSprocket` to find a valid context. Since you are planning on using RAVE to do your rendering, you should reserve the context using a page count of 1, which tells `DrawSprocket` to not allocate any back buffers.  Once you've activated the context, you should test that one of the RAVE engines you've chosen will run on that device. Some 3D accelerators only work in certain video depths, so you need to test again using `QAEngineCheckDevice` after the mode switch has occurred. Most of the current accelerators will always work in thousands of colors.  You should be prepared to delete all of the RAVE context information and textures before releasing the `DrawSprocket` context or allowing `DrawSprocket` to change video modes. Any resolution change can reorganize memory on the graphics card, which will disturb the RAVE buffers and texture memory.  Alternatively, you can allow the user to choose any monitor and simply default to your own software engine if there isn't a decent 3D hardware solution that will work with that device. [Apr 20 1998] |

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
