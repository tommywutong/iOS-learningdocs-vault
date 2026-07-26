---
title: foreground
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationactionoptions/foreground
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions/foreground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionoptions/foreground.json'
content_hash: 'sha256:5237e9709f2e3350'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationActionOptions](../unnotificationactionoptions.md)

# foreground

<sub>Type Property</sub>

The action causes the app to launch in the foreground.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static var foreground: UNNotificationActionOptions { get }
```

## Discussion

When the user selects an action containing this option, the system brings the app to the foreground, asking the user to unlock the device as needed. Use this option for actions that require the user to interact further with your app. Do not use this option simply to bring your app to the foreground.

## See Also

### Constants

- [UNNotificationActionOptionAuthenticationRequired](authenticationrequired.md) — The action can be performed only on an unlocked device.
- [UNNotificationActionOptionDestructive](destructive.md) — The action performs a destructive task.
