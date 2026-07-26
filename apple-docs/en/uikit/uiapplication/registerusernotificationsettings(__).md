---
title: 'registerUserNotificationSettings(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/registerusernotificationsettings(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/registerusernotificationsettings(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/registerusernotificationsettings%28_%3A%29.json'
content_hash: 'sha256:a81c8278b33f8f76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# registerUserNotificationSettings(_:)

<sub>Instance Method</sub>

Registers your preferred options for notifying the user.

> [!warning] Deprecated
> Use [requestAuthorization(options:completionHandler:)](<../../usernotifications/unusernotificationcenter/requestauthorization(options_completionhandler_).md>) and [setNotificationCategories(_:)](<../../usernotifications/unusernotificationcenter/setnotificationcategories(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func registerUserNotificationSettings(_ notificationSettings: UIUserNotificationSettings)
```

## Parameters

- `notificationSettings` — The types of notifications that your app wants to use. You also use this object to specify custom actions that can be initiated by the user from an alert displayed in response to a local or remote notification.

## Discussion

If your app displays alerts, play sounds, or badges its icon, you must call this method during your launch cycle to request permission to alert the user in these ways. (You must also make this request if you want to set the [applicationIconBadgeNumber](applicationiconbadgenumber.md) property directly.) Typically, you make this request if your app uses local or remote notifications to alert the user to new information involving your app. The first time your app launches and calls this method, the system asks the user whether your app should be allowed to deliver notifications and stores the response. Thereafter, the system uses the stored response to determine the actual types of notifications you may use.

After calling this method, the app calls the [- application:didRegisterUserNotificationSettings:](<../uiapplicationdelegate/application(__didregister_).md>) method of its app delegate to report the results. You can use that method to determine if your request was granted or denied by the user.

It is recommended that you call this method before you schedule any local notifications or register with the push notification service. Apps that support custom actions must include all of their supported actions in the `notificationSettings` object.

## See Also

### Related Documentation

- [currentUserNotificationSettings](currentusernotificationsettings.md) — Returns the user notification settings for the app. _(deprecated)_

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
- [- registerForRemoteNotificationTypes:](<registerforremotenotifications(matching_).md>) — Register to receive remote notifications of the specified types via Apple Push Notification service. _(deprecated)_
