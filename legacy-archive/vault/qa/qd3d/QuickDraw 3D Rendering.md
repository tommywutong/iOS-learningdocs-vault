---
title: QuickDraw 3D Rendering
apple_id: DTS10001814
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d16.html
archived_at: '2026-07-18T02:38:40.041410Z'
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
| Technical Q&A QD3D16QuickDraw 3D Rendering |

|  |  |  |
| --- | --- | --- |
|  Q: When I open a file that comes from our translator with NURBS PATCH, the model is drawn in `scrap3d` but not in Spin, SpinLinked, or Enzo, and not in my own application, where I implemented the QuickDraw 3D rendering. Why is this happening?  A: The reason the model doesn't draw with some of the applications that you mention is that the camera information written to the file is not useable with those applications. To avoid this problem, comment out the camera information, as shown here:   |  | | --- | | ```     preceeding lines omitted 		 #		viewangleaspectcamera4: #		Container ( #			ViewAngleAspectCamera ( 0.5235988 1.428571 ) #			CameraPlacement ( #				85.06377 -126.2345 189.3926 # location #				85.06377 37.99321 25.16492 # point of interest #				0 0 1 # up vector #			) #			CameraRange ( 0.01 150000 ) #			CameraViewPort ( -1 1 2 2 ) #		) 		lightgroup5: 		LightGroup ( )     following lines omitted ``` |   This allows the object to draw properly. What is actually happening is that the object is being drawn, but it's not in the field of view for the camera. Both Tumbler and Spin attempt to a best-guess approximation for useable camera settings if these settings are not supplied. This is what Spin used for the camera values:   |  | | --- | | ``` 		viewangleaspectcamera4: 		Container ( 			ViewAngleAspectCamera ( 0.03389506 1.428571 ) 			CameraPlacement ( 				0 0 30 # location 				0 0 0 # point of interest 				0 1 0 # up vector 			) 			CameraRange ( 29.5 30.5 ) 			CameraViewPort ( -1 1 2 2 ) 		) ``` |   If you use something like Spin or Tumbler (which always tries to generate a good view of the data if no camera information is supplied), first get the camera object from the view with some debugging code. Next, get the camera data from the object, and inspect the values that are generated. Then, work your way back to determine why the original values in the camera object differ, and try to adjust them to produce something reasonable. You can also read in the file, determine what values are assigned, write it back out as a text metafile, and investigate the values assigned. |

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
