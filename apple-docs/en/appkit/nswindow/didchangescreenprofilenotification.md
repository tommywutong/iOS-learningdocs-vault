---
title: didChangeScreenProfileNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nswindow/didchangescreenprofilenotification
source_url: 'https://developer.apple.com/documentation/appkit/nswindow/didchangescreenprofilenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nswindow/didchangescreenprofilenotification.json'
content_hash: 'sha256:e2cdc3d0c8ee5555'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWindow](../nswindow.md)

# didChangeScreenProfileNotification

<sub>Type Property</sub>

A notification that the screen containing the window changed.

<sub>macOS</sub>

```swift
class let didChangeScreenProfileNotification: NSNotification.Name
```

## Discussion

NSWindow sends this notification only if the value of [displaysWhenScreenProfileChanges](displayswhenscreenprofilechanges.md) is [true](../../swift/true.md), and in the following situations:

- When most of the window moves to a screen whose profile is different from the previous screen
- When the ColorSync profile for the current screen changes

The notification object is the `NSWindow` object whose profile changed. This notification doesn’t contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [DidChangeScreenProfileMessage](didchangescreenprofilemessage.md).

## See Also

### Notifications

- [NSWindowDidBecomeKeyNotification](didbecomekeynotification.md) — A notification that the window object became the key window.
- [NSWindowDidBecomeMainNotification](didbecomemainnotification.md) — A notification that the window object became the main window.
- [NSWindowDidChangeScreenNotification](didchangescreennotification.md) — A notification that a portion of the window object’s frame moved onto or off of a screen.
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
- [NSWindowWillCloseNotification](willclosenotification.md) — A notification that the window object is about to close.
