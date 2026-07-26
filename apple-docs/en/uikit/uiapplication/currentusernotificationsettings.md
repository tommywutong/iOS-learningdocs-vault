---
title: currentUserNotificationSettings
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/currentusernotificationsettings
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/currentusernotificationsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/currentusernotificationsettings.json'
content_hash: 'sha256:4f450ac588b8d8ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# currentUserNotificationSettings

<sub>Instance Property</sub>

Returns the user notification settings for the app.

> [!warning] Deprecated
> Use [UNUserNotificationCenter](../../usernotifications/unusernotificationcenter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var currentUserNotificationSettings: UIUserNotificationSettings? { get }
```

## Return Value

A user notification settings object indicating the types of notifications that your app may use.

## Discussion

If you configure local or remote notifications with unavailable notification types, the system does not display the corresponding alerts to the user. The system does still deliver the local and remote notifications to your app.

## See Also

### Related Documentation

- [- registerUserNotificationSettings:](<registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_

### Deprecated properties

- [applicationIconBadgeNumber](applicationiconbadgenumber.md) — The number currently set as the badge of the app icon on the Home screen. _(deprecated)_
- [UIApplicationStatusBarFrameUserInfoKey](statusbarframeuserinfokey.md) — A key whose value indicates the new status bar frame. _(deprecated)_
- [UIApplicationStatusBarOrientationUserInfoKey](statusbarorientationuserinfokey.md) — A key whose value indicates the current interface orientation. _(deprecated)_
- [ignoringInteractionEvents](isignoringinteractionevents.md) — A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen. _(deprecated)_
- [networkActivityIndicatorVisible](isnetworkactivityindicatorvisible.md) — A Boolean value that turns an indicator of network activity on or off. _(deprecated)_
- [statusBarHidden](isstatusbarhidden.md) — A Boolean value that determines whether the status bar is hidden. _(deprecated)_
- [keyWindow](keywindow.md) — The app’s key window. _(deprecated)_
- [scheduledLocalNotifications](scheduledlocalnotifications.md) — All currently scheduled local notifications. _(deprecated)_
- [statusBarFrame](statusbarframe.md) — The frame rectangle defining the area of the status bar. _(deprecated)_
- [statusBarOrientation](statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_
- [statusBarOrientationAnimationDuration](statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarStyle](statusbarstyle.md) — The current style of the status bar. _(deprecated)_
- [windows](windows.md) — The app’s visible and hidden windows. _(deprecated)_
