---
title: 'openURL(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（10.0 起废弃）, iPadOS 2.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（10.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplication/openurl(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openurl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openurl%28_%3A%29.json'
content_hash: 'sha256:c532ba53dcf926af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# openURL(_:)

<sub>Instance Method</sub>

Attempts to open the resource at the specified URL.

> [!warning] Deprecated
> Calling this method has no effect. Use the [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func openURL(_ url: URL) -> Bool
```

## Parameters

- `url` — A URL (Universal Resource Locator). UIKit supports many common schemes, including the `http`, `https`, `tel`, `facetime`, and `mailto` schemes. You can also employ custom URL schemes associated with apps installed on the device.

## Return Value

[true](../../swift/true.md) if the resource located by the URL was successfully opened; otherwise [false](../../swift/false.md).

## Discussion

The URL you pass to this method can identify a resource in the app that calls the method, or a resource to be handled by another app. If the resource is to be handled another app, invoking this method might cause the calling app to quit so the other can launch.

To check if there is an installed app that can handle a scheme, call the [- canOpenURL:](<canopenurl(__).md>) method before calling this one. Be sure to read the description of that method for an important note about registering the schemes you want to employ.

## See Also

### Related Documentation

- [- application:handleOpenURL:](<../uiapplicationdelegate/application(__handleopen_).md>) — Asks the delegate to open a resource identified by URL. _(deprecated)_
- [- canOpenURL:](<canopenurl(__).md>) — Returns a Boolean value that indicates whether an app is available to handle a URL scheme. _(deprecated)_

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
