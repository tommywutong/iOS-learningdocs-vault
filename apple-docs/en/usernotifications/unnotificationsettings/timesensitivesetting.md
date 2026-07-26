---
title: timeSensitiveSetting
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/timesensitivesetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/timesensitivesetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/timesensitivesetting.json'
content_hash: 'sha256:2ec4b8fd80dbac20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# timeSensitiveSetting

<sub>Instance Property</sub>

The setting that indicates the system treats the notification as time-sensitive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var timeSensitiveSetting: UNNotificationSetting { get }
```

## See Also

### Getting Device-Specific Settings

- [notificationCenterSetting](notificationcentersetting.md) — The setting that indicates whether your app’s notifications appear in Notification Center.
- [lockScreenSetting](lockscreensetting.md) — The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [carPlaySetting](carplaysetting.md) — The setting that indicates whether your app’s notifications appear in CarPlay.
- [alertSetting](alertsetting.md) — The authorization status for displaying alerts.
- [badgeSetting](badgesetting.md) — The setting that indicates whether badges appear on your app’s icon.
- [soundSetting](soundsetting.md) — The authorization status for playing sounds for incoming notifications.
- [criticalAlertSetting](criticalalertsetting.md) — The authorization status for playing sounds for critical alerts.
- [announcementSetting](announcementsetting.md) — The setting that indicates whether Siri can announce your app’s notifications.
- [scheduledDeliverySetting](scheduleddeliverysetting.md) — The setting that indicates the system schedules the notification.
- [UNNotificationSetting](../unnotificationsetting.md) — Constants that indicate the current status of a notification setting.
