---
title: UNAuthorizationStatus
framework: User Notifications
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unauthorizationstatus
source_url: 'https://developer.apple.com/documentation/usernotifications/unauthorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unauthorizationstatus.json'
content_hash: 'sha256:f5a4cde9134c3927'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNAuthorizationStatus

<sub>Enumeration</sub>

Constants indicating whether the app is allowed to schedule notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UNAuthorizationStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status

- [UNAuthorizationStatusNotDetermined](unauthorizationstatus/notdetermined.md) — The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatusDenied](unauthorizationstatus/denied.md) — The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatusAuthorized](unauthorizationstatus/authorized.md) — The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatusProvisional](unauthorizationstatus/provisional.md) — The application is provisionally authorized to post noninterruptive user notifications.
- [UNAuthorizationStatusEphemeral](unauthorizationstatus/ephemeral.md) — The app is authorized to schedule or receive notifications for a limited amount of time.

### Initializers

- [init(rawValue:)](<unauthorizationstatus/init(rawvalue_).md>)

## See Also

### Getting the Authorization Status

- [authorizationStatus](unnotificationsettings/authorizationstatus.md) — The app’s ability to schedule and receive local and remote notifications.
