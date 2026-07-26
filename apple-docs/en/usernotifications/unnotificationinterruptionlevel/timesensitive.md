---
title: UNNotificationInterruptionLevel.timeSensitive
framework: User Notifications
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationinterruptionlevel/timesensitive
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive.json'
content_hash: 'sha256:b60b38597ab1f902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md)

# UNNotificationInterruptionLevel.timeSensitive

<sub>Case</sub>

The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case timeSensitive
```

## Discussion

Time Sensitive notifications are similar to active notifications, but can break through system controls such as Notification Summary and Focus. The user can turn off the ability for time sensitive notification interruptions.

## See Also

### Enumeration Cases

- [UNNotificationInterruptionLevelActive](active.md) — The system presents the notification immediately, lights up the screen, and can play a sound.
- [UNNotificationInterruptionLevelCritical](critical.md) — The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.
- [UNNotificationInterruptionLevelPassive](passive.md) — The system adds the notification to the notification list without lighting up the screen or playing a sound.
