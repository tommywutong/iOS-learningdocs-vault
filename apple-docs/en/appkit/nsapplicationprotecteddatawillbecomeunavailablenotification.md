---
title: NSApplicationProtectedDataWillBecomeUnavailableNotification
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 12.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsapplicationprotecteddatawillbecomeunavailablenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsapplicationprotecteddatawillbecomeunavailablenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsapplicationprotecteddatawillbecomeunavailablenotification.json'
content_hash: 'sha256:7e6effa64ca52c9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSApplicationProtectedDataWillBecomeUnavailableNotification

<sub>Global Variable</sub>

Posted when protected data is about to become unavailable.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSNotificationName NSApplicationProtectedDataWillBecomeUnavailableNotification;
```

## Discussion

The notification object is [sharedApplication](nsapplication/shared.md). This notification doesn’t contain a `userInfo` dictionary. The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [ProtectedDataWillBecomeUnavailableMessage](nsapplication/protecteddatawillbecomeunavailablemessage.md).

## See Also

### Notifications

- [NSApplicationDidBecomeActiveNotification](nsapplication/didbecomeactivenotification.md) — Posted immediately after the app becomes active.
- [NSApplicationDidChangeScreenParametersNotification](nsapplication/didchangescreenparametersnotification.md) — Posted when the configuration of the displays attached to the computer is changed.
- [NSApplicationDidFinishLaunchingNotification](nsapplication/didfinishlaunchingnotification.md) — Posted at the end of the [- finishLaunching](<nsapplication/finishlaunching().md>) method to indicate that the app has completed launching and is ready to run.
- [NSApplicationDidHideNotification](nsapplication/didhidenotification.md) — Posted at the end of the [- hide:](<nsapplication/hide(__).md>) method to indicate that the app is now hidden.
- [NSApplicationDidResignActiveNotification](nsapplication/didresignactivenotification.md) — Posted immediately after the app gives up its active status to another app.
- [NSApplicationDidUnhideNotification](nsapplication/didunhidenotification.md) — Posted at the end of the [- unhideWithoutActivation](<nsapplication/unhidewithoutactivation().md>) method to indicate that the app is now visible.
- [NSApplicationDidUpdateNotification](nsapplication/didupdatenotification.md) — Posted at the end of the [- updateWindows](<nsapplication/updatewindows().md>) method to indicate that the app has finished updating its windows.
- [NSApplicationWillBecomeActiveNotification](nsapplication/willbecomeactivenotification.md) — Posted immediately before the app becomes active.
- [NSApplicationWillFinishLaunchingNotification](nsapplication/willfinishlaunchingnotification.md) — Posted at the start of the [- finishLaunching](<nsapplication/finishlaunching().md>) method to indicate that the app has completed its initialization process and is about to finish launching.
- [NSApplicationWillHideNotification](nsapplication/willhidenotification.md) — Posted at the start of the [- hide:](<nsapplication/hide(__).md>) method to indicate that the app is about to be hidden.
- [NSApplicationWillResignActiveNotification](nsapplication/willresignactivenotification.md) — Posted immediately before the app gives up its active status to another app.
- [NSApplicationWillTerminateNotification](nsapplication/willterminatenotification.md) — Sends a notification to terminate the app.
- [NSApplicationWillUnhideNotification](nsapplication/willunhidenotification.md) — Posted at the start of the [- unhideWithoutActivation](<nsapplication/unhidewithoutactivation().md>) method to indicate that the app is about to become visible.
- [NSApplicationWillUpdateNotification](nsapplication/willupdatenotification.md) — Posted at the start of the [- updateWindows](<nsapplication/updatewindows().md>) method to indicate that the app is about to update its windows.
- [NSApplicationDidFinishRestoringWindowsNotification](nsapplication/didfinishrestoringwindowsnotification.md) — Posted when the app has finished restoring windows.
