---
title: unregisterForRemoteNotifications()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/unregisterforremotenotifications()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/unregisterforremotenotifications()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/unregisterforremotenotifications%28%29.json'
content_hash: 'sha256:b84a33a0536da5a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# unregisterForRemoteNotifications()

<sub>Instance Method</sub>

Unregisters for all remote notifications received through Apple Push Notification service.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func unregisterForRemoteNotifications()
```

## Discussion

Call this method when your app no longer needs to receive push notifications, such as when:

- Someone logs out of an account associated with push notifications
- Someone explicitly requests to stop receiving notifications through your app interface
- Your app removes support for all types of remote notifications

The Settings app also provides controls to prevent apps from receiving remote notifications. Apps unregistered through this method can always re-register by calling [- registerForRemoteNotifications](<registerforremotenotifications().md>).

## See Also

### Registering for remote notifications

- [- registerForRemoteNotifications](<registerforremotenotifications().md>) — Registers to receive remote notifications through Apple Push Notification service.
- [registeredForRemoteNotifications](isregisteredforremotenotifications.md) — A Boolean value that indicates whether the app is currently registered for remote notifications.
