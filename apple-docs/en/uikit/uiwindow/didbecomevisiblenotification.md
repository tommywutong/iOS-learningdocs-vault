---
title: didBecomeVisibleNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/didbecomevisiblenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/didbecomevisiblenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/didbecomevisiblenotification.json'
content_hash: 'sha256:522b268a8cd21ea0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# didBecomeVisibleNotification

<sub>Type Property</sub>

A notification that posts when a window becomes visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didBecomeVisibleNotification: NSNotification.Name
```

## Discussion

The notification object is the visible window. This notification doesn’t contain a `userInfo` dictionary.

Switching between apps doesn’t generate visibility-related notifications for windows. Window visibility changes reflect changes to the window’s [hidden](../uiview/ishidden.md) property and reflect only the window’s visibility within the app.

The system posts this notification on the main actor.

## See Also

### Responding to window-related notifications

- [UIWindowDidBecomeHiddenNotification](didbecomehiddennotification.md) — A notification that posts when a window becomes hidden.
- [UIWindowDidBecomeKeyNotification](didbecomekeynotification.md) — A notification that posts whenever a window becomes the key window.
- [UIWindowDidResignKeyNotification](didresignkeynotification.md) — A notification that posts whenever a window resigns its status as main window.
