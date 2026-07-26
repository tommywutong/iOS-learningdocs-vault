---
title: authorizationStatus
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/authorizationstatus
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/authorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/authorizationstatus.json'
content_hash: 'sha256:1cb4f4dbbd36fb82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# authorizationStatus

<sub>Instance Property</sub>

The app’s ability to schedule and receive local and remote notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var authorizationStatus: UNAuthorizationStatus { get }
```

## Discussion

When the value of this property is [UNAuthorizationStatusAuthorized](../unauthorizationstatus/authorized.md), your app is allowed to schedule and receive local and remote notifications. When authorized, use the [alertSetting](alertsetting.md), [badgeSetting](badgesetting.md), and [soundSetting](soundsetting.md) properties to specify which types of interactions are allowed. When the value of the property is [UNAuthorizationStatusDenied](../unauthorizationstatus/denied.md), the system doesn’t deliver notifications to your app, and the system ignores any attempts to schedule local notifications.

The value of this property is [UNAuthorizationStatusNotDetermined](../unauthorizationstatus/notdetermined.md) if your app has never requested authorization using the [- requestAuthorizationWithOptions:completionHandler:](<../unusernotificationcenter/requestauthorization(options_completionhandler_).md>) method.

## See Also

### Getting the Authorization Status

- [UNAuthorizationStatus](../unauthorizationstatus.md) — Constants indicating whether the app is allowed to schedule notifications.
