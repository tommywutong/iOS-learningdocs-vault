---
title: isStatusBarHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/isstatusbarhidden
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/isstatusbarhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/isstatusbarhidden.json'
content_hash: 'sha256:cc96b8bbc83a4b78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# isStatusBarHidden

<sub>Instance Property</sub>

A Boolean value that determines whether the status bar is hidden.

> [!warning] Deprecated
> Use [statusBarManager](../uiwindowscene/statusbarmanager.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isStatusBarHidden: Bool { get set }
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var statusBarHidden: Bool { get set }
```

## Return Value

[true](../../swift/true.md) means the status bar is hidden; [false](../../swift/false.md) means it’s visible.

## Discussion

Changing the value of this property changes the visibility of the status bar immediately—that is, without animations.

## See Also

### Deprecated properties

- [applicationIconBadgeNumber](applicationiconbadgenumber.md) — The number currently set as the badge of the app icon on the Home screen. _(deprecated)_
- [UIApplicationStatusBarFrameUserInfoKey](statusbarframeuserinfokey.md) — A key whose value indicates the new status bar frame. _(deprecated)_
- [UIApplicationStatusBarOrientationUserInfoKey](statusbarorientationuserinfokey.md) — A key whose value indicates the current interface orientation. _(deprecated)_
- [currentUserNotificationSettings](currentusernotificationsettings.md) — Returns the user notification settings for the app. _(deprecated)_
- [ignoringInteractionEvents](isignoringinteractionevents.md) — A Boolean value that indicates whether the receiver is ignoring events initiated by touches on the screen. _(deprecated)_
- [networkActivityIndicatorVisible](isnetworkactivityindicatorvisible.md) — A Boolean value that turns an indicator of network activity on or off. _(deprecated)_
- [keyWindow](keywindow.md) — The app’s key window. _(deprecated)_
- [scheduledLocalNotifications](scheduledlocalnotifications.md) — All currently scheduled local notifications. _(deprecated)_
- [statusBarFrame](statusbarframe.md) — The frame rectangle defining the area of the status bar. _(deprecated)_
- [statusBarOrientation](statusbarorientation.md) — The current orientation of the app’s status bar. _(deprecated)_
- [statusBarOrientationAnimationDuration](statusbarorientationanimationduration.md) — The animation duration in seconds for the status bar during a 90 degree orientation change. _(deprecated)_
- [statusBarStyle](statusbarstyle.md) — The current style of the status bar. _(deprecated)_
- [windows](windows.md) — The app’s visible and hidden windows. _(deprecated)_
