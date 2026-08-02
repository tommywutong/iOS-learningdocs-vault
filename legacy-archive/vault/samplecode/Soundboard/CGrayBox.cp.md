---
title: Soundboard
apple_id: DTS10000059
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Soundboard/Listings/CGrayBox_cp.html
archived_at: '2026-07-18T03:25:12.504915Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Soundboard](Soundboard.md)


[Next](CGrayBox.h.md)[Previous](CFilterControl.h.md)

# CGrayBox.cp

```c
// ===========================================================================
//  CGrayBox.cp                 ©1995 Apple Computer, Inc. All rights reserved.
// ===========================================================================

#include "CGrayBox.h"

#include <UDrawingUtils.h>
#include <UDrawingState.h>


// ---------------------------------------------------------------------------
//      ¥ CreateGrayBoxStream
// ---------------------------------------------------------------------------
//  Create a GrayBox object from the data in a Stream

CGrayBox*
CGrayBox::CreateGrayBoxStream(
    LStream *inStream)
{
    return (new CGrayBox(inStream));
}


// ---------------------------------------------------------------------------
//      ¥ CGrayBox(LStream *)
// ---------------------------------------------------------------------------
//  Constructor
//
//  This class has no new member variables and needs no preparation, so
//  it just calls the constructor for LPane

CGrayBox::CGrayBox(
    LStream *inStream)
        : LView(inStream)
{
    mDrawGrayBkgrnd = false;
}

void
CGrayBox::ApplyForeAndBackColors()
{
    LView::ApplyForeAndBackColors();
    if (mDrawGrayBkgrnd)
        ::RGBBackColor(&mLtGray);
}


// ---------------------------------------------------------------------------
//      ¥ DrawSelf
// ---------------------------------------------------------------------------
//  Draws a filled rectangle. On screens with < 16 colors, the fill is
//  a gray pattern. On screens with >= 16 colors, the fill is a solid
//  gray color.

void
CGrayBox::DrawSelf()
{
    Rect    frame;                  // Get bounds of Pane in local coords
    CalcLocalFrameRect(frame);

    ApplyForeAndBackColors();
    ::EraseRect(&frame);
}

// ---------------------------------------------------------------------------
//      ¥ Draw
// ---------------------------------------------------------------------------
//  Draw a View and all its SubPanes
//
//  inSuperDrawRgnH specifies, in Port coordinates, the portion of the
//  View's SuperView that needs to be drawn. Specify nil to draw the
//  entire View.
//
//  This routine is overridden so that mDrawGrayBkgrnd can be set to draw a
//  gray background when we are drawing to a device with at least 16 colors.

void
CGrayBox::Draw(
    RgnHandle   inSuperDrawRgnH)
{
                                        // Don't draw if invisible or unable
                                        //   to put in focus
    if (IsVisible() && FocusDraw()) {

        Rect    frame;                  // Get bounds of Pane in local coords
        CalcLocalFrameRect(frame);

        StDeviceLoop    theLoop(frame); // Set up for looping thru each device
        Int16   depth;

        while (theLoop.NextDepth(depth)) {

                // At this point, the clipping region is set to the portion
                // of the Pane that is on the screen with the current
                // bit depth. Therefore, we can just draw everything, and
                // let the clipping region restrict the drawing.
                //
                // If you are interested in other characteristics of the
                // current screen device, you can call theLoop.GetCurrentDevice
                // which will return a GDHandle.

            mDrawGrayBkgrnd = (depth >= 4);
            LView::Draw(inSuperDrawRgnH);
        }
        mDrawGrayBkgrnd = false;        // reset back to false
    }
}
```

[Next](CGrayBox.h.md)[Previous](CFilterControl.h.md)

