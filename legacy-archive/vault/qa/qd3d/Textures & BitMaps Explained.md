---
title: Textures & BitMaps Explained
apple_id: DTS10001849
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d51.html
archived_at: '2026-07-18T02:38:42.294280Z'
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
| Technical Q&A QD3D51Textures & BitMaps Explained |

|  |
| --- |
|  Q: What is the difference between `Textures` and `Bitmaps`?  A: In general conversation we may use the two terms interchangeably, but actual differences do exist:  __BitMap__  In graphics terms, a `BitMap` is basically an array of one-bit pixels.  __Texture__  A `Texture` is a data structure that contains information for mapping a predefined image onto the surface of a model. A `Texture` usually uses a `PixMap` as the source for the image.  __PixMap__  A `PixMap is` basically an array of pixels of any depth.  There is more information in both the `BitMap` and `PixMap` structures beyond just pixels, such as `rowBytes` and a bounds rectangle. A `PixMap` also contains additional information such as the pixel depth. Look in the quickdraw.h header (or equivalent on PC), or any good graphics programming book for more information.  A `Texture` is not necessarily a mapping of a `PixMap`, as a `Texture` could map dynamic data onto an object in a model, (e. g., the TextureEyes sample uses a QuickTime movie as its source). The `Texture` is just where this data is stored. The information in the Texture is used by a __shader__ to combine information about the Texture, other material properties, lights, position, and orientations. The shader is called as part of the rendering process.  In the quote below, note that shading is the last of seven steps involved in rendering: "Rendering is a general term that describes the overall process of going from a database representation of a three-dimensional object to a shaded two-dimensional project on a view surface. It involves a number of separate processes:  1. setting up a polygon model that will contain all the information which    is subsequently required in the shading process; 2. applying linear transformation to the polygon mesh model ...; 3. culling back-facing polygons; 4. clipping polygons against a view volume; 5. scan converting or rasterizing polygons ... ; 6. applying hidden surface removal algorithm; 7. shading the individual pixels using an interpolative or incremental    shading scheme."  _3D Computer Graphics_ , page 127, by Alan Watt, (Addison-Wesley) |

#### [Aug 21 1996]

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
