---
title: UNAuthorizationStatus.authorized
framework: User Notifications
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unauthorizationstatus/authorized
source_url: 'https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/authorized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unauthorizationstatus/authorized.json'
content_hash: 'sha256:9e1e9413735afcd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNAuthorizationStatus](../unauthorizationstatus.md)

# UNAuthorizationStatus.authorized

<sub>Case</sub>

The app is authorized to schedule or receive notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case authorized
```

## See Also

### Status

- [UNAuthorizationStatusNotDetermined](notdetermined.md) — The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatusDenied](denied.md) — The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatusProvisional](provisional.md) — The application is provisionally authorized to post noninterruptive user notifications.
- [UNAuthorizationStatusEphemeral](ephemeral.md) — The app is authorized to schedule or receive notifications for a limited amount of time.
