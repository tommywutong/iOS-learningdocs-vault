---
title: didExitFullScreenNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nswindow/didexitfullscreennotification
source_url: 'https://developer.apple.com/documentation/appkit/nswindow/didexitfullscreennotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nswindow/didexitfullscreennotification.json'
content_hash: 'sha256:1b07fc84e24f4101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWindow](../nswindow.md)

# didExitFullScreenNotification

<sub>Type Property</sub>

A notification that the window object exited full-screen mode.

<sub>macOS</sub>

```swift
class let didExitFullScreenNotification: NSNotification.Name
```

## Discussion

The system posts this notification when a window moves in front of other windows or when other windows move from in front of it, exposing part of its content.

The notification object is the [NSWindow](../nswindow.md) object that exposes its content. In the notification’s `userInfo` dictionary, the key `NSExposedRect` specifies an [NSValue](../../foundation/nsvalue.md) object that contains the rectangle the window exposed.

To observe this notification using Swift concurrency, use [DidExitFullScreenMessage](didexitfullscreenmessage.md).

## See Also

### Notifications

- [NSWindowDidBecomeKeyNotification](didbecomekeynotification.md) — A notification that the window object became the key window.
- [NSWindowDidBecomeMainNotification](didbecomemainnotification.md) — A notification that the window object became the main window.
- [NSWindowDidChangeScreenNotification](didchangescreennotification.md) — A notification that a portion of the window object’s frame moved onto or off of a screen.
- [NSWindowDidChangeScreenProfileNotification](didchangescreenprofilenotification.md) — A notification that the screen containing the window changed.
- [NSWindowDidDeminiaturizeNotification](diddeminiaturizenotification.md) — A notification that the window is no longer minimized.
- [NSWindowDidEndSheetNotification](didendsheetnotification.md) — A notification that the window object closed an attached sheet.
- [NSWindowDidEndLiveResizeNotification](didendliveresizenotification.md) — A notification that the user resized the window object.
- [NSWindowDidExposeNotification](didexposenotification.md) — A notification that a window exposed a portion of its nonretained content.
- [NSWindowDidMiniaturizeNotification](didminiaturizenotification.md) — A notification that the window object minimized.
- [NSWindowDidMoveNotification](didmovenotification.md) — A notification that the window object moved.
- [NSWindowDidResignKeyNotification](didresignkeynotification.md) — A notification that the window object resigned its status as key window.
- [NSWindowDidResignMainNotification](didresignmainnotification.md) — A notification that the window object resigned its status as main window.
- [NSWindowDidResizeNotification](didresizenotification.md) — A notification that the window object size changed.
- [NSWindowDidUpdateNotification](didupdatenotification.md) — A notification that the window object received an update message.
- [NSWindowWillBeginSheetNotification](willbeginsheetnotification.md) — A notification that the window object is about to open a sheet.
