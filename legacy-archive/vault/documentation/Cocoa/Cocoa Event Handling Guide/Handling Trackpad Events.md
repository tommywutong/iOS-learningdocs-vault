---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/HandlingTouchEvents/HandlingTouchEvents.html
archived_at: '2026-07-15T07:15:35.483942Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Monitoring%20Events.md)[Previous](Handling%20Tablet%20Events.md)

# Handling Trackpad Events

When users touch and move their fingers on the trackpads of the MacBook Air and more recent models of the MacBook Pro, OS X generates multitouch events, gesture events, and mouse events. The trackpad hardware includes built-in support for interpreting common gestures and for mapping movements of a finger to mouse events. In addition, the operating system provides default handling of gestures; you can observe how OS X handles these gestures in the Trackpad system preference. You can also create applications that receive and respond to gestures and multitouch events in distinctive ways.

An application should not rely on gesture-event or touch-event handling as the sole mechanism for interpreting user actions for any critical feature, because users might not be using a trackpad. Touch-event features should supplement the conventional way of conveying user commands.

Gesture events are a species of multitouch events because they’re based on an interpretation of a sequence of touches. In other words, gestures are a series of multitouch events recognized by the trackpad as constituting a gesture. Gestures and touch events require you to adopt a different approach for handling them. To understand these approaches it’s useful to know how and when the events are generated, how they are delivered to your application, and what kind of information they contain about the actual touches on the trackpad.

Gestures are particular movements of fingers on a touch-sensitive surface, such as a trackpad’s, that have a conventional significance. The trackpad driver interprets some of these movements as specific gestures:

- Pinching movements (in or out) are gestures meaning zoom out or zoom in (also called magnification).
- Two fingers moving in opposite semicircles is a gesture meaning rotate.
- Three fingers brushing across the trackpad surface in a common direction is a swipe gesture.
- Two fingers moving vertically or horizontally is a scroll gesture.

The system delivers low-level events representing specific gestures to the active application, where they’re packaged as [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) objects and placed in the application’s event queue. They go along the same path as mouse events for delivery to the view under the mouse pointer. An [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) object delivers a gesture event to the view by calling the appropriate [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) method for the gesture: [magnifyWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525862-magnifywithevent), [rotateWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525572-rotatewithevent), or [swipeWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1524275-swipewithevent). If the view does not handle a gesture, it travels up the responder chain until another object handles it or until it is discarded.

