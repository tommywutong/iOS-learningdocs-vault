---
title: Scroll View Programming Guide for Mac
apple_id: TP40003221
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-06-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSScrollViewGuide/Articles/Scrolling.html
archived_at: '2026-07-15T07:16:53.406199Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Scroll View Programming Guide for Mac](Introduction%20to%20Scroll%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](Synchronizing%20Scroll%20Views.md)[Previous](Creating%20and%20Configuring%20a%20Scroll%20View.md)

# Scrolling the Document View

A scroll view's document view scrolls in response to one of the following actions:

- The user clicks in one of the scrollers or rotates the mouse scroll wheel or scroll ball. These cases are handled automatically by the `NSScrollView` class.
- The scroll view must scroll to a specific location—for example, to display the current selection in response to a user action. The application is responsible for implementing this functionality as described in [Scrolling To a Specific Location](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinrtfvjvomq).
- The user drags the mouse outside the scroll view, causing autoscrolling to occur. The document view is responsible for supporting autoscrolling in response to mouse-drag events as described in [Supporting Automatic Scrolling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinrtfvjvomy).

Applications often need to scroll to a specific location in a document view because of some user action unrelated to scrolling. For example, when a user searches a document they expect the document to scroll to show the found item. The `NSView` class provides high-level scrolling methods that automatically update the scrollers and redisplay the document view as required. The `NSClipView` and `NSScrollView` classes methods provide low-level scrolling support that requires the application to update the scrollers and mark the document view for display.

Two `NSView` methods support scrolling to reveal a specific location: `scrollPoint:` and `scrollRectToVisible:`. These high-level methods scroll the specified point or rectangle to the origin of the content view. You send these methods to the scroll view's document view or to one of its descendants. Scroll messages are passed up through the view hierarchy to the nearest enclosing `NSClipView` instance. `NSView` also provides a convenience method, `enclosingScrollView`, that returns the `NSScrollView` instance that contains the receiver, allowing the view to interact directly with a parent scroll view. If the receiver is not contained in a scroll view, `enclosingScrollView` returns `nil`.

The code fragment in Listing 1 illustrates how to scroll to the top and bottom of the document view. The orientation of the document view determines where the origin of the content view lies and you must allow for this when calculating the top and bottom locations.

__Listing 1__  Scrolling to the bottom or top of the document view

```objc
- (void)scrollToTop:sender;
{
    NSPoint newScrollOrigin;

    // assume that the scrollview is an existing variable
    if ([[scrollview documentView] isFlipped]) {
        newScrollOrigin=NSMakePoint(0.0,0.0);
    } else {
        newScrollOrigin=NSMakePoint(0.0,NSMaxY([[scrollview documentView] frame])
                                        -NSHeight([[scrollview contentView] bounds]));
    }

    [[scrollview documentView] scrollPoint:newScrollOrigin];

}

- (void)scrollToBottom:sender;
{
    NSPoint newScrollOrigin;

    // assume that the scrollview is an existing variable
    if ([[scrollview documentView] isFlipped]) {
        newScrollOrigin=NSMakePoint(0.0,NSMaxY([[scrollview documentView] frame])
                                       -NSHeight([[scrollview contentView] bounds]));
    } else {
        newScrollOrigin=NSMakePoint(0.0,0.0);
    }

    [[scrollview documentView] scrollPoint:newScrollOrigin];

}
```

The low-level scrolling methods bypass the `adjustScroll:` mechanism described in Constraining Scrolling.

Scroll views scroll automatically as the user drags the mouse outside of the scroll view's content area if the document view, or a descendent, calls the `NSView` method `autoscroll:` as it handles the mouse-drag event. Supporting autoscrolling allows the user to drag the mouse, moving or selecting items, and have the scroll view continually display the active portion of the document.

View subclasses should send `autoscroll:` messages as part of their mouse-drag handling code, passing the current `NSEvent` object as the parameter. The `autoscroll:` method does nothing if the receiver is not contained within a scroll view. Listing 2 shows a typical `NSView` subclass's implementation of a `mouseDragged:` method that supports automatic scrolling.

__Listing 2__  Supporting automatic scrolling in a `mouseDragged:` implementation

```objc
-(void)mouseDragged:(NSEvent *)event
{
    NSPoint dragLocation;
    dragLocation=[self convertPoint:[event locationInWindow]
                           fromView:nil];

    // support automatic scrolling during a drag
    // by calling NSView's autoscroll: method
    [self autoscroll:event];

    // act on the drag as appropriate to the application
}
```


You can determine the current visible location in a scroll view by examining the bounds of its clip view. The origin of the clip view's bounds is suitable for using with `scrollPoint:` to restore the scroll location later. The code fragment in Listing 3 demonstrates getting a scroll view's current scroll location and restoring it.

__Listing 3__  Getting and setting the current scroll location of a view

```
// get the current scroll position of the document view
NSPoint currentScrollPosition=[[theScrollView contentView] bounds].origin;

// restore the scroll location
[[theScrollView documentView] scrollPoint:currentScrollPosition];
```


Subclasses of `NSView` override the `adjustScroll:` method to provide a view fine-grained control of its position during scrolling. A custom view subclass can quantize scrolling into regular units—to the edges of a spreadsheet’s cells, for example—or simply limit scrolling to a specific region of the view. The `adjustScroll:` method provides the proposed rectangle that the scrolling mechanism will make visible and expects the subclass to return the passed rectangle or an altered rectangle that will constrain the scrolling.

Listing 4 shows an implementation of `adjustScroll:` that constrains scrolling of the view to 72 pixel increments, even when dragging the scroll knob.

__Listing 4__  Constraining scrolling with `adjustScroll:`

```objc
- (NSRect)adjustScroll:(NSRect)proposedVisibleRect
{
    NSRect modifiedRect=proposedVisibleRect;

    // snap to 72 pixel increments
    modifiedRect.origin.x = (int)(modifiedRect.origin.x/72.0) * 72.0;
    modifiedRect.origin.y = (int)(modifiedRect.origin.y/72.0) * 72.0;

    // return the modified rectangle
    return modifiedRect;
}
```

The `adjustScroll:` method is not used when scrolling is initiated by lower-level scrolling methods provided by `NSClipView` (`scrollToPoint:`) and `NSScrollView` (`scrollRectToVisible:`).

[Next](Synchronizing%20Scroll%20Views.md)[Previous](Creating%20and%20Configuring%20a%20Scroll%20View.md)

