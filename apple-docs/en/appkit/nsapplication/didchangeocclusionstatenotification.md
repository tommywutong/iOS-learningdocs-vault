---
title: didChangeOcclusionStateNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.9+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsapplication/didchangeocclusionstatenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsapplication/didchangeocclusionstatenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsapplication/didchangeocclusionstatenotification.json'
content_hash: 'sha256:f8aaf38629cca162'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSApplication](../nsapplication.md)

# didChangeOcclusionStateNotification

<sub>Type Property</sub>

Posted when the app’s occlusion state changes.

<sub>macOS</sub>

```swift
class let didChangeOcclusionStateNotification: NSNotification.Name
```

## Discussion

The system posts this notification on the main actor.  Upon receiving this notification, you can query the app for its occlusion state. Note that this only notifies about changes in the state of the occlusion, not when the occlusion region changes. You can use this notification to increase responsiveness and save power by halting any expensive calculations that the user can’t see.

To observe this notification using Swift concurrency, use [DidChangeOcclusionStateMessage](didchangeocclusionstatemessage.md).

## See Also

### Notifications

- [NSApplicationDidBecomeActiveNotification](didbecomeactivenotification.md) — Posted immediately after the app becomes active.
- [NSApplicationDidChangeScreenParametersNotification](didchangescreenparametersnotification.md) — Posted when the configuration of the displays attached to the computer is changed.
- [NSApplicationDidFinishLaunchingNotification](didfinishlaunchingnotification.md) — Posted at the end of the [- finishLaunching](<finishlaunching().md>) method to indicate that the app has completed launching and is ready to run.
- [NSApplicationDidHideNotification](didhidenotification.md) — Posted at the end of the [- hide:](<hide(__).md>) method to indicate that the app is now hidden.
- [NSApplicationDidResignActiveNotification](didresignactivenotification.md) — Posted immediately after the app gives up its active status to another app.
- [NSApplicationDidUnhideNotification](didunhidenotification.md) — Posted at the end of the [- unhideWithoutActivation](<unhidewithoutactivation().md>) method to indicate that the app is now visible.
- [NSApplicationDidUpdateNotification](didupdatenotification.md) — Posted at the end of the [- updateWindows](<updatewindows().md>) method to indicate that the app has finished updating its windows.
- [NSApplicationWillBecomeActiveNotification](willbecomeactivenotification.md) — Posted immediately before the app becomes active.
- [NSApplicationWillFinishLaunchingNotification](willfinishlaunchingnotification.md) — Posted at the start of the [- finishLaunching](<finishlaunching().md>) method to indicate that the app has completed its initialization process and is about to finish launching.
- [NSApplicationWillHideNotification](willhidenotification.md) — Posted at the start of the [- hide:](<hide(__).md>) method to indicate that the app is about to be hidden.
- [NSApplicationWillResignActiveNotification](willresignactivenotification.md) — Posted immediately before the app gives up its active status to another app.
- [NSApplicationWillTerminateNotification](willterminatenotification.md) — Sends a notification to terminate the app.
- [NSApplicationWillUnhideNotification](willunhidenotification.md) — Posted at the start of the [- unhideWithoutActivation](<unhidewithoutactivation().md>) method to indicate that the app is about to become visible.
- [NSApplicationWillUpdateNotification](willupdatenotification.md) — Posted at the start of the [- updateWindows](<updatewindows().md>) method to indicate that the app is about to update its windows.
- [NSApplicationDidFinishRestoringWindowsNotification](didfinishrestoringwindowsnotification.md) — Posted when the app has finished restoring windows.
