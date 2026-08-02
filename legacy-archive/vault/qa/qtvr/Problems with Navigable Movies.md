---
title: Problems with Navigable Movies
apple_id: DTS10002052
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr08.html
archived_at: '2026-07-18T02:38:50.726816Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR08Problems with Navigable Movies |

|  |
| --- |
| Q I am having problems with navigable movies. I've set up a model in Stratavision and taken shots starting at a vpan angle of 90x ending at -20x, with 36 columns at each vpan angle. I rotate the object, not the camera, for the horizontal positions, and I move the camera down 10x for each vpan position. This gives me a series of QT movies, one for each vpan angle, with 36 columns each. I then compile them in Premiere, and run the compiled movies through the Navigable movie player, but it doesn't work. After testing the individual movies individually, I've found that the closer I get to 0x, the better the navigation, with 0x working perfectly and 90x working very poorly. What am I doing wrong?   A If you are trying to simulate moving the camera up and down in a straight line, you need to rotate the camera around the object, such that the lens is always kept the same distance from the vertical center of the object. To visualize this concept, think of your object as if it were enclosed in a sphere (there is a diagram of this on page 3-3 of the manual). The only valid camera positions are on the surface of that sphere. All other camera positions will cause image distortion.   [Jun 01 1995] |

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
