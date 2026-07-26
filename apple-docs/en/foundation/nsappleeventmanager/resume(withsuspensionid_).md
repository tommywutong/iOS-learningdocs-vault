---
title: 'resume(withSuspensionID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventmanager/resume(withsuspensionid:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/resume(withsuspensionid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/resume%28withsuspensionid%3A%29.json'
content_hash: 'sha256:5257d380687ef7c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# resume(withSuspensionID:)

<sub>Instance Method</sub>

Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), signal that handling of the suspended event may now continue.

<sub>Mac Catalyst, macOS</sub>

```swift
func resume(withSuspensionID suspensionID: NSAppleEventManager.SuspensionID)
```

## Discussion

This may result in the immediate sending of the reply event to the sender of the suspended event, if the sender has requested a reply. If `suspensionID` has been used in a previous invocation of [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) the effects of that invocation are completely undone. Redundant invocations of [- resumeWithSuspensionID:](<resume(withsuspensionid_).md>) are ignored. Subsequent invocations of other `NSAppleEventManager` methods using the same suspension ID are invalid. [- resumeWithSuspensionID:](<resume(withsuspensionid_).md>) may be invoked in any thread, not just the one in which the corresponding invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) occurred.

## See Also

### Suspending and resuming Apple events

- [- appleEventForSuspensionID:](<appleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the descriptor for the event whose handling was suspended.
- [currentAppleEvent](currentappleevent.md) — Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [currentReplyAppleEvent](currentreplyappleevent.md) — Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [- replyAppleEventForSuspensionID:](<replyappleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the corresponding reply event descriptor.
- [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), sets the values that will be returned by subsequent invocations of [currentAppleEvent](currentappleevent.md) and [currentReplyAppleEvent](currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.
- [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) — Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [SuspensionID](suspensionid.md) — Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.
