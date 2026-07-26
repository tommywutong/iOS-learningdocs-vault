---
title: 'application(_:shouldSaveApplicationState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（13.2 起废弃）, iPadOS 6.0+（13.2 起废弃）, Mac Catalyst 13.1+（13.2 起废弃）, tvOS（13.2 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:shouldsaveapplicationstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldsaveapplicationstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ashouldsaveapplicationstate%3A%29.json'
content_hash: 'sha256:c50f5b9ce95bcfe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:shouldSaveApplicationState:)

<sub>Instance Method</sub>

Asks the delegate whether to preserve the app’s state.

> [!warning] Deprecated
> Use [- application:shouldSaveSecureApplicationState:](<application(__shouldsavesecureapplicationstate_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func application(_ application: UIApplication, shouldSaveApplicationState coder: NSCoder) -> Bool
```

## Parameters

- `application` — Your singleton app object.

- `coder` — The keyed archiver into which you can put high-level state information.

## Return Value

[true](../../swift/true.md) if the app’s state should be preserved; otherwise, [false](../../swift/false.md).

## Discussion

Apps must implement this method and the [- application:shouldRestoreApplicationState:](<application(__shouldrestoreapplicationstate_).md>) method for state preservation to occur. In addition, your implementation of this method must return [true](../../swift/true.md) each time UIKit tries to preserve the state of your app. You can return [false](../../swift/false.md) to disable state preservation temporarily. For example, during testing, you could disable state preservation to test specific code paths.

You can add version information or any other contextual data to the provided coder object as needed. During restoration, you can use that information to help decide whether or not to proceed with restoring your app to its previous state.

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
