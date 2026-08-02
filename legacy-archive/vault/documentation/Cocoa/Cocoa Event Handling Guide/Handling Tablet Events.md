---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/HandlingTabletEvents/HandlingTabletEvents.html
archived_at: '2026-07-15T07:15:35.477285Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Handling%20Trackpad%20Events.md)[Previous](Using%20Tracking-Area%20Objects.md)

# Handling Tablet Events

The following sections discuss issues related to the handling of tablet events.

Tablet device drivers package low-level events as either native tablet events or as mouse events, usually depending on whether they are proximity events or pointer events. Proximity events are always native tablet events. The Application Kit declares (in `NSEvent.h`) the following event-type constants for native tablet events:

```
typedef enum _NSEventType {
    // ...
    NSTabletPoint     = 23,
    NSTabletProximity = 24,
    // ...
} NSEventType;
```

Drivers almost always package tablet-pointer events as subtypes of mouse events. The Application Kit declares the following constants for tablet subtypes of all event types related to mouse event (`NSLeftMouseDown`, `NSRightMouseUp`, `NSMouseMoved`, and so on):

```
enum {
    NSMouseEventSubtype           = NX_SUBTYPE_DEFAULT,
    NSTabletPointEventSubtype      = NX_SUBTYPE_TABLET_POINT,
    NSTabletProximityEventSubtype = NX_SUBTYPE_TABLET_PROXIMITY
};
```

Under a few exceptional conditions drivers may package a low-level tablet-pointer event as a `NSTabletPoint` event type instead of a mouse-event subtype. These include the following:

- During the interval between a mouse-down (that is, stylus-down) and subsequent dragging events when, for example, only pressure is changing.
- When there are two concurrently active pointing devices, the one not moving the cursor generates `NSTabletPoint` events.
- If, for some reason, the tablet driver is told not to move the cursor, the driver packages tablet events in native form.

For this reason, it is recommended that your code check for tablet-pointer events delivered both as native event types and as mouse subtypes.

Like any NSEvent object, tablet events are routed up the responder chain until they are handled. Responder objects in an application (that is, objects that inherit from NSResponder) can override the appropriate NSResponder methods and handle the NSEvent object that is passed to them in that method. Or they can pass the event on to the next responder in the chain. (If you don’t override one of these method, the event automatically goes to the next responder.

An application that intends to handle tablet events should override at least five NSResponder methods:

- `tabletProximity:` and `tabletPoint:`

  Implement these methods to handle native proximity and pointer tablet events.
- `mouseDown:`, `mouseDragged:`, and `mouseUp:`

  implement these methods to handle mouse events with a subtype of `NSTabletPointEventSubtype` or `NSTabletProximityEventSubtype`.

A recommended approach is to funnel tablet events in these methods to two common handlers, one for proximity events and the other for pointer events. If you have objects in your application that are not in the responder chain and you want these objects to know about tablet events as they arrive, you could implement your event-handler routine so that it posts a notification to all interested observers.

[Next](Handling%20Trackpad%20Events.md)[Previous](Using%20Tracking-Area%20Objects.md)

