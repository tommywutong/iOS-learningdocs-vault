---
title: applicationIconBadgeNumber
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（17.0 起废弃）, iPadOS 2.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/applicationiconbadgenumber
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/applicationiconbadgenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/applicationiconbadgenumber.json'
content_hash: 'sha256:b4f462a028674666'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# applicationIconBadgeNumber

<sub>Instance Property</sub>

The number currently set as the badge of the app icon on the Home screen.

> [!warning] Deprecated
> Use [setBadgeCount(_:withCompletionHandler:)](<../../usernotifications/unusernotificationcenter/setbadgecount(__withcompletionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var applicationIconBadgeNumber: Int { get set }
```

## Discussion

Set to 0 (zero) to hide the badge number. The default value of this property is 0.

## See Also

### Deprecated properties

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
- [windows](windows.md) — The app’s visible and hidden windows. _(deprecated)_
