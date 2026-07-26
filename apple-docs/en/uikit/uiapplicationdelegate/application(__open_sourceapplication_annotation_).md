---
title: 'application(_:open:sourceApplication:annotation:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+（9.0 起废弃）, iPadOS 4.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:open:sourceapplication:annotation:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:open:sourceapplication:annotation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Aopen%3Asourceapplication%3Aannotation%3A%29.json'
content_hash: 'sha256:c68e7c73d3a2766a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:open:sourceApplication:annotation:)

<sub>Instance Method</sub>

Asks the delegate to open a resource identified by a URL.

> [!warning] Deprecated
> Use [- application:openURL:options:](<application(__open_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool
```

## Parameters

- `application` — Your singleton app object.

- `url` — The URL resource to open. This resource can be a network resource or a file. For information about the Apple-registered URL schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

- `sourceApplication` — The bundle ID of the app that is requesting your app to open the URL (`url`).

- `annotation` — A [Property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) supplied by the source app to communicate information to the receiving app.

## Return Value

[true](../../swift/true.md) if the delegate successfully handled the request or [false](../../swift/false.md) if the attempt to open the URL resource failed.

## Discussion

Your implementation of this method should open the specified URL and update its user interface accordingly. If your app had to be launched to open the URL, the app calls the [- application:willFinishLaunchingWithOptions:](<application(__willfinishlaunchingwithoptions_).md>) and [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) methods first, followed by this method. The return values of those methods can be used to prevent this method from being called. (If the app is already running, only this method is called.)

If the URL refers to a file that was opened through a document interaction controller, the `annotation` parameter may contain additional data that the source app wanted to send along with the URL. The format of this data is defined by the app that sent it but the data must consist of objects that can be put into a property list.

Files sent to your app through AirDrop or a document interaction controller are placed in the `Documents/Inbox` directory of your app’s home directory. Your app has permission to read and delete files in this directory but does not have permission to write to them. If you want to modify a file, you must move it to a different directory first. In addition, files in that directory are usually encrypted using data protection. If the file is protected and the user locks the device before this method is called, you will be unable to read the file’s contents immediately. In that case, you should save the URL and try to open the file later rather than return [false](../../swift/false.md) from this method. Use the [protectedDataAvailable](../uiapplication/isprotecteddataavailable.md) property of the app object to determine if data protection is currently enabled.

There is no matching notification for this method.

## See Also

### Related Documentation

- [- application:didFinishLaunchingWithOptions:](<application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [- openURL:](<../uiapplication/openurl(__).md>) — Attempts to open the resource at the specified URL. _(deprecated)_

### Deprecated

- [- application:didRegisterUserNotificationSettings:](<application(__didregister_).md>) — Called to tell the delegate the types of local and remote notifications that can be used to get the user’s attention. _(deprecated)_
- [- application:didReceiveLocalNotification:](<application(__didreceive_).md>) — Sent to the delegate when a running app receives a local notification. _(deprecated)_
- [- application:didReceiveRemoteNotification:](<application(__didreceiveremotenotification_).md>) — Called when your app has received a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<application(__handleactionwithidentifier_for_completionhandler_).md>) — Called when your app has been activated because user selected a custom action from the alert panel of a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forLocalNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_for_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a local notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) — Tells the app delegate to perform the custom action specified by a remote notification. _(deprecated)_
- [- application:handleActionWithIdentifier:forRemoteNotification:withResponseInfo:completionHandler:](<application(__handleactionwithidentifier_forremotenotification_withresponseinfo_completionhandler_).md>) — Called when your app has been activated by the user selecting an action from a remote notification. _(deprecated)_
- [- application:handleOpenURL:](<application(__handleopen_).md>) — Asks the delegate to open a resource identified by URL. _(deprecated)_
- [- application:willChangeStatusBarOrientation:duration:](<application(__willchangestatusbarorientation_duration_).md>) — Tells the delegate when the interface orientation of the status bar is about to change. _(deprecated)_
- [- application:didChangeStatusBarOrientation:](<application(__didchangestatusbarorientation_).md>) — Tells the delegate when the interface orientation of the status bar has changed. _(deprecated)_
- [- application:willChangeStatusBarFrame:](<application(__willchangestatusbarframe_).md>) — Tells the delegate when the frame of the status bar is about to change. _(deprecated)_
- [- application:didChangeStatusBarFrame:](<application(__didchangestatusbarframe_).md>) — Tells the delegate when the frame of the status bar has changed. _(deprecated)_
- [- application:handleIntent:completionHandler:](<application(__handle_completionhandler_).md>) — Asks the delegate to handle the specified SiriKit intent directly. _(deprecated)_
- [- application:performFetchWithCompletionHandler:](<application(__performfetchwithcompletionhandler_).md>) — Tells the app that it can begin a fetch operation if it has data to download. _(deprecated)_
- [- application:shouldSaveApplicationState:](<application(__shouldsaveapplicationstate_).md>) — Asks the delegate whether to preserve the app’s state. _(deprecated)_
