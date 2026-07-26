---
title: didResignKeyNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/didresignkeynotification
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/didresignkeynotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/didresignkeynotification.json'
content_hash: 'sha256:dc51489033b3f1d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# didResignKeyNotification

<sub>Type Property</sub>

A notification that posts whenever a window resigns its status as main window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didResignKeyNotification: NSNotification.Name
```

## Discussion

The notification object is the window that resigned its main window status. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification on the main actor. In iOS 15 and later, the system posts this notification when the window is no longer the key window of its scene. In iOS 14 and earlier, the system posts this notification when the window is no longer the key window of the app.

## See Also

### Responding to window-related notifications

- [UIWindowDidBecomeVisibleNotification](didbecomevisiblenotification.md) — A notification that posts when a window becomes visible.
- [UIWindowDidBecomeHiddenNotification](didbecomehiddennotification.md) — A notification that posts when a window becomes hidden.
- [UIWindowDidBecomeKeyNotification](didbecomekeynotification.md) — A notification that posts whenever a window becomes the key window.
