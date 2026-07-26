---
title: didChangeBackingPropertiesNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nswindow/didchangebackingpropertiesnotification
source_url: 'https://developer.apple.com/documentation/appkit/nswindow/didchangebackingpropertiesnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nswindow/didchangebackingpropertiesnotification.json'
content_hash: 'sha256:0c619e00e1c41e16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWindow](../nswindow.md)

# didChangeBackingPropertiesNotification

<sub>Type Property</sub>

A notification that the window object backing properties changed.

<sub>macOS</sub>

```swift
class let didChangeBackingPropertiesNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSWindow` object whose backing properties changed. This notification contains a `userInfo` dictionary that has backing scale and color space information. See [NSWindowDidChangeBackingPropertiesNotification User Info Properties](../nswindowdidchangebackingpropertiesnotification-user-info-properties.md) for the `userInfo` dictionary keys and values.

To observe this notification using Swift concurrency, use [DidChangeBackingPropertiesMessage](didchangebackingpropertiesmessage.md).

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
