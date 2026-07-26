---
title: Quartz Event Services
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/quartz-event-services
source_url: 'https://developer.apple.com/documentation/coregraphics/quartz-event-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/quartz-event-services.json'
content_hash: 'sha256:0b4364afc5ca4956'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# Quartz Event Services

<sub>API Collection</sub>

Provides features for managing _event taps_—filters for observing and altering the stream of low-level user input events in macOS.

## Overview

Event taps make it possible to monitor and filter input events from several points within the system, prior to their delivery to a foreground application. Event taps complement and extend the capabilities of the Carbon event monitor mechanism, which allows an application to observe input events delivered to other processes.

Event taps are designed to serve as a Section 508 enabling technology. For example, consider a software system to assist a person with language impairments, designed to perform keyboard filtering with spoken review. Such a system could use an event tap to monitor all keystrokes, perform dictionary checks and matches, and recite the assembled word back to the user on detection of a word break in the input stream. If acceptable to the user, as indicated by an additional input keystroke or other gesture, the events would be posted into the system for delivery to the foreground application.

Introduced in OS X version 10.4, event taps provide functionality similar to the Win32 functions `SetWinEventHook` when used to establish an out-of-context event hook, and `SendInput`. Quartz Event Services also includes an older set of event-related functions declared in the file `CGRemoteOperation.h`. These functions are still supported, but they are not recommended for new development.

## Topics

### Working With Events

- [CGEventGetTypeID](cgevent/typeid.md) — Returns the type identifier for the opaque type `CGEventRef`.
- [CGEventCreate](<cgevent/init(source_).md>) — Returns a new Quartz event.
- [CGEventCreateFromData](<cgevent/init(withdataallocator_data_).md>) — Returns a Quartz event created from a flattened data representation of the event.
- [CGEventCreateMouseEvent](<cgevent/init(mouseeventsource_mousetype_mousecursorposition_mousebutton_).md>) — Returns a new Quartz mouse event.
- [CGEventCreateKeyboardEvent](<cgevent/init(keyboardeventsource_virtualkey_keydown_).md>) — Returns a new Quartz keyboard event.
- [CGEventCreateCopy](<cgevent/copy().md>) — Returns a copy of an existing Quartz event.
- [CGEventCreateSourceFromEvent](<cgeventsource/init(event_).md>) — Returns a Quartz event source created from an existing Quartz event.
- [CGEventSetSource](<cgevent/setsource(__).md>) — Sets the event source of a Quartz event.
- [CGEventGetType](cgevent/type.md) — Returns the event type of a Quartz event (left mouse down, for example).
- [CGEventGetTimestamp](cgevent/timestamp.md) — Returns the timestamp of a Quartz event.
- [CGEventGetLocation](cgevent/location.md) — Returns the location of a Quartz mouse event.
- [CGEventGetUnflippedLocation](cgevent/unflippedlocation.md) — Returns the location of a Quartz mouse event.
- [CGEventGetFlags](cgevent/flags.md) — Returns the event flags of a Quartz event.
- [CGEventKeyboardGetUnicodeString](<cgevent/keyboardgetunicodestring(maxstringlength_actualstringlength_unicodestring_).md>) — Returns the Unicode string associated with a Quartz keyboard event.
- [CGEventKeyboardSetUnicodeString](<cgevent/keyboardsetunicodestring(stringlength_unicodestring_).md>) — Sets the Unicode string associated with a Quartz keyboard event.
- [CGEventGetIntegerValueField](<cgevent/getintegervaluefield(__).md>) — Returns the integer value of a field in a Quartz event.
- [CGEventSetIntegerValueField](<cgevent/setintegervaluefield(__value_).md>) — Sets the integer value of a field in a Quartz event.
- [CGEventGetDoubleValueField](<cgevent/getdoublevaluefield(__).md>) — Returns the floating-point value of a field in a Quartz event.
- [CGEventSetDoubleValueField](<cgevent/setdoublevaluefield(__value_).md>) — Sets the floating-point value of a field in a Quartz event.

### Working With Event Taps

- [CGEventTapCreate](<cgevent/tapcreate(tap_place_options_eventsofinterest_callback_userinfo_).md>) — Creates an event tap.
- [CGEventTapCreateForPSN](<cgevent/tapcreateforpsn(processserialnumber_place_options_eventsofinterest_callback_userinfo_).md>) — Creates an event tap for a specified process.
- [CGEventTapEnable](<cgevent/tapenable(tap_enable_).md>) — Enables or disables an event tap.
- [CGEventTapIsEnabled](<cgevent/tapisenabled(tap_).md>) — Returns a Boolean value indicating whether an event tap is enabled.
- [CGEventTapPostEvent](<cgevent/tappostevent(__).md>) — Posts a Quartz event from an event tap into the event stream.
- [CGEventPost](<cgevent/post(tap_).md>) — Posts a Quartz event into the event stream at a specified location.
- [CGEventPostToPSN](<cgevent/posttopsn(processserialnumber_).md>) — Posts a Quartz event into the event stream for a specific application.
- [CGGetEventTapList](<cggeteventtaplist(______).md>) — Gets a list of currently installed event taps.

### Working With Event Sources

