---
title: UIEvent
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent
source_url: 'https://developer.apple.com/documentation/uikit/uievent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent.json'
content_hash: 'sha256:aaf993ecea1ef7ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEvent

<sub>Class</sub>

An object that describes a single user interaction with your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIEvent
```

## Overview

Apps can receive many different types of events, including touch events, motion events, remote-control events, and press events. Touch events are the most common and are delivered to the view in which the touch originally occurred. Motion events are UIKit triggered and are separate from the motion events reported by the Core Motion framework. Remote-control events allow a responder object to receive commands from an external accessory or headset so that it can manage audio and video — for example, playing a video or skipping to the next audio track. Press events represent interactions with a game controller, Apple TV remote, or other device that has physical buttons. You can determine the type of an event using the [type](uievent/type.md) and [subtype](uievent/subtype.md) properties.

A touch event object contains the touches (that is, the fingers on the screen) that have some relation to the event. A touch event object may contain one or more touches, and each touch is represented by a [UITouch](uitouch.md) object. When a touch event occurs, the system routes it to the appropriate responder and calls the appropriate method, such as [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>). The responder then uses the touches to determine an appropriate course of action.

During a multitouch sequence, UIKit reuses the same [UIEvent](uievent.md) object when delivering updated touch data to your app. You should never retain an event object or any object returned from an event object. If you need to retain data outside of the responder method you use to process that data, copy that data from the [UITouch](uitouch.md) or [UIEvent](uievent.md) object to your local data structures.

For more information on how to handle events in your UIKit app, see [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIPressesEvent](uipressesevent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the touches for an event

- [allTouches](uievent/alltouches.md) — All touches associated with the event.
- [- touchesForView:](<uievent/touches(for_)-9neb4.md>) — Returns the touch objects from the event that belong to the specified given view.
- [- touchesForWindow:](<uievent/touches(for_)-767rm.md>) — Returns the touch objects from the event that belong to the specified window.
- [- coalescedTouchesForTouch:](<uievent/coalescedtouches(for_).md>) — Returns all of the touches associated with the specified main touch.
- [- predictedTouchesForTouch:](<uievent/predictedtouches(for_).md>) — Returns an array of touches that are predicted to occur for the specified touch.

### Getting event attributes

- [timestamp](uievent/timestamp.md) — The time when the event occurred.

### Getting the event type

- [type](uievent/type.md) — Returns the type of the event.
- [EventType](uievent/eventtype.md) — Constants that specify the general type of an event.
- [subtype](uievent/subtype.md) — Returns the subtype of the event.
- [EventSubtype](uievent/eventsubtype.md) — Constants that specify the subtype of the event in relation to its general type.

### Getting the touches for a gesture recognizer

- [- touchesForGestureRecognizer:](<uievent/touches(for_)-6krou.md>) — Returns the touch objects that are being delivered to the specified gesture recognizer.

### Getting the button mask

- [buttonMask](uievent/buttonmask-swift.property.md) — A bit mask that represents which input-device buttons are pressed for the current event.
- [ButtonMask](uievent/buttonmask-swift.struct.md) — Constants that indicate which input-device buttons are pressed.

### Getting the modifier flags

- [modifierFlags](uievent/modifierflags.md) — The set of modifier keys that are pressed for the current event.
- [UIKeyModifierFlags](uikeymodifierflags.md) — Constants that indicate which modifier keys are pressed.

## See Also

### Essentials

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md) — Learn how to handle events that propagate through your app.
- [UIResponder](uiresponder.md) — An abstract interface for responding to and handling events.
