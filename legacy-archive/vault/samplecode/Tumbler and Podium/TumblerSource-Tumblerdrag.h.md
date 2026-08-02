---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_drag_h.html
archived_at: '2026-07-18T03:27:21.851284Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-TumblerErrorHandler.c.md)[Previous](TumblerSource-Tumblerdrag.c.md)

# TumblerSource/Tumbler_drag.h

```
// Tumbler_drag.h
//
// Dragging related data structures and function prototypes for the 
// Tumbler application
//
// Modification History
//
//  11/26/94        nick        initial cut - symantec proto_helper app, add defines


#ifndef _Tumbler_DRAG_H_
#define _Tumbler_DRAG_H_


// prototypes from Tumbler_drag.c
pascal OSErr MyDrawingProc(DragRegionMessage message, RgnHandle showRgn, Point showOrigin, RgnHandle hideRgn, Point hideOrigin, void *dragDrawingRefCon, DragReference theDragRef);
Boolean DragItemsAreAcceptable(DragReference theDrag);
Boolean DragIsNotInSourceWindow(DragReference theDrag);
Boolean MouseIsInContentRgn(DragReference theDrag, WindowPtr theWindow);
pascal OSErr MyReceiveDropHandler(WindowPtr theWindow, unsigned long handlerRefCon, DragReference theDrag);
pascal OSErr MyTrackingHandler(short theMessage, WindowPtr theWindow, void *handlerRefCon, DragReference theDrag);
short DoDragObjects(DocumentPtr theDocument, EventRecord *theEvent, RgnHandle hiliteRgn) ;


#endif
```

[Next](TumblerSource-TumblerErrorHandler.c.md)[Previous](TumblerSource-Tumblerdrag.c.md)

