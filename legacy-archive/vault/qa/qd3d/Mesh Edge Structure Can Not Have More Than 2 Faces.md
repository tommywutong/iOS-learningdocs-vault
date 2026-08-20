---
title: Mesh Edge Structure Can Not Have More Than 2 Faces
apple_id: DTS10001863
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d65.html
archived_at: '2026-07-18T02:38:43.487066Z'
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
| Technical Q&A QD3D65Mesh Edge Structure Can Not Have More Than 2 Faces |

|  |
| --- |
| ---   Q: I am using the mesh geometry in my application. Is it possible to make an edge connected to three faces?  A: No. The mesh edge data structure addresses two mesh vertices and two mesh faces (in which either face may be empty). So the mesh edge structure can not have more than two faces. There are provisions in the mesh itself to have more than two faces between two vertices, but this is done by attaching multiple edge structures onto the given vertex structures. So as you see each edge structure still has only two faces adjacent to it. The mesh bookkeeping functions keep track of the adjacencies, but there are no API calls which will cycle through and return all the faces for all those parallel edge structures, so you would have to do this yourself with a loop which looks for identical vertices.  In general, meshes are optimized to work with at most two faces per edge, so it's recommended to use it that way. The structures can handle the case you mention, but the API doesn't allow you to easily extract the information. (e.g., `Q3Mesh_GetEdgeFaces()` returns only the two faces that are specified in the given edge structure, and therefore you must search for the other parallel edge structures). [Jul 11 1997] |

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
