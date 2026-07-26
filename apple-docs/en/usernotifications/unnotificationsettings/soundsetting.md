---
title: soundSetting
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/soundsetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/soundsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/soundsetting.json'
content_hash: 'sha256:5c09f81c6b2bd666'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# soundSetting

<sub>Instance Property</sub>

The authorization status for playing sounds for incoming notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var soundSetting: UNNotificationSetting { get }
```

## Discussion

When the value of this property is [UNNotificationSettingEnabled](../unnotificationsetting/enabled.md), the system authorizes the app to play sounds. The system tries to play a sound when the [sound](../unnotificationcontent/sound.md) property of the [UNNotificationContent](../unnotificationcontent.md) object contains a value, or when the `aps` dictionary in a remote notification contains the `sound` key.

## See Also

### Getting Device-Specific Settings

- [notificationCenterSetting](notificationcentersetting.md) — The setting that indicates whether your app’s notifications appear in Notification Center.
- [lockScreenSetting](lockscreensetting.md) — The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [carPlaySetting](carplaysetting.md) — The setting that indicates whether your app’s notifications appear in CarPlay.
- [alertSetting](alertsetting.md) — The authorization status for displaying alerts.
- [badgeSetting](badgesetting.md) — The setting that indicates whether badges appear on your app’s icon.
- [criticalAlertSetting](criticalalertsetting.md) — The authorization status for playing sounds for critical alerts.
- [announcementSetting](announcementsetting.md) — The setting that indicates whether Siri can announce your app’s notifications.
- [scheduledDeliverySetting](scheduleddeliverysetting.md) — The setting that indicates the system schedules the notification.
- [timeSensitiveSetting](timesensitivesetting.md) — The setting that indicates the system treats the notification as time-sensitive.
- [UNNotificationSetting](../unnotificationsetting.md) — Constants that indicate the current status of a notification setting.
