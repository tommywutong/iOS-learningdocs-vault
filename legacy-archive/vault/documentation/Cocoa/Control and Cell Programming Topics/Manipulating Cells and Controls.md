---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Articles/ManipulateCellControl.html
archived_at: '2026-07-15T07:13:43.860860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Validating%20Control%20Entries.md)[Previous](Cell%20States.md)

# Manipulating Cells and Controls

This article contains miscellaneous tips and examples for manipulating cells and controls.

To set the size of a cell (and any enclosing single-cell control) to an optimum size conforming with the human interface guidelines, do the following:

1. If the cell contains text, set the font of the text to be consistent with one of the three standard sizes: regular, small, and mini. To do this use the NSFont class method [systemFontSizeForControlSize:](https://developer.apple.com/documentation/appkit/nsfont/1529747-systemfontsize). The argument to this method is an [NSControlSize](https://developer.apple.com/documentation/appkit/nscontrolsize) constant declared by the NSControl class.

```
float fontSize = [NSFont systemFontSizeForControlSize:NSMiniControlSize];
NSCell *theCell = [theControl cell];
NSFont *theFont = [NSFont fontWithName:[[theCell font] fontName] size:fontSize];
[theCell setFont:theFont];
```
2. Set the control size to the same size as given for the font size, using the same constant. Use the NSControl [setControlSize:](https://developer.apple.com/documentation/appkit/nscell/1530780-controlsize) method.

```
[theCell setControlSize:NSMiniControlSize];
```
3. Finally, send [sizeToFit](https://developer.apple.com/documentation/appkit/nscontrol/1428877-sizetofit) to the control to trim the extra width.

```
[theControl sizeToFit];
```


The [NSSetFocusRingStyle](https://developer.apple.com/documentation/appkit/nsfocusringplacement/1473702-set) sets the style that a focus ring will be drawn in the next time you fill a bezier path. It takes a constant of type of [NSFocusRingPlacement](https://developer.apple.com/documentation/appkit/nsfocusringplacement) to tell the Application Kit to draw the focus ring over an image, under text, or (when neither text or image is a consideration) around a shape. You can use this function with a constant of `NSFocusRingOnly` to draw a focus ring just inside a cell's bounds.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzyfvjvomi) shows how you draw such a focus ring. It requires you to override the NSCell [drawWithFrame:inView:](https://developer.apple.com/documentation/appkit/nscell/1535830-drawwithframe). In this method, if the cell is supposed to draw evidence of first-responder status, set the rectangle for the focus ring, call [NSSetFocusRingStyle](https://developer.apple.com/documentation/appkit/nsfocusringplacement/1473702-set) with an argument of `NSFocusRingOnly`, and then create and fill a bezier path defining that rectangle. Filling in this case simply draws the ring.

__Listing 1__  Drawing a focus ring just inside a cell's bounds

```objc
- (void)drawWithFrame:(NSRect)cellFrame inView:(NSView *)controlView {
    // other stuff might happen here
    if ([self showsFirstResponder]) {
         // showsFirstResponder is set for us by the NSControl that is drawing  us.
        NSRect focusRingFrame = cellFrame;
        focusRingFrame.size.height -= 2.0;
        [NSGraphicsContext saveGraphicsState];
        NSSetFocusRingStyle(NSFocusRingOnly);
        [[NSBezierPath bezierPathWithRect: NSInsetRect(focusRingFrame,4,4)] fill];
        [NSGraphicsContext restoreGraphicsState];
    }
     // other stuff might happen here
}
```


If a cell is to display an image instead of (or in addition to) text, you can affect the placement of the image within the cell by overriding the [imageRectForBounds:](https://developer.apple.com/documentation/appkit/nscell/1533408-imagerectforbounds) method, which is declared by both the NSCell and NSMenuItemCell classes. This method returns the rectangle the cell's image is drawn in, which is usually a rectangle slightly offset from the cell's bounds. [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzyfvjvomy) gives an example.

__Listing 2__  Centering an image in its cell

| ``` - (NSRect) imageRectForBounds:(NSRect)theBounds { ``` |
```
    NSRect r = theBounds;
    // get size. If no image, result of method returning NSSize is undefined so assume NSZeroSize
    NSSize imageSize = [self image] != nil ? [[self image] size] : NSZeroSize;
    r.origin.x = floor((r.size.width/2)  - (imageSize.width/2)  + 0.5);
    r.origin.y = floor((r.size.height/2) - (imageSize.height/2) + 0.5);
    r.size     = imageSize;
    return r;
}
```

In this example, the cell centers the image in the cell. Note that it rounds the return values to the nearest pixel to avoid blurring that drawing with partial pixel offsets may cause. The code also sets the size field of the returned rectangle to the size of the image so that it is correctly drawn in the rectangle (assuming the NSImage object uses [drawInRect:fromRect:operation:fraction:](https://developer.apple.com/documentation/appkit/nsimage/1520067-drawinrect) for drawing and not [compositeToPoint:operation:](https://developer.apple.com/documentation/appkit/nsimage/1519867-compositetopoint)).

[Next](Validating%20Control%20Entries.md)[Previous](Cell%20States.md)

