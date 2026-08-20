---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/HandlingMouseEvents/HandlingMouseEvents.html
archived_at: '2026-07-15T07:15:35.456522Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Handling%20Key%20Events.md)[Previous](Event%20Handling%20Basics.md)

# Handling Mouse Events

Mouse events are one of the two most frequent kinds of events handled by an application (the other kind being, of course, key events). Mouse clicks—which involve a user pressing and then releasing a mouse button—generally indicate selection, but what the selection means is left up to the object responding to the event. For example, a mouse click could tell the responding object to alter its appearance and then send an action message. Mouse drags generally indicate that the receiving view should move itself or a drawn object within its bounds. The following sections describe how you might handle mouse-down, mouse-up, and mouse-drag events.

Before going into the “how to” of mouse-event handling, let’s review some central facts about mouse events discussed in [Event Architecture](Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4ytc), [Event Objects and Types](Event%20Objects%20and%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedilktk42a), and [Event Handling Basics](Event%20Handling%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedklktk4ytc):

- Mouse events are dispatched by an [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) object to the [NSView](https://developer.apple.com/documentation/appkit/nsview) object over which the event occurred.
- Subsequent key events are dispatched to that view object if it accepts first responder status.
- If the user clicks a view that isn’t in the key window, by default the window is brought forward and made key, but the mouse event is not dispatched.
- Mouse events are of various event types related to the mouse button pressed (left, right, other) and the nature of the action on the mouse button. Each event type is, in turn, related to an [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) method, as Table 4-1 shows for left-button mouse events.

  __Table 4-1__  Type constants and methods related to left-button mouse events

  | Action | Event type (left mouse button) | Mouse-event method invoked (left mouse button) |
  | Press down the button | [NSLeftMouseDown](https://developer.apple.com/documentation/appkit/nsleftmousedown) | [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown) |
  | Move the mouse while pressing the button | [NSLeftMouseDragged](https://developer.apple.com/documentation/appkit/nsleftmousedragged) | [mouseDragged:](https://developer.apple.com/documentation/appkit/nsresponder/1527420-mousedragged) |
  | Release the button | [NSLeftMouseUp](https://developer.apple.com/documentation/appkit/nsleftmouseup) | [mouseUp:](https://developer.apple.com/documentation/appkit/nsresponder/1535349-mouseup) |
  | Move the mouse without pressing any button | [NSMouseMoved](https://developer.apple.com/documentation/appkit/nsmousemoved) | [mouseMoved:](https://developer.apple.com/documentation/appkit/nsresponder/1525114-mousemoved) |

  Right-mouse events are defined by the Application Kit to open contextual menus, but you can override this behavior if necessary (in, for example, [rightMouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524727-rightmousedown)). The Application Kit does not define any default behavior for third (“other”) mouse buttons.
- The general sequence of mouse events is: mouse-down, mouse-dragged (multiple), mouse-up.

  If dispatch of them is turned on, mouse-moved events may only occur between a mouse-up and the next mouse-down. They do not occur between a mouse-down and the subsequent mouse-up.
- Mouse events (as [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) objects) can have subtypes. Currently, these subtypes are restricted to tablet events (particularly tablet-pointer events) but more subtypes could be added in the future. (See [Tablet Events](Event%20Objects%20and%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedilktk4zq) for more information.)

One of the earliest things to consider in handling mouse-down events is whether the receiving [NSView](https://developer.apple.com/documentation/appkit/nsview) object should become the first responder, which means that it will be the first candidate for subsequent key events and action messages. Views that handle graphic elements that the user can select—drawing shapes or text, for example—should typically accept first responder status on a mouse-down event by overriding the [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder) method to return `YES`, as discussed in [Preparing a Custom View for Receiving Events](Event%20Handling%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedklktk4yti).

By default, a mouse-down event in a window that isn’t the key window simply brings the window forward and makes it key; the event isn’t sent to the `NSView` object over which the mouse click occurs. The `NSView` can claim an initial mouse-down event, however, by overriding [acceptsFirstMouse:](https://developer.apple.com/documentation/appkit/nsview/1483410-acceptsfirstmouse) to return `YES`. The argument of this method is the mouse-down event that occurred in the non-key window, which the view object can examine to determine whether it wants to receive the mouse event and potentially become first responder. You want the default behavior of this method in, for example, a control that affects the selected object in a window. However, in certain cases it’s appropriate to override this behavior, such as for controls that should receive [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown) messages even when the window is inactive. Examples of controls that support this click-through behavior are the title-bar buttons of a window.

In your implementation of an [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) mouse-event method, often the first thing you might do is examine the passed-in [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) object to decide _if_ this is an event you want to handle. If it is an event that you handle, then you may need to extract information from the `NSEvent` object to help you handle it. Specifically, you can get the following information from the `NSEvent` object:

- Get the location of the mouse event in base coordinates ([locationInWindow](https://developer.apple.com/documentation/appkit/nsevent/1529068-locationinwindow)) and then convert this location to the receiving view’s coordinate system; see [Getting the Location of an Event](Event%20Handling%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedklktk4ytk) for details.
- See if any modifier keys were pressed when the mouse button was clicked ([modifierFlags](https://developer.apple.com/documentation/appkit/nsevent/1534405-modifierflags)); this procedure is described in [Testing for Event Type and Modifier Flags](Event%20Handling%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedklktk4ytm). An application may define modifier keys to change the significance of a mouse event.
- Find out how many mouse clicks occurred in quick succession ([clickCount](https://developer.apple.com/documentation/appkit/nsevent/1528200-clickcount)); multiple mouse clicks are conceptually treated as a single mouse-down event within a narrow time threshold (although they arrive in a series of `mouseDown:` messages). As with modifier keys, a double- or triple-click can change the significance of a mouse event for an application. (See [Listing 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedmlktk4za) for an example.)
- If the interval between mouse clicks is important, you can send [timestamp](https://developer.apple.com/documentation/appkit/nsevent/1528239-timestamp) to the `NSEvent` object and record the moment each event occurred.
- If the change in position of the mouse between subsequent events is important, you can find out the delta values for the x-coordinate and y-coordinate using, respectively, [deltaX](https://developer.apple.com/documentation/appkit/nsevent/1534871-deltax) and [deltaY](https://developer.apple.com/documentation/appkit/nsevent/1534158-deltay).

Many view objects in the Application Kit (such as controls and menu items) change their appearance in response to mouse-down events, sometimes only until the subsequent mouse-up event. Doing this provides visual confirmation to the user that their action is effective or that the clicked object is now selected. Listing 4-1 shows a simple example of this.

__Listing 4-1__  Simple handling of mouse click—changing view’s appearance

```objc
- (void)mouseDown:(NSEvent *)theEvent {
    [self setFrameColor:[NSColor redColor]];
    [self setNeedsDisplay:YES];
}

- (void)mouseUp:(NSEvent *)theEvent {
    [self setFrameColor:[NSColor greenColor]];
    [self setNeedsDisplay:YES];
}

- (void)drawRect:(NSRect)rect {
    [[self frameColor] set];
    NSRectFill(rect);
}
```

But many view objects, particularly controls and cells, do more than simply change their appearance in response to mouse clicks. One common paradigm is for the clicked view to send an action message to a target object (where both action and target are settable properties of the view). As shown in Listing 4-2, the view typically sends the message on `mouseUp:` rather than `mouseDown:`, thus giving users an opportunity to change their minds mid-click.

__Listing 4-2__  Simple handling of mouse click—sending an action message

```objc
- (void)mouseDown:(NSEvent *)theEvent {
    [self setFrameColor:[NSColor redColor]];
    [self setNeedsDisplay:YES];
}

- (void)mouseUp:(NSEvent *)theEvent {
    [self setFrameColor:[NSColor greenColor]];
    [self setNeedsDisplay:YES];
    [NSApp sendAction:[self action] to:[self target] from:self];
}

- (SEL)action {return action; }

- (void)setAction:(SEL)newAction {
    action = newAction;
}

- (id)target { return target; }

- (void)setTarget:(id)newTarget {
    target = newTarget;
}
```

Listing 4-3 gives a more complex, real-world example. (It’s from the example project for the Sketch application.) This implementation of `mouseDown:` determines if users double-clicked a graphical object and, if they did, enables the editing of that object. Otherwise, if a palette object is selected, it creates an instance of that object at the location of the mouse click.

__Listing 4-3__  Handling a mouse-down event—Sketch application

```objc
- (void)mouseDown:(NSEvent *)theEvent {
    Class theClass = [[SKTToolPaletteController sharedToolPaletteController] currentGraphicClass];
    if ([self editingGraphic]) {
        [self endEditing];
    }
    if ([theEvent clickCount] > 1) {
        NSPoint curPoint = [self convertPoint:[theEvent locationInWindow] fromView:nil];
        SKTGraphic *graphic = [self graphicUnderPoint:curPoint];
        if (graphic && [graphic isEditable]) {
            [self startEditingGraphic:graphic withEvent:theEvent];
            return;
        }
    }
    if (theClass) {
        [self clearSelection];
        [self createGraphicOfClass:theClass withEvent:theEvent];
    } else {
        [self selectAndTrackMouseWithEvent:theEvent];
    }
}
```

The classes of the Application Kit that implement controls manage this target-action behavior for you.

Mouse-down and mouse-up events, which are the events associated with mouse clicks, are not the only types of mouse events dispatched in an application. Views can also receive mouse-dragged events when a user moves a mouse while pressing down a mouse button. A view typically interprets mouse-dragged events as commands to move itself by altering its frame location or to move a region within its bounds by redrawing it. However, other interpretations of mouse-dragged events are possible; for example, a view could respond to mouse-dragged events by magnifying the region that the mouse pointer is dragged over.

With the Application Kit you can take one of two general approaches when handling mouse-dragged events. The first approach is overriding the three `NSResponder` methods [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown), [mouseDragged:](https://developer.apple.com/documentation/appkit/nsresponder/1527420-mousedragged), and [mouseUp:](https://developer.apple.com/documentation/appkit/nsresponder/1535349-mouseup) (for left mouse-button operations). For each dragging sequence, the Application Kit sends a `mouseDown:` message to a responder object, then sends one or more `mouseDragged:` messages, and ends the sequence with a `mouseUp:` message. [The Three-Method Approach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedmlktk4zq) describes this approach.

The other approach treats the mouse events in a dragging sequence as a single event, from mouse down, through dragging, to mouse up. To do this, the responder object must usually short-circuit the application’s normal event loop by entering a event-tracking loop to filter and process only mouse events of interest. For example, an [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) object highlights itself upon a mouse-down event, then follows the mouse location during dragging, highlighting when the mouse is inside and unhighlighting when the mouse is outside. If the mouse is inside on the mouse-up event, the button object sends its action message. This approach is described in [The Mouse-Tracking Loop Approach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedmlktk42a).

Both of these approaches have their advantages and drawbacks. Establishing a mouse-tracking loop gives you greater control over the way other events interact with your application during a dragging operation. However, the application’s main thread is unable to process any other requests during an event-tracking loop and timers might not fire as expected. The mouse-tracking approach is more efficient because it typically requires less code and allows all dragging variables to be local. However, the class implementing it becomes more difficult to extend without the subclass reimplementing all the dragging code.

Implementing the individual `mouseDown:`, `mouseDragged:`, and `mouseUp:` methods is often a better design choice when writing an event-driven application. Each of the methods have a clearly defined scope, which often leads to clearer code. This approach also makes it much easier for subclasses to override behavior for handling mouse-down, mouse-dragged, and mouse-up events. However, this technique can require more code and instance variables.

To handle a mouse-dragging operation, you can override the three `NSResponder` methods that mark the discrete stages of a mouse-dragging operation: [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown), [mouseDragged:](https://developer.apple.com/documentation/appkit/nsresponder/1527420-mousedragged), and [mouseUp:](https://developer.apple.com/documentation/appkit/nsresponder/1535349-mouseup) (or, for right-mouse dragging, [rightMouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524727-rightmousedown), [rightMouseDragged:](https://developer.apple.com/documentation/appkit/nsresponder/1529135-rightmousedragged), and [rightMouseUp:](https://developer.apple.com/documentation/appkit/nsresponder/1526309-rightmouseup)). A mouse-dragging sequence consists of one `mouseDown:` message, followed by (typically) multiple `mouseDragged:` messages, and a concluding `mouseUp:` message.

The subclass implementing these methods often has to declare instance variables to hold the changing values or states of various things between successive events. These things could be geometric entities such as rectangles or points (corresponding to view frames or regions within views) or they could be simple Boolean values indicating, for example, that an object is selected. In the `mouseDown:` method, the view generally initializes any dragging-related instance variables; in the `mouseDragged:` method it might update those instance variables or check them prior to performing an action; and in the `mouseUp:` method, it often resets those instance variables to their initial values.

Because mouse-dragging operations often redraw an object in the incrementally changing locations where users drag that object, implementations of the three mouse-dragging methods usually need to find the location of each mouse event in the view’s coordinate system. As explained in [Getting the Location of an Event](Event%20Handling%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedklktk4ytk), this requires the view to send [locationInWindow](https://developer.apple.com/documentation/appkit/nsevent/1529068-locationinwindow) to the passed-in `NSEvent` object and then use the [convertPoint:fromView:](https://developer.apple.com/documentation/appkit/nsview/1483269-convertpoint) method to convert the resulting location to the local coordinate system. When changes in location or geometry require the view to redraw itself or a portion of itself, the view marks the areas needing display using the [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) or [setNeedsDisplayInRect:](https://developer.apple.com/documentation/appkit/nsview/1483475-setneedsdisplayinrect) method and the view is later asked to redraw itself (in [drawRect:](https://developer.apple.com/documentation/appkit/nsview/1483686-draw)) through the auto-display mechanism (assuming that mechanism is not turned off).

Listing 4-4 illustrates the use of dragging-related instance variables, getting the mouse location in local coordinates (and testing whether that location is in a specific region), and marking that region of the receiving view for redisplay.

__Listing 4-4__  Handling a mouse-dragging operation—three-method approach

```objc
- (void)mouseDown:(NSEvent *)theEvent {
    // mouseInCloseBox and trackingCloseBoxHit are instance variables
    if (mouseInCloseBox = NSPointInRect([self convertPoint:[theEvent locationInWindow] fromView:nil], closeBox)) {
        trackingCloseBoxHit = YES;
        [self setNeedsDisplayInRect:closeBox];
    }
    else if ([theEvent clickCount] > 1) {
        [[self window] miniaturize:self];
        return;
    }
}

- (void)mouseDragged:(NSEvent *)theEvent {
    NSPoint windowOrigin;
    NSWindow *window = [self window];

    if (trackingCloseBoxHit) {
        mouseInCloseBox = NSPointInRect([self convertPoint:[theEvent locationInWindow] fromView:nil], closeBox);
        [self setNeedsDisplayInRect:closeBox];
        return;
    }

    windowOrigin = [window frame].origin;

    [window setFrameOrigin:NSMakePoint(windowOrigin.x + [theEvent deltaX], windowOrigin.y - [theEvent deltaY])];
}

- (void)mouseUp:(NSEvent *)theEvent {
    if (NSPointInRect([self convertPoint:[theEvent locationInWindow] fromView:nil], closeBox)) {
        [self tryToCloseWindow];
        return;
    }
    trackingCloseBoxHit = NO;
    [self setNeedsDisplayInRect:closeBox];
}
```


The mouse-tracking technique for handling mouse-dragging operations is applied in a single method, usually (but not necessarily) in [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown). The implementing responder object first declares and possibly initializes one or more local variables to use within the loop. Often one of these variables holds a value, often Boolean, that is used to control the loop. When some condition is met, typically the receipt of a mouse-up event, the variable value is changed; when this variable is tested next time through the loop, control exits the loop.

The central method of a mouse-tracking loop is the `NSApplication` method [nextEventMatchingMask:untilDate:inMode:dequeue:](https://developer.apple.com/documentation/appkit/nsapplication/1428485-nexteventmatchingmask) and the `NSWindow` method of the same name. These methods fetch events from the event queue that are of the types specified by one or more type-mask constants; for mouse-dragging, these constants are typically [NSLeftMouseDraggedMask](https://developer.apple.com/documentation/appkit/nsleftmousedraggedmask) and [NSLeftMouseUpMask](https://developer.apple.com/documentation/appkit/nsleftmouseupmask). Events of other types are left in the queue. (The run-loop mode parameter of both `nextEventMatchingMask:untilDate:inMode:dequeue:` methods should be `NSEventTrackingRunLoopMode`.)

After receiving a mouse-down event, fetch subsequent mouse events within the loop using `nextEventMatchingMask:untilDate:inMode:dequeue:`. Process [NSLeftMouseDragged](https://developer.apple.com/documentation/appkit/nsleftmousedragged) events as you would process them in the [mouseDragged:](https://developer.apple.com/documentation/appkit/nsresponder/1527420-mousedragged) method (described in [The Three-Method Approach](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedmlktk4zq)); similarly, handle [NSLeftMouseUp](https://developer.apple.com/documentation/appkit/nsleftmouseup) events as you would handle them in [mouseUp:](https://developer.apple.com/documentation/appkit/nsresponder/1535349-mouseup). Usually mouse-up events indicate that execution control should break out of the loop.

The `mouseDown:` method template in Listing 4-5 shows one possible kind of modal event loop.

__Listing 4-5__  Handling mouse-dragging in a mouse-tracking loop—simple example

```objc
- (void)mouseDown:(NSEvent *)theEvent {
    BOOL keepOn = YES;
    BOOL isInside = YES;
    NSPoint mouseLoc;

    while (keepOn) {
        theEvent = [[self window] nextEventMatchingMask: NSLeftMouseUpMask |
                NSLeftMouseDraggedMask];
        mouseLoc = [self convertPoint:[theEvent locationInWindow] fromView:nil];
        isInside = [self mouse:mouseLoc inRect:[self bounds]];

        switch ([theEvent type]) {
            case NSLeftMouseDragged:
                    [self highlight:isInside];
                    break;
            case NSLeftMouseUp:
                    if (isInside) [self doSomethingSignificant];
                    [self highlight:NO];
                    keepOn = NO;
                    break;
            default:
                    /* Ignore any other kind of event. */
                    break;
        }

    };

    return;
}
```

This loop converts the mouse location and checks whether it’s inside the receiver. It highlights itself using the fictional `highlight:` method and, on receiving a mouse-up event, it invokes `doSomethingSignificant` to perform an important action. Instead of merely highlighting, a custom `NSView` object might move a selected object, draw a graphic image according to the mouse’s location, and so on.

Listing 4-6 is a slightly more complicated example that includes the use of an autorelease pool and testing for a modifier key.

__Listing 4-6__  Handling mouse-dragging in a mouse-tracking loop—complex example

```objc
- (void)mouseDown:(NSEvent *)theEvent
{
    if ([theEvent modifierFlags] & NSAlternateKeyMask)  {
        BOOL                dragActive = YES;
        NSPoint             location = [renderView convertPoint:[theEvent locationInWindow] fromView:nil];
        NSAutoreleasePool   *myPool = nil;
        NSEvent*            event = NULL;
        NSWindow            *targetWindow = [renderView window];

        myPool = [[NSAutoreleasePool alloc] init];
        while (dragActive) {
            event = [targetWindow nextEventMatchingMask:(NSLeftMouseDraggedMask | NSLeftMouseUpMask)
                                untilDate:[NSDate distantFuture]
                                inMode:NSEventTrackingRunLoopMode
                                dequeue:YES];
            if(!event)
                continue;
            location = [renderView convertPoint:[event locationInWindow] fromView:nil];
            switch ([event type]) {
                case NSLeftMouseDragged:
                    annotationPeel = (location.x * 2.0 / [renderView bounds].size.width);
                    [imageLayer showLens:(annotationPeel <= 0.0)];
                    [peelOffFilter setValue:[NSNumber numberWithFloat:annotationPeel] forKey:@"inputTime"];
                    [self refresh];
                    break;

                case NSLeftMouseUp:
                    dragActive = NO;
                    break;

                default:
                    break;
            }
        }
        [myPool release];
    } else {
        // other tasks handled here......
    }
}
```

A mouse-tracking loop is driven only as long as the user actually moves the mouse. It won’t work, for example, to cause continual scrolling if the user presses the mouse button but never moves the mouse itself. For this, your loop should start a periodic event stream using the `NSEvent` class method [startPeriodicEventsAfterDelay:withPeriod:](https://developer.apple.com/documentation/appkit/nsevent/1526044-startperiodiceventsafterdelay), and add [NSPeriodicMask](https://developer.apple.com/documentation/appkit/nsperiodicmask) to the mask bit-field passed to `nextEventMatchingMask:`. In the `switch` statement the implementing view object can then check for events of type [NSPeriodic](https://developer.apple.com/documentation/appkit/nsperiodic) and take whatever action it needs to—scrolling a document view or moving a step in an animation, for example. If you need to check the mouse location during a periodic event, you can use the `NSWindow` method [mouseLocationOutsideOfEventStream](https://developer.apple.com/documentation/appkit/nswindow/1419280-mouselocationoutsideofeventstrea).

A potential problem with mouse-tracking code is the user pressing a key combination that is a command, such as Command-z (undo), while a tracking operation is underway. Because your mouse-tracking code (either in the three-method approach or a mouse-tracking loop) isn’t looking for that key event, the code might not know how to handle that key command or could handle it wrongly, with unwelcome consequences.

The problem here with a mouse-tracking loop might not be readily apparent because, after all, the [nextEventMatchingMask:untilDate:inMode:dequeue:](https://developer.apple.com/documentation/appkit/nsapplication/1428485-nexteventmatchingmask) loop ensures only mouse-tracking events are delivered. Why would key events be a problem? Consider the code in Listing 4-7. While this mouse-tracking loop is active, let’s say the user issues some key-equivalent commands.

__Listing 4-7__  Typical mouse-tracking loop

```objc
- (void)mouseDown:(NSEvent *)theEvent {
  NSPoint pos;

  while ((theEvent = [[self window] nextEventMatchingMask:
    NSLeftMouseUpMask | NSLeftMouseDraggedMask])) {

    NSPoint pos = [self convertPoint:[theEvent locationInWindow]
                            fromView:nil];

    if ([theEvent type] == NSLeftMouseUp)
      break;

    // Do some other processing...
  }
}
```

What happens after the mouse-tracking loop concludes? After the user lets go of the mouse button, the application handles all of the pending commands corresponding to the mnemonics the user pressed during the loop. The effects of this delayed handling are probably undesirable. You can guard against this by filtering the event stream for key events and then explicitly ignoring them. Listing 4-8 shows how you can modify the code above to accomplish this (new code in italics).

__Listing 4-8__  Typical mouse-tracking loop—with key events negated

```objc
- (void)mouseDown:(NSEvent *)theEvent {
  NSPoint pos;

  while ((theEvent = [[self window] nextEventMatchingMask:
      NSLeftMouseUpMask | NSLeftMouseDraggedMask | NSKeyDownMask])) {

    NSPoint pos = [self convertPoint:[theEvent locationInWindow]
                            fromView:nil];

    if ([theEvent type] == NSLeftMouseUp)
        break;
         else if ([theEvent type] == NSKeyDown) {
                NSBeep();
                continue;
    }

    // Do some other processing...
  }
}
```

For dragging operations handled with the three-method approach, the situation with simultaneous mouse and key events is a bit different. In this case, the AppKit processes keyboard events as it normally does during tracking. If the user presses a command mnemonic, even while a tracking operation is going on, the application object dispatches the corresponding messages to its targets. So if, for example, in a drawing application the user drags a blue circle they just created and then (perhaps accidentally) presses Command-x (cut) while the mouse button is still down, the code handling the cut operation is going to run, deleting the object the user was dragging.

The solution to this problem involves a few steps:

- Declare a Boolean instance variable that reflects when a dragging operation is underway.
- Set this variable to `YES` in [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown) and reset it to `NO` in [mouseUp:](https://developer.apple.com/documentation/appkit/nsresponder/1535349-mouseup).
- Override [performKeyEquivalent:](https://developer.apple.com/documentation/appkit/nsresponder/1524690-performkeyequivalent) to check the value of the instance variable and, if a dragging operation is occurring, to discard the key event.

Listing 4-9 shows the implementation code for this (`isBeingManipulated` is the Boolean instance variable).

__Listing 4-9__  Discarding key events during a dragging operation with the three-method approach

```objc
@implementation MyView

- (BOOL)performKeyEquivalent:(NSEvent *)anEvent
{
  if (isBeingManipulated) {
    if ([anEvent type] == NSKeyDown) // Can get NSKeyUp here too
      NSBeep ();
    return YES; // Claim we handled it
  }

  return NO;
}

- (void)mouseDown:(NSEvent *)anEvent
{
  isBeingManipulated = YES;
  // other code goes  here...
}

- (void)mouseUp:(NSEvent *)anEvent
{
  isBeingManipulated = NO;
  // other code goes here ...
}

@end
```

This solution to the problem is simplified and is intended for general illustration. In a real application you might want to check the event type, conditionally set the `isBeingManipulated` variable, and selectively handle key equivalents.

[Next](Handling%20Key%20Events.md)[Previous](Event%20Handling%20Basics.md)

