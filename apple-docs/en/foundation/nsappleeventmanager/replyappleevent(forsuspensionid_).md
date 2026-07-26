---
title: 'replyAppleEvent(forSuspensionID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventmanager/replyappleevent(forsuspensionid:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/replyappleevent(forsuspensionid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/replyappleevent%28forsuspensionid%3A%29.json'
content_hash: 'sha256:2055434c83ac2aa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# replyAppleEvent(forSuspensionID:)

<sub>Instance Method</sub>

Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the corresponding reply event descriptor.

<sub>Mac Catalyst, macOS</sub>

```swift
func replyAppleEvent(forSuspensionID suspensionID: NSAppleEventManager.SuspensionID) -> NSAppleEventDescriptor
```

## Discussion

This descriptor, including any mutations, will be returned to the sender of the suspended event when handling of the event is resumed, if the sender has requested a reply. The effects of retaining the descriptor are undefined; it may be copied, but mutations of the copy are returned to the sender of the suspended event. [- replyAppleEventForSuspensionID:](<replyappleevent(forsuspensionid_).md>) may be invoked in any thread, not just the one in which the corresponding invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) occurred.

## See Also

### Suspending and resuming Apple events

- [- appleEventForSuspensionID:](<appleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the descriptor for the event whose handling was suspended.
- [currentAppleEvent](currentappleevent.md) — Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [currentReplyAppleEvent](currentreplyappleevent.md) — Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [- resumeWithSuspensionID:](<resume(withsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), signal that handling of the suspended event may now continue.
- [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), sets the values that will be returned by subsequent invocations of [currentAppleEvent](currentappleevent.md) and [currentReplyAppleEvent](currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) — Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [SuspensionID](suspensionid.md) — Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.
