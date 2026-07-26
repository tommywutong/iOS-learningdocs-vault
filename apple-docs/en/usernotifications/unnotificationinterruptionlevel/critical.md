---
title: UNNotificationInterruptionLevel.critical
framework: User Notifications
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationinterruptionlevel/critical
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationinterruptionlevel/critical.json'
content_hash: 'sha256:6e1128a923ea9cfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md)

# UNNotificationInterruptionLevel.critical

<sub>Case</sub>

The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case critical
```

## Discussion

This interruption level requires an approved entitlement. The system always presents this notification, even when Do Not Disturb is active. If your app doesn’t assign a sound to this notification, the system uses the default critical alert sound.

## See Also

### Enumeration Cases

- [UNNotificationInterruptionLevelActive](active.md) — The system presents the notification immediately, lights up the screen, and can play a sound.
- [UNNotificationInterruptionLevelPassive](passive.md) — The system adds the notification to the notification list without lighting up the screen or playing a sound.
- [UNNotificationInterruptionLevelTimeSensitive](timesensitive.md) — The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.
