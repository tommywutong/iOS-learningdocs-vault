---
title: List Manager & LClick
apple_id: DTS10002195
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb09.html
archived_at: '2026-07-18T02:38:55.466081Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB09List Manager & LClick |

|  |
| --- |
| Q Is there any way I can stop LClick from hiliting the cells when users scroll the cursor outside the list's rView area? My program allows users to select more than one item from a list and then DRAG these selected items to another list and DROP them there. But I run into a problem with the LClick function when I hold down my mouse and drag these items OUTSIDE the list's rview area. This function still hilits other cells when I move my cursor up or down. Orginally, I only selected 3 items, but now I have more than 3 items highlighted because of the resulting action by LCLICK. I already looked at the sample code ModalList: it has this problem too.   A If you want to use LClick and not change the hilite of cells when the mouse leaves the rView of the list, the best way is to install an LClickLoop procedure and check where the mouse is at any given time. If the mouse is outside of your list's rect as in:  ```     GetMouse(&localPt);     if (PtInRect(localPt, &(*list)->rView) == false) {     // we're out of the list, return false     return false;  }  else     return true; ```   return false to tell the List Manager that the current click should be aborted. It turns out that this is a nice way to start a drag as well, since you know that the mouse has left the rect. [May 01 1995] |

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
