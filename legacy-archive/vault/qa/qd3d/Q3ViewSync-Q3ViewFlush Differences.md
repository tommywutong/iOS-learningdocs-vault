---
title: Q3View_Sync/Q3View_Flush Differences
apple_id: DTS10001866
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d68.html
archived_at: '2026-07-18T02:38:43.650546Z'
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
| Technical Q&A QD3D68Q3View_Sync/Q3View_Flush Differences |

|  |
| --- |
| ---   Q: What is the difference between `Q3View_Sync` and `Q3View_Flush`? I have been calling both of them when I want to do a progressive blit, but I get a warning from the QuickDraw 3D debug extensions about being within a submitting loop when calling one of them (not sure which).  A: `Q3View_Flush` is intended to force the image to be displayed, and as such it's called within submitting loop. It is non-blocking, so it seems like it's the one you're looking for.  `Q3View_Sync` is a blocking function that only returns after the renderer has finished its frame, and the submit loop has been ended. Thus, it is to be called only outside the submitting loop. Note that a renderer may be "asynchronous" in that it may complete its frame after the submit loop is exited. In that case, the image will appear in the draw context (i.e., within the window) sometime later, when the renderer has finished. The `Q3View_Sync` call waits until the renderer is done. (Of course, if it is already done, then the call returns immediately). Note that if the application doesn't call `Q3View_Sync`, and the renderer is asynchronous, the view causes a sync at the start of the next frame, and if the renderer is not done by then, the application will block, and then resume once the renderer is done.  Often, one's application might make a call to `Q3View_Sync` right after the submitting loop, in which case the application will always synchronize with the rendering - that is, it won't continue until each frame is completed. Obviously, one might want the application to continue on instead, and wait until rendering is completed \*after\* performing some other tasks or processing (i.e., you put the call to `Q3View_Sync` later in the code, at the point you'd want to be assured the image was completed before going on). In the simplest case, you can just forgo the `Q3View_Sync` call altogether, and be assured that the image would appear before the next frame was started. [Jul 11 1997] |

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
