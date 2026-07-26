---
title: relevanceScore
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unmutablenotificationcontent/relevancescore
source_url: 'https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/relevancescore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unmutablenotificationcontent/relevancescore.json'
content_hash: 'sha256:fd4b8dd5b5f7dbae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNMutableNotificationContent](../unmutablenotificationcontent.md)

# relevanceScore

<sub>Instance Property</sub>

The score the system uses to determine if the notification is the summary’s featured notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var relevanceScore: Double { get set }
```

## Discussion

The system uses the `relevanceScore`, a value between `0` and `1`, to sort the notifications from your app. The highest score gets featured in the notification summary.

## See Also

### Integrating with the system

- [sound](sound.md) — The sound that plays when the system delivers the notification.
- [interruptionLevel](interruptionlevel.md) — The notification’s importance and required delivery timing.
- [UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md) — Constants that indicate the importance and delivery timing of a notification.
- [filterCriteria](filtercriteria.md) — The criteria the system evaluates to determine if it displays the notification in the current Focus.
