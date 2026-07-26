---
title: enabledRemoteNotificationTypes()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/enabledremotenotificationtypes()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/enabledremotenotificationtypes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/enabledremotenotificationtypes%28%29.json'
content_hash: 'sha256:70b91974495f9a2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# enabledRemoteNotificationTypes()

<sub>Instance Method</sub>

Returns the types of notifications the app accepts.

> [!warning] Deprecated
> Use the [registeredForRemoteNotifications](isregisteredforremotenotifications.md) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func enabledRemoteNotificationTypes() -> UIRemoteNotificationType
```

## Return Value

A bit mask whose values indicate the types of notifications the user has requested for the app. See [UIRemoteNotificationType](../uiremotenotificationtype.md) for valid bit-mask values.

## Discussion

The values in the returned bit mask indicate the types of notifications currently enabled for the app. These types are first set when the app calls the [- registerForRemoteNotificationTypes:](<registerforremotenotifications(matching_).md>) method to register itself with Apple Push Notification service. Thereafter, the user may modify these accepted notification types in the Notifications preference of the Settings app. This method returns those initial or modified values. iOS does not display or play notification types specified in the notification payload that are not one of the enabled types. For example, the app might accept icon-badging as a form of notification, but might reject sounds and alert messages, even if they are specified in the notification payload.

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
