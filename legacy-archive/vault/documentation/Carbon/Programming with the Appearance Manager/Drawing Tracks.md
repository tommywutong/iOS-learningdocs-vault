---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.1c.html
archived_at: '2026-07-15T05:23:56.574613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.1b.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1d.md)

---

#    Drawing Tracks

The Appearance Manager provides a variety of functions that you can use to make your program's tracks--that is, its scroll bars, sliders, and progress bars--theme-compliant. You can use the Appearance Manager to handle most aspects of drawing, obtaining values for, and checking for mouse-down events on tracks and their related parts (such as the indicator on a scroll bar or slider, a scroll bar's arrows, or the tick marks on a slider).

Your application can use the function
DrawThemeTrack
to draw a theme-compliant slider, progress bar, or scroll bar. If you use
DrawThemeTrack
to draw a scroll bar, use the function
DrawThemeScrollBarArrows
to draw the scroll bar's arrows; see [Listing 3-7](#apple-ge2dknjs)
for an example of using these two functions together to draw a complete scroll bar. If you use
DrawThemeTrack
to draw a slider, use
DrawThemeTrackTickMarks
if you need to draw tick marks for the slider.

__Listing 3-7__  

Drawing a scroll bar with arrows

`

Rect bounds;
ThemeTrackDrawInfo drawInfo;
OSStatus err;

SetRect (&bounds, 10, 10, 200, 26);

/* Draw the arrows and pass the actual track rect into the
drawInfo structure for DrawThemeTrack to use */
err = DrawThemeScrollBarArrows (&bounds, kThemeTrackActive, 0, true, &drawInfo.bounds);

if (err == noErr)
{
    drawInfo.kind = kThemeScrollBar;
    /* drawInfo.bounds is set to the modified bounds, with the arrows removed,
    on exit from DrawThemeScrollBarArrows */
    drawInfo.min = 0;
    drawInfo.max = 100;
    drawInfo.value = 65;
    drawInfo.attributes = kThemeTrackHorizontal | kThemeTrackShowThumb;
    drawInfo.enableState = kThemeTrackActive;
    drawInfo.trackInfo.scrollbar.viewsize = 0;
    drawInfo.trackInfo.scrollbar.pressState = 0;

    err = DrawThemeTrack (&drawInfo, NULL, NULL, 0);
}`

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.17.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.1b.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.1d.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
