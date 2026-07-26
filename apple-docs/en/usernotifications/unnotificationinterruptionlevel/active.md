---
title: UNNotificationInterruptionLevel.active
framework: User Notifications
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationinterruptionlevel/active
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationinterruptionlevel/active.json'
content_hash: 'sha256:f634ff4a6128e403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md)

# UNNotificationInterruptionLevel.active

<sub>Case</sub>

The system presents the notification immediately, lights up the screen, and can play a sound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case active
```

## Discussion

This is the default interruption level. Active notifications won’t break through system notification controls.

## See Also

### Enumeration Cases

- [UNNotificationInterruptionLevelCritical](critical.md) — The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.
- [UNNotificationInterruptionLevelPassive](passive.md) — The system adds the notification to the notification list without lighting up the screen or playing a sound.
- [UNNotificationInterruptionLevelTimeSensitive](timesensitive.md) — The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.