The AppKit framework declares the [NSEventType](https://developer.apple.com/documentation/appkit/nsevent/eventtype) constants for gestures such as [NSEventTypeMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtype/magnify) and [NSEventTypeQuickLook](https://developer.apple.com/documentation/appkit/nsevent/eventtype/quicklook).

As users touch and move their fingers across the trackpad, the trackpad driver generates a _gesture sequence_, which is roughly concurrent with the multitouch sequence described in [Touch Events Represent Fingers on the Trackpad](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedcmznknltc) but contained within it. A gesture sequence begins when the driver first detects a gesture and ends when the driver determines the gesture has ended. In most cases, you do not need to be aware of the gesture sequence; you only need to implement the `NSResponder` method for handling a specific gesture. However, if you want to commit a change related to a specific gesture, such as register an undo operation or perform detailed drawing, you can implement the `NSResponder` method for that gesture and examine the gesture’s [phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase) property. Because a gesture can either end or be cancelled, you need to be prepared to handle both [NSEventPhaseEnded](https://developer.apple.com/documentation/appkit/nsevent/phase/1529162-ended) and [NSEventPhaseCancelled](https://developer.apple.com/documentation/appkit/nsevent/phase/1534443-cancelled).

__Figure 8-1__  A gesture sequence within a multitouch sequence

!

If you need to commit a change related to a specific gesture, you should be aware of some of the behavioral peculiarities of gesture detection. First, multiple gesture sequences can occur within a single multitouch sequence. For example, the user might first pinch a view and then swipe it without removing all of their fingers from the trackpad. Moreover, between the beginning and end of a gesture sequence, the trackpad driver might first interpret a movement as one gesture and then switch its interpretation to another gesture. Currently, however, this happens only for magnify and rotate gestures. Scroll and swipe gestures, once begun, are locked to that gesture until the gesture ends.

As it generates gestures, the trackpad hardware _might_ also emit the touch events that make up the gesture; the system then routes the touch events to the application along with the gesture events. Some trackpads, however, do not support this feature.

The Trackpad preference pane includes an option for scroll gestures: two fingers moving the content view of a scroll view around. Technically, scroll gestures are not specific gestures but mouse events. Unlike a gesture, a scroll wheel event (that is, an event of type [NSScrollWheel](https://developer.apple.com/documentation/appkit/nsscrollwheel)) can have both a [phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase) property and a [momentumPhase](https://developer.apple.com/documentation/appkit/nsevent/1525439-momentumphase) property. The `momentumPhase` property helps you detect momentum scrolling, in which the hardware continues to issue scroll wheel events even though the user is no longer physically scrolling. Devices such as Magic Mouse and Multi-Touch trackpad enable momentum scrolling.

During non momentum scrolling, AppKit routes each scroll wheel event to the view that is beneath the pointer _for that event_. In non momentum scroll wheel events, [momentumPhase](https://developer.apple.com/documentation/appkit/nsevent/1525439-momentumphase) has the value [NSEventPhaseNone](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasenone).

During momentum scrolling, AppKit routes each scroll wheel event to the view that was beneath the pointer when momentum scrolling started. In momentum scroll wheel events, [phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase) has the value [NSEventPhaseNone](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasenone). When the device switches from user-performed scroll events to momentum scroll wheel events, `momentumPhase` is set to [NSEventPhaseBegan](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasebegan). For subsequent momentum scroll wheel events, `momentumPhase` is set to [NSEventPhaseChanged](https://developer.apple.com/documentation/appkit/nsevent/phase/1534418-changed) until the momentum subsides, or the user stops the momentum scrolling; the final momentum scroll wheel event has a `momentumPhase` value of [NSEventPhaseEnded](https://developer.apple.com/documentation/appkit/nsevent/phase/1529162-ended).

It’s important to understand how the difference in the event-routing behavior can affect the events you receive, depending on the scrolling device users are using. When using a Multi-Touch trackpad, users must physically stop scrolling before they can move the pointer, so you won’t receive any mouse-movement events during a scroll. In contrast, a Magic Mouse lets users move the pointer and click in the middle of a scroll. Because a scroll doesn’t end until the user lifts their finger, any additional movement by a finger resting on a Magic Mouse is still considered to be part of the original scroll, which means that the event’s [phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase) property is [NSEventPhaseChanged](https://developer.apple.com/documentation/appkit/nsevent/phase/1534418-changed) and not [NSEventPhaseBegan](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasebegan), as you might expect. If you process scroll wheel events directly, be prepared to receive mouse-movement events (such as [NSLeftMouseDown](https://developer.apple.com/documentation/appkit/nsleftmousedown), [NSRightMouseDragged](https://developer.apple.com/documentation/appkit/nsrightmousedragged), and [NSOtherMouseUp](https://developer.apple.com/documentation/appkit/nsothermouseup)) between [NSEventPhaseBegan](https://developer.apple.com/documentation/appkit/nseventphase/nseventphasebegan) and [NSEventPhaseEnded](https://developer.apple.com/documentation/appkit/nsevent/phase/1529162-ended) when a Magic Mouse is in use.

To handle an event for a specific gesture—such as a rotation, pinching, or swipe movement—implement in your custom view the appropriate `NSResponder` method—that is, [rotateWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525572-rotatewithevent), [magnifyWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525862-magnifywithevent), or [swipeWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1524275-swipewithevent). Unlike the procedure for handling multitouch events, your custom view does not have to “opt-in”. When the mouse pointer is over your view and the user makes a gesture, the corresponding `NSResponder` method is called to handle the event. It is also called if the views earlier in the responder chain do not handle the event.

Each of the gesture-handling methods has an [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) parameter. You may query the event object for information pertinent to the gesture. For the recognized gestures, the following event-object attributes have special importance:

- Zoom in or out ([NSEventTypeMagnify](https://developer.apple.com/documentation/appkit/nsevent/eventtype/magnify))—The [magnification](https://developer.apple.com/documentation/appkit/nsevent/1531642-magnification) accessor method returns a floating-point (`CGFloat`) value representing a factor of magnification.
- Rotation ([NSEventTypeRotate](https://developer.apple.com/documentation/appkit/nsevent/eventtype/rotate))—The [rotation](https://developer.apple.com/documentation/appkit/nsevent/1526249-rotation) accessor method returns a floating-point value representing the degrees of rotation, counterclockwise.
- Swipe ([NSEventTypeSwipe](https://developer.apple.com/documentation/appkit/nseventtype/nseventtypeswipe))—The [deltaX](https://developer.apple.com/documentation/appkit/nsevent/1534871-deltax) and [deltaY](https://developer.apple.com/documentation/appkit/nsevent/1534158-deltay) accessor methods return the direction of the swipe as a floating-point (`CGFloat`) value. A non-zero `deltaX` value represents a horizontal swipe; -1 indicates a swipe-right and 1 indicates a swipe-left. A non-0 deltaY represent a vertical swipe; -1 indicates a swipe-down and 1 indicates a swipe-up.

The rotate and magnify gestures are relative events. That is, each [rotateWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525572-rotatewithevent) and [magnifyWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525862-magnifywithevent) message carries with it the change of rotation or magnification since the last gesture event of that type. For zooming in or out, you add the value from the `magnification` accessor to 1.0 to get the scale factor. For rotation, you add the newest degree of rotation to the view’s current rotation value. Listing 8-1 illustrates how you might do this.

__Listing 8-1__  Handling magnification and rotation gestures

```objc
- (void)magnifyWithEvent:(NSEvent *)event {
    [resultsField setStringValue:
        [NSString stringWithFormat:@"Magnification value is %f", [event magnification]]];
    NSSize newSize;
    newSize.height = self.frame.size.height * ([event magnification] + 1.0);
    newSize.width = self.frame.size.width * ([event magnification] + 1.0);
    [self setFrameSize:newSize];
}

- (void)rotateWithEvent:(NSEvent *)event {
    [resultsField setStringValue:
        [NSString stringWithFormat:@"Rotation in degree is %f", [event rotation]]];
    [self setFrameCenterRotation:([self frameCenterRotation] + [event rotation])];
}
```

To handle a swipe gesture simply requires you to determine the direction of swipe by analyzing the `deltaX` and `deltaY` values. The code in Listing 8-2 responds to swipes by setting a fill color for the implementing view.

__Listing 8-2__  Handling a swipe gesture

```objc
- (void)swipeWithEvent:(NSEvent *)event {
    CGFloat x = [event deltaX];
    CGFloat y = [event deltaY];
    if (x != 0) {
        swipeColorValue = (x > 0)  ? SwipeLeftGreen : SwipeRightBlue;
    }
    if (y != 0) {
        swipeColorValue = (y > 0)  ? SwipeUpRed : SwipeDownYellow;
    }
    NSString *direction;
    switch (swipeColorValue) {
        case SwipeLeftGreen:
            direction = @"left";
            break;
        case SwipeRightBlue:
            direction = @"right";
            break;
        case SwipeUpRed:
            direction = @"up";
            break;
        case SwipeDownYellow:
        default:
            direction = @"down";
            break;
    }
    [resultsField setStringValue:[NSString stringWithFormat:@"Swipe %@", direction]];
    [self setNeedsDisplay:YES];
}
```

You can also query the passed-in `NSEvent` object for other information related to the gesture event, including the location of the mouse pointer in window coordinates ([locationInWindow](https://developer.apple.com/documentation/appkit/nsevent/1529068-locationinwindow)), the timestamp of the event, and any modifier keys pressed by the user.

Because a gesture event is derived from a multitouch sequence, it might seem reasonable to query the `NSEvent` object for its touches by calling [touchesMatchingPhase:inView:](https://developer.apple.com/documentation/appkit/nsevent/1530950-touches). However, the returned [NSTouch](https://developer.apple.com/documentation/appkit/nstouch) objects might not be an accurate reflection of the touches currently in play. Thus you should not examine touch objects in the gesture-handling methods. The only reliable set of touch objects is returned in touch-event handling methods such as [touchesBeganWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1531151-touchesbegan). For more on these methods, see [Touch Events Represent Fingers on the Trackpad](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedcmznknltc).

As mentioned in [Types of Gesture Events and Gesture Sequences](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedcmznknlts), you can also use the [phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase) property of a gesture responder to perform actions such as coalescing all the gesture changes between start and end points of the gesture so that you can undo the complete sequence instead of just one step of the sequence.

If your custom view handles one of the API-supported gestures, your view’s implementation is called instead of any other implementation if your view is before the other object in the responder chain. However, there are certain system-wide gestures, such as a four-finger swipe, for which the system implementation takes precedence over any gesture handling an application performs.

Instead of handling a gesture, you could choose to track and handle the “raw” touches that make up the gesture. But why might you make such a choice? One obvious reason is that OS X does not recognize the particular gesture you are interested in—that is, something other than magnify (pinch in and out), rotate, or swipe. Or you want your view to respond to a system-supported gesture, but you want more information about the gesture than the AppKit framework currently provides; for example, you would like to have anchor points for a zooming operation. Unless you have reasons such as these, you should prefer gestures to raw touch events.

The following sections discuss the multitouch sequence that delimits a touch event in an abstract sense, point out important touch-event attributes, and show you how to handle touch events.

When a user touches a trackpad with one or more fingers and moves those fingers over the trackpad, the hardware generates low-level events that represent each of those fingers on the trackpad. The stream of events, as with all type of events, is continuous. However, there is a logical unit of touches that together, represent a _multitouch sequence_. A multitouch sequence begins when the user puts one or more fingers on the trackpad. The finger can move in various directions over the trackpad, and additional fingers may touch the trackpad. The multitouch sequence doesn’t end until all of those fingers are lifted from the trackpad.

Within a multitouch sequence, a finger on the trackpad typically goes through distinct phases:

- It touches down on the trackpad.
- It can move in various directions at various speeds.
- It can remain stationary.
- It lifts from the trackpad.

The AppKit framework uses objects of the `NSTouch` class to represent touches through the various phases of a multitouch sequence. That is, an `NSTouch` object is a snapshot of a particular finger—a touch—on the trackpad in a particular phase. For example, when a touch moves in a certain direction, the AppKit represents it with an `NSTouch` instance; it uses another `NSTouch` object to represent the same finger when it lifts from the trackpad.

Each touch object contains its phase as a property whose value is one of the `NSTouchPhase` constants shown in [Listing 8-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedcmznknlti). It also has an [identity](https://developer.apple.com/documentation/appkit/nstouch/1535399-identity) property that you use to track an `NSTouch` instance through a multitouch sequence. ([Touch Identity and Other Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedcmznknltk) describes touch identity in more detail.) Figure 8-2 illustrates a multitouch sequence and the role of these properties in this sequence.

__Figure 8-2__  Multitouch sequence on OS X

!!

AppKit attaches the touches in a multitouch sequence to the view that is under the mouse pointer when the first finger in the sequence touches down on the trackpad. A touch remains attached to this view until it has ended (that is, the finger lifts) or until the multitouch sequence is cancelled. Any interpretations of touches in a multitouch sequence must refer to that view, and that view only. You cannot have touches associated with different views in the same multitouch sequence. A touch, as represented by a `NSTouch` object, does not have a corresponding screen location or location in its view. But you can determine its changing positions on the trackpad, and from that map a delta value for transforming the view.

__Listing 8-3__  Constants for touch phases

```
enum {
    NSTouchPhaseBegan           = 1U << 0,
    NSTouchPhaseMoved           = 1U << 1,
    NSTouchPhaseStationary      = 1U << 2,
    NSTouchPhaseEnded           = 1U << 3,
    NSTouchPhaseCancelled       = 1U << 4,

    NSTouchPhaseTouching        = NSTouchPhaseBegan | NSTouchPhaseMoved | NSTouchPhaseStationary,
    NSTouchPhaseAny             = NSUIntegerMax
};
typedef NSUInteger NSTouchPhase;
```


The `NSTouch` defines a number of properties for its instances. A particularly important property is [identity](https://developer.apple.com/documentation/appkit/nstouch/1535399-identity). As you may recall from the previous discussion, an application creates an `NSTouch` object to represent the same finger on the trackpad for each phase it goes through in a multitouch sequence. Although these are different objects, they have the same [identity](https://developer.apple.com/documentation/appkit/nstouch/1535399-identity) object value, enabling you to track changes to a touch throughout a multitouch sequence. You can determine if two touch objects refer to a particular finger on the trackpad by comparing them with the [isEqual:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/isEqual:) method:

```
if ([previousTouchObject.identity isEqual:currentTouchObject.identity]) {
    // object refers to same finger on trackpad...do something appropriate
}
```

Both touch-identity objects and `NSTouch` objects themselves adopt the [NSCopying](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCopying/Description.html#//apple_ref/occ/intf/NSCopying) protocol. You can therefore copy them. This capability means you can use touch-identity objects as keys in [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) collections.

Two other important and related properties of `NSTouch` objects are [normalizedPosition](https://developer.apple.com/documentation/appkit/nstouch/1534031-normalizedposition) and [deviceSize](https://developer.apple.com/documentation/appkit/nstouch/1528476-devicesize). A touch has no visible location on the screen. (The mouse pointer only identifies the view that first receives touch events if it implements the required methods.) A touch does, however, have a position on the trackpad. The trackpad has a coordinate system defined by an origin of (0,0) in the lower-left corner of the trackpad and a height and width defined by `deviceSize`. Its position in this coordinate system is returned by `normalizedPosition`. Using these two properties you can derive delta values for touch movements and apply these to transformations of the manipulated view. This is illustrated in the code example in [Listing 8-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedcmznknlto).

The trackpad driver might identify one or more fingers (and thumb) as resting. This “resting” status means that the finger or thumb is physically on the digitizer, but the driver determines that it should not be used for input. For example, with the buttonless trackpads, a user may rest his or her thumb on the bottom section of the trackpad, just as one rests their arms on an arm rest. This digit is ignored as input, and its movement does not move the mouse pointer.

The driver might also transition a touch into or out of a resting status at any time, based on its evaluation. Movement of the resting finger or thumb is not always the determinant. A resting finger that moves might not necessarily transition out of "resting". On the other hand, a resting finger or thumb does not have to physically move at all to transition in and out of "resting".

Even if a touch is flagged as “resting” to denote that its should be ignored, the driver still generates touch data for it and sends an event to the application for each touch phase. By default, these events are not delivered to views and are not included in an event’s set of touches. However, you can turn on this capability by invoking the `NSView` method [setWantsRestingTouches:](https://developer.apple.com/documentation/appkit/nsview/1483594-wantsrestingtouches) with an argument of `YES`. If you are not accepting resting touches, be aware that [NSTouchPhaseBegan](https://developer.apple.com/documentation/appkit/nstouch/phase/1527407-began) and [NSTouchPhaseEnded](https://developer.apple.com/documentation/appkit/nstouchphase/nstouchphaseended) events are generated when a touch transitions from or to a resting state.

A view by default does not accept touch events. To handle touch events, your custom view must first call the `NSView` method [setAcceptsTouchEvents:](https://developer.apple.com/documentation/appkit/nsview/1483739-acceptstouchevents) with an argument of `YES`. Then your view must implement the `NSResponder` methods for touch-event handling:

```objc
- (void)touchesBeganWithEvent:(NSEvent *)event;
- (void)touchesMovedWithEvent:(NSEvent *)event;
- (void)touchesEndedWithEvent:(NSEvent *)event;
- (void)touchesCancelledWithEvent:(NSEvent *)event;
```

For custom subclass of [NSView](https://developer.apple.com/documentation/appkit/nsview), you should implement each of these methods. If you subclass an class that handles touches, you don’t need to implement all these methods methods, but you should call the superclass implementation in the methods you do override.

An application invokes each of these methods on the view when a touch enters a phase—that is, when a finger touches down, when it moves on the trackpad, when it lifts from the trackpad, and when the operating system cancels a multitouch sequence for some reason. More than one of these following methods could be called for the same event. The application first sends these messages to the view that is under the mouse pointer. If that view does not handle the event, the event is passed up the responder chain.

The single parameter of these responder methods is an [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) object. You can obtain the set of [NSTouch](https://developer.apple.com/documentation/appkit/nstouch) objects related to a given phase by sending a [touchesMatchingPhase:inView:](https://developer.apple.com/documentation/appkit/nsevent/1530950-touches) to the event object, passing in the constant for the phase. For example, in the [touchesBeganWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1531151-touchesbegan) method you can get touch objects representing fingers that have just touched down with a call similar to this:

```
NSSet *touches = [event touchesMatchingPhase:NSTouchPhaseBegan inView:self];
```

The operating system calls [touchesCancelledWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1530614-touchescancelledwithevent) when an external event—for example, application deactivation—interrupts the current multitouch sequence. You should implement the [touchesCancelledWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1530614-touchescancelledwithevent) method to free resources allocated for touch handling or to reset transient state used in touch handling to initial values.

The remaining code examples are taken from the _[LightTable](../../../samplecode/LightTable/LightTable.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojsg4)_ sample-code project. First, the project declares two static arrays to hold the initial touches and the current touches:

```
NSTouch *_initialTouches[2];
NSTouch *_currentTouches[2];
```

Listing 8-4 illustrates an implementation of the `touchesBeganWithEvent:` method. In this method, the view gets all touches associated with the event and, if there are two touches, stores them in the two static arrays.

__Listing 8-4__  Handling touches in `touchesBeganWithEvent:`

```objc
- (void)touchesBeganWithEvent:(NSEvent *)event {
    if (!self.isEnabled) return;

    NSSet *touches = [event touchesMatchingPhase:NSTouchPhaseTouching inView:self.view];

    if (touches.count == 2) {
        self.initialPoint = [self.view convertPointFromBase:[event locationInWindow]];
        NSArray *array = [touches allObjects];
        _initialTouches[0] = [[array objectAtIndex:0] retain];
        _initialTouches[1] = [[array objectAtIndex:1] retain];
        _currentTouches[0] = [_initialTouches[0] retain];
        _currentTouches[1] = [_initialTouches[1] retain];
    } else if (touches.count > 2) {
        // More than 2 touches. Only track 2.
        if (self.isTracking) {
            [self cancelTracking];
        } else {
            [self releaseTouches];
        }
    }
}
```

When one or both of the fingers move, the [touchesMovedWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1524501-touchesmovedwithevent) method is invoked. The view in `LightTable` implements this method as shown in Listing 8-5. Again, it gets all the touch objects associated with the event and, if there are exactly two touches, it matches the current touches with their initial counterparts. Then it computes the delta values for origin and size and, if these exceed a certain threshold, invokes an action method to perform the transformation.

__Listing 8-5__  Handling touches in `touchesMovedWithEvent:`

```objc
- (void)touchesMovedWithEvent:(NSEvent *)event {
    if (!self.isEnabled) return;
    self.modifiers = [event modifierFlags];
    NSSet *touches = [event touchesMatchingPhase:NSTouchPhaseTouching inView:self.view];
    if (touches.count == 2 && _initialTouches[0]) {
        NSArray *array = [touches allObjects];
        [_currentTouches[0] release];
        [_currentTouches[1] release];

        NSTouch *touch;
        touch = [array objectAtIndex:0];
        if ([touch.identity isEqual:_initialTouches[0].identity]) {
            _currentTouches[0] = [touch retain];
        } else {
            _currentTouches[1] = [touch retain];
        }
        touch = [array objectAtIndex:1];
        if ([touch.identity isEqual:_initialTouches[0].identity]) {
            _currentTouches[0] = [touch retain];
        } else {
            _currentTouches[1] = [touch retain];
        }
        if (!self.isTracking) {
            NSPoint deltaOrigin = self.deltaOrigin;
            NSSize  deltaSize = self.deltaSize;
            if (fabs(deltaOrigin.x) > _threshold ||
                fabs(deltaOrigin.y) > _threshold ||
                fabs(deltaSize.width) > _threshold ||
                fabs(deltaSize.height) > _threshold) {
                self.isTracking = YES;
                if (self.beginTrackingAction)
                    [NSApp sendAction:self.beginTrackingAction to:self.view from:self];
            }
        } else {
            if (self.updateTrackingAction)
                [NSApp sendAction:self.updateTrackingAction to:self.view from:self];
        }
    }
}
```

Listing 8-6 shows how the project computes the delta values for transforming the origin of the view. Note how the code uses values from the `NSTouch` properties [normalizedPosition](https://developer.apple.com/documentation/appkit/nstouch/1534031-normalizedposition) and [deviceSize](https://developer.apple.com/documentation/appkit/nstouch/1528476-devicesize) in this computation.

__Listing 8-6__  Obtaining a delta value using `normalizedPosition` and `deviceSize`

```objc
- (NSPoint)deltaOrigin {
    if (!(_initialTouches[0] && _initialTouches[1] &&
        _currentTouches[0] && _currentTouches[1])) return NSZeroPoint;

    CGFloat x1 = MIN(_initialTouches[0].normalizedPosition.x, _initialTouches[1].normalizedPosition.x);
    CGFloat x2 = MAX(_currentTouches[0].normalizedPosition.x, _currentTouches[1].normalizedPosition.x);
    CGFloat y1 = MIN(_initialTouches[0].normalizedPosition.y, _initialTouches[1].normalizedPosition.y);
    CGFloat y2 = MAX(_currentTouches[0].normalizedPosition.y, _currentTouches[1].normalizedPosition.y);

    NSSize deviceSize = _initialTouches[0].deviceSize;
    NSPoint delta;
    delta.x = (x2 - x1) * deviceSize.width;
    delta.y = (y2 - y1) * deviceSize.height;
    return delta;
}
```

Finally, the view implements the [touchesEndedWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1525779-touchesendedwithevent) and [touchesCancelledWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1530614-touchescancelledwithevent) methods, as shown in Listing 8-7, primarily to cancel tracking of the event.

__Listing 8-7__  Handling ending and cancelled touches

```objc
- (void)touchesEndedWithEvent:(NSEvent *)event {
    if (!self.isEnabled) return;
    self.modifiers = [event modifierFlags];
    [self cancelTracking];
}

- (void)touchesCancelledWithEvent:(NSEvent *)event {
    [self cancelTracking];
}
```

Para

The operating system interprets a single finger moving across the trackpad as a mouse-tracking event, and moves the mouse pointer in a corresponding speed and direction. The single-finger movement generates both gesture events and mouse events, although the gesture events are ignored unless the view accepts touches. Movements of more than one finger on the trackpad do not move the pointer, although they may still result in the generation of mouse events used in scrolling. An exception to this is a buttonless trackpad, where two fingers may be physically touching the trackpad while the pointer is moving because one of them is resting.

If a mouse event is generated by a touch event, the subtype of the mouse event is [NSTouchEventSubtype](https://developer.apple.com/documentation/appkit/nstoucheventsubtype). You could evaluate mouse-event objects to determine when to ignore mouse events in favor of touch events when both are generated. (This advice is not applicable to scroll wheel events.)

You should not attempt to extract touches from a mouse event using the [touchesMatchingPhase:inView:](https://developer.apple.com/documentation/appkit/nsevent/1530950-touches) method. Although you can check the subtype of the event object to see if a touch generated the mouse event, you cannot correlate the mouse event to any particular touch. Further, you cannot query a touch event to find out if it also generated a mouse event.

[Next](Monitoring%20Events.md)[Previous](Handling%20Tablet%20Events.md)

