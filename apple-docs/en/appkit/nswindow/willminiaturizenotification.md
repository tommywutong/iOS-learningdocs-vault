---
title: willMiniaturizeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nswindow/willminiaturizenotification
source_url: 'https://developer.apple.com/documentation/appkit/nswindow/willminiaturizenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nswindow/willminiaturizenotification.json'
content_hash: 'sha256:c49bbae5c423fa5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWindow](../nswindow.md)

# willMiniaturizeNotification

<sub>Type Property</sub>

A notification that the window object is about to minimize.

<sub>macOS</sub>

```swift
class let willMiniaturizeNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSWindow` object that’s about to minimize. This notification doesn’t contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [WillMiniaturizeMessage](willminiaturizemessage.md).

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
