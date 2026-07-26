---
title: 'scheduleLocalNotification(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/schedulelocalnotification(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/schedulelocalnotification(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/schedulelocalnotification%28_%3A%29.json'
content_hash: 'sha256:fe8af6ee58a63870'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# scheduleLocalNotification(_:)

<sub>Instance Method</sub>

Schedules a local notification for delivery at its encapsulated date and time.

> [!warning] Deprecated
> Use the [UNUserNotificationCenter](../../usernotifications/unusernotificationcenter.md) class to schedule local notifications instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func scheduleLocalNotification(_ notification: UILocalNotification)
```

## Parameters

- `notification` — The local notification object that you want to schedule. This object contains information about when to deliver the notification and what to do when that date occurs. The system keeps a copy of this object so you may release the object once it is scheduled.

## Discussion

Prior to scheduling any local notifications, you must call the [- registerUserNotificationSettings:](<registerusernotificationsettings(__).md>) method to let the system know what types of alerts, if any, you plan to display to the user.

## See Also

### Deprecated methods

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — Asks the system to activate an existing scene, or create a new scene and associate it with your app. _(deprecated)_
- [- beginIgnoringInteractionEvents](<beginignoringinteractionevents().md>) — Tells the receiver to suspend the handling of touch-related events. _(deprecated)_
- [- endIgnoringInteractionEvents](<endignoringinteractionevents().md>) — Tells the receiver to resume the handling of touch-related events. _(deprecated)_
- [- setMinimumBackgroundFetchInterval:](<setminimumbackgroundfetchinterval(__).md>) — Specifies the minimum amount of time that must elapse between background fetch operations. _(deprecated)_
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
