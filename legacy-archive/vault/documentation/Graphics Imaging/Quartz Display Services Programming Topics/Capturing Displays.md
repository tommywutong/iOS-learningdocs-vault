---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/DisplayCapture.html
archived_at: '2026-07-15T07:38:03.554537Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Changing%20Display%20Modes%20%28OS%20X%20v10.6%20or%20later%29.md)[Previous](Getting%20Information%20About%20Displays.md)

# Capturing Displays

If you’re writing an immersive application such as a game or a presentation program, you may want to do full-screen drawing.

A common approach is to capture the display you want to use. When you capture a display, you have exclusive use of the display. Other applications and system services are not allowed to use the display or change its configuration. In addition, they are not notified of display changes, thus preventing them from repositioning their windows and the Finder from repositioning desktop icons.

To capture a single display, call the function [CGDisplayCapture](https://developer.apple.com/documentation/coregraphics/1456259-cgdisplaycapture). To capture all online displays at once, call [CGCaptureAllDisplays](https://developer.apple.com/documentation/coregraphics/1455221-cgcapturealldisplays). By default, a captured screen is filled with black color; you have the option of disabling this feature if you capture using the functions [CGDisplayCaptureWithOptions](https://developer.apple.com/documentation/coregraphics/1454934-cgdisplaycapturewithoptions) or [CGCaptureAllDisplaysWithOptions](https://developer.apple.com/documentation/coregraphics/1456514-cgcapturealldisplayswithoptions).

After capturing a display, there are several drawing options:

- If you’re writing an OpenGL application, you can create an OpenGL full-screen drawing context. For more information, see _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_.
- You can draw directly to the screen using Quartz 2D. Use the function [CGDisplayGetDrawingContext](https://developer.apple.com/documentation/coregraphics/1456576-cgdisplaygetdrawingcontext) to obtain a full-featured graphics context for the display. The graphics context remains valid until the display is released or its configuration changes. The context’s origin is the lower-left corner of the display.
- In OS X v10.5, you can draw directly to the screen using your own drawing engine. Call [CGDisplayBaseAddress](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807908-cgdisplaybaseaddress) or [CGDisplayAddressForPosition](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807904-cgdisplayaddressforposition) to get an address in the frame buffer to which to draw. In OS X v10.6 or later you should use Quartz, OpenGL, or another graphics technology.

When you are finished using a captured display, you should release it by calling [CGDisplayRelease](https://developer.apple.com/documentation/coregraphics/1455685-cgdisplayrelease) or [CGReleaseAllDisplays](https://developer.apple.com/documentation/coregraphics/1454901-cgreleasealldisplays).

Listing 1 shows how to capture the main display and draw a text string using Quartz 2D. A detailed explanation for each numbered line of code appears following the listing.

__Listing 1__  Capturing the main display

```
char *text = "Hello, World!";
CGDirectDisplayID display = kCGDirectMainDisplay; // 1
CGError err = CGDisplayCapture (display); // 2
if (err == kCGErrorSuccess)
{
    CGContextRef ctx = CGDisplayGetDrawingContext (display); // 3
    if (ctx != NULL)
    {
        CGContextSelectFont (ctx, "Times-Roman", 48, kCGEncodingMacRoman);
        CGContextSetTextDrawingMode (ctx, kCGTextFillStroke);
        CGContextSetRGBFillColor (ctx, 1, 1, 1, 0.75);
        CGContextSetRGBStrokeColor (ctx, 1, 1, 1, 0.75);
        CGContextShowTextAtPoint (ctx, 40, 40, text, strlen(text)); // 4
        sleep (4); // 5
    }
    CGDisplayRelease (display); // 6
}
```

Here’s what the code does:

1. Gets the display ID of the main display.
2. Captures the main display and changes the color to black. An error is returned only if the display has been captured by another application.
3. Gets a Quartz graphics context associated with the captured display.
4. Draws the text string in the lower-left corner of the screen.
5. Suspends processing for a few seconds to allow the user to read the text.
6. Releases the captured display.

[Next](Changing%20Display%20Modes%20%28OS%20X%20v10.6%20or%20later%29.md)[Previous](Getting%20Information%20About%20Displays.md)

