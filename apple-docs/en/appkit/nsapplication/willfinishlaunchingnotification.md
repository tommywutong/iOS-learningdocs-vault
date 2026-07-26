---
title: willFinishLaunchingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsapplication/willfinishlaunchingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsapplication/willfinishlaunchingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsapplication/willfinishlaunchingnotification.json'
content_hash: 'sha256:df77f3f7cbce0763'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSApplication](../nsapplication.md)

# willFinishLaunchingNotification

<sub>Type Property</sub>

Posted at the start of the [- finishLaunching](<finishlaunching().md>) method to indicate that the app has completed its initialization process and is about to finish launching.

<sub>macOS</sub>

```swift
class let willFinishLaunchingNotification: NSNotification.Name
```

## Discussion

The notification object is `NSApp`. This notification doesn’t contain a `userInfo` dictionary.  The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [WillFinishLaunchingMessage](willfinishlaunchingmessage.md).

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
- [NSApplicationWillHideNotification](willhidenotification.md) — Posted at the start of the [- hide:](<hide(__).md>) method to indicate that the app is about to be hidden.
- [NSApplicationWillResignActiveNotification](willresignactivenotification.md) — Posted immediately before the app gives up its active status to another app.
- [NSApplicationWillTerminateNotification](willterminatenotification.md) — Sends a notification to terminate the app.
- [NSApplicationWillUnhideNotification](willunhidenotification.md) — Posted at the start of the [- unhideWithoutActivation](<unhidewithoutactivation().md>) method to indicate that the app is about to become visible.
- [NSApplicationWillUpdateNotification](willupdatenotification.md) — Posted at the start of the [- updateWindows](<updatewindows().md>) method to indicate that the app is about to update its windows.
- [NSApplicationDidFinishRestoringWindowsNotification](didfinishrestoringwindowsnotification.md) — Posted when the app has finished restoring windows.
- [NSApplicationDidChangeOcclusionStateNotification](didchangeocclusionstatenotification.md) — Posted when the app’s occlusion state changes.
