---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/DisplayMode5.html
archived_at: '2026-07-15T07:38:03.580523Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Configuring%20Displays%20Using%20a%20Transaction.md)[Previous](Changing%20Display%20Modes%20%28OS%20X%20v10.6%20or%20later%29.md)

# Changing Display Modes (OS X v10.5)

A typical display configuration task is to change the mode of a single display. You can use the convenience function [CGDisplaySwitchToMode](https://developer.apple.com/documentation/coregraphics/1562065-cgdisplayswitchtomode) to do this in a single step. This section shows two ways to find and switch to the best mode for a given display.

In the simple case, you want to set the mode of the main display to a mode that most closely matches your required bit depth and resolution. When you are finished drawing, you restore the previous display mode. Finding the Best Mode from the Available Modes shows how to do this. A detailed explanation for each numbered line of code appears following the listing.

__Listing 1__  Setting the mode of the main display

```
size_t desiredBitDepth = 16;
size_t desiredWidth = 1024;
size_t desiredHeight = 768;
boolean_t exactMatch;

CFDictionaryRef mode = CGDisplayBestModeForParameters( // 1
    kCGDirectMainDisplay,
    desiredBitDepth, desiredWidth,
    desiredHeight, &exactMatch);

if (mode != NULL) {
    /* if it is important to have an exact match, check exactMatch here */
    MyDrawToDisplayWithMode (kCGDirectMainDisplay, mode);
}

void MyDrawToDisplayWithMode (CGDirectDisplayID display, CFDictionaryRef mode)
{
    CFDictionaryRef originalMode = CGDisplayCurrentMode (display); // 2
    CGDisplayHideCursor (display);
    CGDisplaySwitchToMode (display, mode); // 3
    CGDisplayCapture (display); // 4

    /* full screen drawing/game loop here */

    CGDisplaySwitchToMode (display, originalMode); // 5
    CGDisplayRelease (display); // 6
    CGDisplayShowCursor (display);
}
```

Here’s what the code does:

1. Finds the best match among the available modes for the specified display.
2. Saves the current display mode.
3. Reconfigures the display to use the new display mode.
4. Captures the display to prepare for full-screen drawing.
5. Restores the previous display mode.
6. Releases the captured display.

In a more complex case, you need more control over which display you use or want to determine for yourself what "best mode" means. Listing 1 shows how to get an array of active displays, iterate over that list examining the modes that each display supports, and choose the most appropriate display and mode combination for your application.

__Listing 2__  Examining the available modes

```
#define MAX_DISPLAYS 32

CGDirectDisplayID displays[MAX_DISPLAYS];
CGDisplayCount numDisplays;
CGDisplayCount i;

CGGetActiveDisplayList (MAX_DISPLAYS, displays, &numDisplays); // 1

for (i = 0; i < numDisplays; i++) // 2
{
    CFDictionaryRef mode;
    CFIndex index, count;
    CFArrayRef modeList;

    modeList = CGDisplayAvailableModes (displays[i]); // 3
    count = CFArrayGetCount (modeList);

    for (index = 0; index < count; index++) // 4
    {
        mode = CFArrayGetValueAtIndex (modeList, index);
        if (MyBestMode (mode)) {
            MyDrawToDisplayWithMode (displays[i], mode); // 5
        }
    }
}

bool MyBestMode (CFDictionaryRef mode) // 6
{
    CFNumberRef value;
    long bitsPerPixel = 0, width = 0;

    value = CFDictionaryGetValue (mode, kCGDisplayBitsPerPixel);
    CFNumberGetValue (value, kCFNumberLongType, &bitsPerPixel);
    value = CFDictionaryGetValue (mode, kCGDisplayWidth);
    CFNumberGetValue (value, kCFNumberLongType, &width);

    if (bitsPerPixel == 32 && width == 1024)
        return true;
    else
        return false;
}
```

Here’s what the code does:

1. Gets the array of active displays, which are the ones available for drawing.
2. Iterates over the array of active displays. Note that the array is zero based.
3. Gets the array of available modes for this display.
4. Iterates over the available modes for a display, calling a custom function to determine if a mode has the desired properties.
5. Calls the drawing function used in the previous example.
6. Checks two properties in the mode dictionary and returns `true` if the mode has the desired properties.

[Next](Configuring%20Displays%20Using%20a%20Transaction.md)[Previous](Changing%20Display%20Modes%20%28OS%20X%20v10.6%20or%20later%29.md)

