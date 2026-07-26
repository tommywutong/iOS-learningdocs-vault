---
title: soundName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/soundname
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/soundname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/soundname.json'
content_hash: 'sha256:0ce751d0d7dabff1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# soundName

<sub>Instance Property</sub>

The name of the file containing the sound to play when an alert is displayed.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var soundName: String? { get set }
```

## Discussion

For this property, specify the filename (including extension) of a sound resource in the app’s main bundle or [UILocalNotificationDefaultSoundName](../uilocalnotificationdefaultsoundname.md) to request the default system sound. When the system displays an alert for a local notification or badges an app icon, it plays this sound. The default value is `nil` (no sound). Sounds that last longer than 30 seconds are not supported. If you specify a file with a sound that plays over 30 seconds, the default sound is played instead.

For information on valid sound resources, see [Registering, Scheduling, and Handling User Notifications](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/IPhoneOSClientImp.html#//apple_ref/doc/uid/TP40008194-CH103) in [Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## See Also

### Configuring other parts of the notification

- [applicationIconBadgeNumber](applicationiconbadgenumber.md) — The number to display as the app’s icon badge. _(deprecated)_
- [userInfo](userinfo.md) — A dictionary for passing custom information to the notified app. _(deprecated)_
