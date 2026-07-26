---
title: 'application(_:handleActionWithIdentifier:for:withResponseInfo:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:handleactionwithidentifier:for:withresponseinfo:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleactionwithidentifier:for:withresponseinfo:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ahandleactionwithidentifier%3Afor%3Awithresponseinfo%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:7a1ef5b60e5a5a2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:handleActionWithIdentifier:for:withResponseInfo:completionHandler:)

<sub>Instance Method</sub>

Called when your app has been activated by the user selecting an action from a local notification.

> [!warning] Deprecated
> Use [userNotificationCenter(_:didReceive:withCompletionHandler:)](<../../usernotifications/unusernotificationcenterdelegate/usernotificationcenter(__didreceive_withcompletionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, for notification: UILocalNotification, withResponseInfo responseInfo: [AnyHashable : Any], completionHandler: @escaping () -> Void)
```

<sub>Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, handleActionWithIdentifier identifier: String?, for notification: UILocalNotification, withResponseInfo responseInfo: [AnyHashable : Any]) async
```

## Parameters

- `application` — The app object that was activated for the user-selected action.

- `identifier` — The identifier for the custom action.

- `notification` — The local notification object that was triggered.

- `responseInfo` — The data dictionary sent by the action.

- `completionHandler` — A block that you must call when you are finished performing the action.

## Discussion

A `nil` value in the `identifier` parameter indicates the default action.

Call the completion handler as soon as you’ve finished handling the action.

## See Also

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
- [- application:didReceiveLocalNotification:](<application(__didreceive_).md>) — Sent to the delegate when a running app receives a local notification. _(deprecated)_
- [- application:didReceiveRemoteNotification:](<application(__didreceiveremotenotification_).md>) — Called when your app has received a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<application(__handleactionwithidentifier_for_completionhandler_).md>) — Called when your app has been activated because user selected a custom action from the alert panel of a local notification. _(deprecated)_
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
