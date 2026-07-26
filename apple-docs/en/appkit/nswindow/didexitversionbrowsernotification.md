---
title: didExitVersionBrowserNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nswindow/didexitversionbrowsernotification
source_url: 'https://developer.apple.com/documentation/appkit/nswindow/didexitversionbrowsernotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nswindow/didexitversionbrowsernotification.json'
content_hash: 'sha256:509382a3abff1607'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWindow](../nswindow.md)

# didExitVersionBrowserNotification

<sub>Type Property</sub>

A notification that the window object exited version browser mode.

<sub>macOS</sub>

```swift
class let didExitVersionBrowserNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSWindow` object that exited version browser mode. This notification doesn’t contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [DidExitVersionBrowserMessage](didexitversionbrowsermessage.md).

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
