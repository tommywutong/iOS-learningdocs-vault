---
title: NSAppleEventManager
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventmanager
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager.json'
content_hash: 'sha256:1953421f7b6d2cd2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAppleEventManager

<sub>Class</sub>

A mechanism for registering handler routines for specific types of Apple events and dispatching events to those handlers.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSAppleEventManager
```

## Overview

Cocoa provides built-in scriptability support that uses scriptability information supplied by an application to automatically convert Apple events into script command objects that perform the desired operation. However, some applications may want to perform more basic Apple event handling, in which an application registers handlers for the Apple events it can process, then calls on the Apple Event Manager to dispatch received Apple events to the appropriate handler. `NSAppleEventManager` supports these mechanisms by providing methods to register and remove handlers and to dispatch Apple events to the appropriate handler, if one exists. For related information, see [How Cocoa Applications Handle Apple Events](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239)

Each application has at most one instance of `NSAppleEventManager`. To obtain a reference to it, you call the class method [+ sharedAppleEventManager](<nsappleeventmanager/shared().md>), which creates the instance if it doesn’t already exist.

For information about the Apple Event Manager, see [Apple Event Manager](../applicationservices/apple_event_manager.md) and Apple Events Programming Guide.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting an event manager

- [+ sharedAppleEventManager](<nsappleeventmanager/shared().md>) — Returns the single instance of `NSAppleEventManager`, creating it first if it doesn’t exist.

### Working with event handlers

- [- removeEventHandlerForEventClass:andEventID:](<nsappleeventmanager/removeeventhandler(foreventclass_andeventid_).md>) — If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.
- [- setEventHandler:andSelector:forEventClass:andEventID:](<nsappleeventmanager/seteventhandler(__andselector_foreventclass_andeventid_).md>) — Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.

### Working with events

- [- dispatchRawAppleEvent:withRawReply:handlerRefCon:](<nsappleeventmanager/dispatchrawappleevent(__withrawreply_handlerrefcon_).md>) — Causes the Apple event specified by `theAppleEvent` to be dispatched to the appropriate Apple event handler, if one has been registered by calling [- setEventHandler:andSelector:forEventClass:andEventID:](<nsappleeventmanager/seteventhandler(__andselector_foreventclass_andeventid_).md>).

### Suspending and resuming Apple events

- [- appleEventForSuspensionID:](<nsappleeventmanager/appleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<nsappleeventmanager/suspendcurrentappleevent().md>), returns the descriptor for the event whose handling was suspended.
- [currentAppleEvent](nsappleeventmanager/currentappleevent.md) — Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [currentReplyAppleEvent](nsappleeventmanager/currentreplyappleevent.md) — Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [- replyAppleEventForSuspensionID:](<nsappleeventmanager/replyappleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<nsappleeventmanager/suspendcurrentappleevent().md>), returns the corresponding reply event descriptor.
- [- resumeWithSuspensionID:](<nsappleeventmanager/resume(withsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<nsappleeventmanager/suspendcurrentappleevent().md>), signal that handling of the suspended event may now continue.
- [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<nsappleeventmanager/setcurrentappleeventandreplyeventwithsuspensionid(__).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<nsappleeventmanager/suspendcurrentappleevent().md>), sets the values that will be returned by subsequent invocations of [currentAppleEvent](nsappleeventmanager/currentappleevent.md) and [currentReplyAppleEvent](nsappleeventmanager/currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [- suspendCurrentAppleEvent](<nsappleeventmanager/suspendcurrentappleevent().md>) — Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [SuspensionID](nsappleeventmanager/suspensionid.md) — Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.

### Constants

- [NSAppleEvent Timeouts](nsappleevent-timeouts.md) — The following constants should not be used and may eventually be removed.

## See Also

### Apple Event Handling

- [NSAppleEventDescriptor](nsappleeventdescriptor.md) — A wrapper for the Apple event descriptor data type.
