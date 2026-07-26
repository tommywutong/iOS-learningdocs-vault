---
title: 'application(_:didFailToRegisterForRemoteNotificationsWithError:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidfailtoregisterforremotenotificationswitherror%3A%29.json'
content_hash: 'sha256:5d45fcf73ccf906c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didFailToRegisterForRemoteNotificationsWithError:)

<sub>Instance Method</sub>

Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error)
```

## Parameters

- `application` — The app object that initiated the remote-notification registration process.

- `error` — An [NSError](../../foundation/nserror.md) object that encapsulates information why registration did not succeed. The app can choose to display this information to the user.

## Discussion

UIKit calls this method if it was unable to register your app with APNs or if your app is not properly configured for remote notifications. During development, make sure your app has the proper entitlements and that its App ID is configured to support push notifications. You might use your implementation of this method to make a note of the failed registration so that you can try again later.

For more information about how to set up and send remote notifications in your app, see [Setting up a remote notification server](../../usernotifications/setting-up-a-remote-notification-server.md).

## See Also

### Handling remote notification registration

- [- application:didRegisterForRemoteNotificationsWithDeviceToken:](<application(__didregisterforremotenotificationswithdevicetoken_).md>) — Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [- application:didReceiveRemoteNotification:fetchCompletionHandler:](<application(__didreceiveremotenotification_fetchcompletionhandler_).md>) — Tells the app that a remote notification arrived that indicates there is data to be fetched.
