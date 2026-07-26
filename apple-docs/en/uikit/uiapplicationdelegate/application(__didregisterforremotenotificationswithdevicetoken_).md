---
title: 'application(_:didRegisterForRemoteNotificationsWithDeviceToken:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidregisterforremotenotificationswithdevicetoken%3A%29.json'
content_hash: 'sha256:9d0e4473c79bc45e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didRegisterForRemoteNotificationsWithDeviceToken:)

<sub>Instance Method</sub>

Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data)
```

## Parameters

- `application` — The app object that initiated the remote-notification registration process.

- `deviceToken` — A globally unique token that identifies this device to APNs. Send this token to the server that you use to generate remote notifications. Your server must pass this token unmodified back to APNs when sending those remote notifications. APNs device tokens are of variable length. Do not hard-code their size.

## Discussion

UIKit calls this method after it successfully registers your app with APNs.  In your implementation of this method, send the contents of the `deviceToken` parameter to the server that you use to generate remote notifications. Never cache the device token locally on the user’s device. Device tokens can change periodically, so caching the value risks sending an invalid token to your server. If the device token hasn’t changed, registering with APNs and returning the token happens quickly.

Typically, this method is called only after you call the [- registerForRemoteNotifications](<../uiapplication/registerforremotenotifications().md>) method of [UIApplication](../uiapplication.md), but UIKit might call it in other rare circumstances. For example, UIKit calls the method when the user launches an app after having restored a device from data that is not the device’s backup data. In this exceptional case, the app won’t know the new device’s token until the user launches it.

## See Also

### Related Documentation

- [- application:didReceiveRemoteNotification:](<application(__didreceiveremotenotification_).md>) — Called when your app has received a remote notification. _(deprecated)_
- [- registerForRemoteNotifications](<../uiapplication/registerforremotenotifications().md>) — Registers to receive remote notifications through Apple Push Notification service.

### Handling remote notification registration

- [- application:didFailToRegisterForRemoteNotificationsWithError:](<application(__didfailtoregisterforremotenotificationswitherror_).md>) — Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [- application:didReceiveRemoteNotification:fetchCompletionHandler:](<application(__didreceiveremotenotification_fetchcompletionhandler_).md>) — Tells the app that a remote notification arrived that indicates there is data to be fetched.
