---
title: didTerminateApplicationNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsworkspace/didterminateapplicationnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsworkspace/didterminateapplicationnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsworkspace/didterminateapplicationnotification.json'
content_hash: 'sha256:c8b8efdeb499c4aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWorkspace](../nsworkspace.md)

# didTerminateApplicationNotification

<sub>Type Property</sub>

A notification that the workspace posts when an app finishes executing.

<sub>macOS</sub>

```swift
class let didTerminateApplicationNotification: NSNotification.Name
```

## Discussion

The notification object is the shared `NSWorkspace` instance. The `userInfo` dictionary contains the [NSWorkspaceApplicationKey](applicationuserinfokey.md) key with a corresponding instance of [NSRunningApplication](../nsrunningapplication.md) that represents the affected app.

The system doesn’t post this notification for background apps or for apps that have the `LSUIElement` key in their `Info.plist` file. If you want to know when all apps (including background apps) launch or terminate, use key-value observing to monitor the value that returns from the [runningApplications](runningapplications.md) method.

> [!important] Important
> To receive this notification, use [notificationCenter](notificationcenter.md) to register for it. If you use a different notification center to register, you won’t receive the notification.

To observe this notification using Swift concurrency, use [DidTerminateApplicationMessage](didterminateapplicationmessage.md).

## See Also

### Responding to Environment Notifications

- [NSWorkspaceWillLaunchApplicationNotification](willlaunchapplicationnotification.md) — A notification that the workspace posts when the Finder is about to launch an app.
- [NSWorkspaceDidLaunchApplicationNotification](didlaunchapplicationnotification.md) — A notification that the workspace posts when a new app starts up.
- [NSWorkspaceSessionDidBecomeActiveNotification](sessiondidbecomeactivenotification.md) — A notification that the workspace posts after a user session switches in.
- [NSWorkspaceSessionDidResignActiveNotification](sessiondidresignactivenotification.md) — A notification that the workspace posts before a user session switches out.
- [NSWorkspaceDidHideApplicationNotification](didhideapplicationnotification.md) — A notification that the workspace posts when the Finder hides an app.
- [NSWorkspaceDidUnhideApplicationNotification](didunhideapplicationnotification.md) — A notification that the workspace posts when the Finder unhides an app.
- [NSWorkspaceDidActivateApplicationNotification](didactivateapplicationnotification.md) — A notification that the workspace posts when the Finder is about to activate an app.
- [NSWorkspaceDidDeactivateApplicationNotification](diddeactivateapplicationnotification.md) — A notification that the workspace posts when the Finder deactivates an app.
- [NSWorkspaceDidRenameVolumeNotification](didrenamevolumenotification.md) — A notification that the workspace posts when a volume changes its name or mount path.
- [NSWorkspaceDidMountNotification](didmountnotification.md) — A notification that the workspace posts when a new device mounts.
- [NSWorkspaceWillUnmountNotification](willunmountnotification.md) — A notification that the workspace posts when the Finder is about to unmount a device.
- [NSWorkspaceDidUnmountNotification](didunmountnotification.md) — A notification that the workspace posts when the Finder unmounts a device.
- [NSWorkspaceDidChangeFileLabelsNotification](didchangefilelabelsnotification.md) — A notification that the workspace posts when the Finder file labels or colors change.
- [NSWorkspaceActiveSpaceDidChangeNotification](activespacedidchangenotification.md) — A notification that the workspace posts when a Spaces change occurs.
- [NSWorkspaceDidWakeNotification](didwakenotification.md) — A notification that the workspace posts when the device wakes from sleep.
