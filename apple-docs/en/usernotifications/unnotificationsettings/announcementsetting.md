---
title: announcementSetting
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/announcementsetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/announcementsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/announcementsetting.json'
content_hash: 'sha256:8a18f8edc787b07e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# announcementSetting

<sub>Instance Property</sub>

The setting that indicates whether Siri can announce your app’s notifications.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var announcementSetting: UNNotificationSetting { get }
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
- [scheduledDeliverySetting](scheduleddeliverysetting.md) — The setting that indicates the system schedules the notification.
- [timeSensitiveSetting](timesensitivesetting.md) — The setting that indicates the system treats the notification as time-sensitive.
- [UNNotificationSetting](../unnotificationsetting.md) — Constants that indicate the current status of a notification setting.
