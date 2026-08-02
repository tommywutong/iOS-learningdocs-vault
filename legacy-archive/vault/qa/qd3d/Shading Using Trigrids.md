---
title: Shading Using Trigrids
apple_id: DTS10001819
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d21.html
archived_at: '2026-07-18T02:38:40.317406Z'
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
| Technical Q&A QD3D21Shading Using Trigrids |

|  |  |
| --- | --- |
|  Q: I am trying to shade a 3D landscape using Trigrids, but I can't get this to work, and the examples in the documentation are not very helpful. The landscapes look fine as wire frames, but when I turn on shading, I just get one continuous gray blob. If I try to use a more advanced shading technique (e.g., pixmap), my application crashes.  A: Try setting up a surface shader (either Phong or Lambert). Assuming you are holding your displayable objects in a display group or an ordered group, you can do this in the following way:   |  | | --- | | ``` //---------------------------------------------------------------------- // attach a shader to the group TQ3Status MyAddShaderToGroup( TQ3GroupObject group ) { 	TQ3ShaderObject	illuminationShader = Q3PhongIllumination_New(); 	Q3Group_AddObject(group, illuminationShader); 	Q3Object_Dispose(illuminationShader); 	return(kQ3Success); } ``` |   Alternatively, you can create a shader object, and draw it before any of your geometries in your submit procedure. Remember that if you are using a plain display group, the shader object must be the first object placed in the group, or all the objects that are put in the group before the shader will be flat-shaded (this does not apply to ordered display groups).  The latest samples, libraries, and headers are available on the Developer CD. See also Apple's [QuickDraw 3D home page](http://www.info.apple.com/qd3d/QD3D.HTML) for the most current 3D development information. |

#### [Jul 15 1995]

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
