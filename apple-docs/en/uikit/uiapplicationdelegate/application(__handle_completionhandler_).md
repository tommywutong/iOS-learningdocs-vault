---
title: 'application(_:handle:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（14.0 起废弃）, iPadOS 11.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, tvOS 11.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:handle:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handle:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ahandle%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:817c1259e3751896'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:handle:completionHandler:)

<sub>Instance Method</sub>

Asks the delegate to handle the specified SiriKit intent directly.

> [!warning] Deprecated
> Use [- application:handlerForIntent:](<application(__handlerfor_).md>) instead to provide an object to resolve, confirm, and handle intents in your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, handle intent: INIntent, completionHandler: @escaping (INIntentResponse) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, handle intent: INIntent) async -> INIntentResponse
```

## Parameters

- `application` — The shared app object.

- `intent` — The intent object that contains information about the SiriKit request. Use this object to identify what the user intends and what kind of response to provide.

- `completionHandler` — The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter: - **intentResponse** — The response object you create to report the status of the request. The exact type of this object must correspond to the type of intent delivered. For example, if the `intent` parameter contains an [INStartWorkoutIntent](../../intents/instartworkoutintent.md) object, you must create an [INStartWorkoutIntentResponse](../../intents/instartworkoutintentresponse.md) object. This parameter must not be `nil`.

## Discussion

With this method, an app can handle an intent directly, rather than handling it in the app’s Intent extension. You might use this method to implement workflows that you can’t implement easily in your extension. For example, you might use it to start or manage a user’s workout session. If your app isn’t running, SiriKit launches your app in the background so that the Siri interface remains active.

Your Intents app extension is still responsible for resolving and confirming the intent details. Your extension’s [handler(for:)](<../../intents/inintenthandlerproviding/handler(for_).md>) method must create a response object that resolves and confirms the intent details. In the response object’s `handle(intent:completion:)` implementation, return a response object with a status code of `failureRequiringAppLaunch`. Upon receiving your response, SiriKit launches the app and calls [- application:handleIntent:completionHandler:](<application(__handle_completionhandler_).md>). In your implementation of this app delegate method, handle the intent by performing the user’s intended action if possible. Then call the provided completion handler with a response object that indicates if your app performed the intent or provides a reason it could not. For details about how to handle a specific intent, see the class reference for that intent in [SiriKit](../../sirikit.md).

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
- [- application:performFetchWithCompletionHandler:](<application(__performfetchwithcompletionhandler_).md>) — Tells the app that it can begin a fetch operation if it has data to download. _(deprecated)_
- [- application:shouldSaveApplicationState:](<application(__shouldsaveapplicationstate_).md>) — Asks the delegate whether to preserve the app’s state. _(deprecated)_
