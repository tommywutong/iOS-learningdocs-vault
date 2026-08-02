---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/MouseCursor.html
archived_at: '2026-07-15T07:38:03.637912Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Display Services Programming Topics](Introduction%20to%20Quartz%20Display%20Services%20Programming%20Topics.md)


[Next](Document%20Revision%20History.md)[Previous](Notification%20of%20Configuration%20Changes.md)

# Controlling the Mouse Cursor

Quartz Display Services includes functions to control the mouse cursor. For example, when your application is in full-screen mode, you may want to hide the mouse cursor, move the cursor to a different location, or disassociate mouse movement from the cursor position. This article briefly describes the functions that provide these services. To use these functions, your application must be in the foreground.

To hide or show the mouse cursor on any display, use the functions [CGDisplayHideCursor](https://developer.apple.com/documentation/coregraphics/1456534-cgdisplayhidecursor) and [CGDisplayShowCursor](https://developer.apple.com/documentation/coregraphics/1455867-cgdisplayshowcursor). These functions take a display ID as a parameter, but the display ID is not used. Calls to these functions need to be balanced; Quartz maintains a hide cursor count that must be zero in order to show the cursor.

Quartz provides a convenient function for disassociating mouse movement from cursor position while an application is in the foreground. By passing `false` to the function [CGAssociateMouseAndMouseCursorPosition](https://developer.apple.com/documentation/coregraphics/1454486-cgassociatemouseandmousecursorpo), you can prevent mouse movement from changing the cursor position. Pass `true` to reverse the effect.

You can change the location of the mouse cursor on a specific display by calling the function [CGDisplayMoveCursorToPoint](https://developer.apple.com/documentation/coregraphics/1455258-cgdisplaymovecursortopoint). This function takes two parameters, a display ID and a point. The location of the point is relative to the origin or upper-left corner of the display. You can also change the location of the mouse cursor to any display by calling the function [CGWarpMouseCursorPosition](https://developer.apple.com/documentation/coregraphics/1456387-cgwarpmousecursorposition). This function takes a single parameter, a point in global display coordinates. Calling either of these functions does not generate a mouse event.

Listing 1 shows how you would hide the cursor, disassociate mouse movement from the cursor, move it to the origin of the main display, and then restore the cursor and mouse when you are done.

__Listing 1__  Controlling the mouse cursor

```
CGDisplayHideCursor (kCGNullDirectDisplay);
CGAssociateMouseAndMouseCursorPosition (false);
CGDisplayMoveCursorToPoint (kCGDirectMainDisplay, CGPointZero);
/* perform your application’s main loop */
CGAssociateMouseAndMouseCursorPosition (true);
CGDisplayShowCursor (kCGNullDirectDisplay);
```

[Next](Document%20Revision%20History.md)[Previous](Notification%20of%20Configuration%20Changes.md)

