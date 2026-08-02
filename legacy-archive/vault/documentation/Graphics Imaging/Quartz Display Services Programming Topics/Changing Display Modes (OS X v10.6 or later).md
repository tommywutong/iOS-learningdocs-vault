---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/DisplayModes.html
archived_at: '2026-07-15T07:38:03.596396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Changing%20Display%20Modes%20%28OS%20X%20v10.5%29.md)[Previous](Capturing%20Displays.md)

# Changing Display Modes (OS X v10.6 or later)

A typical display configuration task is to change the mode of a single display. You can use the convenience function [CGDisplaySetDisplayMode](https://developer.apple.com/documentation/coregraphics/1454760-cgdisplaysetdisplaymode) to do this in a single step. This section shows one way to find and switch to the best mode for a given display.

Listing 1 shows how to get an array of active displays, iterate over that list examining the modes that each display supports, and choose the most appropriate display and mode combination for your application.

__Listing 1__  Examining the available modes

```
#define MAX_DISPLAYS 32

CGDirectDisplayID displays[MAX_DISPLAYS];
uint32_t numDisplays;
uint32_t i;

CGGetActiveDisplayList (MAX_DISPLAYS, displays, &numDisplays); // 1

for (i = 0; i < numDisplays; i++) // 2
{
    CGDisplayModeRef mode;
    CFIndex index, count;
    CFArrayRef modeList;

    modeList = CGDisplayCopyAllDisplayModes (displays[i], NULL); // 3
    count = CFArrayGetCount (modeList);

    for (index = 0; index < count; index++) // 4
    {
        mode = (CGDisplayModeRef)CFArrayGetValueAtIndex (modeList, index);
        if (MyBestMode (mode)) {
            MyDrawToDisplayWithMode (displays[i], mode); // 5
            break;
        }
    }
    CFRelease(modeList);// 6
}

bool MyBestMode (CFDisplayModeRef mode) // 7
{
    long height = 0, width = 0;
    CFStringRef pixelEncoding;

    height=CGDisplayModeGetHeight(mode);
    width=CGDisplayModeGetWidth(mode);
    pixelEncoding=CGDisplayModeCopyPixelEncoding(mode);

    if (height == 640 && width == 1024 && CFStringCompare(pixelEncoding,CFSTR(IO32BitDirectPixels),0)==kCFCompareEqualTo)
    {
        CFRelease(pixelEncoding);
        return true;
    }
    else
    {
        CFRelease(pixelEncoding);
        return false;
    }
}

void MyDrawToDisplayWithMode (CGDirectDisplayID display, CGDisplayModeRef mode)
{
    CGDisplayModeRef originalMode = CGDisplayCopyDisplayMode (display); // 8
    CGDisplayHideCursor (display);
    CGDisplaySetDisplayMode (display, mode, NULL); // 9
    CGDisplayCapture (display); // 10

    /* full screen drawing/game loop here */

    CGDisplaySetDisplayMode (display, originalMode, NULL); // 11
    CGDisplayModeRelease(originalMode);
    CGDisplayRelease (display); // 12
    CGDisplayShowCursor (display);
}
```

Here’s what the code does:

1. Gets the array of active displays, which are the ones available for drawing.
2. Iterates over the array of active displays. Note that the array is zero based.
3. Gets the array of available modes for this display.
4. Iterates over the available modes for a display, calling a custom function to determine if a mode has the desired properties.
5. Calls the drawing function.
6. Releases the `CFArray` of display modes returned by `CGDisplayCopyAllDisplayModes`.
7. Checks two properties in the mode dictionary and returns `true` if the mode has the desired properties.
8. Saves the current display mode.
9. Reconfigures the display to use the new display mode.
10. Captures the display to prepare for full-screen drawing.
11. Restores the previous display mode.
12. Releases the captured display.

[Next](Changing%20Display%20Modes%20%28OS%20X%20v10.5%29.md)[Previous](Capturing%20Displays.md)

