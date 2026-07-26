---
title: 'registerForRemoteNotifications(matching:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/registerforremotenotifications(matching:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/registerforremotenotifications(matching:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/registerforremotenotifications%28matching%3A%29.json'
content_hash: 'sha256:205a58ca88de0903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# registerForRemoteNotifications(matching:)

<sub>Instance Method</sub>

Register to receive remote notifications of the specified types via Apple Push Notification service.

> [!warning] Deprecated
> Use the [- registerForRemoteNotifications](<registerforremotenotifications().md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func registerForRemoteNotifications(matching types: UIRemoteNotificationType)
```

## Parameters

- `types` — A bit mask specifying the types of notifications the app accepts. For a list of values, see [UIRemoteNotificationType](../uiremotenotificationtype.md).

## Discussion

When you send this message, the device initiates the registration process with Apple Push Notification service. If it succeeds, the app delegate receives a device token in the [- application:didRegisterForRemoteNotificationsWithDeviceToken:](<../uiapplicationdelegate/application(__didregisterforremotenotificationswithdevicetoken_).md>) method; if registration doesn’t succeed, the delegate is informed via the [- application:didFailToRegisterForRemoteNotificationsWithError:](<../uiapplicationdelegate/application(__didfailtoregisterforremotenotificationswitherror_).md>) method. If the app delegate receives a device token, it should connect with its provider and pass it the token.

iOS does not display or play notification types specified in the notification payload that are not one of the requested ones. For example, if alert messages are not one of the accepted notification types, iOS does not display an alert even if one is specified in the notification payload. To find out what the app’s current notification types are, call the [- enabledRemoteNotificationTypes](<enabledremotenotificationtypes().md>) method.

## See Also

### Deprecated methods

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — Asks the system to activate an existing scene, or create a new scene and associate it with your app. _(deprecated)_
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
