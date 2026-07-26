---
title: Deprecated symbols
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication-deprecated-symbols.json'
content_hash: 'sha256:682b531b95a533fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [UIApplication](uiapplication.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Deprecated methods

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — Asks the system to activate an existing scene, or create a new scene and associate it with your app. _(deprecated)_
- [- beginIgnoringInteractionEvents](<uiapplication/beginignoringinteractionevents().md>) — Tells the receiver to suspend the handling of touch-related events. _(deprecated)_
- [- endIgnoringInteractionEvents](<uiapplication/endignoringinteractionevents().md>) — Tells the receiver to resume the handling of touch-related events. _(deprecated)_
- [- setMinimumBackgroundFetchInterval:](<uiapplication/setminimumbackgroundfetchinterval(__).md>) — Specifies the minimum amount of time that must elapse between background fetch operations. _(deprecated)_
- [- scheduleLocalNotification:](<uiapplication/schedulelocalnotification(__).md>) — Schedules a local notification for delivery at its encapsulated date and time. _(deprecated)_
- [- presentLocalNotificationNow:](<uiapplication/presentlocalnotificationnow(__).md>) — Presents a local notification immediately. _(deprecated)_
- [- cancelLocalNotification:](<uiapplication/cancellocalnotification(__).md>) — Cancels the delivery of the specified scheduled local notification. _(deprecated)_
- [- cancelAllLocalNotifications](<uiapplication/cancelalllocalnotifications().md>) — Cancels the delivery of all scheduled local notifications. _(deprecated)_
- [- setKeepAliveTimeout:handler:](<uiapplication/setkeepalivetimeout(__handler_).md>) — Configures a periodic handler for VoIP apps in older versions of iOS. _(deprecated)_
- [UIMinimumKeepAliveTimeout](uiminimumkeepalivetimeout.md) — The minimum amount of time (measured in seconds) an app may run a critical background task in the background. _(deprecated)_
- [- clearKeepAliveTimeout](<uiapplication/clearkeepalivetimeout().md>) — Removes a previously installed periodic handler block. _(deprecated)_
- [- setStatusBarHidden:withAnimation:](<uiapplication/setstatusbarhidden(__with_).md>) — Hides or shows the status bar, optionally animating the transition. _(deprecated)_
- [- setStatusBarStyle:animated:](<uiapplication/setstatusbarstyle(__animated_).md>) — Sets the style of the status bar, optionally animating the transition to the new style. _(deprecated)_
- [- setStatusBarOrientation:animated:](<uiapplication/setstatusbarorientation(__animated_).md>) — Sets the app’s status bar to the specified orientation, optionally animating the transition. _(deprecated)_
- [- registerUserNotificationSettings:](<uiapplication/registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_
- [- registerForRemoteNotificationTypes:](<uiapplication/registerforremotenotifications(matching_).md>) — Register to receive remote notifications of the specified types via Apple Push Notification service. _(deprecated)_
- [- enabledRemoteNotificationTypes](<uiapplication/enabledremotenotificationtypes().md>) — Returns the types of notifications the app accepts. _(deprecated)_
- [UIRemoteNotificationType](uiremotenotificationtype.md) — Constants indicating the types of notifications the app may display to the user. _(deprecated)_
- [- openURL:](<uiapplication/openurl(__).md>) — Attempts to open the resource at the specified URL. _(deprecated)_
- [- setNewsstandIconImage:](<uiapplication/setnewsstandiconimage(__).md>) — Sets the icon of a Newsstand app to an image depicting the current issue of a publication. _(deprecated)_

### Deprecated notifications

- [UIApplicationWillChangeStatusBarFrameNotification](uiapplication/willchangestatusbarframenotification.md) — Posted when the app is about to change the frame of the status bar. _(deprecated)_
- [UIApplicationDidChangeStatusBarFrameNotification](uiapplication/didchangestatusbarframenotification.md) — Posted when the frame of the status bar changes. _(deprecated)_
- [UIApplicationWillChangeStatusBarOrientationNotification](uiapplication/willchangestatusbarorientationnotification.md) — Posted when the app is about to change the orientation of its interface. _(deprecated)_
- [UIApplicationDidChangeStatusBarOrientationNotification](uiapplication/didchangestatusbarorientationnotification.md) — Posted when the orientation of the app’s user interface changes. _(deprecated)_

### Deprecated properties

- [applicationIconBadgeNumber](uiapplication/applicationiconbadgenumber.md) — The number currently set as the badge of the app icon on the Home screen. _(deprecated)_
- [UIApplicationStatusBarFrameUserInfoKey](uiapplication/statusbarframeuserinfokey.md) — A key whose value indicates the new status bar frame. _(deprecated)_
- [UIApplicationStatusBarOrientationUserInfoKey](uiapplication/statusbarorientationuserinfokey.md) — A key whose value indicates the current interface orientation. _(deprecated)_
- [currentUserNotificationSettings](uiapplication/currentusernotificationsettings.md) — Returns the user notification settings for the app. _(deprecated)_
- [ignoringInteractionEvents](uiapplication/isignoringinteractionevents.md) — A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen. _(deprecated)_
- [networkActivityIndicatorVisible](uiapplication/isnetworkactivityindicatorvisible.md) — A Boolean value that turns an indicator of network activity on or off. _(deprecated)_
- [statusBarHidden](uiapplication/isstatusbarhidden.md) — A Boolean value that determines whether the status bar is hidden. _(deprecated)_
- [keyWindow](uiapplication/keywindow.md) — The app’s key window. _(deprecated)_
- [scheduledLocalNotifications](uiapplication/scheduledlocalnotifications.md) — All currently scheduled local notifications. _(deprecated)_
- [statusBarFrame](uiapplication/statusbarframe.md) — The frame rectangle defining the area of the status bar. _(deprecated)_
- [statusBarOrientation](uiapplication/statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_
- [statusBarOrientationAnimationDuration](uiapplication/statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarStyle](uiapplication/statusbarstyle.md) — The current style of the status bar. _(deprecated)_
- [windows](uiapplication/windows.md) — The app’s visible and hidden windows. _(deprecated)_
