---
title: windows
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/windows
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/windows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/windows.json'
content_hash: 'sha256:e6d107aad5bc23d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# windows

<sub>Instance Property</sub>

The app’s visible and hidden windows.

> [!warning] Deprecated
> Use the [windows](../uiwindowscene/windows.md) property of the relevant window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var windows: [UIWindow] { get }
```

## Discussion

This property contains the [UIWindow](../uiwindow.md) objects currently associated with the app. This list doesn’t include windows created and managed by the system, such as the window used to display the status bar.

The array orders the windows from back to front by window level; thus, the last window in the array is on top of all other app windows.

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
- [scheduledLocalNotifications](scheduledlocalnotifications.md) — All currently scheduled local notifications. _(deprecated)_
- [statusBarFrame](statusbarframe.md) — The frame rectangle defining the area of the status bar. _(deprecated)_
- [statusBarOrientation](statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_
- [statusBarOrientationAnimationDuration](statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarStyle](statusbarstyle.md) — The current style of the status bar. _(deprecated)_
