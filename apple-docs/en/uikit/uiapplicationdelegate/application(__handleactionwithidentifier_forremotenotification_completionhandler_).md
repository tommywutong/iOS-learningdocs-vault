---
title: 'application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleactionwithidentifier:forremotenotification:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ahandleactionwithidentifier%3Aforremotenotification%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c594b74dc7e9353d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:handleActionWithIdentifier:forRemoteNotification:completionHandler:)

<sub>Instance Method</sub>

Tells the app delegate to perform the custom action specified by a remote notification.

> [!warning] Deprecated
> Use [userNotificationCenter(_:didReceive:withCompletionHandler:)](<../../usernotifications/unusernotificationcenterdelegate/usernotificationcenter(__didreceive_withcompletionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [AnyHashable : Any], completionHandler: @escaping () -> Void)
```

<sub>Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, forRemoteNotification userInfo: [AnyHashable : Any]) async
```

## Parameters

- `application` — The app object that received the remote notification.

- `identifier` — The identifier associated with the custom action.

- `userInfo` — A dictionary that contains information related to the remote notification. This dictionary originates from the provider as a JSON-defined dictionary, which iOS converts to an [NSDictionary](../../foundation/nsdictionary.md) object before calling this method. The contents of the dictionary are the remote notification payload, which consists only of property-list objects plus [NSNull](../../foundation/nsnull.md). For more information about the contents of the remote notification dictionary, see [Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

- `completionHandler` — The block to execute when you are finished performing the specified action. You must call this block at the end of your method.

## Discussion

The app calls this method when the user taps an action button in an alert displayed in response to a remote notification. Remote notifications that include a `category` key in their payload display buttons for the actions in the corresponding category. If the user taps one of those buttons, the system wakes up the app (launching it if needed) and calls this method in the background. Your implementation of this method should perform the action associated with the specified `identifier` and execute the block in the `completionHandler` parameter as soon as you are done. Failure to execute the completion handler block at the end of your implementation will cause your app to be terminated.

To configure the actions for a given category, create a UIUserNotificationActionSettings object and register it with the app when you call the [- registerUserNotificationSettings:](<../uiapplication/registerusernotificationsettings(__).md>) method.

## See Also

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
- [- application:didReceiveLocalNotification:](<application(__didreceive_).md>) — Sent to the delegate when a running app receives a local notification. _(deprecated)_
- [- application:didReceiveRemoteNotification:](<application(__didreceiveremotenotification_).md>) — Called when your app has received a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<application(__handleactionwithidentifier_for_completionhandler_).md>) — Called when your app has been activated because user selected a custom action from the alert panel of a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_for_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a local notification. _(deprecated)_
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