- [CGEventSourceGetTypeID](cgeventsource/typeid.md) — Returns the type identifier for the opaque type `CGEventSourceRef`.
- [CGEventSourceCreate](<cgeventsource/init(stateid_).md>) — Returns a Quartz event source created with a specified source state.
- [CGEventSourceGetKeyboardType](cgeventsource/keyboardtype.md) — Returns the keyboard type to be used with a Quartz event source.
- [CGEventSourceGetSourceStateID](cgeventsource/sourcestateid.md) — Returns the source state associated with a Quartz event source.
- [CGEventSourceButtonState](<cgeventsource/buttonstate(__button_).md>) — Returns a Boolean value indicating the current button state of a Quartz event source.
- [CGEventSourceKeyState](<cgeventsource/keystate(__key_).md>) — Returns a Boolean value indicating the current keyboard state of a Quartz event source.
- [CGEventSourceFlagsState](<cgeventsource/flagsstate(__).md>) — Returns the current flags of a Quartz event source.
- [CGEventSourceSecondsSinceLastEventType](<cgeventsource/secondssincelasteventtype(__eventtype_).md>) — Returns the elapsed time since the last event for a Quartz event source.
- [CGEventSourceCounterForEventType](<cgeventsource/counterforeventtype(__eventtype_).md>) — Returns a count of events of a given type seen since the window server started.
- [CGEventSourceGetUserData](cgeventsource/userdata.md) — Returns the 64-bit user-specified data for a Quartz event source.
- [CGEventSourceGetLocalEventsFilterDuringSuppressionState](<cgeventsource/getlocaleventsfilterduringsuppressionstate(__).md>) — Returns the mask that indicates which classes of local hardware events are enabled during event suppression.
- [CGEventSourceSetLocalEventsFilterDuringSuppressionState](<cgeventsource/setlocaleventsfilterduringsuppressionstate(__state_).md>) — Sets the mask that indicates which classes of local hardware events are enabled during event suppression.
- [CGEventSourceGetLocalEventsSuppressionInterval](cgeventsource/localeventssuppressioninterval.md) — Returns the interval that local hardware events may be suppressed following the posting of a Quartz event.
- [CGEventSourceGetPixelsPerLine](cgeventsource/pixelsperline.md) — Gets the scale of pixels per line in a scrolling event source.

### Callbacks

- [CGEventTapCallBack](cgeventtapcallback.md) — A client-supplied callback function that’s invoked whenever an associated event tap receives a Quartz event.

### Data Types

- [CGButtonCount](cgbuttoncount.md) — Represents the number of buttons being set in a synthetic mouse event.
- [CGCharCode](cgcharcode.md) — Represents a character generated by pressing one or more keys on a keyboard.
- [CGEventMask](cgeventmask.md) — Defines a mask that identifies the set of Quartz events to be observed in an event tap.
- [CGEvent](cgevent.md) — Defines an opaque type that represents a low-level hardware event.
- [CGEventSourceKeyboardType](cgeventsourcekeyboardtype.md) — Defines a code that represents the type of keyboard used with a specified event source.
- [CGEventSource](cgeventsource.md) — Defines an opaque type that represents the source of a Quartz event.
- [CGEventTapInformation](cgeventtapinformation.md) — Defines the structure used to report information about event taps.
- [CGEventTapProxy](cgeventtapproxy.md) — Defines an opaque type that represents state within the client application that’s associated with an event tap.
- [CGEventTimestamp](cgeventtimestamp.md) — Defines the elapsed time in nanoseconds since startup that a Quartz event occurred.
- [CGKeyCode](cgkeycode.md) — Represents the virtual key codes used in keyboard events.
- [CGWheelCount](cgwheelcount.md) — Represents the number of wheels being set in a scroll wheel event.

### Constants

- [CGEventField](cgeventfield.md) — Constants used as keys to access specialized fields in low-level events.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [Event Source Token](event-source-token.md) — Specifies any input event type.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
- [CGEventTapPlacement](cgeventtapplacement.md) — Constants that specify where a new event tap is inserted into the list of active event taps.
- [CGEventType](cgeventtype.md) — Constants that specify the different types of input events.
- [Event Type Mask](event-type-mask.md) — Specifies an event mask that represents all event types.
- [CGMouseButton](cgmousebutton.md) — Constants that specify buttons on a one, two, or three-button mouse.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGScrollEventUnit](cgscrolleventunit.md) — Constants that specify the unit of measurement for a scrolling event.

### Deprecated Functions

- [CGPostKeyboardEvent](<cgpostkeyboardevent(______).md>) — Synthesizes a low-level keyboard event on the local machine. _(deprecated)_
- [CGEnableEventStateCombining](<cgenableeventstatecombining(__).md>) — Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event. _(deprecated)_
- [CGInhibitLocalEvents](<cginhibitlocalevents(__).md>) — Turns off local hardware events in the current session. _(deprecated)_
- [CGSetLocalEventsFilterDuringSuppressionState](<cgsetlocaleventsfilterduringsuppressionstate(____).md>) — Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted. _(deprecated)_
- [CGSetLocalEventsSuppressionInterval](<cgsetlocaleventssuppressioninterval(__).md>) — Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event. _(deprecated)_

## See Also

### Services

- [Quartz Display Services](quartz-display-services.md) — Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- [Quartz Window Services](quartz-window-services.md) — Provides information about the windows managed by the macOS window server.
