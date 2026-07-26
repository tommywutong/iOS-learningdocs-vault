---
title: didBecomeKeyNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/didbecomekeynotification
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/didbecomekeynotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/didbecomekeynotification.json'
content_hash: 'sha256:839dd071e60d76d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# didBecomeKeyNotification

<sub>Type Property</sub>

A notification that posts whenever a window becomes the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didBecomeKeyNotification: NSNotification.Name
```

## Discussion

The notification object is the window that became key. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification on the main actor. In iOS 15 and later, the system posts this notification when the window becomes the key window of its scene. In iOS 14 and earlier, the system posts this notification when the window becomes the key window of the app.

## See Also

### Responding to window-related notifications

- [UIWindowDidBecomeVisibleNotification](didbecomevisiblenotification.md) — A notification that posts when a window becomes visible.
- [UIWindowDidBecomeHiddenNotification](didbecomehiddennotification.md) — A notification that posts when a window becomes hidden.
- [UIWindowDidResignKeyNotification](didresignkeynotification.md) — A notification that posts whenever a window resigns its status as main window.
