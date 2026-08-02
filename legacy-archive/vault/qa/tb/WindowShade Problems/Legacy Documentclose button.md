---
title: WindowShade Problems
apple_id: DTS10002199
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb13.html
archived_at: '2026-07-18T02:38:55.665248Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB13WindowShade Problems |

|  |
| --- |
| Q WindowShade is causing a problem for our application, which saves the window position and size when it saves a document to disk. If our application's windows are "rolled up" using WindowShade, it's windows appear to have zero height, and they are saved that way. Is there any way to determine if a window is "rolled up"? If so, can we determine what its true size is and what the global coordinates of the top left corner of the content region are, so that we can restore and reposition the window when the document is reloaded from disk.   A When WindowShade rolls up a window, it hides the content region of the window. You can tell when a window is shaded, because its contRgn is set to an empty region, and its strucRgn is modified to equal the new "shaded" window outline. WindowShade doesn't do anything with the grafPort, so if you need to store the window's dimensions before closing it, you can obtain them from the window's portRect. When you open your window again, you can look at your window's data structure, obtain the saved portRect info, and size the window appropriately. To determine if a window is rolled up you would use a test such as the one below:   ``` if (EmptyRgn(((WindowPeek) myWindow)->contRgn))   //our window is rolled up ```   With regard to the window's position, WindowShade empties the content region of the window it rolls up by setting the bottom coordinate of the contRgn's region bounding box equal to the top coordinate of the contRgn's region bounding box, but the contRgn's top, left, and right coordinates are not changed. These are global coordinates, so you can obtain them and then store the contRgn top and left coordinates as follows:   ``` Point              contentPosn; contentPosn.v = (**((WindowPeek)myShellWindow)->contRgn).rgnBBox.top; contentPosn.h = (**((WindowPeek)myShellWindow)->contRgn).rgnBBox.left; ```   You should track the strucRgn's top and left coordinates to position your windows later, as shown below:   ``` Point strucPosn;  strucPosn.v = (**((WindowPeek)myShellWindow)->strucRgn).rgnBBox.top; strucPosn.h = (**((WindowPeek)myShellWindow)->strucRgn).rgnBBox.left; ```  [May 01 1995] |

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
