---
title: 'application(_:didReceive:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didreceive:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didreceive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidreceive%3A%29.json'
content_hash: 'sha256:b51b91f474e94a03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didReceive:)

<sub>Instance Method</sub>

Sent to the delegate when a running app receives a local notification.

> [!warning] Deprecated
> Use [userNotificationCenter(_:willPresent:withCompletionHandler:)](<../../usernotifications/unusernotificationcenterdelegate/usernotificationcenter(__willpresent_withcompletionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, didReceive notification: UILocalNotification)
```

## Parameters

- `application` — The app object that received the local notification.

- `notification` — A local notification that encapsulates details about the notification, potentially including custom data.

## Discussion

Local notifications are similar to remote notifications, but differ in that they are scheduled, displayed, and received entirely on the same device. An app can create and schedule a local notification, and the operating system then delivers it at the scheduled date and time. If the app is not active in the foreground when the notification fires, the system uses the information in the [UILocalNotification](../uilocalnotification.md) object to determine whether it should display an alert, badge the app icon, or play a sound. If the app is running in the foreground, the system calls this method directly without alerting the user in any way.

You might implement this method in your delegate if you want to be notified that a local notification occurred. For example, a calendar app might use local notifications to alert the user to upcoming events.

If the user chooses to open the app when a local notification occurs, the launch options dictionary passed to the [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) and [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) methods contains the [UIApplicationLaunchOptionsLocalNotificationKey](../uiapplication/launchoptionskey/localnotification.md) key. This method is called at some point after your delegate’s [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) method.

## See Also

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
- [- application:didReceiveRemoteNotification:](<application(__didreceiveremotenotification_).md>) — Called when your app has received a remote notification. _(deprecated)_
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
