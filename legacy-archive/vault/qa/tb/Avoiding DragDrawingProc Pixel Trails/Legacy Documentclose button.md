---
title: Avoiding DragDrawingProc Pixel Trails
apple_id: DTS10002212
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-10-25'
source_url: https://developer.apple.com/library/archive/qa/tb/tb26.html
archived_at: '2026-07-18T02:38:56.566554Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB26Avoiding DragDrawingProc Pixel Trails |

|  |
| --- |
| Q I've just implemented a DragDrawingProc. To start, I've tried simply to duplicate the default behavior of the Drag Manager (so it will look as if I had not in fact attached a DragDrawingProc). Unfortunately, when the user drags into a valid drop area and the potential drop receiver calls ShowDragHilite, my DragDrawingProc seems to be responsible for leaving a trail of pixels on the screen. What am I doing wrong? A This happens because Drag Manager does not always pass the entire "old" or "new" region to the DragDrawingProc. Here's a function which mimics what Drag Manager does when you don't attach a DragDrawingProc to a DragReference before calling TrackDrag:  ``` static pascal OSErr LikeDefaultDragDrawingProc         (   DragRegionMessage message,             RgnHandle showRegion, Point showOrigin,             RgnHandle hideRegion, Point hideOrigin,             void *dragDrawingRefCon, DragReference theDragRef   )     {         OSErr err = noErr;          RgnHandle   xorMe;         long        oldA5;         Pattern     gray;          switch (message)         {             case dragRegionBegin:                  oldA5 = SetA5 ((long) dragDrawingRefCon);                 gray = qd.gray;                 SetA5 (oldA5);                  PenPat (&gray);                 PenMode (notPatXor);                  break;              case dragRegionDraw:                  xorMe = NewRgn ( );                 if (!(err = MemError ( )))                 {                     XorRgn (showRegion, hideRegion, xorMe);                     PaintRgn (xorMe);                     DisposeRgn (xorMe);                 }                 break;              case dragRegionHide:                  PaintRgn (hideRegion);                 break;         }          return err;     } ```   The call to XorRgn is the key. It's also very important to pass the correct value for the 'dragDrawingRefCon' to SetDragDrawingProc:   ```     SetDragDrawingProc (dragRef,LikeDefaultDragDrawingProc,         (void*)SetCurrentA5 ( )); ```   (The above works for 68K code; UniversalProcPtr creation omitted for simplicity.)  By the way, be careful not to mix the use of SetDragDrawingProc and SetDragImage. See [Technote 1043:On Drag Manager Additions](https://developer.apple.com/library/archive/technotes/tn/tn1043.html) for details. [Oct 25 1996] |

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
