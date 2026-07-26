---
title: interruptionLevel
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/interruptionlevel
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/interruptionlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/interruptionlevel.json'
content_hash: 'sha256:3c0901d1933ac7f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# interruptionLevel

<sub>Instance Property</sub>

The notification’s importance and required delivery timing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interruptionLevel: UNNotificationInterruptionLevel { get set }
```

## See Also

### Integrating with the system

- [sound](sound.md) — The sound that plays when the system delivers the notification.
- [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md) — Constants that indicate the importance and delivery timing of a notification.
- [relevanceScore](relevancescore.md) — The score the system uses to determine if the notification is the summary’s featured notification.
- [filterCriteria](filtercriteria.md) — The criteria the system evaluates to determine if it displays the notification in the current Focus.
