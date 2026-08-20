---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/TrackingAreaObjects/TrackingAreaObjects.html
archived_at: '2026-07-15T07:15:36.431754Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Handling%20Tablet%20Events.md)[Previous](Handling%20Key%20Events.md)

# Using Tracking-Area Objects

An instance of the [NSTrackingArea](https://developer.apple.com/documentation/appkit/nstrackingarea) class defines an area of a view that is responsive to the movements of the mouse. When the mouse cursor enters this area, moves around in it, and leaves it, the Application Kit sends (depending on the options specified) mouse-tracking, mouse-moved, and cursor-update messages to a designated object.

The Application Kit sends the mouse-tracking messages [mouseEntered:](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered) and [mouseExited:](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited) to an object when the mouse cursor enters and exits a region of a window. Mouse tracking enables the view owning the region to respond, for example, by drawing a highlight color or displaying a tool tip. The Application Kit also sends [mouseMoved:](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved) messages to the object if [NSMouseMoved](https://developer.apple.com/documentation/appkit/nsmousemoved) types of events are requested. Cursor-update events are a special kind of mouse-tracking event that the Application Kit handles automatically. When the mouse pointer enters a cursor rectangle, the Application Kit displays a cursor image appropriate to the type of view under the rectangle; for example, when a mouse pointer enters a text view, an I-beam cursor is displayed.

The sections in this chapter describe how to create `NSTrackingArea` objects, attach them to views, respond to related events, and manage the objects when changes in view geometry occur.

An [NSTrackingArea](https://developer.apple.com/documentation/appkit/nstrackingarea) object defines a region of a view that is sensitive to the movements of the mouse. When the mouse enters, moves about, and exits that region, the Application Kit sends mouse-tracking, mouse-moved, and cursor-update messages. The region is a rectangle specified in the local coordinate system of its associated view. The recipient of the messages (the _owner_) is specified when the tracking-area object is [created](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39); although the owner can be any object, it is often the view associated with the tracking-area object.

When you create an `NSTrackingArea` object you must specify one or more options. These options, which are enumerated constants declared by the class, configure various aspects of tracking-area behavior. They fall into three general categories:

- __The type of event message sent__

  You can request [mouseEntered:](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered) and [mouseExited:](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited) messages ([NSTrackingMouseEnteredAndExited](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1524568-mouseenteredandexited)); you can request [mouseMoved:](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved) messages ([NSTrackingMouseMoved](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackingmousemoved)); and you can request [cursorUpdate:](https://developer.apple.com/documentation/appkit/nsresponder/1525066-cursorupdate) messages ([NSTrackingCursorUpdate](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackingcursorupdate)).

  You are not limited to a single option from this set; you can perform a bitwise-OR operation to request multiple types of messages.
- __The active scope of tracking-area messages__

  You must specify _one_ of the following options to request when the tracking area should actively generate events:

  - When the associated view is first responder ([NSTrackingActiveWhenFirstResponder](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1535223-activewhenfirstresponder))
  - When the associated view is in the key window ([NSTrackingActiveInKeyWindow](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1528141-activeinkeywindow))
  - When the associated view is in the active application ([NSTrackingActiveInActiveApp](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1530472-activeinactiveapp))
  - At all times regardless of application activation ([NSTrackingActiveAlways](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1530540-activealways))
- __Refinements of tracking-area behavior__

  You can request that the first message be sent when the mouse cursor first leaves the tracking area ([NSTrackingAssumeInside](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1534113-assumeinside)); you can request the tracking area to be the same as the visible rectangle of the associated view ([NSTrackingInVisibleRect](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackinginvisiblerect)); and you can request that mouse drags into and out of the tracking area generate `mouseEntered:` and `mouseExited:` events ([NSTrackingEnabledDuringMouseDrag](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackingenabledduringmousedrag)).

  You are not limited to a single option from this set; you can perform a bitwise-OR operation to request multiple refinements on behavior.

You [initialize](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) an allocated instance of `NSTrackingArea` with the [initWithRect:options:owner:userInfo:](https://developer.apple.com/documentation/appkit/nstrackingarea/1524488-initwithrect) method. After creating the object, you must associate it with a view by invoking the `NSView` method [addTrackingArea:](https://developer.apple.com/documentation/appkit/nsview/1483489-addtrackingarea). You can create an `NSTrackingArea` instance and add it to a view at any point because (unlike the mouse-tracking API in earlier releases), successful creation does not depend on the view being added to a window. Listing 6-1 shows the creation and addition of an `NSTrackingArea` instance in a custom view’s [initWithFrame:](https://developer.apple.com/documentation/appkit/nsview/1483458-initwithframe) method; in this case, the owning view is requesting that the Application Kit send `mouseEntered:`, `mouseExited:` and `mouseMoved:` messages whenever its window is the key window.

__Listing 6-1__  Initializing an `NSTrackingArea` instance

```objc
- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        trackingArea = [[NSTrackingArea alloc] initWithRect:eyeBox
            options: (NSTrackingMouseEnteredAndExited | NSTrackingMouseMoved | NSTrackingActiveInKeyWindow )
            owner:self userInfo:nil];
        [self addTrackingArea:trackingArea];
    }
    return self;
}
```

The last parameter of `initWithRect:options:owner:userInfo:` is a [dictionary](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) that you can use to pass arbitrary data to the recipient of mouse-tracking and cursor-update messages. The receiving object can access the dictionary by sending [userData](https://developer.apple.com/documentation/appkit/nsevent/1526810-userdata) to the [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) object passed into the [mouseEntered:](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered), [mouseExited:](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited), or [cursorUpdate:](https://developer.apple.com/documentation/appkit/nsresponder/1525066-cursorupdate) method. Sending `userData` messages in [mouseMoved:](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved) methods causes an assertion failure. (In the example in Listing 6-1, the _userInfo_ parameter is set to `nil`.)

Tracking rectangle bounds are inclusive for the top and left edges, but not for the bottom and right edges. Thus, if you have a unflipped view with a tracking rectangle covering its bounds, and the view’s frame has the geometry `frame.origin = (100, 100), frame.size = (200, 200)`, then the area for which the tracking rectangle is active is `frame.origin = (100, 101), frame.size = (199, 199`), in frame coordinates.

Because `NSTrackingArea` objects are owned by their views, the Application Kit can automatically recompute the tracking-area regions when the view is added or removed from a window or when the view changes position within its window. But in situations where the Application Kit cannot recompute an affected tracking area (or areas), it sends [updateTrackingAreas](https://developer.apple.com/documentation/appkit/nsview/1483719-updatetrackingareas) to the associated view, asking it to recompute and reset the areas. One such situation is when a change in view location affects the view’s visible rectangle ([visibleRect](https://developer.apple.com/documentation/appkit/nsview/1483446-visiblerect))—unless the `NSTrackingArea` object for that view was created with the [NSTrackingInVisibleRect](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackinginvisiblerect) option, in which case the Application Kit handles the re-computation. Note that the Application Kit sends `updateTrackingAreas` to every view whether it has a tracking area or not.

You can override the `updateTrackingAreas` method as shown in Listing 6-2 to remove the current tracking areas from their views, [release](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27) them, and then add new `NSTrackingArea` objects to the same views with recomputed regions.

__Listing 6-2__  Resetting a tracking-area object

```objc
- (void)updateTrackingAreas {
    NSRect eyeBox;
    [self removeTrackingArea:trackingArea];
    [trackingArea release];
    eyeBox = [self resetEye];
    trackingArea = [[NSTrackingArea alloc] initWithRect:eyeBox
        options: (NSTrackingMouseEnteredAndExited | NSTrackingMouseMoved | NSTrackingActiveInKeyWindow)
        owner:self userInfo:nil];
    [self addTrackingArea:trackingArea];
}
```

If your class is not a custom view class, you can register your class instance as an observer for the [notification](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35) [NSViewFrameDidChangeNotification](https://developer.apple.com/documentation/appkit/nsviewframedidchangenotification) and have it reestablish the tracking rectangles on receiving the notification.

The owner of an `NSTrackingArea` object created with the [NSTrackingMouseEnteredAndExited](https://developer.apple.com/documentation/appkit/nstrackingarea/options/1524568-mouseenteredandexited) option receives a [mouseEntered:](https://developer.apple.com/documentation/appkit/nsresponder/1529306-mouseentered) whenever the mouse cursor enters the region of a view defined by the tracking-area object; subsequently, it receives a [mouseExited:](https://developer.apple.com/documentation/appkit/nsresponder/1527561-mouseexited) messages when the mouse leaves that region. If the [NSTrackingMouseMoved](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackingmousemoved) option is also specified for the tracking-area object, the owner also receives one or more [mouseMoved:](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved) messages between each `mouseEntered:` and `mouseExited:` message. You override the corresponding `NSResponder` methods to handle these messages to perform such tasks as highlighting the view, displaying a custom tool tip, or displaying related information in another view.

The tracking code in Listing 6-2 is used in making an “eyeball” follow the movement of the mouse pointer when it enters a tracking rectangle.

__Listing 6-3__  Handling mouse-entered, mouse-moved, and mouse-exited events

```objc
- (void)mouseEntered:(NSEvent *)theEvent {
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
    [self resetEye];
    [self setNeedsDisplayInRect:eyeBox];
    [self displayIfNeeded];
}
```

Just as you can with mouse-down and mouse-up messages, you can query the passed-in [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) objects to get information related to the event.

One common use of `NSTrackingArea` objects is to change the cursor image over different types of views. Text, for example, typically requires an I-beam cursor. Many Application Kit classes provide cursor images appropriate to their view instances; you get this behavior “for free.“ However, you may want to specify a specific (or different) cursor image for instances of your custom view subclasses.

You change the cursor image for your view in an override of the `NSResponder` method [cursorUpdate:](https://developer.apple.com/documentation/appkit/nsresponder/1525066-cursorupdate). To receive this message, you must [create](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) an `NSTrackingArea` object by invoking the [initWithRect:options:owner:userInfo:](https://developer.apple.com/documentation/appkit/nstrackingarea/1524488-initwithrect) initializer with an option of [NSTrackingCursorUpdate](https://developer.apple.com/documentation/appkit/nstrackingareaoptions/nstrackingcursorupdate) (along with any other desired options). Then add the created object to a view with [addTrackingArea:](https://developer.apple.com/documentation/appkit/nsview/1483489-addtrackingarea). Thereafter, the entry of the mouse into the tracking area generates an [NSCursorUpdate](https://developer.apple.com/documentation/appkit/nscursorupdate) event; the `NSWindow` object handles this event by sending a `cursorUpdate:` message to the owner of the tracking area (which is typically the view itself). The implementation of `cursorUpdate:` should use the appropriate [NSCursor](https://developer.apple.com/documentation/appkit/nscursor) methods to set a standard or custom cursor image.

Cursor rectangles may overlap or be completely nested, one within the other. Arbitration of cursor updates follows the normal responder chain mechanism. The cursor rectangle of the view under the mouse cursor first receives the `cursorUpdate:` message. It may either display a cursor or pass the message up the responder chain, where a view with an overlapped cursor rectangle can then respond to the message.

Listing 6-4 shows an implementation of `cursorUpdate:` that sets the cursor of the view to a cross-hair image. Note that it is not necessary to reset the cursor image back to what it was when the mouse exits the tracking area. The Application Kit handles this automatically for you by sending a `cursorUpdate:` message to the view over which the mouse cursor moves as it exits the cursor rectangle.

__Listing 6-4__  Handling a cursor-update event

```objc
-(void)cursorUpdate:(NSEvent *)theEvent
{
    [[NSCursor crosshairCursor] set];
}
```

If the responder owning the tracking-area object does not implement the `cursorUpdate:` method, the default implementation forwards the message up the responder chain. If the responder implements `cursorUpdate:` but decides not to handle the current event, it should invoke the superclass implementation of `cursorUpdate:`.

As with any other kind of `NSTrackingArea` object, you might occasionally need to recompute and recreate a tracking-area object used for cursor updates when the associated view has changes in its location or size. See [Managing a Tracking-Area Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedqlktk4zq) for more information.

Beginning with OS X v10.5, the [NSTrackingArea](https://developer.apple.com/documentation/appkit/nstrackingarea) class and the related `NSView` methods [addTrackingArea:](https://developer.apple.com/documentation/appkit/nsview/1483489-addtrackingarea), [removeTrackingArea:](https://developer.apple.com/documentation/appkit/nsview/1483634-removetrackingarea), [updateTrackingAreas](https://developer.apple.com/documentation/appkit/nsview/1483719-updatetrackingareas), and [trackingAreas](https://developer.apple.com/documentation/appkit/nsview/1483333-trackingareas) replace the following methods of `NSView`, which are considered legacy API but remain supported for compatibility:

|  |
| --- |
| [addTrackingRect:owner:userData:assumeInside:](https://developer.apple.com/documentation/appkit/nsview/1483668-addtrackingrect) |
| [removeTrackingRect:](https://developer.apple.com/documentation/appkit/nsview/1483729-removetrackingrect) |
| [addCursorRect:cursor:](https://developer.apple.com/documentation/appkit/nsview/1483540-addcursorrect) |
| [removeCursorRect:cursor:](https://developer.apple.com/documentation/appkit/nsview/1483676-removecursorrect) |
| [discardCursorRects](https://developer.apple.com/documentation/appkit/nsview/1483733-discardcursorrects) |
| [resetCursorRects](https://developer.apple.com/documentation/appkit/nsview/1483448-resetcursorrects) |

The [NSTrackingRectTag](https://developer.apple.com/documentation/appkit/nstrackingrecttag) type, returned by the `addTrackingRect:owner:userData:assumeInside:` and passed into the `removeTrackingRect:` methods, is also a legacy type. Internally this type is treated the same as `NSTrackingArea *`.

The underlying implementation for the legacy methods is based on `NSTrackingArea`, resulting in the following implications:

- An invocation of the `addTrackingRect:owner:userData:assumeInside:` method creates an `NSTrackingArea` object with the options `NSTrackingMouseEnteredAndExited` and `NSTrackingActiveAlways` set. It also includes the `NSTrackingAssumeInside` option if the last parameter of the function is `YES`. After creating the object, it adds it to the receiver (`addTrackingArea:`) and returns it as a tag.
- The [resetCursorRects](https://developer.apple.com/documentation/appkit/nsview/1483448-resetcursorrects) method is invoked after [updateTrackingAreas](https://developer.apple.com/documentation/appkit/nsview/1483719-updatetrackingareas).

In addition, the following `NSWindow` cursor-related methods are legacy API, but maintained for compatibility:

|  |
| --- |
| [discardCursorRects](https://developer.apple.com/documentation/appkit/nswindow/1419269-discardcursorrects) |
| [invalidateCursorRectsForView:](https://developer.apple.com/documentation/appkit/nswindow/1419601-invalidatecursorrects) |
| [resetCursorRects](https://developer.apple.com/documentation/appkit/nswindow/1419464-resetcursorrects) |

[Next](Handling%20Tablet%20Events.md)[Previous](Handling%20Key%20Events.md)

