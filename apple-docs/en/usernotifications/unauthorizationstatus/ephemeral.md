---
title: UNAuthorizationStatus.ephemeral
framework: User Notifications
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unauthorizationstatus/ephemeral
source_url: 'https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/ephemeral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unauthorizationstatus/ephemeral.json'
content_hash: 'sha256:7df3e0f71e5e02ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNAuthorizationStatus](../unauthorizationstatus.md)

# UNAuthorizationStatus.ephemeral

<sub>Case</sub>

The app is authorized to schedule or receive notifications for a limited amount of time.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case ephemeral
```

## Discussion

An App Clip may have the ability to schedule or receive notifications for a limited amount of time. For more information, see [Enabling notifications in App Clips](../../appclip/enabling-notifications-in-app-clips.md).

## See Also

### Status

- [UNAuthorizationStatusNotDetermined](notdetermined.md) — The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatusDenied](denied.md) — The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatusAuthorized](authorized.md) — The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatusProvisional](provisional.md) — The application is provisionally authorized to post noninterruptive user notifications.
