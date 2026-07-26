---
title: isRegisteredForRemoteNotifications
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/isregisteredforremotenotifications
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/isregisteredforremotenotifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/isregisteredforremotenotifications.json'
content_hash: 'sha256:8192a8e365b2718f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# isRegisteredForRemoteNotifications

<sub>Instance Property</sub>

A Boolean value that indicates whether the app is currently registered for remote notifications.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isRegisteredForRemoteNotifications: Bool { get }
```

## Discussion

This method reflects whether the remote registration process completed successfully—a process that begins when you call the [- registerForRemoteNotifications](<registerforremotenotifications().md>) method. This method does not reflect whether remote notifications are actually available due to connectivity issues. The value returned by this method takes into account the user’s preferences for receiving remote notifications.

## See Also

### Registering for remote notifications

- [- registerForRemoteNotifications](<registerforremotenotifications().md>) — Registers to receive remote notifications through Apple Push Notification service.
- [- unregisterForRemoteNotifications](<unregisterforremotenotifications().md>) — Unregisters for all remote notifications received through Apple Push Notification service.
