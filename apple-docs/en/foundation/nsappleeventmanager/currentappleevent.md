---
title: currentAppleEvent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventmanager/currentappleevent
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/currentappleevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/currentappleevent.json'
content_hash: 'sha256:a90e35a652b9bb6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# currentAppleEvent

<sub>Instance Property</sub>

Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.

<sub>Mac Catalyst, macOS</sub>

```swift
var currentAppleEvent: NSAppleEventDescriptor? { get }
```

## Discussion

An Apple event is being handled on the current thread if a handler that was registered with [- setEventHandler:andSelector:forEventClass:andEventID:](<seteventhandler(__andselector_foreventclass_andeventid_).md>) is being messaged at this instant or [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) has just been invoked. Returns `nil` otherwise. The effects of mutating or retaining the returned descriptor are undefined, although it may be copied.

## See Also

### Suspending and resuming Apple events

- [- appleEventForSuspensionID:](<appleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the descriptor for the event whose handling was suspended.
- [currentReplyAppleEvent](currentreplyappleevent.md) — Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [- replyAppleEventForSuspensionID:](<replyappleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the corresponding reply event descriptor.
- [- resumeWithSuspensionID:](<resume(withsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), signal that handling of the suspended event may now continue.
- [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), sets the values that will be returned by subsequent invocations of [currentAppleEvent](currentappleevent.md) and [currentReplyAppleEvent](currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) — Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [SuspensionID](suspensionid.md) — Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.
