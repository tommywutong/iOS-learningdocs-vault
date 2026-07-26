---
title: willUnmountNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsworkspace/willunmountnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsworkspace/willunmountnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsworkspace/willunmountnotification.json'
content_hash: 'sha256:5c4859ef5c94c3de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWorkspace](../nsworkspace.md)

# willUnmountNotification

<sub>Type Property</sub>

A notification that the workspace posts when the Finder is about to unmount a device.

<sub>macOS</sub>

```swift
class let willUnmountNotification: NSNotification.Name
```

## Discussion

This notification doesn’t post if a volume becomes forcibly and immediately unavailable, such as when simply unplugging a drive.

The notification object is the shared `NSWorkspace` instance. The `userInfo` dictionary contains a key `@"NSDevicePath"` that returns the path where the device mounts as a string.

> [!important] Important
> To receive this notification, use [notificationCenter](notificationcenter.md) to register for it. If you use a different notification center to register, you won’t receive the notification.

To observe this notification using Swift concurrency, use [WillUnmountVolumeMessage](willunmountvolumemessage.md).

## See Also

### Responding to Environment Notifications

- [NSWorkspaceWillLaunchApplicationNotification](willlaunchapplicationnotification.md) — A notification that the workspace posts when the Finder is about to launch an app.
- [NSWorkspaceDidLaunchApplicationNotification](didlaunchapplicationnotification.md) — A notification that the workspace posts when a new app starts up.
- [NSWorkspaceDidTerminateApplicationNotification](didterminateapplicationnotification.md) — A notification that the workspace posts when an app finishes executing.
- [NSWorkspaceSessionDidBecomeActiveNotification](sessiondidbecomeactivenotification.md) — A notification that the workspace posts after a user session switches in.
- [NSWorkspaceSessionDidResignActiveNotification](sessiondidresignactivenotification.md) — A notification that the workspace posts before a user session switches out.
- [NSWorkspaceDidHideApplicationNotification](didhideapplicationnotification.md) — A notification that the workspace posts when the Finder hides an app.
- [NSWorkspaceDidUnhideApplicationNotification](didunhideapplicationnotification.md) — A notification that the workspace posts when the Finder unhides an app.
- [NSWorkspaceDidActivateApplicationNotification](didactivateapplicationnotification.md) — A notification that the workspace posts when the Finder is about to activate an app.
- [NSWorkspaceDidDeactivateApplicationNotification](diddeactivateapplicationnotification.md) — A notification that the workspace posts when the Finder deactivates an app.
- [NSWorkspaceDidRenameVolumeNotification](didrenamevolumenotification.md) — A notification that the workspace posts when a volume changes its name or mount path.
- [NSWorkspaceDidMountNotification](didmountnotification.md) — A notification that the workspace posts when a new device mounts.
- [NSWorkspaceDidUnmountNotification](didunmountnotification.md) — A notification that the workspace posts when the Finder unmounts a device.
- [NSWorkspaceDidChangeFileLabelsNotification](didchangefilelabelsnotification.md) — A notification that the workspace posts when the Finder file labels or colors change.
- [NSWorkspaceActiveSpaceDidChangeNotification](activespacedidchangenotification.md) — A notification that the workspace posts when a Spaces change occurs.
- [NSWorkspaceDidWakeNotification](didwakenotification.md) — A notification that the workspace posts when the device wakes from sleep.
