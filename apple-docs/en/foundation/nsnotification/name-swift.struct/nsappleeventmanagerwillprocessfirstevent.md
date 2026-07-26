---
title: NSAppleEventManagerWillProcessFirstEvent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsappleeventmanagerwillprocessfirstevent
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsappleeventmanagerwillprocessfirstevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsappleeventmanagerwillprocessfirstevent.json'
content_hash: 'sha256:c12c7cfaa03af5b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSAppleEventManagerWillProcessFirstEvent

<sub>Type Property</sub>

Posted by `NSAppleEventManager` before it first dispatches an Apple event. Your application can use this notification to avoid registering any Apple event handlers until the first time at which they may be needed.

<sub>Mac Catalyst, macOS</sub>

```swift
static let NSAppleEventManagerWillProcessFirstEvent: NSNotification.Name
```

## Discussion

The notification object is the `NSAppleEventManager`. This notification does not contain a `userInfo` dictionary.

## See Also

### Foundation

- [NSUbiquityIdentityDidChangeNotification](nsubiquityidentitydidchange.md) — Sent after the iCloud (“ubiquity”) identity has changed.
- [NSUndoManagerCheckpointNotification](nsundomanagercheckpoint.md) — Posted whenever an undo manager opens or closes an undo group (except when it opens a top-level group) and when checking the redo stack.
- [NSUndoManagerDidCloseUndoGroupNotification](nsundomanagerdidcloseundogroup.md) — Posted after an undo manager closes an undo group.
- [NSUndoManagerDidOpenUndoGroupNotification](nsundomanagerdidopenundogroup.md) — Posted whenever an undo manager opens an undo group.
- [NSUndoManagerDidRedoChangeNotification](nsundomanagerdidredochange.md) — Posted just after an undo manager performs a redo operation.
- [NSUndoManagerDidUndoChangeNotification](nsundomanagerdidundochange.md) — Posted just after an undo manager performs an undo operation.
- [NSUndoManagerWillCloseUndoGroupNotification](nsundomanagerwillcloseundogroup.md) — Posted before an undo manager closes an undo group.
- [NSUndoManagerWillRedoChangeNotification](nsundomanagerwillredochange.md) — Posted just before an undo manager performs a redo operation.
- [NSUndoManagerWillUndoChangeNotification](nsundomanagerwillundochange.md) — Posted just before an undo manager performs an undo operation.
- [NSWillBecomeMultiThreadedNotification](nswillbecomemultithreaded.md) — Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [+ detachNewThreadSelector:toTarget:withObject:](<../../thread/detachnewthreadselector(__totarget_with_).md>) or the [- start](<../../thread/start().md>) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing. _(deprecated)_
- [NSBundleResourceRequestLowDiskSpaceNotification](nsbundleresourcerequestlowdiskspace.md) — Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center. _(deprecated)_
- [NSCalendarDayChangedNotification](nscalendardaychanged.md) — A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.
- [NSDidBecomeSingleThreadedNotification](nsdidbecomesinglethreaded.md) — Not implemented. _(deprecated)_
- [NSExtensionHostDidBecomeActiveNotification](nsextensionhostdidbecomeactive.md) — Posted when the extension’s host app moves from the inactive to the active state.
- [NSExtensionHostDidEnterBackgroundNotification](nsextensionhostdidenterbackground.md) — Posted when the extension’s host app begins running in the background.
