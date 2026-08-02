---
title: Metafile Specification Discrepancies
apple_id: DTS10001800
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d02.html
archived_at: '2026-07-18T02:38:39.209394Z'
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
| Technical Q&A QD3D02Metafile Specification Discrepancies |

|  |  |  |
| --- | --- | --- |
|  Q: According to the _3DMF Object Spec_, the `FaceAttributeSet`, `GeometryAttributeSet`, `VertexAttributeSet`, and `ViewAttributeSet` objects have been replaced with a single, context-sensitive, `AttributeSet` object. The Metafile 3D parser does not accept the old keywords, while Spin for Beta accepts both the old and new keywords, the _3DMF Object Spec_ documentation shows only the new keywords, and the text files on the CD contain only the old keywords. Which of these sources is correct?  Also, the _3DMF Object Spec_ indicates that the syntax of the grouping keywords has changed. For example, what was previously:   |  | | --- | | ```       DisplayGroup()        ...        EndGroup() ``` |   now should be:   |  | | --- | | ``` 	BeginGroup (  	    DisplayGroup ( )  	)  	... 	EndGroup ( )  ``` |   The Metafile 3D parser does not accept either the old or the new syntax, Spin for Beta seems to accept both, the _3DMF Object Spec_ consistently shows only the new method, and the text files on the CD contain only the old method. Which syntax is correct?  A: The pre-final versions of the metafile descriptors are now obsolete, and they should not be used. The metafile specifications are now final, and the final version is the only version supported. For this reason, all our example files need to be revised, and we are trying to complete this task in time for the release of the QuickDraw 3D SDK. |

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
