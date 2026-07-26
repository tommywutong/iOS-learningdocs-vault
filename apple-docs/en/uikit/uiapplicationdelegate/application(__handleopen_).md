---
title: 'application(_:handleOpen:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:handleopen:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handleopen:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ahandleopen%3A%29.json'
content_hash: 'sha256:4679afd799894b79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:handleOpen:)

<sub>Instance Method</sub>

Asks the delegate to open a resource identified by URL.

> [!warning] Deprecated
> Use the [- application:openURL:options:](<application(__open_options_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, handleOpen url: URL) -> Bool
```

## Parameters

- `application` — Your singleton app object.

- `url` — An object representing a URL (Universal Resource Locator). See the appendix of [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072) for Apple-registered schemes for URLs.

## Return Value

[true](../../swift/true.md) if the delegate successfully handled the request; [false](../../swift/false.md) if the attempt to handle the URL failed.

## Discussion

If the delegate also implements the [- application:openURL:sourceApplication:annotation:](<application(__open_sourceapplication_annotation_).md>) method, that method is called instead of this one.

This method is not called if the delegate returns [false](../../swift/false.md) from both the [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) and [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) methods. (If only one of the two methods is implemented, its return value determines whether this method is called.) If your app implements the [- applicationDidFinishLaunching:](<applicationdidfinishlaunching(__).md>) method instead of [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>), this method is called to open the specified URL after the app has been initialized.

If a URL arrives while your app is suspended or running in the background, the system moves your app to the foreground prior to calling this method.

There is no equivalent notification for this delegation method.

## See Also

### Related Documentation

- [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process has begun.
- [- openURL:](<../uiapplication/openurl(__).md>) — Attempts to open the resource at the specified URL. _(deprecated)_

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
- [- application:didReceiveLocalNotification:](<application(__didreceive_).md>) — Sent to the delegate when a running app receives a local notification. _(deprecated)_
- [- application:didReceiveRemoteNotification:](<application(__didreceiveremotenotification_).md>) — Called when your app has received a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<application(__handleactionwithidentifier_for_completionhandler_).md>) — Called when your app has been activated because user selected a custom action from the alert panel of a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_for_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) — Tells the app delegate to perform the custom action specified by a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_forremotenotification_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a remote notification. _(deprecated)_
- [- application:openURL:sourceApplication:annotation:](<application(__open_sourceapplication_annotation_).md>) — Asks the delegate to open a resource identified by a URL. _(deprecated)_
- [- application:willChangeStatusBarOrientation:duration:](<application(__willchangestatusbarorientation_duration_).md>) — Tells the delegate when the interface orientation of the status bar is about to change. _(deprecated)_
- [- application:didChangeStatusBarOrientation:](<application(__didchangestatusbarorientation_).md>) — Tells the delegate when the interface orientation of the status bar has changed. _(deprecated)_
- [- application:willChangeStatusBarFrame:](<application(__willchangestatusbarframe_).md>) — Tells the delegate when the frame of the status bar is about to change. _(deprecated)_
- [- application:didChangeStatusBarFrame:](<application(__didchangestatusbarframe_).md>) — Tells the delegate when the frame of the status bar has changed. _(deprecated)_
- [- application:handleIntent:completionHandler:](<application(__handle_completionhandler_).md>) — Asks the delegate to handle the specified SiriKit intent directly. _(deprecated)_
- [- application:performFetchWithCompletionHandler:](<application(__performfetchwithcompletionhandler_).md>) — Tells the app that it can begin a fetch operation if it has data to download. _(deprecated)_
- [- application:shouldSaveApplicationState:](<application(__shouldsaveapplicationstate_).md>) — Asks the delegate whether to preserve the app’s state. _(deprecated)_
