---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/UtilCode_WindowUtil_c.html
archived_at: '2026-07-18T03:28:34.976427Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](Document%20Revision%20History.md)[Previous](UtilCode-IsPressed.c.md)

# UtilCode/WindowUtil.c

```swift

void DrawClippedGrowIcon(WindowPtr theWindow)
/*
    Clip out the lines that appear
    on the sides of a window with a grow icon.
*/
{
    Rect        clip;
    RgnHandle   oldClip;

    oldClip = NewRgn();
    if(!oldClip) {
        /* WE ARE IN HELL */
        DebugStr("\pHELL HAS BROKE LOOSE __ NEWRGN FDAILED");
    }
    GetClip(oldClip);
    clip = theWindow->portRect;
    clip.left = clip.right - 15;
    clip.top = clip.bottom - 15;

    ClipRect(&clip);

    DrawGrowIcon(theWindow);
    SetClip(oldClip);
}
```

[Next](Document%20Revision%20History.md)[Previous](UtilCode-IsPressed.c.md)

