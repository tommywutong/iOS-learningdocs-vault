---
title: UNNotificationSettings
framework: User Notifications
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsettings
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsettings.json'
content_hash: 'sha256:0aba35c872058dc3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationSettings

<sub>Class</sub>

The object for managing notification-related settings and the authorization status of your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UNNotificationSettings
```

## Overview

A [UNNotificationSettings](unnotificationsettings.md) object contains the current authorization status and notification-related settings for your app. Apps must receive authorization to schedule notifications and to interact with the user. Apps that run in CarPlay must similarly receive authorization to do so. Use this object to determine what notification-related actions your app can perform. You might then use that information to enable, disable, or adjust your app’s notification-related behaviors. Regardless of whether you take action, the system enforces your app’s settings by preventing denied interactions from occurring.

You don’t create instances of this class directly. Instead, call the [- getNotificationSettingsWithCompletionHandler:](<unusernotificationcenter/getnotificationsettings(completionhandler_).md>) method of your app’s [UNUserNotificationCenter](unusernotificationcenter.md) object to get the current settings.

For more information about requesting authorization for user interactions, see [UNUserNotificationCenter](unusernotificationcenter.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting the Authorization Status

- [authorizationStatus](unnotificationsettings/authorizationstatus.md) — The app’s ability to schedule and receive local and remote notifications.
- [UNAuthorizationStatus](unauthorizationstatus.md) — Constants indicating whether the app is allowed to schedule notifications.

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
- [UNNotificationSetting](unnotificationsetting.md) — Constants that indicate the current status of a notification setting.

### Getting Interface Settings

- [alertStyle](unnotificationsettings/alertstyle.md) — The type of alert that the app may display when the device is unlocked.
- [UNAlertStyle](unalertstyle.md) — Constants indicating the presentation styles for alerts.
- [showPreviewsSetting](unnotificationsettings/showpreviewssetting.md) — The setting that indicates whether the app shows a preview of the notification’s content.
- [UNShowPreviewsSetting](unshowpreviewssetting.md) — Constants indicating the style previewing a notification’s content.
- [providesAppNotificationSettings](unnotificationsettings/providesappnotificationsettings.md) — A Boolean value indicating the system displays a button for in-app notification settings.

### Instance Properties

- [directMessagesSetting](unnotificationsettings/directmessagessetting.md)

### Initializers

- [init(coder:)](<unnotificationsettings/init(coder_).md>)

## See Also

### Notification management

- [UNUserNotificationCenter](unusernotificationcenter.md) — The central object for managing notification-related activities for your app or app extension.
- [UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md) — An interface for processing incoming notifications and responding to notification actions.
