---
title: 'setStatusBarStyle(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/setstatusbarstyle(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarstyle(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setstatusbarstyle%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:07b871f4e6c07189'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# setStatusBarStyle(_:animated:)

<sub>Instance Method</sub>

Sets the style of the status bar, optionally animating the transition to the new style.

> [!warning] Deprecated
> Use [preferredStatusBarStyle](../uiviewcontroller/preferredstatusbarstyle.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setStatusBarStyle(_ statusBarStyle: UIStatusBarStyle, animated: Bool)
```

## Parameters

- `statusBarStyle` — A constant that specifies a style for the status bar. See the descriptions of the constants in [UIStatusBarStyle](../uistatusbarstyle.md) for details.

- `animated` — [true](../../swift/true.md) if the transition to the new style should be animated; otherwise [false](../../swift/false.md) .

## Discussion

The animation slides the status bar out toward the top of the interface.

In iOS 7 and later, status bar behavior is determined by view controllers, and so calling this method has no effect by default. When view controller-based status bar appearance is disabled, this method behaves normally. To opt out of the view controller-based status bar appearance behavior, you must add the `UIViewControllerBasedStatusBarAppearance` key with a value of [false](../../swift/false.md) to your app’s `Info.plist` file, but doing so is not recommended.

## See Also

### Related Documentation

- [statusBarStyle](statusbarstyle.md) — The current style of the status bar. _(deprecated)_

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
- [- setStatusBarOrientation:animated:](<setstatusbarorientation(__animated_).md>) — Sets the app’s status bar to the specified orientation, optionally animating the transition. _(deprecated)_
- [- registerUserNotificationSettings:](<registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_
- [- registerForRemoteNotificationTypes:](<registerforremotenotifications(matching_).md>) — Register to receive remote notifications of the specified types via Apple Push Notification service. _(deprecated)_
