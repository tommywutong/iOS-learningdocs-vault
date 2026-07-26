---
title: 'application(_:didRegister:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:didregister:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didregister:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adidregister%3A%29.json'
content_hash: 'sha256:edb907c934b0d66d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didRegister:)

<sub>Instance Method</sub>

Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention.

> [!warning] Deprecated
> Use [requestAuthorization(options:completionHandler:)](<../../usernotifications/unusernotificationcenter/requestauthorization(options_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, didRegister notificationSettings: UIUserNotificationSettings)
```

## Parameters

- `application` — The app object that registered the user notification settings.

- `notificationSettings` — The user’s specified notification settings for your app. The settings in this object may be different than the ones you originally requested.

## Discussion

Apps that use local or remote notifications to alert the user to new information must register the types of notifications they want to use by calling the [- registerUserNotificationSettings:](<../uiapplication/registerusernotificationsettings(__).md>) method of the app object. The system compares your app’s request with the user’s preferences to determine the types of local and remote notifications allowed, and returns the results to your app by calling this method. Check the contents of the `notificationSettings` parameter whenever this method is called.

Because the user can change notification settings in the Settings app at any time, call the [currentUserNotificationSettings](../uiapplication/currentusernotificationsettings.md) method before your app performs work to prepare a notification for presentation.

The first time you register your app’s preferred notification types, the system asks the user whether your app should be allowed to deliver notifications and stores the user’s response. The system does not prompt the user on subsequent calls to the [- registerUserNotificationSettings:](<../uiapplication/registerusernotificationsettings(__).md>) method, but the user can always change notification preferences using Settings.

A user’s notification settings control only whether the system _displays_ local or remote notifications onscreen. Regardless of the notification settings, local and remote notifications are delivered to your app at the appropriate times.

## See Also

### Deprecated

- [- application:didReceiveLocalNotification:](<application(__didreceive_).md>) — Sent to the delegate when a running app receives a local notification. _(deprecated)_
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
