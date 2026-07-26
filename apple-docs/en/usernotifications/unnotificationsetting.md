---
title: UNNotificationSetting
framework: User Notifications
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsetting
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsetting.json'
content_hash: 'sha256:ce413523f4fc165e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationSetting

<sub>Enumeration</sub>

Constants that indicate the current status of a notification setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UNNotificationSetting
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UNNotificationSettingNotSupported](unnotificationsetting/notsupported.md) — The setting is not available to your app.
- [UNNotificationSettingDisabled](unnotificationsetting/disabled.md) — The setting is disabled.
- [UNNotificationSettingEnabled](unnotificationsetting/enabled.md) — The setting is enabled.

### Initializers

- [init(rawValue:)](<unnotificationsetting/init(rawvalue_).md>)

## See Also

### Getting Device-Specific Settings

- [notificationCenterSetting](unnotificationsettings/notificationcentersetting.md) — The setting that indicates whether your app’s notifications appear in Notification Center.
- [lockScreenSetting](unnotificationsettings/lockscreensetting.md) — The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [carPlaySetting](unnotificationsettings/carplaysetting.md) — The setting that indicates whether your app’s notifications appear in CarPlay.
- [alertSetting](unnotificationsettings/alertsetting.md) — The authorization status for displaying alerts.
- [badgeSetting](unnotificationsettings/badgesetting.md) — The setting that indicates whether badges appear on your app’s icon.
- [soundSetting](unnotificationsettings/soundsetting.md) — The authorization status for playing sounds for incoming notifications.
- [criticalAlertSetting](unnotificationsettings/criticalalertsetting.md) — The authorization status for playing sounds for critical alerts.
- [announcementSetting](unnotificationsettings/announcementsetting.md) — The setting that indicates whether Siri can announce your app’s notifications.
- [scheduledDeliverySetting](unnotificationsettings/scheduleddeliverysetting.md) — The setting that indicates the system schedules the notification.
- [timeSensitiveSetting](unnotificationsettings/timesensitivesetting.md) — The setting that indicates the system treats the notification as time-sensitive.
