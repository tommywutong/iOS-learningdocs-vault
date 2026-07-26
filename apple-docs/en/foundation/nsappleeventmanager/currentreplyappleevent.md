---
title: currentReplyAppleEvent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventmanager/currentreplyappleevent
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/currentreplyappleevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/currentreplyappleevent.json'
content_hash: 'sha256:a3a5692d69e84c4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# currentReplyAppleEvent

<sub>Instance Property</sub>

Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.

<sub>Mac Catalyst, macOS</sub>

```swift
var currentReplyAppleEvent: NSAppleEventDescriptor? { get }
```

## Discussion

An Apple event is being handled on the current thread if [currentAppleEvent](currentappleevent.md) does not return `nil`. Returns `nil` otherwise. This descriptor, including any mutations, will be returned to the sender of the current event when all handling of the event has been completed, if the sender has requested a reply. The effects of retaining the descriptor are undefined; it may be copied, but mutations of the copy are not returned to the sender of the current event.

## See Also

### Suspending and resuming Apple events

- [- appleEventForSuspensionID:](<appleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the descriptor for the event whose handling was suspended.
- [currentAppleEvent](currentappleevent.md) — Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [- replyAppleEventForSuspensionID:](<replyappleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the corresponding reply event descriptor.
- [- resumeWithSuspensionID:](<resume(withsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), signal that handling of the suspended event may now continue.
- [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), sets the values that will be returned by subsequent invocations of [currentAppleEvent](currentappleevent.md) and [currentReplyAppleEvent](currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) — Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [SuspensionID](suspensionid.md) — Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.
