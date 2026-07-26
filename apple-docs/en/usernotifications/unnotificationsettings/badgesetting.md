---
title: badgeSetting
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/badgesetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/badgesetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/badgesetting.json'
content_hash: 'sha256:813fea26bc3de8fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# badgeSetting

<sub>Instance Property</sub>

The setting that indicates whether badges appear on your app’s icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var badgeSetting: UNNotificationSetting { get }
```

## Discussion

When the value of this property is [UNNotificationSettingEnabled](../unnotificationsetting/enabled.md), the app is authorized to badge its icon. The system tries to badge your app’s icon when the [badge](../unnotificationcontent/badge.md) property of a [UNNotificationContent](../unnotificationcontent.md) object contain a value, or when the `aps` dictionary in a remote notification contains the `badge` key.

## See Also

### Getting Device-Specific Settings

- [notificationCenterSetting](notificationcentersetting.md) — The setting that indicates whether your app’s notifications appear in Notification Center.
- [lockScreenSetting](lockscreensetting.md) — The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [carPlaySetting](carplaysetting.md) — The setting that indicates whether your app’s notifications appear in CarPlay.
- [alertSetting](alertsetting.md) — The authorization status for displaying alerts.
- [soundSetting](soundsetting.md) — The authorization status for playing sounds for incoming notifications.
- [criticalAlertSetting](criticalalertsetting.md) — The authorization status for playing sounds for critical alerts.
- [announcementSetting](announcementsetting.md) — The setting that indicates whether Siri can announce your app’s notifications.
- [scheduledDeliverySetting](scheduleddeliverysetting.md) — The setting that indicates the system schedules the notification.
- [timeSensitiveSetting](timesensitivesetting.md) — The setting that indicates the system treats the notification as time-sensitive.
- [UNNotificationSetting](../unnotificationsetting.md) — Constants that indicate the current status of a notification setting.
