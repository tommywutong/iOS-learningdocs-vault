---
title: 'application(_:didReceiveRemoteNotification:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（10.0 起废弃）, iPadOS 3.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（10.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didreceiveremotenotification:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didreceiveremotenotification:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidreceiveremotenotification%3A%29.json'
content_hash: 'sha256:e955b5d63961695f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didReceiveRemoteNotification:)

<sub>Instance Method</sub>

Called when your app has received a remote notification.

> [!warning] Deprecated
> Use [- application:didReceiveRemoteNotification:fetchCompletionHandler:](<application(__didreceiveremotenotification_fetchcompletionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any])
```

## Parameters

- `application` — The app object that received the remote notification.

- `userInfo` — A dictionary that contains information related to the remote notification, potentially including a badge number for the app icon, an alert sound, an alert message to display to the user, a notification identifier, and custom data. The provider originates it as a JSON-defined dictionary that iOS converts to an [NSDictionary](../../foundation/nsdictionary.md) object; the dictionary might contain only property-list objects plus [NSNull](../../foundation/nsnull.md).

## Discussion

Implement the [- application:didReceiveRemoteNotification:fetchCompletionHandler:](<application(__didreceiveremotenotification_fetchcompletionhandler_).md>) method instead of this one whenever possible. If your delegate implements both methods, the app object calls the [- application:didReceiveRemoteNotification:fetchCompletionHandler:](<application(__didreceiveremotenotification_fetchcompletionhandler_).md>) method.

If the app is running, the app calls this method to process incoming remote notifications. The `userInfo` dictionary contains the `aps` key whose value is another dictionary with the remaining notification data. Although you should not need the information in the `aps` dictionary, you can retrieve its contents using the following keys:

- `alert`—The value is either a string for the alert message or a dictionary with two keys: `body` and `show-view`. The value of the `body` key is a string containing the alert message and the value of the `show-view` key is a Boolean. If the value of the `show-view` key is `false`, the alert’s View button is not shown. The default is to show the View button which, if the user taps it, launches the app.
- `badge`—A number indicating the quantity of data items to download from the provider. This number is to be displayed on the app icon. The absence of a `badge` property indicates that any number currently badging the icon should be removed.
- `sound`—The name of a sound file in the app bundle to play as an alert sound. If “default” is specified, the default sound should be played.

The `userInfo` dictionary may also have custom data defined by the provider according to the JSON schema. The properties for custom data should be specified at the same level as the `aps` dictionary. However, custom-defined properties should not be used for mass data transport because there is a strict size limit per notification (256 bytes) and delivery is not guaranteed.

If the app is not running when a remote notification arrives, the method launches the app and provides the appropriate information in the launch options dictionary. The app does not call this method to handle that remote notification. Instead, your implementation of the [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) or [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method needs to get the remote notification payload data and respond appropriately.

For more information about how to implement remote notifications in your app, see [Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## See Also

### Related Documentation

- [- application:didRegisterForRemoteNotificationsWithDeviceToken:](<application(__didregisterforremotenotificationswithdevicetoken_).md>) — Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [- application:didFailToRegisterForRemoteNotificationsWithError:](<application(__didfailtoregisterforremotenotificationswitherror_).md>) — Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
- [- application:didReceiveLocalNotification:](<application(__didreceive_).md>) — Sent to the delegate when a running app receives a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<application(__handleactionwithidentifier_for_completionhandler_).md>) — Called when your app has been activated because user selected a custom action from the alert panel of a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_for_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) — Tells the app delegate to perform the custom action specified by a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_forremotenotification_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a remote notification. _(deprecated)_
- [- application:handleOpenURL:](<application(__handleopen_).md>) — Asks the delegate to open a resource identified by URL. _(deprecated)_
- [- application:openURL:sourceApplication:annotation:](<application(__open_sourceapplication_annotation_).md>) — Asks the delegate to open a resource identified by a URL. _(deprecated)_
- [- application:willChangeStatusBarOrientation:duration:](<application(__willchangestatusbarorientation_duration_).md>) — Tells the delegate when the interface orientation of the status bar is about to change. _(deprecated)_
- [- application:didChangeStatusBarOrientation:](<application(__didchangestatusbarorientation_).md>) — Tells the delegate when the interface orientation of the status bar has changed. _(deprecated)_
- [- application:willChangeStatusBarFrame:](<application(__willchangestatusbarframe_).md>) — Tells the delegate when the frame of the status bar is about to change. _(deprecated)_
- [- application:didChangeStatusBarFrame:](<application(__didchangestatusbarframe_).md>) — Tells the delegate when the frame of the status bar has changed. _(deprecated)_
- [- application:handleIntent:completionHandler:](<application(__handle_completionhandler_).md>) — Asks the delegate to handle the specified SiriKit intent directly. _(deprecated)_
- [- application:performFetchWithCompletionHandler:](<application(__performfetchwithcompletionhandler_).md>) — Tells the app that it can begin a fetch operation if it has data to download. _(deprecated)_
- [- application:shouldSaveApplicationState:](<application(__shouldsaveapplicationstate_).md>) — Asks the delegate whether to preserve the app’s state. _(deprecated)_
