---
title: QD3D Is Not Thread-Safe
apple_id: DTS10001870
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d72.html
archived_at: '2026-07-18T02:38:43.901476Z'
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
| Technical Q&A QD3D72QD3D Is Not Thread-Safe |

|  |  |
| --- | --- |
| ---   Q: I am trying to do rendering in a cooperative thread while another thread is doing something else. I thought I would yield from within a rendering loop, but it seems the rendering loop gets executed only once no matter how lengthy the rendering is. Could someone give me some suggestions?  A: The current version of QuickDraw 3D is not thread safe so I would not recommend that you do this. Also QuickDraw itself is not thread safe, so it would be dangerous to even have two threads that do any drawing at all.  However, if you are doing QD3D stuff in one thread and no drawing in the other thread, you could potentially get 3D to yield time by installing a view idle handler. I haven't not tried this from a threaded application, but you may want to give it a go.  Here is a small snippet that shows how you'd define and install the view idle method:   |  | | --- | | ``` TQ3Status MyIdleMethod( TQ3ViewObject view,  const void *idleData)  ; TQ3Status MyIdleMethod( TQ3ViewObject view,  const void *idleData) { 	TQ3Status 	returnResult = kQ3Success ; 	/* do whatever you need to do here */  	 	/*  	 * NOTE: don't do anything that is particulalry time consuming  	 * or your rendering will take forever!!	 	 */ 	return returnResult ; }  ... 		/* install the idle proc defined earlier */ 		myStatus = Q3View_SetIdleMethod ( gDocument.fView, MyIdleMethod, NULL )  ; ... ``` |   Note that you'll be called more often from the wireframe renderer than the interactive renderer. Your mileage may vary so you'll need to play around with this stuff. [Jul 11 1997] |

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
