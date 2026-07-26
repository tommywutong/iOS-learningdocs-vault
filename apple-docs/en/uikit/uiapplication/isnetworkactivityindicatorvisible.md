---
title: isNetworkActivityIndicatorVisible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/isnetworkactivityindicatorvisible
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/isnetworkactivityindicatorvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/isnetworkactivityindicatorvisible.json'
content_hash: 'sha256:76be89f1dc43c6bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# isNetworkActivityIndicatorVisible

<sub>Instance Property</sub>

A Boolean value that turns an indicator of network activity on or off.

> [!warning] Deprecated
> Use [UIRefreshControl](../uirefreshcontrol.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isNetworkActivityIndicatorVisible: Bool { get set }
```

## Discussion

Specify [true](../../swift/true.md) if the app should show network activity and [false](../../swift/false.md) if it should not. The default value is [false](../../swift/false.md). A spinning indicator in the status bar shows network activity. The app may explicitly hide or show this indicator.

## See Also

### Deprecated properties

- [applicationIconBadgeNumber](applicationiconbadgenumber.md) — The number currently set as the badge of the app icon on the Home screen. _(deprecated)_
- [UIApplicationStatusBarFrameUserInfoKey](statusbarframeuserinfokey.md) — A key whose value indicates the new status bar frame. _(deprecated)_
- [UIApplicationStatusBarOrientationUserInfoKey](statusbarorientationuserinfokey.md) — A key whose value indicates the current interface orientation. _(deprecated)_
- [currentUserNotificationSettings](currentusernotificationsettings.md) — Returns the user notification settings for the app. _(deprecated)_
- [ignoringInteractionEvents](isignoringinteractionevents.md) — A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen. _(deprecated)_
- [statusBarHidden](isstatusbarhidden.md) — A Boolean value that determines whether the status bar is hidden. _(deprecated)_
- [keyWindow](keywindow.md) — The app’s key window. _(deprecated)_
- [scheduledLocalNotifications](scheduledlocalnotifications.md) — All currently scheduled local notifications. _(deprecated)_
- [statusBarFrame](statusbarframe.md) — The frame rectangle defining the area of the status bar. _(deprecated)_
- [statusBarOrientation](statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_
- [statusBarOrientationAnimationDuration](statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarStyle](statusbarstyle.md) — The current style of the status bar. _(deprecated)_
- [windows](windows.md) — The app’s visible and hidden windows. _(deprecated)_
