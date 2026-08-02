---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MouseTrackingEvents/MouseTrackingEvents.html
archived_at: '2026-07-15T07:15:36.401743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Text%20System%20Defaults%20and%20Key%20Bindings.md)

# Mouse-Tracking and Cursor-Update Events

Mouse-tracking messages are sent to an object when the mouse pointer (without a mouse button being pressed) enters and exits a region of a window. This region is known as a tracking rectangle or tracking area. Mouse tracking enables the view owning the region to respond, for example, by drawing a highlight color or displaying a tool tip. Cursor-update events are a special kind of mouse-tracking event that the Application Kit handles automatically. When the mouse pointer enters a cursor rectangle, the Application Kit displays a cursor image appropriate to the type of view under the rectangle; for example, when a mouse pointer enters a text view, an I-beam cursor is displayed instead.

The sections in this chapter describe how you set up tracking rectangles and respond to mouse-tracking events. They also discuss how to specify and manage the rectangles for cursor-update events.

A region of a view set up for tracking mouse movement is known as a tracking rectangle. When the mouse cursor enters the tracking rectangle, the Application Kit sends mouse-entered events (type [NSMouseEntered](https://developer.apple.com/documentation/appkit/nsmouseentered)) to the object owning the rectangle (which is not necessarily the view itself); when the cursor leaves the rectangle, the Application Kit sends the object mouse-exited events (type [NSMouseExited](https://developer.apple.com/documentation/appkit/nsmouseexited)). These events correspond to the [mouseEntered:](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered) and [mouseExited:](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited) methods, respectively, of [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder). Mouse tracking can be useful for such tasks as displaying context-sensitive messages or highlighting graphic elements under the cursor. An [NSView](https://developer.apple.com/documentation/appkit/nsview) object can have any number of tracking rectangles, which can overlap or be nested one within the other; the [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) objects generated to represent mouse-tracking events include a tag (accessed through the [trackingNumber](https://developer.apple.com/documentation/appkit/nsevent/1533974-trackingnumber) method) that identifies the rectangle associated with an event.

To create a tracking rectangle, send a [addTrackingRect:owner:userData:assumeInside:](https://developer.apple.com/documentation/appkit/nsview/1483668-addtrackingrect) message to the `NSView` object associated with the rectangle, as shown in Managing a Tracking-Area Object. This method registers an owner for the tracking rectangle, so that the owner receives the tracking-event [messages](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59). The owner is typically the view object itself, but need not be. The method returns the tracking rectangle’s tag so that you can store it for later reference in the event-handling methods `mouseEntered:` and `mouseExited:`. To remove a tracking rectangle, use the [removeTrackingRect:](https://developer.apple.com/documentation/appkit/nsview/1483729-removetrackingrect) method, which takes as an argument the tag of the tracking rectangle to remove.

__Listing A-1__  Adding a tracking rectangle to a view region

```objc
- (void)viewDidMoveToWindow {
    // trackingRect is an NSTrackingRectTag instance variable
    // eyeBox is a region of the view (instance variable)
    trackingRect = [self addTrackingRect:eyeBox owner:self userData:NULL assumeInside:NO];
}
```

In the above example, the custom view adds the tracking rectangle in the [viewDidMoveToWindow](https://developer.apple.com/documentation/appkit/nsview/1483329-viewdidmovetowindow) method instead of [initWithFrame:](https://developer.apple.com/documentation/appkit/nsview/1483458-initwithframe). Although `NSView` implements the `addTrackingRect:owner:userData:assumeInside:` method, a view’s window maintains the list of tracking rectangles. When a view’s `initWithFrame:` initializer is invoked, the view is not yet associated with a window, so the tracking rectangle cannot yet be added to the window’s list. Thus the best place to add tracking rectangles initially is in the [viewDidMoveToWindow](https://developer.apple.com/documentation/appkit/nsview/1483329-viewdidmovetowindow) method.

Tracking rectangle bounds are inclusive for the top and left edges, but not for the bottom and right edges. Thus, if you have a unflipped view with a tracking rectangle covering its bounds, and the view’s frame has the geometry `frame.origin = (100, 100), frame.size = (200, 200)`, then the area for which the tracking rectangle is active is `frame.origin = (100, 101), frame.size = (199, 199`), in frame coordinates.

Tracking rectangles can also be used to provide [NSMouseMoved](https://developer.apple.com/documentation/appkit/nsmousemoved) events to views in the [mouseMoved:](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved) method. For a view to receive `NSMouseMoved` events, however, two things must happen:

- The view must be the first responder.
- The view’s window must be sent a [setAcceptsMouseMovedEvents:](https://developer.apple.com/documentation/appkit/nswindow/1419340-acceptsmousemovedevents) message with an argument of `YES`.

As noted in [Event Objects and Types](Event%20Objects%20and%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedilktk42a) and [Handling Mouse Events](Handling%20Mouse%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedmlktk4yq), an `NSWindow` object by default does not receive `NSMouseMoved` events because they can easily flood the event queue. If you only want to receive mouse-moved messages while the mouse is over your view, you should turn them off again when a mouse-tracking session completes.

You typically send the `setAcceptsMouseMovedEvents:` message (with an argument of `YES`) in your implementation of [mouseEntered:](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered). If you want to turn them off after a tracking session ends, you can send the message again with an argument of `NO` in your implementation of [mouseExited:](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited). However, you should also set the window state back to what it was before you turned on mouse-moved events to ensure that the window does not stop receiving mouse-moved events if it wants them for other purposes.

The tracking code in Listing 6-2 is used in making an “eyeball” follow the movement of the mouse pointer when it enters a tracking rectangle. Note that the `mouseEntered:` implementation uses the `wasAcceptingMouseEvents` instance variable to capture the window’s current state as regards mouse-moved events before these events are turned on for the current tracking session; later, in `mouseExited:`, the value of this instance variable is used as the argument to `setAcceptsMouseMovedEvents:`, thereby resetting window state.

__Listing A-2__  Handling mouse-entered, mouse-moved, and mouse-exited events

```objc
- (void)mouseEntered:(NSEvent *)theEvent {
    wasAcceptingMouseEvents = [[self window] acceptsMouseMovedEvents];
    [[self window] setAcceptsMouseMovedEvents:YES];
    [[self window] makeFirstResponder:self];
    NSPoint eyeCenter = [self convertPoint:[theEvent locationInWindow] fromView:nil];
    eyeBox = NSMakeRect((eyeCenter.x-10.0), (eyeCenter.y-10.0), 20.0, 20.0);
    [self setNeedsDisplayInRect:eyeBox];
    [self displayIfNeeded];
}

- (void)mouseMoved:(NSEvent *)theEvent {
    NSPoint eyeCenter = [self convertPoint:[theEvent locationInWindow] fromView:nil];
    eyeBox = NSMakeRect((eyeCenter.x-10.0), (eyeCenter.y-10.0), 20.0, 20.0);
    [self setNeedsDisplayInRect:eyeBox];
    [self displayIfNeeded];
}

- (void)mouseExited:(NSEvent *)theEvent {
    [[self window] setAcceptsMouseMovedEvents:wasAcceptingMouseEvents];
    [self resetEye];
    [self setNeedsDisplayInRect:eyeBox];
    [self displayIfNeeded];
}
```

Because tracking rectangles are maintained by `NSWindow` objects, a tracking rectangle is a static entity; it doesn’t move or change its size when an `NSView` object does. If you use tracking rectangles, you should be sure to remove and reestablish them when you change the frame rectangle of the view object that contains them. If you’re creating a custom subclass of `NSView`, you can [override](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) the [setFrame:](https://developer.apple.com/documentation/appkit/nsview/1483713-frame) and [setBounds:](https://developer.apple.com/documentation/appkit/nsview/1483817-bounds) methods to do this, as shown in Compatibility Issues. If your class is not a custom view class, you can register your class instance as an observer for the [notification](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) [NSViewFrameDidChangeNotification](https://developer.apple.com/documentation/appkit/nsviewframedidchangenotification) and have it reestablish the tracking rectangles on receiving the notification.

__Listing A-3__  Resetting a tracking rectangle

```objc
- (void)setFrame:(NSRect)frame {
    [super setFrame:frame];
    [self removeTrackingRect:trackingRect];
    [self resetEye];
    trackingRect = [self addTrackingRect:eyeBox owner:self userData:NULL assumeInside:NO];
}

- (void)setBounds:(NSRect)bounds {
    [super setBounds:bounds];
    [self removeTrackingRect:trackingRect];
    [self resetEye];
    trackingRect = [self addTrackingRect:eyeBox owner:self userData:NULL assumeInside:NO];
}
```

You should also remove the tracking rectangle when your view is removed from its window, which can happen either because the view is moved to a different window, or because the view is removed as part of deallocation. One place to do this is the [viewWillMoveToWindow:](https://developer.apple.com/documentation/appkit/nsview/1483415-viewwillmove) method, as shown in Compatibility Issues.

__Listing A-4__  Removing a tracking rectangle when a view is removed from its window

```objc
- (void)viewWillMoveToWindow:(NSWindow *)newWindow {
    if ( [self window] && trackingRect ) {
        [self removeTrackingRect:trackingRect];
    }
}
```


One common use of tracking rectangles is to change the cursor image over different types of graphic elements. Text, for example, typically requires an I-beam cursor. Changing the cursor is such a common operation that [NSView](https://developer.apple.com/documentation/appkit/nsview) defines several convenience methods to ease the process. A tracking rectangle generated by these methods is called a cursor rectangle. The Application Kit itself assumes ownership of cursor rectangles, so that when the user moves the mouse over the rectangle the cursor automatically changes to the appropriate image. Unlike general tracking rectangles, cursor rectangles may not partially overlap. They may, however, be completely nested, one within the other.

Because cursor rectangles need to be reset often as a view’s size and graphic elements change, `NSView` defines a single method, [resetCursorRects](https://developer.apple.com/documentation/appkit/nsview/1483448-resetcursorrects), that’s invoked any time its cursor rectangles need to be reestablished. A concrete subclass [overrides](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) this method, invoking [addCursorRect:cursor:](https://developer.apple.com/documentation/appkit/nsview/1483540-addcursorrect) for each cursor rectangle it wishes to set (as illustrated in Listing A-5). Thereafter, the view’s cursor rectangles can be rebuilt by invoking the `NSWindow` method [invalidateCursorRectsForView:](https://developer.apple.com/documentation/appkit/nswindow/1419601-invalidatecursorrects). Before `resetCursorRects` is invoked, the owning view is automatically sent a [disableCursorRects](https://developer.apple.com/documentation/appkit/nswindow/1419639-disablecursorrects) message to remove existing cursor rectangles.

Listing 6-4 shows an implementation of `resetCursorRects`.

__Listing A-5__  Resetting a cursor rectangle

```objc
-(void)resetCursorRects
{
    [self addCursorRect:[self calculatedItemBounds] cursor:[NSCursor openHandCursor]];

}
```

Although you can temporarily remove a single cursor rectangle with [removeCursorRect:cursor:](https://developer.apple.com/documentation/appkit/nsview/1483676-removecursorrect), you should rarely need to do so. Whenever cursor rectangles need to be rebuilt, `NSView` invokes `resetCursorRects` so that you can establish only the cursor rectangles needed. If you implement `resetCursorRects` in this way, you can then simply modify the state this method uses to build its cursor rectangles and then invoke the `NSWindow` method `invalidateCursorRectsForView:`.

An `NSView` object’s cursor rectangles are automatically reset whenever:

- Its frame or bounds rectangle changes, whether by a `setFrame...` or `setBounds...` message or by autoresizing.
- Its window is resized. In this case all of the window’s view objects get their cursor rectangles reset.
- It is moved in the view hierarchy.
- It is scrolled in an [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) or [NSClipView](https://developer.apple.com/documentation/appkit/nsclipview) object.

You can temporarily disable all the cursor rectangles in a window using the `NSWindow` method [disableCursorRects](https://developer.apple.com/documentation/appkit/nswindow/1419639-disablecursorrects) and enable them again with the [enableCursorRects](https://developer.apple.com/documentation/appkit/nswindow/1419202-enablecursorrects) method. The [areCursorRectsEnabled](https://developer.apple.com/documentation/appkit/nswindow/1419668-arecursorrectsenabled) method of `NSWindow` tells you whether they’re currently enabled.

[Next](Document%20Revision%20History.md)[Previous](Text%20System%20Defaults%20and%20Key%20Bindings.md)

