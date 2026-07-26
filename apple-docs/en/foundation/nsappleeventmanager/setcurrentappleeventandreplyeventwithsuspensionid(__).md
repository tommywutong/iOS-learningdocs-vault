---
title: 'setCurrentAppleEventAndReplyEventWithSuspensionID(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventmanager/setcurrentappleeventandreplyeventwithsuspensionid(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/setcurrentappleeventandreplyeventwithsuspensionid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/setcurrentappleeventandreplyeventwithsuspensionid%28_%3A%29.json'
content_hash: 'sha256:5db29bfd2506b1c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# setCurrentAppleEventAndReplyEventWithSuspensionID(_:)

<sub>Instance Method</sub>

Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), sets the values that will be returned by subsequent invocations of [currentAppleEvent](currentappleevent.md) and [currentReplyAppleEvent](currentreplyappleevent.md) to be the event whose handling was suspended and its corresponding reply event, respectively.

<sub>Mac Catalyst, macOS</sub>

```swift
func setCurrentAppleEventAndReplyEventWithSuspensionID(_ suspensionID: NSAppleEventManager.SuspensionID)
```

## Discussion

Redundant invocations of [- setCurrentAppleEventAndReplyEventWithSuspensionID:](<setcurrentappleeventandreplyeventwithsuspensionid(__).md>) are ignored.

## See Also

### Suspending and resuming Apple events

- [- appleEventForSuspensionID:](<appleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the descriptor for the event whose handling was suspended.
- [currentAppleEvent](currentappleevent.md) — Returns the descriptor for `currentAppleEvent` if an Apple event is being handled on the current thread.
- [currentReplyAppleEvent](currentreplyappleevent.md) — Returns the corresponding reply event descriptor if an Apple event is being handled on the current thread.
- [- replyAppleEventForSuspensionID:](<replyappleevent(forsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), returns the corresponding reply event descriptor.
- [- resumeWithSuspensionID:](<resume(withsuspensionid_).md>) — Given a nonzero `suspensionID` returned by an invocation of [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>), signal that handling of the suspended event may now continue.
- [- suspendCurrentAppleEvent](<suspendcurrentappleevent().md>) — Suspends the handling of the current event and returns an ID that must be used to resume the handling of the event if an Apple event is being handled on the current thread.
- [SuspensionID](suspensionid.md) — Identifies an Apple event whose handling has been suspended. Can be used to resume handling of the Apple event.
