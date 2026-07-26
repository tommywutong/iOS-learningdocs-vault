---
title: 'requestSceneSessionActivation(_:userActivity:options:errorHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/requestscenesessionactivation%28_%3Auseractivity%3Aoptions%3Aerrorhandler%3A%29.json'
content_hash: 'sha256:f4f13e59e311ea95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# requestSceneSessionActivation(_:userActivity:options:errorHandler:)

<sub>Instance Method</sub>

Asks the system to activate an existing scene, or create a new scene and associate it with your app.

> [!warning] Deprecated
> Use [activateSceneSession(for:errorHandler:)](<activatescenesession(for_errorhandler_).md>) (Swift) or [activateSceneSessionForRequest:errorHandler:](activatescenesessionforrequest_errorhandler_.md) (Objective-C) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestSceneSessionActivation(_ sceneSession: UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)? = nil)
```

## Parameters

- `sceneSession` — The session whose scene you want to activate. Specify `nil` when you want the system to create a new scene for your app.

- `userActivity` — A user activity object to dispatch to the session’s scene. Use this object to communicate details about a task you want the scene to perform.

- `options` — Information for the system to use when creating or activating the scene. For information about how to create this object, see [ActivationRequestOptions](../uiscene/activationrequestoptions.md).

- `errorHandler` — An error handler block to execute if a problem occurs. The method doesn’t execute this block when it successfully activates the scene. This block has no return value and has the following parameter: - **error** — The [NSError](../../foundation/nserror.md) object describing the problem that occurred.

## Discussion

Call this method when you want the system to display one of your app’s scenes. For example, you might call this method to dispatch work to the scene in the form of an [NSUserActivity](../../foundation/nsuseractivity.md) object. When activating an existing session whose scene is no longer in memory, the system creates a new scene and connects it to your app. Similarly, specifying `nil` for the `sceneSession` parameter causes the system to create a new scene and corresponding session.

## See Also

### Deprecated methods

- [- beginIgnoringInteractionEvents](<beginignoringinteractionevents().md>) — Tells the receiver to suspend the handling of touch-related events. _(deprecated)_
- [- endIgnoringInteractionEvents](<endignoringinteractionevents().md>) — Tells the receiver to resume the handling of touch-related events. _(deprecated)_
- [- setMinimumBackgroundFetchInterval:](<setminimumbackgroundfetchinterval(__).md>) — Specifies the minimum amount of time that must elapse between background fetch operations. _(deprecated)_
- [- scheduleLocalNotification:](<schedulelocalnotification(__).md>) — Schedules a local notification for delivery at its encapsulated date and time. _(deprecated)_
- [- presentLocalNotificationNow:](<presentlocalnotificationnow(__).md>) — Presents a local notification immediately. _(deprecated)_
- [- cancelLocalNotification:](<cancellocalnotification(__).md>) — Cancels the delivery of the specified scheduled local notification. _(deprecated)_
- [- cancelAllLocalNotifications](<cancelalllocalnotifications().md>) — Cancels the delivery of all scheduled local notifications. _(deprecated)_
- [- setKeepAliveTimeout:handler:](<setkeepalivetimeout(__handler_).md>) — Configures a periodic handler for VoIP apps in older versions of iOS. _(deprecated)_
- [UIMinimumKeepAliveTimeout](../uiminimumkeepalivetimeout.md) — The minimum amount of time (measured in seconds) an app may run a critical background task in the background. _(deprecated)_
- [- clearKeepAliveTimeout](<clearkeepalivetimeout().md>) — Removes a previously installed periodic handler block. _(deprecated)_
- [- setStatusBarHidden:withAnimation:](<setstatusbarhidden(__with_).md>) — Hides or shows the status bar, optionally animating the transition. _(deprecated)_
- [- setStatusBarStyle:animated:](<setstatusbarstyle(__animated_).md>) — Sets the style of the status bar, optionally animating the transition to the new style. _(deprecated)_
- [- setStatusBarOrientation:animated:](<setstatusbarorientation(__animated_).md>) — Sets the app’s status bar to the specified orientation, optionally animating the transition. _(deprecated)_
- [- registerUserNotificationSettings:](<registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_
- [- registerForRemoteNotificationTypes:](<registerforremotenotifications(matching_).md>) — Register to receive remote notifications of the specified types via Apple Push Notification service. _(deprecated)_
