---
title: 'setKeepAliveTimeout(_:handler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（9.0 起废弃）, iPadOS 4.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/setkeepalivetimeout(_:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/setkeepalivetimeout(_:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/setkeepalivetimeout%28_%3Ahandler%3A%29.json'
content_hash: 'sha256:1bdf03c0a44566c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# setKeepAliveTimeout(_:handler:)

<sub>Instance Method</sub>

Configures a periodic handler for VoIP apps in older versions of iOS.

> [!warning] Deprecated
> This legacy VoIP API was deprecated in iOS 10.0. Use [PushKit](../../pushkit.md) to develop VoIP apps.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setKeepAliveTimeout(_ timeout: TimeInterval, handler keepAliveHandler: (() -> Void)? = nil) -> Bool
```

## Parameters

- `timeout` — The maximum interval (measured in seconds) at which your app should be woken up to check its VoIP connection. The minimum acceptable timeout value is 600 seconds.

- `keepAliveHandler` — A block that performs the tasks needed to maintain your VoIP network connection. Setting this parameter to `nil` releases the current handler block and prevents UIKit from scheduling the next wake.

## Return Value

[true](../../swift/true.md) if the handler was installed or [false](../../swift/false.md) if it was not.

## Discussion

In iOS 8 and later, voice-over-IP (VoIP) apps register for [- registerForRemoteNotifications](<registerforremotenotifications().md>) remote notifications instead of using this method. Using remote notifications eliminates the need for a timeout handler to check in with the VoIP service. Instead, when a calls arrives for the user, the VoIP service sends a VoIP remote notification to the user’s device. Upon receiving this notification, the device launches or wakes the app as needed so that it can handle the incoming call.

In iOS 7 and earlier, VoIP apps use this method to install a handler whose job is to maintain the app’s network connection with a VoIP server. This handler is guaranteed to be called before the specified timeout value but may be called at a slightly different time interval in order to better align execution of your handler with other system tasks, and thereby save power. Your handler has a maximum of 10 seconds to perform any needed tasks and exit. If it does not exit before time expires, the app is suspended.

Timeout values and handlers are not persisted between app launches. Therefore, if your app is terminated for any reason, you must reinstall the handler during the next launch cycle.

For calls to this method to succeed, the app must have the `voip` value in the array associated with the `UIBackgroundModes` key in its `Info.plist` file. Calling this method replaces the previously installed handler and timeout values, if any.

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
- [UIMinimumKeepAliveTimeout](../uiminimumkeepalivetimeout.md) — The minimum amount of time (measured in seconds) an app may run a critical background task in the background. _(deprecated)_
- [- clearKeepAliveTimeout](<clearkeepalivetimeout().md>) — Removes a previously installed periodic handler block. _(deprecated)_
- [- setStatusBarHidden:withAnimation:](<setstatusbarhidden(__with_).md>) — Hides or shows the status bar, optionally animating the transition. _(deprecated)_
- [- setStatusBarStyle:animated:](<setstatusbarstyle(__animated_).md>) — Sets the style of the status bar, optionally animating the transition to the new style. _(deprecated)_
- [- setStatusBarOrientation:animated:](<setstatusbarorientation(__animated_).md>) — Sets the app’s status bar to the specified orientation, optionally animating the transition. _(deprecated)_
- [- registerUserNotificationSettings:](<registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_
- [- registerForRemoteNotificationTypes:](<registerforremotenotifications(matching_).md>) — Register to receive remote notifications of the specified types via Apple Push Notification service. _(deprecated)_
