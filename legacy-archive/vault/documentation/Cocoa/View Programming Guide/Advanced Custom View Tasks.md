---
title: View Programming Guide
apple_id: TP40002978
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/AdvancedSubclassing/AdvancedSubclassing.html
archived_at: '2026-07-15T07:13:20.184158Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [View Programming Guide](Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](Optimizing%20View%20Drawing.md)[Previous](Creating%20a%20Custom%20View.md)

# Advanced Custom View Tasks

The chapter [Creating a Custom View](Creating%20a%20Custom%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnznknlti) describes the common implementation details for a custom view subclass. This chapter describes advanced view subclassing issues that, although not uncommon, are not required by many view subclasses.

Most of a view's displayed image is a stable representation of its state. View objects also interact dynamically with the user, however, and this interaction often involves temporary drawing that isn’t integral to the image itself—selections and other highlighting, for example. Such content should be displayed only to the screen and never to a printer or fax device, or to the pasteboard.

You can determine if a view is drawing to the screen by sending the current graphics context an `isDrawingToScreen` message as shown in Listing 5-1.

__Listing 5-1__  Testing the output device

```objc
- (void)drawRect:(NSRect)rect
{
    [[NSColor whiteColor] set];
    NSRectFill(rect);

    // draw a background grid only if we’re drawing to the screen
    if ([[NSGraphicsContext currentContext] isDrawingToScreen]) {
        [self drawGrid];
    }

    // insert view drawing code here
}
```


If you define methods that need to draw in a view without going through the `drawRect:` method, you must send `lockFocus` to the target view before any drawing is started and send `unlockFocus` as soon as you are done.

It’s perfectly reasonable to lock the focus on one view when another already has it. In fact, this is exactly what happens when subviews are drawn in their superview. The focusing machinery keeps a stack containing the views that have been focused, so that when one view is sent an `unlockFocus` message, the focus is restored to the view that was focused immediately before.

Listing 5-2 illustrates using the `lockFocus` and `unlockFocus` methods to determine the color of the pixel at the cursor location. It would be called from a view's `mouseDown:`, `mouseUp:`, and `mouseMoved:` methods in response to a mouse-down event in a view.

__Listing 5-2__  Using `lockFocus` and `unlockFocus` explicitly

```objc
- (void) examinePixelColor:(NSEvent *) theEvent
{
    NSPoint where;
    NSColor *pixelColor;
    float  red, green, blue;

    where = [self convertPoint:[theEvent locationInWindow] fromView:nil];

    // NSReadPixel pulls data out of the current focused graphics context, so -lockFocus is necessary here.
    [self lockFocus];

    pixelColor = NSReadPixel(where);

    // always balance -lockFocus with an -unlockFocus.
    [self unlockFocus];

    red = [pixelColor redComponent];
    green = [pixelColor greenComponent];
    blue = [pixelColor blueComponent];

    // we have the color, code that does something with it
    // would reside here

  }
```

[Next](Optimizing%20View%20Drawing.md)[Previous](Creating%20a%20Custom%20View.md)

