---
title: 'setMinimumBackgroundFetchInterval(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 11.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/setminimumbackgroundfetchinterval(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/setminimumbackgroundfetchinterval(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setminimumbackgroundfetchinterval%28_%3A%29.json'
content_hash: 'sha256:d591cbdcc04379cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# setMinimumBackgroundFetchInterval(_:)

<sub>Instance Method</sub>

Specifies the minimum amount of time that must elapse between background fetch operations.

> [!warning] Deprecated
> For apps supporting iOS 13 and higher use [BGAppRefreshTask](../../backgroundtasks/bgapprefreshtask.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setMinimumBackgroundFetchInterval(_ minimumBackgroundFetchInterval: TimeInterval)
```

## Parameters

- `minimumBackgroundFetchInterval` — The minimum number of seconds that must elapse before another background fetch can be initiated. This value is advisory only and does not indicate the exact amount of time expected between fetch operations.

## Discussion

This property has no effect for apps that do not have the `UIBackgroundModes` key with the `fetch` value in its `Info.plist` file.

The default fetch interval for apps is [UIApplicationBackgroundFetchIntervalNever](backgroundfetchintervalnever.md). Therefore, you must call this method and set a fetch interval before your app is given background execution time.

## See Also

### Deprecated methods

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — Asks the system to activate an existing scene, or create a new scene and associate it with your app. _(deprecated)_
- [- beginIgnoringInteractionEvents](<beginignoringinteractionevents().md>) — Tells the receiver to suspend the handling of touch-related events. _(deprecated)_
- [- endIgnoringInteractionEvents](<endignoringinteractionevents().md>) — Tells the receiver to resume the handling of touch-related events. _(deprecated)_
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
