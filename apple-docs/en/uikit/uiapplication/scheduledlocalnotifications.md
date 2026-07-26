---
title: scheduledLocalNotifications
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/scheduledlocalnotifications
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/scheduledlocalnotifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/scheduledlocalnotifications.json'
content_hash: 'sha256:624f219426ec81f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# scheduledLocalNotifications

<sub>Instance Property</sub>

All currently scheduled local notifications.

> [!warning] Deprecated
> Use the [UNUserNotificationCenter](../../usernotifications/unusernotificationcenter.md) class to schedule local notifications instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var scheduledLocalNotifications: [UILocalNotification]? { get set }
```

## Discussion

This property holds an array of [UILocalNotification](../uilocalnotification.md) objects representing the current scheduled local notifications. Use this property to access the currently scheduled notifications, perhaps to cancel them. Assigning a new value to this property implicitly schedules all of the notifications in the new array.

This method may be faster than using [- scheduleLocalNotification:](<schedulelocalnotification(__).md>) when scheduling a large number of notifications.

## See Also

### Deprecated properties

- [applicationIconBadgeNumber](applicationiconbadgenumber.md) — The number currently set as the badge of the app icon on the Home screen. _(deprecated)_
- [UIApplicationStatusBarFrameUserInfoKey](statusbarframeuserinfokey.md) — A key whose value indicates the new status bar frame. _(deprecated)_
- [UIApplicationStatusBarOrientationUserInfoKey](statusbarorientationuserinfokey.md) — A key whose value indicates the current interface orientation. _(deprecated)_
- [currentUserNotificationSettings](currentusernotificationsettings.md) — Returns the user notification settings for the app. _(deprecated)_
- [ignoringInteractionEvents](isignoringinteractionevents.md) — A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen. _(deprecated)_
- [networkActivityIndicatorVisible](isnetworkactivityindicatorvisible.md) — A Boolean value that turns an indicator of network activity on or off. _(deprecated)_
- [statusBarHidden](isstatusbarhidden.md) — A Boolean value that determines whether the status bar is hidden. _(deprecated)_
- [keyWindow](keywindow.md) — The app’s key window. _(deprecated)_
- [statusBarFrame](statusbarframe.md) — The frame rectangle defining the area of the status bar. _(deprecated)_
- [statusBarOrientation](statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_
- [statusBarOrientationAnimationDuration](statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarStyle](statusbarstyle.md) — The current style of the status bar. _(deprecated)_
- [windows](windows.md) — The app’s visible and hidden windows. _(deprecated)_
