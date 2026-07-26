---
title: registerForRemoteNotifications()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/registerforremotenotifications()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/registerforremotenotifications()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/registerforremotenotifications%28%29.json'
content_hash: 'sha256:6e2e41ee1fa3198d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# registerForRemoteNotifications()

<sub>Instance Method</sub>

Registers to receive remote notifications through Apple Push Notification service.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func registerForRemoteNotifications()
```

## Discussion

Call this method to initiate the registration process with Apple Push Notification service. If registration succeeds, the app calls your app delegate object’s  [- application:didRegisterForRemoteNotificationsWithDeviceToken:](<../uiapplicationdelegate/application(__didregisterforremotenotificationswithdevicetoken_).md>) method and passes it a device token. You should pass this token along to the server you use to generate remote notifications for the device. If registration fails, the app calls its app delegate’s [- application:didFailToRegisterForRemoteNotificationsWithError:](<../uiapplicationdelegate/application(__didfailtoregisterforremotenotificationswitherror_).md>) method instead.

If you want your app’s remote notifications to display alerts, play sounds, or perform other user-facing actions, you must request authorization to do so using the [requestAuthorization(options:completionHandler:)](<../../usernotifications/unusernotificationcenter/requestauthorization(options_completionhandler_).md>) method of [UNUserNotificationCenter](../../usernotifications/unusernotificationcenter.md). If you do not request and receive authorization for your app’s interactions, the system delivers all remote notifications to your app silently.

## See Also

### Registering for remote notifications

- [- unregisterForRemoteNotifications](<unregisterforremotenotifications().md>) — Unregisters for all remote notifications received through Apple Push Notification service.
- [registeredForRemoteNotifications](isregisteredforremotenotifications.md) — A Boolean value that indicates whether the app is currently registered for remote notifications.
