---
title: 'application(_:shouldRestoreApplicationState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（13.2 起废弃）, iPadOS 6.0+（13.2 起废弃）, Mac Catalyst 13.1+（13.2 起废弃）, tvOS（13.2 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:shouldrestoreapplicationstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldrestoreapplicationstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ashouldrestoreapplicationstate%3A%29.json'
content_hash: 'sha256:a6a32e6e12051acb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:shouldRestoreApplicationState:)

<sub>Instance Method</sub>

Asks the delegate whether to restore the app’s saved state.

> [!warning] Deprecated
> Use [- application:shouldRestoreSecureApplicationState:](<application(__shouldrestoresecureapplicationstate_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func application(_ application: UIApplication, shouldRestoreApplicationState coder: NSCoder) -> Bool
```

## Parameters

- `application` — Your singleton app object.

- `coder` — The keyed archiver containing the app’s previously saved state information.

## Return Value

[true](../../swift/true.md) if the app’s state should be restored; otherwise, [false](../../swift/false.md).

## Discussion

Apps must implement this method and the [- application:shouldSaveApplicationState:](<application(__shouldsaveapplicationstate_).md>) method for state preservation to occur. In addition, your implementation of this method must return [true](../../swift/true.md) each time UIKit tries to restore the state of your app. You can use the information in the provided coder object to decide whether or not to proceed with state restoration. For example, you might return [false](../../swift/false.md) if the data in the coder is from a different version of your app and can’t be effectively restored to the current version.

## See Also

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
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
