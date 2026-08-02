---
title: Sheet Programming Topics
apple_id: 10000002i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Tasks/PositioningSheets.html
archived_at: '2026-07-15T07:19:04.976431Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sheet Programming Topics](Introduction%20to%20Sheets.md)


[Next](Using%20Application-Modal%20Dialogs.md)[Previous](Sheet%20Notifications.md)

# Positioning Sheets

A sheet does not have to be welded to its default location just below the title bar. You can position where a sheet appears attached to a window by implementing the delegate method `window:willPositionSheet:usingRect:`, which an NSWindow object invokes just before it animates the sheet.

The method does more than position the sheet on its window. It can also determine whether the sheet animation originates from a particular object or area of the window. With `window:willPositionSheet:usingRect:` you can, for example, have an alert sheet appear to emerge from the text field associated with the condition described in the alert; you could also position the sheet so that it is centered just under the text field. You might also implement this method to have the sheet placed just below a window’s tool bar rather than its title bar.

Even though the method uses NSRect structures to specify the location of the sheet—one passed in as the default location and another the new (returned) location—the NSRect does not define the rectangle occupied by the sheet. (All sheets are of a standard size in relation to their window.) Instead the NSRect structure, particularly the structure’s `origin` member (an NSPoint structure), specify where the top-left corner of the sheet is attached to the window (in window coordinates). The `size.width` member of the NSRect specifies the width of the initial animation (`size.height` is currently undefined).

The basic implementation of `window:willPositionSheet:usingRect:` is straightforward. It passes in an NSRect structure specifying the default location of the sheet. You return an NSRect structure specifying the new sheet location and the width of initial animation.

Listing 1 shows how a window delegate might implement `window:willPositionSheet:usingRect:` to have the sheet animate from a text field (`fooField`) and then become attached to the window right below the text field.

__Listing 1__  Positioning a sheet right under a text field

```objc
- (NSRect)window:(NSWindow *)window willPositionSheet:(NSWindow *)sheet
        usingRect:(NSRect)rect {
    NSRect fieldRect = [fooField frame];
    fieldRect.size.height = 0;
    return fieldRect;
}
```

Note that, as in the example, it is recommended that you set the `size.height` member of the returned NSRect to zero.

If the window delegate is managing multiple windows and multiple sheets, it should test the first and second arguments of the method to determine which window and sheet is involved and thus which sheet location is appropriate.

[Next](Using%20Application-Modal%20Dialogs.md)[Previous](Sheet%20Notifications.md)

