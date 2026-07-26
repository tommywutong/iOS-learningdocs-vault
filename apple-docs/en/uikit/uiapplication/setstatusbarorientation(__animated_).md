---
title: 'setStatusBarOrientation(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/setstatusbarorientation(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/setstatusbarorientation(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setstatusbarorientation%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:01a74095ba112cc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# setStatusBarOrientation(_:animated:)

<sub>Instance Method</sub>

Sets the app’s status bar to the specified orientation, optionally animating the transition.

> [!warning] Deprecated
> Use [statusBarManager](../uiwindowscene/statusbarmanager.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setStatusBarOrientation(_ interfaceOrientation: UIInterfaceOrientation, animated: Bool)
```

## Parameters

- `interfaceOrientation` — A specific orientation of the status bar. See [UIInterfaceOrientation](../uiinterfaceorientation.md) for details. The default value is [UIInterfaceOrientationPortrait](../uiinterfaceorientation/portrait.md).

- `animated` — [true](../../swift/true.md) if the transition to the new orientation should be animated; [false](../../swift/false.md) if it should be immediate, without animation.

## Discussion

Calling this method changes the value of the  [statusBarOrientation](statusbarorientation.md) property and rotates the status bar, animating the transition if animated is [true](../../swift/true.md) . If your app has rotatable window content, however, you should not arbitrarily set status-bar orientation using this method. The status-bar orientation set by this method does not change if the device changes orientation.

## See Also

### Related Documentation

- [statusBarOrientationAnimationDuration](statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarOrientation](statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_

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
- [- registerUserNotificationSettings:](<registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_
- [- registerForRemoteNotificationTypes:](<registerforremotenotifications(matching_).md>) — Register to receive remote notifications of the specified types via Apple Push Notification service. _(deprecated)_
