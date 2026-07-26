---
title: UNNotificationInterruptionLevel
framework: User Notifications
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationinterruptionlevel
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationinterruptionlevel.json'
content_hash: 'sha256:e0fd0847e66fe167'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationInterruptionLevel

<sub>Enumeration</sub>

Constants that indicate the importance and delivery timing of a notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UNNotificationInterruptionLevel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UNNotificationInterruptionLevelActive](unnotificationinterruptionlevel/active.md) — The system presents the notification immediately, lights up the screen, and can play a sound.
- [UNNotificationInterruptionLevelCritical](unnotificationinterruptionlevel/critical.md) — The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.
- [UNNotificationInterruptionLevelPassive](unnotificationinterruptionlevel/passive.md) — The system adds the notification to the notification list without lighting up the screen or playing a sound.
- [UNNotificationInterruptionLevelTimeSensitive](unnotificationinterruptionlevel/timesensitive.md) — The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.

### Initializers

- [init(rawValue:)](<unnotificationinterruptionlevel/init(rawvalue_).md>)

## See Also

### Integrating with the system

- [sound](unmutablenotificationcontent/sound.md) — The sound that plays when the system delivers the notification.
- [interruptionLevel](unmutablenotificationcontent/interruptionlevel.md) — The notification’s importance and required delivery timing.
- [relevanceScore](unmutablenotificationcontent/relevancescore.md) — The score the system uses to determine if the notification is the summary’s featured notification.
- [filterCriteria](unmutablenotificationcontent/filtercriteria.md) — The criteria the system evaluates to determine if it displays the notification in the current Focus.
