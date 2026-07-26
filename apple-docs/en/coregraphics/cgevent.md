---
title: CGEvent
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgevent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgevent.json'
content_hash: 'sha256:800266f37d87000a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEvent

<sub>Class</sub>

Defines an opaque type that represents a low-level hardware event.

<sub>Mac Catalyst, macOS</sub>

```swift
class CGEvent
```

## Overview

Low-level hardware events of this type are referred to as Quartz events. A typical event in macOS originates when the user manipulates an input device such as a mouse or a keyboard. The device driver associated with that device, through the I/O Kit, creates a low-level event, puts it in the window server’s event queue, and notifies the window server. The window server creates a Quartz event, annotates the event, and dispatches the event to the appropriate run-loop port of the target process. There the event is picked up by the Carbon Event Manager and forwarded to the event-handling mechanism appropriate to the application environment. You can use event taps to gain access to Quartz events at several different steps in this process.

This opaque type is derived from CFType and inherits the properties that all Core Foundation types have in common. For more information, see [CFTypeRef](../corefoundation/cftyperef.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Initializers

- [CGEventCreateCopy](<cgevent/copy().md>) — Returns a copy of an existing Quartz event.
- [CGEventCreateKeyboardEvent](<cgevent/init(keyboardeventsource_virtualkey_keydown_).md>) — Returns a new Quartz keyboard event.
- [CGEventCreateMouseEvent](<cgevent/init(mouseeventsource_mousetype_mousecursorposition_mousebutton_).md>) — Returns a new Quartz mouse event.
- [CGEventCreate](<cgevent/init(source_).md>) — Returns a new Quartz event.
- [CGEventCreateFromData](<cgevent/init(withdataallocator_data_).md>) — Returns a Quartz event created from a flattened data representation of the event.
- [CGEventCreateScrollWheelEvent2](<cgevent/init(scrollwheelevent2source_units_wheelcount_wheel1_wheel2_wheel3_).md>)

### Instance Properties

- [CGEventGetFlags](cgevent/flags.md) — Returns the event flags of a Quartz event.
- [CGEventGetLocation](cgevent/location.md) — Returns the location of a Quartz mouse event.
- [CGEventGetTimestamp](cgevent/timestamp.md) — Returns the timestamp of a Quartz event.
- [CGEventGetType](cgevent/type.md) — Returns the event type of a Quartz event (left mouse down, for example).
- [CGEventGetUnflippedLocation](cgevent/unflippedlocation.md) — Returns the location of a Quartz mouse event.
- [data](cgevent/data.md)

### Type Properties

- [CGEventGetTypeID](cgevent/typeid.md) — Returns the type identifier for the opaque type `CGEventRef`.

### Instance Methods

- [CGEventGetDoubleValueField](<cgevent/getdoublevaluefield(__).md>) — Returns the floating-point value of a field in a Quartz event.
- [CGEventGetIntegerValueField](<cgevent/getintegervaluefield(__).md>) — Returns the integer value of a field in a Quartz event.
- [CGEventKeyboardGetUnicodeString](<cgevent/keyboardgetunicodestring(maxstringlength_actualstringlength_unicodestring_).md>) — Returns the Unicode string associated with a Quartz keyboard event.
- [CGEventKeyboardSetUnicodeString](<cgevent/keyboardsetunicodestring(stringlength_unicodestring_).md>) — Sets the Unicode string associated with a Quartz keyboard event.
- [CGEventPost](<cgevent/post(tap_).md>) — Posts a Quartz event into the event stream at a specified location.
- [CGEventPostToPSN](<cgevent/posttopsn(processserialnumber_).md>) — Posts a Quartz event into the event stream for a specific application.
- [CGEventPostToPid](<cgevent/posttopid(__).md>)
- [CGEventSetDoubleValueField](<cgevent/setdoublevaluefield(__value_).md>) — Sets the floating-point value of a field in a Quartz event.
- [CGEventSetIntegerValueField](<cgevent/setintegervaluefield(__value_).md>) — Sets the integer value of a field in a Quartz event.
- [CGEventSetSource](<cgevent/setsource(__).md>) — Sets the event source of a Quartz event.
- [CGEventTapPostEvent](<cgevent/tappostevent(__).md>) — Posts a Quartz event from an event tap into the event stream.

### Type Methods

- [CGEventTapCreate](<cgevent/tapcreate(tap_place_options_eventsofinterest_callback_userinfo_).md>) — Creates an event tap.
- [CGEventTapCreateForPSN](<cgevent/tapcreateforpsn(processserialnumber_place_options_eventsofinterest_callback_userinfo_).md>) — Creates an event tap for a specified process.
- [CGEventTapCreateForPid](<cgevent/tapcreateforpid(pid_place_options_eventsofinterest_callback_userinfo_).md>)
- [CGEventTapEnable](<cgevent/tapenable(tap_enable_).md>) — Enables or disables an event tap.
- [CGEventTapIsEnabled](<cgevent/tapisenabled(tap_).md>) — Returns a Boolean value indicating whether an event tap is enabled.

## See Also

### Data Types

- [CGButtonCount](cgbuttoncount.md) — Represents the number of buttons being set in a synthetic mouse event.
- [CGCharCode](cgcharcode.md) — Represents a character generated by pressing one or more keys on a keyboard.
- [CGDirectDisplayID](cgdirectdisplayid.md) — A unique identifier for an attached display.
- [CGDisplayBlendFraction](cgdisplayblendfraction.md) — The percentage of blend color used in a fade operation.
- [CGDisplayConfigRef](cgdisplayconfigref.md) — A reference to a display configuration transaction.
- [CGDisplayCount](cgdisplaycount.md) — The number of displays in various lists. _(deprecated)_
- [CGDisplayErr](cgdisplayerr.md) — A uniform type for result codes returned by functions in Quartz Display Services. _(deprecated)_
- [CGDisplayFadeInterval](cgdisplayfadeinterval.md) — The duration in seconds of a fade operation or a fade hardware reservation.
- [CGDisplayFadeReservationToken](cgdisplayfadereservationtoken.md) — A token issued by Quartz when reserving one or more displays for a fade operation during a specified interval.
- [CGDisplayMode](cgdisplaymode.md) — A reference to a display mode object.
- [CGDisplayReconfigurationCallBack](cgdisplayreconfigurationcallback.md) — A client-supplied callback function that’s invoked whenever the configuration of a local display is changed.
- [CGDisplayReservationInterval](cgdisplayreservationinterval.md) — The time interval for a fade reservation.
- [CGDisplayStream](cgdisplaystream.md) — A reference to a display stream object.
- [CGDisplayStreamFrameAvailableHandler](cgdisplaystreamframeavailablehandler.md) — A block called when a data stream has a new frame event to process.
- [CGDisplayStreamUpdate](cgdisplaystreamupdate.md) — A reference to frame update’s metadata.
