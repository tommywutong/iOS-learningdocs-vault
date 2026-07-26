---
title: alertSetting
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings/alertsetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings/alertsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings/alertsetting.json'
content_hash: 'sha256:4dd96fe1a819bf8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSettings](../unnotificationsettings.md)

# alertSetting

<sub>Instance Property</sub>

The authorization status for displaying alerts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var alertSetting: UNNotificationSetting { get }
```

## Discussion

When the value of this property is [UNNotificationSettingEnabled](../unnotificationsetting/enabled.md), the app is authorized to display alerts. Authorization does not guarantee that alerts always appear on the user’s screen. When a device is unlocked, the [alertStyle](alertstyle.md) property determines the presentation style for the alert, which can include not displaying the alert at all.

The system tries to display an alert when the [title](../unnotificationcontent/title.md), [subtitle](../unnotificationcontent/subtitle.md), or [body](../unnotificationcontent/body.md) properties of a [UNNotificationContent](../unnotificationcontent.md) object contain values, or when the `aps` dictionary in a remote notification contains the `alert` key.

## See Also

### Getting Device-Specific Settings

- [notificationCenterSetting](notificationcentersetting.md) — The setting that indicates whether your app’s notifications appear in Notification Center.
- [lockScreenSetting](lockscreensetting.md) — The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [carPlaySetting](carplaysetting.md) — The setting that indicates whether your app’s notifications appear in CarPlay.
- [badgeSetting](badgesetting.md) — The setting that indicates whether badges appear on your app’s icon.
- [soundSetting](soundsetting.md) — The authorization status for playing sounds for incoming notifications.
- [criticalAlertSetting](criticalalertsetting.md) — The authorization status for playing sounds for critical alerts.
- [announcementSetting](announcementsetting.md) — The setting that indicates whether Siri can announce your app’s notifications.
- [scheduledDeliverySetting](scheduleddeliverysetting.md) — The setting that indicates the system schedules the notification.
- [timeSensitiveSetting](timesensitivesetting.md) — The setting that indicates the system treats the notification as time-sensitive.
- [UNNotificationSetting](../unnotificationsetting.md) — Constants that indicate the current status of a notification setting.
