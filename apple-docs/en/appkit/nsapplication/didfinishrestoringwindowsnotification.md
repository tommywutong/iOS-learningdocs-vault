---
title: didFinishRestoringWindowsNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsapplication/didfinishrestoringwindowsnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsapplication/didfinishrestoringwindowsnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsapplication/didfinishrestoringwindowsnotification.json'
content_hash: 'sha256:1d4b1cecb2eb8ef1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSApplication](../nsapplication.md)

# didFinishRestoringWindowsNotification

<sub>Type Property</sub>

Posted when the app has finished restoring windows.

<sub>macOS</sub>

```swift
class let didFinishRestoringWindowsNotification: NSNotification.Name
```

## Discussion

The notification is posted on the main actor when the app is finished restoring windows, that is, when all the completion handlers from [+ restoreWindowWithIdentifier:state:completionHandler:](<../nswindowrestoration/restorewindow(withidentifier_state_completionhandler_).md>) have been called. This is always posted after [NSApplicationWillFinishLaunchingNotification](willfinishlaunchingnotification.md), but may be posted before or after [NSApplicationDidFinishLaunchingNotification](didfinishlaunchingnotification.md), depending on whether clients copy the completion handlers and invoke them later. If there were no windows to restore, then this notification is still posted at the corresponding point in app launch (between [NSApplicationWillFinishLaunchingNotification](willfinishlaunchingnotification.md) and [NSApplicationDidFinishLaunchingNotification](didfinishlaunchingnotification.md)).

The notification object is [sharedApplication](shared.md). This notification doesn’t contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [DidFinishRestoringWindowsMessage](didfinishrestoringwindowsmessage.md).

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
- [NSApplicationDidChangeOcclusionStateNotification](didchangeocclusionstatenotification.md) — Posted when the app’s occlusion state changes.
