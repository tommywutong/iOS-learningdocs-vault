---
title: 'post(notification:argument:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/post(notification:argument:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/post(notification:argument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/post%28notification%3Aargument%3A%29.json'
content_hash: 'sha256:a84b843bb69cdda7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# post(notification:argument:)

<sub>Type Method</sub>

Posts a notification to assistive apps.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func post(notification: UIAccessibility.Notification, argument: Any?)
```

## Parameters

- `notification` — The notification to post (see “Notifications” in [UIAccessibility](../uiaccessibility-protocol.md) for a list of notifications).

- `argument` — The argument specified by the notification. Pass `nil` unless a notification specifies otherwise.

## Discussion

Your application might need to post accessibility notifications if you have user interface components that change very frequently or that appear and disappear.

## See Also

### Notifications

- [Notification names](../notification-names.md) — The names of notifications that the accessibility system generates.
- [Notification dictionary keys](../notification-dictionary-keys.md) — Handle notifications with keys in the user info dictionary.
