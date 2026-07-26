---
title: didMoveNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nswindow/didmovenotification
source_url: 'https://developer.apple.com/documentation/appkit/nswindow/didmovenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nswindow/didmovenotification.json'
content_hash: 'sha256:4d4f556d0be2cb32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWindow](../nswindow.md)

# didMoveNotification

<sub>Type Property</sub>

A notification that the window object moved.

<sub>macOS</sub>

```swift
class let didMoveNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSWindow` object that has moved. This notification doesn’t contain a `userInfo` dictionary.

> [!note] Note
> The system sends this notification when the window that moved didn’t also change size. See [NSWindowDidResizeNotification](didresizenotification.md) for more information.

To observe this notification using Swift concurrency, use [DidMoveMessage](didmovemessage.md).

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
- [NSWindowDidResignKeyNotification](didresignkeynotification.md) — A notification that the window object resigned its status as key window.
- [NSWindowDidResignMainNotification](didresignmainnotification.md) — A notification that the window object resigned its status as main window.
- [NSWindowDidResizeNotification](didresizenotification.md) — A notification that the window object size changed.
- [NSWindowDidUpdateNotification](didupdatenotification.md) — A notification that the window object received an update message.
- [NSWindowWillBeginSheetNotification](willbeginsheetnotification.md) — A notification that the window object is about to open a sheet.
- [NSWindowWillCloseNotification](willclosenotification.md) — A notification that the window object is about to close.
