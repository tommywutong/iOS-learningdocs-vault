---
title: didBecomeHiddenNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/didbecomehiddennotification
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/didbecomehiddennotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/didbecomehiddennotification.json'
content_hash: 'sha256:aa1cb58916091f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# didBecomeHiddenNotification

<sub>Type Property</sub>

A notification that posts when a window becomes hidden.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didBecomeHiddenNotification: NSNotification.Name
```

## Discussion

The notification object is the hidden window. This notification doesn’t contain a `userInfo` dictionary.

Switching between apps doesn’t generate visibility-related notifications for windows. Window visibility changes reflect changes to the window’s [hidden](../uiview/ishidden.md) property and reflect only the window’s visibility within the app.

The system posts this notification on the main actor.

## See Also

### Responding to window-related notifications

- [UIWindowDidBecomeVisibleNotification](didbecomevisiblenotification.md) — A notification that posts when a window becomes visible.
- [UIWindowDidBecomeKeyNotification](didbecomekeynotification.md) — A notification that posts whenever a window becomes the key window.
- [UIWindowDidResignKeyNotification](didresignkeynotification.md) — A notification that posts whenever a window resigns its status as main window.
